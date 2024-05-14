import spacy
import re

nlp = spacy.load("en_core_web_sm")

# This is used to compute the complexity of the requests and as  example I took programming problems description in
# codewars. We are giving score for different features of the text.
# Some test from the research are actually not
# correct, I guess they updated gpt 3.5 as example Evaluate mathematical expression(from codeWars) solved by GPTv3.5


complex_keywords = [
    'algorithm', 'recursion', 'parallelism', 'optimization',
    'data structure', 'dynamic programming', 'asynchronous', 'threading',
    'compile', 'runtime', 'backtracking', 'graph', 'tree', 'binary search',
    'sort', 'search', 'regex', 'parser', 'combinatorial', 'probability'
]

complex_patterns = [
    r'\brecursion\b', r'\boptimization\b', r'\bgraph\b', r'\bbacktracking\b',
    r'\bdynamic programming\b', r'\basynchronous\b', r'\bdata structure\b',
    r'\bparallelism\b', r'\bthreading\b', r'\bcompile\b', r'\bruntime\b',
    r'\bbinary search\b', r'\bcombinatorial\b'
]


def contains_complex_patterns(prompt):
    for pattern in complex_patterns:
        if re.search(pattern, prompt):
            return True
    return False


def extract_features(prompt):
    doc = nlp(prompt)
    features = {
        'num_verbs': sum(1 for token in doc if token.pos_ == 'VERB'),
        'num_nouns': sum(1 for token in doc if token.pos_ == 'NOUN'),
        'num_adjectives': sum(1 for token in doc if token.pos_ == 'ADJ'),
        'num_adverbs': sum(1 for token in doc if token.pos_ == 'ADV'),
        'num_conjunctions': sum(1 for token in doc if token.pos_ == 'CCONJ' or token.pos_ == 'SCONJ'),
        'num_named_entities': len(list(doc.ents)),
        'sentence_count': len(list(doc.sents)),
        'total_length': len(prompt),
        'average_sentence_length': sum(len(sent) for sent in doc.sents) / len(list(doc.sents)),
        'num_unique_terms': len(set(token.lemma_ for token in doc)),
        'num_subordinate_clauses': sum(1 for token in doc if token.dep_ == 'mark' and token.head.dep_ == 'ccomp'),
        'contains_complex_keywords': any(keyword in prompt for keyword in complex_keywords),
        'contains_complex_patterns': contains_complex_patterns(prompt)
    }
    return features


def assess_complexity(features):
    score = 0
    score += features['num_verbs'] * 0.4
    score += features['num_nouns'] * 0.3
    score += features['contains_complex_keywords'] * 10
    score += features['contains_complex_patterns'] * 10
    score += features['sentence_count'] * 0.2
    score += features['average_sentence_length'] * 0.2
    score += features['total_length'] / 200

    return 'complex' if score > 20 else 'simple'

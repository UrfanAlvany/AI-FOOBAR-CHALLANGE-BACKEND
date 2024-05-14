import logging
from fastapi import APIRouter, HTTPException
from app.models.models import SolveRequest
from app.services.azure_openai import get_response_from_openai
from app.services.complexity_assessment import assess_complexity, extract_features

router = APIRouter()
logger = logging.getLogger("api")


@router.post("/solve")
async def solve_problem(request: SolveRequest):
    try:
        features = extract_features(request.prompt)
        complexity = assess_complexity(features)
        model = "gpt-35-turbo" if complexity == 'simple' else "gpt-4-turbo"
        logger.info(f"Selected model: {model} for prompt: {request.prompt}")

        response = await get_response_from_openai(request.prompt, model)
        response_dict = response.to_dict()
        message_content = response_dict.get('choices', [{}])[0].get('message', {}).get('content', "No content")
        return {"message": message_content, "model_used": model}
    except AttributeError as e:
        logger.error(f"AttributeError: {e}")
        raise HTTPException(status_code=500, detail="Invalid response format from OpenAI API")
    except Exception as e:
        logger.error(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))
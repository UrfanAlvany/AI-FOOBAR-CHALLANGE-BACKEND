## Foobar Challenge AI Solver

## Project Overview
This project is a web application that uses Azure OpenAI to solve programming problems submitted by users. It dynamically selects between different AI models based on the complexity of the problem.

## Technologies Used
- Frontend: Next.js
- Backend: FastAPI, Python
- API: Azure OpenAI

## Installation
Follow these steps to set up the project locally:

1. Clone the repository: 
   ```git clone https://github.com/yourusername/projectname.git ```
2. Navigate to the project directory: ```AiFoobarbackend ```
3. ``` python -m venv venv```
4. ```venv\Scripts\activate```
5. Install dependencies: ```pip install -r requirements.txt```


## Configuration
Set up the required environment variables:

- `AZURE_ENDPOINT`: Endpoint for the Azure OpenAI service.
- `AZURE_API_KEY`: API key for accessing Azure OpenAI.

Create a `.env` file in the root of your project and populate it with your keys:


## Usage
Run the server:
```uvicorn app.main:app --reload```

Access the API at `http://127.0.0.1:8000/docs`

#### Conceptual Overview

The `/solve` endpoint is built on a foundation of adaptive AI utilization, aiming to efficiently solve programming challenges by dynamically selecting the optimal AI model based on the complexity of the problem. This decision-making process is chosen in the principle that not all problems require the same computational resources or AI capabilities.

#### Workflow:

1. **Prompt Reception**: The user submits a problem description through a JSON object. 

2. **Feature Extraction**:
   - The system processes the prompt to extract meaningful features such as the number of specific parts of speech and the presence of complex computational terms. This step is crucial for assessing the intellectual demand of the problem.

3. **Complexity Assessment**:
   - A proprietary algorithm assesses the complexity based on the extracted features. The algorithm considers factors like the length of the input, the complexity of the terms used, and the structure of the sentences to assign a complexity score.

4. **Model Selection**:
   - Depending on the complexity score, the system chooses between two models:
     - **GPT-3.5 Turbo**: Selected for simpler queries where the requirements are straightforward and the computational load is lighter.
     - **GPT-4 Turbo**: Used for more complex queries that demand deeper understanding or extensive content generation.

5. **Solution Generation**:
   - The chosen model processes the problem description, utilizing Azure OpenAI's powerful computational infrastructure to generate a solution.
   - This step involves real-time interaction with Azure's API, where the problem is sent and the solution is fetched asynchronously.


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

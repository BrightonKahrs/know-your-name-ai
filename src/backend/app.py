# Copyright (c) Microsoft. All rights reserved.
import os
from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import logging

from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import DefaultAzureCredential

load_dotenv()

project_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
model_deployment_name = os.getenv("AZURE_AI_MODEL_DEPLOYMENT_NAME")
port = int(os.getenv("PORT", 8000))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("know-your-name-api")


class NameRequest(BaseModel):
    name: str


class NameResponse(BaseModel):
    name: str
    analysis: str


class HealthResponse(BaseModel):
    status: str
    message: str


async def get_name_analysis(query: str) -> str:

    credential = DefaultAzureCredential()

    agent = AzureAIAgentClient(
        project_endpoint=project_endpoint,
        model_deployment_name=model_deployment_name,
        async_credential=credential,
    ).create_agent(
        name="NameAnalyzerAgent",
        instructions="""
                You are an AI agent that helps users learn more about their names.
                You have PhD level knowledge in history and etymology, respond intelligently but approachable to users.
                Based on the input from the user, try to determine a name being give, else ask for a name if one is not provided.

                In a few short paragraphs you should walk the user through the following key points:
                 - Origin of name (including country and any notable stories)
                 - Variations of name
                 - Change in popularity of name over time
                 - Famous people with this name (at least 3). The older and more noteworthy the better
                    - When mentioning someone famous with this name - you must mention their birth year and if they are still alive or not
            """,
    )

    result = await agent.run(query)

    return result.text


app = FastAPI()


@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint that returns API status"""
    return HealthResponse(status="healthy", message="Know Your Name AI API is running")


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(status="healthy", message="API is operational")


@app.post("/api/nameanalysis/analyze", response_model=NameResponse)
async def analyze_name(request: NameRequest):
    """Analyze a name and return insights about its origin, meaning, and famous people"""

    if not request.name or not request.name.strip():
        raise HTTPException(
            status_code=400, detail="Name is required and cannot be empty"
        )

    try:
        user_input = request.name.strip()
        result = await get_name_analysis(user_input)

        return NameResponse(name=user_input, analysis=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=port)

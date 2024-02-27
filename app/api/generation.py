from typing import List, Any
from fastapi import Header, APIRouter
from app.api.models import Prompt, Response
from app.api.get_response import get_resp, load_model


generator = APIRouter()
pipeline = load_model()


@generator.post("/get_response", response_model=Response)
async def get_response_from_query(payload: Prompt):
    """Orchestrator that calls

    Args:
        payload (Document): document to generate queries for

    Returns:
        Queries: Query: List[str]
    """
    return get_resp(pipeline, payload)
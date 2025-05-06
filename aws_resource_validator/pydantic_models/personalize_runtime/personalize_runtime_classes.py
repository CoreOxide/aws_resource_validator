from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.personalize_runtime.personalize_runtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class GetActionRecommendationsRequest(BaseValidatorModel):
    campaignArn: Optional[str] = None
    userId: Optional[str] = None
    numResults: Optional[int] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Dict[str, str]] = None


class PredictedAction(BaseValidatorModel):
    actionId: Optional[str] = None
    score: Optional[float] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetPersonalizedRankingRequest(BaseValidatorModel):
    campaignArn: str
    inputList: List[str]
    userId: str
    context: Optional[Dict[str, str]] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Dict[str, str]] = None
    metadataColumns: Optional[Dict[str, List[str]]] = None


class PredictedItem(BaseValidatorModel):
    itemId: Optional[str] = None
    score: Optional[float] = None
    promotionName: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    reason: Optional[List[str]] = None


class Promotion(BaseValidatorModel):
    name: Optional[str] = None
    percentPromotedItems: Optional[int] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Dict[str, str]] = None


class GetActionRecommendationsResponse(BaseValidatorModel):
    actionList: List[PredictedAction]
    recommendationId: str
    ResponseMetadata: ResponseMetadata


class GetPersonalizedRankingResponse(BaseValidatorModel):
    personalizedRanking: List[PredictedItem]
    recommendationId: str
    ResponseMetadata: ResponseMetadata


class GetRecommendationsResponse(BaseValidatorModel):
    itemList: List[PredictedItem]
    recommendationId: str
    ResponseMetadata: ResponseMetadata


class GetRecommendationsRequest(BaseValidatorModel):
    campaignArn: Optional[str] = None
    itemId: Optional[str] = None
    userId: Optional[str] = None
    numResults: Optional[int] = None
    context: Optional[Dict[str, str]] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Dict[str, str]] = None
    recommenderArn: Optional[str] = None
    promotions: Optional[List[Promotion]] = None
    metadataColumns: Optional[Dict[str, List[str]]] = None
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.personalize_runtime_constants import *

class GetActionRecommendationsRequest(BaseValidatorModel):
    campaignArn: Optional[str] = None
    userId: Optional[str] = None
    numResults: Optional[int] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None


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
    inputList: Sequence[str]
    userId: str
    context: Optional[Mapping[str, str]] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None
    metadataColumns: Optional[Mapping[str, Sequence[str]]] = None


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
    filterValues: Optional[Mapping[str, str]] = None


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
    context: Optional[Mapping[str, str]] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None
    recommenderArn: Optional[str] = None
    promotions: Optional[Sequence[Promotion]] = None
    metadataColumns: Optional[Mapping[str, Sequence[str]]] = None



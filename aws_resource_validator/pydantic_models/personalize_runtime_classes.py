from datetime import datetime
from pydantic import BaseModel
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

class GetActionRecommendationsRequestRequestTypeDef(BaseModel):
    campaignArn: Optional[str] = None
    userId: Optional[str] = None
    numResults: Optional[int] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None

class PredictedActionTypeDef(BaseModel):
    actionId: Optional[str] = None
    score: Optional[float] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GetPersonalizedRankingRequestRequestTypeDef(BaseModel):
    campaignArn: str
    inputList: Sequence[str]
    userId: str
    context: Optional[Mapping[str, str]] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None
    metadataColumns: Optional[Mapping[str, Sequence[str]]] = None

class PredictedItemTypeDef(BaseModel):
    itemId: Optional[str] = None
    score: Optional[float] = None
    promotionName: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    reason: Optional[List[str]] = None

class PromotionTypeDef(BaseModel):
    name: Optional[str] = None
    percentPromotedItems: Optional[int] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None

class GetActionRecommendationsResponseTypeDef(BaseModel):
    actionList: List[PredictedActionTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPersonalizedRankingResponseTypeDef(BaseModel):
    personalizedRanking: List[PredictedItemTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsResponseTypeDef(BaseModel):
    itemList: List[PredictedItemTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsRequestRequestTypeDef(BaseModel):
    campaignArn: Optional[str] = None
    itemId: Optional[str] = None
    userId: Optional[str] = None
    numResults: Optional[int] = None
    context: Optional[Mapping[str, str]] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None
    recommenderArn: Optional[str] = None
    promotions: Optional[Sequence[PromotionTypeDef]] = None
    metadataColumns: Optional[Mapping[str, Sequence[str]]] = None


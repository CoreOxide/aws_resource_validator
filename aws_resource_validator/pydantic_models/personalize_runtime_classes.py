from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class GetActionRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    campaignArn: Optional[str] = None
    userId: Optional[str] = None
    numResults: Optional[int] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None

class PredictedActionTypeDef(BaseValidatorModel):
    actionId: Optional[str] = None
    score: Optional[float] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GetPersonalizedRankingRequestRequestTypeDef(BaseValidatorModel):
    campaignArn: str
    inputList: Sequence[str]
    userId: str
    context: Optional[Mapping[str, str]] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None
    metadataColumns: Optional[Mapping[str, Sequence[str]]] = None

class PredictedItemTypeDef(BaseValidatorModel):
    itemId: Optional[str] = None
    score: Optional[float] = None
    promotionName: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    reason: Optional[List[str]] = None

class PromotionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    percentPromotedItems: Optional[int] = None
    filterArn: Optional[str] = None
    filterValues: Optional[Mapping[str, str]] = None

class GetActionRecommendationsResponseTypeDef(BaseValidatorModel):
    actionList: List[PredictedActionTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPersonalizedRankingResponseTypeDef(BaseValidatorModel):
    personalizedRanking: List[PredictedItemTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsResponseTypeDef(BaseValidatorModel):
    itemList: List[PredictedItemTypeDef]
    recommendationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsRequestRequestTypeDef(BaseValidatorModel):
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


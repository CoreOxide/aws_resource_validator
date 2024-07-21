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
from aws_resource_validator.pydantic_models.kendra_ranking_constants import *

class CapacityUnitsConfigurationTypeDef(BaseModel):
    RescoreCapacityUnits: int

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteRescoreExecutionPlanRequestRequestTypeDef(BaseModel):
    Id: str

class DescribeRescoreExecutionPlanRequestRequestTypeDef(BaseModel):
    Id: str

class DocumentTypeDef(BaseModel):
    Id: str
    OriginalScore: float
    GroupId: Optional[str] = None
    Title: Optional[str] = None
    Body: Optional[str] = None
    TokenizedTitle: Optional[Sequence[str]] = None
    TokenizedBody: Optional[Sequence[str]] = None

class ListRescoreExecutionPlansRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RescoreExecutionPlanSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    Id: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    Status: Optional[RescoreExecutionPlanStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class RescoreResultItemTypeDef(BaseModel):
    DocumentId: Optional[str] = None
    Score: Optional[float] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateRescoreExecutionPlanRequestRequestTypeDef(BaseModel):
    Id: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfigurationTypeDef] = None

class CreateRescoreExecutionPlanRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    CapacityUnits: Optional[CapacityUnitsConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateRescoreExecutionPlanResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRescoreExecutionPlanResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    Name: str
    Description: str
    CapacityUnits: CapacityUnitsConfigurationTypeDef
    CreatedAt: datetime
    UpdatedAt: datetime
    Status: RescoreExecutionPlanStatusType
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RescoreRequestRequestTypeDef(BaseModel):
    RescoreExecutionPlanId: str
    SearchQuery: str
    Documents: Sequence[DocumentTypeDef]

class ListRescoreExecutionPlansResponseTypeDef(BaseModel):
    SummaryItems: List[RescoreExecutionPlanSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RescoreResultTypeDef(BaseModel):
    RescoreId: str
    ResultItems: List[RescoreResultItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


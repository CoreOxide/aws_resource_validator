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
from aws_resource_validator.pydantic_models.rbin_constants import *

class ResourceTagTypeDef(BaseModel):
    ResourceTagKey: str
    ResourceTagValue: Optional[str] = None

class RetentionPeriodTypeDef(BaseModel):
    RetentionPeriodValue: int
    RetentionPeriodUnit: Literal["DAYS"]

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteRuleRequestRequestTypeDef(BaseModel):
    Identifier: str

class GetRuleRequestRequestTypeDef(BaseModel):
    Identifier: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class UnlockDelayTypeDef(BaseModel):
    UnlockDelayValue: int
    UnlockDelayUnit: Literal["DAYS"]

class UnlockRuleRequestRequestTypeDef(BaseModel):
    Identifier: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class ListRulesRequestRequestTypeDef(BaseModel):
    ResourceType: ResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockState: Optional[LockStateType] = None

class RuleSummaryTypeDef(BaseModel):
    Identifier: Optional[str] = None
    Description: Optional[str] = None
    RetentionPeriod: Optional[RetentionPeriodTypeDef] = None
    LockState: Optional[LockStateType] = None
    RuleArn: Optional[str] = None

class UpdateRuleRequestRequestTypeDef(BaseModel):
    Identifier: str
    RetentionPeriod: Optional[RetentionPeriodTypeDef] = None
    Description: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleResponseTypeDef(BaseModel):
    Identifier: str
    RetentionPeriod: RetentionPeriodTypeDef
    Description: str
    ResourceType: ResourceTypeType
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesRequestListRulesPaginateTypeDef(BaseModel):
    ResourceType: ResourceTypeType
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockState: Optional[LockStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LockConfigurationTypeDef(BaseModel):
    UnlockDelay: UnlockDelayTypeDef

class ListRulesResponseTypeDef(BaseModel):
    Rules: List[RuleSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleRequestRequestTypeDef(BaseModel):
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceType: ResourceTypeType
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockConfiguration: Optional[LockConfigurationTypeDef] = None

class CreateRuleResponseTypeDef(BaseModel):
    Identifier: str
    RetentionPeriod: RetentionPeriodTypeDef
    Description: str
    Tags: List[TagTypeDef]
    ResourceType: ResourceTypeType
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockConfiguration: LockConfigurationTypeDef
    LockState: LockStateType
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleResponseTypeDef(BaseModel):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockConfiguration: LockConfigurationTypeDef
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class LockRuleRequestRequestTypeDef(BaseModel):
    Identifier: str
    LockConfiguration: LockConfigurationTypeDef

class LockRuleResponseTypeDef(BaseModel):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockConfiguration: LockConfigurationTypeDef
    LockState: LockStateType
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UnlockRuleResponseTypeDef(BaseModel):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceTags: List[ResourceTagTypeDef]
    Status: RuleStatusType
    LockConfiguration: LockConfigurationTypeDef
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.rbin_constants import *

class ResourceTagTypeDef(BaseValidatorModel):
    ResourceTagKey: str
    ResourceTagValue: Optional[str] = None

class RetentionPeriodTypeDef(BaseValidatorModel):
    RetentionPeriodValue: int
    RetentionPeriodUnit: Literal["DAYS"]

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteRuleRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetRuleRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class UnlockDelayTypeDef(BaseValidatorModel):
    UnlockDelayValue: int
    UnlockDelayUnit: Literal["DAYS"]

class UnlockRuleRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class ListRulesRequestRequestTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockState: Optional[LockStateType] = None

class RuleSummaryTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    Description: Optional[str] = None
    RetentionPeriod: Optional[RetentionPeriodTypeDef] = None
    LockState: Optional[LockStateType] = None
    RuleArn: Optional[str] = None

class UpdateRuleRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    RetentionPeriod: Optional[RetentionPeriodTypeDef] = None
    Description: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRuleResponseTypeDef(BaseValidatorModel):
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

class ListRulesRequestListRulesPaginateTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeType
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockState: Optional[LockStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LockConfigurationTypeDef(BaseValidatorModel):
    UnlockDelay: UnlockDelayTypeDef

class ListRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[RuleSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleRequestRequestTypeDef(BaseValidatorModel):
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceType: ResourceTypeType
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockConfiguration: Optional[LockConfigurationTypeDef] = None

class CreateRuleResponseTypeDef(BaseValidatorModel):
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

class GetRuleResponseTypeDef(BaseValidatorModel):
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

class LockRuleRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    LockConfiguration: LockConfigurationTypeDef

class LockRuleResponseTypeDef(BaseValidatorModel):
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

class UnlockRuleResponseTypeDef(BaseValidatorModel):
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


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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteRuleRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetRuleRequestTypeDef(BaseValidatorModel):
    Identifier: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class UnlockDelayTypeDef(BaseValidatorModel):
    UnlockDelayValue: int
    UnlockDelayUnit: Literal["DAYS"]


class UnlockRuleRequestTypeDef(BaseValidatorModel):
    Identifier: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class ListRulesRequestTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockState: Optional[LockStateType] = None
    ExcludeResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class RuleSummaryTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    Description: Optional[str] = None
    RetentionPeriod: Optional[RetentionPeriodTypeDef] = None
    LockState: Optional[LockStateType] = None
    RuleArn: Optional[str] = None


class UpdateRuleRequestTypeDef(BaseValidatorModel):
    Identifier: str
    RetentionPeriod: Optional[RetentionPeriodTypeDef] = None
    Description: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    ExcludeResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
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
    ExcludeResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListRulesRequestPaginateTypeDef(BaseValidatorModel):
    ResourceType: ResourceTypeType
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockState: Optional[LockStateType] = None
    ExcludeResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class LockConfigurationTypeDef(BaseValidatorModel):
    UnlockDelay: UnlockDelayTypeDef


class ListRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateRuleRequestTypeDef(BaseValidatorModel):
    RetentionPeriod: RetentionPeriodTypeDef
    ResourceType: ResourceTypeType
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None
    LockConfiguration: Optional[LockConfigurationTypeDef] = None
    ExcludeResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


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
    ExcludeResourceTags: List[ResourceTagTypeDef]
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
    ExcludeResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LockRuleRequestTypeDef(BaseValidatorModel):
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
    ExcludeResourceTags: List[ResourceTagTypeDef]
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
    ExcludeResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef



from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.rbin.rbin_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResourceTag(BaseValidatorModel):
    ResourceTagKey: str
    ResourceTagValue: Optional[str] = None


class RetentionPeriod(BaseValidatorModel):
    RetentionPeriodValue: int
    RetentionPeriodUnit: Literal['DAYS']


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteRuleRequest(BaseValidatorModel):
    Identifier: str


class GetRuleRequest(BaseValidatorModel):
    Identifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class UnlockDelay(BaseValidatorModel):
    UnlockDelayValue: int
    UnlockDelayUnit: Literal['DAYS']


class UnlockRuleRequest(BaseValidatorModel):
    Identifier: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class ListRulesRequest(BaseValidatorModel):
    ResourceType: ResourceTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ResourceTags: Optional[List[ResourceTag]] = None
    LockState: Optional[LockStateType] = None
    ExcludeResourceTags: Optional[List[ResourceTag]] = None


class RuleSummary(BaseValidatorModel):
    Identifier: Optional[str] = None
    Description: Optional[str] = None
    RetentionPeriod: Optional[RetentionPeriod] = None
    LockState: Optional[LockStateType] = None
    RuleArn: Optional[str] = None


class UpdateRuleRequest(BaseValidatorModel):
    Identifier: str
    RetentionPeriod: Optional[RetentionPeriod] = None
    Description: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    ResourceTags: Optional[List[ResourceTag]] = None
    ExcludeResourceTags: Optional[List[ResourceTag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateRuleResponse(BaseValidatorModel):
    Identifier: str
    RetentionPeriod: RetentionPeriod
    Description: str
    ResourceType: ResourceTypeType
    ResourceTags: List[ResourceTag]
    Status: RuleStatusType
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ExcludeResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


class ListRulesRequestPaginate(BaseValidatorModel):
    ResourceType: ResourceTypeType
    ResourceTags: Optional[List[ResourceTag]] = None
    LockState: Optional[LockStateType] = None
    ExcludeResourceTags: Optional[List[ResourceTag]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class LockConfiguration(BaseValidatorModel):
    UnlockDelay: UnlockDelay


class ListRulesResponse(BaseValidatorModel):
    Rules: List[RuleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateRuleRequest(BaseValidatorModel):
    RetentionPeriod: RetentionPeriod
    ResourceType: ResourceTypeType
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ResourceTags: Optional[List[ResourceTag]] = None
    LockConfiguration: Optional[LockConfiguration] = None
    ExcludeResourceTags: Optional[List[ResourceTag]] = None


class CreateRuleResponse(BaseValidatorModel):
    Identifier: str
    RetentionPeriod: RetentionPeriod
    Description: str
    Tags: List[Tag]
    ResourceType: ResourceTypeType
    ResourceTags: List[ResourceTag]
    Status: RuleStatusType
    LockConfiguration: LockConfiguration
    LockState: LockStateType
    RuleArn: str
    ExcludeResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


class GetRuleResponse(BaseValidatorModel):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriod
    ResourceTags: List[ResourceTag]
    Status: RuleStatusType
    LockConfiguration: LockConfiguration
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ExcludeResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


class LockRuleRequest(BaseValidatorModel):
    Identifier: str
    LockConfiguration: LockConfiguration


class LockRuleResponse(BaseValidatorModel):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriod
    ResourceTags: List[ResourceTag]
    Status: RuleStatusType
    LockConfiguration: LockConfiguration
    LockState: LockStateType
    RuleArn: str
    ExcludeResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


class UnlockRuleResponse(BaseValidatorModel):
    Identifier: str
    Description: str
    ResourceType: ResourceTypeType
    RetentionPeriod: RetentionPeriod
    ResourceTags: List[ResourceTag]
    Status: RuleStatusType
    LockConfiguration: LockConfiguration
    LockState: LockStateType
    LockEndTime: datetime
    RuleArn: str
    ExcludeResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata
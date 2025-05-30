from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.dlm.dlm_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class RetentionArchiveTier(BaseValidatorModel):
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


class CrossRegionCopyTarget(BaseValidatorModel):
    TargetRegion: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ScriptOutput(BaseValidatorModel):
    ExecutionHandler: str
    Stages: Optional[List[StageValuesType]] = None
    ExecutionHandlerService: Optional[Literal['AWS_SYSTEMS_MANAGER']] = None
    ExecuteOperationOnScriptFailure: Optional[bool] = None
    ExecutionTimeout: Optional[int] = None
    MaximumRetryCount: Optional[int] = None


class Script(BaseValidatorModel):
    ExecutionHandler: str
    Stages: Optional[List[StageValuesType]] = None
    ExecutionHandlerService: Optional[Literal['AWS_SYSTEMS_MANAGER']] = None
    ExecuteOperationOnScriptFailure: Optional[bool] = None
    ExecutionTimeout: Optional[int] = None
    MaximumRetryCount: Optional[int] = None


class CrossRegionCopyRetainRule(BaseValidatorModel):
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


class EncryptionConfiguration(BaseValidatorModel):
    Encrypted: bool
    CmkArn: Optional[str] = None


class CrossRegionCopyDeprecateRule(BaseValidatorModel):
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


class DeleteLifecyclePolicyRequest(BaseValidatorModel):
    PolicyId: str


class DeprecateRule(BaseValidatorModel):
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


class EventParametersOutput(BaseValidatorModel):
    EventType: Literal['shareSnapshot']
    SnapshotOwner: List[str]
    DescriptionRegex: str


class EventParameters(BaseValidatorModel):
    EventType: Literal['shareSnapshot']
    SnapshotOwner: List[str]
    DescriptionRegex: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class FastRestoreRuleOutput(BaseValidatorModel):
    AvailabilityZones: List[str]
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


class FastRestoreRule(BaseValidatorModel):
    AvailabilityZones: List[str]
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


# This class is the input for the 'get_lifecycle_policies' function.
class GetLifecyclePoliciesRequest(BaseValidatorModel):
    PolicyIds: Optional[List[str]] = None
    State: Optional[GettablePolicyStateValuesType] = None
    ResourceTypes: Optional[List[ResourceTypeValuesType]] = None
    TargetTags: Optional[List[str]] = None
    TagsToAdd: Optional[List[str]] = None
    DefaultPolicyType: Optional[DefaultPoliciesTypeValuesType] = None


class LifecyclePolicySummary(BaseValidatorModel):
    PolicyId: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[GettablePolicyStateValuesType] = None
    Tags: Optional[Dict[str, str]] = None
    PolicyType: Optional[PolicyTypeValuesType] = None
    DefaultPolicy: Optional[bool] = None


# This class is the input for the 'get_lifecycle_policy' function.
class GetLifecyclePolicyRequest(BaseValidatorModel):
    PolicyId: str


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class RetainRule(BaseValidatorModel):
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


class ShareRuleOutput(BaseValidatorModel):
    TargetAccounts: List[str]
    UnshareInterval: Optional[int] = None
    UnshareIntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


class ShareRule(BaseValidatorModel):
    TargetAccounts: List[str]
    UnshareInterval: Optional[int] = None
    UnshareIntervalUnit: Optional[RetentionIntervalUnitValuesType] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class ArchiveRetainRule(BaseValidatorModel):
    RetentionArchiveTier: RetentionArchiveTier


# This class is the output for the 'create_lifecycle_policy' function.
class CreateLifecyclePolicyResponse(BaseValidatorModel):
    PolicyId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateRuleOutput(BaseValidatorModel):
    Location: Optional[LocationValuesType] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[Literal['HOURS']] = None
    Times: Optional[List[str]] = None
    CronExpression: Optional[str] = None
    Scripts: Optional[List[ScriptOutput]] = None


class CreateRule(BaseValidatorModel):
    Location: Optional[LocationValuesType] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[Literal['HOURS']] = None
    Times: Optional[List[str]] = None
    CronExpression: Optional[str] = None
    Scripts: Optional[List[Script]] = None


class CrossRegionCopyAction(BaseValidatorModel):
    Target: str
    EncryptionConfiguration: EncryptionConfiguration
    RetainRule: Optional[CrossRegionCopyRetainRule] = None


class CrossRegionCopyRule(BaseValidatorModel):
    Encrypted: bool
    TargetRegion: Optional[str] = None
    Target: Optional[str] = None
    CmkArn: Optional[str] = None
    CopyTags: Optional[bool] = None
    RetainRule: Optional[CrossRegionCopyRetainRule] = None
    DeprecateRule: Optional[CrossRegionCopyDeprecateRule] = None


class EventSourceOutput(BaseValidatorModel):
    Type: Literal['MANAGED_CWE']
    Parameters: Optional[EventParametersOutput] = None


class EventSource(BaseValidatorModel):
    Type: Literal['MANAGED_CWE']
    Parameters: Optional[EventParameters] = None


class ExclusionsOutput(BaseValidatorModel):
    ExcludeBootVolumes: Optional[bool] = None
    ExcludeVolumeTypes: Optional[List[str]] = None
    ExcludeTags: Optional[List[Tag]] = None


class Exclusions(BaseValidatorModel):
    ExcludeBootVolumes: Optional[bool] = None
    ExcludeVolumeTypes: Optional[List[str]] = None
    ExcludeTags: Optional[List[Tag]] = None


class ParametersOutput(BaseValidatorModel):
    ExcludeBootVolume: Optional[bool] = None
    NoReboot: Optional[bool] = None
    ExcludeDataVolumeTags: Optional[List[Tag]] = None


class Parameters(BaseValidatorModel):
    ExcludeBootVolume: Optional[bool] = None
    NoReboot: Optional[bool] = None
    ExcludeDataVolumeTags: Optional[List[Tag]] = None


# This class is the output for the 'get_lifecycle_policies' function.
class GetLifecyclePoliciesResponse(BaseValidatorModel):
    Policies: List[LifecyclePolicySummary]
    ResponseMetadata: ResponseMetadata


class ArchiveRule(BaseValidatorModel):
    RetainRule: ArchiveRetainRule


class ActionOutput(BaseValidatorModel):
    Name: str
    CrossRegionCopy: List[CrossRegionCopyAction]


class Action(BaseValidatorModel):
    Name: str
    CrossRegionCopy: List[CrossRegionCopyAction]

ExclusionsUnion = Union[Exclusions, ExclusionsOutput]


class ScheduleOutput(BaseValidatorModel):
    Name: Optional[str] = None
    CopyTags: Optional[bool] = None
    TagsToAdd: Optional[List[Tag]] = None
    VariableTags: Optional[List[Tag]] = None
    CreateRule: Optional[CreateRuleOutput] = None
    RetainRule: Optional[RetainRule] = None
    FastRestoreRule: Optional[FastRestoreRuleOutput] = None
    CrossRegionCopyRules: Optional[List[CrossRegionCopyRule]] = None
    ShareRules: Optional[List[ShareRuleOutput]] = None
    DeprecateRule: Optional[DeprecateRule] = None
    ArchiveRule: Optional[ArchiveRule] = None


class Schedule(BaseValidatorModel):
    Name: Optional[str] = None
    CopyTags: Optional[bool] = None
    TagsToAdd: Optional[List[Tag]] = None
    VariableTags: Optional[List[Tag]] = None
    CreateRule: Optional[CreateRule] = None
    RetainRule: Optional[RetainRule] = None
    FastRestoreRule: Optional[FastRestoreRule] = None
    CrossRegionCopyRules: Optional[List[CrossRegionCopyRule]] = None
    ShareRules: Optional[List[ShareRule]] = None
    DeprecateRule: Optional[DeprecateRule] = None
    ArchiveRule: Optional[ArchiveRule] = None


class PolicyDetailsOutput(BaseValidatorModel):
    PolicyType: Optional[PolicyTypeValuesType] = None
    ResourceTypes: Optional[List[ResourceTypeValuesType]] = None
    ResourceLocations: Optional[List[ResourceLocationValuesType]] = None
    TargetTags: Optional[List[Tag]] = None
    Schedules: Optional[List[ScheduleOutput]] = None
    Parameters: Optional[ParametersOutput] = None
    EventSource: Optional[EventSourceOutput] = None
    Actions: Optional[List[ActionOutput]] = None
    PolicyLanguage: Optional[PolicyLanguageValuesType] = None
    ResourceType: Optional[ResourceTypeValuesType] = None
    CreateInterval: Optional[int] = None
    RetainInterval: Optional[int] = None
    CopyTags: Optional[bool] = None
    CrossRegionCopyTargets: Optional[List[CrossRegionCopyTarget]] = None
    ExtendDeletion: Optional[bool] = None
    Exclusions: Optional[ExclusionsOutput] = None


class PolicyDetails(BaseValidatorModel):
    PolicyType: Optional[PolicyTypeValuesType] = None
    ResourceTypes: Optional[List[ResourceTypeValuesType]] = None
    ResourceLocations: Optional[List[ResourceLocationValuesType]] = None
    TargetTags: Optional[List[Tag]] = None
    Schedules: Optional[List[Schedule]] = None
    Parameters: Optional[Parameters] = None
    EventSource: Optional[EventSource] = None
    Actions: Optional[List[Action]] = None
    PolicyLanguage: Optional[PolicyLanguageValuesType] = None
    ResourceType: Optional[ResourceTypeValuesType] = None
    CreateInterval: Optional[int] = None
    RetainInterval: Optional[int] = None
    CopyTags: Optional[bool] = None
    CrossRegionCopyTargets: Optional[List[CrossRegionCopyTarget]] = None
    ExtendDeletion: Optional[bool] = None
    Exclusions: Optional[Exclusions] = None


class LifecyclePolicy(BaseValidatorModel):
    PolicyId: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[GettablePolicyStateValuesType] = None
    StatusMessage: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None
    PolicyDetails: Optional[PolicyDetailsOutput] = None
    Tags: Optional[Dict[str, str]] = None
    PolicyArn: Optional[str] = None
    DefaultPolicy: Optional[bool] = None

PolicyDetailsUnion = Union[PolicyDetails, PolicyDetailsOutput]


# This class is the output for the 'get_lifecycle_policy' function.
class GetLifecyclePolicyResponse(BaseValidatorModel):
    Policy: LifecyclePolicy
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_lifecycle_policy' function.
class CreateLifecyclePolicyRequest(BaseValidatorModel):
    ExecutionRoleArn: str
    Description: str
    State: SettablePolicyStateValuesType
    PolicyDetails: Optional[PolicyDetailsUnion] = None
    Tags: Optional[Dict[str, str]] = None
    DefaultPolicy: Optional[DefaultPolicyTypeValuesType] = None
    CreateInterval: Optional[int] = None
    RetainInterval: Optional[int] = None
    CopyTags: Optional[bool] = None
    ExtendDeletion: Optional[bool] = None
    CrossRegionCopyTargets: Optional[List[CrossRegionCopyTarget]] = None
    Exclusions: Optional[ExclusionsUnion] = None


class UpdateLifecyclePolicyRequest(BaseValidatorModel):
    PolicyId: str
    ExecutionRoleArn: Optional[str] = None
    State: Optional[SettablePolicyStateValuesType] = None
    Description: Optional[str] = None
    PolicyDetails: Optional[PolicyDetailsUnion] = None
    CreateInterval: Optional[int] = None
    RetainInterval: Optional[int] = None
    CopyTags: Optional[bool] = None
    ExtendDeletion: Optional[bool] = None
    CrossRegionCopyTargets: Optional[List[CrossRegionCopyTarget]] = None
    Exclusions: Optional[ExclusionsUnion] = None
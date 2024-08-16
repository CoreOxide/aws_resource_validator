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
from aws_resource_validator.pydantic_models.dlm_constants import *

class RetentionArchiveTierTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None

class CrossRegionCopyTargetTypeDef(BaseValidatorModel):
    TargetRegion: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ScriptTypeDef(BaseValidatorModel):
    ExecutionHandler: str
    Stages: Optional[Sequence[StageValuesType]] = None
    ExecutionHandlerService: Optional[Literal["AWS_SYSTEMS_MANAGER"]] = None
    ExecuteOperationOnScriptFailure: Optional[bool] = None
    ExecutionTimeout: Optional[int] = None
    MaximumRetryCount: Optional[int] = None

class CrossRegionCopyRetainRuleTypeDef(BaseValidatorModel):
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    Encrypted: bool
    CmkArn: Optional[str] = None

class CrossRegionCopyDeprecateRuleTypeDef(BaseValidatorModel):
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None

class DeleteLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyId: str

class DeprecateRuleTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None

class EventParametersTypeDef(BaseValidatorModel):
    EventType: Literal["shareSnapshot"]
    SnapshotOwner: Sequence[str]
    DescriptionRegex: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class FastRestoreRuleTypeDef(BaseValidatorModel):
    AvailabilityZones: Sequence[str]
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None

class GetLifecyclePoliciesRequestRequestTypeDef(BaseValidatorModel):
    PolicyIds: Optional[Sequence[str]] = None
    State: Optional[GettablePolicyStateValuesType] = None
    ResourceTypes: Optional[Sequence[ResourceTypeValuesType]] = None
    TargetTags: Optional[Sequence[str]] = None
    TagsToAdd: Optional[Sequence[str]] = None
    DefaultPolicyType: Optional[DefaultPoliciesTypeValuesType] = None

class LifecyclePolicySummaryTypeDef(BaseValidatorModel):
    PolicyId: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[GettablePolicyStateValuesType] = None
    Tags: Optional[Dict[str, str]] = None
    PolicyType: Optional[PolicyTypeValuesType] = None
    DefaultPolicy: Optional[bool] = None

class GetLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyId: str

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class RetainRuleTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[RetentionIntervalUnitValuesType] = None

class ShareRuleTypeDef(BaseValidatorModel):
    TargetAccounts: Sequence[str]
    UnshareInterval: Optional[int] = None
    UnshareIntervalUnit: Optional[RetentionIntervalUnitValuesType] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class ArchiveRetainRuleTypeDef(BaseValidatorModel):
    RetentionArchiveTier: RetentionArchiveTierTypeDef

class CreateLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    PolicyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleTypeDef(BaseValidatorModel):
    Location: Optional[LocationValuesType] = None
    Interval: Optional[int] = None
    IntervalUnit: Optional[Literal["HOURS"]] = None
    Times: Optional[Sequence[str]] = None
    CronExpression: Optional[str] = None
    Scripts: Optional[Sequence[ScriptTypeDef]] = None

class CrossRegionCopyActionTypeDef(BaseValidatorModel):
    Target: str
    EncryptionConfiguration: EncryptionConfigurationTypeDef
    RetainRule: Optional[CrossRegionCopyRetainRuleTypeDef] = None

class CrossRegionCopyRuleTypeDef(BaseValidatorModel):
    Encrypted: bool
    TargetRegion: Optional[str] = None
    Target: Optional[str] = None
    CmkArn: Optional[str] = None
    CopyTags: Optional[bool] = None
    RetainRule: Optional[CrossRegionCopyRetainRuleTypeDef] = None
    DeprecateRule: Optional[CrossRegionCopyDeprecateRuleTypeDef] = None

class EventSourceTypeDef(BaseValidatorModel):
    Type: Literal["MANAGED_CWE"]
    Parameters: Optional[EventParametersTypeDef] = None

class ExclusionsTypeDef(BaseValidatorModel):
    ExcludeBootVolumes: Optional[bool] = None
    ExcludeVolumeTypes: Optional[Sequence[str]] = None
    ExcludeTags: Optional[Sequence[TagTypeDef]] = None

class ParametersTypeDef(BaseValidatorModel):
    ExcludeBootVolume: Optional[bool] = None
    NoReboot: Optional[bool] = None
    ExcludeDataVolumeTags: Optional[Sequence[TagTypeDef]] = None

class GetLifecyclePoliciesResponseTypeDef(BaseValidatorModel):
    Policies: List[LifecyclePolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ArchiveRuleTypeDef(BaseValidatorModel):
    RetainRule: ArchiveRetainRuleTypeDef

class ActionTypeDef(BaseValidatorModel):
    Name: str
    CrossRegionCopy: Sequence[CrossRegionCopyActionTypeDef]

class ScheduleTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    CopyTags: Optional[bool] = None
    TagsToAdd: Optional[Sequence[TagTypeDef]] = None
    VariableTags: Optional[Sequence[TagTypeDef]] = None
    CreateRule: Optional[CreateRuleTypeDef] = None
    RetainRule: Optional[RetainRuleTypeDef] = None
    FastRestoreRule: Optional[FastRestoreRuleTypeDef] = None
    CrossRegionCopyRules: Optional[Sequence[CrossRegionCopyRuleTypeDef]] = None
    ShareRules: Optional[Sequence[ShareRuleTypeDef]] = None
    DeprecateRule: Optional[DeprecateRuleTypeDef] = None
    ArchiveRule: Optional[ArchiveRuleTypeDef] = None

class PolicyDetailsTypeDef(BaseValidatorModel):
    PolicyType: Optional[PolicyTypeValuesType] = None
    ResourceTypes: Optional[Sequence[ResourceTypeValuesType]] = None
    ResourceLocations: Optional[Sequence[ResourceLocationValuesType]] = None
    TargetTags: Optional[Sequence[TagTypeDef]] = None
    Schedules: Optional[Sequence[ScheduleTypeDef]] = None
    Parameters: Optional[ParametersTypeDef] = None
    EventSource: Optional[EventSourceTypeDef] = None
    Actions: Optional[Sequence[ActionTypeDef]] = None
    PolicyLanguage: Optional[PolicyLanguageValuesType] = None
    ResourceType: Optional[ResourceTypeValuesType] = None
    CreateInterval: Optional[int] = None
    RetainInterval: Optional[int] = None
    CopyTags: Optional[bool] = None
    CrossRegionCopyTargets: Optional[Sequence[CrossRegionCopyTargetTypeDef]] = None
    ExtendDeletion: Optional[bool] = None
    Exclusions: Optional[ExclusionsTypeDef] = None

class CreateLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    ExecutionRoleArn: str
    Description: str
    State: SettablePolicyStateValuesType
    PolicyDetails: Optional[PolicyDetailsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    DefaultPolicy: Optional[DefaultPolicyTypeValuesType] = None
    CreateInterval: Optional[int] = None
    RetainInterval: Optional[int] = None
    CopyTags: Optional[bool] = None
    ExtendDeletion: Optional[bool] = None
    CrossRegionCopyTargets: Optional[Sequence[CrossRegionCopyTargetTypeDef]] = None
    Exclusions: Optional[ExclusionsTypeDef] = None

class LifecyclePolicyTypeDef(BaseValidatorModel):
    PolicyId: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[GettablePolicyStateValuesType] = None
    StatusMessage: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    DateCreated: Optional[datetime] = None
    DateModified: Optional[datetime] = None
    PolicyDetails: Optional[PolicyDetailsTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    PolicyArn: Optional[str] = None
    DefaultPolicy: Optional[bool] = None

class UpdateLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyId: str
    ExecutionRoleArn: Optional[str] = None
    State: Optional[SettablePolicyStateValuesType] = None
    Description: Optional[str] = None
    PolicyDetails: Optional[PolicyDetailsTypeDef] = None
    CreateInterval: Optional[int] = None
    RetainInterval: Optional[int] = None
    CopyTags: Optional[bool] = None
    ExtendDeletion: Optional[bool] = None
    CrossRegionCopyTargets: Optional[Sequence[CrossRegionCopyTargetTypeDef]] = None
    Exclusions: Optional[ExclusionsTypeDef] = None

class GetLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    Policy: LifecyclePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


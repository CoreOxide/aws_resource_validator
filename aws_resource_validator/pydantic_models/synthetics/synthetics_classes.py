from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.synthetics.synthetics_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class S3EncryptionConfig(BaseValidatorModel):
    EncryptionMode: Optional[EncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class AssociateResourceRequest(BaseValidatorModel):
    GroupIdentifier: str
    ResourceArn: str


class BaseScreenshotOutput(BaseValidatorModel):
    ScreenshotName: str
    IgnoreCoordinates: Optional[List[str]] = None


class BaseScreenshot(BaseValidatorModel):
    ScreenshotName: str
    IgnoreCoordinates: Optional[List[str]] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CanaryCodeOutput(BaseValidatorModel):
    SourceLocationArn: Optional[str] = None
    Handler: Optional[str] = None


class CanaryRunConfigInput(BaseValidatorModel):
    TimeoutInSeconds: Optional[int] = None
    MemoryInMB: Optional[int] = None
    ActiveTracing: Optional[bool] = None
    EnvironmentVariables: Optional[Dict[str, str]] = None


class CanaryRunConfigOutput(BaseValidatorModel):
    TimeoutInSeconds: Optional[int] = None
    MemoryInMB: Optional[int] = None
    ActiveTracing: Optional[bool] = None


class CanaryRunStatus(BaseValidatorModel):
    State: Optional[CanaryRunStateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[CanaryRunStateReasonCodeType] = None


class CanaryRunTimeline(BaseValidatorModel):
    Started: Optional[datetime] = None
    Completed: Optional[datetime] = None


class CanaryScheduleInput(BaseValidatorModel):
    Expression: str
    DurationInSeconds: Optional[int] = None


class CanaryScheduleOutput(BaseValidatorModel):
    Expression: Optional[str] = None
    DurationInSeconds: Optional[int] = None


class CanaryStatus(BaseValidatorModel):
    State: Optional[CanaryStateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[CanaryStateReasonCodeType] = None


class CanaryTimeline(BaseValidatorModel):
    Created: Optional[datetime] = None
    LastModified: Optional[datetime] = None
    LastStarted: Optional[datetime] = None
    LastStopped: Optional[datetime] = None


class VpcConfigOutput(BaseValidatorModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    Ipv6AllowedForDualStack: Optional[bool] = None


class VpcConfigInput(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    Ipv6AllowedForDualStack: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateGroupRequest(BaseValidatorModel):
    Name: str
    Tags: Optional[Dict[str, str]] = None


class Group(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class DeleteCanaryRequest(BaseValidatorModel):
    Name: str
    DeleteLambda: Optional[bool] = None


class DeleteGroupRequest(BaseValidatorModel):
    GroupIdentifier: str


class DescribeCanariesLastRunRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Names: Optional[List[str]] = None


class DescribeCanariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Names: Optional[List[str]] = None


class DescribeRuntimeVersionsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RuntimeVersion(BaseValidatorModel):
    VersionName: Optional[str] = None
    Description: Optional[str] = None
    ReleaseDate: Optional[datetime] = None
    DeprecationDate: Optional[datetime] = None


class DisassociateResourceRequest(BaseValidatorModel):
    GroupIdentifier: str
    ResourceArn: str


class GetCanaryRequest(BaseValidatorModel):
    Name: str


class GetCanaryRunsRequest(BaseValidatorModel):
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetGroupRequest(BaseValidatorModel):
    GroupIdentifier: str


class GroupSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None


class ListAssociatedGroupsRequest(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListGroupResourcesRequest(BaseValidatorModel):
    GroupIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListGroupsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class StartCanaryRequest(BaseValidatorModel):
    Name: str


class StopCanaryRequest(BaseValidatorModel):
    Name: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class ArtifactConfigInput(BaseValidatorModel):
    S3Encryption: Optional[S3EncryptionConfig] = None


class ArtifactConfigOutput(BaseValidatorModel):
    S3Encryption: Optional[S3EncryptionConfig] = None


class VisualReferenceOutput(BaseValidatorModel):
    BaseScreenshots: Optional[List[BaseScreenshotOutput]] = None
    BaseCanaryRunId: Optional[str] = None

BaseScreenshotUnion = Union[BaseScreenshot, BaseScreenshotOutput]


class CanaryCodeInput(BaseValidatorModel):
    Handler: str
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3Version: Optional[str] = None
    ZipFile: Optional[Blob] = None


class CanaryRun(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[CanaryRunStatus] = None
    Timeline: Optional[CanaryRunTimeline] = None
    ArtifactS3Location: Optional[str] = None


class ListGroupResourcesResponse(BaseValidatorModel):
    Resources: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateGroupResponse(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


class GetGroupResponse(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


class DescribeRuntimeVersionsResponse(BaseValidatorModel):
    RuntimeVersions: List[RuntimeVersion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAssociatedGroupsResponse(BaseValidatorModel):
    Groups: List[GroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupsResponse(BaseValidatorModel):
    Groups: List[GroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Canary(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Code: Optional[CanaryCodeOutput] = None
    ExecutionRoleArn: Optional[str] = None
    Schedule: Optional[CanaryScheduleOutput] = None
    RunConfig: Optional[CanaryRunConfigOutput] = None
    SuccessRetentionPeriodInDays: Optional[int] = None
    FailureRetentionPeriodInDays: Optional[int] = None
    Status: Optional[CanaryStatus] = None
    Timeline: Optional[CanaryTimeline] = None
    ArtifactS3Location: Optional[str] = None
    EngineArn: Optional[str] = None
    RuntimeVersion: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    VisualReference: Optional[VisualReferenceOutput] = None
    ProvisionedResourceCleanup: Optional[ProvisionedResourceCleanupSettingType] = None
    Tags: Optional[Dict[str, str]] = None
    ArtifactConfig: Optional[ArtifactConfigOutput] = None


class VisualReferenceInput(BaseValidatorModel):
    BaseCanaryRunId: str
    BaseScreenshots: Optional[List[BaseScreenshotUnion]] = None


class CreateCanaryRequest(BaseValidatorModel):
    Name: str
    Code: CanaryCodeInput
    ArtifactS3Location: str
    ExecutionRoleArn: str
    Schedule: CanaryScheduleInput
    RuntimeVersion: str
    RunConfig: Optional[CanaryRunConfigInput] = None
    SuccessRetentionPeriodInDays: Optional[int] = None
    FailureRetentionPeriodInDays: Optional[int] = None
    VpcConfig: Optional[VpcConfigInput] = None
    ResourcesToReplicateTags: Optional[List[Literal['lambda-function']]] = None
    ProvisionedResourceCleanup: Optional[ProvisionedResourceCleanupSettingType] = None
    Tags: Optional[Dict[str, str]] = None
    ArtifactConfig: Optional[ArtifactConfigInput] = None


class CanaryLastRun(BaseValidatorModel):
    CanaryName: Optional[str] = None
    LastRun: Optional[CanaryRun] = None


class GetCanaryRunsResponse(BaseValidatorModel):
    CanaryRuns: List[CanaryRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateCanaryResponse(BaseValidatorModel):
    Canary: Canary
    ResponseMetadata: ResponseMetadata


class DescribeCanariesResponse(BaseValidatorModel):
    Canaries: List[Canary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCanaryResponse(BaseValidatorModel):
    Canary: Canary
    ResponseMetadata: ResponseMetadata


class UpdateCanaryRequest(BaseValidatorModel):
    Name: str
    Code: Optional[CanaryCodeInput] = None
    ExecutionRoleArn: Optional[str] = None
    RuntimeVersion: Optional[str] = None
    Schedule: Optional[CanaryScheduleInput] = None
    RunConfig: Optional[CanaryRunConfigInput] = None
    SuccessRetentionPeriodInDays: Optional[int] = None
    FailureRetentionPeriodInDays: Optional[int] = None
    VpcConfig: Optional[VpcConfigInput] = None
    VisualReference: Optional[VisualReferenceInput] = None
    ArtifactS3Location: Optional[str] = None
    ArtifactConfig: Optional[ArtifactConfigInput] = None
    ProvisionedResourceCleanup: Optional[ProvisionedResourceCleanupSettingType] = None


class DescribeCanariesLastRunResponse(BaseValidatorModel):
    CanariesLastRun: List[CanaryLastRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
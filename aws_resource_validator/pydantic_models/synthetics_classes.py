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
from aws_resource_validator.pydantic_models.synthetics_constants import *

class S3EncryptionConfigTypeDef(BaseValidatorModel):
    EncryptionMode: Optional[EncryptionModeType] = None
    KmsKeyArn: Optional[str] = None

class AssociateResourceRequestRequestTypeDef(BaseValidatorModel):
    GroupIdentifier: str
    ResourceArn: str

class BaseScreenshotTypeDef(BaseValidatorModel):
    ScreenshotName: str
    IgnoreCoordinates: Optional[List[str]] = None

class CanaryCodeOutputTypeDef(BaseValidatorModel):
    SourceLocationArn: Optional[str] = None
    Handler: Optional[str] = None

class CanaryRunConfigInputTypeDef(BaseValidatorModel):
    TimeoutInSeconds: Optional[int] = None
    MemoryInMB: Optional[int] = None
    ActiveTracing: Optional[bool] = None
    EnvironmentVariables: Optional[Mapping[str, str]] = None

class CanaryRunConfigOutputTypeDef(BaseValidatorModel):
    TimeoutInSeconds: Optional[int] = None
    MemoryInMB: Optional[int] = None
    ActiveTracing: Optional[bool] = None

class CanaryRunStatusTypeDef(BaseValidatorModel):
    State: Optional[CanaryRunStateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[CanaryRunStateReasonCodeType] = None

class CanaryRunTimelineTypeDef(BaseValidatorModel):
    Started: Optional[datetime] = None
    Completed: Optional[datetime] = None

class CanaryScheduleInputTypeDef(BaseValidatorModel):
    Expression: str
    DurationInSeconds: Optional[int] = None

class CanaryScheduleOutputTypeDef(BaseValidatorModel):
    Expression: Optional[str] = None
    DurationInSeconds: Optional[int] = None

class CanaryStatusTypeDef(BaseValidatorModel):
    State: Optional[CanaryStateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[CanaryStateReasonCodeType] = None

class CanaryTimelineTypeDef(BaseValidatorModel):
    Created: Optional[datetime] = None
    LastModified: Optional[datetime] = None
    LastStarted: Optional[datetime] = None
    LastStopped: Optional[datetime] = None

class VpcConfigOutputTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class VpcConfigInputTypeDef(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Tags: Optional[Mapping[str, str]] = None

class GroupTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class DeleteCanaryRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    DeleteLambda: Optional[bool] = None

class DeleteGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupIdentifier: str

class DescribeCanariesLastRunRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Names: Optional[Sequence[str]] = None

class DescribeCanariesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Names: Optional[Sequence[str]] = None

class DescribeRuntimeVersionsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RuntimeVersionTypeDef(BaseValidatorModel):
    VersionName: Optional[str] = None
    Description: Optional[str] = None
    ReleaseDate: Optional[datetime] = None
    DeprecationDate: Optional[datetime] = None

class DisassociateResourceRequestRequestTypeDef(BaseValidatorModel):
    GroupIdentifier: str
    ResourceArn: str

class GetCanaryRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class GetCanaryRunsRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupIdentifier: str

class GroupSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None

class ListAssociatedGroupsRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupResourcesRequestRequestTypeDef(BaseValidatorModel):
    GroupIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class StartCanaryRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StopCanaryRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class ArtifactConfigInputTypeDef(BaseValidatorModel):
    S3Encryption: Optional[S3EncryptionConfigTypeDef] = None

class ArtifactConfigOutputTypeDef(BaseValidatorModel):
    S3Encryption: Optional[S3EncryptionConfigTypeDef] = None

class VisualReferenceInputTypeDef(BaseValidatorModel):
    BaseCanaryRunId: str
    BaseScreenshots: Optional[Sequence[BaseScreenshotTypeDef]] = None

class VisualReferenceOutputTypeDef(BaseValidatorModel):
    BaseScreenshots: Optional[List[BaseScreenshotTypeDef]] = None
    BaseCanaryRunId: Optional[str] = None

class CanaryCodeInputTypeDef(BaseValidatorModel):
    Handler: str
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3Version: Optional[str] = None
    ZipFile: Optional[BlobTypeDef] = None

class CanaryRunTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[CanaryRunStatusTypeDef] = None
    Timeline: Optional[CanaryRunTimelineTypeDef] = None
    ArtifactS3Location: Optional[str] = None

class ListGroupResourcesResponseTypeDef(BaseValidatorModel):
    Resources: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRuntimeVersionsResponseTypeDef(BaseValidatorModel):
    RuntimeVersions: List[RuntimeVersionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CanaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Code: Optional[CanaryCodeOutputTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    Schedule: Optional[CanaryScheduleOutputTypeDef] = None
    RunConfig: Optional[CanaryRunConfigOutputTypeDef] = None
    SuccessRetentionPeriodInDays: Optional[int] = None
    FailureRetentionPeriodInDays: Optional[int] = None
    Status: Optional[CanaryStatusTypeDef] = None
    Timeline: Optional[CanaryTimelineTypeDef] = None
    ArtifactS3Location: Optional[str] = None
    EngineArn: Optional[str] = None
    RuntimeVersion: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutputTypeDef] = None
    VisualReference: Optional[VisualReferenceOutputTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    ArtifactConfig: Optional[ArtifactConfigOutputTypeDef] = None

class CreateCanaryRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Code: CanaryCodeInputTypeDef
    ArtifactS3Location: str
    ExecutionRoleArn: str
    Schedule: CanaryScheduleInputTypeDef
    RuntimeVersion: str
    RunConfig: Optional[CanaryRunConfigInputTypeDef] = None
    SuccessRetentionPeriodInDays: Optional[int] = None
    FailureRetentionPeriodInDays: Optional[int] = None
    VpcConfig: Optional[VpcConfigInputTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    ArtifactConfig: Optional[ArtifactConfigInputTypeDef] = None

class UpdateCanaryRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Code: Optional[CanaryCodeInputTypeDef] = None
    ExecutionRoleArn: Optional[str] = None
    RuntimeVersion: Optional[str] = None
    Schedule: Optional[CanaryScheduleInputTypeDef] = None
    RunConfig: Optional[CanaryRunConfigInputTypeDef] = None
    SuccessRetentionPeriodInDays: Optional[int] = None
    FailureRetentionPeriodInDays: Optional[int] = None
    VpcConfig: Optional[VpcConfigInputTypeDef] = None
    VisualReference: Optional[VisualReferenceInputTypeDef] = None
    ArtifactS3Location: Optional[str] = None
    ArtifactConfig: Optional[ArtifactConfigInputTypeDef] = None

class CanaryLastRunTypeDef(BaseValidatorModel):
    CanaryName: Optional[str] = None
    LastRun: Optional[CanaryRunTypeDef] = None

class GetCanaryRunsResponseTypeDef(BaseValidatorModel):
    CanaryRuns: List[CanaryRunTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCanaryResponseTypeDef(BaseValidatorModel):
    Canary: CanaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCanariesResponseTypeDef(BaseValidatorModel):
    Canaries: List[CanaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCanaryResponseTypeDef(BaseValidatorModel):
    Canary: CanaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCanariesLastRunResponseTypeDef(BaseValidatorModel):
    CanariesLastRun: List[CanaryLastRunTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


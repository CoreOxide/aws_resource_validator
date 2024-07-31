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
from aws_resource_validator.pydantic_models.synthetics_constants import *

class S3EncryptionConfigTypeDef(BaseModel):
    EncryptionMode: Optional[EncryptionModeType] = None
    KmsKeyArn: Optional[str] = None

class AssociateResourceRequestRequestTypeDef(BaseModel):
    GroupIdentifier: str
    ResourceArn: str

class BaseScreenshotTypeDef(BaseModel):
    ScreenshotName: str
    IgnoreCoordinates: Optional[List[str]] = None

class CanaryCodeOutputTypeDef(BaseModel):
    SourceLocationArn: Optional[str] = None
    Handler: Optional[str] = None

class CanaryRunConfigInputTypeDef(BaseModel):
    TimeoutInSeconds: Optional[int] = None
    MemoryInMB: Optional[int] = None
    ActiveTracing: Optional[bool] = None
    EnvironmentVariables: Optional[Mapping[str, str]] = None

class CanaryRunConfigOutputTypeDef(BaseModel):
    TimeoutInSeconds: Optional[int] = None
    MemoryInMB: Optional[int] = None
    ActiveTracing: Optional[bool] = None

class CanaryRunStatusTypeDef(BaseModel):
    State: Optional[CanaryRunStateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[CanaryRunStateReasonCodeType] = None

class CanaryRunTimelineTypeDef(BaseModel):
    Started: Optional[datetime] = None
    Completed: Optional[datetime] = None

class CanaryScheduleInputTypeDef(BaseModel):
    Expression: str
    DurationInSeconds: Optional[int] = None

class CanaryScheduleOutputTypeDef(BaseModel):
    Expression: Optional[str] = None
    DurationInSeconds: Optional[int] = None

class CanaryStatusTypeDef(BaseModel):
    State: Optional[CanaryStateType] = None
    StateReason: Optional[str] = None
    StateReasonCode: Optional[CanaryStateReasonCodeType] = None

class CanaryTimelineTypeDef(BaseModel):
    Created: Optional[datetime] = None
    LastModified: Optional[datetime] = None
    LastStarted: Optional[datetime] = None
    LastStopped: Optional[datetime] = None

class VpcConfigOutputTypeDef(BaseModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class VpcConfigInputTypeDef(BaseModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateGroupRequestRequestTypeDef(BaseModel):
    Name: str
    Tags: Optional[Mapping[str, str]] = None

class GroupTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class DeleteCanaryRequestRequestTypeDef(BaseModel):
    Name: str
    DeleteLambda: Optional[bool] = None

class DeleteGroupRequestRequestTypeDef(BaseModel):
    GroupIdentifier: str

class DescribeCanariesLastRunRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Names: Optional[Sequence[str]] = None

class DescribeCanariesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Names: Optional[Sequence[str]] = None

class DescribeRuntimeVersionsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RuntimeVersionTypeDef(BaseModel):
    VersionName: Optional[str] = None
    Description: Optional[str] = None
    ReleaseDate: Optional[datetime] = None
    DeprecationDate: Optional[datetime] = None

class DisassociateResourceRequestRequestTypeDef(BaseModel):
    GroupIdentifier: str
    ResourceArn: str

class GetCanaryRequestRequestTypeDef(BaseModel):
    Name: str

class GetCanaryRunsRequestRequestTypeDef(BaseModel):
    Name: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetGroupRequestRequestTypeDef(BaseModel):
    GroupIdentifier: str

class GroupSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None

class ListAssociatedGroupsRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupResourcesRequestRequestTypeDef(BaseModel):
    GroupIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListGroupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class StartCanaryRequestRequestTypeDef(BaseModel):
    Name: str

class StopCanaryRequestRequestTypeDef(BaseModel):
    Name: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class ArtifactConfigInputTypeDef(BaseModel):
    S3Encryption: Optional[S3EncryptionConfigTypeDef] = None

class ArtifactConfigOutputTypeDef(BaseModel):
    S3Encryption: Optional[S3EncryptionConfigTypeDef] = None

class VisualReferenceInputTypeDef(BaseModel):
    BaseCanaryRunId: str
    BaseScreenshots: Optional[Sequence[BaseScreenshotTypeDef]] = None

class VisualReferenceOutputTypeDef(BaseModel):
    BaseScreenshots: Optional[List[BaseScreenshotTypeDef]] = None
    BaseCanaryRunId: Optional[str] = None

class CanaryCodeInputTypeDef(BaseModel):
    Handler: str
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3Version: Optional[str] = None
    ZipFile: Optional[BlobTypeDef] = None

class CanaryRunTypeDef(BaseModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[CanaryRunStatusTypeDef] = None
    Timeline: Optional[CanaryRunTimelineTypeDef] = None
    ArtifactS3Location: Optional[str] = None

class ListGroupResourcesResponseTypeDef(BaseModel):
    Resources: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupResponseTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRuntimeVersionsResponseTypeDef(BaseModel):
    RuntimeVersions: List[RuntimeVersionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedGroupsResponseTypeDef(BaseModel):
    Groups: List[GroupSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsResponseTypeDef(BaseModel):
    Groups: List[GroupSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CanaryTypeDef(BaseModel):
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

class CreateCanaryRequestRequestTypeDef(BaseModel):
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

class UpdateCanaryRequestRequestTypeDef(BaseModel):
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

class CanaryLastRunTypeDef(BaseModel):
    CanaryName: Optional[str] = None
    LastRun: Optional[CanaryRunTypeDef] = None

class GetCanaryRunsResponseTypeDef(BaseModel):
    CanaryRuns: List[CanaryRunTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCanaryResponseTypeDef(BaseModel):
    Canary: CanaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCanariesResponseTypeDef(BaseModel):
    Canaries: List[CanaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCanaryResponseTypeDef(BaseModel):
    Canary: CanaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCanariesLastRunResponseTypeDef(BaseModel):
    CanariesLastRun: List[CanaryLastRunTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.osis_constants import *

class BufferOptions(BaseValidatorModel):
    PersistentBufferEnabled: bool


class ChangeProgressStage(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[ChangeProgressStageStatusesType] = None
    Description: Optional[str] = None
    LastUpdatedAt: Optional[datetime] = None


class CloudWatchLogDestination(BaseValidatorModel):
    LogGroup: str


class EncryptionAtRestOptions(BaseValidatorModel):
    KmsKeyArn: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeletePipelineRequest(BaseValidatorModel):
    PipelineName: str


class GetPipelineBlueprintRequest(BaseValidatorModel):
    BlueprintName: str
    Format: Optional[str] = None


class PipelineBlueprint(BaseValidatorModel):
    BlueprintName: Optional[str] = None
    PipelineConfigurationBody: Optional[str] = None
    DisplayName: Optional[str] = None
    DisplayDescription: Optional[str] = None
    Service: Optional[str] = None
    UseCase: Optional[str] = None


class GetPipelineChangeProgressRequest(BaseValidatorModel):
    PipelineName: str


class GetPipelineRequest(BaseValidatorModel):
    PipelineName: str


class PipelineBlueprintSummary(BaseValidatorModel):
    BlueprintName: Optional[str] = None
    DisplayName: Optional[str] = None
    DisplayDescription: Optional[str] = None
    Service: Optional[str] = None
    UseCase: Optional[str] = None


class ListPipelinesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    Arn: str


class PipelineStatusReason(BaseValidatorModel):
    Description: Optional[str] = None


class StartPipelineRequest(BaseValidatorModel):
    PipelineName: str


class StopPipelineRequest(BaseValidatorModel):
    PipelineName: str


class UntagResourceRequest(BaseValidatorModel):
    Arn: str
    TagKeys: Sequence[str]


class ValidatePipelineRequest(BaseValidatorModel):
    PipelineConfigurationBody: str


class ValidationMessage(BaseValidatorModel):
    Message: Optional[str] = None


class VpcAttachmentOptions(BaseValidatorModel):
    AttachToVpc: bool
    CidrBlock: Optional[str] = None


class ChangeProgressStatus(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    Status: Optional[ChangeProgressStatusesType] = None
    TotalNumberOfStages: Optional[int] = None
    ChangeProgressStages: Optional[List[ChangeProgressStage]] = None


class LogPublishingOptions(BaseValidatorModel):
    IsLoggingEnabled: Optional[bool] = None
    CloudWatchLogDestination: Optional[CloudWatchLogDestination] = None


class TagResourceRequest(BaseValidatorModel):
    Arn: str
    Tags: Sequence[Tag]


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class GetPipelineBlueprintResponse(BaseValidatorModel):
    Blueprint: PipelineBlueprint
    Format: str
    ResponseMetadata: ResponseMetadata


class ListPipelineBlueprintsResponse(BaseValidatorModel):
    Blueprints: List[PipelineBlueprintSummary]
    ResponseMetadata: ResponseMetadata


class PipelineDestination(BaseValidatorModel):
    pass


class PipelineSummary(BaseValidatorModel):
    Status: Optional[PipelineStatusType] = None
    StatusReason: Optional[PipelineStatusReason] = None
    PipelineName: Optional[str] = None
    PipelineArn: Optional[str] = None
    MinUnits: Optional[int] = None
    MaxUnits: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Destinations: Optional[List[PipelineDestination]] = None
    Tags: Optional[List[Tag]] = None


class ValidatePipelineResponse(BaseValidatorModel):
    isValid: bool
    Errors: List[ValidationMessage]
    ResponseMetadata: ResponseMetadata


class VpcOptionsOutput(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None
    VpcAttachmentOptions: Optional[VpcAttachmentOptions] = None
    VpcEndpointManagement: Optional[VpcEndpointManagementType] = None


class VpcOptions(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None
    VpcAttachmentOptions: Optional[VpcAttachmentOptions] = None
    VpcEndpointManagement: Optional[VpcEndpointManagementType] = None


class GetPipelineChangeProgressResponse(BaseValidatorModel):
    ChangeProgressStatuses: List[ChangeProgressStatus]
    ResponseMetadata: ResponseMetadata


class UpdatePipelineRequest(BaseValidatorModel):
    PipelineName: str
    MinUnits: Optional[int] = None
    MaxUnits: Optional[int] = None
    PipelineConfigurationBody: Optional[str] = None
    LogPublishingOptions: Optional[LogPublishingOptions] = None
    BufferOptions: Optional[BufferOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None


class ListPipelinesResponse(BaseValidatorModel):
    Pipelines: List[PipelineSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class VpcEndpoint(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcOptions: Optional[VpcOptionsOutput] = None


class ServiceVpcEndpoint(BaseValidatorModel):
    pass


class Pipeline(BaseValidatorModel):
    PipelineName: Optional[str] = None
    PipelineArn: Optional[str] = None
    MinUnits: Optional[int] = None
    MaxUnits: Optional[int] = None
    Status: Optional[PipelineStatusType] = None
    StatusReason: Optional[PipelineStatusReason] = None
    PipelineConfigurationBody: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    IngestEndpointUrls: Optional[List[str]] = None
    LogPublishingOptions: Optional[LogPublishingOptions] = None
    VpcEndpoints: Optional[List[VpcEndpoint]] = None
    BufferOptions: Optional[BufferOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    VpcEndpointService: Optional[str] = None
    ServiceVpcEndpoints: Optional[List[ServiceVpcEndpoint]] = None
    Destinations: Optional[List[PipelineDestination]] = None
    Tags: Optional[List[Tag]] = None


class VpcOptionsUnion(BaseValidatorModel):
    pass


class CreatePipelineRequest(BaseValidatorModel):
    PipelineName: str
    MinUnits: int
    MaxUnits: int
    PipelineConfigurationBody: str
    LogPublishingOptions: Optional[LogPublishingOptions] = None
    VpcOptions: Optional[VpcOptionsUnion] = None
    BufferOptions: Optional[BufferOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    Tags: Optional[Sequence[Tag]] = None


class CreatePipelineResponse(BaseValidatorModel):
    Pipeline: Pipeline
    ResponseMetadata: ResponseMetadata


class GetPipelineResponse(BaseValidatorModel):
    Pipeline: Pipeline
    ResponseMetadata: ResponseMetadata


class StartPipelineResponse(BaseValidatorModel):
    Pipeline: Pipeline
    ResponseMetadata: ResponseMetadata


class StopPipelineResponse(BaseValidatorModel):
    Pipeline: Pipeline
    ResponseMetadata: ResponseMetadata


class UpdatePipelineResponse(BaseValidatorModel):
    Pipeline: Pipeline
    ResponseMetadata: ResponseMetadata



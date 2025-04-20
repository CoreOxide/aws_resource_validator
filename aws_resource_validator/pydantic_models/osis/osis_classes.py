from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.osis.osis_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


class PipelineDestination(BaseValidatorModel):
    ServiceName: Optional[str] = None
    Endpoint: Optional[str] = None


class PipelineStatusReason(BaseValidatorModel):
    Description: Optional[str] = None


class ServiceVpcEndpoint(BaseValidatorModel):
    ServiceName: Optional[Literal['OPENSEARCH_SERVERLESS']] = None
    VpcEndpointId: Optional[str] = None


class StartPipelineRequest(BaseValidatorModel):
    PipelineName: str


class StopPipelineRequest(BaseValidatorModel):
    PipelineName: str


class UntagResourceRequest(BaseValidatorModel):
    Arn: str
    TagKeys: List[str]


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
    Tags: List[Tag]


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
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None
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

VpcOptionsUnion = Union[VpcOptions, VpcOptionsOutput]


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


class CreatePipelineRequest(BaseValidatorModel):
    PipelineName: str
    MinUnits: int
    MaxUnits: int
    PipelineConfigurationBody: str
    LogPublishingOptions: Optional[LogPublishingOptions] = None
    VpcOptions: Optional[VpcOptionsUnion] = None
    BufferOptions: Optional[BufferOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    Tags: Optional[List[Tag]] = None


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
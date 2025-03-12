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

class BufferOptionsTypeDef(BaseValidatorModel):
    PersistentBufferEnabled: bool


class ChangeProgressStageTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[ChangeProgressStageStatusesType] = None
    Description: Optional[str] = None
    LastUpdatedAt: Optional[datetime] = None


class CloudWatchLogDestinationTypeDef(BaseValidatorModel):
    LogGroup: str


class EncryptionAtRestOptionsTypeDef(BaseValidatorModel):
    KmsKeyArn: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeletePipelineRequestTypeDef(BaseValidatorModel):
    PipelineName: str


class GetPipelineBlueprintRequestTypeDef(BaseValidatorModel):
    BlueprintName: str
    Format: Optional[str] = None


class PipelineBlueprintTypeDef(BaseValidatorModel):
    BlueprintName: Optional[str] = None
    PipelineConfigurationBody: Optional[str] = None
    DisplayName: Optional[str] = None
    DisplayDescription: Optional[str] = None
    Service: Optional[str] = None
    UseCase: Optional[str] = None


class GetPipelineChangeProgressRequestTypeDef(BaseValidatorModel):
    PipelineName: str


class GetPipelineRequestTypeDef(BaseValidatorModel):
    PipelineName: str


class PipelineBlueprintSummaryTypeDef(BaseValidatorModel):
    BlueprintName: Optional[str] = None
    DisplayName: Optional[str] = None
    DisplayDescription: Optional[str] = None
    Service: Optional[str] = None
    UseCase: Optional[str] = None


class ListPipelinesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    Arn: str


class PipelineStatusReasonTypeDef(BaseValidatorModel):
    Description: Optional[str] = None


class StartPipelineRequestTypeDef(BaseValidatorModel):
    PipelineName: str


class StopPipelineRequestTypeDef(BaseValidatorModel):
    PipelineName: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    Arn: str
    TagKeys: Sequence[str]


class ValidatePipelineRequestTypeDef(BaseValidatorModel):
    PipelineConfigurationBody: str


class ValidationMessageTypeDef(BaseValidatorModel):
    Message: Optional[str] = None


class VpcAttachmentOptionsTypeDef(BaseValidatorModel):
    AttachToVpc: bool
    CidrBlock: Optional[str] = None


class ChangeProgressStatusTypeDef(BaseValidatorModel):
    StartTime: Optional[datetime] = None
    Status: Optional[ChangeProgressStatusesType] = None
    TotalNumberOfStages: Optional[int] = None
    ChangeProgressStages: Optional[List[ChangeProgressStageTypeDef]] = None


class LogPublishingOptionsTypeDef(BaseValidatorModel):
    IsLoggingEnabled: Optional[bool] = None
    CloudWatchLogDestination: Optional[CloudWatchLogDestinationTypeDef] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Sequence[TagTypeDef]


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetPipelineBlueprintResponseTypeDef(BaseValidatorModel):
    Blueprint: PipelineBlueprintTypeDef
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPipelineBlueprintsResponseTypeDef(BaseValidatorModel):
    Blueprints: List[PipelineBlueprintSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PipelineDestinationTypeDef(BaseValidatorModel):
    pass


class PipelineSummaryTypeDef(BaseValidatorModel):
    Status: Optional[PipelineStatusType] = None
    StatusReason: Optional[PipelineStatusReasonTypeDef] = None
    PipelineName: Optional[str] = None
    PipelineArn: Optional[str] = None
    MinUnits: Optional[int] = None
    MaxUnits: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Destinations: Optional[List[PipelineDestinationTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None


class ValidatePipelineResponseTypeDef(BaseValidatorModel):
    isValid: bool
    Errors: List[ValidationMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class VpcOptionsOutputTypeDef(BaseValidatorModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None
    VpcAttachmentOptions: Optional[VpcAttachmentOptionsTypeDef] = None
    VpcEndpointManagement: Optional[VpcEndpointManagementType] = None


class VpcOptionsTypeDef(BaseValidatorModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None
    VpcAttachmentOptions: Optional[VpcAttachmentOptionsTypeDef] = None
    VpcEndpointManagement: Optional[VpcEndpointManagementType] = None


class GetPipelineChangeProgressResponseTypeDef(BaseValidatorModel):
    ChangeProgressStatuses: List[ChangeProgressStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePipelineRequestTypeDef(BaseValidatorModel):
    PipelineName: str
    MinUnits: Optional[int] = None
    MaxUnits: Optional[int] = None
    PipelineConfigurationBody: Optional[str] = None
    LogPublishingOptions: Optional[LogPublishingOptionsTypeDef] = None
    BufferOptions: Optional[BufferOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None


class ListPipelinesResponseTypeDef(BaseValidatorModel):
    Pipelines: List[PipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class VpcEndpointTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcOptions: Optional[VpcOptionsOutputTypeDef] = None


class ServiceVpcEndpointTypeDef(BaseValidatorModel):
    pass


class PipelineTypeDef(BaseValidatorModel):
    PipelineName: Optional[str] = None
    PipelineArn: Optional[str] = None
    MinUnits: Optional[int] = None
    MaxUnits: Optional[int] = None
    Status: Optional[PipelineStatusType] = None
    StatusReason: Optional[PipelineStatusReasonTypeDef] = None
    PipelineConfigurationBody: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    IngestEndpointUrls: Optional[List[str]] = None
    LogPublishingOptions: Optional[LogPublishingOptionsTypeDef] = None
    VpcEndpoints: Optional[List[VpcEndpointTypeDef]] = None
    BufferOptions: Optional[BufferOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    VpcEndpointService: Optional[str] = None
    ServiceVpcEndpoints: Optional[List[ServiceVpcEndpointTypeDef]] = None
    Destinations: Optional[List[PipelineDestinationTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None


class VpcOptionsUnionTypeDef(BaseValidatorModel):
    pass


class CreatePipelineRequestTypeDef(BaseValidatorModel):
    PipelineName: str
    MinUnits: int
    MaxUnits: int
    PipelineConfigurationBody: str
    LogPublishingOptions: Optional[LogPublishingOptionsTypeDef] = None
    VpcOptions: Optional[VpcOptionsUnionTypeDef] = None
    BufferOptions: Optional[BufferOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreatePipelineResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPipelineResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartPipelineResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopPipelineResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePipelineResponseTypeDef(BaseValidatorModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



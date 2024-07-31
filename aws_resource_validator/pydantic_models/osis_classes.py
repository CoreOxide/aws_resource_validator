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
from aws_resource_validator.pydantic_models.osis_constants import *

class BufferOptionsTypeDef(BaseModel):
    PersistentBufferEnabled: bool

class ChangeProgressStageTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[ChangeProgressStageStatusesType] = None
    Description: Optional[str] = None
    LastUpdatedAt: Optional[datetime] = None

class CloudWatchLogDestinationTypeDef(BaseModel):
    LogGroup: str

class EncryptionAtRestOptionsTypeDef(BaseModel):
    KmsKeyArn: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeletePipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str

class GetPipelineBlueprintRequestRequestTypeDef(BaseModel):
    BlueprintName: str
    Format: Optional[str] = None

class PipelineBlueprintTypeDef(BaseModel):
    BlueprintName: Optional[str] = None
    PipelineConfigurationBody: Optional[str] = None
    DisplayName: Optional[str] = None
    DisplayDescription: Optional[str] = None
    Service: Optional[str] = None
    UseCase: Optional[str] = None

class GetPipelineChangeProgressRequestRequestTypeDef(BaseModel):
    PipelineName: str

class GetPipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str

class PipelineBlueprintSummaryTypeDef(BaseModel):
    BlueprintName: Optional[str] = None
    DisplayName: Optional[str] = None
    DisplayDescription: Optional[str] = None
    Service: Optional[str] = None
    UseCase: Optional[str] = None

class ListPipelinesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    Arn: str

class PipelineDestinationTypeDef(BaseModel):
    ServiceName: Optional[str] = None
    Endpoint: Optional[str] = None

class PipelineStatusReasonTypeDef(BaseModel):
    Description: Optional[str] = None

class ServiceVpcEndpointTypeDef(BaseModel):
    ServiceName: Optional[Literal["OPENSEARCH_SERVERLESS"]] = None
    VpcEndpointId: Optional[str] = None

class StartPipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str

class StopPipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    TagKeys: Sequence[str]

class ValidatePipelineRequestRequestTypeDef(BaseModel):
    PipelineConfigurationBody: str

class ValidationMessageTypeDef(BaseModel):
    Message: Optional[str] = None

class VpcAttachmentOptionsTypeDef(BaseModel):
    AttachToVpc: bool
    CidrBlock: Optional[str] = None

class ChangeProgressStatusTypeDef(BaseModel):
    StartTime: Optional[datetime] = None
    Status: Optional[ChangeProgressStatusesType] = None
    TotalNumberOfStages: Optional[int] = None
    ChangeProgressStages: Optional[List[ChangeProgressStageTypeDef]] = None

class LogPublishingOptionsTypeDef(BaseModel):
    IsLoggingEnabled: Optional[bool] = None
    CloudWatchLogDestination: Optional[CloudWatchLogDestinationTypeDef] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    Tags: Sequence[TagTypeDef]

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPipelineBlueprintResponseTypeDef(BaseModel):
    Blueprint: PipelineBlueprintTypeDef
    Format: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPipelineBlueprintsResponseTypeDef(BaseModel):
    Blueprints: List[PipelineBlueprintSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PipelineSummaryTypeDef(BaseModel):
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

class ValidatePipelineResponseTypeDef(BaseModel):
    isValid: bool
    Errors: List[ValidationMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VpcOptionsOutputTypeDef(BaseModel):
    SubnetIds: List[str]
    SecurityGroupIds: Optional[List[str]] = None
    VpcAttachmentOptions: Optional[VpcAttachmentOptionsTypeDef] = None
    VpcEndpointManagement: Optional[VpcEndpointManagementType] = None

class VpcOptionsTypeDef(BaseModel):
    SubnetIds: Sequence[str]
    SecurityGroupIds: Optional[Sequence[str]] = None
    VpcAttachmentOptions: Optional[VpcAttachmentOptionsTypeDef] = None
    VpcEndpointManagement: Optional[VpcEndpointManagementType] = None

class GetPipelineChangeProgressResponseTypeDef(BaseModel):
    ChangeProgressStatuses: List[ChangeProgressStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str
    MinUnits: Optional[int] = None
    MaxUnits: Optional[int] = None
    PipelineConfigurationBody: Optional[str] = None
    LogPublishingOptions: Optional[LogPublishingOptionsTypeDef] = None
    BufferOptions: Optional[BufferOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None

class ListPipelinesResponseTypeDef(BaseModel):
    Pipelines: List[PipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class VpcEndpointTypeDef(BaseModel):
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcOptions: Optional[VpcOptionsOutputTypeDef] = None

class CreatePipelineRequestRequestTypeDef(BaseModel):
    PipelineName: str
    MinUnits: int
    MaxUnits: int
    PipelineConfigurationBody: str
    LogPublishingOptions: Optional[LogPublishingOptionsTypeDef] = None
    VpcOptions: Optional[VpcOptionsTypeDef] = None
    BufferOptions: Optional[BufferOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class PipelineTypeDef(BaseModel):
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

class CreatePipelineResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPipelineResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipelineResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopPipelineResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineResponseTypeDef(BaseModel):
    Pipeline: PipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


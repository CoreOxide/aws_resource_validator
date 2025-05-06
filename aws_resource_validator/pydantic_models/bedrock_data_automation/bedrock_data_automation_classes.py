from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AudioExtractionCategoryOutput(BaseValidatorModel):
    state: StateType
    types: Optional[List[AudioExtractionCategoryTypeType]] = None


class AudioExtractionCategory(BaseValidatorModel):
    state: StateType
    types: Optional[List[AudioExtractionCategoryTypeType]] = None


class AudioStandardGenerativeFieldOutput(BaseValidatorModel):
    state: StateType
    types: Optional[List[AudioStandardGenerativeFieldTypeType]] = None


class AudioStandardGenerativeField(BaseValidatorModel):
    state: StateType
    types: Optional[List[AudioStandardGenerativeFieldTypeType]] = None


class BlueprintFilter(BaseValidatorModel):
    blueprintArn: str
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None


class BlueprintItem(BaseValidatorModel):
    blueprintArn: str
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None


class BlueprintSummary(BaseValidatorModel):
    blueprintArn: str
    creationTime: datetime
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None
    blueprintName: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None


class Blueprint(BaseValidatorModel):
    blueprintArn: str
    schema: str
    type: TypeType
    creationTime: datetime
    lastModifiedTime: datetime
    blueprintName: str
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None
    kmsKeyId: Optional[str] = None
    kmsEncryptionContext: Optional[Dict[str, str]] = None


class EncryptionConfiguration(BaseValidatorModel):
    kmsKeyId: str
    kmsEncryptionContext: Optional[Dict[str, str]] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateBlueprintVersionRequest(BaseValidatorModel):
    blueprintArn: str
    clientToken: Optional[str] = None


class DataAutomationProjectFilter(BaseValidatorModel):
    projectArn: str
    projectStage: Optional[DataAutomationProjectStageType] = None


class DataAutomationProjectSummary(BaseValidatorModel):
    projectArn: str
    creationTime: datetime
    projectStage: Optional[DataAutomationProjectStageType] = None
    projectName: Optional[str] = None


class DeleteBlueprintRequest(BaseValidatorModel):
    blueprintArn: str
    blueprintVersion: Optional[str] = None


class DeleteDataAutomationProjectRequest(BaseValidatorModel):
    projectArn: str


class DocumentBoundingBox(BaseValidatorModel):
    state: StateType


class DocumentExtractionGranularityOutput(BaseValidatorModel):
    types: Optional[List[DocumentExtractionGranularityTypeType]] = None


class DocumentExtractionGranularity(BaseValidatorModel):
    types: Optional[List[DocumentExtractionGranularityTypeType]] = None


class DocumentOutputAdditionalFileFormat(BaseValidatorModel):
    state: StateType


class DocumentOutputTextFormatOutput(BaseValidatorModel):
    types: Optional[List[DocumentOutputTextFormatTypeType]] = None


class DocumentOutputTextFormat(BaseValidatorModel):
    types: Optional[List[DocumentOutputTextFormatTypeType]] = None


class SplitterConfiguration(BaseValidatorModel):
    state: Optional[StateType] = None


class DocumentStandardGenerativeField(BaseValidatorModel):
    state: StateType


class GetBlueprintRequest(BaseValidatorModel):
    blueprintArn: str
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None


class GetDataAutomationProjectRequest(BaseValidatorModel):
    projectArn: str
    projectStage: Optional[DataAutomationProjectStageType] = None


class ImageBoundingBox(BaseValidatorModel):
    state: StateType


class ImageExtractionCategoryOutput(BaseValidatorModel):
    state: StateType
    types: Optional[List[ImageExtractionCategoryTypeType]] = None


class ImageExtractionCategory(BaseValidatorModel):
    state: StateType
    types: Optional[List[ImageExtractionCategoryTypeType]] = None


class ImageStandardGenerativeFieldOutput(BaseValidatorModel):
    state: StateType
    types: Optional[List[ImageStandardGenerativeFieldTypeType]] = None


class ImageStandardGenerativeField(BaseValidatorModel):
    state: StateType
    types: Optional[List[ImageStandardGenerativeFieldTypeType]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: List[str]


class VideoBoundingBox(BaseValidatorModel):
    state: StateType


class VideoExtractionCategoryOutput(BaseValidatorModel):
    state: StateType
    types: Optional[List[VideoExtractionCategoryTypeType]] = None


class VideoExtractionCategory(BaseValidatorModel):
    state: StateType
    types: Optional[List[VideoExtractionCategoryTypeType]] = None


class VideoStandardGenerativeFieldOutput(BaseValidatorModel):
    state: StateType
    types: Optional[List[VideoStandardGenerativeFieldTypeType]] = None


class VideoStandardGenerativeField(BaseValidatorModel):
    state: StateType
    types: Optional[List[VideoStandardGenerativeFieldTypeType]] = None


class AudioStandardExtractionOutput(BaseValidatorModel):
    category: AudioExtractionCategoryOutput


class AudioStandardExtraction(BaseValidatorModel):
    category: AudioExtractionCategory


class ListDataAutomationProjectsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    projectStageFilter: Optional[DataAutomationProjectStageFilterType] = None
    blueprintFilter: Optional[BlueprintFilter] = None
    resourceOwner: Optional[ResourceOwnerType] = None


class CustomOutputConfigurationOutput(BaseValidatorModel):
    blueprints: Optional[List[BlueprintItem]] = None


class CustomOutputConfiguration(BaseValidatorModel):
    blueprints: Optional[List[BlueprintItem]] = None


class UpdateBlueprintRequest(BaseValidatorModel):
    blueprintArn: str
    schema: str
    blueprintStage: Optional[BlueprintStageType] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None


class CreateBlueprintRequest(BaseValidatorModel):
    blueprintName: str
    type: TypeType
    schema: str
    blueprintStage: Optional[BlueprintStageType] = None
    clientToken: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None
    tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: List[Tag]


class CreateBlueprintResponse(BaseValidatorModel):
    blueprint: Blueprint
    ResponseMetadata: ResponseMetadata


class CreateBlueprintVersionResponse(BaseValidatorModel):
    blueprint: Blueprint
    ResponseMetadata: ResponseMetadata


class CreateDataAutomationProjectResponse(BaseValidatorModel):
    projectArn: str
    projectStage: DataAutomationProjectStageType
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadata


class DeleteDataAutomationProjectResponse(BaseValidatorModel):
    projectArn: str
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadata


class GetBlueprintResponse(BaseValidatorModel):
    blueprint: Blueprint
    ResponseMetadata: ResponseMetadata


class ListBlueprintsResponse(BaseValidatorModel):
    blueprints: List[BlueprintSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateBlueprintResponse(BaseValidatorModel):
    blueprint: Blueprint
    ResponseMetadata: ResponseMetadata


class UpdateDataAutomationProjectResponse(BaseValidatorModel):
    projectArn: str
    projectStage: DataAutomationProjectStageType
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadata


class ListBlueprintsRequest(BaseValidatorModel):
    blueprintArn: Optional[str] = None
    resourceOwner: Optional[ResourceOwnerType] = None
    blueprintStageFilter: Optional[BlueprintStageFilterType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    projectFilter: Optional[DataAutomationProjectFilter] = None


class ListDataAutomationProjectsResponse(BaseValidatorModel):
    projects: List[DataAutomationProjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DocumentStandardExtractionOutput(BaseValidatorModel):
    granularity: DocumentExtractionGranularityOutput
    boundingBox: DocumentBoundingBox


class DocumentStandardExtraction(BaseValidatorModel):
    granularity: DocumentExtractionGranularity
    boundingBox: DocumentBoundingBox


class DocumentOutputFormatOutput(BaseValidatorModel):
    textFormat: DocumentOutputTextFormatOutput
    additionalFileFormat: DocumentOutputAdditionalFileFormat


class DocumentOutputFormat(BaseValidatorModel):
    textFormat: DocumentOutputTextFormat
    additionalFileFormat: DocumentOutputAdditionalFileFormat


class DocumentOverrideConfiguration(BaseValidatorModel):
    splitter: Optional[SplitterConfiguration] = None


class ImageStandardExtractionOutput(BaseValidatorModel):
    category: ImageExtractionCategoryOutput
    boundingBox: ImageBoundingBox


class ImageStandardExtraction(BaseValidatorModel):
    category: ImageExtractionCategory
    boundingBox: ImageBoundingBox


class ListBlueprintsRequestPaginate(BaseValidatorModel):
    blueprintArn: Optional[str] = None
    resourceOwner: Optional[ResourceOwnerType] = None
    blueprintStageFilter: Optional[BlueprintStageFilterType] = None
    projectFilter: Optional[DataAutomationProjectFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataAutomationProjectsRequestPaginate(BaseValidatorModel):
    projectStageFilter: Optional[DataAutomationProjectStageFilterType] = None
    blueprintFilter: Optional[BlueprintFilter] = None
    resourceOwner: Optional[ResourceOwnerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class VideoStandardExtractionOutput(BaseValidatorModel):
    category: VideoExtractionCategoryOutput
    boundingBox: VideoBoundingBox


class VideoStandardExtraction(BaseValidatorModel):
    category: VideoExtractionCategory
    boundingBox: VideoBoundingBox


class AudioStandardOutputConfigurationOutput(BaseValidatorModel):
    extraction: Optional[AudioStandardExtractionOutput] = None
    generativeField: Optional[AudioStandardGenerativeFieldOutput] = None


class AudioStandardOutputConfiguration(BaseValidatorModel):
    extraction: Optional[AudioStandardExtraction] = None
    generativeField: Optional[AudioStandardGenerativeField] = None

CustomOutputConfigurationUnion = Union[CustomOutputConfiguration, CustomOutputConfigurationOutput]


class DocumentStandardOutputConfigurationOutput(BaseValidatorModel):
    extraction: Optional[DocumentStandardExtractionOutput] = None
    generativeField: Optional[DocumentStandardGenerativeField] = None
    outputFormat: Optional[DocumentOutputFormatOutput] = None


class DocumentStandardOutputConfiguration(BaseValidatorModel):
    extraction: Optional[DocumentStandardExtraction] = None
    generativeField: Optional[DocumentStandardGenerativeField] = None
    outputFormat: Optional[DocumentOutputFormat] = None


class OverrideConfiguration(BaseValidatorModel):
    document: Optional[DocumentOverrideConfiguration] = None


class ImageStandardOutputConfigurationOutput(BaseValidatorModel):
    extraction: Optional[ImageStandardExtractionOutput] = None
    generativeField: Optional[ImageStandardGenerativeFieldOutput] = None


class ImageStandardOutputConfiguration(BaseValidatorModel):
    extraction: Optional[ImageStandardExtraction] = None
    generativeField: Optional[ImageStandardGenerativeField] = None


class VideoStandardOutputConfigurationOutput(BaseValidatorModel):
    extraction: Optional[VideoStandardExtractionOutput] = None
    generativeField: Optional[VideoStandardGenerativeFieldOutput] = None


class VideoStandardOutputConfiguration(BaseValidatorModel):
    extraction: Optional[VideoStandardExtraction] = None
    generativeField: Optional[VideoStandardGenerativeField] = None


class StandardOutputConfigurationOutput(BaseValidatorModel):
    document: Optional[DocumentStandardOutputConfigurationOutput] = None
    image: Optional[ImageStandardOutputConfigurationOutput] = None
    video: Optional[VideoStandardOutputConfigurationOutput] = None
    audio: Optional[AudioStandardOutputConfigurationOutput] = None


class StandardOutputConfiguration(BaseValidatorModel):
    document: Optional[DocumentStandardOutputConfiguration] = None
    image: Optional[ImageStandardOutputConfiguration] = None
    video: Optional[VideoStandardOutputConfiguration] = None
    audio: Optional[AudioStandardOutputConfiguration] = None


class DataAutomationProject(BaseValidatorModel):
    projectArn: str
    creationTime: datetime
    lastModifiedTime: datetime
    projectName: str
    status: DataAutomationProjectStatusType
    projectStage: Optional[DataAutomationProjectStageType] = None
    projectDescription: Optional[str] = None
    standardOutputConfiguration: Optional[StandardOutputConfigurationOutput] = None
    customOutputConfiguration: Optional[CustomOutputConfigurationOutput] = None
    overrideConfiguration: Optional[OverrideConfiguration] = None
    kmsKeyId: Optional[str] = None
    kmsEncryptionContext: Optional[Dict[str, str]] = None

StandardOutputConfigurationUnion = Union[StandardOutputConfiguration, StandardOutputConfigurationOutput]


class GetDataAutomationProjectResponse(BaseValidatorModel):
    project: DataAutomationProject
    ResponseMetadata: ResponseMetadata


class CreateDataAutomationProjectRequest(BaseValidatorModel):
    projectName: str
    standardOutputConfiguration: StandardOutputConfigurationUnion
    projectDescription: Optional[str] = None
    projectStage: Optional[DataAutomationProjectStageType] = None
    customOutputConfiguration: Optional[CustomOutputConfigurationUnion] = None
    overrideConfiguration: Optional[OverrideConfiguration] = None
    clientToken: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None
    tags: Optional[List[Tag]] = None


class UpdateDataAutomationProjectRequest(BaseValidatorModel):
    projectArn: str
    standardOutputConfiguration: StandardOutputConfigurationUnion
    projectStage: Optional[DataAutomationProjectStageType] = None
    projectDescription: Optional[str] = None
    customOutputConfiguration: Optional[CustomOutputConfigurationUnion] = None
    overrideConfiguration: Optional[OverrideConfiguration] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None
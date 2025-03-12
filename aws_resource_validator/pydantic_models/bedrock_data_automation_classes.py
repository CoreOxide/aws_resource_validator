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
from aws_resource_validator.pydantic_models.bedrock_data_automation_constants import *

class BlueprintFilterTypeDef(BaseValidatorModel):
    blueprintArn: str
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None


class BlueprintItemTypeDef(BaseValidatorModel):
    blueprintArn: str
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None


class BlueprintSummaryTypeDef(BaseValidatorModel):
    blueprintArn: str
    creationTime: datetime
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None
    blueprintName: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: str
    kmsEncryptionContext: Optional[Mapping[str, str]] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateBlueprintVersionRequestTypeDef(BaseValidatorModel):
    blueprintArn: str
    clientToken: Optional[str] = None


class DataAutomationProjectFilterTypeDef(BaseValidatorModel):
    projectArn: str
    projectStage: Optional[DataAutomationProjectStageType] = None


class DataAutomationProjectSummaryTypeDef(BaseValidatorModel):
    projectArn: str
    creationTime: datetime
    projectStage: Optional[DataAutomationProjectStageType] = None
    projectName: Optional[str] = None


class DeleteBlueprintRequestTypeDef(BaseValidatorModel):
    blueprintArn: str
    blueprintVersion: Optional[str] = None


class DeleteDataAutomationProjectRequestTypeDef(BaseValidatorModel):
    projectArn: str


class DocumentBoundingBoxTypeDef(BaseValidatorModel):
    state: StateType


class DocumentOutputAdditionalFileFormatTypeDef(BaseValidatorModel):
    state: StateType


class SplitterConfigurationTypeDef(BaseValidatorModel):
    state: Optional[StateType] = None


class DocumentStandardGenerativeFieldTypeDef(BaseValidatorModel):
    state: StateType


class GetBlueprintRequestTypeDef(BaseValidatorModel):
    blueprintArn: str
    blueprintVersion: Optional[str] = None
    blueprintStage: Optional[BlueprintStageType] = None


class GetDataAutomationProjectRequestTypeDef(BaseValidatorModel):
    projectArn: str
    projectStage: Optional[DataAutomationProjectStageType] = None


class ImageBoundingBoxTypeDef(BaseValidatorModel):
    state: StateType


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class VideoBoundingBoxTypeDef(BaseValidatorModel):
    state: StateType


class AudioExtractionCategoryOutputTypeDef(BaseValidatorModel):
    pass


class AudioStandardExtractionOutputTypeDef(BaseValidatorModel):
    category: AudioExtractionCategoryOutputTypeDef


class AudioExtractionCategoryTypeDef(BaseValidatorModel):
    pass


class AudioStandardExtractionTypeDef(BaseValidatorModel):
    category: AudioExtractionCategoryTypeDef


class ListDataAutomationProjectsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    projectStageFilter: Optional[DataAutomationProjectStageFilterType] = None
    blueprintFilter: Optional[BlueprintFilterTypeDef] = None
    resourceOwner: Optional[ResourceOwnerType] = None


class CustomOutputConfigurationOutputTypeDef(BaseValidatorModel):
    blueprints: Optional[List[BlueprintItemTypeDef]] = None


class CustomOutputConfigurationTypeDef(BaseValidatorModel):
    blueprints: Optional[Sequence[BlueprintItemTypeDef]] = None


class UpdateBlueprintRequestTypeDef(BaseValidatorModel):
    blueprintArn: str
    schema: str
    blueprintStage: Optional[BlueprintStageType] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]


class BlueprintTypeDef(BaseValidatorModel):
    pass


class CreateBlueprintResponseTypeDef(BaseValidatorModel):
    blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBlueprintVersionResponseTypeDef(BaseValidatorModel):
    blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataAutomationProjectResponseTypeDef(BaseValidatorModel):
    projectArn: str
    projectStage: DataAutomationProjectStageType
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataAutomationProjectResponseTypeDef(BaseValidatorModel):
    projectArn: str
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetBlueprintResponseTypeDef(BaseValidatorModel):
    blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListBlueprintsResponseTypeDef(BaseValidatorModel):
    blueprints: List[BlueprintSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBlueprintResponseTypeDef(BaseValidatorModel):
    blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataAutomationProjectResponseTypeDef(BaseValidatorModel):
    projectArn: str
    projectStage: DataAutomationProjectStageType
    status: DataAutomationProjectStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class ListBlueprintsRequestTypeDef(BaseValidatorModel):
    blueprintArn: Optional[str] = None
    resourceOwner: Optional[ResourceOwnerType] = None
    blueprintStageFilter: Optional[BlueprintStageFilterType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    projectFilter: Optional[DataAutomationProjectFilterTypeDef] = None


class ListDataAutomationProjectsResponseTypeDef(BaseValidatorModel):
    projects: List[DataAutomationProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DocumentExtractionGranularityOutputTypeDef(BaseValidatorModel):
    pass


class DocumentStandardExtractionOutputTypeDef(BaseValidatorModel):
    granularity: DocumentExtractionGranularityOutputTypeDef
    boundingBox: DocumentBoundingBoxTypeDef


class DocumentExtractionGranularityTypeDef(BaseValidatorModel):
    pass


class DocumentStandardExtractionTypeDef(BaseValidatorModel):
    granularity: DocumentExtractionGranularityTypeDef
    boundingBox: DocumentBoundingBoxTypeDef


class DocumentOutputTextFormatOutputTypeDef(BaseValidatorModel):
    pass


class DocumentOutputFormatOutputTypeDef(BaseValidatorModel):
    textFormat: DocumentOutputTextFormatOutputTypeDef
    additionalFileFormat: DocumentOutputAdditionalFileFormatTypeDef


class DocumentOutputTextFormatTypeDef(BaseValidatorModel):
    pass


class DocumentOutputFormatTypeDef(BaseValidatorModel):
    textFormat: DocumentOutputTextFormatTypeDef
    additionalFileFormat: DocumentOutputAdditionalFileFormatTypeDef


class DocumentOverrideConfigurationTypeDef(BaseValidatorModel):
    splitter: Optional[SplitterConfigurationTypeDef] = None


class ImageExtractionCategoryOutputTypeDef(BaseValidatorModel):
    pass


class ImageStandardExtractionOutputTypeDef(BaseValidatorModel):
    category: ImageExtractionCategoryOutputTypeDef
    boundingBox: ImageBoundingBoxTypeDef


class ImageExtractionCategoryTypeDef(BaseValidatorModel):
    pass


class ImageStandardExtractionTypeDef(BaseValidatorModel):
    category: ImageExtractionCategoryTypeDef
    boundingBox: ImageBoundingBoxTypeDef


class ListBlueprintsRequestPaginateTypeDef(BaseValidatorModel):
    blueprintArn: Optional[str] = None
    resourceOwner: Optional[ResourceOwnerType] = None
    blueprintStageFilter: Optional[BlueprintStageFilterType] = None
    projectFilter: Optional[DataAutomationProjectFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataAutomationProjectsRequestPaginateTypeDef(BaseValidatorModel):
    projectStageFilter: Optional[DataAutomationProjectStageFilterType] = None
    blueprintFilter: Optional[BlueprintFilterTypeDef] = None
    resourceOwner: Optional[ResourceOwnerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class VideoExtractionCategoryOutputTypeDef(BaseValidatorModel):
    pass


class VideoStandardExtractionOutputTypeDef(BaseValidatorModel):
    category: VideoExtractionCategoryOutputTypeDef
    boundingBox: VideoBoundingBoxTypeDef


class VideoExtractionCategoryTypeDef(BaseValidatorModel):
    pass


class VideoStandardExtractionTypeDef(BaseValidatorModel):
    category: VideoExtractionCategoryTypeDef
    boundingBox: VideoBoundingBoxTypeDef


class AudioStandardGenerativeFieldOutputTypeDef(BaseValidatorModel):
    pass


class AudioStandardOutputConfigurationOutputTypeDef(BaseValidatorModel):
    extraction: Optional[AudioStandardExtractionOutputTypeDef] = None
    generativeField: Optional[AudioStandardGenerativeFieldOutputTypeDef] = None


class AudioStandardGenerativeFieldTypeDef(BaseValidatorModel):
    pass


class AudioStandardOutputConfigurationTypeDef(BaseValidatorModel):
    extraction: Optional[AudioStandardExtractionTypeDef] = None
    generativeField: Optional[AudioStandardGenerativeFieldTypeDef] = None


class DocumentStandardOutputConfigurationOutputTypeDef(BaseValidatorModel):
    extraction: Optional[DocumentStandardExtractionOutputTypeDef] = None
    generativeField: Optional[DocumentStandardGenerativeFieldTypeDef] = None
    outputFormat: Optional[DocumentOutputFormatOutputTypeDef] = None


class DocumentStandardOutputConfigurationTypeDef(BaseValidatorModel):
    extraction: Optional[DocumentStandardExtractionTypeDef] = None
    generativeField: Optional[DocumentStandardGenerativeFieldTypeDef] = None
    outputFormat: Optional[DocumentOutputFormatTypeDef] = None


class OverrideConfigurationTypeDef(BaseValidatorModel):
    document: Optional[DocumentOverrideConfigurationTypeDef] = None


class ImageStandardGenerativeFieldOutputTypeDef(BaseValidatorModel):
    pass


class ImageStandardOutputConfigurationOutputTypeDef(BaseValidatorModel):
    extraction: Optional[ImageStandardExtractionOutputTypeDef] = None
    generativeField: Optional[ImageStandardGenerativeFieldOutputTypeDef] = None


class ImageStandardGenerativeFieldTypeDef(BaseValidatorModel):
    pass


class ImageStandardOutputConfigurationTypeDef(BaseValidatorModel):
    extraction: Optional[ImageStandardExtractionTypeDef] = None
    generativeField: Optional[ImageStandardGenerativeFieldTypeDef] = None


class VideoStandardGenerativeFieldOutputTypeDef(BaseValidatorModel):
    pass


class VideoStandardOutputConfigurationOutputTypeDef(BaseValidatorModel):
    extraction: Optional[VideoStandardExtractionOutputTypeDef] = None
    generativeField: Optional[VideoStandardGenerativeFieldOutputTypeDef] = None


class VideoStandardGenerativeFieldTypeDef(BaseValidatorModel):
    pass


class VideoStandardOutputConfigurationTypeDef(BaseValidatorModel):
    extraction: Optional[VideoStandardExtractionTypeDef] = None
    generativeField: Optional[VideoStandardGenerativeFieldTypeDef] = None


class StandardOutputConfigurationOutputTypeDef(BaseValidatorModel):
    document: Optional[DocumentStandardOutputConfigurationOutputTypeDef] = None
    image: Optional[ImageStandardOutputConfigurationOutputTypeDef] = None
    video: Optional[VideoStandardOutputConfigurationOutputTypeDef] = None
    audio: Optional[AudioStandardOutputConfigurationOutputTypeDef] = None


class StandardOutputConfigurationTypeDef(BaseValidatorModel):
    document: Optional[DocumentStandardOutputConfigurationTypeDef] = None
    image: Optional[ImageStandardOutputConfigurationTypeDef] = None
    video: Optional[VideoStandardOutputConfigurationTypeDef] = None
    audio: Optional[AudioStandardOutputConfigurationTypeDef] = None


class DataAutomationProjectTypeDef(BaseValidatorModel):
    projectArn: str
    creationTime: datetime
    lastModifiedTime: datetime
    projectName: str
    status: DataAutomationProjectStatusType
    projectStage: Optional[DataAutomationProjectStageType] = None
    projectDescription: Optional[str] = None
    standardOutputConfiguration: Optional[StandardOutputConfigurationOutputTypeDef] = None
    customOutputConfiguration: Optional[CustomOutputConfigurationOutputTypeDef] = None
    overrideConfiguration: Optional[OverrideConfigurationTypeDef] = None
    kmsKeyId: Optional[str] = None
    kmsEncryptionContext: Optional[Dict[str, str]] = None


class GetDataAutomationProjectResponseTypeDef(BaseValidatorModel):
    project: DataAutomationProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CustomOutputConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class StandardOutputConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataAutomationProjectRequestTypeDef(BaseValidatorModel):
    projectName: str
    standardOutputConfiguration: StandardOutputConfigurationUnionTypeDef
    projectDescription: Optional[str] = None
    projectStage: Optional[DataAutomationProjectStageType] = None
    customOutputConfiguration: Optional[CustomOutputConfigurationUnionTypeDef] = None
    overrideConfiguration: Optional[OverrideConfigurationTypeDef] = None
    clientToken: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateDataAutomationProjectRequestTypeDef(BaseValidatorModel):
    projectArn: str
    standardOutputConfiguration: StandardOutputConfigurationUnionTypeDef
    projectStage: Optional[DataAutomationProjectStageType] = None
    projectDescription: Optional[str] = None
    customOutputConfiguration: Optional[CustomOutputConfigurationUnionTypeDef] = None
    overrideConfiguration: Optional[OverrideConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None



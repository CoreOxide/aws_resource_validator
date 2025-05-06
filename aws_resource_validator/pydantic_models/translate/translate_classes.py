from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.translate.translate_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Term(BaseValidatorModel):
    SourceText: Optional[str] = None
    TargetText: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class EncryptionKey(BaseValidatorModel):
    Type: Literal['KMS']
    Id: str


class ParallelDataConfig(BaseValidatorModel):
    S3Uri: Optional[str] = None
    Format: Optional[ParallelDataFormatType] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteParallelDataRequest(BaseValidatorModel):
    Name: str


class DeleteTerminologyRequest(BaseValidatorModel):
    Name: str


class DescribeTextTranslationJobRequest(BaseValidatorModel):
    JobId: str


class GetParallelDataRequest(BaseValidatorModel):
    Name: str


class ParallelDataDataLocation(BaseValidatorModel):
    RepositoryType: str
    Location: str


class GetTerminologyRequest(BaseValidatorModel):
    Name: str
    TerminologyDataFormat: Optional[TerminologyDataFormatType] = None


class TerminologyDataLocation(BaseValidatorModel):
    RepositoryType: str
    Location: str


class InputDataConfig(BaseValidatorModel):
    S3Uri: str
    ContentType: str


class JobDetails(BaseValidatorModel):
    TranslatedDocumentsCount: Optional[int] = None
    DocumentsWithErrorsCount: Optional[int] = None
    InputDocumentsCount: Optional[int] = None


class Language(BaseValidatorModel):
    LanguageName: str
    LanguageCode: str


class ListLanguagesRequest(BaseValidatorModel):
    DisplayLanguageCode: Optional[DisplayLanguageCodeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListParallelDataRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListTerminologiesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TranslationSettings(BaseValidatorModel):
    Formality: Optional[FormalityType] = None
    Profanity: Optional[Literal['MASK']] = None
    Brevity: Optional[Literal['ON']] = None


class StopTextTranslationJobRequest(BaseValidatorModel):
    JobId: str

Timestamp = Union[datetime, str]


class TranslatedDocument(BaseValidatorModel):
    Content: bytes


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class AppliedTerminology(BaseValidatorModel):
    Name: Optional[str] = None
    Terms: Optional[List[Term]] = None


class Document(BaseValidatorModel):
    Content: Blob
    ContentType: str


class TerminologyData(BaseValidatorModel):
    File: Blob
    Format: TerminologyDataFormatType
    Directionality: Optional[DirectionalityType] = None


class OutputDataConfig(BaseValidatorModel):
    S3Uri: str
    EncryptionKey: Optional[EncryptionKey] = None


class TerminologyProperties(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None
    SourceLanguageCode: Optional[str] = None
    TargetLanguageCodes: Optional[List[str]] = None
    EncryptionKey: Optional[EncryptionKey] = None
    SizeBytes: Optional[int] = None
    TermCount: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Directionality: Optional[DirectionalityType] = None
    Message: Optional[str] = None
    SkippedTermCount: Optional[int] = None
    Format: Optional[TerminologyDataFormatType] = None


class ParallelDataProperties(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[ParallelDataStatusType] = None
    SourceLanguageCode: Optional[str] = None
    TargetLanguageCodes: Optional[List[str]] = None
    ParallelDataConfig: Optional[ParallelDataConfig] = None
    Message: Optional[str] = None
    ImportedDataSize: Optional[int] = None
    ImportedRecordCount: Optional[int] = None
    FailedRecordCount: Optional[int] = None
    SkippedRecordCount: Optional[int] = None
    EncryptionKey: Optional[EncryptionKey] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    LatestUpdateAttemptStatus: Optional[ParallelDataStatusType] = None
    LatestUpdateAttemptAt: Optional[datetime] = None


class UpdateParallelDataRequest(BaseValidatorModel):
    Name: str
    ParallelDataConfig: ParallelDataConfig
    ClientToken: str
    Description: Optional[str] = None


class CreateParallelDataRequest(BaseValidatorModel):
    Name: str
    ParallelDataConfig: ParallelDataConfig
    ClientToken: str
    Description: Optional[str] = None
    EncryptionKey: Optional[EncryptionKey] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CreateParallelDataResponse(BaseValidatorModel):
    Name: str
    Status: ParallelDataStatusType
    ResponseMetadata: ResponseMetadata


class DeleteParallelDataResponse(BaseValidatorModel):
    Name: str
    Status: ParallelDataStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class StartTextTranslationJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class StopTextTranslationJobResponse(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadata


class UpdateParallelDataResponse(BaseValidatorModel):
    Name: str
    Status: ParallelDataStatusType
    LatestUpdateAttemptStatus: ParallelDataStatusType
    LatestUpdateAttemptAt: datetime
    ResponseMetadata: ResponseMetadata


class ListLanguagesResponse(BaseValidatorModel):
    Languages: List[Language]
    DisplayLanguageCode: DisplayLanguageCodeType
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTerminologiesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class TranslateTextRequest(BaseValidatorModel):
    Text: str
    SourceLanguageCode: str
    TargetLanguageCode: str
    TerminologyNames: Optional[List[str]] = None
    Settings: Optional[TranslationSettings] = None


class TextTranslationJobFilter(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBeforeTime: Optional[Timestamp] = None
    SubmittedAfterTime: Optional[Timestamp] = None


class TranslateDocumentResponse(BaseValidatorModel):
    TranslatedDocument: TranslatedDocument
    SourceLanguageCode: str
    TargetLanguageCode: str
    AppliedTerminologies: List[AppliedTerminology]
    AppliedSettings: TranslationSettings
    ResponseMetadata: ResponseMetadata


class TranslateTextResponse(BaseValidatorModel):
    TranslatedText: str
    SourceLanguageCode: str
    TargetLanguageCode: str
    AppliedTerminologies: List[AppliedTerminology]
    AppliedSettings: TranslationSettings
    ResponseMetadata: ResponseMetadata


class TranslateDocumentRequest(BaseValidatorModel):
    Document: Document
    SourceLanguageCode: str
    TargetLanguageCode: str
    TerminologyNames: Optional[List[str]] = None
    Settings: Optional[TranslationSettings] = None


class ImportTerminologyRequest(BaseValidatorModel):
    Name: str
    MergeStrategy: Literal['OVERWRITE']
    TerminologyData: TerminologyData
    Description: Optional[str] = None
    EncryptionKey: Optional[EncryptionKey] = None
    Tags: Optional[List[Tag]] = None


class StartTextTranslationJobRequest(BaseValidatorModel):
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    DataAccessRoleArn: str
    SourceLanguageCode: str
    TargetLanguageCodes: List[str]
    ClientToken: str
    JobName: Optional[str] = None
    TerminologyNames: Optional[List[str]] = None
    ParallelDataNames: Optional[List[str]] = None
    Settings: Optional[TranslationSettings] = None


class TextTranslationJobProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    JobDetails: Optional[JobDetails] = None
    SourceLanguageCode: Optional[str] = None
    TargetLanguageCodes: Optional[List[str]] = None
    TerminologyNames: Optional[List[str]] = None
    ParallelDataNames: Optional[List[str]] = None
    Message: Optional[str] = None
    SubmittedTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfig] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    DataAccessRoleArn: Optional[str] = None
    Settings: Optional[TranslationSettings] = None


class GetTerminologyResponse(BaseValidatorModel):
    TerminologyProperties: TerminologyProperties
    TerminologyDataLocation: TerminologyDataLocation
    AuxiliaryDataLocation: TerminologyDataLocation
    ResponseMetadata: ResponseMetadata


class ImportTerminologyResponse(BaseValidatorModel):
    TerminologyProperties: TerminologyProperties
    AuxiliaryDataLocation: TerminologyDataLocation
    ResponseMetadata: ResponseMetadata


class ListTerminologiesResponse(BaseValidatorModel):
    TerminologyPropertiesList: List[TerminologyProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetParallelDataResponse(BaseValidatorModel):
    ParallelDataProperties: ParallelDataProperties
    DataLocation: ParallelDataDataLocation
    AuxiliaryDataLocation: ParallelDataDataLocation
    LatestUpdateAttemptAuxiliaryDataLocation: ParallelDataDataLocation
    ResponseMetadata: ResponseMetadata


class ListParallelDataResponse(BaseValidatorModel):
    ParallelDataPropertiesList: List[ParallelDataProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTextTranslationJobsRequest(BaseValidatorModel):
    Filter: Optional[TextTranslationJobFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeTextTranslationJobResponse(BaseValidatorModel):
    TextTranslationJobProperties: TextTranslationJobProperties
    ResponseMetadata: ResponseMetadata


class ListTextTranslationJobsResponse(BaseValidatorModel):
    TextTranslationJobPropertiesList: List[TextTranslationJobProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
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
from aws_resource_validator.pydantic_models.translate_constants import *

class TermTypeDef(BaseModel):
    SourceText: Optional[str] = None
    TargetText: Optional[str] = None

class EncryptionKeyTypeDef(BaseModel):
    Type: Literal["KMS"]
    Id: str

class ParallelDataConfigTypeDef(BaseModel):
    S3Uri: Optional[str] = None
    Format: Optional[ParallelDataFormatType] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteParallelDataRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteTerminologyRequestRequestTypeDef(BaseModel):
    Name: str

class DescribeTextTranslationJobRequestRequestTypeDef(BaseModel):
    JobId: str

class GetParallelDataRequestRequestTypeDef(BaseModel):
    Name: str

class ParallelDataDataLocationTypeDef(BaseModel):
    RepositoryType: str
    Location: str

class GetTerminologyRequestRequestTypeDef(BaseModel):
    Name: str
    TerminologyDataFormat: Optional[TerminologyDataFormatType] = None

class TerminologyDataLocationTypeDef(BaseModel):
    RepositoryType: str
    Location: str

class InputDataConfigTypeDef(BaseModel):
    S3Uri: str
    ContentType: str

class JobDetailsTypeDef(BaseModel):
    TranslatedDocumentsCount: Optional[int] = None
    DocumentsWithErrorsCount: Optional[int] = None
    InputDocumentsCount: Optional[int] = None

class LanguageTypeDef(BaseModel):
    LanguageName: str
    LanguageCode: str

class ListLanguagesRequestRequestTypeDef(BaseModel):
    DisplayLanguageCode: Optional[DisplayLanguageCodeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListParallelDataRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTerminologiesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TranslationSettingsTypeDef(BaseModel):
    Formality: Optional[FormalityType] = None
    Profanity: Optional[Literal["MASK"]] = None
    Brevity: Optional[Literal["ON"]] = None

class StopTextTranslationJobRequestRequestTypeDef(BaseModel):
    JobId: str

class TranslatedDocumentTypeDef(BaseModel):
    Content: bytes

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AppliedTerminologyTypeDef(BaseModel):
    Name: Optional[str] = None
    Terms: Optional[List[TermTypeDef]] = None

class DocumentTypeDef(BaseModel):
    Content: BlobTypeDef
    ContentType: str

class TerminologyDataTypeDef(BaseModel):
    File: BlobTypeDef
    Format: TerminologyDataFormatType
    Directionality: Optional[DirectionalityType] = None

class OutputDataConfigTypeDef(BaseModel):
    S3Uri: str
    EncryptionKey: Optional[EncryptionKeyTypeDef] = None

class TerminologyPropertiesTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None
    SourceLanguageCode: Optional[str] = None
    TargetLanguageCodes: Optional[List[str]] = None
    EncryptionKey: Optional[EncryptionKeyTypeDef] = None
    SizeBytes: Optional[int] = None
    TermCount: Optional[int] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    Directionality: Optional[DirectionalityType] = None
    Message: Optional[str] = None
    SkippedTermCount: Optional[int] = None
    Format: Optional[TerminologyDataFormatType] = None

class ParallelDataPropertiesTypeDef(BaseModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[ParallelDataStatusType] = None
    SourceLanguageCode: Optional[str] = None
    TargetLanguageCodes: Optional[List[str]] = None
    ParallelDataConfig: Optional[ParallelDataConfigTypeDef] = None
    Message: Optional[str] = None
    ImportedDataSize: Optional[int] = None
    ImportedRecordCount: Optional[int] = None
    FailedRecordCount: Optional[int] = None
    SkippedRecordCount: Optional[int] = None
    EncryptionKey: Optional[EncryptionKeyTypeDef] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    LatestUpdateAttemptStatus: Optional[ParallelDataStatusType] = None
    LatestUpdateAttemptAt: Optional[datetime] = None

class UpdateParallelDataRequestRequestTypeDef(BaseModel):
    Name: str
    ParallelDataConfig: ParallelDataConfigTypeDef
    ClientToken: str
    Description: Optional[str] = None

class CreateParallelDataRequestRequestTypeDef(BaseModel):
    Name: str
    ParallelDataConfig: ParallelDataConfigTypeDef
    ClientToken: str
    Description: Optional[str] = None
    EncryptionKey: Optional[EncryptionKeyTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateParallelDataResponseTypeDef(BaseModel):
    Name: str
    Status: ParallelDataStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteParallelDataResponseTypeDef(BaseModel):
    Name: str
    Status: ParallelDataStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTextTranslationJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopTextTranslationJobResponseTypeDef(BaseModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateParallelDataResponseTypeDef(BaseModel):
    Name: str
    Status: ParallelDataStatusType
    LatestUpdateAttemptStatus: ParallelDataStatusType
    LatestUpdateAttemptAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListLanguagesResponseTypeDef(BaseModel):
    Languages: List[LanguageTypeDef]
    DisplayLanguageCode: DisplayLanguageCodeType
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTerminologiesRequestListTerminologiesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class TranslateTextRequestRequestTypeDef(BaseModel):
    Text: str
    SourceLanguageCode: str
    TargetLanguageCode: str
    TerminologyNames: Optional[Sequence[str]] = None
    Settings: Optional[TranslationSettingsTypeDef] = None

class TextTranslationJobFilterTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBeforeTime: Optional[TimestampTypeDef] = None
    SubmittedAfterTime: Optional[TimestampTypeDef] = None

class TranslateDocumentResponseTypeDef(BaseModel):
    TranslatedDocument: TranslatedDocumentTypeDef
    SourceLanguageCode: str
    TargetLanguageCode: str
    AppliedTerminologies: List[AppliedTerminologyTypeDef]
    AppliedSettings: TranslationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TranslateTextResponseTypeDef(BaseModel):
    TranslatedText: str
    SourceLanguageCode: str
    TargetLanguageCode: str
    AppliedTerminologies: List[AppliedTerminologyTypeDef]
    AppliedSettings: TranslationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TranslateDocumentRequestRequestTypeDef(BaseModel):
    Document: DocumentTypeDef
    SourceLanguageCode: str
    TargetLanguageCode: str
    TerminologyNames: Optional[Sequence[str]] = None
    Settings: Optional[TranslationSettingsTypeDef] = None

class ImportTerminologyRequestRequestTypeDef(BaseModel):
    Name: str
    MergeStrategy: Literal["OVERWRITE"]
    TerminologyData: TerminologyDataTypeDef
    Description: Optional[str] = None
    EncryptionKey: Optional[EncryptionKeyTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartTextTranslationJobRequestRequestTypeDef(BaseModel):
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    DataAccessRoleArn: str
    SourceLanguageCode: str
    TargetLanguageCodes: Sequence[str]
    ClientToken: str
    JobName: Optional[str] = None
    TerminologyNames: Optional[Sequence[str]] = None
    ParallelDataNames: Optional[Sequence[str]] = None
    Settings: Optional[TranslationSettingsTypeDef] = None

class TextTranslationJobPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    JobDetails: Optional[JobDetailsTypeDef] = None
    SourceLanguageCode: Optional[str] = None
    TargetLanguageCodes: Optional[List[str]] = None
    TerminologyNames: Optional[List[str]] = None
    ParallelDataNames: Optional[List[str]] = None
    Message: Optional[str] = None
    SubmittedTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    Settings: Optional[TranslationSettingsTypeDef] = None

class GetTerminologyResponseTypeDef(BaseModel):
    TerminologyProperties: TerminologyPropertiesTypeDef
    TerminologyDataLocation: TerminologyDataLocationTypeDef
    AuxiliaryDataLocation: TerminologyDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportTerminologyResponseTypeDef(BaseModel):
    TerminologyProperties: TerminologyPropertiesTypeDef
    AuxiliaryDataLocation: TerminologyDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTerminologiesResponseTypeDef(BaseModel):
    TerminologyPropertiesList: List[TerminologyPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetParallelDataResponseTypeDef(BaseModel):
    ParallelDataProperties: ParallelDataPropertiesTypeDef
    DataLocation: ParallelDataDataLocationTypeDef
    AuxiliaryDataLocation: ParallelDataDataLocationTypeDef
    LatestUpdateAttemptAuxiliaryDataLocation: ParallelDataDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListParallelDataResponseTypeDef(BaseModel):
    ParallelDataPropertiesList: List[ParallelDataPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTextTranslationJobsRequestRequestTypeDef(BaseModel):
    Filter: Optional[TextTranslationJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeTextTranslationJobResponseTypeDef(BaseModel):
    TextTranslationJobProperties: TextTranslationJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTextTranslationJobsResponseTypeDef(BaseModel):
    TextTranslationJobPropertiesList: List[TextTranslationJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


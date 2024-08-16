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
from aws_resource_validator.pydantic_models.translate_constants import *

class TermTypeDef(BaseValidatorModel):
    SourceText: Optional[str] = None
    TargetText: Optional[str] = None

class EncryptionKeyTypeDef(BaseValidatorModel):
    Type: Literal["KMS"]
    Id: str

class ParallelDataConfigTypeDef(BaseValidatorModel):
    S3Uri: Optional[str] = None
    Format: Optional[ParallelDataFormatType] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteParallelDataRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteTerminologyRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DescribeTextTranslationJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class GetParallelDataRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class ParallelDataDataLocationTypeDef(BaseValidatorModel):
    RepositoryType: str
    Location: str

class GetTerminologyRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    TerminologyDataFormat: Optional[TerminologyDataFormatType] = None

class TerminologyDataLocationTypeDef(BaseValidatorModel):
    RepositoryType: str
    Location: str

class InputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    ContentType: str

class JobDetailsTypeDef(BaseValidatorModel):
    TranslatedDocumentsCount: Optional[int] = None
    DocumentsWithErrorsCount: Optional[int] = None
    InputDocumentsCount: Optional[int] = None

class LanguageTypeDef(BaseValidatorModel):
    LanguageName: str
    LanguageCode: str

class ListLanguagesRequestRequestTypeDef(BaseValidatorModel):
    DisplayLanguageCode: Optional[DisplayLanguageCodeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListParallelDataRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTerminologiesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class TranslationSettingsTypeDef(BaseValidatorModel):
    Formality: Optional[FormalityType] = None
    Profanity: Optional[Literal["MASK"]] = None
    Brevity: Optional[Literal["ON"]] = None

class StopTextTranslationJobRequestRequestTypeDef(BaseValidatorModel):
    JobId: str

class TranslatedDocumentTypeDef(BaseValidatorModel):
    Content: bytes

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AppliedTerminologyTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Terms: Optional[List[TermTypeDef]] = None

class DocumentTypeDef(BaseValidatorModel):
    Content: BlobTypeDef
    ContentType: str

class TerminologyDataTypeDef(BaseValidatorModel):
    File: BlobTypeDef
    Format: TerminologyDataFormatType
    Directionality: Optional[DirectionalityType] = None

class OutputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    EncryptionKey: Optional[EncryptionKeyTypeDef] = None

class TerminologyPropertiesTypeDef(BaseValidatorModel):
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

class ParallelDataPropertiesTypeDef(BaseValidatorModel):
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

class UpdateParallelDataRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ParallelDataConfig: ParallelDataConfigTypeDef
    ClientToken: str
    Description: Optional[str] = None

class CreateParallelDataRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ParallelDataConfig: ParallelDataConfigTypeDef
    ClientToken: str
    Description: Optional[str] = None
    EncryptionKey: Optional[EncryptionKeyTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateParallelDataResponseTypeDef(BaseValidatorModel):
    Name: str
    Status: ParallelDataStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteParallelDataResponseTypeDef(BaseValidatorModel):
    Name: str
    Status: ParallelDataStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTextTranslationJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class StopTextTranslationJobResponseTypeDef(BaseValidatorModel):
    JobId: str
    JobStatus: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateParallelDataResponseTypeDef(BaseValidatorModel):
    Name: str
    Status: ParallelDataStatusType
    LatestUpdateAttemptStatus: ParallelDataStatusType
    LatestUpdateAttemptAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListLanguagesResponseTypeDef(BaseValidatorModel):
    Languages: List[LanguageTypeDef]
    DisplayLanguageCode: DisplayLanguageCodeType
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTerminologiesRequestListTerminologiesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class TranslateTextRequestRequestTypeDef(BaseValidatorModel):
    Text: str
    SourceLanguageCode: str
    TargetLanguageCode: str
    TerminologyNames: Optional[Sequence[str]] = None
    Settings: Optional[TranslationSettingsTypeDef] = None

class TextTranslationJobFilterTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobStatus: Optional[JobStatusType] = None
    SubmittedBeforeTime: Optional[TimestampTypeDef] = None
    SubmittedAfterTime: Optional[TimestampTypeDef] = None

class TranslateDocumentResponseTypeDef(BaseValidatorModel):
    TranslatedDocument: TranslatedDocumentTypeDef
    SourceLanguageCode: str
    TargetLanguageCode: str
    AppliedTerminologies: List[AppliedTerminologyTypeDef]
    AppliedSettings: TranslationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TranslateTextResponseTypeDef(BaseValidatorModel):
    TranslatedText: str
    SourceLanguageCode: str
    TargetLanguageCode: str
    AppliedTerminologies: List[AppliedTerminologyTypeDef]
    AppliedSettings: TranslationSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TranslateDocumentRequestRequestTypeDef(BaseValidatorModel):
    Document: DocumentTypeDef
    SourceLanguageCode: str
    TargetLanguageCode: str
    TerminologyNames: Optional[Sequence[str]] = None
    Settings: Optional[TranslationSettingsTypeDef] = None

class ImportTerminologyRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    MergeStrategy: Literal["OVERWRITE"]
    TerminologyData: TerminologyDataTypeDef
    Description: Optional[str] = None
    EncryptionKey: Optional[EncryptionKeyTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class StartTextTranslationJobRequestRequestTypeDef(BaseValidatorModel):
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

class TextTranslationJobPropertiesTypeDef(BaseValidatorModel):
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

class GetTerminologyResponseTypeDef(BaseValidatorModel):
    TerminologyProperties: TerminologyPropertiesTypeDef
    TerminologyDataLocation: TerminologyDataLocationTypeDef
    AuxiliaryDataLocation: TerminologyDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportTerminologyResponseTypeDef(BaseValidatorModel):
    TerminologyProperties: TerminologyPropertiesTypeDef
    AuxiliaryDataLocation: TerminologyDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTerminologiesResponseTypeDef(BaseValidatorModel):
    TerminologyPropertiesList: List[TerminologyPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetParallelDataResponseTypeDef(BaseValidatorModel):
    ParallelDataProperties: ParallelDataPropertiesTypeDef
    DataLocation: ParallelDataDataLocationTypeDef
    AuxiliaryDataLocation: ParallelDataDataLocationTypeDef
    LatestUpdateAttemptAuxiliaryDataLocation: ParallelDataDataLocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListParallelDataResponseTypeDef(BaseValidatorModel):
    ParallelDataPropertiesList: List[ParallelDataPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTextTranslationJobsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[TextTranslationJobFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeTextTranslationJobResponseTypeDef(BaseValidatorModel):
    TextTranslationJobProperties: TextTranslationJobPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTextTranslationJobsResponseTypeDef(BaseValidatorModel):
    TextTranslationJobPropertiesList: List[TextTranslationJobPropertiesTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


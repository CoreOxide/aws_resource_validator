from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.transcribe.transcribe_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AbsoluteTimeRange(BaseValidatorModel):
    StartTime: Optional[int] = None
    EndTime: Optional[int] = None
    First: Optional[int] = None
    Last: Optional[int] = None


class CallAnalyticsSkippedFeature(BaseValidatorModel):
    Feature: Optional[Literal['GENERATIVE_SUMMARIZATION']] = None
    ReasonCode: Optional[CallAnalyticsSkippedReasonCodeType] = None
    Message: Optional[str] = None


class ContentRedactionOutput(BaseValidatorModel):
    RedactionType: Literal['PII']
    RedactionOutput: RedactionOutputType
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None


class LanguageIdSettings(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    LanguageModelName: Optional[str] = None


class Summarization(BaseValidatorModel):
    GenerateAbstractiveSummary: bool


class ContentRedaction(BaseValidatorModel):
    RedactionType: Literal['PII']
    RedactionOutput: RedactionOutputType
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None


class ChannelDefinition(BaseValidatorModel):
    ChannelId: Optional[int] = None
    ParticipantRole: Optional[ParticipantRoleType] = None


class Media(BaseValidatorModel):
    MediaFileUri: Optional[str] = None
    RedactedMediaFileUri: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class Transcript(BaseValidatorModel):
    TranscriptFileUri: Optional[str] = None
    RedactedTranscriptFileUri: Optional[str] = None


class ClinicalNoteGenerationSettings(BaseValidatorModel):
    NoteTemplate: Optional[MedicalScribeNoteTemplateType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class InputDataConfig(BaseValidatorModel):
    S3Uri: str
    DataAccessRoleArn: str
    TuningDataS3Uri: Optional[str] = None


class DeleteCallAnalyticsCategoryRequest(BaseValidatorModel):
    CategoryName: str


class DeleteCallAnalyticsJobRequest(BaseValidatorModel):
    CallAnalyticsJobName: str


# This class is the input for the 'delete_language_model' function.
class DeleteLanguageModelRequest(BaseValidatorModel):
    ModelName: str


# This class is the input for the 'delete_medical_scribe_job' function.
class DeleteMedicalScribeJobRequest(BaseValidatorModel):
    MedicalScribeJobName: str


# This class is the input for the 'delete_medical_transcription_job' function.
class DeleteMedicalTranscriptionJobRequest(BaseValidatorModel):
    MedicalTranscriptionJobName: str


# This class is the input for the 'delete_medical_vocabulary' function.
class DeleteMedicalVocabularyRequest(BaseValidatorModel):
    VocabularyName: str


# This class is the input for the 'delete_transcription_job' function.
class DeleteTranscriptionJobRequest(BaseValidatorModel):
    TranscriptionJobName: str


# This class is the input for the 'delete_vocabulary_filter' function.
class DeleteVocabularyFilterRequest(BaseValidatorModel):
    VocabularyFilterName: str


# This class is the input for the 'delete_vocabulary' function.
class DeleteVocabularyRequest(BaseValidatorModel):
    VocabularyName: str


# This class is the input for the 'describe_language_model' function.
class DescribeLanguageModelRequest(BaseValidatorModel):
    ModelName: str


# This class is the input for the 'get_call_analytics_category' function.
class GetCallAnalyticsCategoryRequest(BaseValidatorModel):
    CategoryName: str


# This class is the input for the 'get_call_analytics_job' function.
class GetCallAnalyticsJobRequest(BaseValidatorModel):
    CallAnalyticsJobName: str


# This class is the input for the 'get_medical_scribe_job' function.
class GetMedicalScribeJobRequest(BaseValidatorModel):
    MedicalScribeJobName: str


# This class is the input for the 'get_medical_transcription_job' function.
class GetMedicalTranscriptionJobRequest(BaseValidatorModel):
    MedicalTranscriptionJobName: str


# This class is the input for the 'get_medical_vocabulary' function.
class GetMedicalVocabularyRequest(BaseValidatorModel):
    VocabularyName: str


# This class is the input for the 'get_transcription_job' function.
class GetTranscriptionJobRequest(BaseValidatorModel):
    TranscriptionJobName: str


# This class is the input for the 'get_vocabulary_filter' function.
class GetVocabularyFilterRequest(BaseValidatorModel):
    VocabularyFilterName: str


# This class is the input for the 'get_vocabulary' function.
class GetVocabularyRequest(BaseValidatorModel):
    VocabularyName: str


class RelativeTimeRange(BaseValidatorModel):
    StartPercentage: Optional[int] = None
    EndPercentage: Optional[int] = None
    First: Optional[int] = None
    Last: Optional[int] = None


class JobExecutionSettings(BaseValidatorModel):
    AllowDeferredExecution: Optional[bool] = None
    DataAccessRoleArn: Optional[str] = None


class LanguageCodeItem(BaseValidatorModel):
    LanguageCode: Optional[LanguageCodeType] = None
    DurationInSeconds: Optional[float] = None


# This class is the input for the 'list_call_analytics_categories' function.
class ListCallAnalyticsCategoriesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_call_analytics_jobs' function.
class ListCallAnalyticsJobsRequest(BaseValidatorModel):
    Status: Optional[CallAnalyticsJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_language_models' function.
class ListLanguageModelsRequest(BaseValidatorModel):
    StatusEquals: Optional[ModelStatusType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_medical_scribe_jobs' function.
class ListMedicalScribeJobsRequest(BaseValidatorModel):
    Status: Optional[MedicalScribeJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MedicalScribeJobSummary(BaseValidatorModel):
    MedicalScribeJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[Literal['en-US']] = None
    MedicalScribeJobStatus: Optional[MedicalScribeJobStatusType] = None
    FailureReason: Optional[str] = None


# This class is the input for the 'list_medical_transcription_jobs' function.
class ListMedicalTranscriptionJobsRequest(BaseValidatorModel):
    Status: Optional[TranscriptionJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MedicalTranscriptionJobSummary(BaseValidatorModel):
    MedicalTranscriptionJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[LanguageCodeType] = None
    TranscriptionJobStatus: Optional[TranscriptionJobStatusType] = None
    FailureReason: Optional[str] = None
    OutputLocationType: Optional[OutputLocationTypeType] = None
    Specialty: Optional[Literal['PRIMARYCARE']] = None
    ContentIdentificationType: Optional[Literal['PHI']] = None
    Type: Optional[TypeType] = None


# This class is the input for the 'list_medical_vocabularies' function.
class ListMedicalVocabulariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StateEquals: Optional[VocabularyStateType] = None
    NameContains: Optional[str] = None


class VocabularyInfo(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModifiedTime: Optional[datetime] = None
    VocabularyState: Optional[VocabularyStateType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'list_transcription_jobs' function.
class ListTranscriptionJobsRequest(BaseValidatorModel):
    Status: Optional[TranscriptionJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_vocabularies' function.
class ListVocabulariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StateEquals: Optional[VocabularyStateType] = None
    NameContains: Optional[str] = None


# This class is the input for the 'list_vocabulary_filters' function.
class ListVocabularyFiltersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None


class VocabularyFilterInfo(BaseValidatorModel):
    VocabularyFilterName: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModifiedTime: Optional[datetime] = None


class MedicalScribeChannelDefinition(BaseValidatorModel):
    ChannelId: int
    ParticipantRole: MedicalScribeParticipantRoleType


class MedicalScribeOutput(BaseValidatorModel):
    TranscriptFileUri: str
    ClinicalDocumentUri: str


class MedicalTranscript(BaseValidatorModel):
    TranscriptFileUri: Optional[str] = None


class MedicalTranscriptionSetting(BaseValidatorModel):
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    ShowAlternatives: Optional[bool] = None
    MaxAlternatives: Optional[int] = None
    VocabularyName: Optional[str] = None


class ModelSettings(BaseValidatorModel):
    LanguageModelName: Optional[str] = None


class Settings(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    ShowAlternatives: Optional[bool] = None
    MaxAlternatives: Optional[int] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None


class Subtitles(BaseValidatorModel):
    Formats: Optional[List[SubtitleFormatType]] = None
    OutputStartIndex: Optional[int] = None


class SubtitlesOutput(BaseValidatorModel):
    Formats: Optional[List[SubtitleFormatType]] = None
    SubtitleFileUris: Optional[List[str]] = None
    OutputStartIndex: Optional[int] = None


class ToxicityDetectionSettingsOutput(BaseValidatorModel):
    ToxicityCategories: List[Literal['ALL']]


class ToxicityDetectionSettings(BaseValidatorModel):
    ToxicityCategories: List[Literal['ALL']]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_medical_vocabulary' function.
class UpdateMedicalVocabularyRequest(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str


# This class is the input for the 'update_vocabulary_filter' function.
class UpdateVocabularyFilterRequest(BaseValidatorModel):
    VocabularyFilterName: str
    Words: Optional[List[str]] = None
    VocabularyFilterFileUri: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None


# This class is the input for the 'update_vocabulary' function.
class UpdateVocabularyRequest(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    Phrases: Optional[List[str]] = None
    VocabularyFileUri: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None


class CallAnalyticsJobDetails(BaseValidatorModel):
    Skipped: Optional[List[CallAnalyticsSkippedFeature]] = None


class CallAnalyticsJobSettingsOutput(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    LanguageModelName: Optional[str] = None
    ContentRedaction: Optional[ContentRedactionOutput] = None
    LanguageOptions: Optional[List[LanguageCodeType]] = None
    LanguageIdSettings: Optional[Dict[LanguageCodeType, LanguageIdSettings]] = None
    Summarization: Optional[Summarization] = None


class CallAnalyticsJobSettings(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    LanguageModelName: Optional[str] = None
    ContentRedaction: Optional[ContentRedaction] = None
    LanguageOptions: Optional[List[LanguageCodeType]] = None
    LanguageIdSettings: Optional[Dict[LanguageCodeType, LanguageIdSettings]] = None
    Summarization: Optional[Summarization] = None

ContentRedactionUnion = Union[ContentRedaction, ContentRedactionOutput]


# This class is the input for the 'create_medical_vocabulary' function.
class CreateMedicalVocabularyRequest(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_vocabulary_filter' function.
class CreateVocabularyFilterRequest(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    Words: Optional[List[str]] = None
    VocabularyFilterFileUri: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DataAccessRoleArn: Optional[str] = None


# This class is the input for the 'create_vocabulary' function.
class CreateVocabularyRequest(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    Phrases: Optional[List[str]] = None
    VocabularyFileUri: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DataAccessRoleArn: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class MedicalScribeSettings(BaseValidatorModel):
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    ClinicalNoteGenerationSettings: Optional[ClinicalNoteGenerationSettings] = None


# This class is the output for the 'create_medical_vocabulary' function.
class CreateMedicalVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vocabulary_filter' function.
class CreateVocabularyFilterResponse(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vocabulary' function.
class CreateVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vocabulary_filter' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_medical_vocabulary' function.
class GetMedicalVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_vocabulary_filter' function.
class GetVocabularyFilterResponse(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    DownloadUri: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_vocabulary' function.
class GetVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_medical_vocabulary' function.
class UpdateMedicalVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vocabulary_filter' function.
class UpdateVocabularyFilterResponse(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vocabulary' function.
class UpdateVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_language_model' function.
class CreateLanguageModelRequest(BaseValidatorModel):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfig
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_language_model' function.
class CreateLanguageModelResponse(BaseValidatorModel):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfig
    ModelStatus: ModelStatusType
    ResponseMetadata: ResponseMetadata


class LanguageModel(BaseValidatorModel):
    ModelName: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LanguageCode: Optional[CLMLanguageCodeType] = None
    BaseModelName: Optional[BaseModelNameType] = None
    ModelStatus: Optional[ModelStatusType] = None
    UpgradeAvailability: Optional[bool] = None
    FailureReason: Optional[str] = None
    InputDataConfig: Optional[InputDataConfig] = None


class InterruptionFilter(BaseValidatorModel):
    Threshold: Optional[int] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    AbsoluteTimeRange: Optional[AbsoluteTimeRange] = None
    RelativeTimeRange: Optional[RelativeTimeRange] = None
    Negate: Optional[bool] = None


class NonTalkTimeFilter(BaseValidatorModel):
    Threshold: Optional[int] = None
    AbsoluteTimeRange: Optional[AbsoluteTimeRange] = None
    RelativeTimeRange: Optional[RelativeTimeRange] = None
    Negate: Optional[bool] = None


class SentimentFilterOutput(BaseValidatorModel):
    Sentiments: List[SentimentValueType]
    AbsoluteTimeRange: Optional[AbsoluteTimeRange] = None
    RelativeTimeRange: Optional[RelativeTimeRange] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None


class SentimentFilter(BaseValidatorModel):
    Sentiments: List[SentimentValueType]
    AbsoluteTimeRange: Optional[AbsoluteTimeRange] = None
    RelativeTimeRange: Optional[RelativeTimeRange] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None


class TranscriptFilterOutput(BaseValidatorModel):
    TranscriptFilterType: Literal['EXACT']
    Targets: List[str]
    AbsoluteTimeRange: Optional[AbsoluteTimeRange] = None
    RelativeTimeRange: Optional[RelativeTimeRange] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None


class TranscriptFilter(BaseValidatorModel):
    TranscriptFilterType: Literal['EXACT']
    Targets: List[str]
    AbsoluteTimeRange: Optional[AbsoluteTimeRange] = None
    RelativeTimeRange: Optional[RelativeTimeRange] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None


# This class is the output for the 'list_medical_scribe_jobs' function.
class ListMedicalScribeJobsResponse(BaseValidatorModel):
    Status: MedicalScribeJobStatusType
    MedicalScribeJobSummaries: List[MedicalScribeJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_medical_transcription_jobs' function.
class ListMedicalTranscriptionJobsResponse(BaseValidatorModel):
    Status: TranscriptionJobStatusType
    MedicalTranscriptionJobSummaries: List[MedicalTranscriptionJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_medical_vocabularies' function.
class ListMedicalVocabulariesResponse(BaseValidatorModel):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_vocabularies' function.
class ListVocabulariesResponse(BaseValidatorModel):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_vocabulary_filters' function.
class ListVocabularyFiltersResponse(BaseValidatorModel):
    VocabularyFilters: List[VocabularyFilterInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MedicalTranscriptionJob(BaseValidatorModel):
    MedicalTranscriptionJobName: Optional[str] = None
    TranscriptionJobStatus: Optional[TranscriptionJobStatusType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    Media: Optional[Media] = None
    Transcript: Optional[MedicalTranscript] = None
    StartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    Settings: Optional[MedicalTranscriptionSetting] = None
    ContentIdentificationType: Optional[Literal['PHI']] = None
    Specialty: Optional[Literal['PRIMARYCARE']] = None
    Type: Optional[TypeType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'start_medical_transcription_job' function.
class StartMedicalTranscriptionJobRequest(BaseValidatorModel):
    MedicalTranscriptionJobName: str
    LanguageCode: LanguageCodeType
    Media: Media
    OutputBucketName: str
    Specialty: Literal['PRIMARYCARE']
    Type: TypeType
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    OutputKey: Optional[str] = None
    OutputEncryptionKMSKeyId: Optional[str] = None
    KMSEncryptionContext: Optional[Dict[str, str]] = None
    Settings: Optional[MedicalTranscriptionSetting] = None
    ContentIdentificationType: Optional[Literal['PHI']] = None
    Tags: Optional[List[Tag]] = None


class TranscriptionJobSummary(BaseValidatorModel):
    TranscriptionJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[LanguageCodeType] = None
    TranscriptionJobStatus: Optional[TranscriptionJobStatusType] = None
    FailureReason: Optional[str] = None
    OutputLocationType: Optional[OutputLocationTypeType] = None
    ContentRedaction: Optional[ContentRedactionOutput] = None
    ModelSettings: Optional[ModelSettings] = None
    IdentifyLanguage: Optional[bool] = None
    IdentifyMultipleLanguages: Optional[bool] = None
    IdentifiedLanguageScore: Optional[float] = None
    LanguageCodes: Optional[List[LanguageCodeItem]] = None
    ToxicityDetection: Optional[List[ToxicityDetectionSettingsOutput]] = None


class TranscriptionJob(BaseValidatorModel):
    TranscriptionJobName: Optional[str] = None
    TranscriptionJobStatus: Optional[TranscriptionJobStatusType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    Media: Optional[Media] = None
    Transcript: Optional[Transcript] = None
    StartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    Settings: Optional[Settings] = None
    ModelSettings: Optional[ModelSettings] = None
    JobExecutionSettings: Optional[JobExecutionSettings] = None
    ContentRedaction: Optional[ContentRedactionOutput] = None
    IdentifyLanguage: Optional[bool] = None
    IdentifyMultipleLanguages: Optional[bool] = None
    LanguageOptions: Optional[List[LanguageCodeType]] = None
    IdentifiedLanguageScore: Optional[float] = None
    LanguageCodes: Optional[List[LanguageCodeItem]] = None
    Tags: Optional[List[Tag]] = None
    Subtitles: Optional[SubtitlesOutput] = None
    LanguageIdSettings: Optional[Dict[LanguageCodeType, LanguageIdSettings]] = None
    ToxicityDetection: Optional[List[ToxicityDetectionSettingsOutput]] = None

ToxicityDetectionSettingsUnion = Union[ToxicityDetectionSettings, ToxicityDetectionSettingsOutput]


class CallAnalyticsJobSummary(BaseValidatorModel):
    CallAnalyticsJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[LanguageCodeType] = None
    CallAnalyticsJobStatus: Optional[CallAnalyticsJobStatusType] = None
    CallAnalyticsJobDetails: Optional[CallAnalyticsJobDetails] = None
    FailureReason: Optional[str] = None


class CallAnalyticsJob(BaseValidatorModel):
    CallAnalyticsJobName: Optional[str] = None
    CallAnalyticsJobStatus: Optional[CallAnalyticsJobStatusType] = None
    CallAnalyticsJobDetails: Optional[CallAnalyticsJobDetails] = None
    LanguageCode: Optional[LanguageCodeType] = None
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    Media: Optional[Media] = None
    Transcript: Optional[Transcript] = None
    StartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    IdentifiedLanguageScore: Optional[float] = None
    Settings: Optional[CallAnalyticsJobSettingsOutput] = None
    ChannelDefinitions: Optional[List[ChannelDefinition]] = None
    Tags: Optional[List[Tag]] = None

CallAnalyticsJobSettingsUnion = Union[CallAnalyticsJobSettings, CallAnalyticsJobSettingsOutput]


class MedicalScribeJob(BaseValidatorModel):
    MedicalScribeJobName: Optional[str] = None
    MedicalScribeJobStatus: Optional[MedicalScribeJobStatusType] = None
    LanguageCode: Optional[Literal['en-US']] = None
    Media: Optional[Media] = None
    MedicalScribeOutput: Optional[MedicalScribeOutput] = None
    StartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    Settings: Optional[MedicalScribeSettings] = None
    DataAccessRoleArn: Optional[str] = None
    ChannelDefinitions: Optional[List[MedicalScribeChannelDefinition]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'start_medical_scribe_job' function.
class StartMedicalScribeJobRequest(BaseValidatorModel):
    MedicalScribeJobName: str
    Media: Media
    OutputBucketName: str
    DataAccessRoleArn: str
    Settings: MedicalScribeSettings
    OutputEncryptionKMSKeyId: Optional[str] = None
    KMSEncryptionContext: Optional[Dict[str, str]] = None
    ChannelDefinitions: Optional[List[MedicalScribeChannelDefinition]] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_language_model' function.
class DescribeLanguageModelResponse(BaseValidatorModel):
    LanguageModel: LanguageModel
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_language_models' function.
class ListLanguageModelsResponse(BaseValidatorModel):
    Models: List[LanguageModel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

SentimentFilterUnion = Union[SentimentFilter, SentimentFilterOutput]


class RuleOutput(BaseValidatorModel):
    NonTalkTimeFilter: Optional[NonTalkTimeFilter] = None
    InterruptionFilter: Optional[InterruptionFilter] = None
    TranscriptFilter: Optional[TranscriptFilterOutput] = None
    SentimentFilter: Optional[SentimentFilterOutput] = None

TranscriptFilterUnion = Union[TranscriptFilter, TranscriptFilterOutput]


# This class is the output for the 'get_medical_transcription_job' function.
class GetMedicalTranscriptionJobResponse(BaseValidatorModel):
    MedicalTranscriptionJob: MedicalTranscriptionJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_medical_transcription_job' function.
class StartMedicalTranscriptionJobResponse(BaseValidatorModel):
    MedicalTranscriptionJob: MedicalTranscriptionJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_transcription_jobs' function.
class ListTranscriptionJobsResponse(BaseValidatorModel):
    Status: TranscriptionJobStatusType
    TranscriptionJobSummaries: List[TranscriptionJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_transcription_job' function.
class GetTranscriptionJobResponse(BaseValidatorModel):
    TranscriptionJob: TranscriptionJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_transcription_job' function.
class StartTranscriptionJobResponse(BaseValidatorModel):
    TranscriptionJob: TranscriptionJob
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_transcription_job' function.
class StartTranscriptionJobRequest(BaseValidatorModel):
    TranscriptionJobName: str
    Media: Media
    LanguageCode: Optional[LanguageCodeType] = None
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    OutputBucketName: Optional[str] = None
    OutputKey: Optional[str] = None
    OutputEncryptionKMSKeyId: Optional[str] = None
    KMSEncryptionContext: Optional[Dict[str, str]] = None
    Settings: Optional[Settings] = None
    ModelSettings: Optional[ModelSettings] = None
    JobExecutionSettings: Optional[JobExecutionSettings] = None
    ContentRedaction: Optional[ContentRedactionUnion] = None
    IdentifyLanguage: Optional[bool] = None
    IdentifyMultipleLanguages: Optional[bool] = None
    LanguageOptions: Optional[List[LanguageCodeType]] = None
    Subtitles: Optional[Subtitles] = None
    Tags: Optional[List[Tag]] = None
    LanguageIdSettings: Optional[Dict[LanguageCodeType, LanguageIdSettings]] = None
    ToxicityDetection: Optional[List[ToxicityDetectionSettingsUnion]] = None


# This class is the output for the 'list_call_analytics_jobs' function.
class ListCallAnalyticsJobsResponse(BaseValidatorModel):
    Status: CallAnalyticsJobStatusType
    CallAnalyticsJobSummaries: List[CallAnalyticsJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_call_analytics_job' function.
class GetCallAnalyticsJobResponse(BaseValidatorModel):
    CallAnalyticsJob: CallAnalyticsJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_call_analytics_job' function.
class StartCallAnalyticsJobResponse(BaseValidatorModel):
    CallAnalyticsJob: CallAnalyticsJob
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_call_analytics_job' function.
class StartCallAnalyticsJobRequest(BaseValidatorModel):
    CallAnalyticsJobName: str
    Media: Media
    OutputLocation: Optional[str] = None
    OutputEncryptionKMSKeyId: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    Settings: Optional[CallAnalyticsJobSettingsUnion] = None
    Tags: Optional[List[Tag]] = None
    ChannelDefinitions: Optional[List[ChannelDefinition]] = None


# This class is the output for the 'get_medical_scribe_job' function.
class GetMedicalScribeJobResponse(BaseValidatorModel):
    MedicalScribeJob: MedicalScribeJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_medical_scribe_job' function.
class StartMedicalScribeJobResponse(BaseValidatorModel):
    MedicalScribeJob: MedicalScribeJob
    ResponseMetadata: ResponseMetadata


class CategoryProperties(BaseValidatorModel):
    CategoryName: Optional[str] = None
    Rules: Optional[List[RuleOutput]] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None
    InputType: Optional[InputTypeType] = None


class Rule(BaseValidatorModel):
    NonTalkTimeFilter: Optional[NonTalkTimeFilter] = None
    InterruptionFilter: Optional[InterruptionFilter] = None
    TranscriptFilter: Optional[TranscriptFilterUnion] = None
    SentimentFilter: Optional[SentimentFilterUnion] = None


# This class is the output for the 'create_call_analytics_category' function.
class CreateCallAnalyticsCategoryResponse(BaseValidatorModel):
    CategoryProperties: CategoryProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_call_analytics_category' function.
class GetCallAnalyticsCategoryResponse(BaseValidatorModel):
    CategoryProperties: CategoryProperties
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_call_analytics_categories' function.
class ListCallAnalyticsCategoriesResponse(BaseValidatorModel):
    Categories: List[CategoryProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_call_analytics_category' function.
class UpdateCallAnalyticsCategoryResponse(BaseValidatorModel):
    CategoryProperties: CategoryProperties
    ResponseMetadata: ResponseMetadata

RuleUnion = Union[Rule, RuleOutput]


# This class is the input for the 'create_call_analytics_category' function.
class CreateCallAnalyticsCategoryRequest(BaseValidatorModel):
    CategoryName: str
    Rules: List[RuleUnion]
    Tags: Optional[List[Tag]] = None
    InputType: Optional[InputTypeType] = None


# This class is the input for the 'update_call_analytics_category' function.
class UpdateCallAnalyticsCategoryRequest(BaseValidatorModel):
    CategoryName: str
    Rules: List[RuleUnion]
    InputType: Optional[InputTypeType] = None
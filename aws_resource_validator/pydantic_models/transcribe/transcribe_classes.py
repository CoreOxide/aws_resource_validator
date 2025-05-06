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


class DeleteLanguageModelRequest(BaseValidatorModel):
    ModelName: str


class DeleteMedicalScribeJobRequest(BaseValidatorModel):
    MedicalScribeJobName: str


class DeleteMedicalTranscriptionJobRequest(BaseValidatorModel):
    MedicalTranscriptionJobName: str


class DeleteMedicalVocabularyRequest(BaseValidatorModel):
    VocabularyName: str


class DeleteTranscriptionJobRequest(BaseValidatorModel):
    TranscriptionJobName: str


class DeleteVocabularyFilterRequest(BaseValidatorModel):
    VocabularyFilterName: str


class DeleteVocabularyRequest(BaseValidatorModel):
    VocabularyName: str


class DescribeLanguageModelRequest(BaseValidatorModel):
    ModelName: str


class GetCallAnalyticsCategoryRequest(BaseValidatorModel):
    CategoryName: str


class GetCallAnalyticsJobRequest(BaseValidatorModel):
    CallAnalyticsJobName: str


class GetMedicalScribeJobRequest(BaseValidatorModel):
    MedicalScribeJobName: str


class GetMedicalTranscriptionJobRequest(BaseValidatorModel):
    MedicalTranscriptionJobName: str


class GetMedicalVocabularyRequest(BaseValidatorModel):
    VocabularyName: str


class GetTranscriptionJobRequest(BaseValidatorModel):
    TranscriptionJobName: str


class GetVocabularyFilterRequest(BaseValidatorModel):
    VocabularyFilterName: str


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


class ListCallAnalyticsCategoriesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCallAnalyticsJobsRequest(BaseValidatorModel):
    Status: Optional[CallAnalyticsJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLanguageModelsRequest(BaseValidatorModel):
    StatusEquals: Optional[ModelStatusType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


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


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class ListTranscriptionJobsRequest(BaseValidatorModel):
    Status: Optional[TranscriptionJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListVocabulariesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StateEquals: Optional[VocabularyStateType] = None
    NameContains: Optional[str] = None


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


class UpdateMedicalVocabularyRequest(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str


class UpdateVocabularyFilterRequest(BaseValidatorModel):
    VocabularyFilterName: str
    Words: Optional[List[str]] = None
    VocabularyFilterFileUri: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None


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


class CreateMedicalVocabularyRequest(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str
    Tags: Optional[List[Tag]] = None


class CreateVocabularyFilterRequest(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    Words: Optional[List[str]] = None
    VocabularyFilterFileUri: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DataAccessRoleArn: Optional[str] = None


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


class CreateMedicalVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadata


class CreateVocabularyFilterResponse(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class CreateVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetMedicalVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadata


class GetVocabularyFilterResponse(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    DownloadUri: str
    ResponseMetadata: ResponseMetadata


class GetVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateMedicalVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadata


class UpdateVocabularyFilterResponse(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateVocabularyResponse(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadata


class CreateLanguageModelRequest(BaseValidatorModel):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfig
    Tags: Optional[List[Tag]] = None


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


class ListMedicalScribeJobsResponse(BaseValidatorModel):
    Status: MedicalScribeJobStatusType
    MedicalScribeJobSummaries: List[MedicalScribeJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMedicalTranscriptionJobsResponse(BaseValidatorModel):
    Status: TranscriptionJobStatusType
    MedicalTranscriptionJobSummaries: List[MedicalTranscriptionJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMedicalVocabulariesResponse(BaseValidatorModel):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListVocabulariesResponse(BaseValidatorModel):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class DescribeLanguageModelResponse(BaseValidatorModel):
    LanguageModel: LanguageModel
    ResponseMetadata: ResponseMetadata


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


class GetMedicalTranscriptionJobResponse(BaseValidatorModel):
    MedicalTranscriptionJob: MedicalTranscriptionJob
    ResponseMetadata: ResponseMetadata


class StartMedicalTranscriptionJobResponse(BaseValidatorModel):
    MedicalTranscriptionJob: MedicalTranscriptionJob
    ResponseMetadata: ResponseMetadata


class ListTranscriptionJobsResponse(BaseValidatorModel):
    Status: TranscriptionJobStatusType
    TranscriptionJobSummaries: List[TranscriptionJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetTranscriptionJobResponse(BaseValidatorModel):
    TranscriptionJob: TranscriptionJob
    ResponseMetadata: ResponseMetadata


class StartTranscriptionJobResponse(BaseValidatorModel):
    TranscriptionJob: TranscriptionJob
    ResponseMetadata: ResponseMetadata


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


class ListCallAnalyticsJobsResponse(BaseValidatorModel):
    Status: CallAnalyticsJobStatusType
    CallAnalyticsJobSummaries: List[CallAnalyticsJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCallAnalyticsJobResponse(BaseValidatorModel):
    CallAnalyticsJob: CallAnalyticsJob
    ResponseMetadata: ResponseMetadata


class StartCallAnalyticsJobResponse(BaseValidatorModel):
    CallAnalyticsJob: CallAnalyticsJob
    ResponseMetadata: ResponseMetadata


class StartCallAnalyticsJobRequest(BaseValidatorModel):
    CallAnalyticsJobName: str
    Media: Media
    OutputLocation: Optional[str] = None
    OutputEncryptionKMSKeyId: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    Settings: Optional[CallAnalyticsJobSettingsUnion] = None
    Tags: Optional[List[Tag]] = None
    ChannelDefinitions: Optional[List[ChannelDefinition]] = None


class GetMedicalScribeJobResponse(BaseValidatorModel):
    MedicalScribeJob: MedicalScribeJob
    ResponseMetadata: ResponseMetadata


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


class CreateCallAnalyticsCategoryResponse(BaseValidatorModel):
    CategoryProperties: CategoryProperties
    ResponseMetadata: ResponseMetadata


class GetCallAnalyticsCategoryResponse(BaseValidatorModel):
    CategoryProperties: CategoryProperties
    ResponseMetadata: ResponseMetadata


class ListCallAnalyticsCategoriesResponse(BaseValidatorModel):
    Categories: List[CategoryProperties]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateCallAnalyticsCategoryResponse(BaseValidatorModel):
    CategoryProperties: CategoryProperties
    ResponseMetadata: ResponseMetadata

RuleUnion = Union[Rule, RuleOutput]


class CreateCallAnalyticsCategoryRequest(BaseValidatorModel):
    CategoryName: str
    Rules: List[RuleUnion]
    Tags: Optional[List[Tag]] = None
    InputType: Optional[InputTypeType] = None


class UpdateCallAnalyticsCategoryRequest(BaseValidatorModel):
    CategoryName: str
    Rules: List[RuleUnion]
    InputType: Optional[InputTypeType] = None
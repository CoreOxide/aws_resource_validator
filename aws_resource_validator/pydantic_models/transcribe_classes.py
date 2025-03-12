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
from aws_resource_validator.pydantic_models.transcribe_constants import *

class AbsoluteTimeRangeTypeDef(BaseValidatorModel):
    StartTime: Optional[int] = None
    EndTime: Optional[int] = None
    First: Optional[int] = None
    Last: Optional[int] = None


class CallAnalyticsSkippedFeatureTypeDef(BaseValidatorModel):
    Feature: Optional[Literal["GENERATIVE_SUMMARIZATION"]] = None
    ReasonCode: Optional[CallAnalyticsSkippedReasonCodeType] = None
    Message: Optional[str] = None


class ContentRedactionOutputTypeDef(BaseValidatorModel):
    RedactionType: Literal["PII"]
    RedactionOutput: RedactionOutputType
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None


class LanguageIdSettingsTypeDef(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    LanguageModelName: Optional[str] = None


class SummarizationTypeDef(BaseValidatorModel):
    GenerateAbstractiveSummary: bool


class ContentRedactionTypeDef(BaseValidatorModel):
    RedactionType: Literal["PII"]
    RedactionOutput: RedactionOutputType
    PiiEntityTypes: Optional[Sequence[PiiEntityTypeType]] = None


class ChannelDefinitionTypeDef(BaseValidatorModel):
    ChannelId: Optional[int] = None
    ParticipantRole: Optional[ParticipantRoleType] = None


class MediaTypeDef(BaseValidatorModel):
    MediaFileUri: Optional[str] = None
    RedactedMediaFileUri: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class TranscriptTypeDef(BaseValidatorModel):
    TranscriptFileUri: Optional[str] = None
    RedactedTranscriptFileUri: Optional[str] = None


class ClinicalNoteGenerationSettingsTypeDef(BaseValidatorModel):
    NoteTemplate: Optional[MedicalScribeNoteTemplateType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class InputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    DataAccessRoleArn: str
    TuningDataS3Uri: Optional[str] = None


class DeleteCallAnalyticsCategoryRequestTypeDef(BaseValidatorModel):
    CategoryName: str


class DeleteCallAnalyticsJobRequestTypeDef(BaseValidatorModel):
    CallAnalyticsJobName: str


class DeleteLanguageModelRequestTypeDef(BaseValidatorModel):
    ModelName: str


class DeleteMedicalScribeJobRequestTypeDef(BaseValidatorModel):
    MedicalScribeJobName: str


class DeleteMedicalTranscriptionJobRequestTypeDef(BaseValidatorModel):
    MedicalTranscriptionJobName: str


class DeleteMedicalVocabularyRequestTypeDef(BaseValidatorModel):
    VocabularyName: str


class DeleteTranscriptionJobRequestTypeDef(BaseValidatorModel):
    TranscriptionJobName: str


class DeleteVocabularyFilterRequestTypeDef(BaseValidatorModel):
    VocabularyFilterName: str


class DeleteVocabularyRequestTypeDef(BaseValidatorModel):
    VocabularyName: str


class DescribeLanguageModelRequestTypeDef(BaseValidatorModel):
    ModelName: str


class GetCallAnalyticsCategoryRequestTypeDef(BaseValidatorModel):
    CategoryName: str


class GetCallAnalyticsJobRequestTypeDef(BaseValidatorModel):
    CallAnalyticsJobName: str


class GetMedicalScribeJobRequestTypeDef(BaseValidatorModel):
    MedicalScribeJobName: str


class GetMedicalTranscriptionJobRequestTypeDef(BaseValidatorModel):
    MedicalTranscriptionJobName: str


class GetMedicalVocabularyRequestTypeDef(BaseValidatorModel):
    VocabularyName: str


class GetTranscriptionJobRequestTypeDef(BaseValidatorModel):
    TranscriptionJobName: str


class GetVocabularyFilterRequestTypeDef(BaseValidatorModel):
    VocabularyFilterName: str


class GetVocabularyRequestTypeDef(BaseValidatorModel):
    VocabularyName: str


class RelativeTimeRangeTypeDef(BaseValidatorModel):
    StartPercentage: Optional[int] = None
    EndPercentage: Optional[int] = None
    First: Optional[int] = None
    Last: Optional[int] = None


class JobExecutionSettingsTypeDef(BaseValidatorModel):
    AllowDeferredExecution: Optional[bool] = None
    DataAccessRoleArn: Optional[str] = None


class LanguageCodeItemTypeDef(BaseValidatorModel):
    LanguageCode: Optional[LanguageCodeType] = None
    DurationInSeconds: Optional[float] = None


class ListCallAnalyticsCategoriesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCallAnalyticsJobsRequestTypeDef(BaseValidatorModel):
    Status: Optional[CallAnalyticsJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLanguageModelsRequestTypeDef(BaseValidatorModel):
    StatusEquals: Optional[ModelStatusType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMedicalScribeJobsRequestTypeDef(BaseValidatorModel):
    Status: Optional[MedicalScribeJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MedicalScribeJobSummaryTypeDef(BaseValidatorModel):
    MedicalScribeJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[Literal["en-US"]] = None
    MedicalScribeJobStatus: Optional[MedicalScribeJobStatusType] = None
    FailureReason: Optional[str] = None


class ListMedicalTranscriptionJobsRequestTypeDef(BaseValidatorModel):
    Status: Optional[TranscriptionJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMedicalVocabulariesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StateEquals: Optional[VocabularyStateType] = None
    NameContains: Optional[str] = None


class VocabularyInfoTypeDef(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModifiedTime: Optional[datetime] = None
    VocabularyState: Optional[VocabularyStateType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListTranscriptionJobsRequestTypeDef(BaseValidatorModel):
    Status: Optional[TranscriptionJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListVocabulariesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StateEquals: Optional[VocabularyStateType] = None
    NameContains: Optional[str] = None


class ListVocabularyFiltersRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None


class VocabularyFilterInfoTypeDef(BaseValidatorModel):
    VocabularyFilterName: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModifiedTime: Optional[datetime] = None


class MedicalScribeChannelDefinitionTypeDef(BaseValidatorModel):
    ChannelId: int
    ParticipantRole: MedicalScribeParticipantRoleType


class MedicalScribeOutputTypeDef(BaseValidatorModel):
    TranscriptFileUri: str
    ClinicalDocumentUri: str


class MedicalTranscriptTypeDef(BaseValidatorModel):
    TranscriptFileUri: Optional[str] = None


class MedicalTranscriptionSettingTypeDef(BaseValidatorModel):
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    ShowAlternatives: Optional[bool] = None
    MaxAlternatives: Optional[int] = None
    VocabularyName: Optional[str] = None


class ModelSettingsTypeDef(BaseValidatorModel):
    LanguageModelName: Optional[str] = None


class SettingsTypeDef(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    ShowAlternatives: Optional[bool] = None
    MaxAlternatives: Optional[int] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None


class SubtitlesTypeDef(BaseValidatorModel):
    Formats: Optional[Sequence[SubtitleFormatType]] = None
    OutputStartIndex: Optional[int] = None


class SubtitlesOutputTypeDef(BaseValidatorModel):
    Formats: Optional[List[SubtitleFormatType]] = None
    SubtitleFileUris: Optional[List[str]] = None
    OutputStartIndex: Optional[int] = None


class ToxicityDetectionSettingsOutputTypeDef(BaseValidatorModel):
    ToxicityCategories: List[Literal["ALL"]]


class ToxicityDetectionSettingsTypeDef(BaseValidatorModel):
    ToxicityCategories: Sequence[Literal["ALL"]]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateMedicalVocabularyRequestTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str


class UpdateVocabularyFilterRequestTypeDef(BaseValidatorModel):
    VocabularyFilterName: str
    Words: Optional[Sequence[str]] = None
    VocabularyFilterFileUri: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None


class UpdateVocabularyRequestTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    Phrases: Optional[Sequence[str]] = None
    VocabularyFileUri: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None


class CallAnalyticsJobDetailsTypeDef(BaseValidatorModel):
    Skipped: Optional[List[CallAnalyticsSkippedFeatureTypeDef]] = None


class CallAnalyticsJobSettingsOutputTypeDef(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    LanguageModelName: Optional[str] = None
    ContentRedaction: Optional[ContentRedactionOutputTypeDef] = None
    LanguageOptions: Optional[List[LanguageCodeType]] = None
    LanguageIdSettings: Optional[Dict[LanguageCodeType, LanguageIdSettingsTypeDef]] = None
    Summarization: Optional[SummarizationTypeDef] = None


class CallAnalyticsJobSettingsTypeDef(BaseValidatorModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    LanguageModelName: Optional[str] = None
    ContentRedaction: Optional[ContentRedactionTypeDef] = None
    LanguageOptions: Optional[Sequence[LanguageCodeType]] = None
    LanguageIdSettings: Optional[Mapping[LanguageCodeType, LanguageIdSettingsTypeDef]] = None
    Summarization: Optional[SummarizationTypeDef] = None


class CreateMedicalVocabularyRequestTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateVocabularyFilterRequestTypeDef(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    Words: Optional[Sequence[str]] = None
    VocabularyFilterFileUri: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataAccessRoleArn: Optional[str] = None


class CreateVocabularyRequestTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    Phrases: Optional[Sequence[str]] = None
    VocabularyFileUri: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataAccessRoleArn: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class MedicalScribeSettingsTypeDef(BaseValidatorModel):
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    ClinicalNoteGenerationSettings: Optional[ClinicalNoteGenerationSettingsTypeDef] = None


class CreateMedicalVocabularyResponseTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVocabularyFilterResponseTypeDef(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateVocabularyResponseTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetMedicalVocabularyResponseTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetVocabularyFilterResponseTypeDef(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetVocabularyResponseTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMedicalVocabularyResponseTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVocabularyFilterResponseTypeDef(BaseValidatorModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVocabularyResponseTypeDef(BaseValidatorModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLanguageModelRequestTypeDef(BaseValidatorModel):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfigTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateLanguageModelResponseTypeDef(BaseValidatorModel):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfigTypeDef
    ModelStatus: ModelStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class LanguageModelTypeDef(BaseValidatorModel):
    ModelName: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LanguageCode: Optional[CLMLanguageCodeType] = None
    BaseModelName: Optional[BaseModelNameType] = None
    ModelStatus: Optional[ModelStatusType] = None
    UpgradeAvailability: Optional[bool] = None
    FailureReason: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None


class InterruptionFilterTypeDef(BaseValidatorModel):
    Threshold: Optional[int] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    Negate: Optional[bool] = None


class NonTalkTimeFilterTypeDef(BaseValidatorModel):
    Threshold: Optional[int] = None
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    Negate: Optional[bool] = None


class SentimentFilterOutputTypeDef(BaseValidatorModel):
    Sentiments: List[SentimentValueType]
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None


class SentimentFilterTypeDef(BaseValidatorModel):
    Sentiments: Sequence[SentimentValueType]
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None


class TranscriptFilterOutputTypeDef(BaseValidatorModel):
    TranscriptFilterType: Literal["EXACT"]
    Targets: List[str]
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None


class TranscriptFilterTypeDef(BaseValidatorModel):
    TranscriptFilterType: Literal["EXACT"]
    Targets: Sequence[str]
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None


class ListMedicalScribeJobsResponseTypeDef(BaseValidatorModel):
    Status: MedicalScribeJobStatusType
    MedicalScribeJobSummaries: List[MedicalScribeJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MedicalTranscriptionJobSummaryTypeDef(BaseValidatorModel):
    pass


class ListMedicalTranscriptionJobsResponseTypeDef(BaseValidatorModel):
    Status: TranscriptionJobStatusType
    MedicalTranscriptionJobSummaries: List[MedicalTranscriptionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMedicalVocabulariesResponseTypeDef(BaseValidatorModel):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListVocabulariesResponseTypeDef(BaseValidatorModel):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListVocabularyFiltersResponseTypeDef(BaseValidatorModel):
    VocabularyFilters: List[VocabularyFilterInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TranscriptionJobSummaryTypeDef(BaseValidatorModel):
    TranscriptionJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[LanguageCodeType] = None
    TranscriptionJobStatus: Optional[TranscriptionJobStatusType] = None
    FailureReason: Optional[str] = None
    OutputLocationType: Optional[OutputLocationTypeType] = None
    ContentRedaction: Optional[ContentRedactionOutputTypeDef] = None
    ModelSettings: Optional[ModelSettingsTypeDef] = None
    IdentifyLanguage: Optional[bool] = None
    IdentifyMultipleLanguages: Optional[bool] = None
    IdentifiedLanguageScore: Optional[float] = None
    LanguageCodes: Optional[List[LanguageCodeItemTypeDef]] = None
    ToxicityDetection: Optional[List[ToxicityDetectionSettingsOutputTypeDef]] = None


class TranscriptionJobTypeDef(BaseValidatorModel):
    TranscriptionJobName: Optional[str] = None
    TranscriptionJobStatus: Optional[TranscriptionJobStatusType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    Media: Optional[MediaTypeDef] = None
    Transcript: Optional[TranscriptTypeDef] = None
    StartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    Settings: Optional[SettingsTypeDef] = None
    ModelSettings: Optional[ModelSettingsTypeDef] = None
    JobExecutionSettings: Optional[JobExecutionSettingsTypeDef] = None
    ContentRedaction: Optional[ContentRedactionOutputTypeDef] = None
    IdentifyLanguage: Optional[bool] = None
    IdentifyMultipleLanguages: Optional[bool] = None
    LanguageOptions: Optional[List[LanguageCodeType]] = None
    IdentifiedLanguageScore: Optional[float] = None
    LanguageCodes: Optional[List[LanguageCodeItemTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    Subtitles: Optional[SubtitlesOutputTypeDef] = None
    LanguageIdSettings: Optional[Dict[LanguageCodeType, LanguageIdSettingsTypeDef]] = None
    ToxicityDetection: Optional[List[ToxicityDetectionSettingsOutputTypeDef]] = None


class CallAnalyticsJobSummaryTypeDef(BaseValidatorModel):
    CallAnalyticsJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[LanguageCodeType] = None
    CallAnalyticsJobStatus: Optional[CallAnalyticsJobStatusType] = None
    CallAnalyticsJobDetails: Optional[CallAnalyticsJobDetailsTypeDef] = None
    FailureReason: Optional[str] = None


class CallAnalyticsJobTypeDef(BaseValidatorModel):
    CallAnalyticsJobName: Optional[str] = None
    CallAnalyticsJobStatus: Optional[CallAnalyticsJobStatusType] = None
    CallAnalyticsJobDetails: Optional[CallAnalyticsJobDetailsTypeDef] = None
    LanguageCode: Optional[LanguageCodeType] = None
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    Media: Optional[MediaTypeDef] = None
    Transcript: Optional[TranscriptTypeDef] = None
    StartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    IdentifiedLanguageScore: Optional[float] = None
    Settings: Optional[CallAnalyticsJobSettingsOutputTypeDef] = None
    ChannelDefinitions: Optional[List[ChannelDefinitionTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None


class MedicalScribeJobTypeDef(BaseValidatorModel):
    MedicalScribeJobName: Optional[str] = None
    MedicalScribeJobStatus: Optional[MedicalScribeJobStatusType] = None
    LanguageCode: Optional[Literal["en-US"]] = None
    Media: Optional[MediaTypeDef] = None
    MedicalScribeOutput: Optional[MedicalScribeOutputTypeDef] = None
    StartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    Settings: Optional[MedicalScribeSettingsTypeDef] = None
    DataAccessRoleArn: Optional[str] = None
    ChannelDefinitions: Optional[List[MedicalScribeChannelDefinitionTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None


class StartMedicalScribeJobRequestTypeDef(BaseValidatorModel):
    MedicalScribeJobName: str
    Media: MediaTypeDef
    OutputBucketName: str
    DataAccessRoleArn: str
    Settings: MedicalScribeSettingsTypeDef
    OutputEncryptionKMSKeyId: Optional[str] = None
    KMSEncryptionContext: Optional[Mapping[str, str]] = None
    ChannelDefinitions: Optional[Sequence[MedicalScribeChannelDefinitionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DescribeLanguageModelResponseTypeDef(BaseValidatorModel):
    LanguageModel: LanguageModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLanguageModelsResponseTypeDef(BaseValidatorModel):
    Models: List[LanguageModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RuleOutputTypeDef(BaseValidatorModel):
    NonTalkTimeFilter: Optional[NonTalkTimeFilterTypeDef] = None
    InterruptionFilter: Optional[InterruptionFilterTypeDef] = None
    TranscriptFilter: Optional[TranscriptFilterOutputTypeDef] = None
    SentimentFilter: Optional[SentimentFilterOutputTypeDef] = None


class MedicalTranscriptionJobTypeDef(BaseValidatorModel):
    pass


class GetMedicalTranscriptionJobResponseTypeDef(BaseValidatorModel):
    MedicalTranscriptionJob: MedicalTranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartMedicalTranscriptionJobResponseTypeDef(BaseValidatorModel):
    MedicalTranscriptionJob: MedicalTranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTranscriptionJobsResponseTypeDef(BaseValidatorModel):
    Status: TranscriptionJobStatusType
    TranscriptionJobSummaries: List[TranscriptionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetTranscriptionJobResponseTypeDef(BaseValidatorModel):
    TranscriptionJob: TranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartTranscriptionJobResponseTypeDef(BaseValidatorModel):
    TranscriptionJob: TranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ContentRedactionUnionTypeDef(BaseValidatorModel):
    pass


class ToxicityDetectionSettingsUnionTypeDef(BaseValidatorModel):
    pass


class StartTranscriptionJobRequestTypeDef(BaseValidatorModel):
    TranscriptionJobName: str
    Media: MediaTypeDef
    LanguageCode: Optional[LanguageCodeType] = None
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    OutputBucketName: Optional[str] = None
    OutputKey: Optional[str] = None
    OutputEncryptionKMSKeyId: Optional[str] = None
    KMSEncryptionContext: Optional[Mapping[str, str]] = None
    Settings: Optional[SettingsTypeDef] = None
    ModelSettings: Optional[ModelSettingsTypeDef] = None
    JobExecutionSettings: Optional[JobExecutionSettingsTypeDef] = None
    ContentRedaction: Optional[ContentRedactionUnionTypeDef] = None
    IdentifyLanguage: Optional[bool] = None
    IdentifyMultipleLanguages: Optional[bool] = None
    LanguageOptions: Optional[Sequence[LanguageCodeType]] = None
    Subtitles: Optional[SubtitlesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    LanguageIdSettings: Optional[Mapping[LanguageCodeType, LanguageIdSettingsTypeDef]] = None
    ToxicityDetection: Optional[Sequence[ToxicityDetectionSettingsUnionTypeDef]] = None


class ListCallAnalyticsJobsResponseTypeDef(BaseValidatorModel):
    Status: CallAnalyticsJobStatusType
    CallAnalyticsJobSummaries: List[CallAnalyticsJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetCallAnalyticsJobResponseTypeDef(BaseValidatorModel):
    CallAnalyticsJob: CallAnalyticsJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartCallAnalyticsJobResponseTypeDef(BaseValidatorModel):
    CallAnalyticsJob: CallAnalyticsJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CallAnalyticsJobSettingsUnionTypeDef(BaseValidatorModel):
    pass


class StartCallAnalyticsJobRequestTypeDef(BaseValidatorModel):
    CallAnalyticsJobName: str
    Media: MediaTypeDef
    OutputLocation: Optional[str] = None
    OutputEncryptionKMSKeyId: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    Settings: Optional[CallAnalyticsJobSettingsUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ChannelDefinitions: Optional[Sequence[ChannelDefinitionTypeDef]] = None


class GetMedicalScribeJobResponseTypeDef(BaseValidatorModel):
    MedicalScribeJob: MedicalScribeJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartMedicalScribeJobResponseTypeDef(BaseValidatorModel):
    MedicalScribeJob: MedicalScribeJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CategoryPropertiesTypeDef(BaseValidatorModel):
    CategoryName: Optional[str] = None
    Rules: Optional[List[RuleOutputTypeDef]] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None
    InputType: Optional[InputTypeType] = None


class SentimentFilterUnionTypeDef(BaseValidatorModel):
    pass


class TranscriptFilterUnionTypeDef(BaseValidatorModel):
    pass


class RuleTypeDef(BaseValidatorModel):
    NonTalkTimeFilter: Optional[NonTalkTimeFilterTypeDef] = None
    InterruptionFilter: Optional[InterruptionFilterTypeDef] = None
    TranscriptFilter: Optional[TranscriptFilterUnionTypeDef] = None
    SentimentFilter: Optional[SentimentFilterUnionTypeDef] = None


class CreateCallAnalyticsCategoryResponseTypeDef(BaseValidatorModel):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCallAnalyticsCategoryResponseTypeDef(BaseValidatorModel):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCallAnalyticsCategoriesResponseTypeDef(BaseValidatorModel):
    Categories: List[CategoryPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateCallAnalyticsCategoryResponseTypeDef(BaseValidatorModel):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RuleUnionTypeDef(BaseValidatorModel):
    pass


class CreateCallAnalyticsCategoryRequestTypeDef(BaseValidatorModel):
    CategoryName: str
    Rules: Sequence[RuleUnionTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None
    InputType: Optional[InputTypeType] = None


class UpdateCallAnalyticsCategoryRequestTypeDef(BaseValidatorModel):
    CategoryName: str
    Rules: Sequence[RuleUnionTypeDef]
    InputType: Optional[InputTypeType] = None



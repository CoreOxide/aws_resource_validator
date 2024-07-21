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
from aws_resource_validator.pydantic_models.transcribe_constants import *

class AbsoluteTimeRangeTypeDef(BaseModel):
    StartTime: Optional[int] = None
    EndTime: Optional[int] = None
    First: Optional[int] = None
    Last: Optional[int] = None

class CallAnalyticsSkippedFeatureTypeDef(BaseModel):
    Feature: Optional[Literal["GENERATIVE_SUMMARIZATION"]] = None
    ReasonCode: Optional[CallAnalyticsSkippedReasonCodeType] = None
    Message: Optional[str] = None

class ContentRedactionOutputTypeDef(BaseModel):
    RedactionType: Literal["PII"]
    RedactionOutput: RedactionOutputType
    PiiEntityTypes: Optional[List[PiiEntityTypeType]] = None

class LanguageIdSettingsTypeDef(BaseModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    LanguageModelName: Optional[str] = None

class SummarizationTypeDef(BaseModel):
    GenerateAbstractiveSummary: bool

class ContentRedactionTypeDef(BaseModel):
    RedactionType: Literal["PII"]
    RedactionOutput: RedactionOutputType
    PiiEntityTypes: Optional[Sequence[PiiEntityTypeType]] = None

class ChannelDefinitionTypeDef(BaseModel):
    ChannelId: Optional[int] = None
    ParticipantRole: Optional[ParticipantRoleType] = None

class MediaTypeDef(BaseModel):
    MediaFileUri: Optional[str] = None
    RedactedMediaFileUri: Optional[str] = None

class TranscriptTypeDef(BaseModel):
    TranscriptFileUri: Optional[str] = None
    RedactedTranscriptFileUri: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class InputDataConfigTypeDef(BaseModel):
    S3Uri: str
    DataAccessRoleArn: str
    TuningDataS3Uri: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class DeleteCallAnalyticsCategoryRequestRequestTypeDef(BaseModel):
    CategoryName: str

class DeleteCallAnalyticsJobRequestRequestTypeDef(BaseModel):
    CallAnalyticsJobName: str

class DeleteLanguageModelRequestRequestTypeDef(BaseModel):
    ModelName: str

class DeleteMedicalScribeJobRequestRequestTypeDef(BaseModel):
    MedicalScribeJobName: str

class DeleteMedicalTranscriptionJobRequestRequestTypeDef(BaseModel):
    MedicalTranscriptionJobName: str

class DeleteMedicalVocabularyRequestRequestTypeDef(BaseModel):
    VocabularyName: str

class DeleteTranscriptionJobRequestRequestTypeDef(BaseModel):
    TranscriptionJobName: str

class DeleteVocabularyFilterRequestRequestTypeDef(BaseModel):
    VocabularyFilterName: str

class DeleteVocabularyRequestRequestTypeDef(BaseModel):
    VocabularyName: str

class DescribeLanguageModelRequestRequestTypeDef(BaseModel):
    ModelName: str

class GetCallAnalyticsCategoryRequestRequestTypeDef(BaseModel):
    CategoryName: str

class GetCallAnalyticsJobRequestRequestTypeDef(BaseModel):
    CallAnalyticsJobName: str

class GetMedicalScribeJobRequestRequestTypeDef(BaseModel):
    MedicalScribeJobName: str

class GetMedicalTranscriptionJobRequestRequestTypeDef(BaseModel):
    MedicalTranscriptionJobName: str

class GetMedicalVocabularyRequestRequestTypeDef(BaseModel):
    VocabularyName: str

class GetTranscriptionJobRequestRequestTypeDef(BaseModel):
    TranscriptionJobName: str

class GetVocabularyFilterRequestRequestTypeDef(BaseModel):
    VocabularyFilterName: str

class GetVocabularyRequestRequestTypeDef(BaseModel):
    VocabularyName: str

class RelativeTimeRangeTypeDef(BaseModel):
    StartPercentage: Optional[int] = None
    EndPercentage: Optional[int] = None
    First: Optional[int] = None
    Last: Optional[int] = None

class JobExecutionSettingsTypeDef(BaseModel):
    AllowDeferredExecution: Optional[bool] = None
    DataAccessRoleArn: Optional[str] = None

class LanguageCodeItemTypeDef(BaseModel):
    LanguageCode: Optional[LanguageCodeType] = None
    DurationInSeconds: Optional[float] = None

class ListCallAnalyticsCategoriesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCallAnalyticsJobsRequestRequestTypeDef(BaseModel):
    Status: Optional[CallAnalyticsJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLanguageModelsRequestRequestTypeDef(BaseModel):
    StatusEquals: Optional[ModelStatusType] = None
    NameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMedicalScribeJobsRequestRequestTypeDef(BaseModel):
    Status: Optional[MedicalScribeJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MedicalScribeJobSummaryTypeDef(BaseModel):
    MedicalScribeJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[Literal["en-US"]] = None
    MedicalScribeJobStatus: Optional[MedicalScribeJobStatusType] = None
    FailureReason: Optional[str] = None

class ListMedicalTranscriptionJobsRequestRequestTypeDef(BaseModel):
    Status: Optional[TranscriptionJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MedicalTranscriptionJobSummaryTypeDef(BaseModel):
    MedicalTranscriptionJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[LanguageCodeType] = None
    TranscriptionJobStatus: Optional[TranscriptionJobStatusType] = None
    FailureReason: Optional[str] = None
    OutputLocationType: Optional[OutputLocationTypeType] = None
    Specialty: Optional[Literal["PRIMARYCARE"]] = None
    ContentIdentificationType: Optional[Literal["PHI"]] = None
    Type: Optional[TypeType] = None

class ListMedicalVocabulariesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StateEquals: Optional[VocabularyStateType] = None
    NameContains: Optional[str] = None

class VocabularyInfoTypeDef(BaseModel):
    VocabularyName: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModifiedTime: Optional[datetime] = None
    VocabularyState: Optional[VocabularyStateType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListTranscriptionJobsRequestRequestTypeDef(BaseModel):
    Status: Optional[TranscriptionJobStatusType] = None
    JobNameContains: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVocabulariesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StateEquals: Optional[VocabularyStateType] = None
    NameContains: Optional[str] = None

class ListVocabularyFiltersRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    NameContains: Optional[str] = None

class VocabularyFilterInfoTypeDef(BaseModel):
    VocabularyFilterName: Optional[str] = None
    LanguageCode: Optional[LanguageCodeType] = None
    LastModifiedTime: Optional[datetime] = None

class MedicalScribeChannelDefinitionTypeDef(BaseModel):
    ChannelId: int
    ParticipantRole: MedicalScribeParticipantRoleType

class MedicalScribeOutputTypeDef(BaseModel):
    TranscriptFileUri: str
    ClinicalDocumentUri: str

class MedicalScribeSettingsTypeDef(BaseModel):
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None

class MedicalTranscriptTypeDef(BaseModel):
    TranscriptFileUri: Optional[str] = None

class MedicalTranscriptionSettingTypeDef(BaseModel):
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    ShowAlternatives: Optional[bool] = None
    MaxAlternatives: Optional[int] = None
    VocabularyName: Optional[str] = None

class ModelSettingsTypeDef(BaseModel):
    LanguageModelName: Optional[str] = None

class SettingsTypeDef(BaseModel):
    VocabularyName: Optional[str] = None
    ShowSpeakerLabels: Optional[bool] = None
    MaxSpeakerLabels: Optional[int] = None
    ChannelIdentification: Optional[bool] = None
    ShowAlternatives: Optional[bool] = None
    MaxAlternatives: Optional[int] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None

class SubtitlesTypeDef(BaseModel):
    Formats: Optional[Sequence[SubtitleFormatType]] = None
    OutputStartIndex: Optional[int] = None

class SubtitlesOutputTypeDef(BaseModel):
    Formats: Optional[List[SubtitleFormatType]] = None
    SubtitleFileUris: Optional[List[str]] = None
    OutputStartIndex: Optional[int] = None

class ToxicityDetectionSettingsOutputTypeDef(BaseModel):
    ToxicityCategories: List[Literal["ALL"]]

class ToxicityDetectionSettingsTypeDef(BaseModel):
    ToxicityCategories: Sequence[Literal["ALL"]]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateMedicalVocabularyRequestRequestTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str

class UpdateVocabularyFilterRequestRequestTypeDef(BaseModel):
    VocabularyFilterName: str
    Words: Optional[Sequence[str]] = None
    VocabularyFilterFileUri: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None

class UpdateVocabularyRequestRequestTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    Phrases: Optional[Sequence[str]] = None
    VocabularyFileUri: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None

class CallAnalyticsJobDetailsTypeDef(BaseModel):
    Skipped: Optional[List[CallAnalyticsSkippedFeatureTypeDef]] = None

class CallAnalyticsJobSettingsOutputTypeDef(BaseModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    LanguageModelName: Optional[str] = None
    ContentRedaction: Optional[ContentRedactionOutputTypeDef] = None
    LanguageOptions: Optional[List[LanguageCodeType]] = None
    LanguageIdSettings: Optional[Dict[LanguageCodeType, LanguageIdSettingsTypeDef]] = None
    Summarization: Optional[SummarizationTypeDef] = None

class CallAnalyticsJobSettingsTypeDef(BaseModel):
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    LanguageModelName: Optional[str] = None
    ContentRedaction: Optional[ContentRedactionTypeDef] = None
    LanguageOptions: Optional[Sequence[LanguageCodeType]] = None
    LanguageIdSettings: Optional[Mapping[LanguageCodeType, LanguageIdSettingsTypeDef]] = None
    Summarization: Optional[SummarizationTypeDef] = None

class CreateMedicalVocabularyResponseTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVocabularyFilterResponseTypeDef(BaseModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVocabularyResponseTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetMedicalVocabularyResponseTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVocabularyFilterResponseTypeDef(BaseModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVocabularyResponseTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyState: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMedicalVocabularyResponseTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVocabularyFilterResponseTypeDef(BaseModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVocabularyResponseTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    LastModifiedTime: datetime
    VocabularyState: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLanguageModelResponseTypeDef(BaseModel):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfigTypeDef
    ModelStatus: ModelStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class LanguageModelTypeDef(BaseModel):
    ModelName: Optional[str] = None
    CreateTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LanguageCode: Optional[CLMLanguageCodeType] = None
    BaseModelName: Optional[BaseModelNameType] = None
    ModelStatus: Optional[ModelStatusType] = None
    UpgradeAvailability: Optional[bool] = None
    FailureReason: Optional[str] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None

class CreateLanguageModelRequestRequestTypeDef(BaseModel):
    LanguageCode: CLMLanguageCodeType
    BaseModelName: BaseModelNameType
    ModelName: str
    InputDataConfig: InputDataConfigTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMedicalVocabularyRequestRequestTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    VocabularyFileUri: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateVocabularyFilterRequestRequestTypeDef(BaseModel):
    VocabularyFilterName: str
    LanguageCode: LanguageCodeType
    Words: Optional[Sequence[str]] = None
    VocabularyFilterFileUri: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataAccessRoleArn: Optional[str] = None

class CreateVocabularyRequestRequestTypeDef(BaseModel):
    VocabularyName: str
    LanguageCode: LanguageCodeType
    Phrases: Optional[Sequence[str]] = None
    VocabularyFileUri: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataAccessRoleArn: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    ResourceArn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class InterruptionFilterTypeDef(BaseModel):
    Threshold: Optional[int] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    Negate: Optional[bool] = None

class NonTalkTimeFilterTypeDef(BaseModel):
    Threshold: Optional[int] = None
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    Negate: Optional[bool] = None

class SentimentFilterOutputTypeDef(BaseModel):
    Sentiments: List[SentimentValueType]
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None

class SentimentFilterTypeDef(BaseModel):
    Sentiments: Sequence[SentimentValueType]
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None

class TranscriptFilterOutputTypeDef(BaseModel):
    TranscriptFilterType: Literal["EXACT"]
    Targets: List[str]
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None

class TranscriptFilterTypeDef(BaseModel):
    TranscriptFilterType: Literal["EXACT"]
    Targets: Sequence[str]
    AbsoluteTimeRange: Optional[AbsoluteTimeRangeTypeDef] = None
    RelativeTimeRange: Optional[RelativeTimeRangeTypeDef] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    Negate: Optional[bool] = None

class ListMedicalScribeJobsResponseTypeDef(BaseModel):
    Status: MedicalScribeJobStatusType
    MedicalScribeJobSummaries: List[MedicalScribeJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMedicalTranscriptionJobsResponseTypeDef(BaseModel):
    Status: TranscriptionJobStatusType
    MedicalTranscriptionJobSummaries: List[MedicalTranscriptionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMedicalVocabulariesResponseTypeDef(BaseModel):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListVocabulariesResponseTypeDef(BaseModel):
    Status: VocabularyStateType
    Vocabularies: List[VocabularyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListVocabularyFiltersResponseTypeDef(BaseModel):
    VocabularyFilters: List[VocabularyFilterInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MedicalScribeJobTypeDef(BaseModel):
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

class StartMedicalScribeJobRequestRequestTypeDef(BaseModel):
    MedicalScribeJobName: str
    Media: MediaTypeDef
    OutputBucketName: str
    DataAccessRoleArn: str
    Settings: MedicalScribeSettingsTypeDef
    OutputEncryptionKMSKeyId: Optional[str] = None
    KMSEncryptionContext: Optional[Mapping[str, str]] = None
    ChannelDefinitions: Optional[Sequence[MedicalScribeChannelDefinitionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MedicalTranscriptionJobTypeDef(BaseModel):
    MedicalTranscriptionJobName: Optional[str] = None
    TranscriptionJobStatus: Optional[TranscriptionJobStatusType] = None
    LanguageCode: Optional[LanguageCodeType] = None
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    Media: Optional[MediaTypeDef] = None
    Transcript: Optional[MedicalTranscriptTypeDef] = None
    StartTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    FailureReason: Optional[str] = None
    Settings: Optional[MedicalTranscriptionSettingTypeDef] = None
    ContentIdentificationType: Optional[Literal["PHI"]] = None
    Specialty: Optional[Literal["PRIMARYCARE"]] = None
    Type: Optional[TypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class StartMedicalTranscriptionJobRequestRequestTypeDef(BaseModel):
    MedicalTranscriptionJobName: str
    LanguageCode: LanguageCodeType
    Media: MediaTypeDef
    OutputBucketName: str
    Specialty: Literal["PRIMARYCARE"]
    Type: TypeType
    MediaSampleRateHertz: Optional[int] = None
    MediaFormat: Optional[MediaFormatType] = None
    OutputKey: Optional[str] = None
    OutputEncryptionKMSKeyId: Optional[str] = None
    KMSEncryptionContext: Optional[Mapping[str, str]] = None
    Settings: Optional[MedicalTranscriptionSettingTypeDef] = None
    ContentIdentificationType: Optional[Literal["PHI"]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TranscriptionJobSummaryTypeDef(BaseModel):
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

class TranscriptionJobTypeDef(BaseModel):
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

class CallAnalyticsJobSummaryTypeDef(BaseModel):
    CallAnalyticsJobName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    CompletionTime: Optional[datetime] = None
    LanguageCode: Optional[LanguageCodeType] = None
    CallAnalyticsJobStatus: Optional[CallAnalyticsJobStatusType] = None
    CallAnalyticsJobDetails: Optional[CallAnalyticsJobDetailsTypeDef] = None
    FailureReason: Optional[str] = None

class CallAnalyticsJobTypeDef(BaseModel):
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

class StartCallAnalyticsJobRequestRequestTypeDef(BaseModel):
    CallAnalyticsJobName: str
    Media: MediaTypeDef
    OutputLocation: Optional[str] = None
    OutputEncryptionKMSKeyId: Optional[str] = None
    DataAccessRoleArn: Optional[str] = None
    Settings: Optional[CallAnalyticsJobSettingsTypeDef] = None
    ChannelDefinitions: Optional[Sequence[ChannelDefinitionTypeDef]] = None

class DescribeLanguageModelResponseTypeDef(BaseModel):
    LanguageModel: LanguageModelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLanguageModelsResponseTypeDef(BaseModel):
    Models: List[LanguageModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RuleOutputTypeDef(BaseModel):
    NonTalkTimeFilter: Optional[NonTalkTimeFilterTypeDef] = None
    InterruptionFilter: Optional[InterruptionFilterTypeDef] = None
    TranscriptFilter: Optional[TranscriptFilterOutputTypeDef] = None
    SentimentFilter: Optional[SentimentFilterOutputTypeDef] = None

class RuleTypeDef(BaseModel):
    NonTalkTimeFilter: Optional[NonTalkTimeFilterTypeDef] = None
    InterruptionFilter: Optional[InterruptionFilterTypeDef] = None
    TranscriptFilter: Optional[TranscriptFilterTypeDef] = None
    SentimentFilter: Optional[SentimentFilterTypeDef] = None

class GetMedicalScribeJobResponseTypeDef(BaseModel):
    MedicalScribeJob: MedicalScribeJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMedicalScribeJobResponseTypeDef(BaseModel):
    MedicalScribeJob: MedicalScribeJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMedicalTranscriptionJobResponseTypeDef(BaseModel):
    MedicalTranscriptionJob: MedicalTranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMedicalTranscriptionJobResponseTypeDef(BaseModel):
    MedicalTranscriptionJob: MedicalTranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTranscriptionJobsResponseTypeDef(BaseModel):
    Status: TranscriptionJobStatusType
    TranscriptionJobSummaries: List[TranscriptionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTranscriptionJobResponseTypeDef(BaseModel):
    TranscriptionJob: TranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartTranscriptionJobResponseTypeDef(BaseModel):
    TranscriptionJob: TranscriptionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartTranscriptionJobRequestRequestTypeDef(BaseModel):
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
    ContentRedaction: Optional[ContentRedactionTypeDef] = None
    IdentifyLanguage: Optional[bool] = None
    IdentifyMultipleLanguages: Optional[bool] = None
    LanguageOptions: Optional[Sequence[LanguageCodeType]] = None
    Subtitles: Optional[SubtitlesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    LanguageIdSettings: Optional[Mapping[LanguageCodeType, LanguageIdSettingsTypeDef]] = None
    ToxicityDetection: Optional[Sequence[ToxicityDetectionSettingsUnionTypeDef]] = None

class ListCallAnalyticsJobsResponseTypeDef(BaseModel):
    Status: CallAnalyticsJobStatusType
    CallAnalyticsJobSummaries: List[CallAnalyticsJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCallAnalyticsJobResponseTypeDef(BaseModel):
    CallAnalyticsJob: CallAnalyticsJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartCallAnalyticsJobResponseTypeDef(BaseModel):
    CallAnalyticsJob: CallAnalyticsJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CategoryPropertiesTypeDef(BaseModel):
    CategoryName: Optional[str] = None
    Rules: Optional[List[RuleOutputTypeDef]] = None
    CreateTime: Optional[datetime] = None
    LastUpdateTime: Optional[datetime] = None
    InputType: Optional[InputTypeType] = None

class CreateCallAnalyticsCategoryResponseTypeDef(BaseModel):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCallAnalyticsCategoryResponseTypeDef(BaseModel):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCallAnalyticsCategoriesResponseTypeDef(BaseModel):
    Categories: List[CategoryPropertiesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateCallAnalyticsCategoryResponseTypeDef(BaseModel):
    CategoryProperties: CategoryPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCallAnalyticsCategoryRequestRequestTypeDef(BaseModel):
    CategoryName: str
    Rules: Sequence[RuleUnionTypeDef]
    InputType: Optional[InputTypeType] = None

class UpdateCallAnalyticsCategoryRequestRequestTypeDef(BaseModel):
    CategoryName: str
    Rules: Sequence[RuleUnionTypeDef]
    InputType: Optional[InputTypeType] = None


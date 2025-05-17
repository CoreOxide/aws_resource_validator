from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.voice_id.voice_id_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'associate_fraudster' function.
class AssociateFraudsterRequest(BaseValidatorModel):
    DomainId: str
    FraudsterId: str
    WatchlistId: str


class Fraudster(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    GeneratedFraudsterId: Optional[str] = None
    WatchlistIds: Optional[List[str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AuthenticationConfiguration(BaseValidatorModel):
    AcceptanceThreshold: int


class ServerSideEncryptionConfiguration(BaseValidatorModel):
    KmsKeyId: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


# This class is the input for the 'create_watchlist' function.
class CreateWatchlistRequest(BaseValidatorModel):
    DomainId: str
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None


class Watchlist(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DefaultWatchlist: Optional[bool] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    Name: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistId: Optional[str] = None


# This class is the input for the 'delete_domain' function.
class DeleteDomainRequest(BaseValidatorModel):
    DomainId: str


# This class is the input for the 'delete_fraudster' function.
class DeleteFraudsterRequest(BaseValidatorModel):
    DomainId: str
    FraudsterId: str


# This class is the input for the 'delete_speaker' function.
class DeleteSpeakerRequest(BaseValidatorModel):
    DomainId: str
    SpeakerId: str


# This class is the input for the 'delete_watchlist' function.
class DeleteWatchlistRequest(BaseValidatorModel):
    DomainId: str
    WatchlistId: str


# This class is the input for the 'describe_domain' function.
class DescribeDomainRequest(BaseValidatorModel):
    DomainId: str


# This class is the input for the 'describe_fraudster_registration_job' function.
class DescribeFraudsterRegistrationJobRequest(BaseValidatorModel):
    DomainId: str
    JobId: str


# This class is the input for the 'describe_fraudster' function.
class DescribeFraudsterRequest(BaseValidatorModel):
    DomainId: str
    FraudsterId: str


# This class is the input for the 'describe_speaker_enrollment_job' function.
class DescribeSpeakerEnrollmentJobRequest(BaseValidatorModel):
    DomainId: str
    JobId: str


# This class is the input for the 'describe_speaker' function.
class DescribeSpeakerRequest(BaseValidatorModel):
    DomainId: str
    SpeakerId: str


class Speaker(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    CustomerSpeakerId: Optional[str] = None
    DomainId: Optional[str] = None
    GeneratedSpeakerId: Optional[str] = None
    LastAccessedAt: Optional[datetime] = None
    Status: Optional[SpeakerStatusType] = None
    UpdatedAt: Optional[datetime] = None


# This class is the input for the 'describe_watchlist' function.
class DescribeWatchlistRequest(BaseValidatorModel):
    DomainId: str
    WatchlistId: str


# This class is the input for the 'disassociate_fraudster' function.
class DisassociateFraudsterRequest(BaseValidatorModel):
    DomainId: str
    FraudsterId: str
    WatchlistId: str


class ServerSideEncryptionUpdateDetails(BaseValidatorModel):
    Message: Optional[str] = None
    OldKmsKeyId: Optional[str] = None
    UpdateStatus: Optional[ServerSideEncryptionUpdateStatusType] = None


class WatchlistDetails(BaseValidatorModel):
    DefaultWatchlistId: str


class EnrollmentJobFraudDetectionConfigOutput(BaseValidatorModel):
    FraudDetectionAction: Optional[FraudDetectionActionType] = None
    RiskThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None


class EnrollmentJobFraudDetectionConfig(BaseValidatorModel):
    FraudDetectionAction: Optional[FraudDetectionActionType] = None
    RiskThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None


# This class is the input for the 'evaluate_session' function.
class EvaluateSessionRequest(BaseValidatorModel):
    DomainId: str
    SessionNameOrId: str


class FailureDetails(BaseValidatorModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None


class FraudDetectionConfiguration(BaseValidatorModel):
    RiskThreshold: Optional[int] = None
    WatchlistId: Optional[str] = None


class KnownFraudsterRisk(BaseValidatorModel):
    RiskScore: int
    GeneratedFraudsterId: Optional[str] = None


class VoiceSpoofingRisk(BaseValidatorModel):
    RiskScore: int


class JobProgress(BaseValidatorModel):
    PercentComplete: Optional[int] = None


class InputDataConfig(BaseValidatorModel):
    S3Uri: str


class OutputDataConfig(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class RegistrationConfigOutput(BaseValidatorModel):
    DuplicateRegistrationAction: Optional[DuplicateRegistrationActionType] = None
    FraudsterSimilarityThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None


class FraudsterSummary(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    GeneratedFraudsterId: Optional[str] = None
    WatchlistIds: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_domains' function.
class ListDomainsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_fraudster_registration_jobs' function.
class ListFraudsterRegistrationJobsRequest(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_fraudsters' function.
class ListFraudstersRequest(BaseValidatorModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WatchlistId: Optional[str] = None


# This class is the input for the 'list_speaker_enrollment_jobs' function.
class ListSpeakerEnrollmentJobsRequest(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_speakers' function.
class ListSpeakersRequest(BaseValidatorModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SpeakerSummary(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    CustomerSpeakerId: Optional[str] = None
    DomainId: Optional[str] = None
    GeneratedSpeakerId: Optional[str] = None
    LastAccessedAt: Optional[datetime] = None
    Status: Optional[SpeakerStatusType] = None
    UpdatedAt: Optional[datetime] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'list_watchlists' function.
class ListWatchlistsRequest(BaseValidatorModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class WatchlistSummary(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DefaultWatchlist: Optional[bool] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    Name: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistId: Optional[str] = None


# This class is the input for the 'opt_out_speaker' function.
class OptOutSpeakerRequest(BaseValidatorModel):
    DomainId: str
    SpeakerId: str


class RegistrationConfig(BaseValidatorModel):
    DuplicateRegistrationAction: Optional[DuplicateRegistrationActionType] = None
    FraudsterSimilarityThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_watchlist' function.
class UpdateWatchlistRequest(BaseValidatorModel):
    DomainId: str
    WatchlistId: str
    Description: Optional[str] = None
    Name: Optional[str] = None


# This class is the output for the 'associate_fraudster' function.
class AssociateFraudsterResponse(BaseValidatorModel):
    Fraudster: Fraudster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fraudster' function.
class DescribeFraudsterResponse(BaseValidatorModel):
    Fraudster: Fraudster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_fraudster' function.
class DisassociateFraudsterResponse(BaseValidatorModel):
    Fraudster: Fraudster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_watchlist' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class AuthenticationResult(BaseValidatorModel):
    AudioAggregationEndedAt: Optional[datetime] = None
    AudioAggregationStartedAt: Optional[datetime] = None
    AuthenticationResultId: Optional[str] = None
    Configuration: Optional[AuthenticationConfiguration] = None
    CustomerSpeakerId: Optional[str] = None
    Decision: Optional[AuthenticationDecisionType] = None
    GeneratedSpeakerId: Optional[str] = None
    Score: Optional[int] = None


# This class is the input for the 'update_domain' function.
class UpdateDomainRequest(BaseValidatorModel):
    DomainId: str
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfiguration
    Description: Optional[str] = None


# This class is the input for the 'create_domain' function.
class CreateDomainRequest(BaseValidatorModel):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfiguration
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the output for the 'create_watchlist' function.
class CreateWatchlistResponse(BaseValidatorModel):
    Watchlist: Watchlist
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_watchlist' function.
class DescribeWatchlistResponse(BaseValidatorModel):
    Watchlist: Watchlist
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_watchlist' function.
class UpdateWatchlistResponse(BaseValidatorModel):
    Watchlist: Watchlist
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_speaker' function.
class DescribeSpeakerResponse(BaseValidatorModel):
    Speaker: Speaker
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'opt_out_speaker' function.
class OptOutSpeakerResponse(BaseValidatorModel):
    Speaker: Speaker
    ResponseMetadata: ResponseMetadata


class DomainSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    DomainStatus: Optional[DomainStatusType] = None
    Name: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    ServerSideEncryptionUpdateDetails: Optional[ServerSideEncryptionUpdateDetails] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistDetails: Optional[WatchlistDetails] = None


class Domain(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    DomainStatus: Optional[DomainStatusType] = None
    Name: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    ServerSideEncryptionUpdateDetails: Optional[ServerSideEncryptionUpdateDetails] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistDetails: Optional[WatchlistDetails] = None


class EnrollmentConfigOutput(BaseValidatorModel):
    ExistingEnrollmentAction: Optional[ExistingEnrollmentActionType] = None
    FraudDetectionConfig: Optional[EnrollmentJobFraudDetectionConfigOutput] = None


class EnrollmentConfig(BaseValidatorModel):
    ExistingEnrollmentAction: Optional[ExistingEnrollmentActionType] = None
    FraudDetectionConfig: Optional[EnrollmentJobFraudDetectionConfig] = None


class FraudRiskDetails(BaseValidatorModel):
    KnownFraudsterRisk: KnownFraudsterRisk
    VoiceSpoofingRisk: VoiceSpoofingRisk


class FraudsterRegistrationJobSummary(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    FailureDetails: Optional[FailureDetails] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgress] = None
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None


class SpeakerEnrollmentJobSummary(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    FailureDetails: Optional[FailureDetails] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgress] = None
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None


class FraudsterRegistrationJob(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DataAccessRoleArn: Optional[str] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    FailureDetails: Optional[FailureDetails] = None
    InputDataConfig: Optional[InputDataConfig] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgress] = None
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    OutputDataConfig: Optional[OutputDataConfig] = None
    RegistrationConfig: Optional[RegistrationConfigOutput] = None


# This class is the output for the 'list_fraudsters' function.
class ListFraudstersResponse(BaseValidatorModel):
    FraudsterSummaries: List[FraudsterSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDomainsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFraudsterRegistrationJobsRequestPaginate(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFraudstersRequestPaginate(BaseValidatorModel):
    DomainId: str
    WatchlistId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSpeakerEnrollmentJobsRequestPaginate(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSpeakersRequestPaginate(BaseValidatorModel):
    DomainId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWatchlistsRequestPaginate(BaseValidatorModel):
    DomainId: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_speakers' function.
class ListSpeakersResponse(BaseValidatorModel):
    SpeakerSummaries: List[SpeakerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_watchlists' function.
class ListWatchlistsResponse(BaseValidatorModel):
    WatchlistSummaries: List[WatchlistSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

RegistrationConfigUnion = Union[RegistrationConfig, RegistrationConfigOutput]


# This class is the output for the 'list_domains' function.
class ListDomainsResponse(BaseValidatorModel):
    DomainSummaries: List[DomainSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_domain' function.
class CreateDomainResponse(BaseValidatorModel):
    Domain: Domain
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domain' function.
class DescribeDomainResponse(BaseValidatorModel):
    Domain: Domain
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain' function.
class UpdateDomainResponse(BaseValidatorModel):
    Domain: Domain
    ResponseMetadata: ResponseMetadata


class SpeakerEnrollmentJob(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DataAccessRoleArn: Optional[str] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    EnrollmentConfig: Optional[EnrollmentConfigOutput] = None
    FailureDetails: Optional[FailureDetails] = None
    InputDataConfig: Optional[InputDataConfig] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgress] = None
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    OutputDataConfig: Optional[OutputDataConfig] = None

EnrollmentConfigUnion = Union[EnrollmentConfig, EnrollmentConfigOutput]


class FraudDetectionResult(BaseValidatorModel):
    AudioAggregationEndedAt: Optional[datetime] = None
    AudioAggregationStartedAt: Optional[datetime] = None
    Configuration: Optional[FraudDetectionConfiguration] = None
    Decision: Optional[FraudDetectionDecisionType] = None
    FraudDetectionResultId: Optional[str] = None
    Reasons: Optional[List[FraudDetectionReasonType]] = None
    RiskDetails: Optional[FraudRiskDetails] = None


# This class is the output for the 'list_fraudster_registration_jobs' function.
class ListFraudsterRegistrationJobsResponse(BaseValidatorModel):
    JobSummaries: List[FraudsterRegistrationJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_speaker_enrollment_jobs' function.
class ListSpeakerEnrollmentJobsResponse(BaseValidatorModel):
    JobSummaries: List[SpeakerEnrollmentJobSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fraudster_registration_job' function.
class DescribeFraudsterRegistrationJobResponse(BaseValidatorModel):
    Job: FraudsterRegistrationJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_fraudster_registration_job' function.
class StartFraudsterRegistrationJobResponse(BaseValidatorModel):
    Job: FraudsterRegistrationJob
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_fraudster_registration_job' function.
class StartFraudsterRegistrationJobRequest(BaseValidatorModel):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    ClientToken: Optional[str] = None
    JobName: Optional[str] = None
    RegistrationConfig: Optional[RegistrationConfigUnion] = None


# This class is the output for the 'describe_speaker_enrollment_job' function.
class DescribeSpeakerEnrollmentJobResponse(BaseValidatorModel):
    Job: SpeakerEnrollmentJob
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_speaker_enrollment_job' function.
class StartSpeakerEnrollmentJobResponse(BaseValidatorModel):
    Job: SpeakerEnrollmentJob
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_speaker_enrollment_job' function.
class StartSpeakerEnrollmentJobRequest(BaseValidatorModel):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfig
    OutputDataConfig: OutputDataConfig
    ClientToken: Optional[str] = None
    EnrollmentConfig: Optional[EnrollmentConfigUnion] = None
    JobName: Optional[str] = None


# This class is the output for the 'evaluate_session' function.
class EvaluateSessionResponse(BaseValidatorModel):
    AuthenticationResult: AuthenticationResult
    DomainId: str
    FraudDetectionResult: FraudDetectionResult
    SessionId: str
    SessionName: str
    StreamingStatus: StreamingStatusType
    ResponseMetadata: ResponseMetadata
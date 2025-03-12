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
from aws_resource_validator.pydantic_models.voice_id_constants import *

class AssociateFraudsterRequestTypeDef(BaseValidatorModel):
    DomainId: str
    FraudsterId: str
    WatchlistId: str


class FraudsterTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    GeneratedFraudsterId: Optional[str] = None
    WatchlistIds: Optional[List[str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    AcceptanceThreshold: int


class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    KmsKeyId: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CreateWatchlistRequestTypeDef(BaseValidatorModel):
    DomainId: str
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None


class WatchlistTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DefaultWatchlist: Optional[bool] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    Name: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistId: Optional[str] = None


class DeleteDomainRequestTypeDef(BaseValidatorModel):
    DomainId: str


class DeleteFraudsterRequestTypeDef(BaseValidatorModel):
    DomainId: str
    FraudsterId: str


class DeleteSpeakerRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpeakerId: str


class DeleteWatchlistRequestTypeDef(BaseValidatorModel):
    DomainId: str
    WatchlistId: str


class DescribeDomainRequestTypeDef(BaseValidatorModel):
    DomainId: str


class DescribeFraudsterRegistrationJobRequestTypeDef(BaseValidatorModel):
    DomainId: str
    JobId: str


class DescribeFraudsterRequestTypeDef(BaseValidatorModel):
    DomainId: str
    FraudsterId: str


class DescribeSpeakerEnrollmentJobRequestTypeDef(BaseValidatorModel):
    DomainId: str
    JobId: str


class DescribeSpeakerRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpeakerId: str


class SpeakerTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    CustomerSpeakerId: Optional[str] = None
    DomainId: Optional[str] = None
    GeneratedSpeakerId: Optional[str] = None
    LastAccessedAt: Optional[datetime] = None
    Status: Optional[SpeakerStatusType] = None
    UpdatedAt: Optional[datetime] = None


class DescribeWatchlistRequestTypeDef(BaseValidatorModel):
    DomainId: str
    WatchlistId: str


class DisassociateFraudsterRequestTypeDef(BaseValidatorModel):
    DomainId: str
    FraudsterId: str
    WatchlistId: str


class ServerSideEncryptionUpdateDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    OldKmsKeyId: Optional[str] = None
    UpdateStatus: Optional[ServerSideEncryptionUpdateStatusType] = None


class WatchlistDetailsTypeDef(BaseValidatorModel):
    DefaultWatchlistId: str


class EnrollmentJobFraudDetectionConfigOutputTypeDef(BaseValidatorModel):
    FraudDetectionAction: Optional[FraudDetectionActionType] = None
    RiskThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None


class EnrollmentJobFraudDetectionConfigTypeDef(BaseValidatorModel):
    FraudDetectionAction: Optional[FraudDetectionActionType] = None
    RiskThreshold: Optional[int] = None
    WatchlistIds: Optional[Sequence[str]] = None


class EvaluateSessionRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SessionNameOrId: str


class FailureDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None


class FraudDetectionConfigurationTypeDef(BaseValidatorModel):
    RiskThreshold: Optional[int] = None
    WatchlistId: Optional[str] = None


class KnownFraudsterRiskTypeDef(BaseValidatorModel):
    RiskScore: int
    GeneratedFraudsterId: Optional[str] = None


class VoiceSpoofingRiskTypeDef(BaseValidatorModel):
    RiskScore: int


class JobProgressTypeDef(BaseValidatorModel):
    PercentComplete: Optional[int] = None


class InputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str


class OutputDataConfigTypeDef(BaseValidatorModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None


class RegistrationConfigOutputTypeDef(BaseValidatorModel):
    DuplicateRegistrationAction: Optional[DuplicateRegistrationActionType] = None
    FraudsterSimilarityThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None


class FraudsterSummaryTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    GeneratedFraudsterId: Optional[str] = None
    WatchlistIds: Optional[List[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListDomainsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFraudsterRegistrationJobsRequestTypeDef(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFraudstersRequestTypeDef(BaseValidatorModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WatchlistId: Optional[str] = None


class ListSpeakerEnrollmentJobsRequestTypeDef(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSpeakersRequestTypeDef(BaseValidatorModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SpeakerSummaryTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    CustomerSpeakerId: Optional[str] = None
    DomainId: Optional[str] = None
    GeneratedSpeakerId: Optional[str] = None
    LastAccessedAt: Optional[datetime] = None
    Status: Optional[SpeakerStatusType] = None
    UpdatedAt: Optional[datetime] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListWatchlistsRequestTypeDef(BaseValidatorModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class WatchlistSummaryTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DefaultWatchlist: Optional[bool] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    Name: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistId: Optional[str] = None


class OptOutSpeakerRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpeakerId: str


class RegistrationConfigTypeDef(BaseValidatorModel):
    DuplicateRegistrationAction: Optional[DuplicateRegistrationActionType] = None
    FraudsterSimilarityThreshold: Optional[int] = None
    WatchlistIds: Optional[Sequence[str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateWatchlistRequestTypeDef(BaseValidatorModel):
    DomainId: str
    WatchlistId: str
    Description: Optional[str] = None
    Name: Optional[str] = None


class AssociateFraudsterResponseTypeDef(BaseValidatorModel):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFraudsterResponseTypeDef(BaseValidatorModel):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateFraudsterResponseTypeDef(BaseValidatorModel):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class AuthenticationResultTypeDef(BaseValidatorModel):
    AudioAggregationEndedAt: Optional[datetime] = None
    AudioAggregationStartedAt: Optional[datetime] = None
    AuthenticationResultId: Optional[str] = None
    Configuration: Optional[AuthenticationConfigurationTypeDef] = None
    CustomerSpeakerId: Optional[str] = None
    Decision: Optional[AuthenticationDecisionType] = None
    GeneratedSpeakerId: Optional[str] = None
    Score: Optional[int] = None


class UpdateDomainRequestTypeDef(BaseValidatorModel):
    DomainId: str
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    Description: Optional[str] = None


class CreateDomainRequestTypeDef(BaseValidatorModel):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateWatchlistResponseTypeDef(BaseValidatorModel):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWatchlistResponseTypeDef(BaseValidatorModel):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWatchlistResponseTypeDef(BaseValidatorModel):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSpeakerResponseTypeDef(BaseValidatorModel):
    Speaker: SpeakerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OptOutSpeakerResponseTypeDef(BaseValidatorModel):
    Speaker: SpeakerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DomainSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    DomainStatus: Optional[DomainStatusType] = None
    Name: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    ServerSideEncryptionUpdateDetails: Optional[ServerSideEncryptionUpdateDetailsTypeDef] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistDetails: Optional[WatchlistDetailsTypeDef] = None


class DomainTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    DomainStatus: Optional[DomainStatusType] = None
    Name: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    ServerSideEncryptionUpdateDetails: Optional[ServerSideEncryptionUpdateDetailsTypeDef] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistDetails: Optional[WatchlistDetailsTypeDef] = None


class EnrollmentConfigOutputTypeDef(BaseValidatorModel):
    ExistingEnrollmentAction: Optional[ExistingEnrollmentActionType] = None
    FraudDetectionConfig: Optional[EnrollmentJobFraudDetectionConfigOutputTypeDef] = None


class EnrollmentConfigTypeDef(BaseValidatorModel):
    ExistingEnrollmentAction: Optional[ExistingEnrollmentActionType] = None
    FraudDetectionConfig: Optional[EnrollmentJobFraudDetectionConfigTypeDef] = None


class FraudRiskDetailsTypeDef(BaseValidatorModel):
    KnownFraudsterRisk: KnownFraudsterRiskTypeDef
    VoiceSpoofingRisk: VoiceSpoofingRiskTypeDef


class FraudsterRegistrationJobSummaryTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgressTypeDef] = None
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None


class SpeakerEnrollmentJobSummaryTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgressTypeDef] = None
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None


class FraudsterRegistrationJobTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DataAccessRoleArn: Optional[str] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgressTypeDef] = None
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None
    RegistrationConfig: Optional[RegistrationConfigOutputTypeDef] = None


class ListFraudstersResponseTypeDef(BaseValidatorModel):
    FraudsterSummaries: List[FraudsterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDomainsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFraudsterRegistrationJobsRequestPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFraudstersRequestPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    WatchlistId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSpeakerEnrollmentJobsRequestPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSpeakersRequestPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWatchlistsRequestPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSpeakersResponseTypeDef(BaseValidatorModel):
    SpeakerSummaries: List[SpeakerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWatchlistsResponseTypeDef(BaseValidatorModel):
    WatchlistSummaries: List[WatchlistSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDomainsResponseTypeDef(BaseValidatorModel):
    DomainSummaries: List[DomainSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateDomainResponseTypeDef(BaseValidatorModel):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainResponseTypeDef(BaseValidatorModel):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDomainResponseTypeDef(BaseValidatorModel):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SpeakerEnrollmentJobTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    DataAccessRoleArn: Optional[str] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    EnrollmentConfig: Optional[EnrollmentConfigOutputTypeDef] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgressTypeDef] = None
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None


class FraudDetectionResultTypeDef(BaseValidatorModel):
    AudioAggregationEndedAt: Optional[datetime] = None
    AudioAggregationStartedAt: Optional[datetime] = None
    Configuration: Optional[FraudDetectionConfigurationTypeDef] = None
    Decision: Optional[FraudDetectionDecisionType] = None
    FraudDetectionResultId: Optional[str] = None
    Reasons: Optional[List[FraudDetectionReasonType]] = None
    RiskDetails: Optional[FraudRiskDetailsTypeDef] = None


class ListFraudsterRegistrationJobsResponseTypeDef(BaseValidatorModel):
    JobSummaries: List[FraudsterRegistrationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSpeakerEnrollmentJobsResponseTypeDef(BaseValidatorModel):
    JobSummaries: List[SpeakerEnrollmentJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeFraudsterRegistrationJobResponseTypeDef(BaseValidatorModel):
    Job: FraudsterRegistrationJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartFraudsterRegistrationJobResponseTypeDef(BaseValidatorModel):
    Job: FraudsterRegistrationJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RegistrationConfigUnionTypeDef(BaseValidatorModel):
    pass


class StartFraudsterRegistrationJobRequestTypeDef(BaseValidatorModel):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    ClientToken: Optional[str] = None
    JobName: Optional[str] = None
    RegistrationConfig: Optional[RegistrationConfigUnionTypeDef] = None


class DescribeSpeakerEnrollmentJobResponseTypeDef(BaseValidatorModel):
    Job: SpeakerEnrollmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartSpeakerEnrollmentJobResponseTypeDef(BaseValidatorModel):
    Job: SpeakerEnrollmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EnrollmentConfigUnionTypeDef(BaseValidatorModel):
    pass


class StartSpeakerEnrollmentJobRequestTypeDef(BaseValidatorModel):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    ClientToken: Optional[str] = None
    EnrollmentConfig: Optional[EnrollmentConfigUnionTypeDef] = None
    JobName: Optional[str] = None


class EvaluateSessionResponseTypeDef(BaseValidatorModel):
    AuthenticationResult: AuthenticationResultTypeDef
    DomainId: str
    FraudDetectionResult: FraudDetectionResultTypeDef
    SessionId: str
    SessionName: str
    StreamingStatus: StreamingStatusType
    ResponseMetadata: ResponseMetadataTypeDef



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
from aws_resource_validator.pydantic_models.voice_id_constants import *

class AssociateFraudsterRequestRequestTypeDef(BaseValidatorModel):
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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    AcceptanceThreshold: int

class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    KmsKeyId: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CreateWatchlistRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str

class DeleteFraudsterRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    FraudsterId: str

class DeleteSpeakerRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpeakerId: str

class DeleteWatchlistRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    WatchlistId: str

class DescribeDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str

class DescribeFraudsterRegistrationJobRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    JobId: str

class DescribeFraudsterRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    FraudsterId: str

class DescribeSpeakerEnrollmentJobRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    JobId: str

class DescribeSpeakerRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeWatchlistRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    WatchlistId: str

class DisassociateFraudsterRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    FraudsterId: str
    WatchlistId: str

class ServerSideEncryptionUpdateDetailsTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    OldKmsKeyId: Optional[str] = None
    UpdateStatus: Optional[ServerSideEncryptionUpdateStatusType] = None

class WatchlistDetailsTypeDef(BaseValidatorModel):
    DefaultWatchlistId: str

class EnrollmentJobFraudDetectionConfigTypeDef(BaseValidatorModel):
    FraudDetectionAction: Optional[FraudDetectionActionType] = None
    RiskThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None

class EvaluateSessionRequestRequestTypeDef(BaseValidatorModel):
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

class RegistrationConfigTypeDef(BaseValidatorModel):
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

class ListDomainsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFraudsterRegistrationJobsRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFraudstersRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WatchlistId: Optional[str] = None

class ListSpeakerEnrollmentJobsRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSpeakersRequestRequestTypeDef(BaseValidatorModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ListWatchlistsRequestRequestTypeDef(BaseValidatorModel):
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

class OptOutSpeakerRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    SpeakerId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateWatchlistRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateDomainRequestRequestTypeDef(BaseValidatorModel):
    DomainId: str
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    Description: Optional[str] = None

class CreateDomainRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    RegistrationConfig: Optional[RegistrationConfigTypeDef] = None

class StartFraudsterRegistrationJobRequestRequestTypeDef(BaseValidatorModel):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    ClientToken: Optional[str] = None
    JobName: Optional[str] = None
    RegistrationConfig: Optional[RegistrationConfigTypeDef] = None

class ListFraudstersResponseTypeDef(BaseValidatorModel):
    FraudsterSummaries: List[FraudsterSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsRequestListDomainsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFraudsterRegistrationJobsRequestListFraudsterRegistrationJobsPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFraudstersRequestListFraudstersPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    WatchlistId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpeakerEnrollmentJobsRequestListSpeakerEnrollmentJobsPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpeakersRequestListSpeakersPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWatchlistsRequestListWatchlistsPaginateTypeDef(BaseValidatorModel):
    DomainId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpeakersResponseTypeDef(BaseValidatorModel):
    NextToken: str
    SpeakerSummaries: List[SpeakerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWatchlistsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    WatchlistSummaries: List[WatchlistSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResponseTypeDef(BaseValidatorModel):
    DomainSummaries: List[DomainSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    EnrollmentConfig: Optional[EnrollmentConfigTypeDef] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    InputDataConfig: Optional[InputDataConfigTypeDef] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgressTypeDef] = None
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    OutputDataConfig: Optional[OutputDataConfigTypeDef] = None

class StartSpeakerEnrollmentJobRequestRequestTypeDef(BaseValidatorModel):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    ClientToken: Optional[str] = None
    EnrollmentConfig: Optional[EnrollmentConfigTypeDef] = None
    JobName: Optional[str] = None

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSpeakerEnrollmentJobsResponseTypeDef(BaseValidatorModel):
    JobSummaries: List[SpeakerEnrollmentJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFraudsterRegistrationJobResponseTypeDef(BaseValidatorModel):
    Job: FraudsterRegistrationJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartFraudsterRegistrationJobResponseTypeDef(BaseValidatorModel):
    Job: FraudsterRegistrationJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpeakerEnrollmentJobResponseTypeDef(BaseValidatorModel):
    Job: SpeakerEnrollmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerEnrollmentJobResponseTypeDef(BaseValidatorModel):
    Job: SpeakerEnrollmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluateSessionResponseTypeDef(BaseValidatorModel):
    AuthenticationResult: AuthenticationResultTypeDef
    DomainId: str
    FraudDetectionResult: FraudDetectionResultTypeDef
    SessionId: str
    SessionName: str
    StreamingStatus: StreamingStatusType
    ResponseMetadata: ResponseMetadataTypeDef


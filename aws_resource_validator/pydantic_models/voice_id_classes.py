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
from aws_resource_validator.pydantic_models.voice_id_constants import *

class AssociateFraudsterRequestRequestTypeDef(BaseModel):
    DomainId: str
    FraudsterId: str
    WatchlistId: str

class FraudsterTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    GeneratedFraudsterId: Optional[str] = None
    WatchlistIds: Optional[List[str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AuthenticationConfigurationTypeDef(BaseModel):
    AcceptanceThreshold: int

class ServerSideEncryptionConfigurationTypeDef(BaseModel):
    KmsKeyId: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateWatchlistRequestRequestTypeDef(BaseModel):
    DomainId: str
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None

class WatchlistTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    DefaultWatchlist: Optional[bool] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    Name: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistId: Optional[str] = None

class DeleteDomainRequestRequestTypeDef(BaseModel):
    DomainId: str

class DeleteFraudsterRequestRequestTypeDef(BaseModel):
    DomainId: str
    FraudsterId: str

class DeleteSpeakerRequestRequestTypeDef(BaseModel):
    DomainId: str
    SpeakerId: str

class DeleteWatchlistRequestRequestTypeDef(BaseModel):
    DomainId: str
    WatchlistId: str

class DescribeDomainRequestRequestTypeDef(BaseModel):
    DomainId: str

class DescribeFraudsterRegistrationJobRequestRequestTypeDef(BaseModel):
    DomainId: str
    JobId: str

class DescribeFraudsterRequestRequestTypeDef(BaseModel):
    DomainId: str
    FraudsterId: str

class DescribeSpeakerEnrollmentJobRequestRequestTypeDef(BaseModel):
    DomainId: str
    JobId: str

class DescribeSpeakerRequestRequestTypeDef(BaseModel):
    DomainId: str
    SpeakerId: str

class SpeakerTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    CustomerSpeakerId: Optional[str] = None
    DomainId: Optional[str] = None
    GeneratedSpeakerId: Optional[str] = None
    LastAccessedAt: Optional[datetime] = None
    Status: Optional[SpeakerStatusType] = None
    UpdatedAt: Optional[datetime] = None

class DescribeWatchlistRequestRequestTypeDef(BaseModel):
    DomainId: str
    WatchlistId: str

class DisassociateFraudsterRequestRequestTypeDef(BaseModel):
    DomainId: str
    FraudsterId: str
    WatchlistId: str

class ServerSideEncryptionUpdateDetailsTypeDef(BaseModel):
    Message: Optional[str] = None
    OldKmsKeyId: Optional[str] = None
    UpdateStatus: Optional[ServerSideEncryptionUpdateStatusType] = None

class WatchlistDetailsTypeDef(BaseModel):
    DefaultWatchlistId: str

class EnrollmentJobFraudDetectionConfigTypeDef(BaseModel):
    FraudDetectionAction: Optional[FraudDetectionActionType] = None
    RiskThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None

class EvaluateSessionRequestRequestTypeDef(BaseModel):
    DomainId: str
    SessionNameOrId: str

class FailureDetailsTypeDef(BaseModel):
    Message: Optional[str] = None
    StatusCode: Optional[int] = None

class FraudDetectionConfigurationTypeDef(BaseModel):
    RiskThreshold: Optional[int] = None
    WatchlistId: Optional[str] = None

class KnownFraudsterRiskTypeDef(BaseModel):
    RiskScore: int
    GeneratedFraudsterId: Optional[str] = None

class VoiceSpoofingRiskTypeDef(BaseModel):
    RiskScore: int

class JobProgressTypeDef(BaseModel):
    PercentComplete: Optional[int] = None

class InputDataConfigTypeDef(BaseModel):
    S3Uri: str

class OutputDataConfigTypeDef(BaseModel):
    S3Uri: str
    KmsKeyId: Optional[str] = None

class RegistrationConfigTypeDef(BaseModel):
    DuplicateRegistrationAction: Optional[DuplicateRegistrationActionType] = None
    FraudsterSimilarityThreshold: Optional[int] = None
    WatchlistIds: Optional[List[str]] = None

class FraudsterSummaryTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    GeneratedFraudsterId: Optional[str] = None
    WatchlistIds: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListDomainsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFraudsterRegistrationJobsRequestRequestTypeDef(BaseModel):
    DomainId: str
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFraudstersRequestRequestTypeDef(BaseModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WatchlistId: Optional[str] = None

class ListSpeakerEnrollmentJobsRequestRequestTypeDef(BaseModel):
    DomainId: str
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSpeakersRequestRequestTypeDef(BaseModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SpeakerSummaryTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    CustomerSpeakerId: Optional[str] = None
    DomainId: Optional[str] = None
    GeneratedSpeakerId: Optional[str] = None
    LastAccessedAt: Optional[datetime] = None
    Status: Optional[SpeakerStatusType] = None
    UpdatedAt: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListWatchlistsRequestRequestTypeDef(BaseModel):
    DomainId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class WatchlistSummaryTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    DefaultWatchlist: Optional[bool] = None
    Description: Optional[str] = None
    DomainId: Optional[str] = None
    Name: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    WatchlistId: Optional[str] = None

class OptOutSpeakerRequestRequestTypeDef(BaseModel):
    DomainId: str
    SpeakerId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateWatchlistRequestRequestTypeDef(BaseModel):
    DomainId: str
    WatchlistId: str
    Description: Optional[str] = None
    Name: Optional[str] = None

class AssociateFraudsterResponseTypeDef(BaseModel):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFraudsterResponseTypeDef(BaseModel):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFraudsterResponseTypeDef(BaseModel):
    Fraudster: FraudsterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class AuthenticationResultTypeDef(BaseModel):
    AudioAggregationEndedAt: Optional[datetime] = None
    AudioAggregationStartedAt: Optional[datetime] = None
    AuthenticationResultId: Optional[str] = None
    Configuration: Optional[AuthenticationConfigurationTypeDef] = None
    CustomerSpeakerId: Optional[str] = None
    Decision: Optional[AuthenticationDecisionType] = None
    GeneratedSpeakerId: Optional[str] = None
    Score: Optional[int] = None

class UpdateDomainRequestRequestTypeDef(BaseModel):
    DomainId: str
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    Description: Optional[str] = None

class CreateDomainRequestRequestTypeDef(BaseModel):
    Name: str
    ServerSideEncryptionConfiguration: ServerSideEncryptionConfigurationTypeDef
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateWatchlistResponseTypeDef(BaseModel):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWatchlistResponseTypeDef(BaseModel):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWatchlistResponseTypeDef(BaseModel):
    Watchlist: WatchlistTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpeakerResponseTypeDef(BaseModel):
    Speaker: SpeakerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OptOutSpeakerResponseTypeDef(BaseModel):
    Speaker: SpeakerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DomainSummaryTypeDef(BaseModel):
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

class DomainTypeDef(BaseModel):
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

class EnrollmentConfigTypeDef(BaseModel):
    ExistingEnrollmentAction: Optional[ExistingEnrollmentActionType] = None
    FraudDetectionConfig: Optional[EnrollmentJobFraudDetectionConfigTypeDef] = None

class FraudRiskDetailsTypeDef(BaseModel):
    KnownFraudsterRisk: KnownFraudsterRiskTypeDef
    VoiceSpoofingRisk: VoiceSpoofingRiskTypeDef

class FraudsterRegistrationJobSummaryTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgressTypeDef] = None
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None

class SpeakerEnrollmentJobSummaryTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    DomainId: Optional[str] = None
    EndedAt: Optional[datetime] = None
    FailureDetails: Optional[FailureDetailsTypeDef] = None
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobProgress: Optional[JobProgressTypeDef] = None
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None

class FraudsterRegistrationJobTypeDef(BaseModel):
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

class StartFraudsterRegistrationJobRequestRequestTypeDef(BaseModel):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    ClientToken: Optional[str] = None
    JobName: Optional[str] = None
    RegistrationConfig: Optional[RegistrationConfigTypeDef] = None

class ListFraudstersResponseTypeDef(BaseModel):
    FraudsterSummaries: List[FraudsterSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsRequestListDomainsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFraudsterRegistrationJobsRequestListFraudsterRegistrationJobsPaginateTypeDef(BaseModel):
    DomainId: str
    JobStatus: Optional[FraudsterRegistrationJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFraudstersRequestListFraudstersPaginateTypeDef(BaseModel):
    DomainId: str
    WatchlistId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpeakerEnrollmentJobsRequestListSpeakerEnrollmentJobsPaginateTypeDef(BaseModel):
    DomainId: str
    JobStatus: Optional[SpeakerEnrollmentJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpeakersRequestListSpeakersPaginateTypeDef(BaseModel):
    DomainId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWatchlistsRequestListWatchlistsPaginateTypeDef(BaseModel):
    DomainId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSpeakersResponseTypeDef(BaseModel):
    NextToken: str
    SpeakerSummaries: List[SpeakerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListWatchlistsResponseTypeDef(BaseModel):
    NextToken: str
    WatchlistSummaries: List[WatchlistSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDomainsResponseTypeDef(BaseModel):
    DomainSummaries: List[DomainSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResponseTypeDef(BaseModel):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainResponseTypeDef(BaseModel):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainResponseTypeDef(BaseModel):
    Domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SpeakerEnrollmentJobTypeDef(BaseModel):
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

class StartSpeakerEnrollmentJobRequestRequestTypeDef(BaseModel):
    DataAccessRoleArn: str
    DomainId: str
    InputDataConfig: InputDataConfigTypeDef
    OutputDataConfig: OutputDataConfigTypeDef
    ClientToken: Optional[str] = None
    EnrollmentConfig: Optional[EnrollmentConfigTypeDef] = None
    JobName: Optional[str] = None

class FraudDetectionResultTypeDef(BaseModel):
    AudioAggregationEndedAt: Optional[datetime] = None
    AudioAggregationStartedAt: Optional[datetime] = None
    Configuration: Optional[FraudDetectionConfigurationTypeDef] = None
    Decision: Optional[FraudDetectionDecisionType] = None
    FraudDetectionResultId: Optional[str] = None
    Reasons: Optional[List[FraudDetectionReasonType]] = None
    RiskDetails: Optional[FraudRiskDetailsTypeDef] = None

class ListFraudsterRegistrationJobsResponseTypeDef(BaseModel):
    JobSummaries: List[FraudsterRegistrationJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSpeakerEnrollmentJobsResponseTypeDef(BaseModel):
    JobSummaries: List[SpeakerEnrollmentJobSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFraudsterRegistrationJobResponseTypeDef(BaseModel):
    Job: FraudsterRegistrationJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartFraudsterRegistrationJobResponseTypeDef(BaseModel):
    Job: FraudsterRegistrationJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpeakerEnrollmentJobResponseTypeDef(BaseModel):
    Job: SpeakerEnrollmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerEnrollmentJobResponseTypeDef(BaseModel):
    Job: SpeakerEnrollmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluateSessionResponseTypeDef(BaseModel):
    AuthenticationResult: AuthenticationResultTypeDef
    DomainId: str
    FraudDetectionResult: FraudDetectionResultTypeDef
    SessionId: str
    SessionName: str
    StreamingStatus: StreamingStatusType
    ResponseMetadata: ResponseMetadataTypeDef


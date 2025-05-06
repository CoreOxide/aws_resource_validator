from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.transfer.transfer_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class As2ConnectorConfig(BaseValidatorModel):
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None
    MessageSubject: Optional[str] = None
    Compression: Optional[CompressionEnumType] = None
    EncryptionAlgorithm: Optional[EncryptionAlgType] = None
    SigningAlgorithm: Optional[SigningAlgType] = None
    MdnSigningAlgorithm: Optional[MdnSigningAlgType] = None
    MdnResponse: Optional[MdnResponseType] = None
    BasicAuthSecretId: Optional[str] = None
    PreserveContentType: Optional[PreserveContentTypeType] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class ConnectorFileTransferResult(BaseValidatorModel):
    FilePath: str
    StatusCode: TransferTableStatusType
    FailureCode: Optional[str] = None
    FailureMessage: Optional[str] = None


class HomeDirectoryMapEntry(BaseValidatorModel):
    Entry: str
    Target: str
    Type: Optional[MapTypeType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CustomDirectoriesType(BaseValidatorModel):
    FailedFilesDirectory: str
    MdnFilesDirectory: str
    PayloadFilesDirectory: str
    StatusFilesDirectory: str
    TemporaryFilesDirectory: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class IdentityProviderDetails(BaseValidatorModel):
    Url: Optional[str] = None
    InvocationRole: Optional[str] = None
    DirectoryId: Optional[str] = None
    Function: Optional[str] = None
    SftpAuthenticationMethods: Optional[SftpAuthenticationMethodsType] = None


class S3StorageOptions(BaseValidatorModel):
    DirectoryListingOptimization: Optional[DirectoryListingOptimizationType] = None


class WebAppUnits(BaseValidatorModel):
    Provisioned: Optional[int] = None


class CustomStepDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Target: Optional[str] = None
    TimeoutSeconds: Optional[int] = None
    SourceFileLocation: Optional[str] = None


class DeleteAccessRequest(BaseValidatorModel):
    ServerId: str
    ExternalId: str


class DeleteAgreementRequest(BaseValidatorModel):
    AgreementId: str
    ServerId: str


class DeleteCertificateRequest(BaseValidatorModel):
    CertificateId: str


class DeleteConnectorRequest(BaseValidatorModel):
    ConnectorId: str


class DeleteHostKeyRequest(BaseValidatorModel):
    ServerId: str
    HostKeyId: str


class DeleteProfileRequest(BaseValidatorModel):
    ProfileId: str


class DeleteServerRequest(BaseValidatorModel):
    ServerId: str


class DeleteSshPublicKeyRequest(BaseValidatorModel):
    ServerId: str
    SshPublicKeyId: str
    UserName: str


class DeleteStepDetails(BaseValidatorModel):
    Name: Optional[str] = None
    SourceFileLocation: Optional[str] = None


class DeleteUserRequest(BaseValidatorModel):
    ServerId: str
    UserName: str


class DeleteWebAppCustomizationRequest(BaseValidatorModel):
    WebAppId: str


class DeleteWebAppRequest(BaseValidatorModel):
    WebAppId: str


class DeleteWorkflowRequest(BaseValidatorModel):
    WorkflowId: str


class DescribeAccessRequest(BaseValidatorModel):
    ServerId: str
    ExternalId: str


class DescribeAgreementRequest(BaseValidatorModel):
    AgreementId: str
    ServerId: str


class DescribeCertificateRequest(BaseValidatorModel):
    CertificateId: str


class DescribeConnectorRequest(BaseValidatorModel):
    ConnectorId: str


class DescribeExecutionRequest(BaseValidatorModel):
    ExecutionId: str
    WorkflowId: str


class DescribeHostKeyRequest(BaseValidatorModel):
    ServerId: str
    HostKeyId: str


class DescribeProfileRequest(BaseValidatorModel):
    ProfileId: str


class DescribeSecurityPolicyRequest(BaseValidatorModel):
    SecurityPolicyName: str


class DescribedSecurityPolicy(BaseValidatorModel):
    SecurityPolicyName: str
    Fips: Optional[bool] = None
    SshCiphers: Optional[List[str]] = None
    SshKexs: Optional[List[str]] = None
    SshMacs: Optional[List[str]] = None
    TlsCiphers: Optional[List[str]] = None
    SshHostKeyAlgorithms: Optional[List[str]] = None
    Type: Optional[SecurityPolicyResourceTypeType] = None
    Protocols: Optional[List[SecurityPolicyProtocolType]] = None


class DescribeServerRequest(BaseValidatorModel):
    ServerId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeUserRequest(BaseValidatorModel):
    ServerId: str
    UserName: str


class DescribeWebAppCustomizationRequest(BaseValidatorModel):
    WebAppId: str


class DescribedWebAppCustomization(BaseValidatorModel):
    Arn: str
    WebAppId: str
    Title: Optional[str] = None
    LogoFile: Optional[bytes] = None
    FaviconFile: Optional[bytes] = None


class DescribeWebAppRequest(BaseValidatorModel):
    WebAppId: str


class DescribeWorkflowRequest(BaseValidatorModel):
    WorkflowId: str


class PosixProfileOutput(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None


class SftpConnectorConfigOutput(BaseValidatorModel):
    UserSecretId: Optional[str] = None
    TrustedHostKeys: Optional[List[str]] = None


class LoggingConfiguration(BaseValidatorModel):
    LoggingRole: Optional[str] = None
    LogGroupName: Optional[str] = None


class DescribedIdentityCenterConfig(BaseValidatorModel):
    ApplicationArn: Optional[str] = None
    InstanceArn: Optional[str] = None
    Role: Optional[str] = None


class EndpointDetailsOutput(BaseValidatorModel):
    AddressAllocationIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None


class ProtocolDetailsOutput(BaseValidatorModel):
    PassiveIp: Optional[str] = None
    TlsSessionResumptionMode: Optional[TlsSessionResumptionModeType] = None
    SetStatOption: Optional[SetStatOptionType] = None
    As2Transports: Optional[List[Literal['HTTP']]] = None


class SshPublicKey(BaseValidatorModel):
    DateImported: datetime
    SshPublicKeyBody: str
    SshPublicKeyId: str


class EfsFileLocation(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    Path: Optional[str] = None


class EndpointDetails(BaseValidatorModel):
    AddressAllocationIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None


class ExecutionError(BaseValidatorModel):
    Type: ExecutionErrorTypeType
    Message: str


class S3FileLocation(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    Etag: Optional[str] = None


class IdentityCenterConfig(BaseValidatorModel):
    InstanceArn: Optional[str] = None
    Role: Optional[str] = None

Timestamp = Union[datetime, str]


class ImportSshPublicKeyRequest(BaseValidatorModel):
    ServerId: str
    SshPublicKeyBody: str
    UserName: str


class S3InputFileLocation(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccessesRequest(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedAccess(BaseValidatorModel):
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Role: Optional[str] = None
    ExternalId: Optional[str] = None


class ListAgreementsRequest(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedAgreement(BaseValidatorModel):
    Arn: Optional[str] = None
    AgreementId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    ServerId: Optional[str] = None
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None


class ListCertificatesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedCertificate(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateId: Optional[str] = None
    Usage: Optional[CertificateUsageTypeType] = None
    Status: Optional[CertificateStatusTypeType] = None
    ActiveDate: Optional[datetime] = None
    InactiveDate: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None
    Description: Optional[str] = None


class ListConnectorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedConnector(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorId: Optional[str] = None
    Url: Optional[str] = None


class ListExecutionsRequest(BaseValidatorModel):
    WorkflowId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFileTransferResultsRequest(BaseValidatorModel):
    ConnectorId: str
    TransferId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHostKeysRequest(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedHostKey(BaseValidatorModel):
    Arn: str
    HostKeyId: Optional[str] = None
    Fingerprint: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    DateImported: Optional[datetime] = None


class ListProfilesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None


class ListedProfile(BaseValidatorModel):
    Arn: Optional[str] = None
    ProfileId: Optional[str] = None
    As2Id: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None


class ListSecurityPoliciesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedServer(BaseValidatorModel):
    Arn: str
    Domain: Optional[DomainType] = None
    IdentityProviderType: Optional[IdentityProviderTypeType] = None
    EndpointType: Optional[EndpointTypeType] = None
    LoggingRole: Optional[str] = None
    ServerId: Optional[str] = None
    State: Optional[StateType] = None
    UserCount: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListUsersRequest(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedUser(BaseValidatorModel):
    Arn: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Role: Optional[str] = None
    SshPublicKeyCount: Optional[int] = None
    UserName: Optional[str] = None


class ListWebAppsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedWebApp(BaseValidatorModel):
    Arn: str
    WebAppId: str
    AccessEndpoint: Optional[str] = None
    WebAppEndpoint: Optional[str] = None


class ListWorkflowsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedWorkflow(BaseValidatorModel):
    WorkflowId: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None


class PosixProfile(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None


class ProtocolDetails(BaseValidatorModel):
    PassiveIp: Optional[str] = None
    TlsSessionResumptionMode: Optional[TlsSessionResumptionModeType] = None
    SetStatOption: Optional[SetStatOptionType] = None
    As2Transports: Optional[List[Literal['HTTP']]] = None


class S3Tag(BaseValidatorModel):
    Key: str
    Value: str


class SendWorkflowStepStateRequest(BaseValidatorModel):
    WorkflowId: str
    ExecutionId: str
    Token: str
    Status: CustomStepStatusType


class UserDetails(BaseValidatorModel):
    UserName: str
    ServerId: str
    SessionId: Optional[str] = None


class SftpConnectorConfig(BaseValidatorModel):
    UserSecretId: Optional[str] = None
    TrustedHostKeys: Optional[List[str]] = None


class StartDirectoryListingRequest(BaseValidatorModel):
    ConnectorId: str
    RemoteDirectoryPath: str
    OutputDirectoryPath: str
    MaxItems: Optional[int] = None


class StartFileTransferRequest(BaseValidatorModel):
    ConnectorId: str
    SendFilePaths: Optional[List[str]] = None
    RetrieveFilePaths: Optional[List[str]] = None
    LocalDirectoryPath: Optional[str] = None
    RemoteDirectoryPath: Optional[str] = None


class StartServerRequest(BaseValidatorModel):
    ServerId: str


class StopServerRequest(BaseValidatorModel):
    ServerId: str


class TestConnectionRequest(BaseValidatorModel):
    ConnectorId: str


class TestIdentityProviderRequest(BaseValidatorModel):
    ServerId: str
    UserName: str
    ServerProtocol: Optional[ProtocolType] = None
    SourceIp: Optional[str] = None
    UserPassword: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    Arn: str
    TagKeys: List[str]


class UpdateHostKeyRequest(BaseValidatorModel):
    ServerId: str
    HostKeyId: str
    Description: str


class UpdateProfileRequest(BaseValidatorModel):
    ProfileId: str
    CertificateIds: Optional[List[str]] = None


class UpdateWebAppIdentityCenterConfig(BaseValidatorModel):
    Role: Optional[str] = None


class WorkflowDetail(BaseValidatorModel):
    WorkflowId: str
    ExecutionRole: str


class UpdateWebAppCustomizationRequest(BaseValidatorModel):
    WebAppId: str
    Title: Optional[str] = None
    LogoFile: Optional[Blob] = None
    FaviconFile: Optional[Blob] = None


class CreateAccessResponse(BaseValidatorModel):
    ServerId: str
    ExternalId: str
    ResponseMetadata: ResponseMetadata


class CreateAgreementResponse(BaseValidatorModel):
    AgreementId: str
    ResponseMetadata: ResponseMetadata


class CreateConnectorResponse(BaseValidatorModel):
    ConnectorId: str
    ResponseMetadata: ResponseMetadata


class CreateProfileResponse(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadata


class CreateServerResponse(BaseValidatorModel):
    ServerId: str
    ResponseMetadata: ResponseMetadata


class CreateUserResponse(BaseValidatorModel):
    ServerId: str
    UserName: str
    ResponseMetadata: ResponseMetadata


class CreateWebAppResponse(BaseValidatorModel):
    WebAppId: str
    ResponseMetadata: ResponseMetadata


class CreateWorkflowResponse(BaseValidatorModel):
    WorkflowId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ImportCertificateResponse(BaseValidatorModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadata


class ImportHostKeyResponse(BaseValidatorModel):
    ServerId: str
    HostKeyId: str
    ResponseMetadata: ResponseMetadata


class ImportSshPublicKeyResponse(BaseValidatorModel):
    ServerId: str
    SshPublicKeyId: str
    UserName: str
    ResponseMetadata: ResponseMetadata


class ListFileTransferResultsResponse(BaseValidatorModel):
    FileTransferResults: List[ConnectorFileTransferResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSecurityPoliciesResponse(BaseValidatorModel):
    SecurityPolicyNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartDirectoryListingResponse(BaseValidatorModel):
    ListingId: str
    OutputFileName: str
    ResponseMetadata: ResponseMetadata


class StartFileTransferResponse(BaseValidatorModel):
    TransferId: str
    ResponseMetadata: ResponseMetadata


class TestConnectionResponse(BaseValidatorModel):
    ConnectorId: str
    Status: str
    StatusMessage: str
    ResponseMetadata: ResponseMetadata


class TestIdentityProviderResponse(BaseValidatorModel):
    Response: str
    StatusCode: int
    Message: str
    Url: str
    ResponseMetadata: ResponseMetadata


class UpdateAccessResponse(BaseValidatorModel):
    ServerId: str
    ExternalId: str
    ResponseMetadata: ResponseMetadata


class UpdateAgreementResponse(BaseValidatorModel):
    AgreementId: str
    ResponseMetadata: ResponseMetadata


class UpdateCertificateResponse(BaseValidatorModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadata


class UpdateConnectorResponse(BaseValidatorModel):
    ConnectorId: str
    ResponseMetadata: ResponseMetadata


class UpdateHostKeyResponse(BaseValidatorModel):
    ServerId: str
    HostKeyId: str
    ResponseMetadata: ResponseMetadata


class UpdateProfileResponse(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadata


class UpdateServerResponse(BaseValidatorModel):
    ServerId: str
    ResponseMetadata: ResponseMetadata


class UpdateUserResponse(BaseValidatorModel):
    ServerId: str
    UserName: str
    ResponseMetadata: ResponseMetadata


class UpdateWebAppCustomizationResponse(BaseValidatorModel):
    WebAppId: str
    ResponseMetadata: ResponseMetadata


class UpdateWebAppResponse(BaseValidatorModel):
    WebAppId: str
    ResponseMetadata: ResponseMetadata


class UpdateAgreementRequest(BaseValidatorModel):
    AgreementId: str
    ServerId: str
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None
    BaseDirectory: Optional[str] = None
    AccessRole: Optional[str] = None
    PreserveFilename: Optional[PreserveFilenameTypeType] = None
    EnforceMessageSigning: Optional[EnforceMessageSigningTypeType] = None
    CustomDirectories: Optional[CustomDirectoriesType] = None


class CreateAgreementRequest(BaseValidatorModel):
    ServerId: str
    LocalProfileId: str
    PartnerProfileId: str
    AccessRole: str
    Description: Optional[str] = None
    BaseDirectory: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    Tags: Optional[List[Tag]] = None
    PreserveFilename: Optional[PreserveFilenameTypeType] = None
    EnforceMessageSigning: Optional[EnforceMessageSigningTypeType] = None
    CustomDirectories: Optional[CustomDirectoriesType] = None


class CreateProfileRequest(BaseValidatorModel):
    As2Id: str
    ProfileType: ProfileTypeType
    CertificateIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


class DescribedAgreement(BaseValidatorModel):
    Arn: str
    AgreementId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    ServerId: Optional[str] = None
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None
    BaseDirectory: Optional[str] = None
    AccessRole: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    PreserveFilename: Optional[PreserveFilenameTypeType] = None
    EnforceMessageSigning: Optional[EnforceMessageSigningTypeType] = None
    CustomDirectories: Optional[CustomDirectoriesType] = None


class DescribedCertificate(BaseValidatorModel):
    Arn: str
    CertificateId: Optional[str] = None
    Usage: Optional[CertificateUsageTypeType] = None
    Status: Optional[CertificateStatusTypeType] = None
    Certificate: Optional[str] = None
    CertificateChain: Optional[str] = None
    ActiveDate: Optional[datetime] = None
    InactiveDate: Optional[datetime] = None
    Serial: Optional[str] = None
    NotBeforeDate: Optional[datetime] = None
    NotAfterDate: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DescribedHostKey(BaseValidatorModel):
    Arn: str
    HostKeyId: Optional[str] = None
    HostKeyFingerprint: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    DateImported: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class DescribedProfile(BaseValidatorModel):
    Arn: str
    ProfileId: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None
    As2Id: Optional[str] = None
    CertificateIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


class ImportHostKeyRequest(BaseValidatorModel):
    ServerId: str
    HostKeyBody: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Arn: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    Arn: str
    Tags: List[Tag]


class DescribeSecurityPolicyResponse(BaseValidatorModel):
    SecurityPolicy: DescribedSecurityPolicy
    ResponseMetadata: ResponseMetadata


class DescribeServerRequestWaitExtra(BaseValidatorModel):
    ServerId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeServerRequestWait(BaseValidatorModel):
    ServerId: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeWebAppCustomizationResponse(BaseValidatorModel):
    WebAppCustomization: DescribedWebAppCustomization
    ResponseMetadata: ResponseMetadata


class DescribedAccess(BaseValidatorModel):
    HomeDirectory: Optional[str] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntry]] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileOutput] = None
    Role: Optional[str] = None
    ExternalId: Optional[str] = None


class DescribedConnector(BaseValidatorModel):
    Arn: str
    ConnectorId: Optional[str] = None
    Url: Optional[str] = None
    As2Config: Optional[As2ConnectorConfig] = None
    AccessRole: Optional[str] = None
    LoggingRole: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SftpConfig: Optional[SftpConnectorConfigOutput] = None
    ServiceManagedEgressIpAddresses: Optional[List[str]] = None
    SecurityPolicyName: Optional[str] = None


class DescribedWebAppIdentityProviderDetails(BaseValidatorModel):
    IdentityCenterConfig: Optional[DescribedIdentityCenterConfig] = None


class DescribedUser(BaseValidatorModel):
    Arn: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntry]] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileOutput] = None
    Role: Optional[str] = None
    SshPublicKeys: Optional[List[SshPublicKey]] = None
    Tags: Optional[List[Tag]] = None
    UserName: Optional[str] = None

EndpointDetailsUnion = Union[EndpointDetails, EndpointDetailsOutput]


class ExecutionStepResult(BaseValidatorModel):
    StepType: Optional[WorkflowStepTypeType] = None
    Outputs: Optional[str] = None
    Error: Optional[ExecutionError] = None


class FileLocation(BaseValidatorModel):
    S3FileLocation: Optional[S3FileLocation] = None
    EfsFileLocation: Optional[EfsFileLocation] = None


class WebAppIdentityProviderDetails(BaseValidatorModel):
    IdentityCenterConfig: Optional[IdentityCenterConfig] = None


class ImportCertificateRequest(BaseValidatorModel):
    Usage: CertificateUsageTypeType
    Certificate: str
    CertificateChain: Optional[str] = None
    PrivateKey: Optional[str] = None
    ActiveDate: Optional[Timestamp] = None
    InactiveDate: Optional[Timestamp] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateCertificateRequest(BaseValidatorModel):
    CertificateId: str
    ActiveDate: Optional[Timestamp] = None
    InactiveDate: Optional[Timestamp] = None
    Description: Optional[str] = None


class InputFileLocation(BaseValidatorModel):
    S3FileLocation: Optional[S3InputFileLocation] = None
    EfsFileLocation: Optional[EfsFileLocation] = None


class ListAccessesRequestPaginate(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAgreementsRequestPaginate(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCertificatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConnectorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExecutionsRequestPaginate(BaseValidatorModel):
    WorkflowId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFileTransferResultsRequestPaginate(BaseValidatorModel):
    ConnectorId: str
    TransferId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProfilesRequestPaginate(BaseValidatorModel):
    ProfileType: Optional[ProfileTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityPoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    Arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWebAppsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccessesResponse(BaseValidatorModel):
    ServerId: str
    Accesses: List[ListedAccess]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAgreementsResponse(BaseValidatorModel):
    Agreements: List[ListedAgreement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCertificatesResponse(BaseValidatorModel):
    Certificates: List[ListedCertificate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListConnectorsResponse(BaseValidatorModel):
    Connectors: List[ListedConnector]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListHostKeysResponse(BaseValidatorModel):
    ServerId: str
    HostKeys: List[ListedHostKey]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProfilesResponse(BaseValidatorModel):
    Profiles: List[ListedProfile]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListServersResponse(BaseValidatorModel):
    Servers: List[ListedServer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUsersResponse(BaseValidatorModel):
    ServerId: str
    Users: List[ListedUser]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWebAppsResponse(BaseValidatorModel):
    WebApps: List[ListedWebApp]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWorkflowsResponse(BaseValidatorModel):
    Workflows: List[ListedWorkflow]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

PosixProfileUnion = Union[PosixProfile, PosixProfileOutput]

ProtocolDetailsUnion = Union[ProtocolDetails, ProtocolDetailsOutput]


class TagStepDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Tags: Optional[List[S3Tag]] = None
    SourceFileLocation: Optional[str] = None


class TagStepDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Tags: Optional[List[S3Tag]] = None
    SourceFileLocation: Optional[str] = None


class ServiceMetadata(BaseValidatorModel):
    UserDetails: UserDetails

SftpConnectorConfigUnion = Union[SftpConnectorConfig, SftpConnectorConfigOutput]


class UpdateWebAppIdentityProviderDetails(BaseValidatorModel):
    IdentityCenterConfig: Optional[UpdateWebAppIdentityCenterConfig] = None


class WorkflowDetailsOutput(BaseValidatorModel):
    OnUpload: Optional[List[WorkflowDetail]] = None
    OnPartialUpload: Optional[List[WorkflowDetail]] = None


class WorkflowDetails(BaseValidatorModel):
    OnUpload: Optional[List[WorkflowDetail]] = None
    OnPartialUpload: Optional[List[WorkflowDetail]] = None


class DescribeAgreementResponse(BaseValidatorModel):
    Agreement: DescribedAgreement
    ResponseMetadata: ResponseMetadata


class DescribeCertificateResponse(BaseValidatorModel):
    Certificate: DescribedCertificate
    ResponseMetadata: ResponseMetadata


class DescribeHostKeyResponse(BaseValidatorModel):
    HostKey: DescribedHostKey
    ResponseMetadata: ResponseMetadata


class DescribeProfileResponse(BaseValidatorModel):
    Profile: DescribedProfile
    ResponseMetadata: ResponseMetadata


class DescribeAccessResponse(BaseValidatorModel):
    ServerId: str
    Access: DescribedAccess
    ResponseMetadata: ResponseMetadata


class DescribeConnectorResponse(BaseValidatorModel):
    Connector: DescribedConnector
    ResponseMetadata: ResponseMetadata


class DescribedWebApp(BaseValidatorModel):
    Arn: str
    WebAppId: str
    DescribedIdentityProviderDetails: Optional[DescribedWebAppIdentityProviderDetails] = None
    AccessEndpoint: Optional[str] = None
    WebAppEndpoint: Optional[str] = None
    WebAppUnits: Optional[WebAppUnits] = None
    Tags: Optional[List[Tag]] = None


class DescribeUserResponse(BaseValidatorModel):
    ServerId: str
    User: DescribedUser
    ResponseMetadata: ResponseMetadata


class ExecutionResults(BaseValidatorModel):
    Steps: Optional[List[ExecutionStepResult]] = None
    OnExceptionSteps: Optional[List[ExecutionStepResult]] = None


class CreateWebAppRequest(BaseValidatorModel):
    IdentityProviderDetails: WebAppIdentityProviderDetails
    AccessEndpoint: Optional[str] = None
    WebAppUnits: Optional[WebAppUnits] = None
    Tags: Optional[List[Tag]] = None


class CopyStepDetails(BaseValidatorModel):
    Name: Optional[str] = None
    DestinationFileLocation: Optional[InputFileLocation] = None
    OverwriteExisting: Optional[OverwriteExistingType] = None
    SourceFileLocation: Optional[str] = None


class DecryptStepDetails(BaseValidatorModel):
    Type: Literal['PGP']
    DestinationFileLocation: InputFileLocation
    Name: Optional[str] = None
    SourceFileLocation: Optional[str] = None
    OverwriteExisting: Optional[OverwriteExistingType] = None


class CreateAccessRequest(BaseValidatorModel):
    Role: str
    ServerId: str
    ExternalId: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntry]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileUnion] = None


class CreateUserRequest(BaseValidatorModel):
    Role: str
    ServerId: str
    UserName: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntry]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileUnion] = None
    SshPublicKeyBody: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class UpdateAccessRequest(BaseValidatorModel):
    ServerId: str
    ExternalId: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntry]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileUnion] = None
    Role: Optional[str] = None


class UpdateUserRequest(BaseValidatorModel):
    ServerId: str
    UserName: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntry]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileUnion] = None
    Role: Optional[str] = None

TagStepDetailsUnion = Union[TagStepDetails, TagStepDetailsOutput]


class ListedExecution(BaseValidatorModel):
    ExecutionId: Optional[str] = None
    InitialFileLocation: Optional[FileLocation] = None
    ServiceMetadata: Optional[ServiceMetadata] = None
    Status: Optional[ExecutionStatusType] = None


class CreateConnectorRequest(BaseValidatorModel):
    Url: str
    AccessRole: str
    As2Config: Optional[As2ConnectorConfig] = None
    LoggingRole: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SftpConfig: Optional[SftpConnectorConfigUnion] = None
    SecurityPolicyName: Optional[str] = None


class UpdateConnectorRequest(BaseValidatorModel):
    ConnectorId: str
    Url: Optional[str] = None
    As2Config: Optional[As2ConnectorConfig] = None
    AccessRole: Optional[str] = None
    LoggingRole: Optional[str] = None
    SftpConfig: Optional[SftpConnectorConfigUnion] = None
    SecurityPolicyName: Optional[str] = None


class UpdateWebAppRequest(BaseValidatorModel):
    WebAppId: str
    IdentityProviderDetails: Optional[UpdateWebAppIdentityProviderDetails] = None
    AccessEndpoint: Optional[str] = None
    WebAppUnits: Optional[WebAppUnits] = None


class DescribedServer(BaseValidatorModel):
    Arn: str
    Certificate: Optional[str] = None
    ProtocolDetails: Optional[ProtocolDetailsOutput] = None
    Domain: Optional[DomainType] = None
    EndpointDetails: Optional[EndpointDetailsOutput] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostKeyFingerprint: Optional[str] = None
    IdentityProviderDetails: Optional[IdentityProviderDetails] = None
    IdentityProviderType: Optional[IdentityProviderTypeType] = None
    LoggingRole: Optional[str] = None
    PostAuthenticationLoginBanner: Optional[str] = None
    PreAuthenticationLoginBanner: Optional[str] = None
    Protocols: Optional[List[ProtocolType]] = None
    SecurityPolicyName: Optional[str] = None
    ServerId: Optional[str] = None
    State: Optional[StateType] = None
    Tags: Optional[List[Tag]] = None
    UserCount: Optional[int] = None
    WorkflowDetails: Optional[WorkflowDetailsOutput] = None
    StructuredLogDestinations: Optional[List[str]] = None
    S3StorageOptions: Optional[S3StorageOptions] = None
    As2ServiceManagedEgressIpAddresses: Optional[List[str]] = None

WorkflowDetailsUnion = Union[WorkflowDetails, WorkflowDetailsOutput]


class DescribeWebAppResponse(BaseValidatorModel):
    WebApp: DescribedWebApp
    ResponseMetadata: ResponseMetadata


class DescribedExecution(BaseValidatorModel):
    ExecutionId: Optional[str] = None
    InitialFileLocation: Optional[FileLocation] = None
    ServiceMetadata: Optional[ServiceMetadata] = None
    ExecutionRole: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfiguration] = None
    PosixProfile: Optional[PosixProfileOutput] = None
    Status: Optional[ExecutionStatusType] = None
    Results: Optional[ExecutionResults] = None


class WorkflowStepOutput(BaseValidatorModel):
    Type: Optional[WorkflowStepTypeType] = None
    CopyStepDetails: Optional[CopyStepDetails] = None
    CustomStepDetails: Optional[CustomStepDetails] = None
    DeleteStepDetails: Optional[DeleteStepDetails] = None
    TagStepDetails: Optional[TagStepDetailsOutput] = None
    DecryptStepDetails: Optional[DecryptStepDetails] = None


class WorkflowStep(BaseValidatorModel):
    Type: Optional[WorkflowStepTypeType] = None
    CopyStepDetails: Optional[CopyStepDetails] = None
    CustomStepDetails: Optional[CustomStepDetails] = None
    DeleteStepDetails: Optional[DeleteStepDetails] = None
    TagStepDetails: Optional[TagStepDetailsUnion] = None
    DecryptStepDetails: Optional[DecryptStepDetails] = None


class ListExecutionsResponse(BaseValidatorModel):
    WorkflowId: str
    Executions: List[ListedExecution]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeServerResponse(BaseValidatorModel):
    Server: DescribedServer
    ResponseMetadata: ResponseMetadata


class CreateServerRequest(BaseValidatorModel):
    Certificate: Optional[str] = None
    Domain: Optional[DomainType] = None
    EndpointDetails: Optional[EndpointDetailsUnion] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostKey: Optional[str] = None
    IdentityProviderDetails: Optional[IdentityProviderDetails] = None
    IdentityProviderType: Optional[IdentityProviderTypeType] = None
    LoggingRole: Optional[str] = None
    PostAuthenticationLoginBanner: Optional[str] = None
    PreAuthenticationLoginBanner: Optional[str] = None
    Protocols: Optional[List[ProtocolType]] = None
    ProtocolDetails: Optional[ProtocolDetailsUnion] = None
    SecurityPolicyName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    WorkflowDetails: Optional[WorkflowDetailsUnion] = None
    StructuredLogDestinations: Optional[List[str]] = None
    S3StorageOptions: Optional[S3StorageOptions] = None


class UpdateServerRequest(BaseValidatorModel):
    ServerId: str
    Certificate: Optional[str] = None
    ProtocolDetails: Optional[ProtocolDetailsUnion] = None
    EndpointDetails: Optional[EndpointDetailsUnion] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostKey: Optional[str] = None
    IdentityProviderDetails: Optional[IdentityProviderDetails] = None
    LoggingRole: Optional[str] = None
    PostAuthenticationLoginBanner: Optional[str] = None
    PreAuthenticationLoginBanner: Optional[str] = None
    Protocols: Optional[List[ProtocolType]] = None
    SecurityPolicyName: Optional[str] = None
    WorkflowDetails: Optional[WorkflowDetailsUnion] = None
    StructuredLogDestinations: Optional[List[str]] = None
    S3StorageOptions: Optional[S3StorageOptions] = None


class DescribeExecutionResponse(BaseValidatorModel):
    WorkflowId: str
    Execution: DescribedExecution
    ResponseMetadata: ResponseMetadata


class DescribedWorkflow(BaseValidatorModel):
    Arn: str
    Description: Optional[str] = None
    Steps: Optional[List[WorkflowStepOutput]] = None
    OnExceptionSteps: Optional[List[WorkflowStepOutput]] = None
    WorkflowId: Optional[str] = None
    Tags: Optional[List[Tag]] = None

WorkflowStepUnion = Union[WorkflowStep, WorkflowStepOutput]


class DescribeWorkflowResponse(BaseValidatorModel):
    Workflow: DescribedWorkflow
    ResponseMetadata: ResponseMetadata


class CreateWorkflowRequest(BaseValidatorModel):
    Steps: List[WorkflowStepUnion]
    Description: Optional[str] = None
    OnExceptionSteps: Optional[List[WorkflowStepUnion]] = None
    Tags: Optional[List[Tag]] = None
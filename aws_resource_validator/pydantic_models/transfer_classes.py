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
from aws_resource_validator.pydantic_models.transfer_constants import *

class As2ConnectorConfigTypeDef(BaseModel):
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None
    MessageSubject: Optional[str] = None
    Compression: Optional[CompressionEnumType] = None
    EncryptionAlgorithm: Optional[EncryptionAlgType] = None
    SigningAlgorithm: Optional[SigningAlgType] = None
    MdnSigningAlgorithm: Optional[MdnSigningAlgType] = None
    MdnResponse: Optional[MdnResponseType] = None
    BasicAuthSecretId: Optional[str] = None

class HomeDirectoryMapEntryTypeDef(BaseModel):
    Entry: str
    Target: str
    Type: Optional[MapTypeType] = None

class PosixProfileTypeDef(BaseModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[Sequence[int]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class SftpConnectorConfigTypeDef(BaseModel):
    UserSecretId: Optional[str] = None
    TrustedHostKeys: Optional[Sequence[str]] = None

class EndpointDetailsTypeDef(BaseModel):
    AddressAllocationIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class IdentityProviderDetailsTypeDef(BaseModel):
    Url: Optional[str] = None
    InvocationRole: Optional[str] = None
    DirectoryId: Optional[str] = None
    Function: Optional[str] = None
    SftpAuthenticationMethods: Optional[SftpAuthenticationMethodsType] = None

class ProtocolDetailsTypeDef(BaseModel):
    PassiveIp: Optional[str] = None
    TlsSessionResumptionMode: Optional[TlsSessionResumptionModeType] = None
    SetStatOption: Optional[SetStatOptionType] = None
    As2Transports: Optional[Sequence[Literal["HTTP"]]] = None

class S3StorageOptionsTypeDef(BaseModel):
    DirectoryListingOptimization: Optional[DirectoryListingOptimizationType] = None

class CustomStepDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Target: Optional[str] = None
    TimeoutSeconds: Optional[int] = None
    SourceFileLocation: Optional[str] = None

class DeleteAccessRequestRequestTypeDef(BaseModel):
    ServerId: str
    ExternalId: str

class DeleteAgreementRequestRequestTypeDef(BaseModel):
    AgreementId: str
    ServerId: str

class DeleteCertificateRequestRequestTypeDef(BaseModel):
    CertificateId: str

class DeleteConnectorRequestRequestTypeDef(BaseModel):
    ConnectorId: str

class DeleteHostKeyRequestRequestTypeDef(BaseModel):
    ServerId: str
    HostKeyId: str

class DeleteProfileRequestRequestTypeDef(BaseModel):
    ProfileId: str

class DeleteServerRequestRequestTypeDef(BaseModel):
    ServerId: str

class DeleteSshPublicKeyRequestRequestTypeDef(BaseModel):
    ServerId: str
    SshPublicKeyId: str
    UserName: str

class DeleteStepDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    SourceFileLocation: Optional[str] = None

class DeleteUserRequestRequestTypeDef(BaseModel):
    ServerId: str
    UserName: str

class DeleteWorkflowRequestRequestTypeDef(BaseModel):
    WorkflowId: str

class DescribeAccessRequestRequestTypeDef(BaseModel):
    ServerId: str
    ExternalId: str

class DescribeAgreementRequestRequestTypeDef(BaseModel):
    AgreementId: str
    ServerId: str

class DescribeCertificateRequestRequestTypeDef(BaseModel):
    CertificateId: str

class DescribeConnectorRequestRequestTypeDef(BaseModel):
    ConnectorId: str

class DescribeExecutionRequestRequestTypeDef(BaseModel):
    ExecutionId: str
    WorkflowId: str

class DescribeHostKeyRequestRequestTypeDef(BaseModel):
    ServerId: str
    HostKeyId: str

class DescribeProfileRequestRequestTypeDef(BaseModel):
    ProfileId: str

class DescribeSecurityPolicyRequestRequestTypeDef(BaseModel):
    SecurityPolicyName: str

class DescribedSecurityPolicyTypeDef(BaseModel):
    SecurityPolicyName: str
    Fips: Optional[bool] = None
    SshCiphers: Optional[List[str]] = None
    SshKexs: Optional[List[str]] = None
    SshMacs: Optional[List[str]] = None
    TlsCiphers: Optional[List[str]] = None
    SshHostKeyAlgorithms: Optional[List[str]] = None
    Type: Optional[SecurityPolicyResourceTypeType] = None
    Protocols: Optional[List[SecurityPolicyProtocolType]] = None

class DescribeServerRequestRequestTypeDef(BaseModel):
    ServerId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeUserRequestRequestTypeDef(BaseModel):
    ServerId: str
    UserName: str

class DescribeWorkflowRequestRequestTypeDef(BaseModel):
    WorkflowId: str

class PosixProfileOutputTypeDef(BaseModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None

class SftpConnectorConfigOutputTypeDef(BaseModel):
    UserSecretId: Optional[str] = None
    TrustedHostKeys: Optional[List[str]] = None

class LoggingConfigurationTypeDef(BaseModel):
    LoggingRole: Optional[str] = None
    LogGroupName: Optional[str] = None

class EndpointDetailsOutputTypeDef(BaseModel):
    AddressAllocationIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None

class ProtocolDetailsOutputTypeDef(BaseModel):
    PassiveIp: Optional[str] = None
    TlsSessionResumptionMode: Optional[TlsSessionResumptionModeType] = None
    SetStatOption: Optional[SetStatOptionType] = None
    As2Transports: Optional[List[Literal["HTTP"]]] = None

class SshPublicKeyTypeDef(BaseModel):
    DateImported: datetime
    SshPublicKeyBody: str
    SshPublicKeyId: str

class EfsFileLocationTypeDef(BaseModel):
    FileSystemId: Optional[str] = None
    Path: Optional[str] = None

class ExecutionErrorTypeDef(BaseModel):
    Type: ExecutionErrorTypeType
    Message: str

class S3FileLocationTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    Etag: Optional[str] = None

class ImportSshPublicKeyRequestRequestTypeDef(BaseModel):
    ServerId: str
    SshPublicKeyBody: str
    UserName: str

class S3InputFileLocationTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessesRequestRequestTypeDef(BaseModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedAccessTypeDef(BaseModel):
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Role: Optional[str] = None
    ExternalId: Optional[str] = None

class ListAgreementsRequestRequestTypeDef(BaseModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedAgreementTypeDef(BaseModel):
    Arn: Optional[str] = None
    AgreementId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    ServerId: Optional[str] = None
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None

class ListCertificatesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedCertificateTypeDef(BaseModel):
    Arn: Optional[str] = None
    CertificateId: Optional[str] = None
    Usage: Optional[CertificateUsageTypeType] = None
    Status: Optional[CertificateStatusTypeType] = None
    ActiveDate: Optional[datetime] = None
    InactiveDate: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None
    Description: Optional[str] = None

class ListConnectorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedConnectorTypeDef(BaseModel):
    Arn: Optional[str] = None
    ConnectorId: Optional[str] = None
    Url: Optional[str] = None

class ListExecutionsRequestRequestTypeDef(BaseModel):
    WorkflowId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHostKeysRequestRequestTypeDef(BaseModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedHostKeyTypeDef(BaseModel):
    Arn: str
    HostKeyId: Optional[str] = None
    Fingerprint: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    DateImported: Optional[datetime] = None

class ListProfilesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None

class ListedProfileTypeDef(BaseModel):
    Arn: Optional[str] = None
    ProfileId: Optional[str] = None
    As2Id: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None

class ListSecurityPoliciesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedServerTypeDef(BaseModel):
    Arn: str
    Domain: Optional[DomainType] = None
    IdentityProviderType: Optional[IdentityProviderTypeType] = None
    EndpointType: Optional[EndpointTypeType] = None
    LoggingRole: Optional[str] = None
    ServerId: Optional[str] = None
    State: Optional[StateType] = None
    UserCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListUsersRequestRequestTypeDef(BaseModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedUserTypeDef(BaseModel):
    Arn: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Role: Optional[str] = None
    SshPublicKeyCount: Optional[int] = None
    UserName: Optional[str] = None

class ListWorkflowsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedWorkflowTypeDef(BaseModel):
    WorkflowId: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None

class S3TagTypeDef(BaseModel):
    Key: str
    Value: str

class SendWorkflowStepStateRequestRequestTypeDef(BaseModel):
    WorkflowId: str
    ExecutionId: str
    Token: str
    Status: CustomStepStatusType

class UserDetailsTypeDef(BaseModel):
    UserName: str
    ServerId: str
    SessionId: Optional[str] = None

class StartDirectoryListingRequestRequestTypeDef(BaseModel):
    ConnectorId: str
    RemoteDirectoryPath: str
    OutputDirectoryPath: str
    MaxItems: Optional[int] = None

class StartFileTransferRequestRequestTypeDef(BaseModel):
    ConnectorId: str
    SendFilePaths: Optional[Sequence[str]] = None
    RetrieveFilePaths: Optional[Sequence[str]] = None
    LocalDirectoryPath: Optional[str] = None
    RemoteDirectoryPath: Optional[str] = None

class StartServerRequestRequestTypeDef(BaseModel):
    ServerId: str

class StopServerRequestRequestTypeDef(BaseModel):
    ServerId: str

class TestConnectionRequestRequestTypeDef(BaseModel):
    ConnectorId: str

class TestIdentityProviderRequestRequestTypeDef(BaseModel):
    ServerId: str
    UserName: str
    ServerProtocol: Optional[ProtocolType] = None
    SourceIp: Optional[str] = None
    UserPassword: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    TagKeys: Sequence[str]

class UpdateAgreementRequestRequestTypeDef(BaseModel):
    AgreementId: str
    ServerId: str
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None
    BaseDirectory: Optional[str] = None
    AccessRole: Optional[str] = None

class UpdateHostKeyRequestRequestTypeDef(BaseModel):
    ServerId: str
    HostKeyId: str
    Description: str

class UpdateProfileRequestRequestTypeDef(BaseModel):
    ProfileId: str
    CertificateIds: Optional[Sequence[str]] = None

class WorkflowDetailTypeDef(BaseModel):
    WorkflowId: str
    ExecutionRole: str

class CreateAccessRequestRequestTypeDef(BaseModel):
    Role: str
    ServerId: str
    ExternalId: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileTypeDef] = None

class UpdateAccessRequestRequestTypeDef(BaseModel):
    ServerId: str
    ExternalId: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileTypeDef] = None
    Role: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseModel):
    ServerId: str
    UserName: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileTypeDef] = None
    Role: Optional[str] = None

class CreateAccessResponseTypeDef(BaseModel):
    ServerId: str
    ExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgreementResponseTypeDef(BaseModel):
    AgreementId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorResponseTypeDef(BaseModel):
    ConnectorId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileResponseTypeDef(BaseModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServerResponseTypeDef(BaseModel):
    ServerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseModel):
    ServerId: str
    UserName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowResponseTypeDef(BaseModel):
    WorkflowId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ImportCertificateResponseTypeDef(BaseModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportHostKeyResponseTypeDef(BaseModel):
    ServerId: str
    HostKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSshPublicKeyResponseTypeDef(BaseModel):
    ServerId: str
    SshPublicKeyId: str
    UserName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityPoliciesResponseTypeDef(BaseModel):
    SecurityPolicyNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartDirectoryListingResponseTypeDef(BaseModel):
    ListingId: str
    OutputFileName: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFileTransferResponseTypeDef(BaseModel):
    TransferId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestConnectionResponseTypeDef(BaseModel):
    ConnectorId: str
    Status: str
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestIdentityProviderResponseTypeDef(BaseModel):
    Response: str
    StatusCode: int
    Message: str
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessResponseTypeDef(BaseModel):
    ServerId: str
    ExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgreementResponseTypeDef(BaseModel):
    AgreementId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCertificateResponseTypeDef(BaseModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorResponseTypeDef(BaseModel):
    ConnectorId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHostKeyResponseTypeDef(BaseModel):
    ServerId: str
    HostKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileResponseTypeDef(BaseModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServerResponseTypeDef(BaseModel):
    ServerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseModel):
    ServerId: str
    UserName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgreementRequestRequestTypeDef(BaseModel):
    ServerId: str
    LocalProfileId: str
    PartnerProfileId: str
    BaseDirectory: str
    AccessRole: str
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateProfileRequestRequestTypeDef(BaseModel):
    As2Id: str
    ProfileType: ProfileTypeType
    CertificateIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserRequestRequestTypeDef(BaseModel):
    Role: str
    ServerId: str
    UserName: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileTypeDef] = None
    SshPublicKeyBody: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribedAgreementTypeDef(BaseModel):
    Arn: str
    AgreementId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    ServerId: Optional[str] = None
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None
    BaseDirectory: Optional[str] = None
    AccessRole: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribedCertificateTypeDef(BaseModel):
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
    Tags: Optional[List[TagTypeDef]] = None

class DescribedHostKeyTypeDef(BaseModel):
    Arn: str
    HostKeyId: Optional[str] = None
    HostKeyFingerprint: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    DateImported: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribedProfileTypeDef(BaseModel):
    Arn: str
    ProfileId: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None
    As2Id: Optional[str] = None
    CertificateIds: Optional[List[str]] = None
    Tags: Optional[List[TagTypeDef]] = None

class ImportHostKeyRequestRequestTypeDef(BaseModel):
    ServerId: str
    HostKeyBody: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Arn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    Tags: Sequence[TagTypeDef]

class CreateConnectorRequestRequestTypeDef(BaseModel):
    Url: str
    AccessRole: str
    As2Config: Optional[As2ConnectorConfigTypeDef] = None
    LoggingRole: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SftpConfig: Optional[SftpConnectorConfigTypeDef] = None
    SecurityPolicyName: Optional[str] = None

class UpdateConnectorRequestRequestTypeDef(BaseModel):
    ConnectorId: str
    Url: Optional[str] = None
    As2Config: Optional[As2ConnectorConfigTypeDef] = None
    AccessRole: Optional[str] = None
    LoggingRole: Optional[str] = None
    SftpConfig: Optional[SftpConnectorConfigTypeDef] = None
    SecurityPolicyName: Optional[str] = None

class DescribeSecurityPolicyResponseTypeDef(BaseModel):
    SecurityPolicy: DescribedSecurityPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServerRequestServerOfflineWaitTypeDef(BaseModel):
    ServerId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeServerRequestServerOnlineWaitTypeDef(BaseModel):
    ServerId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribedAccessTypeDef(BaseModel):
    HomeDirectory: Optional[str] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntryTypeDef]] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileOutputTypeDef] = None
    Role: Optional[str] = None
    ExternalId: Optional[str] = None

class DescribedConnectorTypeDef(BaseModel):
    Arn: str
    ConnectorId: Optional[str] = None
    Url: Optional[str] = None
    As2Config: Optional[As2ConnectorConfigTypeDef] = None
    AccessRole: Optional[str] = None
    LoggingRole: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    SftpConfig: Optional[SftpConnectorConfigOutputTypeDef] = None
    ServiceManagedEgressIpAddresses: Optional[List[str]] = None
    SecurityPolicyName: Optional[str] = None

class DescribedUserTypeDef(BaseModel):
    Arn: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntryTypeDef]] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileOutputTypeDef] = None
    Role: Optional[str] = None
    SshPublicKeys: Optional[List[SshPublicKeyTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    UserName: Optional[str] = None

class ExecutionStepResultTypeDef(BaseModel):
    StepType: Optional[WorkflowStepTypeType] = None
    Outputs: Optional[str] = None
    Error: Optional[ExecutionErrorTypeDef] = None

class FileLocationTypeDef(BaseModel):
    S3FileLocation: Optional[S3FileLocationTypeDef] = None
    EfsFileLocation: Optional[EfsFileLocationTypeDef] = None

class ImportCertificateRequestRequestTypeDef(BaseModel):
    Usage: CertificateUsageTypeType
    Certificate: str
    CertificateChain: Optional[str] = None
    PrivateKey: Optional[str] = None
    ActiveDate: Optional[TimestampTypeDef] = None
    InactiveDate: Optional[TimestampTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateCertificateRequestRequestTypeDef(BaseModel):
    CertificateId: str
    ActiveDate: Optional[TimestampTypeDef] = None
    InactiveDate: Optional[TimestampTypeDef] = None
    Description: Optional[str] = None

class InputFileLocationTypeDef(BaseModel):
    S3FileLocation: Optional[S3InputFileLocationTypeDef] = None
    EfsFileLocation: Optional[EfsFileLocationTypeDef] = None

class ListAccessesRequestListAccessesPaginateTypeDef(BaseModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgreementsRequestListAgreementsPaginateTypeDef(BaseModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCertificatesRequestListCertificatesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExecutionsRequestListExecutionsPaginateTypeDef(BaseModel):
    WorkflowId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfilesRequestListProfilesPaginateTypeDef(BaseModel):
    ProfileType: Optional[ProfileTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityPoliciesRequestListSecurityPoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServersRequestListServersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    Arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowsRequestListWorkflowsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessesResponseTypeDef(BaseModel):
    ServerId: str
    Accesses: List[ListedAccessTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAgreementsResponseTypeDef(BaseModel):
    Agreements: List[ListedAgreementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCertificatesResponseTypeDef(BaseModel):
    Certificates: List[ListedCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListConnectorsResponseTypeDef(BaseModel):
    Connectors: List[ListedConnectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHostKeysResponseTypeDef(BaseModel):
    ServerId: str
    HostKeys: List[ListedHostKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProfilesResponseTypeDef(BaseModel):
    Profiles: List[ListedProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListServersResponseTypeDef(BaseModel):
    Servers: List[ListedServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUsersResponseTypeDef(BaseModel):
    ServerId: str
    Users: List[ListedUserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListWorkflowsResponseTypeDef(BaseModel):
    Workflows: List[ListedWorkflowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagStepDetailsOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Tags: Optional[List[S3TagTypeDef]] = None
    SourceFileLocation: Optional[str] = None

class TagStepDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Tags: Optional[Sequence[S3TagTypeDef]] = None
    SourceFileLocation: Optional[str] = None

class ServiceMetadataTypeDef(BaseModel):
    UserDetails: UserDetailsTypeDef

class WorkflowDetailsOutputTypeDef(BaseModel):
    OnUpload: Optional[List[WorkflowDetailTypeDef]] = None
    OnPartialUpload: Optional[List[WorkflowDetailTypeDef]] = None

class WorkflowDetailsTypeDef(BaseModel):
    OnUpload: Optional[Sequence[WorkflowDetailTypeDef]] = None
    OnPartialUpload: Optional[Sequence[WorkflowDetailTypeDef]] = None

class DescribeAgreementResponseTypeDef(BaseModel):
    Agreement: DescribedAgreementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateResponseTypeDef(BaseModel):
    Certificate: DescribedCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHostKeyResponseTypeDef(BaseModel):
    HostKey: DescribedHostKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProfileResponseTypeDef(BaseModel):
    Profile: DescribedProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessResponseTypeDef(BaseModel):
    ServerId: str
    Access: DescribedAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorResponseTypeDef(BaseModel):
    Connector: DescribedConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserResponseTypeDef(BaseModel):
    ServerId: str
    User: DescribedUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecutionResultsTypeDef(BaseModel):
    Steps: Optional[List[ExecutionStepResultTypeDef]] = None
    OnExceptionSteps: Optional[List[ExecutionStepResultTypeDef]] = None

class CopyStepDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    DestinationFileLocation: Optional[InputFileLocationTypeDef] = None
    OverwriteExisting: Optional[OverwriteExistingType] = None
    SourceFileLocation: Optional[str] = None

class DecryptStepDetailsTypeDef(BaseModel):
    Type: Literal["PGP"]
    DestinationFileLocation: InputFileLocationTypeDef
    Name: Optional[str] = None
    SourceFileLocation: Optional[str] = None
    OverwriteExisting: Optional[OverwriteExistingType] = None

class ListedExecutionTypeDef(BaseModel):
    ExecutionId: Optional[str] = None
    InitialFileLocation: Optional[FileLocationTypeDef] = None
    ServiceMetadata: Optional[ServiceMetadataTypeDef] = None
    Status: Optional[ExecutionStatusType] = None

class DescribedServerTypeDef(BaseModel):
    Arn: str
    Certificate: Optional[str] = None
    ProtocolDetails: Optional[ProtocolDetailsOutputTypeDef] = None
    Domain: Optional[DomainType] = None
    EndpointDetails: Optional[EndpointDetailsOutputTypeDef] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostKeyFingerprint: Optional[str] = None
    IdentityProviderDetails: Optional[IdentityProviderDetailsTypeDef] = None
    IdentityProviderType: Optional[IdentityProviderTypeType] = None
    LoggingRole: Optional[str] = None
    PostAuthenticationLoginBanner: Optional[str] = None
    PreAuthenticationLoginBanner: Optional[str] = None
    Protocols: Optional[List[ProtocolType]] = None
    SecurityPolicyName: Optional[str] = None
    ServerId: Optional[str] = None
    State: Optional[StateType] = None
    Tags: Optional[List[TagTypeDef]] = None
    UserCount: Optional[int] = None
    WorkflowDetails: Optional[WorkflowDetailsOutputTypeDef] = None
    StructuredLogDestinations: Optional[List[str]] = None
    S3StorageOptions: Optional[S3StorageOptionsTypeDef] = None
    As2ServiceManagedEgressIpAddresses: Optional[List[str]] = None

class CreateServerRequestRequestTypeDef(BaseModel):
    Certificate: Optional[str] = None
    Domain: Optional[DomainType] = None
    EndpointDetails: Optional[EndpointDetailsTypeDef] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostKey: Optional[str] = None
    IdentityProviderDetails: Optional[IdentityProviderDetailsTypeDef] = None
    IdentityProviderType: Optional[IdentityProviderTypeType] = None
    LoggingRole: Optional[str] = None
    PostAuthenticationLoginBanner: Optional[str] = None
    PreAuthenticationLoginBanner: Optional[str] = None
    Protocols: Optional[Sequence[ProtocolType]] = None
    ProtocolDetails: Optional[ProtocolDetailsTypeDef] = None
    SecurityPolicyName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WorkflowDetails: Optional[WorkflowDetailsTypeDef] = None
    StructuredLogDestinations: Optional[Sequence[str]] = None
    S3StorageOptions: Optional[S3StorageOptionsTypeDef] = None

class UpdateServerRequestRequestTypeDef(BaseModel):
    ServerId: str
    Certificate: Optional[str] = None
    ProtocolDetails: Optional[ProtocolDetailsTypeDef] = None
    EndpointDetails: Optional[EndpointDetailsTypeDef] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostKey: Optional[str] = None
    IdentityProviderDetails: Optional[IdentityProviderDetailsTypeDef] = None
    LoggingRole: Optional[str] = None
    PostAuthenticationLoginBanner: Optional[str] = None
    PreAuthenticationLoginBanner: Optional[str] = None
    Protocols: Optional[Sequence[ProtocolType]] = None
    SecurityPolicyName: Optional[str] = None
    WorkflowDetails: Optional[WorkflowDetailsTypeDef] = None
    StructuredLogDestinations: Optional[Sequence[str]] = None
    S3StorageOptions: Optional[S3StorageOptionsTypeDef] = None

class DescribedExecutionTypeDef(BaseModel):
    ExecutionId: Optional[str] = None
    InitialFileLocation: Optional[FileLocationTypeDef] = None
    ServiceMetadata: Optional[ServiceMetadataTypeDef] = None
    ExecutionRole: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationTypeDef] = None
    PosixProfile: Optional[PosixProfileOutputTypeDef] = None
    Status: Optional[ExecutionStatusType] = None
    Results: Optional[ExecutionResultsTypeDef] = None

class WorkflowStepOutputTypeDef(BaseModel):
    Type: Optional[WorkflowStepTypeType] = None
    CopyStepDetails: Optional[CopyStepDetailsTypeDef] = None
    CustomStepDetails: Optional[CustomStepDetailsTypeDef] = None
    DeleteStepDetails: Optional[DeleteStepDetailsTypeDef] = None
    TagStepDetails: Optional[TagStepDetailsOutputTypeDef] = None
    DecryptStepDetails: Optional[DecryptStepDetailsTypeDef] = None

class WorkflowStepTypeDef(BaseModel):
    Type: Optional[WorkflowStepTypeType] = None
    CopyStepDetails: Optional[CopyStepDetailsTypeDef] = None
    CustomStepDetails: Optional[CustomStepDetailsTypeDef] = None
    DeleteStepDetails: Optional[DeleteStepDetailsTypeDef] = None
    TagStepDetails: Optional[TagStepDetailsTypeDef] = None
    DecryptStepDetails: Optional[DecryptStepDetailsTypeDef] = None

class ListExecutionsResponseTypeDef(BaseModel):
    WorkflowId: str
    Executions: List[ListedExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeServerResponseTypeDef(BaseModel):
    Server: DescribedServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExecutionResponseTypeDef(BaseModel):
    WorkflowId: str
    Execution: DescribedExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribedWorkflowTypeDef(BaseModel):
    Arn: str
    Description: Optional[str] = None
    Steps: Optional[List[WorkflowStepOutputTypeDef]] = None
    OnExceptionSteps: Optional[List[WorkflowStepOutputTypeDef]] = None
    WorkflowId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeWorkflowResponseTypeDef(BaseModel):
    Workflow: DescribedWorkflowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowRequestRequestTypeDef(BaseModel):
    Steps: Sequence[WorkflowStepUnionTypeDef]
    Description: Optional[str] = None
    OnExceptionSteps: Optional[Sequence[WorkflowStepUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


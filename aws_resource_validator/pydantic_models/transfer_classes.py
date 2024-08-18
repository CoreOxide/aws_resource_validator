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
from aws_resource_validator.pydantic_models.transfer_constants import *

class As2ConnectorConfigTypeDef(BaseValidatorModel):
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None
    MessageSubject: Optional[str] = None
    Compression: Optional[CompressionEnumType] = None
    EncryptionAlgorithm: Optional[EncryptionAlgType] = None
    SigningAlgorithm: Optional[SigningAlgType] = None
    MdnSigningAlgorithm: Optional[MdnSigningAlgType] = None
    MdnResponse: Optional[MdnResponseType] = None
    BasicAuthSecretId: Optional[str] = None

class HomeDirectoryMapEntryTypeDef(BaseValidatorModel):
    Entry: str
    Target: str
    Type: Optional[MapTypeType] = None

class PosixProfileTypeDef(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[Sequence[int]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class SftpConnectorConfigTypeDef(BaseValidatorModel):
    UserSecretId: Optional[str] = None
    TrustedHostKeys: Optional[Sequence[str]] = None

class EndpointDetailsTypeDef(BaseValidatorModel):
    AddressAllocationIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class IdentityProviderDetailsTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    InvocationRole: Optional[str] = None
    DirectoryId: Optional[str] = None
    Function: Optional[str] = None
    SftpAuthenticationMethods: Optional[SftpAuthenticationMethodsType] = None

class ProtocolDetailsTypeDef(BaseValidatorModel):
    PassiveIp: Optional[str] = None
    TlsSessionResumptionMode: Optional[TlsSessionResumptionModeType] = None
    SetStatOption: Optional[SetStatOptionType] = None
    As2Transports: Optional[Sequence[Literal["HTTP"]]] = None

class S3StorageOptionsTypeDef(BaseValidatorModel):
    DirectoryListingOptimization: Optional[DirectoryListingOptimizationType] = None

class CustomStepDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Target: Optional[str] = None
    TimeoutSeconds: Optional[int] = None
    SourceFileLocation: Optional[str] = None

class DeleteAccessRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    ExternalId: str

class DeleteAgreementRequestRequestTypeDef(BaseValidatorModel):
    AgreementId: str
    ServerId: str

class DeleteCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateId: str

class DeleteConnectorRequestRequestTypeDef(BaseValidatorModel):
    ConnectorId: str

class DeleteHostKeyRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyId: str

class DeleteProfileRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str

class DeleteServerRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str

class DeleteSshPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    SshPublicKeyId: str
    UserName: str

class DeleteStepDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    SourceFileLocation: Optional[str] = None

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str

class DeleteWorkflowRequestRequestTypeDef(BaseValidatorModel):
    WorkflowId: str

class DescribeAccessRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    ExternalId: str

class DescribeAgreementRequestRequestTypeDef(BaseValidatorModel):
    AgreementId: str
    ServerId: str

class DescribeCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateId: str

class DescribeConnectorRequestRequestTypeDef(BaseValidatorModel):
    ConnectorId: str

class DescribeExecutionRequestRequestTypeDef(BaseValidatorModel):
    ExecutionId: str
    WorkflowId: str

class DescribeHostKeyRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyId: str

class DescribeProfileRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str

class DescribeSecurityPolicyRequestRequestTypeDef(BaseValidatorModel):
    SecurityPolicyName: str

class DescribedSecurityPolicyTypeDef(BaseValidatorModel):
    SecurityPolicyName: str
    Fips: Optional[bool] = None
    SshCiphers: Optional[List[str]] = None
    SshKexs: Optional[List[str]] = None
    SshMacs: Optional[List[str]] = None
    TlsCiphers: Optional[List[str]] = None
    SshHostKeyAlgorithms: Optional[List[str]] = None
    Type: Optional[SecurityPolicyResourceTypeType] = None
    Protocols: Optional[List[SecurityPolicyProtocolType]] = None

class DescribeServerRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeUserRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str

class DescribeWorkflowRequestRequestTypeDef(BaseValidatorModel):
    WorkflowId: str

class PosixProfileOutputTypeDef(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[List[int]] = None

class SftpConnectorConfigOutputTypeDef(BaseValidatorModel):
    UserSecretId: Optional[str] = None
    TrustedHostKeys: Optional[List[str]] = None

class LoggingConfigurationTypeDef(BaseValidatorModel):
    LoggingRole: Optional[str] = None
    LogGroupName: Optional[str] = None

class EndpointDetailsOutputTypeDef(BaseValidatorModel):
    AddressAllocationIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None

class ProtocolDetailsOutputTypeDef(BaseValidatorModel):
    PassiveIp: Optional[str] = None
    TlsSessionResumptionMode: Optional[TlsSessionResumptionModeType] = None
    SetStatOption: Optional[SetStatOptionType] = None
    As2Transports: Optional[List[Literal["HTTP"]]] = None

class SshPublicKeyTypeDef(BaseValidatorModel):
    DateImported: datetime
    SshPublicKeyBody: str
    SshPublicKeyId: str

class EfsFileLocationTypeDef(BaseValidatorModel):
    FileSystemId: Optional[str] = None
    Path: Optional[str] = None

class ExecutionErrorTypeDef(BaseValidatorModel):
    Type: ExecutionErrorTypeType
    Message: str

class S3FileLocationTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    Etag: Optional[str] = None

class ImportSshPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    SshPublicKeyBody: str
    UserName: str

class S3InputFileLocationTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessesRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedAccessTypeDef(BaseValidatorModel):
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Role: Optional[str] = None
    ExternalId: Optional[str] = None

class ListAgreementsRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedAgreementTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AgreementId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    ServerId: Optional[str] = None
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None

class ListCertificatesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedCertificateTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateId: Optional[str] = None
    Usage: Optional[CertificateUsageTypeType] = None
    Status: Optional[CertificateStatusTypeType] = None
    ActiveDate: Optional[datetime] = None
    InactiveDate: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None
    Description: Optional[str] = None

class ListConnectorsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedConnectorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorId: Optional[str] = None
    Url: Optional[str] = None

class ListExecutionsRequestRequestTypeDef(BaseValidatorModel):
    WorkflowId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListHostKeysRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedHostKeyTypeDef(BaseValidatorModel):
    Arn: str
    HostKeyId: Optional[str] = None
    Fingerprint: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    DateImported: Optional[datetime] = None

class ListProfilesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None

class ListedProfileTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ProfileId: Optional[str] = None
    As2Id: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None

class ListSecurityPoliciesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListServersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedServerTypeDef(BaseValidatorModel):
    Arn: str
    Domain: Optional[DomainType] = None
    IdentityProviderType: Optional[IdentityProviderTypeType] = None
    EndpointType: Optional[EndpointTypeType] = None
    LoggingRole: Optional[str] = None
    ServerId: Optional[str] = None
    State: Optional[StateType] = None
    UserCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListUsersRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedUserTypeDef(BaseValidatorModel):
    Arn: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Role: Optional[str] = None
    SshPublicKeyCount: Optional[int] = None
    UserName: Optional[str] = None

class ListWorkflowsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListedWorkflowTypeDef(BaseValidatorModel):
    WorkflowId: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None

class S3TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class SendWorkflowStepStateRequestRequestTypeDef(BaseValidatorModel):
    WorkflowId: str
    ExecutionId: str
    Token: str
    Status: CustomStepStatusType

class UserDetailsTypeDef(BaseValidatorModel):
    UserName: str
    ServerId: str
    SessionId: Optional[str] = None

class StartDirectoryListingRequestRequestTypeDef(BaseValidatorModel):
    ConnectorId: str
    RemoteDirectoryPath: str
    OutputDirectoryPath: str
    MaxItems: Optional[int] = None

class StartFileTransferRequestRequestTypeDef(BaseValidatorModel):
    ConnectorId: str
    SendFilePaths: Optional[Sequence[str]] = None
    RetrieveFilePaths: Optional[Sequence[str]] = None
    LocalDirectoryPath: Optional[str] = None
    RemoteDirectoryPath: Optional[str] = None

class StartServerRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str

class StopServerRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str

class TestConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectorId: str

class TestIdentityProviderRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str
    ServerProtocol: Optional[ProtocolType] = None
    SourceIp: Optional[str] = None
    UserPassword: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    TagKeys: Sequence[str]

class UpdateAgreementRequestRequestTypeDef(BaseValidatorModel):
    AgreementId: str
    ServerId: str
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    LocalProfileId: Optional[str] = None
    PartnerProfileId: Optional[str] = None
    BaseDirectory: Optional[str] = None
    AccessRole: Optional[str] = None

class UpdateHostKeyRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyId: str
    Description: str

class UpdateProfileRequestRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    CertificateIds: Optional[Sequence[str]] = None

class WorkflowDetailTypeDef(BaseValidatorModel):
    WorkflowId: str
    ExecutionRole: str

class CreateAccessRequestRequestTypeDef(BaseValidatorModel):
    Role: str
    ServerId: str
    ExternalId: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileTypeDef] = None

class UpdateAccessRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    ExternalId: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileTypeDef] = None
    Role: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileTypeDef] = None
    Role: Optional[str] = None

class CreateAccessResponseTypeDef(BaseValidatorModel):
    ServerId: str
    ExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgreementResponseTypeDef(BaseValidatorModel):
    AgreementId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectorResponseTypeDef(BaseValidatorModel):
    ConnectorId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProfileResponseTypeDef(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServerResponseTypeDef(BaseValidatorModel):
    ServerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowResponseTypeDef(BaseValidatorModel):
    WorkflowId: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ImportCertificateResponseTypeDef(BaseValidatorModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportHostKeyResponseTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSshPublicKeyResponseTypeDef(BaseValidatorModel):
    ServerId: str
    SshPublicKeyId: str
    UserName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityPoliciesResponseTypeDef(BaseValidatorModel):
    SecurityPolicyNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartDirectoryListingResponseTypeDef(BaseValidatorModel):
    ListingId: str
    OutputFileName: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartFileTransferResponseTypeDef(BaseValidatorModel):
    TransferId: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestConnectionResponseTypeDef(BaseValidatorModel):
    ConnectorId: str
    Status: str
    StatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class TestIdentityProviderResponseTypeDef(BaseValidatorModel):
    Response: str
    StatusCode: int
    Message: str
    Url: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessResponseTypeDef(BaseValidatorModel):
    ServerId: str
    ExternalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAgreementResponseTypeDef(BaseValidatorModel):
    AgreementId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCertificateResponseTypeDef(BaseValidatorModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectorResponseTypeDef(BaseValidatorModel):
    ConnectorId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateHostKeyResponseTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProfileResponseTypeDef(BaseValidatorModel):
    ProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServerResponseTypeDef(BaseValidatorModel):
    ServerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgreementRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    LocalProfileId: str
    PartnerProfileId: str
    BaseDirectory: str
    AccessRole: str
    Description: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateProfileRequestRequestTypeDef(BaseValidatorModel):
    As2Id: str
    ProfileType: ProfileTypeType
    CertificateIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
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

class DescribedAgreementTypeDef(BaseValidatorModel):
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

class DescribedCertificateTypeDef(BaseValidatorModel):
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

class DescribedHostKeyTypeDef(BaseValidatorModel):
    Arn: str
    HostKeyId: Optional[str] = None
    HostKeyFingerprint: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    DateImported: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribedProfileTypeDef(BaseValidatorModel):
    Arn: str
    ProfileId: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None
    As2Id: Optional[str] = None
    CertificateIds: Optional[List[str]] = None
    Tags: Optional[List[TagTypeDef]] = None

class ImportHostKeyRequestRequestTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyBody: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Sequence[TagTypeDef]

class CreateConnectorRequestRequestTypeDef(BaseValidatorModel):
    Url: str
    AccessRole: str
    As2Config: Optional[As2ConnectorConfigTypeDef] = None
    LoggingRole: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SftpConfig: Optional[SftpConnectorConfigTypeDef] = None
    SecurityPolicyName: Optional[str] = None

class UpdateConnectorRequestRequestTypeDef(BaseValidatorModel):
    ConnectorId: str
    Url: Optional[str] = None
    As2Config: Optional[As2ConnectorConfigTypeDef] = None
    AccessRole: Optional[str] = None
    LoggingRole: Optional[str] = None
    SftpConfig: Optional[SftpConnectorConfigTypeDef] = None
    SecurityPolicyName: Optional[str] = None

class DescribeSecurityPolicyResponseTypeDef(BaseValidatorModel):
    SecurityPolicy: DescribedSecurityPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServerRequestServerOfflineWaitTypeDef(BaseValidatorModel):
    ServerId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeServerRequestServerOnlineWaitTypeDef(BaseValidatorModel):
    ServerId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribedAccessTypeDef(BaseValidatorModel):
    HomeDirectory: Optional[str] = None
    HomeDirectoryMappings: Optional[List[HomeDirectoryMapEntryTypeDef]] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileOutputTypeDef] = None
    Role: Optional[str] = None
    ExternalId: Optional[str] = None

class DescribedConnectorTypeDef(BaseValidatorModel):
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

class DescribedUserTypeDef(BaseValidatorModel):
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

class ExecutionStepResultTypeDef(BaseValidatorModel):
    StepType: Optional[WorkflowStepTypeType] = None
    Outputs: Optional[str] = None
    Error: Optional[ExecutionErrorTypeDef] = None

class FileLocationTypeDef(BaseValidatorModel):
    S3FileLocation: Optional[S3FileLocationTypeDef] = None
    EfsFileLocation: Optional[EfsFileLocationTypeDef] = None

class ImportCertificateRequestRequestTypeDef(BaseValidatorModel):
    Usage: CertificateUsageTypeType
    Certificate: str
    CertificateChain: Optional[str] = None
    PrivateKey: Optional[str] = None
    ActiveDate: Optional[TimestampTypeDef] = None
    InactiveDate: Optional[TimestampTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class UpdateCertificateRequestRequestTypeDef(BaseValidatorModel):
    CertificateId: str
    ActiveDate: Optional[TimestampTypeDef] = None
    InactiveDate: Optional[TimestampTypeDef] = None
    Description: Optional[str] = None

class InputFileLocationTypeDef(BaseValidatorModel):
    S3FileLocation: Optional[S3InputFileLocationTypeDef] = None
    EfsFileLocation: Optional[EfsFileLocationTypeDef] = None

class ListAccessesRequestListAccessesPaginateTypeDef(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAgreementsRequestListAgreementsPaginateTypeDef(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCertificatesRequestListCertificatesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectorsRequestListConnectorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExecutionsRequestListExecutionsPaginateTypeDef(BaseValidatorModel):
    WorkflowId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProfilesRequestListProfilesPaginateTypeDef(BaseValidatorModel):
    ProfileType: Optional[ProfileTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityPoliciesRequestListSecurityPoliciesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServersRequestListServersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    Arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowsRequestListWorkflowsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccessesResponseTypeDef(BaseValidatorModel):
    ServerId: str
    Accesses: List[ListedAccessTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAgreementsResponseTypeDef(BaseValidatorModel):
    Agreements: List[ListedAgreementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCertificatesResponseTypeDef(BaseValidatorModel):
    Certificates: List[ListedCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListConnectorsResponseTypeDef(BaseValidatorModel):
    Connectors: List[ListedConnectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListHostKeysResponseTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeys: List[ListedHostKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListProfilesResponseTypeDef(BaseValidatorModel):
    Profiles: List[ListedProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListServersResponseTypeDef(BaseValidatorModel):
    Servers: List[ListedServerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUsersResponseTypeDef(BaseValidatorModel):
    ServerId: str
    Users: List[ListedUserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    Workflows: List[ListedWorkflowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagStepDetailsOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Tags: Optional[List[S3TagTypeDef]] = None
    SourceFileLocation: Optional[str] = None

class TagStepDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Tags: Optional[Sequence[S3TagTypeDef]] = None
    SourceFileLocation: Optional[str] = None

class ServiceMetadataTypeDef(BaseValidatorModel):
    UserDetails: UserDetailsTypeDef

class WorkflowDetailsOutputTypeDef(BaseValidatorModel):
    OnUpload: Optional[List[WorkflowDetailTypeDef]] = None
    OnPartialUpload: Optional[List[WorkflowDetailTypeDef]] = None

class WorkflowDetailsTypeDef(BaseValidatorModel):
    OnUpload: Optional[Sequence[WorkflowDetailTypeDef]] = None
    OnPartialUpload: Optional[Sequence[WorkflowDetailTypeDef]] = None

class DescribeAgreementResponseTypeDef(BaseValidatorModel):
    Agreement: DescribedAgreementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: DescribedCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHostKeyResponseTypeDef(BaseValidatorModel):
    HostKey: DescribedHostKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeProfileResponseTypeDef(BaseValidatorModel):
    Profile: DescribedProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccessResponseTypeDef(BaseValidatorModel):
    ServerId: str
    Access: DescribedAccessTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectorResponseTypeDef(BaseValidatorModel):
    Connector: DescribedConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUserResponseTypeDef(BaseValidatorModel):
    ServerId: str
    User: DescribedUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecutionResultsTypeDef(BaseValidatorModel):
    Steps: Optional[List[ExecutionStepResultTypeDef]] = None
    OnExceptionSteps: Optional[List[ExecutionStepResultTypeDef]] = None

class CopyStepDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DestinationFileLocation: Optional[InputFileLocationTypeDef] = None
    OverwriteExisting: Optional[OverwriteExistingType] = None
    SourceFileLocation: Optional[str] = None

class DecryptStepDetailsTypeDef(BaseValidatorModel):
    Type: Literal["PGP"]
    DestinationFileLocation: InputFileLocationTypeDef
    Name: Optional[str] = None
    SourceFileLocation: Optional[str] = None
    OverwriteExisting: Optional[OverwriteExistingType] = None

class ListedExecutionTypeDef(BaseValidatorModel):
    ExecutionId: Optional[str] = None
    InitialFileLocation: Optional[FileLocationTypeDef] = None
    ServiceMetadata: Optional[ServiceMetadataTypeDef] = None
    Status: Optional[ExecutionStatusType] = None

class DescribedServerTypeDef(BaseValidatorModel):
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

class CreateServerRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateServerRequestRequestTypeDef(BaseValidatorModel):
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

class DescribedExecutionTypeDef(BaseValidatorModel):
    ExecutionId: Optional[str] = None
    InitialFileLocation: Optional[FileLocationTypeDef] = None
    ServiceMetadata: Optional[ServiceMetadataTypeDef] = None
    ExecutionRole: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationTypeDef] = None
    PosixProfile: Optional[PosixProfileOutputTypeDef] = None
    Status: Optional[ExecutionStatusType] = None
    Results: Optional[ExecutionResultsTypeDef] = None

class WorkflowStepOutputTypeDef(BaseValidatorModel):
    Type: Optional[WorkflowStepTypeType] = None
    CopyStepDetails: Optional[CopyStepDetailsTypeDef] = None
    CustomStepDetails: Optional[CustomStepDetailsTypeDef] = None
    DeleteStepDetails: Optional[DeleteStepDetailsTypeDef] = None
    TagStepDetails: Optional[TagStepDetailsOutputTypeDef] = None
    DecryptStepDetails: Optional[DecryptStepDetailsTypeDef] = None

class WorkflowStepTypeDef(BaseValidatorModel):
    Type: Optional[WorkflowStepTypeType] = None
    CopyStepDetails: Optional[CopyStepDetailsTypeDef] = None
    CustomStepDetails: Optional[CustomStepDetailsTypeDef] = None
    DeleteStepDetails: Optional[DeleteStepDetailsTypeDef] = None
    TagStepDetails: Optional[TagStepDetailsTypeDef] = None
    DecryptStepDetails: Optional[DecryptStepDetailsTypeDef] = None

class ListExecutionsResponseTypeDef(BaseValidatorModel):
    WorkflowId: str
    Executions: List[ListedExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeServerResponseTypeDef(BaseValidatorModel):
    Server: DescribedServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExecutionResponseTypeDef(BaseValidatorModel):
    WorkflowId: str
    Execution: DescribedExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribedWorkflowTypeDef(BaseValidatorModel):
    Arn: str
    Description: Optional[str] = None
    Steps: Optional[List[WorkflowStepOutputTypeDef]] = None
    OnExceptionSteps: Optional[List[WorkflowStepOutputTypeDef]] = None
    WorkflowId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeWorkflowResponseTypeDef(BaseValidatorModel):
    Workflow: DescribedWorkflowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowRequestRequestTypeDef(BaseValidatorModel):
    Steps: Sequence[WorkflowStepUnionTypeDef]
    Description: Optional[str] = None
    OnExceptionSteps: Optional[Sequence[WorkflowStepUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


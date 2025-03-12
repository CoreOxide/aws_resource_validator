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
    PreserveContentType: Optional[PreserveContentTypeType] = None


class ConnectorFileTransferResultTypeDef(BaseValidatorModel):
    FilePath: str
    StatusCode: TransferTableStatusType
    FailureCode: Optional[str] = None
    FailureMessage: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CustomDirectoriesTypeTypeDef(BaseValidatorModel):
    FailedFilesDirectory: str
    MdnFilesDirectory: str
    PayloadFilesDirectory: str
    StatusFilesDirectory: str
    TemporaryFilesDirectory: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class IdentityProviderDetailsTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    InvocationRole: Optional[str] = None
    DirectoryId: Optional[str] = None
    Function: Optional[str] = None
    SftpAuthenticationMethods: Optional[SftpAuthenticationMethodsType] = None


class S3StorageOptionsTypeDef(BaseValidatorModel):
    DirectoryListingOptimization: Optional[DirectoryListingOptimizationType] = None


class WebAppUnitsTypeDef(BaseValidatorModel):
    Provisioned: Optional[int] = None


class CustomStepDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Target: Optional[str] = None
    TimeoutSeconds: Optional[int] = None
    SourceFileLocation: Optional[str] = None


class DeleteAccessRequestTypeDef(BaseValidatorModel):
    ServerId: str
    ExternalId: str


class DeleteAgreementRequestTypeDef(BaseValidatorModel):
    AgreementId: str
    ServerId: str


class DeleteCertificateRequestTypeDef(BaseValidatorModel):
    CertificateId: str


class DeleteConnectorRequestTypeDef(BaseValidatorModel):
    ConnectorId: str


class DeleteHostKeyRequestTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyId: str


class DeleteProfileRequestTypeDef(BaseValidatorModel):
    ProfileId: str


class DeleteServerRequestTypeDef(BaseValidatorModel):
    ServerId: str


class DeleteSshPublicKeyRequestTypeDef(BaseValidatorModel):
    ServerId: str
    SshPublicKeyId: str
    UserName: str


class DeleteStepDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    SourceFileLocation: Optional[str] = None


class DeleteUserRequestTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str


class DeleteWebAppCustomizationRequestTypeDef(BaseValidatorModel):
    WebAppId: str


class DeleteWebAppRequestTypeDef(BaseValidatorModel):
    WebAppId: str


class DeleteWorkflowRequestTypeDef(BaseValidatorModel):
    WorkflowId: str


class DescribeAccessRequestTypeDef(BaseValidatorModel):
    ServerId: str
    ExternalId: str


class DescribeAgreementRequestTypeDef(BaseValidatorModel):
    AgreementId: str
    ServerId: str


class DescribeCertificateRequestTypeDef(BaseValidatorModel):
    CertificateId: str


class DescribeConnectorRequestTypeDef(BaseValidatorModel):
    ConnectorId: str


class DescribeExecutionRequestTypeDef(BaseValidatorModel):
    ExecutionId: str
    WorkflowId: str


class DescribeHostKeyRequestTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyId: str


class DescribeProfileRequestTypeDef(BaseValidatorModel):
    ProfileId: str


class DescribeSecurityPolicyRequestTypeDef(BaseValidatorModel):
    SecurityPolicyName: str


class DescribeServerRequestTypeDef(BaseValidatorModel):
    ServerId: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeUserRequestTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str


class DescribeWebAppCustomizationRequestTypeDef(BaseValidatorModel):
    WebAppId: str


class DescribedWebAppCustomizationTypeDef(BaseValidatorModel):
    Arn: str
    WebAppId: str
    Title: Optional[str] = None
    LogoFile: Optional[bytes] = None
    FaviconFile: Optional[bytes] = None


class DescribeWebAppRequestTypeDef(BaseValidatorModel):
    WebAppId: str


class DescribeWorkflowRequestTypeDef(BaseValidatorModel):
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


class DescribedIdentityCenterConfigTypeDef(BaseValidatorModel):
    ApplicationArn: Optional[str] = None
    InstanceArn: Optional[str] = None
    Role: Optional[str] = None


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


class EndpointDetailsTypeDef(BaseValidatorModel):
    AddressAllocationIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None


class S3FileLocationTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None
    VersionId: Optional[str] = None
    Etag: Optional[str] = None


class IdentityCenterConfigTypeDef(BaseValidatorModel):
    InstanceArn: Optional[str] = None
    Role: Optional[str] = None


class ImportSshPublicKeyRequestTypeDef(BaseValidatorModel):
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


class ListAccessesRequestTypeDef(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedAccessTypeDef(BaseValidatorModel):
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    Role: Optional[str] = None
    ExternalId: Optional[str] = None


class ListAgreementsRequestTypeDef(BaseValidatorModel):
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


class ListCertificatesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConnectorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedConnectorTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ConnectorId: Optional[str] = None
    Url: Optional[str] = None


class ListExecutionsRequestTypeDef(BaseValidatorModel):
    WorkflowId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFileTransferResultsRequestTypeDef(BaseValidatorModel):
    ConnectorId: str
    TransferId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHostKeysRequestTypeDef(BaseValidatorModel):
    ServerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListProfilesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None


class ListedProfileTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ProfileId: Optional[str] = None
    As2Id: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None


class ListSecurityPoliciesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListServersRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    Arn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
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


class ListWebAppsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedWebAppTypeDef(BaseValidatorModel):
    Arn: str
    WebAppId: str
    AccessEndpoint: Optional[str] = None
    WebAppEndpoint: Optional[str] = None


class ListWorkflowsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListedWorkflowTypeDef(BaseValidatorModel):
    WorkflowId: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None


class PosixProfileTypeDef(BaseValidatorModel):
    Uid: int
    Gid: int
    SecondaryGids: Optional[Sequence[int]] = None


class ProtocolDetailsTypeDef(BaseValidatorModel):
    PassiveIp: Optional[str] = None
    TlsSessionResumptionMode: Optional[TlsSessionResumptionModeType] = None
    SetStatOption: Optional[SetStatOptionType] = None
    As2Transports: Optional[Sequence[Literal["HTTP"]]] = None


class S3TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class SendWorkflowStepStateRequestTypeDef(BaseValidatorModel):
    WorkflowId: str
    ExecutionId: str
    Token: str
    Status: CustomStepStatusType


class UserDetailsTypeDef(BaseValidatorModel):
    UserName: str
    ServerId: str
    SessionId: Optional[str] = None


class SftpConnectorConfigTypeDef(BaseValidatorModel):
    UserSecretId: Optional[str] = None
    TrustedHostKeys: Optional[Sequence[str]] = None


class StartDirectoryListingRequestTypeDef(BaseValidatorModel):
    ConnectorId: str
    RemoteDirectoryPath: str
    OutputDirectoryPath: str
    MaxItems: Optional[int] = None


class StartFileTransferRequestTypeDef(BaseValidatorModel):
    ConnectorId: str
    SendFilePaths: Optional[Sequence[str]] = None
    RetrieveFilePaths: Optional[Sequence[str]] = None
    LocalDirectoryPath: Optional[str] = None
    RemoteDirectoryPath: Optional[str] = None


class StartServerRequestTypeDef(BaseValidatorModel):
    ServerId: str


class StopServerRequestTypeDef(BaseValidatorModel):
    ServerId: str


class TestConnectionRequestTypeDef(BaseValidatorModel):
    ConnectorId: str


class TestIdentityProviderRequestTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str
    ServerProtocol: Optional[ProtocolType] = None
    SourceIp: Optional[str] = None
    UserPassword: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    Arn: str
    TagKeys: Sequence[str]


class UpdateHostKeyRequestTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyId: str
    Description: str


class UpdateProfileRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    CertificateIds: Optional[Sequence[str]] = None


class UpdateWebAppIdentityCenterConfigTypeDef(BaseValidatorModel):
    Role: Optional[str] = None


class WorkflowDetailTypeDef(BaseValidatorModel):
    WorkflowId: str
    ExecutionRole: str


class BlobTypeDef(BaseValidatorModel):
    pass


class UpdateWebAppCustomizationRequestTypeDef(BaseValidatorModel):
    WebAppId: str
    Title: Optional[str] = None
    LogoFile: Optional[BlobTypeDef] = None
    FaviconFile: Optional[BlobTypeDef] = None


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


class CreateWebAppResponseTypeDef(BaseValidatorModel):
    WebAppId: str
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


class ListFileTransferResultsResponseTypeDef(BaseValidatorModel):
    FileTransferResults: List[ConnectorFileTransferResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class UpdateWebAppCustomizationResponseTypeDef(BaseValidatorModel):
    WebAppId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWebAppResponseTypeDef(BaseValidatorModel):
    WebAppId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAgreementRequestTypeDef(BaseValidatorModel):
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
    CustomDirectories: Optional[CustomDirectoriesTypeTypeDef] = None


class CreateAgreementRequestTypeDef(BaseValidatorModel):
    ServerId: str
    LocalProfileId: str
    PartnerProfileId: str
    AccessRole: str
    Description: Optional[str] = None
    BaseDirectory: Optional[str] = None
    Status: Optional[AgreementStatusTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    PreserveFilename: Optional[PreserveFilenameTypeType] = None
    EnforceMessageSigning: Optional[EnforceMessageSigningTypeType] = None
    CustomDirectories: Optional[CustomDirectoriesTypeTypeDef] = None


class CreateProfileRequestTypeDef(BaseValidatorModel):
    As2Id: str
    ProfileType: ProfileTypeType
    CertificateIds: Optional[Sequence[str]] = None
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
    PreserveFilename: Optional[PreserveFilenameTypeType] = None
    EnforceMessageSigning: Optional[EnforceMessageSigningTypeType] = None
    CustomDirectories: Optional[CustomDirectoriesTypeTypeDef] = None


class DescribedProfileTypeDef(BaseValidatorModel):
    Arn: str
    ProfileId: Optional[str] = None
    ProfileType: Optional[ProfileTypeType] = None
    As2Id: Optional[str] = None
    CertificateIds: Optional[List[str]] = None
    Tags: Optional[List[TagTypeDef]] = None


class ImportHostKeyRequestTypeDef(BaseValidatorModel):
    ServerId: str
    HostKeyBody: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Arn: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Sequence[TagTypeDef]


class DescribedSecurityPolicyTypeDef(BaseValidatorModel):
    pass


class DescribeSecurityPolicyResponseTypeDef(BaseValidatorModel):
    SecurityPolicy: DescribedSecurityPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeServerRequestWaitExtraTypeDef(BaseValidatorModel):
    ServerId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeServerRequestWaitTypeDef(BaseValidatorModel):
    ServerId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeWebAppCustomizationResponseTypeDef(BaseValidatorModel):
    WebAppCustomization: DescribedWebAppCustomizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class HomeDirectoryMapEntryTypeDef(BaseValidatorModel):
    pass


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


class DescribedWebAppIdentityProviderDetailsTypeDef(BaseValidatorModel):
    IdentityCenterConfig: Optional[DescribedIdentityCenterConfigTypeDef] = None


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


class ExecutionErrorTypeDef(BaseValidatorModel):
    pass


class ExecutionStepResultTypeDef(BaseValidatorModel):
    StepType: Optional[WorkflowStepTypeType] = None
    Outputs: Optional[str] = None
    Error: Optional[ExecutionErrorTypeDef] = None


class FileLocationTypeDef(BaseValidatorModel):
    S3FileLocation: Optional[S3FileLocationTypeDef] = None
    EfsFileLocation: Optional[EfsFileLocationTypeDef] = None


class WebAppIdentityProviderDetailsTypeDef(BaseValidatorModel):
    IdentityCenterConfig: Optional[IdentityCenterConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ImportCertificateRequestTypeDef(BaseValidatorModel):
    Usage: CertificateUsageTypeType
    Certificate: str
    CertificateChain: Optional[str] = None
    PrivateKey: Optional[str] = None
    ActiveDate: Optional[TimestampTypeDef] = None
    InactiveDate: Optional[TimestampTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateCertificateRequestTypeDef(BaseValidatorModel):
    CertificateId: str
    ActiveDate: Optional[TimestampTypeDef] = None
    InactiveDate: Optional[TimestampTypeDef] = None
    Description: Optional[str] = None


class InputFileLocationTypeDef(BaseValidatorModel):
    S3FileLocation: Optional[S3InputFileLocationTypeDef] = None
    EfsFileLocation: Optional[EfsFileLocationTypeDef] = None


class ListAccessesRequestPaginateTypeDef(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAgreementsRequestPaginateTypeDef(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCertificatesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConnectorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    WorkflowId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFileTransferResultsRequestPaginateTypeDef(BaseValidatorModel):
    ConnectorId: str
    TransferId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProfilesRequestPaginateTypeDef(BaseValidatorModel):
    ProfileType: Optional[ProfileTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSecurityPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    Arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    ServerId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWebAppsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkflowsRequestPaginateTypeDef(BaseValidatorModel):
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


class ListedCertificateTypeDef(BaseValidatorModel):
    pass


class ListCertificatesResponseTypeDef(BaseValidatorModel):
    Certificates: List[ListedCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListConnectorsResponseTypeDef(BaseValidatorModel):
    Connectors: List[ListedConnectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListedHostKeyTypeDef(BaseValidatorModel):
    pass


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


class ListWebAppsResponseTypeDef(BaseValidatorModel):
    WebApps: List[ListedWebAppTypeDef]
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


class UpdateWebAppIdentityProviderDetailsTypeDef(BaseValidatorModel):
    IdentityCenterConfig: Optional[UpdateWebAppIdentityCenterConfigTypeDef] = None


class WorkflowDetailsOutputTypeDef(BaseValidatorModel):
    OnUpload: Optional[List[WorkflowDetailTypeDef]] = None
    OnPartialUpload: Optional[List[WorkflowDetailTypeDef]] = None


class WorkflowDetailsTypeDef(BaseValidatorModel):
    OnUpload: Optional[Sequence[WorkflowDetailTypeDef]] = None
    OnPartialUpload: Optional[Sequence[WorkflowDetailTypeDef]] = None


class DescribeAgreementResponseTypeDef(BaseValidatorModel):
    Agreement: DescribedAgreementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribedCertificateTypeDef(BaseValidatorModel):
    pass


class DescribeCertificateResponseTypeDef(BaseValidatorModel):
    Certificate: DescribedCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribedHostKeyTypeDef(BaseValidatorModel):
    pass


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


class DescribedWebAppTypeDef(BaseValidatorModel):
    Arn: str
    WebAppId: str
    DescribedIdentityProviderDetails: Optional[DescribedWebAppIdentityProviderDetailsTypeDef] = None
    AccessEndpoint: Optional[str] = None
    WebAppEndpoint: Optional[str] = None
    WebAppUnits: Optional[WebAppUnitsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None


class DescribeUserResponseTypeDef(BaseValidatorModel):
    ServerId: str
    User: DescribedUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExecutionResultsTypeDef(BaseValidatorModel):
    Steps: Optional[List[ExecutionStepResultTypeDef]] = None
    OnExceptionSteps: Optional[List[ExecutionStepResultTypeDef]] = None


class CreateWebAppRequestTypeDef(BaseValidatorModel):
    IdentityProviderDetails: WebAppIdentityProviderDetailsTypeDef
    AccessEndpoint: Optional[str] = None
    WebAppUnits: Optional[WebAppUnitsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CopyStepDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DestinationFileLocation: Optional[InputFileLocationTypeDef] = None
    OverwriteExisting: Optional[OverwriteExistingType] = None
    SourceFileLocation: Optional[str] = None


class PosixProfileUnionTypeDef(BaseValidatorModel):
    pass


class CreateAccessRequestTypeDef(BaseValidatorModel):
    Role: str
    ServerId: str
    ExternalId: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileUnionTypeDef] = None


class CreateUserRequestTypeDef(BaseValidatorModel):
    Role: str
    ServerId: str
    UserName: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileUnionTypeDef] = None
    SshPublicKeyBody: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateAccessRequestTypeDef(BaseValidatorModel):
    ServerId: str
    ExternalId: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileUnionTypeDef] = None
    Role: Optional[str] = None


class UpdateUserRequestTypeDef(BaseValidatorModel):
    ServerId: str
    UserName: str
    HomeDirectory: Optional[str] = None
    HomeDirectoryType: Optional[HomeDirectoryTypeType] = None
    HomeDirectoryMappings: Optional[Sequence[HomeDirectoryMapEntryTypeDef]] = None
    Policy: Optional[str] = None
    PosixProfile: Optional[PosixProfileUnionTypeDef] = None
    Role: Optional[str] = None


class ListedExecutionTypeDef(BaseValidatorModel):
    ExecutionId: Optional[str] = None
    InitialFileLocation: Optional[FileLocationTypeDef] = None
    ServiceMetadata: Optional[ServiceMetadataTypeDef] = None
    Status: Optional[ExecutionStatusType] = None


class SftpConnectorConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateConnectorRequestTypeDef(BaseValidatorModel):
    Url: str
    AccessRole: str
    As2Config: Optional[As2ConnectorConfigTypeDef] = None
    LoggingRole: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SftpConfig: Optional[SftpConnectorConfigUnionTypeDef] = None
    SecurityPolicyName: Optional[str] = None


class UpdateConnectorRequestTypeDef(BaseValidatorModel):
    ConnectorId: str
    Url: Optional[str] = None
    As2Config: Optional[As2ConnectorConfigTypeDef] = None
    AccessRole: Optional[str] = None
    LoggingRole: Optional[str] = None
    SftpConfig: Optional[SftpConnectorConfigUnionTypeDef] = None
    SecurityPolicyName: Optional[str] = None


class UpdateWebAppRequestTypeDef(BaseValidatorModel):
    WebAppId: str
    IdentityProviderDetails: Optional[UpdateWebAppIdentityProviderDetailsTypeDef] = None
    AccessEndpoint: Optional[str] = None
    WebAppUnits: Optional[WebAppUnitsTypeDef] = None


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


class DescribeWebAppResponseTypeDef(BaseValidatorModel):
    WebApp: DescribedWebAppTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribedExecutionTypeDef(BaseValidatorModel):
    ExecutionId: Optional[str] = None
    InitialFileLocation: Optional[FileLocationTypeDef] = None
    ServiceMetadata: Optional[ServiceMetadataTypeDef] = None
    ExecutionRole: Optional[str] = None
    LoggingConfiguration: Optional[LoggingConfigurationTypeDef] = None
    PosixProfile: Optional[PosixProfileOutputTypeDef] = None
    Status: Optional[ExecutionStatusType] = None
    Results: Optional[ExecutionResultsTypeDef] = None


class ListExecutionsResponseTypeDef(BaseValidatorModel):
    WorkflowId: str
    Executions: List[ListedExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeServerResponseTypeDef(BaseValidatorModel):
    Server: DescribedServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointDetailsUnionTypeDef(BaseValidatorModel):
    pass


class ProtocolDetailsUnionTypeDef(BaseValidatorModel):
    pass


class WorkflowDetailsUnionTypeDef(BaseValidatorModel):
    pass


class CreateServerRequestTypeDef(BaseValidatorModel):
    Certificate: Optional[str] = None
    Domain: Optional[DomainType] = None
    EndpointDetails: Optional[EndpointDetailsUnionTypeDef] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostKey: Optional[str] = None
    IdentityProviderDetails: Optional[IdentityProviderDetailsTypeDef] = None
    IdentityProviderType: Optional[IdentityProviderTypeType] = None
    LoggingRole: Optional[str] = None
    PostAuthenticationLoginBanner: Optional[str] = None
    PreAuthenticationLoginBanner: Optional[str] = None
    Protocols: Optional[Sequence[ProtocolType]] = None
    ProtocolDetails: Optional[ProtocolDetailsUnionTypeDef] = None
    SecurityPolicyName: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WorkflowDetails: Optional[WorkflowDetailsUnionTypeDef] = None
    StructuredLogDestinations: Optional[Sequence[str]] = None
    S3StorageOptions: Optional[S3StorageOptionsTypeDef] = None


class UpdateServerRequestTypeDef(BaseValidatorModel):
    ServerId: str
    Certificate: Optional[str] = None
    ProtocolDetails: Optional[ProtocolDetailsUnionTypeDef] = None
    EndpointDetails: Optional[EndpointDetailsUnionTypeDef] = None
    EndpointType: Optional[EndpointTypeType] = None
    HostKey: Optional[str] = None
    IdentityProviderDetails: Optional[IdentityProviderDetailsTypeDef] = None
    LoggingRole: Optional[str] = None
    PostAuthenticationLoginBanner: Optional[str] = None
    PreAuthenticationLoginBanner: Optional[str] = None
    Protocols: Optional[Sequence[ProtocolType]] = None
    SecurityPolicyName: Optional[str] = None
    WorkflowDetails: Optional[WorkflowDetailsUnionTypeDef] = None
    StructuredLogDestinations: Optional[Sequence[str]] = None
    S3StorageOptions: Optional[S3StorageOptionsTypeDef] = None


class DescribeExecutionResponseTypeDef(BaseValidatorModel):
    WorkflowId: str
    Execution: DescribedExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WorkflowStepOutputTypeDef(BaseValidatorModel):
    pass


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


class WorkflowStepUnionTypeDef(BaseValidatorModel):
    pass


class CreateWorkflowRequestTypeDef(BaseValidatorModel):
    Steps: Sequence[WorkflowStepUnionTypeDef]
    Description: Optional[str] = None
    OnExceptionSteps: Optional[Sequence[WorkflowStepUnionTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None



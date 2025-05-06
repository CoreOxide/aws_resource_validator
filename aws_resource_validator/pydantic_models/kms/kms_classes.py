from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.kms.kms_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AliasListEntry(BaseValidatorModel):
    AliasName: Optional[str] = None
    AliasArn: Optional[str] = None
    TargetKeyId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastUpdatedDate: Optional[datetime] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelKeyDeletionRequest(BaseValidatorModel):
    KeyId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ConnectCustomKeyStoreRequest(BaseValidatorModel):
    CustomKeyStoreId: str


class CreateAliasRequest(BaseValidatorModel):
    AliasName: str
    TargetKeyId: str


class XksProxyAuthenticationCredentialType(BaseValidatorModel):
    AccessKeyId: str
    RawSecretAccessKey: str


class Tag(BaseValidatorModel):
    TagKey: str
    TagValue: str


class XksProxyConfigurationType(BaseValidatorModel):
    Connectivity: Optional[XksProxyConnectivityTypeType] = None
    AccessKeyId: Optional[str] = None
    UriEndpoint: Optional[str] = None
    UriPath: Optional[str] = None
    VpcEndpointServiceName: Optional[str] = None


class DeleteAliasRequest(BaseValidatorModel):
    AliasName: str


class DeleteCustomKeyStoreRequest(BaseValidatorModel):
    CustomKeyStoreId: str


class DeleteImportedKeyMaterialRequest(BaseValidatorModel):
    KeyId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCustomKeyStoresRequest(BaseValidatorModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class DescribeKeyRequest(BaseValidatorModel):
    KeyId: str
    GrantTokens: Optional[List[str]] = None


class DisableKeyRequest(BaseValidatorModel):
    KeyId: str


class DisableKeyRotationRequest(BaseValidatorModel):
    KeyId: str


class DisconnectCustomKeyStoreRequest(BaseValidatorModel):
    CustomKeyStoreId: str


class EnableKeyRequest(BaseValidatorModel):
    KeyId: str


class EnableKeyRotationRequest(BaseValidatorModel):
    KeyId: str
    RotationPeriodInDays: Optional[int] = None


class GenerateDataKeyPairWithoutPlaintextRequest(BaseValidatorModel):
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    EncryptionContext: Optional[Dict[str, str]] = None
    GrantTokens: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class GenerateDataKeyWithoutPlaintextRequest(BaseValidatorModel):
    KeyId: str
    EncryptionContext: Optional[Dict[str, str]] = None
    KeySpec: Optional[DataKeySpecType] = None
    NumberOfBytes: Optional[int] = None
    GrantTokens: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class GetKeyPolicyRequest(BaseValidatorModel):
    KeyId: str
    PolicyName: Optional[str] = None


class GetKeyRotationStatusRequest(BaseValidatorModel):
    KeyId: str


class GetParametersForImportRequest(BaseValidatorModel):
    KeyId: str
    WrappingAlgorithm: AlgorithmSpecType
    WrappingKeySpec: WrappingKeySpecType


class GetPublicKeyRequest(BaseValidatorModel):
    KeyId: str
    GrantTokens: Optional[List[str]] = None


class GrantConstraintsOutput(BaseValidatorModel):
    EncryptionContextSubset: Optional[Dict[str, str]] = None
    EncryptionContextEquals: Optional[Dict[str, str]] = None


class GrantConstraints(BaseValidatorModel):
    EncryptionContextSubset: Optional[Dict[str, str]] = None
    EncryptionContextEquals: Optional[Dict[str, str]] = None

Timestamp = Union[datetime, str]


class KeyListEntry(BaseValidatorModel):
    KeyId: Optional[str] = None
    KeyArn: Optional[str] = None


class XksKeyConfigurationType(BaseValidatorModel):
    Id: Optional[str] = None


class ListAliasesRequest(BaseValidatorModel):
    KeyId: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ListGrantsRequest(BaseValidatorModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None
    GrantId: Optional[str] = None
    GranteePrincipal: Optional[str] = None


class ListKeyPoliciesRequest(BaseValidatorModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ListKeyRotationsRequest(BaseValidatorModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class RotationsListEntry(BaseValidatorModel):
    KeyId: Optional[str] = None
    RotationDate: Optional[datetime] = None
    RotationType: Optional[RotationTypeType] = None


class ListKeysRequest(BaseValidatorModel):
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ListResourceTagsRequest(BaseValidatorModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class ListRetirableGrantsRequest(BaseValidatorModel):
    RetiringPrincipal: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None


class MultiRegionKey(BaseValidatorModel):
    Arn: Optional[str] = None
    Region: Optional[str] = None


class PutKeyPolicyRequest(BaseValidatorModel):
    KeyId: str
    Policy: str
    PolicyName: Optional[str] = None
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None


class RetireGrantRequest(BaseValidatorModel):
    GrantToken: Optional[str] = None
    KeyId: Optional[str] = None
    GrantId: Optional[str] = None
    DryRun: Optional[bool] = None


class RevokeGrantRequest(BaseValidatorModel):
    KeyId: str
    GrantId: str
    DryRun: Optional[bool] = None


class RotateKeyOnDemandRequest(BaseValidatorModel):
    KeyId: str


class ScheduleKeyDeletionRequest(BaseValidatorModel):
    KeyId: str
    PendingWindowInDays: Optional[int] = None


class UntagResourceRequest(BaseValidatorModel):
    KeyId: str
    TagKeys: List[str]


class UpdateAliasRequest(BaseValidatorModel):
    AliasName: str
    TargetKeyId: str


class UpdateKeyDescriptionRequest(BaseValidatorModel):
    KeyId: str
    Description: str


class UpdatePrimaryRegionRequest(BaseValidatorModel):
    KeyId: str
    PrimaryRegion: str


class EncryptRequest(BaseValidatorModel):
    KeyId: str
    Plaintext: Blob
    EncryptionContext: Optional[Dict[str, str]] = None
    GrantTokens: Optional[List[str]] = None
    EncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    DryRun: Optional[bool] = None


class GenerateMacRequest(BaseValidatorModel):
    Message: Blob
    KeyId: str
    MacAlgorithm: MacAlgorithmSpecType
    GrantTokens: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class ReEncryptRequest(BaseValidatorModel):
    CiphertextBlob: Blob
    DestinationKeyId: str
    SourceEncryptionContext: Optional[Dict[str, str]] = None
    SourceKeyId: Optional[str] = None
    DestinationEncryptionContext: Optional[Dict[str, str]] = None
    SourceEncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    DestinationEncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    GrantTokens: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class RecipientInfo(BaseValidatorModel):
    KeyEncryptionAlgorithm: Optional[Literal['RSAES_OAEP_SHA_256']] = None
    AttestationDocument: Optional[Blob] = None


class SignRequest(BaseValidatorModel):
    KeyId: str
    Message: Blob
    SigningAlgorithm: SigningAlgorithmSpecType
    MessageType: Optional[MessageTypeType] = None
    GrantTokens: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class VerifyMacRequest(BaseValidatorModel):
    Message: Blob
    KeyId: str
    MacAlgorithm: MacAlgorithmSpecType
    Mac: Blob
    GrantTokens: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class VerifyRequest(BaseValidatorModel):
    KeyId: str
    Message: Blob
    Signature: Blob
    SigningAlgorithm: SigningAlgorithmSpecType
    MessageType: Optional[MessageTypeType] = None
    GrantTokens: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class CancelKeyDeletionResponse(BaseValidatorModel):
    KeyId: str
    ResponseMetadata: ResponseMetadata


class CreateCustomKeyStoreResponse(BaseValidatorModel):
    CustomKeyStoreId: str
    ResponseMetadata: ResponseMetadata


class CreateGrantResponse(BaseValidatorModel):
    GrantToken: str
    GrantId: str
    ResponseMetadata: ResponseMetadata


class DecryptResponse(BaseValidatorModel):
    KeyId: str
    Plaintext: bytes
    EncryptionAlgorithm: EncryptionAlgorithmSpecType
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadata


class DeriveSharedSecretResponse(BaseValidatorModel):
    KeyId: str
    SharedSecret: bytes
    CiphertextForRecipient: bytes
    KeyAgreementAlgorithm: Literal['ECDH']
    KeyOrigin: OriginTypeType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class EncryptResponse(BaseValidatorModel):
    CiphertextBlob: bytes
    KeyId: str
    EncryptionAlgorithm: EncryptionAlgorithmSpecType
    ResponseMetadata: ResponseMetadata


class GenerateDataKeyPairResponse(BaseValidatorModel):
    PrivateKeyCiphertextBlob: bytes
    PrivateKeyPlaintext: bytes
    PublicKey: bytes
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadata


class GenerateDataKeyPairWithoutPlaintextResponse(BaseValidatorModel):
    PrivateKeyCiphertextBlob: bytes
    PublicKey: bytes
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    ResponseMetadata: ResponseMetadata


class GenerateDataKeyResponse(BaseValidatorModel):
    CiphertextBlob: bytes
    Plaintext: bytes
    KeyId: str
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadata


class GenerateDataKeyWithoutPlaintextResponse(BaseValidatorModel):
    CiphertextBlob: bytes
    KeyId: str
    ResponseMetadata: ResponseMetadata


class GenerateMacResponse(BaseValidatorModel):
    Mac: bytes
    MacAlgorithm: MacAlgorithmSpecType
    KeyId: str
    ResponseMetadata: ResponseMetadata


class GenerateRandomResponse(BaseValidatorModel):
    Plaintext: bytes
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadata


class GetKeyPolicyResponse(BaseValidatorModel):
    Policy: str
    PolicyName: str
    ResponseMetadata: ResponseMetadata


class GetKeyRotationStatusResponse(BaseValidatorModel):
    KeyRotationEnabled: bool
    KeyId: str
    RotationPeriodInDays: int
    NextRotationDate: datetime
    OnDemandRotationStartDate: datetime
    ResponseMetadata: ResponseMetadata


class GetParametersForImportResponse(BaseValidatorModel):
    KeyId: str
    ImportToken: bytes
    PublicKey: bytes
    ParametersValidTo: datetime
    ResponseMetadata: ResponseMetadata


class GetPublicKeyResponse(BaseValidatorModel):
    KeyId: str
    PublicKey: bytes
    CustomerMasterKeySpec: CustomerMasterKeySpecType
    KeySpec: KeySpecType
    KeyUsage: KeyUsageTypeType
    EncryptionAlgorithms: List[EncryptionAlgorithmSpecType]
    SigningAlgorithms: List[SigningAlgorithmSpecType]
    KeyAgreementAlgorithms: List[Literal['ECDH']]
    ResponseMetadata: ResponseMetadata


class ListAliasesResponse(BaseValidatorModel):
    Aliases: List[AliasListEntry]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadata


class ListKeyPoliciesResponse(BaseValidatorModel):
    PolicyNames: List[str]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadata


class ReEncryptResponse(BaseValidatorModel):
    CiphertextBlob: bytes
    SourceKeyId: str
    KeyId: str
    SourceEncryptionAlgorithm: EncryptionAlgorithmSpecType
    DestinationEncryptionAlgorithm: EncryptionAlgorithmSpecType
    ResponseMetadata: ResponseMetadata


class RotateKeyOnDemandResponse(BaseValidatorModel):
    KeyId: str
    ResponseMetadata: ResponseMetadata


class ScheduleKeyDeletionResponse(BaseValidatorModel):
    KeyId: str
    DeletionDate: datetime
    KeyState: KeyStateType
    PendingWindowInDays: int
    ResponseMetadata: ResponseMetadata


class SignResponse(BaseValidatorModel):
    KeyId: str
    Signature: bytes
    SigningAlgorithm: SigningAlgorithmSpecType
    ResponseMetadata: ResponseMetadata


class VerifyMacResponse(BaseValidatorModel):
    KeyId: str
    MacValid: bool
    MacAlgorithm: MacAlgorithmSpecType
    ResponseMetadata: ResponseMetadata


class VerifyResponse(BaseValidatorModel):
    KeyId: str
    SignatureValid: bool
    SigningAlgorithm: SigningAlgorithmSpecType
    ResponseMetadata: ResponseMetadata


class CreateCustomKeyStoreRequest(BaseValidatorModel):
    CustomKeyStoreName: str
    CloudHsmClusterId: Optional[str] = None
    TrustAnchorCertificate: Optional[str] = None
    KeyStorePassword: Optional[str] = None
    CustomKeyStoreType: Optional[CustomKeyStoreTypeType] = None
    XksProxyUriEndpoint: Optional[str] = None
    XksProxyUriPath: Optional[str] = None
    XksProxyVpcEndpointServiceName: Optional[str] = None
    XksProxyAuthenticationCredential: Optional[XksProxyAuthenticationCredentialType] = None
    XksProxyConnectivity: Optional[XksProxyConnectivityTypeType] = None


class UpdateCustomKeyStoreRequest(BaseValidatorModel):
    CustomKeyStoreId: str
    NewCustomKeyStoreName: Optional[str] = None
    KeyStorePassword: Optional[str] = None
    CloudHsmClusterId: Optional[str] = None
    XksProxyUriEndpoint: Optional[str] = None
    XksProxyUriPath: Optional[str] = None
    XksProxyVpcEndpointServiceName: Optional[str] = None
    XksProxyAuthenticationCredential: Optional[XksProxyAuthenticationCredentialType] = None
    XksProxyConnectivity: Optional[XksProxyConnectivityTypeType] = None


class CreateKeyRequest(BaseValidatorModel):
    Policy: Optional[str] = None
    Description: Optional[str] = None
    KeyUsage: Optional[KeyUsageTypeType] = None
    CustomerMasterKeySpec: Optional[CustomerMasterKeySpecType] = None
    KeySpec: Optional[KeySpecType] = None
    Origin: Optional[OriginTypeType] = None
    CustomKeyStoreId: Optional[str] = None
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    MultiRegion: Optional[bool] = None
    XksKeyId: Optional[str] = None


class ListResourceTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadata


class ReplicateKeyRequest(BaseValidatorModel):
    KeyId: str
    ReplicaRegion: str
    Policy: Optional[str] = None
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    KeyId: str
    Tags: List[Tag]


class CustomKeyStoresListEntry(BaseValidatorModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    CloudHsmClusterId: Optional[str] = None
    TrustAnchorCertificate: Optional[str] = None
    ConnectionState: Optional[ConnectionStateTypeType] = None
    ConnectionErrorCode: Optional[ConnectionErrorCodeTypeType] = None
    CreationDate: Optional[datetime] = None
    CustomKeyStoreType: Optional[CustomKeyStoreTypeType] = None
    XksProxyConfiguration: Optional[XksProxyConfigurationType] = None


class DescribeCustomKeyStoresRequestPaginate(BaseValidatorModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAliasesRequestPaginate(BaseValidatorModel):
    KeyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGrantsRequestPaginate(BaseValidatorModel):
    KeyId: str
    GrantId: Optional[str] = None
    GranteePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKeyPoliciesRequestPaginate(BaseValidatorModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKeyRotationsRequestPaginate(BaseValidatorModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKeysRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceTagsRequestPaginate(BaseValidatorModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRetirableGrantsRequestPaginate(BaseValidatorModel):
    RetiringPrincipal: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GrantListEntry(BaseValidatorModel):
    KeyId: Optional[str] = None
    GrantId: Optional[str] = None
    Name: Optional[str] = None
    CreationDate: Optional[datetime] = None
    GranteePrincipal: Optional[str] = None
    RetiringPrincipal: Optional[str] = None
    IssuingAccount: Optional[str] = None
    Operations: Optional[List[GrantOperationType]] = None
    Constraints: Optional[GrantConstraintsOutput] = None

GrantConstraintsUnion = Union[GrantConstraints, GrantConstraintsOutput]


class ImportKeyMaterialRequest(BaseValidatorModel):
    KeyId: str
    ImportToken: Blob
    EncryptedKeyMaterial: Blob
    ValidTo: Optional[Timestamp] = None
    ExpirationModel: Optional[ExpirationModelTypeType] = None


class ListKeysResponse(BaseValidatorModel):
    Keys: List[KeyListEntry]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadata


class ListKeyRotationsResponse(BaseValidatorModel):
    Rotations: List[RotationsListEntry]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadata


class MultiRegionConfiguration(BaseValidatorModel):
    MultiRegionKeyType: Optional[MultiRegionKeyTypeType] = None
    PrimaryKey: Optional[MultiRegionKey] = None
    ReplicaKeys: Optional[List[MultiRegionKey]] = None


class DecryptRequest(BaseValidatorModel):
    CiphertextBlob: Blob
    EncryptionContext: Optional[Dict[str, str]] = None
    GrantTokens: Optional[List[str]] = None
    KeyId: Optional[str] = None
    EncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    Recipient: Optional[RecipientInfo] = None
    DryRun: Optional[bool] = None


class DeriveSharedSecretRequest(BaseValidatorModel):
    KeyId: str
    KeyAgreementAlgorithm: Literal['ECDH']
    PublicKey: Blob
    GrantTokens: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Recipient: Optional[RecipientInfo] = None


class GenerateDataKeyPairRequest(BaseValidatorModel):
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    EncryptionContext: Optional[Dict[str, str]] = None
    GrantTokens: Optional[List[str]] = None
    Recipient: Optional[RecipientInfo] = None
    DryRun: Optional[bool] = None


class GenerateDataKeyRequest(BaseValidatorModel):
    KeyId: str
    EncryptionContext: Optional[Dict[str, str]] = None
    NumberOfBytes: Optional[int] = None
    KeySpec: Optional[DataKeySpecType] = None
    GrantTokens: Optional[List[str]] = None
    Recipient: Optional[RecipientInfo] = None
    DryRun: Optional[bool] = None


class GenerateRandomRequest(BaseValidatorModel):
    NumberOfBytes: Optional[int] = None
    CustomKeyStoreId: Optional[str] = None
    Recipient: Optional[RecipientInfo] = None


class DescribeCustomKeyStoresResponse(BaseValidatorModel):
    CustomKeyStores: List[CustomKeyStoresListEntry]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadata


class ListGrantsResponse(BaseValidatorModel):
    Grants: List[GrantListEntry]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadata


class CreateGrantRequest(BaseValidatorModel):
    KeyId: str
    GranteePrincipal: str
    Operations: List[GrantOperationType]
    RetiringPrincipal: Optional[str] = None
    Constraints: Optional[GrantConstraintsUnion] = None
    GrantTokens: Optional[List[str]] = None
    Name: Optional[str] = None
    DryRun: Optional[bool] = None


class KeyMetadata(BaseValidatorModel):
    KeyId: str
    AWSAccountId: Optional[str] = None
    Arn: Optional[str] = None
    CreationDate: Optional[datetime] = None
    Enabled: Optional[bool] = None
    Description: Optional[str] = None
    KeyUsage: Optional[KeyUsageTypeType] = None
    KeyState: Optional[KeyStateType] = None
    DeletionDate: Optional[datetime] = None
    ValidTo: Optional[datetime] = None
    Origin: Optional[OriginTypeType] = None
    CustomKeyStoreId: Optional[str] = None
    CloudHsmClusterId: Optional[str] = None
    ExpirationModel: Optional[ExpirationModelTypeType] = None
    KeyManager: Optional[KeyManagerTypeType] = None
    CustomerMasterKeySpec: Optional[CustomerMasterKeySpecType] = None
    KeySpec: Optional[KeySpecType] = None
    EncryptionAlgorithms: Optional[List[EncryptionAlgorithmSpecType]] = None
    SigningAlgorithms: Optional[List[SigningAlgorithmSpecType]] = None
    KeyAgreementAlgorithms: Optional[List[Literal['ECDH']]] = None
    MultiRegion: Optional[bool] = None
    MultiRegionConfiguration: Optional[MultiRegionConfiguration] = None
    PendingDeletionWindowInDays: Optional[int] = None
    MacAlgorithms: Optional[List[MacAlgorithmSpecType]] = None
    XksKeyConfiguration: Optional[XksKeyConfigurationType] = None


class CreateKeyResponse(BaseValidatorModel):
    KeyMetadata: KeyMetadata
    ResponseMetadata: ResponseMetadata


class DescribeKeyResponse(BaseValidatorModel):
    KeyMetadata: KeyMetadata
    ResponseMetadata: ResponseMetadata


class ReplicateKeyResponse(BaseValidatorModel):
    ReplicaKeyMetadata: KeyMetadata
    ReplicaPolicy: str
    ReplicaTags: List[Tag]
    ResponseMetadata: ResponseMetadata
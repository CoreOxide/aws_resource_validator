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
from aws_resource_validator.pydantic_models.kms_constants import *

class AliasListEntryTypeDef(BaseModel):
    AliasName: Optional[str] = None
    AliasArn: Optional[str] = None
    TargetKeyId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastUpdatedDate: Optional[datetime] = None

class CancelKeyDeletionRequestRequestTypeDef(BaseModel):
    KeyId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConnectCustomKeyStoreRequestRequestTypeDef(BaseModel):
    CustomKeyStoreId: str

class CreateAliasRequestRequestTypeDef(BaseModel):
    AliasName: str
    TargetKeyId: str

class XksProxyAuthenticationCredentialTypeTypeDef(BaseModel):
    AccessKeyId: str
    RawSecretAccessKey: str

class GrantConstraintsTypeDef(BaseModel):
    EncryptionContextSubset: Optional[Mapping[str, str]] = None
    EncryptionContextEquals: Optional[Mapping[str, str]] = None

class TagTypeDef(BaseModel):
    TagKey: str
    TagValue: str

class XksProxyConfigurationTypeTypeDef(BaseModel):
    Connectivity: Optional[XksProxyConnectivityTypeType] = None
    AccessKeyId: Optional[str] = None
    UriEndpoint: Optional[str] = None
    UriPath: Optional[str] = None
    VpcEndpointServiceName: Optional[str] = None

class DeleteAliasRequestRequestTypeDef(BaseModel):
    AliasName: str

class DeleteCustomKeyStoreRequestRequestTypeDef(BaseModel):
    CustomKeyStoreId: str

class DeleteImportedKeyMaterialRequestRequestTypeDef(BaseModel):
    KeyId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeCustomKeyStoresRequestRequestTypeDef(BaseModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class DescribeKeyRequestRequestTypeDef(BaseModel):
    KeyId: str
    GrantTokens: Optional[Sequence[str]] = None

class DisableKeyRequestRequestTypeDef(BaseModel):
    KeyId: str

class DisableKeyRotationRequestRequestTypeDef(BaseModel):
    KeyId: str

class DisconnectCustomKeyStoreRequestRequestTypeDef(BaseModel):
    CustomKeyStoreId: str

class EnableKeyRequestRequestTypeDef(BaseModel):
    KeyId: str

class EnableKeyRotationRequestRequestTypeDef(BaseModel):
    KeyId: str
    RotationPeriodInDays: Optional[int] = None

class GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef(BaseModel):
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    EncryptionContext: Optional[Mapping[str, str]] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class GenerateDataKeyWithoutPlaintextRequestRequestTypeDef(BaseModel):
    KeyId: str
    EncryptionContext: Optional[Mapping[str, str]] = None
    KeySpec: Optional[DataKeySpecType] = None
    NumberOfBytes: Optional[int] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class GetKeyPolicyRequestRequestTypeDef(BaseModel):
    KeyId: str
    PolicyName: Optional[str] = None

class GetKeyRotationStatusRequestRequestTypeDef(BaseModel):
    KeyId: str

class GetParametersForImportRequestRequestTypeDef(BaseModel):
    KeyId: str
    WrappingAlgorithm: AlgorithmSpecType
    WrappingKeySpec: WrappingKeySpecType

class GetPublicKeyRequestRequestTypeDef(BaseModel):
    KeyId: str
    GrantTokens: Optional[Sequence[str]] = None

class GrantConstraintsExtraOutputTypeDef(BaseModel):
    EncryptionContextSubset: Optional[Dict[str, str]] = None
    EncryptionContextEquals: Optional[Dict[str, str]] = None

class GrantConstraintsOutputTypeDef(BaseModel):
    EncryptionContextSubset: Optional[Dict[str, str]] = None
    EncryptionContextEquals: Optional[Dict[str, str]] = None

class KeyListEntryTypeDef(BaseModel):
    KeyId: Optional[str] = None
    KeyArn: Optional[str] = None

class XksKeyConfigurationTypeTypeDef(BaseModel):
    Id: Optional[str] = None

class ListAliasesRequestRequestTypeDef(BaseModel):
    KeyId: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListGrantsRequestRequestTypeDef(BaseModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None
    GrantId: Optional[str] = None
    GranteePrincipal: Optional[str] = None

class ListKeyPoliciesRequestRequestTypeDef(BaseModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListKeyRotationsRequestRequestTypeDef(BaseModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class RotationsListEntryTypeDef(BaseModel):
    KeyId: Optional[str] = None
    RotationDate: Optional[datetime] = None
    RotationType: Optional[RotationTypeType] = None

class ListKeysRequestRequestTypeDef(BaseModel):
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListResourceTagsRequestRequestTypeDef(BaseModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListRetirableGrantsRequestRequestTypeDef(BaseModel):
    RetiringPrincipal: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class MultiRegionKeyTypeDef(BaseModel):
    Arn: Optional[str] = None
    Region: Optional[str] = None

class PutKeyPolicyRequestRequestTypeDef(BaseModel):
    KeyId: str
    Policy: str
    PolicyName: Optional[str] = None
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None

class RetireGrantRequestRequestTypeDef(BaseModel):
    GrantToken: Optional[str] = None
    KeyId: Optional[str] = None
    GrantId: Optional[str] = None
    DryRun: Optional[bool] = None

class RevokeGrantRequestRequestTypeDef(BaseModel):
    KeyId: str
    GrantId: str
    DryRun: Optional[bool] = None

class RotateKeyOnDemandRequestRequestTypeDef(BaseModel):
    KeyId: str

class ScheduleKeyDeletionRequestRequestTypeDef(BaseModel):
    KeyId: str
    PendingWindowInDays: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    KeyId: str
    TagKeys: Sequence[str]

class UpdateAliasRequestRequestTypeDef(BaseModel):
    AliasName: str
    TargetKeyId: str

class UpdateKeyDescriptionRequestRequestTypeDef(BaseModel):
    KeyId: str
    Description: str

class UpdatePrimaryRegionRequestRequestTypeDef(BaseModel):
    KeyId: str
    PrimaryRegion: str

class EncryptRequestRequestTypeDef(BaseModel):
    KeyId: str
    Plaintext: BlobTypeDef
    EncryptionContext: Optional[Mapping[str, str]] = None
    GrantTokens: Optional[Sequence[str]] = None
    EncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    DryRun: Optional[bool] = None

class GenerateMacRequestRequestTypeDef(BaseModel):
    Message: BlobTypeDef
    KeyId: str
    MacAlgorithm: MacAlgorithmSpecType
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class ReEncryptRequestRequestTypeDef(BaseModel):
    CiphertextBlob: BlobTypeDef
    DestinationKeyId: str
    SourceEncryptionContext: Optional[Mapping[str, str]] = None
    SourceKeyId: Optional[str] = None
    DestinationEncryptionContext: Optional[Mapping[str, str]] = None
    SourceEncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    DestinationEncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class RecipientInfoTypeDef(BaseModel):
    KeyEncryptionAlgorithm: Optional[Literal["RSAES_OAEP_SHA_256"]] = None
    AttestationDocument: Optional[BlobTypeDef] = None

class SignRequestRequestTypeDef(BaseModel):
    KeyId: str
    Message: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmSpecType
    MessageType: Optional[MessageTypeType] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class VerifyMacRequestRequestTypeDef(BaseModel):
    Message: BlobTypeDef
    KeyId: str
    MacAlgorithm: MacAlgorithmSpecType
    Mac: BlobTypeDef
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class VerifyRequestRequestTypeDef(BaseModel):
    KeyId: str
    Message: BlobTypeDef
    Signature: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmSpecType
    MessageType: Optional[MessageTypeType] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class CancelKeyDeletionResponseTypeDef(BaseModel):
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomKeyStoreResponseTypeDef(BaseModel):
    CustomKeyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGrantResponseTypeDef(BaseModel):
    GrantToken: str
    GrantId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DecryptResponseTypeDef(BaseModel):
    KeyId: str
    Plaintext: bytes
    EncryptionAlgorithm: EncryptionAlgorithmSpecType
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class DeriveSharedSecretResponseTypeDef(BaseModel):
    KeyId: str
    SharedSecret: bytes
    CiphertextForRecipient: bytes
    KeyAgreementAlgorithm: Literal["ECDH"]
    KeyOrigin: OriginTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptResponseTypeDef(BaseModel):
    CiphertextBlob: bytes
    KeyId: str
    EncryptionAlgorithm: EncryptionAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyPairResponseTypeDef(BaseModel):
    PrivateKeyCiphertextBlob: bytes
    PrivateKeyPlaintext: bytes
    PublicKey: bytes
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyPairWithoutPlaintextResponseTypeDef(BaseModel):
    PrivateKeyCiphertextBlob: bytes
    PublicKey: bytes
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyResponseTypeDef(BaseModel):
    CiphertextBlob: bytes
    Plaintext: bytes
    KeyId: str
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyWithoutPlaintextResponseTypeDef(BaseModel):
    CiphertextBlob: bytes
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMacResponseTypeDef(BaseModel):
    Mac: bytes
    MacAlgorithm: MacAlgorithmSpecType
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateRandomResponseTypeDef(BaseModel):
    Plaintext: bytes
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyPolicyResponseTypeDef(BaseModel):
    Policy: str
    PolicyName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyRotationStatusResponseTypeDef(BaseModel):
    KeyRotationEnabled: bool
    KeyId: str
    RotationPeriodInDays: int
    NextRotationDate: datetime
    OnDemandRotationStartDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForImportResponseTypeDef(BaseModel):
    KeyId: str
    ImportToken: bytes
    PublicKey: bytes
    ParametersValidTo: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyResponseTypeDef(BaseModel):
    KeyId: str
    PublicKey: bytes
    CustomerMasterKeySpec: CustomerMasterKeySpecType
    KeySpec: KeySpecType
    KeyUsage: KeyUsageTypeType
    EncryptionAlgorithms: List[EncryptionAlgorithmSpecType]
    SigningAlgorithms: List[SigningAlgorithmSpecType]
    KeyAgreementAlgorithms: List[Literal["ECDH"]]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(BaseModel):
    Aliases: List[AliasListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyPoliciesResponseTypeDef(BaseModel):
    PolicyNames: List[str]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReEncryptResponseTypeDef(BaseModel):
    CiphertextBlob: bytes
    SourceKeyId: str
    KeyId: str
    SourceEncryptionAlgorithm: EncryptionAlgorithmSpecType
    DestinationEncryptionAlgorithm: EncryptionAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class RotateKeyOnDemandResponseTypeDef(BaseModel):
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduleKeyDeletionResponseTypeDef(BaseModel):
    KeyId: str
    DeletionDate: datetime
    KeyState: KeyStateType
    PendingWindowInDays: int
    ResponseMetadata: ResponseMetadataTypeDef

class SignResponseTypeDef(BaseModel):
    KeyId: str
    Signature: bytes
    SigningAlgorithm: SigningAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyMacResponseTypeDef(BaseModel):
    KeyId: str
    MacValid: bool
    MacAlgorithm: MacAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyResponseTypeDef(BaseModel):
    KeyId: str
    SignatureValid: bool
    SigningAlgorithm: SigningAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomKeyStoreRequestRequestTypeDef(BaseModel):
    CustomKeyStoreName: str
    CloudHsmClusterId: Optional[str] = None
    TrustAnchorCertificate: Optional[str] = None
    KeyStorePassword: Optional[str] = None
    CustomKeyStoreType: Optional[CustomKeyStoreTypeType] = None
    XksProxyUriEndpoint: Optional[str] = None
    XksProxyUriPath: Optional[str] = None
    XksProxyVpcEndpointServiceName: Optional[str] = None
    XksProxyAuthenticationCredential: Optional[       XksProxyAuthenticationCredentialTypeTypeDef     ] = None
    XksProxyConnectivity: Optional[XksProxyConnectivityTypeType] = None

class UpdateCustomKeyStoreRequestRequestTypeDef(BaseModel):
    CustomKeyStoreId: str
    NewCustomKeyStoreName: Optional[str] = None
    KeyStorePassword: Optional[str] = None
    CloudHsmClusterId: Optional[str] = None
    XksProxyUriEndpoint: Optional[str] = None
    XksProxyUriPath: Optional[str] = None
    XksProxyVpcEndpointServiceName: Optional[str] = None
    XksProxyAuthenticationCredential: Optional[       XksProxyAuthenticationCredentialTypeTypeDef     ] = None
    XksProxyConnectivity: Optional[XksProxyConnectivityTypeType] = None

class CreateGrantRequestRequestTypeDef(BaseModel):
    KeyId: str
    GranteePrincipal: str
    Operations: Sequence[GrantOperationType]
    RetiringPrincipal: Optional[str] = None
    Constraints: Optional[GrantConstraintsTypeDef] = None
    GrantTokens: Optional[Sequence[str]] = None
    Name: Optional[str] = None
    DryRun: Optional[bool] = None

class CreateKeyRequestRequestTypeDef(BaseModel):
    Policy: Optional[str] = None
    Description: Optional[str] = None
    KeyUsage: Optional[KeyUsageTypeType] = None
    CustomerMasterKeySpec: Optional[CustomerMasterKeySpecType] = None
    KeySpec: Optional[KeySpecType] = None
    Origin: Optional[OriginTypeType] = None
    CustomKeyStoreId: Optional[str] = None
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    MultiRegion: Optional[bool] = None
    XksKeyId: Optional[str] = None

class ListResourceTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateKeyRequestRequestTypeDef(BaseModel):
    KeyId: str
    ReplicaRegion: str
    Policy: Optional[str] = None
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    KeyId: str
    Tags: Sequence[TagTypeDef]

class CustomKeyStoresListEntryTypeDef(BaseModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    CloudHsmClusterId: Optional[str] = None
    TrustAnchorCertificate: Optional[str] = None
    ConnectionState: Optional[ConnectionStateTypeType] = None
    ConnectionErrorCode: Optional[ConnectionErrorCodeTypeType] = None
    CreationDate: Optional[datetime] = None
    CustomKeyStoreType: Optional[CustomKeyStoreTypeType] = None
    XksProxyConfiguration: Optional[XksProxyConfigurationTypeTypeDef] = None

class DescribeCustomKeyStoresRequestDescribeCustomKeyStoresPaginateTypeDef(BaseModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAliasesRequestListAliasesPaginateTypeDef(BaseModel):
    KeyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGrantsRequestListGrantsPaginateTypeDef(BaseModel):
    KeyId: str
    GrantId: Optional[str] = None
    GranteePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeyPoliciesRequestListKeyPoliciesPaginateTypeDef(BaseModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeyRotationsRequestListKeyRotationsPaginateTypeDef(BaseModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeysRequestListKeysPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceTagsRequestListResourceTagsPaginateTypeDef(BaseModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRetirableGrantsRequestListRetirableGrantsPaginateTypeDef(BaseModel):
    RetiringPrincipal: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GrantListEntryTypeDef(BaseModel):
    KeyId: Optional[str] = None
    GrantId: Optional[str] = None
    Name: Optional[str] = None
    CreationDate: Optional[datetime] = None
    GranteePrincipal: Optional[str] = None
    RetiringPrincipal: Optional[str] = None
    IssuingAccount: Optional[str] = None
    Operations: Optional[List[GrantOperationType]] = None
    Constraints: Optional[GrantConstraintsOutputTypeDef] = None

class ImportKeyMaterialRequestRequestTypeDef(BaseModel):
    KeyId: str
    ImportToken: BlobTypeDef
    EncryptedKeyMaterial: BlobTypeDef
    ValidTo: Optional[TimestampTypeDef] = None
    ExpirationModel: Optional[ExpirationModelTypeType] = None

class ListKeysResponseTypeDef(BaseModel):
    Keys: List[KeyListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyRotationsResponseTypeDef(BaseModel):
    Rotations: List[RotationsListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class MultiRegionConfigurationTypeDef(BaseModel):
    MultiRegionKeyType: Optional[MultiRegionKeyTypeType] = None
    PrimaryKey: Optional[MultiRegionKeyTypeDef] = None
    ReplicaKeys: Optional[List[MultiRegionKeyTypeDef]] = None

class DecryptRequestRequestTypeDef(BaseModel):
    CiphertextBlob: BlobTypeDef
    EncryptionContext: Optional[Mapping[str, str]] = None
    GrantTokens: Optional[Sequence[str]] = None
    KeyId: Optional[str] = None
    EncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    Recipient: Optional[RecipientInfoTypeDef] = None
    DryRun: Optional[bool] = None

class DeriveSharedSecretRequestRequestTypeDef(BaseModel):
    KeyId: str
    KeyAgreementAlgorithm: Literal["ECDH"]
    PublicKey: BlobTypeDef
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Recipient: Optional[RecipientInfoTypeDef] = None

class GenerateDataKeyPairRequestRequestTypeDef(BaseModel):
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    EncryptionContext: Optional[Mapping[str, str]] = None
    GrantTokens: Optional[Sequence[str]] = None
    Recipient: Optional[RecipientInfoTypeDef] = None
    DryRun: Optional[bool] = None

class GenerateDataKeyRequestRequestTypeDef(BaseModel):
    KeyId: str
    EncryptionContext: Optional[Mapping[str, str]] = None
    NumberOfBytes: Optional[int] = None
    KeySpec: Optional[DataKeySpecType] = None
    GrantTokens: Optional[Sequence[str]] = None
    Recipient: Optional[RecipientInfoTypeDef] = None
    DryRun: Optional[bool] = None

class GenerateRandomRequestRequestTypeDef(BaseModel):
    NumberOfBytes: Optional[int] = None
    CustomKeyStoreId: Optional[str] = None
    Recipient: Optional[RecipientInfoTypeDef] = None

class DescribeCustomKeyStoresResponseTypeDef(BaseModel):
    CustomKeyStores: List[CustomKeyStoresListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListGrantsResponseTypeDef(BaseModel):
    Grants: List[GrantListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class KeyMetadataTypeDef(BaseModel):
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
    KeyAgreementAlgorithms: Optional[List[Literal["ECDH"]]] = None
    MultiRegion: Optional[bool] = None
    MultiRegionConfiguration: Optional[MultiRegionConfigurationTypeDef] = None
    PendingDeletionWindowInDays: Optional[int] = None
    MacAlgorithms: Optional[List[MacAlgorithmSpecType]] = None
    XksKeyConfiguration: Optional[XksKeyConfigurationTypeTypeDef] = None

class CreateKeyResponseTypeDef(BaseModel):
    KeyMetadata: KeyMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyResponseTypeDef(BaseModel):
    KeyMetadata: KeyMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateKeyResponseTypeDef(BaseModel):
    ReplicaKeyMetadata: KeyMetadataTypeDef
    ReplicaPolicy: str
    ReplicaTags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


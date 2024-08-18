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
from aws_resource_validator.pydantic_models.kms_constants import *

class AliasListEntryTypeDef(BaseValidatorModel):
    AliasName: Optional[str] = None
    AliasArn: Optional[str] = None
    TargetKeyId: Optional[str] = None
    CreationDate: Optional[datetime] = None
    LastUpdatedDate: Optional[datetime] = None

class CancelKeyDeletionRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ConnectCustomKeyStoreRequestRequestTypeDef(BaseValidatorModel):
    CustomKeyStoreId: str

class CreateAliasRequestRequestTypeDef(BaseValidatorModel):
    AliasName: str
    TargetKeyId: str

class XksProxyAuthenticationCredentialTypeTypeDef(BaseValidatorModel):
    AccessKeyId: str
    RawSecretAccessKey: str

class GrantConstraintsTypeDef(BaseValidatorModel):
    EncryptionContextSubset: Optional[Mapping[str, str]] = None
    EncryptionContextEquals: Optional[Mapping[str, str]] = None

class TagTypeDef(BaseValidatorModel):
    TagKey: str
    TagValue: str

class XksProxyConfigurationTypeTypeDef(BaseValidatorModel):
    Connectivity: Optional[XksProxyConnectivityTypeType] = None
    AccessKeyId: Optional[str] = None
    UriEndpoint: Optional[str] = None
    UriPath: Optional[str] = None
    VpcEndpointServiceName: Optional[str] = None

class DeleteAliasRequestRequestTypeDef(BaseValidatorModel):
    AliasName: str

class DeleteCustomKeyStoreRequestRequestTypeDef(BaseValidatorModel):
    CustomKeyStoreId: str

class DeleteImportedKeyMaterialRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeCustomKeyStoresRequestRequestTypeDef(BaseValidatorModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class DescribeKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    GrantTokens: Optional[Sequence[str]] = None

class DisableKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str

class DisableKeyRotationRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str

class DisconnectCustomKeyStoreRequestRequestTypeDef(BaseValidatorModel):
    CustomKeyStoreId: str

class EnableKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str

class EnableKeyRotationRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    RotationPeriodInDays: Optional[int] = None

class GenerateDataKeyPairWithoutPlaintextRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    EncryptionContext: Optional[Mapping[str, str]] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class GenerateDataKeyWithoutPlaintextRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    EncryptionContext: Optional[Mapping[str, str]] = None
    KeySpec: Optional[DataKeySpecType] = None
    NumberOfBytes: Optional[int] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class GetKeyPolicyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    PolicyName: Optional[str] = None

class GetKeyRotationStatusRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str

class GetParametersForImportRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    WrappingAlgorithm: AlgorithmSpecType
    WrappingKeySpec: WrappingKeySpecType

class GetPublicKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    GrantTokens: Optional[Sequence[str]] = None

class GrantConstraintsExtraOutputTypeDef(BaseValidatorModel):
    EncryptionContextSubset: Optional[Dict[str, str]] = None
    EncryptionContextEquals: Optional[Dict[str, str]] = None

class GrantConstraintsOutputTypeDef(BaseValidatorModel):
    EncryptionContextSubset: Optional[Dict[str, str]] = None
    EncryptionContextEquals: Optional[Dict[str, str]] = None

class KeyListEntryTypeDef(BaseValidatorModel):
    KeyId: Optional[str] = None
    KeyArn: Optional[str] = None

class XksKeyConfigurationTypeTypeDef(BaseValidatorModel):
    Id: Optional[str] = None

class ListAliasesRequestRequestTypeDef(BaseValidatorModel):
    KeyId: Optional[str] = None
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListGrantsRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None
    GrantId: Optional[str] = None
    GranteePrincipal: Optional[str] = None

class ListKeyPoliciesRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListKeyRotationsRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class RotationsListEntryTypeDef(BaseValidatorModel):
    KeyId: Optional[str] = None
    RotationDate: Optional[datetime] = None
    RotationType: Optional[RotationTypeType] = None

class ListKeysRequestRequestTypeDef(BaseValidatorModel):
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListResourceTagsRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class ListRetirableGrantsRequestRequestTypeDef(BaseValidatorModel):
    RetiringPrincipal: str
    Limit: Optional[int] = None
    Marker: Optional[str] = None

class MultiRegionKeyTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Region: Optional[str] = None

class PutKeyPolicyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Policy: str
    PolicyName: Optional[str] = None
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None

class RetireGrantRequestRequestTypeDef(BaseValidatorModel):
    GrantToken: Optional[str] = None
    KeyId: Optional[str] = None
    GrantId: Optional[str] = None
    DryRun: Optional[bool] = None

class RevokeGrantRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    GrantId: str
    DryRun: Optional[bool] = None

class RotateKeyOnDemandRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str

class ScheduleKeyDeletionRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    PendingWindowInDays: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    TagKeys: Sequence[str]

class UpdateAliasRequestRequestTypeDef(BaseValidatorModel):
    AliasName: str
    TargetKeyId: str

class UpdateKeyDescriptionRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Description: str

class UpdatePrimaryRegionRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    PrimaryRegion: str

class EncryptRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Plaintext: BlobTypeDef
    EncryptionContext: Optional[Mapping[str, str]] = None
    GrantTokens: Optional[Sequence[str]] = None
    EncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    DryRun: Optional[bool] = None

class GenerateMacRequestRequestTypeDef(BaseValidatorModel):
    Message: BlobTypeDef
    KeyId: str
    MacAlgorithm: MacAlgorithmSpecType
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class ReEncryptRequestRequestTypeDef(BaseValidatorModel):
    CiphertextBlob: BlobTypeDef
    DestinationKeyId: str
    SourceEncryptionContext: Optional[Mapping[str, str]] = None
    SourceKeyId: Optional[str] = None
    DestinationEncryptionContext: Optional[Mapping[str, str]] = None
    SourceEncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    DestinationEncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class RecipientInfoTypeDef(BaseValidatorModel):
    KeyEncryptionAlgorithm: Optional[Literal["RSAES_OAEP_SHA_256"]] = None
    AttestationDocument: Optional[BlobTypeDef] = None

class SignRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Message: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmSpecType
    MessageType: Optional[MessageTypeType] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class VerifyMacRequestRequestTypeDef(BaseValidatorModel):
    Message: BlobTypeDef
    KeyId: str
    MacAlgorithm: MacAlgorithmSpecType
    Mac: BlobTypeDef
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class VerifyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Message: BlobTypeDef
    Signature: BlobTypeDef
    SigningAlgorithm: SigningAlgorithmSpecType
    MessageType: Optional[MessageTypeType] = None
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class CancelKeyDeletionResponseTypeDef(BaseValidatorModel):
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomKeyStoreResponseTypeDef(BaseValidatorModel):
    CustomKeyStoreId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGrantResponseTypeDef(BaseValidatorModel):
    GrantToken: str
    GrantId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DecryptResponseTypeDef(BaseValidatorModel):
    KeyId: str
    Plaintext: bytes
    EncryptionAlgorithm: EncryptionAlgorithmSpecType
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class DeriveSharedSecretResponseTypeDef(BaseValidatorModel):
    KeyId: str
    SharedSecret: bytes
    CiphertextForRecipient: bytes
    KeyAgreementAlgorithm: Literal["ECDH"]
    KeyOrigin: OriginTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptResponseTypeDef(BaseValidatorModel):
    CiphertextBlob: bytes
    KeyId: str
    EncryptionAlgorithm: EncryptionAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyPairResponseTypeDef(BaseValidatorModel):
    PrivateKeyCiphertextBlob: bytes
    PrivateKeyPlaintext: bytes
    PublicKey: bytes
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyPairWithoutPlaintextResponseTypeDef(BaseValidatorModel):
    PrivateKeyCiphertextBlob: bytes
    PublicKey: bytes
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyResponseTypeDef(BaseValidatorModel):
    CiphertextBlob: bytes
    Plaintext: bytes
    KeyId: str
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateDataKeyWithoutPlaintextResponseTypeDef(BaseValidatorModel):
    CiphertextBlob: bytes
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMacResponseTypeDef(BaseValidatorModel):
    Mac: bytes
    MacAlgorithm: MacAlgorithmSpecType
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateRandomResponseTypeDef(BaseValidatorModel):
    Plaintext: bytes
    CiphertextForRecipient: bytes
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyPolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    PolicyName: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyRotationStatusResponseTypeDef(BaseValidatorModel):
    KeyRotationEnabled: bool
    KeyId: str
    RotationPeriodInDays: int
    NextRotationDate: datetime
    OnDemandRotationStartDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForImportResponseTypeDef(BaseValidatorModel):
    KeyId: str
    ImportToken: bytes
    PublicKey: bytes
    ParametersValidTo: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyResponseTypeDef(BaseValidatorModel):
    KeyId: str
    PublicKey: bytes
    CustomerMasterKeySpec: CustomerMasterKeySpecType
    KeySpec: KeySpecType
    KeyUsage: KeyUsageTypeType
    EncryptionAlgorithms: List[EncryptionAlgorithmSpecType]
    SigningAlgorithms: List[SigningAlgorithmSpecType]
    KeyAgreementAlgorithms: List[Literal["ECDH"]]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesResponseTypeDef(BaseValidatorModel):
    Aliases: List[AliasListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyPoliciesResponseTypeDef(BaseValidatorModel):
    PolicyNames: List[str]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReEncryptResponseTypeDef(BaseValidatorModel):
    CiphertextBlob: bytes
    SourceKeyId: str
    KeyId: str
    SourceEncryptionAlgorithm: EncryptionAlgorithmSpecType
    DestinationEncryptionAlgorithm: EncryptionAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class RotateKeyOnDemandResponseTypeDef(BaseValidatorModel):
    KeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduleKeyDeletionResponseTypeDef(BaseValidatorModel):
    KeyId: str
    DeletionDate: datetime
    KeyState: KeyStateType
    PendingWindowInDays: int
    ResponseMetadata: ResponseMetadataTypeDef

class SignResponseTypeDef(BaseValidatorModel):
    KeyId: str
    Signature: bytes
    SigningAlgorithm: SigningAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyMacResponseTypeDef(BaseValidatorModel):
    KeyId: str
    MacValid: bool
    MacAlgorithm: MacAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyResponseTypeDef(BaseValidatorModel):
    KeyId: str
    SignatureValid: bool
    SigningAlgorithm: SigningAlgorithmSpecType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomKeyStoreRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateCustomKeyStoreRequestRequestTypeDef(BaseValidatorModel):
    CustomKeyStoreId: str
    NewCustomKeyStoreName: Optional[str] = None
    KeyStorePassword: Optional[str] = None
    CloudHsmClusterId: Optional[str] = None
    XksProxyUriEndpoint: Optional[str] = None
    XksProxyUriPath: Optional[str] = None
    XksProxyVpcEndpointServiceName: Optional[str] = None
    XksProxyAuthenticationCredential: Optional[       XksProxyAuthenticationCredentialTypeTypeDef     ] = None
    XksProxyConnectivity: Optional[XksProxyConnectivityTypeType] = None

class CreateGrantRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    GranteePrincipal: str
    Operations: Sequence[GrantOperationType]
    RetiringPrincipal: Optional[str] = None
    Constraints: Optional[GrantConstraintsTypeDef] = None
    GrantTokens: Optional[Sequence[str]] = None
    Name: Optional[str] = None
    DryRun: Optional[bool] = None

class CreateKeyRequestRequestTypeDef(BaseValidatorModel):
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

class ListResourceTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    ReplicaRegion: str
    Policy: Optional[str] = None
    BypassPolicyLockoutSafetyCheck: Optional[bool] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    Tags: Sequence[TagTypeDef]

class CustomKeyStoresListEntryTypeDef(BaseValidatorModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    CloudHsmClusterId: Optional[str] = None
    TrustAnchorCertificate: Optional[str] = None
    ConnectionState: Optional[ConnectionStateTypeType] = None
    ConnectionErrorCode: Optional[ConnectionErrorCodeTypeType] = None
    CreationDate: Optional[datetime] = None
    CustomKeyStoreType: Optional[CustomKeyStoreTypeType] = None
    XksProxyConfiguration: Optional[XksProxyConfigurationTypeTypeDef] = None

class DescribeCustomKeyStoresRequestDescribeCustomKeyStoresPaginateTypeDef(BaseValidatorModel):
    CustomKeyStoreId: Optional[str] = None
    CustomKeyStoreName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAliasesRequestListAliasesPaginateTypeDef(BaseValidatorModel):
    KeyId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGrantsRequestListGrantsPaginateTypeDef(BaseValidatorModel):
    KeyId: str
    GrantId: Optional[str] = None
    GranteePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeyPoliciesRequestListKeyPoliciesPaginateTypeDef(BaseValidatorModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeyRotationsRequestListKeyRotationsPaginateTypeDef(BaseValidatorModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeysRequestListKeysPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourceTagsRequestListResourceTagsPaginateTypeDef(BaseValidatorModel):
    KeyId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRetirableGrantsRequestListRetirableGrantsPaginateTypeDef(BaseValidatorModel):
    RetiringPrincipal: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GrantListEntryTypeDef(BaseValidatorModel):
    KeyId: Optional[str] = None
    GrantId: Optional[str] = None
    Name: Optional[str] = None
    CreationDate: Optional[datetime] = None
    GranteePrincipal: Optional[str] = None
    RetiringPrincipal: Optional[str] = None
    IssuingAccount: Optional[str] = None
    Operations: Optional[List[GrantOperationType]] = None
    Constraints: Optional[GrantConstraintsOutputTypeDef] = None

class ImportKeyMaterialRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    ImportToken: BlobTypeDef
    EncryptedKeyMaterial: BlobTypeDef
    ValidTo: Optional[TimestampTypeDef] = None
    ExpirationModel: Optional[ExpirationModelTypeType] = None

class ListKeysResponseTypeDef(BaseValidatorModel):
    Keys: List[KeyListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListKeyRotationsResponseTypeDef(BaseValidatorModel):
    Rotations: List[RotationsListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class MultiRegionConfigurationTypeDef(BaseValidatorModel):
    MultiRegionKeyType: Optional[MultiRegionKeyTypeType] = None
    PrimaryKey: Optional[MultiRegionKeyTypeDef] = None
    ReplicaKeys: Optional[List[MultiRegionKeyTypeDef]] = None

class DecryptRequestRequestTypeDef(BaseValidatorModel):
    CiphertextBlob: BlobTypeDef
    EncryptionContext: Optional[Mapping[str, str]] = None
    GrantTokens: Optional[Sequence[str]] = None
    KeyId: Optional[str] = None
    EncryptionAlgorithm: Optional[EncryptionAlgorithmSpecType] = None
    Recipient: Optional[RecipientInfoTypeDef] = None
    DryRun: Optional[bool] = None

class DeriveSharedSecretRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    KeyAgreementAlgorithm: Literal["ECDH"]
    PublicKey: BlobTypeDef
    GrantTokens: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Recipient: Optional[RecipientInfoTypeDef] = None

class GenerateDataKeyPairRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    KeyPairSpec: DataKeyPairSpecType
    EncryptionContext: Optional[Mapping[str, str]] = None
    GrantTokens: Optional[Sequence[str]] = None
    Recipient: Optional[RecipientInfoTypeDef] = None
    DryRun: Optional[bool] = None

class GenerateDataKeyRequestRequestTypeDef(BaseValidatorModel):
    KeyId: str
    EncryptionContext: Optional[Mapping[str, str]] = None
    NumberOfBytes: Optional[int] = None
    KeySpec: Optional[DataKeySpecType] = None
    GrantTokens: Optional[Sequence[str]] = None
    Recipient: Optional[RecipientInfoTypeDef] = None
    DryRun: Optional[bool] = None

class GenerateRandomRequestRequestTypeDef(BaseValidatorModel):
    NumberOfBytes: Optional[int] = None
    CustomKeyStoreId: Optional[str] = None
    Recipient: Optional[RecipientInfoTypeDef] = None

class DescribeCustomKeyStoresResponseTypeDef(BaseValidatorModel):
    CustomKeyStores: List[CustomKeyStoresListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListGrantsResponseTypeDef(BaseValidatorModel):
    Grants: List[GrantListEntryTypeDef]
    NextMarker: str
    Truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class KeyMetadataTypeDef(BaseValidatorModel):
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

class CreateKeyResponseTypeDef(BaseValidatorModel):
    KeyMetadata: KeyMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyResponseTypeDef(BaseValidatorModel):
    KeyMetadata: KeyMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateKeyResponseTypeDef(BaseValidatorModel):
    ReplicaKeyMetadata: KeyMetadataTypeDef
    ReplicaPolicy: str
    ReplicaTags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.payment_cryptography_constants import *

class AliasTypeDef(BaseValidatorModel):
    AliasName: str
    KeyArn: Optional[str] = None

class CreateAliasInputRequestTypeDef(BaseValidatorModel):
    AliasName: str
    KeyArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class DeleteAliasInputRequestTypeDef(BaseValidatorModel):
    AliasName: str

class DeleteKeyInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str
    DeleteKeyInDays: Optional[int] = None

class ExportDukptInitialKeyTypeDef(BaseValidatorModel):
    KeySerialNumber: str

class ExportKeyCryptogramTypeDef(BaseValidatorModel):
    CertificateAuthorityPublicKeyIdentifier: str
    WrappingKeyCertificate: str
    WrappingSpec: Optional[WrappingKeySpecType] = None

class WrappedKeyTypeDef(BaseValidatorModel):
    WrappingKeyArn: str
    WrappedKeyMaterialFormat: WrappedKeyMaterialFormatType
    KeyMaterial: str
    KeyCheckValue: Optional[str] = None
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None

class GetAliasInputRequestTypeDef(BaseValidatorModel):
    AliasName: str

class GetKeyInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str

class GetParametersForExportInputRequestTypeDef(BaseValidatorModel):
    KeyMaterialType: KeyMaterialTypeType
    SigningKeyAlgorithm: KeyAlgorithmType

class GetParametersForImportInputRequestTypeDef(BaseValidatorModel):
    KeyMaterialType: KeyMaterialTypeType
    WrappingKeyAlgorithm: KeyAlgorithmType

class GetPublicKeyCertificateInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str

class ImportTr31KeyBlockTypeDef(BaseValidatorModel):
    WrappingKeyIdentifier: str
    WrappedKeyBlock: str

class ImportTr34KeyBlockTypeDef(BaseValidatorModel):
    CertificateAuthorityPublicKeyIdentifier: str
    SigningKeyCertificate: str
    ImportToken: str
    WrappedKeyBlock: str
    KeyBlockFormat: Literal["X9_TR34_2012"]
    RandomNonce: Optional[str] = None

class KeyModesOfUseTypeDef(BaseValidatorModel):
    Encrypt: Optional[bool] = None
    Decrypt: Optional[bool] = None
    Wrap: Optional[bool] = None
    Unwrap: Optional[bool] = None
    Generate: Optional[bool] = None
    Sign: Optional[bool] = None
    Verify: Optional[bool] = None
    DeriveKey: Optional[bool] = None
    NoRestrictions: Optional[bool] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAliasesInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListKeysInputRequestTypeDef(BaseValidatorModel):
    KeyState: Optional[KeyStateType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RestoreKeyInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str

class StartKeyUsageInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str

class StopKeyUsageInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAliasInputRequestTypeDef(BaseValidatorModel):
    AliasName: str
    KeyArn: Optional[str] = None

class CreateAliasOutputTypeDef(BaseValidatorModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAliasOutputTypeDef(BaseValidatorModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForExportOutputTypeDef(BaseValidatorModel):
    SigningKeyCertificate: str
    SigningKeyCertificateChain: str
    SigningKeyAlgorithm: KeyAlgorithmType
    ExportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForImportOutputTypeDef(BaseValidatorModel):
    WrappingKeyCertificate: str
    WrappingKeyCertificateChain: str
    WrappingKeyAlgorithm: KeyAlgorithmType
    ImportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyCertificateOutputTypeDef(BaseValidatorModel):
    KeyCertificate: str
    KeyCertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesOutputTypeDef(BaseValidatorModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateAliasOutputTypeDef(BaseValidatorModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ExportAttributesTypeDef(BaseValidatorModel):
    ExportDukptInitialKey: Optional[ExportDukptInitialKeyTypeDef] = None
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None

class ExportKeyOutputTypeDef(BaseValidatorModel):
    WrappedKey: WrappedKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KeyAttributesTypeDef(BaseValidatorModel):
    KeyUsage: KeyUsageType
    KeyClass: KeyClassType
    KeyAlgorithm: KeyAlgorithmType
    KeyModesOfUse: KeyModesOfUseTypeDef

class KeyBlockHeadersTypeDef(BaseValidatorModel):
    KeyModesOfUse: Optional[KeyModesOfUseTypeDef] = None
    KeyExportability: Optional[KeyExportabilityType] = None
    KeyVersion: Optional[str] = None
    OptionalBlocks: Optional[Mapping[str, str]] = None

class ListAliasesInputListAliasesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeysInputListKeysPaginateTypeDef(BaseValidatorModel):
    KeyState: Optional[KeyStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateKeyInputRequestTypeDef(BaseValidatorModel):
    KeyAttributes: KeyAttributesTypeDef
    Exportable: bool
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ImportKeyCryptogramTypeDef(BaseValidatorModel):
    KeyAttributes: KeyAttributesTypeDef
    Exportable: bool
    WrappedKeyCryptogram: str
    ImportToken: str
    WrappingSpec: Optional[WrappingKeySpecType] = None

class KeySummaryTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyState: KeyStateType
    KeyAttributes: KeyAttributesTypeDef
    KeyCheckValue: str
    Exportable: bool
    Enabled: bool

class KeyTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyAttributes: KeyAttributesTypeDef
    KeyCheckValue: str
    KeyCheckValueAlgorithm: KeyCheckValueAlgorithmType
    Enabled: bool
    Exportable: bool
    KeyState: KeyStateType
    KeyOrigin: KeyOriginType
    CreateTimestamp: datetime
    UsageStartTimestamp: Optional[datetime] = None
    UsageStopTimestamp: Optional[datetime] = None
    DeletePendingTimestamp: Optional[datetime] = None
    DeleteTimestamp: Optional[datetime] = None

class RootCertificatePublicKeyTypeDef(BaseValidatorModel):
    KeyAttributes: KeyAttributesTypeDef
    PublicKeyCertificate: str

class TrustedCertificatePublicKeyTypeDef(BaseValidatorModel):
    KeyAttributes: KeyAttributesTypeDef
    PublicKeyCertificate: str
    CertificateAuthorityPublicKeyIdentifier: str

class ExportTr31KeyBlockTypeDef(BaseValidatorModel):
    WrappingKeyIdentifier: str
    KeyBlockHeaders: Optional[KeyBlockHeadersTypeDef] = None

class ExportTr34KeyBlockTypeDef(BaseValidatorModel):
    CertificateAuthorityPublicKeyIdentifier: str
    WrappingKeyCertificate: str
    ExportToken: str
    KeyBlockFormat: Literal["X9_TR34_2012"]
    RandomNonce: Optional[str] = None
    KeyBlockHeaders: Optional[KeyBlockHeadersTypeDef] = None

class ListKeysOutputTypeDef(BaseValidatorModel):
    Keys: List[KeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateKeyOutputTypeDef(BaseValidatorModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeyOutputTypeDef(BaseValidatorModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyOutputTypeDef(BaseValidatorModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportKeyOutputTypeDef(BaseValidatorModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreKeyOutputTypeDef(BaseValidatorModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartKeyUsageOutputTypeDef(BaseValidatorModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopKeyUsageOutputTypeDef(BaseValidatorModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportKeyMaterialTypeDef(BaseValidatorModel):
    RootCertificatePublicKey: Optional[RootCertificatePublicKeyTypeDef] = None
    TrustedCertificatePublicKey: Optional[TrustedCertificatePublicKeyTypeDef] = None
    Tr31KeyBlock: Optional[ImportTr31KeyBlockTypeDef] = None
    Tr34KeyBlock: Optional[ImportTr34KeyBlockTypeDef] = None
    KeyCryptogram: Optional[ImportKeyCryptogramTypeDef] = None

class ExportKeyMaterialTypeDef(BaseValidatorModel):
    Tr31KeyBlock: Optional[ExportTr31KeyBlockTypeDef] = None
    Tr34KeyBlock: Optional[ExportTr34KeyBlockTypeDef] = None
    KeyCryptogram: Optional[ExportKeyCryptogramTypeDef] = None

class ImportKeyInputRequestTypeDef(BaseValidatorModel):
    KeyMaterial: ImportKeyMaterialTypeDef
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ExportKeyInputRequestTypeDef(BaseValidatorModel):
    KeyMaterial: ExportKeyMaterialTypeDef
    ExportKeyIdentifier: str
    ExportAttributes: Optional[ExportAttributesTypeDef] = None


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
from aws_resource_validator.pydantic_models.payment_cryptography_constants import *

class AliasTypeDef(BaseModel):
    AliasName: str
    KeyArn: Optional[str] = None

class CreateAliasInputRequestTypeDef(BaseModel):
    AliasName: str
    KeyArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class DeleteAliasInputRequestTypeDef(BaseModel):
    AliasName: str

class DeleteKeyInputRequestTypeDef(BaseModel):
    KeyIdentifier: str
    DeleteKeyInDays: Optional[int] = None

class ExportDukptInitialKeyTypeDef(BaseModel):
    KeySerialNumber: str

class ExportKeyCryptogramTypeDef(BaseModel):
    CertificateAuthorityPublicKeyIdentifier: str
    WrappingKeyCertificate: str
    WrappingSpec: Optional[WrappingKeySpecType] = None

class WrappedKeyTypeDef(BaseModel):
    WrappingKeyArn: str
    WrappedKeyMaterialFormat: WrappedKeyMaterialFormatType
    KeyMaterial: str
    KeyCheckValue: Optional[str] = None
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None

class GetAliasInputRequestTypeDef(BaseModel):
    AliasName: str

class GetKeyInputRequestTypeDef(BaseModel):
    KeyIdentifier: str

class GetParametersForExportInputRequestTypeDef(BaseModel):
    KeyMaterialType: KeyMaterialTypeType
    SigningKeyAlgorithm: KeyAlgorithmType

class GetParametersForImportInputRequestTypeDef(BaseModel):
    KeyMaterialType: KeyMaterialTypeType
    WrappingKeyAlgorithm: KeyAlgorithmType

class GetPublicKeyCertificateInputRequestTypeDef(BaseModel):
    KeyIdentifier: str

class ImportTr31KeyBlockTypeDef(BaseModel):
    WrappingKeyIdentifier: str
    WrappedKeyBlock: str

class ImportTr34KeyBlockTypeDef(BaseModel):
    CertificateAuthorityPublicKeyIdentifier: str
    SigningKeyCertificate: str
    ImportToken: str
    WrappedKeyBlock: str
    KeyBlockFormat: Literal["X9_TR34_2012"]
    RandomNonce: Optional[str] = None

class KeyModesOfUseTypeDef(BaseModel):
    Encrypt: Optional[bool] = None
    Decrypt: Optional[bool] = None
    Wrap: Optional[bool] = None
    Unwrap: Optional[bool] = None
    Generate: Optional[bool] = None
    Sign: Optional[bool] = None
    Verify: Optional[bool] = None
    DeriveKey: Optional[bool] = None
    NoRestrictions: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAliasesInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListKeysInputRequestTypeDef(BaseModel):
    KeyState: Optional[KeyStateType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RestoreKeyInputRequestTypeDef(BaseModel):
    KeyIdentifier: str

class StartKeyUsageInputRequestTypeDef(BaseModel):
    KeyIdentifier: str

class StopKeyUsageInputRequestTypeDef(BaseModel):
    KeyIdentifier: str

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAliasInputRequestTypeDef(BaseModel):
    AliasName: str
    KeyArn: Optional[str] = None

class CreateAliasOutputTypeDef(BaseModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAliasOutputTypeDef(BaseModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForExportOutputTypeDef(BaseModel):
    SigningKeyCertificate: str
    SigningKeyCertificateChain: str
    SigningKeyAlgorithm: KeyAlgorithmType
    ExportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetParametersForImportOutputTypeDef(BaseModel):
    WrappingKeyCertificate: str
    WrappingKeyCertificateChain: str
    WrappingKeyAlgorithm: KeyAlgorithmType
    ImportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPublicKeyCertificateOutputTypeDef(BaseModel):
    KeyCertificate: str
    KeyCertificateChain: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAliasesOutputTypeDef(BaseModel):
    Aliases: List[AliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateAliasOutputTypeDef(BaseModel):
    Alias: AliasTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class ExportAttributesTypeDef(BaseModel):
    ExportDukptInitialKey: Optional[ExportDukptInitialKeyTypeDef] = None
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None

class ExportKeyOutputTypeDef(BaseModel):
    WrappedKey: WrappedKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KeyAttributesTypeDef(BaseModel):
    KeyUsage: KeyUsageType
    KeyClass: KeyClassType
    KeyAlgorithm: KeyAlgorithmType
    KeyModesOfUse: KeyModesOfUseTypeDef

class KeyBlockHeadersTypeDef(BaseModel):
    KeyModesOfUse: Optional[KeyModesOfUseTypeDef] = None
    KeyExportability: Optional[KeyExportabilityType] = None
    KeyVersion: Optional[str] = None
    OptionalBlocks: Optional[Mapping[str, str]] = None

class ListAliasesInputListAliasesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKeysInputListKeysPaginateTypeDef(BaseModel):
    KeyState: Optional[KeyStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateKeyInputRequestTypeDef(BaseModel):
    KeyAttributes: KeyAttributesTypeDef
    Exportable: bool
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ImportKeyCryptogramTypeDef(BaseModel):
    KeyAttributes: KeyAttributesTypeDef
    Exportable: bool
    WrappedKeyCryptogram: str
    ImportToken: str
    WrappingSpec: Optional[WrappingKeySpecType] = None

class KeySummaryTypeDef(BaseModel):
    KeyArn: str
    KeyState: KeyStateType
    KeyAttributes: KeyAttributesTypeDef
    KeyCheckValue: str
    Exportable: bool
    Enabled: bool

class KeyTypeDef(BaseModel):
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

class RootCertificatePublicKeyTypeDef(BaseModel):
    KeyAttributes: KeyAttributesTypeDef
    PublicKeyCertificate: str

class TrustedCertificatePublicKeyTypeDef(BaseModel):
    KeyAttributes: KeyAttributesTypeDef
    PublicKeyCertificate: str
    CertificateAuthorityPublicKeyIdentifier: str

class ExportTr31KeyBlockTypeDef(BaseModel):
    WrappingKeyIdentifier: str
    KeyBlockHeaders: Optional[KeyBlockHeadersTypeDef] = None

class ExportTr34KeyBlockTypeDef(BaseModel):
    CertificateAuthorityPublicKeyIdentifier: str
    WrappingKeyCertificate: str
    ExportToken: str
    KeyBlockFormat: Literal["X9_TR34_2012"]
    RandomNonce: Optional[str] = None
    KeyBlockHeaders: Optional[KeyBlockHeadersTypeDef] = None

class ListKeysOutputTypeDef(BaseModel):
    Keys: List[KeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateKeyOutputTypeDef(BaseModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeyOutputTypeDef(BaseModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyOutputTypeDef(BaseModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportKeyOutputTypeDef(BaseModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreKeyOutputTypeDef(BaseModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartKeyUsageOutputTypeDef(BaseModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopKeyUsageOutputTypeDef(BaseModel):
    Key: KeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportKeyMaterialTypeDef(BaseModel):
    RootCertificatePublicKey: Optional[RootCertificatePublicKeyTypeDef] = None
    TrustedCertificatePublicKey: Optional[TrustedCertificatePublicKeyTypeDef] = None
    Tr31KeyBlock: Optional[ImportTr31KeyBlockTypeDef] = None
    Tr34KeyBlock: Optional[ImportTr34KeyBlockTypeDef] = None
    KeyCryptogram: Optional[ImportKeyCryptogramTypeDef] = None

class ExportKeyMaterialTypeDef(BaseModel):
    Tr31KeyBlock: Optional[ExportTr31KeyBlockTypeDef] = None
    Tr34KeyBlock: Optional[ExportTr34KeyBlockTypeDef] = None
    KeyCryptogram: Optional[ExportKeyCryptogramTypeDef] = None

class ImportKeyInputRequestTypeDef(BaseModel):
    KeyMaterial: ImportKeyMaterialTypeDef
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ExportKeyInputRequestTypeDef(BaseModel):
    KeyMaterial: ExportKeyMaterialTypeDef
    ExportKeyIdentifier: str
    ExportAttributes: Optional[ExportAttributesTypeDef] = None


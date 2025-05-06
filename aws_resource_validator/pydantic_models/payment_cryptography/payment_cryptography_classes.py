from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Alias(BaseValidatorModel):
    AliasName: str
    KeyArn: Optional[str] = None


class CreateAliasInput(BaseValidatorModel):
    AliasName: str
    KeyArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class DeleteAliasInput(BaseValidatorModel):
    AliasName: str


class DeleteKeyInput(BaseValidatorModel):
    KeyIdentifier: str
    DeleteKeyInDays: Optional[int] = None


class ExportDukptInitialKey(BaseValidatorModel):
    KeySerialNumber: str


class ExportKeyCryptogram(BaseValidatorModel):
    CertificateAuthorityPublicKeyIdentifier: str
    WrappingKeyCertificate: str
    WrappingSpec: Optional[WrappingKeySpecType] = None


class WrappedKey(BaseValidatorModel):
    WrappingKeyArn: str
    WrappedKeyMaterialFormat: WrappedKeyMaterialFormatType
    KeyMaterial: str
    KeyCheckValue: Optional[str] = None
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None


class GetAliasInput(BaseValidatorModel):
    AliasName: str


class GetKeyInput(BaseValidatorModel):
    KeyIdentifier: str


class GetParametersForExportInput(BaseValidatorModel):
    KeyMaterialType: KeyMaterialTypeType
    SigningKeyAlgorithm: KeyAlgorithmType


class GetParametersForImportInput(BaseValidatorModel):
    KeyMaterialType: KeyMaterialTypeType
    WrappingKeyAlgorithm: KeyAlgorithmType


class GetPublicKeyCertificateInput(BaseValidatorModel):
    KeyIdentifier: str


class ImportTr31KeyBlock(BaseValidatorModel):
    WrappingKeyIdentifier: str
    WrappedKeyBlock: str


class ImportTr34KeyBlock(BaseValidatorModel):
    CertificateAuthorityPublicKeyIdentifier: str
    SigningKeyCertificate: str
    ImportToken: str
    WrappedKeyBlock: str
    KeyBlockFormat: Literal['X9_TR34_2012']
    RandomNonce: Optional[str] = None


class KeyModesOfUse(BaseValidatorModel):
    Encrypt: Optional[bool] = None
    Decrypt: Optional[bool] = None
    Wrap: Optional[bool] = None
    Unwrap: Optional[bool] = None
    Generate: Optional[bool] = None
    Sign: Optional[bool] = None
    Verify: Optional[bool] = None
    DeriveKey: Optional[bool] = None
    NoRestrictions: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAliasesInput(BaseValidatorModel):
    KeyArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListKeysInput(BaseValidatorModel):
    KeyState: Optional[KeyStateType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RestoreKeyInput(BaseValidatorModel):
    KeyIdentifier: str


class StartKeyUsageInput(BaseValidatorModel):
    KeyIdentifier: str


class StopKeyUsageInput(BaseValidatorModel):
    KeyIdentifier: str


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateAliasInput(BaseValidatorModel):
    AliasName: str
    KeyArn: Optional[str] = None


class CreateAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


class GetAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


class GetParametersForExportOutput(BaseValidatorModel):
    SigningKeyCertificate: str
    SigningKeyCertificateChain: str
    SigningKeyAlgorithm: KeyAlgorithmType
    ExportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetParametersForImportOutput(BaseValidatorModel):
    WrappingKeyCertificate: str
    WrappingKeyCertificateChain: str
    WrappingKeyAlgorithm: KeyAlgorithmType
    ImportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetPublicKeyCertificateOutput(BaseValidatorModel):
    KeyCertificate: str
    KeyCertificateChain: str
    ResponseMetadata: ResponseMetadata


class ListAliasesOutput(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class ExportAttributes(BaseValidatorModel):
    ExportDukptInitialKey: Optional[ExportDukptInitialKey] = None
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None


class ExportKeyOutput(BaseValidatorModel):
    WrappedKey: WrappedKey
    ResponseMetadata: ResponseMetadata


class KeyAttributes(BaseValidatorModel):
    KeyUsage: KeyUsageType
    KeyClass: KeyClassType
    KeyAlgorithm: KeyAlgorithmType
    KeyModesOfUse: KeyModesOfUse


class KeyBlockHeaders(BaseValidatorModel):
    KeyModesOfUse: Optional[KeyModesOfUse] = None
    KeyExportability: Optional[KeyExportabilityType] = None
    KeyVersion: Optional[str] = None
    OptionalBlocks: Optional[Dict[str, str]] = None


class ListAliasesInputPaginate(BaseValidatorModel):
    KeyArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKeysInputPaginate(BaseValidatorModel):
    KeyState: Optional[KeyStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceInputPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class CreateKeyInput(BaseValidatorModel):
    KeyAttributes: KeyAttributes
    Exportable: bool
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class ImportKeyCryptogram(BaseValidatorModel):
    KeyAttributes: KeyAttributes
    Exportable: bool
    WrappedKeyCryptogram: str
    ImportToken: str
    WrappingSpec: Optional[WrappingKeySpecType] = None


class KeySummary(BaseValidatorModel):
    KeyArn: str
    KeyState: KeyStateType
    KeyAttributes: KeyAttributes
    KeyCheckValue: str
    Exportable: bool
    Enabled: bool


class Key(BaseValidatorModel):
    KeyArn: str
    KeyAttributes: KeyAttributes
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


class RootCertificatePublicKey(BaseValidatorModel):
    KeyAttributes: KeyAttributes
    PublicKeyCertificate: str


class TrustedCertificatePublicKey(BaseValidatorModel):
    KeyAttributes: KeyAttributes
    PublicKeyCertificate: str
    CertificateAuthorityPublicKeyIdentifier: str


class ExportTr31KeyBlock(BaseValidatorModel):
    WrappingKeyIdentifier: str
    KeyBlockHeaders: Optional[KeyBlockHeaders] = None


class ExportTr34KeyBlock(BaseValidatorModel):
    CertificateAuthorityPublicKeyIdentifier: str
    WrappingKeyCertificate: str
    ExportToken: str
    KeyBlockFormat: Literal['X9_TR34_2012']
    RandomNonce: Optional[str] = None
    KeyBlockHeaders: Optional[KeyBlockHeaders] = None


class ListKeysOutput(BaseValidatorModel):
    Keys: List[KeySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


class DeleteKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


class GetKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


class ImportKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


class RestoreKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


class StartKeyUsageOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


class StopKeyUsageOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


class ImportKeyMaterial(BaseValidatorModel):
    RootCertificatePublicKey: Optional[RootCertificatePublicKey] = None
    TrustedCertificatePublicKey: Optional[TrustedCertificatePublicKey] = None
    Tr31KeyBlock: Optional[ImportTr31KeyBlock] = None
    Tr34KeyBlock: Optional[ImportTr34KeyBlock] = None
    KeyCryptogram: Optional[ImportKeyCryptogram] = None


class ExportKeyMaterial(BaseValidatorModel):
    Tr31KeyBlock: Optional[ExportTr31KeyBlock] = None
    Tr34KeyBlock: Optional[ExportTr34KeyBlock] = None
    KeyCryptogram: Optional[ExportKeyCryptogram] = None


class ImportKeyInput(BaseValidatorModel):
    KeyMaterial: ImportKeyMaterial
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class ExportKeyInput(BaseValidatorModel):
    KeyMaterial: ExportKeyMaterial
    ExportKeyIdentifier: str
    ExportAttributes: Optional[ExportAttributes] = None
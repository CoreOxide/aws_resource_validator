from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.payment_cryptography.payment_cryptography_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Alias(BaseValidatorModel):
    AliasName: str
    KeyArn: Optional[str] = None


# This class is the input for the 'create_alias' function.
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


# This class is the input for the 'delete_key' function.
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


# This class is the input for the 'get_alias' function.
class GetAliasInput(BaseValidatorModel):
    AliasName: str


# This class is the input for the 'get_key' function.
class GetKeyInput(BaseValidatorModel):
    KeyIdentifier: str


# This class is the input for the 'get_parameters_for_export' function.
class GetParametersForExportInput(BaseValidatorModel):
    KeyMaterialType: KeyMaterialTypeType
    SigningKeyAlgorithm: KeyAlgorithmType


# This class is the input for the 'get_parameters_for_import' function.
class GetParametersForImportInput(BaseValidatorModel):
    KeyMaterialType: KeyMaterialTypeType
    WrappingKeyAlgorithm: KeyAlgorithmType


# This class is the input for the 'get_public_key_certificate' function.
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


# This class is the input for the 'list_aliases' function.
class ListAliasesInput(BaseValidatorModel):
    KeyArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_keys' function.
class ListKeysInput(BaseValidatorModel):
    KeyState: Optional[KeyStateType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'restore_key' function.
class RestoreKeyInput(BaseValidatorModel):
    KeyIdentifier: str


# This class is the input for the 'start_key_usage' function.
class StartKeyUsageInput(BaseValidatorModel):
    KeyIdentifier: str


# This class is the input for the 'stop_key_usage' function.
class StopKeyUsageInput(BaseValidatorModel):
    KeyIdentifier: str


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_alias' function.
class UpdateAliasInput(BaseValidatorModel):
    AliasName: str
    KeyArn: Optional[str] = None


# This class is the output for the 'create_alias' function.
class CreateAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_alias' function.
class GetAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_parameters_for_export' function.
class GetParametersForExportOutput(BaseValidatorModel):
    SigningKeyCertificate: str
    SigningKeyCertificateChain: str
    SigningKeyAlgorithm: KeyAlgorithmType
    ExportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_parameters_for_import' function.
class GetParametersForImportOutput(BaseValidatorModel):
    WrappingKeyCertificate: str
    WrappingKeyCertificateChain: str
    WrappingKeyAlgorithm: KeyAlgorithmType
    ImportToken: str
    ParametersValidUntilTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_public_key_certificate' function.
class GetPublicKeyCertificateOutput(BaseValidatorModel):
    KeyCertificate: str
    KeyCertificateChain: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_aliases' function.
class ListAliasesOutput(BaseValidatorModel):
    Aliases: List[Alias]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_alias' function.
class UpdateAliasOutput(BaseValidatorModel):
    Alias: Alias
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
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


# This class is the output for the 'export_key' function.
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


# This class is the input for the 'create_key' function.
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


# This class is the output for the 'list_keys' function.
class ListKeysOutput(BaseValidatorModel):
    Keys: List[KeySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_key' function.
class CreateKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_key' function.
class DeleteKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_key' function.
class GetKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_key' function.
class ImportKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_key' function.
class RestoreKeyOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_key_usage' function.
class StartKeyUsageOutput(BaseValidatorModel):
    Key: Key
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_key_usage' function.
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


# This class is the input for the 'import_key' function.
class ImportKeyInput(BaseValidatorModel):
    KeyMaterial: ImportKeyMaterial
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'export_key' function.
class ExportKeyInput(BaseValidatorModel):
    KeyMaterial: ExportKeyMaterial
    ExportKeyIdentifier: str
    ExportAttributes: Optional[ExportAttributes] = None
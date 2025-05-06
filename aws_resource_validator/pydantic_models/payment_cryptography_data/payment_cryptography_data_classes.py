from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.payment_cryptography_data.payment_cryptography_data_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class CurrentPinAttributes(BaseValidatorModel):
    CurrentPinPekIdentifier: str
    CurrentEncryptedPinBlock: str


class AmexCardSecurityCodeVersion1(BaseValidatorModel):
    CardExpiryDate: str


class AmexCardSecurityCodeVersion2(BaseValidatorModel):
    CardExpiryDate: str
    ServiceCode: str


class AsymmetricEncryptionAttributes(BaseValidatorModel):
    PaddingType: Optional[PaddingTypeType] = None


class CardHolderVerificationValue(BaseValidatorModel):
    UnpredictableNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str


class CardVerificationValue1(BaseValidatorModel):
    CardExpiryDate: str
    ServiceCode: str


class CardVerificationValue2(BaseValidatorModel):
    CardExpiryDate: str


class DynamicCardVerificationCode(BaseValidatorModel):
    UnpredictableNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    TrackData: str


class DynamicCardVerificationValue(BaseValidatorModel):
    PanSequenceNumber: str
    CardExpiryDate: str
    ServiceCode: str
    ApplicationTransactionCounter: str


class DiscoverDynamicCardVerificationCode(BaseValidatorModel):
    CardExpiryDate: str
    UnpredictableNumber: str
    ApplicationTransactionCounter: str


class CryptogramVerificationArpcMethod1(BaseValidatorModel):
    AuthResponseCode: str


class CryptogramVerificationArpcMethod2(BaseValidatorModel):
    CardStatusUpdate: str
    ProprietaryAuthenticationData: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Emv2000Attributes(BaseValidatorModel):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str


class EmvCommonAttributes(BaseValidatorModel):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationCryptogram: str
    Mode: EmvEncryptionModeType
    PinBlockPaddingType: PinBlockPaddingTypeType
    PinBlockLengthPosition: PinBlockLengthPositionType


class MasterCardAttributes(BaseValidatorModel):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationCryptogram: str


class DukptAttributes(BaseValidatorModel):
    KeySerialNumber: str
    DukptDerivationType: DukptDerivationTypeType


class DukptDerivationAttributes(BaseValidatorModel):
    KeySerialNumber: str
    DukptKeyDerivationType: Optional[DukptDerivationTypeType] = None
    DukptKeyVariant: Optional[DukptKeyVariantType] = None


class DukptEncryptionAttributes(BaseValidatorModel):
    KeySerialNumber: str
    Mode: Optional[DukptEncryptionModeType] = None
    DukptKeyDerivationType: Optional[DukptDerivationTypeType] = None
    DukptKeyVariant: Optional[DukptKeyVariantType] = None
    InitializationVector: Optional[str] = None


class EcdhDerivationAttributes(BaseValidatorModel):
    CertificateAuthorityPublicKeyIdentifier: str
    PublicKeyCertificate: str
    KeyAlgorithm: SymmetricKeyAlgorithmType
    KeyDerivationFunction: KeyDerivationFunctionType
    KeyDerivationHashAlgorithm: KeyDerivationHashAlgorithmType
    SharedInformation: str


class EmvEncryptionAttributes(BaseValidatorModel):
    MajorKeyDerivationMode: EmvMajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    SessionDerivationData: str
    Mode: Optional[EmvEncryptionModeType] = None
    InitializationVector: Optional[str] = None


class SymmetricEncryptionAttributes(BaseValidatorModel):
    Mode: EncryptionModeType
    InitializationVector: Optional[str] = None
    PaddingType: Optional[PaddingTypeType] = None


class VisaAmexDerivationOutputs(BaseValidatorModel):
    AuthorizationRequestKeyArn: str
    AuthorizationRequestKeyCheckValue: str
    CurrentPinPekArn: Optional[str] = None
    CurrentPinPekKeyCheckValue: Optional[str] = None


class PinData(BaseValidatorModel):
    PinOffset: Optional[str] = None
    VerificationValue: Optional[str] = None


class Ibm3624NaturalPin(BaseValidatorModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str


class Ibm3624PinFromOffset(BaseValidatorModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str
    PinOffset: str


class Ibm3624PinOffset(BaseValidatorModel):
    EncryptedPinBlock: str
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str


class Ibm3624PinVerification(BaseValidatorModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str
    PinOffset: str


class Ibm3624RandomPin(BaseValidatorModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str


class MacAlgorithmDukpt(BaseValidatorModel):
    KeySerialNumber: str
    DukptKeyVariant: DukptKeyVariantType
    DukptDerivationType: Optional[DukptDerivationTypeType] = None


class SessionKeyDerivationValue(BaseValidatorModel):
    ApplicationCryptogram: Optional[str] = None
    ApplicationTransactionCounter: Optional[str] = None


class VisaPin(BaseValidatorModel):
    PinVerificationKeyIndex: int


class VisaPinVerificationValue(BaseValidatorModel):
    EncryptedPinBlock: str
    PinVerificationKeyIndex: int


class VisaPinVerification(BaseValidatorModel):
    PinVerificationKeyIndex: int
    VerificationValue: str


class SessionKeyAmex(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str


class SessionKeyEmv2000(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str


class SessionKeyEmvCommon(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str


class SessionKeyMastercard(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    UnpredictableNumber: str


class SessionKeyVisa(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str


class TranslationPinDataIsoFormat034(BaseValidatorModel):
    PrimaryAccountNumber: str


class AmexAttributes(BaseValidatorModel):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    AuthorizationRequestKeyIdentifier: str
    CurrentPinAttributes: Optional[CurrentPinAttributes] = None


class VisaAttributes(BaseValidatorModel):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    AuthorizationRequestKeyIdentifier: str
    CurrentPinAttributes: Optional[CurrentPinAttributes] = None


class CardGenerationAttributes(BaseValidatorModel):
    AmexCardSecurityCodeVersion1: Optional[AmexCardSecurityCodeVersion1] = None
    AmexCardSecurityCodeVersion2: Optional[AmexCardSecurityCodeVersion2] = None
    CardVerificationValue1: Optional[CardVerificationValue1] = None
    CardVerificationValue2: Optional[CardVerificationValue2] = None
    CardHolderVerificationValue: Optional[CardHolderVerificationValue] = None
    DynamicCardVerificationCode: Optional[DynamicCardVerificationCode] = None
    DynamicCardVerificationValue: Optional[DynamicCardVerificationValue] = None


class CardVerificationAttributes(BaseValidatorModel):
    AmexCardSecurityCodeVersion1: Optional[AmexCardSecurityCodeVersion1] = None
    AmexCardSecurityCodeVersion2: Optional[AmexCardSecurityCodeVersion2] = None
    CardVerificationValue1: Optional[CardVerificationValue1] = None
    CardVerificationValue2: Optional[CardVerificationValue2] = None
    CardHolderVerificationValue: Optional[CardHolderVerificationValue] = None
    DynamicCardVerificationCode: Optional[DynamicCardVerificationCode] = None
    DynamicCardVerificationValue: Optional[DynamicCardVerificationValue] = None
    DiscoverDynamicCardVerificationCode: Optional[DiscoverDynamicCardVerificationCode] = None


class CryptogramAuthResponse(BaseValidatorModel):
    ArpcMethod1: Optional[CryptogramVerificationArpcMethod1] = None
    ArpcMethod2: Optional[CryptogramVerificationArpcMethod2] = None


class DecryptDataOutput(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    PlainText: str
    ResponseMetadata: ResponseMetadata


class EncryptDataOutput(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    CipherText: str
    ResponseMetadata: ResponseMetadata


class GenerateCardValidationDataOutput(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    ValidationData: str
    ResponseMetadata: ResponseMetadata


class GenerateMacOutput(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    Mac: str
    ResponseMetadata: ResponseMetadata


class ReEncryptDataOutput(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    CipherText: str
    ResponseMetadata: ResponseMetadata


class TranslatePinDataOutput(BaseValidatorModel):
    PinBlock: str
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadata


class VerifyAuthRequestCryptogramOutput(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    AuthResponseValue: str
    ResponseMetadata: ResponseMetadata


class VerifyCardValidationDataOutput(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadata


class VerifyMacOutput(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadata


class VerifyPinDataOutput(BaseValidatorModel):
    VerificationKeyArn: str
    VerificationKeyCheckValue: str
    EncryptionKeyArn: str
    EncryptionKeyCheckValue: str
    ResponseMetadata: ResponseMetadata


class WrappedKeyMaterial(BaseValidatorModel):
    Tr31KeyBlock: Optional[str] = None
    DiffieHellmanSymmetricKey: Optional[EcdhDerivationAttributes] = None


class EncryptionDecryptionAttributes(BaseValidatorModel):
    Symmetric: Optional[SymmetricEncryptionAttributes] = None
    Asymmetric: Optional[AsymmetricEncryptionAttributes] = None
    Dukpt: Optional[DukptEncryptionAttributes] = None
    Emv: Optional[EmvEncryptionAttributes] = None


class ReEncryptionAttributes(BaseValidatorModel):
    Symmetric: Optional[SymmetricEncryptionAttributes] = None
    Dukpt: Optional[DukptEncryptionAttributes] = None


class GenerateMacEmvPinChangeOutput(BaseValidatorModel):
    NewPinPekArn: str
    SecureMessagingIntegrityKeyArn: str
    SecureMessagingConfidentialityKeyArn: str
    Mac: str
    EncryptedPinBlock: str
    NewPinPekKeyCheckValue: str
    SecureMessagingIntegrityKeyCheckValue: str
    SecureMessagingConfidentialityKeyCheckValue: str
    VisaAmexDerivationOutputs: VisaAmexDerivationOutputs
    ResponseMetadata: ResponseMetadata


class GeneratePinDataOutput(BaseValidatorModel):
    GenerationKeyArn: str
    GenerationKeyCheckValue: str
    EncryptionKeyArn: str
    EncryptionKeyCheckValue: str
    EncryptedPinBlock: str
    PinData: PinData
    ResponseMetadata: ResponseMetadata


class MacAlgorithmEmv(BaseValidatorModel):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    SessionKeyDerivationMode: SessionKeyDerivationModeType
    SessionKeyDerivationValue: SessionKeyDerivationValue


class PinGenerationAttributes(BaseValidatorModel):
    VisaPin: Optional[VisaPin] = None
    VisaPinVerificationValue: Optional[VisaPinVerificationValue] = None
    Ibm3624PinOffset: Optional[Ibm3624PinOffset] = None
    Ibm3624NaturalPin: Optional[Ibm3624NaturalPin] = None
    Ibm3624RandomPin: Optional[Ibm3624RandomPin] = None
    Ibm3624PinFromOffset: Optional[Ibm3624PinFromOffset] = None


class PinVerificationAttributes(BaseValidatorModel):
    VisaPin: Optional[VisaPinVerification] = None
    Ibm3624Pin: Optional[Ibm3624PinVerification] = None


class SessionKeyDerivation(BaseValidatorModel):
    EmvCommon: Optional[SessionKeyEmvCommon] = None
    Mastercard: Optional[SessionKeyMastercard] = None
    Emv2000: Optional[SessionKeyEmv2000] = None
    Amex: Optional[SessionKeyAmex] = None
    Visa: Optional[SessionKeyVisa] = None


class TranslationIsoFormats(BaseValidatorModel):
    IsoFormat0: Optional[TranslationPinDataIsoFormat034] = None
    IsoFormat1: Optional[Dict[str, Any]] = None
    IsoFormat3: Optional[TranslationPinDataIsoFormat034] = None
    IsoFormat4: Optional[TranslationPinDataIsoFormat034] = None


class DerivationMethodAttributes(BaseValidatorModel):
    EmvCommon: Optional[EmvCommonAttributes] = None
    Amex: Optional[AmexAttributes] = None
    Visa: Optional[VisaAttributes] = None
    Emv2000: Optional[Emv2000Attributes] = None
    Mastercard: Optional[MasterCardAttributes] = None


class GenerateCardValidationDataInput(BaseValidatorModel):
    KeyIdentifier: str
    PrimaryAccountNumber: str
    GenerationAttributes: CardGenerationAttributes
    ValidationDataLength: Optional[int] = None


class VerifyCardValidationDataInput(BaseValidatorModel):
    KeyIdentifier: str
    PrimaryAccountNumber: str
    VerificationAttributes: CardVerificationAttributes
    ValidationData: str


class WrappedKey(BaseValidatorModel):
    WrappedKeyMaterial: WrappedKeyMaterial
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None


class MacAttributes(BaseValidatorModel):
    Algorithm: Optional[MacAlgorithmType] = None
    EmvMac: Optional[MacAlgorithmEmv] = None
    DukptIso9797Algorithm1: Optional[MacAlgorithmDukpt] = None
    DukptIso9797Algorithm3: Optional[MacAlgorithmDukpt] = None
    DukptCmac: Optional[MacAlgorithmDukpt] = None


class VerifyAuthRequestCryptogramInput(BaseValidatorModel):
    KeyIdentifier: str
    TransactionData: str
    AuthRequestCryptogram: str
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    SessionKeyDerivationAttributes: SessionKeyDerivation
    AuthResponseAttributes: Optional[CryptogramAuthResponse] = None


class GenerateMacEmvPinChangeInput(BaseValidatorModel):
    NewPinPekIdentifier: str
    NewEncryptedPinBlock: str
    PinBlockFormat: PinBlockFormatForEmvPinChangeType
    SecureMessagingIntegrityKeyIdentifier: str
    SecureMessagingConfidentialityKeyIdentifier: str
    MessageData: str
    DerivationMethodAttributes: DerivationMethodAttributes


class DecryptDataInput(BaseValidatorModel):
    KeyIdentifier: str
    CipherText: str
    DecryptionAttributes: EncryptionDecryptionAttributes
    WrappedKey: Optional[WrappedKey] = None


class EncryptDataInput(BaseValidatorModel):
    KeyIdentifier: str
    PlainText: str
    EncryptionAttributes: EncryptionDecryptionAttributes
    WrappedKey: Optional[WrappedKey] = None


class GeneratePinDataInput(BaseValidatorModel):
    GenerationKeyIdentifier: str
    EncryptionKeyIdentifier: str
    GenerationAttributes: PinGenerationAttributes
    PrimaryAccountNumber: str
    PinBlockFormat: PinBlockFormatForPinDataType
    PinDataLength: Optional[int] = None
    EncryptionWrappedKey: Optional[WrappedKey] = None


class ReEncryptDataInput(BaseValidatorModel):
    IncomingKeyIdentifier: str
    OutgoingKeyIdentifier: str
    CipherText: str
    IncomingEncryptionAttributes: ReEncryptionAttributes
    OutgoingEncryptionAttributes: ReEncryptionAttributes
    IncomingWrappedKey: Optional[WrappedKey] = None
    OutgoingWrappedKey: Optional[WrappedKey] = None


class TranslatePinDataInput(BaseValidatorModel):
    IncomingKeyIdentifier: str
    OutgoingKeyIdentifier: str
    IncomingTranslationAttributes: TranslationIsoFormats
    OutgoingTranslationAttributes: TranslationIsoFormats
    EncryptedPinBlock: str
    IncomingDukptAttributes: Optional[DukptDerivationAttributes] = None
    OutgoingDukptAttributes: Optional[DukptDerivationAttributes] = None
    IncomingWrappedKey: Optional[WrappedKey] = None
    OutgoingWrappedKey: Optional[WrappedKey] = None


class VerifyPinDataInput(BaseValidatorModel):
    VerificationKeyIdentifier: str
    EncryptionKeyIdentifier: str
    VerificationAttributes: PinVerificationAttributes
    EncryptedPinBlock: str
    PrimaryAccountNumber: str
    PinBlockFormat: PinBlockFormatForPinDataType
    PinDataLength: Optional[int] = None
    DukptAttributes: Optional[DukptAttributes] = None
    EncryptionWrappedKey: Optional[WrappedKey] = None


class GenerateMacInput(BaseValidatorModel):
    KeyIdentifier: str
    MessageData: str
    GenerationAttributes: MacAttributes
    MacLength: Optional[int] = None


class VerifyMacInput(BaseValidatorModel):
    KeyIdentifier: str
    MessageData: str
    Mac: str
    VerificationAttributes: MacAttributes
    MacLength: Optional[int] = None
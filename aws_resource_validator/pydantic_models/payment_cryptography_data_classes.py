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
from aws_resource_validator.pydantic_models.payment_cryptography_data_constants import *

class AmexCardSecurityCodeVersion1TypeDef(BaseValidatorModel):
    CardExpiryDate: str

class AmexCardSecurityCodeVersion2TypeDef(BaseValidatorModel):
    CardExpiryDate: str
    ServiceCode: str

class AsymmetricEncryptionAttributesTypeDef(BaseValidatorModel):
    PaddingType: Optional[PaddingTypeType] = None

class CardHolderVerificationValueTypeDef(BaseValidatorModel):
    UnpredictableNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class CardVerificationValue1TypeDef(BaseValidatorModel):
    CardExpiryDate: str
    ServiceCode: str

class CardVerificationValue2TypeDef(BaseValidatorModel):
    CardExpiryDate: str

class DynamicCardVerificationCodeTypeDef(BaseValidatorModel):
    UnpredictableNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    TrackData: str

class DynamicCardVerificationValueTypeDef(BaseValidatorModel):
    PanSequenceNumber: str
    CardExpiryDate: str
    ServiceCode: str
    ApplicationTransactionCounter: str

class DiscoverDynamicCardVerificationCodeTypeDef(BaseValidatorModel):
    CardExpiryDate: str
    UnpredictableNumber: str
    ApplicationTransactionCounter: str

class CryptogramVerificationArpcMethod1TypeDef(BaseValidatorModel):
    AuthResponseCode: str

class CryptogramVerificationArpcMethod2TypeDef(BaseValidatorModel):
    CardStatusUpdate: str
    ProprietaryAuthenticationData: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DukptAttributesTypeDef(BaseValidatorModel):
    KeySerialNumber: str
    DukptDerivationType: DukptDerivationTypeType

class DukptDerivationAttributesTypeDef(BaseValidatorModel):
    KeySerialNumber: str
    DukptKeyDerivationType: Optional[DukptDerivationTypeType] = None
    DukptKeyVariant: Optional[DukptKeyVariantType] = None

class DukptEncryptionAttributesTypeDef(BaseValidatorModel):
    KeySerialNumber: str
    Mode: Optional[DukptEncryptionModeType] = None
    DukptKeyDerivationType: Optional[DukptDerivationTypeType] = None
    DukptKeyVariant: Optional[DukptKeyVariantType] = None
    InitializationVector: Optional[str] = None

class EmvEncryptionAttributesTypeDef(BaseValidatorModel):
    MajorKeyDerivationMode: EmvMajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    SessionDerivationData: str
    Mode: Optional[EmvEncryptionModeType] = None
    InitializationVector: Optional[str] = None

class SymmetricEncryptionAttributesTypeDef(BaseValidatorModel):
    Mode: EncryptionModeType
    InitializationVector: Optional[str] = None
    PaddingType: Optional[PaddingTypeType] = None

class PinDataTypeDef(BaseValidatorModel):
    PinOffset: Optional[str] = None
    VerificationValue: Optional[str] = None

class Ibm3624NaturalPinTypeDef(BaseValidatorModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class Ibm3624PinFromOffsetTypeDef(BaseValidatorModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str
    PinOffset: str

class Ibm3624PinOffsetTypeDef(BaseValidatorModel):
    EncryptedPinBlock: str
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class Ibm3624PinVerificationTypeDef(BaseValidatorModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str
    PinOffset: str

class Ibm3624RandomPinTypeDef(BaseValidatorModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class MacAlgorithmDukptTypeDef(BaseValidatorModel):
    KeySerialNumber: str
    DukptKeyVariant: DukptKeyVariantType
    DukptDerivationType: Optional[DukptDerivationTypeType] = None

class SessionKeyDerivationValueTypeDef(BaseValidatorModel):
    ApplicationCryptogram: Optional[str] = None
    ApplicationTransactionCounter: Optional[str] = None

class VisaPinTypeDef(BaseValidatorModel):
    PinVerificationKeyIndex: int

class VisaPinVerificationValueTypeDef(BaseValidatorModel):
    EncryptedPinBlock: str
    PinVerificationKeyIndex: int

class VisaPinVerificationTypeDef(BaseValidatorModel):
    PinVerificationKeyIndex: int
    VerificationValue: str

class SessionKeyAmexTypeDef(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str

class SessionKeyEmv2000TypeDef(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class SessionKeyEmvCommonTypeDef(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class SessionKeyMastercardTypeDef(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    UnpredictableNumber: str

class SessionKeyVisaTypeDef(BaseValidatorModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str

class TranslationPinDataIsoFormat034TypeDef(BaseValidatorModel):
    PrimaryAccountNumber: str

class WrappedKeyMaterialTypeDef(BaseValidatorModel):
    Tr31KeyBlock: Optional[str] = None

class CardGenerationAttributesTypeDef(BaseValidatorModel):
    AmexCardSecurityCodeVersion1: Optional[AmexCardSecurityCodeVersion1TypeDef] = None
    AmexCardSecurityCodeVersion2: Optional[AmexCardSecurityCodeVersion2TypeDef] = None
    CardVerificationValue1: Optional[CardVerificationValue1TypeDef] = None
    CardVerificationValue2: Optional[CardVerificationValue2TypeDef] = None
    CardHolderVerificationValue: Optional[CardHolderVerificationValueTypeDef] = None
    DynamicCardVerificationCode: Optional[DynamicCardVerificationCodeTypeDef] = None
    DynamicCardVerificationValue: Optional[DynamicCardVerificationValueTypeDef] = None

class CardVerificationAttributesTypeDef(BaseValidatorModel):
    AmexCardSecurityCodeVersion1: Optional[AmexCardSecurityCodeVersion1TypeDef] = None
    AmexCardSecurityCodeVersion2: Optional[AmexCardSecurityCodeVersion2TypeDef] = None
    CardVerificationValue1: Optional[CardVerificationValue1TypeDef] = None
    CardVerificationValue2: Optional[CardVerificationValue2TypeDef] = None
    CardHolderVerificationValue: Optional[CardHolderVerificationValueTypeDef] = None
    DynamicCardVerificationCode: Optional[DynamicCardVerificationCodeTypeDef] = None
    DynamicCardVerificationValue: Optional[DynamicCardVerificationValueTypeDef] = None
    DiscoverDynamicCardVerificationCode: Optional[       DiscoverDynamicCardVerificationCodeTypeDef     ] = None

class CryptogramAuthResponseTypeDef(BaseValidatorModel):
    ArpcMethod1: Optional[CryptogramVerificationArpcMethod1TypeDef] = None
    ArpcMethod2: Optional[CryptogramVerificationArpcMethod2TypeDef] = None

class DecryptDataOutputTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    PlainText: str
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptDataOutputTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    CipherText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateCardValidationDataOutputTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    ValidationData: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMacOutputTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    Mac: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReEncryptDataOutputTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    CipherText: str
    ResponseMetadata: ResponseMetadataTypeDef

class TranslatePinDataOutputTypeDef(BaseValidatorModel):
    PinBlock: str
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyAuthRequestCryptogramOutputTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    AuthResponseValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyCardValidationDataOutputTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyMacOutputTypeDef(BaseValidatorModel):
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyPinDataOutputTypeDef(BaseValidatorModel):
    VerificationKeyArn: str
    VerificationKeyCheckValue: str
    EncryptionKeyArn: str
    EncryptionKeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptionDecryptionAttributesTypeDef(BaseValidatorModel):
    Symmetric: Optional[SymmetricEncryptionAttributesTypeDef] = None
    Asymmetric: Optional[AsymmetricEncryptionAttributesTypeDef] = None
    Dukpt: Optional[DukptEncryptionAttributesTypeDef] = None
    Emv: Optional[EmvEncryptionAttributesTypeDef] = None

class ReEncryptionAttributesTypeDef(BaseValidatorModel):
    Symmetric: Optional[SymmetricEncryptionAttributesTypeDef] = None
    Dukpt: Optional[DukptEncryptionAttributesTypeDef] = None

class GeneratePinDataOutputTypeDef(BaseValidatorModel):
    GenerationKeyArn: str
    GenerationKeyCheckValue: str
    EncryptionKeyArn: str
    EncryptionKeyCheckValue: str
    EncryptedPinBlock: str
    PinData: PinDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MacAlgorithmEmvTypeDef(BaseValidatorModel):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    SessionKeyDerivationMode: SessionKeyDerivationModeType
    SessionKeyDerivationValue: SessionKeyDerivationValueTypeDef

class PinGenerationAttributesTypeDef(BaseValidatorModel):
    VisaPin: Optional[VisaPinTypeDef] = None
    VisaPinVerificationValue: Optional[VisaPinVerificationValueTypeDef] = None
    Ibm3624PinOffset: Optional[Ibm3624PinOffsetTypeDef] = None
    Ibm3624NaturalPin: Optional[Ibm3624NaturalPinTypeDef] = None
    Ibm3624RandomPin: Optional[Ibm3624RandomPinTypeDef] = None
    Ibm3624PinFromOffset: Optional[Ibm3624PinFromOffsetTypeDef] = None

class PinVerificationAttributesTypeDef(BaseValidatorModel):
    VisaPin: Optional[VisaPinVerificationTypeDef] = None
    Ibm3624Pin: Optional[Ibm3624PinVerificationTypeDef] = None

class SessionKeyDerivationTypeDef(BaseValidatorModel):
    EmvCommon: Optional[SessionKeyEmvCommonTypeDef] = None
    Mastercard: Optional[SessionKeyMastercardTypeDef] = None
    Emv2000: Optional[SessionKeyEmv2000TypeDef] = None
    Amex: Optional[SessionKeyAmexTypeDef] = None
    Visa: Optional[SessionKeyVisaTypeDef] = None

class TranslationIsoFormatsTypeDef(BaseValidatorModel):
    IsoFormat0: Optional[TranslationPinDataIsoFormat034TypeDef] = None
    IsoFormat1: Optional[Mapping[str, Any]] = None
    IsoFormat3: Optional[TranslationPinDataIsoFormat034TypeDef] = None
    IsoFormat4: Optional[TranslationPinDataIsoFormat034TypeDef] = None

class WrappedKeyTypeDef(BaseValidatorModel):
    WrappedKeyMaterial: WrappedKeyMaterialTypeDef
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None

class GenerateCardValidationDataInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str
    PrimaryAccountNumber: str
    GenerationAttributes: CardGenerationAttributesTypeDef
    ValidationDataLength: Optional[int] = None

class VerifyCardValidationDataInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str
    PrimaryAccountNumber: str
    VerificationAttributes: CardVerificationAttributesTypeDef
    ValidationData: str

class MacAttributesTypeDef(BaseValidatorModel):
    Algorithm: Optional[MacAlgorithmType] = None
    EmvMac: Optional[MacAlgorithmEmvTypeDef] = None
    DukptIso9797Algorithm1: Optional[MacAlgorithmDukptTypeDef] = None
    DukptIso9797Algorithm3: Optional[MacAlgorithmDukptTypeDef] = None
    DukptCmac: Optional[MacAlgorithmDukptTypeDef] = None

class GeneratePinDataInputRequestTypeDef(BaseValidatorModel):
    GenerationKeyIdentifier: str
    EncryptionKeyIdentifier: str
    GenerationAttributes: PinGenerationAttributesTypeDef
    PrimaryAccountNumber: str
    PinBlockFormat: PinBlockFormatForPinDataType
    PinDataLength: Optional[int] = None

class VerifyPinDataInputRequestTypeDef(BaseValidatorModel):
    VerificationKeyIdentifier: str
    EncryptionKeyIdentifier: str
    VerificationAttributes: PinVerificationAttributesTypeDef
    EncryptedPinBlock: str
    PrimaryAccountNumber: str
    PinBlockFormat: PinBlockFormatForPinDataType
    PinDataLength: Optional[int] = None
    DukptAttributes: Optional[DukptAttributesTypeDef] = None

class VerifyAuthRequestCryptogramInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str
    TransactionData: str
    AuthRequestCryptogram: str
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    SessionKeyDerivationAttributes: SessionKeyDerivationTypeDef
    AuthResponseAttributes: Optional[CryptogramAuthResponseTypeDef] = None

class DecryptDataInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str
    CipherText: str
    DecryptionAttributes: EncryptionDecryptionAttributesTypeDef
    WrappedKey: Optional[WrappedKeyTypeDef] = None

class EncryptDataInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str
    PlainText: str
    EncryptionAttributes: EncryptionDecryptionAttributesTypeDef
    WrappedKey: Optional[WrappedKeyTypeDef] = None

class ReEncryptDataInputRequestTypeDef(BaseValidatorModel):
    IncomingKeyIdentifier: str
    OutgoingKeyIdentifier: str
    CipherText: str
    IncomingEncryptionAttributes: ReEncryptionAttributesTypeDef
    OutgoingEncryptionAttributes: ReEncryptionAttributesTypeDef
    IncomingWrappedKey: Optional[WrappedKeyTypeDef] = None
    OutgoingWrappedKey: Optional[WrappedKeyTypeDef] = None

class TranslatePinDataInputRequestTypeDef(BaseValidatorModel):
    IncomingKeyIdentifier: str
    OutgoingKeyIdentifier: str
    IncomingTranslationAttributes: TranslationIsoFormatsTypeDef
    OutgoingTranslationAttributes: TranslationIsoFormatsTypeDef
    EncryptedPinBlock: str
    IncomingDukptAttributes: Optional[DukptDerivationAttributesTypeDef] = None
    OutgoingDukptAttributes: Optional[DukptDerivationAttributesTypeDef] = None
    IncomingWrappedKey: Optional[WrappedKeyTypeDef] = None
    OutgoingWrappedKey: Optional[WrappedKeyTypeDef] = None

class GenerateMacInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str
    MessageData: str
    GenerationAttributes: MacAttributesTypeDef
    MacLength: Optional[int] = None

class VerifyMacInputRequestTypeDef(BaseValidatorModel):
    KeyIdentifier: str
    MessageData: str
    Mac: str
    VerificationAttributes: MacAttributesTypeDef
    MacLength: Optional[int] = None


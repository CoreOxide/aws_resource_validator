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
from aws_resource_validator.pydantic_models.payment_cryptography_data_constants import *

class AmexCardSecurityCodeVersion1TypeDef(BaseModel):
    CardExpiryDate: str

class AmexCardSecurityCodeVersion2TypeDef(BaseModel):
    CardExpiryDate: str
    ServiceCode: str

class AsymmetricEncryptionAttributesTypeDef(BaseModel):
    PaddingType: Optional[PaddingTypeType] = None

class CardHolderVerificationValueTypeDef(BaseModel):
    UnpredictableNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class CardVerificationValue1TypeDef(BaseModel):
    CardExpiryDate: str
    ServiceCode: str

class CardVerificationValue2TypeDef(BaseModel):
    CardExpiryDate: str

class DynamicCardVerificationCodeTypeDef(BaseModel):
    UnpredictableNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    TrackData: str

class DynamicCardVerificationValueTypeDef(BaseModel):
    PanSequenceNumber: str
    CardExpiryDate: str
    ServiceCode: str
    ApplicationTransactionCounter: str

class DiscoverDynamicCardVerificationCodeTypeDef(BaseModel):
    CardExpiryDate: str
    UnpredictableNumber: str
    ApplicationTransactionCounter: str

class CryptogramVerificationArpcMethod1TypeDef(BaseModel):
    AuthResponseCode: str

class CryptogramVerificationArpcMethod2TypeDef(BaseModel):
    CardStatusUpdate: str
    ProprietaryAuthenticationData: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DukptAttributesTypeDef(BaseModel):
    KeySerialNumber: str
    DukptDerivationType: DukptDerivationTypeType

class DukptDerivationAttributesTypeDef(BaseModel):
    KeySerialNumber: str
    DukptKeyDerivationType: Optional[DukptDerivationTypeType] = None
    DukptKeyVariant: Optional[DukptKeyVariantType] = None

class DukptEncryptionAttributesTypeDef(BaseModel):
    KeySerialNumber: str
    Mode: Optional[DukptEncryptionModeType] = None
    DukptKeyDerivationType: Optional[DukptDerivationTypeType] = None
    DukptKeyVariant: Optional[DukptKeyVariantType] = None
    InitializationVector: Optional[str] = None

class EmvEncryptionAttributesTypeDef(BaseModel):
    MajorKeyDerivationMode: EmvMajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    SessionDerivationData: str
    Mode: Optional[EmvEncryptionModeType] = None
    InitializationVector: Optional[str] = None

class SymmetricEncryptionAttributesTypeDef(BaseModel):
    Mode: EncryptionModeType
    InitializationVector: Optional[str] = None
    PaddingType: Optional[PaddingTypeType] = None

class PinDataTypeDef(BaseModel):
    PinOffset: Optional[str] = None
    VerificationValue: Optional[str] = None

class Ibm3624NaturalPinTypeDef(BaseModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class Ibm3624PinFromOffsetTypeDef(BaseModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str
    PinOffset: str

class Ibm3624PinOffsetTypeDef(BaseModel):
    EncryptedPinBlock: str
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class Ibm3624PinVerificationTypeDef(BaseModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str
    PinOffset: str

class Ibm3624RandomPinTypeDef(BaseModel):
    DecimalizationTable: str
    PinValidationDataPadCharacter: str
    PinValidationData: str

class MacAlgorithmDukptTypeDef(BaseModel):
    KeySerialNumber: str
    DukptKeyVariant: DukptKeyVariantType
    DukptDerivationType: Optional[DukptDerivationTypeType] = None

class SessionKeyDerivationValueTypeDef(BaseModel):
    ApplicationCryptogram: Optional[str] = None
    ApplicationTransactionCounter: Optional[str] = None

class VisaPinTypeDef(BaseModel):
    PinVerificationKeyIndex: int

class VisaPinVerificationValueTypeDef(BaseModel):
    EncryptedPinBlock: str
    PinVerificationKeyIndex: int

class VisaPinVerificationTypeDef(BaseModel):
    PinVerificationKeyIndex: int
    VerificationValue: str

class SessionKeyAmexTypeDef(BaseModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str

class SessionKeyEmv2000TypeDef(BaseModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class SessionKeyEmvCommonTypeDef(BaseModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str

class SessionKeyMastercardTypeDef(BaseModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    ApplicationTransactionCounter: str
    UnpredictableNumber: str

class SessionKeyVisaTypeDef(BaseModel):
    PrimaryAccountNumber: str
    PanSequenceNumber: str

class TranslationPinDataIsoFormat034TypeDef(BaseModel):
    PrimaryAccountNumber: str

class WrappedKeyMaterialTypeDef(BaseModel):
    Tr31KeyBlock: Optional[str] = None

class CardGenerationAttributesTypeDef(BaseModel):
    AmexCardSecurityCodeVersion1: Optional[AmexCardSecurityCodeVersion1TypeDef] = None
    AmexCardSecurityCodeVersion2: Optional[AmexCardSecurityCodeVersion2TypeDef] = None
    CardVerificationValue1: Optional[CardVerificationValue1TypeDef] = None
    CardVerificationValue2: Optional[CardVerificationValue2TypeDef] = None
    CardHolderVerificationValue: Optional[CardHolderVerificationValueTypeDef] = None
    DynamicCardVerificationCode: Optional[DynamicCardVerificationCodeTypeDef] = None
    DynamicCardVerificationValue: Optional[DynamicCardVerificationValueTypeDef] = None

class CardVerificationAttributesTypeDef(BaseModel):
    AmexCardSecurityCodeVersion1: Optional[AmexCardSecurityCodeVersion1TypeDef] = None
    AmexCardSecurityCodeVersion2: Optional[AmexCardSecurityCodeVersion2TypeDef] = None
    CardVerificationValue1: Optional[CardVerificationValue1TypeDef] = None
    CardVerificationValue2: Optional[CardVerificationValue2TypeDef] = None
    CardHolderVerificationValue: Optional[CardHolderVerificationValueTypeDef] = None
    DynamicCardVerificationCode: Optional[DynamicCardVerificationCodeTypeDef] = None
    DynamicCardVerificationValue: Optional[DynamicCardVerificationValueTypeDef] = None
    DiscoverDynamicCardVerificationCode: Optional[       DiscoverDynamicCardVerificationCodeTypeDef     ] = None

class CryptogramAuthResponseTypeDef(BaseModel):
    ArpcMethod1: Optional[CryptogramVerificationArpcMethod1TypeDef] = None
    ArpcMethod2: Optional[CryptogramVerificationArpcMethod2TypeDef] = None

class DecryptDataOutputTypeDef(BaseModel):
    KeyArn: str
    KeyCheckValue: str
    PlainText: str
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptDataOutputTypeDef(BaseModel):
    KeyArn: str
    KeyCheckValue: str
    CipherText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateCardValidationDataOutputTypeDef(BaseModel):
    KeyArn: str
    KeyCheckValue: str
    ValidationData: str
    ResponseMetadata: ResponseMetadataTypeDef

class GenerateMacOutputTypeDef(BaseModel):
    KeyArn: str
    KeyCheckValue: str
    Mac: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReEncryptDataOutputTypeDef(BaseModel):
    KeyArn: str
    KeyCheckValue: str
    CipherText: str
    ResponseMetadata: ResponseMetadataTypeDef

class TranslatePinDataOutputTypeDef(BaseModel):
    PinBlock: str
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyAuthRequestCryptogramOutputTypeDef(BaseModel):
    KeyArn: str
    KeyCheckValue: str
    AuthResponseValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyCardValidationDataOutputTypeDef(BaseModel):
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyMacOutputTypeDef(BaseModel):
    KeyArn: str
    KeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyPinDataOutputTypeDef(BaseModel):
    VerificationKeyArn: str
    VerificationKeyCheckValue: str
    EncryptionKeyArn: str
    EncryptionKeyCheckValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class EncryptionDecryptionAttributesTypeDef(BaseModel):
    Symmetric: Optional[SymmetricEncryptionAttributesTypeDef] = None
    Asymmetric: Optional[AsymmetricEncryptionAttributesTypeDef] = None
    Dukpt: Optional[DukptEncryptionAttributesTypeDef] = None
    Emv: Optional[EmvEncryptionAttributesTypeDef] = None

class ReEncryptionAttributesTypeDef(BaseModel):
    Symmetric: Optional[SymmetricEncryptionAttributesTypeDef] = None
    Dukpt: Optional[DukptEncryptionAttributesTypeDef] = None

class GeneratePinDataOutputTypeDef(BaseModel):
    GenerationKeyArn: str
    GenerationKeyCheckValue: str
    EncryptionKeyArn: str
    EncryptionKeyCheckValue: str
    EncryptedPinBlock: str
    PinData: PinDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MacAlgorithmEmvTypeDef(BaseModel):
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    PrimaryAccountNumber: str
    PanSequenceNumber: str
    SessionKeyDerivationMode: SessionKeyDerivationModeType
    SessionKeyDerivationValue: SessionKeyDerivationValueTypeDef

class PinGenerationAttributesTypeDef(BaseModel):
    VisaPin: Optional[VisaPinTypeDef] = None
    VisaPinVerificationValue: Optional[VisaPinVerificationValueTypeDef] = None
    Ibm3624PinOffset: Optional[Ibm3624PinOffsetTypeDef] = None
    Ibm3624NaturalPin: Optional[Ibm3624NaturalPinTypeDef] = None
    Ibm3624RandomPin: Optional[Ibm3624RandomPinTypeDef] = None
    Ibm3624PinFromOffset: Optional[Ibm3624PinFromOffsetTypeDef] = None

class PinVerificationAttributesTypeDef(BaseModel):
    VisaPin: Optional[VisaPinVerificationTypeDef] = None
    Ibm3624Pin: Optional[Ibm3624PinVerificationTypeDef] = None

class SessionKeyDerivationTypeDef(BaseModel):
    EmvCommon: Optional[SessionKeyEmvCommonTypeDef] = None
    Mastercard: Optional[SessionKeyMastercardTypeDef] = None
    Emv2000: Optional[SessionKeyEmv2000TypeDef] = None
    Amex: Optional[SessionKeyAmexTypeDef] = None
    Visa: Optional[SessionKeyVisaTypeDef] = None

class TranslationIsoFormatsTypeDef(BaseModel):
    IsoFormat0: Optional[TranslationPinDataIsoFormat034TypeDef] = None
    IsoFormat1: Optional[Mapping[str, Any]] = None
    IsoFormat3: Optional[TranslationPinDataIsoFormat034TypeDef] = None
    IsoFormat4: Optional[TranslationPinDataIsoFormat034TypeDef] = None

class WrappedKeyTypeDef(BaseModel):
    WrappedKeyMaterial: WrappedKeyMaterialTypeDef
    KeyCheckValueAlgorithm: Optional[KeyCheckValueAlgorithmType] = None

class GenerateCardValidationDataInputRequestTypeDef(BaseModel):
    KeyIdentifier: str
    PrimaryAccountNumber: str
    GenerationAttributes: CardGenerationAttributesTypeDef
    ValidationDataLength: Optional[int] = None

class VerifyCardValidationDataInputRequestTypeDef(BaseModel):
    KeyIdentifier: str
    PrimaryAccountNumber: str
    VerificationAttributes: CardVerificationAttributesTypeDef
    ValidationData: str

class MacAttributesTypeDef(BaseModel):
    Algorithm: Optional[MacAlgorithmType] = None
    EmvMac: Optional[MacAlgorithmEmvTypeDef] = None
    DukptIso9797Algorithm1: Optional[MacAlgorithmDukptTypeDef] = None
    DukptIso9797Algorithm3: Optional[MacAlgorithmDukptTypeDef] = None
    DukptCmac: Optional[MacAlgorithmDukptTypeDef] = None

class GeneratePinDataInputRequestTypeDef(BaseModel):
    GenerationKeyIdentifier: str
    EncryptionKeyIdentifier: str
    GenerationAttributes: PinGenerationAttributesTypeDef
    PrimaryAccountNumber: str
    PinBlockFormat: PinBlockFormatForPinDataType
    PinDataLength: Optional[int] = None

class VerifyPinDataInputRequestTypeDef(BaseModel):
    VerificationKeyIdentifier: str
    EncryptionKeyIdentifier: str
    VerificationAttributes: PinVerificationAttributesTypeDef
    EncryptedPinBlock: str
    PrimaryAccountNumber: str
    PinBlockFormat: PinBlockFormatForPinDataType
    PinDataLength: Optional[int] = None
    DukptAttributes: Optional[DukptAttributesTypeDef] = None

class VerifyAuthRequestCryptogramInputRequestTypeDef(BaseModel):
    KeyIdentifier: str
    TransactionData: str
    AuthRequestCryptogram: str
    MajorKeyDerivationMode: MajorKeyDerivationModeType
    SessionKeyDerivationAttributes: SessionKeyDerivationTypeDef
    AuthResponseAttributes: Optional[CryptogramAuthResponseTypeDef] = None

class DecryptDataInputRequestTypeDef(BaseModel):
    KeyIdentifier: str
    CipherText: str
    DecryptionAttributes: EncryptionDecryptionAttributesTypeDef
    WrappedKey: Optional[WrappedKeyTypeDef] = None

class EncryptDataInputRequestTypeDef(BaseModel):
    KeyIdentifier: str
    PlainText: str
    EncryptionAttributes: EncryptionDecryptionAttributesTypeDef
    WrappedKey: Optional[WrappedKeyTypeDef] = None

class ReEncryptDataInputRequestTypeDef(BaseModel):
    IncomingKeyIdentifier: str
    OutgoingKeyIdentifier: str
    CipherText: str
    IncomingEncryptionAttributes: ReEncryptionAttributesTypeDef
    OutgoingEncryptionAttributes: ReEncryptionAttributesTypeDef
    IncomingWrappedKey: Optional[WrappedKeyTypeDef] = None
    OutgoingWrappedKey: Optional[WrappedKeyTypeDef] = None

class TranslatePinDataInputRequestTypeDef(BaseModel):
    IncomingKeyIdentifier: str
    OutgoingKeyIdentifier: str
    IncomingTranslationAttributes: TranslationIsoFormatsTypeDef
    OutgoingTranslationAttributes: TranslationIsoFormatsTypeDef
    EncryptedPinBlock: str
    IncomingDukptAttributes: Optional[DukptDerivationAttributesTypeDef] = None
    OutgoingDukptAttributes: Optional[DukptDerivationAttributesTypeDef] = None
    IncomingWrappedKey: Optional[WrappedKeyTypeDef] = None
    OutgoingWrappedKey: Optional[WrappedKeyTypeDef] = None

class GenerateMacInputRequestTypeDef(BaseModel):
    KeyIdentifier: str
    MessageData: str
    GenerationAttributes: MacAttributesTypeDef
    MacLength: Optional[int] = None

class VerifyMacInputRequestTypeDef(BaseModel):
    KeyIdentifier: str
    MessageData: str
    Mac: str
    VerificationAttributes: MacAttributesTypeDef
    MacLength: Optional[int] = None


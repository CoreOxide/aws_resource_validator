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
from aws_resource_validator.pydantic_models.taxsettings_constants import *

class TaxInheritanceDetailsTypeDef(BaseValidatorModel):
    inheritanceObtainedReason: Optional[str] = None
    parentEntityId: Optional[str] = None

class AddressTypeDef(BaseValidatorModel):
    addressLine1: str
    city: str
    countryCode: str
    postalCode: str
    addressLine2: Optional[str] = None
    addressLine3: Optional[str] = None
    districtOrCounty: Optional[str] = None
    stateOrRegion: Optional[str] = None

class JurisdictionTypeDef(BaseValidatorModel):
    countryCode: str
    stateOrRegion: Optional[str] = None

class CanadaAdditionalInfoTypeDef(BaseValidatorModel):
    canadaQuebecSalesTaxNumber: Optional[str] = None
    canadaRetailSalesTaxNumber: Optional[str] = None
    isResellerAccount: Optional[bool] = None
    provincialSalesTaxId: Optional[str] = None

class EstoniaAdditionalInfoTypeDef(BaseValidatorModel):
    registryCommercialCode: str

class GeorgiaAdditionalInfoTypeDef(BaseValidatorModel):
    personType: PersonTypeType

class IsraelAdditionalInfoTypeDef(BaseValidatorModel):
    customerType: IsraelCustomerTypeType
    dealerType: IsraelDealerTypeType

class ItalyAdditionalInfoTypeDef(BaseValidatorModel):
    cigNumber: Optional[str] = None
    cupNumber: Optional[str] = None
    sdiAccountId: Optional[str] = None
    taxCode: Optional[str] = None

class KenyaAdditionalInfoTypeDef(BaseValidatorModel):
    personType: PersonTypeType

class MalaysiaAdditionalInfoTypeDef(BaseValidatorModel):
    serviceTaxCodes: Sequence[MalaysiaServiceTaxCodeType]

class PolandAdditionalInfoTypeDef(BaseValidatorModel):
    individualRegistrationNumber: Optional[str] = None
    isGroupVatEnabled: Optional[bool] = None

class RomaniaAdditionalInfoTypeDef(BaseValidatorModel):
    taxRegistrationNumberType: TaxRegistrationNumberTypeType

class SaudiArabiaAdditionalInfoTypeDef(BaseValidatorModel):
    taxRegistrationNumberType: Optional[SaudiArabiaTaxRegistrationNumberTypeType] = None

class SouthKoreaAdditionalInfoTypeDef(BaseValidatorModel):
    businessRepresentativeName: str
    itemOfBusiness: str
    lineOfBusiness: str

class SpainAdditionalInfoTypeDef(BaseValidatorModel):
    registrationType: RegistrationTypeType

class TurkeyAdditionalInfoTypeDef(BaseValidatorModel):
    industries: Optional[IndustriesType] = None
    kepEmailId: Optional[str] = None
    secondaryTaxId: Optional[str] = None
    taxOffice: Optional[str] = None

class UkraineAdditionalInfoTypeDef(BaseValidatorModel):
    ukraineTrnType: UkraineTrnTypeType

class BrazilAdditionalInfoTypeDef(BaseValidatorModel):
    ccmCode: Optional[str] = None
    legalNatureCode: Optional[str] = None

class IndiaAdditionalInfoTypeDef(BaseValidatorModel):
    pan: Optional[str] = None

class MalaysiaAdditionalInfoOutputTypeDef(BaseValidatorModel):
    serviceTaxCodes: List[MalaysiaServiceTaxCodeType]

class BatchDeleteTaxRegistrationErrorTypeDef(BaseValidatorModel):
    accountId: str
    message: str
    code: Optional[str] = None

class BatchDeleteTaxRegistrationRequestRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchPutTaxRegistrationErrorTypeDef(BaseValidatorModel):
    accountId: str
    message: str
    code: Optional[str] = None

class DeleteTaxRegistrationRequestRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class DestinationS3LocationTypeDef(BaseValidatorModel):
    bucket: str
    prefix: Optional[str] = None

class TaxDocumentMetadataTypeDef(BaseValidatorModel):
    taxDocumentAccessToken: str
    taxDocumentName: str

class GetTaxRegistrationRequestRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTaxRegistrationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SourceS3LocationTypeDef(BaseValidatorModel):
    bucket: str
    key: str

class AccountMetaDataTypeDef(BaseValidatorModel):
    accountName: Optional[str] = None
    address: Optional[AddressTypeDef] = None
    addressRoleMap: Optional[Dict[AddressRoleTypeType, JurisdictionTypeDef]] = None
    addressType: Optional[AddressRoleTypeType] = None
    seller: Optional[str] = None

class AdditionalInfoRequestTypeDef(BaseValidatorModel):
    canadaAdditionalInfo: Optional[CanadaAdditionalInfoTypeDef] = None
    estoniaAdditionalInfo: Optional[EstoniaAdditionalInfoTypeDef] = None
    georgiaAdditionalInfo: Optional[GeorgiaAdditionalInfoTypeDef] = None
    israelAdditionalInfo: Optional[IsraelAdditionalInfoTypeDef] = None
    italyAdditionalInfo: Optional[ItalyAdditionalInfoTypeDef] = None
    kenyaAdditionalInfo: Optional[KenyaAdditionalInfoTypeDef] = None
    malaysiaAdditionalInfo: Optional[MalaysiaAdditionalInfoTypeDef] = None
    polandAdditionalInfo: Optional[PolandAdditionalInfoTypeDef] = None
    romaniaAdditionalInfo: Optional[RomaniaAdditionalInfoTypeDef] = None
    saudiArabiaAdditionalInfo: Optional[SaudiArabiaAdditionalInfoTypeDef] = None
    southKoreaAdditionalInfo: Optional[SouthKoreaAdditionalInfoTypeDef] = None
    spainAdditionalInfo: Optional[SpainAdditionalInfoTypeDef] = None
    turkeyAdditionalInfo: Optional[TurkeyAdditionalInfoTypeDef] = None
    ukraineAdditionalInfo: Optional[UkraineAdditionalInfoTypeDef] = None

class AdditionalInfoResponseTypeDef(BaseValidatorModel):
    brazilAdditionalInfo: Optional[BrazilAdditionalInfoTypeDef] = None
    canadaAdditionalInfo: Optional[CanadaAdditionalInfoTypeDef] = None
    estoniaAdditionalInfo: Optional[EstoniaAdditionalInfoTypeDef] = None
    georgiaAdditionalInfo: Optional[GeorgiaAdditionalInfoTypeDef] = None
    indiaAdditionalInfo: Optional[IndiaAdditionalInfoTypeDef] = None
    israelAdditionalInfo: Optional[IsraelAdditionalInfoTypeDef] = None
    italyAdditionalInfo: Optional[ItalyAdditionalInfoTypeDef] = None
    kenyaAdditionalInfo: Optional[KenyaAdditionalInfoTypeDef] = None
    malaysiaAdditionalInfo: Optional[MalaysiaAdditionalInfoOutputTypeDef] = None
    polandAdditionalInfo: Optional[PolandAdditionalInfoTypeDef] = None
    romaniaAdditionalInfo: Optional[RomaniaAdditionalInfoTypeDef] = None
    saudiArabiaAdditionalInfo: Optional[SaudiArabiaAdditionalInfoTypeDef] = None
    southKoreaAdditionalInfo: Optional[SouthKoreaAdditionalInfoTypeDef] = None
    spainAdditionalInfo: Optional[SpainAdditionalInfoTypeDef] = None
    turkeyAdditionalInfo: Optional[TurkeyAdditionalInfoTypeDef] = None
    ukraineAdditionalInfo: Optional[UkraineAdditionalInfoTypeDef] = None

class BatchDeleteTaxRegistrationResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteTaxRegistrationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaxRegistrationDocumentResponseTypeDef(BaseValidatorModel):
    destinationFilePath: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutTaxRegistrationResponseTypeDef(BaseValidatorModel):
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutTaxRegistrationResponseTypeDef(BaseValidatorModel):
    errors: List[BatchPutTaxRegistrationErrorTypeDef]
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaxRegistrationDocumentRequestRequestTypeDef(BaseValidatorModel):
    destinationS3Location: DestinationS3LocationTypeDef
    taxDocumentMetadata: TaxDocumentMetadataTypeDef

class ListTaxRegistrationsRequestListTaxRegistrationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class TaxRegistrationDocumentTypeDef(BaseValidatorModel):
    s3Location: SourceS3LocationTypeDef

class TaxRegistrationTypeDef(BaseValidatorModel):
    legalAddress: AddressTypeDef
    legalName: str
    registrationId: str
    registrationType: TaxRegistrationTypeType
    status: TaxRegistrationStatusType
    additionalTaxInformation: Optional[AdditionalInfoResponseTypeDef] = None
    certifiedEmailId: Optional[str] = None
    sector: Optional[SectorType] = None
    taxDocumentMetadatas: Optional[List[TaxDocumentMetadataTypeDef]] = None

class TaxRegistrationWithJurisdictionTypeDef(BaseValidatorModel):
    jurisdiction: JurisdictionTypeDef
    legalName: str
    registrationId: str
    registrationType: TaxRegistrationTypeType
    status: TaxRegistrationStatusType
    additionalTaxInformation: Optional[AdditionalInfoResponseTypeDef] = None
    certifiedEmailId: Optional[str] = None
    sector: Optional[SectorType] = None
    taxDocumentMetadatas: Optional[List[TaxDocumentMetadataTypeDef]] = None

class VerificationDetailsTypeDef(BaseValidatorModel):
    dateOfBirth: Optional[str] = None
    taxRegistrationDocuments: Optional[Sequence[TaxRegistrationDocumentTypeDef]] = None

class GetTaxRegistrationResponseTypeDef(BaseValidatorModel):
    taxRegistration: TaxRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccountDetailsTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    accountMetaData: Optional[AccountMetaDataTypeDef] = None
    taxInheritanceDetails: Optional[TaxInheritanceDetailsTypeDef] = None
    taxRegistration: Optional[TaxRegistrationWithJurisdictionTypeDef] = None

class TaxRegistrationEntryTypeDef(BaseValidatorModel):
    registrationId: str
    registrationType: TaxRegistrationTypeType
    additionalTaxInformation: Optional[AdditionalInfoRequestTypeDef] = None
    certifiedEmailId: Optional[str] = None
    legalAddress: Optional[AddressTypeDef] = None
    legalName: Optional[str] = None
    sector: Optional[SectorType] = None
    verificationDetails: Optional[VerificationDetailsTypeDef] = None

class ListTaxRegistrationsResponseTypeDef(BaseValidatorModel):
    accountDetails: List[AccountDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutTaxRegistrationRequestRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]
    taxRegistrationEntry: TaxRegistrationEntryTypeDef

class PutTaxRegistrationRequestRequestTypeDef(BaseValidatorModel):
    taxRegistrationEntry: TaxRegistrationEntryTypeDef
    accountId: Optional[str] = None


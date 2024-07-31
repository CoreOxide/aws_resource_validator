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
from aws_resource_validator.pydantic_models.taxsettings_constants import *

class TaxInheritanceDetailsTypeDef(BaseModel):
    inheritanceObtainedReason: Optional[str] = None
    parentEntityId: Optional[str] = None

class AddressTypeDef(BaseModel):
    addressLine1: str
    city: str
    countryCode: str
    postalCode: str
    addressLine2: Optional[str] = None
    addressLine3: Optional[str] = None
    districtOrCounty: Optional[str] = None
    stateOrRegion: Optional[str] = None

class JurisdictionTypeDef(BaseModel):
    countryCode: str
    stateOrRegion: Optional[str] = None

class CanadaAdditionalInfoTypeDef(BaseModel):
    canadaQuebecSalesTaxNumber: Optional[str] = None
    canadaRetailSalesTaxNumber: Optional[str] = None
    isResellerAccount: Optional[bool] = None
    provincialSalesTaxId: Optional[str] = None

class EstoniaAdditionalInfoTypeDef(BaseModel):
    registryCommercialCode: str

class GeorgiaAdditionalInfoTypeDef(BaseModel):
    personType: PersonTypeType

class IsraelAdditionalInfoTypeDef(BaseModel):
    customerType: IsraelCustomerTypeType
    dealerType: IsraelDealerTypeType

class ItalyAdditionalInfoTypeDef(BaseModel):
    cigNumber: Optional[str] = None
    cupNumber: Optional[str] = None
    sdiAccountId: Optional[str] = None
    taxCode: Optional[str] = None

class KenyaAdditionalInfoTypeDef(BaseModel):
    personType: PersonTypeType

class MalaysiaAdditionalInfoTypeDef(BaseModel):
    serviceTaxCodes: Sequence[MalaysiaServiceTaxCodeType]

class PolandAdditionalInfoTypeDef(BaseModel):
    individualRegistrationNumber: Optional[str] = None
    isGroupVatEnabled: Optional[bool] = None

class RomaniaAdditionalInfoTypeDef(BaseModel):
    taxRegistrationNumberType: TaxRegistrationNumberTypeType

class SaudiArabiaAdditionalInfoTypeDef(BaseModel):
    taxRegistrationNumberType: Optional[SaudiArabiaTaxRegistrationNumberTypeType] = None

class SouthKoreaAdditionalInfoTypeDef(BaseModel):
    businessRepresentativeName: str
    itemOfBusiness: str
    lineOfBusiness: str

class SpainAdditionalInfoTypeDef(BaseModel):
    registrationType: RegistrationTypeType

class TurkeyAdditionalInfoTypeDef(BaseModel):
    industries: Optional[IndustriesType] = None
    kepEmailId: Optional[str] = None
    secondaryTaxId: Optional[str] = None
    taxOffice: Optional[str] = None

class UkraineAdditionalInfoTypeDef(BaseModel):
    ukraineTrnType: UkraineTrnTypeType

class BrazilAdditionalInfoTypeDef(BaseModel):
    ccmCode: Optional[str] = None
    legalNatureCode: Optional[str] = None

class IndiaAdditionalInfoTypeDef(BaseModel):
    pan: Optional[str] = None

class MalaysiaAdditionalInfoOutputTypeDef(BaseModel):
    serviceTaxCodes: List[MalaysiaServiceTaxCodeType]

class BatchDeleteTaxRegistrationErrorTypeDef(BaseModel):
    accountId: str
    message: str
    code: Optional[str] = None

class BatchDeleteTaxRegistrationRequestRequestTypeDef(BaseModel):
    accountIds: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchPutTaxRegistrationErrorTypeDef(BaseModel):
    accountId: str
    message: str
    code: Optional[str] = None

class DeleteTaxRegistrationRequestRequestTypeDef(BaseModel):
    accountId: Optional[str] = None

class DestinationS3LocationTypeDef(BaseModel):
    bucket: str
    prefix: Optional[str] = None

class TaxDocumentMetadataTypeDef(BaseModel):
    taxDocumentAccessToken: str
    taxDocumentName: str

class GetTaxRegistrationRequestRequestTypeDef(BaseModel):
    accountId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListTaxRegistrationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SourceS3LocationTypeDef(BaseModel):
    bucket: str
    key: str

class AccountMetaDataTypeDef(BaseModel):
    accountName: Optional[str] = None
    address: Optional[AddressTypeDef] = None
    addressRoleMap: Optional[Dict[AddressRoleTypeType, JurisdictionTypeDef]] = None
    addressType: Optional[AddressRoleTypeType] = None
    seller: Optional[str] = None

class AdditionalInfoRequestTypeDef(BaseModel):
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

class AdditionalInfoResponseTypeDef(BaseModel):
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

class BatchDeleteTaxRegistrationResponseTypeDef(BaseModel):
    errors: List[BatchDeleteTaxRegistrationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaxRegistrationDocumentResponseTypeDef(BaseModel):
    destinationFilePath: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutTaxRegistrationResponseTypeDef(BaseModel):
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutTaxRegistrationResponseTypeDef(BaseModel):
    errors: List[BatchPutTaxRegistrationErrorTypeDef]
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetTaxRegistrationDocumentRequestRequestTypeDef(BaseModel):
    destinationS3Location: DestinationS3LocationTypeDef
    taxDocumentMetadata: TaxDocumentMetadataTypeDef

class ListTaxRegistrationsRequestListTaxRegistrationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class TaxRegistrationDocumentTypeDef(BaseModel):
    s3Location: SourceS3LocationTypeDef

class TaxRegistrationTypeDef(BaseModel):
    legalAddress: AddressTypeDef
    legalName: str
    registrationId: str
    registrationType: TaxRegistrationTypeType
    status: TaxRegistrationStatusType
    additionalTaxInformation: Optional[AdditionalInfoResponseTypeDef] = None
    certifiedEmailId: Optional[str] = None
    sector: Optional[SectorType] = None
    taxDocumentMetadatas: Optional[List[TaxDocumentMetadataTypeDef]] = None

class TaxRegistrationWithJurisdictionTypeDef(BaseModel):
    jurisdiction: JurisdictionTypeDef
    legalName: str
    registrationId: str
    registrationType: TaxRegistrationTypeType
    status: TaxRegistrationStatusType
    additionalTaxInformation: Optional[AdditionalInfoResponseTypeDef] = None
    certifiedEmailId: Optional[str] = None
    sector: Optional[SectorType] = None
    taxDocumentMetadatas: Optional[List[TaxDocumentMetadataTypeDef]] = None

class VerificationDetailsTypeDef(BaseModel):
    dateOfBirth: Optional[str] = None
    taxRegistrationDocuments: Optional[Sequence[TaxRegistrationDocumentTypeDef]] = None

class GetTaxRegistrationResponseTypeDef(BaseModel):
    taxRegistration: TaxRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccountDetailsTypeDef(BaseModel):
    accountId: Optional[str] = None
    accountMetaData: Optional[AccountMetaDataTypeDef] = None
    taxInheritanceDetails: Optional[TaxInheritanceDetailsTypeDef] = None
    taxRegistration: Optional[TaxRegistrationWithJurisdictionTypeDef] = None

class TaxRegistrationEntryTypeDef(BaseModel):
    registrationId: str
    registrationType: TaxRegistrationTypeType
    additionalTaxInformation: Optional[AdditionalInfoRequestTypeDef] = None
    certifiedEmailId: Optional[str] = None
    legalAddress: Optional[AddressTypeDef] = None
    legalName: Optional[str] = None
    sector: Optional[SectorType] = None
    verificationDetails: Optional[VerificationDetailsTypeDef] = None

class ListTaxRegistrationsResponseTypeDef(BaseModel):
    accountDetails: List[AccountDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutTaxRegistrationRequestRequestTypeDef(BaseModel):
    accountIds: Sequence[str]
    taxRegistrationEntry: TaxRegistrationEntryTypeDef

class PutTaxRegistrationRequestRequestTypeDef(BaseModel):
    taxRegistrationEntry: TaxRegistrationEntryTypeDef
    accountId: Optional[str] = None


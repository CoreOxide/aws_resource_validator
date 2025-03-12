from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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


class EgyptAdditionalInfoTypeDef(BaseValidatorModel):
    uniqueIdentificationNumber: Optional[str] = None
    uniqueIdentificationNumberExpirationDate: Optional[str] = None


class EstoniaAdditionalInfoTypeDef(BaseValidatorModel):
    registryCommercialCode: str


class GeorgiaAdditionalInfoTypeDef(BaseValidatorModel):
    personType: PersonTypeType


class GreeceAdditionalInfoTypeDef(BaseValidatorModel):
    contractingAuthorityCode: Optional[str] = None


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


class VietnamAdditionalInfoTypeDef(BaseValidatorModel):
    electronicTransactionCodeNumber: Optional[str] = None
    enterpriseIdentificationNumber: Optional[str] = None
    paymentVoucherNumber: Optional[str] = None
    paymentVoucherNumberDate: Optional[str] = None


class BrazilAdditionalInfoTypeDef(BaseValidatorModel):
    ccmCode: Optional[str] = None
    legalNatureCode: Optional[str] = None


class IndiaAdditionalInfoTypeDef(BaseValidatorModel):
    pan: Optional[str] = None


class MalaysiaAdditionalInfoOutputTypeDef(BaseValidatorModel):
    businessRegistrationNumber: Optional[str] = None
    serviceTaxCodes: Optional[List[MalaysiaServiceTaxCodeType]] = None
    taxInformationNumber: Optional[str] = None


class AuthorityTypeDef(BaseValidatorModel):
    country: str
    state: Optional[str] = None


class BatchDeleteTaxRegistrationErrorTypeDef(BaseValidatorModel):
    accountId: str
    message: str
    code: Optional[str] = None


class BatchDeleteTaxRegistrationRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetTaxExemptionsRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]


class BatchPutTaxRegistrationErrorTypeDef(BaseValidatorModel):
    accountId: str
    message: str
    code: Optional[str] = None


class DeleteSupplementalTaxRegistrationRequestTypeDef(BaseValidatorModel):
    authorityId: str


class DeleteTaxRegistrationRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None


class DestinationS3LocationTypeDef(BaseValidatorModel):
    bucket: str
    prefix: Optional[str] = None


class TaxDocumentMetadataTypeDef(BaseValidatorModel):
    taxDocumentAccessToken: str
    taxDocumentName: str


class GetTaxRegistrationRequestTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSupplementalTaxRegistrationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTaxExemptionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTaxRegistrationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MalaysiaAdditionalInfoTypeDef(BaseValidatorModel):
    businessRegistrationNumber: Optional[str] = None
    serviceTaxCodes: Optional[Sequence[MalaysiaServiceTaxCodeType]] = None
    taxInformationNumber: Optional[str] = None


class PutTaxInheritanceRequestTypeDef(BaseValidatorModel):
    heritageStatus: Optional[HeritageStatusType] = None


class SourceS3LocationTypeDef(BaseValidatorModel):
    bucket: str
    key: str


class SupplementalTaxRegistrationEntryTypeDef(BaseValidatorModel):
    address: AddressTypeDef
    legalName: str
    registrationId: str
    registrationType: Literal["VAT"]


class SupplementalTaxRegistrationTypeDef(BaseValidatorModel):
    address: AddressTypeDef
    authorityId: str
    legalName: str
    registrationId: str
    registrationType: Literal["VAT"]
    status: TaxRegistrationStatusType


class AccountMetaDataTypeDef(BaseValidatorModel):
    accountName: Optional[str] = None
    address: Optional[AddressTypeDef] = None
    addressRoleMap: Optional[Dict[AddressRoleTypeType, JurisdictionTypeDef]] = None
    addressType: Optional[AddressRoleTypeType] = None
    seller: Optional[str] = None


class AdditionalInfoResponseTypeDef(BaseValidatorModel):
    brazilAdditionalInfo: Optional[BrazilAdditionalInfoTypeDef] = None
    canadaAdditionalInfo: Optional[CanadaAdditionalInfoTypeDef] = None
    egyptAdditionalInfo: Optional[EgyptAdditionalInfoTypeDef] = None
    estoniaAdditionalInfo: Optional[EstoniaAdditionalInfoTypeDef] = None
    georgiaAdditionalInfo: Optional[GeorgiaAdditionalInfoTypeDef] = None
    greeceAdditionalInfo: Optional[GreeceAdditionalInfoTypeDef] = None
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
    vietnamAdditionalInfo: Optional[VietnamAdditionalInfoTypeDef] = None


class TaxExemptionTypeTypeDef(BaseValidatorModel):
    applicableJurisdictions: Optional[List[AuthorityTypeDef]] = None
    description: Optional[str] = None
    displayName: Optional[str] = None


class BatchDeleteTaxRegistrationResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteTaxRegistrationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetTaxInheritanceResponseTypeDef(BaseValidatorModel):
    heritageStatus: HeritageStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetTaxRegistrationDocumentResponseTypeDef(BaseValidatorModel):
    destinationFilePath: str
    presignedS3Url: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutSupplementalTaxRegistrationResponseTypeDef(BaseValidatorModel):
    authorityId: str
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class PutTaxExemptionResponseTypeDef(BaseValidatorModel):
    caseId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutTaxRegistrationResponseTypeDef(BaseValidatorModel):
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class BatchPutTaxRegistrationResponseTypeDef(BaseValidatorModel):
    errors: List[BatchPutTaxRegistrationErrorTypeDef]
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class ExemptionCertificateTypeDef(BaseValidatorModel):
    documentFile: BlobTypeDef
    documentName: str


class TaxRegistrationDocFileTypeDef(BaseValidatorModel):
    fileContent: BlobTypeDef
    fileName: str


class GetTaxRegistrationDocumentRequestTypeDef(BaseValidatorModel):
    taxDocumentMetadata: TaxDocumentMetadataTypeDef
    destinationS3Location: Optional[DestinationS3LocationTypeDef] = None


class ListSupplementalTaxRegistrationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTaxExemptionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTaxRegistrationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PutSupplementalTaxRegistrationRequestTypeDef(BaseValidatorModel):
    taxRegistrationEntry: SupplementalTaxRegistrationEntryTypeDef


class ListSupplementalTaxRegistrationsResponseTypeDef(BaseValidatorModel):
    taxRegistrations: List[SupplementalTaxRegistrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class GetTaxExemptionTypesResponseTypeDef(BaseValidatorModel):
    taxExemptionTypes: List[TaxExemptionTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TaxExemptionTypeDef(BaseValidatorModel):
    authority: AuthorityTypeDef
    taxExemptionType: TaxExemptionTypeTypeDef
    effectiveDate: Optional[datetime] = None
    expirationDate: Optional[datetime] = None
    status: Optional[EntityExemptionAccountStatusType] = None
    systemEffectiveDate: Optional[datetime] = None


class PutTaxExemptionRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]
    authority: AuthorityTypeDef
    exemptionCertificate: ExemptionCertificateTypeDef
    exemptionType: str


class TaxRegistrationDocumentTypeDef(BaseValidatorModel):
    file: Optional[TaxRegistrationDocFileTypeDef] = None
    s3Location: Optional[SourceS3LocationTypeDef] = None


class MalaysiaAdditionalInfoUnionTypeDef(BaseValidatorModel):
    pass


class AdditionalInfoRequestTypeDef(BaseValidatorModel):
    canadaAdditionalInfo: Optional[CanadaAdditionalInfoTypeDef] = None
    egyptAdditionalInfo: Optional[EgyptAdditionalInfoTypeDef] = None
    estoniaAdditionalInfo: Optional[EstoniaAdditionalInfoTypeDef] = None
    georgiaAdditionalInfo: Optional[GeorgiaAdditionalInfoTypeDef] = None
    greeceAdditionalInfo: Optional[GreeceAdditionalInfoTypeDef] = None
    israelAdditionalInfo: Optional[IsraelAdditionalInfoTypeDef] = None
    italyAdditionalInfo: Optional[ItalyAdditionalInfoTypeDef] = None
    kenyaAdditionalInfo: Optional[KenyaAdditionalInfoTypeDef] = None
    malaysiaAdditionalInfo: Optional[MalaysiaAdditionalInfoUnionTypeDef] = None
    polandAdditionalInfo: Optional[PolandAdditionalInfoTypeDef] = None
    romaniaAdditionalInfo: Optional[RomaniaAdditionalInfoTypeDef] = None
    saudiArabiaAdditionalInfo: Optional[SaudiArabiaAdditionalInfoTypeDef] = None
    southKoreaAdditionalInfo: Optional[SouthKoreaAdditionalInfoTypeDef] = None
    spainAdditionalInfo: Optional[SpainAdditionalInfoTypeDef] = None
    turkeyAdditionalInfo: Optional[TurkeyAdditionalInfoTypeDef] = None
    ukraineAdditionalInfo: Optional[UkraineAdditionalInfoTypeDef] = None
    vietnamAdditionalInfo: Optional[VietnamAdditionalInfoTypeDef] = None


class GetTaxRegistrationResponseTypeDef(BaseValidatorModel):
    taxRegistration: TaxRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AccountDetailsTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    accountMetaData: Optional[AccountMetaDataTypeDef] = None
    taxInheritanceDetails: Optional[TaxInheritanceDetailsTypeDef] = None
    taxRegistration: Optional[TaxRegistrationWithJurisdictionTypeDef] = None


class TaxExemptionDetailsTypeDef(BaseValidatorModel):
    heritageObtainedDetails: Optional[bool] = None
    heritageObtainedParentEntity: Optional[str] = None
    heritageObtainedReason: Optional[str] = None
    taxExemptions: Optional[List[TaxExemptionTypeDef]] = None


class VerificationDetailsTypeDef(BaseValidatorModel):
    dateOfBirth: Optional[str] = None
    taxRegistrationDocuments: Optional[Sequence[TaxRegistrationDocumentTypeDef]] = None


class ListTaxRegistrationsResponseTypeDef(BaseValidatorModel):
    accountDetails: List[AccountDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BatchGetTaxExemptionsResponseTypeDef(BaseValidatorModel):
    failedAccounts: List[str]
    taxExemptionDetailsMap: Dict[str, TaxExemptionDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTaxExemptionsResponseTypeDef(BaseValidatorModel):
    taxExemptionDetailsMap: Dict[str, TaxExemptionDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TaxRegistrationEntryTypeDef(BaseValidatorModel):
    registrationId: str
    registrationType: TaxRegistrationTypeType
    additionalTaxInformation: Optional[AdditionalInfoRequestTypeDef] = None
    certifiedEmailId: Optional[str] = None
    legalAddress: Optional[AddressTypeDef] = None
    legalName: Optional[str] = None
    sector: Optional[SectorType] = None
    verificationDetails: Optional[VerificationDetailsTypeDef] = None


class BatchPutTaxRegistrationRequestTypeDef(BaseValidatorModel):
    accountIds: Sequence[str]
    taxRegistrationEntry: TaxRegistrationEntryTypeDef


class PutTaxRegistrationRequestTypeDef(BaseValidatorModel):
    taxRegistrationEntry: TaxRegistrationEntryTypeDef
    accountId: Optional[str] = None



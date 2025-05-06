from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.taxsettings.taxsettings_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class TaxInheritanceDetails(BaseValidatorModel):
    inheritanceObtainedReason: Optional[str] = None
    parentEntityId: Optional[str] = None


class Address(BaseValidatorModel):
    addressLine1: str
    city: str
    countryCode: str
    postalCode: str
    addressLine2: Optional[str] = None
    addressLine3: Optional[str] = None
    districtOrCounty: Optional[str] = None
    stateOrRegion: Optional[str] = None


class Jurisdiction(BaseValidatorModel):
    countryCode: str
    stateOrRegion: Optional[str] = None


class CanadaAdditionalInfo(BaseValidatorModel):
    canadaQuebecSalesTaxNumber: Optional[str] = None
    canadaRetailSalesTaxNumber: Optional[str] = None
    isResellerAccount: Optional[bool] = None
    provincialSalesTaxId: Optional[str] = None


class EgyptAdditionalInfo(BaseValidatorModel):
    uniqueIdentificationNumber: Optional[str] = None
    uniqueIdentificationNumberExpirationDate: Optional[str] = None


class EstoniaAdditionalInfo(BaseValidatorModel):
    registryCommercialCode: str


class GeorgiaAdditionalInfo(BaseValidatorModel):
    personType: PersonTypeType


class GreeceAdditionalInfo(BaseValidatorModel):
    contractingAuthorityCode: Optional[str] = None


class IsraelAdditionalInfo(BaseValidatorModel):
    customerType: IsraelCustomerTypeType
    dealerType: IsraelDealerTypeType


class ItalyAdditionalInfo(BaseValidatorModel):
    cigNumber: Optional[str] = None
    cupNumber: Optional[str] = None
    sdiAccountId: Optional[str] = None
    taxCode: Optional[str] = None


class KenyaAdditionalInfo(BaseValidatorModel):
    personType: PersonTypeType


class PolandAdditionalInfo(BaseValidatorModel):
    individualRegistrationNumber: Optional[str] = None
    isGroupVatEnabled: Optional[bool] = None


class RomaniaAdditionalInfo(BaseValidatorModel):
    taxRegistrationNumberType: TaxRegistrationNumberTypeType


class SaudiArabiaAdditionalInfo(BaseValidatorModel):
    taxRegistrationNumberType: Optional[SaudiArabiaTaxRegistrationNumberTypeType] = None


class SouthKoreaAdditionalInfo(BaseValidatorModel):
    businessRepresentativeName: str
    itemOfBusiness: str
    lineOfBusiness: str


class SpainAdditionalInfo(BaseValidatorModel):
    registrationType: RegistrationTypeType


class TurkeyAdditionalInfo(BaseValidatorModel):
    industries: Optional[IndustriesType] = None
    kepEmailId: Optional[str] = None
    secondaryTaxId: Optional[str] = None
    taxOffice: Optional[str] = None


class UkraineAdditionalInfo(BaseValidatorModel):
    ukraineTrnType: UkraineTrnTypeType


class VietnamAdditionalInfo(BaseValidatorModel):
    electronicTransactionCodeNumber: Optional[str] = None
    enterpriseIdentificationNumber: Optional[str] = None
    paymentVoucherNumber: Optional[str] = None
    paymentVoucherNumberDate: Optional[str] = None


class BrazilAdditionalInfo(BaseValidatorModel):
    ccmCode: Optional[str] = None
    legalNatureCode: Optional[str] = None


class IndiaAdditionalInfo(BaseValidatorModel):
    pan: Optional[str] = None


class MalaysiaAdditionalInfoOutput(BaseValidatorModel):
    businessRegistrationNumber: Optional[str] = None
    serviceTaxCodes: Optional[List[MalaysiaServiceTaxCodeType]] = None
    taxInformationNumber: Optional[str] = None


class Authority(BaseValidatorModel):
    country: str
    state: Optional[str] = None


class BatchDeleteTaxRegistrationError(BaseValidatorModel):
    accountId: str
    message: str
    code: Optional[str] = None


class BatchDeleteTaxRegistrationRequest(BaseValidatorModel):
    accountIds: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetTaxExemptionsRequest(BaseValidatorModel):
    accountIds: List[str]


class BatchPutTaxRegistrationError(BaseValidatorModel):
    accountId: str
    message: str
    code: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class DeleteSupplementalTaxRegistrationRequest(BaseValidatorModel):
    authorityId: str


class DeleteTaxRegistrationRequest(BaseValidatorModel):
    accountId: Optional[str] = None


class DestinationS3Location(BaseValidatorModel):
    bucket: str
    prefix: Optional[str] = None


class TaxDocumentMetadata(BaseValidatorModel):
    taxDocumentAccessToken: str
    taxDocumentName: str


class GetTaxRegistrationRequest(BaseValidatorModel):
    accountId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListSupplementalTaxRegistrationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTaxExemptionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTaxRegistrationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MalaysiaAdditionalInfo(BaseValidatorModel):
    businessRegistrationNumber: Optional[str] = None
    serviceTaxCodes: Optional[List[MalaysiaServiceTaxCodeType]] = None
    taxInformationNumber: Optional[str] = None


class PutTaxInheritanceRequest(BaseValidatorModel):
    heritageStatus: Optional[HeritageStatusType] = None


class SourceS3Location(BaseValidatorModel):
    bucket: str
    key: str


class SupplementalTaxRegistrationEntry(BaseValidatorModel):
    address: Address
    legalName: str
    registrationId: str
    registrationType: Literal['VAT']


class SupplementalTaxRegistration(BaseValidatorModel):
    address: Address
    authorityId: str
    legalName: str
    registrationId: str
    registrationType: Literal['VAT']
    status: TaxRegistrationStatusType


class AccountMetaData(BaseValidatorModel):
    accountName: Optional[str] = None
    address: Optional[Address] = None
    addressRoleMap: Optional[Dict[AddressRoleTypeType, Jurisdiction]] = None
    addressType: Optional[AddressRoleTypeType] = None
    seller: Optional[str] = None


class AdditionalInfoResponse(BaseValidatorModel):
    brazilAdditionalInfo: Optional[BrazilAdditionalInfo] = None
    canadaAdditionalInfo: Optional[CanadaAdditionalInfo] = None
    egyptAdditionalInfo: Optional[EgyptAdditionalInfo] = None
    estoniaAdditionalInfo: Optional[EstoniaAdditionalInfo] = None
    georgiaAdditionalInfo: Optional[GeorgiaAdditionalInfo] = None
    greeceAdditionalInfo: Optional[GreeceAdditionalInfo] = None
    indiaAdditionalInfo: Optional[IndiaAdditionalInfo] = None
    israelAdditionalInfo: Optional[IsraelAdditionalInfo] = None
    italyAdditionalInfo: Optional[ItalyAdditionalInfo] = None
    kenyaAdditionalInfo: Optional[KenyaAdditionalInfo] = None
    malaysiaAdditionalInfo: Optional[MalaysiaAdditionalInfoOutput] = None
    polandAdditionalInfo: Optional[PolandAdditionalInfo] = None
    romaniaAdditionalInfo: Optional[RomaniaAdditionalInfo] = None
    saudiArabiaAdditionalInfo: Optional[SaudiArabiaAdditionalInfo] = None
    southKoreaAdditionalInfo: Optional[SouthKoreaAdditionalInfo] = None
    spainAdditionalInfo: Optional[SpainAdditionalInfo] = None
    turkeyAdditionalInfo: Optional[TurkeyAdditionalInfo] = None
    ukraineAdditionalInfo: Optional[UkraineAdditionalInfo] = None
    vietnamAdditionalInfo: Optional[VietnamAdditionalInfo] = None


class TaxExemptionType(BaseValidatorModel):
    applicableJurisdictions: Optional[List[Authority]] = None
    description: Optional[str] = None
    displayName: Optional[str] = None


class BatchDeleteTaxRegistrationResponse(BaseValidatorModel):
    errors: List[BatchDeleteTaxRegistrationError]
    ResponseMetadata: ResponseMetadata


class GetTaxInheritanceResponse(BaseValidatorModel):
    heritageStatus: HeritageStatusType
    ResponseMetadata: ResponseMetadata


class GetTaxRegistrationDocumentResponse(BaseValidatorModel):
    destinationFilePath: str
    presignedS3Url: str
    ResponseMetadata: ResponseMetadata


class PutSupplementalTaxRegistrationResponse(BaseValidatorModel):
    authorityId: str
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadata


class PutTaxExemptionResponse(BaseValidatorModel):
    caseId: str
    ResponseMetadata: ResponseMetadata


class PutTaxRegistrationResponse(BaseValidatorModel):
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadata


class BatchPutTaxRegistrationResponse(BaseValidatorModel):
    errors: List[BatchPutTaxRegistrationError]
    status: TaxRegistrationStatusType
    ResponseMetadata: ResponseMetadata


class ExemptionCertificate(BaseValidatorModel):
    documentFile: Blob
    documentName: str


class TaxRegistrationDocFile(BaseValidatorModel):
    fileContent: Blob
    fileName: str


class GetTaxRegistrationDocumentRequest(BaseValidatorModel):
    taxDocumentMetadata: TaxDocumentMetadata
    destinationS3Location: Optional[DestinationS3Location] = None


class ListSupplementalTaxRegistrationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTaxExemptionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTaxRegistrationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None

MalaysiaAdditionalInfoUnion = Union[MalaysiaAdditionalInfo, MalaysiaAdditionalInfoOutput]


class PutSupplementalTaxRegistrationRequest(BaseValidatorModel):
    taxRegistrationEntry: SupplementalTaxRegistrationEntry


class ListSupplementalTaxRegistrationsResponse(BaseValidatorModel):
    taxRegistrations: List[SupplementalTaxRegistration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TaxRegistration(BaseValidatorModel):
    legalAddress: Address
    legalName: str
    registrationId: str
    registrationType: TaxRegistrationTypeType
    status: TaxRegistrationStatusType
    additionalTaxInformation: Optional[AdditionalInfoResponse] = None
    certifiedEmailId: Optional[str] = None
    sector: Optional[SectorType] = None
    taxDocumentMetadatas: Optional[List[TaxDocumentMetadata]] = None


class TaxRegistrationWithJurisdiction(BaseValidatorModel):
    jurisdiction: Jurisdiction
    legalName: str
    registrationId: str
    registrationType: TaxRegistrationTypeType
    status: TaxRegistrationStatusType
    additionalTaxInformation: Optional[AdditionalInfoResponse] = None
    certifiedEmailId: Optional[str] = None
    sector: Optional[SectorType] = None
    taxDocumentMetadatas: Optional[List[TaxDocumentMetadata]] = None


class GetTaxExemptionTypesResponse(BaseValidatorModel):
    taxExemptionTypes: List[TaxExemptionType]
    ResponseMetadata: ResponseMetadata


class TaxExemption(BaseValidatorModel):
    authority: Authority
    taxExemptionType: TaxExemptionType
    effectiveDate: Optional[datetime] = None
    expirationDate: Optional[datetime] = None
    status: Optional[EntityExemptionAccountStatusType] = None
    systemEffectiveDate: Optional[datetime] = None


class PutTaxExemptionRequest(BaseValidatorModel):
    accountIds: List[str]
    authority: Authority
    exemptionCertificate: ExemptionCertificate
    exemptionType: str


class TaxRegistrationDocument(BaseValidatorModel):
    file: Optional[TaxRegistrationDocFile] = None
    s3Location: Optional[SourceS3Location] = None


class AdditionalInfoRequest(BaseValidatorModel):
    canadaAdditionalInfo: Optional[CanadaAdditionalInfo] = None
    egyptAdditionalInfo: Optional[EgyptAdditionalInfo] = None
    estoniaAdditionalInfo: Optional[EstoniaAdditionalInfo] = None
    georgiaAdditionalInfo: Optional[GeorgiaAdditionalInfo] = None
    greeceAdditionalInfo: Optional[GreeceAdditionalInfo] = None
    israelAdditionalInfo: Optional[IsraelAdditionalInfo] = None
    italyAdditionalInfo: Optional[ItalyAdditionalInfo] = None
    kenyaAdditionalInfo: Optional[KenyaAdditionalInfo] = None
    malaysiaAdditionalInfo: Optional[MalaysiaAdditionalInfoUnion] = None
    polandAdditionalInfo: Optional[PolandAdditionalInfo] = None
    romaniaAdditionalInfo: Optional[RomaniaAdditionalInfo] = None
    saudiArabiaAdditionalInfo: Optional[SaudiArabiaAdditionalInfo] = None
    southKoreaAdditionalInfo: Optional[SouthKoreaAdditionalInfo] = None
    spainAdditionalInfo: Optional[SpainAdditionalInfo] = None
    turkeyAdditionalInfo: Optional[TurkeyAdditionalInfo] = None
    ukraineAdditionalInfo: Optional[UkraineAdditionalInfo] = None
    vietnamAdditionalInfo: Optional[VietnamAdditionalInfo] = None


class GetTaxRegistrationResponse(BaseValidatorModel):
    taxRegistration: TaxRegistration
    ResponseMetadata: ResponseMetadata


class AccountDetails(BaseValidatorModel):
    accountId: Optional[str] = None
    accountMetaData: Optional[AccountMetaData] = None
    taxInheritanceDetails: Optional[TaxInheritanceDetails] = None
    taxRegistration: Optional[TaxRegistrationWithJurisdiction] = None


class TaxExemptionDetails(BaseValidatorModel):
    heritageObtainedDetails: Optional[bool] = None
    heritageObtainedParentEntity: Optional[str] = None
    heritageObtainedReason: Optional[str] = None
    taxExemptions: Optional[List[TaxExemption]] = None


class VerificationDetails(BaseValidatorModel):
    dateOfBirth: Optional[str] = None
    taxRegistrationDocuments: Optional[List[TaxRegistrationDocument]] = None


class ListTaxRegistrationsResponse(BaseValidatorModel):
    accountDetails: List[AccountDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchGetTaxExemptionsResponse(BaseValidatorModel):
    failedAccounts: List[str]
    taxExemptionDetailsMap: Dict[str, TaxExemptionDetails]
    ResponseMetadata: ResponseMetadata


class ListTaxExemptionsResponse(BaseValidatorModel):
    taxExemptionDetailsMap: Dict[str, TaxExemptionDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TaxRegistrationEntry(BaseValidatorModel):
    registrationId: str
    registrationType: TaxRegistrationTypeType
    additionalTaxInformation: Optional[AdditionalInfoRequest] = None
    certifiedEmailId: Optional[str] = None
    legalAddress: Optional[Address] = None
    legalName: Optional[str] = None
    sector: Optional[SectorType] = None
    verificationDetails: Optional[VerificationDetails] = None


class BatchPutTaxRegistrationRequest(BaseValidatorModel):
    accountIds: List[str]
    taxRegistrationEntry: TaxRegistrationEntry


class PutTaxRegistrationRequest(BaseValidatorModel):
    taxRegistrationEntry: TaxRegistrationEntry
    accountId: Optional[str] = None
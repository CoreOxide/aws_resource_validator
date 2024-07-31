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
from aws_resource_validator.pydantic_models.marketplace_agreement_constants import *

class ByolPricingTermTypeDef(BaseModel):
    type: Optional[str] = None

class RecurringPaymentTermTypeDef(BaseModel):
    billingPeriod: Optional[str] = None
    currencyCode: Optional[str] = None
    price: Optional[str] = None
    type: Optional[str] = None

class SupportTermTypeDef(BaseModel):
    refundPolicy: Optional[str] = None
    type: Optional[str] = None

class ValidityTermTypeDef(BaseModel):
    agreementDuration: Optional[str] = None
    agreementEndDate: Optional[datetime] = None
    agreementStartDate: Optional[datetime] = None
    type: Optional[str] = None

class AcceptorTypeDef(BaseModel):
    accountId: Optional[str] = None

class ProposerTypeDef(BaseModel):
    accountId: Optional[str] = None

class DimensionTypeDef(BaseModel):
    dimensionKey: str
    dimensionValue: int

class ConstraintsTypeDef(BaseModel):
    multipleDimensionSelection: Optional[str] = None
    quantityConfiguration: Optional[str] = None

class RateCardItemTypeDef(BaseModel):
    dimensionKey: Optional[str] = None
    price: Optional[str] = None

class SelectorTypeDef(BaseModel):
    type: Optional[str] = None
    value: Optional[str] = None

class DescribeAgreementInputRequestTypeDef(BaseModel):
    agreementId: str

class EstimatedChargesTypeDef(BaseModel):
    agreementValue: Optional[str] = None
    currencyCode: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DocumentItemTypeDef(BaseModel):
    type: Optional[str] = None
    url: Optional[str] = None
    version: Optional[str] = None

class FilterTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class GrantItemTypeDef(BaseModel):
    dimensionKey: Optional[str] = None
    maxQuantity: Optional[int] = None

class GetAgreementTermsInputRequestTypeDef(BaseModel):
    agreementId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ScheduleItemTypeDef(BaseModel):
    chargeAmount: Optional[str] = None
    chargeDate: Optional[datetime] = None

class ResourceTypeDef(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None

class RenewalTermConfigurationTypeDef(BaseModel):
    enableAutoRenew: bool

class SortTypeDef(BaseModel):
    sortBy: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None

class ConfigurableUpfrontPricingTermConfigurationTypeDef(BaseModel):
    dimensions: List[DimensionTypeDef]
    selectorValue: str

class UsageBasedRateCardItemTypeDef(BaseModel):
    rateCard: Optional[List[RateCardItemTypeDef]] = None

class ConfigurableUpfrontRateCardItemTypeDef(BaseModel):
    constraints: Optional[ConstraintsTypeDef] = None
    rateCard: Optional[List[RateCardItemTypeDef]] = None
    selector: Optional[SelectorTypeDef] = None

class LegalTermTypeDef(BaseModel):
    documents: Optional[List[DocumentItemTypeDef]] = None
    type: Optional[str] = None

class FixedUpfrontPricingTermTypeDef(BaseModel):
    currencyCode: Optional[str] = None
    duration: Optional[str] = None
    grants: Optional[List[GrantItemTypeDef]] = None
    price: Optional[str] = None
    type: Optional[str] = None

class FreeTrialPricingTermTypeDef(BaseModel):
    duration: Optional[str] = None
    grants: Optional[List[GrantItemTypeDef]] = None
    type: Optional[str] = None

class PaymentScheduleTermTypeDef(BaseModel):
    currencyCode: Optional[str] = None
    schedule: Optional[List[ScheduleItemTypeDef]] = None
    type: Optional[str] = None

class ProposalSummaryTypeDef(BaseModel):
    offerId: Optional[str] = None
    resources: Optional[List[ResourceTypeDef]] = None

class RenewalTermTypeDef(BaseModel):
    configuration: Optional[RenewalTermConfigurationTypeDef] = None
    type: Optional[str] = None

class SearchAgreementsInputRequestTypeDef(BaseModel):
    catalog: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortTypeDef] = None

class UsageBasedPricingTermTypeDef(BaseModel):
    currencyCode: Optional[str] = None
    rateCards: Optional[List[UsageBasedRateCardItemTypeDef]] = None
    type: Optional[str] = None

class ConfigurableUpfrontPricingTermTypeDef(BaseModel):
    configuration: Optional[ConfigurableUpfrontPricingTermConfigurationTypeDef] = None
    currencyCode: Optional[str] = None
    rateCards: Optional[List[ConfigurableUpfrontRateCardItemTypeDef]] = None
    type: Optional[str] = None

class AgreementViewSummaryTypeDef(BaseModel):
    acceptanceTime: Optional[datetime] = None
    acceptor: Optional[AcceptorTypeDef] = None
    agreementId: Optional[str] = None
    agreementType: Optional[str] = None
    endTime: Optional[datetime] = None
    proposalSummary: Optional[ProposalSummaryTypeDef] = None
    proposer: Optional[ProposerTypeDef] = None
    startTime: Optional[datetime] = None
    status: Optional[AgreementStatusType] = None

class DescribeAgreementOutputTypeDef(BaseModel):
    acceptanceTime: datetime
    acceptor: AcceptorTypeDef
    agreementId: str
    agreementType: str
    endTime: datetime
    estimatedCharges: EstimatedChargesTypeDef
    proposalSummary: ProposalSummaryTypeDef
    proposer: ProposerTypeDef
    startTime: datetime
    status: AgreementStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptedTermTypeDef(BaseModel):
    byolPricingTerm: Optional[ByolPricingTermTypeDef] = None
    configurableUpfrontPricingTerm: Optional[ConfigurableUpfrontPricingTermTypeDef] = None
    fixedUpfrontPricingTerm: Optional[FixedUpfrontPricingTermTypeDef] = None
    freeTrialPricingTerm: Optional[FreeTrialPricingTermTypeDef] = None
    legalTerm: Optional[LegalTermTypeDef] = None
    paymentScheduleTerm: Optional[PaymentScheduleTermTypeDef] = None
    recurringPaymentTerm: Optional[RecurringPaymentTermTypeDef] = None
    renewalTerm: Optional[RenewalTermTypeDef] = None
    supportTerm: Optional[SupportTermTypeDef] = None
    usageBasedPricingTerm: Optional[UsageBasedPricingTermTypeDef] = None
    validityTerm: Optional[ValidityTermTypeDef] = None

class SearchAgreementsOutputTypeDef(BaseModel):
    agreementViewSummaries: List[AgreementViewSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgreementTermsOutputTypeDef(BaseModel):
    acceptedTerms: List[AcceptedTermTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


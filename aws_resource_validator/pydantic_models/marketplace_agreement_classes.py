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
from aws_resource_validator.pydantic_models.marketplace_agreement_constants import *

class ByolPricingTermTypeDef(BaseValidatorModel):
    type: Optional[str] = None

class RecurringPaymentTermTypeDef(BaseValidatorModel):
    billingPeriod: Optional[str] = None
    currencyCode: Optional[str] = None
    price: Optional[str] = None
    type: Optional[str] = None

class SupportTermTypeDef(BaseValidatorModel):
    refundPolicy: Optional[str] = None
    type: Optional[str] = None

class ValidityTermTypeDef(BaseValidatorModel):
    agreementDuration: Optional[str] = None
    agreementEndDate: Optional[datetime] = None
    agreementStartDate: Optional[datetime] = None
    type: Optional[str] = None

class AcceptorTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class ProposerTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None

class DimensionTypeDef(BaseValidatorModel):
    dimensionKey: str
    dimensionValue: int

class ConstraintsTypeDef(BaseValidatorModel):
    multipleDimensionSelection: Optional[str] = None
    quantityConfiguration: Optional[str] = None

class RateCardItemTypeDef(BaseValidatorModel):
    dimensionKey: Optional[str] = None
    price: Optional[str] = None

class SelectorTypeDef(BaseValidatorModel):
    type: Optional[str] = None
    value: Optional[str] = None

class DescribeAgreementInputRequestTypeDef(BaseValidatorModel):
    agreementId: str

class EstimatedChargesTypeDef(BaseValidatorModel):
    agreementValue: Optional[str] = None
    currencyCode: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DocumentItemTypeDef(BaseValidatorModel):
    type: Optional[str] = None
    url: Optional[str] = None
    version: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class GrantItemTypeDef(BaseValidatorModel):
    dimensionKey: Optional[str] = None
    maxQuantity: Optional[int] = None

class GetAgreementTermsInputRequestTypeDef(BaseValidatorModel):
    agreementId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ScheduleItemTypeDef(BaseValidatorModel):
    chargeAmount: Optional[str] = None
    chargeDate: Optional[datetime] = None

class ResourceTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[str] = None

class RenewalTermConfigurationTypeDef(BaseValidatorModel):
    enableAutoRenew: bool

class SortTypeDef(BaseValidatorModel):
    sortBy: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None

class ConfigurableUpfrontPricingTermConfigurationTypeDef(BaseValidatorModel):
    dimensions: List[DimensionTypeDef]
    selectorValue: str

class UsageBasedRateCardItemTypeDef(BaseValidatorModel):
    rateCard: Optional[List[RateCardItemTypeDef]] = None

class ConfigurableUpfrontRateCardItemTypeDef(BaseValidatorModel):
    constraints: Optional[ConstraintsTypeDef] = None
    rateCard: Optional[List[RateCardItemTypeDef]] = None
    selector: Optional[SelectorTypeDef] = None

class LegalTermTypeDef(BaseValidatorModel):
    documents: Optional[List[DocumentItemTypeDef]] = None
    type: Optional[str] = None

class FixedUpfrontPricingTermTypeDef(BaseValidatorModel):
    currencyCode: Optional[str] = None
    duration: Optional[str] = None
    grants: Optional[List[GrantItemTypeDef]] = None
    price: Optional[str] = None
    type: Optional[str] = None

class FreeTrialPricingTermTypeDef(BaseValidatorModel):
    duration: Optional[str] = None
    grants: Optional[List[GrantItemTypeDef]] = None
    type: Optional[str] = None

class PaymentScheduleTermTypeDef(BaseValidatorModel):
    currencyCode: Optional[str] = None
    schedule: Optional[List[ScheduleItemTypeDef]] = None
    type: Optional[str] = None

class ProposalSummaryTypeDef(BaseValidatorModel):
    offerId: Optional[str] = None
    resources: Optional[List[ResourceTypeDef]] = None

class RenewalTermTypeDef(BaseValidatorModel):
    configuration: Optional[RenewalTermConfigurationTypeDef] = None
    type: Optional[str] = None

class SearchAgreementsInputRequestTypeDef(BaseValidatorModel):
    catalog: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortTypeDef] = None

class UsageBasedPricingTermTypeDef(BaseValidatorModel):
    currencyCode: Optional[str] = None
    rateCards: Optional[List[UsageBasedRateCardItemTypeDef]] = None
    type: Optional[str] = None

class ConfigurableUpfrontPricingTermTypeDef(BaseValidatorModel):
    configuration: Optional[ConfigurableUpfrontPricingTermConfigurationTypeDef] = None
    currencyCode: Optional[str] = None
    rateCards: Optional[List[ConfigurableUpfrontRateCardItemTypeDef]] = None
    type: Optional[str] = None

class AgreementViewSummaryTypeDef(BaseValidatorModel):
    acceptanceTime: Optional[datetime] = None
    acceptor: Optional[AcceptorTypeDef] = None
    agreementId: Optional[str] = None
    agreementType: Optional[str] = None
    endTime: Optional[datetime] = None
    proposalSummary: Optional[ProposalSummaryTypeDef] = None
    proposer: Optional[ProposerTypeDef] = None
    startTime: Optional[datetime] = None
    status: Optional[AgreementStatusType] = None

class DescribeAgreementOutputTypeDef(BaseValidatorModel):
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

class AcceptedTermTypeDef(BaseValidatorModel):
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

class SearchAgreementsOutputTypeDef(BaseValidatorModel):
    agreementViewSummaries: List[AgreementViewSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAgreementTermsOutputTypeDef(BaseValidatorModel):
    acceptedTerms: List[AcceptedTermTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


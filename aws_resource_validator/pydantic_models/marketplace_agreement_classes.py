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
from aws_resource_validator.pydantic_models.marketplace_agreement_constants import *

class Acceptor(BaseValidatorModel):
    accountId: Optional[str] = None


class Proposer(BaseValidatorModel):
    accountId: Optional[str] = None


class Dimension(BaseValidatorModel):
    dimensionKey: str
    dimensionValue: int


class Constraints(BaseValidatorModel):
    multipleDimensionSelection: Optional[str] = None
    quantityConfiguration: Optional[str] = None


class RateCardItem(BaseValidatorModel):
    dimensionKey: Optional[str] = None
    price: Optional[str] = None


class DescribeAgreementInput(BaseValidatorModel):
    agreementId: str


class EstimatedCharges(BaseValidatorModel):
    agreementValue: Optional[str] = None
    currencyCode: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Filter(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None


class GrantItem(BaseValidatorModel):
    dimensionKey: Optional[str] = None
    maxQuantity: Optional[int] = None


class GetAgreementTermsInput(BaseValidatorModel):
    agreementId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ScheduleItem(BaseValidatorModel):
    chargeAmount: Optional[str] = None
    chargeDate: Optional[datetime] = None


class RenewalTermConfiguration(BaseValidatorModel):
    enableAutoRenew: bool


class Sort(BaseValidatorModel):
    sortBy: Optional[str] = None
    sortOrder: Optional[SortOrderType] = None


class ConfigurableUpfrontPricingTermConfiguration(BaseValidatorModel):
    dimensions: List[Dimension]
    selectorValue: str


class UsageBasedRateCardItem(BaseValidatorModel):
    rateCard: Optional[List[RateCardItem]] = None


class Selector(BaseValidatorModel):
    pass


class ConfigurableUpfrontRateCardItem(BaseValidatorModel):
    constraints: Optional[Constraints] = None
    rateCard: Optional[List[RateCardItem]] = None
    selector: Optional[Selector] = None


class Resource(BaseValidatorModel):
    pass


class ProposalSummary(BaseValidatorModel):
    offerId: Optional[str] = None
    resources: Optional[List[Resource]] = None


class SearchAgreementsInput(BaseValidatorModel):
    catalog: Optional[str] = None
    filters: Optional[Sequence[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[Sort] = None


class AgreementViewSummary(BaseValidatorModel):
    acceptanceTime: Optional[datetime] = None
    acceptor: Optional[Acceptor] = None
    agreementId: Optional[str] = None
    agreementType: Optional[str] = None
    endTime: Optional[datetime] = None
    proposalSummary: Optional[ProposalSummary] = None
    proposer: Optional[Proposer] = None
    startTime: Optional[datetime] = None
    status: Optional[AgreementStatusType] = None


class DescribeAgreementOutput(BaseValidatorModel):
    acceptanceTime: datetime
    acceptor: Acceptor
    agreementId: str
    agreementType: str
    endTime: datetime
    estimatedCharges: EstimatedCharges
    proposalSummary: ProposalSummary
    proposer: Proposer
    startTime: datetime
    status: AgreementStatusType
    ResponseMetadata: ResponseMetadata


class LegalTerm(BaseValidatorModel):
    pass


class ByolPricingTerm(BaseValidatorModel):
    pass


class ValidityTerm(BaseValidatorModel):
    pass


class RenewalTerm(BaseValidatorModel):
    pass


class SupportTerm(BaseValidatorModel):
    pass


class RecurringPaymentTerm(BaseValidatorModel):
    pass


class ConfigurableUpfrontPricingTerm(BaseValidatorModel):
    pass


class UsageBasedPricingTerm(BaseValidatorModel):
    pass


class FixedUpfrontPricingTerm(BaseValidatorModel):
    pass


class PaymentScheduleTerm(BaseValidatorModel):
    pass


class FreeTrialPricingTerm(BaseValidatorModel):
    pass


class AcceptedTerm(BaseValidatorModel):
    byolPricingTerm: Optional[ByolPricingTerm] = None
    configurableUpfrontPricingTerm: Optional[ConfigurableUpfrontPricingTerm] = None
    fixedUpfrontPricingTerm: Optional[FixedUpfrontPricingTerm] = None
    freeTrialPricingTerm: Optional[FreeTrialPricingTerm] = None
    legalTerm: Optional[LegalTerm] = None
    paymentScheduleTerm: Optional[PaymentScheduleTerm] = None
    recurringPaymentTerm: Optional[RecurringPaymentTerm] = None
    renewalTerm: Optional[RenewalTerm] = None
    supportTerm: Optional[SupportTerm] = None
    usageBasedPricingTerm: Optional[UsageBasedPricingTerm] = None
    validityTerm: Optional[ValidityTerm] = None


class SearchAgreementsOutput(BaseValidatorModel):
    agreementViewSummaries: List[AgreementViewSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetAgreementTermsOutput(BaseValidatorModel):
    acceptedTerms: List[AcceptedTerm]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None



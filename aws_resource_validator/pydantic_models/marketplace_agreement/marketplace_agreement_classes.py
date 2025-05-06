from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ByolPricingTerm(BaseValidatorModel):
    type: Optional[str] = None


class RecurringPaymentTerm(BaseValidatorModel):
    billingPeriod: Optional[str] = None
    currencyCode: Optional[str] = None
    price: Optional[str] = None
    type: Optional[str] = None


class SupportTerm(BaseValidatorModel):
    refundPolicy: Optional[str] = None
    type: Optional[str] = None


class ValidityTerm(BaseValidatorModel):
    agreementDuration: Optional[str] = None
    agreementEndDate: Optional[datetime] = None
    agreementStartDate: Optional[datetime] = None
    type: Optional[str] = None


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


class Selector(BaseValidatorModel):
    type: Optional[str] = None
    value: Optional[str] = None


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


class DocumentItem(BaseValidatorModel):
    type: Optional[str] = None
    url: Optional[str] = None
    version: Optional[str] = None


class Filter(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


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


class Resource(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[str] = None


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


class ConfigurableUpfrontRateCardItem(BaseValidatorModel):
    constraints: Optional[Constraints] = None
    rateCard: Optional[List[RateCardItem]] = None
    selector: Optional[Selector] = None


class LegalTerm(BaseValidatorModel):
    documents: Optional[List[DocumentItem]] = None
    type: Optional[str] = None


class FixedUpfrontPricingTerm(BaseValidatorModel):
    currencyCode: Optional[str] = None
    duration: Optional[str] = None
    grants: Optional[List[GrantItem]] = None
    price: Optional[str] = None
    type: Optional[str] = None


class FreeTrialPricingTerm(BaseValidatorModel):
    duration: Optional[str] = None
    grants: Optional[List[GrantItem]] = None
    type: Optional[str] = None


class PaymentScheduleTerm(BaseValidatorModel):
    currencyCode: Optional[str] = None
    schedule: Optional[List[ScheduleItem]] = None
    type: Optional[str] = None


class ProposalSummary(BaseValidatorModel):
    offerId: Optional[str] = None
    resources: Optional[List[Resource]] = None


class RenewalTerm(BaseValidatorModel):
    configuration: Optional[RenewalTermConfiguration] = None
    type: Optional[str] = None


class SearchAgreementsInput(BaseValidatorModel):
    catalog: Optional[str] = None
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[Sort] = None


class UsageBasedPricingTerm(BaseValidatorModel):
    currencyCode: Optional[str] = None
    rateCards: Optional[List[UsageBasedRateCardItem]] = None
    type: Optional[str] = None


class ConfigurableUpfrontPricingTerm(BaseValidatorModel):
    configuration: Optional[ConfigurableUpfrontPricingTermConfiguration] = None
    currencyCode: Optional[str] = None
    rateCards: Optional[List[ConfigurableUpfrontRateCardItem]] = None
    type: Optional[str] = None


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
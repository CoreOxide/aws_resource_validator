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


class DescribeAgreementInputTypeDef(BaseValidatorModel):
    agreementId: str


class EstimatedChargesTypeDef(BaseValidatorModel):
    agreementValue: Optional[str] = None
    currencyCode: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None


class GrantItemTypeDef(BaseValidatorModel):
    dimensionKey: Optional[str] = None
    maxQuantity: Optional[int] = None


class GetAgreementTermsInputTypeDef(BaseValidatorModel):
    agreementId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ScheduleItemTypeDef(BaseValidatorModel):
    chargeAmount: Optional[str] = None
    chargeDate: Optional[datetime] = None


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


class SelectorTypeDef(BaseValidatorModel):
    pass


class ConfigurableUpfrontRateCardItemTypeDef(BaseValidatorModel):
    constraints: Optional[ConstraintsTypeDef] = None
    rateCard: Optional[List[RateCardItemTypeDef]] = None
    selector: Optional[SelectorTypeDef] = None


class ResourceTypeDef(BaseValidatorModel):
    pass


class ProposalSummaryTypeDef(BaseValidatorModel):
    offerId: Optional[str] = None
    resources: Optional[List[ResourceTypeDef]] = None


class SearchAgreementsInputTypeDef(BaseValidatorModel):
    catalog: Optional[str] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sort: Optional[SortTypeDef] = None


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


class LegalTermTypeDef(BaseValidatorModel):
    pass


class ByolPricingTermTypeDef(BaseValidatorModel):
    pass


class ValidityTermTypeDef(BaseValidatorModel):
    pass


class RenewalTermTypeDef(BaseValidatorModel):
    pass


class SupportTermTypeDef(BaseValidatorModel):
    pass


class RecurringPaymentTermTypeDef(BaseValidatorModel):
    pass


class ConfigurableUpfrontPricingTermTypeDef(BaseValidatorModel):
    pass


class UsageBasedPricingTermTypeDef(BaseValidatorModel):
    pass


class FixedUpfrontPricingTermTypeDef(BaseValidatorModel):
    pass


class PaymentScheduleTermTypeDef(BaseValidatorModel):
    pass


class FreeTrialPricingTermTypeDef(BaseValidatorModel):
    pass


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetAgreementTermsOutputTypeDef(BaseValidatorModel):
    acceptedTerms: List[AcceptedTermTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None



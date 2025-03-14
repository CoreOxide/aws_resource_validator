# Marketplace Agreement Classes

# AcceptedTermTypeDef

### byolPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ByolPricingTermTypeDef]

### configurableUpfrontPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ConfigurableUpfrontPricingTermTypeDef]

### fixedUpfrontPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.FixedUpfrontPricingTermTypeDef]

### freeTrialPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.FreeTrialPricingTermTypeDef]

### legalTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.LegalTermTypeDef]

### paymentScheduleTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.PaymentScheduleTermTypeDef]

### recurringPaymentTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.RecurringPaymentTermTypeDef]

### renewalTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.RenewalTermTypeDef]

### supportTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.SupportTermTypeDef]

### usageBasedPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.UsageBasedPricingTermTypeDef]

### validityTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ValidityTermTypeDef]


# AcceptorTypeDef

### accountId
- **Type**: typing.Optional[str]


# AgreementViewSummaryTypeDef

### acceptanceTime
- **Type**: typing.Optional[datetime.datetime]

### acceptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.AcceptorTypeDef]

### agreementId
- **Type**: typing.Optional[str]

### agreementType
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### proposalSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ProposalSummaryTypeDef]

### proposer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ProposerTypeDef]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED', 'CANCELLED', 'EXPIRED', 'RENEWED', 'REPLACED', 'ROLLED_BACK', 'SUPERSEDED', 'TERMINATED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByolPricingTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurableUpfrontPricingTermConfigurationTypeDef

### dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.DimensionTypeDef]
- **Required**: Yes

### selectorValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurableUpfrontPricingTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurableUpfrontRateCardItemTypeDef

### constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ConstraintsTypeDef]

### rateCard
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.RateCardItemTypeDef]]

### selector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.SelectorTypeDef]


# ConstraintsTypeDef

### multipleDimensionSelection
- **Type**: typing.Optional[str]

### quantityConfiguration
- **Type**: typing.Optional[str]


# DescribeAgreementInputTypeDef

### agreementId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgreementOutputTypeDef

### acceptanceTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### acceptor
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.AcceptorTypeDef'>
- **Required**: Yes

### agreementId
- **Type**: <class 'str'>
- **Required**: Yes

### agreementType
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### estimatedCharges
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.EstimatedChargesTypeDef'>
- **Required**: Yes

### proposalSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.ProposalSummaryTypeDef'>
- **Required**: Yes

### proposer
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.ProposerTypeDef'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED', 'CANCELLED', 'EXPIRED', 'RENEWED', 'REPLACED', 'ROLLED_BACK', 'SUPERSEDED', 'TERMINATED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DimensionTypeDef

### dimensionKey
- **Type**: <class 'str'>
- **Required**: Yes

### dimensionValue
- **Type**: <class 'int'>
- **Required**: Yes


# EstimatedChargesTypeDef

### agreementValue
- **Type**: typing.Optional[str]

### currencyCode
- **Type**: typing.Optional[str]


# FilterTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# FixedUpfrontPricingTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FreeTrialPricingTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAgreementTermsInputTypeDef

### agreementId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetAgreementTermsOutputTypeDef

### acceptedTerms
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.AcceptedTermTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GrantItemTypeDef

### dimensionKey
- **Type**: typing.Optional[str]

### maxQuantity
- **Type**: typing.Optional[int]


# LegalTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaymentScheduleTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProposalSummaryTypeDef

### offerId
- **Type**: typing.Optional[str]

### resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ResourceTypeDef]]


# ProposerTypeDef

### accountId
- **Type**: typing.Optional[str]


# RateCardItemTypeDef

### dimensionKey
- **Type**: typing.Optional[str]

### price
- **Type**: typing.Optional[str]


# RecurringPaymentTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RenewalTermConfigurationTypeDef

### enableAutoRenew
- **Type**: <class 'bool'>
- **Required**: Yes


# RenewalTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# ScheduleItemTypeDef

### chargeAmount
- **Type**: typing.Optional[str]

### chargeDate
- **Type**: typing.Optional[datetime.datetime]


# SearchAgreementsInputTypeDef

### catalog
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.marketplace_agreement_classes.FilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.SortTypeDef]


# SearchAgreementsOutputTypeDef

### agreementViewSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.AgreementViewSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SelectorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SortTypeDef

### sortBy
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# SupportTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsageBasedPricingTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UsageBasedRateCardItemTypeDef

### rateCard
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.RateCardItemTypeDef]]


# ValidityTermTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


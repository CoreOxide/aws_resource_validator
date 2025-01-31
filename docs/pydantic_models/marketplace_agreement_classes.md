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

### type
- **Type**: typing.Optional[str]


# ConfigurableUpfrontPricingTermConfigurationTypeDef

### dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.DimensionTypeDef]
- **Required**: Yes

### selectorValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurableUpfrontPricingTermTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ConfigurableUpfrontPricingTermConfigurationTypeDef]

### currencyCode
- **Type**: typing.Optional[str]

### rateCards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ConfigurableUpfrontRateCardItemTypeDef]]

### type
- **Type**: typing.Optional[str]


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


# DescribeAgreementInputRequestTypeDef

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


# DocumentItemTypeDef

### type
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


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

### currencyCode
- **Type**: typing.Optional[str]

### duration
- **Type**: typing.Optional[str]

### grants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.GrantItemTypeDef]]

### price
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# FreeTrialPricingTermTypeDef

### duration
- **Type**: typing.Optional[str]

### grants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.GrantItemTypeDef]]

### type
- **Type**: typing.Optional[str]


# GetAgreementTermsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GrantItemTypeDef

### dimensionKey
- **Type**: typing.Optional[str]

### maxQuantity
- **Type**: typing.Optional[int]


# LegalTermTypeDef

### documents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.DocumentItemTypeDef]]

### type
- **Type**: typing.Optional[str]


# PaymentScheduleTermTypeDef

### currencyCode
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.ScheduleItemTypeDef]]

### type
- **Type**: typing.Optional[str]


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

### billingPeriod
- **Type**: typing.Optional[str]

### currencyCode
- **Type**: typing.Optional[str]

### price
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# RenewalTermConfigurationTypeDef

### enableAutoRenew
- **Type**: <class 'bool'>
- **Required**: Yes


# RenewalTermTypeDef

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement_classes.RenewalTermConfigurationTypeDef]

### type
- **Type**: typing.Optional[str]


# ResourceTypeDef

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# ScheduleItemTypeDef

### chargeAmount
- **Type**: typing.Optional[str]

### chargeDate
- **Type**: typing.Optional[datetime.datetime]


# SearchAgreementsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SelectorTypeDef

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# SortTypeDef

### sortBy
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# SupportTermTypeDef

### refundPolicy
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# UsageBasedPricingTermTypeDef

### currencyCode
- **Type**: typing.Optional[str]

### rateCards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.UsageBasedRateCardItemTypeDef]]

### type
- **Type**: typing.Optional[str]


# UsageBasedRateCardItemTypeDef

### rateCard
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement_classes.RateCardItemTypeDef]]


# ValidityTermTypeDef

### agreementDuration
- **Type**: typing.Optional[str]

### agreementEndDate
- **Type**: typing.Optional[datetime.datetime]

### agreementStartDate
- **Type**: typing.Optional[datetime.datetime]

### type
- **Type**: typing.Optional[str]



# Marketplace Agreement Marketplace Agreement Classes

# AcceptedTerm

### byolPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ByolPricingTerm]

### configurableUpfrontPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ConfigurableUpfrontPricingTerm]

### fixedUpfrontPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.FixedUpfrontPricingTerm]

### freeTrialPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.FreeTrialPricingTerm]

### legalTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.LegalTerm]

### paymentScheduleTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.PaymentScheduleTerm]

### recurringPaymentTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.RecurringPaymentTerm]

### renewalTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.RenewalTerm]

### supportTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.SupportTerm]

### usageBasedPricingTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.UsageBasedPricingTerm]

### validityTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ValidityTerm]


# Acceptor

### accountId
- **Type**: typing.Optional[str]


# AgreementViewSummary

### acceptanceTime
- **Type**: typing.Optional[datetime.datetime]

### acceptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Acceptor]

### agreementId
- **Type**: typing.Optional[str]

### agreementType
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### proposalSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ProposalSummary]

### proposer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Proposer]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ARCHIVED', 'CANCELLED', 'EXPIRED', 'RENEWED', 'REPLACED', 'ROLLED_BACK', 'SUPERSEDED', 'TERMINATED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByolPricingTerm

### type
- **Type**: typing.Optional[str]


# ConfigurableUpfrontPricingTerm

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ConfigurableUpfrontPricingTermConfiguration]

### currencyCode
- **Type**: typing.Optional[str]

### rateCards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ConfigurableUpfrontRateCardItem]]

### type
- **Type**: typing.Optional[str]


# ConfigurableUpfrontPricingTermConfiguration

### dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Dimension]
- **Required**: Yes

### selectorValue
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurableUpfrontRateCardItem

### constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Constraints]

### rateCard
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.RateCardItem]]

### selector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Selector]


# Constraints

### multipleDimensionSelection
- **Type**: typing.Optional[str]

### quantityConfiguration
- **Type**: typing.Optional[str]


# DescribeAgreementInput

### agreementId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgreementOutput

### acceptanceTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### acceptor
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Acceptor'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.EstimatedCharges'>
- **Required**: Yes

### proposalSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ProposalSummary'>
- **Required**: Yes

### proposer
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Proposer'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'ARCHIVED', 'CANCELLED', 'EXPIRED', 'RENEWED', 'REPLACED', 'ROLLED_BACK', 'SUPERSEDED', 'TERMINATED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ResponseMetadata'>
- **Required**: Yes


# Dimension

### dimensionKey
- **Type**: <class 'str'>
- **Required**: Yes

### dimensionValue
- **Type**: <class 'int'>
- **Required**: Yes


# DocumentItem

### type
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# EstimatedCharges

### agreementValue
- **Type**: typing.Optional[str]

### currencyCode
- **Type**: typing.Optional[str]


# Filter

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# FixedUpfrontPricingTerm

### currencyCode
- **Type**: typing.Optional[str]

### duration
- **Type**: typing.Optional[str]

### grants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.GrantItem]]

### price
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# FreeTrialPricingTerm

### duration
- **Type**: typing.Optional[str]

### grants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.GrantItem]]

### type
- **Type**: typing.Optional[str]


# GetAgreementTermsInput

### agreementId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetAgreementTermsOutput

### acceptedTerms
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.AcceptedTerm]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GrantItem

### dimensionKey
- **Type**: typing.Optional[str]

### maxQuantity
- **Type**: typing.Optional[int]


# LegalTerm

### documents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.DocumentItem]]

### type
- **Type**: typing.Optional[str]


# PaymentScheduleTerm

### currencyCode
- **Type**: typing.Optional[str]

### schedule
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ScheduleItem]]

### type
- **Type**: typing.Optional[str]


# ProposalSummary

### offerId
- **Type**: typing.Optional[str]

### resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Resource]]


# Proposer

### accountId
- **Type**: typing.Optional[str]


# RateCardItem

### dimensionKey
- **Type**: typing.Optional[str]

### price
- **Type**: typing.Optional[str]


# RecurringPaymentTerm

### billingPeriod
- **Type**: typing.Optional[str]

### currencyCode
- **Type**: typing.Optional[str]

### price
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# RenewalTerm

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.RenewalTermConfiguration]

### type
- **Type**: typing.Optional[str]


# RenewalTermConfiguration

### enableAutoRenew
- **Type**: <class 'bool'>
- **Required**: Yes


# Resource

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# ResponseMetadata

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


# ScheduleItem

### chargeAmount
- **Type**: typing.Optional[str]

### chargeDate
- **Type**: typing.Optional[datetime.datetime]


# SearchAgreementsInput

### catalog
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Filter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sort
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.Sort]


# SearchAgreementsOutput

### agreementViewSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.AgreementViewSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Selector

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# Sort

### sortBy
- **Type**: typing.Optional[str]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]


# SupportTerm

### refundPolicy
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# UsageBasedPricingTerm

### currencyCode
- **Type**: typing.Optional[str]

### rateCards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.UsageBasedRateCardItem]]

### type
- **Type**: typing.Optional[str]


# UsageBasedRateCardItem

### rateCard
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.marketplace_agreement.marketplace_agreement_classes.RateCardItem]]


# ValidityTerm

### agreementDuration
- **Type**: typing.Optional[str]

### agreementEndDate
- **Type**: typing.Optional[datetime.datetime]

### agreementStartDate
- **Type**: typing.Optional[datetime.datetime]

### type
- **Type**: typing.Optional[str]



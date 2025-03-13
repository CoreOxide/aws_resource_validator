# Trustedadvisor Classes

# AccountRecommendationLifecycleSummaryTypeDef

### accountId
- **Type**: typing.Optional[str]

### accountRecommendationArn
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleStage
- **Type**: typing.Optional[typing.Literal['dismissed', 'in_progress', 'pending_response', 'resolved']]

### updateReason
- **Type**: typing.Optional[str]

### updateReasonCode
- **Type**: typing.Optional[typing.Literal['low_priority', 'non_critical_account', 'not_applicable', 'other', 'other_methods_available', 'temporary_account', 'valid_business_case']]

### updatedOnBehalfOf
- **Type**: typing.Optional[str]

### updatedOnBehalfOfJobTitle
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchUpdateRecommendationResourceExclusionRequestTypeDef

### recommendationResourceExclusions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourceExclusionTypeDef]
- **Required**: Yes


# BatchUpdateRecommendationResourceExclusionResponseTypeDef

### batchUpdateRecommendationResourceExclusionErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.UpdateRecommendationResourceExclusionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CheckSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOrganizationRecommendationRequestTypeDef

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetOrganizationRecommendationResponseTypeDef

### organizationRecommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.OrganizationRecommendationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecommendationRequestTypeDef

### recommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecommendationResponseTypeDef

### recommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChecksRequestPaginateTypeDef

### awsService
- **Type**: typing.Optional[str]

### language
- **Type**: typing.Optional[typing.Literal['de', 'en', 'es', 'fr', 'id', 'it', 'ja', 'ko', 'pt_BR', 'zh', 'zh_TW']]

### pillar
- **Type**: typing.Optional[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]

### source
- **Type**: typing.Optional[typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfigTypeDef]


# ListChecksRequestTypeDef

### awsService
- **Type**: typing.Optional[str]

### language
- **Type**: typing.Optional[typing.Literal['de', 'en', 'es', 'fr', 'id', 'it', 'ja', 'ko', 'pt_BR', 'zh', 'zh_TW']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### pillar
- **Type**: typing.Optional[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]

### source
- **Type**: typing.Optional[typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']]


# ListChecksResponseTypeDef

### checkSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.CheckSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationRecommendationAccountsRequestPaginateTypeDef

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### affectedAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfigTypeDef]


# ListOrganizationRecommendationAccountsRequestTypeDef

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### affectedAccountId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationRecommendationAccountsResponseTypeDef

### accountRecommendationLifecycleSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.AccountRecommendationLifecycleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationRecommendationResourcesRequestPaginateTypeDef

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### affectedAccountId
- **Type**: typing.Optional[str]

### exclusionStatus
- **Type**: typing.Optional[typing.Literal['excluded', 'included']]

### regionCode
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['error', 'ok', 'warning']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfigTypeDef]


# ListOrganizationRecommendationResourcesRequestTypeDef

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### affectedAccountId
- **Type**: typing.Optional[str]

### exclusionStatus
- **Type**: typing.Optional[typing.Literal['excluded', 'included']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### regionCode
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['error', 'ok', 'warning']]


# ListOrganizationRecommendationResourcesResponseTypeDef

### organizationRecommendationResourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.OrganizationRecommendationResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationRecommendationsResponseTypeDef

### organizationRecommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.OrganizationRecommendationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationResourcesRequestPaginateTypeDef

### recommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### exclusionStatus
- **Type**: typing.Optional[typing.Literal['excluded', 'included']]

### regionCode
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['error', 'ok', 'warning']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfigTypeDef]


# ListRecommendationResourcesRequestTypeDef

### recommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### exclusionStatus
- **Type**: typing.Optional[typing.Literal['excluded', 'included']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### regionCode
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['error', 'ok', 'warning']]


# ListRecommendationResourcesResponseTypeDef

### recommendationResourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationsResponseTypeDef

### recommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# OrganizationRecommendationResourceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrganizationRecommendationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrganizationRecommendationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RecommendationCostOptimizingAggregatesTypeDef

### estimatedMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes

### estimatedPercentMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes


# RecommendationPillarSpecificAggregatesTypeDef

### costOptimizing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationCostOptimizingAggregatesTypeDef]


# RecommendationResourceExclusionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### isExcluded
- **Type**: <class 'bool'>
- **Required**: Yes


# RecommendationResourceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationResourcesAggregatesTypeDef

### errorCount
- **Type**: <class 'int'>
- **Required**: Yes

### okCount
- **Type**: <class 'int'>
- **Required**: Yes

### warningCount
- **Type**: <class 'int'>
- **Required**: Yes


# RecommendationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationTypeDef

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


# UpdateOrganizationRecommendationLifecycleRequestTypeDef

### lifecycleStage
- **Type**: typing.Literal['dismissed', 'in_progress', 'pending_response', 'resolved']
- **Required**: Yes

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### updateReason
- **Type**: typing.Optional[str]

### updateReasonCode
- **Type**: typing.Optional[typing.Literal['low_priority', 'non_critical_account', 'not_applicable', 'other', 'other_methods_available', 'temporary_account', 'valid_business_case']]


# UpdateRecommendationLifecycleRequestTypeDef

### lifecycleStage
- **Type**: typing.Literal['dismissed', 'in_progress', 'pending_response', 'resolved']
- **Required**: Yes

### recommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### updateReason
- **Type**: typing.Optional[str]

### updateReasonCode
- **Type**: typing.Optional[typing.Literal['low_priority', 'non_critical_account', 'not_applicable', 'other', 'other_methods_available', 'temporary_account', 'valid_business_case']]


# UpdateRecommendationResourceExclusionErrorTypeDef

### arn
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]



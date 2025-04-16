# Trustedadvisor Classes

# AccountRecommendationLifecycleSummary

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

# BatchUpdateRecommendationResourceExclusionRequest

### recommendationResourceExclusions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourceExclusion]
- **Required**: Yes


# BatchUpdateRecommendationResourceExclusionResponse

### batchUpdateRecommendationResourceExclusionErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.UpdateRecommendationResourceExclusionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# CheckSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# GetOrganizationRecommendationRequest

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetOrganizationRecommendationResponse

### organizationRecommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.OrganizationRecommendation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecommendationRequest

### recommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecommendationResponse

### recommendation
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.Recommendation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes


# ListChecksRequest

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


# ListChecksRequestPaginate

### awsService
- **Type**: typing.Optional[str]

### language
- **Type**: typing.Optional[typing.Literal['de', 'en', 'es', 'fr', 'id', 'it', 'ja', 'ko', 'pt_BR', 'zh', 'zh_TW']]

### pillar
- **Type**: typing.Optional[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]

### source
- **Type**: typing.Optional[typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfig]


# ListChecksResponse

### checkSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.CheckSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationRecommendationAccountsRequest

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### affectedAccountId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationRecommendationAccountsRequestPaginate

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### affectedAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfig]


# ListOrganizationRecommendationAccountsResponse

### accountRecommendationLifecycleSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.AccountRecommendationLifecycleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationRecommendationResourcesRequest

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


# ListOrganizationRecommendationResourcesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfig]


# ListOrganizationRecommendationResourcesResponse

### organizationRecommendationResourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.OrganizationRecommendationResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationRecommendationsResponse

### organizationRecommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.OrganizationRecommendationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationResourcesRequest

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


# ListRecommendationResourcesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfig]


# ListRecommendationResourcesResponse

### recommendationResourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendationsResponse

### recommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# OrganizationRecommendation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrganizationRecommendationResourceSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrganizationRecommendationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Recommendation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationCostOptimizingAggregates

### estimatedMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes

### estimatedPercentMonthlySavings
- **Type**: <class 'float'>
- **Required**: Yes


# RecommendationPillarSpecificAggregates

### costOptimizing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationCostOptimizingAggregates]


# RecommendationResourceExclusion

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### isExcluded
- **Type**: <class 'bool'>
- **Required**: Yes


# RecommendationResourceSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationResourcesAggregates

### errorCount
- **Type**: <class 'int'>
- **Required**: Yes

### okCount
- **Type**: <class 'int'>
- **Required**: Yes

### warningCount
- **Type**: <class 'int'>
- **Required**: Yes


# RecommendationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# UpdateOrganizationRecommendationLifecycleRequest

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


# UpdateRecommendationLifecycleRequest

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


# UpdateRecommendationResourceExclusionError

### arn
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]



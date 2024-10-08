# Pydantic Models in trustedadvisor_classes

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

# BatchUpdateRecommendationResourceExclusionRequestRequestTypeDef

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

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### awsServices
- **Type**: typing.List[str]
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pillars
- **Type**: typing.List[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]
- **Required**: Yes

### source
- **Type**: typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOrganizationRecommendationRequestRequestTypeDef

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


# GetRecommendationRequestRequestTypeDef

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


# ListChecksRequestListChecksPaginateTypeDef

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


# ListChecksRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOrganizationRecommendationAccountsRequestListOrganizationRecommendationAccountsPaginateTypeDef

### organizationRecommendationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### affectedAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfigTypeDef]


# ListOrganizationRecommendationAccountsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOrganizationRecommendationResourcesRequestListOrganizationRecommendationResourcesPaginateTypeDef

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


# ListOrganizationRecommendationResourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### organizationRecommendationResourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.OrganizationRecommendationResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOrganizationRecommendationsRequestListOrganizationRecommendationsPaginateTypeDef

### afterLastUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### awsService
- **Type**: typing.Optional[str]

### beforeLastUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### checkIdentifier
- **Type**: typing.Optional[str]

### pillar
- **Type**: typing.Optional[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]

### source
- **Type**: typing.Optional[typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']]

### status
- **Type**: typing.Optional[typing.Literal['error', 'ok', 'warning']]

### type
- **Type**: typing.Optional[typing.Literal['priority', 'standard']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfigTypeDef]


# ListOrganizationRecommendationsRequestRequestTypeDef

### afterLastUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### awsService
- **Type**: typing.Optional[str]

### beforeLastUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### checkIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### pillar
- **Type**: typing.Optional[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]

### source
- **Type**: typing.Optional[typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']]

### status
- **Type**: typing.Optional[typing.Literal['error', 'ok', 'warning']]

### type
- **Type**: typing.Optional[typing.Literal['priority', 'standard']]


# ListOrganizationRecommendationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### organizationRecommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.OrganizationRecommendationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendationResourcesRequestListRecommendationResourcesPaginateTypeDef

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


# ListRecommendationResourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationResourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendationsRequestListRecommendationsPaginateTypeDef

### afterLastUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### awsService
- **Type**: typing.Optional[str]

### beforeLastUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### checkIdentifier
- **Type**: typing.Optional[str]

### pillar
- **Type**: typing.Optional[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]

### source
- **Type**: typing.Optional[typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']]

### status
- **Type**: typing.Optional[typing.Literal['error', 'ok', 'warning']]

### type
- **Type**: typing.Optional[typing.Literal['priority', 'standard']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.PaginatorConfigTypeDef]


# ListRecommendationsRequestRequestTypeDef

### afterLastUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### awsService
- **Type**: typing.Optional[str]

### beforeLastUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### checkIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### pillar
- **Type**: typing.Optional[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]

### source
- **Type**: typing.Optional[typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']]

### status
- **Type**: typing.Optional[typing.Literal['error', 'ok', 'warning']]

### type
- **Type**: typing.Optional[typing.Literal['priority', 'standard']]


# ListRecommendationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OrganizationRecommendationResourceSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### awsResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### recommendationArn
- **Type**: <class 'str'>
- **Required**: Yes

### regionCode
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['error', 'ok', 'warning']
- **Required**: Yes

### accountId
- **Type**: typing.Optional[str]

### exclusionStatus
- **Type**: typing.Optional[typing.Literal['excluded', 'included']]


# OrganizationRecommendationSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pillars
- **Type**: typing.List[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]
- **Required**: Yes

### resourcesAggregates
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourcesAggregatesTypeDef'>
- **Required**: Yes

### source
- **Type**: typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']
- **Required**: Yes

### status
- **Type**: typing.Literal['error', 'ok', 'warning']
- **Required**: Yes

### type
- **Type**: typing.Literal['priority', 'standard']
- **Required**: Yes

### awsServices
- **Type**: typing.Optional[typing.List[str]]

### checkArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleStage
- **Type**: typing.Optional[typing.Literal['dismissed', 'in_progress', 'pending_response', 'resolved']]

### pillarSpecificAggregates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationPillarSpecificAggregatesTypeDef]


# OrganizationRecommendationTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pillars
- **Type**: typing.List[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]
- **Required**: Yes

### resourcesAggregates
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourcesAggregatesTypeDef'>
- **Required**: Yes

### source
- **Type**: typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']
- **Required**: Yes

### status
- **Type**: typing.Literal['error', 'ok', 'warning']
- **Required**: Yes

### type
- **Type**: typing.Literal['priority', 'standard']
- **Required**: Yes

### awsServices
- **Type**: typing.Optional[typing.List[str]]

### checkArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleStage
- **Type**: typing.Optional[typing.Literal['dismissed', 'in_progress', 'pending_response', 'resolved']]

### pillarSpecificAggregates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationPillarSpecificAggregatesTypeDef]

### resolvedAt
- **Type**: typing.Optional[datetime.datetime]

### updateReason
- **Type**: typing.Optional[str]

### updateReasonCode
- **Type**: typing.Optional[typing.Literal['low_priority', 'non_critical_account', 'not_applicable', 'other', 'other_methods_available', 'temporary_account', 'valid_business_case']]

### updatedOnBehalfOf
- **Type**: typing.Optional[str]

### updatedOnBehalfOfJobTitle
- **Type**: typing.Optional[str]


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

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### awsResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### recommendationArn
- **Type**: <class 'str'>
- **Required**: Yes

### regionCode
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['error', 'ok', 'warning']
- **Required**: Yes

### exclusionStatus
- **Type**: typing.Optional[typing.Literal['excluded', 'included']]


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

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pillars
- **Type**: typing.List[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]
- **Required**: Yes

### resourcesAggregates
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourcesAggregatesTypeDef'>
- **Required**: Yes

### source
- **Type**: typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']
- **Required**: Yes

### status
- **Type**: typing.Literal['error', 'ok', 'warning']
- **Required**: Yes

### type
- **Type**: typing.Literal['priority', 'standard']
- **Required**: Yes

### awsServices
- **Type**: typing.Optional[typing.List[str]]

### checkArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleStage
- **Type**: typing.Optional[typing.Literal['dismissed', 'in_progress', 'pending_response', 'resolved']]

### pillarSpecificAggregates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationPillarSpecificAggregatesTypeDef]


# RecommendationTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pillars
- **Type**: typing.List[typing.Literal['cost_optimizing', 'fault_tolerance', 'operational_excellence', 'performance', 'security', 'service_limits']]
- **Required**: Yes

### resourcesAggregates
- **Type**: <class 'aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationResourcesAggregatesTypeDef'>
- **Required**: Yes

### source
- **Type**: typing.Literal['aws_config', 'compute_optimizer', 'cost_explorer', 'lse', 'manual', 'pse', 'rds', 'resilience', 'resilience_hub', 'security_hub', 'stir', 'ta_check', 'well_architected']
- **Required**: Yes

### status
- **Type**: typing.Literal['error', 'ok', 'warning']
- **Required**: Yes

### type
- **Type**: typing.Literal['priority', 'standard']
- **Required**: Yes

### awsServices
- **Type**: typing.Optional[typing.List[str]]

### checkArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleStage
- **Type**: typing.Optional[typing.Literal['dismissed', 'in_progress', 'pending_response', 'resolved']]

### pillarSpecificAggregates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.trustedadvisor_classes.RecommendationPillarSpecificAggregatesTypeDef]

### resolvedAt
- **Type**: typing.Optional[datetime.datetime]

### updateReason
- **Type**: typing.Optional[str]

### updateReasonCode
- **Type**: typing.Optional[typing.Literal['low_priority', 'non_critical_account', 'not_applicable', 'other', 'other_methods_available', 'temporary_account', 'valid_business_case']]

### updatedOnBehalfOf
- **Type**: typing.Optional[str]

### updatedOnBehalfOfJobTitle
- **Type**: typing.Optional[str]


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


# UpdateOrganizationRecommendationLifecycleRequestRequestTypeDef

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


# UpdateRecommendationLifecycleRequestRequestTypeDef

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



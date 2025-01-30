# route53_recovery_readiness_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CellOutputTypeDef

### CellArn
- **Type**: <class 'str'>
- **Required**: Yes

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### ParentReadinessScopes
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCellRequestRequestTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCellResponseTypeDef

### CellArn
- **Type**: <class 'str'>
- **Required**: Yes

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### ParentReadinessScopes
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCrossAccountAuthorizationRequestRequestTypeDef

### CrossAccountAuthorization
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCrossAccountAuthorizationResponseTypeDef

### CrossAccountAuthorization
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReadinessCheckRequestRequestTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateReadinessCheckResponseTypeDef

### ReadinessCheckArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSet
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRecoveryGroupRequestRequestTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRecoveryGroupResponseTypeDef

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### RecoveryGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceSetRequestRequestTypeDef

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateResourceSetResponseTypeDef

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DNSTargetResourceTypeDef

### DomainName
- **Type**: typing.Optional[str]

### HostedZoneArn
- **Type**: typing.Optional[str]

### RecordSetId
- **Type**: typing.Optional[str]

### RecordType
- **Type**: typing.Optional[str]

### TargetResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.TargetResourceTypeDef]


# DeleteCellRequestRequestTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCrossAccountAuthorizationRequestRequestTypeDef

### CrossAccountAuthorization
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReadinessCheckRequestRequestTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecoveryGroupRequestRequestTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceSetRequestRequestTypeDef

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchitectureRecommendationsRequestRequestTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetArchitectureRecommendationsResponseTypeDef

### LastAuditTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.RecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCellReadinessSummaryRequestGetCellReadinessSummaryPaginateTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# GetCellReadinessSummaryRequestRequestTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCellReadinessSummaryResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ReadinessCheckSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCellRequestRequestTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCellResponseTypeDef

### CellArn
- **Type**: <class 'str'>
- **Required**: Yes

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### ParentReadinessScopes
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReadinessCheckRequestRequestTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadinessCheckResourceStatusRequestGetReadinessCheckResourceStatusPaginateTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# GetReadinessCheckResourceStatusRequestRequestTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetReadinessCheckResourceStatusResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.RuleResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReadinessCheckResponseTypeDef

### ReadinessCheckArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSet
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReadinessCheckStatusRequestGetReadinessCheckStatusPaginateTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# GetReadinessCheckStatusRequestRequestTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetReadinessCheckStatusResponseTypeDef

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.MessageTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecoveryGroupReadinessSummaryRequestGetRecoveryGroupReadinessSummaryPaginateTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# GetRecoveryGroupReadinessSummaryRequestRequestTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetRecoveryGroupReadinessSummaryResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ReadinessCheckSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecoveryGroupRequestRequestTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecoveryGroupResponseTypeDef

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### RecoveryGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceSetRequestRequestTypeDef

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceSetResponseTypeDef

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCellsRequestListCellsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListCellsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCellsResponseTypeDef

### Cells
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.CellOutputTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCrossAccountAuthorizationsRequestListCrossAccountAuthorizationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListCrossAccountAuthorizationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAuthorizationsResponseTypeDef

### CrossAccountAuthorizations
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReadinessChecksRequestListReadinessChecksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListReadinessChecksRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReadinessChecksResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ReadinessCheckOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecoveryGroupsRequestListRecoveryGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListRecoveryGroupsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryGroupsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.RecoveryGroupOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceSetsRequestListResourceSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListResourceSetsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetsResponsePaginatorTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceSetOutputPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceSetsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceSetOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRulesOutputTypeDef

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### RuleDescription
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# ListRulesRequestListRulesPaginateTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListRulesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ListRulesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ListRulesOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourcesRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourcesResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MessageTypeDef

### MessageText
- **Type**: typing.Optional[str]


# NLBResourceTypeDef

### Arn
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# R53ResourceRecordTypeDef

### DomainName
- **Type**: typing.Optional[str]

### RecordSetId
- **Type**: typing.Optional[str]


# ReadinessCheckOutputTypeDef

### ReadinessCheckArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSet
- **Type**: <class 'str'>
- **Required**: Yes

### ReadinessCheckName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ReadinessCheckSummaryTypeDef

### Readiness
- **Type**: typing.Optional[typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']]

### ReadinessCheckName
- **Type**: typing.Optional[str]


# RecommendationTypeDef

### RecommendationText
- **Type**: <class 'str'>
- **Required**: Yes


# RecoveryGroupOutputTypeDef

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### RecoveryGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ResourcePaginatorTypeDef

### ComponentId
- **Type**: typing.Optional[str]

### DnsTargetResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.DNSTargetResourceTypeDef]

### ReadinessScopes
- **Type**: typing.Optional[typing.List[str]]

### ResourceArn
- **Type**: typing.Optional[str]


# ResourceResultTypeDef

### LastCheckedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### ComponentId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# ResourceSetOutputPaginatorTypeDef

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourcePaginatorTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ResourceSetOutputTypeDef

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ResourceTypeDef

### ComponentId
- **Type**: typing.Optional[str]

### DnsTargetResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.DNSTargetResourceTypeDef]

### ReadinessScopes
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceArn
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


# RuleResultTypeDef

### LastCheckedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.MessageTypeDef]
- **Required**: Yes

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetResourceTypeDef

### NLBResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.NLBResourceTypeDef]

### R53Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.R53ResourceRecordTypeDef]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCellRequestRequestTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCellResponseTypeDef

### CellArn
- **Type**: <class 'str'>
- **Required**: Yes

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### ParentReadinessScopes
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReadinessCheckRequestRequestTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateReadinessCheckResponseTypeDef

### ReadinessCheckArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSet
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRecoveryGroupRequestRequestTypeDef

### Cells
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRecoveryGroupResponseTypeDef

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### RecoveryGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResourceSetRequestRequestTypeDef

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceTypeDef]
- **Required**: Yes


# UpdateResourceSetResponseTypeDef

### ResourceSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



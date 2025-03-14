# Route53 Recovery Readiness Classes

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


# CreateCellRequestTypeDef

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


# CreateCrossAccountAuthorizationRequestTypeDef

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


# CreateReadinessCheckRequestTypeDef

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


# CreateRecoveryGroupRequestTypeDef

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


# CreateResourceSetRequestTypeDef

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceUnionTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceOutputTypeDef]
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


# DeleteCellRequestTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCrossAccountAuthorizationRequestTypeDef

### CrossAccountAuthorization
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReadinessCheckRequestTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecoveryGroupRequestTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceSetRequestTypeDef

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchitectureRecommendationsRequestTypeDef

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

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.RecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCellReadinessSummaryRequestPaginateTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# GetCellReadinessSummaryRequestTypeDef

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCellReadinessSummaryResponseTypeDef

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ReadinessCheckSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCellRequestTypeDef

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


# GetReadinessCheckRequestTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadinessCheckResourceStatusRequestPaginateTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# GetReadinessCheckResourceStatusRequestTypeDef

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

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.RuleResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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


# GetReadinessCheckStatusRequestPaginateTypeDef

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# GetReadinessCheckStatusRequestTypeDef

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

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRecoveryGroupReadinessSummaryRequestPaginateTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# GetRecoveryGroupReadinessSummaryRequestTypeDef

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetRecoveryGroupReadinessSummaryResponseTypeDef

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ReadinessCheckSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRecoveryGroupRequestTypeDef

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


# GetResourceSetRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceOutputTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCellsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListCellsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCellsResponseTypeDef

### Cells
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.CellOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAuthorizationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListCrossAccountAuthorizationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAuthorizationsResponseTypeDef

### CrossAccountAuthorizations
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReadinessChecksRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListReadinessChecksRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReadinessChecksResponseTypeDef

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ReadinessCheckOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListRecoveryGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryGroupsResponseTypeDef

### RecoveryGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.RecoveryGroupOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListResourceSetsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetsResponseTypeDef

### ResourceSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceSetOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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


# ListRulesRequestPaginateTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.PaginatorConfigTypeDef]


# ListRulesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ListRulesResponseTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ListRulesOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourcesRequestTypeDef

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


# ResourceOutputTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceOutputTypeDef]
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


# ResourceUnionTypeDef

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


# TagResourceRequestTypeDef

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


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCellRequestTypeDef

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


# UpdateReadinessCheckRequestTypeDef

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


# UpdateRecoveryGroupRequestTypeDef

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


# UpdateResourceSetRequestTypeDef

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceUnionTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResourceOutputTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



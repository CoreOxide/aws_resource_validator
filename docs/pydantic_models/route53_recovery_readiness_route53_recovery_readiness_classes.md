# Route53 Recovery Readiness Route53 Recovery Readiness Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CellOutput

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


# CreateCellRequest

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCellResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCrossAccountAuthorizationRequest

### CrossAccountAuthorization
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCrossAccountAuthorizationResponse

### CrossAccountAuthorization
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReadinessCheckRequest

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateReadinessCheckResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRecoveryGroupRequest

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRecoveryGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceSetRequest

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.Resource, aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResourceOutput]]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateResourceSetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResourceOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# DNSTargetResource

### DomainName
- **Type**: typing.Optional[str]

### HostedZoneArn
- **Type**: typing.Optional[str]

### RecordSetId
- **Type**: typing.Optional[str]

### RecordType
- **Type**: typing.Optional[str]

### TargetResource
- **Type**: <class 'NoneType'>


# DeleteCellRequest

### CellName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCrossAccountAuthorizationRequest

### CrossAccountAuthorization
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReadinessCheckRequest

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecoveryGroupRequest

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceSetRequest

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetArchitectureRecommendationsRequest

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetArchitectureRecommendationsResponse

### LastAuditTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.Recommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCellReadinessSummaryRequest

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetCellReadinessSummaryRequestPaginate

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# GetCellReadinessSummaryResponse

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ReadinessCheckSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetCellRequest

### CellName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCellResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetReadinessCheckRequest

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes


# GetReadinessCheckResourceStatusRequest

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


# GetReadinessCheckResourceStatusRequestPaginate

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# GetReadinessCheckResourceStatusResponse

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.RuleResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetReadinessCheckResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetReadinessCheckStatusRequest

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetReadinessCheckStatusRequestPaginate

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# GetReadinessCheckStatusResponse

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.Message]
- **Required**: Yes

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResourceResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRecoveryGroupReadinessSummaryRequest

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetRecoveryGroupReadinessSummaryRequestPaginate

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# GetRecoveryGroupReadinessSummaryResponse

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ReadinessCheckSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRecoveryGroupRequest

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecoveryGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceSetRequest

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceSetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResourceOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# ListCellsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCellsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# ListCellsResponse

### Cells
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.CellOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAuthorizationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCrossAccountAuthorizationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# ListCrossAccountAuthorizationsResponse

### CrossAccountAuthorizations
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReadinessChecksRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListReadinessChecksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# ListReadinessChecksResponse

### ReadinessChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ReadinessCheckOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRecoveryGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# ListRecoveryGroupsResponse

### RecoveryGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.RecoveryGroupOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# ListResourceSetsResponse

### ResourceSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResourceSetOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRulesOutput

### ResourceType
- **Type**: <class 'str'>
- **Required**: Yes

### RuleDescription
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# ListRulesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ListRulesRequestPaginate

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.PaginatorConfig]


# ListRulesResponse

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ListRulesOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourcesRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourcesResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# Message

### MessageText
- **Type**: typing.Optional[str]


# NLBResource

### Arn
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# R53ResourceRecord

### DomainName
- **Type**: typing.Optional[str]

### RecordSetId
- **Type**: typing.Optional[str]


# ReadinessCheckOutput

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


# ReadinessCheckSummary

### Readiness
- **Type**: typing.Optional[typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']]

### ReadinessCheckName
- **Type**: typing.Optional[str]


# Recommendation

### RecommendationText
- **Type**: <class 'str'>
- **Required**: Yes


# RecoveryGroupOutput

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


# Resource

### ComponentId
- **Type**: typing.Optional[str]

### DnsTargetResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.DNSTargetResource]

### ReadinessScopes
- **Type**: typing.Optional[typing.List[str]]

### ResourceArn
- **Type**: typing.Optional[str]


# ResourceOutput

### ComponentId
- **Type**: typing.Optional[str]

### DnsTargetResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.DNSTargetResource]

### ReadinessScopes
- **Type**: typing.Optional[typing.List[str]]

### ResourceArn
- **Type**: typing.Optional[str]


# ResourceResult

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


# ResourceSetOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResourceOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# RuleResult

### LastCheckedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.Message]
- **Required**: Yes

### Readiness
- **Type**: typing.Literal['NOT_AUTHORIZED', 'NOT_READY', 'READY', 'UNKNOWN']
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TargetResource

### NLBResource
- **Type**: <class 'NoneType'>

### R53Resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.R53ResourceRecord]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCellRequest

### CellName
- **Type**: <class 'str'>
- **Required**: Yes

### Cells
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCellResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReadinessCheckRequest

### ReadinessCheckName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateReadinessCheckResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRecoveryGroupRequest

### Cells
- **Type**: typing.List[str]
- **Required**: Yes

### RecoveryGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRecoveryGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResourceSetRequest

### ResourceSetName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceSetType
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.Resource, aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResourceOutput]]
- **Required**: Yes


# UpdateResourceSetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResourceOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_readiness.route53_recovery_readiness_classes.ResponseMetadata'>
- **Required**: Yes



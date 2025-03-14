# Amp Classes

# AlertManagerDefinitionDescriptionTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### data
- **Type**: <class 'bytes'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.AlertManagerDefinitionStatusTypeDef'>
- **Required**: Yes


# AlertManagerDefinitionStatusTypeDef

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# AmpConfigurationTypeDef

### workspaceArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAlertManagerDefinitionRequestTypeDef

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.BlobTypeDef'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateAlertManagerDefinitionResponseTypeDef

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.AlertManagerDefinitionStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoggingConfigurationRequestTypeDef

### logGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateLoggingConfigurationResponseTypeDef

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.LoggingConfigurationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleGroupsNamespaceRequestTypeDef

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.BlobTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRuleGroupsNamespaceResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceStatusTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateScraperRequestTypeDef

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.DestinationTypeDef'>
- **Required**: Yes

### scrapeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScrapeConfigurationUnionTypeDef'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceUnionTypeDef'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### roleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.RoleConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateScraperResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatusTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspaceRequestTypeDef

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateWorkspaceResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.WorkspaceStatusTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAlertManagerDefinitionRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteLoggingConfigurationRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteRuleGroupsNamespaceRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteScraperRequestTypeDef

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteScraperResponseTypeDef

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkspaceRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DescribeAlertManagerDefinitionRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlertManagerDefinitionResponseTypeDef

### alertManagerDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.AlertManagerDefinitionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoggingConfigurationRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoggingConfigurationResponseTypeDef

### loggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.LoggingConfigurationMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRuleGroupsNamespaceRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRuleGroupsNamespaceResponseTypeDef

### ruleGroupsNamespace
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeScraperRequestTypeDef

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScraperRequestWaitExtraTypeDef

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.WaiterConfigTypeDef]


# DescribeScraperRequestWaitTypeDef

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.WaiterConfigTypeDef]


# DescribeScraperResponseTypeDef

### scraper
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkspaceRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceRequestWaitExtraTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.WaiterConfigTypeDef]


# DescribeWorkspaceRequestWaitTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.WaiterConfigTypeDef]


# DescribeWorkspaceResponseTypeDef

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.WorkspaceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

### ampConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.AmpConfigurationTypeDef]


# EksConfigurationOutputTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# EksConfigurationTypeDef

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDefaultScraperConfigurationResponseTypeDef

### configuration
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRuleGroupsNamespacesRequestPaginateTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfigTypeDef]


# ListRuleGroupsNamespacesRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListRuleGroupsNamespacesResponseTypeDef

### ruleGroupsNamespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScrapersRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfigTypeDef]


# ListScrapersRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListScrapersResponseTypeDef

### scrapers
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.ScraperSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkspacesRequestPaginateTypeDef

### alias
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfigTypeDef]


# ListWorkspacesRequestTypeDef

### alias
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesResponseTypeDef

### workspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.WorkspaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LoggingConfigurationMetadataTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### logGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.LoggingConfigurationStatusTypeDef'>
- **Required**: Yes

### workspace
- **Type**: <class 'str'>
- **Required**: Yes


# LoggingConfigurationStatusTypeDef

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutAlertManagerDefinitionRequestTypeDef

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.BlobTypeDef'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PutAlertManagerDefinitionResponseTypeDef

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.AlertManagerDefinitionStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRuleGroupsNamespaceRequestTypeDef

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.BlobTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PutRuleGroupsNamespaceResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceStatusTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RoleConfigurationTypeDef

### sourceRoleArn
- **Type**: typing.Optional[str]

### targetRoleArn
- **Type**: typing.Optional[str]


# RuleGroupsNamespaceDescriptionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### data
- **Type**: <class 'bytes'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceStatusTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RuleGroupsNamespaceStatusTypeDef

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# RuleGroupsNamespaceSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceStatusTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ScrapeConfigurationOutputTypeDef

### configurationBlob
- **Type**: typing.Optional[bytes]


# ScrapeConfigurationTypeDef

### configurationBlob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.BlobTypeDef]


# ScrapeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScraperDescriptionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.DestinationTypeDef'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### scrapeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScrapeConfigurationOutputTypeDef'>
- **Required**: Yes

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceOutputTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatusTypeDef'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### roleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.RoleConfigurationTypeDef]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ScraperStatusTypeDef

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'DELETION_FAILED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes


# ScraperSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.DestinationTypeDef'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceOutputTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatusTypeDef'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### roleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.RoleConfigurationTypeDef]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SourceOutputTypeDef

### eksConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.EksConfigurationOutputTypeDef]


# SourceTypeDef

### eksConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.EksConfigurationTypeDef]


# SourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLoggingConfigurationRequestTypeDef

### logGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateLoggingConfigurationResponseTypeDef

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.LoggingConfigurationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScraperRequestTypeDef

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.DestinationTypeDef]

### roleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.RoleConfigurationTypeDef]

### scrapeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.ScrapeConfigurationUnionTypeDef]


# UpdateScraperResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatusTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkspaceAliasRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkspaceDescriptionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.WorkspaceStatusTypeDef'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### prometheusEndpoint
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# WorkspaceStatusTypeDef

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'UPDATING']
- **Required**: Yes


# WorkspaceSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.WorkspaceStatusTypeDef'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]



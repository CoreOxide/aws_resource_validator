# amp_classes

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

# CreateAlertManagerDefinitionRequestRequestTypeDef

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# CreateLoggingConfigurationRequestRequestTypeDef

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


# CreateRuleGroupsNamespaceRequestRequestTypeDef

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# CreateScraperRequestRequestTypeDef

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.DestinationTypeDef'>
- **Required**: Yes

### scrapeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScrapeConfigurationTypeDef'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceTypeDef'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

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


# CreateWorkspaceRequestRequestTypeDef

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


# DeleteAlertManagerDefinitionRequestRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteLoggingConfigurationRequestRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteRuleGroupsNamespaceRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteScraperRequestRequestTypeDef

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


# DeleteWorkspaceRequestRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DescribeAlertManagerDefinitionRequestRequestTypeDef

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


# DescribeLoggingConfigurationRequestRequestTypeDef

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


# DescribeRuleGroupsNamespaceRequestRequestTypeDef

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


# DescribeScraperRequestRequestTypeDef

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScraperRequestScraperActiveWaitTypeDef

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.WaiterConfigTypeDef]


# DescribeScraperRequestScraperDeletedWaitTypeDef

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


# DescribeWorkspaceRequestRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceRequestWorkspaceActiveWaitTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.WaiterConfigTypeDef]


# DescribeWorkspaceRequestWorkspaceDeletedWaitTypeDef

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


# EksConfigurationPaginatorTypeDef

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


# ListRuleGroupsNamespacesRequestListRuleGroupsNamespacesPaginateTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfigTypeDef]


# ListRuleGroupsNamespacesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ruleGroupsNamespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListScrapersRequestListScrapersPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfigTypeDef]


# ListScrapersRequestRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListScrapersResponsePaginatorTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### scrapers
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.ScraperSummaryPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListScrapersResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### scrapers
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.ScraperSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListWorkspacesRequestListWorkspacesPaginateTypeDef

### alias
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfigTypeDef]


# ListWorkspacesRequestRequestTypeDef

### alias
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.WorkspaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# PutAlertManagerDefinitionRequestRequestTypeDef

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# PutRuleGroupsNamespaceRequestRequestTypeDef

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# ScrapeConfigurationTypeDef

### configurationBlob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScrapeConfigurationTypeDef'>
- **Required**: Yes

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatusTypeDef'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ScraperStatusTypeDef

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'DELETION_FAILED']
- **Required**: Yes


# ScraperSummaryPaginatorTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourcePaginatorTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatusTypeDef'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatusTypeDef'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SourcePaginatorTypeDef

### eksConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.EksConfigurationPaginatorTypeDef]


# SourceTypeDef

### eksConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.EksConfigurationTypeDef]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLoggingConfigurationRequestRequestTypeDef

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


# UpdateWorkspaceAliasRequestRequestTypeDef

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



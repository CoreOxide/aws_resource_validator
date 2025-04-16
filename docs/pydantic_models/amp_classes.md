# Amp Classes

# AlertManagerDefinitionDescription

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.AlertManagerDefinitionStatus'>
- **Required**: Yes


# AlertManagerDefinitionStatus

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# AmpConfiguration

### workspaceArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAlertManagerDefinitionRequest

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.Blob'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateAlertManagerDefinitionResponse

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.AlertManagerDefinitionStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoggingConfigurationRequest

### logGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateLoggingConfigurationResponse

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.LoggingConfigurationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleGroupsNamespaceRequest

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.Blob'>
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


# CreateRuleGroupsNamespaceResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceStatus'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateScraperRequest

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.Destination'>
- **Required**: Yes

### scrapeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScrapeConfigurationUnion'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceUnion'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### roleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.RoleConfiguration]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateScraperResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatus'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspaceRequest

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateWorkspaceResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.WorkspaceStatus'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAlertManagerDefinitionRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteLoggingConfigurationRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteRuleGroupsNamespaceRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteScraperRequest

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteScraperResponse

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DescribeAlertManagerDefinitionRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlertManagerDefinitionResponse

### alertManagerDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.AlertManagerDefinitionDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoggingConfigurationRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoggingConfigurationResponse

### loggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.LoggingConfigurationMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRuleGroupsNamespaceRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRuleGroupsNamespaceResponse

### ruleGroupsNamespace
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeScraperRequest

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScraperRequestWait

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeScraperRequestWaitExtra

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeScraperResponse

### scraper
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceRequestWait

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeWorkspaceRequestWaitExtra

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeWorkspaceResponse

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.WorkspaceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

### ampConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.AmpConfiguration]


# EksConfiguration

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# EksConfigurationOutput

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# GetDefaultScraperConfigurationResponse

### configuration
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# ListRuleGroupsNamespacesRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListRuleGroupsNamespacesRequestPaginate

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfig]


# ListRuleGroupsNamespacesResponse

### ruleGroupsNamespaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListScrapersRequest

### filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListScrapersRequestPaginate

### filters
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfig]


# ListScrapersResponse

### scrapers
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.ScraperSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# ListWorkspacesRequest

### alias
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesRequestPaginate

### alias
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.PaginatorConfig]


# ListWorkspacesResponse

### workspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.amp_classes.WorkspaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LoggingConfigurationMetadata

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.LoggingConfigurationStatus'>
- **Required**: Yes

### workspace
- **Type**: <class 'str'>
- **Required**: Yes


# LoggingConfigurationStatus

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutAlertManagerDefinitionRequest

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.Blob'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PutAlertManagerDefinitionResponse

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.AlertManagerDefinitionStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# PutRuleGroupsNamespaceRequest

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.Blob'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PutRuleGroupsNamespaceResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceStatus'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


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


# RoleConfiguration

### sourceRoleArn
- **Type**: typing.Optional[str]

### targetRoleArn
- **Type**: typing.Optional[str]


# RuleGroupsNamespaceDescription

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceStatus'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RuleGroupsNamespaceStatus

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]


# RuleGroupsNamespaceSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.RuleGroupsNamespaceStatus'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ScrapeConfiguration

### configurationBlob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.Blob]


# ScrapeConfigurationOutput

### configurationBlob
- **Type**: typing.Optional[bytes]


# ScrapeConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScraperDescription

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.Destination'>
- **Required**: Yes

### lastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### scrapeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScrapeConfigurationOutput'>
- **Required**: Yes

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceOutput'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatus'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### roleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.RoleConfiguration]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ScraperStatus

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'DELETION_FAILED', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes


# ScraperSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.Destination'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.SourceOutput'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatus'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### roleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.RoleConfiguration]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# Source

### eksConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.EksConfiguration]


# SourceOutput

### eksConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.EksConfigurationOutput]


# SourceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLoggingConfigurationRequest

### logGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateLoggingConfigurationResponse

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.LoggingConfigurationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScraperRequest

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.Destination]

### roleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.RoleConfiguration]

### scrapeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amp_classes.ScrapeConfigurationUnion]


# UpdateScraperResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### scraperId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ScraperStatus'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkspaceAliasRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WorkspaceDescription

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.WorkspaceStatus'>
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


# WorkspaceStatus

### statusCode
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'UPDATING']
- **Required**: Yes


# WorkspaceSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.amp_classes.WorkspaceStatus'>
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



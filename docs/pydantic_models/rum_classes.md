# Rum Classes

# AppMonitorConfigurationOutputTypeDef

### AllowCookies
- **Type**: typing.Optional[bool]

### EnableXRay
- **Type**: typing.Optional[bool]

### ExcludedPages
- **Type**: typing.Optional[typing.List[str]]

### FavoritePages
- **Type**: typing.Optional[typing.List[str]]

### GuestRoleArn
- **Type**: typing.Optional[str]

### IdentityPoolId
- **Type**: typing.Optional[str]

### IncludedPages
- **Type**: typing.Optional[typing.List[str]]

### SessionSampleRate
- **Type**: typing.Optional[float]

### Telemetries
- **Type**: typing.Optional[typing.List[typing.Literal['errors', 'http', 'performance']]]


# AppMonitorConfigurationTypeDef

### AllowCookies
- **Type**: typing.Optional[bool]

### EnableXRay
- **Type**: typing.Optional[bool]

### ExcludedPages
- **Type**: typing.Optional[typing.Sequence[str]]

### FavoritePages
- **Type**: typing.Optional[typing.Sequence[str]]

### GuestRoleArn
- **Type**: typing.Optional[str]

### IdentityPoolId
- **Type**: typing.Optional[str]

### IncludedPages
- **Type**: typing.Optional[typing.Sequence[str]]

### SessionSampleRate
- **Type**: typing.Optional[float]

### Telemetries
- **Type**: typing.Optional[typing.Sequence[typing.Literal['errors', 'http', 'performance']]]


# AppMonitorConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppMonitorDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppMonitorSummaryTypeDef

### Created
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATED', 'DELETING']]


# AppMonitorTypeDef

### AppMonitorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationOutputTypeDef]

### Created
- **Type**: typing.Optional[str]

### CustomEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.CustomEventsTypeDef]

### DataStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.DataStorageTypeDef]

### Domain
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATED', 'DELETING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateRumMetricDefinitionsErrorTypeDef

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### MetricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestOutputTypeDef'>
- **Required**: Yes


# BatchCreateRumMetricDefinitionsRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### MetricDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestUnionTypeDef]
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]


# BatchCreateRumMetricDefinitionsResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.BatchCreateRumMetricDefinitionsErrorTypeDef]
- **Required**: Yes

### MetricDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteRumMetricDefinitionsErrorTypeDef

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### MetricDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteRumMetricDefinitionsRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### MetricDefinitionIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]


# BatchDeleteRumMetricDefinitionsResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.BatchDeleteRumMetricDefinitionsErrorTypeDef]
- **Required**: Yes

### MetricDefinitionIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetRumMetricDefinitionsRequestPaginateTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfigTypeDef]


# BatchGetRumMetricDefinitionsRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# BatchGetRumMetricDefinitionsResponseTypeDef

### MetricDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CreateAppMonitorRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AppMonitorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationUnionTypeDef]

### CustomEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.CustomEventsTypeDef]

### CwLogEnabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAppMonitorResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomEventsTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CwLogTypeDef

### CwLogEnabled
- **Type**: typing.Optional[bool]

### CwLogGroup
- **Type**: typing.Optional[str]


# DataStorageTypeDef

### CwLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.CwLogTypeDef]


# DeleteAppMonitorRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DeleteResourcePolicyResponseTypeDef

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRumMetricsDestinationRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]


# GetAppMonitorDataRequestPaginateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.TimeRangeTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.QueryFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfigTypeDef]


# GetAppMonitorDataRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.TimeRangeTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.QueryFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAppMonitorDataResponseTypeDef

### Events
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAppMonitorRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppMonitorResponseTypeDef

### AppMonitor
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.AppMonitorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePolicyRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppMonitorsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfigTypeDef]


# ListAppMonitorsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppMonitorsResponseTypeDef

### AppMonitorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.AppMonitorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRumMetricsDestinationsRequestPaginateTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfigTypeDef]


# ListRumMetricsDestinationsRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRumMetricsDestinationsResponseTypeDef

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.MetricDestinationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricDefinitionRequestOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionKeys
- **Type**: typing.Optional[typing.Dict[str, str]]

### EventPattern
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### UnitLabel
- **Type**: typing.Optional[str]

### ValueKey
- **Type**: typing.Optional[str]


# MetricDefinitionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionKeys
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EventPattern
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### UnitLabel
- **Type**: typing.Optional[str]

### ValueKey
- **Type**: typing.Optional[str]


# MetricDefinitionRequestUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetricDefinitionTypeDef

### MetricDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionKeys
- **Type**: typing.Optional[typing.Dict[str, str]]

### EventPattern
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### UnitLabel
- **Type**: typing.Optional[str]

### ValueKey
- **Type**: typing.Optional[str]


# MetricDestinationSummaryTypeDef

### Destination
- **Type**: typing.Optional[typing.Literal['CloudWatch', 'Evidently']]

### DestinationArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# PutResourcePolicyResponseTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRumEventsRequestTypeDef

### AppMonitorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.AppMonitorDetailsTypeDef'>
- **Required**: Yes

### BatchId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RumEvents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.RumEventTypeDef]
- **Required**: Yes

### UserDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.UserDetailsTypeDef'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]


# PutRumMetricsDestinationRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# QueryFilterTypeDef

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


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


# RumEventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimeRangeTypeDef

### After
- **Type**: <class 'int'>
- **Required**: Yes

### Before
- **Type**: typing.Optional[int]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppMonitorRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AppMonitorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationUnionTypeDef]

### CustomEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.CustomEventsTypeDef]

### CwLogEnabled
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]


# UpdateRumMetricDefinitionRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### MetricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestUnionTypeDef'>
- **Required**: Yes

### MetricDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]


# UserDetailsTypeDef

### sessionId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]



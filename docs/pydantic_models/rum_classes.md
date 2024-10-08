# Pydantic Models in rum_classes

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


# AppMonitorDetailsTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestTypeDef'>
- **Required**: Yes


# BatchCreateRumMetricDefinitionsRequestRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### MetricDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestTypeDef]
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


# BatchDeleteRumMetricDefinitionsRequestRequestTypeDef

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


# BatchGetRumMetricDefinitionsRequestBatchGetRumMetricDefinitionsPaginateTypeDef

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


# BatchGetRumMetricDefinitionsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppMonitorRequestRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AppMonitorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationTypeDef]

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


# DeleteAppMonitorRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRumMetricsDestinationRequestRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]


# GetAppMonitorDataRequestGetAppMonitorDataPaginateTypeDef

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


# GetAppMonitorDataRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppMonitorRequestRequestTypeDef

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


# ListAppMonitorsRequestListAppMonitorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfigTypeDef]


# ListAppMonitorsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppMonitorsResponseTypeDef

### AppMonitorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.AppMonitorSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRumMetricsDestinationsRequestListRumMetricsDestinationsPaginateTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfigTypeDef]


# ListRumMetricsDestinationsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# PutRumEventsRequestRequestTypeDef

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


# PutRumMetricsDestinationRequestRequestTypeDef

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


# RumEventTypeDef

### details
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppMonitorRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AppMonitorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationTypeDef]

### CustomEvents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.CustomEventsTypeDef]

### CwLogEnabled
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]


# UpdateRumMetricDefinitionRequestRequestTypeDef

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### MetricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestTypeDef'>
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



# Rum Classes

# AppMonitor

### AppMonitorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationOutput]

### Created
- **Type**: typing.Optional[str]

### CustomEvents
- **Type**: <class 'NoneType'>

### DataStorage
- **Type**: <class 'NoneType'>

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


# AppMonitorConfiguration

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


# AppMonitorConfigurationOutput

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


# AppMonitorConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppMonitorDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppMonitorSummary

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateRumMetricDefinitionsError

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### MetricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestOutput'>
- **Required**: Yes


# BatchCreateRumMetricDefinitionsRequest

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### MetricDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestUnion]
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]


# BatchCreateRumMetricDefinitionsResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.BatchCreateRumMetricDefinitionsError]
- **Required**: Yes

### MetricDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.MetricDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteRumMetricDefinitionsError

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### MetricDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteRumMetricDefinitionsRequest

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


# BatchDeleteRumMetricDefinitionsResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.BatchDeleteRumMetricDefinitionsError]
- **Required**: Yes

### MetricDefinitionIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetRumMetricDefinitionsRequest

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


# BatchGetRumMetricDefinitionsRequestPaginate

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfig]


# BatchGetRumMetricDefinitionsResponse

### MetricDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.MetricDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CreateAppMonitorRequest

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AppMonitorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationUnion]

### CustomEvents
- **Type**: <class 'NoneType'>

### CwLogEnabled
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAppMonitorResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes


# CustomEvents

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CwLog

### CwLogEnabled
- **Type**: typing.Optional[bool]

### CwLogGroup
- **Type**: typing.Optional[str]


# DataStorage

### CwLog
- **Type**: <class 'NoneType'>


# DeleteAppMonitorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DeleteResourcePolicyResponse

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRumMetricsDestinationRequest

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]


# GetAppMonitorDataRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.TimeRange'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.QueryFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetAppMonitorDataRequestPaginate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.TimeRange'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.QueryFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfig]


# GetAppMonitorDataResponse

### Events
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetAppMonitorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppMonitorResponse

### AppMonitor
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.AppMonitor'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePolicyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes


# ListAppMonitorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppMonitorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfig]


# ListAppMonitorsResponse

### AppMonitorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.AppMonitorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRumMetricsDestinationsRequest

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRumMetricsDestinationsRequestPaginate

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.PaginatorConfig]


# ListRumMetricsDestinationsResponse

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rum_classes.MetricDestinationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes


# MetricDefinition

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


# MetricDefinitionRequest

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


# MetricDefinitionRequestOutput

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


# MetricDefinitionRequestUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetricDestinationSummary

### Destination
- **Type**: typing.Optional[typing.Literal['CloudWatch', 'Evidently']]

### DestinationArn
- **Type**: typing.Optional[str]

### IamRoleArn
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutResourcePolicyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# PutResourcePolicyResponse

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.ResponseMetadata'>
- **Required**: Yes


# PutRumEventsRequest

### AppMonitorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.AppMonitorDetails'>
- **Required**: Yes

### BatchId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RumEvents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rum_classes.RumEvent]
- **Required**: Yes

### UserDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.UserDetails'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]


# PutRumMetricsDestinationRequest

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


# QueryFilter

### Name
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


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


# RumEvent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimeRange

### After
- **Type**: <class 'int'>
- **Required**: Yes

### Before
- **Type**: typing.Optional[int]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppMonitorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AppMonitorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rum_classes.AppMonitorConfigurationUnion]

### CustomEvents
- **Type**: <class 'NoneType'>

### CwLogEnabled
- **Type**: typing.Optional[bool]

### Domain
- **Type**: typing.Optional[str]


# UpdateRumMetricDefinitionRequest

### AppMonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: typing.Literal['CloudWatch', 'Evidently']
- **Required**: Yes

### MetricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.rum_classes.MetricDefinitionRequestUnion'>
- **Required**: Yes

### MetricDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationArn
- **Type**: typing.Optional[str]


# UserDetails

### sessionId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]



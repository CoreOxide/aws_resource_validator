# Pydantic Models in internetmonitor_classes

# AvailabilityMeasurementTypeDef

### ExperienceScore
- **Type**: typing.Optional[float]

### PercentOfTotalTrafficImpacted
- **Type**: typing.Optional[float]

### PercentOfClientLocationImpacted
- **Type**: typing.Optional[float]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientLocationTypeDef

### ASName
- **Type**: <class 'str'>
- **Required**: Yes

### ASNumber
- **Type**: <class 'int'>
- **Required**: Yes

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### City
- **Type**: <class 'str'>
- **Required**: Yes

### Latitude
- **Type**: <class 'float'>
- **Required**: Yes

### Longitude
- **Type**: <class 'float'>
- **Required**: Yes

### Subdivision
- **Type**: typing.Optional[str]

### Metro
- **Type**: typing.Optional[str]


# CreateMonitorInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Optional[typing.Sequence[str]]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### MaxCityNetworksToMonitor
- **Type**: typing.Optional[int]

### InternetMeasurementsLogDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.InternetMeasurementsLogDeliveryTypeDef]

### TrafficPercentageToMonitor
- **Type**: typing.Optional[int]

### HealthEventsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.HealthEventsConfigTypeDef]


# CreateMonitorOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMonitorInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes


# FilterParameterTypeDef

### Field
- **Type**: typing.Optional[str]

### Operator
- **Type**: typing.Optional[typing.Literal['EQUALS', 'NOT_EQUALS']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# GetHealthEventInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkedAccountId
- **Type**: typing.Optional[str]


# GetHealthEventOutputTypeDef

### EventArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImpactedLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor_classes.ImpactedLocationTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### PercentOfTotalTrafficImpacted
- **Type**: <class 'float'>
- **Required**: Yes

### ImpactType
- **Type**: typing.Literal['AVAILABILITY', 'LOCAL_AVAILABILITY', 'LOCAL_PERFORMANCE', 'PERFORMANCE']
- **Required**: Yes

### HealthScoreThreshold
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInternetEventInputRequestTypeDef

### EventId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInternetEventOutputTypeDef

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### EventArn
- **Type**: <class 'str'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ClientLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ClientLocationTypeDef'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['AVAILABILITY', 'PERFORMANCE']
- **Required**: Yes

### EventStatus
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMonitorInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### LinkedAccountId
- **Type**: typing.Optional[str]


# GetMonitorOutputTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.List[str]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProcessingStatus
- **Type**: typing.Literal['COLLECTING_DATA', 'FAULT_ACCESS_CLOUDWATCH', 'FAULT_SERVICE', 'INACTIVE', 'INSUFFICIENT_DATA', 'OK']
- **Required**: Yes

### ProcessingStatusInfo
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### MaxCityNetworksToMonitor
- **Type**: <class 'int'>
- **Required**: Yes

### InternetMeasurementsLogDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.InternetMeasurementsLogDeliveryTypeDef'>
- **Required**: Yes

### TrafficPercentageToMonitor
- **Type**: <class 'int'>
- **Required**: Yes

### HealthEventsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.HealthEventsConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryResultsInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetQueryResultsOutputTypeDef

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor_classes.QueryFieldTypeDef]
- **Required**: Yes

### Data
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryStatusInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStatusOutputTypeDef

### Status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HealthEventTypeDef

### EventArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImpactedLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor_classes.ImpactedLocationTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### ImpactType
- **Type**: typing.Literal['AVAILABILITY', 'LOCAL_AVAILABILITY', 'LOCAL_PERFORMANCE', 'PERFORMANCE']
- **Required**: Yes

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### PercentOfTotalTrafficImpacted
- **Type**: typing.Optional[float]

### HealthScoreThreshold
- **Type**: typing.Optional[float]


# HealthEventsConfigTypeDef

### AvailabilityScoreThreshold
- **Type**: typing.Optional[float]

### PerformanceScoreThreshold
- **Type**: typing.Optional[float]

### AvailabilityLocalHealthEventsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.LocalHealthEventsConfigTypeDef]

### PerformanceLocalHealthEventsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.LocalHealthEventsConfigTypeDef]


# ImpactedLocationTypeDef

### ASName
- **Type**: <class 'str'>
- **Required**: Yes

### ASNumber
- **Type**: <class 'int'>
- **Required**: Yes

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### Subdivision
- **Type**: typing.Optional[str]

### Metro
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### Latitude
- **Type**: typing.Optional[float]

### Longitude
- **Type**: typing.Optional[float]

### CountryCode
- **Type**: typing.Optional[str]

### SubdivisionCode
- **Type**: typing.Optional[str]

### ServiceLocation
- **Type**: typing.Optional[str]

### CausedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.NetworkImpairmentTypeDef]

### InternetHealth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.InternetHealthTypeDef]

### Ipv4Prefixes
- **Type**: typing.Optional[typing.List[str]]


# InternetEventSummaryTypeDef

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### EventArn
- **Type**: <class 'str'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ClientLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ClientLocationTypeDef'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['AVAILABILITY', 'PERFORMANCE']
- **Required**: Yes

### EventStatus
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### EndedAt
- **Type**: typing.Optional[datetime.datetime]


# InternetHealthTypeDef

### Availability
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.AvailabilityMeasurementTypeDef]

### Performance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.PerformanceMeasurementTypeDef]


# InternetMeasurementsLogDeliveryTypeDef

### S3Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.S3ConfigTypeDef]


# ListHealthEventsInputListHealthEventsPaginateTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EventStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'RESOLVED']]

### LinkedAccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.PaginatorConfigTypeDef]


# ListHealthEventsInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### EventStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'RESOLVED']]

### LinkedAccountId
- **Type**: typing.Optional[str]


# ListHealthEventsOutputTypeDef

### HealthEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor_classes.HealthEventTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInternetEventsInputListInternetEventsPaginateTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EventStatus
- **Type**: typing.Optional[str]

### EventType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.PaginatorConfigTypeDef]


# ListInternetEventsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EventStatus
- **Type**: typing.Optional[str]

### EventType
- **Type**: typing.Optional[str]


# ListInternetEventsOutputTypeDef

### InternetEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor_classes.InternetEventSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMonitorsInputListMonitorsPaginateTypeDef

### MonitorStatus
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.PaginatorConfigTypeDef]


# ListMonitorsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### MonitorStatus
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]


# ListMonitorsOutputTypeDef

### Monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor_classes.MonitorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LocalHealthEventsConfigTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### HealthScoreThreshold
- **Type**: typing.Optional[float]

### MinTrafficImpact
- **Type**: typing.Optional[float]


# MonitorTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### ProcessingStatus
- **Type**: typing.Optional[typing.Literal['COLLECTING_DATA', 'FAULT_ACCESS_CLOUDWATCH', 'FAULT_SERVICE', 'INACTIVE', 'INSUFFICIENT_DATA', 'OK']]


# NetworkImpairmentTypeDef

### Networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor_classes.NetworkTypeDef]
- **Required**: Yes

### AsPath
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor_classes.NetworkTypeDef]
- **Required**: Yes

### NetworkEventType
- **Type**: typing.Literal['AWS', 'Internet']
- **Required**: Yes


# NetworkTypeDef

### ASName
- **Type**: <class 'str'>
- **Required**: Yes

### ASNumber
- **Type**: <class 'int'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceMeasurementTypeDef

### ExperienceScore
- **Type**: typing.Optional[float]

### PercentOfTotalTrafficImpacted
- **Type**: typing.Optional[float]

### PercentOfClientLocationImpacted
- **Type**: typing.Optional[float]

### RoundTripTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.RoundTripTimeTypeDef]


# QueryFieldTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
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


# RoundTripTimeTypeDef

### P50
- **Type**: typing.Optional[float]

### P90
- **Type**: typing.Optional[float]

### P95
- **Type**: typing.Optional[float]


# S3ConfigTypeDef

### BucketName
- **Type**: typing.Optional[str]

### BucketPrefix
- **Type**: typing.Optional[str]

### LogDeliveryStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# StartQueryInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### QueryType
- **Type**: typing.Literal['MEASUREMENTS', 'TOP_LOCATIONS', 'TOP_LOCATION_DETAILS']
- **Required**: Yes

### FilterParameters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.internetmonitor_classes.FilterParameterTypeDef]]

### LinkedAccountId
- **Type**: typing.Optional[str]


# StartQueryOutputTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopQueryInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMonitorInputRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcesToAdd
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourcesToRemove
- **Type**: typing.Optional[typing.Sequence[str]]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'PENDING']]

### ClientToken
- **Type**: typing.Optional[str]

### MaxCityNetworksToMonitor
- **Type**: typing.Optional[int]

### InternetMeasurementsLogDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.InternetMeasurementsLogDeliveryTypeDef]

### TrafficPercentageToMonitor
- **Type**: typing.Optional[int]

### HealthEventsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor_classes.HealthEventsConfigTypeDef]


# UpdateMonitorOutputTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



# Internetmonitor Internetmonitor Classes

# AvailabilityMeasurement

### ExperienceScore
- **Type**: typing.Optional[float]

### PercentOfTotalTrafficImpacted
- **Type**: typing.Optional[float]

### PercentOfClientLocationImpacted
- **Type**: typing.Optional[float]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientLocation

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


# CreateMonitorInput

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### Resources
- **Type**: typing.Optional[typing.List[str]]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### MaxCityNetworksToMonitor
- **Type**: typing.Optional[int]

### InternetMeasurementsLogDelivery
- **Type**: <class 'NoneType'>

### TrafficPercentageToMonitor
- **Type**: typing.Optional[int]

### HealthEventsConfig
- **Type**: <class 'NoneType'>


# CreateMonitorOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMonitorInput

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes


# FilterParameter

### Field
- **Type**: typing.Optional[str]

### Operator
- **Type**: typing.Optional[typing.Literal['EQUALS', 'NOT_EQUALS']]

### Values
- **Type**: typing.Optional[typing.List[str]]


# GetHealthEventInput

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### LinkedAccountId
- **Type**: typing.Optional[str]


# GetHealthEventOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ImpactedLocation]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# GetInternetEventInput

### EventId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInternetEventOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ClientLocation'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['AVAILABILITY', 'PERFORMANCE']
- **Required**: Yes

### EventStatus
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# GetMonitorInput

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### LinkedAccountId
- **Type**: typing.Optional[str]


# GetMonitorOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.InternetMeasurementsLogDelivery'>
- **Required**: Yes

### TrafficPercentageToMonitor
- **Type**: <class 'int'>
- **Required**: Yes

### HealthEventsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.HealthEventsConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryResultsInput

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


# GetQueryResultsOutput

### Fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.QueryField]
- **Required**: Yes

### Data
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetQueryStatusInput

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryStatusOutput

### Status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'QUEUED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# HealthEvent

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ImpactedLocation]
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


# HealthEventsConfig

### AvailabilityScoreThreshold
- **Type**: typing.Optional[float]

### PerformanceScoreThreshold
- **Type**: typing.Optional[float]

### AvailabilityLocalHealthEventsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.LocalHealthEventsConfig]

### PerformanceLocalHealthEventsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.LocalHealthEventsConfig]


# ImpactedLocation

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.NetworkImpairment]

### InternetHealth
- **Type**: <class 'NoneType'>

### Ipv4Prefixes
- **Type**: typing.Optional[typing.List[str]]


# InternetEventSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ClientLocation'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['AVAILABILITY', 'PERFORMANCE']
- **Required**: Yes

### EventStatus
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### EndedAt
- **Type**: typing.Optional[datetime.datetime]


# InternetHealth

### Availability
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.AvailabilityMeasurement]

### Performance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.PerformanceMeasurement]


# InternetMeasurementsLogDelivery

### S3Config
- **Type**: <class 'NoneType'>


# ListHealthEventsInput

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


# ListHealthEventsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.PaginatorConfig]


# ListHealthEventsOutput

### HealthEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.HealthEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInternetEventsInput

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


# ListInternetEventsInputPaginate

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EventStatus
- **Type**: typing.Optional[str]

### EventType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.PaginatorConfig]


# ListInternetEventsOutput

### InternetEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.InternetEventSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitorsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### MonitorStatus
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]


# ListMonitorsInputPaginate

### MonitorStatus
- **Type**: typing.Optional[str]

### IncludeLinkedAccounts
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.PaginatorConfig]


# ListMonitorsOutput

### Monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.Monitor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# LocalHealthEventsConfig

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### HealthScoreThreshold
- **Type**: typing.Optional[float]

### MinTrafficImpact
- **Type**: typing.Optional[float]


# Monitor

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


# Network

### ASName
- **Type**: <class 'str'>
- **Required**: Yes

### ASNumber
- **Type**: <class 'int'>
- **Required**: Yes


# NetworkImpairment

### Networks
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.Network]
- **Required**: Yes

### AsPath
- **Type**: typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.Network]
- **Required**: Yes

### NetworkEventType
- **Type**: typing.Literal['AWS', 'Internet']
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceMeasurement

### ExperienceScore
- **Type**: typing.Optional[float]

### PercentOfTotalTrafficImpacted
- **Type**: typing.Optional[float]

### PercentOfClientLocationImpacted
- **Type**: typing.Optional[float]

### RoundTripTime
- **Type**: <class 'NoneType'>


# QueryField

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


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


# RoundTripTime

### P50
- **Type**: typing.Optional[float]

### P90
- **Type**: typing.Optional[float]

### P95
- **Type**: typing.Optional[float]


# S3Config

### BucketName
- **Type**: typing.Optional[str]

### BucketPrefix
- **Type**: typing.Optional[str]

### LogDeliveryStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# StartQueryInput

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
- **Type**: typing.Literal['MEASUREMENTS', 'OVERALL_TRAFFIC_SUGGESTIONS', 'OVERALL_TRAFFIC_SUGGESTIONS_DETAILS', 'ROUTING_SUGGESTIONS', 'TOP_LOCATIONS', 'TOP_LOCATION_DETAILS']
- **Required**: Yes

### FilterParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.FilterParameter]]

### LinkedAccountId
- **Type**: typing.Optional[str]


# StartQueryOutput

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes


# StopQueryInput

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateMonitorInput

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcesToAdd
- **Type**: typing.Optional[typing.List[str]]

### ResourcesToRemove
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'PENDING']]

### ClientToken
- **Type**: typing.Optional[str]

### MaxCityNetworksToMonitor
- **Type**: typing.Optional[int]

### InternetMeasurementsLogDelivery
- **Type**: <class 'NoneType'>

### TrafficPercentageToMonitor
- **Type**: typing.Optional[int]

### HealthEventsConfig
- **Type**: <class 'NoneType'>


# UpdateMonitorOutput

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ERROR', 'INACTIVE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.internetmonitor.internetmonitor_classes.ResponseMetadata'>
- **Required**: Yes



# Cloudtrail Classes

# AddTagsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagsList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]
- **Required**: Yes


# AdvancedEventSelector

### FieldSelectors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedFieldSelectorUnion]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AdvancedEventSelectorOutput

### FieldSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedFieldSelectorOutput]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AdvancedEventSelectorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AdvancedFieldSelector

### Field
- **Type**: <class 'str'>
- **Required**: Yes

### Equals
- **Type**: typing.Optional[typing.Sequence[str]]

### StartsWith
- **Type**: typing.Optional[typing.Sequence[str]]

### EndsWith
- **Type**: typing.Optional[typing.Sequence[str]]

### NotEquals
- **Type**: typing.Optional[typing.Sequence[str]]

### NotStartsWith
- **Type**: typing.Optional[typing.Sequence[str]]

### NotEndsWith
- **Type**: typing.Optional[typing.Sequence[str]]


# AdvancedFieldSelectorOutput

### Field
- **Type**: <class 'str'>
- **Required**: Yes

### Equals
- **Type**: typing.Optional[typing.List[str]]

### StartsWith
- **Type**: typing.Optional[typing.List[str]]

### EndsWith
- **Type**: typing.Optional[typing.List[str]]

### NotEquals
- **Type**: typing.Optional[typing.List[str]]

### NotStartsWith
- **Type**: typing.Optional[typing.List[str]]

### NotEndsWith
- **Type**: typing.Optional[typing.List[str]]


# AdvancedFieldSelectorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelQueryRequest

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### EventDataStore
- **Type**: typing.Optional[str]

### EventDataStoreOwnerAccountId
- **Type**: typing.Optional[str]


# CancelQueryResponse

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryStatus
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'FINISHED', 'QUEUED', 'RUNNING', 'TIMED_OUT']
- **Required**: Yes

### EventDataStoreOwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# Channel

### ChannelArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# CreateChannelRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.Destination]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]]


# CreateChannelResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Destination]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDashboardRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshSchedule
- **Type**: <class 'NoneType'>

### TagsList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]

### Widgets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.RequestWidget]]


# CreateEventDataStoreRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorUnion]]

### MultiRegionEnabled
- **Type**: typing.Optional[bool]

### OrganizationEnabled
- **Type**: typing.Optional[bool]

### RetentionPeriod
- **Type**: typing.Optional[int]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]

### TagsList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### StartIngestion
- **Type**: typing.Optional[bool]

### BillingMode
- **Type**: typing.Optional[typing.Literal['EXTENDABLE_RETENTION_PRICING', 'FIXED_RETENTION_PRICING']]


# CreateEventDataStoreResponse

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'ENABLED', 'PENDING_DELETION', 'STARTING_INGESTION', 'STOPPED_INGESTION', 'STOPPING_INGESTION']
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutput]
- **Required**: Yes

### MultiRegionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OrganizationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### TerminationProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TagsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### BillingMode
- **Type**: typing.Literal['EXTENDABLE_RETENTION_PRICING', 'FIXED_RETENTION_PRICING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrailRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]

### SnsTopicName
- **Type**: typing.Optional[str]

### IncludeGlobalServiceEvents
- **Type**: typing.Optional[bool]

### IsMultiRegionTrail
- **Type**: typing.Optional[bool]

### EnableLogFileValidation
- **Type**: typing.Optional[bool]

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### CloudWatchLogsRoleArn
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### IsOrganizationTrail
- **Type**: typing.Optional[bool]

### TagsList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]]


# CreateTrailResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicARN
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGlobalServiceEvents
- **Type**: <class 'bool'>
- **Required**: Yes

### IsMultiRegionTrail
- **Type**: <class 'bool'>
- **Required**: Yes

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### LogFileValidationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CloudWatchLogsLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### IsOrganizationTrail
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# DashboardDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataResourceOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataResourceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteChannelRequest

### Channel
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDashboardRequest

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventDataStoreRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrailRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterOrganizationDelegatedAdminRequest

### DelegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQueryRequest

### EventDataStore
- **Type**: typing.Optional[str]

### QueryId
- **Type**: typing.Optional[str]

### QueryAlias
- **Type**: typing.Optional[str]

### RefreshId
- **Type**: typing.Optional[str]

### EventDataStoreOwnerAccountId
- **Type**: typing.Optional[str]


# DescribeQueryResponse

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### QueryStatus
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'FINISHED', 'QUEUED', 'RUNNING', 'TIMED_OUT']
- **Required**: Yes

### QueryStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.QueryStatisticsForDescribeQuery'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### DeliveryStatus
- **Type**: typing.Literal['ACCESS_DENIED', 'ACCESS_DENIED_SIGNING_FILE', 'CANCELLED', 'FAILED', 'FAILED_SIGNING_FILE', 'PENDING', 'RESOURCE_NOT_FOUND', 'SUCCESS', 'UNKNOWN']
- **Required**: Yes

### Prompt
- **Type**: <class 'str'>
- **Required**: Yes

### EventDataStoreOwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrailsRequest

### trailNameList
- **Type**: typing.Optional[typing.Sequence[str]]

### includeShadowTrails
- **Type**: typing.Optional[bool]


# DescribeTrailsResponse

### trailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Trail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisableFederationRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# DisableFederationResponse

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### FederationStatus
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# EnableFederationRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes

### FederationRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# EnableFederationResponse

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### FederationStatus
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']
- **Required**: Yes

### FederationRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# Event

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventDataStore

### EventDataStoreArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'ENABLED', 'PENDING_DELETION', 'STARTING_INGESTION', 'STOPPED_INGESTION', 'STOPPING_INGESTION']]

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutput]]

### MultiRegionEnabled
- **Type**: typing.Optional[bool]

### OrganizationEnabled
- **Type**: typing.Optional[bool]

### RetentionPeriod
- **Type**: typing.Optional[int]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# EventSelector

### ReadWriteType
- **Type**: typing.Optional[typing.Literal['All', 'ReadOnly', 'WriteOnly']]

### IncludeManagementEvents
- **Type**: typing.Optional[bool]

### DataResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.DataResourceUnion]]

### ExcludeManagementEventSources
- **Type**: typing.Optional[typing.Sequence[str]]


# EventSelectorOutput

### ReadWriteType
- **Type**: typing.Optional[typing.Literal['All', 'ReadOnly', 'WriteOnly']]

### IncludeManagementEvents
- **Type**: typing.Optional[bool]

### DataResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.DataResourceOutput]]

### ExcludeManagementEventSources
- **Type**: typing.Optional[typing.List[str]]


# EventSelectorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GenerateQueryRequest

### EventDataStores
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Prompt
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateQueryResponse

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### QueryAlias
- **Type**: <class 'str'>
- **Required**: Yes

### EventDataStoreOwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelRequest

### Channel
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### SourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.SourceConfig'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Destination]
- **Required**: Yes

### IngestionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.IngestionStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDashboardRequest

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventDataStoreRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventDataStoreResponse

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'ENABLED', 'PENDING_DELETION', 'STARTING_INGESTION', 'STOPPED_INGESTION', 'STOPPING_INGESTION']
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutput]
- **Required**: Yes

### MultiRegionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OrganizationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### TerminationProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### BillingMode
- **Type**: typing.Literal['EXTENDABLE_RETENTION_PRICING', 'FIXED_RETENTION_PRICING']
- **Required**: Yes

### FederationStatus
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']
- **Required**: Yes

### FederationRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.PartitionKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventSelectorsRequest

### TrailName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventSelectorsResponse

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### EventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.EventSelectorOutput]
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportRequest

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportResponse

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[str]
- **Required**: Yes

### ImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportSource'>
- **Required**: Yes

### StartEventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndEventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# GetInsightSelectorsRequest

### TrailName
- **Type**: typing.Optional[str]

### EventDataStore
- **Type**: typing.Optional[str]


# GetInsightSelectorsResponse

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### InsightSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.InsightSelector]
- **Required**: Yes

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### InsightsDestination
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryResultsRequest

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### EventDataStore
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxQueryResults
- **Type**: typing.Optional[int]

### EventDataStoreOwnerAccountId
- **Type**: typing.Optional[str]


# GetQueryResultsResponse

### QueryStatus
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'FINISHED', 'QUEUED', 'RUNNING', 'TIMED_OUT']
- **Required**: Yes

### QueryStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.QueryStatistics'>
- **Required**: Yes

### QueryResultRows
- **Type**: typing.List[typing.List[typing.Dict[str, str]]]
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### DelegatedAdminResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrailRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrailResponse

### Trail
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.Trail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrailStatusRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrailStatusResponse

### IsLogging
- **Type**: <class 'bool'>
- **Required**: Yes

### LatestDeliveryError
- **Type**: <class 'str'>
- **Required**: Yes

### LatestNotificationError
- **Type**: <class 'str'>
- **Required**: Yes

### LatestDeliveryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestNotificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartLoggingTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StopLoggingTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestCloudWatchLogsDeliveryError
- **Type**: <class 'str'>
- **Required**: Yes

### LatestCloudWatchLogsDeliveryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestDigestDeliveryTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestDigestDeliveryError
- **Type**: <class 'str'>
- **Required**: Yes

### LatestDeliveryAttemptTime
- **Type**: <class 'str'>
- **Required**: Yes

### LatestNotificationAttemptTime
- **Type**: <class 'str'>
- **Required**: Yes

### LatestNotificationAttemptSucceeded
- **Type**: <class 'str'>
- **Required**: Yes

### LatestDeliveryAttemptSucceeded
- **Type**: <class 'str'>
- **Required**: Yes

### TimeLoggingStarted
- **Type**: <class 'str'>
- **Required**: Yes

### TimeLoggingStopped
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# ImportFailureListItem

### Location
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RETRY', 'SUCCEEDED']]

### ErrorType
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# ImportSource

### S3
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.S3ImportSource'>
- **Required**: Yes


# ImportStatistics

### PrefixesFound
- **Type**: typing.Optional[int]

### PrefixesCompleted
- **Type**: typing.Optional[int]

### FilesCompleted
- **Type**: typing.Optional[int]

### EventsCompleted
- **Type**: typing.Optional[int]

### FailedEntries
- **Type**: typing.Optional[int]


# ImportsListItem

### ImportId
- **Type**: typing.Optional[str]

### ImportStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED']]

### Destinations
- **Type**: typing.Optional[typing.List[str]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# IngestionStatus

### LatestIngestionSuccessTime
- **Type**: typing.Optional[datetime.datetime]

### LatestIngestionSuccessEventID
- **Type**: typing.Optional[str]

### LatestIngestionErrorCode
- **Type**: typing.Optional[str]

### LatestIngestionAttemptTime
- **Type**: typing.Optional[datetime.datetime]

### LatestIngestionAttemptEventID
- **Type**: typing.Optional[str]


# InsightSelector

### InsightType
- **Type**: typing.Optional[typing.Literal['ApiCallRateInsight', 'ApiErrorRateInsight']]


# ListChannelsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsResponse

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Channel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDashboardsResponse

### Dashboards
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.DashboardDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventDataStoresRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventDataStoresResponse

### EventDataStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.EventDataStore]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportFailuresRequest

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListImportFailuresRequestPaginate

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfig]


# ListImportFailuresResponse

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.ImportFailureListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportsRequest

### MaxResults
- **Type**: typing.Optional[int]

### Destination
- **Type**: typing.Optional[str]

### ImportStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED']]

### NextToken
- **Type**: typing.Optional[str]


# ListImportsRequestPaginate

### Destination
- **Type**: typing.Optional[str]

### ImportStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfig]


# ListImportsResponse

### Imports
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.ImportsListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsMetricDataRequest

### EventSource
- **Type**: <class 'str'>
- **Required**: Yes

### EventName
- **Type**: <class 'str'>
- **Required**: Yes

### InsightType
- **Type**: typing.Literal['ApiCallRateInsight', 'ApiErrorRateInsight']
- **Required**: Yes

### ErrorCode
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### Period
- **Type**: typing.Optional[int]

### DataType
- **Type**: typing.Optional[typing.Literal['FillWithZeros', 'NonZeroData']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsMetricDataResponse

### EventSource
- **Type**: <class 'str'>
- **Required**: Yes

### EventName
- **Type**: <class 'str'>
- **Required**: Yes

### InsightType
- **Type**: typing.Literal['ApiCallRateInsight', 'ApiErrorRateInsight']
- **Required**: Yes

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### Values
- **Type**: typing.List[float]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPublicKeysRequest

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### NextToken
- **Type**: typing.Optional[str]


# ListPublicKeysRequestPaginate

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfig]


# ListPublicKeysResponse

### PublicKeyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.PublicKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueriesRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### QueryStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FINISHED', 'QUEUED', 'RUNNING', 'TIMED_OUT']]


# ListQueriesResponse

### Queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Query]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequest

### ResourceIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequestPaginate

### ResourceIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfig]


# ListTagsResponse

### ResourceTagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrailsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListTrailsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfig]


# ListTrailsResponse

### Trails
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.TrailInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LookupAttribute

### AttributeKey
- **Type**: typing.Literal['AccessKeyId', 'EventId', 'EventName', 'EventSource', 'ReadOnly', 'ResourceName', 'ResourceType', 'Username']
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# LookupEventsRequest

### LookupAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.LookupAttribute]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EventCategory
- **Type**: typing.Optional[typing.Literal['insight']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# LookupEventsRequestPaginate

### LookupAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.LookupAttribute]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EventCategory
- **Type**: typing.Optional[typing.Literal['insight']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfig]


# LookupEventsResponse

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartitionKey

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PublicKey

### Value
- **Type**: typing.Optional[bytes]

### ValidityStartTime
- **Type**: typing.Optional[datetime.datetime]

### ValidityEndTime
- **Type**: typing.Optional[datetime.datetime]

### Fingerprint
- **Type**: typing.Optional[str]


# PutEventSelectorsRequest

### TrailName
- **Type**: <class 'str'>
- **Required**: Yes

### EventSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.EventSelectorUnion]]

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorUnion]]


# PutEventSelectorsResponse

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### EventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.EventSelectorOutput]
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# PutInsightSelectorsRequest

### InsightSelectors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.InsightSelector]
- **Required**: Yes

### TrailName
- **Type**: typing.Optional[str]

### EventDataStore
- **Type**: typing.Optional[str]

### InsightsDestination
- **Type**: typing.Optional[str]


# PutInsightSelectorsResponse

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### InsightSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.InsightSelector]
- **Required**: Yes

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### InsightsDestination
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### DelegatedAdminResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# Query

### QueryId
- **Type**: typing.Optional[str]

### QueryStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FINISHED', 'QUEUED', 'RUNNING', 'TIMED_OUT']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# QueryStatistics

### ResultsCount
- **Type**: typing.Optional[int]

### TotalResultsCount
- **Type**: typing.Optional[int]

### BytesScanned
- **Type**: typing.Optional[int]


# QueryStatisticsForDescribeQuery

### EventsMatched
- **Type**: typing.Optional[int]

### EventsScanned
- **Type**: typing.Optional[int]

### BytesScanned
- **Type**: typing.Optional[int]

### ExecutionTimeInMillis
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# RefreshSchedule

### Frequency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.RefreshScheduleFrequency]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TimeOfDay
- **Type**: typing.Optional[str]


# RefreshScheduleFrequency

### Unit
- **Type**: typing.Optional[typing.Literal['DAYS', 'HOURS']]

### Value
- **Type**: typing.Optional[int]


# RegisterOrganizationDelegatedAdminRequest

### MemberAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagsList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]
- **Required**: Yes


# RequestWidget

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### ViewProperties
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### QueryParameters
- **Type**: typing.Optional[typing.Sequence[str]]


# Resource

### ResourceType
- **Type**: typing.Optional[str]

### ResourceName
- **Type**: typing.Optional[str]


# ResourceTag

### ResourceId
- **Type**: typing.Optional[str]

### TagsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Tag]]


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


# RestoreEventDataStoreRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreEventDataStoreResponse

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'ENABLED', 'PENDING_DELETION', 'STARTING_INGESTION', 'STOPPED_INGESTION', 'STOPPING_INGESTION']
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutput]
- **Required**: Yes

### MultiRegionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OrganizationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### TerminationProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### BillingMode
- **Type**: typing.Literal['EXTENDABLE_RETENTION_PRICING', 'FIXED_RETENTION_PRICING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# S3ImportSource

### S3LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketRegion
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# SearchSampleQueriesRequest

### SearchPhrase
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchSampleQueriesResponse

### SearchResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.SearchSampleQueriesSearchResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchSampleQueriesSearchResult

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SQL
- **Type**: typing.Optional[str]

### Relevance
- **Type**: typing.Optional[float]


# SourceConfig

### ApplyToAllRegions
- **Type**: typing.Optional[bool]

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutput]]


# StartDashboardRefreshRequest

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryParameterValues
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartDashboardRefreshResponse

### RefreshId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# StartEventDataStoreIngestionRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# StartImportRequest

### Destinations
- **Type**: typing.Optional[typing.Sequence[str]]

### ImportSource
- **Type**: <class 'NoneType'>

### StartEventTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### EndEventTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.Timestamp]

### ImportId
- **Type**: typing.Optional[str]


# StartImportResponse

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[str]
- **Required**: Yes

### ImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportSource'>
- **Required**: Yes

### StartEventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndEventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# StartLoggingRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartQueryRequest

### QueryStatement
- **Type**: typing.Optional[str]

### DeliveryS3Uri
- **Type**: typing.Optional[str]

### QueryAlias
- **Type**: typing.Optional[str]

### QueryParameters
- **Type**: typing.Optional[typing.Sequence[str]]

### EventDataStoreOwnerAccountId
- **Type**: typing.Optional[str]


# StartQueryResponse

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### EventDataStoreOwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# StopEventDataStoreIngestionRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# StopImportRequest

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes


# StopImportResponse

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportSource'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[str]
- **Required**: Yes

### ImportStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartEventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndEventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# StopLoggingRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Trail

### Name
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]

### S3KeyPrefix
- **Type**: typing.Optional[str]

### SnsTopicName
- **Type**: typing.Optional[str]

### SnsTopicARN
- **Type**: typing.Optional[str]

### IncludeGlobalServiceEvents
- **Type**: typing.Optional[bool]

### IsMultiRegionTrail
- **Type**: typing.Optional[bool]

### HomeRegion
- **Type**: typing.Optional[str]

### TrailARN
- **Type**: typing.Optional[str]

### LogFileValidationEnabled
- **Type**: typing.Optional[bool]

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### CloudWatchLogsRoleArn
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### HasCustomEventSelectors
- **Type**: typing.Optional[bool]

### HasInsightSelectors
- **Type**: typing.Optional[bool]

### IsOrganizationTrail
- **Type**: typing.Optional[bool]


# TrailInfo

### TrailARN
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### HomeRegion
- **Type**: typing.Optional[str]


# UpdateChannelRequest

### Channel
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.Destination]]

### Name
- **Type**: typing.Optional[str]


# UpdateChannelResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.Destination]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDashboardRequest

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Widgets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.RequestWidget]]

### RefreshSchedule
- **Type**: <class 'NoneType'>

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdateEventDataStoreRequest

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorUnion]]

### MultiRegionEnabled
- **Type**: typing.Optional[bool]

### OrganizationEnabled
- **Type**: typing.Optional[bool]

### RetentionPeriod
- **Type**: typing.Optional[int]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### BillingMode
- **Type**: typing.Optional[typing.Literal['EXTENDABLE_RETENTION_PRICING', 'FIXED_RETENTION_PRICING']]


# UpdateEventDataStoreResponse

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'ENABLED', 'PENDING_DELETION', 'STARTING_INGESTION', 'STOPPED_INGESTION', 'STOPPING_INGESTION']
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutput]
- **Required**: Yes

### MultiRegionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OrganizationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### RetentionPeriod
- **Type**: <class 'int'>
- **Required**: Yes

### TerminationProtectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### BillingMode
- **Type**: typing.Literal['EXTENDABLE_RETENTION_PRICING', 'FIXED_RETENTION_PRICING']
- **Required**: Yes

### FederationStatus
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']
- **Required**: Yes

### FederationRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrailRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: typing.Optional[str]

### S3KeyPrefix
- **Type**: typing.Optional[str]

### SnsTopicName
- **Type**: typing.Optional[str]

### IncludeGlobalServiceEvents
- **Type**: typing.Optional[bool]

### IsMultiRegionTrail
- **Type**: typing.Optional[bool]

### EnableLogFileValidation
- **Type**: typing.Optional[bool]

### CloudWatchLogsLogGroupArn
- **Type**: typing.Optional[str]

### CloudWatchLogsRoleArn
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### IsOrganizationTrail
- **Type**: typing.Optional[bool]


# UpdateTrailResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicARN
- **Type**: <class 'str'>
- **Required**: Yes

### IncludeGlobalServiceEvents
- **Type**: <class 'bool'>
- **Required**: Yes

### IsMultiRegionTrail
- **Type**: <class 'bool'>
- **Required**: Yes

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### LogFileValidationEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CloudWatchLogsLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### IsOrganizationTrail
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadata'>
- **Required**: Yes


# Widget

### QueryAlias
- **Type**: typing.Optional[str]

### QueryStatement
- **Type**: typing.Optional[str]

### QueryParameters
- **Type**: typing.Optional[typing.List[str]]

### ViewProperties
- **Type**: typing.Optional[typing.Dict[str, str]]



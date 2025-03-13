# Cloudtrail Classes

# AddTagsRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagsList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]
- **Required**: Yes


# AdvancedEventSelectorOutputTypeDef

### FieldSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedFieldSelectorOutputTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AdvancedEventSelectorTypeDef

### FieldSelectors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedFieldSelectorUnionTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# AdvancedEventSelectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AdvancedFieldSelectorOutputTypeDef

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


# AdvancedFieldSelectorTypeDef

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


# AdvancedFieldSelectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelQueryRequestTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### EventDataStore
- **Type**: typing.Optional[str]

### EventDataStoreOwnerAccountId
- **Type**: typing.Optional[str]


# CancelQueryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChannelTypeDef

### ChannelArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# CreateChannelRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.DestinationTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]]


# CreateChannelResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.DestinationTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDashboardRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RefreshSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.RefreshScheduleTypeDef]

### TagsList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]

### Widgets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.RequestWidgetTypeDef]]


# CreateEventDataStoreRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorUnionTypeDef]]

### MultiRegionEnabled
- **Type**: typing.Optional[bool]

### OrganizationEnabled
- **Type**: typing.Optional[bool]

### RetentionPeriod
- **Type**: typing.Optional[int]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]

### TagsList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### StartIngestion
- **Type**: typing.Optional[bool]

### BillingMode
- **Type**: typing.Optional[typing.Literal['EXTENDABLE_RETENTION_PRICING', 'FIXED_RETENTION_PRICING']]


# CreateEventDataStoreResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutputTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrailRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]]


# CreateTrailResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DashboardDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataResourceOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataResourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteChannelRequestTypeDef

### Channel
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDashboardRequestTypeDef

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventDataStoreRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrailRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterOrganizationDelegatedAdminRequestTypeDef

### DelegatedAdminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQueryRequestTypeDef

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


# DescribeQueryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.QueryStatisticsForDescribeQueryTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrailsRequestTypeDef

### trailNameList
- **Type**: typing.Optional[typing.Sequence[str]]

### includeShadowTrails
- **Type**: typing.Optional[bool]


# DescribeTrailsResponseTypeDef

### trailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.TrailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisableFederationRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# DisableFederationResponseTypeDef

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### FederationStatus
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableFederationRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes

### FederationRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# EnableFederationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventDataStoreTypeDef

### EventDataStoreArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'ENABLED', 'PENDING_DELETION', 'STARTING_INGESTION', 'STOPPED_INGESTION', 'STOPPING_INGESTION']]

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutputTypeDef]]

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


# EventSelectorOutputTypeDef

### ReadWriteType
- **Type**: typing.Optional[typing.Literal['All', 'ReadOnly', 'WriteOnly']]

### IncludeManagementEvents
- **Type**: typing.Optional[bool]

### DataResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.DataResourceOutputTypeDef]]

### ExcludeManagementEventSources
- **Type**: typing.Optional[typing.List[str]]


# EventSelectorTypeDef

### ReadWriteType
- **Type**: typing.Optional[typing.Literal['All', 'ReadOnly', 'WriteOnly']]

### IncludeManagementEvents
- **Type**: typing.Optional[bool]

### DataResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.DataResourceUnionTypeDef]]

### ExcludeManagementEventSources
- **Type**: typing.Optional[typing.Sequence[str]]


# EventSelectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GenerateQueryRequestTypeDef

### EventDataStores
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Prompt
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateQueryResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelRequestTypeDef

### Channel
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.SourceConfigTypeDef'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.DestinationTypeDef]
- **Required**: Yes

### IngestionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.IngestionStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDashboardRequestTypeDef

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventDataStoreRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventDataStoreResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutputTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.PartitionKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventSelectorsRequestTypeDef

### TrailName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventSelectorsResponseTypeDef

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### EventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.EventSelectorOutputTypeDef]
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportRequestTypeDef

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportResponseTypeDef

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[str]
- **Required**: Yes

### ImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportSourceTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightSelectorsRequestTypeDef

### TrailName
- **Type**: typing.Optional[str]

### EventDataStore
- **Type**: typing.Optional[str]


# GetInsightSelectorsResponseTypeDef

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### InsightSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.InsightSelectorTypeDef]
- **Required**: Yes

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### InsightsDestination
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryResultsRequestTypeDef

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


# GetQueryResultsResponseTypeDef

### QueryStatus
- **Type**: typing.Literal['CANCELLED', 'FAILED', 'FINISHED', 'QUEUED', 'RUNNING', 'TIMED_OUT']
- **Required**: Yes

### QueryStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.QueryStatisticsTypeDef'>
- **Required**: Yes

### QueryResultRows
- **Type**: typing.List[typing.List[typing.Dict[str, str]]]
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrailRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrailResponseTypeDef

### Trail
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.TrailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrailStatusRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrailStatusResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportFailureListItemTypeDef

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


# ImportSourceTypeDef

### S3
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.S3ImportSourceTypeDef'>
- **Required**: Yes


# ImportStatisticsTypeDef

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


# ImportsListItemTypeDef

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


# IngestionStatusTypeDef

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


# InsightSelectorTypeDef

### InsightType
- **Type**: typing.Optional[typing.Literal['ApiCallRateInsight', 'ApiErrorRateInsight']]


# ListChannelsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.ChannelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDashboardsResponseTypeDef

### Dashboards
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.DashboardDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventDataStoresRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventDataStoresResponseTypeDef

### EventDataStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.EventDataStoreTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportFailuresRequestPaginateTypeDef

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfigTypeDef]


# ListImportFailuresRequestTypeDef

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListImportFailuresResponseTypeDef

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.ImportFailureListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImportsRequestPaginateTypeDef

### Destination
- **Type**: typing.Optional[str]

### ImportStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfigTypeDef]


# ListImportsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### Destination
- **Type**: typing.Optional[str]

### ImportStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED']]

### NextToken
- **Type**: typing.Optional[str]


# ListImportsResponseTypeDef

### Imports
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.ImportsListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsMetricDataRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### Period
- **Type**: typing.Optional[int]

### DataType
- **Type**: typing.Optional[typing.Literal['FillWithZeros', 'NonZeroData']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsMetricDataResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPublicKeysRequestPaginateTypeDef

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfigTypeDef]


# ListPublicKeysRequestTypeDef

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### NextToken
- **Type**: typing.Optional[str]


# ListPublicKeysResponseTypeDef

### PublicKeyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.PublicKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQueriesRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### QueryStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FINISHED', 'QUEUED', 'RUNNING', 'TIMED_OUT']]


# ListQueriesResponseTypeDef

### Queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.QueryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsRequestPaginateTypeDef

### ResourceIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfigTypeDef]


# ListTagsRequestTypeDef

### ResourceIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsResponseTypeDef

### ResourceTagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrailsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfigTypeDef]


# ListTrailsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListTrailsResponseTypeDef

### Trails
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.TrailInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LookupAttributeTypeDef

### AttributeKey
- **Type**: typing.Literal['AccessKeyId', 'EventId', 'EventName', 'EventSource', 'ReadOnly', 'ResourceName', 'ResourceType', 'Username']
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes


# LookupEventsRequestPaginateTypeDef

### LookupAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.LookupAttributeTypeDef]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EventCategory
- **Type**: typing.Optional[typing.Literal['insight']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.PaginatorConfigTypeDef]


# LookupEventsRequestTypeDef

### LookupAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.LookupAttributeTypeDef]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EventCategory
- **Type**: typing.Optional[typing.Literal['insight']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# LookupEventsResponseTypeDef

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PartitionKeyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PublicKeyTypeDef

### Value
- **Type**: typing.Optional[bytes]

### ValidityStartTime
- **Type**: typing.Optional[datetime.datetime]

### ValidityEndTime
- **Type**: typing.Optional[datetime.datetime]

### Fingerprint
- **Type**: typing.Optional[str]


# PutEventSelectorsRequestTypeDef

### TrailName
- **Type**: <class 'str'>
- **Required**: Yes

### EventSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.EventSelectorUnionTypeDef]]

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorUnionTypeDef]]


# PutEventSelectorsResponseTypeDef

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### EventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.EventSelectorOutputTypeDef]
- **Required**: Yes

### AdvancedEventSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutInsightSelectorsRequestTypeDef

### InsightSelectors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.InsightSelectorTypeDef]
- **Required**: Yes

### TrailName
- **Type**: typing.Optional[str]

### EventDataStore
- **Type**: typing.Optional[str]

### InsightsDestination
- **Type**: typing.Optional[str]


# PutInsightSelectorsResponseTypeDef

### TrailARN
- **Type**: <class 'str'>
- **Required**: Yes

### InsightSelectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.InsightSelectorTypeDef]
- **Required**: Yes

### EventDataStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### InsightsDestination
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutResourcePolicyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryStatisticsForDescribeQueryTypeDef

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


# QueryStatisticsTypeDef

### ResultsCount
- **Type**: typing.Optional[int]

### TotalResultsCount
- **Type**: typing.Optional[int]

### BytesScanned
- **Type**: typing.Optional[int]


# QueryTypeDef

### QueryId
- **Type**: typing.Optional[str]

### QueryStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'FAILED', 'FINISHED', 'QUEUED', 'RUNNING', 'TIMED_OUT']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# RefreshScheduleFrequencyTypeDef

### Unit
- **Type**: typing.Optional[typing.Literal['DAYS', 'HOURS']]

### Value
- **Type**: typing.Optional[int]


# RefreshScheduleTypeDef

### Frequency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.RefreshScheduleFrequencyTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TimeOfDay
- **Type**: typing.Optional[str]


# RegisterOrganizationDelegatedAdminRequestTypeDef

### MemberAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagsList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]
- **Required**: Yes


# RequestWidgetTypeDef

### QueryStatement
- **Type**: <class 'str'>
- **Required**: Yes

### ViewProperties
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### QueryParameters
- **Type**: typing.Optional[typing.Sequence[str]]


# ResourceTagTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### TagsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.TagTypeDef]]


# ResourceTypeDef

### ResourceType
- **Type**: typing.Optional[str]

### ResourceName
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


# RestoreEventDataStoreRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# RestoreEventDataStoreResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3ImportSourceTypeDef

### S3LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketRegion
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# SearchSampleQueriesRequestTypeDef

### SearchPhrase
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchSampleQueriesResponseTypeDef

### SearchResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.SearchSampleQueriesSearchResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchSampleQueriesSearchResultTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SQL
- **Type**: typing.Optional[str]

### Relevance
- **Type**: typing.Optional[float]


# SourceConfigTypeDef

### ApplyToAllRegions
- **Type**: typing.Optional[bool]

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutputTypeDef]]


# StartDashboardRefreshRequestTypeDef

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryParameterValues
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartDashboardRefreshResponseTypeDef

### RefreshId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartEventDataStoreIngestionRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# StartImportRequestTypeDef

### Destinations
- **Type**: typing.Optional[typing.Sequence[str]]

### ImportSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.ImportSourceTypeDef]

### StartEventTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### EndEventTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.TimestampTypeDef]

### ImportId
- **Type**: typing.Optional[str]


# StartImportResponseTypeDef

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[str]
- **Required**: Yes

### ImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportSourceTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartLoggingRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartQueryRequestTypeDef

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


# StartQueryResponseTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### EventDataStoreOwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopEventDataStoreIngestionRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes


# StopImportRequestTypeDef

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes


# StopImportResponseTypeDef

### ImportId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportSourceTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ImportStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopLoggingRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrailInfoTypeDef

### TrailARN
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### HomeRegion
- **Type**: typing.Optional[str]


# TrailTypeDef

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


# UpdateChannelRequestTypeDef

### Channel
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.DestinationTypeDef]]

### Name
- **Type**: typing.Optional[str]


# UpdateChannelResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.DestinationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDashboardRequestTypeDef

### DashboardId
- **Type**: <class 'str'>
- **Required**: Yes

### Widgets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.RequestWidgetTypeDef]]

### RefreshSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudtrail_classes.RefreshScheduleTypeDef]

### TerminationProtectionEnabled
- **Type**: typing.Optional[bool]


# UpdateEventDataStoreRequestTypeDef

### EventDataStore
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AdvancedEventSelectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorUnionTypeDef]]

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


# UpdateEventDataStoreResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_classes.AdvancedEventSelectorOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrailRequestTypeDef

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


# UpdateTrailResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WidgetTypeDef

### QueryAlias
- **Type**: typing.Optional[str]

### QueryStatement
- **Type**: typing.Optional[str]

### QueryParameters
- **Type**: typing.Optional[typing.List[str]]

### ViewProperties
- **Type**: typing.Optional[typing.Dict[str, str]]



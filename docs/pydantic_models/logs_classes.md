# logs_classes

# AccountPolicyTypeDef

### policyName
- **Type**: typing.Optional[str]

### policyDocument
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[int]

### policyType
- **Type**: typing.Optional[typing.Literal['DATA_PROTECTION_POLICY', 'SUBSCRIPTION_FILTER_POLICY']]

### scope
- **Type**: typing.Optional[typing.Literal['ALL']]

### selectionCriteria
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]


# AnomalyDetectorTypeDef

### anomalyDetectorArn
- **Type**: typing.Optional[str]

### detectorName
- **Type**: typing.Optional[str]

### logGroupArnList
- **Type**: typing.Optional[typing.List[str]]

### evaluationFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MIN', 'FIVE_MIN', 'ONE_HOUR', 'ONE_MIN', 'TEN_MIN', 'THIRTY_MIN']]

### filterPattern
- **Type**: typing.Optional[str]

### anomalyDetectorStatus
- **Type**: typing.Optional[typing.Literal['ANALYZING', 'DELETED', 'FAILED', 'INITIALIZING', 'PAUSED', 'TRAINING']]

### kmsKeyId
- **Type**: typing.Optional[str]

### creationTimeStamp
- **Type**: typing.Optional[int]

### lastModifiedTimeStamp
- **Type**: typing.Optional[int]

### anomalyVisibilityTime
- **Type**: typing.Optional[int]


# AnomalyTypeDef

### anomalyId
- **Type**: <class 'str'>
- **Required**: Yes

### patternId
- **Type**: <class 'str'>
- **Required**: Yes

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### patternString
- **Type**: <class 'str'>
- **Required**: Yes

### firstSeen
- **Type**: <class 'int'>
- **Required**: Yes

### lastSeen
- **Type**: <class 'int'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### active
- **Type**: <class 'bool'>
- **Required**: Yes

### state
- **Type**: typing.Literal['Active', 'Baseline', 'Suppressed']
- **Required**: Yes

### histogram
- **Type**: typing.Dict[str, int]
- **Required**: Yes

### logSamples
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.LogEventTypeDef]
- **Required**: Yes

### patternTokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.PatternTokenTypeDef]
- **Required**: Yes

### logGroupArnList
- **Type**: typing.List[str]
- **Required**: Yes

### patternRegex
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[str]

### suppressed
- **Type**: typing.Optional[bool]

### suppressedDate
- **Type**: typing.Optional[int]

### suppressedUntil
- **Type**: typing.Optional[int]

### isPatternLevelSuppression
- **Type**: typing.Optional[bool]


# AssociateKmsKeyRequestRequestTypeDef

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### logGroupName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelExportTaskRequestRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDeliveryRequestRequestTypeDef

### deliverySourceName
- **Type**: <class 'str'>
- **Required**: Yes

### deliveryDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDeliveryResponseTypeDef

### delivery
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliveryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExportTaskRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### fromTime
- **Type**: <class 'int'>
- **Required**: Yes

### to
- **Type**: <class 'int'>
- **Required**: Yes

### destination
- **Type**: <class 'str'>
- **Required**: Yes

### taskName
- **Type**: typing.Optional[str]

### logStreamNamePrefix
- **Type**: typing.Optional[str]

### destinationPrefix
- **Type**: typing.Optional[str]


# CreateExportTaskResponseTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLogAnomalyDetectorRequestRequestTypeDef

### logGroupArnList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### detectorName
- **Type**: typing.Optional[str]

### evaluationFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MIN', 'FIVE_MIN', 'ONE_HOUR', 'ONE_MIN', 'TEN_MIN', 'THIRTY_MIN']]

### filterPattern
- **Type**: typing.Optional[str]

### kmsKeyId
- **Type**: typing.Optional[str]

### anomalyVisibilityTime
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLogAnomalyDetectorResponseTypeDef

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLogGroupRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### logGroupClass
- **Type**: typing.Optional[typing.Literal['INFREQUENT_ACCESS', 'STANDARD']]


# CreateLogStreamRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccountPolicyRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['DATA_PROTECTION_POLICY', 'SUBSCRIPTION_FILTER_POLICY']
- **Required**: Yes


# DeleteDataProtectionPolicyRequestRequestTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryDestinationPolicyRequestRequestTypeDef

### deliveryDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryDestinationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliverySourceRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDestinationRequestRequestTypeDef

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogAnomalyDetectorRequestRequestTypeDef

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogGroupRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogStreamRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMetricFilterRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueryDefinitionRequestRequestTypeDef

### queryDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueryDefinitionResponseTypeDef

### success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcePolicyRequestRequestTypeDef

### policyName
- **Type**: typing.Optional[str]


# DeleteRetentionPolicyRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionFilterRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeliveryDestinationConfigurationTypeDef

### destinationResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeliveryDestinationTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### deliveryDestinationType
- **Type**: typing.Optional[typing.Literal['CWL', 'FH', 'S3']]

### outputFormat
- **Type**: typing.Optional[typing.Literal['json', 'parquet', 'plain', 'raw', 'w3c']]

### deliveryDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.DeliveryDestinationConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeliverySourceTypeDef

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### service
- **Type**: typing.Optional[str]

### logType
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeliveryTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### deliverySourceName
- **Type**: typing.Optional[str]

### deliveryDestinationArn
- **Type**: typing.Optional[str]

### deliveryDestinationType
- **Type**: typing.Optional[typing.Literal['CWL', 'FH', 'S3']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DescribeAccountPoliciesRequestRequestTypeDef

### policyType
- **Type**: typing.Literal['DATA_PROTECTION_POLICY', 'SUBSCRIPTION_FILTER_POLICY']
- **Required**: Yes

### policyName
- **Type**: typing.Optional[str]

### accountIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeAccountPoliciesResponseTypeDef

### accountPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.AccountPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeliveriesRequestDescribeDeliveriesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeDeliveriesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliveriesResponseTypeDef

### deliveries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.DeliveryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeliveryDestinationsRequestDescribeDeliveryDestinationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeDeliveryDestinationsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliveryDestinationsResponseTypeDef

### deliveryDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.DeliveryDestinationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeliverySourcesRequestDescribeDeliverySourcesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeDeliverySourcesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliverySourcesResponseTypeDef

### deliverySources
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.DeliverySourceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDestinationsRequestDescribeDestinationsPaginateTypeDef

### DestinationNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeDestinationsRequestRequestTypeDef

### DestinationNamePrefix
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDestinationsResponseTypeDef

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.DestinationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef

### taskId
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'PENDING_CANCEL', 'RUNNING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeExportTasksRequestRequestTypeDef

### taskId
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'PENDING_CANCEL', 'RUNNING']]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeExportTasksResponseTypeDef

### exportTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.ExportTaskTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLogGroupsRequestDescribeLogGroupsPaginateTypeDef

### accountIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### logGroupNamePrefix
- **Type**: typing.Optional[str]

### logGroupNamePattern
- **Type**: typing.Optional[str]

### includeLinkedAccounts
- **Type**: typing.Optional[bool]

### logGroupClass
- **Type**: typing.Optional[typing.Literal['INFREQUENT_ACCESS', 'STANDARD']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeLogGroupsRequestRequestTypeDef

### accountIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### logGroupNamePrefix
- **Type**: typing.Optional[str]

### logGroupNamePattern
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### includeLinkedAccounts
- **Type**: typing.Optional[bool]

### logGroupClass
- **Type**: typing.Optional[typing.Literal['INFREQUENT_ACCESS', 'STANDARD']]


# DescribeLogGroupsResponseTypeDef

### logGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.LogGroupTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLogStreamsRequestDescribeLogStreamsPaginateTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### logGroupIdentifier
- **Type**: typing.Optional[str]

### logStreamNamePrefix
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['LastEventTime', 'LogStreamName']]

### descending
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeLogStreamsRequestRequestTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### logGroupIdentifier
- **Type**: typing.Optional[str]

### logStreamNamePrefix
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['LastEventTime', 'LogStreamName']]

### descending
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeLogStreamsResponseTypeDef

### logStreams
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.LogStreamTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetricFiltersRequestDescribeMetricFiltersPaginateTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### filterNamePrefix
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### metricNamespace
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeMetricFiltersRequestRequestTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### filterNamePrefix
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### metricName
- **Type**: typing.Optional[str]

### metricNamespace
- **Type**: typing.Optional[str]


# DescribeMetricFiltersResponseTypeDef

### metricFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.MetricFilterTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeQueriesRequestDescribeQueriesPaginateTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Complete', 'Failed', 'Running', 'Scheduled', 'Timeout', 'Unknown']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeQueriesRequestRequestTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Complete', 'Failed', 'Running', 'Scheduled', 'Timeout', 'Unknown']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeQueriesResponseTypeDef

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.QueryInfoTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeQueryDefinitionsRequestRequestTypeDef

### queryDefinitionNamePrefix
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeQueryDefinitionsResponseTypeDef

### queryDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.QueryDefinitionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourcePoliciesRequestDescribeResourcePoliciesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeResourcePoliciesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeResourcePoliciesResponseTypeDef

### resourcePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.ResourcePolicyTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSubscriptionFiltersRequestDescribeSubscriptionFiltersPaginateTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeSubscriptionFiltersRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterNamePrefix
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeSubscriptionFiltersResponseTypeDef

### subscriptionFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.SubscriptionFilterTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

### destinationName
- **Type**: typing.Optional[str]

### targetArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### accessPolicy
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[int]


# DisassociateKmsKeyRequestRequestTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportTaskExecutionInfoTypeDef

### creationTime
- **Type**: typing.Optional[int]

### completionTime
- **Type**: typing.Optional[int]


# ExportTaskStatusTypeDef

### code
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'PENDING_CANCEL', 'RUNNING']]

### message
- **Type**: typing.Optional[str]


# ExportTaskTypeDef

### taskId
- **Type**: typing.Optional[str]

### taskName
- **Type**: typing.Optional[str]

### logGroupName
- **Type**: typing.Optional[str]

### to
- **Type**: typing.Optional[int]

### destination
- **Type**: typing.Optional[str]

### destinationPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ExportTaskStatusTypeDef]

### executionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ExportTaskExecutionInfoTypeDef]


# FilterLogEventsRequestFilterLogEventsPaginateTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### logGroupIdentifier
- **Type**: typing.Optional[str]

### logStreamNames
- **Type**: typing.Optional[typing.Sequence[str]]

### logStreamNamePrefix
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[int]

### endTime
- **Type**: typing.Optional[int]

### filterPattern
- **Type**: typing.Optional[str]

### interleaved
- **Type**: typing.Optional[bool]

### unmask
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# FilterLogEventsRequestRequestTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### logGroupIdentifier
- **Type**: typing.Optional[str]

### logStreamNames
- **Type**: typing.Optional[typing.Sequence[str]]

### logStreamNamePrefix
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[int]

### endTime
- **Type**: typing.Optional[int]

### filterPattern
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### interleaved
- **Type**: typing.Optional[bool]

### unmask
- **Type**: typing.Optional[bool]


# FilterLogEventsResponseTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.FilteredLogEventTypeDef]
- **Required**: Yes

### searchedLogStreams
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.SearchedLogStreamTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FilteredLogEventTypeDef

### logStreamName
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]

### ingestionTime
- **Type**: typing.Optional[int]

### eventId
- **Type**: typing.Optional[str]


# GetDataProtectionPolicyRequestRequestTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataProtectionPolicyResponseTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeliveryDestinationPolicyRequestRequestTypeDef

### deliveryDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliveryDestinationPolicyResponseTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeliveryDestinationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliveryDestinationResponseTypeDef

### deliveryDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliveryDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeliveryRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliveryResponseTypeDef

### delivery
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliveryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeliverySourceRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliverySourceResponseTypeDef

### deliverySource
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliverySourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLogAnomalyDetectorRequestRequestTypeDef

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLogAnomalyDetectorResponseTypeDef

### detectorName
- **Type**: <class 'str'>
- **Required**: Yes

### logGroupArnList
- **Type**: typing.List[str]
- **Required**: Yes

### evaluationFrequency
- **Type**: typing.Literal['FIFTEEN_MIN', 'FIVE_MIN', 'ONE_HOUR', 'ONE_MIN', 'TEN_MIN', 'THIRTY_MIN']
- **Required**: Yes

### filterPattern
- **Type**: <class 'str'>
- **Required**: Yes

### anomalyDetectorStatus
- **Type**: typing.Literal['ANALYZING', 'DELETED', 'FAILED', 'INITIALIZING', 'PAUSED', 'TRAINING']
- **Required**: Yes

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### creationTimeStamp
- **Type**: <class 'int'>
- **Required**: Yes

### lastModifiedTimeStamp
- **Type**: <class 'int'>
- **Required**: Yes

### anomalyVisibilityTime
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLogEventsRequestRequestTypeDef

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### logGroupName
- **Type**: typing.Optional[str]

### logGroupIdentifier
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[int]

### endTime
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### startFromHead
- **Type**: typing.Optional[bool]

### unmask
- **Type**: typing.Optional[bool]


# GetLogEventsResponseTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.OutputLogEventTypeDef]
- **Required**: Yes

### nextForwardToken
- **Type**: <class 'str'>
- **Required**: Yes

### nextBackwardToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLogGroupFieldsRequestRequestTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### time
- **Type**: typing.Optional[int]

### logGroupIdentifier
- **Type**: typing.Optional[str]


# GetLogGroupFieldsResponseTypeDef

### logGroupFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.LogGroupFieldTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLogRecordRequestRequestTypeDef

### logRecordPointer
- **Type**: <class 'str'>
- **Required**: Yes

### unmask
- **Type**: typing.Optional[bool]


# GetLogRecordResponseTypeDef

### logRecord
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryResultsRequestRequestTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryResultsResponseTypeDef

### results
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.logs_classes.ResultFieldTypeDef]]
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.QueryStatisticsTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Cancelled', 'Complete', 'Failed', 'Running', 'Scheduled', 'Timeout', 'Unknown']
- **Required**: Yes

### encryptionKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputLogEventTypeDef

### timestamp
- **Type**: <class 'int'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# ListAnomaliesRequestListAnomaliesPaginateTypeDef

### anomalyDetectorArn
- **Type**: typing.Optional[str]

### suppressionState
- **Type**: typing.Optional[typing.Literal['SUPPRESSED', 'UNSUPPRESSED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# ListAnomaliesRequestRequestTypeDef

### anomalyDetectorArn
- **Type**: typing.Optional[str]

### suppressionState
- **Type**: typing.Optional[typing.Literal['SUPPRESSED', 'UNSUPPRESSED']]

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAnomaliesResponseTypeDef

### anomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.AnomalyTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLogAnomalyDetectorsRequestListLogAnomalyDetectorsPaginateTypeDef

### filterLogGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# ListLogAnomalyDetectorsRequestRequestTypeDef

### filterLogGroupArn
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLogAnomalyDetectorsResponseTypeDef

### anomalyDetectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.AnomalyDetectorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsLogGroupRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsLogGroupResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LiveTailSessionLogEventTypeDef

### logStreamName
- **Type**: typing.Optional[str]

### logGroupIdentifier
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[int]

### ingestionTime
- **Type**: typing.Optional[int]


# LiveTailSessionMetadataTypeDef

### sampled
- **Type**: typing.Optional[bool]


# LiveTailSessionStartTypeDef

### requestId
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### logGroupIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### logStreamNames
- **Type**: typing.Optional[typing.List[str]]

### logStreamNamePrefixes
- **Type**: typing.Optional[typing.List[str]]

### logEventFilterPattern
- **Type**: typing.Optional[str]


# LiveTailSessionUpdateTypeDef

### sessionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.LiveTailSessionMetadataTypeDef]

### sessionResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.logs_classes.LiveTailSessionLogEventTypeDef]]


# LogEventTypeDef

### timestamp
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]


# LogGroupFieldTypeDef

### name
- **Type**: typing.Optional[str]

### percent
- **Type**: typing.Optional[int]


# LogGroupTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[int]

### retentionInDays
- **Type**: typing.Optional[int]

### metricFilterCount
- **Type**: typing.Optional[int]

### arn
- **Type**: typing.Optional[str]

### storedBytes
- **Type**: typing.Optional[int]

### kmsKeyId
- **Type**: typing.Optional[str]

### dataProtectionStatus
- **Type**: typing.Optional[typing.Literal['ACTIVATED', 'ARCHIVED', 'DELETED', 'DISABLED']]

### inheritedProperties
- **Type**: typing.Optional[typing.List[typing.Literal['ACCOUNT_DATA_PROTECTION']]]

### logGroupClass
- **Type**: typing.Optional[typing.Literal['INFREQUENT_ACCESS', 'STANDARD']]

### logGroupArn
- **Type**: typing.Optional[str]


# LogStreamTypeDef

### logStreamName
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[int]

### firstEventTimestamp
- **Type**: typing.Optional[int]

### lastEventTimestamp
- **Type**: typing.Optional[int]

### lastIngestionTime
- **Type**: typing.Optional[int]

### uploadSequenceToken
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### storedBytes
- **Type**: typing.Optional[int]


# MetricFilterMatchRecordTypeDef

### eventNumber
- **Type**: typing.Optional[int]

### eventMessage
- **Type**: typing.Optional[str]

### extractedValues
- **Type**: typing.Optional[typing.Dict[str, str]]


# MetricFilterTypeDef

### filterName
- **Type**: typing.Optional[str]

### filterPattern
- **Type**: typing.Optional[str]

### metricTransformations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.logs_classes.MetricTransformationTypeDef]]

### creationTime
- **Type**: typing.Optional[int]

### logGroupName
- **Type**: typing.Optional[str]


# MetricTransformationTypeDef

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### metricNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### metricValue
- **Type**: <class 'str'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[float]

### dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# OutputLogEventTypeDef

### timestamp
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]

### ingestionTime
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PatternTokenTypeDef

### dynamicTokenPosition
- **Type**: typing.Optional[int]

### isDynamic
- **Type**: typing.Optional[bool]

### tokenString
- **Type**: typing.Optional[str]

### enumerations
- **Type**: typing.Optional[typing.Dict[str, int]]


# PolicyTypeDef

### deliveryDestinationPolicy
- **Type**: typing.Optional[str]


# PutAccountPolicyRequestRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['DATA_PROTECTION_POLICY', 'SUBSCRIPTION_FILTER_POLICY']
- **Required**: Yes

### scope
- **Type**: typing.Optional[typing.Literal['ALL']]

### selectionCriteria
- **Type**: typing.Optional[str]


# PutAccountPolicyResponseTypeDef

### accountPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.AccountPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDataProtectionPolicyRequestRequestTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutDataProtectionPolicyResponseTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDeliveryDestinationPolicyRequestRequestTypeDef

### deliveryDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### deliveryDestinationPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutDeliveryDestinationPolicyResponseTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDeliveryDestinationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### deliveryDestinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliveryDestinationConfigurationTypeDef'>
- **Required**: Yes

### outputFormat
- **Type**: typing.Optional[typing.Literal['json', 'parquet', 'plain', 'raw', 'w3c']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutDeliveryDestinationResponseTypeDef

### deliveryDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliveryDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDeliverySourceRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### logType
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutDeliverySourceResponseTypeDef

### deliverySource
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliverySourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDestinationPolicyRequestRequestTypeDef

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### forceUpdate
- **Type**: typing.Optional[bool]


# PutDestinationRequestRequestTypeDef

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### targetArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutDestinationResponseTypeDef

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutLogEventsRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### logEvents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.InputLogEventTypeDef]
- **Required**: Yes

### sequenceToken
- **Type**: typing.Optional[str]


# PutLogEventsResponseTypeDef

### nextSequenceToken
- **Type**: <class 'str'>
- **Required**: Yes

### rejectedLogEventsInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.RejectedLogEventsInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutMetricFilterRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterName
- **Type**: <class 'str'>
- **Required**: Yes

### filterPattern
- **Type**: <class 'str'>
- **Required**: Yes

### metricTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.MetricTransformationTypeDef]
- **Required**: Yes


# PutQueryDefinitionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryDefinitionId
- **Type**: typing.Optional[str]

### logGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]


# PutQueryDefinitionResponseTypeDef

### queryDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestRequestTypeDef

### policyName
- **Type**: typing.Optional[str]

### policyDocument
- **Type**: typing.Optional[str]


# PutResourcePolicyResponseTypeDef

### resourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRetentionPolicyRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionInDays
- **Type**: <class 'int'>
- **Required**: Yes


# PutSubscriptionFilterRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterName
- **Type**: <class 'str'>
- **Required**: Yes

### filterPattern
- **Type**: <class 'str'>
- **Required**: Yes

### destinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### distribution
- **Type**: typing.Optional[typing.Literal['ByLogStream', 'Random']]


# QueryDefinitionTypeDef

### queryDefinitionId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### queryString
- **Type**: typing.Optional[str]

### lastModified
- **Type**: typing.Optional[int]

### logGroupNames
- **Type**: typing.Optional[typing.List[str]]


# QueryInfoTypeDef

### queryId
- **Type**: typing.Optional[str]

### queryString
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Complete', 'Failed', 'Running', 'Scheduled', 'Timeout', 'Unknown']]

### createTime
- **Type**: typing.Optional[int]

### logGroupName
- **Type**: typing.Optional[str]


# QueryStatisticsTypeDef

### recordsMatched
- **Type**: typing.Optional[float]

### recordsScanned
- **Type**: typing.Optional[float]

### bytesScanned
- **Type**: typing.Optional[float]


# RejectedLogEventsInfoTypeDef

### tooNewLogEventStartIndex
- **Type**: typing.Optional[int]

### tooOldLogEventEndIndex
- **Type**: typing.Optional[int]

### expiredLogEventEndIndex
- **Type**: typing.Optional[int]


# ResourcePolicyTypeDef

### policyName
- **Type**: typing.Optional[str]

### policyDocument
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[int]


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


# ResultFieldTypeDef

### field
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# SearchedLogStreamTypeDef

### logStreamName
- **Type**: typing.Optional[str]

### searchedCompletely
- **Type**: typing.Optional[bool]


# SessionStreamingExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# SessionTimeoutExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# StartLiveTailRequestRequestTypeDef

### logGroupIdentifiers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### logStreamNames
- **Type**: typing.Optional[typing.Sequence[str]]

### logStreamNamePrefixes
- **Type**: typing.Optional[typing.Sequence[str]]

### logEventFilterPattern
- **Type**: typing.Optional[str]


# StartLiveTailResponseStreamTypeDef

### sessionStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.LiveTailSessionStartTypeDef]

### sessionUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.LiveTailSessionUpdateTypeDef]

### SessionTimeoutException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.SessionTimeoutExceptionTypeDef]

### SessionStreamingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.SessionStreamingExceptionTypeDef]


# StartLiveTailResponseTypeDef

### responseStream
- **Type**: ForwardRef('EventStream[StartLiveTailResponseStreamTypeDef]')
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartQueryRequestRequestTypeDef

### startTime
- **Type**: <class 'int'>
- **Required**: Yes

### endTime
- **Type**: <class 'int'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### logGroupName
- **Type**: typing.Optional[str]

### logGroupNames
- **Type**: typing.Optional[typing.Sequence[str]]

### logGroupIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### limit
- **Type**: typing.Optional[int]


# StartQueryResponseTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopQueryRequestRequestTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# StopQueryResponseTypeDef

### success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubscriptionFilterTypeDef

### filterName
- **Type**: typing.Optional[str]

### logGroupName
- **Type**: typing.Optional[str]

### filterPattern
- **Type**: typing.Optional[str]

### destinationArn
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### distribution
- **Type**: typing.Optional[typing.Literal['ByLogStream', 'Random']]

### creationTime
- **Type**: typing.Optional[int]


# SuppressionPeriodTypeDef

### value
- **Type**: typing.Optional[int]

### suppressionUnit
- **Type**: typing.Optional[typing.Literal['HOURS', 'MINUTES', 'SECONDS']]


# TagLogGroupRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestMetricFilterRequestRequestTypeDef

### filterPattern
- **Type**: <class 'str'>
- **Required**: Yes

### logEventMessages
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TestMetricFilterResponseTypeDef

### matches
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.MetricFilterMatchRecordTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagLogGroupRequestRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnomalyRequestRequestTypeDef

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### anomalyId
- **Type**: typing.Optional[str]

### patternId
- **Type**: typing.Optional[str]

### suppressionType
- **Type**: typing.Optional[typing.Literal['INFINITE', 'LIMITED']]

### suppressionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.SuppressionPeriodTypeDef]


# UpdateLogAnomalyDetectorRequestRequestTypeDef

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### evaluationFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MIN', 'FIVE_MIN', 'ONE_HOUR', 'ONE_MIN', 'TEN_MIN', 'THIRTY_MIN']]

### filterPattern
- **Type**: typing.Optional[str]

### anomalyVisibilityTime
- **Type**: typing.Optional[int]



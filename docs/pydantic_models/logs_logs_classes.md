# Logs Logs Classes

# AccountPolicy

### policyName
- **Type**: typing.Optional[str]

### policyDocument
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[int]

### policyType
- **Type**: typing.Optional[typing.Literal['DATA_PROTECTION_POLICY', 'FIELD_INDEX_POLICY', 'SUBSCRIPTION_FILTER_POLICY', 'TRANSFORMER_POLICY']]

### scope
- **Type**: typing.Optional[typing.Literal['ALL']]

### selectionCriteria
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]


# AddKeyEntry

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### overwriteIfExists
- **Type**: typing.Optional[bool]


# AddKeys

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.AddKeyEntry]
- **Required**: Yes


# AddKeysOutput

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.AddKeyEntry]
- **Required**: Yes


# Anomaly

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.LogEvent]
- **Required**: Yes

### patternTokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.PatternToken]
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


# AnomalyDetector

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


# AssociateKmsKeyRequest

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

# CSV

### quoteCharacter
- **Type**: typing.Optional[str]

### delimiter
- **Type**: typing.Optional[str]

### columns
- **Type**: typing.Optional[typing.List[str]]

### source
- **Type**: typing.Optional[str]


# CSVOutput

### quoteCharacter
- **Type**: typing.Optional[str]

### delimiter
- **Type**: typing.Optional[str]

### columns
- **Type**: typing.Optional[typing.List[str]]

### source
- **Type**: typing.Optional[str]


# CancelExportTaskRequest

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationTemplate

### service
- **Type**: typing.Optional[str]

### logType
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]

### deliveryDestinationType
- **Type**: typing.Optional[typing.Literal['CWL', 'FH', 'S3']]

### defaultDeliveryConfigValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ConfigurationTemplateDeliveryConfigValues]

### allowedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.RecordField]]

### allowedOutputFormats
- **Type**: typing.Optional[typing.List[typing.Literal['json', 'parquet', 'plain', 'raw', 'w3c']]]

### allowedActionForAllowVendedLogsDeliveryForResource
- **Type**: typing.Optional[str]

### allowedFieldDelimiters
- **Type**: typing.Optional[typing.List[str]]

### allowedSuffixPathFields
- **Type**: typing.Optional[typing.List[str]]


# ConfigurationTemplateDeliveryConfigValues

### recordFields
- **Type**: typing.Optional[typing.List[str]]

### fieldDelimiter
- **Type**: typing.Optional[str]

### s3DeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.S3DeliveryConfiguration]


# CopyValue

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.CopyValueEntry]
- **Required**: Yes


# CopyValueEntry

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### overwriteIfExists
- **Type**: typing.Optional[bool]


# CopyValueOutput

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.CopyValueEntry]
- **Required**: Yes


# CreateDeliveryRequest

### deliverySourceName
- **Type**: <class 'str'>
- **Required**: Yes

### deliveryDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### recordFields
- **Type**: typing.Optional[typing.List[str]]

### fieldDelimiter
- **Type**: typing.Optional[str]

### s3DeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.S3DeliveryConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDeliveryResponse

### delivery
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.Delivery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExportTaskRequest

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


# CreateExportTaskResponse

### taskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLogAnomalyDetectorRequest

### logGroupArnList
- **Type**: typing.List[str]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLogAnomalyDetectorResponse

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLogGroupRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### logGroupClass
- **Type**: typing.Optional[typing.Literal['INFREQUENT_ACCESS', 'STANDARD']]


# CreateLogStreamRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# DateTimeConverter

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### matchPatterns
- **Type**: typing.List[str]
- **Required**: Yes

### targetFormat
- **Type**: typing.Optional[str]

### sourceTimezone
- **Type**: typing.Optional[str]

### targetTimezone
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]


# DateTimeConverterOutput

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### matchPatterns
- **Type**: typing.List[str]
- **Required**: Yes

### targetFormat
- **Type**: typing.Optional[str]

### sourceTimezone
- **Type**: typing.Optional[str]

### targetTimezone
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]


# DeleteAccountPolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['DATA_PROTECTION_POLICY', 'FIELD_INDEX_POLICY', 'SUBSCRIPTION_FILTER_POLICY', 'TRANSFORMER_POLICY']
- **Required**: Yes


# DeleteDataProtectionPolicyRequest

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryDestinationPolicyRequest

### deliveryDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryDestinationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliverySourceRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDestinationRequest

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexPolicyRequest

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationRequest

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteKeys

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteKeysOutput

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteLogAnomalyDetectorRequest

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogGroupRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogStreamRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMetricFilterRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueryDefinitionRequest

### queryDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueryDefinitionResponse

### success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### policyName
- **Type**: typing.Optional[str]


# DeleteRetentionPolicyRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionFilterRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTransformerRequest

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# Delivery

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

### recordFields
- **Type**: typing.Optional[typing.List[str]]

### fieldDelimiter
- **Type**: typing.Optional[str]

### s3DeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.S3DeliveryConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeliveryDestination

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### deliveryDestinationType
- **Type**: typing.Optional[typing.Literal['CWL', 'FH', 'S3']]

### outputFormat
- **Type**: typing.Optional[typing.Literal['json', 'parquet', 'plain', 'raw', 'w3c']]

### deliveryDestinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.DeliveryDestinationConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeliveryDestinationConfiguration

### destinationResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverySource

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


# DescribeAccountPoliciesRequest

### policyType
- **Type**: typing.Literal['DATA_PROTECTION_POLICY', 'FIELD_INDEX_POLICY', 'SUBSCRIPTION_FILTER_POLICY', 'TRANSFORMER_POLICY']
- **Required**: Yes

### policyName
- **Type**: typing.Optional[str]

### accountIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]


# DescribeAccountPoliciesResponse

### accountPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.AccountPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationTemplatesRequest

### service
- **Type**: typing.Optional[str]

### logTypes
- **Type**: typing.Optional[typing.List[str]]

### resourceTypes
- **Type**: typing.Optional[typing.List[str]]

### deliveryDestinationTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CWL', 'FH', 'S3']]]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeConfigurationTemplatesRequestPaginate

### service
- **Type**: typing.Optional[str]

### logTypes
- **Type**: typing.Optional[typing.List[str]]

### resourceTypes
- **Type**: typing.Optional[typing.List[str]]

### deliveryDestinationTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CWL', 'FH', 'S3']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeConfigurationTemplatesResponse

### configurationTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.ConfigurationTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDeliveriesRequest

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliveriesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeDeliveriesResponse

### deliveries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.Delivery]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDeliveryDestinationsRequest

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliveryDestinationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeDeliveryDestinationsResponse

### deliveryDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.DeliveryDestination]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDeliverySourcesRequest

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliverySourcesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeDeliverySourcesResponse

### deliverySources
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.DeliverySource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDestinationsRequest

### DestinationNamePrefix
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDestinationsRequestPaginate

### DestinationNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeDestinationsResponse

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.Destination]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeExportTasksRequest

### taskId
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'PENDING_CANCEL', 'RUNNING']]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeExportTasksRequestPaginate

### taskId
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'PENDING_CANCEL', 'RUNNING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeExportTasksResponse

### exportTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.ExportTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeFieldIndexesRequest

### logGroupIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeFieldIndexesResponse

### fieldIndexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.FieldIndex]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeIndexPoliciesRequest

### logGroupIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeIndexPoliciesResponse

### indexPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.IndexPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeLogGroupsRequest

### accountIdentifiers
- **Type**: typing.Optional[typing.List[str]]

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


# DescribeLogGroupsRequestPaginate

### accountIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### logGroupNamePrefix
- **Type**: typing.Optional[str]

### logGroupNamePattern
- **Type**: typing.Optional[str]

### includeLinkedAccounts
- **Type**: typing.Optional[bool]

### logGroupClass
- **Type**: typing.Optional[typing.Literal['INFREQUENT_ACCESS', 'STANDARD']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeLogGroupsResponse

### logGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.LogGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeLogStreamsRequest

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


# DescribeLogStreamsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeLogStreamsResponse

### logStreams
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.LogStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeMetricFiltersRequest

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


# DescribeMetricFiltersRequestPaginate

### logGroupName
- **Type**: typing.Optional[str]

### filterNamePrefix
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### metricNamespace
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeMetricFiltersResponse

### metricFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.MetricFilter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeQueriesRequest

### logGroupName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Complete', 'Failed', 'Running', 'Scheduled', 'Timeout', 'Unknown']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]


# DescribeQueriesRequestPaginate

### logGroupName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Complete', 'Failed', 'Running', 'Scheduled', 'Timeout', 'Unknown']]

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeQueriesResponse

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.QueryInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeQueryDefinitionsRequest

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]

### queryDefinitionNamePrefix
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeQueryDefinitionsResponse

### queryDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.QueryDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeResourcePoliciesRequest

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeResourcePoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeResourcePoliciesResponse

### resourcePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.ResourcePolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeSubscriptionFiltersRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterNamePrefix
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeSubscriptionFiltersRequestPaginate

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# DescribeSubscriptionFiltersResponse

### subscriptionFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.SubscriptionFilter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Destination

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


# DisassociateKmsKeyRequest

### logGroupName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# Entity

### keyAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExportTask

### taskId
- **Type**: typing.Optional[str]

### taskName
- **Type**: typing.Optional[str]

### logGroupName
- **Type**: typing.Optional[str]

### from_
- **Type**: typing.Optional[int]

### to
- **Type**: typing.Optional[int]

### destination
- **Type**: typing.Optional[str]

### destinationPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ExportTaskStatus]

### executionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ExportTaskExecutionInfo]


# ExportTaskExecutionInfo

### creationTime
- **Type**: typing.Optional[int]

### completionTime
- **Type**: typing.Optional[int]


# ExportTaskStatus

### code
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'PENDING_CANCEL', 'RUNNING']]

### message
- **Type**: typing.Optional[str]


# FieldIndex

### logGroupIdentifier
- **Type**: typing.Optional[str]

### fieldIndexName
- **Type**: typing.Optional[str]

### lastScanTime
- **Type**: typing.Optional[int]

### firstEventTime
- **Type**: typing.Optional[int]

### lastEventTime
- **Type**: typing.Optional[int]


# FilterLogEventsRequest

### logGroupName
- **Type**: typing.Optional[str]

### logGroupIdentifier
- **Type**: typing.Optional[str]

### logStreamNames
- **Type**: typing.Optional[typing.List[str]]

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


# FilterLogEventsRequestPaginate

### logGroupName
- **Type**: typing.Optional[str]

### logGroupIdentifier
- **Type**: typing.Optional[str]

### logStreamNames
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# FilterLogEventsResponse

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.FilteredLogEvent]
- **Required**: Yes

### searchedLogStreams
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.SearchedLogStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# FilteredLogEvent

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


# GetDataProtectionPolicyRequest

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataProtectionPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeliveryDestinationPolicyRequest

### deliveryDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliveryDestinationPolicyResponse

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeliveryDestinationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliveryDestinationResponse

### deliveryDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.DeliveryDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeliveryRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliveryResponse

### delivery
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.Delivery'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeliverySourceRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeliverySourceResponse

### deliverySource
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.DeliverySource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetIntegrationRequest

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponse

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes

### integrationType
- **Type**: typing.Literal['OPENSEARCH']
- **Required**: Yes

### integrationStatus
- **Type**: typing.Literal['ACTIVE', 'FAILED', 'PROVISIONING']
- **Required**: Yes

### integrationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.IntegrationDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetLogAnomalyDetectorRequest

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLogAnomalyDetectorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetLogEventsRequest

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


# GetLogEventsResponse

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.OutputLogEvent]
- **Required**: Yes

### nextForwardToken
- **Type**: <class 'str'>
- **Required**: Yes

### nextBackwardToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetLogGroupFieldsRequest

### logGroupName
- **Type**: typing.Optional[str]

### time
- **Type**: typing.Optional[int]

### logGroupIdentifier
- **Type**: typing.Optional[str]


# GetLogGroupFieldsResponse

### logGroupFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.LogGroupField]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetLogRecordRequest

### logRecordPointer
- **Type**: <class 'str'>
- **Required**: Yes

### unmask
- **Type**: typing.Optional[bool]


# GetLogRecordResponse

### logRecord
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryResultsRequest

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryResultsResponse

### queryLanguage
- **Type**: typing.Literal['CWLI', 'PPL', 'SQL']
- **Required**: Yes

### results
- **Type**: typing.List[typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.ResultField]]
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.QueryStatistics'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Cancelled', 'Complete', 'Failed', 'Running', 'Scheduled', 'Timeout', 'Unknown']
- **Required**: Yes

### encryptionKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# GetTransformerRequest

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransformerResponse

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'int'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### transformerConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.ProcessorOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# Grok

### match
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: typing.Optional[str]


# IndexPolicy

### logGroupIdentifier
- **Type**: typing.Optional[str]

### lastUpdateTime
- **Type**: typing.Optional[int]

### policyDocument
- **Type**: typing.Optional[str]

### policyName
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'LOG_GROUP']]


# InputLogEvent

### timestamp
- **Type**: <class 'int'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# IntegrationDetails

### openSearchIntegrationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchIntegrationDetails]


# IntegrationSummary

### integrationName
- **Type**: typing.Optional[str]

### integrationType
- **Type**: typing.Optional[typing.Literal['OPENSEARCH']]

### integrationStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'PROVISIONING']]


# ListAnomaliesRequest

### anomalyDetectorArn
- **Type**: typing.Optional[str]

### suppressionState
- **Type**: typing.Optional[typing.Literal['SUPPRESSED', 'UNSUPPRESSED']]

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAnomaliesRequestPaginate

### anomalyDetectorArn
- **Type**: typing.Optional[str]

### suppressionState
- **Type**: typing.Optional[typing.Literal['SUPPRESSED', 'UNSUPPRESSED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# ListAnomaliesResponse

### anomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.Anomaly]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIntegrationsRequest

### integrationNamePrefix
- **Type**: typing.Optional[str]

### integrationType
- **Type**: typing.Optional[typing.Literal['OPENSEARCH']]

### integrationStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'PROVISIONING']]


# ListIntegrationsResponse

### integrationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.IntegrationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# ListLogAnomalyDetectorsRequest

### filterLogGroupArn
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLogAnomalyDetectorsRequestPaginate

### filterLogGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# ListLogAnomalyDetectorsResponse

### anomalyDetectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.AnomalyDetector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLogGroupsForQueryRequest

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLogGroupsForQueryRequestPaginate

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.PaginatorConfig]


# ListLogGroupsForQueryResponse

### logGroupIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsLogGroupRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsLogGroupResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# ListToMap

### source
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### valueKey
- **Type**: typing.Optional[str]

### target
- **Type**: typing.Optional[str]

### flatten
- **Type**: typing.Optional[bool]

### flattenedElement
- **Type**: typing.Optional[typing.Literal['first', 'last']]


# LiveTailSessionLogEvent

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


# LiveTailSessionMetadata

### sampled
- **Type**: typing.Optional[bool]


# LiveTailSessionStart

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


# LiveTailSessionUpdate

### sessionMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.LiveTailSessionMetadata]

### sessionResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.LiveTailSessionLogEvent]]


# LogEvent

### timestamp
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]


# LogGroup

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


# LogGroupField

### name
- **Type**: typing.Optional[str]

### percent
- **Type**: typing.Optional[int]


# LogStream

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


# LowerCaseString

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# LowerCaseStringOutput

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# MetricFilter

### filterName
- **Type**: typing.Optional[str]

### filterPattern
- **Type**: typing.Optional[str]

### metricTransformations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.MetricTransformationOutput]]

### creationTime
- **Type**: typing.Optional[int]

### logGroupName
- **Type**: typing.Optional[str]

### applyOnTransformedLogs
- **Type**: typing.Optional[bool]


# MetricFilterMatchRecord

### eventNumber
- **Type**: typing.Optional[int]

### eventMessage
- **Type**: typing.Optional[str]

### extractedValues
- **Type**: typing.Optional[typing.Dict[str, str]]


# MetricTransformation

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


# MetricTransformationOutput

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


# MoveKeyEntry

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### overwriteIfExists
- **Type**: typing.Optional[bool]


# MoveKeys

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.MoveKeyEntry]
- **Required**: Yes


# MoveKeysOutput

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.MoveKeyEntry]
- **Required**: Yes


# OpenSearchApplication

### applicationEndpoint
- **Type**: typing.Optional[str]

### applicationArn
- **Type**: typing.Optional[str]

### applicationId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceStatus]


# OpenSearchCollection

### collectionEndpoint
- **Type**: typing.Optional[str]

### collectionArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceStatus]


# OpenSearchDataAccessPolicy

### policyName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceStatus]


# OpenSearchDataSource

### dataSourceName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceStatus]


# OpenSearchEncryptionPolicy

### policyName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceStatus]


# OpenSearchIntegrationDetails

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchDataSource]

### application
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchApplication]

### collection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchCollection]

### workspace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchWorkspace]

### encryptionPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchEncryptionPolicy]

### networkPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchNetworkPolicy]

### accessPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchDataAccessPolicy]

### lifecyclePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchLifecyclePolicy]


# OpenSearchLifecyclePolicy

### policyName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceStatus]


# OpenSearchNetworkPolicy

### policyName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceStatus]


# OpenSearchResourceConfig

### dataSourceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardViewerPrincipals
- **Type**: typing.List[str]
- **Required**: Yes

### retentionDays
- **Type**: <class 'int'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]

### applicationArn
- **Type**: typing.Optional[str]


# OpenSearchResourceStatus

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ERROR', 'NOT_FOUND']]

### statusMessage
- **Type**: typing.Optional[str]


# OpenSearchWorkspace

### workspaceId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceStatus]


# OutputLogEvent

### timestamp
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]

### ingestionTime
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParseCloudfront

### source
- **Type**: typing.Optional[str]


# ParseJSON

### source
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[str]


# ParseKeyValue

### source
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[str]

### fieldDelimiter
- **Type**: typing.Optional[str]

### keyValueDelimiter
- **Type**: typing.Optional[str]

### keyPrefix
- **Type**: typing.Optional[str]

### nonMatchValue
- **Type**: typing.Optional[str]

### overwriteIfExists
- **Type**: typing.Optional[bool]


# ParsePostgres

### source
- **Type**: typing.Optional[str]


# ParseRoute53

### source
- **Type**: typing.Optional[str]


# ParseVPC

### source
- **Type**: typing.Optional[str]


# ParseWAF

### source
- **Type**: typing.Optional[str]


# PatternToken

### dynamicTokenPosition
- **Type**: typing.Optional[int]

### isDynamic
- **Type**: typing.Optional[bool]

### tokenString
- **Type**: typing.Optional[str]

### enumerations
- **Type**: typing.Optional[typing.Dict[str, int]]

### inferredTokenName
- **Type**: typing.Optional[str]


# Policy

### deliveryDestinationPolicy
- **Type**: typing.Optional[str]


# Processor

### addKeys
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.AddKeys, aws_resource_validator.pydantic_models.logs.logs_classes.AddKeysOutput, NoneType]

### copyValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.CopyValue, aws_resource_validator.pydantic_models.logs.logs_classes.CopyValueOutput, NoneType]

### csv
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.CSV, aws_resource_validator.pydantic_models.logs.logs_classes.CSVOutput, NoneType]

### dateTimeConverter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.DateTimeConverter, aws_resource_validator.pydantic_models.logs.logs_classes.DateTimeConverterOutput, NoneType]

### deleteKeys
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.DeleteKeys, aws_resource_validator.pydantic_models.logs.logs_classes.DeleteKeysOutput, NoneType]

### grok
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.Grok]

### listToMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ListToMap]

### lowerCaseString
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.LowerCaseString, aws_resource_validator.pydantic_models.logs.logs_classes.LowerCaseStringOutput, NoneType]

### moveKeys
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.MoveKeys, aws_resource_validator.pydantic_models.logs.logs_classes.MoveKeysOutput, NoneType]

### parseCloudfront
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseCloudfront]

### parseJSON
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseJSON]

### parseKeyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseKeyValue]

### parseRoute53
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseRoute53]

### parsePostgres
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParsePostgres]

### parseVPC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseVPC]

### parseWAF
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseWAF]

### renameKeys
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.RenameKeys, aws_resource_validator.pydantic_models.logs.logs_classes.RenameKeysOutput, NoneType]

### splitString
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.SplitString, aws_resource_validator.pydantic_models.logs.logs_classes.SplitStringOutput, NoneType]

### substituteString
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.SubstituteString, aws_resource_validator.pydantic_models.logs.logs_classes.SubstituteStringOutput, NoneType]

### trimString
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.TrimString, aws_resource_validator.pydantic_models.logs.logs_classes.TrimStringOutput, NoneType]

### typeConverter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.TypeConverter, aws_resource_validator.pydantic_models.logs.logs_classes.TypeConverterOutput, NoneType]

### upperCaseString
- **Type**: typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.UpperCaseString, aws_resource_validator.pydantic_models.logs.logs_classes.UpperCaseStringOutput, NoneType]


# ProcessorOutput

### addKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.AddKeysOutput]

### copyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.CopyValueOutput]

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.CSVOutput]

### dateTimeConverter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.DateTimeConverterOutput]

### deleteKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.DeleteKeysOutput]

### grok
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.Grok]

### listToMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ListToMap]

### lowerCaseString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.LowerCaseStringOutput]

### moveKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.MoveKeysOutput]

### parseCloudfront
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseCloudfront]

### parseJSON
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseJSON]

### parseKeyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseKeyValue]

### parseRoute53
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseRoute53]

### parsePostgres
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParsePostgres]

### parseVPC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseVPC]

### parseWAF
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.ParseWAF]

### renameKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.RenameKeysOutput]

### splitString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.SplitStringOutput]

### substituteString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.SubstituteStringOutput]

### trimString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.TrimStringOutput]

### typeConverter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.TypeConverterOutput]

### upperCaseString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.UpperCaseStringOutput]


# PutAccountPolicyRequest

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['DATA_PROTECTION_POLICY', 'FIELD_INDEX_POLICY', 'SUBSCRIPTION_FILTER_POLICY', 'TRANSFORMER_POLICY']
- **Required**: Yes

### scope
- **Type**: typing.Optional[typing.Literal['ALL']]

### selectionCriteria
- **Type**: typing.Optional[str]


# PutAccountPolicyResponse

### accountPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.AccountPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutDataProtectionPolicyRequest

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutDataProtectionPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutDeliveryDestinationPolicyRequest

### deliveryDestinationName
- **Type**: <class 'str'>
- **Required**: Yes

### deliveryDestinationPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# PutDeliveryDestinationPolicyResponse

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutDeliveryDestinationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### deliveryDestinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.DeliveryDestinationConfiguration'>
- **Required**: Yes

### outputFormat
- **Type**: typing.Optional[typing.Literal['json', 'parquet', 'plain', 'raw', 'w3c']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutDeliveryDestinationResponse

### deliveryDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.DeliveryDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutDeliverySourceRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutDeliverySourceResponse

### deliverySource
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.DeliverySource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutDestinationPolicyRequest

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### forceUpdate
- **Type**: typing.Optional[bool]


# PutDestinationRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutDestinationResponse

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.Destination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutIndexPolicyRequest

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutIndexPolicyResponse

### indexPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.IndexPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutIntegrationRequest

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResourceConfig'>
- **Required**: Yes

### integrationType
- **Type**: typing.Literal['OPENSEARCH']
- **Required**: Yes


# PutIntegrationResponse

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes

### integrationStatus
- **Type**: typing.Literal['ACTIVE', 'FAILED', 'PROVISIONING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutLogEventsRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### logEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.InputLogEvent]
- **Required**: Yes

### sequenceToken
- **Type**: typing.Optional[str]

### entity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.Entity]


# PutLogEventsResponse

### nextSequenceToken
- **Type**: <class 'str'>
- **Required**: Yes

### rejectedLogEventsInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.RejectedLogEventsInfo'>
- **Required**: Yes

### rejectedEntityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.RejectedEntityInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutMetricFilterRequest

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
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.MetricTransformation, aws_resource_validator.pydantic_models.logs.logs_classes.MetricTransformationOutput]]
- **Required**: Yes

### applyOnTransformedLogs
- **Type**: typing.Optional[bool]


# PutQueryDefinitionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]

### queryDefinitionId
- **Type**: typing.Optional[str]

### logGroupNames
- **Type**: typing.Optional[typing.List[str]]

### clientToken
- **Type**: typing.Optional[str]


# PutQueryDefinitionResponse

### queryDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyRequest

### policyName
- **Type**: typing.Optional[str]

### policyDocument
- **Type**: typing.Optional[str]


# PutResourcePolicyResponse

### resourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# PutRetentionPolicyRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionInDays
- **Type**: <class 'int'>
- **Required**: Yes


# PutSubscriptionFilterRequest

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

### applyOnTransformedLogs
- **Type**: typing.Optional[bool]


# PutTransformerRequest

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### transformerConfig
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.Processor, aws_resource_validator.pydantic_models.logs.logs_classes.ProcessorOutput]]
- **Required**: Yes


# QueryDefinition

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]

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


# QueryInfo

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]

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


# QueryStatistics

### recordsMatched
- **Type**: typing.Optional[float]

### recordsScanned
- **Type**: typing.Optional[float]

### estimatedRecordsSkipped
- **Type**: typing.Optional[float]

### bytesScanned
- **Type**: typing.Optional[float]

### estimatedBytesSkipped
- **Type**: typing.Optional[float]

### logGroupsScanned
- **Type**: typing.Optional[float]


# RecordField

### name
- **Type**: typing.Optional[str]

### mandatory
- **Type**: typing.Optional[bool]


# RejectedEntityInfo

### errorType
- **Type**: typing.Literal['EntitySizeTooLarge', 'InvalidAttributes', 'InvalidEntity', 'InvalidKeyAttributes', 'InvalidTypeValue', 'MissingRequiredFields', 'UnsupportedLogGroupType']
- **Required**: Yes


# RejectedLogEventsInfo

### tooNewLogEventStartIndex
- **Type**: typing.Optional[int]

### tooOldLogEventEndIndex
- **Type**: typing.Optional[int]

### expiredLogEventEndIndex
- **Type**: typing.Optional[int]


# RenameKeyEntry

### key
- **Type**: <class 'str'>
- **Required**: Yes

### renameTo
- **Type**: <class 'str'>
- **Required**: Yes

### overwriteIfExists
- **Type**: typing.Optional[bool]


# RenameKeys

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.RenameKeyEntry]
- **Required**: Yes


# RenameKeysOutput

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.RenameKeyEntry]
- **Required**: Yes


# ResourceConfig

### openSearchResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.OpenSearchResourceConfig]


# ResourcePolicy

### policyName
- **Type**: typing.Optional[str]

### policyDocument
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[int]


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


# ResultField

### field
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# S3DeliveryConfiguration

### suffixPath
- **Type**: typing.Optional[str]

### enableHiveCompatiblePath
- **Type**: typing.Optional[bool]


# SearchedLogStream

### logStreamName
- **Type**: typing.Optional[str]

### searchedCompletely
- **Type**: typing.Optional[bool]


# SessionStreamingException

### message
- **Type**: typing.Optional[str]


# SessionTimeoutException

### message
- **Type**: typing.Optional[str]


# SplitString

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.SplitStringEntry]
- **Required**: Yes


# SplitStringEntry

### source
- **Type**: <class 'str'>
- **Required**: Yes

### delimiter
- **Type**: <class 'str'>
- **Required**: Yes


# SplitStringOutput

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.SplitStringEntry]
- **Required**: Yes


# StartLiveTailRequest

### logGroupIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### logStreamNames
- **Type**: typing.Optional[typing.List[str]]

### logStreamNamePrefixes
- **Type**: typing.Optional[typing.List[str]]

### logEventFilterPattern
- **Type**: typing.Optional[str]


# StartLiveTailResponse

### responseStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.logs.logs_classes.StartLiveTailResponseStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# StartLiveTailResponseStream

### sessionStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.LiveTailSessionStart]

### sessionUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.LiveTailSessionUpdate]

### SessionTimeoutException
- **Type**: <class 'NoneType'>

### SessionStreamingException
- **Type**: <class 'NoneType'>


# StartQueryRequest

### startTime
- **Type**: <class 'int'>
- **Required**: Yes

### endTime
- **Type**: <class 'int'>
- **Required**: Yes

### queryString
- **Type**: <class 'str'>
- **Required**: Yes

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]

### logGroupName
- **Type**: typing.Optional[str]

### logGroupNames
- **Type**: typing.Optional[typing.List[str]]

### logGroupIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### limit
- **Type**: typing.Optional[int]


# StartQueryResponse

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# StopQueryRequest

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# StopQueryResponse

### success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# SubscriptionFilter

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

### applyOnTransformedLogs
- **Type**: typing.Optional[bool]

### creationTime
- **Type**: typing.Optional[int]


# SubstituteString

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.SubstituteStringEntry]
- **Required**: Yes


# SubstituteStringEntry

### source
- **Type**: <class 'str'>
- **Required**: Yes

### from_
- **Type**: <class 'str'>
- **Required**: Yes

### to
- **Type**: <class 'str'>
- **Required**: Yes


# SubstituteStringOutput

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.SubstituteStringEntry]
- **Required**: Yes


# SuppressionPeriod

### value
- **Type**: typing.Optional[int]

### suppressionUnit
- **Type**: typing.Optional[typing.Literal['HOURS', 'MINUTES', 'SECONDS']]


# TagLogGroupRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TestMetricFilterRequest

### filterPattern
- **Type**: <class 'str'>
- **Required**: Yes

### logEventMessages
- **Type**: typing.List[str]
- **Required**: Yes


# TestMetricFilterResponse

### matches
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.MetricFilterMatchRecord]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# TestTransformerRequest

### transformerConfig
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.logs.logs_classes.Processor, aws_resource_validator.pydantic_models.logs.logs_classes.ProcessorOutput]]
- **Required**: Yes

### logEventMessages
- **Type**: typing.List[str]
- **Required**: Yes


# TestTransformerResponse

### transformedLogs
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.TransformedLogRecord]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs.logs_classes.ResponseMetadata'>
- **Required**: Yes


# TransformedLogRecord

### eventNumber
- **Type**: typing.Optional[int]

### eventMessage
- **Type**: typing.Optional[str]

### transformedEventMessage
- **Type**: typing.Optional[str]


# TrimString

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# TrimStringOutput

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# TypeConverter

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.TypeConverterEntry]
- **Required**: Yes


# TypeConverterEntry

### key
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['boolean', 'double', 'integer', 'string']
- **Required**: Yes


# TypeConverterOutput

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs.logs_classes.TypeConverterEntry]
- **Required**: Yes


# UntagLogGroupRequest

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAnomalyRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.SuppressionPeriod]

### baseline
- **Type**: typing.Optional[bool]


# UpdateDeliveryConfigurationRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### recordFields
- **Type**: typing.Optional[typing.List[str]]

### fieldDelimiter
- **Type**: typing.Optional[str]

### s3DeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs.logs_classes.S3DeliveryConfiguration]


# UpdateLogAnomalyDetectorRequest

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


# UpperCaseString

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpperCaseStringOutput

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes



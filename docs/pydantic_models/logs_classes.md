# Logs Classes

# AccountPolicyTypeDef

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


# AddKeyEntryTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### overwriteIfExists
- **Type**: typing.Optional[bool]


# AddKeysOutputTypeDef

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.AddKeyEntryTypeDef]
- **Required**: Yes


# AddKeysTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.AddKeyEntryTypeDef]
- **Required**: Yes


# AddKeysUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# AssociateKmsKeyRequestTypeDef

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

# CSVOutputTypeDef

### quoteCharacter
- **Type**: typing.Optional[str]

### delimiter
- **Type**: typing.Optional[str]

### columns
- **Type**: typing.Optional[typing.List[str]]

### source
- **Type**: typing.Optional[str]


# CSVTypeDef

### quoteCharacter
- **Type**: typing.Optional[str]

### delimiter
- **Type**: typing.Optional[str]

### columns
- **Type**: typing.Optional[typing.Sequence[str]]

### source
- **Type**: typing.Optional[str]


# CSVUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelExportTaskRequestTypeDef

### taskId
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigurationTemplateDeliveryConfigValuesTypeDef

### recordFields
- **Type**: typing.Optional[typing.List[str]]

### fieldDelimiter
- **Type**: typing.Optional[str]

### s3DeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.S3DeliveryConfigurationTypeDef]


# ConfigurationTemplateTypeDef

### service
- **Type**: typing.Optional[str]

### logType
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]

### deliveryDestinationType
- **Type**: typing.Optional[typing.Literal['CWL', 'FH', 'S3']]

### defaultDeliveryConfigValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ConfigurationTemplateDeliveryConfigValuesTypeDef]

### allowedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.logs_classes.RecordFieldTypeDef]]

### allowedOutputFormats
- **Type**: typing.Optional[typing.List[typing.Literal['json', 'parquet', 'plain', 'raw', 'w3c']]]

### allowedActionForAllowVendedLogsDeliveryForResource
- **Type**: typing.Optional[str]

### allowedFieldDelimiters
- **Type**: typing.Optional[typing.List[str]]

### allowedSuffixPathFields
- **Type**: typing.Optional[typing.List[str]]


# CopyValueEntryTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### overwriteIfExists
- **Type**: typing.Optional[bool]


# CopyValueOutputTypeDef

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.CopyValueEntryTypeDef]
- **Required**: Yes


# CopyValueTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.CopyValueEntryTypeDef]
- **Required**: Yes


# CopyValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDeliveryRequestTypeDef

### deliverySourceName
- **Type**: <class 'str'>
- **Required**: Yes

### deliveryDestinationArn
- **Type**: <class 'str'>
- **Required**: Yes

### recordFields
- **Type**: typing.Optional[typing.Sequence[str]]

### fieldDelimiter
- **Type**: typing.Optional[str]

### s3DeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.S3DeliveryConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDeliveryResponseTypeDef

### delivery
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliveryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExportTaskRequestTypeDef

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


# CreateLogAnomalyDetectorRequestTypeDef

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


# CreateLogGroupRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### logGroupClass
- **Type**: typing.Optional[typing.Literal['INFREQUENT_ACCESS', 'STANDARD']]


# CreateLogStreamRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# DateTimeConverterOutputTypeDef

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


# DateTimeConverterTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### matchPatterns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### targetFormat
- **Type**: typing.Optional[str]

### sourceTimezone
- **Type**: typing.Optional[str]

### targetTimezone
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]


# DateTimeConverterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAccountPolicyRequestTypeDef

### policyName
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['DATA_PROTECTION_POLICY', 'FIELD_INDEX_POLICY', 'SUBSCRIPTION_FILTER_POLICY', 'TRANSFORMER_POLICY']
- **Required**: Yes


# DeleteDataProtectionPolicyRequestTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryDestinationPolicyRequestTypeDef

### deliveryDestinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliveryDestinationRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeliverySourceRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDestinationRequestTypeDef

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexPolicyRequestTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationRequestTypeDef

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteKeysOutputTypeDef

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteKeysTypeDef

### withKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteKeysUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteLogAnomalyDetectorRequestTypeDef

### anomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogGroupRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogStreamRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### logStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMetricFilterRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQueryDefinitionRequestTypeDef

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


# DeleteResourcePolicyRequestTypeDef

### policyName
- **Type**: typing.Optional[str]


# DeleteRetentionPolicyRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriptionFilterRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTransformerRequestTypeDef

### logGroupIdentifier
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DescribeAccountPoliciesRequestTypeDef

### policyType
- **Type**: typing.Literal['DATA_PROTECTION_POLICY', 'FIELD_INDEX_POLICY', 'SUBSCRIPTION_FILTER_POLICY', 'TRANSFORMER_POLICY']
- **Required**: Yes

### policyName
- **Type**: typing.Optional[str]

### accountIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]


# DescribeAccountPoliciesResponseTypeDef

### accountPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.AccountPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeConfigurationTemplatesRequestPaginateTypeDef

### service
- **Type**: typing.Optional[str]

### logTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### deliveryDestinationTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CWL', 'FH', 'S3']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeConfigurationTemplatesRequestTypeDef

### service
- **Type**: typing.Optional[str]

### logTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### deliveryDestinationTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CWL', 'FH', 'S3']]]

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeConfigurationTemplatesResponseTypeDef

### configurationTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.ConfigurationTemplateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDeliveriesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeDeliveriesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliveriesResponseTypeDef

### deliveries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.DeliveryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDeliveryDestinationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeDeliveryDestinationsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliveryDestinationsResponseTypeDef

### deliveryDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.DeliveryDestinationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDeliverySourcesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeDeliverySourcesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeDeliverySourcesResponseTypeDef

### deliverySources
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.DeliverySourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeDestinationsRequestPaginateTypeDef

### DestinationNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeDestinationsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeExportTasksRequestPaginateTypeDef

### taskId
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PENDING', 'PENDING_CANCEL', 'RUNNING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeExportTasksRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeFieldIndexesRequestTypeDef

### logGroupIdentifiers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeFieldIndexesResponseTypeDef

### fieldIndexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.FieldIndexTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeIndexPoliciesRequestTypeDef

### logGroupIdentifiers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeIndexPoliciesResponseTypeDef

### indexPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.IndexPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeLogGroupsRequestPaginateTypeDef

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


# DescribeLogGroupsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeLogStreamsRequestPaginateTypeDef

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


# DescribeLogStreamsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeMetricFiltersRequestPaginateTypeDef

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


# DescribeMetricFiltersRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeQueriesRequestPaginateTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Complete', 'Failed', 'Running', 'Scheduled', 'Timeout', 'Unknown']]

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeQueriesRequestTypeDef

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


# DescribeQueriesResponseTypeDef

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.QueryInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeQueryDefinitionsRequestTypeDef

### queryLanguage
- **Type**: typing.Optional[typing.Literal['CWLI', 'PPL', 'SQL']]

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeResourcePoliciesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeResourcePoliciesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### limit
- **Type**: typing.Optional[int]


# DescribeResourcePoliciesResponseTypeDef

### resourcePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.ResourcePolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeSubscriptionFiltersRequestPaginateTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### filterNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# DescribeSubscriptionFiltersRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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


# DisassociateKmsKeyRequestTypeDef

### logGroupName
- **Type**: typing.Optional[str]

### resourceIdentifier
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EntityTypeDef

### keyAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldIndexTypeDef

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


# FilterLogEventsRequestPaginateTypeDef

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


# FilterLogEventsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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


# GetDataProtectionPolicyRequestTypeDef

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


# GetDeliveryDestinationPolicyRequestTypeDef

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


# GetDeliveryDestinationRequestTypeDef

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


# GetDeliveryResponseTypeDef

### delivery
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.DeliveryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeliverySourceRequestTypeDef

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


# GetIntegrationRequestTypeDef

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.IntegrationDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLogAnomalyDetectorRequestTypeDef

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


# GetLogEventsRequestTypeDef

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


# GetLogGroupFieldsRequestTypeDef

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


# GetLogRecordRequestTypeDef

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


# GetQueryResultsRequestTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryResultsResponseTypeDef

### queryLanguage
- **Type**: typing.Literal['CWLI', 'PPL', 'SQL']
- **Required**: Yes

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


# GetTransformerRequestTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTransformerResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.ProcessorOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GrokTypeDef

### match
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: typing.Optional[str]


# IndexPolicyTypeDef

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


# InputLogEventTypeDef

### timestamp
- **Type**: <class 'int'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# IntegrationDetailsTypeDef

### openSearchIntegrationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchIntegrationDetailsTypeDef]


# IntegrationSummaryTypeDef

### integrationName
- **Type**: typing.Optional[str]

### integrationType
- **Type**: typing.Optional[typing.Literal['OPENSEARCH']]

### integrationStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'PROVISIONING']]


# ListAnomaliesRequestPaginateTypeDef

### anomalyDetectorArn
- **Type**: typing.Optional[str]

### suppressionState
- **Type**: typing.Optional[typing.Literal['SUPPRESSED', 'UNSUPPRESSED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# ListAnomaliesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIntegrationsRequestTypeDef

### integrationNamePrefix
- **Type**: typing.Optional[str]

### integrationType
- **Type**: typing.Optional[typing.Literal['OPENSEARCH']]

### integrationStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'PROVISIONING']]


# ListIntegrationsResponseTypeDef

### integrationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.IntegrationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLogAnomalyDetectorsRequestPaginateTypeDef

### filterLogGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# ListLogAnomalyDetectorsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLogGroupsForQueryRequestPaginateTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.PaginatorConfigTypeDef]


# ListLogGroupsForQueryRequestTypeDef

### queryId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLogGroupsForQueryResponseTypeDef

### logGroupIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

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


# ListTagsLogGroupRequestTypeDef

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


# ListToMapTypeDef

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


# LowerCaseStringOutputTypeDef

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# LowerCaseStringTypeDef

### withKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# LowerCaseStringUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.logs_classes.MetricTransformationOutputTypeDef]]

### creationTime
- **Type**: typing.Optional[int]

### logGroupName
- **Type**: typing.Optional[str]

### applyOnTransformedLogs
- **Type**: typing.Optional[bool]


# MetricTransformationOutputTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]


# MetricTransformationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MoveKeyEntryTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### overwriteIfExists
- **Type**: typing.Optional[bool]


# MoveKeysOutputTypeDef

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.MoveKeyEntryTypeDef]
- **Required**: Yes


# MoveKeysTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.MoveKeyEntryTypeDef]
- **Required**: Yes


# MoveKeysUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OpenSearchApplicationTypeDef

### applicationEndpoint
- **Type**: typing.Optional[str]

### applicationArn
- **Type**: typing.Optional[str]

### applicationId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceStatusTypeDef]


# OpenSearchCollectionTypeDef

### collectionEndpoint
- **Type**: typing.Optional[str]

### collectionArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceStatusTypeDef]


# OpenSearchDataAccessPolicyTypeDef

### policyName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceStatusTypeDef]


# OpenSearchDataSourceTypeDef

### dataSourceName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceStatusTypeDef]


# OpenSearchEncryptionPolicyTypeDef

### policyName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceStatusTypeDef]


# OpenSearchIntegrationDetailsTypeDef

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchDataSourceTypeDef]

### application
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchApplicationTypeDef]

### collection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchCollectionTypeDef]

### workspace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchWorkspaceTypeDef]

### encryptionPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchEncryptionPolicyTypeDef]

### networkPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchNetworkPolicyTypeDef]

### accessPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchDataAccessPolicyTypeDef]

### lifecyclePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchLifecyclePolicyTypeDef]


# OpenSearchLifecyclePolicyTypeDef

### policyName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceStatusTypeDef]


# OpenSearchNetworkPolicyTypeDef

### policyName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceStatusTypeDef]


# OpenSearchResourceConfigTypeDef

### dataSourceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dashboardViewerPrincipals
- **Type**: typing.Sequence[str]
- **Required**: Yes

### retentionDays
- **Type**: <class 'int'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]

### applicationArn
- **Type**: typing.Optional[str]


# OpenSearchResourceStatusTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ERROR', 'NOT_FOUND']]

### statusMessage
- **Type**: typing.Optional[str]


# OpenSearchWorkspaceTypeDef

### workspaceId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceStatusTypeDef]


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


# ParseCloudfrontTypeDef

### source
- **Type**: typing.Optional[str]


# ParseJSONTypeDef

### source
- **Type**: typing.Optional[str]

### destination
- **Type**: typing.Optional[str]


# ParseKeyValueTypeDef

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


# ParsePostgresTypeDef

### source
- **Type**: typing.Optional[str]


# ParseRoute53TypeDef

### source
- **Type**: typing.Optional[str]


# ParseVPCTypeDef

### source
- **Type**: typing.Optional[str]


# ParseWAFTypeDef

### source
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

### inferredTokenName
- **Type**: typing.Optional[str]


# PolicyTypeDef

### deliveryDestinationPolicy
- **Type**: typing.Optional[str]


# ProcessorOutputTypeDef

### addKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.AddKeysOutputTypeDef]

### copyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.CopyValueOutputTypeDef]

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.CSVOutputTypeDef]

### dateTimeConverter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.DateTimeConverterOutputTypeDef]

### deleteKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.DeleteKeysOutputTypeDef]

### grok
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.GrokTypeDef]

### listToMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ListToMapTypeDef]

### lowerCaseString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.LowerCaseStringOutputTypeDef]

### moveKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.MoveKeysOutputTypeDef]

### parseCloudfront
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseCloudfrontTypeDef]

### parseJSON
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseJSONTypeDef]

### parseKeyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseKeyValueTypeDef]

### parseRoute53
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseRoute53TypeDef]

### parsePostgres
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParsePostgresTypeDef]

### parseVPC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseVPCTypeDef]

### parseWAF
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseWAFTypeDef]

### renameKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.RenameKeysOutputTypeDef]

### splitString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.SplitStringOutputTypeDef]

### substituteString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.SubstituteStringOutputTypeDef]

### trimString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.TrimStringOutputTypeDef]

### typeConverter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.TypeConverterOutputTypeDef]

### upperCaseString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.UpperCaseStringOutputTypeDef]


# ProcessorTypeDef

### addKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.AddKeysUnionTypeDef]

### copyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.CopyValueUnionTypeDef]

### csv
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.CSVUnionTypeDef]

### dateTimeConverter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.DateTimeConverterUnionTypeDef]

### deleteKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.DeleteKeysUnionTypeDef]

### grok
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.GrokTypeDef]

### listToMap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ListToMapTypeDef]

### lowerCaseString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.LowerCaseStringUnionTypeDef]

### moveKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.MoveKeysUnionTypeDef]

### parseCloudfront
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseCloudfrontTypeDef]

### parseJSON
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseJSONTypeDef]

### parseKeyValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseKeyValueTypeDef]

### parseRoute53
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseRoute53TypeDef]

### parsePostgres
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParsePostgresTypeDef]

### parseVPC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseVPCTypeDef]

### parseWAF
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.ParseWAFTypeDef]

### renameKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.RenameKeysUnionTypeDef]

### splitString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.SplitStringUnionTypeDef]

### substituteString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.SubstituteStringUnionTypeDef]

### trimString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.TrimStringUnionTypeDef]

### typeConverter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.TypeConverterUnionTypeDef]

### upperCaseString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.UpperCaseStringUnionTypeDef]


# ProcessorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutAccountPolicyRequestTypeDef

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


# PutAccountPolicyResponseTypeDef

### accountPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.AccountPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDataProtectionPolicyRequestTypeDef

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


# PutDeliveryDestinationPolicyRequestTypeDef

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


# PutDeliveryDestinationRequestTypeDef

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


# PutDeliverySourceRequestTypeDef

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


# PutDestinationPolicyRequestTypeDef

### destinationName
- **Type**: <class 'str'>
- **Required**: Yes

### accessPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### forceUpdate
- **Type**: typing.Optional[bool]


# PutDestinationRequestTypeDef

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


# PutIndexPolicyRequestTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutIndexPolicyResponseTypeDef

### indexPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.IndexPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutIntegrationRequestTypeDef

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResourceConfigTypeDef'>
- **Required**: Yes

### integrationType
- **Type**: typing.Literal['OPENSEARCH']
- **Required**: Yes


# PutIntegrationResponseTypeDef

### integrationName
- **Type**: <class 'str'>
- **Required**: Yes

### integrationStatus
- **Type**: typing.Literal['ACTIVE', 'FAILED', 'PROVISIONING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutLogEventsRequestTypeDef

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

### entity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.EntityTypeDef]


# PutLogEventsResponseTypeDef

### nextSequenceToken
- **Type**: <class 'str'>
- **Required**: Yes

### rejectedLogEventsInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.RejectedLogEventsInfoTypeDef'>
- **Required**: Yes

### rejectedEntityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.RejectedEntityInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutMetricFilterRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.MetricTransformationUnionTypeDef]
- **Required**: Yes

### applyOnTransformedLogs
- **Type**: typing.Optional[bool]


# PutQueryDefinitionRequestTypeDef

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


# PutResourcePolicyRequestTypeDef

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


# PutRetentionPolicyRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### retentionInDays
- **Type**: <class 'int'>
- **Required**: Yes


# PutSubscriptionFilterRequestTypeDef

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


# PutTransformerRequestTypeDef

### logGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### transformerConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.ProcessorUnionTypeDef]
- **Required**: Yes


# QueryDefinitionTypeDef

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


# QueryInfoTypeDef

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


# QueryStatisticsTypeDef

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


# RecordFieldTypeDef

### name
- **Type**: typing.Optional[str]

### mandatory
- **Type**: typing.Optional[bool]


# RejectedEntityInfoTypeDef

### errorType
- **Type**: typing.Literal['EntitySizeTooLarge', 'InvalidAttributes', 'InvalidEntity', 'InvalidKeyAttributes', 'InvalidTypeValue', 'MissingRequiredFields', 'UnsupportedLogGroupType']
- **Required**: Yes


# RejectedLogEventsInfoTypeDef

### tooNewLogEventStartIndex
- **Type**: typing.Optional[int]

### tooOldLogEventEndIndex
- **Type**: typing.Optional[int]

### expiredLogEventEndIndex
- **Type**: typing.Optional[int]


# RenameKeyEntryTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### renameTo
- **Type**: <class 'str'>
- **Required**: Yes

### overwriteIfExists
- **Type**: typing.Optional[bool]


# RenameKeysOutputTypeDef

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.RenameKeyEntryTypeDef]
- **Required**: Yes


# RenameKeysTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.RenameKeyEntryTypeDef]
- **Required**: Yes


# RenameKeysUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceConfigTypeDef

### openSearchResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.logs_classes.OpenSearchResourceConfigTypeDef]


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


# S3DeliveryConfigurationTypeDef

### suffixPath
- **Type**: typing.Optional[str]

### enableHiveCompatiblePath
- **Type**: typing.Optional[bool]


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


# SplitStringEntryTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### delimiter
- **Type**: <class 'str'>
- **Required**: Yes


# SplitStringOutputTypeDef

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.SplitStringEntryTypeDef]
- **Required**: Yes


# SplitStringTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.SplitStringEntryTypeDef]
- **Required**: Yes


# SplitStringUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartLiveTailRequestTypeDef

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
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.logs_classes.StartLiveTailResponseStreamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartQueryRequestTypeDef

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


# StopQueryRequestTypeDef

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

### applyOnTransformedLogs
- **Type**: typing.Optional[bool]

### creationTime
- **Type**: typing.Optional[int]


# SubstituteStringEntryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SubstituteStringOutputTypeDef

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.SubstituteStringEntryTypeDef]
- **Required**: Yes


# SubstituteStringTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.SubstituteStringEntryTypeDef]
- **Required**: Yes


# SubstituteStringUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SuppressionPeriodTypeDef

### value
- **Type**: typing.Optional[int]

### suppressionUnit
- **Type**: typing.Optional[typing.Literal['HOURS', 'MINUTES', 'SECONDS']]


# TagLogGroupRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestMetricFilterRequestTypeDef

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


# TestTransformerRequestTypeDef

### transformerConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.ProcessorUnionTypeDef]
- **Required**: Yes

### logEventMessages
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TestTransformerResponseTypeDef

### transformedLogs
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.TransformedLogRecordTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.logs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TransformedLogRecordTypeDef

### eventNumber
- **Type**: typing.Optional[int]

### eventMessage
- **Type**: typing.Optional[str]

### transformedEventMessage
- **Type**: typing.Optional[str]


# TrimStringOutputTypeDef

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# TrimStringTypeDef

### withKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TrimStringUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TypeConverterEntryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TypeConverterOutputTypeDef

### entries
- **Type**: typing.List[aws_resource_validator.pydantic_models.logs_classes.TypeConverterEntryTypeDef]
- **Required**: Yes


# TypeConverterTypeDef

### entries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.logs_classes.TypeConverterEntryTypeDef]
- **Required**: Yes


# TypeConverterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagLogGroupRequestTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAnomalyRequestTypeDef

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

### baseline
- **Type**: typing.Optional[bool]


# UpdateLogAnomalyDetectorRequestTypeDef

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


# UpperCaseStringOutputTypeDef

### withKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpperCaseStringTypeDef

### withKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpperCaseStringUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


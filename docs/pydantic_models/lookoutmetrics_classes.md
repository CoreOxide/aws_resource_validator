# Lookoutmetrics Classes

# ActionTypeDef

### SNSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.SNSConfigurationTypeDef]

### LambdaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.LambdaConfigurationTypeDef]


# ActivateAnomalyDetectorRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# AlertFiltersTypeDef

### MetricList
- **Type**: typing.Optional[typing.Sequence[str]]

### DimensionFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DimensionFilterTypeDef]]


# AlertSummaryTypeDef

### AlertArn
- **Type**: typing.Optional[str]

### AnomalyDetectorArn
- **Type**: typing.Optional[str]

### AlertName
- **Type**: typing.Optional[str]

### AlertSensitivityThreshold
- **Type**: typing.Optional[int]

### AlertType
- **Type**: typing.Optional[typing.Literal['LAMBDA', 'SNS']]

### AlertStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AlertTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.ActionTypeDef]

### AlertDescription
- **Type**: typing.Optional[str]

### AlertArn
- **Type**: typing.Optional[str]

### AnomalyDetectorArn
- **Type**: typing.Optional[str]

### AlertName
- **Type**: typing.Optional[str]

### AlertSensitivityThreshold
- **Type**: typing.Optional[int]

### AlertType
- **Type**: typing.Optional[typing.Literal['LAMBDA', 'SNS']]

### AlertStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### AlertFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AlertFiltersTypeDef]


# AnomalyDetectorConfigSummaryTypeDef

### AnomalyDetectorFrequency
- **Type**: typing.Optional[typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']]


# AnomalyDetectorConfigTypeDef

### AnomalyDetectorFrequency
- **Type**: typing.Optional[typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']]


# AnomalyDetectorDataQualityMetricTypeDef

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### MetricSetDataQualityMetricList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricSetDataQualityMetricTypeDef]]


# AnomalyDetectorSummaryTypeDef

### AnomalyDetectorArn
- **Type**: typing.Optional[str]

### AnomalyDetectorName
- **Type**: typing.Optional[str]

### AnomalyDetectorDescription
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVATING', 'ACTIVE', 'BACK_TEST_ACTIVATING', 'BACK_TEST_ACTIVE', 'BACK_TEST_COMPLETE', 'DEACTIVATED', 'DEACTIVATING', 'DELETING', 'FAILED', 'INACTIVE', 'LEARNING']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AnomalyGroupStatisticsTypeDef

### EvaluationStartDate
- **Type**: typing.Optional[str]

### TotalCount
- **Type**: typing.Optional[int]

### ItemizedMetricStatsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.ItemizedMetricStatsTypeDef]]


# AnomalyGroupSummaryTypeDef

### StartTime
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[str]

### AnomalyGroupId
- **Type**: typing.Optional[str]

### AnomalyGroupScore
- **Type**: typing.Optional[float]

### PrimaryMetricName
- **Type**: typing.Optional[str]


# AnomalyGroupTimeSeriesFeedbackTypeDef

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesId
- **Type**: <class 'str'>
- **Required**: Yes

### IsAnomaly
- **Type**: <class 'bool'>
- **Required**: Yes


# AnomalyGroupTimeSeriesTypeDef

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesId
- **Type**: typing.Optional[str]


# AnomalyGroupTypeDef

### StartTime
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[str]

### AnomalyGroupId
- **Type**: typing.Optional[str]

### AnomalyGroupScore
- **Type**: typing.Optional[float]

### PrimaryMetricName
- **Type**: typing.Optional[str]

### MetricLevelImpactList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricLevelImpactTypeDef]]


# AppFlowConfigTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### FlowName
- **Type**: typing.Optional[str]


# AthenaSourceConfigTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### DataCatalog
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### WorkGroupName
- **Type**: typing.Optional[str]

### S3ResultsPath
- **Type**: typing.Optional[str]

### BackTestConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.BackTestConfigurationTypeDef]


# AttributeValueTypeDef

### S
- **Type**: typing.Optional[str]

### N
- **Type**: typing.Optional[str]

### B
- **Type**: typing.Optional[str]

### SS
- **Type**: typing.Optional[typing.List[str]]

### NS
- **Type**: typing.Optional[typing.List[str]]

### BS
- **Type**: typing.Optional[typing.List[str]]


# AutoDetectionMetricSourceTypeDef

### S3SourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AutoDetectionS3SourceConfigTypeDef]


# AutoDetectionS3SourceConfigTypeDef

### TemplatedPathList
- **Type**: typing.Optional[typing.Sequence[str]]

### HistoricalDataPathList
- **Type**: typing.Optional[typing.Sequence[str]]


# BackTestAnomalyDetectorRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# BackTestConfigurationTypeDef

### RunBackTestMode
- **Type**: <class 'bool'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchConfigTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### BackTestConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.BackTestConfigurationTypeDef]


# ContributionMatrixTypeDef

### DimensionContributionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DimensionContributionTypeDef]]


# CreateAlertRequestRequestTypeDef

### AlertName
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ActionTypeDef'>
- **Required**: Yes

### AlertSensitivityThreshold
- **Type**: typing.Optional[int]

### AlertDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AlertFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AlertFiltersTypeDef]


# CreateAlertResponseTypeDef

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAnomalyDetectorRequestRequestTypeDef

### AnomalyDetectorName
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyDetectorConfigTypeDef'>
- **Required**: Yes

### AnomalyDetectorDescription
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAnomalyDetectorResponseTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMetricSetRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricTypeDef]
- **Required**: Yes

### MetricSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricSourceTypeDef'>
- **Required**: Yes

### MetricSetDescription
- **Type**: typing.Optional[str]

### Offset
- **Type**: typing.Optional[int]

### TimestampColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.TimestampColumnTypeDef]

### DimensionList
- **Type**: typing.Optional[typing.Sequence[str]]

### MetricSetFrequency
- **Type**: typing.Optional[typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']]

### Timezone
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### DimensionFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricSetDimensionFilterTypeDef]]


# CreateMetricSetResponseTypeDef

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CsvFormatDescriptorTypeDef

### FileCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### Charset
- **Type**: typing.Optional[str]

### ContainsHeader
- **Type**: typing.Optional[bool]

### Delimiter
- **Type**: typing.Optional[str]

### HeaderList
- **Type**: typing.Optional[typing.Sequence[str]]

### QuoteSymbol
- **Type**: typing.Optional[str]


# DataQualityMetricTypeDef

### MetricType
- **Type**: typing.Optional[typing.Literal['BACKTEST_INFERENCE_DATA_END_TIME_STAMP', 'BACKTEST_INFERENCE_DATA_START_TIME_STAMP', 'BACKTEST_TRAINING_DATA_END_TIME_STAMP', 'BACKTEST_TRAINING_DATA_START_TIME_STAMP', 'COLUMN_COMPLETENESS', 'DIMENSION_UNIQUENESS', 'INVALID_ROWS_COMPLIANCE', 'ROWS_PARTIAL_COMPLIANCE', 'ROWS_PROCESSED', 'TIME_SERIES_COUNT']]

### MetricDescription
- **Type**: typing.Optional[str]

### RelatedColumnName
- **Type**: typing.Optional[str]

### MetricValue
- **Type**: typing.Optional[float]


# DeactivateAnomalyDetectorRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAlertRequestRequestTypeDef

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAnomalyDetectorRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlertRequestRequestTypeDef

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlertResponseTypeDef

### Alert
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.AlertTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnomalyDetectionExecutionsRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAnomalyDetectionExecutionsResponseTypeDef

### ExecutionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.ExecutionStatusTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnomalyDetectorRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAnomalyDetectorResponseTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorName
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorDescription
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyDetectorConfigSummaryTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVATING', 'ACTIVE', 'BACK_TEST_ACTIVATING', 'BACK_TEST_ACTIVE', 'BACK_TEST_COMPLETE', 'DEACTIVATED', 'DEACTIVATING', 'DELETING', 'FAILED', 'INACTIVE', 'LEARNING']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### FailureType
- **Type**: typing.Literal['ACTIVATION_FAILURE', 'BACK_TEST_ACTIVATION_FAILURE', 'DEACTIVATION_FAILURE', 'DELETION_FAILURE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetricSetRequestRequestTypeDef

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMetricSetResponseTypeDef

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSetDescription
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Offset
- **Type**: <class 'int'>
- **Required**: Yes

### MetricList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricTypeDef]
- **Required**: Yes

### TimestampColumn
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.TimestampColumnTypeDef'>
- **Required**: Yes

### DimensionList
- **Type**: typing.List[str]
- **Required**: Yes

### MetricSetFrequency
- **Type**: typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']
- **Required**: Yes

### Timezone
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricSourceTypeDef'>
- **Required**: Yes

### DimensionFilterList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricSetDimensionFilterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectMetricSetConfigRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoDetectionMetricSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.AutoDetectionMetricSourceTypeDef'>
- **Required**: Yes


# DetectMetricSetConfigResponseTypeDef

### DetectedMetricSetConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedMetricSetConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectedCsvFormatDescriptorTypeDef

### FileCompression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]

### Charset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]

### ContainsHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]

### Delimiter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]

### HeaderList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]

### QuoteSymbol
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]


# DetectedFieldTypeDef

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AttributeValueTypeDef]

### Confidence
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'NONE']]

### Message
- **Type**: typing.Optional[str]


# DetectedFileFormatDescriptorTypeDef

### CsvFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedCsvFormatDescriptorTypeDef]

### JsonFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedJsonFormatDescriptorTypeDef]


# DetectedJsonFormatDescriptorTypeDef

### FileCompression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]

### Charset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]


# DetectedMetricSetConfigTypeDef

### Offset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]

### MetricSetFrequency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFieldTypeDef]

### MetricSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedMetricSourceTypeDef]


# DetectedMetricSourceTypeDef

### S3SourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedS3SourceConfigTypeDef]


# DetectedS3SourceConfigTypeDef

### FileFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DetectedFileFormatDescriptorTypeDef]


# DimensionContributionTypeDef

### DimensionName
- **Type**: typing.Optional[str]

### DimensionValueContributionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DimensionValueContributionTypeDef]]


# DimensionFilterTypeDef

### DimensionName
- **Type**: typing.Optional[str]

### DimensionValueList
- **Type**: typing.Optional[typing.Sequence[str]]


# DimensionNameValueTypeDef

### DimensionName
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValue
- **Type**: <class 'str'>
- **Required**: Yes


# DimensionValueContributionTypeDef

### DimensionValue
- **Type**: typing.Optional[str]

### ContributionScore
- **Type**: typing.Optional[float]


# ExecutionStatusTypeDef

### Timestamp
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'IN_PROGRESS', 'PENDING']]

### FailureReason
- **Type**: typing.Optional[str]


# FileFormatDescriptorTypeDef

### CsvFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.CsvFormatDescriptorTypeDef]

### JsonFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.JsonFormatDescriptorTypeDef]


# FilterTypeDef

### DimensionValue
- **Type**: typing.Optional[str]

### FilterOperation
- **Type**: typing.Optional[typing.Literal['EQUALS']]


# GetAnomalyGroupRequestRequestTypeDef

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnomalyGroupResponseTypeDef

### AnomalyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataQualityMetricsRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSetArn
- **Type**: typing.Optional[str]


# GetDataQualityMetricsResponseTypeDef

### AnomalyDetectorDataQualityMetricList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyDetectorDataQualityMetricTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFeedbackRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyGroupTimeSeriesFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyGroupTimeSeriesTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetFeedbackResponseTypeDef

### AnomalyGroupTimeSeriesFeedback
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.TimeSeriesFeedbackTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSampleDataRequestRequestTypeDef

### S3SourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.SampleDataS3SourceConfigTypeDef]


# GetSampleDataResponseTypeDef

### HeaderValues
- **Type**: typing.List[str]
- **Required**: Yes

### SampleRows
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InterMetricImpactDetailsTypeDef

### MetricName
- **Type**: typing.Optional[str]

### AnomalyGroupId
- **Type**: typing.Optional[str]

### RelationshipType
- **Type**: typing.Optional[typing.Literal['CAUSE_OF_INPUT_ANOMALY_GROUP', 'EFFECT_OF_INPUT_ANOMALY_GROUP']]

### ContributionPercentage
- **Type**: typing.Optional[float]


# ItemizedMetricStatsTypeDef

### MetricName
- **Type**: typing.Optional[str]

### OccurrenceCount
- **Type**: typing.Optional[int]


# JsonFormatDescriptorTypeDef

### FileCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### Charset
- **Type**: typing.Optional[str]


# LambdaConfigurationTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListAlertsRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAlertsResponseTypeDef

### AlertSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AlertSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnomalyDetectorsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyDetectorsResponseTypeDef

### AnomalyDetectorSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyDetectorSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnomalyGroupRelatedMetricsRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### RelationshipTypeFilter
- **Type**: typing.Optional[typing.Literal['CAUSE_OF_INPUT_ANOMALY_GROUP', 'EFFECT_OF_INPUT_ANOMALY_GROUP']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyGroupRelatedMetricsResponseTypeDef

### InterMetricImpactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.InterMetricImpactDetailsTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnomalyGroupSummariesRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### SensitivityThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyGroupSummariesResponseTypeDef

### AnomalyGroupSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyGroupSummaryTypeDef]
- **Required**: Yes

### AnomalyGroupStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyGroupStatisticsTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnomalyGroupTimeSeriesRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyGroupTimeSeriesResponseTypeDef

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### TimestampList
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.TimeSeriesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetricSetsRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMetricSetsResponseTypeDef

### MetricSetSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricSetSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricLevelImpactTypeDef

### MetricName
- **Type**: typing.Optional[str]

### NumTimeSeries
- **Type**: typing.Optional[int]

### ContributionMatrix
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.ContributionMatrixTypeDef]


# MetricSetDataQualityMetricTypeDef

### MetricSetArn
- **Type**: typing.Optional[str]

### DataQualityMetricList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DataQualityMetricTypeDef]]


# MetricSetDimensionFilterTypeDef

### Name
- **Type**: typing.Optional[str]

### FilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutmetrics_classes.FilterTypeDef]]


# MetricSetSummaryTypeDef

### MetricSetArn
- **Type**: typing.Optional[str]

### AnomalyDetectorArn
- **Type**: typing.Optional[str]

### MetricSetDescription
- **Type**: typing.Optional[str]

### MetricSetName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# MetricSourceTypeDef

### S3SourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.S3SourceConfigTypeDef]

### AppFlowConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AppFlowConfigTypeDef]

### CloudWatchConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.CloudWatchConfigTypeDef]

### RDSSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.RDSSourceConfigTypeDef]

### RedshiftSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.RedshiftSourceConfigTypeDef]

### AthenaSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AthenaSourceConfigTypeDef]


# MetricTypeDef

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Literal['AVG', 'SUM']
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# PutFeedbackRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyGroupTimeSeriesFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyGroupTimeSeriesFeedbackTypeDef'>
- **Required**: Yes


# RDSSourceConfigTypeDef

### DBInstanceIdentifier
- **Type**: typing.Optional[str]

### DatabaseHost
- **Type**: typing.Optional[str]

### DatabasePort
- **Type**: typing.Optional[int]

### SecretManagerArn
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.VpcConfigurationTypeDef]


# RedshiftSourceConfigTypeDef

### ClusterIdentifier
- **Type**: typing.Optional[str]

### DatabaseHost
- **Type**: typing.Optional[str]

### DatabasePort
- **Type**: typing.Optional[int]

### SecretManagerArn
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.VpcConfigurationTypeDef]


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


# S3SourceConfigTypeDef

### RoleArn
- **Type**: typing.Optional[str]

### TemplatedPathList
- **Type**: typing.Optional[typing.Sequence[str]]

### HistoricalDataPathList
- **Type**: typing.Optional[typing.Sequence[str]]

### FileFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.FileFormatDescriptorTypeDef]


# SNSConfigurationTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'LONG_TEXT', 'SHORT_TEXT']]


# SampleDataS3SourceConfigTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileFormatDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.FileFormatDescriptorTypeDef'>
- **Required**: Yes

### TemplatedPathList
- **Type**: typing.Optional[typing.Sequence[str]]

### HistoricalDataPathList
- **Type**: typing.Optional[typing.Sequence[str]]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimeSeriesFeedbackTypeDef

### TimeSeriesId
- **Type**: typing.Optional[str]

### IsAnomaly
- **Type**: typing.Optional[bool]


# TimeSeriesTypeDef

### TimeSeriesId
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics_classes.DimensionNameValueTypeDef]
- **Required**: Yes

### MetricValueList
- **Type**: typing.List[float]
- **Required**: Yes


# TimestampColumnTypeDef

### ColumnName
- **Type**: typing.Optional[str]

### ColumnFormat
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAlertRequestRequestTypeDef

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes

### AlertDescription
- **Type**: typing.Optional[str]

### AlertSensitivityThreshold
- **Type**: typing.Optional[int]

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.ActionTypeDef]

### AlertFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AlertFiltersTypeDef]


# UpdateAlertResponseTypeDef

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAnomalyDetectorRequestRequestTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: typing.Optional[str]

### AnomalyDetectorDescription
- **Type**: typing.Optional[str]

### AnomalyDetectorConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.AnomalyDetectorConfigTypeDef]


# UpdateAnomalyDetectorResponseTypeDef

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMetricSetRequestRequestTypeDef

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSetDescription
- **Type**: typing.Optional[str]

### MetricList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricTypeDef]]

### Offset
- **Type**: typing.Optional[int]

### TimestampColumn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.TimestampColumnTypeDef]

### DimensionList
- **Type**: typing.Optional[typing.Sequence[str]]

### MetricSetFrequency
- **Type**: typing.Optional[typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']]

### MetricSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricSourceTypeDef]

### DimensionFilterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutmetrics_classes.MetricSetDimensionFilterTypeDef]]


# UpdateMetricSetResponseTypeDef

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcConfigurationTypeDef

### SubnetIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes



# Lookoutmetrics Classes

# Action

### SNSConfiguration
- **Type**: <class 'NoneType'>

### LambdaConfiguration
- **Type**: <class 'NoneType'>


# ActivateAnomalyDetectorRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# Alert

### Action
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AlertFiltersOutput]


# AlertFilters

### MetricList
- **Type**: typing.Optional[typing.List[str]]

### DimensionFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DimensionFilter]]


# AlertFiltersOutput

### MetricList
- **Type**: typing.Optional[typing.List[str]]

### DimensionFilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DimensionFilterOutput]]


# AlertSummary

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


# AnomalyDetectorConfig

### AnomalyDetectorFrequency
- **Type**: typing.Optional[typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']]


# AnomalyDetectorConfigSummary

### AnomalyDetectorFrequency
- **Type**: typing.Optional[typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']]


# AnomalyDetectorDataQualityMetric

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]

### MetricSetDataQualityMetricList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSetDataQualityMetric]]


# AnomalyDetectorSummary

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


# AnomalyGroup

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricLevelImpact]]


# AnomalyGroupStatistics

### EvaluationStartDate
- **Type**: typing.Optional[str]

### TotalCount
- **Type**: typing.Optional[int]

### ItemizedMetricStatsList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ItemizedMetricStats]]


# AnomalyGroupSummary

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


# AnomalyGroupTimeSeries

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesId
- **Type**: typing.Optional[str]


# AnomalyGroupTimeSeriesFeedback

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesId
- **Type**: <class 'str'>
- **Required**: Yes

### IsAnomaly
- **Type**: <class 'bool'>
- **Required**: Yes


# AppFlowConfig

### RoleArn
- **Type**: typing.Optional[str]

### FlowName
- **Type**: typing.Optional[str]


# AthenaSourceConfig

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
- **Type**: <class 'NoneType'>


# AttributeValue

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


# AutoDetectionMetricSource

### S3SourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AutoDetectionS3SourceConfig]


# AutoDetectionS3SourceConfig

### TemplatedPathList
- **Type**: typing.Optional[typing.List[str]]

### HistoricalDataPathList
- **Type**: typing.Optional[typing.List[str]]


# BackTestAnomalyDetectorRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# BackTestConfiguration

### RunBackTestMode
- **Type**: <class 'bool'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchConfig

### RoleArn
- **Type**: typing.Optional[str]

### BackTestConfiguration
- **Type**: <class 'NoneType'>


# ContributionMatrix

### DimensionContributionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DimensionContribution]]


# CreateAlertRequest

### AlertName
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.Action'>
- **Required**: Yes

### AlertSensitivityThreshold
- **Type**: typing.Optional[int]

### AlertDescription
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### AlertFilters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AlertFilters, aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AlertFiltersOutput, NoneType]


# CreateAlertResponse

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAnomalyDetectorRequest

### AnomalyDetectorName
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyDetectorConfig'>
- **Required**: Yes

### AnomalyDetectorDescription
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAnomalyDetectorResponse

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMetricSetRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSetName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.Metric]
- **Required**: Yes

### MetricSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSource, aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSourceOutput]
- **Required**: Yes

### MetricSetDescription
- **Type**: typing.Optional[str]

### Offset
- **Type**: typing.Optional[int]

### TimestampColumn
- **Type**: <class 'NoneType'>

### DimensionList
- **Type**: typing.Optional[typing.List[str]]

### MetricSetFrequency
- **Type**: typing.Optional[typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']]

### Timezone
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### DimensionFilterList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSetDimensionFilter, aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSetDimensionFilterOutput]]]


# CreateMetricSetResponse

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# CsvFormatDescriptor

### FileCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### Charset
- **Type**: typing.Optional[str]

### ContainsHeader
- **Type**: typing.Optional[bool]

### Delimiter
- **Type**: typing.Optional[str]

### HeaderList
- **Type**: typing.Optional[typing.List[str]]

### QuoteSymbol
- **Type**: typing.Optional[str]


# CsvFormatDescriptorOutput

### FileCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### Charset
- **Type**: typing.Optional[str]

### ContainsHeader
- **Type**: typing.Optional[bool]

### Delimiter
- **Type**: typing.Optional[str]

### HeaderList
- **Type**: typing.Optional[typing.List[str]]

### QuoteSymbol
- **Type**: typing.Optional[str]


# DataQualityMetric

### MetricType
- **Type**: typing.Optional[typing.Literal['BACKTEST_INFERENCE_DATA_END_TIME_STAMP', 'BACKTEST_INFERENCE_DATA_START_TIME_STAMP', 'BACKTEST_TRAINING_DATA_END_TIME_STAMP', 'BACKTEST_TRAINING_DATA_START_TIME_STAMP', 'COLUMN_COMPLETENESS', 'DIMENSION_UNIQUENESS', 'INVALID_ROWS_COMPLIANCE', 'ROWS_PARTIAL_COMPLIANCE', 'ROWS_PROCESSED', 'TIME_SERIES_COUNT']]

### MetricDescription
- **Type**: typing.Optional[str]

### RelatedColumnName
- **Type**: typing.Optional[str]

### MetricValue
- **Type**: typing.Optional[float]


# DeactivateAnomalyDetectorRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAlertRequest

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAnomalyDetectorRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlertRequest

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlertResponse

### Alert
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.Alert'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAnomalyDetectionExecutionsRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeAnomalyDetectionExecutionsResponse

### ExecutionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ExecutionStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAnomalyDetectorRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAnomalyDetectorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyDetectorConfigSummary'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMetricSetRequest

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMetricSetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.Metric]
- **Required**: Yes

### TimestampColumn
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.TimestampColumn'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSourceOutput'>
- **Required**: Yes

### DimensionFilterList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSetDimensionFilterOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# DetectMetricSetConfigRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoDetectionMetricSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AutoDetectionMetricSource'>
- **Required**: Yes


# DetectMetricSetConfigResponse

### DetectedMetricSetConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedMetricSetConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# DetectedCsvFormatDescriptor

### FileCompression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]

### Charset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]

### ContainsHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]

### Delimiter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]

### HeaderList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]

### QuoteSymbol
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]


# DetectedField

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AttributeValue]

### Confidence
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'NONE']]

### Message
- **Type**: typing.Optional[str]


# DetectedFileFormatDescriptor

### CsvFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedCsvFormatDescriptor]

### JsonFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedJsonFormatDescriptor]


# DetectedJsonFormatDescriptor

### FileCompression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]

### Charset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]


# DetectedMetricSetConfig

### Offset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]

### MetricSetFrequency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedField]

### MetricSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedMetricSource]


# DetectedMetricSource

### S3SourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedS3SourceConfig]


# DetectedS3SourceConfig

### FileFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DetectedFileFormatDescriptor]


# DimensionContribution

### DimensionName
- **Type**: typing.Optional[str]

### DimensionValueContributionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DimensionValueContribution]]


# DimensionFilter

### DimensionName
- **Type**: typing.Optional[str]

### DimensionValueList
- **Type**: typing.Optional[typing.List[str]]


# DimensionFilterOutput

### DimensionName
- **Type**: typing.Optional[str]

### DimensionValueList
- **Type**: typing.Optional[typing.List[str]]


# DimensionNameValue

### DimensionName
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValue
- **Type**: <class 'str'>
- **Required**: Yes


# DimensionValueContribution

### DimensionValue
- **Type**: typing.Optional[str]

### ContributionScore
- **Type**: typing.Optional[float]


# ExecutionStatus

### Timestamp
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'FAILED_TO_SCHEDULE', 'IN_PROGRESS', 'PENDING']]

### FailureReason
- **Type**: typing.Optional[str]


# FileFormatDescriptor

### CsvFormatDescriptor
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.CsvFormatDescriptor, aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.CsvFormatDescriptorOutput, NoneType]

### JsonFormatDescriptor
- **Type**: <class 'NoneType'>


# FileFormatDescriptorOutput

### CsvFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.CsvFormatDescriptorOutput]

### JsonFormatDescriptor
- **Type**: <class 'NoneType'>


# Filter

### DimensionValue
- **Type**: typing.Optional[str]

### FilterOperation
- **Type**: typing.Optional[typing.Literal['EQUALS']]


# GetAnomalyGroupRequest

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnomalyGroupResponse

### AnomalyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataQualityMetricsRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSetArn
- **Type**: typing.Optional[str]


# GetDataQualityMetricsResponse

### AnomalyDetectorDataQualityMetricList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyDetectorDataQualityMetric]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# GetFeedbackRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyGroupTimeSeriesFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyGroupTimeSeries'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetFeedbackResponse

### AnomalyGroupTimeSeriesFeedback
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.TimeSeriesFeedback]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSampleDataRequest

### S3SourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.SampleDataS3SourceConfig]


# GetSampleDataResponse

### HeaderValues
- **Type**: typing.List[str]
- **Required**: Yes

### SampleRows
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# InterMetricImpactDetails

### MetricName
- **Type**: typing.Optional[str]

### AnomalyGroupId
- **Type**: typing.Optional[str]

### RelationshipType
- **Type**: typing.Optional[typing.Literal['CAUSE_OF_INPUT_ANOMALY_GROUP', 'EFFECT_OF_INPUT_ANOMALY_GROUP']]

### ContributionPercentage
- **Type**: typing.Optional[float]


# ItemizedMetricStats

### MetricName
- **Type**: typing.Optional[str]

### OccurrenceCount
- **Type**: typing.Optional[int]


# JsonFormatDescriptor

### FileCompression
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]

### Charset
- **Type**: typing.Optional[str]


# LambdaConfiguration

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListAlertsRequest

### AnomalyDetectorArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAlertsResponse

### AlertSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AlertSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyDetectorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyDetectorsResponse

### AnomalyDetectorSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyDetectorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyGroupRelatedMetricsRequest

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


# ListAnomalyGroupRelatedMetricsResponse

### InterMetricImpactList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.InterMetricImpactDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyGroupSummariesRequest

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


# ListAnomalyGroupSummariesResponse

### AnomalyGroupSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyGroupSummary]
- **Required**: Yes

### AnomalyGroupStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyGroupStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalyGroupTimeSeriesRequest

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


# ListAnomalyGroupTimeSeriesResponse

### AnomalyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### TimestampList
- **Type**: typing.List[str]
- **Required**: Yes

### TimeSeriesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.TimeSeries]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMetricSetsRequest

### AnomalyDetectorArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMetricSetsResponse

### MetricSetSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# Metric

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### AggregationFunction
- **Type**: typing.Literal['AVG', 'SUM']
- **Required**: Yes

### Namespace
- **Type**: typing.Optional[str]


# MetricLevelImpact

### MetricName
- **Type**: typing.Optional[str]

### NumTimeSeries
- **Type**: typing.Optional[int]

### ContributionMatrix
- **Type**: <class 'NoneType'>


# MetricSetDataQualityMetric

### MetricSetArn
- **Type**: typing.Optional[str]

### DataQualityMetricList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DataQualityMetric]]


# MetricSetDimensionFilter

### Name
- **Type**: typing.Optional[str]

### FilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.Filter]]


# MetricSetDimensionFilterOutput

### Name
- **Type**: typing.Optional[str]

### FilterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.Filter]]


# MetricSetSummary

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


# MetricSource

### S3SourceConfig
- **Type**: <class 'NoneType'>

### AppFlowConfig
- **Type**: <class 'NoneType'>

### CloudWatchConfig
- **Type**: <class 'NoneType'>

### RDSSourceConfig
- **Type**: <class 'NoneType'>

### RedshiftSourceConfig
- **Type**: <class 'NoneType'>

### AthenaSourceConfig
- **Type**: <class 'NoneType'>


# MetricSourceOutput

### S3SourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.S3SourceConfigOutput]

### AppFlowConfig
- **Type**: <class 'NoneType'>

### CloudWatchConfig
- **Type**: <class 'NoneType'>

### RDSSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.RDSSourceConfigOutput]

### RedshiftSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.RedshiftSourceConfigOutput]

### AthenaSourceConfig
- **Type**: <class 'NoneType'>


# PutFeedbackRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalyGroupTimeSeriesFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AnomalyGroupTimeSeriesFeedback'>
- **Required**: Yes


# RDSSourceConfig

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
- **Type**: <class 'NoneType'>


# RDSSourceConfigOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.VpcConfigurationOutput]


# RedshiftSourceConfig

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
- **Type**: <class 'NoneType'>


# RedshiftSourceConfigOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.VpcConfigurationOutput]


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


# S3SourceConfig

### RoleArn
- **Type**: typing.Optional[str]

### TemplatedPathList
- **Type**: typing.Optional[typing.List[str]]

### HistoricalDataPathList
- **Type**: typing.Optional[typing.List[str]]

### FileFormatDescriptor
- **Type**: <class 'NoneType'>


# S3SourceConfigOutput

### RoleArn
- **Type**: typing.Optional[str]

### TemplatedPathList
- **Type**: typing.Optional[typing.List[str]]

### HistoricalDataPathList
- **Type**: typing.Optional[typing.List[str]]

### FileFormatDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.FileFormatDescriptorOutput]


# SNSConfiguration

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'LONG_TEXT', 'SHORT_TEXT']]


# SampleDataS3SourceConfig

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileFormatDescriptor
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.FileFormatDescriptor, aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.FileFormatDescriptorOutput]
- **Required**: Yes

### TemplatedPathList
- **Type**: typing.Optional[typing.List[str]]

### HistoricalDataPathList
- **Type**: typing.Optional[typing.List[str]]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TimeSeries

### TimeSeriesId
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.DimensionNameValue]
- **Required**: Yes

### MetricValueList
- **Type**: typing.List[float]
- **Required**: Yes


# TimeSeriesFeedback

### TimeSeriesId
- **Type**: typing.Optional[str]

### IsAnomaly
- **Type**: typing.Optional[bool]


# TimestampColumn

### ColumnName
- **Type**: typing.Optional[str]

### ColumnFormat
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAlertRequest

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes

### AlertDescription
- **Type**: typing.Optional[str]

### AlertSensitivityThreshold
- **Type**: typing.Optional[int]

### Action
- **Type**: <class 'NoneType'>

### AlertFilters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AlertFilters, aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.AlertFiltersOutput, NoneType]


# UpdateAlertResponse

### AlertArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAnomalyDetectorRequest

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: typing.Optional[str]

### AnomalyDetectorDescription
- **Type**: typing.Optional[str]

### AnomalyDetectorConfig
- **Type**: <class 'NoneType'>


# UpdateAnomalyDetectorResponse

### AnomalyDetectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMetricSetRequest

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricSetDescription
- **Type**: typing.Optional[str]

### MetricList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.Metric]]

### Offset
- **Type**: typing.Optional[int]

### TimestampColumn
- **Type**: <class 'NoneType'>

### DimensionList
- **Type**: typing.Optional[typing.List[str]]

### MetricSetFrequency
- **Type**: typing.Optional[typing.Literal['P1D', 'PT10M', 'PT1H', 'PT5M']]

### MetricSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSource, aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSourceOutput, NoneType]

### DimensionFilterList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSetDimensionFilter, aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.MetricSetDimensionFilterOutput]]]


# UpdateMetricSetResponse

### MetricSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutmetrics.lookoutmetrics_classes.ResponseMetadata'>
- **Required**: Yes


# VpcConfiguration

### SubnetIdList
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIdList
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigurationOutput

### SubnetIdList
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIdList
- **Type**: typing.List[str]
- **Required**: Yes



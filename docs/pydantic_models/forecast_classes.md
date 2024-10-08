# Pydantic Models in forecast_classes

# ActionTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['ADD', 'DIVIDE', 'MULTIPLY', 'SUBTRACT']
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# AdditionalDatasetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# AttributeConfigTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Transformations
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaselineMetricTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]


# BaselineTypeDef

### PredictorBaseline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PredictorBaselineTypeDef]


# CategoricalParameterRangeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ContinuousParameterRangeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'float'>
- **Required**: Yes

### MinValue
- **Type**: <class 'float'>
- **Required**: Yes

### ScalingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Linear', 'Logarithmic', 'ReverseLogarithmic']]


# CreateAutoPredictorRequestRequestTypeDef

### PredictorName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: typing.Optional[int]

### ForecastTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### ForecastDimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### ForecastFrequency
- **Type**: typing.Optional[str]

### DataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataConfigTypeDef]

### EncryptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfigTypeDef]

### ReferencePredictorArn
- **Type**: typing.Optional[str]

### OptimizationMetric
- **Type**: typing.Optional[typing.Literal['AverageWeightedQuantileLoss', 'MAPE', 'MASE', 'RMSE', 'WAPE']]

### ExplainPredictor
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]

### MonitorConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.MonitorConfigTypeDef]

### TimeAlignmentBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeAlignmentBoundaryTypeDef]


# CreateAutoPredictorResponseTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetGroupRequestRequestTypeDef

### DatasetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Literal['CUSTOM', 'EC2_CAPACITY', 'INVENTORY_PLANNING', 'METRICS', 'RETAIL', 'WEB_TRAFFIC', 'WORK_FORCE']
- **Required**: Yes

### DatasetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]


# CreateDatasetGroupResponseTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetImportJobRequestRequestTypeDef

### DatasetImportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataSourceTypeDef'>
- **Required**: Yes

### TimestampFormat
- **Type**: typing.Optional[str]

### TimeZone
- **Type**: typing.Optional[str]

### UseGeolocationForTimeZone
- **Type**: typing.Optional[bool]

### GeolocationFormat
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]

### Format
- **Type**: typing.Optional[str]

### ImportMode
- **Type**: typing.Optional[typing.Literal['FULL', 'INCREMENTAL']]


# CreateDatasetImportJobResponseTypeDef

### DatasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetRequestRequestTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Literal['CUSTOM', 'EC2_CAPACITY', 'INVENTORY_PLANNING', 'METRICS', 'RETAIL', 'WEB_TRAFFIC', 'WORK_FORCE']
- **Required**: Yes

### DatasetType
- **Type**: typing.Literal['ITEM_METADATA', 'RELATED_TIME_SERIES', 'TARGET_TIME_SERIES']
- **Required**: Yes

### Schema
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaTypeDef'>
- **Required**: Yes

### DataFrequency
- **Type**: typing.Optional[str]

### EncryptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]


# CreateDatasetResponseTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExplainabilityExportRequestRequestTypeDef

### ExplainabilityExportName
- **Type**: <class 'str'>
- **Required**: Yes

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]

### Format
- **Type**: typing.Optional[str]


# CreateExplainabilityExportResponseTypeDef

### ExplainabilityExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExplainabilityRequestRequestTypeDef

### ExplainabilityName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExplainabilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityConfigTypeDef'>
- **Required**: Yes

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataSourceTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.SchemaTypeDef]

### EnableVisualization
- **Type**: typing.Optional[bool]

### StartDateTime
- **Type**: typing.Optional[str]

### EndDateTime
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]


# CreateExplainabilityResponseTypeDef

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateForecastExportJobRequestRequestTypeDef

### ForecastExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]

### Format
- **Type**: typing.Optional[str]


# CreateForecastExportJobResponseTypeDef

### ForecastExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateForecastRequestRequestTypeDef

### ForecastName
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]

### TimeSeriesSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorTypeDef]


# CreateForecastResponseTypeDef

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMonitorRequestRequestTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]


# CreateMonitorResponseTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePredictorBacktestExportJobRequestRequestTypeDef

### PredictorBacktestExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]

### Format
- **Type**: typing.Optional[str]


# CreatePredictorBacktestExportJobResponseTypeDef

### PredictorBacktestExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePredictorRequestRequestTypeDef

### PredictorName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### FeaturizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.FeaturizationConfigTypeDef'>
- **Required**: Yes

### AlgorithmArn
- **Type**: typing.Optional[str]

### ForecastTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### PerformAutoML
- **Type**: typing.Optional[bool]

### AutoMLOverrideStrategy
- **Type**: typing.Optional[typing.Literal['AccuracyOptimized', 'LatencyOptimized']]

### PerformHPO
- **Type**: typing.Optional[bool]

### TrainingParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EvaluationParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.EvaluationParametersTypeDef]

### HPOConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.HyperParameterTuningJobConfigTypeDef]

### EncryptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]

### OptimizationMetric
- **Type**: typing.Optional[typing.Literal['AverageWeightedQuantileLoss', 'MAPE', 'MASE', 'RMSE', 'WAPE']]


# CreatePredictorResponseTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWhatIfAnalysisRequestRequestTypeDef

### WhatIfAnalysisName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]


# CreateWhatIfAnalysisResponseTypeDef

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWhatIfForecastExportRequestRequestTypeDef

### WhatIfForecastExportName
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfForecastArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]

### Format
- **Type**: typing.Optional[str]


# CreateWhatIfForecastExportResponseTypeDef

### WhatIfForecastExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWhatIfForecastRequestRequestTypeDef

### WhatIfForecastName
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesTransformations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesTransformationTypeDef]]

### TimeSeriesReplacementsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesReplacementsDataSourceTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]


# CreateWhatIfForecastResponseTypeDef

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataConfigTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.AttributeConfigTypeDef]]

### AdditionalDatasets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.AdditionalDatasetTypeDef]]


# DataDestinationTypeDef

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.S3ConfigTypeDef'>
- **Required**: Yes


# DataSourceTypeDef

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.S3ConfigTypeDef'>
- **Required**: Yes


# DatasetGroupSummaryTypeDef

### DatasetGroupArn
- **Type**: typing.Optional[str]

### DatasetGroupName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# DatasetImportJobSummaryTypeDef

### DatasetImportJobArn
- **Type**: typing.Optional[str]

### DatasetImportJobName
- **Type**: typing.Optional[str]

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataSourceTypeDef]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]

### ImportMode
- **Type**: typing.Optional[typing.Literal['FULL', 'INCREMENTAL']]


# DatasetSummaryTypeDef

### DatasetArn
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### DatasetType
- **Type**: typing.Optional[typing.Literal['ITEM_METADATA', 'RELATED_TIME_SERIES', 'TARGET_TIME_SERIES']]

### Domain
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'EC2_CAPACITY', 'INVENTORY_PLANNING', 'METRICS', 'RETAIL', 'WEB_TRAFFIC', 'WORK_FORCE']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# DeleteDatasetGroupRequestRequestTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetImportJobRequestRequestTypeDef

### DatasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetRequestRequestTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExplainabilityExportRequestRequestTypeDef

### ExplainabilityExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExplainabilityRequestRequestTypeDef

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteForecastExportJobRequestRequestTypeDef

### ForecastExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteForecastRequestRequestTypeDef

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitorRequestRequestTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePredictorBacktestExportJobRequestRequestTypeDef

### PredictorBacktestExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePredictorRequestRequestTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceTreeRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfAnalysisRequestRequestTypeDef

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfForecastExportRequestRequestTypeDef

### WhatIfForecastExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfForecastRequestRequestTypeDef

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoPredictorRequestRequestTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoPredictorResponseTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### ForecastTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastDimensions
- **Type**: typing.List[str]
- **Required**: Yes

### DatasetImportJobArns
- **Type**: typing.List[str]
- **Required**: Yes

### DataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataConfigTypeDef'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfigTypeDef'>
- **Required**: Yes

### ReferencePredictorSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ReferencePredictorSummaryTypeDef'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OptimizationMetric
- **Type**: typing.Literal['AverageWeightedQuantileLoss', 'MAPE', 'MASE', 'RMSE', 'WAPE']
- **Required**: Yes

### ExplainabilityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityInfoTypeDef'>
- **Required**: Yes

### MonitorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.MonitorInfoTypeDef'>
- **Required**: Yes

### TimeAlignmentBoundary
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeAlignmentBoundaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetGroupRequestRequestTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetGroupResponseTypeDef

### DatasetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArns
- **Type**: typing.List[str]
- **Required**: Yes

### Domain
- **Type**: typing.Literal['CUSTOM', 'EC2_CAPACITY', 'INVENTORY_PLANNING', 'METRICS', 'RETAIL', 'WEB_TRAFFIC', 'WORK_FORCE']
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetImportJobRequestRequestTypeDef

### DatasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetImportJobResponseTypeDef

### DatasetImportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimestampFormat
- **Type**: <class 'str'>
- **Required**: Yes

### TimeZone
- **Type**: <class 'str'>
- **Required**: Yes

### UseGeolocationForTimeZone
- **Type**: <class 'bool'>
- **Required**: Yes

### GeolocationFormat
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataSourceTypeDef'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### FieldStatistics
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.forecast_classes.StatisticsTypeDef]
- **Required**: Yes

### DataSize
- **Type**: <class 'float'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### ImportMode
- **Type**: typing.Literal['FULL', 'INCREMENTAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetRequestRequestTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Literal['CUSTOM', 'EC2_CAPACITY', 'INVENTORY_PLANNING', 'METRICS', 'RETAIL', 'WEB_TRAFFIC', 'WORK_FORCE']
- **Required**: Yes

### DatasetType
- **Type**: typing.Literal['ITEM_METADATA', 'RELATED_TIME_SERIES', 'TARGET_TIME_SERIES']
- **Required**: Yes

### DataFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaTypeDef'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfigTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExplainabilityExportRequestRequestTypeDef

### ExplainabilityExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExplainabilityExportResponseTypeDef

### ExplainabilityExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExplainabilityExportName
- **Type**: <class 'str'>
- **Required**: Yes

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExplainabilityRequestRequestTypeDef

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExplainabilityResponseTypeDef

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExplainabilityName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExplainabilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityConfigTypeDef'>
- **Required**: Yes

### EnableVisualization
- **Type**: <class 'bool'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataSourceTypeDef'>
- **Required**: Yes

### Schema
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaTypeDef'>
- **Required**: Yes

### StartDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### EndDateTime
- **Type**: <class 'str'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeForecastExportJobRequestRequestTypeDef

### ForecastExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeForecastExportJobResponseTypeDef

### ForecastExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeForecastRequestRequestTypeDef

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeForecastResponseTypeDef

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastTypes
- **Type**: typing.List[str]
- **Required**: Yes

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TimeSeriesSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMonitorRequestRequestTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMonitorResponseTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### LastEvaluationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastEvaluationState
- **Type**: <class 'str'>
- **Required**: Yes

### Baseline
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.BaselineTypeDef'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EstimatedEvaluationTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePredictorBacktestExportJobRequestRequestTypeDef

### PredictorBacktestExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePredictorBacktestExportJobResponseTypeDef

### PredictorBacktestExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorBacktestExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePredictorRequestRequestTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePredictorResponseTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorName
- **Type**: <class 'str'>
- **Required**: Yes

### AlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### AutoMLAlgorithmArns
- **Type**: typing.List[str]
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### ForecastTypes
- **Type**: typing.List[str]
- **Required**: Yes

### PerformAutoML
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoMLOverrideStrategy
- **Type**: typing.Literal['AccuracyOptimized', 'LatencyOptimized']
- **Required**: Yes

### PerformHPO
- **Type**: <class 'bool'>
- **Required**: Yes

### TrainingParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### EvaluationParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.EvaluationParametersTypeDef'>
- **Required**: Yes

### HPOConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.HyperParameterTuningJobConfigTypeDef'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### FeaturizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.FeaturizationConfigTypeDef'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfigTypeDef'>
- **Required**: Yes

### PredictorExecutionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.PredictorExecutionDetailsTypeDef'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### IsAutoPredictor
- **Type**: <class 'bool'>
- **Required**: Yes

### DatasetImportJobArns
- **Type**: typing.List[str]
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OptimizationMetric
- **Type**: typing.Literal['AverageWeightedQuantileLoss', 'MAPE', 'MASE', 'RMSE', 'WAPE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWhatIfAnalysisRequestRequestTypeDef

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWhatIfAnalysisResponseTypeDef

### WhatIfAnalysisName
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TimeSeriesSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWhatIfForecastExportRequestRequestTypeDef

### WhatIfForecastExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWhatIfForecastExportResponseTypeDef

### WhatIfForecastExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfForecastExportName
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfForecastArns
- **Type**: typing.List[str]
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Format
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWhatIfForecastRequestRequestTypeDef

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWhatIfForecastResponseTypeDef

### WhatIfForecastName
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TimeSeriesTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesTransformationTypeDef]
- **Required**: Yes

### TimeSeriesReplacementsDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesReplacementsDataSourceTypeDef'>
- **Required**: Yes

### ForecastTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionConfigTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorMetricTypeDef

### ForecastType
- **Type**: typing.Optional[str]

### WAPE
- **Type**: typing.Optional[float]

### RMSE
- **Type**: typing.Optional[float]

### MASE
- **Type**: typing.Optional[float]

### MAPE
- **Type**: typing.Optional[float]


# EvaluationParametersTypeDef

### NumberOfBacktestWindows
- **Type**: typing.Optional[int]

### BackTestWindowOffset
- **Type**: typing.Optional[int]


# EvaluationResultTypeDef

### AlgorithmArn
- **Type**: typing.Optional[str]

### TestWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.WindowSummaryTypeDef]]


# ExplainabilityConfigTypeDef

### TimeSeriesGranularity
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### TimePointGranularity
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes


# ExplainabilityExportSummaryTypeDef

### ExplainabilityExportArn
- **Type**: typing.Optional[str]

### ExplainabilityExportName
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# ExplainabilityInfoTypeDef

### ExplainabilityArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ExplainabilitySummaryTypeDef

### ExplainabilityArn
- **Type**: typing.Optional[str]

### ExplainabilityName
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ExplainabilityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityConfigTypeDef]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# FeaturizationConfigTypeDef

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastDimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### Featurizations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FeaturizationTypeDef]]


# FeaturizationMethodTypeDef

### FeaturizationMethodName
- **Type**: typing.Literal['filling']
- **Required**: Yes

### FeaturizationMethodParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FeaturizationTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturizationPipeline
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FeaturizationMethodTypeDef]]


# FilterTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['IS', 'IS_NOT']
- **Required**: Yes


# ForecastExportJobSummaryTypeDef

### ForecastExportJobArn
- **Type**: typing.Optional[str]

### ForecastExportJobName
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# ForecastSummaryTypeDef

### ForecastArn
- **Type**: typing.Optional[str]

### ForecastName
- **Type**: typing.Optional[str]

### PredictorArn
- **Type**: typing.Optional[str]

### CreatedUsingAutoPredictor
- **Type**: typing.Optional[bool]

### DatasetGroupArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# GetAccuracyMetricsRequestRequestTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccuracyMetricsResponseTypeDef

### PredictorEvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.EvaluationResultTypeDef]
- **Required**: Yes

### IsAutoPredictor
- **Type**: <class 'bool'>
- **Required**: Yes

### AutoMLOverrideStrategy
- **Type**: typing.Literal['AccuracyOptimized', 'LatencyOptimized']
- **Required**: Yes

### OptimizationMetric
- **Type**: typing.Literal['AverageWeightedQuantileLoss', 'MAPE', 'MASE', 'RMSE', 'WAPE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HyperParameterTuningJobConfigTypeDef

### ParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ParameterRangesTypeDef]


# InputDataConfigTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### SupplementaryFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.SupplementaryFeatureTypeDef]]


# IntegerParameterRangeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MaxValue
- **Type**: <class 'int'>
- **Required**: Yes

### MinValue
- **Type**: <class 'int'>
- **Required**: Yes

### ScalingType
- **Type**: typing.Optional[typing.Literal['Auto', 'Linear', 'Logarithmic', 'ReverseLogarithmic']]


# ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListDatasetGroupsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetGroupsResponseTypeDef

### DatasetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.DatasetGroupSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListDatasetImportJobsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListDatasetImportJobsResponseTypeDef

### DatasetImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.DatasetImportJobSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetsRequestListDatasetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListDatasetsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponseTypeDef

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.DatasetSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExplainabilitiesRequestListExplainabilitiesPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListExplainabilitiesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListExplainabilitiesResponseTypeDef

### Explainabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.ExplainabilitySummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExplainabilityExportsRequestListExplainabilityExportsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListExplainabilityExportsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListExplainabilityExportsResponseTypeDef

### ExplainabilityExports
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityExportSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListForecastExportJobsRequestListForecastExportJobsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListForecastExportJobsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListForecastExportJobsResponseTypeDef

### ForecastExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.ForecastExportJobSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListForecastsRequestListForecastsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListForecastsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListForecastsResponseTypeDef

### Forecasts
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.ForecastSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMonitorEvaluationsRequestListMonitorEvaluationsPaginateTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListMonitorEvaluationsRequestRequestTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListMonitorEvaluationsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorMonitorEvaluations
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorMonitorEvaluationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMonitorsRequestListMonitorsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListMonitorsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListMonitorsResponseTypeDef

### Monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.MonitorSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPredictorBacktestExportJobsRequestListPredictorBacktestExportJobsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListPredictorBacktestExportJobsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListPredictorBacktestExportJobsResponseTypeDef

### PredictorBacktestExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorBacktestExportJobSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPredictorsRequestListPredictorsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListPredictorsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListPredictorsResponseTypeDef

### Predictors
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWhatIfAnalysesRequestListWhatIfAnalysesPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListWhatIfAnalysesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListWhatIfAnalysesResponseTypeDef

### WhatIfAnalyses
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.WhatIfAnalysisSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWhatIfForecastExportsRequestListWhatIfForecastExportsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListWhatIfForecastExportsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListWhatIfForecastExportsResponseTypeDef

### WhatIfForecastExports
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.WhatIfForecastExportSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWhatIfForecastsRequestListWhatIfForecastsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListWhatIfForecastsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]


# ListWhatIfForecastsResponseTypeDef

### WhatIfForecasts
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.WhatIfForecastSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricResultTypeDef

### MetricName
- **Type**: typing.Optional[str]

### MetricValue
- **Type**: typing.Optional[float]


# MetricsTypeDef

### RMSE
- **Type**: typing.Optional[float]

### WeightedQuantileLosses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.WeightedQuantileLossTypeDef]]

### ErrorMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.ErrorMetricTypeDef]]

### AverageWeightedQuantileLoss
- **Type**: typing.Optional[float]


# MonitorConfigTypeDef

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes


# MonitorDataSourceTypeDef

### DatasetImportJobArn
- **Type**: typing.Optional[str]

### ForecastArn
- **Type**: typing.Optional[str]

### PredictorArn
- **Type**: typing.Optional[str]


# MonitorInfoTypeDef

### MonitorArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# MonitorSummaryTypeDef

### MonitorArn
- **Type**: typing.Optional[str]

### MonitorName
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterRangesTypeDef

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.CategoricalParameterRangeTypeDef]]

### ContinuousParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.ContinuousParameterRangeTypeDef]]

### IntegerParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.IntegerParameterRangeTypeDef]]


# PredictorBacktestExportJobSummaryTypeDef

### PredictorBacktestExportJobArn
- **Type**: typing.Optional[str]

### PredictorBacktestExportJobName
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# PredictorBaselineTypeDef

### BaselineMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.BaselineMetricTypeDef]]


# PredictorEventTypeDef

### Detail
- **Type**: typing.Optional[str]

### Datetime
- **Type**: typing.Optional[datetime.datetime]


# PredictorExecutionDetailsTypeDef

### PredictorExecutions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorExecutionTypeDef]]


# PredictorExecutionTypeDef

### AlgorithmArn
- **Type**: typing.Optional[str]

### TestWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.TestWindowSummaryTypeDef]]


# PredictorMonitorEvaluationTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### MonitorArn
- **Type**: typing.Optional[str]

### EvaluationTime
- **Type**: typing.Optional[datetime.datetime]

### EvaluationState
- **Type**: typing.Optional[str]

### WindowStartDatetime
- **Type**: typing.Optional[datetime.datetime]

### WindowEndDatetime
- **Type**: typing.Optional[datetime.datetime]

### PredictorEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PredictorEventTypeDef]

### MonitorDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.MonitorDataSourceTypeDef]

### MetricResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.MetricResultTypeDef]]

### NumItemsEvaluated
- **Type**: typing.Optional[int]

### Message
- **Type**: typing.Optional[str]


# PredictorSummaryTypeDef

### PredictorArn
- **Type**: typing.Optional[str]

### PredictorName
- **Type**: typing.Optional[str]

### DatasetGroupArn
- **Type**: typing.Optional[str]

### IsAutoPredictor
- **Type**: typing.Optional[bool]

### ReferencePredictorSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ReferencePredictorSummaryTypeDef]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# ReferencePredictorSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['Active', 'Deleted']]


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


# ResumeResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# S3ConfigTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyArn
- **Type**: typing.Optional[str]


# SchemaAttributeTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeType
- **Type**: typing.Optional[typing.Literal['float', 'geolocation', 'integer', 'string', 'timestamp']]


# SchemaTypeDef

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.SchemaAttributeTypeDef]]


# StatisticsTypeDef

### Count
- **Type**: typing.Optional[int]

### CountDistinct
- **Type**: typing.Optional[int]

### CountNull
- **Type**: typing.Optional[int]

### CountNan
- **Type**: typing.Optional[int]

### Min
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[str]

### Avg
- **Type**: typing.Optional[float]

### Stddev
- **Type**: typing.Optional[float]

### CountLong
- **Type**: typing.Optional[int]

### CountDistinctLong
- **Type**: typing.Optional[int]

### CountNullLong
- **Type**: typing.Optional[int]

### CountNanLong
- **Type**: typing.Optional[int]


# StopResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# SupplementaryFeatureTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TestWindowSummaryTypeDef

### TestWindowStart
- **Type**: typing.Optional[datetime.datetime]

### TestWindowEnd
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# TimeAlignmentBoundaryTypeDef

### Month
- **Type**: typing.Optional[typing.Literal['APRIL', 'AUGUST', 'DECEMBER', 'FEBRUARY', 'JANUARY', 'JULY', 'JUNE', 'MARCH', 'MAY', 'NOVEMBER', 'OCTOBER', 'SEPTEMBER']]

### DayOfMonth
- **Type**: typing.Optional[int]

### DayOfWeek
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### Hour
- **Type**: typing.Optional[int]


# TimeSeriesConditionTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['EQUALS', 'GREATER_THAN', 'LESS_THAN', 'NOT_EQUALS']
- **Required**: Yes


# TimeSeriesIdentifiersTypeDef

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataSourceTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.SchemaTypeDef]

### Format
- **Type**: typing.Optional[str]


# TimeSeriesReplacementsDataSourceTypeDef

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.S3ConfigTypeDef'>
- **Required**: Yes

### Schema
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaTypeDef'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[str]

### TimestampFormat
- **Type**: typing.Optional[str]


# TimeSeriesSelectorTypeDef

### TimeSeriesIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesIdentifiersTypeDef]


# TimeSeriesTransformationTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ActionTypeDef]

### TimeSeriesConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesConditionTypeDef]]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetGroupRequestRequestTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WeightedQuantileLossTypeDef

### Quantile
- **Type**: typing.Optional[float]

### LossValue
- **Type**: typing.Optional[float]


# WhatIfAnalysisSummaryTypeDef

### WhatIfAnalysisArn
- **Type**: typing.Optional[str]

### WhatIfAnalysisName
- **Type**: typing.Optional[str]

### ForecastArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# WhatIfForecastExportSummaryTypeDef

### WhatIfForecastExportArn
- **Type**: typing.Optional[str]

### WhatIfForecastArns
- **Type**: typing.Optional[typing.List[str]]

### WhatIfForecastExportName
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataDestinationTypeDef]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# WhatIfForecastSummaryTypeDef

### WhatIfForecastArn
- **Type**: typing.Optional[str]

### WhatIfForecastName
- **Type**: typing.Optional[str]

### WhatIfAnalysisArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# WindowSummaryTypeDef

### TestWindowStart
- **Type**: typing.Optional[datetime.datetime]

### TestWindowEnd
- **Type**: typing.Optional[datetime.datetime]

### ItemCount
- **Type**: typing.Optional[int]

### EvaluationType
- **Type**: typing.Optional[typing.Literal['COMPUTED', 'SUMMARY']]

### Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.MetricsTypeDef]



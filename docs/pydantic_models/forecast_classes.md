# Forecast Classes

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


# AdditionalDatasetOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# AdditionalDatasetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# AttributeConfigOutputTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Transformations
- **Type**: typing.Dict[str, str]
- **Required**: Yes


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


# CategoricalParameterRangeOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


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


# CreateAutoPredictorRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataConfigUnionTypeDef]

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


# CreateDatasetGroupRequestTypeDef

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


# CreateDatasetImportJobRequestTypeDef

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


# CreateDatasetRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaUnionTypeDef'>
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


# CreateExplainabilityExportRequestTypeDef

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


# CreateExplainabilityRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.SchemaUnionTypeDef]

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


# CreateForecastExportJobRequestTypeDef

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


# CreateForecastRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorUnionTypeDef]


# CreateForecastResponseTypeDef

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMonitorRequestTypeDef

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


# CreatePredictorBacktestExportJobRequestTypeDef

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


# CreatePredictorRequestTypeDef

### PredictorName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### FeaturizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.FeaturizationConfigUnionTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.HyperParameterTuningJobConfigUnionTypeDef]

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


# CreateWhatIfAnalysisRequestTypeDef

### WhatIfAnalysisName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]


# CreateWhatIfAnalysisResponseTypeDef

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWhatIfForecastExportRequestTypeDef

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


# CreateWhatIfForecastRequestTypeDef

### WhatIfForecastName
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesTransformations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesTransformationUnionTypeDef]]

### TimeSeriesReplacementsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesReplacementsDataSourceUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TagTypeDef]]


# CreateWhatIfForecastResponseTypeDef

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataConfigOutputTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.AttributeConfigOutputTypeDef]]

### AdditionalDatasets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.AdditionalDatasetOutputTypeDef]]


# DataConfigTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.AttributeConfigTypeDef]]

### AdditionalDatasets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.AdditionalDatasetTypeDef]]


# DataConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# DeleteDatasetGroupRequestTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetImportJobRequestTypeDef

### DatasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetRequestTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExplainabilityExportRequestTypeDef

### ExplainabilityExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExplainabilityRequestTypeDef

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteForecastExportJobRequestTypeDef

### ForecastExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteForecastRequestTypeDef

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitorRequestTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePredictorBacktestExportJobRequestTypeDef

### PredictorBacktestExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePredictorRequestTypeDef

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceTreeRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfAnalysisRequestTypeDef

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfForecastExportRequestTypeDef

### WhatIfForecastExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfForecastRequestTypeDef

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoPredictorRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataConfigOutputTypeDef'>
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


# DescribeDatasetGroupRequestTypeDef

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


# DescribeDatasetImportJobRequestTypeDef

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


# DescribeDatasetRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaOutputTypeDef'>
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


# DescribeExplainabilityExportRequestTypeDef

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


# DescribeExplainabilityRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaOutputTypeDef'>
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


# DescribeForecastExportJobRequestTypeDef

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


# DescribeForecastRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMonitorRequestTypeDef

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


# DescribePredictorBacktestExportJobRequestTypeDef

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


# DescribePredictorRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.HyperParameterTuningJobConfigOutputTypeDef'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.InputDataConfigOutputTypeDef'>
- **Required**: Yes

### FeaturizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.FeaturizationConfigOutputTypeDef'>
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


# DescribeWhatIfAnalysisRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWhatIfForecastExportRequestTypeDef

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


# DescribeWhatIfForecastRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesTransformationOutputTypeDef]
- **Required**: Yes

### TimeSeriesReplacementsDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesReplacementsDataSourceOutputTypeDef'>
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


# FeaturizationConfigOutputTypeDef

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastDimensions
- **Type**: typing.Optional[typing.List[str]]

### Featurizations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.FeaturizationOutputTypeDef]]


# FeaturizationConfigTypeDef

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastDimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### Featurizations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FeaturizationTypeDef]]


# FeaturizationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FeaturizationMethodOutputTypeDef

### FeaturizationMethodName
- **Type**: typing.Literal['filling']
- **Required**: Yes

### FeaturizationMethodParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# FeaturizationMethodTypeDef

### FeaturizationMethodName
- **Type**: typing.Literal['filling']
- **Required**: Yes

### FeaturizationMethodParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FeaturizationOutputTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturizationPipeline
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.FeaturizationMethodOutputTypeDef]]


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


# GetAccuracyMetricsRequestTypeDef

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


# HyperParameterTuningJobConfigOutputTypeDef

### ParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ParameterRangesOutputTypeDef]


# HyperParameterTuningJobConfigTypeDef

### ParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ParameterRangesTypeDef]


# HyperParameterTuningJobConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputDataConfigOutputTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### SupplementaryFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.SupplementaryFeatureTypeDef]]


# InputDataConfigTypeDef

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### SupplementaryFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.SupplementaryFeatureTypeDef]]


# InputDataConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ListDatasetGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListDatasetGroupsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetGroupsResponseTypeDef

### DatasetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.DatasetGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetImportJobsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListDatasetImportJobsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListDatasetsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponseTypeDef

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.DatasetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExplainabilitiesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListExplainabilitiesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExplainabilityExportsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListExplainabilityExportsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListForecastExportJobsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListForecastExportJobsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListForecastsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListForecastsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitorEvaluationsRequestPaginateTypeDef

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListMonitorEvaluationsRequestTypeDef

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

### PredictorMonitorEvaluations
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorMonitorEvaluationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitorsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListMonitorsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPredictorBacktestExportJobsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListPredictorBacktestExportJobsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPredictorsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListPredictorsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

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


# ListWhatIfAnalysesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListWhatIfAnalysesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWhatIfForecastExportsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListWhatIfForecastExportsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWhatIfForecastsRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfigTypeDef]


# ListWhatIfForecastsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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


# ParameterRangesOutputTypeDef

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.CategoricalParameterRangeOutputTypeDef]]

### ContinuousParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.ContinuousParameterRangeTypeDef]]

### IntegerParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.IntegerParameterRangeTypeDef]]


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


# ResumeResourceRequestTypeDef

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


# SchemaOutputTypeDef

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.SchemaAttributeTypeDef]]


# SchemaTypeDef

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.SchemaAttributeTypeDef]]


# SchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# StopResourceRequestTypeDef

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


# TagResourceRequestTypeDef

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


# TimeSeriesIdentifiersOutputTypeDef

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataSourceTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.SchemaOutputTypeDef]

### Format
- **Type**: typing.Optional[str]


# TimeSeriesIdentifiersTypeDef

### DataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataSourceTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.SchemaTypeDef]

### Format
- **Type**: typing.Optional[str]


# TimeSeriesReplacementsDataSourceOutputTypeDef

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.S3ConfigTypeDef'>
- **Required**: Yes

### Schema
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaOutputTypeDef'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[str]

### TimestampFormat
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


# TimeSeriesReplacementsDataSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeSeriesSelectorOutputTypeDef

### TimeSeriesIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesIdentifiersOutputTypeDef]


# TimeSeriesSelectorTypeDef

### TimeSeriesIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesIdentifiersTypeDef]


# TimeSeriesSelectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeSeriesTransformationOutputTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ActionTypeDef]

### TimeSeriesConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesConditionTypeDef]]


# TimeSeriesTransformationTypeDef

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ActionTypeDef]

### TimeSeriesConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesConditionTypeDef]]


# TimeSeriesTransformationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetGroupRequestTypeDef

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



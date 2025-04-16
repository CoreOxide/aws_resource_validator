# Forecast Classes

# Action

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['ADD', 'DIVIDE', 'MULTIPLY', 'SUBTRACT']
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# AdditionalDataset

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# AdditionalDatasetOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# AttributeConfig

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Transformations
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# AttributeConfigOutput

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Transformations
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Baseline

### PredictorBaseline
- **Type**: <class 'NoneType'>


# BaselineMetric

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]


# CategoricalParameterRange

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CategoricalParameterRangeOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ContinuousParameterRange

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


# CreateAutoPredictorRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataConfigUnion]

### EncryptionConfig
- **Type**: <class 'NoneType'>

### ReferencePredictorArn
- **Type**: typing.Optional[str]

### OptimizationMetric
- **Type**: typing.Optional[typing.Literal['AverageWeightedQuantileLoss', 'MAPE', 'MASE', 'RMSE', 'WAPE']]

### ExplainPredictor
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]

### MonitorConfig
- **Type**: <class 'NoneType'>

### TimeAlignmentBoundary
- **Type**: <class 'NoneType'>


# CreateAutoPredictorResponse

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetGroupRequest

### DatasetGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Literal['CUSTOM', 'EC2_CAPACITY', 'INVENTORY_PLANNING', 'METRICS', 'RETAIL', 'WEB_TRAFFIC', 'WORK_FORCE']
- **Required**: Yes

### DatasetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]


# CreateDatasetGroupResponse

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetImportJobRequest

### DatasetImportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataSource'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]

### Format
- **Type**: typing.Optional[str]

### ImportMode
- **Type**: typing.Optional[typing.Literal['FULL', 'INCREMENTAL']]


# CreateDatasetImportJobResponse

### DatasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaUnion'>
- **Required**: Yes

### DataFrequency
- **Type**: typing.Optional[str]

### EncryptionConfig
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]


# CreateDatasetResponse

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExplainabilityExportRequest

### ExplainabilityExportName
- **Type**: <class 'str'>
- **Required**: Yes

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestination'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]

### Format
- **Type**: typing.Optional[str]


# CreateExplainabilityExportResponse

### ExplainabilityExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExplainabilityRequest

### ExplainabilityName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExplainabilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityConfig'>
- **Required**: Yes

### DataSource
- **Type**: <class 'NoneType'>

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.SchemaUnion]

### EnableVisualization
- **Type**: typing.Optional[bool]

### StartDateTime
- **Type**: typing.Optional[str]

### EndDateTime
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]


# CreateExplainabilityResponse

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateForecastExportJobRequest

### ForecastExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestination'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]

### Format
- **Type**: typing.Optional[str]


# CreateForecastExportJobResponse

### ForecastExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateForecastRequest

### ForecastName
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]

### TimeSeriesSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorUnion]


# CreateForecastResponse

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMonitorRequest

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]


# CreateMonitorResponse

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePredictorBacktestExportJobRequest

### PredictorBacktestExportJobName
- **Type**: <class 'str'>
- **Required**: Yes

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestination'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]

### Format
- **Type**: typing.Optional[str]


# CreatePredictorBacktestExportJobResponse

### PredictorBacktestExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePredictorRequest

### PredictorName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastHorizon
- **Type**: <class 'int'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.InputDataConfigUnion'>
- **Required**: Yes

### FeaturizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.FeaturizationConfigUnion'>
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
- **Type**: <class 'NoneType'>

### HPOConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.HyperParameterTuningJobConfigUnion]

### EncryptionConfig
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]

### OptimizationMetric
- **Type**: typing.Optional[typing.Literal['AverageWeightedQuantileLoss', 'MAPE', 'MASE', 'RMSE', 'WAPE']]


# CreatePredictorResponse

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWhatIfAnalysisRequest

### WhatIfAnalysisName
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorUnion]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]


# CreateWhatIfAnalysisResponse

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWhatIfForecastExportRequest

### WhatIfForecastExportName
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfForecastArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestination'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]

### Format
- **Type**: typing.Optional[str]


# CreateWhatIfForecastExportResponse

### WhatIfForecastExportArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWhatIfForecastRequest

### WhatIfForecastName
- **Type**: <class 'str'>
- **Required**: Yes

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimeSeriesTransformations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesTransformationUnion]]

### TimeSeriesReplacementsDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesReplacementsDataSourceUnion]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]]


# CreateWhatIfForecastResponse

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DataConfig

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.AttributeConfig]]

### AdditionalDatasets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.AdditionalDataset]]


# DataConfigOutput

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.AttributeConfigOutput]]

### AdditionalDatasets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.AdditionalDatasetOutput]]


# DataConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataDestination

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.S3Config'>
- **Required**: Yes


# DataSource

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.S3Config'>
- **Required**: Yes


# DatasetGroupSummary

### DatasetGroupArn
- **Type**: typing.Optional[str]

### DatasetGroupName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# DatasetImportJobSummary

### DatasetImportJobArn
- **Type**: typing.Optional[str]

### DatasetImportJobName
- **Type**: typing.Optional[str]

### DataSource
- **Type**: <class 'NoneType'>

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


# DatasetSummary

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


# DeleteDatasetGroupRequest

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetImportJobRequest

### DatasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetRequest

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExplainabilityExportRequest

### ExplainabilityExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExplainabilityRequest

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteForecastExportJobRequest

### ForecastExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteForecastRequest

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitorRequest

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePredictorBacktestExportJobRequest

### PredictorBacktestExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePredictorRequest

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceTreeRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfAnalysisRequest

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfForecastExportRequest

### WhatIfForecastExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWhatIfForecastRequest

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoPredictorRequest

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAutoPredictorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataConfigOutput'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfig'>
- **Required**: Yes

### ReferencePredictorSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ReferencePredictorSummary'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityInfo'>
- **Required**: Yes

### MonitorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.MonitorInfo'>
- **Required**: Yes

### TimeAlignmentBoundary
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeAlignmentBoundary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetGroupRequest

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetImportJobRequest

### DatasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetImportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataSource'>
- **Required**: Yes

### EstimatedTimeRemainingInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### FieldStatistics
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.forecast_classes.Statistics]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaOutput'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExplainabilityExportRequest

### ExplainabilityExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExplainabilityExportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestination'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExplainabilityRequest

### ExplainabilityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExplainabilityResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityConfig'>
- **Required**: Yes

### EnableVisualization
- **Type**: <class 'bool'>
- **Required**: Yes

### DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataSource'>
- **Required**: Yes

### Schema
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeForecastExportJobRequest

### ForecastExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeForecastExportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestination'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeForecastRequest

### ForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeForecastResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMonitorRequest

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMonitorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.Baseline'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePredictorBacktestExportJobRequest

### PredictorBacktestExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePredictorBacktestExportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestination'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePredictorRequest

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePredictorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.EvaluationParameters'>
- **Required**: Yes

### HPOConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.HyperParameterTuningJobConfigOutput'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.InputDataConfigOutput'>
- **Required**: Yes

### FeaturizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.FeaturizationConfigOutput'>
- **Required**: Yes

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.EncryptionConfig'>
- **Required**: Yes

### PredictorExecutionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.PredictorExecutionDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWhatIfAnalysisRequest

### WhatIfAnalysisArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWhatIfAnalysisResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesSelectorOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWhatIfForecastExportRequest

### WhatIfForecastExportArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWhatIfForecastExportResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.DataDestination'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWhatIfForecastRequest

### WhatIfForecastArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWhatIfForecastResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesTransformationOutput]
- **Required**: Yes

### TimeSeriesReplacementsDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesReplacementsDataSourceOutput'>
- **Required**: Yes

### ForecastTypes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionConfig

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorMetric

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


# EvaluationParameters

### NumberOfBacktestWindows
- **Type**: typing.Optional[int]

### BackTestWindowOffset
- **Type**: typing.Optional[int]


# EvaluationResult

### AlgorithmArn
- **Type**: typing.Optional[str]

### TestWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.WindowSummary]]


# ExplainabilityConfig

### TimeSeriesGranularity
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes

### TimePointGranularity
- **Type**: typing.Literal['ALL', 'SPECIFIC']
- **Required**: Yes


# ExplainabilityExportSummary

### ExplainabilityExportArn
- **Type**: typing.Optional[str]

### ExplainabilityExportName
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataDestination]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# ExplainabilityInfo

### ExplainabilityArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ExplainabilitySummary

### ExplainabilityArn
- **Type**: typing.Optional[str]

### ExplainabilityName
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ExplainabilityConfig
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# Featurization

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturizationPipeline
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.FeaturizationMethod]]


# FeaturizationConfig

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastDimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### Featurizations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Featurization]]


# FeaturizationConfigOutput

### ForecastFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### ForecastDimensions
- **Type**: typing.Optional[typing.List[str]]

### Featurizations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.FeaturizationOutput]]


# FeaturizationConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FeaturizationMethod

### FeaturizationMethodName
- **Type**: typing.Literal['filling']
- **Required**: Yes

### FeaturizationMethodParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FeaturizationMethodOutput

### FeaturizationMethodName
- **Type**: typing.Literal['filling']
- **Required**: Yes

### FeaturizationMethodParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# FeaturizationOutput

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturizationPipeline
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.FeaturizationMethodOutput]]


# Filter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['IS', 'IS_NOT']
- **Required**: Yes


# ForecastExportJobSummary

### ForecastExportJobArn
- **Type**: typing.Optional[str]

### ForecastExportJobName
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataDestination]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# ForecastSummary

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


# GetAccuracyMetricsRequest

### PredictorArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccuracyMetricsResponse

### PredictorEvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.EvaluationResult]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# HyperParameterTuningJobConfig

### ParameterRanges
- **Type**: <class 'NoneType'>


# HyperParameterTuningJobConfigOutput

### ParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.ParameterRangesOutput]


# HyperParameterTuningJobConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InputDataConfig

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### SupplementaryFeatures
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.SupplementaryFeature]]


# InputDataConfigOutput

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### SupplementaryFeatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.SupplementaryFeature]]


# InputDataConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntegerParameterRange

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


# ListDatasetGroupsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListDatasetGroupsResponse

### DatasetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.DatasetGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetImportJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListDatasetImportJobsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListDatasetImportJobsResponse

### DatasetImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.DatasetImportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListDatasetsResponse

### Datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.DatasetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExplainabilitiesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListExplainabilitiesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListExplainabilitiesResponse

### Explainabilities
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.ExplainabilitySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExplainabilityExportsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListExplainabilityExportsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListExplainabilityExportsResponse

### ExplainabilityExports
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.ExplainabilityExportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListForecastExportJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListForecastExportJobsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListForecastExportJobsResponse

### ForecastExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.ForecastExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListForecastsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListForecastsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListForecastsResponse

### Forecasts
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.ForecastSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitorEvaluationsRequest

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListMonitorEvaluationsRequestPaginate

### MonitorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListMonitorEvaluationsResponse

### PredictorMonitorEvaluations
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorMonitorEvaluation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMonitorsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListMonitorsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListMonitorsResponse

### Monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.MonitorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPredictorBacktestExportJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListPredictorBacktestExportJobsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListPredictorBacktestExportJobsResponse

### PredictorBacktestExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorBacktestExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPredictorsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListPredictorsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListPredictorsResponse

### Predictors
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes


# ListWhatIfAnalysesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListWhatIfAnalysesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListWhatIfAnalysesResponse

### WhatIfAnalyses
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.WhatIfAnalysisSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWhatIfForecastExportsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListWhatIfForecastExportsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListWhatIfForecastExportsResponse

### WhatIfForecastExports
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.WhatIfForecastExportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListWhatIfForecastsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]


# ListWhatIfForecastsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.PaginatorConfig]


# ListWhatIfForecastsResponse

### WhatIfForecasts
- **Type**: typing.List[aws_resource_validator.pydantic_models.forecast_classes.WhatIfForecastSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MetricResult

### MetricName
- **Type**: typing.Optional[str]

### MetricValue
- **Type**: typing.Optional[float]


# Metrics

### RMSE
- **Type**: typing.Optional[float]

### WeightedQuantileLosses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.WeightedQuantileLoss]]

### ErrorMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.ErrorMetric]]

### AverageWeightedQuantileLoss
- **Type**: typing.Optional[float]


# MonitorConfig

### MonitorName
- **Type**: <class 'str'>
- **Required**: Yes


# MonitorDataSource

### DatasetImportJobArn
- **Type**: typing.Optional[str]

### ForecastArn
- **Type**: typing.Optional[str]

### PredictorArn
- **Type**: typing.Optional[str]


# MonitorInfo

### MonitorArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# MonitorSummary

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterRanges

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.CategoricalParameterRange]]

### ContinuousParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.ContinuousParameterRange]]

### IntegerParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.IntegerParameterRange]]


# ParameterRangesOutput

### CategoricalParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.CategoricalParameterRangeOutput]]

### ContinuousParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.ContinuousParameterRange]]

### IntegerParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.IntegerParameterRange]]


# PredictorBacktestExportJobSummary

### PredictorBacktestExportJobArn
- **Type**: typing.Optional[str]

### PredictorBacktestExportJobName
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataDestination]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# PredictorBaseline

### BaselineMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.BaselineMetric]]


# PredictorEvent

### Detail
- **Type**: typing.Optional[str]

### Datetime
- **Type**: typing.Optional[datetime.datetime]


# PredictorExecution

### AlgorithmArn
- **Type**: typing.Optional[str]

### TestWindows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.TestWindowSummary]]


# PredictorExecutionDetails

### PredictorExecutions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.PredictorExecution]]


# PredictorMonitorEvaluation

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
- **Type**: <class 'NoneType'>

### MonitorDataSource
- **Type**: <class 'NoneType'>

### MetricResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.MetricResult]]

### NumItemsEvaluated
- **Type**: typing.Optional[int]

### Message
- **Type**: typing.Optional[str]


# PredictorSummary

### PredictorArn
- **Type**: typing.Optional[str]

### PredictorName
- **Type**: typing.Optional[str]

### DatasetGroupArn
- **Type**: typing.Optional[str]

### IsAutoPredictor
- **Type**: typing.Optional[bool]

### ReferencePredictorSummary
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# ReferencePredictorSummary

### Arn
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['Active', 'Deleted']]


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


# ResumeResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# S3Config

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KMSKeyArn
- **Type**: typing.Optional[str]


# Schema

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.SchemaAttribute]]


# SchemaAttribute

### AttributeName
- **Type**: typing.Optional[str]

### AttributeType
- **Type**: typing.Optional[typing.Literal['float', 'geolocation', 'integer', 'string', 'timestamp']]


# SchemaOutput

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.SchemaAttribute]]


# SchemaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Statistics

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


# StopResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# SupplementaryFeature

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.Tag]
- **Required**: Yes


# TestWindowSummary

### TestWindowStart
- **Type**: typing.Optional[datetime.datetime]

### TestWindowEnd
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# TimeAlignmentBoundary

### Month
- **Type**: typing.Optional[typing.Literal['APRIL', 'AUGUST', 'DECEMBER', 'FEBRUARY', 'JANUARY', 'JULY', 'JUNE', 'MARCH', 'MAY', 'NOVEMBER', 'OCTOBER', 'SEPTEMBER']]

### DayOfMonth
- **Type**: typing.Optional[int]

### DayOfWeek
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]

### Hour
- **Type**: typing.Optional[int]


# TimeSeriesCondition

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeValue
- **Type**: <class 'str'>
- **Required**: Yes

### Condition
- **Type**: typing.Literal['EQUALS', 'GREATER_THAN', 'LESS_THAN', 'NOT_EQUALS']
- **Required**: Yes


# TimeSeriesIdentifiers

### DataSource
- **Type**: <class 'NoneType'>

### Schema
- **Type**: <class 'NoneType'>

### Format
- **Type**: typing.Optional[str]


# TimeSeriesIdentifiersOutput

### DataSource
- **Type**: <class 'NoneType'>

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.SchemaOutput]

### Format
- **Type**: typing.Optional[str]


# TimeSeriesReplacementsDataSource

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.S3Config'>
- **Required**: Yes

### Schema
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.Schema'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[str]

### TimestampFormat
- **Type**: typing.Optional[str]


# TimeSeriesReplacementsDataSourceOutput

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.S3Config'>
- **Required**: Yes

### Schema
- **Type**: <class 'aws_resource_validator.pydantic_models.forecast_classes.SchemaOutput'>
- **Required**: Yes

### Format
- **Type**: typing.Optional[str]

### TimestampFormat
- **Type**: typing.Optional[str]


# TimeSeriesReplacementsDataSourceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeSeriesSelector

### TimeSeriesIdentifiers
- **Type**: <class 'NoneType'>


# TimeSeriesSelectorOutput

### TimeSeriesIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesIdentifiersOutput]


# TimeSeriesSelectorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeSeriesTransformation

### Action
- **Type**: <class 'NoneType'>

### TimeSeriesConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesCondition]]


# TimeSeriesTransformationOutput

### Action
- **Type**: <class 'NoneType'>

### TimeSeriesConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.forecast_classes.TimeSeriesCondition]]


# TimeSeriesTransformationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetGroupRequest

### DatasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WeightedQuantileLoss

### Quantile
- **Type**: typing.Optional[float]

### LossValue
- **Type**: typing.Optional[float]


# WhatIfAnalysisSummary

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


# WhatIfForecastExportSummary

### WhatIfForecastExportArn
- **Type**: typing.Optional[str]

### WhatIfForecastArns
- **Type**: typing.Optional[typing.List[str]]

### WhatIfForecastExportName
- **Type**: typing.Optional[str]

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.forecast_classes.DataDestination]

### Status
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModificationTime
- **Type**: typing.Optional[datetime.datetime]


# WhatIfForecastSummary

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


# WindowSummary

### TestWindowStart
- **Type**: typing.Optional[datetime.datetime]

### TestWindowEnd
- **Type**: typing.Optional[datetime.datetime]

### ItemCount
- **Type**: typing.Optional[int]

### EvaluationType
- **Type**: typing.Optional[typing.Literal['COMPUTED', 'SUMMARY']]

### Metrics
- **Type**: <class 'NoneType'>



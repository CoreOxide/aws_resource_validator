# Lookoutequipment Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CategoricalValuesTypeDef

### Status
- **Type**: typing.Literal['NO_ISSUE_DETECTED', 'POTENTIAL_ISSUE_DETECTED']
- **Required**: Yes

### NumberOfCategory
- **Type**: typing.Optional[int]


# CountPercentTypeDef

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### Percentage
- **Type**: <class 'float'>
- **Required**: Yes


# CreateDatasetRequestTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.DatasetSchemaTypeDef]

### ServerSideKmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutequipment_classes.TagTypeDef]]


# CreateDatasetResponseTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATED', 'IMPORT_IN_PROGRESS', 'INGESTION_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInferenceSchedulerRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### DataUploadFrequency
- **Type**: typing.Literal['PT10M', 'PT15M', 'PT1H', 'PT30M', 'PT5M']
- **Required**: Yes

### DataInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceInputConfigurationTypeDef'>
- **Required**: Yes

### DataOutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceOutputConfigurationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### DataDelayOffsetInMinutes
- **Type**: typing.Optional[int]

### ServerSideKmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutequipment_classes.TagTypeDef]]


# CreateInferenceSchedulerResponseTypeDef

### InferenceSchedulerArn
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ModelQuality
- **Type**: typing.Literal['CANNOT_DETERMINE_QUALITY', 'POOR_QUALITY_DETECTED', 'QUALITY_THRESHOLD_MET']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLabelGroupRequestTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### FaultCodes
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutequipment_classes.TagTypeDef]]


# CreateLabelGroupResponseTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLabelRequestTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef'>
- **Required**: Yes

### Rating
- **Type**: typing.Literal['ANOMALY', 'NEUTRAL', 'NO_ANOMALY']
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### FaultCode
- **Type**: typing.Optional[str]

### Notes
- **Type**: typing.Optional[str]

### Equipment
- **Type**: typing.Optional[str]


# CreateLabelResponseTypeDef

### LabelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateModelRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.DatasetSchemaTypeDef]

### LabelsInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.LabelsInputConfigurationTypeDef]

### TrainingDataStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### TrainingDataEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### EvaluationDataStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### EvaluationDataEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### DataPreProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.DataPreProcessingConfigurationTypeDef]

### ServerSideKmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutequipment_classes.TagTypeDef]]

### OffCondition
- **Type**: typing.Optional[str]

### ModelDiagnosticsOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.ModelDiagnosticsOutputConfigurationTypeDef]


# CreateModelResponseTypeDef

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRetrainingSchedulerRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### RetrainingFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### LookbackWindow
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### RetrainingStartDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### PromoteMode
- **Type**: typing.Optional[typing.Literal['MANAGED', 'MANUAL']]


# CreateRetrainingSchedulerResponseTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataIngestionJobSummaryTypeDef

### JobId
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### DatasetArn
- **Type**: typing.Optional[str]

### IngestionInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.IngestionInputConfigurationTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]


# DataPreProcessingConfigurationTypeDef

### TargetSamplingRate
- **Type**: typing.Optional[typing.Literal['PT10M', 'PT10S', 'PT15M', 'PT15S', 'PT1H', 'PT1M', 'PT1S', 'PT30M', 'PT30S', 'PT5M', 'PT5S']]


# DataQualitySummaryTypeDef

### InsufficientSensorData
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.InsufficientSensorDataTypeDef'>
- **Required**: Yes

### MissingSensorData
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.MissingSensorDataTypeDef'>
- **Required**: Yes

### InvalidSensorData
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.InvalidSensorDataTypeDef'>
- **Required**: Yes

### UnsupportedTimestamps
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.UnsupportedTimestampsTypeDef'>
- **Required**: Yes

### DuplicateTimestamps
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.DuplicateTimestampsTypeDef'>
- **Required**: Yes


# DatasetSchemaTypeDef

### InlineDataSchema
- **Type**: typing.Optional[str]


# DatasetSummaryTypeDef

### DatasetName
- **Type**: typing.Optional[str]

### DatasetArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATED', 'IMPORT_IN_PROGRESS', 'INGESTION_IN_PROGRESS']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteDatasetRequestTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInferenceSchedulerRequestTypeDef

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLabelGroupRequestTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLabelRequestTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetrainingSchedulerRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataIngestionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataIngestionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.IngestionInputConfigurationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### FailedReason
- **Type**: <class 'str'>
- **Required**: Yes

### DataQualitySummary
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.DataQualitySummaryTypeDef'>
- **Required**: Yes

### IngestedFilesSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.IngestedFilesSummaryTypeDef'>
- **Required**: Yes

### StatusDetail
- **Type**: <class 'str'>
- **Required**: Yes

### IngestedDataSize
- **Type**: <class 'int'>
- **Required**: Yes

### DataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetRequestTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATED', 'IMPORT_IN_PROGRESS', 'INGESTION_IN_PROGRESS']
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.IngestionInputConfigurationTypeDef'>
- **Required**: Yes

### DataQualitySummary
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.DataQualitySummaryTypeDef'>
- **Required**: Yes

### IngestedFilesSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.IngestedFilesSummaryTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInferenceSchedulerRequestTypeDef

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInferenceSchedulerResponseTypeDef

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceSchedulerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### DataDelayOffsetInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### DataUploadFrequency
- **Type**: typing.Literal['PT10M', 'PT15M', 'PT1H', 'PT30M', 'PT5M']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceInputConfigurationTypeDef'>
- **Required**: Yes

### DataOutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceOutputConfigurationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### LatestInferenceResult
- **Type**: typing.Literal['ANOMALOUS', 'NORMAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLabelGroupRequestTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLabelGroupResponseTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### FaultCodes
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLabelRequestTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLabelResponseTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### LabelId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Rating
- **Type**: typing.Literal['ANOMALY', 'NEUTRAL', 'NO_ANOMALY']
- **Required**: Yes

### FaultCode
- **Type**: <class 'str'>
- **Required**: Yes

### Notes
- **Type**: <class 'str'>
- **Required**: Yes

### Equipment
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelResponseTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### LabelsInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.LabelsInputConfigurationTypeDef'>
- **Required**: Yes

### TrainingDataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingDataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EvaluationDataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EvaluationDataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataPreProcessingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.DataPreProcessingConfigurationTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### TrainingExecutionStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingExecutionEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailedReason
- **Type**: <class 'str'>
- **Required**: Yes

### ModelMetrics
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServerSideKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### OffCondition
- **Type**: <class 'str'>
- **Required**: Yes

### SourceModelVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImportJobStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportJobEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ActiveModelVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ActiveModelVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersionActivatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PreviousActiveModelVersion
- **Type**: <class 'int'>
- **Required**: Yes

### PreviousActiveModelVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PreviousModelVersionActivatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PriorModelMetrics
- **Type**: <class 'str'>
- **Required**: Yes

### LatestScheduledRetrainingFailedReason
- **Type**: <class 'str'>
- **Required**: Yes

### LatestScheduledRetrainingStatus
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### LatestScheduledRetrainingModelVersion
- **Type**: <class 'int'>
- **Required**: Yes

### LatestScheduledRetrainingStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestScheduledRetrainingAvailableDataInDays
- **Type**: <class 'int'>
- **Required**: Yes

### NextScheduledRetrainingStartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccumulatedInferenceDataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccumulatedInferenceDataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RetrainingSchedulerStatus
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ModelDiagnosticsOutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ModelDiagnosticsOutputConfigurationTypeDef'>
- **Required**: Yes

### ModelQuality
- **Type**: typing.Literal['CANNOT_DETERMINE_QUALITY', 'POOR_QUALITY_DETECTED', 'QUALITY_THRESHOLD_MET']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelVersionRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeModelVersionResponseTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ModelVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### SourceType
- **Type**: typing.Literal['IMPORT', 'RETRAINING', 'TRAINING']
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Schema
- **Type**: <class 'str'>
- **Required**: Yes

### LabelsInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.LabelsInputConfigurationTypeDef'>
- **Required**: Yes

### TrainingDataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingDataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EvaluationDataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EvaluationDataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataPreProcessingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.DataPreProcessingConfigurationTypeDef'>
- **Required**: Yes

### TrainingExecutionStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TrainingExecutionEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FailedReason
- **Type**: <class 'str'>
- **Required**: Yes

### ModelMetrics
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServerSideKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### OffCondition
- **Type**: <class 'str'>
- **Required**: Yes

### SourceModelVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ImportJobStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportJobEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportedDataSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### PriorModelMetrics
- **Type**: <class 'str'>
- **Required**: Yes

### RetrainingAvailableDataInDays
- **Type**: <class 'int'>
- **Required**: Yes

### AutoPromotionResult
- **Type**: typing.Literal['MODEL_NOT_PROMOTED', 'MODEL_PROMOTED', 'RETRAINING_CANCELLED', 'RETRAINING_CUSTOMER_ERROR', 'RETRAINING_INTERNAL_ERROR']
- **Required**: Yes

### AutoPromotionResultReason
- **Type**: <class 'str'>
- **Required**: Yes

### ModelDiagnosticsOutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ModelDiagnosticsOutputConfigurationTypeDef'>
- **Required**: Yes

### ModelDiagnosticsResultsObject
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.S3ObjectTypeDef'>
- **Required**: Yes

### ModelQuality
- **Type**: typing.Literal['CANNOT_DETERMINE_QUALITY', 'POOR_QUALITY_DETECTED', 'QUALITY_THRESHOLD_MET']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourcePolicyResponseTypeDef

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRetrainingSchedulerRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRetrainingSchedulerResponseTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### RetrainingStartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RetrainingFrequency
- **Type**: <class 'str'>
- **Required**: Yes

### LookbackWindow
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### PromoteMode
- **Type**: typing.Literal['MANAGED', 'MANUAL']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DuplicateTimestampsTypeDef

### TotalNumberOfDuplicateTimestamps
- **Type**: <class 'int'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportDatasetRequestTypeDef

### SourceDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: typing.Optional[str]

### ServerSideKmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutequipment_classes.TagTypeDef]]


# ImportDatasetResponseTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATED', 'IMPORT_IN_PROGRESS', 'INGESTION_IN_PROGRESS']
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportModelVersionRequestTypeDef

### SourceModelVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: typing.Optional[str]

### LabelsInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.LabelsInputConfigurationTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### ServerSideKmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lookoutequipment_classes.TagTypeDef]]

### InferenceDataImportStrategy
- **Type**: typing.Optional[typing.Literal['ADD_WHEN_EMPTY', 'NO_IMPORT', 'OVERWRITE']]


# ImportModelVersionResponseTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InferenceEventSummaryTypeDef

### InferenceSchedulerArn
- **Type**: typing.Optional[str]

### InferenceSchedulerName
- **Type**: typing.Optional[str]

### EventStartTime
- **Type**: typing.Optional[datetime.datetime]

### EventEndTime
- **Type**: typing.Optional[datetime.datetime]

### Diagnostics
- **Type**: typing.Optional[str]

### EventDurationInSeconds
- **Type**: typing.Optional[int]


# InferenceExecutionSummaryTypeDef

### ModelName
- **Type**: typing.Optional[str]

### ModelArn
- **Type**: typing.Optional[str]

### InferenceSchedulerName
- **Type**: typing.Optional[str]

### InferenceSchedulerArn
- **Type**: typing.Optional[str]

### ScheduledStartTime
- **Type**: typing.Optional[datetime.datetime]

### DataStartTime
- **Type**: typing.Optional[datetime.datetime]

### DataEndTime
- **Type**: typing.Optional[datetime.datetime]

### DataInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceInputConfigurationTypeDef]

### DataOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceOutputConfigurationTypeDef]

### CustomerResultObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.S3ObjectTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### FailedReason
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[int]

### ModelVersionArn
- **Type**: typing.Optional[str]


# InferenceInputConfigurationTypeDef

### S3InputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceS3InputConfigurationTypeDef]

### InputTimeZoneOffset
- **Type**: typing.Optional[str]

### InferenceInputNameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceInputNameConfigurationTypeDef]


# InferenceInputNameConfigurationTypeDef

### TimestampFormat
- **Type**: typing.Optional[str]

### ComponentTimestampDelimiter
- **Type**: typing.Optional[str]


# InferenceOutputConfigurationTypeDef

### S3OutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceS3OutputConfigurationTypeDef'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# InferenceS3InputConfigurationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# InferenceS3OutputConfigurationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# InferenceSchedulerSummaryTypeDef

### ModelName
- **Type**: typing.Optional[str]

### ModelArn
- **Type**: typing.Optional[str]

### InferenceSchedulerName
- **Type**: typing.Optional[str]

### InferenceSchedulerArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]

### DataDelayOffsetInMinutes
- **Type**: typing.Optional[int]

### DataUploadFrequency
- **Type**: typing.Optional[typing.Literal['PT10M', 'PT15M', 'PT1H', 'PT30M', 'PT5M']]

### LatestInferenceResult
- **Type**: typing.Optional[typing.Literal['ANOMALOUS', 'NORMAL']]


# IngestedFilesSummaryTypeDef

### TotalNumberOfFiles
- **Type**: <class 'int'>
- **Required**: Yes

### IngestedNumberOfFiles
- **Type**: <class 'int'>
- **Required**: Yes

### DiscardedFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.S3ObjectTypeDef]]


# IngestionInputConfigurationTypeDef

### S3InputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.IngestionS3InputConfigurationTypeDef'>
- **Required**: Yes


# IngestionS3InputConfigurationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### KeyPattern
- **Type**: typing.Optional[str]


# InsufficientSensorDataTypeDef

### MissingCompleteSensorData
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.MissingCompleteSensorDataTypeDef'>
- **Required**: Yes

### SensorsWithShortDateRange
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.SensorsWithShortDateRangeTypeDef'>
- **Required**: Yes


# InvalidSensorDataTypeDef

### AffectedSensorCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalNumberOfInvalidValues
- **Type**: <class 'int'>
- **Required**: Yes


# LabelGroupSummaryTypeDef

### LabelGroupName
- **Type**: typing.Optional[str]

### LabelGroupArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# LabelSummaryTypeDef

### LabelGroupName
- **Type**: typing.Optional[str]

### LabelId
- **Type**: typing.Optional[str]

### LabelGroupArn
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Rating
- **Type**: typing.Optional[typing.Literal['ANOMALY', 'NEUTRAL', 'NO_ANOMALY']]

### FaultCode
- **Type**: typing.Optional[str]

### Equipment
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# LabelsInputConfigurationTypeDef

### S3InputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.LabelsS3InputConfigurationTypeDef]

### LabelGroupName
- **Type**: typing.Optional[str]


# LabelsS3InputConfigurationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# LargeTimestampGapsTypeDef

### Status
- **Type**: typing.Literal['NO_ISSUE_DETECTED', 'POTENTIAL_ISSUE_DETECTED']
- **Required**: Yes

### NumberOfLargeTimestampGaps
- **Type**: typing.Optional[int]

### MaxTimestampGapInDays
- **Type**: typing.Optional[int]


# ListDataIngestionJobsRequestTypeDef

### DatasetName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]


# ListDataIngestionJobsResponseTypeDef

### DataIngestionJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.DataIngestionJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### DatasetNameBeginsWith
- **Type**: typing.Optional[str]


# ListDatasetsResponseTypeDef

### DatasetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.DatasetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceEventsRequestTypeDef

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### IntervalStartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef'>
- **Required**: Yes

### IntervalEndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInferenceEventsResponseTypeDef

### InferenceEventSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceEventSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceExecutionsRequestTypeDef

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### DataStartTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### DataEndTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]


# ListInferenceExecutionsResponseTypeDef

### InferenceExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceExecutionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceSchedulersRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### InferenceSchedulerNameBeginsWith
- **Type**: typing.Optional[str]

### ModelName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]


# ListInferenceSchedulersResponseTypeDef

### InferenceSchedulerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceSchedulerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLabelGroupsRequestTypeDef

### LabelGroupNameBeginsWith
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLabelGroupsResponseTypeDef

### LabelGroupSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.LabelGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLabelsRequestTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### IntervalStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### IntervalEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### FaultCode
- **Type**: typing.Optional[str]

### Equipment
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLabelsResponseTypeDef

### LabelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.LabelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelVersionsRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]

### SourceType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'RETRAINING', 'TRAINING']]

### CreatedAtEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### CreatedAtStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### MaxModelVersion
- **Type**: typing.Optional[int]

### MinModelVersion
- **Type**: typing.Optional[int]


# ListModelVersionsResponseTypeDef

### ModelVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.ModelVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]

### ModelNameBeginsWith
- **Type**: typing.Optional[str]

### DatasetNameBeginsWith
- **Type**: typing.Optional[str]


# ListModelsResponseTypeDef

### ModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.ModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRetrainingSchedulersRequestTypeDef

### ModelNameBeginsWith
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRetrainingSchedulersResponseTypeDef

### RetrainingSchedulerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.RetrainingSchedulerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSensorStatisticsRequestTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionJobId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSensorStatisticsResponseTypeDef

### SensorStatisticsSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.SensorStatisticsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MissingCompleteSensorDataTypeDef

### AffectedSensorCount
- **Type**: <class 'int'>
- **Required**: Yes


# MissingSensorDataTypeDef

### AffectedSensorCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalNumberOfMissingValues
- **Type**: <class 'int'>
- **Required**: Yes


# ModelDiagnosticsOutputConfigurationTypeDef

### S3OutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ModelDiagnosticsS3OutputConfigurationTypeDef'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ModelDiagnosticsS3OutputConfigurationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# ModelSummaryTypeDef

### ModelName
- **Type**: typing.Optional[str]

### ModelArn
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### DatasetArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ActiveModelVersion
- **Type**: typing.Optional[int]

### ActiveModelVersionArn
- **Type**: typing.Optional[str]

### LatestScheduledRetrainingStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]

### LatestScheduledRetrainingModelVersion
- **Type**: typing.Optional[int]

### LatestScheduledRetrainingStartTime
- **Type**: typing.Optional[datetime.datetime]

### NextScheduledRetrainingStartDate
- **Type**: typing.Optional[datetime.datetime]

### RetrainingSchedulerStatus
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]

### ModelDiagnosticsOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.ModelDiagnosticsOutputConfigurationTypeDef]

### ModelQuality
- **Type**: typing.Optional[typing.Literal['CANNOT_DETERMINE_QUALITY', 'POOR_QUALITY_DETECTED', 'QUALITY_THRESHOLD_MET']]


# ModelVersionSummaryTypeDef

### ModelName
- **Type**: typing.Optional[str]

### ModelArn
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[int]

### ModelVersionArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]

### SourceType
- **Type**: typing.Optional[typing.Literal['IMPORT', 'RETRAINING', 'TRAINING']]

### ModelQuality
- **Type**: typing.Optional[typing.Literal['CANNOT_DETERMINE_QUALITY', 'POOR_QUALITY_DETECTED', 'QUALITY_THRESHOLD_MET']]


# MonotonicValuesTypeDef

### Status
- **Type**: typing.Literal['NO_ISSUE_DETECTED', 'POTENTIAL_ISSUE_DETECTED']
- **Required**: Yes

### Monotonicity
- **Type**: typing.Optional[typing.Literal['DECREASING', 'INCREASING', 'STATIC']]


# MultipleOperatingModesTypeDef

### Status
- **Type**: typing.Literal['NO_ISSUE_DETECTED', 'POTENTIAL_ISSUE_DETECTED']
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# PutResourcePolicyResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RetrainingSchedulerSummaryTypeDef

### ModelName
- **Type**: typing.Optional[str]

### ModelArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]

### RetrainingStartDate
- **Type**: typing.Optional[datetime.datetime]

### RetrainingFrequency
- **Type**: typing.Optional[str]

### LookbackWindow
- **Type**: typing.Optional[str]


# S3ObjectTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# SensorStatisticsSummaryTypeDef

### ComponentName
- **Type**: typing.Optional[str]

### SensorName
- **Type**: typing.Optional[str]

### DataExists
- **Type**: typing.Optional[bool]

### MissingValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.CountPercentTypeDef]

### InvalidValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.CountPercentTypeDef]

### InvalidDateEntries
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.CountPercentTypeDef]

### DuplicateTimestamps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.CountPercentTypeDef]

### CategoricalValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.CategoricalValuesTypeDef]

### MultipleOperatingModes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.MultipleOperatingModesTypeDef]

### LargeTimestampGaps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.LargeTimestampGapsTypeDef]

### MonotonicValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.MonotonicValuesTypeDef]

### DataStartTime
- **Type**: typing.Optional[datetime.datetime]

### DataEndTime
- **Type**: typing.Optional[datetime.datetime]


# SensorsWithShortDateRangeTypeDef

### AffectedSensorCount
- **Type**: <class 'int'>
- **Required**: Yes


# StartDataIngestionJobRequestTypeDef

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.IngestionInputConfigurationTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartDataIngestionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartInferenceSchedulerRequestTypeDef

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes


# StartInferenceSchedulerResponseTypeDef

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceSchedulerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartRetrainingSchedulerRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# StartRetrainingSchedulerResponseTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopInferenceSchedulerRequestTypeDef

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopInferenceSchedulerResponseTypeDef

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### InferenceSchedulerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopRetrainingSchedulerRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# StopRetrainingSchedulerResponseTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.lookoutequipment_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnsupportedTimestampsTypeDef

### TotalNumberOfUnsupportedTimestamps
- **Type**: <class 'int'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateActiveModelVersionRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateActiveModelVersionResponseTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentActiveVersion
- **Type**: <class 'int'>
- **Required**: Yes

### PreviousActiveVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CurrentActiveVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PreviousActiveVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateInferenceSchedulerRequestTypeDef

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### DataDelayOffsetInMinutes
- **Type**: typing.Optional[int]

### DataUploadFrequency
- **Type**: typing.Optional[typing.Literal['PT10M', 'PT15M', 'PT1H', 'PT30M', 'PT5M']]

### DataInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceInputConfigurationTypeDef]

### DataOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.InferenceOutputConfigurationTypeDef]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateLabelGroupRequestTypeDef

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FaultCodes
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateModelRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelsInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.LabelsInputConfigurationTypeDef]

### RoleArn
- **Type**: typing.Optional[str]

### ModelDiagnosticsOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.ModelDiagnosticsOutputConfigurationTypeDef]


# UpdateRetrainingSchedulerRequestTypeDef

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### RetrainingStartDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment_classes.TimestampTypeDef]

### RetrainingFrequency
- **Type**: typing.Optional[str]

### LookbackWindow
- **Type**: typing.Optional[str]

### PromoteMode
- **Type**: typing.Optional[typing.Literal['MANAGED', 'MANUAL']]



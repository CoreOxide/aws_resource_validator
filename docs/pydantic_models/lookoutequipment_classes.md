# Lookoutequipment Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CategoricalValues

### Status
- **Type**: typing.Literal['NO_ISSUE_DETECTED', 'POTENTIAL_ISSUE_DETECTED']
- **Required**: Yes

### NumberOfCategory
- **Type**: typing.Optional[int]


# CountPercent

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### Percentage
- **Type**: <class 'float'>
- **Required**: Yes


# CreateDatasetRequest

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetSchema
- **Type**: <class 'NoneType'>

### ServerSideKmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.Tag]]


# CreateDatasetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInferenceSchedulerRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceInputConfiguration'>
- **Required**: Yes

### DataOutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceOutputConfiguration'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.Tag]]


# CreateInferenceSchedulerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLabelGroupRequest

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### FaultCodes
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.Tag]]


# CreateLabelGroupResponse

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLabelRequest

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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


# CreateLabelResponse

### LabelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# CreateModelRequest

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
- **Type**: <class 'NoneType'>

### LabelsInputConfiguration
- **Type**: <class 'NoneType'>

### TrainingDataStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### TrainingDataEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EvaluationDataStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EvaluationDataEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### RoleArn
- **Type**: typing.Optional[str]

### DataPreProcessingConfiguration
- **Type**: <class 'NoneType'>

### ServerSideKmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.Tag]]

### OffCondition
- **Type**: typing.Optional[str]

### ModelDiagnosticsOutputConfiguration
- **Type**: <class 'NoneType'>


# CreateModelResponse

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRetrainingSchedulerRequest

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PromoteMode
- **Type**: typing.Optional[typing.Literal['MANAGED', 'MANUAL']]


# CreateRetrainingSchedulerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DataIngestionJobSummary

### JobId
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### DatasetArn
- **Type**: typing.Optional[str]

### IngestionInputConfiguration
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]


# DataPreProcessingConfiguration

### TargetSamplingRate
- **Type**: typing.Optional[typing.Literal['PT10M', 'PT10S', 'PT15M', 'PT15S', 'PT1H', 'PT1M', 'PT1S', 'PT30M', 'PT30S', 'PT5M', 'PT5S']]


# DataQualitySummary

### InsufficientSensorData
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InsufficientSensorData'>
- **Required**: Yes

### MissingSensorData
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.MissingSensorData'>
- **Required**: Yes

### InvalidSensorData
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InvalidSensorData'>
- **Required**: Yes

### UnsupportedTimestamps
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.UnsupportedTimestamps'>
- **Required**: Yes

### DuplicateTimestamps
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.DuplicateTimestamps'>
- **Required**: Yes


# DatasetSchema

### InlineDataSchema
- **Type**: typing.Optional[str]


# DatasetSummary

### DatasetName
- **Type**: typing.Optional[str]

### DatasetArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATED', 'IMPORT_IN_PROGRESS', 'INGESTION_IN_PROGRESS']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]


# DeleteDatasetRequest

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInferenceSchedulerRequest

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLabelGroupRequest

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLabelRequest

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetrainingSchedulerRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataIngestionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataIngestionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.IngestionInputConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.DataQualitySummary'>
- **Required**: Yes

### IngestedFilesSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.IngestedFilesSummary'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.IngestionInputConfiguration'>
- **Required**: Yes

### DataQualitySummary
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.DataQualitySummary'>
- **Required**: Yes

### IngestedFilesSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.IngestedFilesSummary'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInferenceSchedulerRequest

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInferenceSchedulerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceInputConfiguration'>
- **Required**: Yes

### DataOutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceOutputConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLabelGroupRequest

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLabelGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLabelRequest

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLabelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.LabelsInputConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.DataPreProcessingConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ModelDiagnosticsOutputConfiguration'>
- **Required**: Yes

### ModelQuality
- **Type**: typing.Literal['CANNOT_DETERMINE_QUALITY', 'POOR_QUALITY_DETECTED', 'QUALITY_THRESHOLD_MET']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeModelVersionRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeModelVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.LabelsInputConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.DataPreProcessingConfiguration'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ModelDiagnosticsOutputConfiguration'>
- **Required**: Yes

### ModelDiagnosticsResultsObject
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.S3Object'>
- **Required**: Yes

### ModelQuality
- **Type**: typing.Literal['CANNOT_DETERMINE_QUALITY', 'POOR_QUALITY_DETECTED', 'QUALITY_THRESHOLD_MET']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourcePolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRetrainingSchedulerRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRetrainingSchedulerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# DuplicateTimestamps

### TotalNumberOfDuplicateTimestamps
- **Type**: <class 'int'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# ImportDatasetRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.Tag]]


# ImportDatasetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# ImportModelVersionRequest

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
- **Type**: <class 'NoneType'>

### RoleArn
- **Type**: typing.Optional[str]

### ServerSideKmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.Tag]]

### InferenceDataImportStrategy
- **Type**: typing.Optional[typing.Literal['ADD_WHEN_EMPTY', 'NO_IMPORT', 'OVERWRITE']]


# ImportModelVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# InferenceEventSummary

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


# InferenceExecutionSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceInputConfiguration]

### DataOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceOutputConfiguration]

### CustomerResultObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.S3Object]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]

### FailedReason
- **Type**: typing.Optional[str]

### ModelVersion
- **Type**: typing.Optional[int]

### ModelVersionArn
- **Type**: typing.Optional[str]


# InferenceInputConfiguration

### S3InputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceS3InputConfiguration]

### InputTimeZoneOffset
- **Type**: typing.Optional[str]

### InferenceInputNameConfiguration
- **Type**: <class 'NoneType'>


# InferenceInputNameConfiguration

### TimestampFormat
- **Type**: typing.Optional[str]

### ComponentTimestampDelimiter
- **Type**: typing.Optional[str]


# InferenceOutputConfiguration

### S3OutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceS3OutputConfiguration'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# InferenceS3InputConfiguration

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# InferenceS3OutputConfiguration

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# InferenceSchedulerSummary

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


# IngestedFilesSummary

### TotalNumberOfFiles
- **Type**: <class 'int'>
- **Required**: Yes

### IngestedNumberOfFiles
- **Type**: <class 'int'>
- **Required**: Yes

### DiscardedFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.S3Object]]


# IngestionInputConfiguration

### S3InputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.IngestionS3InputConfiguration'>
- **Required**: Yes


# IngestionS3InputConfiguration

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### KeyPattern
- **Type**: typing.Optional[str]


# InsufficientSensorData

### MissingCompleteSensorData
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.MissingCompleteSensorData'>
- **Required**: Yes

### SensorsWithShortDateRange
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.SensorsWithShortDateRange'>
- **Required**: Yes


# InvalidSensorData

### AffectedSensorCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalNumberOfInvalidValues
- **Type**: <class 'int'>
- **Required**: Yes


# LabelGroupSummary

### LabelGroupName
- **Type**: typing.Optional[str]

### LabelGroupArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# LabelSummary

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


# LabelsInputConfiguration

### S3InputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.LabelsS3InputConfiguration]

### LabelGroupName
- **Type**: typing.Optional[str]


# LabelsS3InputConfiguration

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# LargeTimestampGaps

### Status
- **Type**: typing.Literal['NO_ISSUE_DETECTED', 'POTENTIAL_ISSUE_DETECTED']
- **Required**: Yes

### NumberOfLargeTimestampGaps
- **Type**: typing.Optional[int]

### MaxTimestampGapInDays
- **Type**: typing.Optional[int]


# ListDataIngestionJobsRequest

### DatasetName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']]


# ListDataIngestionJobsResponse

### DataIngestionJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.DataIngestionJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### DatasetNameBeginsWith
- **Type**: typing.Optional[str]


# ListDatasetsResponse

### DatasetSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.DatasetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceEventsRequest

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### IntervalStartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### IntervalEndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListInferenceEventsResponse

### InferenceEventSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceEventSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceExecutionsRequest

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### DataStartTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DataEndTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCESS']]


# ListInferenceExecutionsResponse

### InferenceExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInferenceSchedulersRequest

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


# ListInferenceSchedulersResponse

### InferenceSchedulerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceSchedulerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLabelGroupsRequest

### LabelGroupNameBeginsWith
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLabelGroupsResponse

### LabelGroupSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.LabelGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLabelsRequest

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### IntervalStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### IntervalEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### FaultCode
- **Type**: typing.Optional[str]

### Equipment
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListLabelsResponse

### LabelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.LabelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelVersionsRequest

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedAtStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxModelVersion
- **Type**: typing.Optional[int]

### MinModelVersion
- **Type**: typing.Optional[int]


# ListModelVersionsResponse

### ModelVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ModelVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListModelsRequest

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


# ListModelsResponse

### ModelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRetrainingSchedulersRequest

### ModelNameBeginsWith
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'STOPPED', 'STOPPING']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRetrainingSchedulersResponse

### RetrainingSchedulerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.RetrainingSchedulerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSensorStatisticsRequest

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionJobId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSensorStatisticsResponse

### SensorStatisticsSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.SensorStatisticsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# MissingCompleteSensorData

### AffectedSensorCount
- **Type**: <class 'int'>
- **Required**: Yes


# MissingSensorData

### AffectedSensorCount
- **Type**: <class 'int'>
- **Required**: Yes

### TotalNumberOfMissingValues
- **Type**: <class 'int'>
- **Required**: Yes


# ModelDiagnosticsOutputConfiguration

### S3OutputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ModelDiagnosticsS3OutputConfiguration'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ModelDiagnosticsS3OutputConfiguration

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]


# ModelSummary

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
- **Type**: <class 'NoneType'>

### ModelQuality
- **Type**: typing.Optional[typing.Literal['CANNOT_DETERMINE_QUALITY', 'POOR_QUALITY_DETECTED', 'QUALITY_THRESHOLD_MET']]


# ModelVersionSummary

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


# MonotonicValues

### Status
- **Type**: typing.Literal['NO_ISSUE_DETECTED', 'POTENTIAL_ISSUE_DETECTED']
- **Required**: Yes

### Monotonicity
- **Type**: typing.Optional[typing.Literal['DECREASING', 'INCREASING', 'STATIC']]


# MultipleOperatingModes

### Status
- **Type**: typing.Literal['NO_ISSUE_DETECTED', 'POTENTIAL_ISSUE_DETECTED']
- **Required**: Yes


# PutResourcePolicyRequest

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


# PutResourcePolicyResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


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


# RetrainingSchedulerSummary

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


# S3Object

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# SensorStatisticsSummary

### ComponentName
- **Type**: typing.Optional[str]

### SensorName
- **Type**: typing.Optional[str]

### DataExists
- **Type**: typing.Optional[bool]

### MissingValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.CountPercent]

### InvalidValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.CountPercent]

### InvalidDateEntries
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.CountPercent]

### DuplicateTimestamps
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.CountPercent]

### CategoricalValues
- **Type**: <class 'NoneType'>

### MultipleOperatingModes
- **Type**: <class 'NoneType'>

### LargeTimestampGaps
- **Type**: <class 'NoneType'>

### MonotonicValues
- **Type**: <class 'NoneType'>

### DataStartTime
- **Type**: typing.Optional[datetime.datetime]

### DataEndTime
- **Type**: typing.Optional[datetime.datetime]


# SensorsWithShortDateRange

### AffectedSensorCount
- **Type**: <class 'int'>
- **Required**: Yes


# StartDataIngestionJobRequest

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionInputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.IngestionInputConfiguration'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartDataIngestionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IMPORT_IN_PROGRESS', 'IN_PROGRESS', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# StartInferenceSchedulerRequest

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes


# StartInferenceSchedulerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# StartRetrainingSchedulerRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# StartRetrainingSchedulerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# StopInferenceSchedulerRequest

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes


# StopInferenceSchedulerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# StopRetrainingSchedulerRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes


# StopRetrainingSchedulerResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.Tag]
- **Required**: Yes


# UnsupportedTimestamps

### TotalNumberOfUnsupportedTimestamps
- **Type**: <class 'int'>
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateActiveModelVersionRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### ModelVersion
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateActiveModelVersionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateInferenceSchedulerRequest

### InferenceSchedulerName
- **Type**: <class 'str'>
- **Required**: Yes

### DataDelayOffsetInMinutes
- **Type**: typing.Optional[int]

### DataUploadFrequency
- **Type**: typing.Optional[typing.Literal['PT10M', 'PT15M', 'PT1H', 'PT30M', 'PT5M']]

### DataInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceInputConfiguration]

### DataOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lookoutequipment.lookoutequipment_classes.InferenceOutputConfiguration]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateLabelGroupRequest

### LabelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FaultCodes
- **Type**: typing.Optional[typing.List[str]]


# UpdateModelRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### LabelsInputConfiguration
- **Type**: <class 'NoneType'>

### RoleArn
- **Type**: typing.Optional[str]

### ModelDiagnosticsOutputConfiguration
- **Type**: <class 'NoneType'>


# UpdateRetrainingSchedulerRequest

### ModelName
- **Type**: <class 'str'>
- **Required**: Yes

### RetrainingStartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### RetrainingFrequency
- **Type**: typing.Optional[str]

### LookbackWindow
- **Type**: typing.Optional[str]

### PromoteMode
- **Type**: typing.Optional[typing.Literal['MANAGED', 'MANUAL']]



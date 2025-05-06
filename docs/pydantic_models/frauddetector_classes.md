# Frauddetector Classes

# ATIMetricDataPoint

### cr
- **Type**: typing.Optional[float]

### adr
- **Type**: typing.Optional[float]

### threshold
- **Type**: typing.Optional[float]

### atodr
- **Type**: typing.Optional[float]


# ATIModelPerformance

### asi
- **Type**: typing.Optional[float]


# ATITrainingMetricsValue

### metricDataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ATIMetricDataPoint]]

### modelPerformance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ATIModelPerformance]


# AggregatedLogOddsMetric

### variableNames
- **Type**: typing.List[str]
- **Required**: Yes

### aggregatedVariablesImportance
- **Type**: <class 'float'>
- **Required**: Yes


# AggregatedVariablesImpactExplanation

### eventVariableNames
- **Type**: typing.Optional[typing.List[str]]

### relativeImpact
- **Type**: typing.Optional[str]

### logOddsImpact
- **Type**: typing.Optional[float]


# AggregatedVariablesImportanceMetrics

### logOddsMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.AggregatedLogOddsMetric]]


# AllowDenyList

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### variableType
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### updatedTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateVariableError

### name
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]


# BatchCreateVariableRequest

### variableEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.VariableEntry]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# BatchCreateVariableResult

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.BatchCreateVariableError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetVariableError

### name
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]


# BatchGetVariableRequest

### names
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetVariableResult

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Variable]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.BatchGetVariableError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# BatchImport

### jobId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'CANCEL_IN_PROGRESS', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'IN_PROGRESS_INITIALIZING']]

### failureReason
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[str]

### completionTime
- **Type**: typing.Optional[str]

### inputPath
- **Type**: typing.Optional[str]

### outputPath
- **Type**: typing.Optional[str]

### eventTypeName
- **Type**: typing.Optional[str]

### iamRoleArn
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### processedRecordsCount
- **Type**: typing.Optional[int]

### failedRecordsCount
- **Type**: typing.Optional[int]

### totalRecordsCount
- **Type**: typing.Optional[int]


# BatchPrediction

### jobId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'CANCEL_IN_PROGRESS', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'IN_PROGRESS_INITIALIZING']]

### failureReason
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[str]

### completionTime
- **Type**: typing.Optional[str]

### lastHeartbeatTime
- **Type**: typing.Optional[str]

### inputPath
- **Type**: typing.Optional[str]

### outputPath
- **Type**: typing.Optional[str]

### eventTypeName
- **Type**: typing.Optional[str]

### detectorName
- **Type**: typing.Optional[str]

### detectorVersion
- **Type**: typing.Optional[str]

### iamRoleArn
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### processedRecordsCount
- **Type**: typing.Optional[int]

### totalRecordsCount
- **Type**: typing.Optional[int]


# CancelBatchImportJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelBatchPredictionJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBatchImportJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### inputPath
- **Type**: <class 'str'>
- **Required**: Yes

### outputPath
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### iamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# CreateBatchPredictionJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### inputPath
- **Type**: <class 'str'>
- **Required**: Yes

### outputPath
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorName
- **Type**: <class 'str'>
- **Required**: Yes

### iamRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersion
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# CreateDetectorVersionRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Rule]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### externalModelEndpoints
- **Type**: typing.Optional[typing.List[str]]

### modelVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelVersion]]

### ruleExecutionMode
- **Type**: typing.Optional[typing.Literal['ALL_MATCHED', 'FIRST_MATCHED']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# CreateDetectorVersionResult

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DRAFT', 'INACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# CreateListRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### elements
- **Type**: typing.Optional[typing.List[str]]

### variableType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# CreateModelRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# CreateModelVersionRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### trainingDataSource
- **Type**: typing.Literal['EXTERNAL_EVENTS', 'INGESTED_EVENTS']
- **Required**: Yes

### trainingDataSchema
- **Type**: typing.Union[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TrainingDataSchema, aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TrainingDataSchemaOutput]
- **Required**: Yes

### externalEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ExternalEventsDetail]

### ingestedEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.IngestedEventsDetail]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# CreateModelVersionResult

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleRequest

### ruleId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### language
- **Type**: typing.Literal['DETECTORPL']
- **Required**: Yes

### outcomes
- **Type**: typing.List[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# CreateRuleResult

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Rule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVariableRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: typing.Literal['BOOLEAN', 'DATETIME', 'FLOAT', 'INTEGER', 'STRING']
- **Required**: Yes

### dataSource
- **Type**: typing.Literal['EVENT', 'EXTERNAL_MODEL_SCORE', 'MODEL_SCORE']
- **Required**: Yes

### defaultValue
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### variableType
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# DataValidationMetrics

### fileLevelMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.FileValidationMessage]]

### fieldLevelMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.FieldValidationMessage]]


# DeleteBatchImportJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBatchPredictionJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorVersionRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEntityTypeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventRequest

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### deleteAuditHistory
- **Type**: typing.Optional[bool]


# DeleteEventTypeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventsByEventTypeRequest

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventsByEventTypeResult

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### eventsDeletionStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteExternalModelRequest

### modelEndpoint
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLabelRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes


# DeleteModelVersionRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutcomeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequest

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Rule'>
- **Required**: Yes


# DeleteVariableRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDetectorRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeDetectorResult

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.DetectorVersionSummary]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeModelVersionsRequest

### modelId
- **Type**: typing.Optional[str]

### modelVersionNumber
- **Type**: typing.Optional[str]

### modelType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeModelVersionsResult

### modelVersionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelVersionDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Detector

### detectorId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### eventTypeName
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# DetectorVersionSummary

### detectorVersionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAFT', 'INACTIVE']]

### description
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]


# Entity

### entityType
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes


# EntityType

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# EvaluatedExternalModel

### modelEndpoint
- **Type**: typing.Optional[str]

### useEventVariables
- **Type**: typing.Optional[bool]

### inputVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### outputVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# EvaluatedModelVersion

### modelId
- **Type**: typing.Optional[str]

### modelVersion
- **Type**: typing.Optional[str]

### modelType
- **Type**: typing.Optional[str]

### evaluations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelVersionEvaluation]]


# EvaluatedRule

### ruleId
- **Type**: typing.Optional[str]

### ruleVersion
- **Type**: typing.Optional[str]

### expression
- **Type**: typing.Optional[str]

### expressionWithValues
- **Type**: typing.Optional[str]

### outcomes
- **Type**: typing.Optional[typing.List[str]]

### evaluated
- **Type**: typing.Optional[bool]

### matched
- **Type**: typing.Optional[bool]


# Event

### eventId
- **Type**: typing.Optional[str]

### eventTypeName
- **Type**: typing.Optional[str]

### eventTimestamp
- **Type**: typing.Optional[str]

### eventVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### currentLabel
- **Type**: typing.Optional[str]

### labelTimestamp
- **Type**: typing.Optional[str]

### entities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Entity]]


# EventOrchestration

### eventBridgeEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# EventPredictionSummary

### eventId
- **Type**: typing.Optional[str]

### eventTypeName
- **Type**: typing.Optional[str]

### eventTimestamp
- **Type**: typing.Optional[str]

### predictionTimestamp
- **Type**: typing.Optional[str]

### detectorId
- **Type**: typing.Optional[str]

### detectorVersionId
- **Type**: typing.Optional[str]


# EventType

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### eventVariables
- **Type**: typing.Optional[typing.List[str]]

### labels
- **Type**: typing.Optional[typing.List[str]]

### entityTypes
- **Type**: typing.Optional[typing.List[str]]

### eventIngestion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ingestedEventStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.IngestedEventStatistics]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### eventOrchestration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EventOrchestration]


# EventVariableSummary

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]


# ExternalEventsDetail

### dataLocation
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ExternalModel

### modelEndpoint
- **Type**: typing.Optional[str]

### modelSource
- **Type**: typing.Optional[typing.Literal['SAGEMAKER']]

### invokeModelEndpointRoleArn
- **Type**: typing.Optional[str]

### inputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelInputConfiguration]

### outputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelOutputConfigurationOutput]

### modelEndpointStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'DISSOCIATED']]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# ExternalModelOutputs

### externalModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ExternalModelSummary]

### outputs
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExternalModelSummary

### modelEndpoint
- **Type**: typing.Optional[str]

### modelSource
- **Type**: typing.Optional[typing.Literal['SAGEMAKER']]


# FieldValidationMessage

### fieldName
- **Type**: typing.Optional[str]

### identifier
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### content
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# FileValidationMessage

### title
- **Type**: typing.Optional[str]

### content
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# FilterCondition

### value
- **Type**: typing.Optional[str]


# GetBatchImportJobsRequest

### jobId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetBatchImportJobsResult

### batchImports
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.BatchImport]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBatchPredictionJobsRequest

### jobId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetBatchPredictionJobsResult

### batchPredictions
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.BatchPrediction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetDeleteEventsByEventTypeStatusRequest

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeleteEventsByEventTypeStatusResult

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### eventsDeletionStatus
- **Type**: typing.Literal['CANCELED', 'CANCEL_IN_PROGRESS', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'IN_PROGRESS_INITIALIZING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# GetDetectorVersionRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDetectorVersionResult

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### externalModelEndpoints
- **Type**: typing.List[str]
- **Required**: Yes

### modelVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelVersion]
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Rule]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DRAFT', 'INACTIVE']
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'str'>
- **Required**: Yes

### ruleExecutionMode
- **Type**: typing.Literal['ALL_MATCHED', 'FIRST_MATCHED']
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# GetDetectorsRequest

### detectorId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetDetectorsResult

### detectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Detector]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEntityTypesRequest

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEntityTypesResult

### entityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EntityType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEventPredictionMetadataRequest

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### predictionTimestamp
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventPredictionMetadataResult

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### entityType
- **Type**: <class 'str'>
- **Required**: Yes

### eventTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionStatus
- **Type**: <class 'str'>
- **Required**: Yes

### eventVariables
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EventVariableSummary]
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EvaluatedRule]
- **Required**: Yes

### ruleExecutionMode
- **Type**: typing.Literal['ALL_MATCHED', 'FIRST_MATCHED']
- **Required**: Yes

### outcomes
- **Type**: typing.List[str]
- **Required**: Yes

### evaluatedModelVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EvaluatedModelVersion]
- **Required**: Yes

### evaluatedExternalModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EvaluatedExternalModel]
- **Required**: Yes

### predictionTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventPredictionRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Entity]
- **Required**: Yes

### eventTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### eventVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### detectorVersionId
- **Type**: typing.Optional[str]

### externalModelEndpointDataBlobs
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelEndpointDataBlob]]


# GetEventPredictionResult

### modelScores
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelScores]
- **Required**: Yes

### ruleResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.RuleResult]
- **Required**: Yes

### externalModelOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ExternalModelOutputs]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventRequest

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventResult

### event
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Event'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventTypesRequest

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEventTypesResult

### eventTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EventType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetExternalModelsRequest

### modelEndpoint
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetExternalModelsResult

### externalModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ExternalModel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetKMSEncryptionKeyResult

### kmsKey
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.KMSKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# GetLabelsRequest

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetLabelsResult

### labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Label]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetListElementsRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetListElementsResult

### elements
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetListsMetadataRequest

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetListsMetadataResult

### lists
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.AllowDenyList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetModelVersionRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelVersionResult

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDataSource
- **Type**: typing.Literal['EXTERNAL_EVENTS', 'INGESTED_EVENTS']
- **Required**: Yes

### trainingDataSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TrainingDataSchemaOutput'>
- **Required**: Yes

### externalEventsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ExternalEventsDetail'>
- **Required**: Yes

### ingestedEventsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.IngestedEventsDetail'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# GetModelsRequest

### modelId
- **Type**: typing.Optional[str]

### modelType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetModelsResult

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Model]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetOutcomesRequest

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetOutcomesResult

### outcomes
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Outcome]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetRulesRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ruleId
- **Type**: typing.Optional[str]

### ruleVersion
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetRulesResult

### ruleDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.RuleDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetVariablesRequest

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetVariablesResult

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Variable]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# IngestedEventStatistics

### numberOfEvents
- **Type**: typing.Optional[int]

### eventDataSizeInBytes
- **Type**: typing.Optional[int]

### leastRecentEvent
- **Type**: typing.Optional[str]

### mostRecentEvent
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]


# IngestedEventsDetail

### ingestedEventsTimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.IngestedEventsTimeWindow'>
- **Required**: Yes


# IngestedEventsTimeWindow

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'str'>
- **Required**: Yes


# KMSKey

### kmsEncryptionKeyArn
- **Type**: typing.Optional[str]


# Label

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# LabelSchema

### labelMapper
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### unlabeledEventsTreatment
- **Type**: typing.Optional[typing.Literal['AUTO', 'FRAUD', 'IGNORE', 'LEGIT']]


# LabelSchemaOutput

### labelMapper
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### unlabeledEventsTreatment
- **Type**: typing.Optional[typing.Literal['AUTO', 'FRAUD', 'IGNORE', 'LEGIT']]


# ListEventPredictionsRequest

### eventId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.FilterCondition]

### eventType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.FilterCondition]

### detectorId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.FilterCondition]

### detectorVersionId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.FilterCondition]

### predictionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.PredictionTimeRange]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEventPredictionsResult

### eventPredictionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EventPredictionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceResult

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogOddsMetric

### variableName
- **Type**: <class 'str'>
- **Required**: Yes

### variableType
- **Type**: <class 'str'>
- **Required**: Yes

### variableImportance
- **Type**: <class 'float'>
- **Required**: Yes


# MetricDataPoint

### fpr
- **Type**: typing.Optional[float]

### precision
- **Type**: typing.Optional[float]

### tpr
- **Type**: typing.Optional[float]

### threshold
- **Type**: typing.Optional[float]


# Model

### modelId
- **Type**: typing.Optional[str]

### modelType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']]

### description
- **Type**: typing.Optional[str]

### eventTypeName
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# ModelEndpointDataBlob

### byteBuffer
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### contentType
- **Type**: typing.Optional[str]


# ModelInputConfiguration

### useEventVariables
- **Type**: <class 'bool'>
- **Required**: Yes

### eventTypeName
- **Type**: typing.Optional[str]

### format
- **Type**: typing.Optional[typing.Literal['APPLICATION_JSON', 'TEXT_CSV']]

### jsonInputTemplate
- **Type**: typing.Optional[str]

### csvInputTemplate
- **Type**: typing.Optional[str]


# ModelOutputConfiguration

### format
- **Type**: typing.Literal['APPLICATION_JSONLINES', 'TEXT_CSV']
- **Required**: Yes

### jsonKeyToVariableMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### csvIndexToVariableMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelOutputConfigurationOutput

### format
- **Type**: typing.Literal['APPLICATION_JSONLINES', 'TEXT_CSV']
- **Required**: Yes

### jsonKeyToVariableMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### csvIndexToVariableMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# ModelScores

### modelVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelVersion]

### scores
- **Type**: typing.Optional[typing.Dict[str, float]]


# ModelVersion

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]


# ModelVersionDetail

### modelId
- **Type**: typing.Optional[str]

### modelType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']]

### modelVersionNumber
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### trainingDataSource
- **Type**: typing.Optional[typing.Literal['EXTERNAL_EVENTS', 'INGESTED_EVENTS']]

### trainingDataSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TrainingDataSchemaOutput]

### externalEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ExternalEventsDetail]

### ingestedEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.IngestedEventsDetail]

### trainingResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TrainingResult]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### trainingResultV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TrainingResultV2]


# ModelVersionEvaluation

### outputVariableName
- **Type**: typing.Optional[str]

### evaluationScore
- **Type**: typing.Optional[str]

### predictionExplanations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.PredictionExplanations]


# OFIMetricDataPoint

### fpr
- **Type**: typing.Optional[float]

### precision
- **Type**: typing.Optional[float]

### tpr
- **Type**: typing.Optional[float]

### threshold
- **Type**: typing.Optional[float]


# OFIModelPerformance

### auc
- **Type**: typing.Optional[float]

### uncertaintyRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.UncertaintyRange]


# OFITrainingMetricsValue

### metricDataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.OFIMetricDataPoint]]

### modelPerformance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.OFIModelPerformance]


# Outcome

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# PredictionExplanations

### variableImpactExplanations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.VariableImpactExplanation]]

### aggregatedVariablesImpactExplanations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.AggregatedVariablesImpactExplanation]]


# PredictionTimeRange

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'str'>
- **Required**: Yes


# PutDetectorRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# PutEntityTypeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# PutEventTypeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### eventVariables
- **Type**: typing.List[str]
- **Required**: Yes

### entityTypes
- **Type**: typing.List[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.List[str]]

### eventIngestion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]

### eventOrchestration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.EventOrchestration]


# PutExternalModelRequest

### modelEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### modelSource
- **Type**: typing.Literal['SAGEMAKER']
- **Required**: Yes

### invokeModelEndpointRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### inputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelInputConfiguration'>
- **Required**: Yes

### outputConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelOutputConfiguration, aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelOutputConfigurationOutput]
- **Required**: Yes

### modelEndpointStatus
- **Type**: typing.Literal['ASSOCIATED', 'DISSOCIATED']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# PutKMSEncryptionKeyRequest

### kmsEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutLabelRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# PutOutcomeRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


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


# Rule

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ruleId
- **Type**: <class 'str'>
- **Required**: Yes

### ruleVersion
- **Type**: <class 'str'>
- **Required**: Yes


# RuleDetail

### ruleId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### detectorId
- **Type**: typing.Optional[str]

### ruleVersion
- **Type**: typing.Optional[str]

### expression
- **Type**: typing.Optional[str]

### language
- **Type**: typing.Optional[typing.Literal['DETECTORPL']]

### outcomes
- **Type**: typing.Optional[typing.List[str]]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# RuleResult

### ruleId
- **Type**: typing.Optional[str]

### outcomes
- **Type**: typing.Optional[typing.List[str]]


# SendEventRequest

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### eventTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### eventVariables
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Entity]
- **Required**: Yes

### assignedLabel
- **Type**: typing.Optional[str]

### labelTimestamp
- **Type**: typing.Optional[str]


# TFIMetricDataPoint

### fpr
- **Type**: typing.Optional[float]

### precision
- **Type**: typing.Optional[float]

### tpr
- **Type**: typing.Optional[float]

### threshold
- **Type**: typing.Optional[float]


# TFIModelPerformance

### auc
- **Type**: typing.Optional[float]

### uncertaintyRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.UncertaintyRange]


# TFITrainingMetricsValue

### metricDataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TFIMetricDataPoint]]

### modelPerformance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TFIModelPerformance]


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]
- **Required**: Yes


# TrainingDataSchema

### modelVariables
- **Type**: typing.List[str]
- **Required**: Yes

### labelSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.LabelSchema]


# TrainingDataSchemaOutput

### modelVariables
- **Type**: typing.List[str]
- **Required**: Yes

### labelSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.LabelSchemaOutput]


# TrainingMetrics

### auc
- **Type**: typing.Optional[float]

### metricDataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.MetricDataPoint]]


# TrainingMetricsV2

### ofi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.OFITrainingMetricsValue]

### tfi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TFITrainingMetricsValue]

### ati
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ATITrainingMetricsValue]


# TrainingResult

### dataValidationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.DataValidationMetrics]

### trainingMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TrainingMetrics]

### variableImportanceMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.VariableImportanceMetrics]


# TrainingResultV2

### dataValidationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.DataValidationMetrics]

### trainingMetricsV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.TrainingMetricsV2]

### variableImportanceMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.VariableImportanceMetrics]

### aggregatedVariablesImportanceMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.AggregatedVariablesImportanceMetrics]


# UncertaintyRange

### lowerBoundValue
- **Type**: <class 'float'>
- **Required**: Yes

### upperBoundValue
- **Type**: <class 'float'>
- **Required**: Yes


# UntagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDetectorVersionMetadataRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDetectorVersionRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### externalModelEndpoints
- **Type**: typing.List[str]
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Rule]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### modelVersions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ModelVersion]]

### ruleExecutionMode
- **Type**: typing.Optional[typing.Literal['ALL_MATCHED', 'FIRST_MATCHED']]


# UpdateDetectorVersionStatusRequest

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DRAFT', 'INACTIVE']
- **Required**: Yes


# UpdateEventLabelRequest

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### assignedLabel
- **Type**: <class 'str'>
- **Required**: Yes

### labelTimestamp
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateListRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### elements
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### updateMode
- **Type**: typing.Optional[typing.Literal['APPEND', 'REMOVE', 'REPLACE']]

### variableType
- **Type**: typing.Optional[str]


# UpdateModelRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateModelVersionRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### majorVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes

### externalEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ExternalEventsDetail]

### ingestedEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.IngestedEventsDetail]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# UpdateModelVersionResult

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateModelVersionStatusRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE', 'TRAINING_CANCELLED']
- **Required**: Yes


# UpdateRuleMetadataRequest

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Rule'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRuleVersionRequest

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Rule'>
- **Required**: Yes

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### language
- **Type**: typing.Literal['DETECTORPL']
- **Required**: Yes

### outcomes
- **Type**: typing.List[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Tag]]


# UpdateRuleVersionResult

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.Rule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVariableRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### variableType
- **Type**: typing.Optional[str]


# Variable

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['BOOLEAN', 'DATETIME', 'FLOAT', 'INTEGER', 'STRING']]

### dataSource
- **Type**: typing.Optional[typing.Literal['EVENT', 'EXTERNAL_MODEL_SCORE', 'MODEL_SCORE']]

### defaultValue
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### variableType
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# VariableEntry

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[str]

### dataSource
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### variableType
- **Type**: typing.Optional[str]


# VariableImpactExplanation

### eventVariableName
- **Type**: typing.Optional[str]

### relativeImpact
- **Type**: typing.Optional[str]

### logOddsImpact
- **Type**: typing.Optional[float]


# VariableImportanceMetrics

### logOddsMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector.frauddetector_classes.LogOddsMetric]]



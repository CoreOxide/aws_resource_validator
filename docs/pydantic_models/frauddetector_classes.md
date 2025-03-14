# Frauddetector Classes

# ATIMetricDataPointTypeDef

### cr
- **Type**: typing.Optional[float]

### adr
- **Type**: typing.Optional[float]

### threshold
- **Type**: typing.Optional[float]

### atodr
- **Type**: typing.Optional[float]


# ATIModelPerformanceTypeDef

### asi
- **Type**: typing.Optional[float]


# ATITrainingMetricsValueTypeDef

### metricDataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ATIMetricDataPointTypeDef]]

### modelPerformance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ATIModelPerformanceTypeDef]


# AggregatedLogOddsMetricTypeDef

### variableNames
- **Type**: typing.List[str]
- **Required**: Yes

### aggregatedVariablesImportance
- **Type**: <class 'float'>
- **Required**: Yes


# AggregatedVariablesImpactExplanationTypeDef

### eventVariableNames
- **Type**: typing.Optional[typing.List[str]]

### relativeImpact
- **Type**: typing.Optional[str]

### logOddsImpact
- **Type**: typing.Optional[float]


# AggregatedVariablesImportanceMetricsTypeDef

### logOddsMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.AggregatedLogOddsMetricTypeDef]]


# AllowDenyListTypeDef

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

# BatchCreateVariableErrorTypeDef

### name
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]


# BatchCreateVariableRequestTypeDef

### variableEntries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.VariableEntryTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# BatchCreateVariableResultTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.BatchCreateVariableErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetVariableErrorTypeDef

### name
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[int]

### message
- **Type**: typing.Optional[str]


# BatchGetVariableRequestTypeDef

### names
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetVariableResultTypeDef

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.VariableTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.BatchGetVariableErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchImportTypeDef

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


# BatchPredictionTypeDef

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


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelBatchImportJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelBatchPredictionJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBatchImportJobRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# CreateBatchPredictionJobRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# CreateDetectorVersionRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### externalModelEndpoints
- **Type**: typing.Optional[typing.Sequence[str]]

### modelVersions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.ModelVersionTypeDef]]

### ruleExecutionMode
- **Type**: typing.Optional[typing.Literal['ALL_MATCHED', 'FIRST_MATCHED']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# CreateDetectorVersionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateListRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### elements
- **Type**: typing.Optional[typing.Sequence[str]]

### variableType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# CreateModelRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# CreateModelVersionRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.TrainingDataSchemaUnionTypeDef'>
- **Required**: Yes

### externalEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ExternalEventsDetailTypeDef]

### ingestedEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.IngestedEventsDetailTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# CreateModelVersionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleRequestTypeDef

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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# CreateRuleResultTypeDef

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVariableRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# DataValidationMetricsTypeDef

### fileLevelMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.FileValidationMessageTypeDef]]

### fieldLevelMessages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.FieldValidationMessageTypeDef]]


# DeleteBatchImportJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBatchPredictionJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorVersionRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEntityTypeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventRequestTypeDef

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### deleteAuditHistory
- **Type**: typing.Optional[bool]


# DeleteEventTypeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventsByEventTypeRequestTypeDef

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventsByEventTypeResultTypeDef

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### eventsDeletionStatus
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteExternalModelRequestTypeDef

### modelEndpoint
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLabelRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes


# DeleteModelVersionRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutcomeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequestTypeDef

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef'>
- **Required**: Yes


# DeleteVariableRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDetectorRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeDetectorResultTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.DetectorVersionSummaryTypeDef]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeModelVersionsRequestTypeDef

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


# DescribeModelVersionsResultTypeDef

### modelVersionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ModelVersionDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DetectorTypeDef

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


# DetectorVersionSummaryTypeDef

### detectorVersionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DRAFT', 'INACTIVE']]

### description
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[str]


# EntityTypeDef

### entityType
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes


# EntityTypeTypeDef

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


# EvaluatedExternalModelTypeDef

### modelEndpoint
- **Type**: typing.Optional[str]

### useEventVariables
- **Type**: typing.Optional[bool]

### inputVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### outputVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# EvaluatedModelVersionTypeDef

### modelId
- **Type**: typing.Optional[str]

### modelVersion
- **Type**: typing.Optional[str]

### modelType
- **Type**: typing.Optional[str]

### evaluations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ModelVersionEvaluationTypeDef]]


# EvaluatedRuleTypeDef

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


# EventOrchestrationTypeDef

### eventBridgeEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# EventPredictionSummaryTypeDef

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


# EventTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.EntityTypeDef]]


# EventTypeTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.IngestedEventStatisticsTypeDef]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### eventOrchestration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.EventOrchestrationTypeDef]


# EventVariableSummaryTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]


# ExternalEventsDetailTypeDef

### dataLocation
- **Type**: <class 'str'>
- **Required**: Yes

### dataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ExternalModelOutputsTypeDef

### externalModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ExternalModelSummaryTypeDef]

### outputs
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExternalModelSummaryTypeDef

### modelEndpoint
- **Type**: typing.Optional[str]

### modelSource
- **Type**: typing.Optional[typing.Literal['SAGEMAKER']]


# ExternalModelTypeDef

### modelEndpoint
- **Type**: typing.Optional[str]

### modelSource
- **Type**: typing.Optional[typing.Literal['SAGEMAKER']]

### invokeModelEndpointRoleArn
- **Type**: typing.Optional[str]

### inputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ModelInputConfigurationTypeDef]

### outputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ModelOutputConfigurationOutputTypeDef]

### modelEndpointStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'DISSOCIATED']]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# FieldValidationMessageTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileValidationMessageTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterConditionTypeDef

### value
- **Type**: typing.Optional[str]


# GetBatchImportJobsRequestTypeDef

### jobId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetBatchImportJobsResultTypeDef

### batchImports
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.BatchImportTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetBatchPredictionJobsRequestTypeDef

### jobId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetBatchPredictionJobsResultTypeDef

### batchPredictions
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.BatchPredictionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetDeleteEventsByEventTypeStatusRequestTypeDef

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeleteEventsByEventTypeStatusResultTypeDef

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### eventsDeletionStatus
- **Type**: typing.Literal['CANCELED', 'CANCEL_IN_PROGRESS', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'IN_PROGRESS_INITIALIZING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDetectorVersionRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDetectorVersionResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ModelVersionTypeDef]
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDetectorsRequestTypeDef

### detectorId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetDetectorsResultTypeDef

### detectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.DetectorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEntityTypesRequestTypeDef

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEntityTypesResultTypeDef

### entityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.EntityTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetEventPredictionMetadataRequestTypeDef

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


# GetEventPredictionMetadataResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.EventVariableSummaryTypeDef]
- **Required**: Yes

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.EvaluatedRuleTypeDef]
- **Required**: Yes

### ruleExecutionMode
- **Type**: typing.Literal['ALL_MATCHED', 'FIRST_MATCHED']
- **Required**: Yes

### outcomes
- **Type**: typing.List[str]
- **Required**: Yes

### evaluatedModelVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.EvaluatedModelVersionTypeDef]
- **Required**: Yes

### evaluatedExternalModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.EvaluatedExternalModelTypeDef]
- **Required**: Yes

### predictionTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventPredictionRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.EntityTypeDef]
- **Required**: Yes

### eventTimestamp
- **Type**: <class 'str'>
- **Required**: Yes

### eventVariables
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### detectorVersionId
- **Type**: typing.Optional[str]

### externalModelEndpointDataBlobs
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.frauddetector_classes.ModelEndpointDataBlobTypeDef]]


# GetEventPredictionResultTypeDef

### modelScores
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ModelScoresTypeDef]
- **Required**: Yes

### ruleResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.RuleResultTypeDef]
- **Required**: Yes

### externalModelOutputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ExternalModelOutputsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventRequestTypeDef

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventResultTypeDef

### event
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.EventTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventTypesRequestTypeDef

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetEventTypesResultTypeDef

### eventTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.EventTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetExternalModelsRequestTypeDef

### modelEndpoint
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetExternalModelsResultTypeDef

### externalModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ExternalModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetKMSEncryptionKeyResultTypeDef

### kmsKey
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.KMSKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLabelsRequestTypeDef

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetLabelsResultTypeDef

### labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.LabelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetListElementsRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetListElementsResultTypeDef

### elements
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetListsMetadataRequestTypeDef

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetListsMetadataResultTypeDef

### lists
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.AllowDenyListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetModelVersionRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes


# GetModelVersionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.TrainingDataSchemaOutputTypeDef'>
- **Required**: Yes

### externalEventsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ExternalEventsDetailTypeDef'>
- **Required**: Yes

### ingestedEventsDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.IngestedEventsDetailTypeDef'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelsRequestTypeDef

### modelId
- **Type**: typing.Optional[str]

### modelType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetModelsResultTypeDef

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetOutcomesRequestTypeDef

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetOutcomesResultTypeDef

### outcomes
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.OutcomeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetRulesRequestTypeDef

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


# GetRulesResultTypeDef

### ruleDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.RuleDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetVariablesRequestTypeDef

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetVariablesResultTypeDef

### variables
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.VariableTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# IngestedEventStatisticsTypeDef

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


# IngestedEventsDetailTypeDef

### ingestedEventsTimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.IngestedEventsTimeWindowTypeDef'>
- **Required**: Yes


# IngestedEventsTimeWindowTypeDef

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'str'>
- **Required**: Yes


# KMSKeyTypeDef

### kmsEncryptionKeyArn
- **Type**: typing.Optional[str]


# LabelSchemaOutputTypeDef

### labelMapper
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### unlabeledEventsTreatment
- **Type**: typing.Optional[typing.Literal['AUTO', 'FRAUD', 'IGNORE', 'LEGIT']]


# LabelSchemaTypeDef

### labelMapper
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]

### unlabeledEventsTreatment
- **Type**: typing.Optional[typing.Literal['AUTO', 'FRAUD', 'IGNORE', 'LEGIT']]


# LabelTypeDef

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


# ListEventPredictionsRequestTypeDef

### eventId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.FilterConditionTypeDef]

### eventType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.FilterConditionTypeDef]

### detectorId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.FilterConditionTypeDef]

### detectorVersionId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.FilterConditionTypeDef]

### predictionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.PredictionTimeRangeTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEventPredictionsResultTypeDef

### eventPredictionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.EventPredictionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceResultTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogOddsMetricTypeDef

### variableName
- **Type**: <class 'str'>
- **Required**: Yes

### variableType
- **Type**: <class 'str'>
- **Required**: Yes

### variableImportance
- **Type**: <class 'float'>
- **Required**: Yes


# MetricDataPointTypeDef

### fpr
- **Type**: typing.Optional[float]

### precision
- **Type**: typing.Optional[float]

### tpr
- **Type**: typing.Optional[float]

### threshold
- **Type**: typing.Optional[float]


# ModelEndpointDataBlobTypeDef

### byteBuffer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.BlobTypeDef]

### contentType
- **Type**: typing.Optional[str]


# ModelInputConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelOutputConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelOutputConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelScoresTypeDef

### modelVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ModelVersionTypeDef]

### scores
- **Type**: typing.Optional[typing.Dict[str, float]]


# ModelTypeDef

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


# ModelVersionDetailTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.TrainingDataSchemaOutputTypeDef]

### externalEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ExternalEventsDetailTypeDef]

### ingestedEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.IngestedEventsDetailTypeDef]

### trainingResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.TrainingResultTypeDef]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### trainingResultV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.TrainingResultV2TypeDef]


# ModelVersionEvaluationTypeDef

### outputVariableName
- **Type**: typing.Optional[str]

### evaluationScore
- **Type**: typing.Optional[str]

### predictionExplanations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.PredictionExplanationsTypeDef]


# ModelVersionTypeDef

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


# OFIMetricDataPointTypeDef

### fpr
- **Type**: typing.Optional[float]

### precision
- **Type**: typing.Optional[float]

### tpr
- **Type**: typing.Optional[float]

### threshold
- **Type**: typing.Optional[float]


# OFIModelPerformanceTypeDef

### auc
- **Type**: typing.Optional[float]

### uncertaintyRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.UncertaintyRangeTypeDef]


# OFITrainingMetricsValueTypeDef

### metricDataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.OFIMetricDataPointTypeDef]]

### modelPerformance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.OFIModelPerformanceTypeDef]


# OutcomeTypeDef

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


# PredictionExplanationsTypeDef

### variableImpactExplanations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.VariableImpactExplanationTypeDef]]

### aggregatedVariablesImpactExplanations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.AggregatedVariablesImpactExplanationTypeDef]]


# PredictionTimeRangeTypeDef

### startTime
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: <class 'str'>
- **Required**: Yes


# PutDetectorRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# PutEntityTypeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# PutEventTypeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### eventVariables
- **Type**: typing.Sequence[str]
- **Required**: Yes

### entityTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### labels
- **Type**: typing.Optional[typing.Sequence[str]]

### eventIngestion
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]

### eventOrchestration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.EventOrchestrationTypeDef]


# PutExternalModelRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ModelInputConfigurationTypeDef'>
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ModelOutputConfigurationUnionTypeDef'>
- **Required**: Yes

### modelEndpointStatus
- **Type**: typing.Literal['ASSOCIATED', 'DISSOCIATED']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# PutKMSEncryptionKeyRequestTypeDef

### kmsEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutLabelRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# PutOutcomeRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


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


# RuleDetailTypeDef

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


# RuleResultTypeDef

### ruleId
- **Type**: typing.Optional[str]

### outcomes
- **Type**: typing.Optional[typing.List[str]]


# RuleTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ruleId
- **Type**: <class 'str'>
- **Required**: Yes

### ruleVersion
- **Type**: <class 'str'>
- **Required**: Yes


# SendEventRequestTypeDef

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
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### entities
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.EntityTypeDef]
- **Required**: Yes

### assignedLabel
- **Type**: typing.Optional[str]

### labelTimestamp
- **Type**: typing.Optional[str]


# TFIMetricDataPointTypeDef

### fpr
- **Type**: typing.Optional[float]

### precision
- **Type**: typing.Optional[float]

### tpr
- **Type**: typing.Optional[float]

### threshold
- **Type**: typing.Optional[float]


# TFIModelPerformanceTypeDef

### auc
- **Type**: typing.Optional[float]

### uncertaintyRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.UncertaintyRangeTypeDef]


# TFITrainingMetricsValueTypeDef

### metricDataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.TFIMetricDataPointTypeDef]]

### modelPerformance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.TFIModelPerformanceTypeDef]


# TagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TrainingDataSchemaOutputTypeDef

### modelVariables
- **Type**: typing.List[str]
- **Required**: Yes

### labelSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.LabelSchemaOutputTypeDef]


# TrainingDataSchemaTypeDef

### modelVariables
- **Type**: typing.Sequence[str]
- **Required**: Yes

### labelSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.LabelSchemaTypeDef]


# TrainingDataSchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrainingMetricsTypeDef

### auc
- **Type**: typing.Optional[float]

### metricDataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.MetricDataPointTypeDef]]


# TrainingMetricsV2TypeDef

### ofi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.OFITrainingMetricsValueTypeDef]

### tfi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.TFITrainingMetricsValueTypeDef]

### ati
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ATITrainingMetricsValueTypeDef]


# TrainingResultTypeDef

### dataValidationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.DataValidationMetricsTypeDef]

### trainingMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.TrainingMetricsTypeDef]

### variableImportanceMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.VariableImportanceMetricsTypeDef]


# TrainingResultV2TypeDef

### dataValidationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.DataValidationMetricsTypeDef]

### trainingMetricsV2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.TrainingMetricsV2TypeDef]

### variableImportanceMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.VariableImportanceMetricsTypeDef]

### aggregatedVariablesImportanceMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.AggregatedVariablesImportanceMetricsTypeDef]


# UncertaintyRangeTypeDef

### lowerBoundValue
- **Type**: <class 'float'>
- **Required**: Yes

### upperBoundValue
- **Type**: <class 'float'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDetectorVersionMetadataRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDetectorVersionRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### externalModelEndpoints
- **Type**: typing.Sequence[str]
- **Required**: Yes

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### modelVersions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.ModelVersionTypeDef]]

### ruleExecutionMode
- **Type**: typing.Optional[typing.Literal['ALL_MATCHED', 'FIRST_MATCHED']]


# UpdateDetectorVersionStatusRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DRAFT', 'INACTIVE']
- **Required**: Yes


# UpdateEventLabelRequestTypeDef

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


# UpdateListRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### elements
- **Type**: typing.Optional[typing.Sequence[str]]

### description
- **Type**: typing.Optional[str]

### updateMode
- **Type**: typing.Optional[typing.Literal['APPEND', 'REMOVE', 'REPLACE']]

### variableType
- **Type**: typing.Optional[str]


# UpdateModelRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateModelVersionRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ExternalEventsDetailTypeDef]

### ingestedEventsDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.IngestedEventsDetailTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# UpdateModelVersionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateModelVersionStatusRequestTypeDef

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


# UpdateRuleMetadataRequestTypeDef

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRuleVersionRequestTypeDef

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef'>
- **Required**: Yes

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### language
- **Type**: typing.Literal['DETECTORPL']
- **Required**: Yes

### outcomes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# UpdateRuleVersionResultTypeDef

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVariableRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### variableType
- **Type**: typing.Optional[str]


# VariableEntryTypeDef

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


# VariableImpactExplanationTypeDef

### eventVariableName
- **Type**: typing.Optional[str]

### relativeImpact
- **Type**: typing.Optional[str]

### logOddsImpact
- **Type**: typing.Optional[float]


# VariableImportanceMetricsTypeDef

### logOddsMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.LogOddsMetricTypeDef]]


# VariableTypeDef

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



# frauddetector_classes

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


# BatchCreateVariableRequestRequestTypeDef

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


# BatchGetVariableRequestRequestTypeDef

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


# CancelBatchImportJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelBatchPredictionJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBatchImportJobRequestRequestTypeDef

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


# CreateBatchPredictionJobRequestRequestTypeDef

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


# CreateDetectorVersionRequestRequestTypeDef

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


# CreateListRequestRequestTypeDef

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


# CreateModelRequestRequestTypeDef

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


# CreateModelVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.TrainingDataSchemaTypeDef'>
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


# CreateRuleRequestRequestTypeDef

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


# CreateVariableRequestRequestTypeDef

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


# DeleteBatchImportJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBatchPredictionJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorRequestRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDetectorVersionRequestRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEntityTypeRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventRequestRequestTypeDef

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### deleteAuditHistory
- **Type**: typing.Optional[bool]


# DeleteEventTypeRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventsByEventTypeRequestRequestTypeDef

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


# DeleteExternalModelRequestRequestTypeDef

### modelEndpoint
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLabelRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteListRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteModelRequestRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes


# DeleteModelVersionRequestRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### modelVersionNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOutcomeRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleRequestRequestTypeDef

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef'>
- **Required**: Yes


# DeleteVariableRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDetectorRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeModelVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.ModelOutputConfigurationTypeDef]

### modelEndpointStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'DISSOCIATED']]

### lastUpdatedTime
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# FieldValidationMessageTypeDef

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


# FileValidationMessageTypeDef

### title
- **Type**: typing.Optional[str]

### content
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# FilterConditionTypeDef

### value
- **Type**: typing.Optional[str]


# GetBatchImportJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBatchPredictionJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeleteEventsByEventTypeStatusRequestRequestTypeDef

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


# GetDetectorVersionRequestRequestTypeDef

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


# GetDetectorsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEntityTypesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventPredictionMetadataRequestRequestTypeDef

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


# GetEventPredictionRequestRequestTypeDef

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


# GetEventRequestRequestTypeDef

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


# GetEventTypesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExternalModelsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKMSEncryptionKeyResultTypeDef

### kmsKey
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.KMSKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLabelsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetListElementsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetListsMetadataRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetModelVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.TrainingDataSchemaTypeDef'>
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


# GetModelsRequestRequestTypeDef

### modelId
- **Type**: typing.Optional[str]

### modelType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetModelsResultTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### models
- **Type**: typing.List[aws_resource_validator.pydantic_models.frauddetector_classes.ModelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOutcomesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRulesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVariablesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ListEventPredictionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### contentType
- **Type**: typing.Optional[str]


# ModelInputConfigurationTypeDef

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


# ModelOutputConfigurationTypeDef

### format
- **Type**: typing.Literal['APPLICATION_JSONLINES', 'TEXT_CSV']
- **Required**: Yes

### jsonKeyToVariableMap
- **Type**: typing.Optional[typing.Dict[str, str]]

### csvIndexToVariableMap
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.TrainingDataSchemaTypeDef]

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


# PutDetectorRequestRequestTypeDef

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


# PutEntityTypeRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# PutEventTypeRequestRequestTypeDef

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


# PutExternalModelRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.ModelOutputConfigurationTypeDef'>
- **Required**: Yes

### modelEndpointStatus
- **Type**: typing.Literal['ASSOCIATED', 'DISSOCIATED']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# PutKMSEncryptionKeyRequestRequestTypeDef

### kmsEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutLabelRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.frauddetector_classes.TagTypeDef]]


# PutOutcomeRequestRequestTypeDef

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


# SendEventRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# TrainingDataSchemaTypeDef

### modelVariables
- **Type**: typing.Sequence[str]
- **Required**: Yes

### labelSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.frauddetector_classes.LabelSchemaTypeDef]


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


# UntagResourceRequestRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDetectorVersionMetadataRequestRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDetectorVersionRequestRequestTypeDef

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


# UpdateDetectorVersionStatusRequestRequestTypeDef

### detectorId
- **Type**: <class 'str'>
- **Required**: Yes

### detectorVersionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DRAFT', 'INACTIVE']
- **Required**: Yes


# UpdateEventLabelRequestRequestTypeDef

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


# UpdateListRequestRequestTypeDef

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


# UpdateModelRequestRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelType
- **Type**: typing.Literal['ACCOUNT_TAKEOVER_INSIGHTS', 'ONLINE_FRAUD_INSIGHTS', 'TRANSACTION_FRAUD_INSIGHTS']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateModelVersionRequestRequestTypeDef

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


# UpdateModelVersionStatusRequestRequestTypeDef

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


# UpdateRuleMetadataRequestRequestTypeDef

### rule
- **Type**: <class 'aws_resource_validator.pydantic_models.frauddetector_classes.RuleTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRuleVersionRequestRequestTypeDef

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


# UpdateVariableRequestRequestTypeDef

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



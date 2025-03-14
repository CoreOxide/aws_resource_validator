# Evidently Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchEvaluateFeatureRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### requests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.EvaluationRequestTypeDef]
- **Required**: Yes


# BatchEvaluateFeatureResponseTypeDef

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.EvaluationResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudWatchLogsDestinationConfigTypeDef

### logGroup
- **Type**: typing.Optional[str]


# CloudWatchLogsDestinationTypeDef

### logGroup
- **Type**: typing.Optional[str]


# CreateExperimentRequestTypeDef

### metricGoals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.MetricGoalConfigTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### treatments
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.TreatmentConfigTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### onlineAbConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.OnlineAbConfigTypeDef]

### randomizationSalt
- **Type**: typing.Optional[str]

### samplingRate
- **Type**: typing.Optional[int]

### segment
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateExperimentResponseTypeDef

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ExperimentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFeatureRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### variations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.VariationConfigTypeDef]
- **Required**: Yes

### defaultVariation
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### entityOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### evaluationStrategy
- **Type**: typing.Optional[typing.Literal['ALL_RULES', 'DEFAULT_VARIATION']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFeatureResponseTypeDef

### feature
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.FeatureTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLaunchRequestTypeDef

### groups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.LaunchGroupConfigTypeDef]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### metricMonitors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.MetricMonitorConfigTypeDef]]

### randomizationSalt
- **Type**: typing.Optional[str]

### scheduledSplitsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitsLaunchConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLaunchResponseTypeDef

### launch
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.LaunchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### appConfigResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ProjectAppConfigResourceConfigTypeDef]

### dataDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ProjectDataDeliveryConfigTypeDef]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectResponseTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSegmentRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSegmentResponseTypeDef

### segment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.SegmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteExperimentRequestTypeDef

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFeatureRequestTypeDef

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLaunchRequestTypeDef

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSegmentRequestTypeDef

### segment
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateFeatureRequestTypeDef

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### evaluationContext
- **Type**: typing.Optional[str]


# EvaluateFeatureResponseTypeDef

### details
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.VariableValueTypeDef'>
- **Required**: Yes

### variation
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EvaluationRequestTypeDef

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### evaluationContext
- **Type**: typing.Optional[str]


# EvaluationResultTypeDef

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]

### project
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.VariableValueTypeDef]

### variation
- **Type**: typing.Optional[str]


# EvaluationRuleTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExperimentExecutionTypeDef

### endedTime
- **Type**: typing.Optional[datetime.datetime]

### startedTime
- **Type**: typing.Optional[datetime.datetime]


# ExperimentReportTypeDef

### content
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### reportName
- **Type**: typing.Optional[typing.Literal['BayesianInference']]

### treatmentName
- **Type**: typing.Optional[str]


# ExperimentResultsDataTypeDef

### metricName
- **Type**: typing.Optional[str]

### resultStat
- **Type**: typing.Optional[typing.Literal['ConfidenceIntervalLowerBound', 'ConfidenceIntervalUpperBound', 'Mean', 'PValue', 'TreatmentEffect']]

### treatmentName
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[float]]


# ExperimentScheduleTypeDef

### analysisCompleteTime
- **Type**: typing.Optional[datetime.datetime]


# ExperimentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FeatureSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### evaluationStrategy
- **Type**: typing.Literal['ALL_RULES', 'DEFAULT_VARIATION']
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'UPDATING']
- **Required**: Yes

### defaultVariation
- **Type**: typing.Optional[str]

### evaluationRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.EvaluationRuleTypeDef]]

### project
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# FeatureTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### evaluationStrategy
- **Type**: typing.Literal['ALL_RULES', 'DEFAULT_VARIATION']
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'UPDATING']
- **Required**: Yes

### valueType
- **Type**: typing.Literal['BOOLEAN', 'DOUBLE', 'LONG', 'STRING']
- **Required**: Yes

### variations
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.VariationTypeDef]
- **Required**: Yes

### defaultVariation
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### entityOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### evaluationRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.EvaluationRuleTypeDef]]

### project
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetExperimentRequestTypeDef

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# GetExperimentResponseTypeDef

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ExperimentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExperimentResultsRequestTypeDef

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### metricNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### treatmentNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### baseStat
- **Type**: typing.Optional[typing.Literal['Mean']]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.TimestampTypeDef]

### period
- **Type**: typing.Optional[int]

### reportNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BayesianInference']]]

### resultStats
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BaseStat', 'ConfidenceInterval', 'PValue', 'TreatmentEffect']]]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.TimestampTypeDef]


# GetExperimentResultsResponseTypeDef

### details
- **Type**: <class 'str'>
- **Required**: Yes

### reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.ExperimentReportTypeDef]
- **Required**: Yes

### resultsData
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.ExperimentResultsDataTypeDef]
- **Required**: Yes

### timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFeatureRequestTypeDef

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# GetFeatureResponseTypeDef

### feature
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.FeatureTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLaunchRequestTypeDef

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# GetLaunchResponseTypeDef

### launch
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.LaunchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProjectRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectResponseTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentRequestTypeDef

### segment
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentResponseTypeDef

### segment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.SegmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LaunchExecutionTypeDef

### endedTime
- **Type**: typing.Optional[datetime.datetime]

### startedTime
- **Type**: typing.Optional[datetime.datetime]


# LaunchGroupConfigTypeDef

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### variation
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# LaunchGroupTypeDef

### featureVariations
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# LaunchTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListExperimentsRequestPaginateTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListExperimentsRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]


# ListExperimentsResponseTypeDef

### experiments
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.ExperimentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFeaturesRequestPaginateTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListFeaturesRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFeaturesResponseTypeDef

### features
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.FeatureSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLaunchesRequestPaginateTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListLaunchesRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]


# ListLaunchesResponseTypeDef

### launches
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.LaunchTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListProjectsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsResponseTypeDef

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSegmentReferencesResponseTypeDef

### referencedBy
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.RefResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSegmentsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListSegmentsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSegmentsResponseTypeDef

### segments
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.SegmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricDefinitionConfigTypeDef

### entityIdKey
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### valueKey
- **Type**: <class 'str'>
- **Required**: Yes

### eventPattern
- **Type**: typing.Optional[str]

### unitLabel
- **Type**: typing.Optional[str]


# MetricDefinitionTypeDef

### entityIdKey
- **Type**: typing.Optional[str]

### eventPattern
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### unitLabel
- **Type**: typing.Optional[str]

### valueKey
- **Type**: typing.Optional[str]


# MetricGoalConfigTypeDef

### metricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.MetricDefinitionConfigTypeDef'>
- **Required**: Yes

### desiredChange
- **Type**: typing.Optional[typing.Literal['DECREASE', 'INCREASE']]


# MetricGoalTypeDef

### metricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.MetricDefinitionTypeDef'>
- **Required**: Yes

### desiredChange
- **Type**: typing.Optional[typing.Literal['DECREASE', 'INCREASE']]


# MetricMonitorConfigTypeDef

### metricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.MetricDefinitionConfigTypeDef'>
- **Required**: Yes


# MetricMonitorTypeDef

### metricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.MetricDefinitionTypeDef'>
- **Required**: Yes


# OnlineAbConfigTypeDef

### controlTreatmentName
- **Type**: typing.Optional[str]

### treatmentWeights
- **Type**: typing.Optional[typing.Mapping[str, int]]


# OnlineAbDefinitionTypeDef

### controlTreatmentName
- **Type**: typing.Optional[str]

### treatmentWeights
- **Type**: typing.Optional[typing.Dict[str, int]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProjectAppConfigResourceConfigTypeDef

### applicationId
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]


# ProjectAppConfigResourceTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### configurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# ProjectDataDeliveryConfigTypeDef

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.CloudWatchLogsDestinationConfigTypeDef]

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.S3DestinationConfigTypeDef]


# ProjectDataDeliveryTypeDef

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.CloudWatchLogsDestinationTypeDef]

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.S3DestinationTypeDef]


# ProjectSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'UPDATING']
- **Required**: Yes

### activeExperimentCount
- **Type**: typing.Optional[int]

### activeLaunchCount
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### experimentCount
- **Type**: typing.Optional[int]

### featureCount
- **Type**: typing.Optional[int]

### launchCount
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProjectTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'UPDATING']
- **Required**: Yes

### activeExperimentCount
- **Type**: typing.Optional[int]

### activeLaunchCount
- **Type**: typing.Optional[int]

### appConfigResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ProjectAppConfigResourceTypeDef]

### dataDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ProjectDataDeliveryTypeDef]

### description
- **Type**: typing.Optional[str]

### experimentCount
- **Type**: typing.Optional[int]

### featureCount
- **Type**: typing.Optional[int]

### launchCount
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutProjectEventsRequestTypeDef

### events
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.EventTypeDef]
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# PutProjectEventsResponseTypeDef

### eventResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.PutProjectEventsResultEntryTypeDef]
- **Required**: Yes

### failedEventCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutProjectEventsResultEntryTypeDef

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]


# RefResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# S3DestinationConfigTypeDef

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# S3DestinationTypeDef

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ScheduledSplitConfigTypeDef

### groupWeights
- **Type**: typing.Mapping[str, int]
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.TimestampTypeDef'>
- **Required**: Yes

### segmentOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.SegmentOverrideUnionTypeDef]]


# ScheduledSplitTypeDef

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### groupWeights
- **Type**: typing.Optional[typing.Dict[str, int]]

### segmentOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.SegmentOverrideOutputTypeDef]]


# ScheduledSplitsLaunchConfigTypeDef

### steps
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitConfigTypeDef]
- **Required**: Yes


# ScheduledSplitsLaunchDefinitionTypeDef

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitTypeDef]]


# SegmentOverrideOutputTypeDef

### evaluationOrder
- **Type**: <class 'int'>
- **Required**: Yes

### segment
- **Type**: <class 'str'>
- **Required**: Yes

### weights
- **Type**: typing.Dict[str, int]
- **Required**: Yes


# SegmentOverrideTypeDef

### evaluationOrder
- **Type**: <class 'int'>
- **Required**: Yes

### segment
- **Type**: <class 'str'>
- **Required**: Yes

### weights
- **Type**: typing.Mapping[str, int]
- **Required**: Yes


# SegmentOverrideUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SegmentTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### experimentCount
- **Type**: typing.Optional[int]

### launchCount
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartExperimentRequestTypeDef

### analysisCompleteTime
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.TimestampTypeDef'>
- **Required**: Yes

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# StartExperimentResponseTypeDef

### startedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartLaunchRequestTypeDef

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# StartLaunchResponseTypeDef

### launch
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.LaunchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopExperimentRequestTypeDef

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### desiredState
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED']]

### reason
- **Type**: typing.Optional[str]


# StopExperimentResponseTypeDef

### endedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopLaunchRequestTypeDef

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### desiredState
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED']]

### reason
- **Type**: typing.Optional[str]


# StopLaunchResponseTypeDef

### endedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestSegmentPatternRequestTypeDef

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'str'>
- **Required**: Yes


# TestSegmentPatternResponseTypeDef

### match
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TreatmentConfigTypeDef

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### variation
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# TreatmentTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### featureVariations
- **Type**: typing.Optional[typing.Dict[str, str]]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateExperimentRequestTypeDef

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### metricGoals
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.MetricGoalConfigTypeDef]]

### onlineAbConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.OnlineAbConfigTypeDef]

### randomizationSalt
- **Type**: typing.Optional[str]

### removeSegment
- **Type**: typing.Optional[bool]

### samplingRate
- **Type**: typing.Optional[int]

### segment
- **Type**: typing.Optional[str]

### treatments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.TreatmentConfigTypeDef]]


# UpdateExperimentResponseTypeDef

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ExperimentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFeatureRequestTypeDef

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### addOrUpdateVariations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.VariationConfigTypeDef]]

### defaultVariation
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### entityOverrides
- **Type**: typing.Optional[typing.Mapping[str, str]]

### evaluationStrategy
- **Type**: typing.Optional[typing.Literal['ALL_RULES', 'DEFAULT_VARIATION']]

### removeVariations
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateFeatureResponseTypeDef

### feature
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.FeatureTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLaunchRequestTypeDef

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### groups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.LaunchGroupConfigTypeDef]]

### metricMonitors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.MetricMonitorConfigTypeDef]]

### randomizationSalt
- **Type**: typing.Optional[str]

### scheduledSplitsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitsLaunchConfigTypeDef]


# UpdateLaunchResponseTypeDef

### launch
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.LaunchTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectDataDeliveryRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.CloudWatchLogsDestinationConfigTypeDef]

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.S3DestinationConfigTypeDef]


# UpdateProjectDataDeliveryResponseTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### appConfigResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ProjectAppConfigResourceConfigTypeDef]

### description
- **Type**: typing.Optional[str]


# UpdateProjectResponseTypeDef

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ProjectTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VariableValueTypeDef

### boolValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### longValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]


# VariationConfigTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.VariableValueTypeDef'>
- **Required**: Yes


# VariationTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.VariableValueTypeDef]



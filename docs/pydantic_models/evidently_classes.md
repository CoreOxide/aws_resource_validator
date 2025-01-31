# evidently_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchEvaluateFeatureRequestRequestTypeDef

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


# CreateExperimentRequestRequestTypeDef

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


# CreateFeatureRequestRequestTypeDef

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


# CreateLaunchRequestRequestTypeDef

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


# CreateProjectRequestRequestTypeDef

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


# CreateSegmentRequestRequestTypeDef

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


# DeleteExperimentRequestRequestTypeDef

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFeatureRequestRequestTypeDef

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLaunchRequestRequestTypeDef

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectRequestRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSegmentRequestRequestTypeDef

### segment
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateFeatureRequestRequestTypeDef

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

### type
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# EventTypeDef

### data
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### type
- **Type**: typing.Literal['aws.evidently.custom', 'aws.evidently.evaluation']
- **Required**: Yes


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
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### type
- **Type**: typing.Literal['aws.evidently.onlineab']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ExperimentExecutionTypeDef]

### metricGoals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.MetricGoalTypeDef]]

### onlineAbDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.OnlineAbDefinitionTypeDef]

### project
- **Type**: typing.Optional[str]

### randomizationSalt
- **Type**: typing.Optional[str]

### samplingRate
- **Type**: typing.Optional[int]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ExperimentScheduleTypeDef]

### segment
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### treatments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.TreatmentTypeDef]]


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


# GetExperimentRequestRequestTypeDef

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


# GetExperimentResultsRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### period
- **Type**: typing.Optional[int]

### reportNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BayesianInference']]]

### resultStats
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BaseStat', 'ConfidenceInterval', 'PValue', 'TreatmentEffect']]]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# GetFeatureRequestRequestTypeDef

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


# GetLaunchRequestRequestTypeDef

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


# GetProjectRequestRequestTypeDef

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


# GetSegmentRequestRequestTypeDef

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


# LaunchPaginatorTypeDef

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
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### type
- **Type**: typing.Literal['aws.evidently.splits']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.LaunchExecutionTypeDef]

### groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.LaunchGroupTypeDef]]

### metricMonitors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.MetricMonitorTypeDef]]

### project
- **Type**: typing.Optional[str]

### randomizationSalt
- **Type**: typing.Optional[str]

### scheduledSplitsDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitsLaunchDefinitionPaginatorTypeDef]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# LaunchTypeDef

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
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### type
- **Type**: typing.Literal['aws.evidently.splits']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### execution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.LaunchExecutionTypeDef]

### groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.LaunchGroupTypeDef]]

### metricMonitors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.MetricMonitorTypeDef]]

### project
- **Type**: typing.Optional[str]

### randomizationSalt
- **Type**: typing.Optional[str]

### scheduledSplitsDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitsLaunchDefinitionTypeDef]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListExperimentsRequestListExperimentsPaginateTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListExperimentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFeaturesRequestListFeaturesPaginateTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListFeaturesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLaunchesRequestListLaunchesPaginateTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListLaunchesRequestRequestTypeDef

### project
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]


# ListLaunchesResponsePaginatorTypeDef

### launches
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.LaunchPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLaunchesResponseTypeDef

### launches
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.LaunchTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsRequestListProjectsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef

### segment
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EXPERIMENT', 'LAUNCH']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListSegmentReferencesRequestRequestTypeDef

### segment
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EXPERIMENT', 'LAUNCH']
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSegmentReferencesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### referencedBy
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.RefResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSegmentsRequestListSegmentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently_classes.PaginatorConfigTypeDef]


# ListSegmentsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSegmentsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### segments
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently_classes.SegmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# PutProjectEventsRequestRequestTypeDef

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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[str]

### lastUpdatedOn
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]


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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### segmentOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.SegmentOverrideTypeDef]]


# ScheduledSplitPaginatorTypeDef

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### groupWeights
- **Type**: typing.Optional[typing.Dict[str, int]]

### segmentOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.SegmentOverridePaginatorTypeDef]]


# ScheduledSplitTypeDef

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### groupWeights
- **Type**: typing.Optional[typing.Dict[str, int]]

### segmentOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.SegmentOverrideTypeDef]]


# ScheduledSplitsLaunchConfigTypeDef

### steps
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitConfigTypeDef]
- **Required**: Yes


# ScheduledSplitsLaunchDefinitionPaginatorTypeDef

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitPaginatorTypeDef]]


# ScheduledSplitsLaunchDefinitionTypeDef

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently_classes.ScheduledSplitTypeDef]]


# SegmentOverridePaginatorTypeDef

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


# StartExperimentRequestRequestTypeDef

### analysisCompleteTime
- **Type**: typing.Union[datetime.datetime, str]
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


# StartLaunchRequestRequestTypeDef

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


# StopExperimentRequestRequestTypeDef

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


# StopLaunchRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestSegmentPatternRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateExperimentRequestRequestTypeDef

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


# UpdateFeatureRequestRequestTypeDef

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


# UpdateLaunchRequestRequestTypeDef

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


# UpdateProjectDataDeliveryRequestRequestTypeDef

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


# UpdateProjectRequestRequestTypeDef

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



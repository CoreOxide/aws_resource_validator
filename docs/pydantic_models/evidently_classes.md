# Evidently Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchEvaluateFeatureRequest

### project
- **Type**: <class 'str'>
- **Required**: Yes

### requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.EvaluationRequest]
- **Required**: Yes


# BatchEvaluateFeatureResponse

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.EvaluationResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# CloudWatchLogsDestination

### logGroup
- **Type**: typing.Optional[str]


# CloudWatchLogsDestinationConfig

### logGroup
- **Type**: typing.Optional[str]


# CreateExperimentRequest

### metricGoals
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricGoalConfig]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### treatments
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.TreatmentConfig]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### onlineAbConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.OnlineAbConfig]

### randomizationSalt
- **Type**: typing.Optional[str]

### samplingRate
- **Type**: typing.Optional[int]

### segment
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFeatureRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### variations
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.VariationConfig]
- **Required**: Yes

### defaultVariation
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### entityOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### evaluationStrategy
- **Type**: typing.Optional[typing.Literal['ALL_RULES', 'DEFAULT_VARIATION']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateFeatureResponse

### feature
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Feature'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLaunchRequest

### groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.LaunchGroupConfig]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricMonitorConfig]]

### randomizationSalt
- **Type**: typing.Optional[str]

### scheduledSplitsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ScheduledSplitsLaunchConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLaunchResponse

### launch
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Launch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### appConfigResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ProjectAppConfigResourceConfig]

### dataDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ProjectDataDeliveryConfig]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateProjectResponse

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSegmentRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSegmentResponse

### segment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Segment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteExperimentRequest

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFeatureRequest

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLaunchRequest

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectRequest

### project
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSegmentRequest

### segment
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateFeatureRequest

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


# EvaluateFeatureResponse

### details
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.VariableValue'>
- **Required**: Yes

### variation
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# EvaluationRequest

### entityId
- **Type**: <class 'str'>
- **Required**: Yes

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### evaluationContext
- **Type**: typing.Optional[str]


# EvaluationResult

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.VariableValue]

### variation
- **Type**: typing.Optional[str]


# EvaluationRule

### type
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# Event

### data
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### type
- **Type**: typing.Literal['aws.evidently.custom', 'aws.evidently.evaluation']
- **Required**: Yes


# Experiment

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ExperimentExecution]

### metricGoals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricGoal]]

### onlineAbDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.OnlineAbDefinition]

### project
- **Type**: typing.Optional[str]

### randomizationSalt
- **Type**: typing.Optional[str]

### samplingRate
- **Type**: typing.Optional[int]

### schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ExperimentSchedule]

### segment
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### treatments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.Treatment]]


# ExperimentExecution

### endedTime
- **Type**: typing.Optional[datetime.datetime]

### startedTime
- **Type**: typing.Optional[datetime.datetime]


# ExperimentReport

### content
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### reportName
- **Type**: typing.Optional[typing.Literal['BayesianInference']]

### treatmentName
- **Type**: typing.Optional[str]


# ExperimentResultsData

### metricName
- **Type**: typing.Optional[str]

### resultStat
- **Type**: typing.Optional[typing.Literal['ConfidenceIntervalLowerBound', 'ConfidenceIntervalUpperBound', 'Mean', 'PValue', 'TreatmentEffect']]

### treatmentName
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[float]]


# ExperimentSchedule

### analysisCompleteTime
- **Type**: typing.Optional[datetime.datetime]


# Feature

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.Variation]
- **Required**: Yes

### defaultVariation
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### entityOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### evaluationRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.EvaluationRule]]

### project
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# FeatureSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.EvaluationRule]]

### project
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetExperimentRequest

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# GetExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# GetExperimentResultsRequest

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### metricNames
- **Type**: typing.List[str]
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### treatmentNames
- **Type**: typing.List[str]
- **Required**: Yes

### baseStat
- **Type**: typing.Optional[typing.Literal['Mean']]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### period
- **Type**: typing.Optional[int]

### reportNames
- **Type**: typing.Optional[typing.List[typing.Literal['BayesianInference']]]

### resultStats
- **Type**: typing.Optional[typing.List[typing.Literal['BaseStat', 'ConfidenceInterval', 'PValue', 'TreatmentEffect']]]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# GetExperimentResultsResponse

### details
- **Type**: <class 'str'>
- **Required**: Yes

### reports
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.ExperimentReport]
- **Required**: Yes

### resultsData
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.ExperimentResultsData]
- **Required**: Yes

### timestamps
- **Type**: typing.List[datetime.datetime]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# GetFeatureRequest

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# GetFeatureResponse

### feature
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Feature'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# GetLaunchRequest

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# GetLaunchResponse

### launch
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Launch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# GetProjectRequest

### project
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectResponse

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentRequest

### segment
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentResponse

### segment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Segment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# Launch

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.LaunchExecution]

### groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.LaunchGroup]]

### metricMonitors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricMonitor]]

### project
- **Type**: typing.Optional[str]

### randomizationSalt
- **Type**: typing.Optional[str]

### scheduledSplitsDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ScheduledSplitsLaunchDefinition]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# LaunchExecution

### endedTime
- **Type**: typing.Optional[datetime.datetime]

### startedTime
- **Type**: typing.Optional[datetime.datetime]


# LaunchGroup

### featureVariations
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# LaunchGroupConfig

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


# ListExperimentsRequest

### project
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]


# ListExperimentsRequestPaginate

### project
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.PaginatorConfig]


# ListExperimentsResponse

### experiments
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.Experiment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFeaturesRequest

### project
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFeaturesRequestPaginate

### project
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.PaginatorConfig]


# ListFeaturesResponse

### features
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.FeatureSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListLaunchesRequest

### project
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]


# ListLaunchesRequestPaginate

### project
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'CREATED', 'RUNNING', 'UPDATING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.PaginatorConfig]


# ListLaunchesResponse

### launches
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.Launch]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.PaginatorConfig]


# ListProjectsResponse

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.ProjectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSegmentReferencesRequest

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


# ListSegmentReferencesRequestPaginate

### segment
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EXPERIMENT', 'LAUNCH']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.PaginatorConfig]


# ListSegmentReferencesResponse

### referencedBy
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.RefResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSegmentsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSegmentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.PaginatorConfig]


# ListSegmentsResponse

### segments
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.Segment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# MetricDefinition

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


# MetricDefinitionConfig

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


# MetricGoal

### metricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricDefinition'>
- **Required**: Yes

### desiredChange
- **Type**: typing.Optional[typing.Literal['DECREASE', 'INCREASE']]


# MetricGoalConfig

### metricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricDefinitionConfig'>
- **Required**: Yes

### desiredChange
- **Type**: typing.Optional[typing.Literal['DECREASE', 'INCREASE']]


# MetricMonitor

### metricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricDefinition'>
- **Required**: Yes


# MetricMonitorConfig

### metricDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricDefinitionConfig'>
- **Required**: Yes


# OnlineAbConfig

### controlTreatmentName
- **Type**: typing.Optional[str]

### treatmentWeights
- **Type**: typing.Optional[typing.Dict[str, int]]


# OnlineAbDefinition

### controlTreatmentName
- **Type**: typing.Optional[str]

### treatmentWeights
- **Type**: typing.Optional[typing.Dict[str, int]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Project

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ProjectAppConfigResource]

### dataDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ProjectDataDelivery]

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


# ProjectAppConfigResource

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### configurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentId
- **Type**: <class 'str'>
- **Required**: Yes


# ProjectAppConfigResourceConfig

### applicationId
- **Type**: typing.Optional[str]

### environmentId
- **Type**: typing.Optional[str]


# ProjectDataDelivery

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.CloudWatchLogsDestination]

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.S3Destination]


# ProjectDataDeliveryConfig

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.CloudWatchLogsDestinationConfig]

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.S3DestinationConfig]


# ProjectSummary

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


# PutProjectEventsRequest

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.Event]
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# PutProjectEventsResponse

### eventResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.PutProjectEventsResultEntry]
- **Required**: Yes

### failedEventCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# PutProjectEventsResultEntry

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]

### eventId
- **Type**: typing.Optional[str]


# RefResource

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


# S3Destination

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# S3DestinationConfig

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ScheduledSplit

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### groupWeights
- **Type**: typing.Optional[typing.Dict[str, int]]

### segmentOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.SegmentOverrideOutput]]


# ScheduledSplitConfig

### groupWeights
- **Type**: typing.Dict[str, int]
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### segmentOverrides
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.evidently.evidently_classes.SegmentOverride, aws_resource_validator.pydantic_models.evidently.evidently_classes.SegmentOverrideOutput]]]


# ScheduledSplitsLaunchConfig

### steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.ScheduledSplitConfig]
- **Required**: Yes


# ScheduledSplitsLaunchDefinition

### steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.ScheduledSplit]]


# Segment

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


# SegmentOverride

### evaluationOrder
- **Type**: <class 'int'>
- **Required**: Yes

### segment
- **Type**: <class 'str'>
- **Required**: Yes

### weights
- **Type**: typing.Dict[str, int]
- **Required**: Yes


# SegmentOverrideOutput

### evaluationOrder
- **Type**: <class 'int'>
- **Required**: Yes

### segment
- **Type**: <class 'str'>
- **Required**: Yes

### weights
- **Type**: typing.Dict[str, int]
- **Required**: Yes


# StartExperimentRequest

### analysisCompleteTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# StartExperimentResponse

### startedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# StartLaunchRequest

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes


# StartLaunchResponse

### launch
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Launch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# StopExperimentRequest

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


# StopExperimentResponse

### endedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# StopLaunchRequest

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


# StopLaunchResponse

### endedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TestSegmentPatternRequest

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'str'>
- **Required**: Yes


# TestSegmentPatternResponse

### match
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# Treatment

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### featureVariations
- **Type**: typing.Optional[typing.Dict[str, str]]


# TreatmentConfig

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


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateExperimentRequest

### experiment
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### metricGoals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricGoalConfig]]

### onlineAbConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.OnlineAbConfig]

### randomizationSalt
- **Type**: typing.Optional[str]

### removeSegment
- **Type**: typing.Optional[bool]

### samplingRate
- **Type**: typing.Optional[int]

### segment
- **Type**: typing.Optional[str]

### treatments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.TreatmentConfig]]


# UpdateExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFeatureRequest

### feature
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### addOrUpdateVariations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.VariationConfig]]

### defaultVariation
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### entityOverrides
- **Type**: typing.Optional[typing.Dict[str, str]]

### evaluationStrategy
- **Type**: typing.Optional[typing.Literal['ALL_RULES', 'DEFAULT_VARIATION']]

### removeVariations
- **Type**: typing.Optional[typing.List[str]]


# UpdateFeatureResponse

### feature
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Feature'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLaunchRequest

### launch
- **Type**: <class 'str'>
- **Required**: Yes

### project
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.LaunchGroupConfig]]

### metricMonitors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.evidently.evidently_classes.MetricMonitorConfig]]

### randomizationSalt
- **Type**: typing.Optional[str]

### scheduledSplitsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ScheduledSplitsLaunchConfig]


# UpdateLaunchResponse

### launch
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Launch'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectDataDeliveryRequest

### project
- **Type**: <class 'str'>
- **Required**: Yes

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.CloudWatchLogsDestinationConfig]

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.S3DestinationConfig]


# UpdateProjectDataDeliveryResponse

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProjectRequest

### project
- **Type**: <class 'str'>
- **Required**: Yes

### appConfigResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.ProjectAppConfigResourceConfig]

### description
- **Type**: typing.Optional[str]


# UpdateProjectResponse

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.Project'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.ResponseMetadata'>
- **Required**: Yes


# VariableValue

### boolValue
- **Type**: typing.Optional[bool]

### doubleValue
- **Type**: typing.Optional[float]

### longValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]


# Variation

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.evidently.evidently_classes.VariableValue]


# VariationConfig

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.evidently.evidently_classes.VariableValue'>
- **Required**: Yes



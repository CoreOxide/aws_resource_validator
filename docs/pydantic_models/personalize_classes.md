# Personalize Classes

# Algorithm

### name
- **Type**: typing.Optional[str]

### algorithmArn
- **Type**: typing.Optional[str]

### algorithmImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.AlgorithmImage]

### defaultHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### defaultHyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.DefaultHyperParameterRanges]

### defaultResourceConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### trainingInputMode
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# AlgorithmImage

### dockerURI
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# AutoMLConfig

### metricName
- **Type**: typing.Optional[str]

### recipeList
- **Type**: typing.Optional[typing.List[str]]


# AutoMLConfigOutput

### metricName
- **Type**: typing.Optional[str]

### recipeList
- **Type**: typing.Optional[typing.List[str]]


# AutoMLResult

### bestRecipeArn
- **Type**: typing.Optional[str]


# AutoTrainingConfig

### schedulingExpression
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchInferenceJob

### jobName
- **Type**: typing.Optional[str]

### batchInferenceJobArn
- **Type**: typing.Optional[str]

### filterArn
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### solutionVersionArn
- **Type**: typing.Optional[str]

### numResults
- **Type**: typing.Optional[int]

### jobInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJobInput]

### jobOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJobOutput]

### batchInferenceJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJobConfigOutput]

### roleArn
- **Type**: typing.Optional[str]

### batchInferenceJobMode
- **Type**: typing.Optional[typing.Literal['BATCH_INFERENCE', 'THEME_GENERATION']]

### themeGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.ThemeGenerationConfig]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# BatchInferenceJobConfig

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]


# BatchInferenceJobConfigOutput

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]


# BatchInferenceJobInput

### s3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.S3DataConfig'>
- **Required**: Yes


# BatchInferenceJobOutput

### s3DataDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.S3DataConfig'>
- **Required**: Yes


# BatchInferenceJobSummary

### batchInferenceJobArn
- **Type**: typing.Optional[str]

### jobName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]

### solutionVersionArn
- **Type**: typing.Optional[str]

### batchInferenceJobMode
- **Type**: typing.Optional[typing.Literal['BATCH_INFERENCE', 'THEME_GENERATION']]


# BatchSegmentJob

### jobName
- **Type**: typing.Optional[str]

### batchSegmentJobArn
- **Type**: typing.Optional[str]

### filterArn
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### solutionVersionArn
- **Type**: typing.Optional[str]

### numResults
- **Type**: typing.Optional[int]

### jobInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchSegmentJobInput]

### jobOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchSegmentJobOutput]

### roleArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# BatchSegmentJobInput

### s3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.S3DataConfig'>
- **Required**: Yes


# BatchSegmentJobOutput

### s3DataDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.S3DataConfig'>
- **Required**: Yes


# BatchSegmentJobSummary

### batchSegmentJobArn
- **Type**: typing.Optional[str]

### jobName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]

### solutionVersionArn
- **Type**: typing.Optional[str]


# Campaign

### name
- **Type**: typing.Optional[str]

### campaignArn
- **Type**: typing.Optional[str]

### solutionVersionArn
- **Type**: typing.Optional[str]

### minProvisionedTPS
- **Type**: typing.Optional[int]

### campaignConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.CampaignConfigOutput]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### latestCampaignUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.CampaignUpdateSummary]


# CampaignConfig

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]

### syncWithLatestSolutionVersion
- **Type**: typing.Optional[bool]


# CampaignConfigOutput

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]

### syncWithLatestSolutionVersion
- **Type**: typing.Optional[bool]


# CampaignSummary

### name
- **Type**: typing.Optional[str]

### campaignArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# CampaignUpdateSummary

### solutionVersionArn
- **Type**: typing.Optional[str]

### minProvisionedTPS
- **Type**: typing.Optional[int]

### campaignConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.CampaignConfigOutput]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# CategoricalHyperParameterRange

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# CategoricalHyperParameterRangeOutput

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# ContinuousHyperParameterRange

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]


# CreateBatchInferenceJobRequest

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJobInput'>
- **Required**: Yes

### jobOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJobOutput'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterArn
- **Type**: typing.Optional[str]

### numResults
- **Type**: typing.Optional[int]

### batchInferenceJobConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJobConfig, aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJobConfigOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]

### batchInferenceJobMode
- **Type**: typing.Optional[typing.Literal['BATCH_INFERENCE', 'THEME_GENERATION']]

### themeGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.ThemeGenerationConfig]


# CreateBatchInferenceJobResponse

### batchInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBatchSegmentJobRequest

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchSegmentJobInput'>
- **Required**: Yes

### jobOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchSegmentJobOutput'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterArn
- **Type**: typing.Optional[str]

### numResults
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateBatchSegmentJobResponse

### batchSegmentJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCampaignRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### minProvisionedTPS
- **Type**: typing.Optional[int]

### campaignConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.personalize.personalize_classes.CampaignConfig, aws_resource_validator.pydantic_models.personalize.personalize_classes.CampaignConfigOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateCampaignResponse

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataDeletionJobRequest

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DataSource'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateDataDeletionJobResponse

### dataDeletionJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetExportJobRequest

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetExportJobOutput'>
- **Required**: Yes

### ingestionMode
- **Type**: typing.Optional[typing.Literal['ALL', 'BULK', 'PUT']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateDatasetExportJobResponse

### datasetExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetGroupRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateDatasetGroupResponse

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### domain
- **Type**: typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetImportJobRequest

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DataSource'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]

### importMode
- **Type**: typing.Optional[typing.Literal['FULL', 'INCREMENTAL']]

### publishAttributionMetricsToS3
- **Type**: typing.Optional[bool]


# CreateDatasetImportJobResponse

### datasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### datasetType
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateDatasetResponse

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventTrackerRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateEventTrackerResponse

### eventTrackerArn
- **Type**: <class 'str'>
- **Required**: Yes

### trackingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFilterRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterExpression
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateFilterResponse

### filterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMetricAttributionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.MetricAttribute]
- **Required**: Yes

### metricsOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.MetricAttributionOutput'>
- **Required**: Yes


# CreateMetricAttributionResponse

### metricAttributionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRecommenderRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### recipeArn
- **Type**: <class 'str'>
- **Required**: Yes

### recommenderConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderConfig, aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderConfigOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateRecommenderResponse

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSchemaRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.CreateSchemaRequest'>>

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# CreateSchemaResponse

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSolutionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### performHPO
- **Type**: typing.Optional[bool]

### performAutoML
- **Type**: typing.Optional[bool]

### performAutoTraining
- **Type**: typing.Optional[bool]

### recipeArn
- **Type**: typing.Optional[str]

### eventType
- **Type**: typing.Optional[str]

### solutionConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionConfig, aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionConfigOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateSolutionResponse

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSolutionVersionRequest

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### trainingMode
- **Type**: typing.Optional[typing.Literal['AUTOTRAIN', 'FULL', 'UPDATE']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]]


# CreateSolutionVersionResponse

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DataDeletionJob

### jobName
- **Type**: typing.Optional[str]

### dataDeletionJobArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.DataSource]

### roleArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### numDeleted
- **Type**: typing.Optional[int]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# DataDeletionJobSummary

### dataDeletionJobArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### jobName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# DataSource

### dataLocation
- **Type**: typing.Optional[str]


# Dataset

### name
- **Type**: typing.Optional[str]

### datasetArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### datasetType
- **Type**: typing.Optional[str]

### schemaArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### latestDatasetUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetUpdateSummary]

### trackingId
- **Type**: typing.Optional[str]


# DatasetExportJob

### jobName
- **Type**: typing.Optional[str]

### datasetExportJobArn
- **Type**: typing.Optional[str]

### datasetArn
- **Type**: typing.Optional[str]

### ingestionMode
- **Type**: typing.Optional[typing.Literal['ALL', 'BULK', 'PUT']]

### roleArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### jobOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetExportJobOutput]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# DatasetExportJobOutput

### s3DataDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.S3DataConfig'>
- **Required**: Yes


# DatasetExportJobSummary

### datasetExportJobArn
- **Type**: typing.Optional[str]

### jobName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# DatasetGroup

### name
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# DatasetGroupSummary

### name
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# DatasetImportJob

### jobName
- **Type**: typing.Optional[str]

### datasetImportJobArn
- **Type**: typing.Optional[str]

### datasetArn
- **Type**: typing.Optional[str]

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.DataSource]

### roleArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]

### importMode
- **Type**: typing.Optional[typing.Literal['FULL', 'INCREMENTAL']]

### publishAttributionMetricsToS3
- **Type**: typing.Optional[bool]


# DatasetImportJobSummary

### datasetImportJobArn
- **Type**: typing.Optional[str]

### jobName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]

### importMode
- **Type**: typing.Optional[typing.Literal['FULL', 'INCREMENTAL']]


# DatasetSchema

### name
- **Type**: typing.Optional[str]

### schemaArn
- **Type**: typing.Optional[str]

### schema
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# DatasetSchemaSummary

### name
- **Type**: typing.Optional[str]

### schemaArn
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# DatasetSummary

### name
- **Type**: typing.Optional[str]

### datasetArn
- **Type**: typing.Optional[str]

### datasetType
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# DatasetUpdateSummary

### schemaArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# DefaultCategoricalHyperParameterRange

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]

### isTunable
- **Type**: typing.Optional[bool]


# DefaultContinuousHyperParameterRange

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]

### isTunable
- **Type**: typing.Optional[bool]


# DefaultHyperParameterRanges

### integerHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DefaultIntegerHyperParameterRange]]

### continuousHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DefaultContinuousHyperParameterRange]]

### categoricalHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DefaultCategoricalHyperParameterRange]]


# DefaultIntegerHyperParameterRange

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[int]

### maxValue
- **Type**: typing.Optional[int]

### isTunable
- **Type**: typing.Optional[bool]


# DeleteCampaignRequest

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetGroupRequest

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetRequest

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventTrackerRequest

### eventTrackerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFilterRequest

### filterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMetricAttributionRequest

### metricAttributionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecommenderRequest

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaRequest

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSolutionRequest

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlgorithmRequest

### algorithmArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlgorithmResponse

### algorithm
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.Algorithm'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBatchInferenceJobRequest

### batchInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchInferenceJobResponse

### batchInferenceJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBatchSegmentJobRequest

### batchSegmentJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchSegmentJobResponse

### batchSegmentJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchSegmentJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCampaignRequest

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCampaignResponse

### campaign
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.Campaign'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataDeletionJobRequest

### dataDeletionJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataDeletionJobResponse

### dataDeletionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DataDeletionJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetExportJobRequest

### datasetExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetExportJobResponse

### datasetExportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetExportJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetGroupRequest

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetGroupResponse

### datasetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetImportJobRequest

### datasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetImportJobResponse

### datasetImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetImportJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.Dataset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventTrackerRequest

### eventTrackerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEventTrackerResponse

### eventTracker
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.EventTracker'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFeatureTransformationRequest

### featureTransformationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFeatureTransformationResponse

### featureTransformation
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.FeatureTransformation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFilterRequest

### filterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFilterResponse

### filter
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.Filter'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMetricAttributionRequest

### metricAttributionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMetricAttributionResponse

### metricAttribution
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.MetricAttribution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRecipeRequest

### recipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRecipeResponse

### recipe
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.Recipe'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRecommenderRequest

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRecommenderResponse

### recommender
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.Recommender'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSchemaRequest

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSchemaResponse

### schema
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetSchema'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.DescribeSchemaResponse'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSolutionRequest

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSolutionResponse

### solution
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.Solution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSolutionVersionRequest

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSolutionVersionResponse

### solutionVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# EventTracker

### name
- **Type**: typing.Optional[str]

### eventTrackerArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### trackingId
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# EventTrackerSummary

### name
- **Type**: typing.Optional[str]

### eventTrackerArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# FeatureTransformation

### name
- **Type**: typing.Optional[str]

### featureTransformationArn
- **Type**: typing.Optional[str]

### defaultParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[str]


# FieldsForThemeGeneration

### itemName
- **Type**: <class 'str'>
- **Required**: Yes


# Filter

### name
- **Type**: typing.Optional[str]

### filterArn
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### datasetGroupArn
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### filterExpression
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]


# FilterSummary

### name
- **Type**: typing.Optional[str]

### filterArn
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### datasetGroupArn
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]


# GetSolutionMetricsRequest

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolutionMetricsResponse

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: typing.Dict[str, float]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# HPOConfig

### hpoObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.HPOObjective]

### hpoResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.HPOResourceConfig]

### algorithmHyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.HyperParameterRanges]


# HPOConfigOutput

### hpoObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.HPOObjective]

### hpoResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.HPOResourceConfig]

### algorithmHyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.HyperParameterRangesOutput]


# HPOObjective

### type
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### metricRegex
- **Type**: typing.Optional[str]


# HPOResourceConfig

### maxNumberOfTrainingJobs
- **Type**: typing.Optional[str]

### maxParallelTrainingJobs
- **Type**: typing.Optional[str]


# HyperParameterRanges

### integerHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.IntegerHyperParameterRange]]

### continuousHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.ContinuousHyperParameterRange]]

### categoricalHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.CategoricalHyperParameterRange]]


# HyperParameterRangesOutput

### integerHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.IntegerHyperParameterRange]]

### continuousHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.ContinuousHyperParameterRange]]

### categoricalHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.CategoricalHyperParameterRangeOutput]]


# IntegerHyperParameterRange

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[int]

### maxValue
- **Type**: typing.Optional[int]


# ListBatchInferenceJobsRequest

### solutionVersionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBatchInferenceJobsRequestPaginate

### solutionVersionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListBatchInferenceJobsResponse

### batchInferenceJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchInferenceJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListBatchSegmentJobsRequest

### solutionVersionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBatchSegmentJobsRequestPaginate

### solutionVersionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListBatchSegmentJobsResponse

### batchSegmentJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.BatchSegmentJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCampaignsRequest

### solutionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCampaignsRequestPaginate

### solutionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListCampaignsResponse

### campaigns
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.CampaignSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataDeletionJobsRequest

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataDeletionJobsResponse

### dataDeletionJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DataDeletionJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetExportJobsRequest

### datasetArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetExportJobsRequestPaginate

### datasetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListDatasetExportJobsResponse

### datasetExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetGroupsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListDatasetGroupsResponse

### datasetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetImportJobsRequest

### datasetArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetImportJobsRequestPaginate

### datasetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListDatasetImportJobsResponse

### datasetImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetImportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDatasetsRequest

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsRequestPaginate

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListDatasetsResponse

### datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEventTrackersRequest

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEventTrackersRequestPaginate

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListEventTrackersResponse

### eventTrackers
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.EventTrackerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFiltersRequest

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFiltersRequestPaginate

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListFiltersResponse

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.FilterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetricAttributionMetricsRequest

### metricAttributionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMetricAttributionMetricsRequestPaginate

### metricAttributionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListMetricAttributionMetricsResponse

### metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.MetricAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMetricAttributionsRequest

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMetricAttributionsRequestPaginate

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListMetricAttributionsResponse

### metricAttributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.MetricAttributionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecipesRequest

### recipeProvider
- **Type**: typing.Optional[typing.Literal['SERVICE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# ListRecipesRequestPaginate

### recipeProvider
- **Type**: typing.Optional[typing.Literal['SERVICE']]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListRecipesResponse

### recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.RecipeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecommendersRequest

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRecommendersRequestPaginate

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListRecommendersResponse

### recommenders
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSchemasRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSchemasRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListSchemasResponse

### schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.DatasetSchemaSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolutionVersionsRequest

### solutionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSolutionVersionsRequestPaginate

### solutionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListSolutionVersionsResponse

### solutionVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSolutionsRequest

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSolutionsRequestPaginate

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.PaginatorConfig]


# ListSolutionsResponse

### solutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# MetricAttribute

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### expression
- **Type**: <class 'str'>
- **Required**: Yes


# MetricAttribution

### name
- **Type**: typing.Optional[str]

### metricAttributionArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### metricsOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.MetricAttributionOutput]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# MetricAttributionOutput

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### s3DataDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.S3DataConfig]


# MetricAttributionSummary

### name
- **Type**: typing.Optional[str]

### metricAttributionArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# OptimizationObjective

### itemAttribute
- **Type**: typing.Optional[str]

### objectiveSensitivity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'OFF']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Recipe

### name
- **Type**: typing.Optional[str]

### recipeArn
- **Type**: typing.Optional[str]

### algorithmArn
- **Type**: typing.Optional[str]

### featureTransformationArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### recipeType
- **Type**: typing.Optional[str]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# RecipeSummary

### name
- **Type**: typing.Optional[str]

### recipeArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# Recommender

### recommenderArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### recipeArn
- **Type**: typing.Optional[str]

### recommenderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderConfigOutput]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### latestRecommenderUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderUpdateSummary]

### modelMetrics
- **Type**: typing.Optional[typing.Dict[str, float]]


# RecommenderConfig

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### minRecommendationRequestsPerSecond
- **Type**: typing.Optional[int]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.TrainingDataConfig]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]


# RecommenderConfigOutput

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### minRecommendationRequestsPerSecond
- **Type**: typing.Optional[int]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.TrainingDataConfigOutput]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]


# RecommenderSummary

### name
- **Type**: typing.Optional[str]

### recommenderArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### recipeArn
- **Type**: typing.Optional[str]

### recommenderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderConfigOutput]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# RecommenderUpdateSummary

### recommenderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderConfigOutput]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[str]

### failureReason
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


# S3DataConfig

### path
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# Solution

### name
- **Type**: typing.Optional[str]

### solutionArn
- **Type**: typing.Optional[str]

### performHPO
- **Type**: typing.Optional[bool]

### performAutoML
- **Type**: typing.Optional[bool]

### performAutoTraining
- **Type**: typing.Optional[bool]

### recipeArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### eventType
- **Type**: typing.Optional[str]

### solutionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionConfigOutput]

### autoMLResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.AutoMLResult]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### latestSolutionVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionVersionSummary]

### latestSolutionUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionUpdateSummary]


# SolutionConfig

### eventValueThreshold
- **Type**: typing.Optional[str]

### hpoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.HPOConfig]

### algorithmHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### featureTransformationParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### autoMLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.AutoMLConfig]

### optimizationObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.OptimizationObjective]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.TrainingDataConfig]

### autoTrainingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.AutoTrainingConfig]


# SolutionConfigOutput

### eventValueThreshold
- **Type**: typing.Optional[str]

### hpoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.HPOConfigOutput]

### algorithmHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### featureTransformationParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### autoMLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.AutoMLConfigOutput]

### optimizationObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.OptimizationObjective]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.TrainingDataConfigOutput]

### autoTrainingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.AutoTrainingConfig]


# SolutionSummary

### name
- **Type**: typing.Optional[str]

### solutionArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### recipeArn
- **Type**: typing.Optional[str]


# SolutionUpdateConfig

### autoTrainingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.AutoTrainingConfig]


# SolutionUpdateSummary

### solutionUpdateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionUpdateConfig]

### status
- **Type**: typing.Optional[str]

### performAutoTraining
- **Type**: typing.Optional[bool]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# SolutionVersion

### name
- **Type**: typing.Optional[str]

### solutionVersionArn
- **Type**: typing.Optional[str]

### solutionArn
- **Type**: typing.Optional[str]

### performHPO
- **Type**: typing.Optional[bool]

### performAutoML
- **Type**: typing.Optional[bool]

### recipeArn
- **Type**: typing.Optional[str]

### eventType
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### solutionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionConfigOutput]

### trainingHours
- **Type**: typing.Optional[float]

### trainingMode
- **Type**: typing.Optional[typing.Literal['AUTOTRAIN', 'FULL', 'UPDATE']]

### tunedHPOParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.TunedHPOParams]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### trainingType
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]


# SolutionVersionSummary

### solutionVersionArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### trainingMode
- **Type**: typing.Optional[typing.Literal['AUTOTRAIN', 'FULL', 'UPDATE']]

### trainingType
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL']]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# StartRecommenderRequest

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartRecommenderResponse

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# StopRecommenderRequest

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopRecommenderResponse

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# StopSolutionVersionCreationRequest

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### tagKey
- **Type**: <class 'str'>
- **Required**: Yes

### tagValue
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.Tag]
- **Required**: Yes


# ThemeGenerationConfig

### fieldsForThemeGeneration
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.FieldsForThemeGeneration'>
- **Required**: Yes


# TrainingDataConfig

### excludedDatasetColumns
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# TrainingDataConfigOutput

### excludedDatasetColumns
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# TunedHPOParams

### algorithmHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateCampaignRequest

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes

### solutionVersionArn
- **Type**: typing.Optional[str]

### minProvisionedTPS
- **Type**: typing.Optional[int]

### campaignConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.personalize.personalize_classes.CampaignConfig, aws_resource_validator.pydantic_models.personalize.personalize_classes.CampaignConfigOutput, NoneType]


# UpdateCampaignResponse

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDatasetRequest

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDatasetResponse

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMetricAttributionRequest

### addMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize.personalize_classes.MetricAttribute]]

### removeMetrics
- **Type**: typing.Optional[typing.List[str]]

### metricsOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.MetricAttributionOutput]

### metricAttributionArn
- **Type**: typing.Optional[str]


# UpdateMetricAttributionResponse

### metricAttributionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRecommenderRequest

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### recommenderConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderConfig, aws_resource_validator.pydantic_models.personalize.personalize_classes.RecommenderConfigOutput]
- **Required**: Yes


# UpdateRecommenderResponse

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSolutionRequest

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### performAutoTraining
- **Type**: typing.Optional[bool]

### solutionUpdateConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize.personalize_classes.SolutionUpdateConfig]


# UpdateSolutionResponse

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize.personalize_classes.ResponseMetadata'>
- **Required**: Yes



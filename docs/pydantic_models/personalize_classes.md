# Personalize Classes

# AlgorithmImageTypeDef

### dockerURI
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]


# AlgorithmTypeDef

### name
- **Type**: typing.Optional[str]

### algorithmArn
- **Type**: typing.Optional[str]

### algorithmImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.AlgorithmImageTypeDef]

### defaultHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### defaultHyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.DefaultHyperParameterRangesTypeDef]

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


# AutoMLConfigOutputTypeDef

### metricName
- **Type**: typing.Optional[str]

### recipeList
- **Type**: typing.Optional[typing.List[str]]


# AutoMLConfigTypeDef

### metricName
- **Type**: typing.Optional[str]

### recipeList
- **Type**: typing.Optional[typing.Sequence[str]]


# AutoMLResultTypeDef

### bestRecipeArn
- **Type**: typing.Optional[str]


# AutoTrainingConfigTypeDef

### schedulingExpression
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchInferenceJobConfigOutputTypeDef

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]


# BatchInferenceJobConfigTypeDef

### itemExplorationConfig
- **Type**: typing.Optional[typing.Mapping[str, str]]


# BatchInferenceJobInputTypeDef

### s3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.S3DataConfigTypeDef'>
- **Required**: Yes


# BatchInferenceJobOutputTypeDef

### s3DataDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.S3DataConfigTypeDef'>
- **Required**: Yes


# BatchInferenceJobSummaryTypeDef

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


# BatchInferenceJobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.BatchInferenceJobInputTypeDef]

### jobOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.BatchInferenceJobOutputTypeDef]

### batchInferenceJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.BatchInferenceJobConfigOutputTypeDef]

### roleArn
- **Type**: typing.Optional[str]

### batchInferenceJobMode
- **Type**: typing.Optional[typing.Literal['BATCH_INFERENCE', 'THEME_GENERATION']]

### themeGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.ThemeGenerationConfigTypeDef]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# BatchSegmentJobInputTypeDef

### s3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.S3DataConfigTypeDef'>
- **Required**: Yes


# BatchSegmentJobOutputTypeDef

### s3DataDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.S3DataConfigTypeDef'>
- **Required**: Yes


# BatchSegmentJobSummaryTypeDef

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


# BatchSegmentJobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.BatchSegmentJobInputTypeDef]

### jobOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.BatchSegmentJobOutputTypeDef]

### roleArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# CampaignConfigOutputTypeDef

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]

### syncWithLatestSolutionVersion
- **Type**: typing.Optional[bool]


# CampaignConfigTypeDef

### itemExplorationConfig
- **Type**: typing.Optional[typing.Mapping[str, str]]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]

### syncWithLatestSolutionVersion
- **Type**: typing.Optional[bool]


# CampaignSummaryTypeDef

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


# CampaignTypeDef

### name
- **Type**: typing.Optional[str]

### campaignArn
- **Type**: typing.Optional[str]

### solutionVersionArn
- **Type**: typing.Optional[str]

### minProvisionedTPS
- **Type**: typing.Optional[int]

### campaignConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.CampaignConfigOutputTypeDef]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### latestCampaignUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.CampaignUpdateSummaryTypeDef]


# CampaignUpdateSummaryTypeDef

### solutionVersionArn
- **Type**: typing.Optional[str]

### minProvisionedTPS
- **Type**: typing.Optional[int]

### campaignConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.CampaignConfigOutputTypeDef]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# CategoricalHyperParameterRangeOutputTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# CategoricalHyperParameterRangeTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# ContinuousHyperParameterRangeTypeDef

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]


# CreateBatchInferenceJobRequestRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.BatchInferenceJobInputTypeDef'>
- **Required**: Yes

### jobOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.BatchInferenceJobOutputTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterArn
- **Type**: typing.Optional[str]

### numResults
- **Type**: typing.Optional[int]

### batchInferenceJobConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.BatchInferenceJobConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]

### batchInferenceJobMode
- **Type**: typing.Optional[typing.Literal['BATCH_INFERENCE', 'THEME_GENERATION']]

### themeGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.ThemeGenerationConfigTypeDef]


# CreateBatchInferenceJobResponseTypeDef

### batchInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBatchSegmentJobRequestRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobInput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.BatchSegmentJobInputTypeDef'>
- **Required**: Yes

### jobOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.BatchSegmentJobOutputTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### filterArn
- **Type**: typing.Optional[str]

### numResults
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateBatchSegmentJobResponseTypeDef

### batchSegmentJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCampaignRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### minProvisionedTPS
- **Type**: typing.Optional[int]

### campaignConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.CampaignConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateCampaignResponseTypeDef

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataDeletionJobRequestRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DataSourceTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateDataDeletionJobResponseTypeDef

### dataDeletionJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetExportJobRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DatasetExportJobOutputTypeDef'>
- **Required**: Yes

### ingestionMode
- **Type**: typing.Optional[typing.Literal['ALL', 'BULK', 'PUT']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateDatasetExportJobResponseTypeDef

### datasetExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetGroupRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateDatasetGroupResponseTypeDef

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### domain
- **Type**: typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetImportJobRequestRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DataSourceTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]

### importMode
- **Type**: typing.Optional[typing.Literal['FULL', 'INCREMENTAL']]

### publishAttributionMetricsToS3
- **Type**: typing.Optional[bool]


# CreateDatasetImportJobResponseTypeDef

### datasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateDatasetResponseTypeDef

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventTrackerRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateEventTrackerResponseTypeDef

### eventTrackerArn
- **Type**: <class 'str'>
- **Required**: Yes

### trackingId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFilterRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateFilterResponseTypeDef

### filterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMetricAttributionRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.MetricAttributeTypeDef]
- **Required**: Yes

### metricsOutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.MetricAttributionOutputTypeDef'>
- **Required**: Yes


# CreateMetricAttributionResponseTypeDef

### metricAttributionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRecommenderRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.RecommenderConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateRecommenderResponseTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSchemaRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.personalize_classes.CreateSchemaRequestRequestTypeDef'>>

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# CreateSchemaResponseTypeDef

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSolutionRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.SolutionConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateSolutionResponseTypeDef

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSolutionVersionRequestRequestTypeDef

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### trainingMode
- **Type**: typing.Optional[typing.Literal['AUTOTRAIN', 'FULL', 'UPDATE']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]]


# CreateSolutionVersionResponseTypeDef

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataDeletionJobSummaryTypeDef

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


# DataDeletionJobTypeDef

### jobName
- **Type**: typing.Optional[str]

### dataDeletionJobArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.DataSourceTypeDef]

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


# DataSourceTypeDef

### dataLocation
- **Type**: typing.Optional[str]


# DatasetExportJobOutputTypeDef

### s3DataDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.S3DataConfigTypeDef'>
- **Required**: Yes


# DatasetExportJobSummaryTypeDef

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


# DatasetExportJobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.DatasetExportJobOutputTypeDef]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# DatasetGroupSummaryTypeDef

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


# DatasetGroupTypeDef

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


# DatasetImportJobSummaryTypeDef

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


# DatasetImportJobTypeDef

### jobName
- **Type**: typing.Optional[str]

### datasetImportJobArn
- **Type**: typing.Optional[str]

### datasetArn
- **Type**: typing.Optional[str]

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.DataSourceTypeDef]

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


# DatasetSchemaSummaryTypeDef

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


# DatasetSchemaTypeDef

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


# DatasetSummaryTypeDef

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


# DatasetTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.DatasetUpdateSummaryTypeDef]

### trackingId
- **Type**: typing.Optional[str]


# DatasetUpdateSummaryTypeDef

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


# DefaultCategoricalHyperParameterRangeTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]

### isTunable
- **Type**: typing.Optional[bool]


# DefaultContinuousHyperParameterRangeTypeDef

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]

### isTunable
- **Type**: typing.Optional[bool]


# DefaultHyperParameterRangesTypeDef

### integerHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize_classes.DefaultIntegerHyperParameterRangeTypeDef]]

### continuousHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize_classes.DefaultContinuousHyperParameterRangeTypeDef]]

### categoricalHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize_classes.DefaultCategoricalHyperParameterRangeTypeDef]]


# DefaultIntegerHyperParameterRangeTypeDef

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[int]

### maxValue
- **Type**: typing.Optional[int]

### isTunable
- **Type**: typing.Optional[bool]


# DeleteCampaignRequestRequestTypeDef

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetGroupRequestRequestTypeDef

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDatasetRequestRequestTypeDef

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventTrackerRequestRequestTypeDef

### eventTrackerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFilterRequestRequestTypeDef

### filterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMetricAttributionRequestRequestTypeDef

### metricAttributionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecommenderRequestRequestTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchemaRequestRequestTypeDef

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSolutionRequestRequestTypeDef

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlgorithmRequestRequestTypeDef

### algorithmArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAlgorithmResponseTypeDef

### algorithm
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.AlgorithmTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBatchInferenceJobRequestRequestTypeDef

### batchInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchInferenceJobResponseTypeDef

### batchInferenceJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.BatchInferenceJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBatchSegmentJobRequestRequestTypeDef

### batchSegmentJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchSegmentJobResponseTypeDef

### batchSegmentJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.BatchSegmentJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCampaignRequestRequestTypeDef

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCampaignResponseTypeDef

### campaign
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.CampaignTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataDeletionJobRequestRequestTypeDef

### dataDeletionJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataDeletionJobResponseTypeDef

### dataDeletionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DataDeletionJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetExportJobRequestRequestTypeDef

### datasetExportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetExportJobResponseTypeDef

### datasetExportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DatasetExportJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetGroupRequestRequestTypeDef

### datasetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetGroupResponseTypeDef

### datasetGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DatasetGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetImportJobRequestRequestTypeDef

### datasetImportJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetImportJobResponseTypeDef

### datasetImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DatasetImportJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetRequestRequestTypeDef

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

### dataset
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DatasetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventTrackerRequestRequestTypeDef

### eventTrackerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEventTrackerResponseTypeDef

### eventTracker
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.EventTrackerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFeatureTransformationRequestRequestTypeDef

### featureTransformationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFeatureTransformationResponseTypeDef

### featureTransformation
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.FeatureTransformationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFilterRequestRequestTypeDef

### filterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFilterResponseTypeDef

### filter
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.FilterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMetricAttributionRequestRequestTypeDef

### metricAttributionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMetricAttributionResponseTypeDef

### metricAttribution
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.MetricAttributionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRecipeRequestRequestTypeDef

### recipeArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRecipeResponseTypeDef

### recipe
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.RecipeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRecommenderRequestRequestTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRecommenderResponseTypeDef

### recommender
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.RecommenderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSchemaRequestRequestTypeDef

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSchemaResponseTypeDef

### schema
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.DatasetSchemaTypeDef'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.personalize_classes.DescribeSchemaResponseTypeDef'>>

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSolutionRequestRequestTypeDef

### solutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSolutionResponseTypeDef

### solution
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.SolutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSolutionVersionRequestRequestTypeDef

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSolutionVersionResponseTypeDef

### solutionVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.SolutionVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventTrackerSummaryTypeDef

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


# EventTrackerTypeDef

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


# FeatureTransformationTypeDef

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


# FieldsForThemeGenerationTypeDef

### itemName
- **Type**: <class 'str'>
- **Required**: Yes


# FilterSummaryTypeDef

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


# FilterTypeDef

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


# GetSolutionMetricsRequestRequestTypeDef

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSolutionMetricsResponseTypeDef

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: typing.Dict[str, float]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HPOConfigOutputTypeDef

### hpoObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.HPOObjectiveTypeDef]

### hpoResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.HPOResourceConfigTypeDef]

### algorithmHyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.HyperParameterRangesOutputTypeDef]


# HPOConfigTypeDef

### hpoObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.HPOObjectiveTypeDef]

### hpoResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.HPOResourceConfigTypeDef]

### algorithmHyperParameterRanges
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.HyperParameterRangesTypeDef]


# HPOObjectiveTypeDef

### type
- **Type**: typing.Optional[str]

### metricName
- **Type**: typing.Optional[str]

### metricRegex
- **Type**: typing.Optional[str]


# HPOResourceConfigTypeDef

### maxNumberOfTrainingJobs
- **Type**: typing.Optional[str]

### maxParallelTrainingJobs
- **Type**: typing.Optional[str]


# HyperParameterRangesOutputTypeDef

### integerHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize_classes.IntegerHyperParameterRangeTypeDef]]

### continuousHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize_classes.ContinuousHyperParameterRangeTypeDef]]

### categoricalHyperParameterRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.personalize_classes.CategoricalHyperParameterRangeOutputTypeDef]]


# HyperParameterRangesTypeDef

### integerHyperParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.IntegerHyperParameterRangeTypeDef]]

### continuousHyperParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.ContinuousHyperParameterRangeTypeDef]]

### categoricalHyperParameterRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.CategoricalHyperParameterRangeTypeDef]]


# IntegerHyperParameterRangeTypeDef

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[int]

### maxValue
- **Type**: typing.Optional[int]


# ListBatchInferenceJobsRequestListBatchInferenceJobsPaginateTypeDef

### solutionVersionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListBatchInferenceJobsRequestRequestTypeDef

### solutionVersionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBatchInferenceJobsResponseTypeDef

### batchInferenceJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.BatchInferenceJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBatchSegmentJobsRequestListBatchSegmentJobsPaginateTypeDef

### solutionVersionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListBatchSegmentJobsRequestRequestTypeDef

### solutionVersionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListBatchSegmentJobsResponseTypeDef

### batchSegmentJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.BatchSegmentJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCampaignsRequestListCampaignsPaginateTypeDef

### solutionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListCampaignsRequestRequestTypeDef

### solutionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCampaignsResponseTypeDef

### campaigns
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.CampaignSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataDeletionJobsRequestRequestTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDataDeletionJobsResponseTypeDef

### dataDeletionJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.DataDeletionJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetExportJobsRequestListDatasetExportJobsPaginateTypeDef

### datasetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListDatasetExportJobsRequestRequestTypeDef

### datasetArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetExportJobsResponseTypeDef

### datasetExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.DatasetExportJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListDatasetGroupsRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetGroupsResponseTypeDef

### datasetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.DatasetGroupSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef

### datasetArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListDatasetImportJobsRequestRequestTypeDef

### datasetArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetImportJobsResponseTypeDef

### datasetImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.DatasetImportJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatasetsRequestListDatasetsPaginateTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListDatasetsRequestRequestTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponseTypeDef

### datasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.DatasetSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEventTrackersRequestListEventTrackersPaginateTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListEventTrackersRequestRequestTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEventTrackersResponseTypeDef

### eventTrackers
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.EventTrackerSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFiltersRequestListFiltersPaginateTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListFiltersRequestRequestTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFiltersResponseTypeDef

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.FilterSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetricAttributionMetricsRequestListMetricAttributionMetricsPaginateTypeDef

### metricAttributionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListMetricAttributionMetricsRequestRequestTypeDef

### metricAttributionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMetricAttributionMetricsResponseTypeDef

### metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.MetricAttributeTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMetricAttributionsRequestListMetricAttributionsPaginateTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListMetricAttributionsRequestRequestTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMetricAttributionsResponseTypeDef

### metricAttributions
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.MetricAttributionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecipesRequestListRecipesPaginateTypeDef

### recipeProvider
- **Type**: typing.Optional[typing.Literal['SERVICE']]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListRecipesRequestRequestTypeDef

### recipeProvider
- **Type**: typing.Optional[typing.Literal['SERVICE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### domain
- **Type**: typing.Optional[typing.Literal['ECOMMERCE', 'VIDEO_ON_DEMAND']]


# ListRecipesResponseTypeDef

### recipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.RecipeSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendersRequestListRecommendersPaginateTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListRecommendersRequestRequestTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRecommendersResponseTypeDef

### recommenders
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.RecommenderSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSchemasRequestListSchemasPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListSchemasRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSchemasResponseTypeDef

### schemas
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.DatasetSchemaSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSolutionVersionsRequestListSolutionVersionsPaginateTypeDef

### solutionArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListSolutionVersionsRequestRequestTypeDef

### solutionArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSolutionVersionsResponseTypeDef

### solutionVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.SolutionVersionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSolutionsRequestListSolutionsPaginateTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.PaginatorConfigTypeDef]


# ListSolutionsRequestRequestTypeDef

### datasetGroupArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSolutionsResponseTypeDef

### solutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.SolutionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricAttributeTypeDef

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### metricName
- **Type**: <class 'str'>
- **Required**: Yes

### expression
- **Type**: <class 'str'>
- **Required**: Yes


# MetricAttributionOutputTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### s3DataDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.S3DataConfigTypeDef]


# MetricAttributionSummaryTypeDef

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


# MetricAttributionTypeDef

### name
- **Type**: typing.Optional[str]

### metricAttributionArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### metricsOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.MetricAttributionOutputTypeDef]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### failureReason
- **Type**: typing.Optional[str]


# OptimizationObjectiveTypeDef

### itemAttribute
- **Type**: typing.Optional[str]

### objectiveSensitivity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'OFF']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RecipeSummaryTypeDef

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


# RecipeTypeDef

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


# RecommenderConfigExtraOutputTypeDef

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### minRecommendationRequestsPerSecond
- **Type**: typing.Optional[int]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.TrainingDataConfigExtraOutputTypeDef]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]


# RecommenderConfigOutputTypeDef

### itemExplorationConfig
- **Type**: typing.Optional[typing.Dict[str, str]]

### minRecommendationRequestsPerSecond
- **Type**: typing.Optional[int]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.TrainingDataConfigOutputTypeDef]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]


# RecommenderConfigTypeDef

### itemExplorationConfig
- **Type**: typing.Optional[typing.Mapping[str, str]]

### minRecommendationRequestsPerSecond
- **Type**: typing.Optional[int]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.TrainingDataConfigTypeDef]

### enableMetadataWithRecommendations
- **Type**: typing.Optional[bool]


# RecommenderSummaryTypeDef

### name
- **Type**: typing.Optional[str]

### recommenderArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### recipeArn
- **Type**: typing.Optional[str]

### recommenderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.RecommenderConfigOutputTypeDef]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# RecommenderTypeDef

### recommenderArn
- **Type**: typing.Optional[str]

### datasetGroupArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### recipeArn
- **Type**: typing.Optional[str]

### recommenderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.RecommenderConfigOutputTypeDef]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]

### latestRecommenderUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.RecommenderUpdateSummaryTypeDef]

### modelMetrics
- **Type**: typing.Optional[typing.Dict[str, float]]


# RecommenderUpdateSummaryTypeDef

### recommenderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.RecommenderConfigOutputTypeDef]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[str]

### failureReason
- **Type**: typing.Optional[str]


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


# S3DataConfigTypeDef

### path
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: typing.Optional[str]


# SolutionConfigOutputTypeDef

### eventValueThreshold
- **Type**: typing.Optional[str]

### hpoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.HPOConfigOutputTypeDef]

### algorithmHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### featureTransformationParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### autoMLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.AutoMLConfigOutputTypeDef]

### optimizationObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.OptimizationObjectiveTypeDef]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.TrainingDataConfigOutputTypeDef]

### autoTrainingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.AutoTrainingConfigTypeDef]


# SolutionConfigTypeDef

### eventValueThreshold
- **Type**: typing.Optional[str]

### hpoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.HPOConfigTypeDef]

### algorithmHyperParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### featureTransformationParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### autoMLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.AutoMLConfigTypeDef]

### optimizationObjective
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.OptimizationObjectiveTypeDef]

### trainingDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.TrainingDataConfigTypeDef]

### autoTrainingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.AutoTrainingConfigTypeDef]


# SolutionSummaryTypeDef

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


# SolutionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.SolutionConfigOutputTypeDef]

### autoMLResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.AutoMLResultTypeDef]

### status
- **Type**: typing.Optional[str]

### creationDateTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### latestSolutionVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.SolutionVersionSummaryTypeDef]


# SolutionVersionSummaryTypeDef

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


# SolutionVersionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.SolutionConfigOutputTypeDef]

### trainingHours
- **Type**: typing.Optional[float]

### trainingMode
- **Type**: typing.Optional[typing.Literal['AUTOTRAIN', 'FULL', 'UPDATE']]

### tunedHPOParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.TunedHPOParamsTypeDef]

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


# StartRecommenderRequestRequestTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes


# StartRecommenderResponseTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopRecommenderRequestRequestTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopRecommenderResponseTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopSolutionVersionCreationRequestRequestTypeDef

### solutionVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### tagKey
- **Type**: <class 'str'>
- **Required**: Yes

### tagValue
- **Type**: <class 'str'>
- **Required**: Yes


# ThemeGenerationConfigTypeDef

### fieldsForThemeGeneration
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.FieldsForThemeGenerationTypeDef'>
- **Required**: Yes


# TrainingDataConfigExtraOutputTypeDef

### excludedDatasetColumns
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# TrainingDataConfigOutputTypeDef

### excludedDatasetColumns
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# TrainingDataConfigTypeDef

### excludedDatasetColumns
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# TunedHPOParamsTypeDef

### algorithmHyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCampaignRequestRequestTypeDef

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes

### solutionVersionArn
- **Type**: typing.Optional[str]

### minProvisionedTPS
- **Type**: typing.Optional[int]

### campaignConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.CampaignConfigTypeDef]


# UpdateCampaignResponseTypeDef

### campaignArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDatasetRequestRequestTypeDef

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### schemaArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDatasetResponseTypeDef

### datasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMetricAttributionRequestRequestTypeDef

### addMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.personalize_classes.MetricAttributeTypeDef]]

### removeMetrics
- **Type**: typing.Optional[typing.Sequence[str]]

### metricsOutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.personalize_classes.MetricAttributionOutputTypeDef]

### metricAttributionArn
- **Type**: typing.Optional[str]


# UpdateMetricAttributionResponseTypeDef

### metricAttributionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRecommenderRequestRequestTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### recommenderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.RecommenderConfigTypeDef'>
- **Required**: Yes


# UpdateRecommenderResponseTypeDef

### recommenderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.personalize_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



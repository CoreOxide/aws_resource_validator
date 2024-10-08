# Pydantic Models in cleanroomsml_classes

# AudienceDestinationTypeDef

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.S3ConfigMapTypeDef'>
- **Required**: Yes


# AudienceExportJobSummaryTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### audienceSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeTypeDef'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING']
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### outputLocation
- **Type**: typing.Optional[str]

### statusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef]


# AudienceGenerationJobDataSourceTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.S3ConfigMapTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# AudienceGenerationJobSummaryTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING']
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### collaborationId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### startedBy
- **Type**: typing.Optional[str]


# AudienceModelSummaryTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING']
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# AudienceQualityMetricsTypeDef

### relevanceMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.RelevanceMetricTypeDef]
- **Required**: Yes

### recallMetric
- **Type**: typing.Optional[float]


# AudienceSizeConfigTypeDef

### audienceSizeBins
- **Type**: typing.Sequence[int]
- **Required**: Yes

### audienceSizeType
- **Type**: typing.Literal['ABSOLUTE', 'PERCENTAGE']
- **Required**: Yes


# AudienceSizeTypeDef

### type
- **Type**: typing.Literal['ABSOLUTE', 'PERCENTAGE']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnSchemaTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### columnTypes
- **Type**: typing.Sequence[typing.Literal['CATEGORICAL_FEATURE', 'ITEM_ID', 'NUMERICAL_FEATURE', 'TIMESTAMP', 'USER_ID']]
- **Required**: Yes


# ConfiguredAudienceModelOutputConfigTypeDef

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceDestinationTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConfiguredAudienceModelSummaryTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelOutputConfigTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateAudienceModelRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### trainingDataEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### trainingDataStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CreateAudienceModelResponseTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredAudienceModelRequestRequestTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelOutputConfigTypeDef'>
- **Required**: Yes

### sharedAudienceMetrics
- **Type**: typing.Sequence[typing.Literal['ALL', 'NONE']]
- **Required**: Yes

### audienceSizeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeConfigTypeDef]

### childResourceTagOnCreatePolicy
- **Type**: typing.Optional[typing.Literal['FROM_PARENT_RESOURCE', 'NONE']]

### description
- **Type**: typing.Optional[str]

### minMatchingSeedSize
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConfiguredAudienceModelResponseTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrainingDatasetRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### trainingData
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.DatasetTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTrainingDatasetResponseTypeDef

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSourceTypeDef

### glueDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.GlueDataSourceTypeDef'>
- **Required**: Yes


# DatasetInputConfigTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.DataSourceTypeDef'>
- **Required**: Yes

### schema
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.ColumnSchemaTypeDef]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.DatasetInputConfigTypeDef'>>


# DatasetTypeDef

### inputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.DatasetInputConfigTypeDef'>
- **Required**: Yes

### type
- **Type**: typing.Literal['INTERACTIONS']
- **Required**: Yes


# DeleteAudienceGenerationJobRequestRequestTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAudienceModelRequestRequestTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelRequestRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrainingDatasetRequestRequestTypeDef

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAudienceGenerationJobRequestRequestTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAudienceGenerationJobResponseTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### includeSeedInOutput
- **Type**: <class 'bool'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceQualityMetricsTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### seedAudience
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceGenerationJobDataSourceTypeDef'>
- **Required**: Yes

### startedBy
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING']
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAudienceModelRequestRequestTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAudienceModelResponseTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING']
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### trainingDataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainingDataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredAudienceModelPolicyRequestRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredAudienceModelPolicyResponseTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### policyHash
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredAudienceModelRequestRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredAudienceModelResponseTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### audienceSizeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeConfigTypeDef'>
- **Required**: Yes

### childResourceTagOnCreatePolicy
- **Type**: typing.Literal['FROM_PARENT_RESOURCE', 'NONE']
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### minMatchingSeedSize
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelOutputConfigTypeDef'>
- **Required**: Yes

### sharedAudienceMetrics
- **Type**: typing.List[typing.Literal['ALL', 'NONE']]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrainingDatasetRequestRequestTypeDef

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrainingDatasetResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### trainingData
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.DatasetTypeDef]
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlueDataSourceTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### catalogId
- **Type**: typing.Optional[str]


# ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef

### audienceGenerationJobArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListAudienceExportJobsRequestRequestTypeDef

### audienceGenerationJobArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAudienceExportJobsResponseTypeDef

### audienceExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceExportJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef

### collaborationId
- **Type**: typing.Optional[str]

### configuredAudienceModelArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListAudienceGenerationJobsRequestRequestTypeDef

### collaborationId
- **Type**: typing.Optional[str]

### configuredAudienceModelArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAudienceGenerationJobsResponseTypeDef

### audienceGenerationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceGenerationJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAudienceModelsRequestListAudienceModelsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListAudienceModelsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAudienceModelsResponseTypeDef

### audienceModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceModelSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListConfiguredAudienceModelsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredAudienceModelsResponseTypeDef

### configuredAudienceModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListTrainingDatasetsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTrainingDatasetsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDatasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainingDatasetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutConfiguredAudienceModelPolicyRequestRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### policyExistenceCondition
- **Type**: typing.Optional[typing.Literal['POLICY_MUST_EXIST', 'POLICY_MUST_NOT_EXIST']]

### previousPolicyHash
- **Type**: typing.Optional[str]


# PutConfiguredAudienceModelPolicyResponseTypeDef

### configuredAudienceModelPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### policyHash
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RelevanceMetricTypeDef

### audienceSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeTypeDef'>
- **Required**: Yes

### score
- **Type**: typing.Optional[float]


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


# S3ConfigMapTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# StartAudienceExportJobRequestRequestTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### audienceSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartAudienceGenerationJobRequestRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### seedAudience
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceGenerationJobDataSourceTypeDef'>
- **Required**: Yes

### collaborationId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### includeSeedInOutput
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartAudienceGenerationJobResponseTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatusDetailsTypeDef

### message
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TrainingDatasetSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConfiguredAudienceModelRequestRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### audienceModelArn
- **Type**: typing.Optional[str]

### audienceSizeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeConfigTypeDef]

### description
- **Type**: typing.Optional[str]

### minMatchingSeedSize
- **Type**: typing.Optional[int]

### outputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelOutputConfigTypeDef]

### sharedAudienceMetrics
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'NONE']]]


# UpdateConfiguredAudienceModelResponseTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



# Cleanroomsml Classes

# AudienceDestinationTypeDef

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.S3ConfigMapTypeDef'>
- **Required**: Yes


# AudienceExportJobSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### audienceSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### statusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef]

### outputLocation
- **Type**: typing.Optional[str]


# AudienceGenerationJobDataSourceOutputTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.S3ConfigMapTypeDef]

### sqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ProtectedQuerySQLParametersOutputTypeDef]

### sqlComputeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ComputeConfigurationTypeDef]


# AudienceGenerationJobDataSourceTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.S3ConfigMapTypeDef]

### sqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ProtectedQuerySQLParametersTypeDef]

### sqlComputeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ComputeConfigurationTypeDef]


# AudienceGenerationJobDataSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudienceGenerationJobSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING']
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### collaborationId
- **Type**: typing.Optional[str]

### startedBy
- **Type**: typing.Optional[str]


# AudienceModelSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# AudienceQualityMetricsTypeDef

### relevanceMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.RelevanceMetricTypeDef]
- **Required**: Yes

### recallMetric
- **Type**: typing.Optional[float]


# AudienceSizeConfigOutputTypeDef

### audienceSizeType
- **Type**: typing.Literal['ABSOLUTE', 'PERCENTAGE']
- **Required**: Yes

### audienceSizeBins
- **Type**: typing.List[int]
- **Required**: Yes


# AudienceSizeConfigTypeDef

### audienceSizeType
- **Type**: typing.Literal['ABSOLUTE', 'PERCENTAGE']
- **Required**: Yes

### audienceSizeBins
- **Type**: typing.Sequence[int]
- **Required**: Yes


# AudienceSizeConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudienceSizeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTrainedModelInferenceJobRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# CancelTrainedModelRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CollaborationMLInputChannelSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociations
- **Type**: typing.List[str]
- **Required**: Yes

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'INACTIVE']
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CollaborationTrainedModelExportJobSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelExportOutputConfigurationOutputTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING']
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### statusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef]

### description
- **Type**: typing.Optional[str]


# CollaborationTrainedModelInferenceJobSummaryTypeDef

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_PENDING', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'INACTIVE']
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceOutputConfigurationOutputTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### metricsStatus
- **Type**: typing.Optional[typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']]

### metricsStatusDetails
- **Type**: typing.Optional[str]

### logsStatus
- **Type**: typing.Optional[typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']]

### logsStatusDetails
- **Type**: typing.Optional[str]


# CollaborationTrainedModelSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_PENDING', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'INACTIVE']
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ColumnSchemaOutputTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### columnTypes
- **Type**: typing.List[typing.Literal['CATEGORICAL_FEATURE', 'ITEM_ID', 'NUMERICAL_FEATURE', 'TIMESTAMP', 'USER_ID']]
- **Required**: Yes


# ColumnSchemaTypeDef

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### columnTypes
- **Type**: typing.Sequence[typing.Literal['CATEGORICAL_FEATURE', 'ITEM_ID', 'NUMERICAL_FEATURE', 'TIMESTAMP', 'USER_ID']]
- **Required**: Yes


# ColumnSchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComputeConfigurationTypeDef

### worker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.WorkerComputeConfigurationTypeDef]


# ConfiguredAudienceModelOutputConfigTypeDef

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceDestinationTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConfiguredAudienceModelSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelOutputConfigTypeDef'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ConfiguredModelAlgorithmAssociationSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ConfiguredModelAlgorithmSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ContainerConfigOutputTypeDef

### imageUri
- **Type**: <class 'str'>
- **Required**: Yes

### entrypoint
- **Type**: typing.Optional[typing.List[str]]

### arguments
- **Type**: typing.Optional[typing.List[str]]

### metricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.MetricDefinitionTypeDef]]


# ContainerConfigTypeDef

### imageUri
- **Type**: <class 'str'>
- **Required**: Yes

### entrypoint
- **Type**: typing.Optional[typing.Sequence[str]]

### arguments
- **Type**: typing.Optional[typing.Sequence[str]]

### metricDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.MetricDefinitionTypeDef]]


# ContainerConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAudienceModelRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDataStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TimestampTypeDef]

### trainingDataEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TimestampTypeDef]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### description
- **Type**: typing.Optional[str]


# CreateAudienceModelResponseTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredAudienceModelRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelOutputConfigTypeDef'>
- **Required**: Yes

### sharedAudienceMetrics
- **Type**: typing.Sequence[typing.Literal['ALL', 'NONE']]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### minMatchingSeedSize
- **Type**: typing.Optional[int]

### audienceSizeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeConfigUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### childResourceTagOnCreatePolicy
- **Type**: typing.Optional[typing.Literal['FROM_PARENT_RESOURCE', 'NONE']]


# CreateConfiguredAudienceModelResponseTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredModelAlgorithmAssociationRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### privacyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PrivacyConfigurationUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConfiguredModelAlgorithmAssociationResponseTypeDef

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfiguredModelAlgorithmRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### trainingContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ContainerConfigUnionTypeDef]

### inferenceContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceContainerConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateConfiguredModelAlgorithmResponseTypeDef

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMLInputChannelRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociations
- **Type**: typing.Sequence[str]
- **Required**: Yes

### inputChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InputChannelUnionTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### retentionInDays
- **Type**: <class 'int'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMLInputChannelResponseTypeDef

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrainedModelRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResourceConfigTypeDef'>
- **Required**: Yes

### dataChannels
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.ModelTrainingDataChannelTypeDef]
- **Required**: Yes

### hyperparameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### stoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.StoppingConditionTypeDef]

### description
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTrainedModelResponseTypeDef

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrainingDatasetRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### trainingData
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.DatasetUnionTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### description
- **Type**: typing.Optional[str]


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


# DatasetInputConfigOutputTypeDef

### schema
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.ColumnSchemaOutputTypeDef]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.DatasetInputConfigOutputTypeDef'>>

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.DataSourceTypeDef'>
- **Required**: Yes


# DatasetInputConfigTypeDef

### schema
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.ColumnSchemaUnionTypeDef]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.DatasetInputConfigTypeDef'>>

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.DataSourceTypeDef'>
- **Required**: Yes


# DatasetOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatasetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAudienceGenerationJobRequestTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAudienceModelRequestTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelPolicyRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredModelAlgorithmAssociationRequestTypeDef

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredModelAlgorithmRequestTypeDef

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMLConfigurationRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMLInputChannelDataRequestTypeDef

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrainedModelOutputRequestTypeDef

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrainingDatasetRequestTypeDef

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationTypeDef

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.S3ConfigMapTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAudienceGenerationJobRequestTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAudienceGenerationJobResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING']
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### seedAudience
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceGenerationJobDataSourceOutputTypeDef'>
- **Required**: Yes

### includeSeedInOutput
- **Type**: <class 'bool'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceQualityMetricsTypeDef'>
- **Required**: Yes

### startedBy
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### protectedQueryIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAudienceModelRequestTypeDef

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAudienceModelResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainingDataStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainingDataEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING']
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### privacyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.PrivacyConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCollaborationMLInputChannelRequestTypeDef

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationMLInputChannelResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociations
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'INACTIVE']
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### retentionInDays
- **Type**: <class 'int'>
- **Required**: Yes

### numberOfRecords
- **Type**: <class 'int'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCollaborationTrainedModelRequestTypeDef

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationTrainedModelResponseTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_PENDING', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'INACTIVE']
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResourceConfigTypeDef'>
- **Required**: Yes

### stoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### metricsStatus
- **Type**: typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']
- **Required**: Yes

### metricsStatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### logsStatus
- **Type**: typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']
- **Required**: Yes

### logsStatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### trainingContainerImageDigest
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### creatorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredAudienceModelPolicyRequestTypeDef

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


# GetConfiguredAudienceModelRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredAudienceModelResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelOutputConfigTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### sharedAudienceMetrics
- **Type**: typing.List[typing.Literal['ALL', 'NONE']]
- **Required**: Yes

### minMatchingSeedSize
- **Type**: <class 'int'>
- **Required**: Yes

### audienceSizeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeConfigOutputTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### childResourceTagOnCreatePolicy
- **Type**: typing.Literal['FROM_PARENT_RESOURCE', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredModelAlgorithmAssociationRequestTypeDef

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredModelAlgorithmAssociationResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### privacyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.PrivacyConfigurationOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConfiguredModelAlgorithmRequestTypeDef

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredModelAlgorithmResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainingContainerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ContainerConfigOutputTypeDef'>
- **Required**: Yes

### inferenceContainerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceContainerConfigTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLConfigurationRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMLConfigurationResponseTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### defaultOutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.MLOutputConfigurationTypeDef'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMLInputChannelRequestTypeDef

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMLInputChannelResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inputChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InputChannelOutputTypeDef'>
- **Required**: Yes

### protectedQueryIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociations
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'INACTIVE']
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### retentionInDays
- **Type**: <class 'int'>
- **Required**: Yes

### numberOfRecords
- **Type**: <class 'int'>
- **Required**: Yes

### numberOfFiles
- **Type**: <class 'float'>
- **Required**: Yes

### sizeInGb
- **Type**: <class 'float'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrainedModelInferenceJobRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrainedModelInferenceJobResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_PENDING', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'INACTIVE']
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceResourceConfigTypeDef'>
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceOutputConfigurationOutputTypeDef'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ModelInferenceDataSourceTypeDef'>
- **Required**: Yes

### containerExecutionParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceContainerExecutionParametersTypeDef'>
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### inferenceContainerImageDigest
- **Type**: <class 'str'>
- **Required**: Yes

### environment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### metricsStatus
- **Type**: typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']
- **Required**: Yes

### metricsStatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### logsStatus
- **Type**: typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']
- **Required**: Yes

### logsStatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrainedModelRequestTypeDef

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrainedModelResponseTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_PENDING', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'INACTIVE']
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StatusDetailsTypeDef'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResourceConfigTypeDef'>
- **Required**: Yes

### stoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.StoppingConditionTypeDef'>
- **Required**: Yes

### metricsStatus
- **Type**: typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']
- **Required**: Yes

### metricsStatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### logsStatus
- **Type**: typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']
- **Required**: Yes

### logsStatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### trainingContainerImageDigest
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### hyperparameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### environment
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### dataChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.ModelTrainingDataChannelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrainingDatasetRequestTypeDef

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrainingDatasetResponseTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainingData
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.DatasetOutputTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlueDataSourceTypeDef

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### catalogId
- **Type**: typing.Optional[str]


# InferenceContainerConfigTypeDef

### imageUri
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceContainerExecutionParametersTypeDef

### maxPayloadInMB
- **Type**: typing.Optional[int]


# InferenceOutputConfigurationOutputTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceReceiverMemberTypeDef]
- **Required**: Yes

### accept
- **Type**: typing.Optional[str]


# InferenceOutputConfigurationTypeDef

### members
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceReceiverMemberTypeDef]
- **Required**: Yes

### accept
- **Type**: typing.Optional[str]


# InferenceOutputConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceReceiverMemberTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceResourceConfigTypeDef

### instanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge']
- **Required**: Yes

### instanceCount
- **Type**: typing.Optional[int]


# InputChannelDataSourceOutputTypeDef

### protectedQueryInputParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ProtectedQueryInputParametersOutputTypeDef]


# InputChannelDataSourceTypeDef

### protectedQueryInputParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ProtectedQueryInputParametersTypeDef]


# InputChannelOutputTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InputChannelDataSourceOutputTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# InputChannelTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InputChannelDataSourceTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# InputChannelUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAudienceExportJobsRequestPaginateTypeDef

### audienceGenerationJobArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListAudienceExportJobsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### audienceGenerationJobArn
- **Type**: typing.Optional[str]


# ListAudienceExportJobsResponseTypeDef

### audienceExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceExportJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAudienceGenerationJobsRequestPaginateTypeDef

### configuredAudienceModelArn
- **Type**: typing.Optional[str]

### collaborationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListAudienceGenerationJobsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### configuredAudienceModelArn
- **Type**: typing.Optional[str]

### collaborationId
- **Type**: typing.Optional[str]


# ListAudienceGenerationJobsResponseTypeDef

### audienceGenerationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceGenerationJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAudienceModelsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListAudienceModelsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAudienceModelsResponseTypeDef

### audienceModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef

### collaborationConfiguredModelAlgorithmAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationMLInputChannelsRequestPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListCollaborationMLInputChannelsRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationMLInputChannelsResponseTypeDef

### collaborationMLInputChannelsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.CollaborationMLInputChannelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListCollaborationTrainedModelExportJobsRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationTrainedModelExportJobsResponseTypeDef

### collaborationTrainedModelExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.CollaborationTrainedModelExportJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListCollaborationTrainedModelInferenceJobsRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### trainedModelArn
- **Type**: typing.Optional[str]


# ListCollaborationTrainedModelInferenceJobsResponseTypeDef

### collaborationTrainedModelInferenceJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.CollaborationTrainedModelInferenceJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationTrainedModelsRequestPaginateTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListCollaborationTrainedModelsRequestTypeDef

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationTrainedModelsResponseTypeDef

### collaborationTrainedModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.CollaborationTrainedModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredAudienceModelsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListConfiguredAudienceModelsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredAudienceModelsResponseTypeDef

### configuredAudienceModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListConfiguredModelAlgorithmAssociationsRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredModelAlgorithmAssociationsResponseTypeDef

### configuredModelAlgorithmAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredModelAlgorithmAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredModelAlgorithmsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListConfiguredModelAlgorithmsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredModelAlgorithmsResponseTypeDef

### configuredModelAlgorithms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredModelAlgorithmSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMLInputChannelsRequestPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListMLInputChannelsRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMLInputChannelsResponseTypeDef

### mlInputChannelsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.MLInputChannelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrainedModelInferenceJobsRequestPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListTrainedModelInferenceJobsRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### trainedModelArn
- **Type**: typing.Optional[str]


# ListTrainedModelInferenceJobsResponseTypeDef

### trainedModelInferenceJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelInferenceJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTrainedModelsRequestPaginateTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListTrainedModelsRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTrainedModelsResponseTypeDef

### trainedModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTrainingDatasetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.PaginatorConfigTypeDef]


# ListTrainingDatasetsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTrainingDatasetsResponseTypeDef

### trainingDatasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainingDatasetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogsConfigurationPolicyOutputTypeDef

### allowedAccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### filterPattern
- **Type**: typing.Optional[str]


# LogsConfigurationPolicyTypeDef

### allowedAccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### filterPattern
- **Type**: typing.Optional[str]


# MLInputChannelSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociations
- **Type**: typing.List[str]
- **Required**: Yes

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'INACTIVE']
- **Required**: Yes

### protectedQueryIdentifier
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# MLOutputConfigurationTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.DestinationTypeDef]


# MetricDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### regex
- **Type**: <class 'str'>
- **Required**: Yes


# MetricsConfigurationPolicyTypeDef

### noiseLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes


# ModelInferenceDataSourceTypeDef

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes


# ModelTrainingDataChannelTypeDef

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### channelName
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrivacyConfigurationOutputTypeDef

### policies
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.PrivacyConfigurationPoliciesOutputTypeDef'>
- **Required**: Yes


# PrivacyConfigurationPoliciesOutputTypeDef

### trainedModels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelsConfigurationPolicyOutputTypeDef]

### trainedModelExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelExportsConfigurationPolicyOutputTypeDef]

### trainedModelInferenceJobs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef]


# PrivacyConfigurationPoliciesTypeDef

### trainedModels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelsConfigurationPolicyTypeDef]

### trainedModelExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelExportsConfigurationPolicyTypeDef]

### trainedModelInferenceJobs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelInferenceJobsConfigurationPolicyTypeDef]


# PrivacyConfigurationTypeDef

### policies
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.PrivacyConfigurationPoliciesTypeDef'>
- **Required**: Yes


# PrivacyConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProtectedQueryInputParametersOutputTypeDef

### sqlParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ProtectedQuerySQLParametersOutputTypeDef'>
- **Required**: Yes

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ComputeConfigurationTypeDef]


# ProtectedQueryInputParametersTypeDef

### sqlParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ProtectedQuerySQLParametersTypeDef'>
- **Required**: Yes

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ComputeConfigurationTypeDef]


# ProtectedQuerySQLParametersOutputTypeDef

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProtectedQuerySQLParametersTypeDef

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutConfiguredAudienceModelPolicyRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### previousPolicyHash
- **Type**: typing.Optional[str]

### policyExistenceCondition
- **Type**: typing.Optional[typing.Literal['POLICY_MUST_EXIST', 'POLICY_MUST_NOT_EXIST']]


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


# PutMLConfigurationRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### defaultOutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.MLOutputConfigurationTypeDef'>
- **Required**: Yes


# RelevanceMetricTypeDef

### audienceSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeTypeDef'>
- **Required**: Yes

### score
- **Type**: typing.Optional[float]


# ResourceConfigTypeDef

### instanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### volumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### instanceCount
- **Type**: typing.Optional[int]


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


# StartAudienceExportJobRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### audienceSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartAudienceGenerationJobRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### seedAudience
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceGenerationJobDataSourceUnionTypeDef'>
- **Required**: Yes

### includeSeedInOutput
- **Type**: typing.Optional[bool]

### collaborationId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartAudienceGenerationJobResponseTypeDef

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTrainedModelExportJobRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelExportOutputConfigurationUnionTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartTrainedModelInferenceJobRequestTypeDef

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceResourceConfigTypeDef'>
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceOutputConfigurationUnionTypeDef'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ModelInferenceDataSourceTypeDef'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### containerExecutionParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceContainerExecutionParametersTypeDef]

### environment
- **Type**: typing.Optional[typing.Mapping[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartTrainedModelInferenceJobResponseTypeDef

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatusDetailsTypeDef

### statusCode
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# StoppingConditionTypeDef

### maxRuntimeInSeconds
- **Type**: typing.Optional[int]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrainedModelExportOutputConfigurationOutputTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelExportReceiverMemberTypeDef]
- **Required**: Yes


# TrainedModelExportOutputConfigurationTypeDef

### members
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelExportReceiverMemberTypeDef]
- **Required**: Yes


# TrainedModelExportOutputConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrainedModelExportReceiverMemberTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# TrainedModelExportsConfigurationPolicyOutputTypeDef

### maxSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelExportsMaxSizeTypeDef'>
- **Required**: Yes

### filesToExport
- **Type**: typing.List[typing.Literal['MODEL', 'OUTPUT']]
- **Required**: Yes


# TrainedModelExportsConfigurationPolicyTypeDef

### maxSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelExportsMaxSizeTypeDef'>
- **Required**: Yes

### filesToExport
- **Type**: typing.Sequence[typing.Literal['MODEL', 'OUTPUT']]
- **Required**: Yes


# TrainedModelExportsMaxSizeTypeDef

### unit
- **Type**: typing.Literal['GB']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# TrainedModelInferenceJobSummaryTypeDef

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_PENDING', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'INACTIVE']
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.InferenceOutputConfigurationOutputTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### metricsStatus
- **Type**: typing.Optional[typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']]

### metricsStatusDetails
- **Type**: typing.Optional[str]

### logsStatus
- **Type**: typing.Optional[typing.Literal['PUBLISH_FAILED', 'PUBLISH_SUCCEEDED']]

### logsStatusDetails
- **Type**: typing.Optional[str]


# TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef

### containerLogs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.LogsConfigurationPolicyOutputTypeDef]]

### maxOutputSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelInferenceMaxOutputSizeTypeDef]


# TrainedModelInferenceJobsConfigurationPolicyTypeDef

### containerLogs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.LogsConfigurationPolicyTypeDef]]

### maxOutputSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.TrainedModelInferenceMaxOutputSizeTypeDef]


# TrainedModelInferenceMaxOutputSizeTypeDef

### unit
- **Type**: typing.Literal['GB']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# TrainedModelSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CANCEL_FAILED', 'CANCEL_IN_PROGRESS', 'CANCEL_PENDING', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'DELETE_PENDING', 'INACTIVE']
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# TrainedModelsConfigurationPolicyOutputTypeDef

### containerLogs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml_classes.LogsConfigurationPolicyOutputTypeDef]]

### containerMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.MetricsConfigurationPolicyTypeDef]


# TrainedModelsConfigurationPolicyTypeDef

### containerLogs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cleanroomsml_classes.LogsConfigurationPolicyTypeDef]]

### containerMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.MetricsConfigurationPolicyTypeDef]


# TrainingDatasetSummaryTypeDef

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConfiguredAudienceModelRequestTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.ConfiguredAudienceModelOutputConfigTypeDef]

### audienceModelArn
- **Type**: typing.Optional[str]

### sharedAudienceMetrics
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL', 'NONE']]]

### minMatchingSeedSize
- **Type**: typing.Optional[int]

### audienceSizeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml_classes.AudienceSizeConfigUnionTypeDef]

### description
- **Type**: typing.Optional[str]


# UpdateConfiguredAudienceModelResponseTypeDef

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkerComputeConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


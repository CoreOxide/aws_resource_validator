# Cleanroomsml Cleanroomsml Classes

# AudienceDestination

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.S3ConfigMap'>
- **Required**: Yes


# AudienceExportJobSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceSize'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'CREATE_PENDING']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### statusDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails]

### outputLocation
- **Type**: typing.Optional[str]


# AudienceGenerationJobDataSource

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.S3ConfigMap]

### sqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ProtectedQuerySQLParameters]

### sqlComputeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ComputeConfiguration]


# AudienceGenerationJobDataSourceOutput

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.S3ConfigMap]

### sqlParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ProtectedQuerySQLParametersOutput]

### sqlComputeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ComputeConfiguration]


# AudienceGenerationJobSummary

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


# AudienceModelSummary

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


# AudienceQualityMetrics

### relevanceMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.RelevanceMetric]
- **Required**: Yes

### recallMetric
- **Type**: typing.Optional[float]


# AudienceSize

### type
- **Type**: typing.Literal['ABSOLUTE', 'PERCENTAGE']
- **Required**: Yes

### value
- **Type**: <class 'int'>
- **Required**: Yes


# AudienceSizeConfig

### audienceSizeType
- **Type**: typing.Literal['ABSOLUTE', 'PERCENTAGE']
- **Required**: Yes

### audienceSizeBins
- **Type**: typing.List[int]
- **Required**: Yes


# AudienceSizeConfigOutput

### audienceSizeType
- **Type**: typing.Literal['ABSOLUTE', 'PERCENTAGE']
- **Required**: Yes

### audienceSizeBins
- **Type**: typing.List[int]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTrainedModelInferenceJobRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# CancelTrainedModelRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# CollaborationConfiguredModelAlgorithmAssociationSummary

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


# CollaborationMLInputChannelSummary

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


# CollaborationTrainedModelExportJobSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportOutputConfigurationOutput'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails]

### description
- **Type**: typing.Optional[str]


# CollaborationTrainedModelInferenceJobSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceOutputConfigurationOutput'>
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


# CollaborationTrainedModelSummary

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


# ColumnSchema

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### columnTypes
- **Type**: typing.List[typing.Literal['CATEGORICAL_FEATURE', 'ITEM_ID', 'NUMERICAL_FEATURE', 'TIMESTAMP', 'USER_ID']]
- **Required**: Yes


# ColumnSchemaOutput

### columnName
- **Type**: <class 'str'>
- **Required**: Yes

### columnTypes
- **Type**: typing.List[typing.Literal['CATEGORICAL_FEATURE', 'ITEM_ID', 'NUMERICAL_FEATURE', 'TIMESTAMP', 'USER_ID']]
- **Required**: Yes


# ComputeConfiguration

### worker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.WorkerComputeConfiguration]


# ConfiguredAudienceModelOutputConfig

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceDestination'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ConfiguredAudienceModelSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ConfiguredAudienceModelOutputConfig'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ConfiguredModelAlgorithmAssociationSummary

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


# ConfiguredModelAlgorithmSummary

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


# ContainerConfig

### imageUri
- **Type**: <class 'str'>
- **Required**: Yes

### entrypoint
- **Type**: typing.Optional[typing.List[str]]

### arguments
- **Type**: typing.Optional[typing.List[str]]

### metricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.MetricDefinition]]


# ContainerConfigOutput

### imageUri
- **Type**: <class 'str'>
- **Required**: Yes

### entrypoint
- **Type**: typing.Optional[typing.List[str]]

### arguments
- **Type**: typing.Optional[typing.List[str]]

### metricDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.MetricDefinition]]


# CreateAudienceModelRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### trainingDataStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### trainingDataEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### description
- **Type**: typing.Optional[str]


# CreateAudienceModelResponse

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredAudienceModelRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ConfiguredAudienceModelOutputConfig'>
- **Required**: Yes

### sharedAudienceMetrics
- **Type**: typing.List[typing.Literal['ALL', 'NONE']]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### minMatchingSeedSize
- **Type**: typing.Optional[int]

### audienceSizeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceSizeConfig, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceSizeConfigOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### childResourceTagOnCreatePolicy
- **Type**: typing.Optional[typing.Literal['FROM_PARENT_RESOURCE', 'NONE']]


# CreateConfiguredAudienceModelResponse

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredModelAlgorithmAssociationRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PrivacyConfiguration, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PrivacyConfigurationOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConfiguredModelAlgorithmAssociationResponse

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfiguredModelAlgorithmRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### trainingContainerConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ContainerConfig, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ContainerConfigOutput, NoneType]

### inferenceContainerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceContainerConfig]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]


# CreateConfiguredModelAlgorithmResponse

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMLInputChannelRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### configuredModelAlgorithmAssociations
- **Type**: typing.List[str]
- **Required**: Yes

### inputChannel
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InputChannel, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InputChannelOutput]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMLInputChannelResponse

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrainedModelRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResourceConfig'>
- **Required**: Yes

### dataChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ModelTrainingDataChannel]
- **Required**: Yes

### hyperparameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### stoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StoppingCondition]

### description
- **Type**: typing.Optional[str]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateTrainedModelResponse

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrainingDatasetRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### trainingData
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.Dataset, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DatasetOutput]]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### description
- **Type**: typing.Optional[str]


# CreateTrainingDatasetResponse

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# DataSource

### glueDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.GlueDataSource'>
- **Required**: Yes


# Dataset

### type
- **Type**: typing.Literal['INTERACTIONS']
- **Required**: Yes

### inputConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DatasetInputConfig, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DatasetInputConfigOutput]
- **Required**: Yes


# DatasetInputConfig

### schema
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ColumnSchema, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ColumnSchemaOutput]]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DatasetInputConfig'>>

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DataSource'>
- **Required**: Yes


# DatasetInputConfigOutput

### schema
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ColumnSchemaOutput]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DatasetInputConfigOutput'>>

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DataSource'>
- **Required**: Yes


# DatasetOutput

### type
- **Type**: typing.Literal['INTERACTIONS']
- **Required**: Yes

### inputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DatasetInputConfigOutput'>
- **Required**: Yes


# DeleteAudienceGenerationJobRequest

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAudienceModelRequest

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelPolicyRequest

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredAudienceModelRequest

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredModelAlgorithmAssociationRequest

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfiguredModelAlgorithmRequest

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMLConfigurationRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMLInputChannelDataRequest

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrainedModelOutputRequest

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrainingDatasetRequest

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# Destination

### s3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.S3ConfigMap'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetAudienceGenerationJobRequest

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAudienceGenerationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### seedAudience
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceGenerationJobDataSourceOutput'>
- **Required**: Yes

### includeSeedInOutput
- **Type**: <class 'bool'>
- **Required**: Yes

### collaborationId
- **Type**: <class 'str'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceQualityMetrics'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetAudienceModelRequest

### audienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAudienceModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationConfiguredModelAlgorithmAssociationRequest

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationConfiguredModelAlgorithmAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PrivacyConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationMLInputChannelRequest

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationMLInputChannelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetCollaborationTrainedModelRequest

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetCollaborationTrainedModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResourceConfig'>
- **Required**: Yes

### stoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StoppingCondition'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredAudienceModelPolicyRequest

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredAudienceModelPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredAudienceModelRequest

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredAudienceModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ConfiguredAudienceModelOutputConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceSizeConfigOutput'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### childResourceTagOnCreatePolicy
- **Type**: typing.Literal['FROM_PARENT_RESOURCE', 'NONE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredModelAlgorithmAssociationRequest

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredModelAlgorithmAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PrivacyConfigurationOutput'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfiguredModelAlgorithmRequest

### configuredModelAlgorithmArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfiguredModelAlgorithmResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ContainerConfigOutput'>
- **Required**: Yes

### inferenceContainerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceContainerConfig'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLConfigurationRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMLConfigurationResponse

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### defaultOutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.MLOutputConfiguration'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetMLInputChannelRequest

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMLInputChannelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InputChannelOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrainedModelInferenceJobRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrainedModelInferenceJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceResourceConfig'>
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceOutputConfigurationOutput'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ModelInferenceDataSource'>
- **Required**: Yes

### containerExecutionParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceContainerExecutionParameters'>
- **Required**: Yes

### statusDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrainedModelRequest

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrainedModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StatusDetails'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResourceConfig'>
- **Required**: Yes

### stoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.StoppingCondition'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ModelTrainingDataChannel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrainingDatasetRequest

### trainingDatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrainingDatasetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.DatasetOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# GlueDataSource

### tableName
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### catalogId
- **Type**: typing.Optional[str]


# InferenceContainerConfig

### imageUri
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceContainerExecutionParameters

### maxPayloadInMB
- **Type**: typing.Optional[int]


# InferenceOutputConfiguration

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceReceiverMember]
- **Required**: Yes

### accept
- **Type**: typing.Optional[str]


# InferenceOutputConfigurationOutput

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceReceiverMember]
- **Required**: Yes

### accept
- **Type**: typing.Optional[str]


# InferenceReceiverMember

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceResourceConfig

### instanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.large', 'ml.c6i.xlarge', 'ml.c7i.12xlarge', 'ml.c7i.16xlarge', 'ml.c7i.24xlarge', 'ml.c7i.2xlarge', 'ml.c7i.48xlarge', 'ml.c7i.4xlarge', 'ml.c7i.8xlarge', 'ml.c7i.large', 'ml.c7i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.m7i.12xlarge', 'ml.m7i.16xlarge', 'ml.m7i.24xlarge', 'ml.m7i.2xlarge', 'ml.m7i.48xlarge', 'ml.m7i.4xlarge', 'ml.m7i.8xlarge', 'ml.m7i.large', 'ml.m7i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.r6i.12xlarge', 'ml.r6i.16xlarge', 'ml.r6i.24xlarge', 'ml.r6i.2xlarge', 'ml.r6i.32xlarge', 'ml.r6i.4xlarge', 'ml.r6i.8xlarge', 'ml.r6i.large', 'ml.r6i.xlarge', 'ml.r7i.12xlarge', 'ml.r7i.16xlarge', 'ml.r7i.24xlarge', 'ml.r7i.2xlarge', 'ml.r7i.48xlarge', 'ml.r7i.4xlarge', 'ml.r7i.8xlarge', 'ml.r7i.large', 'ml.r7i.xlarge']
- **Required**: Yes

### instanceCount
- **Type**: typing.Optional[int]


# InputChannel

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InputChannelDataSource'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# InputChannelDataSource

### protectedQueryInputParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ProtectedQueryInputParameters]


# InputChannelDataSourceOutput

### protectedQueryInputParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ProtectedQueryInputParametersOutput]


# InputChannelOutput

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InputChannelDataSourceOutput'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListAudienceExportJobsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### audienceGenerationJobArn
- **Type**: typing.Optional[str]


# ListAudienceExportJobsRequestPaginate

### audienceGenerationJobArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListAudienceExportJobsResponse

### audienceExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAudienceGenerationJobsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### configuredAudienceModelArn
- **Type**: typing.Optional[str]

### collaborationId
- **Type**: typing.Optional[str]


# ListAudienceGenerationJobsRequestPaginate

### configuredAudienceModelArn
- **Type**: typing.Optional[str]

### collaborationId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListAudienceGenerationJobsResponse

### audienceGenerationJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceGenerationJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAudienceModelsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAudienceModelsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListAudienceModelsResponse

### audienceModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationConfiguredModelAlgorithmAssociationsRequest

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListCollaborationConfiguredModelAlgorithmAssociationsResponse

### collaborationConfiguredModelAlgorithmAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.CollaborationConfiguredModelAlgorithmAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationMLInputChannelsRequest

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationMLInputChannelsRequestPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListCollaborationMLInputChannelsResponse

### collaborationMLInputChannelsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.CollaborationMLInputChannelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationTrainedModelExportJobsRequest

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


# ListCollaborationTrainedModelExportJobsRequestPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListCollaborationTrainedModelExportJobsResponse

### collaborationTrainedModelExportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.CollaborationTrainedModelExportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationTrainedModelInferenceJobsRequest

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### trainedModelArn
- **Type**: typing.Optional[str]


# ListCollaborationTrainedModelInferenceJobsRequestPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListCollaborationTrainedModelInferenceJobsResponse

### collaborationTrainedModelInferenceJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.CollaborationTrainedModelInferenceJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCollaborationTrainedModelsRequest

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCollaborationTrainedModelsRequestPaginate

### collaborationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListCollaborationTrainedModelsResponse

### collaborationTrainedModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.CollaborationTrainedModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredAudienceModelsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredAudienceModelsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListConfiguredAudienceModelsResponse

### configuredAudienceModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ConfiguredAudienceModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredModelAlgorithmAssociationsRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredModelAlgorithmAssociationsRequestPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListConfiguredModelAlgorithmAssociationsResponse

### configuredModelAlgorithmAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ConfiguredModelAlgorithmAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConfiguredModelAlgorithmsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListConfiguredModelAlgorithmsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListConfiguredModelAlgorithmsResponse

### configuredModelAlgorithms
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ConfiguredModelAlgorithmSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMLInputChannelsRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListMLInputChannelsRequestPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListMLInputChannelsResponse

### mlInputChannelsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.MLInputChannelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrainedModelInferenceJobsRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### trainedModelArn
- **Type**: typing.Optional[str]


# ListTrainedModelInferenceJobsRequestPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### trainedModelArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListTrainedModelInferenceJobsResponse

### trainedModelInferenceJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelInferenceJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTrainedModelsRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTrainedModelsRequestPaginate

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListTrainedModelsResponse

### trainedModels
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTrainingDatasetsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTrainingDatasetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PaginatorConfig]


# ListTrainingDatasetsResponse

### trainingDatasets
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainingDatasetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogsConfigurationPolicy

### allowedAccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### filterPattern
- **Type**: typing.Optional[str]


# LogsConfigurationPolicyOutput

### allowedAccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### filterPattern
- **Type**: typing.Optional[str]


# MLInputChannelSummary

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


# MLOutputConfiguration

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.Destination]


# MetricDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### regex
- **Type**: <class 'str'>
- **Required**: Yes


# MetricsConfigurationPolicy

### noiseLevel
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes


# ModelInferenceDataSource

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes


# ModelTrainingDataChannel

### mlInputChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### channelName
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrivacyConfiguration

### policies
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PrivacyConfigurationPolicies'>
- **Required**: Yes


# PrivacyConfigurationOutput

### policies
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.PrivacyConfigurationPoliciesOutput'>
- **Required**: Yes


# PrivacyConfigurationPolicies

### trainedModels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelsConfigurationPolicy]

### trainedModelExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportsConfigurationPolicy]

### trainedModelInferenceJobs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelInferenceJobsConfigurationPolicy]


# PrivacyConfigurationPoliciesOutput

### trainedModels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelsConfigurationPolicyOutput]

### trainedModelExports
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportsConfigurationPolicyOutput]

### trainedModelInferenceJobs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelInferenceJobsConfigurationPolicyOutput]


# ProtectedQueryInputParameters

### sqlParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ProtectedQuerySQLParameters'>
- **Required**: Yes

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ComputeConfiguration]


# ProtectedQueryInputParametersOutput

### sqlParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ProtectedQuerySQLParametersOutput'>
- **Required**: Yes

### computeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ComputeConfiguration]


# ProtectedQuerySQLParameters

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ProtectedQuerySQLParametersOutput

### queryString
- **Type**: typing.Optional[str]

### analysisTemplateArn
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutConfiguredAudienceModelPolicyRequest

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


# PutConfiguredAudienceModelPolicyResponse

### configuredAudienceModelPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### policyHash
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# PutMLConfigurationRequest

### membershipIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### defaultOutputLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.MLOutputConfiguration'>
- **Required**: Yes


# RelevanceMetric

### audienceSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceSize'>
- **Required**: Yes

### score
- **Type**: typing.Optional[float]


# ResourceConfig

### instanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.c6i.12xlarge', 'ml.c6i.16xlarge', 'ml.c6i.24xlarge', 'ml.c6i.2xlarge', 'ml.c6i.32xlarge', 'ml.c6i.4xlarge', 'ml.c6i.8xlarge', 'ml.c6i.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.g5.12xlarge', 'ml.g5.16xlarge', 'ml.g5.24xlarge', 'ml.g5.2xlarge', 'ml.g5.48xlarge', 'ml.g5.4xlarge', 'ml.g5.8xlarge', 'ml.g5.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.m6i.12xlarge', 'ml.m6i.16xlarge', 'ml.m6i.24xlarge', 'ml.m6i.2xlarge', 'ml.m6i.32xlarge', 'ml.m6i.4xlarge', 'ml.m6i.8xlarge', 'ml.m6i.large', 'ml.m6i.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge', 'ml.p4de.24xlarge', 'ml.p5.48xlarge', 'ml.r5.12xlarge', 'ml.r5.16xlarge', 'ml.r5.24xlarge', 'ml.r5.2xlarge', 'ml.r5.4xlarge', 'ml.r5.8xlarge', 'ml.r5.large', 'ml.r5.xlarge', 'ml.r5d.12xlarge', 'ml.r5d.16xlarge', 'ml.r5d.24xlarge', 'ml.r5d.2xlarge', 'ml.r5d.4xlarge', 'ml.r5d.8xlarge', 'ml.r5d.large', 'ml.r5d.xlarge', 'ml.t3.2xlarge', 'ml.t3.large', 'ml.t3.medium', 'ml.t3.xlarge', 'ml.trn1.2xlarge', 'ml.trn1.32xlarge', 'ml.trn1n.32xlarge']
- **Required**: Yes

### volumeSizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### instanceCount
- **Type**: typing.Optional[int]


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


# S3ConfigMap

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# StartAudienceExportJobRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### audienceSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceSize'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartAudienceGenerationJobRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### seedAudience
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceGenerationJobDataSource, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceGenerationJobDataSourceOutput]
- **Required**: Yes

### includeSeedInOutput
- **Type**: typing.Optional[bool]

### collaborationId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartAudienceGenerationJobResponse

### audienceGenerationJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# StartTrainedModelExportJobRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportOutputConfiguration, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportOutputConfigurationOutput]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StartTrainedModelInferenceJobRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceResourceConfig'>
- **Required**: Yes

### outputConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceOutputConfiguration, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceOutputConfigurationOutput]
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ModelInferenceDataSource'>
- **Required**: Yes

### configuredModelAlgorithmAssociationArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### containerExecutionParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceContainerExecutionParameters]

### environment
- **Type**: typing.Optional[typing.Dict[str, str]]

### kmsKeyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartTrainedModelInferenceJobResponse

### trainedModelInferenceJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# StatusDetails

### statusCode
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# StoppingCondition

### maxRuntimeInSeconds
- **Type**: typing.Optional[int]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TrainedModelExportOutputConfiguration

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportReceiverMember]
- **Required**: Yes


# TrainedModelExportOutputConfigurationOutput

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportReceiverMember]
- **Required**: Yes


# TrainedModelExportReceiverMember

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# TrainedModelExportsConfigurationPolicy

### maxSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportsMaxSize'>
- **Required**: Yes

### filesToExport
- **Type**: typing.List[typing.Literal['MODEL', 'OUTPUT']]
- **Required**: Yes


# TrainedModelExportsConfigurationPolicyOutput

### maxSize
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelExportsMaxSize'>
- **Required**: Yes

### filesToExport
- **Type**: typing.List[typing.Literal['MODEL', 'OUTPUT']]
- **Required**: Yes


# TrainedModelExportsMaxSize

### unit
- **Type**: typing.Literal['GB']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# TrainedModelInferenceJobSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.InferenceOutputConfigurationOutput'>
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


# TrainedModelInferenceJobsConfigurationPolicy

### containerLogs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.LogsConfigurationPolicy]]

### maxOutputSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelInferenceMaxOutputSize]


# TrainedModelInferenceJobsConfigurationPolicyOutput

### containerLogs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.LogsConfigurationPolicyOutput]]

### maxOutputSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.TrainedModelInferenceMaxOutputSize]


# TrainedModelInferenceMaxOutputSize

### unit
- **Type**: typing.Literal['GB']
- **Required**: Yes

### value
- **Type**: <class 'float'>
- **Required**: Yes


# TrainedModelSummary

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


# TrainedModelsConfigurationPolicy

### containerLogs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.LogsConfigurationPolicy]]

### containerMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.MetricsConfigurationPolicy]


# TrainedModelsConfigurationPolicyOutput

### containerLogs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.LogsConfigurationPolicyOutput]]

### containerMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.MetricsConfigurationPolicy]


# TrainingDatasetSummary

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


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateConfiguredAudienceModelRequest

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ConfiguredAudienceModelOutputConfig]

### audienceModelArn
- **Type**: typing.Optional[str]

### sharedAudienceMetrics
- **Type**: typing.Optional[typing.List[typing.Literal['ALL', 'NONE']]]

### minMatchingSeedSize
- **Type**: typing.Optional[int]

### audienceSizeConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceSizeConfig, aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.AudienceSizeConfigOutput, NoneType]

### description
- **Type**: typing.Optional[str]


# UpdateConfiguredAudienceModelResponse

### configuredAudienceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_classes.ResponseMetadata'>
- **Required**: Yes


# WorkerComputeConfiguration

### type
- **Type**: typing.Optional[typing.Literal['CR.1X', 'CR.4X']]

### number
- **Type**: typing.Optional[int]



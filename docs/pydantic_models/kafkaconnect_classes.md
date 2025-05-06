# Kafkaconnect Classes

# ApacheKafkaCluster

### bootstrapServers
- **Type**: <class 'str'>
- **Required**: Yes

### vpc
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.Vpc'>
- **Required**: Yes


# ApacheKafkaClusterDescription

### bootstrapServers
- **Type**: typing.Optional[str]

### vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.VpcDescription]


# AutoScaling

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### mcuCount
- **Type**: <class 'int'>
- **Required**: Yes

### minWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### scaleInPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ScaleInPolicy]

### scaleOutPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ScaleOutPolicy]


# AutoScalingDescription

### maxWorkerCount
- **Type**: typing.Optional[int]

### mcuCount
- **Type**: typing.Optional[int]

### minWorkerCount
- **Type**: typing.Optional[int]

### scaleInPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ScaleInPolicyDescription]

### scaleOutPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ScaleOutPolicyDescription]


# AutoScalingUpdate

### maxWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### mcuCount
- **Type**: <class 'int'>
- **Required**: Yes

### minWorkerCount
- **Type**: <class 'int'>
- **Required**: Yes

### scaleInPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ScaleInPolicyUpdate'>
- **Required**: Yes

### scaleOutPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ScaleOutPolicyUpdate'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Capacity

### autoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.AutoScaling]

### provisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ProvisionedCapacity]


# CapacityDescription

### autoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.AutoScalingDescription]

### provisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ProvisionedCapacityDescription]


# CapacityUpdate

### autoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.AutoScalingUpdate]

### provisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ProvisionedCapacityUpdate]


# CloudWatchLogsLogDelivery

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### logGroup
- **Type**: typing.Optional[str]


# CloudWatchLogsLogDeliveryDescription

### enabled
- **Type**: typing.Optional[bool]

### logGroup
- **Type**: typing.Optional[str]


# ConnectorOperationStep

### stepType
- **Type**: typing.Optional[typing.Literal['FINALIZE_UPDATE', 'INITIALIZE_UPDATE', 'UPDATE_CONNECTOR_CONFIGURATION', 'UPDATE_WORKER_SETTING', 'VALIDATE_UPDATE']]

### stepState
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PENDING']]


# ConnectorOperationSummary

### connectorOperationArn
- **Type**: typing.Optional[str]

### connectorOperationType
- **Type**: typing.Optional[typing.Literal['ISOLATE_CONNECTOR', 'RESTORE_CONNECTOR', 'UPDATE_CONNECTOR_CONFIGURATION', 'UPDATE_WORKER_SETTING']]

### connectorOperationState
- **Type**: typing.Optional[typing.Literal['PENDING', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# ConnectorSummary

### capacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CapacityDescription]

### connectorArn
- **Type**: typing.Optional[str]

### connectorDescription
- **Type**: typing.Optional[str]

### connectorName
- **Type**: typing.Optional[str]

### connectorState
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### currentVersion
- **Type**: typing.Optional[str]

### kafkaCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaClusterDescription]

### kafkaClusterClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaClusterClientAuthenticationDescription]

### kafkaClusterEncryptionInTransit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaClusterEncryptionInTransitDescription]

### kafkaConnectVersion
- **Type**: typing.Optional[str]

### logDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.LogDeliveryDescription]

### plugins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.PluginDescription]]

### serviceExecutionRoleArn
- **Type**: typing.Optional[str]

### workerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerConfigurationDescription]


# CreateConnectorRequest

### capacity
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.Capacity'>
- **Required**: Yes

### connectorConfiguration
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### connectorName
- **Type**: <class 'str'>
- **Required**: Yes

### kafkaCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaCluster'>
- **Required**: Yes

### kafkaClusterClientAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaClusterClientAuthentication'>
- **Required**: Yes

### kafkaClusterEncryptionInTransit
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaClusterEncryptionInTransit'>
- **Required**: Yes

### kafkaConnectVersion
- **Type**: <class 'str'>
- **Required**: Yes

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.Plugin]
- **Required**: Yes

### serviceExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorDescription
- **Type**: typing.Optional[str]

### logDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.LogDelivery]

### workerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConnectorResponse

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorName
- **Type**: <class 'str'>
- **Required**: Yes

### connectorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomPluginRequest

### contentType
- **Type**: typing.Literal['JAR', 'ZIP']
- **Required**: Yes

### location
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CustomPluginLocation'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCustomPluginResponse

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### customPluginState
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkerConfigurationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### propertiesFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateWorkerConfigurationResponse

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### latestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerConfigurationRevisionSummary'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### workerConfigurationState
- **Type**: typing.Literal['ACTIVE', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CustomPlugin

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'int'>
- **Required**: Yes


# CustomPluginDescription

### customPluginArn
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[int]


# CustomPluginFileDescription

### fileMd5
- **Type**: typing.Optional[str]

### fileSize
- **Type**: typing.Optional[int]


# CustomPluginLocation

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.S3Location'>
- **Required**: Yes


# CustomPluginLocationDescription

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.S3LocationDescription]


# CustomPluginRevisionSummary

### contentType
- **Type**: typing.Optional[typing.Literal['JAR', 'ZIP']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### fileDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CustomPluginFileDescription]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CustomPluginLocationDescription]

### revision
- **Type**: typing.Optional[int]


# CustomPluginSummary

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### customPluginArn
- **Type**: typing.Optional[str]

### customPluginState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### description
- **Type**: typing.Optional[str]

### latestRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CustomPluginRevisionSummary]

### name
- **Type**: typing.Optional[str]


# DeleteConnectorRequest

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentVersion
- **Type**: typing.Optional[str]


# DeleteConnectorResponse

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCustomPluginRequest

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomPluginResponse

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### customPluginState
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkerConfigurationRequest

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkerConfigurationResponse

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### workerConfigurationState
- **Type**: typing.Literal['ACTIVE', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectorOperationRequest

### connectorOperationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectorOperationResponse

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorOperationState
- **Type**: typing.Literal['PENDING', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### connectorOperationType
- **Type**: typing.Literal['ISOLATE_CONNECTOR', 'RESTORE_CONNECTOR', 'UPDATE_CONNECTOR_CONFIGURATION', 'UPDATE_WORKER_SETTING']
- **Required**: Yes

### operationSteps
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ConnectorOperationStep]
- **Required**: Yes

### originWorkerSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerSetting'>
- **Required**: Yes

### originConnectorConfiguration
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### targetWorkerSetting
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerSetting'>
- **Required**: Yes

### targetConnectorConfiguration
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### errorInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.StateDescription'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectorRequest

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectorResponse

### capacity
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CapacityDescription'>
- **Required**: Yes

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorConfiguration
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### connectorDescription
- **Type**: <class 'str'>
- **Required**: Yes

### connectorName
- **Type**: <class 'str'>
- **Required**: Yes

### connectorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### currentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### kafkaCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaClusterDescription'>
- **Required**: Yes

### kafkaClusterClientAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaClusterClientAuthenticationDescription'>
- **Required**: Yes

### kafkaClusterEncryptionInTransit
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.KafkaClusterEncryptionInTransitDescription'>
- **Required**: Yes

### kafkaConnectVersion
- **Type**: <class 'str'>
- **Required**: Yes

### logDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.LogDeliveryDescription'>
- **Required**: Yes

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.PluginDescription]
- **Required**: Yes

### serviceExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### workerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerConfigurationDescription'>
- **Required**: Yes

### stateDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.StateDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCustomPluginRequest

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomPluginResponse

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### customPluginState
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### latestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CustomPluginRevisionSummary'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stateDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.StateDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkerConfigurationRequest

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkerConfigurationResponse

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### latestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerConfigurationRevisionDescription'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### workerConfigurationState
- **Type**: typing.Literal['ACTIVE', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# FirehoseLogDelivery

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### deliveryStream
- **Type**: typing.Optional[str]


# FirehoseLogDeliveryDescription

### deliveryStream
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]


# KafkaCluster

### apacheKafkaCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ApacheKafkaCluster'>
- **Required**: Yes


# KafkaClusterClientAuthentication

### authenticationType
- **Type**: typing.Literal['IAM', 'NONE']
- **Required**: Yes


# KafkaClusterClientAuthenticationDescription

### authenticationType
- **Type**: typing.Optional[typing.Literal['IAM', 'NONE']]


# KafkaClusterDescription

### apacheKafkaCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ApacheKafkaClusterDescription]


# KafkaClusterEncryptionInTransit

### encryptionType
- **Type**: typing.Literal['PLAINTEXT', 'TLS']
- **Required**: Yes


# KafkaClusterEncryptionInTransitDescription

### encryptionType
- **Type**: typing.Optional[typing.Literal['PLAINTEXT', 'TLS']]


# ListConnectorOperationsRequest

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorOperationsRequestPaginate

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.PaginatorConfig]


# ListConnectorOperationsResponse

### connectorOperations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ConnectorOperationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequest

### connectorNamePrefix
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequestPaginate

### connectorNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.PaginatorConfig]


# ListConnectorsResponse

### connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ConnectorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCustomPluginsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### namePrefix
- **Type**: typing.Optional[str]


# ListCustomPluginsRequestPaginate

### namePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.PaginatorConfig]


# ListCustomPluginsResponse

### customPlugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CustomPluginSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ListWorkerConfigurationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### namePrefix
- **Type**: typing.Optional[str]


# ListWorkerConfigurationsRequestPaginate

### namePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.PaginatorConfig]


# ListWorkerConfigurationsResponse

### workerConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LogDelivery

### workerLogDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerLogDelivery'>
- **Required**: Yes


# LogDeliveryDescription

### workerLogDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerLogDeliveryDescription]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Plugin

### customPlugin
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CustomPlugin'>
- **Required**: Yes


# PluginDescription

### customPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CustomPluginDescription]


# ProvisionedCapacity

### mcuCount
- **Type**: <class 'int'>
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes


# ProvisionedCapacityDescription

### mcuCount
- **Type**: typing.Optional[int]

### workerCount
- **Type**: typing.Optional[int]


# ProvisionedCapacityUpdate

### mcuCount
- **Type**: <class 'int'>
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes


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


# S3Location

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### fileKey
- **Type**: <class 'str'>
- **Required**: Yes

### objectVersion
- **Type**: typing.Optional[str]


# S3LocationDescription

### bucketArn
- **Type**: typing.Optional[str]

### fileKey
- **Type**: typing.Optional[str]

### objectVersion
- **Type**: typing.Optional[str]


# S3LogDelivery

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# S3LogDeliveryDescription

### bucket
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### prefix
- **Type**: typing.Optional[str]


# ScaleInPolicy

### cpuUtilizationPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# ScaleInPolicyDescription

### cpuUtilizationPercentage
- **Type**: typing.Optional[int]


# ScaleInPolicyUpdate

### cpuUtilizationPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# ScaleOutPolicy

### cpuUtilizationPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# ScaleOutPolicyDescription

### cpuUtilizationPercentage
- **Type**: typing.Optional[int]


# ScaleOutPolicyUpdate

### cpuUtilizationPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# StateDescription

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateConnectorRequest

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### capacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CapacityUpdate]

### connectorConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateConnectorResponse

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### connectorOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.ResponseMetadata'>
- **Required**: Yes


# Vpc

### subnets
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.List[str]]


# VpcDescription

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### subnets
- **Type**: typing.Optional[typing.List[str]]


# WorkerConfiguration

### revision
- **Type**: <class 'int'>
- **Required**: Yes

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# WorkerConfigurationDescription

### revision
- **Type**: typing.Optional[int]

### workerConfigurationArn
- **Type**: typing.Optional[str]


# WorkerConfigurationRevisionDescription

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### propertiesFileContent
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[int]


# WorkerConfigurationRevisionSummary

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[int]


# WorkerConfigurationSummary

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### latestRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.WorkerConfigurationRevisionSummary]

### name
- **Type**: typing.Optional[str]

### workerConfigurationArn
- **Type**: typing.Optional[str]

### workerConfigurationState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]


# WorkerLogDelivery

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CloudWatchLogsLogDelivery]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.FirehoseLogDelivery]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.S3LogDelivery]


# WorkerLogDeliveryDescription

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CloudWatchLogsLogDeliveryDescription]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.FirehoseLogDeliveryDescription]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.S3LogDeliveryDescription]


# WorkerSetting

### capacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect.kafkaconnect_classes.CapacityDescription]



# Pydantic Models in kafkaconnect_classes

# ApacheKafkaClusterDescriptionTypeDef

### bootstrapServers
- **Type**: typing.Optional[str]

### vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.VpcDescriptionTypeDef]


# ApacheKafkaClusterTypeDef

### bootstrapServers
- **Type**: <class 'str'>
- **Required**: Yes

### vpc
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.VpcTypeDef'>
- **Required**: Yes


# AutoScalingDescriptionTypeDef

### maxWorkerCount
- **Type**: typing.Optional[int]

### mcuCount
- **Type**: typing.Optional[int]

### minWorkerCount
- **Type**: typing.Optional[int]

### scaleInPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.ScaleInPolicyDescriptionTypeDef]

### scaleOutPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.ScaleOutPolicyDescriptionTypeDef]


# AutoScalingTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.ScaleInPolicyTypeDef]

### scaleOutPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.ScaleOutPolicyTypeDef]


# AutoScalingUpdateTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ScaleInPolicyUpdateTypeDef'>
- **Required**: Yes

### scaleOutPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ScaleOutPolicyUpdateTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityDescriptionTypeDef

### autoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.AutoScalingDescriptionTypeDef]

### provisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.ProvisionedCapacityDescriptionTypeDef]


# CapacityTypeDef

### autoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.AutoScalingTypeDef]

### provisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.ProvisionedCapacityTypeDef]


# CapacityUpdateTypeDef

### autoScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.AutoScalingUpdateTypeDef]

### provisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.ProvisionedCapacityUpdateTypeDef]


# CloudWatchLogsLogDeliveryDescriptionTypeDef

### enabled
- **Type**: typing.Optional[bool]

### logGroup
- **Type**: typing.Optional[str]


# CloudWatchLogsLogDeliveryTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### logGroup
- **Type**: typing.Optional[str]


# ConnectorSummaryTypeDef

### capacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.CapacityDescriptionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterDescriptionTypeDef]

### kafkaClusterClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterClientAuthenticationDescriptionTypeDef]

### kafkaClusterEncryptionInTransit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterEncryptionInTransitDescriptionTypeDef]

### kafkaConnectVersion
- **Type**: typing.Optional[str]

### logDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.LogDeliveryDescriptionTypeDef]

### plugins
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafkaconnect_classes.PluginDescriptionTypeDef]]

### serviceExecutionRoleArn
- **Type**: typing.Optional[str]

### workerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerConfigurationDescriptionTypeDef]


# CreateConnectorRequestRequestTypeDef

### capacity
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.CapacityTypeDef'>
- **Required**: Yes

### connectorConfiguration
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### connectorName
- **Type**: <class 'str'>
- **Required**: Yes

### kafkaCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterTypeDef'>
- **Required**: Yes

### kafkaClusterClientAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterClientAuthenticationTypeDef'>
- **Required**: Yes

### kafkaClusterEncryptionInTransit
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterEncryptionInTransitTypeDef'>
- **Required**: Yes

### kafkaConnectVersion
- **Type**: <class 'str'>
- **Required**: Yes

### plugins
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kafkaconnect_classes.PluginTypeDef]
- **Required**: Yes

### serviceExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorDescription
- **Type**: typing.Optional[str]

### logDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.LogDeliveryTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### workerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerConfigurationTypeDef]


# CreateConnectorResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomPluginRequestRequestTypeDef

### contentType
- **Type**: typing.Literal['JAR', 'ZIP']
- **Required**: Yes

### location
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.CustomPluginLocationTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCustomPluginResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkerConfigurationRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### propertiesFileContent
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateWorkerConfigurationResponseTypeDef

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### latestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerConfigurationRevisionSummaryTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomPluginDescriptionTypeDef

### customPluginArn
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[int]


# CustomPluginFileDescriptionTypeDef

### fileMd5
- **Type**: typing.Optional[str]

### fileSize
- **Type**: typing.Optional[int]


# CustomPluginLocationDescriptionTypeDef

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.S3LocationDescriptionTypeDef]


# CustomPluginLocationTypeDef

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.S3LocationTypeDef'>
- **Required**: Yes


# CustomPluginRevisionSummaryTypeDef

### contentType
- **Type**: typing.Optional[typing.Literal['JAR', 'ZIP']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### fileDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.CustomPluginFileDescriptionTypeDef]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.CustomPluginLocationDescriptionTypeDef]

### revision
- **Type**: typing.Optional[int]


# CustomPluginSummaryTypeDef

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### customPluginArn
- **Type**: typing.Optional[str]

### customPluginState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### description
- **Type**: typing.Optional[str]

### latestRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.CustomPluginRevisionSummaryTypeDef]

### name
- **Type**: typing.Optional[str]


# CustomPluginTypeDef

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteConnectorRequestRequestTypeDef

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentVersion
- **Type**: typing.Optional[str]


# DeleteConnectorResponseTypeDef

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomPluginRequestRequestTypeDef

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCustomPluginResponseTypeDef

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes

### customPluginState
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkerConfigurationRequestRequestTypeDef

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkerConfigurationResponseTypeDef

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### workerConfigurationState
- **Type**: typing.Literal['ACTIVE', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectorRequestRequestTypeDef

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConnectorResponseTypeDef

### capacity
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.CapacityDescriptionTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterDescriptionTypeDef'>
- **Required**: Yes

### kafkaClusterClientAuthentication
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterClientAuthenticationDescriptionTypeDef'>
- **Required**: Yes

### kafkaClusterEncryptionInTransit
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.KafkaClusterEncryptionInTransitDescriptionTypeDef'>
- **Required**: Yes

### kafkaConnectVersion
- **Type**: <class 'str'>
- **Required**: Yes

### logDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.LogDeliveryDescriptionTypeDef'>
- **Required**: Yes

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect_classes.PluginDescriptionTypeDef]
- **Required**: Yes

### serviceExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.StateDescriptionTypeDef'>
- **Required**: Yes

### workerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerConfigurationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCustomPluginRequestRequestTypeDef

### customPluginArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCustomPluginResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.CustomPluginRevisionSummaryTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stateDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.StateDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkerConfigurationRequestRequestTypeDef

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkerConfigurationResponseTypeDef

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### latestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerConfigurationRevisionDescriptionTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FirehoseLogDeliveryDescriptionTypeDef

### deliveryStream
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]


# FirehoseLogDeliveryTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### deliveryStream
- **Type**: typing.Optional[str]


# KafkaClusterClientAuthenticationDescriptionTypeDef

### authenticationType
- **Type**: typing.Optional[typing.Literal['IAM', 'NONE']]


# KafkaClusterClientAuthenticationTypeDef

### authenticationType
- **Type**: typing.Literal['IAM', 'NONE']
- **Required**: Yes


# KafkaClusterDescriptionTypeDef

### apacheKafkaCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.ApacheKafkaClusterDescriptionTypeDef]


# KafkaClusterEncryptionInTransitDescriptionTypeDef

### encryptionType
- **Type**: typing.Optional[typing.Literal['PLAINTEXT', 'TLS']]


# KafkaClusterEncryptionInTransitTypeDef

### encryptionType
- **Type**: typing.Literal['PLAINTEXT', 'TLS']
- **Required**: Yes


# KafkaClusterTypeDef

### apacheKafkaCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ApacheKafkaClusterTypeDef'>
- **Required**: Yes


# ListConnectorsRequestListConnectorsPaginateTypeDef

### connectorNamePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.PaginatorConfigTypeDef]


# ListConnectorsRequestRequestTypeDef

### connectorNamePrefix
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsResponseTypeDef

### connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect_classes.ConnectorSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomPluginsRequestListCustomPluginsPaginateTypeDef

### namePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.PaginatorConfigTypeDef]


# ListCustomPluginsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### namePrefix
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomPluginsResponseTypeDef

### customPlugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect_classes.CustomPluginSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkerConfigurationsRequestListWorkerConfigurationsPaginateTypeDef

### namePrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.PaginatorConfigTypeDef]


# ListWorkerConfigurationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### namePrefix
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkerConfigurationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workerConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogDeliveryDescriptionTypeDef

### workerLogDelivery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerLogDeliveryDescriptionTypeDef]


# LogDeliveryTypeDef

### workerLogDelivery
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerLogDeliveryTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PluginDescriptionTypeDef

### customPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.CustomPluginDescriptionTypeDef]


# PluginTypeDef

### customPlugin
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.CustomPluginTypeDef'>
- **Required**: Yes


# ProvisionedCapacityDescriptionTypeDef

### mcuCount
- **Type**: typing.Optional[int]

### workerCount
- **Type**: typing.Optional[int]


# ProvisionedCapacityTypeDef

### mcuCount
- **Type**: <class 'int'>
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes


# ProvisionedCapacityUpdateTypeDef

### mcuCount
- **Type**: <class 'int'>
- **Required**: Yes

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes


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


# S3LocationDescriptionTypeDef

### bucketArn
- **Type**: typing.Optional[str]

### fileKey
- **Type**: typing.Optional[str]

### objectVersion
- **Type**: typing.Optional[str]


# S3LocationTypeDef

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### fileKey
- **Type**: <class 'str'>
- **Required**: Yes

### objectVersion
- **Type**: typing.Optional[str]


# S3LogDeliveryDescriptionTypeDef

### bucket
- **Type**: typing.Optional[str]

### enabled
- **Type**: typing.Optional[bool]

### prefix
- **Type**: typing.Optional[str]


# S3LogDeliveryTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### bucket
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ScaleInPolicyDescriptionTypeDef

### cpuUtilizationPercentage
- **Type**: typing.Optional[int]


# ScaleInPolicyTypeDef

### cpuUtilizationPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# ScaleInPolicyUpdateTypeDef

### cpuUtilizationPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# ScaleOutPolicyDescriptionTypeDef

### cpuUtilizationPercentage
- **Type**: typing.Optional[int]


# ScaleOutPolicyTypeDef

### cpuUtilizationPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# ScaleOutPolicyUpdateTypeDef

### cpuUtilizationPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# StateDescriptionTypeDef

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectorRequestRequestTypeDef

### capacity
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.CapacityUpdateTypeDef'>
- **Required**: Yes

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### currentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateConnectorResponseTypeDef

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### connectorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafkaconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcDescriptionTypeDef

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### subnets
- **Type**: typing.Optional[typing.List[str]]


# VpcTypeDef

### subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# WorkerConfigurationDescriptionTypeDef

### revision
- **Type**: typing.Optional[int]

### workerConfigurationArn
- **Type**: typing.Optional[str]


# WorkerConfigurationRevisionDescriptionTypeDef

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### propertiesFileContent
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[int]


# WorkerConfigurationRevisionSummaryTypeDef

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[int]


# WorkerConfigurationSummaryTypeDef

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### latestRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.WorkerConfigurationRevisionSummaryTypeDef]

### name
- **Type**: typing.Optional[str]

### workerConfigurationArn
- **Type**: typing.Optional[str]

### workerConfigurationState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING']]


# WorkerConfigurationTypeDef

### revision
- **Type**: <class 'int'>
- **Required**: Yes

### workerConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# WorkerLogDeliveryDescriptionTypeDef

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.CloudWatchLogsLogDeliveryDescriptionTypeDef]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.FirehoseLogDeliveryDescriptionTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.S3LogDeliveryDescriptionTypeDef]


# WorkerLogDeliveryTypeDef

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.CloudWatchLogsLogDeliveryTypeDef]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.FirehoseLogDeliveryTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafkaconnect_classes.S3LogDeliveryTypeDef]


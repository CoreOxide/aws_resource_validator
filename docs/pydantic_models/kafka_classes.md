# Kafka Classes

# AmazonMskClusterTypeDef

### MskClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateScramSecretRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArnList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchAssociateScramSecretResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### UnprocessedScramSecrets
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.UnprocessedScramSecretTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDisassociateScramSecretRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArnList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDisassociateScramSecretResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### UnprocessedScramSecrets
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.UnprocessedScramSecretTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrokerCountUpdateInfoTypeDef

### CreatedBrokerIds
- **Type**: typing.Optional[typing.List[float]]

### DeletedBrokerIds
- **Type**: typing.Optional[typing.List[float]]


# BrokerEBSVolumeInfoTypeDef

### KafkaBrokerNodeId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ProvisionedThroughputTypeDef]

### VolumeSizeGB
- **Type**: typing.Optional[int]


# BrokerLogsTypeDef

### CloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.CloudWatchLogsTypeDef]

### Firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.FirehoseTypeDef]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.S3TypeDef]


# BrokerNodeGroupInfoOutputTypeDef

### ClientSubnets
- **Type**: typing.List[str]
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### BrokerAZDistribution
- **Type**: typing.Optional[typing.Literal['DEFAULT']]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### StorageInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.StorageInfoTypeDef]

### ConnectivityInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConnectivityInfoTypeDef]

### ZoneIds
- **Type**: typing.Optional[typing.List[str]]


# BrokerNodeGroupInfoTypeDef

### ClientSubnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### BrokerAZDistribution
- **Type**: typing.Optional[typing.Literal['DEFAULT']]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### StorageInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.StorageInfoTypeDef]

### ConnectivityInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConnectivityInfoTypeDef]

### ZoneIds
- **Type**: typing.Optional[typing.Sequence[str]]


# BrokerNodeGroupInfoUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrokerNodeInfoTypeDef

### AttachedENIId
- **Type**: typing.Optional[str]

### BrokerId
- **Type**: typing.Optional[float]

### ClientSubnet
- **Type**: typing.Optional[str]

### ClientVpcIpAddress
- **Type**: typing.Optional[str]

### CurrentBrokerSoftwareInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.BrokerSoftwareInfoTypeDef]

### Endpoints
- **Type**: typing.Optional[typing.List[str]]


# BrokerSoftwareInfoTypeDef

### ConfigurationArn
- **Type**: typing.Optional[str]

### ConfigurationRevision
- **Type**: typing.Optional[int]

### KafkaVersion
- **Type**: typing.Optional[str]


# ClientAuthenticationOutputTypeDef

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.SaslTypeDef]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.TlsOutputTypeDef]

### Unauthenticated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.UnauthenticatedTypeDef]


# ClientAuthenticationTypeDef

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.SaslTypeDef]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.TlsUnionTypeDef]

### Unauthenticated
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.UnauthenticatedTypeDef]


# ClientAuthenticationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientVpcConnectionTypeDef

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Authentication
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DEACTIVATING', 'DELETING', 'FAILED', 'INACTIVE', 'REJECTED', 'REJECTING']]

### Owner
- **Type**: typing.Optional[str]


# CloudWatchLogsTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### LogGroup
- **Type**: typing.Optional[str]


# ClusterInfoTypeDef

### ActiveOperationArn
- **Type**: typing.Optional[str]

### BrokerNodeGroupInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.BrokerNodeGroupInfoOutputTypeDef]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClientAuthenticationOutputTypeDef]

### ClusterArn
- **Type**: typing.Optional[str]

### ClusterName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CurrentBrokerSoftwareInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.BrokerSoftwareInfoTypeDef]

### CurrentVersion
- **Type**: typing.Optional[str]

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EncryptionInfoTypeDef]

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.OpenMonitoringTypeDef]

### LoggingInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.LoggingInfoTypeDef]

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'HEALING', 'MAINTENANCE', 'REBOOTING_BROKER', 'UPDATING']]

### StateInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.StateInfoTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ZookeeperConnectString
- **Type**: typing.Optional[str]

### ZookeeperConnectStringTls
- **Type**: typing.Optional[str]

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]

### CustomerActionStatus
- **Type**: typing.Optional[typing.Literal['ACTION_RECOMMENDED', 'CRITICAL_ACTION_REQUIRED', 'NONE']]


# ClusterOperationInfoTypeDef

### ClientRequestId
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### ErrorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ErrorInfoTypeDef]

### OperationArn
- **Type**: typing.Optional[str]

### OperationState
- **Type**: typing.Optional[str]

### OperationSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationStepTypeDef]]

### OperationType
- **Type**: typing.Optional[str]

### SourceClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.MutableClusterInfoTypeDef]

### TargetClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.MutableClusterInfoTypeDef]

### VpcConnectionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectionInfoTypeDef]


# ClusterOperationStepInfoTypeDef

### StepStatus
- **Type**: typing.Optional[str]


# ClusterOperationStepTypeDef

### StepInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationStepInfoTypeDef]

### StepName
- **Type**: typing.Optional[str]


# ClusterOperationV2ProvisionedTypeDef

### OperationSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationStepTypeDef]]

### SourceClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.MutableClusterInfoTypeDef]

### TargetClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.MutableClusterInfoTypeDef]

### VpcConnectionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectionInfoTypeDef]


# ClusterOperationV2ServerlessTypeDef

### VpcConnectionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectionInfoServerlessTypeDef]


# ClusterOperationV2SummaryTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[typing.Literal['PROVISIONED', 'SERVERLESS']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### OperationArn
- **Type**: typing.Optional[str]

### OperationState
- **Type**: typing.Optional[str]

### OperationType
- **Type**: typing.Optional[str]


# ClusterOperationV2TypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[typing.Literal['PROVISIONED', 'SERVERLESS']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### ErrorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ErrorInfoTypeDef]

### OperationArn
- **Type**: typing.Optional[str]

### OperationState
- **Type**: typing.Optional[str]

### OperationType
- **Type**: typing.Optional[str]

### Provisioned
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationV2ProvisionedTypeDef]

### Serverless
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationV2ServerlessTypeDef]


# ClusterTypeDef

### ActiveOperationArn
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[typing.Literal['PROVISIONED', 'SERVERLESS']]

### ClusterArn
- **Type**: typing.Optional[str]

### ClusterName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CurrentVersion
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'HEALING', 'MAINTENANCE', 'REBOOTING_BROKER', 'UPDATING']]

### StateInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.StateInfoTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Provisioned
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ProvisionedTypeDef]

### Serverless
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ServerlessTypeDef]


# CompatibleKafkaVersionTypeDef

### SourceVersion
- **Type**: typing.Optional[str]

### TargetVersions
- **Type**: typing.Optional[typing.List[str]]


# ConfigurationInfoTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes


# ConfigurationRevisionTypeDef

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ConfigurationTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### KafkaVersions
- **Type**: typing.List[str]
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ConfigurationRevisionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes


# ConnectivityInfoTypeDef

### PublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PublicAccessTypeDef]

### VpcConnectivity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectivityTypeDef]


# ConsumerGroupReplicationOutputTypeDef

### ConsumerGroupsToReplicate
- **Type**: typing.List[str]
- **Required**: Yes

### ConsumerGroupsToExclude
- **Type**: typing.Optional[typing.List[str]]

### DetectAndCopyNewConsumerGroups
- **Type**: typing.Optional[bool]

### SynchroniseConsumerGroupOffsets
- **Type**: typing.Optional[bool]


# ConsumerGroupReplicationTypeDef

### ConsumerGroupsToReplicate
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ConsumerGroupsToExclude
- **Type**: typing.Optional[typing.Sequence[str]]

### DetectAndCopyNewConsumerGroups
- **Type**: typing.Optional[bool]

### SynchroniseConsumerGroupOffsets
- **Type**: typing.Optional[bool]


# ConsumerGroupReplicationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConsumerGroupReplicationUpdateTypeDef

### ConsumerGroupsToExclude
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ConsumerGroupsToReplicate
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DetectAndCopyNewConsumerGroups
- **Type**: <class 'bool'>
- **Required**: Yes

### SynchroniseConsumerGroupOffsets
- **Type**: <class 'bool'>
- **Required**: Yes


# ControllerNodeInfoTypeDef

### Endpoints
- **Type**: typing.Optional[typing.List[str]]


# CreateClusterRequestTypeDef

### BrokerNodeGroupInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.BrokerNodeGroupInfoUnionTypeDef'>
- **Required**: Yes

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### KafkaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfBrokerNodes
- **Type**: <class 'int'>
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClientAuthenticationUnionTypeDef]

### ConfigurationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConfigurationInfoTypeDef]

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EncryptionInfoTypeDef]

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.OpenMonitoringInfoTypeDef]

### LoggingInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.LoggingInfoTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]


# CreateClusterResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'HEALING', 'MAINTENANCE', 'REBOOTING_BROKER', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterV2RequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Provisioned
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ProvisionedRequestTypeDef]

### Serverless
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ServerlessRequestTypeDef]


# CreateClusterV2ResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'HEALING', 'MAINTENANCE', 'REBOOTING_BROKER', 'UPDATING']
- **Required**: Yes

### ClusterType
- **Type**: typing.Literal['PROVISIONED', 'SERVERLESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConfigurationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServerProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.BlobTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### KafkaVersions
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ConfigurationRevisionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReplicatorRequestTypeDef

### KafkaClusters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kafka_classes.KafkaClusterTypeDef]
- **Required**: Yes

### ReplicationInfoList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kafka_classes.ReplicationInfoTypeDef]
- **Required**: Yes

### ReplicatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateReplicatorResponseTypeDef

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcConnectionRequestTypeDef

### TargetClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### Authentication
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSubnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVpcConnectionResponseTypeDef

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DEACTIVATING', 'DELETING', 'FAILED', 'INACTIVE', 'REJECTED', 'REJECTING']
- **Required**: Yes

### Authentication
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSubnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterPolicyRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# DeleteClusterResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'HEALING', 'MAINTENANCE', 'REBOOTING_BROKER', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConfigurationRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteReplicatorRequestTypeDef

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# DeleteReplicatorResponseTypeDef

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVpcConnectionRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcConnectionResponseTypeDef

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DEACTIVATING', 'DELETING', 'FAILED', 'INACTIVE', 'REJECTED', 'REJECTING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterOperationRequestTypeDef

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterOperationResponseTypeDef

### ClusterOperationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterOperationV2RequestTypeDef

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterOperationV2ResponseTypeDef

### ClusterOperationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationV2TypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterResponseTypeDef

### ClusterInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ClusterInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClusterV2RequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterV2ResponseTypeDef

### ClusterInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConfigurationRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### KafkaVersions
- **Type**: typing.List[str]
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ConfigurationRevisionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConfigurationRevisionRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeConfigurationRevisionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes

### ServerProperties
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicatorRequestTypeDef

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReplicatorResponseTypeDef

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### IsReplicatorReference
- **Type**: <class 'bool'>
- **Required**: Yes

### KafkaClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.KafkaClusterDescriptionTypeDef]
- **Required**: Yes

### ReplicationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ReplicationInfoDescriptionTypeDef]
- **Required**: Yes

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ServiceExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### StateInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ReplicationStateInfoTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVpcConnectionRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVpcConnectionResponseTypeDef

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DEACTIVATING', 'DELETING', 'FAILED', 'INACTIVE', 'REJECTED', 'REJECTING']
- **Required**: Yes

### Authentication
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EBSStorageInfoTypeDef

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ProvisionedThroughputTypeDef]

### VolumeSize
- **Type**: typing.Optional[int]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionAtRestTypeDef

### DataVolumeKMSKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# EncryptionInTransitTypeDef

### ClientBroker
- **Type**: typing.Optional[typing.Literal['PLAINTEXT', 'TLS', 'TLS_PLAINTEXT']]

### InCluster
- **Type**: typing.Optional[bool]


# EncryptionInfoTypeDef

### EncryptionAtRest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EncryptionAtRestTypeDef]

### EncryptionInTransit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EncryptionInTransitTypeDef]


# ErrorInfoTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorString
- **Type**: typing.Optional[str]


# FirehoseTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### DeliveryStream
- **Type**: typing.Optional[str]


# GetBootstrapBrokersRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetBootstrapBrokersResponseTypeDef

### BootstrapBrokerString
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringTls
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringSaslScram
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringSaslIam
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringPublicTls
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringPublicSaslScram
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringPublicSaslIam
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringVpcConnectivityTls
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringVpcConnectivitySaslScram
- **Type**: <class 'str'>
- **Required**: Yes

### BootstrapBrokerStringVpcConnectivitySaslIam
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetClusterPolicyRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetClusterPolicyResponseTypeDef

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCompatibleKafkaVersionsRequestTypeDef

### ClusterArn
- **Type**: typing.Optional[str]


# GetCompatibleKafkaVersionsResponseTypeDef

### CompatibleKafkaVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.CompatibleKafkaVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IamTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# JmxExporterInfoTypeDef

### EnabledInBroker
- **Type**: <class 'bool'>
- **Required**: Yes


# JmxExporterTypeDef

### EnabledInBroker
- **Type**: <class 'bool'>
- **Required**: Yes


# KafkaClusterClientVpcConfigOutputTypeDef

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# KafkaClusterClientVpcConfigTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# KafkaClusterClientVpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KafkaClusterDescriptionTypeDef

### AmazonMskCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.AmazonMskClusterTypeDef]

### KafkaClusterAlias
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.KafkaClusterClientVpcConfigOutputTypeDef]


# KafkaClusterSummaryTypeDef

### AmazonMskCluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.AmazonMskClusterTypeDef]

### KafkaClusterAlias
- **Type**: typing.Optional[str]


# KafkaClusterTypeDef

### AmazonMskCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.AmazonMskClusterTypeDef'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.KafkaClusterClientVpcConfigUnionTypeDef'>
- **Required**: Yes


# KafkaVersionTypeDef

### Version
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEPRECATED']]


# ListClientVpcConnectionsRequestPaginateTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListClientVpcConnectionsRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClientVpcConnectionsResponseTypeDef

### ClientVpcConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ClientVpcConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClusterOperationsRequestPaginateTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListClusterOperationsRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClusterOperationsResponseTypeDef

### ClusterOperationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClusterOperationsV2RequestPaginateTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListClusterOperationsV2RequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClusterOperationsV2ResponseTypeDef

### ClusterOperationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ClusterOperationV2SummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginateTypeDef

### ClusterNameFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListClustersRequestTypeDef

### ClusterNameFilter
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersResponseTypeDef

### ClusterInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ClusterInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersV2RequestPaginateTypeDef

### ClusterNameFilter
- **Type**: typing.Optional[str]

### ClusterTypeFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListClustersV2RequestTypeDef

### ClusterNameFilter
- **Type**: typing.Optional[str]

### ClusterTypeFilter
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersV2ResponseTypeDef

### ClusterInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRevisionsRequestPaginateTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListConfigurationRevisionsRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRevisionsResponseTypeDef

### Revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ConfigurationRevisionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListConfigurationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsResponseTypeDef

### Configurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKafkaVersionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListKafkaVersionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListKafkaVersionsResponseTypeDef

### KafkaVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.KafkaVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequestPaginateTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListNodesRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNodesResponseTypeDef

### NodeInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.NodeInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReplicatorsRequestPaginateTypeDef

### ReplicatorNameFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListReplicatorsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ReplicatorNameFilter
- **Type**: typing.Optional[str]


# ListReplicatorsResponseTypeDef

### Replicators
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.ReplicatorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListScramSecretsRequestPaginateTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListScramSecretsRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListScramSecretsResponseTypeDef

### SecretArnList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcConnectionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.PaginatorConfigTypeDef]


# ListVpcConnectionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVpcConnectionsResponseTypeDef

### VpcConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoggingInfoTypeDef

### BrokerLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.BrokerLogsTypeDef'>
- **Required**: Yes


# MutableClusterInfoTypeDef

### BrokerEBSVolumeInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka_classes.BrokerEBSVolumeInfoTypeDef]]

### ConfigurationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConfigurationInfoTypeDef]

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.OpenMonitoringTypeDef]

### KafkaVersion
- **Type**: typing.Optional[str]

### LoggingInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.LoggingInfoTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClientAuthenticationOutputTypeDef]

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EncryptionInfoTypeDef]

### ConnectivityInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConnectivityInfoTypeDef]

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]

### BrokerCountUpdateInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.BrokerCountUpdateInfoTypeDef]


# NodeExporterInfoTypeDef

### EnabledInBroker
- **Type**: <class 'bool'>
- **Required**: Yes


# NodeExporterTypeDef

### EnabledInBroker
- **Type**: <class 'bool'>
- **Required**: Yes


# NodeInfoTypeDef

### AddedToClusterTime
- **Type**: typing.Optional[str]

### BrokerNodeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.BrokerNodeInfoTypeDef]

### ControllerNodeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ControllerNodeInfoTypeDef]

### InstanceType
- **Type**: typing.Optional[str]

### NodeARN
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[typing.Literal['BROKER']]

### ZookeeperNodeInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ZookeeperNodeInfoTypeDef]


# OpenMonitoringInfoTypeDef

### Prometheus
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.PrometheusInfoTypeDef'>
- **Required**: Yes


# OpenMonitoringTypeDef

### Prometheus
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.PrometheusTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrometheusInfoTypeDef

### JmxExporter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.JmxExporterInfoTypeDef]

### NodeExporter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.NodeExporterInfoTypeDef]


# PrometheusTypeDef

### JmxExporter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.JmxExporterTypeDef]

### NodeExporter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.NodeExporterTypeDef]


# ProvisionedRequestTypeDef

### BrokerNodeGroupInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.BrokerNodeGroupInfoUnionTypeDef'>
- **Required**: Yes

### KafkaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfBrokerNodes
- **Type**: <class 'int'>
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClientAuthenticationUnionTypeDef]

### ConfigurationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConfigurationInfoTypeDef]

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EncryptionInfoTypeDef]

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.OpenMonitoringInfoTypeDef]

### LoggingInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.LoggingInfoTypeDef]

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]


# ProvisionedThroughputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### VolumeThroughput
- **Type**: typing.Optional[int]


# ProvisionedTypeDef

### BrokerNodeGroupInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.BrokerNodeGroupInfoOutputTypeDef'>
- **Required**: Yes

### NumberOfBrokerNodes
- **Type**: <class 'int'>
- **Required**: Yes

### CurrentBrokerSoftwareInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.BrokerSoftwareInfoTypeDef]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClientAuthenticationOutputTypeDef]

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EncryptionInfoTypeDef]

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.OpenMonitoringInfoTypeDef]

### LoggingInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.LoggingInfoTypeDef]

### ZookeeperConnectString
- **Type**: typing.Optional[str]

### ZookeeperConnectStringTls
- **Type**: typing.Optional[str]

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]

### CustomerActionStatus
- **Type**: typing.Optional[typing.Literal['ACTION_RECOMMENDED', 'CRITICAL_ACTION_REQUIRED', 'NONE']]


# PublicAccessTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutClusterPolicyRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# PutClusterPolicyResponseTypeDef

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebootBrokerRequestTypeDef

### BrokerIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# RebootBrokerResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RejectClientVpcConnectionRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# ReplicationInfoDescriptionTypeDef

### ConsumerGroupReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConsumerGroupReplicationOutputTypeDef]

### SourceKafkaClusterAlias
- **Type**: typing.Optional[str]

### TargetCompressionType
- **Type**: typing.Optional[typing.Literal['GZIP', 'LZ4', 'NONE', 'SNAPPY', 'ZSTD']]

### TargetKafkaClusterAlias
- **Type**: typing.Optional[str]

### TopicReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.TopicReplicationOutputTypeDef]


# ReplicationInfoSummaryTypeDef

### SourceKafkaClusterAlias
- **Type**: typing.Optional[str]

### TargetKafkaClusterAlias
- **Type**: typing.Optional[str]


# ReplicationInfoTypeDef

### ConsumerGroupReplication
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ConsumerGroupReplicationUnionTypeDef'>
- **Required**: Yes

### SourceKafkaClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetCompressionType
- **Type**: typing.Literal['GZIP', 'LZ4', 'NONE', 'SNAPPY', 'ZSTD']
- **Required**: Yes

### TargetKafkaClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### TopicReplication
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.TopicReplicationUnionTypeDef'>
- **Required**: Yes


# ReplicationStartingPositionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReplicationStateInfoTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# ReplicationTopicNameConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReplicatorSummaryTypeDef

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CurrentVersion
- **Type**: typing.Optional[str]

### IsReplicatorReference
- **Type**: typing.Optional[bool]

### KafkaClustersSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka_classes.KafkaClusterSummaryTypeDef]]

### ReplicationInfoSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka_classes.ReplicationInfoSummaryTypeDef]]

### ReplicatorArn
- **Type**: typing.Optional[str]

### ReplicatorName
- **Type**: typing.Optional[str]

### ReplicatorResourceArn
- **Type**: typing.Optional[str]

### ReplicatorState
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']]


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


# S3TypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Bucket
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]


# SaslTypeDef

### Scram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ScramTypeDef]

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.IamTypeDef]


# ScramTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# ServerlessClientAuthenticationTypeDef

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ServerlessSaslTypeDef]


# ServerlessRequestTypeDef

### VpcConfigs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kafka_classes.VpcConfigUnionTypeDef]
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ServerlessClientAuthenticationTypeDef]


# ServerlessSaslTypeDef

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.IamTypeDef]


# ServerlessTypeDef

### VpcConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka_classes.VpcConfigOutputTypeDef]
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ServerlessClientAuthenticationTypeDef]


# StateInfoTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# StorageInfoTypeDef

### EbsStorageInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EBSStorageInfoTypeDef]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TlsOutputTypeDef

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]


# TlsTypeDef

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.Sequence[str]]

### Enabled
- **Type**: typing.Optional[bool]


# TlsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicReplicationOutputTypeDef

### TopicsToReplicate
- **Type**: typing.List[str]
- **Required**: Yes

### CopyAccessControlListsForTopics
- **Type**: typing.Optional[bool]

### CopyTopicConfigurations
- **Type**: typing.Optional[bool]

### DetectAndCopyNewTopics
- **Type**: typing.Optional[bool]

### StartingPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ReplicationStartingPositionTypeDef]

### TopicNameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ReplicationTopicNameConfigurationTypeDef]

### TopicsToExclude
- **Type**: typing.Optional[typing.List[str]]


# TopicReplicationTypeDef

### TopicsToReplicate
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CopyAccessControlListsForTopics
- **Type**: typing.Optional[bool]

### CopyTopicConfigurations
- **Type**: typing.Optional[bool]

### DetectAndCopyNewTopics
- **Type**: typing.Optional[bool]

### StartingPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ReplicationStartingPositionTypeDef]

### TopicNameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ReplicationTopicNameConfigurationTypeDef]

### TopicsToExclude
- **Type**: typing.Optional[typing.Sequence[str]]


# TopicReplicationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicReplicationUpdateTypeDef

### CopyAccessControlListsForTopics
- **Type**: <class 'bool'>
- **Required**: Yes

### CopyTopicConfigurations
- **Type**: <class 'bool'>
- **Required**: Yes

### DetectAndCopyNewTopics
- **Type**: <class 'bool'>
- **Required**: Yes

### TopicsToExclude
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TopicsToReplicate
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UnauthenticatedTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# UnprocessedScramSecretTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBrokerCountRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TargetNumberOfBrokerNodes
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateBrokerCountResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBrokerStorageRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TargetBrokerEBSVolumeInfo
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kafka_classes.BrokerEBSVolumeInfoTypeDef]
- **Required**: Yes


# UpdateBrokerStorageResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBrokerTypeRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TargetInstanceType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBrokerTypeResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterConfigurationRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ConfigurationInfoTypeDef'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateClusterConfigurationResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterKafkaVersionRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TargetKafkaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConfigurationInfoTypeDef]


# UpdateClusterKafkaVersionResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConfigurationRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.BlobTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ConfigurationRevisionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConnectivityRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectivityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ConnectivityInfoTypeDef'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateConnectivityResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMonitoringRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.OpenMonitoringInfoTypeDef]

### LoggingInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.LoggingInfoTypeDef]


# UpdateMonitoringResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateReplicationInfoRequestTypeDef

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceKafkaClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetKafkaClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConsumerGroupReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ConsumerGroupReplicationUpdateTypeDef]

### TopicReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.TopicReplicationUpdateTypeDef]


# UpdateReplicationInfoResponseTypeDef

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSecurityRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ClientAuthenticationUnionTypeDef]

### EncryptionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.EncryptionInfoTypeDef]


# UpdateSecurityResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStorageRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedThroughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.ProvisionedThroughputTypeDef]

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]

### VolumeSizeGB
- **Type**: typing.Optional[int]


# UpdateStorageResponseTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserIdentityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcConfigOutputTypeDef

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VpcConfigTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# VpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcConnectionInfoServerlessTypeDef

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Owner
- **Type**: typing.Optional[str]

### UserIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.UserIdentityTypeDef]

### VpcConnectionArn
- **Type**: typing.Optional[str]


# VpcConnectionInfoTypeDef

### VpcConnectionArn
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### UserIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.UserIdentityTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# VpcConnectionTypeDef

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Authentication
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DEACTIVATING', 'DELETING', 'FAILED', 'INACTIVE', 'REJECTED', 'REJECTING']]


# VpcConnectivityClientAuthenticationTypeDef

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectivitySaslTypeDef]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectivityTlsTypeDef]


# VpcConnectivityIamTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# VpcConnectivitySaslTypeDef

### Scram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectivityScramTypeDef]

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectivityIamTypeDef]


# VpcConnectivityScramTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# VpcConnectivityTlsTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# VpcConnectivityTypeDef

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka_classes.VpcConnectivityClientAuthenticationTypeDef]


# ZookeeperNodeInfoTypeDef

### AttachedENIId
- **Type**: typing.Optional[str]

### ClientVpcIpAddress
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.List[str]]

### ZookeeperId
- **Type**: typing.Optional[float]

### ZookeeperVersion
- **Type**: typing.Optional[str]



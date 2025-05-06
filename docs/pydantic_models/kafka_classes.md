# Kafka Classes

# AmazonMskCluster

### MskClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAssociateScramSecretRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArnList
- **Type**: typing.List[str]
- **Required**: Yes


# BatchAssociateScramSecretResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### UnprocessedScramSecrets
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.UnprocessedScramSecret]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDisassociateScramSecretRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArnList
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDisassociateScramSecretResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### UnprocessedScramSecrets
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.UnprocessedScramSecret]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# BrokerCountUpdateInfo

### CreatedBrokerIds
- **Type**: typing.Optional[typing.List[float]]

### DeletedBrokerIds
- **Type**: typing.Optional[typing.List[float]]


# BrokerEBSVolumeInfo

### KafkaBrokerNodeId
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedThroughput
- **Type**: <class 'NoneType'>

### VolumeSizeGB
- **Type**: typing.Optional[int]


# BrokerLogs

### CloudWatchLogs
- **Type**: <class 'NoneType'>

### Firehose
- **Type**: <class 'NoneType'>

### S3
- **Type**: <class 'NoneType'>


# BrokerNodeGroupInfo

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
- **Type**: <class 'NoneType'>

### ConnectivityInfo
- **Type**: <class 'NoneType'>

### ZoneIds
- **Type**: typing.Optional[typing.List[str]]


# BrokerNodeGroupInfoOutput

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
- **Type**: <class 'NoneType'>

### ConnectivityInfo
- **Type**: <class 'NoneType'>

### ZoneIds
- **Type**: typing.Optional[typing.List[str]]


# BrokerNodeInfo

### AttachedENIId
- **Type**: typing.Optional[str]

### BrokerId
- **Type**: typing.Optional[float]

### ClientSubnet
- **Type**: typing.Optional[str]

### ClientVpcIpAddress
- **Type**: typing.Optional[str]

### CurrentBrokerSoftwareInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerSoftwareInfo]

### Endpoints
- **Type**: typing.Optional[typing.List[str]]


# BrokerSoftwareInfo

### ConfigurationArn
- **Type**: typing.Optional[str]

### ConfigurationRevision
- **Type**: typing.Optional[int]

### KafkaVersion
- **Type**: typing.Optional[str]


# ClientAuthentication

### Sasl
- **Type**: <class 'NoneType'>

### Tls
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.Tls, aws_resource_validator.pydantic_models.kafka.kafka_classes.TlsOutput, NoneType]

### Unauthenticated
- **Type**: <class 'NoneType'>


# ClientAuthenticationOutput

### Sasl
- **Type**: <class 'NoneType'>

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.TlsOutput]

### Unauthenticated
- **Type**: <class 'NoneType'>


# ClientVpcConnection

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


# CloudWatchLogs

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### LogGroup
- **Type**: typing.Optional[str]


# Cluster

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
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Provisioned
- **Type**: <class 'NoneType'>

### Serverless
- **Type**: <class 'NoneType'>


# ClusterInfo

### ActiveOperationArn
- **Type**: typing.Optional[str]

### BrokerNodeGroupInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerNodeGroupInfoOutput]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthenticationOutput]

### ClusterArn
- **Type**: typing.Optional[str]

### ClusterName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CurrentBrokerSoftwareInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerSoftwareInfo]

### CurrentVersion
- **Type**: typing.Optional[str]

### EncryptionInfo
- **Type**: <class 'NoneType'>

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: <class 'NoneType'>

### LoggingInfo
- **Type**: <class 'NoneType'>

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'HEALING', 'MAINTENANCE', 'REBOOTING_BROKER', 'UPDATING']]

### StateInfo
- **Type**: <class 'NoneType'>

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


# ClusterOperationInfo

### ClientRequestId
- **Type**: typing.Optional[str]

### ClusterArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### ErrorInfo
- **Type**: <class 'NoneType'>

### OperationArn
- **Type**: typing.Optional[str]

### OperationState
- **Type**: typing.Optional[str]

### OperationSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationStep]]

### OperationType
- **Type**: typing.Optional[str]

### SourceClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.MutableClusterInfo]

### TargetClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.MutableClusterInfo]

### VpcConnectionInfo
- **Type**: <class 'NoneType'>


# ClusterOperationStep

### StepInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationStepInfo]

### StepName
- **Type**: typing.Optional[str]


# ClusterOperationStepInfo

### StepStatus
- **Type**: typing.Optional[str]


# ClusterOperationV2

### ClusterArn
- **Type**: typing.Optional[str]

### ClusterType
- **Type**: typing.Optional[typing.Literal['PROVISIONED', 'SERVERLESS']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### ErrorInfo
- **Type**: <class 'NoneType'>

### OperationArn
- **Type**: typing.Optional[str]

### OperationState
- **Type**: typing.Optional[str]

### OperationType
- **Type**: typing.Optional[str]

### Provisioned
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationV2Provisioned]

### Serverless
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationV2Serverless]


# ClusterOperationV2Provisioned

### OperationSteps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationStep]]

### SourceClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.MutableClusterInfo]

### TargetClusterInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.MutableClusterInfo]

### VpcConnectionInfo
- **Type**: <class 'NoneType'>


# ClusterOperationV2Serverless

### VpcConnectionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConnectionInfoServerless]


# ClusterOperationV2Summary

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


# CompatibleKafkaVersion

### SourceVersion
- **Type**: typing.Optional[str]

### TargetVersions
- **Type**: typing.Optional[typing.List[str]]


# Configuration

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ConfigurationRevision'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes


# ConfigurationInfo

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes


# ConfigurationRevision

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ConnectivityInfo

### PublicAccess
- **Type**: <class 'NoneType'>

### VpcConnectivity
- **Type**: <class 'NoneType'>


# ConsumerGroupReplication

### ConsumerGroupsToReplicate
- **Type**: typing.List[str]
- **Required**: Yes

### ConsumerGroupsToExclude
- **Type**: typing.Optional[typing.List[str]]

### DetectAndCopyNewConsumerGroups
- **Type**: typing.Optional[bool]

### SynchroniseConsumerGroupOffsets
- **Type**: typing.Optional[bool]


# ConsumerGroupReplicationOutput

### ConsumerGroupsToReplicate
- **Type**: typing.List[str]
- **Required**: Yes

### ConsumerGroupsToExclude
- **Type**: typing.Optional[typing.List[str]]

### DetectAndCopyNewConsumerGroups
- **Type**: typing.Optional[bool]

### SynchroniseConsumerGroupOffsets
- **Type**: typing.Optional[bool]


# ConsumerGroupReplicationUpdate

### ConsumerGroupsToExclude
- **Type**: typing.List[str]
- **Required**: Yes

### ConsumerGroupsToReplicate
- **Type**: typing.List[str]
- **Required**: Yes

### DetectAndCopyNewConsumerGroups
- **Type**: <class 'bool'>
- **Required**: Yes

### SynchroniseConsumerGroupOffsets
- **Type**: <class 'bool'>
- **Required**: Yes


# ControllerNodeInfo

### Endpoints
- **Type**: typing.Optional[typing.List[str]]


# CreateClusterRequest

### BrokerNodeGroupInfo
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerNodeGroupInfo, aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerNodeGroupInfoOutput]
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthentication, aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthenticationOutput, NoneType]

### ConfigurationInfo
- **Type**: <class 'NoneType'>

### EncryptionInfo
- **Type**: <class 'NoneType'>

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.OpenMonitoringInfo]

### LoggingInfo
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]


# CreateClusterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterV2Request

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Provisioned
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ProvisionedRequest]

### Serverless
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ServerlessRequest]


# CreateClusterV2Response

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConfigurationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServerProperties
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### KafkaVersions
- **Type**: typing.Optional[typing.List[str]]


# CreateConfigurationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ConfigurationRevision'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReplicatorRequest

### KafkaClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.KafkaCluster]
- **Required**: Yes

### ReplicationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicationInfo]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateReplicatorResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcConnectionRequest

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
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateVpcConnectionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterPolicyRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# DeleteClusterResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'HEALING', 'MAINTENANCE', 'REBOOTING_BROKER', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConfigurationRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteReplicatorRequest

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# DeleteReplicatorResponse

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVpcConnectionRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcConnectionResponse

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DEACTIVATING', 'DELETING', 'FAILED', 'INACTIVE', 'REJECTED', 'REJECTING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterOperationRequest

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterOperationResponse

### ClusterOperationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterOperationV2Request

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterOperationV2Response

### ClusterOperationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationV2'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterResponse

### ClusterInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClusterV2Request

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterV2Response

### ClusterInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConfigurationRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ConfigurationRevision'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ACTIVE', 'DELETE_FAILED', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConfigurationRevisionRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Revision
- **Type**: <class 'int'>
- **Required**: Yes


# DescribeConfigurationRevisionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicatorRequest

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeReplicatorResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.KafkaClusterDescription]
- **Required**: Yes

### ReplicationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicationInfoDescription]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicationStateInfo'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVpcConnectionRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVpcConnectionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# EBSStorageInfo

### ProvisionedThroughput
- **Type**: <class 'NoneType'>

### VolumeSize
- **Type**: typing.Optional[int]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionAtRest

### DataVolumeKMSKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# EncryptionInTransit

### ClientBroker
- **Type**: typing.Optional[typing.Literal['PLAINTEXT', 'TLS', 'TLS_PLAINTEXT']]

### InCluster
- **Type**: typing.Optional[bool]


# EncryptionInfo

### EncryptionAtRest
- **Type**: <class 'NoneType'>

### EncryptionInTransit
- **Type**: <class 'NoneType'>


# ErrorInfo

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorString
- **Type**: typing.Optional[str]


# Firehose

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### DeliveryStream
- **Type**: typing.Optional[str]


# GetBootstrapBrokersRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetBootstrapBrokersResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# GetClusterPolicyRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetClusterPolicyResponse

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# GetCompatibleKafkaVersionsRequest

### ClusterArn
- **Type**: typing.Optional[str]


# GetCompatibleKafkaVersionsResponse

### CompatibleKafkaVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.CompatibleKafkaVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# Iam

### Enabled
- **Type**: typing.Optional[bool]


# JmxExporter

### EnabledInBroker
- **Type**: <class 'bool'>
- **Required**: Yes


# JmxExporterInfo

### EnabledInBroker
- **Type**: <class 'bool'>
- **Required**: Yes


# KafkaCluster

### AmazonMskCluster
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.AmazonMskCluster'>
- **Required**: Yes

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.KafkaClusterClientVpcConfig, aws_resource_validator.pydantic_models.kafka.kafka_classes.KafkaClusterClientVpcConfigOutput]
- **Required**: Yes


# KafkaClusterClientVpcConfig

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# KafkaClusterClientVpcConfigOutput

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# KafkaClusterDescription

### AmazonMskCluster
- **Type**: <class 'NoneType'>

### KafkaClusterAlias
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.KafkaClusterClientVpcConfigOutput]


# KafkaClusterSummary

### AmazonMskCluster
- **Type**: <class 'NoneType'>

### KafkaClusterAlias
- **Type**: typing.Optional[str]


# KafkaVersion

### Version
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEPRECATED']]


# ListClientVpcConnectionsRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClientVpcConnectionsRequestPaginate

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListClientVpcConnectionsResponse

### ClientVpcConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientVpcConnection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClusterOperationsRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClusterOperationsRequestPaginate

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListClusterOperationsResponse

### ClusterOperationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClusterOperationsV2Request

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClusterOperationsV2RequestPaginate

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListClusterOperationsV2Response

### ClusterOperationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterOperationV2Summary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequest

### ClusterNameFilter
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginate

### ClusterNameFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListClustersResponse

### ClusterInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClusterInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersV2Request

### ClusterNameFilter
- **Type**: typing.Optional[str]

### ClusterTypeFilter
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersV2RequestPaginate

### ClusterNameFilter
- **Type**: typing.Optional[str]

### ClusterTypeFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListClustersV2Response

### ClusterInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.Cluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRevisionsRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationRevisionsRequestPaginate

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListConfigurationRevisionsResponse

### Revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ConfigurationRevision]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListConfigurationsResponse

### Configurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.Configuration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKafkaVersionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListKafkaVersionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListKafkaVersionsResponse

### KafkaVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.KafkaVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListNodesRequestPaginate

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListNodesResponse

### NodeInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.NodeInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReplicatorsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ReplicatorNameFilter
- **Type**: typing.Optional[str]


# ListReplicatorsRequestPaginate

### ReplicatorNameFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListReplicatorsResponse

### Replicators
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicatorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListScramSecretsRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListScramSecretsRequestPaginate

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListScramSecretsResponse

### SecretArnList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcConnectionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVpcConnectionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.PaginatorConfig]


# ListVpcConnectionsResponse

### VpcConnections
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConnection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoggingInfo

### BrokerLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerLogs'>
- **Required**: Yes


# MutableClusterInfo

### BrokerEBSVolumeInfo
- **Type**: typing.Optional[typing.List[NoneType]]

### ConfigurationInfo
- **Type**: <class 'NoneType'>

### NumberOfBrokerNodes
- **Type**: typing.Optional[int]

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: <class 'NoneType'>

### KafkaVersion
- **Type**: typing.Optional[str]

### LoggingInfo
- **Type**: <class 'NoneType'>

### InstanceType
- **Type**: typing.Optional[str]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthenticationOutput]

### EncryptionInfo
- **Type**: <class 'NoneType'>

### ConnectivityInfo
- **Type**: <class 'NoneType'>

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]

### BrokerCountUpdateInfo
- **Type**: <class 'NoneType'>


# NodeExporter

### EnabledInBroker
- **Type**: <class 'bool'>
- **Required**: Yes


# NodeExporterInfo

### EnabledInBroker
- **Type**: <class 'bool'>
- **Required**: Yes


# NodeInfo

### AddedToClusterTime
- **Type**: typing.Optional[str]

### BrokerNodeInfo
- **Type**: <class 'NoneType'>

### ControllerNodeInfo
- **Type**: <class 'NoneType'>

### InstanceType
- **Type**: typing.Optional[str]

### NodeARN
- **Type**: typing.Optional[str]

### NodeType
- **Type**: typing.Optional[typing.Literal['BROKER']]

### ZookeeperNodeInfo
- **Type**: <class 'NoneType'>


# OpenMonitoring

### Prometheus
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.Prometheus'>
- **Required**: Yes


# OpenMonitoringInfo

### Prometheus
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.PrometheusInfo'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Prometheus

### JmxExporter
- **Type**: <class 'NoneType'>

### NodeExporter
- **Type**: <class 'NoneType'>


# PrometheusInfo

### JmxExporter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.JmxExporterInfo]

### NodeExporter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.NodeExporterInfo]


# Provisioned

### BrokerNodeGroupInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerNodeGroupInfoOutput'>
- **Required**: Yes

### NumberOfBrokerNodes
- **Type**: <class 'int'>
- **Required**: Yes

### CurrentBrokerSoftwareInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerSoftwareInfo]

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthenticationOutput]

### EncryptionInfo
- **Type**: <class 'NoneType'>

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.OpenMonitoringInfo]

### LoggingInfo
- **Type**: <class 'NoneType'>

### ZookeeperConnectString
- **Type**: typing.Optional[str]

### ZookeeperConnectStringTls
- **Type**: typing.Optional[str]

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]

### CustomerActionStatus
- **Type**: typing.Optional[typing.Literal['ACTION_RECOMMENDED', 'CRITICAL_ACTION_REQUIRED', 'NONE']]


# ProvisionedRequest

### BrokerNodeGroupInfo
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerNodeGroupInfo, aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerNodeGroupInfoOutput]
- **Required**: Yes

### KafkaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfBrokerNodes
- **Type**: <class 'int'>
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthentication, aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthenticationOutput, NoneType]

### ConfigurationInfo
- **Type**: <class 'NoneType'>

### EncryptionInfo
- **Type**: <class 'NoneType'>

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.OpenMonitoringInfo]

### LoggingInfo
- **Type**: <class 'NoneType'>

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]


# ProvisionedThroughput

### Enabled
- **Type**: typing.Optional[bool]

### VolumeThroughput
- **Type**: typing.Optional[int]


# PublicAccess

### Type
- **Type**: typing.Optional[str]


# PutClusterPolicyRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# PutClusterPolicyResponse

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# RebootBrokerRequest

### BrokerIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# RebootBrokerResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# RejectClientVpcConnectionRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# ReplicationInfo

### ConsumerGroupReplication
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.ConsumerGroupReplication, aws_resource_validator.pydantic_models.kafka.kafka_classes.ConsumerGroupReplicationOutput]
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.TopicReplication, aws_resource_validator.pydantic_models.kafka.kafka_classes.TopicReplicationOutput]
- **Required**: Yes


# ReplicationInfoDescription

### ConsumerGroupReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ConsumerGroupReplicationOutput]

### SourceKafkaClusterAlias
- **Type**: typing.Optional[str]

### TargetCompressionType
- **Type**: typing.Optional[typing.Literal['GZIP', 'LZ4', 'NONE', 'SNAPPY', 'ZSTD']]

### TargetKafkaClusterAlias
- **Type**: typing.Optional[str]

### TopicReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.TopicReplicationOutput]


# ReplicationInfoSummary

### SourceKafkaClusterAlias
- **Type**: typing.Optional[str]

### TargetKafkaClusterAlias
- **Type**: typing.Optional[str]


# ReplicationStartingPosition

### Type
- **Type**: typing.Optional[typing.Literal['EARLIEST', 'LATEST']]


# ReplicationStateInfo

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# ReplicationTopicNameConfiguration

### Type
- **Type**: typing.Optional[typing.Literal['IDENTICAL', 'PREFIXED_WITH_SOURCE_CLUSTER_ALIAS']]


# ReplicatorSummary

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### CurrentVersion
- **Type**: typing.Optional[str]

### IsReplicatorReference
- **Type**: typing.Optional[bool]

### KafkaClustersSummary
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.KafkaClusterSummary]]

### ReplicationInfoSummaryList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicationInfoSummary]]

### ReplicatorArn
- **Type**: typing.Optional[str]

### ReplicatorName
- **Type**: typing.Optional[str]

### ReplicatorResourceArn
- **Type**: typing.Optional[str]

### ReplicatorState
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']]


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


# S3

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Bucket
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]


# Sasl

### Scram
- **Type**: <class 'NoneType'>

### Iam
- **Type**: <class 'NoneType'>


# Scram

### Enabled
- **Type**: typing.Optional[bool]


# Serverless

### VpcConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConfigOutput]
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ServerlessClientAuthentication]


# ServerlessClientAuthentication

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ServerlessSasl]


# ServerlessRequest

### VpcConfigs
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConfig, aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConfigOutput]]
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ServerlessClientAuthentication]


# ServerlessSasl

### Iam
- **Type**: <class 'NoneType'>


# StateInfo

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# StorageInfo

### EbsStorageInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.EBSStorageInfo]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Tls

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]


# TlsOutput

### CertificateAuthorityArnList
- **Type**: typing.Optional[typing.List[str]]

### Enabled
- **Type**: typing.Optional[bool]


# TopicReplication

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicationStartingPosition]

### TopicNameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicationTopicNameConfiguration]

### TopicsToExclude
- **Type**: typing.Optional[typing.List[str]]


# TopicReplicationOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicationStartingPosition]

### TopicNameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ReplicationTopicNameConfiguration]

### TopicsToExclude
- **Type**: typing.Optional[typing.List[str]]


# TopicReplicationUpdate

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
- **Type**: typing.List[str]
- **Required**: Yes

### TopicsToReplicate
- **Type**: typing.List[str]
- **Required**: Yes


# Unauthenticated

### Enabled
- **Type**: typing.Optional[bool]


# UnprocessedScramSecret

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateBrokerCountRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TargetNumberOfBrokerNodes
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateBrokerCountResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBrokerStorageRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TargetBrokerEBSVolumeInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.kafka.kafka_classes.BrokerEBSVolumeInfo]
- **Required**: Yes


# UpdateBrokerStorageResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBrokerTypeRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TargetInstanceType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBrokerTypeResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterConfigurationRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ConfigurationInfo'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateClusterConfigurationResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterKafkaVersionRequest

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
- **Type**: <class 'NoneType'>


# UpdateClusterKafkaVersionResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConfigurationRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerProperties
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LatestRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ConfigurationRevision'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConnectivityRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectivityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ConnectivityInfo'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateConnectivityResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMonitoringRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### EnhancedMonitoring
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION']]

### OpenMonitoring
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.OpenMonitoringInfo]

### LoggingInfo
- **Type**: <class 'NoneType'>


# UpdateMonitoringResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateReplicationInfoRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.ConsumerGroupReplicationUpdate]

### TopicReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.TopicReplicationUpdate]


# UpdateReplicationInfoResponse

### ReplicatorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicatorState
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'RUNNING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSecurityRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientAuthentication
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthentication, aws_resource_validator.pydantic_models.kafka.kafka_classes.ClientAuthenticationOutput, NoneType]

### EncryptionInfo
- **Type**: <class 'NoneType'>


# UpdateSecurityResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStorageRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedThroughput
- **Type**: <class 'NoneType'>

### StorageMode
- **Type**: typing.Optional[typing.Literal['LOCAL', 'TIERED']]

### VolumeSizeGB
- **Type**: typing.Optional[int]


# UpdateStorageResponse

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterOperationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kafka.kafka_classes.ResponseMetadata'>
- **Required**: Yes


# UserIdentity

### Type
- **Type**: typing.Optional[typing.Literal['AWSACCOUNT', 'AWSSERVICE']]

### PrincipalId
- **Type**: typing.Optional[str]


# VpcConfig

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VpcConfigOutput

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# VpcConnection

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


# VpcConnectionInfo

### VpcConnectionArn
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### UserIdentity
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# VpcConnectionInfoServerless

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Owner
- **Type**: typing.Optional[str]

### UserIdentity
- **Type**: <class 'NoneType'>

### VpcConnectionArn
- **Type**: typing.Optional[str]


# VpcConnectivity

### ClientAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConnectivityClientAuthentication]


# VpcConnectivityClientAuthentication

### Sasl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConnectivitySasl]

### Tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConnectivityTls]


# VpcConnectivityIam

### Enabled
- **Type**: typing.Optional[bool]


# VpcConnectivitySasl

### Scram
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConnectivityScram]

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kafka.kafka_classes.VpcConnectivityIam]


# VpcConnectivityScram

### Enabled
- **Type**: typing.Optional[bool]


# VpcConnectivityTls

### Enabled
- **Type**: typing.Optional[bool]


# ZookeeperNodeInfo

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



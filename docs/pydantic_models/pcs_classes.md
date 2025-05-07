# Pcs Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Cluster

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### scheduler
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.Scheduler'>
- **Required**: Yes

### size
- **Type**: typing.Literal['LARGE', 'MEDIUM', 'SMALL']
- **Required**: Yes

### networking
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.Networking'>
- **Required**: Yes

### slurmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.ClusterSlurmConfiguration]

### endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.Endpoint]]

### errorInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.ErrorInfo]]


# ClusterSlurmConfiguration

### scaleDownIdleTimeInSeconds
- **Type**: typing.Optional[int]

### slurmCustomSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.SlurmCustomSetting]]

### authKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.SlurmAuthKey]


# ClusterSlurmConfigurationRequest

### scaleDownIdleTimeInSeconds
- **Type**: typing.Optional[int]

### slurmCustomSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.SlurmCustomSetting]]


# ClusterSummary

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes


# ComputeNodeGroup

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### customLaunchTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.CustomLaunchTemplate'>
- **Required**: Yes

### iamInstanceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### scalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ScalingConfiguration'>
- **Required**: Yes

### instanceConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.InstanceConfig]
- **Required**: Yes

### amiId
- **Type**: typing.Optional[str]

### purchaseOption
- **Type**: typing.Optional[typing.Literal['ONDEMAND', 'SPOT']]

### spotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.SpotOptions]

### slurmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroupSlurmConfiguration]

### errorInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.ErrorInfo]]


# ComputeNodeGroupConfiguration

### computeNodeGroupId
- **Type**: typing.Optional[str]


# ComputeNodeGroupSlurmConfiguration

### slurmCustomSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.SlurmCustomSetting]]


# ComputeNodeGroupSlurmConfigurationRequest

### slurmCustomSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.SlurmCustomSetting]]


# ComputeNodeGroupSummary

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes


# CreateClusterRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### scheduler
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.SchedulerRequest'>
- **Required**: Yes

### size
- **Type**: typing.Literal['LARGE', 'MEDIUM', 'SMALL']
- **Required**: Yes

### networking
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.NetworkingRequest'>
- **Required**: Yes

### slurmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.ClusterSlurmConfigurationRequest]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateComputeNodeGroupRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### computeNodeGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### customLaunchTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.CustomLaunchTemplate'>
- **Required**: Yes

### iamInstanceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### scalingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ScalingConfigurationRequest'>
- **Required**: Yes

### instanceConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.InstanceConfig]
- **Required**: Yes

### amiId
- **Type**: typing.Optional[str]

### purchaseOption
- **Type**: typing.Optional[typing.Literal['ONDEMAND', 'SPOT']]

### spotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.SpotOptions]

### slurmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroupSlurmConfigurationRequest]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateComputeNodeGroupResponse

### computeNodeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQueueRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queueName
- **Type**: <class 'str'>
- **Required**: Yes

### computeNodeGroupConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroupConfiguration]]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateQueueResponse

### queue
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.Queue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# CustomLaunchTemplate

### id
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteComputeNodeGroupRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### computeNodeGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteQueueRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queueIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### type
- **Type**: typing.Literal['SLURMCTLD', 'SLURMDBD']
- **Required**: Yes

### privateIpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### port
- **Type**: <class 'str'>
- **Required**: Yes

### publicIpAddress
- **Type**: typing.Optional[str]


# ErrorInfo

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# GetClusterRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# GetComputeNodeGroupRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### computeNodeGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetComputeNodeGroupResponse

### computeNodeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueueRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queueIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueueResponse

### queue
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.Queue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# InstanceConfig

### instanceType
- **Type**: typing.Optional[str]


# ListClustersRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListClustersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.PaginatorConfig]


# ListClustersResponse

### clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.ClusterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComputeNodeGroupsRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListComputeNodeGroupsRequestPaginate

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.PaginatorConfig]


# ListComputeNodeGroupsResponse

### computeNodeGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQueuesRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListQueuesRequestPaginate

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.PaginatorConfig]


# ListQueuesResponse

### queues
- **Type**: typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.QueueSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# Networking

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# NetworkingRequest

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Queue

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### computeNodeGroupConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroupConfiguration]
- **Required**: Yes

### errorInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.ErrorInfo]]


# QueueSummary

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clusterId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### modifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes


# RegisterComputeNodeGroupInstanceRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### bootstrapId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterComputeNodeGroupInstanceResponse

### nodeID
- **Type**: <class 'str'>
- **Required**: Yes

### sharedSecret
- **Type**: <class 'str'>
- **Required**: Yes

### endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
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


# ScalingConfiguration

### minInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### maxInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes


# ScalingConfigurationRequest

### minInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### maxInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes


# Scheduler

### type
- **Type**: typing.Literal['SLURM']
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# SchedulerRequest

### type
- **Type**: typing.Literal['SLURM']
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# SlurmAuthKey

### secretArn
- **Type**: <class 'str'>
- **Required**: Yes

### secretVersion
- **Type**: <class 'str'>
- **Required**: Yes


# SlurmCustomSetting

### parameterName
- **Type**: <class 'str'>
- **Required**: Yes

### parameterValue
- **Type**: <class 'str'>
- **Required**: Yes


# SpotOptions

### allocationStrategy
- **Type**: typing.Optional[typing.Literal['capacity-optimized', 'lowest-price', 'price-capacity-optimized']]


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


# UpdateComputeNodeGroupRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### computeNodeGroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### amiId
- **Type**: typing.Optional[str]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### customLaunchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.CustomLaunchTemplate]

### purchaseOption
- **Type**: typing.Optional[typing.Literal['ONDEMAND', 'SPOT']]

### spotOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.SpotOptions]

### scalingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.ScalingConfigurationRequest]

### iamInstanceProfileArn
- **Type**: typing.Optional[str]

### slurmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pcs.pcs_classes.UpdateComputeNodeGroupSlurmConfigurationRequest]

### clientToken
- **Type**: typing.Optional[str]


# UpdateComputeNodeGroupResponse

### computeNodeGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateComputeNodeGroupSlurmConfigurationRequest

### slurmCustomSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.SlurmCustomSetting]]


# UpdateQueueRequest

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### queueIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### computeNodeGroupConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pcs.pcs_classes.ComputeNodeGroupConfiguration]]

### clientToken
- **Type**: typing.Optional[str]


# UpdateQueueResponse

### queue
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.Queue'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pcs.pcs_classes.ResponseMetadata'>
- **Required**: Yes



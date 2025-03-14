# Batch Classes

# ArrayPropertiesDetailTypeDef

### statusSummary
- **Type**: typing.Optional[typing.Dict[str, int]]

### size
- **Type**: typing.Optional[int]

### index
- **Type**: typing.Optional[int]


# ArrayPropertiesSummaryTypeDef

### size
- **Type**: typing.Optional[int]

### index
- **Type**: typing.Optional[int]


# ArrayPropertiesTypeDef

### size
- **Type**: typing.Optional[int]


# AttemptContainerDetailTypeDef

### containerInstanceArn
- **Type**: typing.Optional[str]

### taskArn
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]

### logStreamName
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.NetworkInterfaceTypeDef]]


# AttemptDetailTypeDef

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.AttemptContainerDetailTypeDef]

### startedAt
- **Type**: typing.Optional[int]

### stoppedAt
- **Type**: typing.Optional[int]

### statusReason
- **Type**: typing.Optional[str]

### taskProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.AttemptEcsTaskDetailsTypeDef]]


# AttemptEcsTaskDetailsTypeDef

### containerInstanceArn
- **Type**: typing.Optional[str]

### taskArn
- **Type**: typing.Optional[str]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.AttemptTaskContainerDetailsTypeDef]]


# AttemptTaskContainerDetailsTypeDef

### exitCode
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### logStreamName
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.NetworkInterfaceTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# ComputeEnvironmentDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComputeEnvironmentOrderTypeDef

### order
- **Type**: <class 'int'>
- **Required**: Yes

### computeEnvironment
- **Type**: <class 'str'>
- **Required**: Yes


# ComputeResourceUpdateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConsumableResourcePropertiesOutputTypeDef

### consumableResourceList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.ConsumableResourceRequirementTypeDef]]


# ConsumableResourcePropertiesTypeDef

### consumableResourceList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ConsumableResourceRequirementTypeDef]]


# ConsumableResourcePropertiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConsumableResourceRequirementTypeDef

### consumableResource
- **Type**: typing.Optional[str]

### quantity
- **Type**: typing.Optional[int]


# ConsumableResourceSummaryTypeDef

### consumableResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### consumableResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### totalQuantity
- **Type**: typing.Optional[int]

### inUseQuantity
- **Type**: typing.Optional[int]

### resourceType
- **Type**: typing.Optional[str]


# ContainerDetailTypeDef

### image
- **Type**: typing.Optional[str]

### vcpus
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### command
- **Type**: typing.Optional[typing.List[str]]

### jobRoleArn
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.VolumeTypeDef]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.KeyValuePairTypeDef]]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.MountPointTypeDef]]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.UlimitTypeDef]]

### privileged
- **Type**: typing.Optional[bool]

### user
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]

### containerInstanceArn
- **Type**: typing.Optional[str]

### taskArn
- **Type**: typing.Optional[str]

### logStreamName
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.NetworkInterfaceTypeDef]]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.ResourceRequirementTypeDef]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LinuxParametersOutputTypeDef]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LogConfigurationOutputTypeDef]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.SecretTypeDef]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NetworkConfigurationTypeDef]

### fargatePlatformConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.FargatePlatformConfigurationTypeDef]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EphemeralStorageTypeDef]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RuntimePlatformTypeDef]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RepositoryCredentialsTypeDef]


# ContainerOverridesTypeDef

### vcpus
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### instanceType
- **Type**: typing.Optional[str]

### environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuePairTypeDef]]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ResourceRequirementTypeDef]]


# ContainerPropertiesOutputTypeDef

### image
- **Type**: typing.Optional[str]

### vcpus
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### command
- **Type**: typing.Optional[typing.List[str]]

### jobRoleArn
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.VolumeTypeDef]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.KeyValuePairTypeDef]]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.MountPointTypeDef]]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### privileged
- **Type**: typing.Optional[bool]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.UlimitTypeDef]]

### user
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.ResourceRequirementTypeDef]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LinuxParametersOutputTypeDef]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LogConfigurationOutputTypeDef]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.SecretTypeDef]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NetworkConfigurationTypeDef]

### fargatePlatformConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.FargatePlatformConfigurationTypeDef]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EphemeralStorageTypeDef]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RuntimePlatformTypeDef]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RepositoryCredentialsTypeDef]


# ContainerPropertiesTypeDef

### image
- **Type**: typing.Optional[str]

### vcpus
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### jobRoleArn
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.VolumeTypeDef]]

### environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuePairTypeDef]]

### mountPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.MountPointTypeDef]]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### privileged
- **Type**: typing.Optional[bool]

### ulimits
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.UlimitTypeDef]]

### user
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ResourceRequirementTypeDef]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LinuxParametersTypeDef]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LogConfigurationTypeDef]

### secrets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.SecretTypeDef]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NetworkConfigurationTypeDef]

### fargatePlatformConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.FargatePlatformConfigurationTypeDef]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EphemeralStorageTypeDef]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RuntimePlatformTypeDef]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RepositoryCredentialsTypeDef]


# ContainerSummaryTypeDef

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]


# CreateComputeEnvironmentResponseTypeDef

### computeEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### computeEnvironmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConsumableResourceRequestTypeDef

### consumableResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### totalQuantity
- **Type**: typing.Optional[int]

### resourceType
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConsumableResourceResponseTypeDef

### consumableResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### consumableResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobQueueRequestTypeDef

### jobQueueName
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### computeEnvironmentOrder
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ComputeEnvironmentOrderTypeDef]
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### schedulingPolicyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### jobStateTimeLimitActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.JobStateTimeLimitActionTypeDef]]


# CreateJobQueueResponseTypeDef

### jobQueueName
- **Type**: <class 'str'>
- **Required**: Yes

### jobQueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSchedulingPolicyRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fairsharePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.FairsharePolicyUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSchedulingPolicyResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteComputeEnvironmentRequestTypeDef

### computeEnvironment
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConsumableResourceRequestTypeDef

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobQueueRequestTypeDef

### jobQueue
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchedulingPolicyRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterJobDefinitionRequestTypeDef

### jobDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeComputeEnvironmentsRequestPaginateTypeDef

### computeEnvironments
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.PaginatorConfigTypeDef]


# DescribeComputeEnvironmentsRequestTypeDef

### computeEnvironments
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeComputeEnvironmentsResponseTypeDef

### computeEnvironments
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.ComputeEnvironmentDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeConsumableResourceRequestTypeDef

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConsumableResourceResponseTypeDef

### consumableResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### consumableResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### totalQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### inUseQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### availableQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobDefinitionsRequestPaginateTypeDef

### jobDefinitions
- **Type**: typing.Optional[typing.Sequence[str]]

### jobDefinitionName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.PaginatorConfigTypeDef]


# DescribeJobDefinitionsRequestTypeDef

### jobDefinitions
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### jobDefinitionName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobDefinitionsResponseTypeDef

### jobDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.JobDefinitionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobQueuesRequestPaginateTypeDef

### jobQueues
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.PaginatorConfigTypeDef]


# DescribeJobQueuesRequestTypeDef

### jobQueues
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobQueuesResponseTypeDef

### jobQueues
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.JobQueueDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsRequestTypeDef

### jobs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeJobsResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.JobDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSchedulingPoliciesRequestTypeDef

### arns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeSchedulingPoliciesResponseTypeDef

### schedulingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.SchedulingPolicyDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceOutputTypeDef

### hostPath
- **Type**: <class 'str'>
- **Required**: Yes

### containerPath
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.List[typing.Literal['MKNOD', 'READ', 'WRITE']]]


# DeviceTypeDef

### hostPath
- **Type**: <class 'str'>
- **Required**: Yes

### containerPath
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['MKNOD', 'READ', 'WRITE']]]


# EFSAuthorizationConfigTypeDef

### accessPointId
- **Type**: typing.Optional[str]

### iam
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# EFSVolumeConfigurationTypeDef

### fileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### rootDirectory
- **Type**: typing.Optional[str]

### transitEncryption
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### transitEncryptionPort
- **Type**: typing.Optional[int]

### authorizationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EFSAuthorizationConfigTypeDef]


# Ec2ConfigurationTypeDef

### imageType
- **Type**: <class 'str'>
- **Required**: Yes

### imageIdOverride
- **Type**: typing.Optional[str]

### imageKubernetesVersion
- **Type**: typing.Optional[str]


# EcsPropertiesDetailTypeDef

### taskProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EcsTaskDetailsTypeDef]]


# EcsPropertiesOutputTypeDef

### taskProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.EcsTaskPropertiesOutputTypeDef]
- **Required**: Yes


# EcsPropertiesOverrideTypeDef

### taskProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.TaskPropertiesOverrideTypeDef]]


# EcsPropertiesTypeDef

### taskProperties
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EcsTaskPropertiesTypeDef]
- **Required**: Yes


# EcsTaskDetailsTypeDef

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.TaskContainerDetailsTypeDef]]

### containerInstanceArn
- **Type**: typing.Optional[str]

### taskArn
- **Type**: typing.Optional[str]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EphemeralStorageTypeDef]

### executionRoleArn
- **Type**: typing.Optional[str]

### platformVersion
- **Type**: typing.Optional[str]

### ipcMode
- **Type**: typing.Optional[str]

### taskRoleArn
- **Type**: typing.Optional[str]

### pidMode
- **Type**: typing.Optional[str]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NetworkConfigurationTypeDef]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RuntimePlatformTypeDef]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.VolumeTypeDef]]


# EcsTaskPropertiesOutputTypeDef

### containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.TaskContainerPropertiesOutputTypeDef]
- **Required**: Yes

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EphemeralStorageTypeDef]

### executionRoleArn
- **Type**: typing.Optional[str]

### platformVersion
- **Type**: typing.Optional[str]

### ipcMode
- **Type**: typing.Optional[str]

### taskRoleArn
- **Type**: typing.Optional[str]

### pidMode
- **Type**: typing.Optional[str]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NetworkConfigurationTypeDef]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RuntimePlatformTypeDef]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.VolumeTypeDef]]


# EcsTaskPropertiesTypeDef

### containers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.TaskContainerPropertiesTypeDef]
- **Required**: Yes

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EphemeralStorageTypeDef]

### executionRoleArn
- **Type**: typing.Optional[str]

### platformVersion
- **Type**: typing.Optional[str]

### ipcMode
- **Type**: typing.Optional[str]

### taskRoleArn
- **Type**: typing.Optional[str]

### pidMode
- **Type**: typing.Optional[str]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NetworkConfigurationTypeDef]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RuntimePlatformTypeDef]

### volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.VolumeTypeDef]]


# EksAttemptContainerDetailTypeDef

### name
- **Type**: typing.Optional[str]

### containerID
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]


# EksAttemptDetailTypeDef

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksAttemptContainerDetailTypeDef]]

### initContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksAttemptContainerDetailTypeDef]]

### eksClusterArn
- **Type**: typing.Optional[str]

### podName
- **Type**: typing.Optional[str]

### podNamespace
- **Type**: typing.Optional[str]

### nodeName
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[int]

### stoppedAt
- **Type**: typing.Optional[int]

### statusReason
- **Type**: typing.Optional[str]


# EksConfigurationTypeDef

### eksClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### kubernetesNamespace
- **Type**: <class 'str'>
- **Required**: Yes


# EksContainerDetailTypeDef

### name
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### imagePullPolicy
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.List[str]]

### args
- **Type**: typing.Optional[typing.List[str]]

### env
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksContainerEnvironmentVariableTypeDef]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksContainerResourceRequirementsOutputTypeDef]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]

### volumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksContainerVolumeMountTypeDef]]

### securityContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksContainerSecurityContextTypeDef]


# EksContainerEnvironmentVariableTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# EksContainerOutputTypeDef

### image
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### imagePullPolicy
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.List[str]]

### args
- **Type**: typing.Optional[typing.List[str]]

### env
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksContainerEnvironmentVariableTypeDef]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksContainerResourceRequirementsOutputTypeDef]

### volumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksContainerVolumeMountTypeDef]]

### securityContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksContainerSecurityContextTypeDef]


# EksContainerOverrideTypeDef

### name
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### args
- **Type**: typing.Optional[typing.Sequence[str]]

### env
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EksContainerEnvironmentVariableTypeDef]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksContainerResourceRequirementsUnionTypeDef]


# EksContainerResourceRequirementsOutputTypeDef

### limits
- **Type**: typing.Optional[typing.Dict[str, str]]

### requests
- **Type**: typing.Optional[typing.Dict[str, str]]


# EksContainerResourceRequirementsTypeDef

### limits
- **Type**: typing.Optional[typing.Mapping[str, str]]

### requests
- **Type**: typing.Optional[typing.Mapping[str, str]]


# EksContainerResourceRequirementsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EksContainerSecurityContextTypeDef

### runAsUser
- **Type**: typing.Optional[int]

### runAsGroup
- **Type**: typing.Optional[int]

### privileged
- **Type**: typing.Optional[bool]

### allowPrivilegeEscalation
- **Type**: typing.Optional[bool]

### readOnlyRootFilesystem
- **Type**: typing.Optional[bool]

### runAsNonRoot
- **Type**: typing.Optional[bool]


# EksContainerTypeDef

### image
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### imagePullPolicy
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### args
- **Type**: typing.Optional[typing.Sequence[str]]

### env
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EksContainerEnvironmentVariableTypeDef]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksContainerResourceRequirementsTypeDef]

### volumeMounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EksContainerVolumeMountTypeDef]]

### securityContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksContainerSecurityContextTypeDef]


# EksContainerVolumeMountTypeDef

### name
- **Type**: typing.Optional[str]

### mountPath
- **Type**: typing.Optional[str]

### subPath
- **Type**: typing.Optional[str]

### readOnly
- **Type**: typing.Optional[bool]


# EksEmptyDirTypeDef

### medium
- **Type**: typing.Optional[str]

### sizeLimit
- **Type**: typing.Optional[str]


# EksHostPathTypeDef

### path
- **Type**: typing.Optional[str]


# EksMetadataOutputTypeDef

### labels
- **Type**: typing.Optional[typing.Dict[str, str]]

### annotations
- **Type**: typing.Optional[typing.Dict[str, str]]

### namespace
- **Type**: typing.Optional[str]


# EksMetadataTypeDef

### labels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### annotations
- **Type**: typing.Optional[typing.Mapping[str, str]]

### namespace
- **Type**: typing.Optional[str]


# EksMetadataUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EksPersistentVolumeClaimTypeDef

### claimName
- **Type**: <class 'str'>
- **Required**: Yes

### readOnly
- **Type**: typing.Optional[bool]


# EksPodPropertiesDetailTypeDef

### serviceAccountName
- **Type**: typing.Optional[str]

### hostNetwork
- **Type**: typing.Optional[bool]

### dnsPolicy
- **Type**: typing.Optional[str]

### imagePullSecrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.ImagePullSecretTypeDef]]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksContainerDetailTypeDef]]

### initContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksContainerDetailTypeDef]]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksVolumeTypeDef]]

### podName
- **Type**: typing.Optional[str]

### nodeName
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksMetadataOutputTypeDef]

### shareProcessNamespace
- **Type**: typing.Optional[bool]


# EksPodPropertiesOutputTypeDef

### serviceAccountName
- **Type**: typing.Optional[str]

### hostNetwork
- **Type**: typing.Optional[bool]

### dnsPolicy
- **Type**: typing.Optional[str]

### imagePullSecrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.ImagePullSecretTypeDef]]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksContainerOutputTypeDef]]

### initContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksContainerOutputTypeDef]]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksVolumeTypeDef]]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksMetadataOutputTypeDef]

### shareProcessNamespace
- **Type**: typing.Optional[bool]


# EksPodPropertiesOverrideTypeDef

### containers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EksContainerOverrideTypeDef]]

### initContainers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EksContainerOverrideTypeDef]]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksMetadataUnionTypeDef]


# EksPodPropertiesTypeDef

### serviceAccountName
- **Type**: typing.Optional[str]

### hostNetwork
- **Type**: typing.Optional[bool]

### dnsPolicy
- **Type**: typing.Optional[str]

### imagePullSecrets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ImagePullSecretTypeDef]]

### containers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EksContainerTypeDef]]

### initContainers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EksContainerTypeDef]]

### volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EksVolumeTypeDef]]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksMetadataTypeDef]

### shareProcessNamespace
- **Type**: typing.Optional[bool]


# EksPropertiesDetailTypeDef

### podProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPodPropertiesDetailTypeDef]


# EksPropertiesOutputTypeDef

### podProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPodPropertiesOutputTypeDef]


# EksPropertiesOverrideTypeDef

### podProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPodPropertiesOverrideTypeDef]


# EksPropertiesTypeDef

### podProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPodPropertiesTypeDef]


# EksSecretTypeDef

### secretName
- **Type**: <class 'str'>
- **Required**: Yes

### optional
- **Type**: typing.Optional[bool]


# EksVolumeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### hostPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksHostPathTypeDef]

### emptyDir
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksEmptyDirTypeDef]

### secret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksSecretTypeDef]

### persistentVolumeClaim
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPersistentVolumeClaimTypeDef]


# EphemeralStorageTypeDef

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# EvaluateOnExitTypeDef

### action
- **Type**: typing.Literal['EXIT', 'RETRY']
- **Required**: Yes

### onStatusReason
- **Type**: typing.Optional[str]

### onReason
- **Type**: typing.Optional[str]

### onExitCode
- **Type**: typing.Optional[str]


# FairsharePolicyOutputTypeDef

### shareDecaySeconds
- **Type**: typing.Optional[int]

### computeReservation
- **Type**: typing.Optional[int]

### shareDistribution
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.ShareAttributesTypeDef]]


# FairsharePolicyTypeDef

### shareDecaySeconds
- **Type**: typing.Optional[int]

### computeReservation
- **Type**: typing.Optional[int]

### shareDistribution
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ShareAttributesTypeDef]]


# FairsharePolicyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FargatePlatformConfigurationTypeDef

### platformVersion
- **Type**: typing.Optional[str]


# FrontOfQueueDetailTypeDef

### jobs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.FrontOfQueueJobSummaryTypeDef]]

### lastUpdatedAt
- **Type**: typing.Optional[int]


# FrontOfQueueJobSummaryTypeDef

### jobArn
- **Type**: typing.Optional[str]

### earliestTimeAtPosition
- **Type**: typing.Optional[int]


# GetJobQueueSnapshotRequestTypeDef

### jobQueue
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobQueueSnapshotResponseTypeDef

### frontOfQueue
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.FrontOfQueueDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HostTypeDef

### sourcePath
- **Type**: typing.Optional[str]


# ImagePullSecretTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# JobDefinitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobDependencyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobDetailTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobQueue
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'PENDING', 'RUNNABLE', 'RUNNING', 'STARTING', 'SUBMITTED', 'SUCCEEDED']
- **Required**: Yes

### startedAt
- **Type**: <class 'int'>
- **Required**: Yes

### jobDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### jobArn
- **Type**: typing.Optional[str]

### shareIdentifier
- **Type**: typing.Optional[str]

### schedulingPriority
- **Type**: typing.Optional[int]

### attempts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.AttemptDetailTypeDef]]

### statusReason
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[int]

### retryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RetryStrategyOutputTypeDef]

### stoppedAt
- **Type**: typing.Optional[int]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.JobDependencyTypeDef]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ContainerDetailTypeDef]

### nodeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NodeDetailsTypeDef]

### nodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NodePropertiesOutputTypeDef]

### arrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ArrayPropertiesDetailTypeDef]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.JobTimeoutTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### propagateTags
- **Type**: typing.Optional[bool]

### platformCapabilities
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'FARGATE']]]

### eksProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPropertiesDetailTypeDef]

### eksAttempts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EksAttemptDetailTypeDef]]

### ecsProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EcsPropertiesDetailTypeDef]

### isCancelled
- **Type**: typing.Optional[bool]

### isTerminated
- **Type**: typing.Optional[bool]

### consumableResourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ConsumableResourcePropertiesOutputTypeDef]


# JobQueueDetailTypeDef

### jobQueueName
- **Type**: <class 'str'>
- **Required**: Yes

### jobQueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### computeEnvironmentOrder
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.ComputeEnvironmentOrderTypeDef]
- **Required**: Yes

### schedulingPolicyArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETED', 'DELETING', 'INVALID', 'UPDATING', 'VALID']]

### statusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### jobStateTimeLimitActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.JobStateTimeLimitActionTypeDef]]


# JobStateTimeLimitActionTypeDef

### reason
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['RUNNABLE']
- **Required**: Yes

### maxTimeSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### action
- **Type**: typing.Literal['CANCEL']
- **Required**: Yes


# JobSummaryTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'RUNNABLE', 'RUNNING', 'STARTING', 'SUBMITTED', 'SUCCEEDED']]

### statusReason
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[int]

### stoppedAt
- **Type**: typing.Optional[int]

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ContainerSummaryTypeDef]

### arrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ArrayPropertiesSummaryTypeDef]

### nodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NodePropertiesSummaryTypeDef]

### jobDefinition
- **Type**: typing.Optional[str]


# JobTimeoutTypeDef

### attemptDurationSeconds
- **Type**: typing.Optional[int]


# KeyValuePairTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# KeyValuesPairTypeDef

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchTemplateSpecificationOutputTypeDef

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.LaunchTemplateSpecificationOverrideOutputTypeDef]]


# LaunchTemplateSpecificationOverrideOutputTypeDef

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### targetInstanceTypes
- **Type**: typing.Optional[typing.List[str]]


# LaunchTemplateSpecificationOverrideTypeDef

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### targetInstanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# LaunchTemplateSpecificationOverrideUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LaunchTemplateSpecificationTypeDef

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.LaunchTemplateSpecificationOverrideUnionTypeDef]]


# LinuxParametersOutputTypeDef

### devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.DeviceOutputTypeDef]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.TmpfsOutputTypeDef]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# LinuxParametersTypeDef

### devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.DeviceTypeDef]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.TmpfsTypeDef]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# ListConsumableResourcesRequestPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuesPairTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.PaginatorConfigTypeDef]


# ListConsumableResourcesRequestTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuesPairTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConsumableResourcesResponseTypeDef

### consumableResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.ConsumableResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsByConsumableResourceRequestPaginateTypeDef

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuesPairTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.PaginatorConfigTypeDef]


# ListJobsByConsumableResourceRequestTypeDef

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuesPairTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobsByConsumableResourceResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.ListJobsByConsumableResourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsByConsumableResourceSummaryTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobQueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: <class 'str'>
- **Required**: Yes

### quantity
- **Type**: <class 'int'>
- **Required**: Yes

### createdAt
- **Type**: <class 'int'>
- **Required**: Yes

### consumableResourceProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ConsumableResourcePropertiesOutputTypeDef'>
- **Required**: Yes

### jobDefinitionArn
- **Type**: typing.Optional[str]

### shareIdentifier
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[int]


# ListJobsRequestPaginateTypeDef

### jobQueue
- **Type**: typing.Optional[str]

### arrayJobId
- **Type**: typing.Optional[str]

### multiNodeJobId
- **Type**: typing.Optional[str]

### jobStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'RUNNABLE', 'RUNNING', 'STARTING', 'SUBMITTED', 'SUCCEEDED']]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuesPairTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.PaginatorConfigTypeDef]


# ListJobsRequestTypeDef

### jobQueue
- **Type**: typing.Optional[str]

### arrayJobId
- **Type**: typing.Optional[str]

### multiNodeJobId
- **Type**: typing.Optional[str]

### jobStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'RUNNABLE', 'RUNNING', 'STARTING', 'SUBMITTED', 'SUCCEEDED']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuesPairTypeDef]]


# ListJobsResponseTypeDef

### jobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.JobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSchedulingPoliciesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.PaginatorConfigTypeDef]


# ListSchedulingPoliciesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSchedulingPoliciesResponseTypeDef

### schedulingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.SchedulingPolicyListingDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogConfigurationOutputTypeDef

### logDriver
- **Type**: typing.Literal['awslogs', 'fluentd', 'gelf', 'journald', 'json-file', 'splunk', 'syslog']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Dict[str, str]]

### secretOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.SecretTypeDef]]


# LogConfigurationTypeDef

### logDriver
- **Type**: typing.Literal['awslogs', 'fluentd', 'gelf', 'journald', 'json-file', 'splunk', 'syslog']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Mapping[str, str]]

### secretOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.SecretTypeDef]]


# MountPointTypeDef

### containerPath
- **Type**: typing.Optional[str]

### readOnly
- **Type**: typing.Optional[bool]

### sourceVolume
- **Type**: typing.Optional[str]


# NetworkConfigurationTypeDef

### assignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# NetworkInterfaceTypeDef

### attachmentId
- **Type**: typing.Optional[str]

### ipv6Address
- **Type**: typing.Optional[str]

### privateIpv4Address
- **Type**: typing.Optional[str]


# NodeDetailsTypeDef

### nodeIndex
- **Type**: typing.Optional[int]

### isMainNode
- **Type**: typing.Optional[bool]


# NodeOverridesTypeDef

### numNodes
- **Type**: typing.Optional[int]

### nodePropertyOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.NodePropertyOverrideTypeDef]]


# NodePropertiesOutputTypeDef

### numNodes
- **Type**: <class 'int'>
- **Required**: Yes

### mainNode
- **Type**: <class 'int'>
- **Required**: Yes

### nodeRangeProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch_classes.NodeRangePropertyOutputTypeDef]
- **Required**: Yes


# NodePropertiesSummaryTypeDef

### isMainNode
- **Type**: typing.Optional[bool]

### numNodes
- **Type**: typing.Optional[int]

### nodeIndex
- **Type**: typing.Optional[int]


# NodePropertiesTypeDef

### numNodes
- **Type**: <class 'int'>
- **Required**: Yes

### mainNode
- **Type**: <class 'int'>
- **Required**: Yes

### nodeRangeProperties
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.NodeRangePropertyTypeDef]
- **Required**: Yes


# NodePropertyOverrideTypeDef

### targetNodes
- **Type**: <class 'str'>
- **Required**: Yes

### containerOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ContainerOverridesTypeDef]

### ecsPropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EcsPropertiesOverrideTypeDef]

### instanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### eksPropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPropertiesOverrideTypeDef]

### consumableResourcePropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ConsumableResourcePropertiesUnionTypeDef]


# NodeRangePropertyOutputTypeDef

### targetNodes
- **Type**: <class 'str'>
- **Required**: Yes

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ContainerPropertiesOutputTypeDef]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### ecsProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EcsPropertiesOutputTypeDef]

### eksProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPropertiesOutputTypeDef]

### consumableResourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ConsumableResourcePropertiesOutputTypeDef]


# NodeRangePropertyTypeDef

### targetNodes
- **Type**: <class 'str'>
- **Required**: Yes

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ContainerPropertiesTypeDef]

### instanceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### ecsProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EcsPropertiesTypeDef]

### eksProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPropertiesTypeDef]

### consumableResourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ConsumableResourcePropertiesTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterJobDefinitionResponseTypeDef

### jobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### jobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RepositoryCredentialsTypeDef

### credentialsParameter
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceRequirementTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RetryStrategyOutputTypeDef

### attempts
- **Type**: typing.Optional[int]

### evaluateOnExit
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.EvaluateOnExitTypeDef]]


# RetryStrategyTypeDef

### attempts
- **Type**: typing.Optional[int]

### evaluateOnExit
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.EvaluateOnExitTypeDef]]


# RetryStrategyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuntimePlatformTypeDef

### operatingSystemFamily
- **Type**: typing.Optional[str]

### cpuArchitecture
- **Type**: typing.Optional[str]


# SchedulingPolicyDetailTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### fairsharePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.FairsharePolicyOutputTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SchedulingPolicyListingDetailTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# SecretTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### valueFrom
- **Type**: <class 'str'>
- **Required**: Yes


# ShareAttributesTypeDef

### shareIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### weightFactor
- **Type**: typing.Optional[float]


# SubmitJobRequestTypeDef

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobQueue
- **Type**: <class 'str'>
- **Required**: Yes

### jobDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### shareIdentifier
- **Type**: typing.Optional[str]

### schedulingPriorityOverride
- **Type**: typing.Optional[int]

### arrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ArrayPropertiesTypeDef]

### dependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.JobDependencyTypeDef]]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### containerOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ContainerOverridesTypeDef]

### nodeOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.NodeOverridesTypeDef]

### retryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RetryStrategyUnionTypeDef]

### propagateTags
- **Type**: typing.Optional[bool]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.JobTimeoutTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### eksPropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EksPropertiesOverrideTypeDef]

### ecsPropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EcsPropertiesOverrideTypeDef]

### consumableResourcePropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ConsumableResourcePropertiesUnionTypeDef]


# SubmitJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TaskContainerDependencyTypeDef

### containerName
- **Type**: typing.Optional[str]

### condition
- **Type**: typing.Optional[str]


# TaskContainerDetailsTypeDef

### command
- **Type**: typing.Optional[typing.List[str]]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.TaskContainerDependencyTypeDef]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.KeyValuePairTypeDef]]

### essential
- **Type**: typing.Optional[bool]

### image
- **Type**: typing.Optional[str]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LinuxParametersOutputTypeDef]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LogConfigurationOutputTypeDef]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.MountPointTypeDef]]

### name
- **Type**: typing.Optional[str]

### privileged
- **Type**: typing.Optional[bool]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RepositoryCredentialsTypeDef]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.ResourceRequirementTypeDef]]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.SecretTypeDef]]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.UlimitTypeDef]]

### user
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]

### logStreamName
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.NetworkInterfaceTypeDef]]


# TaskContainerOverridesTypeDef

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuePairTypeDef]]

### name
- **Type**: typing.Optional[str]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ResourceRequirementTypeDef]]


# TaskContainerPropertiesOutputTypeDef

### image
- **Type**: <class 'str'>
- **Required**: Yes

### command
- **Type**: typing.Optional[typing.List[str]]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.TaskContainerDependencyTypeDef]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.KeyValuePairTypeDef]]

### essential
- **Type**: typing.Optional[bool]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LinuxParametersOutputTypeDef]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LogConfigurationOutputTypeDef]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.MountPointTypeDef]]

### name
- **Type**: typing.Optional[str]

### privileged
- **Type**: typing.Optional[bool]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RepositoryCredentialsTypeDef]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.ResourceRequirementTypeDef]]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.SecretTypeDef]]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch_classes.UlimitTypeDef]]

### user
- **Type**: typing.Optional[str]


# TaskContainerPropertiesTypeDef

### image
- **Type**: <class 'str'>
- **Required**: Yes

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### dependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.TaskContainerDependencyTypeDef]]

### environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.KeyValuePairTypeDef]]

### essential
- **Type**: typing.Optional[bool]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LinuxParametersTypeDef]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.LogConfigurationTypeDef]

### mountPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.MountPointTypeDef]]

### name
- **Type**: typing.Optional[str]

### privileged
- **Type**: typing.Optional[bool]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.RepositoryCredentialsTypeDef]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ResourceRequirementTypeDef]]

### secrets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.SecretTypeDef]]

### ulimits
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.UlimitTypeDef]]

### user
- **Type**: typing.Optional[str]


# TaskPropertiesOverrideTypeDef

### containers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.TaskContainerOverridesTypeDef]]


# TerminateJobRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# TmpfsOutputTypeDef

### containerPath
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: <class 'int'>
- **Required**: Yes

### mountOptions
- **Type**: typing.Optional[typing.List[str]]


# TmpfsTypeDef

### containerPath
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: <class 'int'>
- **Required**: Yes

### mountOptions
- **Type**: typing.Optional[typing.Sequence[str]]


# UlimitTypeDef

### hardLimit
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### softLimit
- **Type**: <class 'int'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateComputeEnvironmentRequestTypeDef

### computeEnvironment
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### unmanagedvCpus
- **Type**: typing.Optional[int]

### computeResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.ComputeResourceUpdateTypeDef]

### serviceRole
- **Type**: typing.Optional[str]

### updatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.UpdatePolicyTypeDef]

### context
- **Type**: typing.Optional[str]


# UpdateComputeEnvironmentResponseTypeDef

### computeEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### computeEnvironmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConsumableResourceRequestTypeDef

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: typing.Optional[str]

### quantity
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]


# UpdateConsumableResourceResponseTypeDef

### consumableResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### consumableResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### totalQuantity
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateJobQueueRequestTypeDef

### jobQueue
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### schedulingPolicyArn
- **Type**: typing.Optional[str]

### priority
- **Type**: typing.Optional[int]

### computeEnvironmentOrder
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.ComputeEnvironmentOrderTypeDef]]

### jobStateTimeLimitActions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.batch_classes.JobStateTimeLimitActionTypeDef]]


# UpdateJobQueueResponseTypeDef

### jobQueueName
- **Type**: <class 'str'>
- **Required**: Yes

### jobQueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePolicyTypeDef

### terminateJobsOnUpdate
- **Type**: typing.Optional[bool]

### jobExecutionTimeoutMinutes
- **Type**: typing.Optional[int]


# UpdateSchedulingPolicyRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### fairsharePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.FairsharePolicyUnionTypeDef]


# VolumeTypeDef

### host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.HostTypeDef]

### name
- **Type**: typing.Optional[str]

### efsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch_classes.EFSVolumeConfigurationTypeDef]



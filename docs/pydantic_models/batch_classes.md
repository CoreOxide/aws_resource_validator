# Batch Classes

# ArrayProperties

### size
- **Type**: typing.Optional[int]


# ArrayPropertiesDetail

### statusSummary
- **Type**: typing.Optional[typing.Dict[str, int]]

### size
- **Type**: typing.Optional[int]

### index
- **Type**: typing.Optional[int]


# ArrayPropertiesSummary

### size
- **Type**: typing.Optional[int]

### index
- **Type**: typing.Optional[int]


# AttemptContainerDetail

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkInterface]]


# AttemptDetail

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.AttemptContainerDetail]

### startedAt
- **Type**: typing.Optional[int]

### stoppedAt
- **Type**: typing.Optional[int]

### statusReason
- **Type**: typing.Optional[str]

### taskProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.AttemptEcsTaskDetails]]


# AttemptEcsTaskDetails

### containerInstanceArn
- **Type**: typing.Optional[str]

### taskArn
- **Type**: typing.Optional[str]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.AttemptTaskContainerDetails]]


# AttemptTaskContainerDetails

### exitCode
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### logStreamName
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkInterface]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# ComputeEnvironmentDetail

### computeEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### computeEnvironmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### unmanagedvCpus
- **Type**: typing.Optional[int]

### ecsClusterArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['MANAGED', 'UNMANAGED']]

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETED', 'DELETING', 'INVALID', 'UPDATING', 'VALID']]

### statusReason
- **Type**: typing.Optional[str]

### computeResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ComputeResourceOutput]

### serviceRole
- **Type**: typing.Optional[str]

### updatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.UpdatePolicy]

### eksConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksConfiguration]

### containerOrchestrationType
- **Type**: typing.Optional[typing.Literal['ECS', 'EKS']]

### uuid
- **Type**: typing.Optional[str]

### context
- **Type**: typing.Optional[str]


# ComputeEnvironmentOrder

### order
- **Type**: <class 'int'>
- **Required**: Yes

### computeEnvironment
- **Type**: <class 'str'>
- **Required**: Yes


# ComputeResource

### type
- **Type**: typing.Literal['EC2', 'FARGATE', 'FARGATE_SPOT', 'SPOT']
- **Required**: Yes

### maxvCpus
- **Type**: <class 'int'>
- **Required**: Yes

### subnets
- **Type**: typing.List[str]
- **Required**: Yes

### allocationStrategy
- **Type**: typing.Optional[typing.Literal['BEST_FIT', 'BEST_FIT_PROGRESSIVE', 'SPOT_CAPACITY_OPTIMIZED', 'SPOT_PRICE_CAPACITY_OPTIMIZED']]

### minvCpus
- **Type**: typing.Optional[int]

### desiredvCpus
- **Type**: typing.Optional[int]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### imageId
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### ec2KeyPair
- **Type**: typing.Optional[str]

### instanceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### placementGroup
- **Type**: typing.Optional[str]

### bidPercentage
- **Type**: typing.Optional[int]

### spotIamFleetRole
- **Type**: typing.Optional[str]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LaunchTemplateSpecification]

### ec2Configuration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ec2Configuration]]


# ComputeResourceOutput

### type
- **Type**: typing.Literal['EC2', 'FARGATE', 'FARGATE_SPOT', 'SPOT']
- **Required**: Yes

### maxvCpus
- **Type**: <class 'int'>
- **Required**: Yes

### subnets
- **Type**: typing.List[str]
- **Required**: Yes

### allocationStrategy
- **Type**: typing.Optional[typing.Literal['BEST_FIT', 'BEST_FIT_PROGRESSIVE', 'SPOT_CAPACITY_OPTIMIZED', 'SPOT_PRICE_CAPACITY_OPTIMIZED']]

### minvCpus
- **Type**: typing.Optional[int]

### desiredvCpus
- **Type**: typing.Optional[int]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### imageId
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### ec2KeyPair
- **Type**: typing.Optional[str]

### instanceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### placementGroup
- **Type**: typing.Optional[str]

### bidPercentage
- **Type**: typing.Optional[int]

### spotIamFleetRole
- **Type**: typing.Optional[str]

### launchTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LaunchTemplateSpecificationOutput]

### ec2Configuration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ec2Configuration]]


# ComputeResourceUpdate

### minvCpus
- **Type**: typing.Optional[int]

### maxvCpus
- **Type**: typing.Optional[int]

### desiredvCpus
- **Type**: typing.Optional[int]

### subnets
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### allocationStrategy
- **Type**: typing.Optional[typing.Literal['BEST_FIT_PROGRESSIVE', 'SPOT_CAPACITY_OPTIMIZED', 'SPOT_PRICE_CAPACITY_OPTIMIZED']]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### ec2KeyPair
- **Type**: typing.Optional[str]

### instanceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### placementGroup
- **Type**: typing.Optional[str]

### bidPercentage
- **Type**: typing.Optional[int]

### launchTemplate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.LaunchTemplateSpecification, aws_resource_validator.pydantic_models.batch.batch_classes.LaunchTemplateSpecificationOutput, NoneType]

### ec2Configuration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ec2Configuration]]

### updateToLatestImageVersion
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[typing.Literal['EC2', 'FARGATE', 'FARGATE_SPOT', 'SPOT']]

### imageId
- **Type**: typing.Optional[str]


# ConsumableResourceProperties

### consumableResourceList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourceRequirement]]


# ConsumableResourcePropertiesOutput

### consumableResourceList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourceRequirement]]


# ConsumableResourceRequirement

### consumableResource
- **Type**: typing.Optional[str]

### quantity
- **Type**: typing.Optional[int]


# ConsumableResourceSummary

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


# ContainerDetail

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Volume]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuePair]]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.MountPoint]]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ulimit]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkInterface]]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ResourceRequirement]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LinuxParametersOutput]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LogConfigurationOutput]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Secret]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkConfiguration]

### fargatePlatformConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.FargatePlatformConfiguration]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EphemeralStorage]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RuntimePlatform]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RepositoryCredentials]


# ContainerOverrides

### vcpus
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### command
- **Type**: typing.Optional[typing.List[str]]

### instanceType
- **Type**: typing.Optional[str]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuePair]]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ResourceRequirement]]


# ContainerProperties

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Volume]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuePair]]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.MountPoint]]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### privileged
- **Type**: typing.Optional[bool]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ulimit]]

### user
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ResourceRequirement]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LinuxParameters]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LogConfiguration]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Secret]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkConfiguration]

### fargatePlatformConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.FargatePlatformConfiguration]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EphemeralStorage]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RuntimePlatform]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RepositoryCredentials]


# ContainerPropertiesOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Volume]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuePair]]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.MountPoint]]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### privileged
- **Type**: typing.Optional[bool]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ulimit]]

### user
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[str]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ResourceRequirement]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LinuxParametersOutput]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LogConfigurationOutput]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Secret]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkConfiguration]

### fargatePlatformConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.FargatePlatformConfiguration]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EphemeralStorage]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RuntimePlatform]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RepositoryCredentials]


# ContainerSummary

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]


# CreateComputeEnvironmentRequest

### computeEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['MANAGED', 'UNMANAGED']
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### unmanagedvCpus
- **Type**: typing.Optional[int]

### computeResources
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.ComputeResource, aws_resource_validator.pydantic_models.batch.batch_classes.ComputeResourceOutput, NoneType]

### serviceRole
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### eksConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksConfiguration]

### context
- **Type**: typing.Optional[str]


# CreateComputeEnvironmentResponse

### computeEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### computeEnvironmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConsumableResourceRequest

### consumableResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### totalQuantity
- **Type**: typing.Optional[int]

### resourceType
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConsumableResourceResponse

### consumableResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### consumableResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobQueueRequest

### jobQueueName
- **Type**: <class 'str'>
- **Required**: Yes

### priority
- **Type**: <class 'int'>
- **Required**: Yes

### computeEnvironmentOrder
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ComputeEnvironmentOrder]
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### schedulingPolicyArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### jobStateTimeLimitActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobStateTimeLimitAction]]


# CreateJobQueueResponse

### jobQueueName
- **Type**: <class 'str'>
- **Required**: Yes

### jobQueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSchedulingPolicyRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### fairsharePolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.FairsharePolicy, aws_resource_validator.pydantic_models.batch.batch_classes.FairsharePolicyOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSchedulingPolicyResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteComputeEnvironmentRequest

### computeEnvironment
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConsumableResourceRequest

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobQueueRequest

### jobQueue
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSchedulingPolicyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterJobDefinitionRequest

### jobDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeComputeEnvironmentsRequest

### computeEnvironments
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeComputeEnvironmentsRequestPaginate

### computeEnvironments
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.PaginatorConfig]


# DescribeComputeEnvironmentsResponse

### computeEnvironments
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ComputeEnvironmentDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeConsumableResourceRequest

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeConsumableResourceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobDefinitionsRequest

### jobDefinitions
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### jobDefinitionName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobDefinitionsRequestPaginate

### jobDefinitions
- **Type**: typing.Optional[typing.List[str]]

### jobDefinitionName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.PaginatorConfig]


# DescribeJobDefinitionsResponse

### jobDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobQueuesRequest

### jobQueues
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobQueuesRequestPaginate

### jobQueues
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.PaginatorConfig]


# DescribeJobQueuesResponse

### jobQueues
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobQueueDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeJobsRequest

### jobs
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeJobsResponse

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSchedulingPoliciesRequest

### arns
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeSchedulingPoliciesResponse

### schedulingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.SchedulingPolicyDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# Device

### hostPath
- **Type**: <class 'str'>
- **Required**: Yes

### containerPath
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.List[typing.Literal['MKNOD', 'READ', 'WRITE']]]


# DeviceOutput

### hostPath
- **Type**: <class 'str'>
- **Required**: Yes

### containerPath
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.List[typing.Literal['MKNOD', 'READ', 'WRITE']]]


# EFSAuthorizationConfig

### accessPointId
- **Type**: typing.Optional[str]

### iam
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# EFSVolumeConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EFSAuthorizationConfig]


# Ec2Configuration

### imageType
- **Type**: <class 'str'>
- **Required**: Yes

### imageIdOverride
- **Type**: typing.Optional[str]

### imageKubernetesVersion
- **Type**: typing.Optional[str]


# EcsProperties

### taskProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EcsTaskProperties]
- **Required**: Yes


# EcsPropertiesDetail

### taskProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EcsTaskDetails]]


# EcsPropertiesOutput

### taskProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EcsTaskPropertiesOutput]
- **Required**: Yes


# EcsPropertiesOverride

### taskProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TaskPropertiesOverride]]


# EcsTaskDetails

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TaskContainerDetails]]

### containerInstanceArn
- **Type**: typing.Optional[str]

### taskArn
- **Type**: typing.Optional[str]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EphemeralStorage]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkConfiguration]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RuntimePlatform]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Volume]]


# EcsTaskProperties

### containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TaskContainerProperties]
- **Required**: Yes

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EphemeralStorage]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkConfiguration]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RuntimePlatform]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Volume]]


# EcsTaskPropertiesOutput

### containers
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TaskContainerPropertiesOutput]
- **Required**: Yes

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EphemeralStorage]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkConfiguration]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RuntimePlatform]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Volume]]


# EksAttemptContainerDetail

### name
- **Type**: typing.Optional[str]

### containerID
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]


# EksAttemptDetail

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksAttemptContainerDetail]]

### initContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksAttemptContainerDetail]]

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


# EksConfiguration

### eksClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### kubernetesNamespace
- **Type**: <class 'str'>
- **Required**: Yes


# EksContainer

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerEnvironmentVariable]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerResourceRequirements]

### volumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerVolumeMount]]

### securityContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerSecurityContext]


# EksContainerDetail

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerEnvironmentVariable]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerResourceRequirementsOutput]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]

### volumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerVolumeMount]]

### securityContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerSecurityContext]


# EksContainerEnvironmentVariable

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# EksContainerOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerEnvironmentVariable]]

### resources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerResourceRequirementsOutput]

### volumeMounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerVolumeMount]]

### securityContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerSecurityContext]


# EksContainerOverride

### name
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.List[str]]

### args
- **Type**: typing.Optional[typing.List[str]]

### env
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerEnvironmentVariable]]

### resources
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerResourceRequirements, aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerResourceRequirementsOutput, NoneType]


# EksContainerResourceRequirements

### limits
- **Type**: typing.Optional[typing.Dict[str, str]]

### requests
- **Type**: typing.Optional[typing.Dict[str, str]]


# EksContainerResourceRequirementsOutput

### limits
- **Type**: typing.Optional[typing.Dict[str, str]]

### requests
- **Type**: typing.Optional[typing.Dict[str, str]]


# EksContainerSecurityContext

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


# EksContainerVolumeMount

### name
- **Type**: typing.Optional[str]

### mountPath
- **Type**: typing.Optional[str]

### subPath
- **Type**: typing.Optional[str]

### readOnly
- **Type**: typing.Optional[bool]


# EksEmptyDir

### medium
- **Type**: typing.Optional[str]

### sizeLimit
- **Type**: typing.Optional[str]


# EksHostPath

### path
- **Type**: typing.Optional[str]


# EksMetadata

### labels
- **Type**: typing.Optional[typing.Dict[str, str]]

### annotations
- **Type**: typing.Optional[typing.Dict[str, str]]

### namespace
- **Type**: typing.Optional[str]


# EksMetadataOutput

### labels
- **Type**: typing.Optional[typing.Dict[str, str]]

### annotations
- **Type**: typing.Optional[typing.Dict[str, str]]

### namespace
- **Type**: typing.Optional[str]


# EksPersistentVolumeClaim

### claimName
- **Type**: <class 'str'>
- **Required**: Yes

### readOnly
- **Type**: typing.Optional[bool]


# EksPodProperties

### serviceAccountName
- **Type**: typing.Optional[str]

### hostNetwork
- **Type**: typing.Optional[bool]

### dnsPolicy
- **Type**: typing.Optional[str]

### imagePullSecrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ImagePullSecret]]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainer]]

### initContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainer]]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksVolume]]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksMetadata]

### shareProcessNamespace
- **Type**: typing.Optional[bool]


# EksPodPropertiesDetail

### serviceAccountName
- **Type**: typing.Optional[str]

### hostNetwork
- **Type**: typing.Optional[bool]

### dnsPolicy
- **Type**: typing.Optional[str]

### imagePullSecrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ImagePullSecret]]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerDetail]]

### initContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerDetail]]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksVolume]]

### podName
- **Type**: typing.Optional[str]

### nodeName
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksMetadataOutput]

### shareProcessNamespace
- **Type**: typing.Optional[bool]


# EksPodPropertiesOutput

### serviceAccountName
- **Type**: typing.Optional[str]

### hostNetwork
- **Type**: typing.Optional[bool]

### dnsPolicy
- **Type**: typing.Optional[str]

### imagePullSecrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ImagePullSecret]]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerOutput]]

### initContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerOutput]]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksVolume]]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksMetadataOutput]

### shareProcessNamespace
- **Type**: typing.Optional[bool]


# EksPodPropertiesOverride

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerOverride]]

### initContainers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksContainerOverride]]

### metadata
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.EksMetadata, aws_resource_validator.pydantic_models.batch.batch_classes.EksMetadataOutput, NoneType]


# EksProperties

### podProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPodProperties]


# EksPropertiesDetail

### podProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPodPropertiesDetail]


# EksPropertiesOutput

### podProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPodPropertiesOutput]


# EksPropertiesOverride

### podProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPodPropertiesOverride]


# EksSecret

### secretName
- **Type**: <class 'str'>
- **Required**: Yes

### optional
- **Type**: typing.Optional[bool]


# EksVolume

### name
- **Type**: <class 'str'>
- **Required**: Yes

### hostPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksHostPath]

### emptyDir
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksEmptyDir]

### secret
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksSecret]

### persistentVolumeClaim
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPersistentVolumeClaim]


# EphemeralStorage

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# EvaluateOnExit

### action
- **Type**: typing.Literal['EXIT', 'RETRY']
- **Required**: Yes

### onStatusReason
- **Type**: typing.Optional[str]

### onReason
- **Type**: typing.Optional[str]

### onExitCode
- **Type**: typing.Optional[str]


# FairsharePolicy

### shareDecaySeconds
- **Type**: typing.Optional[int]

### computeReservation
- **Type**: typing.Optional[int]

### shareDistribution
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ShareAttributes]]


# FairsharePolicyOutput

### shareDecaySeconds
- **Type**: typing.Optional[int]

### computeReservation
- **Type**: typing.Optional[int]

### shareDistribution
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ShareAttributes]]


# FargatePlatformConfiguration

### platformVersion
- **Type**: typing.Optional[str]


# FrontOfQueueDetail

### jobs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.FrontOfQueueJobSummary]]

### lastUpdatedAt
- **Type**: typing.Optional[int]


# FrontOfQueueJobSummary

### jobArn
- **Type**: typing.Optional[str]

### earliestTimeAtPosition
- **Type**: typing.Optional[int]


# GetJobQueueSnapshotRequest

### jobQueue
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobQueueSnapshotResponse

### frontOfQueue
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.FrontOfQueueDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# Host

### sourcePath
- **Type**: typing.Optional[str]


# ImagePullSecret

### name
- **Type**: <class 'str'>
- **Required**: Yes


# JobDefinition

### jobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### jobDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'int'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[str]

### schedulingPriority
- **Type**: typing.Optional[int]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### retryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RetryStrategyOutput]

### containerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ContainerPropertiesOutput]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.JobTimeout]

### nodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NodePropertiesOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### propagateTags
- **Type**: typing.Optional[bool]

### platformCapabilities
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'FARGATE']]]

### ecsProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EcsPropertiesOutput]

### eksProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPropertiesOutput]

### containerOrchestrationType
- **Type**: typing.Optional[typing.Literal['ECS', 'EKS']]

### consumableResourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourcePropertiesOutput]


# JobDependency

### jobId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['N_TO_N', 'SEQUENTIAL']]


# JobDetail

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.AttemptDetail]]

### statusReason
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[int]

### retryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RetryStrategyOutput]

### stoppedAt
- **Type**: typing.Optional[int]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobDependency]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ContainerDetail]

### nodeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NodeDetails]

### nodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NodePropertiesOutput]

### arrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ArrayPropertiesDetail]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.JobTimeout]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### propagateTags
- **Type**: typing.Optional[bool]

### platformCapabilities
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'FARGATE']]]

### eksProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPropertiesDetail]

### eksAttempts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EksAttemptDetail]]

### ecsProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EcsPropertiesDetail]

### isCancelled
- **Type**: typing.Optional[bool]

### isTerminated
- **Type**: typing.Optional[bool]

### consumableResourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourcePropertiesOutput]


# JobQueueDetail

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ComputeEnvironmentOrder]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobStateTimeLimitAction]]


# JobStateTimeLimitAction

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


# JobSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ContainerSummary]

### arrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ArrayPropertiesSummary]

### nodeProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NodePropertiesSummary]

### jobDefinition
- **Type**: typing.Optional[str]


# JobTimeout

### attemptDurationSeconds
- **Type**: typing.Optional[int]


# KeyValuePair

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# KeyValuesPair

### name
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# LaunchTemplateSpecification

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### overrides
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.LaunchTemplateSpecificationOverride, aws_resource_validator.pydantic_models.batch.batch_classes.LaunchTemplateSpecificationOverrideOutput]]]


# LaunchTemplateSpecificationOutput

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.LaunchTemplateSpecificationOverrideOutput]]


# LaunchTemplateSpecificationOverride

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### targetInstanceTypes
- **Type**: typing.Optional[typing.List[str]]


# LaunchTemplateSpecificationOverrideOutput

### launchTemplateId
- **Type**: typing.Optional[str]

### launchTemplateName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### targetInstanceTypes
- **Type**: typing.Optional[typing.List[str]]


# LinuxParameters

### devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Device]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Tmpfs]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# LinuxParametersOutput

### devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.DeviceOutput]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TmpfsOutput]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# ListConsumableResourcesRequest

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuesPair]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConsumableResourcesRequestPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuesPair]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.PaginatorConfig]


# ListConsumableResourcesResponse

### consumableResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsByConsumableResourceRequest

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuesPair]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListJobsByConsumableResourceRequestPaginate

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuesPair]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.PaginatorConfig]


# ListJobsByConsumableResourceResponse

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ListJobsByConsumableResourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsByConsumableResourceSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourcePropertiesOutput'>
- **Required**: Yes

### jobDefinitionArn
- **Type**: typing.Optional[str]

### shareIdentifier
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[int]


# ListJobsRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuesPair]]


# ListJobsRequestPaginate

### jobQueue
- **Type**: typing.Optional[str]

### arrayJobId
- **Type**: typing.Optional[str]

### multiNodeJobId
- **Type**: typing.Optional[str]

### jobStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'RUNNABLE', 'RUNNING', 'STARTING', 'SUBMITTED', 'SUCCEEDED']]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuesPair]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.PaginatorConfig]


# ListJobsResponse

### jobSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSchedulingPoliciesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSchedulingPoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.PaginatorConfig]


# ListSchedulingPoliciesResponse

### schedulingPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.SchedulingPolicyListingDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# LogConfiguration

### logDriver
- **Type**: typing.Literal['awslogs', 'fluentd', 'gelf', 'journald', 'json-file', 'splunk', 'syslog']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Dict[str, str]]

### secretOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Secret]]


# LogConfigurationOutput

### logDriver
- **Type**: typing.Literal['awslogs', 'fluentd', 'gelf', 'journald', 'json-file', 'splunk', 'syslog']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Dict[str, str]]

### secretOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Secret]]


# MountPoint

### containerPath
- **Type**: typing.Optional[str]

### readOnly
- **Type**: typing.Optional[bool]

### sourceVolume
- **Type**: typing.Optional[str]


# NetworkConfiguration

### assignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# NetworkInterface

### attachmentId
- **Type**: typing.Optional[str]

### ipv6Address
- **Type**: typing.Optional[str]

### privateIpv4Address
- **Type**: typing.Optional[str]


# NodeDetails

### nodeIndex
- **Type**: typing.Optional[int]

### isMainNode
- **Type**: typing.Optional[bool]


# NodeOverrides

### numNodes
- **Type**: typing.Optional[int]

### nodePropertyOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.NodePropertyOverride]]


# NodeProperties

### numNodes
- **Type**: <class 'int'>
- **Required**: Yes

### mainNode
- **Type**: <class 'int'>
- **Required**: Yes

### nodeRangeProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.NodeRangeProperty]
- **Required**: Yes


# NodePropertiesOutput

### numNodes
- **Type**: <class 'int'>
- **Required**: Yes

### mainNode
- **Type**: <class 'int'>
- **Required**: Yes

### nodeRangeProperties
- **Type**: typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.NodeRangePropertyOutput]
- **Required**: Yes


# NodePropertiesSummary

### isMainNode
- **Type**: typing.Optional[bool]

### numNodes
- **Type**: typing.Optional[int]

### nodeIndex
- **Type**: typing.Optional[int]


# NodePropertyOverride

### targetNodes
- **Type**: <class 'str'>
- **Required**: Yes

### containerOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ContainerOverrides]

### ecsPropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EcsPropertiesOverride]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### eksPropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPropertiesOverride]

### consumableResourcePropertiesOverride
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourceProperties, aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourcePropertiesOutput, NoneType]


# NodeRangeProperty

### targetNodes
- **Type**: <class 'str'>
- **Required**: Yes

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ContainerProperties]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### ecsProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EcsProperties]

### eksProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksProperties]

### consumableResourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourceProperties]


# NodeRangePropertyOutput

### targetNodes
- **Type**: <class 'str'>
- **Required**: Yes

### container
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ContainerPropertiesOutput]

### instanceTypes
- **Type**: typing.Optional[typing.List[str]]

### ecsProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EcsPropertiesOutput]

### eksProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPropertiesOutput]

### consumableResourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourcePropertiesOutput]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterJobDefinitionRequest

### jobDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['container', 'multinode']
- **Required**: Yes

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### schedulingPriority
- **Type**: typing.Optional[int]

### containerProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.ContainerProperties, aws_resource_validator.pydantic_models.batch.batch_classes.ContainerPropertiesOutput, NoneType]

### nodeProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.NodeProperties, aws_resource_validator.pydantic_models.batch.batch_classes.NodePropertiesOutput, NoneType]

### retryStrategy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.RetryStrategy, aws_resource_validator.pydantic_models.batch.batch_classes.RetryStrategyOutput, NoneType]

### propagateTags
- **Type**: typing.Optional[bool]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.JobTimeout]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### platformCapabilities
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'FARGATE']]]

### eksProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.EksProperties, aws_resource_validator.pydantic_models.batch.batch_classes.EksPropertiesOutput, NoneType]

### ecsProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.EcsProperties, aws_resource_validator.pydantic_models.batch.batch_classes.EcsPropertiesOutput, NoneType]

### consumableResourceProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourceProperties, aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourcePropertiesOutput, NoneType]


# RegisterJobDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# RepositoryCredentials

### credentialsParameter
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceRequirement

### value
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['GPU', 'MEMORY', 'VCPU']
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


# RetryStrategy

### attempts
- **Type**: typing.Optional[int]

### evaluateOnExit
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EvaluateOnExit]]


# RetryStrategyOutput

### attempts
- **Type**: typing.Optional[int]

### evaluateOnExit
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.EvaluateOnExit]]


# RuntimePlatform

### operatingSystemFamily
- **Type**: typing.Optional[str]

### cpuArchitecture
- **Type**: typing.Optional[str]


# SchedulingPolicyDetail

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### fairsharePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.FairsharePolicyOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SchedulingPolicyListingDetail

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# Secret

### name
- **Type**: <class 'str'>
- **Required**: Yes

### valueFrom
- **Type**: <class 'str'>
- **Required**: Yes


# ShareAttributes

### shareIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### weightFactor
- **Type**: typing.Optional[float]


# SubmitJobRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ArrayProperties]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobDependency]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### containerOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ContainerOverrides]

### nodeOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.NodeOverrides]

### retryStrategy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.RetryStrategy, aws_resource_validator.pydantic_models.batch.batch_classes.RetryStrategyOutput, NoneType]

### propagateTags
- **Type**: typing.Optional[bool]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.JobTimeout]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### eksPropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EksPropertiesOverride]

### ecsPropertiesOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EcsPropertiesOverride]

### consumableResourcePropertiesOverride
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourceProperties, aws_resource_validator.pydantic_models.batch.batch_classes.ConsumableResourcePropertiesOutput, NoneType]


# SubmitJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TaskContainerDependency

### containerName
- **Type**: typing.Optional[str]

### condition
- **Type**: typing.Optional[str]


# TaskContainerDetails

### command
- **Type**: typing.Optional[typing.List[str]]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TaskContainerDependency]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuePair]]

### essential
- **Type**: typing.Optional[bool]

### image
- **Type**: typing.Optional[str]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LinuxParametersOutput]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LogConfigurationOutput]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.MountPoint]]

### name
- **Type**: typing.Optional[str]

### privileged
- **Type**: typing.Optional[bool]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RepositoryCredentials]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ResourceRequirement]]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Secret]]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ulimit]]

### user
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]

### logStreamName
- **Type**: typing.Optional[str]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.NetworkInterface]]


# TaskContainerOverrides

### command
- **Type**: typing.Optional[typing.List[str]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuePair]]

### name
- **Type**: typing.Optional[str]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ResourceRequirement]]


# TaskContainerProperties

### image
- **Type**: <class 'str'>
- **Required**: Yes

### command
- **Type**: typing.Optional[typing.List[str]]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TaskContainerDependency]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuePair]]

### essential
- **Type**: typing.Optional[bool]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LinuxParameters]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LogConfiguration]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.MountPoint]]

### name
- **Type**: typing.Optional[str]

### privileged
- **Type**: typing.Optional[bool]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RepositoryCredentials]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ResourceRequirement]]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Secret]]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ulimit]]

### user
- **Type**: typing.Optional[str]


# TaskContainerPropertiesOutput

### image
- **Type**: <class 'str'>
- **Required**: Yes

### command
- **Type**: typing.Optional[typing.List[str]]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TaskContainerDependency]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.KeyValuePair]]

### essential
- **Type**: typing.Optional[bool]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LinuxParametersOutput]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.LogConfigurationOutput]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.MountPoint]]

### name
- **Type**: typing.Optional[str]

### privileged
- **Type**: typing.Optional[bool]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.RepositoryCredentials]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ResourceRequirement]]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Secret]]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.Ulimit]]

### user
- **Type**: typing.Optional[str]


# TaskPropertiesOverride

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.TaskContainerOverrides]]


# TerminateJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# Tmpfs

### containerPath
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: <class 'int'>
- **Required**: Yes

### mountOptions
- **Type**: typing.Optional[typing.List[str]]


# TmpfsOutput

### containerPath
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: <class 'int'>
- **Required**: Yes

### mountOptions
- **Type**: typing.Optional[typing.List[str]]


# Ulimit

### hardLimit
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### softLimit
- **Type**: <class 'int'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateComputeEnvironmentRequest

### computeEnvironment
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### unmanagedvCpus
- **Type**: typing.Optional[int]

### computeResources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.ComputeResourceUpdate]

### serviceRole
- **Type**: typing.Optional[str]

### updatePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.UpdatePolicy]

### context
- **Type**: typing.Optional[str]


# UpdateComputeEnvironmentResponse

### computeEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### computeEnvironmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConsumableResourceRequest

### consumableResource
- **Type**: <class 'str'>
- **Required**: Yes

### operation
- **Type**: typing.Optional[str]

### quantity
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]


# UpdateConsumableResourceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateJobQueueRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.ComputeEnvironmentOrder]]

### jobStateTimeLimitActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.batch.batch_classes.JobStateTimeLimitAction]]


# UpdateJobQueueResponse

### jobQueueName
- **Type**: <class 'str'>
- **Required**: Yes

### jobQueueArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.batch.batch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePolicy

### terminateJobsOnUpdate
- **Type**: typing.Optional[bool]

### jobExecutionTimeoutMinutes
- **Type**: typing.Optional[int]


# UpdateSchedulingPolicyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### fairsharePolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.batch.batch_classes.FairsharePolicy, aws_resource_validator.pydantic_models.batch.batch_classes.FairsharePolicyOutput, NoneType]


# Volume

### host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.Host]

### name
- **Type**: typing.Optional[str]

### efsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.batch.batch_classes.EFSVolumeConfiguration]



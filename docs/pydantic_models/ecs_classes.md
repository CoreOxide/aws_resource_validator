# Ecs Classes

# Attachment

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttachmentStateChange

### attachmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes


# Attribute

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]

### targetType
- **Type**: typing.Optional[typing.Literal['container-instance']]

### targetId
- **Type**: typing.Optional[str]


# AutoScalingGroupProvider

### autoScalingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### managedScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ManagedScaling]

### managedTerminationProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### managedDraining
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AutoScalingGroupProviderUpdate

### managedScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ManagedScaling]

### managedTerminationProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### managedDraining
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfiguration

### subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### assignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationOutput

### subnets
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### assignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityProvider

### capacityProviderArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### autoScalingGroupProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.AutoScalingGroupProvider]

### updateStatus
- **Type**: typing.Optional[typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### updateStatusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]]


# CapacityProviderStrategyItem

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### base
- **Type**: typing.Optional[int]


# Cluster

### clusterArn
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterConfiguration]

### status
- **Type**: typing.Optional[str]

### registeredContainerInstancesCount
- **Type**: typing.Optional[int]

### runningTasksCount
- **Type**: typing.Optional[int]

### pendingTasksCount
- **Type**: typing.Optional[int]

### activeServicesCount
- **Type**: typing.Optional[int]

### statistics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePair]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### settings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ClusterSetting]]

### capacityProviders
- **Type**: typing.Optional[typing.List[str]]

### defaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]]

### attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attachment]]

### attachmentsStatus
- **Type**: typing.Optional[str]

### serviceConnectDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterServiceConnectDefaults]


# ClusterConfiguration

### executeCommandConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ExecuteCommandConfiguration]

### managedStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ManagedStorageConfiguration]


# ClusterServiceConnectDefaults

### namespace
- **Type**: typing.Optional[str]


# ClusterServiceConnectDefaultsRequest

### namespace
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterSetting

### name
- **Type**: typing.Optional[typing.Literal['containerInsights']]

### value
- **Type**: typing.Optional[str]


# Container

### containerArn
- **Type**: typing.Optional[str]

### taskArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### imageDigest
- **Type**: typing.Optional[str]

### runtimeId
- **Type**: typing.Optional[str]

### lastStatus
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]

### networkBindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.NetworkBinding]]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.NetworkInterface]]

### healthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]

### managedAgents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ManagedAgent]]

### cpu
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### memoryReservation
- **Type**: typing.Optional[str]

### gpuIds
- **Type**: typing.Optional[typing.List[str]]


# ContainerDefinition

### name
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RepositoryCredentials]

### cpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]

### links
- **Type**: typing.Optional[typing.Sequence[str]]

### portMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PortMapping]]

### essential
- **Type**: typing.Optional[bool]

### restartPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ContainerRestartPolicyUnion]

### entryPoint
- **Type**: typing.Optional[typing.Sequence[str]]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePair]]

### environmentFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EnvironmentFile]]

### mountPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.MountPoint]]

### volumesFrom
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.VolumeFrom]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LinuxParametersUnion]

### secrets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Secret]]

### dependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerDependency]]

### startTimeout
- **Type**: typing.Optional[int]

### stopTimeout
- **Type**: typing.Optional[int]

### versionConsistency
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### hostname
- **Type**: typing.Optional[str]

### user
- **Type**: typing.Optional[str]

### workingDirectory
- **Type**: typing.Optional[str]

### disableNetworking
- **Type**: typing.Optional[bool]

### privileged
- **Type**: typing.Optional[bool]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### dnsServers
- **Type**: typing.Optional[typing.Sequence[str]]

### dnsSearchDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### extraHosts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.HostEntry]]

### dockerSecurityOptions
- **Type**: typing.Optional[typing.Sequence[str]]

### interactive
- **Type**: typing.Optional[bool]

### pseudoTerminal
- **Type**: typing.Optional[bool]

### dockerLabels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ulimits
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Ulimit]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfigurationUnion]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HealthCheckUnion]

### systemControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.SystemControl]]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirement]]

### firelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FirelensConfigurationUnion]

### credentialSpecs
- **Type**: typing.Optional[typing.Sequence[str]]


# ContainerDefinitionOutput

### name
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RepositoryCredentials]

### cpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]

### links
- **Type**: typing.Optional[typing.List[str]]

### portMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.PortMapping]]

### essential
- **Type**: typing.Optional[bool]

### restartPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ContainerRestartPolicyOutput]

### entryPoint
- **Type**: typing.Optional[typing.List[str]]

### command
- **Type**: typing.Optional[typing.List[str]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePair]]

### environmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.EnvironmentFile]]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.MountPoint]]

### volumesFrom
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.VolumeFrom]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LinuxParametersOutput]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Secret]]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerDependency]]

### startTimeout
- **Type**: typing.Optional[int]

### stopTimeout
- **Type**: typing.Optional[int]

### versionConsistency
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### hostname
- **Type**: typing.Optional[str]

### user
- **Type**: typing.Optional[str]

### workingDirectory
- **Type**: typing.Optional[str]

### disableNetworking
- **Type**: typing.Optional[bool]

### privileged
- **Type**: typing.Optional[bool]

### readonlyRootFilesystem
- **Type**: typing.Optional[bool]

### dnsServers
- **Type**: typing.Optional[typing.List[str]]

### dnsSearchDomains
- **Type**: typing.Optional[typing.List[str]]

### extraHosts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.HostEntry]]

### dockerSecurityOptions
- **Type**: typing.Optional[typing.List[str]]

### interactive
- **Type**: typing.Optional[bool]

### pseudoTerminal
- **Type**: typing.Optional[bool]

### dockerLabels
- **Type**: typing.Optional[typing.Dict[str, str]]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Ulimit]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfigurationOutput]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HealthCheckOutput]

### systemControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.SystemControl]]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirement]]

### firelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FirelensConfigurationOutput]

### credentialSpecs
- **Type**: typing.Optional[typing.List[str]]


# ContainerDefinitionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerDependency

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Literal['COMPLETE', 'HEALTHY', 'START', 'SUCCESS']
- **Required**: Yes


# ContainerImage

### containerName
- **Type**: typing.Optional[str]

### imageDigest
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]


# ContainerInstance

### containerInstanceArn
- **Type**: typing.Optional[str]

### ec2InstanceId
- **Type**: typing.Optional[str]

### capacityProviderName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[int]

### versionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.VersionInfo]

### remainingResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ResourceOutput]]

### registeredResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ResourceOutput]]

### status
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### agentConnected
- **Type**: typing.Optional[bool]

### runningTasksCount
- **Type**: typing.Optional[int]

### pendingTasksCount
- **Type**: typing.Optional[int]

### agentUpdateStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'STAGED', 'STAGING', 'UPDATED', 'UPDATING']]

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attribute]]

### registeredAt
- **Type**: typing.Optional[datetime.datetime]

### attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attachment]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### healthStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ContainerInstanceHealthStatus]


# ContainerInstanceHealthStatus

### overallStatus
- **Type**: typing.Optional[typing.Literal['IMPAIRED', 'INITIALIZING', 'INSUFFICIENT_DATA', 'OK']]

### details
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.InstanceHealthCheckResult]]


# ContainerOverride

### name
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePair]]

### environmentFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EnvironmentFile]]

### cpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirement]]


# ContainerOverrideOutput

### name
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.List[str]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePair]]

### environmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.EnvironmentFile]]

### cpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirement]]


# ContainerRestartPolicy

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ignoredExitCodes
- **Type**: typing.Optional[typing.Sequence[int]]

### restartAttemptPeriod
- **Type**: typing.Optional[int]


# ContainerRestartPolicyOutput

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ignoredExitCodes
- **Type**: typing.Optional[typing.List[int]]

### restartAttemptPeriod
- **Type**: typing.Optional[int]


# ContainerRestartPolicyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerStateChange

### containerName
- **Type**: typing.Optional[str]

### imageDigest
- **Type**: typing.Optional[str]

### runtimeId
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### networkBindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.NetworkBinding]]

### reason
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]


# CreateCapacityProviderRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### autoScalingGroupProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.AutoScalingGroupProvider'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]


# CreateCapacityProviderResponse

### capacityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.CapacityProvider'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClusterRequest

### clusterName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### settings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ClusterSetting]]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterConfiguration]

### capacityProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### defaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]]

### serviceConnectDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterServiceConnectDefaultsRequest]


# CreateClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceRequest

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### taskDefinition
- **Type**: typing.Optional[str]

### availabilityZoneRebalancing
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### loadBalancers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancer]]

### serviceRegistries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistry]]

### desiredCount
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]]

### platformVersion
- **Type**: typing.Optional[str]

### role
- **Type**: typing.Optional[str]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationUnion]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraint]]

### placementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategy]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnion]

### healthCheckGracePeriodSeconds
- **Type**: typing.Optional[int]

### schedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### deploymentController
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentController]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### enableECSManagedTags
- **Type**: typing.Optional[bool]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### enableExecuteCommand
- **Type**: typing.Optional[bool]

### serviceConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationUnion]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationUnion]]

### vpcLatticeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.VpcLatticeConfiguration]]


# CreateServiceResponse

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTaskSetRequest

### service
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### taskDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnion]

### loadBalancers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancer]]

### serviceRegistries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistry]]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]]

### platformVersion
- **Type**: typing.Optional[str]

### scale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.Scale]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]


# CreateTaskSetResponse

### taskSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# CreatedAt

### before
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.Timestamp]

### after
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.Timestamp]


# DeleteAccountSettingRequest

### name
- **Type**: typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']
- **Required**: Yes

### principalArn
- **Type**: typing.Optional[str]


# DeleteAccountSettingResponse

### setting
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Setting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAttributesRequest

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Attribute]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# DeleteAttributesResponse

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCapacityProviderRequest

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCapacityProviderResponse

### capacityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.CapacityProvider'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceRequest

### service
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# DeleteServiceResponse

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTaskDefinitionsRequest

### taskDefinitions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteTaskDefinitionsResponse

### taskDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskDefinition]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTaskSetRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### service
- **Type**: <class 'str'>
- **Required**: Yes

### taskSet
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeleteTaskSetResponse

### taskSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# Deployment

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentAlarms

### alarmNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### rollback
- **Type**: <class 'bool'>
- **Required**: Yes

### enable
- **Type**: <class 'bool'>
- **Required**: Yes


# DeploymentAlarmsOutput

### alarmNames
- **Type**: typing.List[str]
- **Required**: Yes

### rollback
- **Type**: <class 'bool'>
- **Required**: Yes

### enable
- **Type**: <class 'bool'>
- **Required**: Yes


# DeploymentCircuitBreaker

### enable
- **Type**: <class 'bool'>
- **Required**: Yes

### rollback
- **Type**: <class 'bool'>
- **Required**: Yes


# DeploymentConfiguration

### deploymentCircuitBreaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentCircuitBreaker]

### maximumPercent
- **Type**: typing.Optional[int]

### minimumHealthyPercent
- **Type**: typing.Optional[int]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentAlarms]


# DeploymentConfigurationOutput

### deploymentCircuitBreaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentCircuitBreaker]

### maximumPercent
- **Type**: typing.Optional[int]

### minimumHealthyPercent
- **Type**: typing.Optional[int]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentAlarmsOutput]


# DeploymentConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentController

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentEphemeralStorage

### kmsKeyId
- **Type**: typing.Optional[str]


# DeregisterContainerInstanceRequest

### containerInstance
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# DeregisterContainerInstanceResponse

### containerInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ContainerInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterTaskDefinitionRequest

### taskDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTaskDefinitionResponse

### taskDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCapacityProvidersRequest

### capacityProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeCapacityProvidersResponse

### capacityProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProvider]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeClustersRequest

### clusters
- **Type**: typing.Optional[typing.Sequence[str]]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ATTACHMENTS', 'CONFIGURATIONS', 'SETTINGS', 'STATISTICS', 'TAGS']]]


# DescribeClustersResponse

### clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Cluster]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeContainerInstancesRequest

### containerInstances
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTAINER_INSTANCE_HEALTH', 'TAGS']]]


# DescribeContainerInstancesResponse

### containerInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerInstance]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServiceDeploymentsRequest

### serviceDeploymentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeServiceDeploymentsResponse

### serviceDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceDeployment]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServiceRevisionsRequest

### serviceRevisionArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeServiceRevisionsResponse

### serviceRevisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRevision]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServicesRequest

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeServicesRequestWait

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeServicesRequestWaitExtra

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeServicesResponse

### services
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Service]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTaskDefinitionRequest

### taskDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeTaskDefinitionResponse

### taskDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskDefinition'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTaskSetsRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### service
- **Type**: <class 'str'>
- **Required**: Yes

### taskSets
- **Type**: typing.Optional[typing.Sequence[str]]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeTaskSetsResponse

### taskSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskSet]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTasksRequest

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeTasksRequestWait

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTasksRequestWaitExtra

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTasksResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Task]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# Device

### hostPath
- **Type**: <class 'str'>
- **Required**: Yes

### containerPath
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['mknod', 'read', 'write']]]


# DeviceOutput

### hostPath
- **Type**: <class 'str'>
- **Required**: Yes

### containerPath
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.List[typing.Literal['mknod', 'read', 'write']]]


# DeviceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DiscoverPollEndpointRequest

### containerInstance
- **Type**: typing.Optional[str]

### cluster
- **Type**: typing.Optional[str]


# DiscoverPollEndpointResponse

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### telemetryEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### serviceConnectEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# DockerVolumeConfiguration

### scope
- **Type**: typing.Optional[typing.Literal['shared', 'task']]

### autoprovision
- **Type**: typing.Optional[bool]

### driver
- **Type**: typing.Optional[str]

### driverOpts
- **Type**: typing.Optional[typing.Mapping[str, str]]

### labels
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DockerVolumeConfigurationOutput

### scope
- **Type**: typing.Optional[typing.Literal['shared', 'task']]

### autoprovision
- **Type**: typing.Optional[bool]

### driver
- **Type**: typing.Optional[str]

### driverOpts
- **Type**: typing.Optional[typing.Dict[str, str]]

### labels
- **Type**: typing.Optional[typing.Dict[str, str]]


# DockerVolumeConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EBSTagSpecification

### resourceType
- **Type**: typing.Literal['volume']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]


# EBSTagSpecificationOutput

### resourceType
- **Type**: typing.Literal['volume']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]


# EBSTagSpecificationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EFSAuthorizationConfig]


# EnvironmentFile

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EphemeralStorage

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# ExecuteCommandConfiguration

### kmsKeyId
- **Type**: typing.Optional[str]

### logging
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NONE', 'OVERRIDE']]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ExecuteCommandLogConfiguration]


# ExecuteCommandLogConfiguration

### cloudWatchLogGroupName
- **Type**: typing.Optional[str]

### cloudWatchEncryptionEnabled
- **Type**: typing.Optional[bool]

### s3BucketName
- **Type**: typing.Optional[str]

### s3EncryptionEnabled
- **Type**: typing.Optional[bool]

### s3KeyPrefix
- **Type**: typing.Optional[str]


# ExecuteCommandRequest

### command
- **Type**: <class 'str'>
- **Required**: Yes

### interactive
- **Type**: <class 'bool'>
- **Required**: Yes

### task
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### container
- **Type**: typing.Optional[str]


# ExecuteCommandResponse

### clusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### containerArn
- **Type**: <class 'str'>
- **Required**: Yes

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### interactive
- **Type**: <class 'bool'>
- **Required**: Yes

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Session'>
- **Required**: Yes

### taskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# FSxWindowsFileServerAuthorizationConfig

### credentialsParameter
- **Type**: <class 'str'>
- **Required**: Yes

### domain
- **Type**: <class 'str'>
- **Required**: Yes


# FSxWindowsFileServerVolumeConfiguration

### fileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### rootDirectory
- **Type**: <class 'str'>
- **Required**: Yes

### authorizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.FSxWindowsFileServerAuthorizationConfig'>
- **Required**: Yes


# Failure

### arn
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### detail
- **Type**: typing.Optional[str]


# FirelensConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FirelensConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetTaskProtectionRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### tasks
- **Type**: typing.Optional[typing.Sequence[str]]


# GetTaskProtectionResponse

### protectedTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ProtectedTask]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# HealthCheck

### command
- **Type**: typing.Sequence[str]
- **Required**: Yes

### interval
- **Type**: typing.Optional[int]

### timeout
- **Type**: typing.Optional[int]

### retries
- **Type**: typing.Optional[int]

### startPeriod
- **Type**: typing.Optional[int]


# HealthCheckOutput

### command
- **Type**: typing.List[str]
- **Required**: Yes

### interval
- **Type**: typing.Optional[int]

### timeout
- **Type**: typing.Optional[int]

### retries
- **Type**: typing.Optional[int]

### startPeriod
- **Type**: typing.Optional[int]


# HealthCheckUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HostEntry

### hostname
- **Type**: <class 'str'>
- **Required**: Yes

### ipAddress
- **Type**: <class 'str'>
- **Required**: Yes


# HostVolumeProperties

### sourcePath
- **Type**: typing.Optional[str]


# InferenceAccelerator

### deviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deviceType
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceAcceleratorOverride

### deviceName
- **Type**: typing.Optional[str]

### deviceType
- **Type**: typing.Optional[str]


# InstanceHealthCheckResult

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KernelCapabilities

### add
- **Type**: typing.Optional[typing.Sequence[str]]

### drop
- **Type**: typing.Optional[typing.Sequence[str]]


# KernelCapabilitiesOutput

### add
- **Type**: typing.Optional[typing.List[str]]

### drop
- **Type**: typing.Optional[typing.List[str]]


# KernelCapabilitiesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeyValuePair

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# LinuxParameters

### capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.KernelCapabilitiesUnion]

### devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.DeviceUnion]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TmpfsUnion]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# LinuxParametersOutput

### capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.KernelCapabilitiesOutput]

### devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.DeviceOutput]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TmpfsOutput]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# LinuxParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccountSettingsRequest

### name
- **Type**: typing.Optional[typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']]

### value
- **Type**: typing.Optional[str]

### principalArn
- **Type**: typing.Optional[str]

### effectiveSettings
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAccountSettingsRequestPaginate

### name
- **Type**: typing.Optional[typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']]

### value
- **Type**: typing.Optional[str]

### principalArn
- **Type**: typing.Optional[str]

### effectiveSettings
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfig]


# ListAccountSettingsResponse

### settings
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Setting]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttributesRequest

### targetType
- **Type**: typing.Literal['container-instance']
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### attributeName
- **Type**: typing.Optional[str]

### attributeValue
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListAttributesRequestPaginate

### targetType
- **Type**: typing.Literal['container-instance']
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### attributeName
- **Type**: typing.Optional[str]

### attributeValue
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfig]


# ListAttributesResponse

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListClustersRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListClustersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfig]


# ListClustersResponse

### clusterArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContainerInstancesResponse

### containerInstanceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceDeploymentsRequest

### service
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['IN_PROGRESS', 'PENDING', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCESSFUL', 'STOPPED', 'STOP_REQUESTED', 'SUCCESSFUL']]]

### createdAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.CreatedAt]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListServiceDeploymentsResponse

### serviceDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceDeploymentBrief]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicesByNamespaceRequest

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListServicesByNamespaceRequestPaginate

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfig]


# ListServicesByNamespaceResponse

### serviceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicesRequest

### cluster
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### schedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]


# ListServicesRequestPaginate

### cluster
- **Type**: typing.Optional[str]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### schedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfig]


# ListServicesResponse

### serviceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# ListTaskDefinitionFamiliesRequest

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ALL', 'INACTIVE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTaskDefinitionFamiliesRequestPaginate

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ALL', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfig]


# ListTaskDefinitionFamiliesResponse

### families
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTaskDefinitionsRequest

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETE_IN_PROGRESS', 'INACTIVE']]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTaskDefinitionsRequestPaginate

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETE_IN_PROGRESS', 'INACTIVE']]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfig]


# ListTaskDefinitionsResponse

### taskDefinitionArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTasksRequest

### cluster
- **Type**: typing.Optional[str]

### containerInstance
- **Type**: typing.Optional[str]

### family
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### startedBy
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### desiredStatus
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'STOPPED']]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]


# ListTasksRequestPaginate

### cluster
- **Type**: typing.Optional[str]

### containerInstance
- **Type**: typing.Optional[str]

### family
- **Type**: typing.Optional[str]

### startedBy
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### desiredStatus
- **Type**: typing.Optional[typing.Literal['PENDING', 'RUNNING', 'STOPPED']]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfig]


# ListTasksResponse

### taskArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LoadBalancer

### targetGroupArn
- **Type**: typing.Optional[str]

### loadBalancerName
- **Type**: typing.Optional[str]

### containerName
- **Type**: typing.Optional[str]

### containerPort
- **Type**: typing.Optional[int]


# LogConfiguration

### logDriver
- **Type**: typing.Literal['awsfirelens', 'awslogs', 'fluentd', 'gelf', 'journald', 'json-file', 'splunk', 'syslog']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Mapping[str, str]]

### secretOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Secret]]


# LogConfigurationOutput

### logDriver
- **Type**: typing.Literal['awsfirelens', 'awslogs', 'fluentd', 'gelf', 'journald', 'json-file', 'splunk', 'syslog']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Dict[str, str]]

### secretOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Secret]]


# LogConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ManagedAgent

### lastStartedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[typing.Literal['ExecuteCommandAgent']]

### reason
- **Type**: typing.Optional[str]

### lastStatus
- **Type**: typing.Optional[str]


# ManagedAgentStateChange

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### managedAgentName
- **Type**: typing.Literal['ExecuteCommandAgent']
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# ManagedScaling

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### targetCapacity
- **Type**: typing.Optional[int]

### minimumScalingStepSize
- **Type**: typing.Optional[int]

### maximumScalingStepSize
- **Type**: typing.Optional[int]

### instanceWarmupPeriod
- **Type**: typing.Optional[int]


# ManagedStorageConfiguration

### kmsKeyId
- **Type**: typing.Optional[str]

### fargateEphemeralStorageKmsKeyId
- **Type**: typing.Optional[str]


# MountPoint

### sourceVolume
- **Type**: typing.Optional[str]

### containerPath
- **Type**: typing.Optional[str]

### readOnly
- **Type**: typing.Optional[bool]


# NetworkBinding

### bindIP
- **Type**: typing.Optional[str]

### containerPort
- **Type**: typing.Optional[int]

### hostPort
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['tcp', 'udp']]

### containerPortRange
- **Type**: typing.Optional[str]

### hostPortRange
- **Type**: typing.Optional[str]


# NetworkConfiguration

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.AwsVpcConfiguration]


# NetworkConfigurationOutput

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.AwsVpcConfigurationOutput]


# NetworkConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkInterface

### attachmentId
- **Type**: typing.Optional[str]

### privateIpv4Address
- **Type**: typing.Optional[str]

### ipv6Address
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacementConstraint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PlacementStrategy

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PlatformDevice

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PortMapping

### containerPort
- **Type**: typing.Optional[int]

### hostPort
- **Type**: typing.Optional[int]

### protocol
- **Type**: typing.Optional[typing.Literal['tcp', 'udp']]

### name
- **Type**: typing.Optional[str]

### appProtocol
- **Type**: typing.Optional[typing.Literal['grpc', 'http', 'http2']]

### containerPortRange
- **Type**: typing.Optional[str]


# ProtectedTask

### taskArn
- **Type**: typing.Optional[str]

### protectionEnabled
- **Type**: typing.Optional[bool]

### expirationDate
- **Type**: typing.Optional[datetime.datetime]


# ProxyConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProxyConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutAccountSettingDefaultRequest

### name
- **Type**: typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PutAccountSettingDefaultResponse

### setting
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Setting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# PutAccountSettingRequest

### name
- **Type**: typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: typing.Optional[str]


# PutAccountSettingResponse

### setting
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Setting'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# PutAttributesRequest

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Attribute]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# PutAttributesResponse

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# PutClusterCapacityProvidersRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### capacityProviders
- **Type**: typing.Sequence[str]
- **Required**: Yes

### defaultCapacityProviderStrategy
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]
- **Required**: Yes


# PutClusterCapacityProvidersResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterContainerInstanceRequest

### cluster
- **Type**: typing.Optional[str]

### instanceIdentityDocument
- **Type**: typing.Optional[str]

### instanceIdentityDocumentSignature
- **Type**: typing.Optional[str]

### totalResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ResourceUnion]]

### versionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.VersionInfo]

### containerInstanceArn
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Attribute]]

### platformDevices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlatformDevice]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]


# RegisterContainerInstanceResponse

### containerInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ContainerInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterTaskDefinitionRequest

### family
- **Type**: <class 'str'>
- **Required**: Yes

### containerDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerDefinitionUnion]
- **Required**: Yes

### taskRoleArn
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### networkMode
- **Type**: typing.Optional[typing.Literal['awsvpc', 'bridge', 'host', 'none']]

### volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.VolumeUnion]]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TaskDefinitionPlacementConstraint]]

### requiresCompatibilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]]

### cpu
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### pidMode
- **Type**: typing.Optional[typing.Literal['host', 'task']]

### ipcMode
- **Type**: typing.Optional[typing.Literal['host', 'none', 'task']]

### proxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ProxyConfigurationUnion]

### inferenceAccelerators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.InferenceAccelerator]]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorage]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RuntimePlatform]

### enableFaultInjection
- **Type**: typing.Optional[bool]


# RegisterTaskDefinitionResponse

### taskDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskDefinition'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# RepositoryCredentials

### credentialsParameter
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceRequirement

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# Rollback

### reason
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### serviceRevisionArn
- **Type**: typing.Optional[str]


# RunTaskRequest

### taskDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### capacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]]

### cluster
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### enableECSManagedTags
- **Type**: typing.Optional[bool]

### enableExecuteCommand
- **Type**: typing.Optional[bool]

### group
- **Type**: typing.Optional[str]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnion]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskOverrideUnion]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraint]]

### placementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategy]]

### platformVersion
- **Type**: typing.Optional[str]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### referenceId
- **Type**: typing.Optional[str]

### startedBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### clientToken
- **Type**: typing.Optional[str]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TaskVolumeConfiguration]]


# RunTaskResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Task]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# RuntimePlatform

### cpuArchitecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]

### operatingSystemFamily
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS_SERVER_2004_CORE', 'WINDOWS_SERVER_2016_FULL', 'WINDOWS_SERVER_2019_CORE', 'WINDOWS_SERVER_2019_FULL', 'WINDOWS_SERVER_2022_CORE', 'WINDOWS_SERVER_2022_FULL', 'WINDOWS_SERVER_20H2_CORE']]


# Scale

### value
- **Type**: typing.Optional[float]

### unit
- **Type**: typing.Optional[typing.Literal['PERCENT']]


# Secret

### name
- **Type**: <class 'str'>
- **Required**: Yes

### valueFrom
- **Type**: <class 'str'>
- **Required**: Yes


# Service

### serviceArn
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### clusterArn
- **Type**: typing.Optional[str]

### loadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancer]]

### serviceRegistries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistry]]

### status
- **Type**: typing.Optional[str]

### desiredCount
- **Type**: typing.Optional[int]

### runningCount
- **Type**: typing.Optional[int]

### pendingCount
- **Type**: typing.Optional[int]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]]

### platformVersion
- **Type**: typing.Optional[str]

### platformFamily
- **Type**: typing.Optional[str]

### taskDefinition
- **Type**: typing.Optional[str]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationOutput]

### taskSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskSet]]

### deployments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Deployment]]

### roleArn
- **Type**: typing.Optional[str]

### events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceEvent]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### placementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraint]]

### placementStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategy]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationOutput]

### healthCheckGracePeriodSeconds
- **Type**: typing.Optional[int]

### schedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### deploymentController
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentController]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### createdBy
- **Type**: typing.Optional[str]

### enableECSManagedTags
- **Type**: typing.Optional[bool]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### enableExecuteCommand
- **Type**: typing.Optional[bool]

### availabilityZoneRebalancing
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ServiceConnectClientAlias

### port
- **Type**: <class 'int'>
- **Required**: Yes

### dnsName
- **Type**: typing.Optional[str]


# ServiceConnectConfiguration

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### services
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectService]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfiguration]


# ServiceConnectConfigurationOutput

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectServiceOutput]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfigurationOutput]


# ServiceConnectConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceConnectService

### portName
- **Type**: <class 'str'>
- **Required**: Yes

### discoveryName
- **Type**: typing.Optional[str]

### clientAliases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectClientAlias]]

### ingressPortOverride
- **Type**: typing.Optional[int]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimeoutConfiguration]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectTlsConfiguration]


# ServiceConnectServiceOutput

### portName
- **Type**: <class 'str'>
- **Required**: Yes

### discoveryName
- **Type**: typing.Optional[str]

### clientAliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectClientAlias]]

### ingressPortOverride
- **Type**: typing.Optional[int]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimeoutConfiguration]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectTlsConfiguration]


# ServiceConnectServiceResource

### discoveryName
- **Type**: typing.Optional[str]

### discoveryArn
- **Type**: typing.Optional[str]


# ServiceConnectTlsCertificateAuthority

### awsPcaAuthorityArn
- **Type**: typing.Optional[str]


# ServiceConnectTlsConfiguration

### issuerCertificateAuthority
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectTlsCertificateAuthority'>
- **Required**: Yes

### kmsKey
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# ServiceDeployment

### serviceDeploymentArn
- **Type**: typing.Optional[str]

### serviceArn
- **Type**: typing.Optional[str]

### clusterArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### finishedAt
- **Type**: typing.Optional[datetime.datetime]

### stoppedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### sourceServiceRevisions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRevisionSummary]]

### targetServiceRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceRevisionSummary]

### status
- **Type**: typing.Optional[typing.Literal['IN_PROGRESS', 'PENDING', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCESSFUL', 'STOPPED', 'STOP_REQUESTED', 'SUCCESSFUL']]

### statusReason
- **Type**: typing.Optional[str]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationOutput]

### rollback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.Rollback]

### deploymentCircuitBreaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceDeploymentCircuitBreaker]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceDeploymentAlarms]


# ServiceDeploymentAlarms

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'MONITORING', 'MONITORING_COMPLETE', 'TRIGGERED']]

### alarmNames
- **Type**: typing.Optional[typing.List[str]]

### triggeredAlarmNames
- **Type**: typing.Optional[typing.List[str]]


# ServiceDeploymentBrief

### serviceDeploymentArn
- **Type**: typing.Optional[str]

### serviceArn
- **Type**: typing.Optional[str]

### clusterArn
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### finishedAt
- **Type**: typing.Optional[datetime.datetime]

### targetServiceRevisionArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['IN_PROGRESS', 'PENDING', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCESSFUL', 'STOPPED', 'STOP_REQUESTED', 'SUCCESSFUL']]

### statusReason
- **Type**: typing.Optional[str]


# ServiceDeploymentCircuitBreaker

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'MONITORING', 'MONITORING_COMPLETE', 'TRIGGERED']]

### failureCount
- **Type**: typing.Optional[int]

### threshold
- **Type**: typing.Optional[int]


# ServiceEvent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceManagedEBSVolumeConfiguration

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]

### volumeType
- **Type**: typing.Optional[str]

### sizeInGiB
- **Type**: typing.Optional[int]

### snapshotId
- **Type**: typing.Optional[str]

### iops
- **Type**: typing.Optional[int]

### throughput
- **Type**: typing.Optional[int]

### tagSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EBSTagSpecificationUnion]]

### filesystemType
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'ntfs', 'xfs']]


# ServiceManagedEBSVolumeConfigurationOutput

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]

### volumeType
- **Type**: typing.Optional[str]

### sizeInGiB
- **Type**: typing.Optional[int]

### snapshotId
- **Type**: typing.Optional[str]

### iops
- **Type**: typing.Optional[int]

### throughput
- **Type**: typing.Optional[int]

### tagSpecifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.EBSTagSpecificationOutput]]

### filesystemType
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'ntfs', 'xfs']]


# ServiceManagedEBSVolumeConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceRegistry

### registryArn
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### containerName
- **Type**: typing.Optional[str]

### containerPort
- **Type**: typing.Optional[int]


# ServiceRevision

### serviceRevisionArn
- **Type**: typing.Optional[str]

### serviceArn
- **Type**: typing.Optional[str]

### clusterArn
- **Type**: typing.Optional[str]

### taskDefinition
- **Type**: typing.Optional[str]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### platformVersion
- **Type**: typing.Optional[str]

### platformFamily
- **Type**: typing.Optional[str]

### loadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancer]]

### serviceRegistries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistry]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationOutput]

### containerImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerImage]]

### guardDutyEnabled
- **Type**: typing.Optional[bool]

### serviceConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationOutput]

### volumeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationOutput]]

### fargateEphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentEphemeralStorage]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### vpcLatticeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.VpcLatticeConfiguration]]


# ServiceRevisionSummary

### arn
- **Type**: typing.Optional[str]

### requestedTaskCount
- **Type**: typing.Optional[int]

### runningTaskCount
- **Type**: typing.Optional[int]

### pendingTaskCount
- **Type**: typing.Optional[int]


# ServiceVolumeConfiguration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### managedEBSVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceManagedEBSVolumeConfigurationUnion]


# ServiceVolumeConfigurationOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### managedEBSVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceManagedEBSVolumeConfigurationOutput]


# ServiceVolumeConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Session

### sessionId
- **Type**: typing.Optional[str]

### streamUrl
- **Type**: typing.Optional[str]

### tokenValue
- **Type**: typing.Optional[str]


# Setting

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartTaskRequest

### containerInstances
- **Type**: typing.Sequence[str]
- **Required**: Yes

### taskDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### enableECSManagedTags
- **Type**: typing.Optional[bool]

### enableExecuteCommand
- **Type**: typing.Optional[bool]

### group
- **Type**: typing.Optional[str]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnion]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskOverrideUnion]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### referenceId
- **Type**: typing.Optional[str]

### startedBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TaskVolumeConfiguration]]


# StartTaskResponse

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Task]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# StopTaskRequest

### task
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# StopTaskResponse

### task
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Task'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# SubmitAttachmentStateChangesRequest

### attachments
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.AttachmentStateChange]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# SubmitAttachmentStateChangesResponse

### acknowledgment
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# SubmitContainerStateChangeRequest

### cluster
- **Type**: typing.Optional[str]

### task
- **Type**: typing.Optional[str]

### containerName
- **Type**: typing.Optional[str]

### runtimeId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### reason
- **Type**: typing.Optional[str]

### networkBindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.NetworkBinding]]


# SubmitContainerStateChangeResponse

### acknowledgment
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# SubmitTaskStateChangeRequest

### cluster
- **Type**: typing.Optional[str]

### task
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### containers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerStateChange]]

### attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.AttachmentStateChange]]

### managedAgents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ManagedAgentStateChange]]

### pullStartedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.Timestamp]

### pullStoppedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.Timestamp]

### executionStoppedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.Timestamp]


# SubmitTaskStateChangeResponse

### acknowledgment
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# SystemControl

### namespace
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.Tag]
- **Required**: Yes


# Task

### attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attachment]]

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attribute]]

### availabilityZone
- **Type**: typing.Optional[str]

### capacityProviderName
- **Type**: typing.Optional[str]

### clusterArn
- **Type**: typing.Optional[str]

### connectivity
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### connectivityAt
- **Type**: typing.Optional[datetime.datetime]

### containerInstanceArn
- **Type**: typing.Optional[str]

### containers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Container]]

### cpu
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### desiredStatus
- **Type**: typing.Optional[str]

### enableExecuteCommand
- **Type**: typing.Optional[bool]

### executionStoppedAt
- **Type**: typing.Optional[datetime.datetime]

### group
- **Type**: typing.Optional[str]

### healthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]

### inferenceAccelerators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.InferenceAccelerator]]

### lastStatus
- **Type**: typing.Optional[str]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### memory
- **Type**: typing.Optional[str]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskOverrideOutput]

### platformVersion
- **Type**: typing.Optional[str]

### platformFamily
- **Type**: typing.Optional[str]

### pullStartedAt
- **Type**: typing.Optional[datetime.datetime]

### pullStoppedAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### startedBy
- **Type**: typing.Optional[str]

### stopCode
- **Type**: typing.Optional[typing.Literal['EssentialContainerExited', 'ServiceSchedulerInitiated', 'SpotInterruption', 'TaskFailedToStart', 'TerminationNotice', 'UserInitiated']]

### stoppedAt
- **Type**: typing.Optional[datetime.datetime]

### stoppedReason
- **Type**: typing.Optional[str]

### stoppingAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Tag]]

### taskArn
- **Type**: typing.Optional[str]

### taskDefinitionArn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[int]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorage]

### fargateEphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskEphemeralStorage]


# TaskDefinition

### taskDefinitionArn
- **Type**: typing.Optional[str]

### containerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerDefinitionOutput]]

### family
- **Type**: typing.Optional[str]

### taskRoleArn
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### networkMode
- **Type**: typing.Optional[typing.Literal['awsvpc', 'bridge', 'host', 'none']]

### revision
- **Type**: typing.Optional[int]

### volumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.VolumeOutput]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETE_IN_PROGRESS', 'INACTIVE']]

### requiresAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.Attribute]]

### placementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskDefinitionPlacementConstraint]]

### compatibilities
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RuntimePlatform]

### requiresCompatibilities
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]]

### cpu
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### inferenceAccelerators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.InferenceAccelerator]]

### pidMode
- **Type**: typing.Optional[typing.Literal['host', 'task']]

### ipcMode
- **Type**: typing.Optional[typing.Literal['host', 'none', 'task']]

### proxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ProxyConfigurationOutput]

### registeredAt
- **Type**: typing.Optional[datetime.datetime]

### deregisteredAt
- **Type**: typing.Optional[datetime.datetime]

### registeredBy
- **Type**: typing.Optional[str]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorage]

### enableFaultInjection
- **Type**: typing.Optional[bool]


# TaskDefinitionPlacementConstraint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskEphemeralStorage

### sizeInGiB
- **Type**: typing.Optional[int]

### kmsKeyId
- **Type**: typing.Optional[str]


# TaskManagedEBSVolumeConfiguration

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### encrypted
- **Type**: typing.Optional[bool]

### kmsKeyId
- **Type**: typing.Optional[str]

### volumeType
- **Type**: typing.Optional[str]

### sizeInGiB
- **Type**: typing.Optional[int]

### snapshotId
- **Type**: typing.Optional[str]

### iops
- **Type**: typing.Optional[int]

### throughput
- **Type**: typing.Optional[int]

### tagSpecifications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EBSTagSpecificationUnion]]

### terminationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskManagedEBSVolumeTerminationPolicy]

### filesystemType
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'ntfs', 'xfs']]


# TaskManagedEBSVolumeTerminationPolicy

### deleteOnTermination
- **Type**: <class 'bool'>
- **Required**: Yes


# TaskOverride

### containerOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerOverride]]

### cpu
- **Type**: typing.Optional[str]

### inferenceAcceleratorOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.InferenceAcceleratorOverride]]

### executionRoleArn
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### taskRoleArn
- **Type**: typing.Optional[str]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorage]


# TaskOverrideOutput

### containerOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerOverrideOutput]]

### cpu
- **Type**: typing.Optional[str]

### inferenceAcceleratorOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.InferenceAcceleratorOverride]]

### executionRoleArn
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### taskRoleArn
- **Type**: typing.Optional[str]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorage]


# TaskOverrideUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskSet

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskVolumeConfiguration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### managedEBSVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskManagedEBSVolumeConfiguration]


# TimeoutConfiguration

### idleTimeoutSeconds
- **Type**: typing.Optional[int]

### perRequestTimeoutSeconds
- **Type**: typing.Optional[int]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Tmpfs

### containerPath
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: <class 'int'>
- **Required**: Yes

### mountOptions
- **Type**: typing.Optional[typing.Sequence[str]]


# TmpfsOutput

### containerPath
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: <class 'int'>
- **Required**: Yes

### mountOptions
- **Type**: typing.Optional[typing.List[str]]


# TmpfsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Ulimit

### name
- **Type**: typing.Literal['core', 'cpu', 'data', 'fsize', 'locks', 'memlock', 'msgqueue', 'nice', 'nofile', 'nproc', 'rss', 'rtprio', 'rttime', 'sigpending', 'stack']
- **Required**: Yes

### softLimit
- **Type**: <class 'int'>
- **Required**: Yes

### hardLimit
- **Type**: <class 'int'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCapacityProviderRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### autoScalingGroupProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.AutoScalingGroupProviderUpdate'>
- **Required**: Yes


# UpdateCapacityProviderResponse

### capacityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.CapacityProvider'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### settings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ClusterSetting]]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterConfiguration]

### serviceConnectDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterServiceConnectDefaultsRequest]


# UpdateClusterResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateClusterSettingsRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### settings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ClusterSetting]
- **Required**: Yes


# UpdateClusterSettingsResponse

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContainerAgentRequest

### containerInstance
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# UpdateContainerAgentResponse

### containerInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ContainerInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContainerInstancesStateRequest

### containerInstances
- **Type**: typing.Sequence[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DEREGISTERING', 'DRAINING', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# UpdateContainerInstancesStateResponse

### containerInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerInstance]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServicePrimaryTaskSetRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### service
- **Type**: <class 'str'>
- **Required**: Yes

### primaryTaskSet
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServicePrimaryTaskSetResponse

### taskSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceRequest

### service
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### desiredCount
- **Type**: typing.Optional[int]

### taskDefinition
- **Type**: typing.Optional[str]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItem]]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationUnion]

### availabilityZoneRebalancing
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnion]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraint]]

### placementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategy]]

### platformVersion
- **Type**: typing.Optional[str]

### forceNewDeployment
- **Type**: typing.Optional[bool]

### healthCheckGracePeriodSeconds
- **Type**: typing.Optional[int]

### enableExecuteCommand
- **Type**: typing.Optional[bool]

### enableECSManagedTags
- **Type**: typing.Optional[bool]

### loadBalancers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancer]]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### serviceRegistries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistry]]

### serviceConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationUnion]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationUnion]]

### vpcLatticeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.VpcLatticeConfiguration]]


# UpdateServiceResponse

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Service'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTaskProtectionRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### protectionEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### expiresInMinutes
- **Type**: typing.Optional[int]


# UpdateTaskProtectionResponse

### protectedTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ProtectedTask]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.Failure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTaskSetRequest

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### service
- **Type**: <class 'str'>
- **Required**: Yes

### taskSet
- **Type**: <class 'str'>
- **Required**: Yes

### scale
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.Scale'>
- **Required**: Yes


# UpdateTaskSetResponse

### taskSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadata'>
- **Required**: Yes


# VersionInfo

### agentVersion
- **Type**: typing.Optional[str]

### agentHash
- **Type**: typing.Optional[str]

### dockerVersion
- **Type**: typing.Optional[str]


# Volume

### name
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HostVolumeProperties]

### dockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DockerVolumeConfigurationUnion]

### efsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EFSVolumeConfiguration]

### fsxWindowsFileServerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FSxWindowsFileServerVolumeConfiguration]

### configuredAtLaunch
- **Type**: typing.Optional[bool]


# VolumeFrom

### sourceContainer
- **Type**: typing.Optional[str]

### readOnly
- **Type**: typing.Optional[bool]


# VolumeOutput

### name
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HostVolumeProperties]

### dockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DockerVolumeConfigurationOutput]

### efsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EFSVolumeConfiguration]

### fsxWindowsFileServerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FSxWindowsFileServerVolumeConfiguration]

### configuredAtLaunch
- **Type**: typing.Optional[bool]


# VolumeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcLatticeConfiguration

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### portName
- **Type**: <class 'str'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



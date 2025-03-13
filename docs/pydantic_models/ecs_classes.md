# Ecs Classes

# AttachmentStateChangeTypeDef

### attachmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes


# AttachmentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttributeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]

### targetType
- **Type**: typing.Optional[typing.Literal['container-instance']]

### targetId
- **Type**: typing.Optional[str]


# AutoScalingGroupProviderTypeDef

### autoScalingGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### managedScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ManagedScalingTypeDef]

### managedTerminationProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### managedDraining
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AutoScalingGroupProviderUpdateTypeDef

### managedScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ManagedScalingTypeDef]

### managedTerminationProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### managedDraining
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationOutputTypeDef

### subnets
- **Type**: typing.List[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.List[str]]

### assignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationTypeDef

### subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### securityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### assignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityProviderStrategyItemTypeDef

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### base
- **Type**: typing.Optional[int]


# CapacityProviderTypeDef

### capacityProviderArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### autoScalingGroupProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.AutoScalingGroupProviderTypeDef]

### updateStatus
- **Type**: typing.Optional[typing.Literal['DELETE_COMPLETE', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### updateStatusReason
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]


# ClusterConfigurationTypeDef

### executeCommandConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ExecuteCommandConfigurationTypeDef]

### managedStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ManagedStorageConfigurationTypeDef]


# ClusterServiceConnectDefaultsRequestTypeDef

### namespace
- **Type**: <class 'str'>
- **Required**: Yes


# ClusterServiceConnectDefaultsTypeDef

### namespace
- **Type**: typing.Optional[str]


# ClusterSettingTypeDef

### name
- **Type**: typing.Optional[typing.Literal['containerInsights']]

### value
- **Type**: typing.Optional[str]


# ClusterTypeDef

### clusterArn
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterConfigurationTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePairTypeDef]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### settings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ClusterSettingTypeDef]]

### capacityProviders
- **Type**: typing.Optional[typing.List[str]]

### defaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttachmentTypeDef]]

### attachmentsStatus
- **Type**: typing.Optional[str]

### serviceConnectDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterServiceConnectDefaultsTypeDef]


# ContainerDefinitionOutputTypeDef

### name
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RepositoryCredentialsTypeDef]

### cpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]

### links
- **Type**: typing.Optional[typing.List[str]]

### portMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.PortMappingTypeDef]]

### essential
- **Type**: typing.Optional[bool]

### restartPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ContainerRestartPolicyOutputTypeDef]

### entryPoint
- **Type**: typing.Optional[typing.List[str]]

### command
- **Type**: typing.Optional[typing.List[str]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePairTypeDef]]

### environmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.EnvironmentFileTypeDef]]

### mountPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.MountPointTypeDef]]

### volumesFrom
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.VolumeFromTypeDef]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LinuxParametersOutputTypeDef]

### secrets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.SecretTypeDef]]

### dependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerDependencyTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.HostEntryTypeDef]]

### dockerSecurityOptions
- **Type**: typing.Optional[typing.List[str]]

### interactive
- **Type**: typing.Optional[bool]

### pseudoTerminal
- **Type**: typing.Optional[bool]

### dockerLabels
- **Type**: typing.Optional[typing.Dict[str, str]]

### ulimits
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.UlimitTypeDef]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfigurationOutputTypeDef]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HealthCheckOutputTypeDef]

### systemControls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.SystemControlTypeDef]]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirementTypeDef]]

### firelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FirelensConfigurationOutputTypeDef]

### credentialSpecs
- **Type**: typing.Optional[typing.List[str]]


# ContainerDefinitionTypeDef

### name
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]

### repositoryCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RepositoryCredentialsTypeDef]

### cpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]

### links
- **Type**: typing.Optional[typing.Sequence[str]]

### portMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PortMappingTypeDef]]

### essential
- **Type**: typing.Optional[bool]

### restartPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ContainerRestartPolicyUnionTypeDef]

### entryPoint
- **Type**: typing.Optional[typing.Sequence[str]]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePairTypeDef]]

### environmentFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EnvironmentFileTypeDef]]

### mountPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.MountPointTypeDef]]

### volumesFrom
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.VolumeFromTypeDef]]

### linuxParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LinuxParametersUnionTypeDef]

### secrets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.SecretTypeDef]]

### dependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerDependencyTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.HostEntryTypeDef]]

### dockerSecurityOptions
- **Type**: typing.Optional[typing.Sequence[str]]

### interactive
- **Type**: typing.Optional[bool]

### pseudoTerminal
- **Type**: typing.Optional[bool]

### dockerLabels
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ulimits
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.UlimitTypeDef]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfigurationUnionTypeDef]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HealthCheckUnionTypeDef]

### systemControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.SystemControlTypeDef]]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirementTypeDef]]

### firelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FirelensConfigurationUnionTypeDef]

### credentialSpecs
- **Type**: typing.Optional[typing.Sequence[str]]


# ContainerDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerDependencyTypeDef

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Literal['COMPLETE', 'HEALTHY', 'START', 'SUCCESS']
- **Required**: Yes


# ContainerImageTypeDef

### containerName
- **Type**: typing.Optional[str]

### imageDigest
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[str]


# ContainerInstanceHealthStatusTypeDef

### overallStatus
- **Type**: typing.Optional[typing.Literal['IMPAIRED', 'INITIALIZING', 'INSUFFICIENT_DATA', 'OK']]

### details
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.InstanceHealthCheckResultTypeDef]]


# ContainerInstanceTypeDef

### containerInstanceArn
- **Type**: typing.Optional[str]

### ec2InstanceId
- **Type**: typing.Optional[str]

### capacityProviderName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[int]

### versionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.VersionInfoTypeDef]

### remainingResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ResourceOutputTypeDef]]

### registeredResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ResourceOutputTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]]

### registeredAt
- **Type**: typing.Optional[datetime.datetime]

### attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttachmentTypeDef]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### healthStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ContainerInstanceHealthStatusTypeDef]


# ContainerOverrideOutputTypeDef

### name
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.List[str]]

### environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePairTypeDef]]

### environmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.EnvironmentFileTypeDef]]

### cpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]

### resourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirementTypeDef]]


# ContainerOverrideTypeDef

### name
- **Type**: typing.Optional[str]

### command
- **Type**: typing.Optional[typing.Sequence[str]]

### environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePairTypeDef]]

### environmentFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EnvironmentFileTypeDef]]

### cpu
- **Type**: typing.Optional[int]

### memory
- **Type**: typing.Optional[int]

### memoryReservation
- **Type**: typing.Optional[int]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirementTypeDef]]


# ContainerRestartPolicyOutputTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ignoredExitCodes
- **Type**: typing.Optional[typing.List[int]]

### restartAttemptPeriod
- **Type**: typing.Optional[int]


# ContainerRestartPolicyTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ignoredExitCodes
- **Type**: typing.Optional[typing.Sequence[int]]

### restartAttemptPeriod
- **Type**: typing.Optional[int]


# ContainerRestartPolicyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContainerStateChangeTypeDef

### containerName
- **Type**: typing.Optional[str]

### imageDigest
- **Type**: typing.Optional[str]

### runtimeId
- **Type**: typing.Optional[str]

### exitCode
- **Type**: typing.Optional[int]

### networkBindings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.NetworkBindingTypeDef]]

### reason
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]


# ContainerTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.NetworkBindingTypeDef]]

### networkInterfaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.NetworkInterfaceTypeDef]]

### healthStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY', 'UNKNOWN']]

### managedAgents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ManagedAgentTypeDef]]

### cpu
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### memoryReservation
- **Type**: typing.Optional[str]

### gpuIds
- **Type**: typing.Optional[typing.List[str]]


# CreateCapacityProviderRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### autoScalingGroupProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.AutoScalingGroupProviderTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]


# CreateCapacityProviderResponseTypeDef

### capacityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClusterRequestTypeDef

### clusterName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### settings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ClusterSettingTypeDef]]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterConfigurationTypeDef]

### capacityProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### defaultCapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### serviceConnectDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterServiceConnectDefaultsRequestTypeDef]


# CreateClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancerTypeDef]]

### serviceRegistries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistryTypeDef]]

### desiredCount
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### platformVersion
- **Type**: typing.Optional[str]

### role
- **Type**: typing.Optional[str]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationUnionTypeDef]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraintTypeDef]]

### placementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategyTypeDef]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnionTypeDef]

### healthCheckGracePeriodSeconds
- **Type**: typing.Optional[int]

### schedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### deploymentController
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentControllerTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### enableECSManagedTags
- **Type**: typing.Optional[bool]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### enableExecuteCommand
- **Type**: typing.Optional[bool]

### serviceConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationUnionTypeDef]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationUnionTypeDef]]

### vpcLatticeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.VpcLatticeConfigurationTypeDef]]


# CreateServiceResponseTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTaskSetRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnionTypeDef]

### loadBalancers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancerTypeDef]]

### serviceRegistries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistryTypeDef]]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### platformVersion
- **Type**: typing.Optional[str]

### scale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ScaleTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]


# CreateTaskSetResponseTypeDef

### taskSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatedAtTypeDef

### before
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimestampTypeDef]

### after
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimestampTypeDef]


# DeleteAccountSettingRequestTypeDef

### name
- **Type**: typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']
- **Required**: Yes

### principalArn
- **Type**: typing.Optional[str]


# DeleteAccountSettingResponseTypeDef

### setting
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.SettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAttributesRequestTypeDef

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# DeleteAttributesResponseTypeDef

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCapacityProviderRequestTypeDef

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCapacityProviderResponseTypeDef

### capacityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterRequestTypeDef

### cluster
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceRequestTypeDef

### service
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# DeleteServiceResponseTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTaskDefinitionsRequestTypeDef

### taskDefinitions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteTaskDefinitionsResponseTypeDef

### taskDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskDefinitionTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTaskSetRequestTypeDef

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


# DeleteTaskSetResponseTypeDef

### taskSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeploymentAlarmsOutputTypeDef

### alarmNames
- **Type**: typing.List[str]
- **Required**: Yes

### rollback
- **Type**: <class 'bool'>
- **Required**: Yes

### enable
- **Type**: <class 'bool'>
- **Required**: Yes


# DeploymentAlarmsTypeDef

### alarmNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### rollback
- **Type**: <class 'bool'>
- **Required**: Yes

### enable
- **Type**: <class 'bool'>
- **Required**: Yes


# DeploymentCircuitBreakerTypeDef

### enable
- **Type**: <class 'bool'>
- **Required**: Yes

### rollback
- **Type**: <class 'bool'>
- **Required**: Yes


# DeploymentConfigurationOutputTypeDef

### deploymentCircuitBreaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentCircuitBreakerTypeDef]

### maximumPercent
- **Type**: typing.Optional[int]

### minimumHealthyPercent
- **Type**: typing.Optional[int]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentAlarmsOutputTypeDef]


# DeploymentConfigurationTypeDef

### deploymentCircuitBreaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentCircuitBreakerTypeDef]

### maximumPercent
- **Type**: typing.Optional[int]

### minimumHealthyPercent
- **Type**: typing.Optional[int]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentAlarmsTypeDef]


# DeploymentConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentControllerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentEphemeralStorageTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]


# DeploymentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeregisterContainerInstanceRequestTypeDef

### containerInstance
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# DeregisterContainerInstanceResponseTypeDef

### containerInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ContainerInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterTaskDefinitionRequestTypeDef

### taskDefinition
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTaskDefinitionResponseTypeDef

### taskDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCapacityProvidersRequestTypeDef

### capacityProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeCapacityProvidersResponseTypeDef

### capacityProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeClustersRequestTypeDef

### clusters
- **Type**: typing.Optional[typing.Sequence[str]]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ATTACHMENTS', 'CONFIGURATIONS', 'SETTINGS', 'STATISTICS', 'TAGS']]]


# DescribeClustersResponseTypeDef

### clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ClusterTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeContainerInstancesRequestTypeDef

### containerInstances
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTAINER_INSTANCE_HEALTH', 'TAGS']]]


# DescribeContainerInstancesResponseTypeDef

### containerInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerInstanceTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceDeploymentsRequestTypeDef

### serviceDeploymentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeServiceDeploymentsResponseTypeDef

### serviceDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceDeploymentTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceRevisionsRequestTypeDef

### serviceRevisionArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeServiceRevisionsResponseTypeDef

### serviceRevisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRevisionTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServicesRequestTypeDef

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeServicesRequestWaitExtraTypeDef

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.WaiterConfigTypeDef]


# DescribeServicesRequestWaitTypeDef

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.WaiterConfigTypeDef]


# DescribeServicesResponseTypeDef

### services
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTaskDefinitionRequestTypeDef

### taskDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeTaskDefinitionResponseTypeDef

### taskDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskDefinitionTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTaskSetsRequestTypeDef

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


# DescribeTaskSetsResponseTypeDef

### taskSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskSetTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTasksRequestTypeDef

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeTasksRequestWaitExtraTypeDef

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.WaiterConfigTypeDef]


# DescribeTasksRequestWaitTypeDef

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.WaiterConfigTypeDef]


# DescribeTasksResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceOutputTypeDef

### hostPath
- **Type**: <class 'str'>
- **Required**: Yes

### containerPath
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.List[typing.Literal['mknod', 'read', 'write']]]


# DeviceTypeDef

### hostPath
- **Type**: <class 'str'>
- **Required**: Yes

### containerPath
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['mknod', 'read', 'write']]]


# DeviceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DiscoverPollEndpointRequestTypeDef

### containerInstance
- **Type**: typing.Optional[str]

### cluster
- **Type**: typing.Optional[str]


# DiscoverPollEndpointResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DockerVolumeConfigurationOutputTypeDef

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


# DockerVolumeConfigurationTypeDef

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


# DockerVolumeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EBSTagSpecificationOutputTypeDef

### resourceType
- **Type**: typing.Literal['volume']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]


# EBSTagSpecificationTypeDef

### resourceType
- **Type**: typing.Literal['volume']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]


# EBSTagSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EFSAuthorizationConfigTypeDef]


# EnvironmentFileTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EphemeralStorageTypeDef

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# ExecuteCommandConfigurationTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]

### logging
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'NONE', 'OVERRIDE']]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ExecuteCommandLogConfigurationTypeDef]


# ExecuteCommandLogConfigurationTypeDef

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


# ExecuteCommandRequestTypeDef

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


# ExecuteCommandResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.SessionTypeDef'>
- **Required**: Yes

### taskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FSxWindowsFileServerAuthorizationConfigTypeDef

### credentialsParameter
- **Type**: <class 'str'>
- **Required**: Yes

### domain
- **Type**: <class 'str'>
- **Required**: Yes


# FSxWindowsFileServerVolumeConfigurationTypeDef

### fileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### rootDirectory
- **Type**: <class 'str'>
- **Required**: Yes

### authorizationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.FSxWindowsFileServerAuthorizationConfigTypeDef'>
- **Required**: Yes


# FailureTypeDef

### arn
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### detail
- **Type**: typing.Optional[str]


# FirelensConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FirelensConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetTaskProtectionRequestTypeDef

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### tasks
- **Type**: typing.Optional[typing.Sequence[str]]


# GetTaskProtectionResponseTypeDef

### protectedTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ProtectedTaskTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HealthCheckOutputTypeDef

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


# HealthCheckTypeDef

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


# HealthCheckUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HostEntryTypeDef

### hostname
- **Type**: <class 'str'>
- **Required**: Yes

### ipAddress
- **Type**: <class 'str'>
- **Required**: Yes


# HostVolumePropertiesTypeDef

### sourcePath
- **Type**: typing.Optional[str]


# InferenceAcceleratorOverrideTypeDef

### deviceName
- **Type**: typing.Optional[str]

### deviceType
- **Type**: typing.Optional[str]


# InferenceAcceleratorTypeDef

### deviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deviceType
- **Type**: <class 'str'>
- **Required**: Yes


# InstanceHealthCheckResultTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KernelCapabilitiesOutputTypeDef

### add
- **Type**: typing.Optional[typing.List[str]]

### drop
- **Type**: typing.Optional[typing.List[str]]


# KernelCapabilitiesTypeDef

### add
- **Type**: typing.Optional[typing.Sequence[str]]

### drop
- **Type**: typing.Optional[typing.Sequence[str]]


# KernelCapabilitiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeyValuePairTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# LinuxParametersOutputTypeDef

### capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.KernelCapabilitiesOutputTypeDef]

### devices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.DeviceOutputTypeDef]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TmpfsOutputTypeDef]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# LinuxParametersTypeDef

### capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.KernelCapabilitiesUnionTypeDef]

### devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.DeviceUnionTypeDef]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TmpfsUnionTypeDef]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# LinuxParametersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAccountSettingsRequestPaginateTypeDef

### name
- **Type**: typing.Optional[typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']]

### value
- **Type**: typing.Optional[str]

### principalArn
- **Type**: typing.Optional[str]

### effectiveSettings
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListAccountSettingsRequestTypeDef

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


# ListAccountSettingsResponseTypeDef

### settings
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.SettingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAttributesRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListAttributesRequestTypeDef

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


# ListAttributesResponseTypeDef

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListClustersRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListClustersResponseTypeDef

### clusterArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContainerInstancesResponseTypeDef

### containerInstanceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServiceDeploymentsRequestTypeDef

### service
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Sequence[typing.Literal['IN_PROGRESS', 'PENDING', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCESSFUL', 'STOPPED', 'STOP_REQUESTED', 'SUCCESSFUL']]]

### createdAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.CreatedAtTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListServiceDeploymentsResponseTypeDef

### serviceDeployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceDeploymentBriefTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicesByNamespaceRequestPaginateTypeDef

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListServicesByNamespaceRequestTypeDef

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListServicesByNamespaceResponseTypeDef

### serviceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListServicesRequestPaginateTypeDef

### cluster
- **Type**: typing.Optional[str]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### schedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListServicesRequestTypeDef

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


# ListServicesResponseTypeDef

### serviceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTaskDefinitionFamiliesRequestPaginateTypeDef

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ALL', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListTaskDefinitionFamiliesRequestTypeDef

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ALL', 'INACTIVE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTaskDefinitionFamiliesResponseTypeDef

### families
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTaskDefinitionsRequestPaginateTypeDef

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETE_IN_PROGRESS', 'INACTIVE']]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListTaskDefinitionsRequestTypeDef

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


# ListTaskDefinitionsResponseTypeDef

### taskDefinitionArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTasksRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListTasksRequestTypeDef

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


# ListTasksResponseTypeDef

### taskArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# LoadBalancerTypeDef

### targetGroupArn
- **Type**: typing.Optional[str]

### loadBalancerName
- **Type**: typing.Optional[str]

### containerName
- **Type**: typing.Optional[str]

### containerPort
- **Type**: typing.Optional[int]


# LogConfigurationOutputTypeDef

### logDriver
- **Type**: typing.Literal['awsfirelens', 'awslogs', 'fluentd', 'gelf', 'journald', 'json-file', 'splunk', 'syslog']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Dict[str, str]]

### secretOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.SecretTypeDef]]


# LogConfigurationTypeDef

### logDriver
- **Type**: typing.Literal['awsfirelens', 'awslogs', 'fluentd', 'gelf', 'journald', 'json-file', 'splunk', 'syslog']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Mapping[str, str]]

### secretOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.SecretTypeDef]]


# LogConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ManagedAgentStateChangeTypeDef

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


# ManagedAgentTypeDef

### lastStartedAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[typing.Literal['ExecuteCommandAgent']]

### reason
- **Type**: typing.Optional[str]

### lastStatus
- **Type**: typing.Optional[str]


# ManagedScalingTypeDef

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


# ManagedStorageConfigurationTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]

### fargateEphemeralStorageKmsKeyId
- **Type**: typing.Optional[str]


# MountPointTypeDef

### sourceVolume
- **Type**: typing.Optional[str]

### containerPath
- **Type**: typing.Optional[str]

### readOnly
- **Type**: typing.Optional[bool]


# NetworkBindingTypeDef

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


# NetworkConfigurationOutputTypeDef

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.AwsVpcConfigurationOutputTypeDef]


# NetworkConfigurationTypeDef

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.AwsVpcConfigurationTypeDef]


# NetworkConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkInterfaceTypeDef

### attachmentId
- **Type**: typing.Optional[str]

### privateIpv4Address
- **Type**: typing.Optional[str]

### ipv6Address
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacementConstraintTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PlacementStrategyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PlatformDeviceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PortMappingTypeDef

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


# ProtectedTaskTypeDef

### taskArn
- **Type**: typing.Optional[str]

### protectionEnabled
- **Type**: typing.Optional[bool]

### expirationDate
- **Type**: typing.Optional[datetime.datetime]


# ProxyConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProxyConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutAccountSettingDefaultRequestTypeDef

### name
- **Type**: typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PutAccountSettingDefaultResponseTypeDef

### setting
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.SettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutAccountSettingRequestTypeDef

### name
- **Type**: typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### principalArn
- **Type**: typing.Optional[str]


# PutAccountSettingResponseTypeDef

### setting
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.SettingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutAttributesRequestTypeDef

### attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# PutAttributesResponseTypeDef

### attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutClusterCapacityProvidersRequestTypeDef

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### capacityProviders
- **Type**: typing.Sequence[str]
- **Required**: Yes

### defaultCapacityProviderStrategy
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]
- **Required**: Yes


# PutClusterCapacityProvidersResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterContainerInstanceRequestTypeDef

### cluster
- **Type**: typing.Optional[str]

### instanceIdentityDocument
- **Type**: typing.Optional[str]

### instanceIdentityDocumentSignature
- **Type**: typing.Optional[str]

### totalResources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ResourceUnionTypeDef]]

### versionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.VersionInfoTypeDef]

### containerInstanceArn
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]]

### platformDevices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlatformDeviceTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]


# RegisterContainerInstanceResponseTypeDef

### containerInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ContainerInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterTaskDefinitionRequestTypeDef

### family
- **Type**: <class 'str'>
- **Required**: Yes

### containerDefinitions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerDefinitionUnionTypeDef]
- **Required**: Yes

### taskRoleArn
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### networkMode
- **Type**: typing.Optional[typing.Literal['awsvpc', 'bridge', 'host', 'none']]

### volumes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.VolumeUnionTypeDef]]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TaskDefinitionPlacementConstraintTypeDef]]

### requiresCompatibilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]]

### cpu
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### pidMode
- **Type**: typing.Optional[typing.Literal['host', 'task']]

### ipcMode
- **Type**: typing.Optional[typing.Literal['host', 'none', 'task']]

### proxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ProxyConfigurationUnionTypeDef]

### inferenceAccelerators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.InferenceAcceleratorTypeDef]]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorageTypeDef]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RuntimePlatformTypeDef]

### enableFaultInjection
- **Type**: typing.Optional[bool]


# RegisterTaskDefinitionResponseTypeDef

### taskDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskDefinitionTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RepositoryCredentialsTypeDef

### credentialsParameter
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceRequirementTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceUnionTypeDef

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


# RollbackTypeDef

### reason
- **Type**: typing.Optional[str]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### serviceRevisionArn
- **Type**: typing.Optional[str]


# RunTaskRequestTypeDef

### taskDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### capacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnionTypeDef]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskOverrideUnionTypeDef]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraintTypeDef]]

### placementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategyTypeDef]]

### platformVersion
- **Type**: typing.Optional[str]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### referenceId
- **Type**: typing.Optional[str]

### startedBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TaskVolumeConfigurationTypeDef]]


# RunTaskResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RuntimePlatformTypeDef

### cpuArchitecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]

### operatingSystemFamily
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS_SERVER_2004_CORE', 'WINDOWS_SERVER_2016_FULL', 'WINDOWS_SERVER_2019_CORE', 'WINDOWS_SERVER_2019_FULL', 'WINDOWS_SERVER_2022_CORE', 'WINDOWS_SERVER_2022_FULL', 'WINDOWS_SERVER_20H2_CORE']]


# ScaleTypeDef

### value
- **Type**: typing.Optional[float]

### unit
- **Type**: typing.Optional[typing.Literal['PERCENT']]


# SecretTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### valueFrom
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceConnectClientAliasTypeDef

### port
- **Type**: <class 'int'>
- **Required**: Yes

### dnsName
- **Type**: typing.Optional[str]


# ServiceConnectConfigurationOutputTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectServiceOutputTypeDef]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfigurationOutputTypeDef]


# ServiceConnectConfigurationTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]

### services
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectServiceTypeDef]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfigurationTypeDef]


# ServiceConnectConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceConnectServiceOutputTypeDef

### portName
- **Type**: <class 'str'>
- **Required**: Yes

### discoveryName
- **Type**: typing.Optional[str]

### clientAliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectClientAliasTypeDef]]

### ingressPortOverride
- **Type**: typing.Optional[int]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimeoutConfigurationTypeDef]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectTlsConfigurationTypeDef]


# ServiceConnectServiceResourceTypeDef

### discoveryName
- **Type**: typing.Optional[str]

### discoveryArn
- **Type**: typing.Optional[str]


# ServiceConnectServiceTypeDef

### portName
- **Type**: <class 'str'>
- **Required**: Yes

### discoveryName
- **Type**: typing.Optional[str]

### clientAliases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectClientAliasTypeDef]]

### ingressPortOverride
- **Type**: typing.Optional[int]

### timeout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimeoutConfigurationTypeDef]

### tls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectTlsConfigurationTypeDef]


# ServiceConnectTlsCertificateAuthorityTypeDef

### awsPcaAuthorityArn
- **Type**: typing.Optional[str]


# ServiceConnectTlsConfigurationTypeDef

### issuerCertificateAuthority
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectTlsCertificateAuthorityTypeDef'>
- **Required**: Yes

### kmsKey
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# ServiceDeploymentAlarmsTypeDef

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'MONITORING', 'MONITORING_COMPLETE', 'TRIGGERED']]

### alarmNames
- **Type**: typing.Optional[typing.List[str]]

### triggeredAlarmNames
- **Type**: typing.Optional[typing.List[str]]


# ServiceDeploymentBriefTypeDef

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


# ServiceDeploymentCircuitBreakerTypeDef

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'MONITORING', 'MONITORING_COMPLETE', 'TRIGGERED']]

### failureCount
- **Type**: typing.Optional[int]

### threshold
- **Type**: typing.Optional[int]


# ServiceDeploymentTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRevisionSummaryTypeDef]]

### targetServiceRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceRevisionSummaryTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['IN_PROGRESS', 'PENDING', 'ROLLBACK_FAILED', 'ROLLBACK_IN_PROGRESS', 'ROLLBACK_SUCCESSFUL', 'STOPPED', 'STOP_REQUESTED', 'SUCCESSFUL']]

### statusReason
- **Type**: typing.Optional[str]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationOutputTypeDef]

### rollback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RollbackTypeDef]

### deploymentCircuitBreaker
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceDeploymentCircuitBreakerTypeDef]

### alarms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceDeploymentAlarmsTypeDef]


# ServiceEventTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceManagedEBSVolumeConfigurationOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.EBSTagSpecificationOutputTypeDef]]

### filesystemType
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'ntfs', 'xfs']]


# ServiceManagedEBSVolumeConfigurationTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EBSTagSpecificationUnionTypeDef]]

### filesystemType
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'ntfs', 'xfs']]


# ServiceManagedEBSVolumeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceRegistryTypeDef

### registryArn
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### containerName
- **Type**: typing.Optional[str]

### containerPort
- **Type**: typing.Optional[int]


# ServiceRevisionSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### requestedTaskCount
- **Type**: typing.Optional[int]

### runningTaskCount
- **Type**: typing.Optional[int]

### pendingTaskCount
- **Type**: typing.Optional[int]


# ServiceRevisionTypeDef

### serviceRevisionArn
- **Type**: typing.Optional[str]

### serviceArn
- **Type**: typing.Optional[str]

### clusterArn
- **Type**: typing.Optional[str]

### taskDefinition
- **Type**: typing.Optional[str]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### platformVersion
- **Type**: typing.Optional[str]

### platformFamily
- **Type**: typing.Optional[str]

### loadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancerTypeDef]]

### serviceRegistries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistryTypeDef]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationOutputTypeDef]

### containerImages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerImageTypeDef]]

### guardDutyEnabled
- **Type**: typing.Optional[bool]

### serviceConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationOutputTypeDef]

### volumeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationOutputTypeDef]]

### fargateEphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentEphemeralStorageTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### vpcLatticeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.VpcLatticeConfigurationTypeDef]]


# ServiceTypeDef

### serviceArn
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### clusterArn
- **Type**: typing.Optional[str]

### loadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancerTypeDef]]

### serviceRegistries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistryTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### platformVersion
- **Type**: typing.Optional[str]

### platformFamily
- **Type**: typing.Optional[str]

### taskDefinition
- **Type**: typing.Optional[str]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationOutputTypeDef]

### taskSets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskSetTypeDef]]

### deployments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.DeploymentTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### events
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceEventTypeDef]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### placementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraintTypeDef]]

### placementStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategyTypeDef]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationOutputTypeDef]

### healthCheckGracePeriodSeconds
- **Type**: typing.Optional[int]

### schedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### deploymentController
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentControllerTypeDef]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

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


# ServiceVolumeConfigurationOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### managedEBSVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceManagedEBSVolumeConfigurationOutputTypeDef]


# ServiceVolumeConfigurationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### managedEBSVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceManagedEBSVolumeConfigurationUnionTypeDef]


# ServiceVolumeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SessionTypeDef

### sessionId
- **Type**: typing.Optional[str]

### streamUrl
- **Type**: typing.Optional[str]

### tokenValue
- **Type**: typing.Optional[str]


# SettingTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartTaskRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnionTypeDef]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskOverrideUnionTypeDef]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### referenceId
- **Type**: typing.Optional[str]

### startedBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TaskVolumeConfigurationTypeDef]]


# StartTaskResponseTypeDef

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopTaskRequestTypeDef

### task
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# StopTaskResponseTypeDef

### task
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubmitAttachmentStateChangesRequestTypeDef

### attachments
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.AttachmentStateChangeTypeDef]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# SubmitAttachmentStateChangesResponseTypeDef

### acknowledgment
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubmitContainerStateChangeRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.NetworkBindingTypeDef]]


# SubmitContainerStateChangeResponseTypeDef

### acknowledgment
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SubmitTaskStateChangeRequestTypeDef

### cluster
- **Type**: typing.Optional[str]

### task
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### containers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerStateChangeTypeDef]]

### attachments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.AttachmentStateChangeTypeDef]]

### managedAgents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ManagedAgentStateChangeTypeDef]]

### pullStartedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimestampTypeDef]

### pullStoppedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimestampTypeDef]

### executionStoppedAt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TimestampTypeDef]


# SubmitTaskStateChangeResponseTypeDef

### acknowledgment
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SystemControlTypeDef

### namespace
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TaskDefinitionPlacementConstraintTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskDefinitionTypeDef

### taskDefinitionArn
- **Type**: typing.Optional[str]

### containerDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerDefinitionOutputTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.VolumeOutputTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETE_IN_PROGRESS', 'INACTIVE']]

### requiresAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]]

### placementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TaskDefinitionPlacementConstraintTypeDef]]

### compatibilities
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RuntimePlatformTypeDef]

### requiresCompatibilities
- **Type**: typing.Optional[typing.List[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]]

### cpu
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### inferenceAccelerators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.InferenceAcceleratorTypeDef]]

### pidMode
- **Type**: typing.Optional[typing.Literal['host', 'task']]

### ipcMode
- **Type**: typing.Optional[typing.Literal['host', 'none', 'task']]

### proxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ProxyConfigurationOutputTypeDef]

### registeredAt
- **Type**: typing.Optional[datetime.datetime]

### deregisteredAt
- **Type**: typing.Optional[datetime.datetime]

### registeredBy
- **Type**: typing.Optional[str]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorageTypeDef]

### enableFaultInjection
- **Type**: typing.Optional[bool]


# TaskEphemeralStorageTypeDef

### sizeInGiB
- **Type**: typing.Optional[int]

### kmsKeyId
- **Type**: typing.Optional[str]


# TaskManagedEBSVolumeConfigurationTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EBSTagSpecificationUnionTypeDef]]

### terminationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskManagedEBSVolumeTerminationPolicyTypeDef]

### filesystemType
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'ntfs', 'xfs']]


# TaskManagedEBSVolumeTerminationPolicyTypeDef

### deleteOnTermination
- **Type**: <class 'bool'>
- **Required**: Yes


# TaskOverrideOutputTypeDef

### containerOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerOverrideOutputTypeDef]]

### cpu
- **Type**: typing.Optional[str]

### inferenceAcceleratorOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.InferenceAcceleratorOverrideTypeDef]]

### executionRoleArn
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### taskRoleArn
- **Type**: typing.Optional[str]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorageTypeDef]


# TaskOverrideTypeDef

### containerOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerOverrideTypeDef]]

### cpu
- **Type**: typing.Optional[str]

### inferenceAcceleratorOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.InferenceAcceleratorOverrideTypeDef]]

### executionRoleArn
- **Type**: typing.Optional[str]

### memory
- **Type**: typing.Optional[str]

### taskRoleArn
- **Type**: typing.Optional[str]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorageTypeDef]


# TaskOverrideUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskSetTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskTypeDef

### attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttachmentTypeDef]]

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.AttributeTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.InferenceAcceleratorTypeDef]]

### lastStatus
- **Type**: typing.Optional[str]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### memory
- **Type**: typing.Optional[str]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskOverrideOutputTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### taskArn
- **Type**: typing.Optional[str]

### taskDefinitionArn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[int]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorageTypeDef]

### fargateEphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskEphemeralStorageTypeDef]


# TaskVolumeConfigurationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### managedEBSVolume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskManagedEBSVolumeConfigurationTypeDef]


# TimeoutConfigurationTypeDef

### idleTimeoutSeconds
- **Type**: typing.Optional[int]

### perRequestTimeoutSeconds
- **Type**: typing.Optional[int]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# TmpfsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UlimitTypeDef

### name
- **Type**: typing.Literal['core', 'cpu', 'data', 'fsize', 'locks', 'memlock', 'msgqueue', 'nice', 'nofile', 'nproc', 'rss', 'rtprio', 'rttime', 'sigpending', 'stack']
- **Required**: Yes

### softLimit
- **Type**: <class 'int'>
- **Required**: Yes

### hardLimit
- **Type**: <class 'int'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCapacityProviderRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### autoScalingGroupProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.AutoScalingGroupProviderUpdateTypeDef'>
- **Required**: Yes


# UpdateCapacityProviderResponseTypeDef

### capacityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterRequestTypeDef

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### settings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ClusterSettingTypeDef]]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterConfigurationTypeDef]

### serviceConnectDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ClusterServiceConnectDefaultsRequestTypeDef]


# UpdateClusterResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateClusterSettingsRequestTypeDef

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### settings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ClusterSettingTypeDef]
- **Required**: Yes


# UpdateClusterSettingsResponseTypeDef

### cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateContainerAgentRequestTypeDef

### containerInstance
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# UpdateContainerAgentResponseTypeDef

### containerInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ContainerInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateContainerInstancesStateRequestTypeDef

### containerInstances
- **Type**: typing.Sequence[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DEREGISTERING', 'DRAINING', 'REGISTERING', 'REGISTRATION_FAILED']
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]


# UpdateContainerInstancesStateResponseTypeDef

### containerInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ContainerInstanceTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServicePrimaryTaskSetRequestTypeDef

### cluster
- **Type**: <class 'str'>
- **Required**: Yes

### service
- **Type**: <class 'str'>
- **Required**: Yes

### primaryTaskSet
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServicePrimaryTaskSetResponseTypeDef

### taskSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### deploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationUnionTypeDef]

### availabilityZoneRebalancing
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationUnionTypeDef]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraintTypeDef]]

### placementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategyTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancerTypeDef]]

### propagateTags
- **Type**: typing.Optional[typing.Literal['NONE', 'SERVICE', 'TASK_DEFINITION']]

### serviceRegistries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistryTypeDef]]

### serviceConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationUnionTypeDef]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationUnionTypeDef]]

### vpcLatticeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.VpcLatticeConfigurationTypeDef]]


# UpdateServiceResponseTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTaskProtectionRequestTypeDef

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


# UpdateTaskProtectionResponseTypeDef

### protectedTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.ProtectedTaskTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecs_classes.FailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTaskSetRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ScaleTypeDef'>
- **Required**: Yes


# UpdateTaskSetResponseTypeDef

### taskSet
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.TaskSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VersionInfoTypeDef

### agentVersion
- **Type**: typing.Optional[str]

### agentHash
- **Type**: typing.Optional[str]

### dockerVersion
- **Type**: typing.Optional[str]


# VolumeFromTypeDef

### sourceContainer
- **Type**: typing.Optional[str]

### readOnly
- **Type**: typing.Optional[bool]


# VolumeOutputTypeDef

### name
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HostVolumePropertiesTypeDef]

### dockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DockerVolumeConfigurationOutputTypeDef]

### efsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EFSVolumeConfigurationTypeDef]

### fsxWindowsFileServerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FSxWindowsFileServerVolumeConfigurationTypeDef]

### configuredAtLaunch
- **Type**: typing.Optional[bool]


# VolumeTypeDef

### name
- **Type**: typing.Optional[str]

### host
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HostVolumePropertiesTypeDef]

### dockerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DockerVolumeConfigurationUnionTypeDef]

### efsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EFSVolumeConfigurationTypeDef]

### fsxWindowsFileServerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FSxWindowsFileServerVolumeConfigurationTypeDef]

### configuredAtLaunch
- **Type**: typing.Optional[bool]


# VolumeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcLatticeConfigurationTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### targetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### portName
- **Type**: <class 'str'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



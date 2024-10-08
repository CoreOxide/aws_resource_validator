# Pydantic Models in ecs_classes

# AttachmentStateChangeTypeDef

### attachmentArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes


# AttachmentTypeDef

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePairTypeDef]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LinuxParametersTypeDef]

### secrets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.SecretTypeDef]]

### dependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ContainerDependencyTypeDef]]

### startTimeout
- **Type**: typing.Optional[int]

### stopTimeout
- **Type**: typing.Optional[int]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.LogConfigurationTypeDef]

### healthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.HealthCheckTypeDef]

### systemControls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.SystemControlTypeDef]]

### resourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.ResourceRequirementTypeDef]]

### firelensConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FirelensConfigurationTypeDef]

### credentialSpecs
- **Type**: typing.Optional[typing.Sequence[str]]


# ContainerDependencyTypeDef

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: typing.Literal['COMPLETE', 'HEALTHY', 'START', 'SUCCESS']
- **Required**: Yes


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


# CreateCapacityProviderRequestRequestTypeDef

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


# CreateClusterRequestRequestTypeDef

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


# CreateServiceRequestRequestTypeDef

### serviceName
- **Type**: <class 'str'>
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### taskDefinition
- **Type**: typing.Optional[str]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationTypeDef]

### placementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementConstraintTypeDef]]

### placementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.PlacementStrategyTypeDef]]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationTypeDef]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationTypeDef, aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationOutputTypeDef]]]


# CreateServiceResponseTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTaskSetRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationTypeDef]

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


# DeleteAccountSettingRequestRequestTypeDef

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


# DeleteAttributesRequestRequestTypeDef

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


# DeleteCapacityProviderRequestRequestTypeDef

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


# DeleteClusterRequestRequestTypeDef

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


# DeleteServiceRequestRequestTypeDef

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


# DeleteTaskDefinitionsRequestRequestTypeDef

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


# DeleteTaskSetRequestRequestTypeDef

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

### enable
- **Type**: <class 'bool'>
- **Required**: Yes

### rollback
- **Type**: <class 'bool'>
- **Required**: Yes


# DeploymentAlarmsTypeDef

### alarmNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### enable
- **Type**: <class 'bool'>
- **Required**: Yes

### rollback
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


# DeploymentControllerTypeDef

### type
- **Type**: typing.Literal['CODE_DEPLOY', 'ECS', 'EXTERNAL']
- **Required**: Yes


# DeploymentEphemeralStorageTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]


# DeploymentTypeDef

### id
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### taskDefinition
- **Type**: typing.Optional[str]

### desiredCount
- **Type**: typing.Optional[int]

### pendingCount
- **Type**: typing.Optional[int]

### runningCount
- **Type**: typing.Optional[int]

### failedTasks
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### platformVersion
- **Type**: typing.Optional[str]

### platformFamily
- **Type**: typing.Optional[str]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationOutputTypeDef]

### rolloutState
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### rolloutStateReason
- **Type**: typing.Optional[str]

### serviceConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationOutputTypeDef]

### serviceConnectResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectServiceResourceTypeDef]]

### volumeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationOutputTypeDef]]

### fargateEphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentEphemeralStorageTypeDef]


# DeregisterContainerInstanceRequestRequestTypeDef

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


# DeregisterTaskDefinitionRequestRequestTypeDef

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


# DescribeCapacityProvidersRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClustersRequestRequestTypeDef

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


# DescribeContainerInstancesRequestRequestTypeDef

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


# DescribeServicesRequestRequestTypeDef

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeServicesRequestServicesInactiveWaitTypeDef

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.WaiterConfigTypeDef]


# DescribeServicesRequestServicesStableWaitTypeDef

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


# DescribeTaskDefinitionRequestRequestTypeDef

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


# DescribeTaskSetsRequestRequestTypeDef

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


# DescribeTasksRequestRequestTypeDef

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]


# DescribeTasksRequestTasksRunningWaitTypeDef

### tasks
- **Type**: typing.Sequence[str]
- **Required**: Yes

### cluster
- **Type**: typing.Optional[str]

### include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['TAGS']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.WaiterConfigTypeDef]


# DescribeTasksRequestTasksStoppedWaitTypeDef

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


# DiscoverPollEndpointRequestRequestTypeDef

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

### value
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['s3']
- **Required**: Yes


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


# ExecuteCommandRequestRequestTypeDef

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

### type
- **Type**: typing.Literal['fluentbit', 'fluentd']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Dict[str, str]]


# FirelensConfigurationTypeDef

### type
- **Type**: typing.Literal['fluentbit', 'fluentd']
- **Required**: Yes

### options
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetTaskProtectionRequestRequestTypeDef

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

### type
- **Type**: typing.Optional[typing.Literal['CONTAINER_RUNTIME']]

### status
- **Type**: typing.Optional[typing.Literal['IMPAIRED', 'INITIALIZING', 'INSUFFICIENT_DATA', 'OK']]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]

### lastStatusChange
- **Type**: typing.Optional[datetime.datetime]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.KernelCapabilitiesTypeDef]

### devices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.DeviceTypeDef]]

### initProcessEnabled
- **Type**: typing.Optional[bool]

### sharedMemorySize
- **Type**: typing.Optional[int]

### tmpfs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.TmpfsTypeDef]]

### maxSwap
- **Type**: typing.Optional[int]

### swappiness
- **Type**: typing.Optional[int]


# ListAccountSettingsRequestListAccountSettingsPaginateTypeDef

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


# ListAccountSettingsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttributesRequestListAttributesPaginateTypeDef

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


# ListAttributesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListClustersRequestListClustersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListClustersRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListClustersResponseTypeDef

### clusterArns
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContainerInstancesRequestListContainerInstancesPaginateTypeDef

### cluster
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEREGISTERING', 'DRAINING', 'REGISTERING', 'REGISTRATION_FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListContainerInstancesRequestRequestTypeDef

### cluster
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEREGISTERING', 'DRAINING', 'REGISTERING', 'REGISTRATION_FAILED']]


# ListContainerInstancesResponseTypeDef

### containerInstanceArns
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListServicesByNamespaceRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServicesRequestListServicesPaginateTypeDef

### cluster
- **Type**: typing.Optional[str]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### schedulingStrategy
- **Type**: typing.Optional[typing.Literal['DAEMON', 'REPLICA']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListServicesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListTaskDefinitionFamiliesRequestListTaskDefinitionFamiliesPaginateTypeDef

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ALL', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListTaskDefinitionFamiliesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTaskDefinitionsRequestListTaskDefinitionsPaginateTypeDef

### familyPrefix
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETE_IN_PROGRESS', 'INACTIVE']]

### sort
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.PaginatorConfigTypeDef]


# ListTaskDefinitionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTasksRequestListTasksPaginateTypeDef

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


# ListTasksRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### type
- **Type**: typing.Optional[typing.Literal['distinctInstance', 'memberOf']]

### expression
- **Type**: typing.Optional[str]


# PlacementStrategyTypeDef

### type
- **Type**: typing.Optional[typing.Literal['binpack', 'random', 'spread']]

### field
- **Type**: typing.Optional[str]


# PlatformDeviceTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['GPU']
- **Required**: Yes


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

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['APPMESH']]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePairTypeDef]]


# ProxyConfigurationTypeDef

### containerName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['APPMESH']]

### properties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.KeyValuePairTypeDef]]


# PutAccountSettingDefaultRequestRequestTypeDef

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


# PutAccountSettingRequestRequestTypeDef

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


# PutAttributesRequestRequestTypeDef

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


# PutClusterCapacityProvidersRequestRequestTypeDef

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


# RegisterContainerInstanceRequestRequestTypeDef

### cluster
- **Type**: typing.Optional[str]

### instanceIdentityDocument
- **Type**: typing.Optional[str]

### instanceIdentityDocumentSignature
- **Type**: typing.Optional[str]

### totalResources
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.ecs_classes.ResourceTypeDef, aws_resource_validator.pydantic_models.ecs_classes.ResourceOutputTypeDef]]]

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


# RegisterTaskDefinitionRequestRequestTypeDef

### family
- **Type**: <class 'str'>
- **Required**: Yes

### containerDefinitions
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.ecs_classes.ContainerDefinitionTypeDef, aws_resource_validator.pydantic_models.ecs_classes.ContainerDefinitionOutputTypeDef]]
- **Required**: Yes

### taskRoleArn
- **Type**: typing.Optional[str]

### executionRoleArn
- **Type**: typing.Optional[str]

### networkMode
- **Type**: typing.Optional[typing.Literal['awsvpc', 'bridge', 'host', 'none']]

### volumes
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.ecs_classes.VolumeTypeDef, aws_resource_validator.pydantic_models.ecs_classes.VolumeOutputTypeDef]]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ProxyConfigurationTypeDef]

### inferenceAccelerators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.InferenceAcceleratorTypeDef]]

### ephemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EphemeralStorageTypeDef]

### runtimePlatform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.RuntimePlatformTypeDef]


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

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### doubleValue
- **Type**: typing.Optional[float]

### longValue
- **Type**: typing.Optional[int]

### integerValue
- **Type**: typing.Optional[int]

### stringSetValue
- **Type**: typing.Optional[typing.List[str]]


# ResourceRequirementTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['GPU', 'InferenceAccelerator']
- **Required**: Yes


# ResourceTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### doubleValue
- **Type**: typing.Optional[float]

### longValue
- **Type**: typing.Optional[int]

### integerValue
- **Type**: typing.Optional[int]

### stringSetValue
- **Type**: typing.Optional[typing.Sequence[str]]


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


# RunTaskRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationTypeDef]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskOverrideTypeDef]

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


# ServiceEventTypeDef

### id
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### message
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'xfs']]


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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EBSTagSpecificationTypeDef]]

### filesystemType
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'xfs']]


# ServiceRegistryTypeDef

### registryArn
- **Type**: typing.Optional[str]

### port
- **Type**: typing.Optional[int]

### containerName
- **Type**: typing.Optional[str]

### containerPort
- **Type**: typing.Optional[int]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceManagedEBSVolumeConfigurationTypeDef]


# SessionTypeDef

### sessionId
- **Type**: typing.Optional[str]

### streamUrl
- **Type**: typing.Optional[str]

### tokenValue
- **Type**: typing.Optional[str]


# SettingTypeDef

### name
- **Type**: typing.Optional[typing.Literal['awsvpcTrunking', 'containerInsights', 'containerInstanceLongArnFormat', 'fargateFIPSMode', 'fargateTaskRetirementWaitPeriod', 'guardDutyActivate', 'serviceLongArnFormat', 'tagResourceAuthorization', 'taskLongArnFormat']]

### value
- **Type**: typing.Optional[str]

### principalArn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['aws_managed', 'user']]


# StartTaskRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationTypeDef]

### overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskOverrideTypeDef]

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


# StopTaskRequestRequestTypeDef

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


# SubmitAttachmentStateChangesRequestRequestTypeDef

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


# SubmitContainerStateChangeRequestRequestTypeDef

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


# SubmitTaskStateChangeRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### pullStoppedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### executionStoppedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# TagResourceRequestRequestTypeDef

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

### type
- **Type**: typing.Optional[typing.Literal['memberOf']]

### expression
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecs_classes.EBSTagSpecificationTypeDef]]

### terminationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.TaskManagedEBSVolumeTerminationPolicyTypeDef]

### filesystemType
- **Type**: typing.Optional[typing.Literal['ext3', 'ext4', 'xfs']]


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


# TaskSetTypeDef

### id
- **Type**: typing.Optional[str]

### taskSetArn
- **Type**: typing.Optional[str]

### serviceArn
- **Type**: typing.Optional[str]

### clusterArn
- **Type**: typing.Optional[str]

### startedBy
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### taskDefinition
- **Type**: typing.Optional[str]

### computedDesiredCount
- **Type**: typing.Optional[int]

### pendingCount
- **Type**: typing.Optional[int]

### runningCount
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### launchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### capacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.CapacityProviderStrategyItemTypeDef]]

### platformVersion
- **Type**: typing.Optional[str]

### platformFamily
- **Type**: typing.Optional[str]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationOutputTypeDef]

### loadBalancers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.LoadBalancerTypeDef]]

### serviceRegistries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.ServiceRegistryTypeDef]]

### scale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ScaleTypeDef]

### stabilityStatus
- **Type**: typing.Optional[typing.Literal['STABILIZING', 'STEADY_STATE']]

### stabilityStatusAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecs_classes.TagTypeDef]]

### fargateEphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentEphemeralStorageTypeDef]


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

### name
- **Type**: typing.Literal['core', 'cpu', 'data', 'fsize', 'locks', 'memlock', 'msgqueue', 'nice', 'nofile', 'nproc', 'rss', 'rtprio', 'rttime', 'sigpending', 'stack']
- **Required**: Yes

### softLimit
- **Type**: <class 'int'>
- **Required**: Yes

### hardLimit
- **Type**: <class 'int'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateCapacityProviderRequestRequestTypeDef

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


# UpdateClusterRequestRequestTypeDef

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


# UpdateClusterSettingsRequestRequestTypeDef

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


# UpdateContainerAgentRequestRequestTypeDef

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


# UpdateContainerInstancesStateRequestRequestTypeDef

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


# UpdateServicePrimaryTaskSetRequestRequestTypeDef

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


# UpdateServiceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DeploymentConfigurationTypeDef]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.NetworkConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.ServiceConnectConfigurationTypeDef]

### volumeConfigurations
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationTypeDef, aws_resource_validator.pydantic_models.ecs_classes.ServiceVolumeConfigurationOutputTypeDef]]]


# UpdateServiceResponseTypeDef

### service
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ServiceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTaskProtectionRequestRequestTypeDef

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


# UpdateTaskSetRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.DockerVolumeConfigurationTypeDef]

### efsVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.EFSVolumeConfigurationTypeDef]

### fsxWindowsFileServerVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecs_classes.FSxWindowsFileServerVolumeConfigurationTypeDef]

### configuredAtLaunch
- **Type**: typing.Optional[bool]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



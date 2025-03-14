# Opsworks Classes

# AgentVersionTypeDef

### Version
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.StackConfigurationManagerTypeDef]


# AppTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssignInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssignVolumeRequestTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]


# AssociateElasticIpRequestTypeDef

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]


# AttachElasticLoadBalancerRequestTypeDef

### ElasticLoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes


# AutoScalingThresholdsOutputTypeDef

### InstanceCount
- **Type**: typing.Optional[int]

### ThresholdsWaitTime
- **Type**: typing.Optional[int]

### IgnoreMetricsTime
- **Type**: typing.Optional[int]

### CpuThreshold
- **Type**: typing.Optional[float]

### MemoryThreshold
- **Type**: typing.Optional[float]

### LoadThreshold
- **Type**: typing.Optional[float]

### Alarms
- **Type**: typing.Optional[typing.List[str]]


# AutoScalingThresholdsTypeDef

### InstanceCount
- **Type**: typing.Optional[int]

### ThresholdsWaitTime
- **Type**: typing.Optional[int]

### IgnoreMetricsTime
- **Type**: typing.Optional[int]

### CpuThreshold
- **Type**: typing.Optional[float]

### MemoryThreshold
- **Type**: typing.Optional[float]

### LoadThreshold
- **Type**: typing.Optional[float]

### Alarms
- **Type**: typing.Optional[typing.Sequence[str]]


# AutoScalingThresholdsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockDeviceMappingTypeDef

### DeviceName
- **Type**: typing.Optional[str]

### NoDevice
- **Type**: typing.Optional[str]

### VirtualName
- **Type**: typing.Optional[str]

### Ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.EbsBlockDeviceTypeDef]


# ChefConfigurationTypeDef

### ManageBerkshelf
- **Type**: typing.Optional[bool]

### BerkshelfVersion
- **Type**: typing.Optional[str]


# CloneStackRequestTypeDef

### SourceStackId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['Color'], str]]

### DefaultInstanceProfileArn
- **Type**: typing.Optional[str]

### DefaultOs
- **Type**: typing.Optional[str]

### HostnameTheme
- **Type**: typing.Optional[str]

### DefaultAvailabilityZone
- **Type**: typing.Optional[str]

### DefaultSubnetId
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.StackConfigurationManagerTypeDef]

### ChefConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.ChefConfigurationTypeDef]

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.SourceTypeDef]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### ClonePermissions
- **Type**: typing.Optional[bool]

### CloneAppIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### AgentVersion
- **Type**: typing.Optional[str]


# CloneStackResultTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudWatchLogsConfigurationOutputTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### LogStreams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks_classes.CloudWatchLogsLogStreamTypeDef]]


# CloudWatchLogsConfigurationTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### LogStreams
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworks_classes.CloudWatchLogsLogStreamTypeDef]]


# CloudWatchLogsConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsLogStreamTypeDef

### LogGroupName
- **Type**: typing.Optional[str]

### DatetimeFormat
- **Type**: typing.Optional[str]

### TimeZone
- **Type**: typing.Optional[typing.Literal['LOCAL', 'UTC']]

### File
- **Type**: typing.Optional[str]

### FileFingerprintLines
- **Type**: typing.Optional[str]

### MultiLineStartPattern
- **Type**: typing.Optional[str]

### InitialPosition
- **Type**: typing.Optional[typing.Literal['end_of_file', 'start_of_file']]

### Encoding
- **Type**: typing.Optional[typing.Literal['ascii', 'big5', 'big5hkscs', 'cp037', 'cp1006', 'cp1026', 'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp424', 'cp437', 'cp500', 'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp864', 'cp865', 'cp866', 'cp869', 'cp874', 'cp875', 'cp932', 'cp949', 'cp950', 'euc_jis_2004', 'euc_jisx0213', 'euc_jp', 'euc_kr', 'gb18030', 'gb2312', 'gbk', 'hz', 'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr', 'iso8859_10', 'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'iso8859_2', 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 'iso8859_7', 'iso8859_8', 'iso8859_9', 'johab', 'koi8_r', 'koi8_u', 'latin_1', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 'mac_latin2', 'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis', 'shift_jis_2004', 'shift_jisx0213', 'utf_16', 'utf_16_be', 'utf_16_le', 'utf_32', 'utf_32_be', 'utf_32_le', 'utf_7', 'utf_8', 'utf_8_sig']]

### BufferDuration
- **Type**: typing.Optional[int]

### BatchCount
- **Type**: typing.Optional[int]

### BatchSize
- **Type**: typing.Optional[int]


# CommandTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAppResultTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Command
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.DeploymentCommandUnionTypeDef'>
- **Required**: Yes

### AppId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### LayerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Comment
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]


# CreateDeploymentResultTypeDef

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstanceRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingType
- **Type**: typing.Optional[typing.Literal['load', 'timer']]

### Hostname
- **Type**: typing.Optional[str]

### Os
- **Type**: typing.Optional[str]

### AmiId
- **Type**: typing.Optional[str]

### SshKeyName
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VirtualizationType
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[typing.Literal['i386', 'x86_64']]

### RootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworks_classes.BlockDeviceMappingTypeDef]]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### EbsOptimized
- **Type**: typing.Optional[bool]

### AgentVersion
- **Type**: typing.Optional[str]

### Tenancy
- **Type**: typing.Optional[str]


# CreateInstanceResultTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLayerResultTypeDef

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStackRequestServiceResourceCreateStackTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultInstanceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['Color'], str]]

### DefaultOs
- **Type**: typing.Optional[str]

### HostnameTheme
- **Type**: typing.Optional[str]

### DefaultAvailabilityZone
- **Type**: typing.Optional[str]

### DefaultSubnetId
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.StackConfigurationManagerTypeDef]

### ChefConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.ChefConfigurationTypeDef]

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.SourceTypeDef]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### AgentVersion
- **Type**: typing.Optional[str]


# CreateStackRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultInstanceProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['Color'], str]]

### DefaultOs
- **Type**: typing.Optional[str]

### HostnameTheme
- **Type**: typing.Optional[str]

### DefaultAvailabilityZone
- **Type**: typing.Optional[str]

### DefaultSubnetId
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.StackConfigurationManagerTypeDef]

### ChefConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.ChefConfigurationTypeDef]

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.SourceTypeDef]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### AgentVersion
- **Type**: typing.Optional[str]


# CreateStackResultTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserProfileRequestTypeDef

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### SshUsername
- **Type**: typing.Optional[str]

### SshPublicKey
- **Type**: typing.Optional[str]

### AllowSelfManagement
- **Type**: typing.Optional[bool]


# CreateUserProfileResultTypeDef

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteElasticIp
- **Type**: typing.Optional[bool]

### DeleteVolumes
- **Type**: typing.Optional[bool]


# DeleteLayerRequestTypeDef

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStackRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserProfileRequestTypeDef

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeploymentCommandOutputTypeDef

### Name
- **Type**: typing.Literal['configure', 'deploy', 'execute_recipes', 'install_dependencies', 'restart', 'rollback', 'setup', 'start', 'stop', 'undeploy', 'update_custom_cookbooks', 'update_dependencies']
- **Required**: Yes

### Args
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# DeploymentCommandTypeDef

### Name
- **Type**: typing.Literal['configure', 'deploy', 'execute_recipes', 'install_dependencies', 'restart', 'rollback', 'setup', 'start', 'stop', 'undeploy', 'update_custom_cookbooks', 'update_dependencies']
- **Required**: Yes

### Args
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# DeploymentCommandUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentTypeDef

### DeploymentId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### AppId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### CompletedAt
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[int]

### IamUserArn
- **Type**: typing.Optional[str]

### Comment
- **Type**: typing.Optional[str]

### Command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.DeploymentCommandOutputTypeDef]

### Status
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# DeregisterEcsClusterRequestTypeDef

### EcsClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterElasticIpRequestTypeDef

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterRdsDbInstanceRequestTypeDef

### RdsDbInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterVolumeRequestTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgentVersionsRequestTypeDef

### StackId
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.StackConfigurationManagerTypeDef]


# DescribeAgentVersionsResultTypeDef

### AgentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.AgentVersionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppsRequestTypeDef

### StackId
- **Type**: typing.Optional[str]

### AppIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeAppsRequestWaitTypeDef

### StackId
- **Type**: typing.Optional[str]

### AppIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.WaiterConfigTypeDef]


# DescribeAppsResultTypeDef

### Apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.AppTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCommandsRequestTypeDef

### DeploymentId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### CommandIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeCommandsResultTypeDef

### Commands
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.CommandTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeploymentsRequestTypeDef

### StackId
- **Type**: typing.Optional[str]

### AppId
- **Type**: typing.Optional[str]

### DeploymentIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeDeploymentsRequestWaitTypeDef

### StackId
- **Type**: typing.Optional[str]

### AppId
- **Type**: typing.Optional[str]

### DeploymentIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.WaiterConfigTypeDef]


# DescribeDeploymentsResultTypeDef

### Deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.DeploymentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEcsClustersRequestPaginateTypeDef

### EcsClusterArns
- **Type**: typing.Optional[typing.Sequence[str]]

### StackId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.PaginatorConfigTypeDef]


# DescribeEcsClustersRequestTypeDef

### EcsClusterArns
- **Type**: typing.Optional[typing.Sequence[str]]

### StackId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeEcsClustersResultTypeDef

### EcsClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.EcsClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeElasticIpsRequestTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### Ips
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeElasticIpsResultTypeDef

### ElasticIps
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.ElasticIpTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeElasticLoadBalancersRequestTypeDef

### StackId
- **Type**: typing.Optional[str]

### LayerIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeElasticLoadBalancersResultTypeDef

### ElasticLoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.ElasticLoadBalancerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInstancesRequestTypeDef

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeInstancesRequestWaitExtraExtraExtraTypeDef

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.WaiterConfigTypeDef]


# DescribeInstancesRequestWaitExtraExtraTypeDef

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.WaiterConfigTypeDef]


# DescribeInstancesRequestWaitExtraTypeDef

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.WaiterConfigTypeDef]


# DescribeInstancesRequestWaitTypeDef

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.WaiterConfigTypeDef]


# DescribeInstancesResultTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.InstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLayersRequestTypeDef

### StackId
- **Type**: typing.Optional[str]

### LayerIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeLayersResultTypeDef

### Layers
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.LayerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoadBasedAutoScalingRequestTypeDef

### LayerIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeLoadBasedAutoScalingResultTypeDef

### LoadBasedAutoScalingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.LoadBasedAutoScalingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMyUserProfileResultTypeDef

### UserProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.SelfUserProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOperatingSystemsResponseTypeDef

### OperatingSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.OperatingSystemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePermissionsRequestTypeDef

### IamUserArn
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]


# DescribePermissionsResultTypeDef

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.PermissionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRaidArraysRequestTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### RaidArrayIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeRaidArraysResultTypeDef

### RaidArrays
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.RaidArrayTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRdsDbInstancesRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### RdsDbInstanceArns
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeRdsDbInstancesResultTypeDef

### RdsDbInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.RdsDbInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceErrorsRequestTypeDef

### StackId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### ServiceErrorIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeServiceErrorsResultTypeDef

### ServiceErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.ServiceErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackProvisioningParametersRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackProvisioningParametersResultTypeDef

### AgentInstallerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStackSummaryRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackSummaryResultTypeDef

### StackSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.StackSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStacksRequestTypeDef

### StackIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeStacksResultTypeDef

### Stacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.StackTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTimeBasedAutoScalingRequestTypeDef

### InstanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTimeBasedAutoScalingResultTypeDef

### TimeBasedAutoScalingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.TimeBasedAutoScalingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserProfilesRequestTypeDef

### IamUserArns
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeUserProfilesResultTypeDef

### UserProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.UserProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVolumesRequestTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### RaidArrayId
- **Type**: typing.Optional[str]

### VolumeIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeVolumesResultTypeDef

### Volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks_classes.VolumeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachElasticLoadBalancerRequestTypeDef

### ElasticLoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateElasticIpRequestTypeDef

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes


# EbsBlockDeviceTypeDef

### SnapshotId
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### VolumeSize
- **Type**: typing.Optional[int]

### VolumeType
- **Type**: typing.Optional[typing.Literal['gp2', 'io1', 'standard']]

### DeleteOnTermination
- **Type**: typing.Optional[bool]


# EcsClusterTypeDef

### EcsClusterArn
- **Type**: typing.Optional[str]

### EcsClusterName
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### RegisteredAt
- **Type**: typing.Optional[str]


# ElasticIpTypeDef

### Ip
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]


# ElasticLoadBalancerTypeDef

### ElasticLoadBalancerName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### DnsName
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Ec2InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentVariableTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Secure
- **Type**: typing.Optional[bool]


# GetHostnameSuggestionRequestTypeDef

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHostnameSuggestionResultTypeDef

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### Hostname
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GrantAccessRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ValidForInMinutes
- **Type**: typing.Optional[int]


# GrantAccessResultTypeDef

### TemporaryCredential
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.TemporaryCredentialTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceIdentityTypeDef

### Document
- **Type**: typing.Optional[str]

### Signature
- **Type**: typing.Optional[str]


# InstanceTypeDef

### AgentVersion
- **Type**: typing.Optional[str]

### AmiId
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[typing.Literal['i386', 'x86_64']]

### Arn
- **Type**: typing.Optional[str]

### AutoScalingType
- **Type**: typing.Optional[typing.Literal['load', 'timer']]

### AvailabilityZone
- **Type**: typing.Optional[str]

### BlockDeviceMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks_classes.BlockDeviceMappingTypeDef]]

### CreatedAt
- **Type**: typing.Optional[str]

### EbsOptimized
- **Type**: typing.Optional[bool]

### Ec2InstanceId
- **Type**: typing.Optional[str]

### EcsClusterArn
- **Type**: typing.Optional[str]

### EcsContainerInstanceArn
- **Type**: typing.Optional[str]

### ElasticIp
- **Type**: typing.Optional[str]

### Hostname
- **Type**: typing.Optional[str]

### InfrastructureClass
- **Type**: typing.Optional[str]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### InstanceId
- **Type**: typing.Optional[str]

### InstanceProfileArn
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### LastServiceErrorId
- **Type**: typing.Optional[str]

### LayerIds
- **Type**: typing.Optional[typing.List[str]]

### Os
- **Type**: typing.Optional[str]

### Platform
- **Type**: typing.Optional[str]

### PrivateDns
- **Type**: typing.Optional[str]

### PrivateIp
- **Type**: typing.Optional[str]

### PublicDns
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]

### RegisteredBy
- **Type**: typing.Optional[str]

### ReportedAgentVersion
- **Type**: typing.Optional[str]

### ReportedOs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.ReportedOsTypeDef]

### RootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### RootDeviceVolumeId
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### SshHostDsaKeyFingerprint
- **Type**: typing.Optional[str]

### SshHostRsaKeyFingerprint
- **Type**: typing.Optional[str]

### SshKeyName
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### Tenancy
- **Type**: typing.Optional[str]

### VirtualizationType
- **Type**: typing.Optional[typing.Literal['hvm', 'paravirtual']]


# InstancesCountTypeDef

### Assigning
- **Type**: typing.Optional[int]

### Booting
- **Type**: typing.Optional[int]

### ConnectionLost
- **Type**: typing.Optional[int]

### Deregistering
- **Type**: typing.Optional[int]

### Online
- **Type**: typing.Optional[int]

### Pending
- **Type**: typing.Optional[int]

### Rebooting
- **Type**: typing.Optional[int]

### Registered
- **Type**: typing.Optional[int]

### Registering
- **Type**: typing.Optional[int]

### Requested
- **Type**: typing.Optional[int]

### RunningSetup
- **Type**: typing.Optional[int]

### SetupFailed
- **Type**: typing.Optional[int]

### ShuttingDown
- **Type**: typing.Optional[int]

### StartFailed
- **Type**: typing.Optional[int]

### StopFailed
- **Type**: typing.Optional[int]

### Stopped
- **Type**: typing.Optional[int]

### Stopping
- **Type**: typing.Optional[int]

### Terminated
- **Type**: typing.Optional[int]

### Terminating
- **Type**: typing.Optional[int]

### Unassigning
- **Type**: typing.Optional[int]


# LayerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LifecycleEventConfigurationTypeDef

### Shutdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.ShutdownEventConfigurationTypeDef]


# ListTagsRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsResultTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoadBasedAutoScalingConfigurationTypeDef

### LayerId
- **Type**: typing.Optional[str]

### Enable
- **Type**: typing.Optional[bool]

### UpScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.AutoScalingThresholdsOutputTypeDef]

### DownScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.AutoScalingThresholdsOutputTypeDef]


# OperatingSystemConfigurationManagerTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# OperatingSystemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionTypeDef

### StackId
- **Type**: typing.Optional[str]

### IamUserArn
- **Type**: typing.Optional[str]

### AllowSsh
- **Type**: typing.Optional[bool]

### AllowSudo
- **Type**: typing.Optional[bool]

### Level
- **Type**: typing.Optional[str]


# RaidArrayTypeDef

### RaidArrayId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RaidLevel
- **Type**: typing.Optional[int]

### NumberOfDisks
- **Type**: typing.Optional[int]

### Size
- **Type**: typing.Optional[int]

### Device
- **Type**: typing.Optional[str]

### MountPoint
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]


# RdsDbInstanceTypeDef

### RdsDbInstanceArn
- **Type**: typing.Optional[str]

### DbInstanceIdentifier
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### DbPassword
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### Address
- **Type**: typing.Optional[str]

### Engine
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### MissingOnRds
- **Type**: typing.Optional[bool]


# RebootInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# RecipesOutputTypeDef

### Setup
- **Type**: typing.Optional[typing.List[str]]

### Configure
- **Type**: typing.Optional[typing.List[str]]

### Deploy
- **Type**: typing.Optional[typing.List[str]]

### Undeploy
- **Type**: typing.Optional[typing.List[str]]

### Shutdown
- **Type**: typing.Optional[typing.List[str]]


# RecipesTypeDef

### Setup
- **Type**: typing.Optional[typing.Sequence[str]]

### Configure
- **Type**: typing.Optional[typing.Sequence[str]]

### Deploy
- **Type**: typing.Optional[typing.Sequence[str]]

### Undeploy
- **Type**: typing.Optional[typing.Sequence[str]]

### Shutdown
- **Type**: typing.Optional[typing.Sequence[str]]


# RecipesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegisterEcsClusterRequestTypeDef

### EcsClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterEcsClusterResultTypeDef

### EcsClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterElasticIpRequestTypeDef

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterElasticIpResultTypeDef

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterInstanceRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Hostname
- **Type**: typing.Optional[str]

### PublicIp
- **Type**: typing.Optional[str]

### PrivateIp
- **Type**: typing.Optional[str]

### RsaPublicKey
- **Type**: typing.Optional[str]

### RsaPublicKeyFingerprint
- **Type**: typing.Optional[str]

### InstanceIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.InstanceIdentityTypeDef]


# RegisterInstanceResultTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterRdsDbInstanceRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### RdsDbInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DbUser
- **Type**: <class 'str'>
- **Required**: Yes

### DbPassword
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterVolumeRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2VolumeId
- **Type**: typing.Optional[str]


# RegisterVolumeResultTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReportedOsTypeDef

### Family
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


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


# SelfUserProfileTypeDef

### IamUserArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SshUsername
- **Type**: typing.Optional[str]

### SshPublicKey
- **Type**: typing.Optional[str]


# ServiceErrorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SetLoadBasedAutoScalingRequestTypeDef

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### Enable
- **Type**: typing.Optional[bool]

### UpScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.AutoScalingThresholdsUnionTypeDef]

### DownScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.AutoScalingThresholdsUnionTypeDef]


# SetPermissionRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### AllowSsh
- **Type**: typing.Optional[bool]

### AllowSudo
- **Type**: typing.Optional[bool]

### Level
- **Type**: typing.Optional[str]


# SetTimeBasedAutoScalingRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.WeeklyAutoScalingScheduleUnionTypeDef]


# ShutdownEventConfigurationTypeDef

### ExecutionTimeout
- **Type**: typing.Optional[int]

### DelayUntilElbConnectionsDrained
- **Type**: typing.Optional[bool]


# SourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SslConfigurationTypeDef

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### PrivateKey
- **Type**: <class 'str'>
- **Required**: Yes

### Chain
- **Type**: typing.Optional[str]


# StackConfigurationManagerTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# StackSummaryTypeDef

### StackId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### LayersCount
- **Type**: typing.Optional[int]

### AppsCount
- **Type**: typing.Optional[int]

### InstancesCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.InstancesCountTypeDef]


# StackTypeDef

### StackId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['Color'], str]]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### DefaultInstanceProfileArn
- **Type**: typing.Optional[str]

### DefaultOs
- **Type**: typing.Optional[str]

### HostnameTheme
- **Type**: typing.Optional[str]

### DefaultAvailabilityZone
- **Type**: typing.Optional[str]

### DefaultSubnetId
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.StackConfigurationManagerTypeDef]

### ChefConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.ChefConfigurationTypeDef]

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.SourceTypeDef]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### AgentVersion
- **Type**: typing.Optional[str]


# StartInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# StartStackRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# StopInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# StopStackRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemporaryCredentialTypeDef

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### ValidForInMinutes
- **Type**: typing.Optional[int]

### InstanceId
- **Type**: typing.Optional[str]


# TimeBasedAutoScalingConfigurationTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### AutoScalingSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.WeeklyAutoScalingScheduleOutputTypeDef]


# UnassignInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UnassignVolumeRequestTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateElasticIpRequestTypeDef

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateInstanceRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### InstanceType
- **Type**: typing.Optional[str]

### AutoScalingType
- **Type**: typing.Optional[typing.Literal['load', 'timer']]

### Hostname
- **Type**: typing.Optional[str]

### Os
- **Type**: typing.Optional[str]

### AmiId
- **Type**: typing.Optional[str]

### SshKeyName
- **Type**: typing.Optional[str]

### Architecture
- **Type**: typing.Optional[typing.Literal['i386', 'x86_64']]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### EbsOptimized
- **Type**: typing.Optional[bool]

### AgentVersion
- **Type**: typing.Optional[str]


# UpdateLayerRequestTypeDef

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Shortname
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['BundlerVersion', 'EcsClusterArn', 'EnableHaproxyStats', 'GangliaPassword', 'GangliaUrl', 'GangliaUser', 'HaproxyHealthCheckMethod', 'HaproxyHealthCheckUrl', 'HaproxyStatsPassword', 'HaproxyStatsUrl', 'HaproxyStatsUser', 'JavaAppServer', 'JavaAppServerVersion', 'Jvm', 'JvmOptions', 'JvmVersion', 'ManageBundler', 'MemcachedMemory', 'MysqlRootPassword', 'MysqlRootPasswordUbiquitous', 'NodejsVersion', 'PassengerVersion', 'RailsStack', 'RubyVersion', 'RubygemsVersion'], str]]

### CloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.CloudWatchLogsConfigurationUnionTypeDef]

### CustomInstanceProfileArn
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### CustomSecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Packages
- **Type**: typing.Optional[typing.Sequence[str]]

### VolumeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.opsworks_classes.VolumeConfigurationTypeDef]]

### EnableAutoHealing
- **Type**: typing.Optional[bool]

### AutoAssignElasticIps
- **Type**: typing.Optional[bool]

### AutoAssignPublicIps
- **Type**: typing.Optional[bool]

### CustomRecipes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.RecipesUnionTypeDef]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### UseEbsOptimizedInstances
- **Type**: typing.Optional[bool]

### LifecycleEventConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.LifecycleEventConfigurationTypeDef]


# UpdateMyUserProfileRequestTypeDef

### SshPublicKey
- **Type**: typing.Optional[str]


# UpdateRdsDbInstanceRequestTypeDef

### RdsDbInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DbUser
- **Type**: typing.Optional[str]

### DbPassword
- **Type**: typing.Optional[str]


# UpdateStackRequestTypeDef

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[typing.Literal['Color'], str]]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### DefaultInstanceProfileArn
- **Type**: typing.Optional[str]

### DefaultOs
- **Type**: typing.Optional[str]

### HostnameTheme
- **Type**: typing.Optional[str]

### DefaultAvailabilityZone
- **Type**: typing.Optional[str]

### DefaultSubnetId
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.StackConfigurationManagerTypeDef]

### ChefConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.ChefConfigurationTypeDef]

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks_classes.SourceTypeDef]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### AgentVersion
- **Type**: typing.Optional[str]


# UpdateUserProfileRequestTypeDef

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### SshUsername
- **Type**: typing.Optional[str]

### SshPublicKey
- **Type**: typing.Optional[str]

### AllowSelfManagement
- **Type**: typing.Optional[bool]


# UpdateVolumeRequestTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MountPoint
- **Type**: typing.Optional[str]


# UserProfileTypeDef

### IamUserArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SshUsername
- **Type**: typing.Optional[str]

### SshPublicKey
- **Type**: typing.Optional[str]

### AllowSelfManagement
- **Type**: typing.Optional[bool]


# VolumeConfigurationTypeDef

### MountPoint
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfDisks
- **Type**: <class 'int'>
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### RaidLevel
- **Type**: typing.Optional[int]

### VolumeType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### Encrypted
- **Type**: typing.Optional[bool]


# VolumeTypeDef

### VolumeId
- **Type**: typing.Optional[str]

### Ec2VolumeId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RaidArrayId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Size
- **Type**: typing.Optional[int]

### Device
- **Type**: typing.Optional[str]

### MountPoint
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### Iops
- **Type**: typing.Optional[int]

### Encrypted
- **Type**: typing.Optional[bool]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WeeklyAutoScalingScheduleOutputTypeDef

### Monday
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tuesday
- **Type**: typing.Optional[typing.Dict[str, str]]

### Wednesday
- **Type**: typing.Optional[typing.Dict[str, str]]

### Thursday
- **Type**: typing.Optional[typing.Dict[str, str]]

### Friday
- **Type**: typing.Optional[typing.Dict[str, str]]

### Saturday
- **Type**: typing.Optional[typing.Dict[str, str]]

### Sunday
- **Type**: typing.Optional[typing.Dict[str, str]]


# WeeklyAutoScalingScheduleTypeDef

### Monday
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tuesday
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Wednesday
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Thursday
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Friday
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Saturday
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Sunday
- **Type**: typing.Optional[typing.Mapping[str, str]]


# WeeklyAutoScalingScheduleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


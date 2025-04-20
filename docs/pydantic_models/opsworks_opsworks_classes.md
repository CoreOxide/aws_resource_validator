# Opsworks Opsworks Classes

# AgentVersion

### Version
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.StackConfigurationManager]


# App

### AppId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### Shortname
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.DataSource]]

### Type
- **Type**: typing.Optional[typing.Literal['aws-flow-ruby', 'java', 'nodejs', 'other', 'php', 'rails', 'static']]

### AppSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Source]

### Domains
- **Type**: typing.Optional[typing.List[str]]

### EnableSsl
- **Type**: typing.Optional[bool]

### SslConfiguration
- **Type**: <class 'NoneType'>

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['AutoBundleOnDeploy', 'AwsFlowRubySettings', 'DocumentRoot', 'RailsEnv'], str]]

### CreatedAt
- **Type**: typing.Optional[str]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.EnvironmentVariable]]


# AssignInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerIds
- **Type**: typing.List[str]
- **Required**: Yes


# AssignVolumeRequest

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]


# AssociateElasticIpRequest

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceId
- **Type**: typing.Optional[str]


# AttachElasticLoadBalancerRequest

### ElasticLoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes


# AutoScalingThresholds

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


# AutoScalingThresholdsOutput

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockDeviceMapping

### DeviceName
- **Type**: typing.Optional[str]

### NoDevice
- **Type**: typing.Optional[str]

### VirtualName
- **Type**: typing.Optional[str]

### Ebs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.EbsBlockDevice]


# ChefConfiguration

### ManageBerkshelf
- **Type**: typing.Optional[bool]

### BerkshelfVersion
- **Type**: typing.Optional[str]


# CloneStackRequest

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['Color'], str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.StackConfigurationManager]

### ChefConfiguration
- **Type**: <class 'NoneType'>

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Source]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### ClonePermissions
- **Type**: typing.Optional[bool]

### CloneAppIds
- **Type**: typing.Optional[typing.List[str]]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### AgentVersion
- **Type**: typing.Optional[str]


# CloneStackResult

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# CloudWatchLogsConfiguration

### Enabled
- **Type**: typing.Optional[bool]

### LogStreams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsLogStream]]


# CloudWatchLogsConfigurationOutput

### Enabled
- **Type**: typing.Optional[bool]

### LogStreams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsLogStream]]


# CloudWatchLogsLogStream

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


# Command

### CommandId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### DeploymentId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### AcknowledgedAt
- **Type**: typing.Optional[str]

### CompletedAt
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### ExitCode
- **Type**: typing.Optional[int]

### LogUrl
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# CreateAppRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['aws-flow-ruby', 'java', 'nodejs', 'other', 'php', 'rails', 'static']
- **Required**: Yes

### Shortname
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.DataSource]]

### AppSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Source]

### Domains
- **Type**: typing.Optional[typing.List[str]]

### EnableSsl
- **Type**: typing.Optional[bool]

### SslConfiguration
- **Type**: <class 'NoneType'>

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['AutoBundleOnDeploy', 'AwsFlowRubySettings', 'DocumentRoot', 'RailsEnv'], str]]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.EnvironmentVariable]]


# CreateAppResult

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Command
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.DeploymentCommand, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.DeploymentCommandOutput]
- **Required**: Yes

### AppId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### LayerIds
- **Type**: typing.Optional[typing.List[str]]

### Comment
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]


# CreateDeploymentResult

### DeploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstanceRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerIds
- **Type**: typing.List[str]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.BlockDeviceMapping]]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### EbsOptimized
- **Type**: typing.Optional[bool]

### AgentVersion
- **Type**: typing.Optional[str]

### Tenancy
- **Type**: typing.Optional[str]


# CreateInstanceResult

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLayerRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['aws-flow-ruby', 'custom', 'db-master', 'ecs-cluster', 'java-app', 'lb', 'memcached', 'monitoring-master', 'nodejs-app', 'php-app', 'rails-app', 'web']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Shortname
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['BundlerVersion', 'EcsClusterArn', 'EnableHaproxyStats', 'GangliaPassword', 'GangliaUrl', 'GangliaUser', 'HaproxyHealthCheckMethod', 'HaproxyHealthCheckUrl', 'HaproxyStatsPassword', 'HaproxyStatsUrl', 'HaproxyStatsUser', 'JavaAppServer', 'JavaAppServerVersion', 'Jvm', 'JvmOptions', 'JvmVersion', 'ManageBundler', 'MemcachedMemory', 'MysqlRootPassword', 'MysqlRootPasswordUbiquitous', 'NodejsVersion', 'PassengerVersion', 'RailsStack', 'RubyVersion', 'RubygemsVersion'], str]]

### CloudWatchLogsConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsConfiguration, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsConfigurationOutput, NoneType]

### CustomInstanceProfileArn
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### CustomSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Packages
- **Type**: typing.Optional[typing.List[str]]

### VolumeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.VolumeConfiguration]]

### EnableAutoHealing
- **Type**: typing.Optional[bool]

### AutoAssignElasticIps
- **Type**: typing.Optional[bool]

### AutoAssignPublicIps
- **Type**: typing.Optional[bool]

### CustomRecipes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Recipes, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.RecipesOutput, NoneType]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### UseEbsOptimizedInstances
- **Type**: typing.Optional[bool]

### LifecycleEventConfiguration
- **Type**: <class 'NoneType'>


# CreateLayerRequestStackCreateLayer

### Type
- **Type**: typing.Literal['aws-flow-ruby', 'custom', 'db-master', 'ecs-cluster', 'java-app', 'lb', 'memcached', 'monitoring-master', 'nodejs-app', 'php-app', 'rails-app', 'web']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Shortname
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['BundlerVersion', 'EcsClusterArn', 'EnableHaproxyStats', 'GangliaPassword', 'GangliaUrl', 'GangliaUser', 'HaproxyHealthCheckMethod', 'HaproxyHealthCheckUrl', 'HaproxyStatsPassword', 'HaproxyStatsUrl', 'HaproxyStatsUser', 'JavaAppServer', 'JavaAppServerVersion', 'Jvm', 'JvmOptions', 'JvmVersion', 'ManageBundler', 'MemcachedMemory', 'MysqlRootPassword', 'MysqlRootPasswordUbiquitous', 'NodejsVersion', 'PassengerVersion', 'RailsStack', 'RubyVersion', 'RubygemsVersion'], str]]

### CloudWatchLogsConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsConfiguration, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsConfigurationOutput, NoneType]

### CustomInstanceProfileArn
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### CustomSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Packages
- **Type**: typing.Optional[typing.List[str]]

### VolumeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.VolumeConfiguration]]

### EnableAutoHealing
- **Type**: typing.Optional[bool]

### AutoAssignElasticIps
- **Type**: typing.Optional[bool]

### AutoAssignPublicIps
- **Type**: typing.Optional[bool]

### CustomRecipes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Recipes, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.RecipesOutput, NoneType]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### UseEbsOptimizedInstances
- **Type**: typing.Optional[bool]

### LifecycleEventConfiguration
- **Type**: <class 'NoneType'>


# CreateLayerResult

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStackRequest

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['Color'], str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.StackConfigurationManager]

### ChefConfiguration
- **Type**: <class 'NoneType'>

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Source]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### AgentVersion
- **Type**: typing.Optional[str]


# CreateStackRequestServiceResourceCreateStack

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['Color'], str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.StackConfigurationManager]

### ChefConfiguration
- **Type**: <class 'NoneType'>

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Source]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### AgentVersion
- **Type**: typing.Optional[str]


# CreateStackResult

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserProfileRequest

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### SshUsername
- **Type**: typing.Optional[str]

### SshPublicKey
- **Type**: typing.Optional[str]

### AllowSelfManagement
- **Type**: typing.Optional[bool]


# CreateUserProfileResult

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DataSource

### Type
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]


# DeleteAppRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteElasticIp
- **Type**: typing.Optional[bool]

### DeleteVolumes
- **Type**: typing.Optional[bool]


# DeleteLayerRequest

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStackRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserProfileRequest

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes


# Deployment

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.DeploymentCommandOutput]

### Status
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# DeploymentCommand

### Name
- **Type**: typing.Literal['configure', 'deploy', 'execute_recipes', 'install_dependencies', 'restart', 'rollback', 'setup', 'start', 'stop', 'undeploy', 'update_custom_cookbooks', 'update_dependencies']
- **Required**: Yes

### Args
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# DeploymentCommandOutput

### Name
- **Type**: typing.Literal['configure', 'deploy', 'execute_recipes', 'install_dependencies', 'restart', 'rollback', 'setup', 'start', 'stop', 'undeploy', 'update_custom_cookbooks', 'update_dependencies']
- **Required**: Yes

### Args
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# DeregisterEcsClusterRequest

### EcsClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterElasticIpRequest

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterRdsDbInstanceRequest

### RdsDbInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterVolumeRequest

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgentVersionsRequest

### StackId
- **Type**: typing.Optional[str]

### ConfigurationManager
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.StackConfigurationManager]


# DescribeAgentVersionsResult

### AgentVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.AgentVersion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppsRequest

### StackId
- **Type**: typing.Optional[str]

### AppIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeAppsRequestWait

### StackId
- **Type**: typing.Optional[str]

### AppIds
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeAppsResult

### Apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.App]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCommandsRequest

### DeploymentId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### CommandIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeCommandsResult

### Commands
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Command]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDeploymentsRequest

### StackId
- **Type**: typing.Optional[str]

### AppId
- **Type**: typing.Optional[str]

### DeploymentIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeDeploymentsRequestWait

### StackId
- **Type**: typing.Optional[str]

### AppId
- **Type**: typing.Optional[str]

### DeploymentIds
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeDeploymentsResult

### Deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Deployment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEcsClustersRequest

### EcsClusterArns
- **Type**: typing.Optional[typing.List[str]]

### StackId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeEcsClustersRequestPaginate

### EcsClusterArns
- **Type**: typing.Optional[typing.List[str]]

### StackId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.PaginatorConfig]


# DescribeEcsClustersResult

### EcsClusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.EcsCluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeElasticIpsRequest

### InstanceId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### Ips
- **Type**: typing.Optional[typing.List[str]]


# DescribeElasticIpsResult

### ElasticIps
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ElasticIp]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeElasticLoadBalancersRequest

### StackId
- **Type**: typing.Optional[str]

### LayerIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeElasticLoadBalancersResult

### ElasticLoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ElasticLoadBalancer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInstancesRequest

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeInstancesRequestWait

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeInstancesRequestWaitExtra

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeInstancesRequestWaitExtraExtra

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeInstancesRequestWaitExtraExtraExtra

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### InstanceIds
- **Type**: typing.Optional[typing.List[str]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeInstancesResult

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Instance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLayersRequest

### StackId
- **Type**: typing.Optional[str]

### LayerIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeLayersResult

### Layers
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Layer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoadBasedAutoScalingRequest

### LayerIds
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeLoadBasedAutoScalingResult

### LoadBasedAutoScalingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.LoadBasedAutoScalingConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMyUserProfileResult

### UserProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.SelfUserProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOperatingSystemsResponse

### OperatingSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.OperatingSystem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePermissionsRequest

### IamUserArn
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]


# DescribePermissionsResult

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Permission]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRaidArraysRequest

### InstanceId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### RaidArrayIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeRaidArraysResult

### RaidArrays
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.RaidArray]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRdsDbInstancesRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### RdsDbInstanceArns
- **Type**: typing.Optional[typing.List[str]]


# DescribeRdsDbInstancesResult

### RdsDbInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.RdsDbInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServiceErrorsRequest

### StackId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### ServiceErrorIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeServiceErrorsResult

### ServiceErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ServiceError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackProvisioningParametersRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackProvisioningParametersResult

### AgentInstallerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStackSummaryRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStackSummaryResult

### StackSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.StackSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStacksRequest

### StackIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeStacksResult

### Stacks
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Stack]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTimeBasedAutoScalingRequest

### InstanceIds
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeTimeBasedAutoScalingResult

### TimeBasedAutoScalingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.TimeBasedAutoScalingConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserProfilesRequest

### IamUserArns
- **Type**: typing.Optional[typing.List[str]]


# DescribeUserProfilesResult

### UserProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.UserProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVolumesRequest

### InstanceId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### RaidArrayId
- **Type**: typing.Optional[str]

### VolumeIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeVolumesResult

### Volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Volume]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# DetachElasticLoadBalancerRequest

### ElasticLoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateElasticIpRequest

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes


# EbsBlockDevice

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


# EcsCluster

### EcsClusterArn
- **Type**: typing.Optional[str]

### EcsClusterName
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### RegisteredAt
- **Type**: typing.Optional[str]


# ElasticIp

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


# ElasticLoadBalancer

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# EnvironmentVariable

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Secure
- **Type**: typing.Optional[bool]


# GetHostnameSuggestionRequest

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHostnameSuggestionResult

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### Hostname
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# GrantAccessRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ValidForInMinutes
- **Type**: typing.Optional[int]


# GrantAccessResult

### TemporaryCredential
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.TemporaryCredential'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# Instance

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.BlockDeviceMapping]]

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
- **Type**: <class 'NoneType'>

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


# InstanceIdentity

### Document
- **Type**: typing.Optional[str]

### Signature
- **Type**: typing.Optional[str]


# InstancesCount

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


# Layer

### Arn
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### LayerId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['aws-flow-ruby', 'custom', 'db-master', 'ecs-cluster', 'java-app', 'lb', 'memcached', 'monitoring-master', 'nodejs-app', 'php-app', 'rails-app', 'web']]

### Name
- **Type**: typing.Optional[str]

### Shortname
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['BundlerVersion', 'EcsClusterArn', 'EnableHaproxyStats', 'GangliaPassword', 'GangliaUrl', 'GangliaUser', 'HaproxyHealthCheckMethod', 'HaproxyHealthCheckUrl', 'HaproxyStatsPassword', 'HaproxyStatsUrl', 'HaproxyStatsUser', 'JavaAppServer', 'JavaAppServerVersion', 'Jvm', 'JvmOptions', 'JvmVersion', 'ManageBundler', 'MemcachedMemory', 'MysqlRootPassword', 'MysqlRootPasswordUbiquitous', 'NodejsVersion', 'PassengerVersion', 'RailsStack', 'RubyVersion', 'RubygemsVersion'], str]]

### CloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsConfigurationOutput]

### CustomInstanceProfileArn
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### CustomSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### DefaultSecurityGroupNames
- **Type**: typing.Optional[typing.List[str]]

### Packages
- **Type**: typing.Optional[typing.List[str]]

### VolumeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.VolumeConfiguration]]

### EnableAutoHealing
- **Type**: typing.Optional[bool]

### AutoAssignElasticIps
- **Type**: typing.Optional[bool]

### AutoAssignPublicIps
- **Type**: typing.Optional[bool]

### DefaultRecipes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.RecipesOutput]

### CustomRecipes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.RecipesOutput]

### CreatedAt
- **Type**: typing.Optional[str]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### UseEbsOptimizedInstances
- **Type**: typing.Optional[bool]

### LifecycleEventConfiguration
- **Type**: <class 'NoneType'>


# LifecycleEventConfiguration

### Shutdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ShutdownEventConfiguration]


# ListTagsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsResult

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoadBasedAutoScalingConfiguration

### LayerId
- **Type**: typing.Optional[str]

### Enable
- **Type**: typing.Optional[bool]

### UpScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.AutoScalingThresholdsOutput]

### DownScaling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.AutoScalingThresholdsOutput]


# OperatingSystem

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### ConfigurationManagers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.OperatingSystemConfigurationManager]]

### ReportedName
- **Type**: typing.Optional[str]

### ReportedVersion
- **Type**: typing.Optional[str]

### Supported
- **Type**: typing.Optional[bool]


# OperatingSystemConfigurationManager

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Permission

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


# RaidArray

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


# RdsDbInstance

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


# RebootInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# Recipes

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


# RecipesOutput

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


# RegisterEcsClusterRequest

### EcsClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterEcsClusterResult

### EcsClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterElasticIpRequest

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterElasticIpResult

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterInstanceRequest

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
- **Type**: <class 'NoneType'>


# RegisterInstanceResult

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterRdsDbInstanceRequest

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


# RegisterVolumeRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2VolumeId
- **Type**: typing.Optional[str]


# RegisterVolumeResult

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.opsworks.opsworks_classes.ResponseMetadata'>
- **Required**: Yes


# ReportedOs

### Family
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


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


# SelfUserProfile

### IamUserArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### SshUsername
- **Type**: typing.Optional[str]

### SshPublicKey
- **Type**: typing.Optional[str]


# ServiceError

### ServiceErrorId
- **Type**: typing.Optional[str]

### StackId
- **Type**: typing.Optional[str]

### InstanceId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]


# SetLoadBasedAutoScalingRequest

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### Enable
- **Type**: typing.Optional[bool]

### UpScaling
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.AutoScalingThresholds, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.AutoScalingThresholdsOutput, NoneType]

### DownScaling
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.AutoScalingThresholds, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.AutoScalingThresholdsOutput, NoneType]


# SetPermissionRequest

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


# SetTimeBasedAutoScalingRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingSchedule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.WeeklyAutoScalingSchedule, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.WeeklyAutoScalingScheduleOutput, NoneType]


# ShutdownEventConfiguration

### ExecutionTimeout
- **Type**: typing.Optional[int]

### DelayUntilElbConnectionsDrained
- **Type**: typing.Optional[bool]


# Source

### Type
- **Type**: typing.Optional[typing.Literal['archive', 'git', 's3', 'svn']]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### SshKey
- **Type**: typing.Optional[str]

### Revision
- **Type**: typing.Optional[str]


# SslConfiguration

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### PrivateKey
- **Type**: <class 'str'>
- **Required**: Yes

### Chain
- **Type**: typing.Optional[str]


# Stack

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.StackConfigurationManager]

### ChefConfiguration
- **Type**: <class 'NoneType'>

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Source]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### AgentVersion
- **Type**: typing.Optional[str]


# StackConfigurationManager

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# StackSummary

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
- **Type**: <class 'NoneType'>


# StartInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# StartStackRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# StopInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# StopStackRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TemporaryCredential

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### ValidForInMinutes
- **Type**: typing.Optional[int]

### InstanceId
- **Type**: typing.Optional[str]


# TimeBasedAutoScalingConfiguration

### InstanceId
- **Type**: typing.Optional[str]

### AutoScalingSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.WeeklyAutoScalingScheduleOutput]


# UnassignInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# UnassignVolumeRequest

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAppRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DataSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.DataSource]]

### Type
- **Type**: typing.Optional[typing.Literal['aws-flow-ruby', 'java', 'nodejs', 'other', 'php', 'rails', 'static']]

### AppSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Source]

### Domains
- **Type**: typing.Optional[typing.List[str]]

### EnableSsl
- **Type**: typing.Optional[bool]

### SslConfiguration
- **Type**: <class 'NoneType'>

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['AutoBundleOnDeploy', 'AwsFlowRubySettings', 'DocumentRoot', 'RailsEnv'], str]]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.EnvironmentVariable]]


# UpdateElasticIpRequest

### ElasticIp
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateInstanceRequest

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### LayerIds
- **Type**: typing.Optional[typing.List[str]]

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


# UpdateLayerRequest

### LayerId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Shortname
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[typing.Literal['BundlerVersion', 'EcsClusterArn', 'EnableHaproxyStats', 'GangliaPassword', 'GangliaUrl', 'GangliaUser', 'HaproxyHealthCheckMethod', 'HaproxyHealthCheckUrl', 'HaproxyStatsPassword', 'HaproxyStatsUrl', 'HaproxyStatsUser', 'JavaAppServer', 'JavaAppServerVersion', 'Jvm', 'JvmOptions', 'JvmVersion', 'ManageBundler', 'MemcachedMemory', 'MysqlRootPassword', 'MysqlRootPasswordUbiquitous', 'NodejsVersion', 'PassengerVersion', 'RailsStack', 'RubyVersion', 'RubygemsVersion'], str]]

### CloudWatchLogsConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsConfiguration, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.CloudWatchLogsConfigurationOutput, NoneType]

### CustomInstanceProfileArn
- **Type**: typing.Optional[str]

### CustomJson
- **Type**: typing.Optional[str]

### CustomSecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Packages
- **Type**: typing.Optional[typing.List[str]]

### VolumeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.VolumeConfiguration]]

### EnableAutoHealing
- **Type**: typing.Optional[bool]

### AutoAssignElasticIps
- **Type**: typing.Optional[bool]

### AutoAssignPublicIps
- **Type**: typing.Optional[bool]

### CustomRecipes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Recipes, aws_resource_validator.pydantic_models.opsworks.opsworks_classes.RecipesOutput, NoneType]

### InstallUpdatesOnBoot
- **Type**: typing.Optional[bool]

### UseEbsOptimizedInstances
- **Type**: typing.Optional[bool]

### LifecycleEventConfiguration
- **Type**: <class 'NoneType'>


# UpdateMyUserProfileRequest

### SshPublicKey
- **Type**: typing.Optional[str]


# UpdateRdsDbInstanceRequest

### RdsDbInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### DbUser
- **Type**: typing.Optional[str]

### DbPassword
- **Type**: typing.Optional[str]


# UpdateStackRequest

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.StackConfigurationManager]

### ChefConfiguration
- **Type**: <class 'NoneType'>

### UseCustomCookbooks
- **Type**: typing.Optional[bool]

### CustomCookbooksSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.opsworks.opsworks_classes.Source]

### DefaultSshKeyName
- **Type**: typing.Optional[str]

### DefaultRootDeviceType
- **Type**: typing.Optional[typing.Literal['ebs', 'instance-store']]

### UseOpsworksSecurityGroups
- **Type**: typing.Optional[bool]

### AgentVersion
- **Type**: typing.Optional[str]


# UpdateUserProfileRequest

### IamUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### SshUsername
- **Type**: typing.Optional[str]

### SshPublicKey
- **Type**: typing.Optional[str]

### AllowSelfManagement
- **Type**: typing.Optional[bool]


# UpdateVolumeRequest

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MountPoint
- **Type**: typing.Optional[str]


# UserProfile

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


# Volume

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


# VolumeConfiguration

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


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WeeklyAutoScalingSchedule

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


# WeeklyAutoScalingScheduleOutput

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



# Emr Emr Classes

# AddInstanceFleetInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceFleet
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetConfig'>
- **Required**: Yes


# AddInstanceFleetOutput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceFleetId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# AddInstanceGroupsInput

### InstanceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupConfig]
- **Required**: Yes

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# AddInstanceGroupsOutput

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# AddJobFlowStepsInput

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Steps
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.StepConfig, aws_resource_validator.pydantic_models.emr.emr_classes.StepConfigOutput]]
- **Required**: Yes

### ExecutionRoleArn
- **Type**: typing.Optional[str]


# AddJobFlowStepsOutput

### StepIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsInput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Tag]
- **Required**: Yes


# Application

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]

### AdditionalInfo
- **Type**: typing.Optional[typing.Dict[str, str]]


# ApplicationOutput

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]

### AdditionalInfo
- **Type**: typing.Optional[typing.Dict[str, str]]


# AutoScalingPolicy

### Constraints
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ScalingConstraints'>
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.ScalingRule, aws_resource_validator.pydantic_models.emr.emr_classes.ScalingRuleOutput]]
- **Required**: Yes


# AutoScalingPolicyDescription

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.AutoScalingPolicyStatus]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ScalingConstraints]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ScalingRuleOutput]]


# AutoScalingPolicyStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['CLEANUP_FAILURE', 'PROVISION_FAILURE', 'USER_REQUEST']]

### Message
- **Type**: typing.Optional[str]


# AutoScalingPolicyStatus

### State
- **Type**: typing.Optional[typing.Literal['ATTACHED', 'ATTACHING', 'DETACHED', 'DETACHING', 'FAILED', 'PENDING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.AutoScalingPolicyStateChangeReason]


# AutoTerminationPolicy

### IdleTimeout
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockPublicAccessConfiguration

### BlockPublicSecurityGroupRules
- **Type**: <class 'bool'>
- **Required**: Yes

### PermittedPublicSecurityGroupRuleRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.PortRange]]


# BlockPublicAccessConfigurationMetadata

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedByArn
- **Type**: <class 'str'>
- **Required**: Yes


# BlockPublicAccessConfigurationOutput

### BlockPublicSecurityGroupRules
- **Type**: <class 'bool'>
- **Required**: Yes

### PermittedPublicSecurityGroupRuleRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.PortRange]]


# BootstrapActionConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScriptBootstrapAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.ScriptBootstrapActionConfig, aws_resource_validator.pydantic_models.emr.emr_classes.ScriptBootstrapActionConfigOutput]
- **Required**: Yes


# BootstrapActionConfigOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScriptBootstrapAction
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ScriptBootstrapActionConfigOutput'>
- **Required**: Yes


# BootstrapActionDetail

### BootstrapActionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.BootstrapActionConfigOutput]


# CancelStepsInfo

### StepId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUBMITTED']]

### Reason
- **Type**: typing.Optional[str]


# CancelStepsInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepIds
- **Type**: typing.List[str]
- **Required**: Yes

### StepCancellationOption
- **Type**: typing.Optional[typing.Literal['SEND_INTERRUPT', 'TERMINATE_PROCESS']]


# CancelStepsOutput

### CancelStepsInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.CancelStepsInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# CloudWatchAlarmDefinition

### ComparisonOperator
- **Type**: typing.Literal['GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL']
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### EvaluationPeriods
- **Type**: typing.Optional[int]

### Namespace
- **Type**: typing.Optional[str]

### Statistic
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'MAXIMUM', 'MINIMUM', 'SAMPLE_COUNT', 'SUM']]

### Unit
- **Type**: typing.Optional[typing.Literal['BITS', 'BITS_PER_SECOND', 'BYTES', 'BYTES_PER_SECOND', 'COUNT', 'COUNT_PER_SECOND', 'GIGA_BITS', 'GIGA_BITS_PER_SECOND', 'GIGA_BYTES', 'GIGA_BYTES_PER_SECOND', 'KILO_BITS', 'KILO_BITS_PER_SECOND', 'KILO_BYTES', 'KILO_BYTES_PER_SECOND', 'MEGA_BITS', 'MEGA_BITS_PER_SECOND', 'MEGA_BYTES', 'MEGA_BYTES_PER_SECOND', 'MICRO_SECONDS', 'MILLI_SECONDS', 'NONE', 'PERCENT', 'SECONDS', 'TERA_BITS', 'TERA_BITS_PER_SECOND', 'TERA_BYTES', 'TERA_BYTES_PER_SECOND']]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.MetricDimension]]


# CloudWatchAlarmDefinitionOutput

### ComparisonOperator
- **Type**: typing.Literal['GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL']
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### EvaluationPeriods
- **Type**: typing.Optional[int]

### Namespace
- **Type**: typing.Optional[str]

### Statistic
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'MAXIMUM', 'MINIMUM', 'SAMPLE_COUNT', 'SUM']]

### Unit
- **Type**: typing.Optional[typing.Literal['BITS', 'BITS_PER_SECOND', 'BYTES', 'BYTES_PER_SECOND', 'COUNT', 'COUNT_PER_SECOND', 'GIGA_BITS', 'GIGA_BITS_PER_SECOND', 'GIGA_BYTES', 'GIGA_BYTES_PER_SECOND', 'KILO_BITS', 'KILO_BITS_PER_SECOND', 'KILO_BYTES', 'KILO_BYTES_PER_SECOND', 'MEGA_BITS', 'MEGA_BITS_PER_SECOND', 'MEGA_BYTES', 'MEGA_BYTES_PER_SECOND', 'MICRO_SECONDS', 'MILLI_SECONDS', 'NONE', 'PERCENT', 'SECONDS', 'TERA_BITS', 'TERA_BITS_PER_SECOND', 'TERA_BYTES', 'TERA_BYTES_PER_SECOND']]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.MetricDimension]]


# Cluster

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ClusterStatus]

### Ec2InstanceAttributes
- **Type**: <class 'NoneType'>

### InstanceCollectionType
- **Type**: typing.Optional[typing.Literal['INSTANCE_FLEET', 'INSTANCE_GROUP']]

### LogUri
- **Type**: typing.Optional[str]

### LogEncryptionKmsKeyId
- **Type**: typing.Optional[str]

### RequestedAmiVersion
- **Type**: typing.Optional[str]

### RunningAmiVersion
- **Type**: typing.Optional[str]

### ReleaseLabel
- **Type**: typing.Optional[str]

### AutoTerminate
- **Type**: typing.Optional[bool]

### TerminationProtected
- **Type**: typing.Optional[bool]

### UnhealthyNodeReplacement
- **Type**: typing.Optional[bool]

### VisibleToAllUsers
- **Type**: typing.Optional[bool]

### Applications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ApplicationOutput]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Tag]]

### ServiceRole
- **Type**: typing.Optional[str]

### NormalizedInstanceHours
- **Type**: typing.Optional[int]

### MasterPublicDnsName
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationOutput]]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### AutoScalingRole
- **Type**: typing.Optional[str]

### ScaleDownBehavior
- **Type**: typing.Optional[typing.Literal['TERMINATE_AT_INSTANCE_HOUR', 'TERMINATE_AT_TASK_COMPLETION']]

### CustomAmiId
- **Type**: typing.Optional[str]

### EbsRootVolumeSize
- **Type**: typing.Optional[int]

### RepoUpgradeOnBoot
- **Type**: typing.Optional[typing.Literal['NONE', 'SECURITY']]

### KerberosAttributes
- **Type**: <class 'NoneType'>

### ClusterArn
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]

### StepConcurrencyLevel
- **Type**: typing.Optional[int]

### PlacementGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.PlacementGroupConfig]]

### OSReleaseLabel
- **Type**: typing.Optional[str]

### EbsRootVolumeIops
- **Type**: typing.Optional[int]

### EbsRootVolumeThroughput
- **Type**: typing.Optional[int]


# ClusterStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['ALL_STEPS_COMPLETED', 'BOOTSTRAP_FAILURE', 'INSTANCE_FAILURE', 'INSTANCE_FLEET_TIMEOUT', 'INTERNAL_ERROR', 'STEP_FAILURE', 'USER_REQUEST', 'VALIDATION_ERROR']]

### Message
- **Type**: typing.Optional[str]


# ClusterStatus

### State
- **Type**: typing.Optional[typing.Literal['BOOTSTRAPPING', 'RUNNING', 'STARTING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING', 'WAITING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ClusterStateChangeReason]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ClusterTimeline]

### ErrorDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ErrorDetail]]


# ClusterSummary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ClusterStatus]

### NormalizedInstanceHours
- **Type**: typing.Optional[int]

### ClusterArn
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]


# ClusterTimeline

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# Command

### Name
- **Type**: typing.Optional[str]

### ScriptPath
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]


# ComputeLimits

### UnitType
- **Type**: typing.Literal['InstanceFleetUnits', 'Instances', 'VCPU']
- **Required**: Yes

### MinimumCapacityUnits
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumCapacityUnits
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumOnDemandCapacityUnits
- **Type**: typing.Optional[int]

### MaximumCoreCapacityUnits
- **Type**: typing.Optional[int]


# Configuration

### Classification
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConfigurationOutput

### Classification
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConfigurationPaginator

### Classification
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSecurityConfigurationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSecurityConfigurationOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStudioInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AuthMode
- **Type**: typing.Literal['IAM', 'SSO']
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ServiceRole
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### EngineSecurityGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultS3Location
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### UserRole
- **Type**: typing.Optional[str]

### IdpAuthUrl
- **Type**: typing.Optional[str]

### IdpRelayStateParameterName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Tag]]

### TrustedIdentityPropagationEnabled
- **Type**: typing.Optional[bool]

### IdcUserAssignment
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRED']]

### IdcInstanceArn
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# CreateStudioOutput

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStudioSessionMappingInput

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### SessionPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: typing.Optional[str]

### IdentityName
- **Type**: typing.Optional[str]


# Credentials

### UsernamePassword
- **Type**: <class 'NoneType'>


# DeleteSecurityConfigurationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStudioInput

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStudioSessionMappingInput

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### IdentityId
- **Type**: typing.Optional[str]

### IdentityName
- **Type**: typing.Optional[str]


# DescribeClusterInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterInputWait

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterInputWaitExtra

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterOutput

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeJobFlowsInput

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### JobFlowIds
- **Type**: typing.Optional[typing.List[str]]

### JobFlowStates
- **Type**: typing.Optional[typing.List[typing.Literal['BOOTSTRAPPING', 'COMPLETED', 'FAILED', 'RUNNING', 'SHUTTING_DOWN', 'STARTING', 'TERMINATED', 'WAITING']]]


# DescribeJobFlowsOutput

### JobFlows
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.JobFlowDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNotebookExecutionInput

### NotebookExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNotebookExecutionOutput

### NotebookExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.NotebookExecution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReleaseLabelInput

### ReleaseLabel
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeReleaseLabelOutput

### ReleaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.SimplifiedApplication]
- **Required**: Yes

### AvailableOSReleases
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.OSRelease]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSecurityConfigurationInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityConfigurationOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStepInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStepInputWait

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeStepOutput

### Step
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.Step'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStudioInput

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStudioOutput

### Studio
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.Studio'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# EbsBlockDevice

### VolumeSpecification
- **Type**: <class 'NoneType'>

### Device
- **Type**: typing.Optional[str]


# EbsBlockDeviceConfig

### VolumeSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.VolumeSpecification'>
- **Required**: Yes

### VolumesPerInstance
- **Type**: typing.Optional[int]


# EbsConfiguration

### EbsBlockDeviceConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.EbsBlockDeviceConfig]]

### EbsOptimized
- **Type**: typing.Optional[bool]


# EbsVolume

### Device
- **Type**: typing.Optional[str]

### VolumeId
- **Type**: typing.Optional[str]


# Ec2InstanceAttributes

### Ec2KeyName
- **Type**: typing.Optional[str]

### Ec2SubnetId
- **Type**: typing.Optional[str]

### RequestedEc2SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### Ec2AvailabilityZone
- **Type**: typing.Optional[str]

### RequestedEc2AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### IamInstanceProfile
- **Type**: typing.Optional[str]

### EmrManagedMasterSecurityGroup
- **Type**: typing.Optional[str]

### EmrManagedSlaveSecurityGroup
- **Type**: typing.Optional[str]

### ServiceAccessSecurityGroup
- **Type**: typing.Optional[str]

### AdditionalMasterSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### AdditionalSlaveSecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ErrorDetail

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorData
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]

### ErrorMessage
- **Type**: typing.Optional[str]


# ExecutionEngineConfig

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['EMR']]

### MasterInstanceSecurityGroupId
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]


# FailureDetails

### Reason
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### LogFile
- **Type**: typing.Optional[str]


# GetAutoTerminationPolicyInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAutoTerminationPolicyOutput

### AutoTerminationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.AutoTerminationPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# GetBlockPublicAccessConfigurationOutput

### BlockPublicAccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.BlockPublicAccessConfigurationOutput'>
- **Required**: Yes

### BlockPublicAccessConfigurationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.BlockPublicAccessConfigurationMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# GetClusterSessionCredentialsInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: typing.Optional[str]


# GetClusterSessionCredentialsOutput

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.Credentials'>
- **Required**: Yes

### ExpiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedScalingPolicyInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedScalingPolicyOutput

### ManagedScalingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ManagedScalingPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# GetStudioSessionMappingInput

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### IdentityId
- **Type**: typing.Optional[str]

### IdentityName
- **Type**: typing.Optional[str]


# GetStudioSessionMappingOutput

### SessionMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.SessionMappingDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# HadoopJarStepConfig

### Jar
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.KeyValue]]

### MainClass
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]


# HadoopJarStepConfigOutput

### Jar
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.KeyValue]]

### MainClass
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]


# HadoopStepConfig

### Jar
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### MainClass
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]


# Instance

### Id
- **Type**: typing.Optional[str]

### Ec2InstanceId
- **Type**: typing.Optional[str]

### PublicDnsName
- **Type**: typing.Optional[str]

### PublicIpAddress
- **Type**: typing.Optional[str]

### PrivateDnsName
- **Type**: typing.Optional[str]

### PrivateIpAddress
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceStatus]

### InstanceGroupId
- **Type**: typing.Optional[str]

### InstanceFleetId
- **Type**: typing.Optional[str]

### Market
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### InstanceType
- **Type**: typing.Optional[str]

### EbsVolumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.EbsVolume]]


# InstanceFleet

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetStatus]

### InstanceFleetType
- **Type**: typing.Optional[typing.Literal['CORE', 'MASTER', 'TASK']]

### TargetOnDemandCapacity
- **Type**: typing.Optional[int]

### TargetSpotCapacity
- **Type**: typing.Optional[int]

### ProvisionedOnDemandCapacity
- **Type**: typing.Optional[int]

### ProvisionedSpotCapacity
- **Type**: typing.Optional[int]

### InstanceTypeSpecifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceTypeSpecification]]

### LaunchSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetProvisioningSpecifications]

### ResizeSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetResizingSpecifications]

### Context
- **Type**: typing.Optional[str]


# InstanceFleetConfig

### InstanceFleetType
- **Type**: typing.Literal['CORE', 'MASTER', 'TASK']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### TargetOnDemandCapacity
- **Type**: typing.Optional[int]

### TargetSpotCapacity
- **Type**: typing.Optional[int]

### InstanceTypeConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceTypeConfig]]

### LaunchSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetProvisioningSpecifications]

### ResizeSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetResizingSpecifications]

### Context
- **Type**: typing.Optional[str]


# InstanceFleetModifyConfig

### InstanceFleetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetOnDemandCapacity
- **Type**: typing.Optional[int]

### TargetSpotCapacity
- **Type**: typing.Optional[int]

### ResizeSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetResizingSpecifications]

### InstanceTypeConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceTypeConfig]]

### Context
- **Type**: typing.Optional[str]


# InstanceFleetPaginator

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetStatus]

### InstanceFleetType
- **Type**: typing.Optional[typing.Literal['CORE', 'MASTER', 'TASK']]

### TargetOnDemandCapacity
- **Type**: typing.Optional[int]

### TargetSpotCapacity
- **Type**: typing.Optional[int]

### ProvisionedOnDemandCapacity
- **Type**: typing.Optional[int]

### ProvisionedSpotCapacity
- **Type**: typing.Optional[int]

### InstanceTypeSpecifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceTypeSpecificationPaginator]]

### LaunchSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetProvisioningSpecifications]

### ResizeSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetResizingSpecifications]

### Context
- **Type**: typing.Optional[str]


# InstanceFleetProvisioningSpecifications

### SpotSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.SpotProvisioningSpecification]

### OnDemandSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.OnDemandProvisioningSpecification]


# InstanceFleetResizingSpecifications

### SpotResizeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.SpotResizingSpecification]

### OnDemandResizeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.OnDemandResizingSpecification]


# InstanceFleetStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['CLUSTER_TERMINATED', 'INSTANCE_FAILURE', 'INTERNAL_ERROR', 'VALIDATION_ERROR']]

### Message
- **Type**: typing.Optional[str]


# InstanceFleetStatus

### State
- **Type**: typing.Optional[typing.Literal['BOOTSTRAPPING', 'PROVISIONING', 'RESIZING', 'RUNNING', 'SUSPENDED', 'TERMINATED', 'TERMINATING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetStateChangeReason]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetTimeline]


# InstanceFleetTimeline

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# InstanceGroup

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Market
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### InstanceGroupType
- **Type**: typing.Optional[typing.Literal['CORE', 'MASTER', 'TASK']]

### BidPrice
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### RequestedInstanceCount
- **Type**: typing.Optional[int]

### RunningInstanceCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupStatus]

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationOutput]]

### ConfigurationsVersion
- **Type**: typing.Optional[int]

### LastSuccessfullyAppliedConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationOutput]]

### LastSuccessfullyAppliedConfigurationsVersion
- **Type**: typing.Optional[int]

### EbsBlockDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.EbsBlockDevice]]

### EbsOptimized
- **Type**: typing.Optional[bool]

### ShrinkPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ShrinkPolicyOutput]

### AutoScalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.AutoScalingPolicyDescription]

### CustomAmiId
- **Type**: typing.Optional[str]


# InstanceGroupConfig

### InstanceRole
- **Type**: typing.Literal['CORE', 'MASTER', 'TASK']
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Market
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### BidPrice
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.Configuration, aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationOutput]]]

### EbsConfiguration
- **Type**: <class 'NoneType'>

### AutoScalingPolicy
- **Type**: <class 'NoneType'>

### CustomAmiId
- **Type**: typing.Optional[str]


# InstanceGroupDetail

### Market
- **Type**: typing.Literal['ON_DEMAND', 'SPOT']
- **Required**: Yes

### InstanceRole
- **Type**: typing.Literal['CORE', 'MASTER', 'TASK']
- **Required**: Yes

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceRequestCount
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceRunningCount
- **Type**: <class 'int'>
- **Required**: Yes

### State
- **Type**: typing.Literal['ARRESTED', 'BOOTSTRAPPING', 'ENDED', 'PROVISIONING', 'RECONFIGURING', 'RESIZING', 'RUNNING', 'SHUTTING_DOWN', 'SUSPENDED', 'TERMINATED', 'TERMINATING']
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InstanceGroupId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### BidPrice
- **Type**: typing.Optional[str]

### LastStateChangeReason
- **Type**: typing.Optional[str]

### StartDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]

### CustomAmiId
- **Type**: typing.Optional[str]


# InstanceGroupModifyConfig

### InstanceGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: typing.Optional[int]

### EC2InstanceIdsToTerminate
- **Type**: typing.Optional[typing.List[str]]

### ShrinkPolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.ShrinkPolicy, aws_resource_validator.pydantic_models.emr.emr_classes.ShrinkPolicyOutput, NoneType]

### ReconfigurationType
- **Type**: typing.Optional[typing.Literal['MERGE', 'OVERWRITE']]

### Configurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.Configuration, aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationOutput]]]


# InstanceGroupPaginator

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Market
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### InstanceGroupType
- **Type**: typing.Optional[typing.Literal['CORE', 'MASTER', 'TASK']]

### BidPrice
- **Type**: typing.Optional[str]

### InstanceType
- **Type**: typing.Optional[str]

### RequestedInstanceCount
- **Type**: typing.Optional[int]

### RunningInstanceCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupStatus]

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationPaginator]]

### ConfigurationsVersion
- **Type**: typing.Optional[int]

### LastSuccessfullyAppliedConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationPaginator]]

### LastSuccessfullyAppliedConfigurationsVersion
- **Type**: typing.Optional[int]

### EbsBlockDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.EbsBlockDevice]]

### EbsOptimized
- **Type**: typing.Optional[bool]

### ShrinkPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ShrinkPolicyOutput]

### AutoScalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.AutoScalingPolicyDescription]

### CustomAmiId
- **Type**: typing.Optional[str]


# InstanceGroupStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['CLUSTER_TERMINATED', 'INSTANCE_FAILURE', 'INTERNAL_ERROR', 'VALIDATION_ERROR']]

### Message
- **Type**: typing.Optional[str]


# InstanceGroupStatus

### State
- **Type**: typing.Optional[typing.Literal['ARRESTED', 'BOOTSTRAPPING', 'ENDED', 'PROVISIONING', 'RECONFIGURING', 'RESIZING', 'RUNNING', 'SHUTTING_DOWN', 'SUSPENDED', 'TERMINATED', 'TERMINATING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupStateChangeReason]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupTimeline]


# InstanceGroupTimeline

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# InstanceResizePolicy

### InstancesToTerminate
- **Type**: typing.Optional[typing.List[str]]

### InstancesToProtect
- **Type**: typing.Optional[typing.List[str]]

### InstanceTerminationTimeout
- **Type**: typing.Optional[int]


# InstanceResizePolicyOutput

### InstancesToTerminate
- **Type**: typing.Optional[typing.List[str]]

### InstancesToProtect
- **Type**: typing.Optional[typing.List[str]]

### InstanceTerminationTimeout
- **Type**: typing.Optional[int]


# InstanceStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['BOOTSTRAP_FAILURE', 'CLUSTER_TERMINATED', 'INSTANCE_FAILURE', 'INTERNAL_ERROR', 'VALIDATION_ERROR']]

### Message
- **Type**: typing.Optional[str]


# InstanceStatus

### State
- **Type**: typing.Optional[typing.Literal['AWAITING_FULFILLMENT', 'BOOTSTRAPPING', 'PROVISIONING', 'RUNNING', 'TERMINATED']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceStateChangeReason]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceTimeline]


# InstanceTimeline

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# InstanceTypeConfig

### InstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### WeightedCapacity
- **Type**: typing.Optional[int]

### BidPrice
- **Type**: typing.Optional[str]

### BidPriceAsPercentageOfOnDemandPrice
- **Type**: typing.Optional[float]

### EbsConfiguration
- **Type**: <class 'NoneType'>

### Configurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.Configuration, aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationOutput]]]

### CustomAmiId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[float]


# InstanceTypeSpecification

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[int]

### BidPrice
- **Type**: typing.Optional[str]

### BidPriceAsPercentageOfOnDemandPrice
- **Type**: typing.Optional[float]

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationOutput]]

### EbsBlockDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.EbsBlockDevice]]

### EbsOptimized
- **Type**: typing.Optional[bool]

### CustomAmiId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[float]


# InstanceTypeSpecificationPaginator

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[int]

### BidPrice
- **Type**: typing.Optional[str]

### BidPriceAsPercentageOfOnDemandPrice
- **Type**: typing.Optional[float]

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationPaginator]]

### EbsBlockDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.EbsBlockDevice]]

### EbsOptimized
- **Type**: typing.Optional[bool]

### CustomAmiId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[float]


# JobFlowDetail

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionStatusDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.JobFlowExecutionStatusDetail'>
- **Required**: Yes

### Instances
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.JobFlowInstancesDetail'>
- **Required**: Yes

### LogUri
- **Type**: typing.Optional[str]

### LogEncryptionKmsKeyId
- **Type**: typing.Optional[str]

### AmiVersion
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.StepDetail]]

### BootstrapActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.BootstrapActionDetail]]

### SupportedProducts
- **Type**: typing.Optional[typing.List[str]]

### VisibleToAllUsers
- **Type**: typing.Optional[bool]

### JobFlowRole
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### AutoScalingRole
- **Type**: typing.Optional[str]

### ScaleDownBehavior
- **Type**: typing.Optional[typing.Literal['TERMINATE_AT_INSTANCE_HOUR', 'TERMINATE_AT_TASK_COMPLETION']]


# JobFlowExecutionStatusDetail

### State
- **Type**: typing.Literal['BOOTSTRAPPING', 'COMPLETED', 'FAILED', 'RUNNING', 'SHUTTING_DOWN', 'STARTING', 'TERMINATED', 'WAITING']
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]

### LastStateChangeReason
- **Type**: typing.Optional[str]


# JobFlowInstancesConfig

### MasterInstanceType
- **Type**: typing.Optional[str]

### SlaveInstanceType
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### InstanceGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupConfig]]

### InstanceFleets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetConfig]]

### Ec2KeyName
- **Type**: typing.Optional[str]

### Placement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.PlacementType, aws_resource_validator.pydantic_models.emr.emr_classes.PlacementTypeOutput, NoneType]

### KeepJobFlowAliveWhenNoSteps
- **Type**: typing.Optional[bool]

### TerminationProtected
- **Type**: typing.Optional[bool]

### UnhealthyNodeReplacement
- **Type**: typing.Optional[bool]

### HadoopVersion
- **Type**: typing.Optional[str]

### Ec2SubnetId
- **Type**: typing.Optional[str]

### Ec2SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### EmrManagedMasterSecurityGroup
- **Type**: typing.Optional[str]

### EmrManagedSlaveSecurityGroup
- **Type**: typing.Optional[str]

### ServiceAccessSecurityGroup
- **Type**: typing.Optional[str]

### AdditionalMasterSecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### AdditionalSlaveSecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# JobFlowInstancesDetail

### MasterInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### SlaveInstanceType
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### MasterPublicDnsName
- **Type**: typing.Optional[str]

### MasterInstanceId
- **Type**: typing.Optional[str]

### InstanceGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupDetail]]

### NormalizedInstanceHours
- **Type**: typing.Optional[int]

### Ec2KeyName
- **Type**: typing.Optional[str]

### Ec2SubnetId
- **Type**: typing.Optional[str]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PlacementTypeOutput]

### KeepJobFlowAliveWhenNoSteps
- **Type**: typing.Optional[bool]

### TerminationProtected
- **Type**: typing.Optional[bool]

### UnhealthyNodeReplacement
- **Type**: typing.Optional[bool]

### HadoopVersion
- **Type**: typing.Optional[str]


# KerberosAttributes

### Realm
- **Type**: <class 'str'>
- **Required**: Yes

### KdcAdminPassword
- **Type**: <class 'str'>
- **Required**: Yes

### CrossRealmTrustPrincipalPassword
- **Type**: typing.Optional[str]

### ADDomainJoinUser
- **Type**: typing.Optional[str]

### ADDomainJoinPassword
- **Type**: typing.Optional[str]


# KeyValue

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ListBootstrapActionsInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListBootstrapActionsInputPaginate

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListBootstrapActionsOutput

### BootstrapActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Command]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListClustersInput

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ClusterStates
- **Type**: typing.Optional[typing.List[typing.Literal['BOOTSTRAPPING', 'RUNNING', 'STARTING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING', 'WAITING']]]

### Marker
- **Type**: typing.Optional[str]


# ListClustersInputPaginate

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ClusterStates
- **Type**: typing.Optional[typing.List[typing.Literal['BOOTSTRAPPING', 'RUNNING', 'STARTING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING', 'WAITING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListClustersOutput

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.ClusterSummary]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListInstanceFleetsInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListInstanceFleetsInputPaginate

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListInstanceFleetsOutput

### InstanceFleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleet]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListInstanceFleetsOutputPaginator

### InstanceFleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetPaginator]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListInstanceGroupsInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListInstanceGroupsInputPaginate

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListInstanceGroupsOutput

### InstanceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroup]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListInstanceGroupsOutputPaginator

### InstanceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupPaginator]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListInstancesInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: typing.Optional[str]

### InstanceGroupTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CORE', 'MASTER', 'TASK']]]

### InstanceFleetId
- **Type**: typing.Optional[str]

### InstanceFleetType
- **Type**: typing.Optional[typing.Literal['CORE', 'MASTER', 'TASK']]

### InstanceStates
- **Type**: typing.Optional[typing.List[typing.Literal['AWAITING_FULFILLMENT', 'BOOTSTRAPPING', 'PROVISIONING', 'RUNNING', 'TERMINATED']]]

### Marker
- **Type**: typing.Optional[str]


# ListInstancesInputPaginate

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: typing.Optional[str]

### InstanceGroupTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CORE', 'MASTER', 'TASK']]]

### InstanceFleetId
- **Type**: typing.Optional[str]

### InstanceFleetType
- **Type**: typing.Optional[typing.Literal['CORE', 'MASTER', 'TASK']]

### InstanceStates
- **Type**: typing.Optional[typing.List[typing.Literal['AWAITING_FULFILLMENT', 'BOOTSTRAPPING', 'PROVISIONING', 'RUNNING', 'TERMINATED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListInstancesOutput

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Instance]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListNotebookExecutionsInput

### EditorId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAILING', 'FINISHED', 'FINISHING', 'RUNNING', 'STARTING', 'START_PENDING', 'STOPPED', 'STOPPING', 'STOP_PENDING']]

### From
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### To
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Marker
- **Type**: typing.Optional[str]

### ExecutionEngineId
- **Type**: typing.Optional[str]


# ListNotebookExecutionsInputPaginate

### EditorId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAILING', 'FINISHED', 'FINISHING', 'RUNNING', 'STARTING', 'START_PENDING', 'STOPPED', 'STOPPING', 'STOP_PENDING']]

### From
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### To
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ExecutionEngineId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListNotebookExecutionsOutput

### NotebookExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.NotebookExecutionSummary]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListReleaseLabelsInput

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ReleaseLabelFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReleaseLabelsOutput

### ReleaseLabels
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsInput

### Marker
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListSecurityConfigurationsOutput

### SecurityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.SecurityConfigurationSummary]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListStepsInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepStates
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'INTERRUPTED', 'PENDING', 'RUNNING']]]

### StepIds
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]


# ListStepsInputPaginate

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepStates
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'INTERRUPTED', 'PENDING', 'RUNNING']]]

### StepIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListStepsOutput

### Steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.StepSummary]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListStudioSessionMappingsInput

### StudioId
- **Type**: typing.Optional[str]

### IdentityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### Marker
- **Type**: typing.Optional[str]


# ListStudioSessionMappingsInputPaginate

### StudioId
- **Type**: typing.Optional[str]

### IdentityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListStudioSessionMappingsOutput

### SessionMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.SessionMappingSummary]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListStudiosInput

### Marker
- **Type**: typing.Optional[str]


# ListStudiosInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.PaginatorConfig]


# ListStudiosOutput

### Studios
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.StudioSummary]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ListSupportedInstanceTypesInput

### ReleaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListSupportedInstanceTypesOutput

### SupportedInstanceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.SupportedInstanceType]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ManagedScalingPolicy

### ComputeLimits
- **Type**: <class 'NoneType'>

### UtilizationPerformanceIndex
- **Type**: typing.Optional[int]

### ScalingStrategy
- **Type**: typing.Optional[typing.Literal['ADVANCED', 'DEFAULT']]


# MetricDimension

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ModifyClusterInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepConcurrencyLevel
- **Type**: typing.Optional[int]


# ModifyClusterOutput

### StepConcurrencyLevel
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyInstanceFleetInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceFleet
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.InstanceFleetModifyConfig'>
- **Required**: Yes


# ModifyInstanceGroupsInput

### ClusterId
- **Type**: typing.Optional[str]

### InstanceGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceGroupModifyConfig]]


# NotebookExecution

### NotebookExecutionId
- **Type**: typing.Optional[str]

### EditorId
- **Type**: typing.Optional[str]

### ExecutionEngine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.ExecutionEngineConfig]

### NotebookExecutionName
- **Type**: typing.Optional[str]

### NotebookParams
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAILING', 'FINISHED', 'FINISHING', 'RUNNING', 'STARTING', 'START_PENDING', 'STOPPED', 'STOPPING', 'STOP_PENDING']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Arn
- **Type**: typing.Optional[str]

### OutputNotebookURI
- **Type**: typing.Optional[str]

### LastStateChangeReason
- **Type**: typing.Optional[str]

### NotebookInstanceSecurityGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Tag]]

### NotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.NotebookS3LocationForOutput]

### OutputNotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.OutputNotebookS3LocationForOutput]

### OutputNotebookFormat
- **Type**: typing.Optional[typing.Literal['HTML']]

### EnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# NotebookExecutionSummary

### NotebookExecutionId
- **Type**: typing.Optional[str]

### EditorId
- **Type**: typing.Optional[str]

### NotebookExecutionName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'FAILING', 'FINISHED', 'FINISHING', 'RUNNING', 'STARTING', 'START_PENDING', 'STOPPED', 'STOPPING', 'STOP_PENDING']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### NotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.NotebookS3LocationForOutput]

### ExecutionEngineId
- **Type**: typing.Optional[str]


# NotebookS3LocationForOutput

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# NotebookS3LocationFromInput

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# OSRelease

### Label
- **Type**: typing.Optional[str]


# OnDemandCapacityReservationOptions

### UsageStrategy
- **Type**: typing.Optional[typing.Literal['use-capacity-reservations-first']]

### CapacityReservationPreference
- **Type**: typing.Optional[typing.Literal['none', 'open']]

### CapacityReservationResourceGroupArn
- **Type**: typing.Optional[str]


# OnDemandProvisioningSpecification

### AllocationStrategy
- **Type**: typing.Literal['lowest-price', 'prioritized']
- **Required**: Yes

### CapacityReservationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.OnDemandCapacityReservationOptions]


# OnDemandResizingSpecification

### TimeoutDurationMinutes
- **Type**: typing.Optional[int]

### AllocationStrategy
- **Type**: typing.Optional[typing.Literal['lowest-price', 'prioritized']]

### CapacityReservationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.OnDemandCapacityReservationOptions]


# OutputNotebookS3LocationForOutput

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# OutputNotebookS3LocationFromInput

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacementGroupConfig

### InstanceRole
- **Type**: typing.Literal['CORE', 'MASTER', 'TASK']
- **Required**: Yes

### PlacementStrategy
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'NONE', 'PARTITION', 'SPREAD']]


# PlacementType

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]


# PlacementTypeOutput

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]


# PortRange

### MinRange
- **Type**: <class 'int'>
- **Required**: Yes

### MaxRange
- **Type**: typing.Optional[int]


# PutAutoScalingPolicyInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.AutoScalingPolicy'>
- **Required**: Yes


# PutAutoScalingPolicyOutput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.AutoScalingPolicyDescription'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# PutAutoTerminationPolicyInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoTerminationPolicy
- **Type**: <class 'NoneType'>


# PutBlockPublicAccessConfigurationInput

### BlockPublicAccessConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.BlockPublicAccessConfiguration, aws_resource_validator.pydantic_models.emr.emr_classes.BlockPublicAccessConfigurationOutput]
- **Required**: Yes


# PutManagedScalingPolicyInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedScalingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ManagedScalingPolicy'>
- **Required**: Yes


# ReleaseLabelFilter

### Prefix
- **Type**: typing.Optional[str]

### Application
- **Type**: typing.Optional[str]


# RemoveAutoScalingPolicyInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveAutoTerminationPolicyInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveManagedScalingPolicyInput

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsInput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
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


# RunJobFlowInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.JobFlowInstancesConfig'>
- **Required**: Yes

### LogUri
- **Type**: typing.Optional[str]

### LogEncryptionKmsKeyId
- **Type**: typing.Optional[str]

### AdditionalInfo
- **Type**: typing.Optional[str]

### AmiVersion
- **Type**: typing.Optional[str]

### ReleaseLabel
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.StepConfig, aws_resource_validator.pydantic_models.emr.emr_classes.StepConfigOutput]]]

### BootstrapActions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.BootstrapActionConfig, aws_resource_validator.pydantic_models.emr.emr_classes.BootstrapActionConfigOutput]]]

### SupportedProducts
- **Type**: typing.Optional[typing.List[str]]

### NewSupportedProducts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.SupportedProductConfig]]

### Applications
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.Application, aws_resource_validator.pydantic_models.emr.emr_classes.ApplicationOutput]]]

### Configurations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.Configuration, aws_resource_validator.pydantic_models.emr.emr_classes.ConfigurationOutput]]]

### VisibleToAllUsers
- **Type**: typing.Optional[bool]

### JobFlowRole
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Tag]]

### SecurityConfiguration
- **Type**: typing.Optional[str]

### AutoScalingRole
- **Type**: typing.Optional[str]

### ScaleDownBehavior
- **Type**: typing.Optional[typing.Literal['TERMINATE_AT_INSTANCE_HOUR', 'TERMINATE_AT_TASK_COMPLETION']]

### CustomAmiId
- **Type**: typing.Optional[str]

### EbsRootVolumeSize
- **Type**: typing.Optional[int]

### RepoUpgradeOnBoot
- **Type**: typing.Optional[typing.Literal['NONE', 'SECURITY']]

### KerberosAttributes
- **Type**: <class 'NoneType'>

### StepConcurrencyLevel
- **Type**: typing.Optional[int]

### ManagedScalingPolicy
- **Type**: <class 'NoneType'>

### PlacementGroupConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.PlacementGroupConfig]]

### AutoTerminationPolicy
- **Type**: <class 'NoneType'>

### OSReleaseLabel
- **Type**: typing.Optional[str]

### EbsRootVolumeIops
- **Type**: typing.Optional[int]

### EbsRootVolumeThroughput
- **Type**: typing.Optional[int]


# RunJobFlowOutput

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# ScalingAction

### SimpleScalingPolicyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.SimpleScalingPolicyConfiguration'>
- **Required**: Yes

### Market
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]


# ScalingConstraints

### MinCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### MaxCapacity
- **Type**: <class 'int'>
- **Required**: Yes


# ScalingRule

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ScalingAction'>
- **Required**: Yes

### Trigger
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.ScalingTrigger, aws_resource_validator.pydantic_models.emr.emr_classes.ScalingTriggerOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ScalingRuleOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ScalingAction'>
- **Required**: Yes

### Trigger
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ScalingTriggerOutput'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ScalingTrigger

### CloudWatchAlarmDefinition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.CloudWatchAlarmDefinition, aws_resource_validator.pydantic_models.emr.emr_classes.CloudWatchAlarmDefinitionOutput]
- **Required**: Yes


# ScalingTriggerOutput

### CloudWatchAlarmDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.CloudWatchAlarmDefinitionOutput'>
- **Required**: Yes


# ScriptBootstrapActionConfig

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Args
- **Type**: typing.Optional[typing.List[str]]


# ScriptBootstrapActionConfigOutput

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Args
- **Type**: typing.Optional[typing.List[str]]


# SecurityConfigurationSummary

### Name
- **Type**: typing.Optional[str]

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]


# SessionMappingDetail

### StudioId
- **Type**: typing.Optional[str]

### IdentityId
- **Type**: typing.Optional[str]

### IdentityName
- **Type**: typing.Optional[str]

### IdentityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### SessionPolicyArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# SessionMappingSummary

### StudioId
- **Type**: typing.Optional[str]

### IdentityId
- **Type**: typing.Optional[str]

### IdentityName
- **Type**: typing.Optional[str]

### IdentityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### SessionPolicyArn
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# SetKeepJobFlowAliveWhenNoStepsInput

### JobFlowIds
- **Type**: typing.List[str]
- **Required**: Yes

### KeepJobFlowAliveWhenNoSteps
- **Type**: <class 'bool'>
- **Required**: Yes


# SetTerminationProtectionInput

### JobFlowIds
- **Type**: typing.List[str]
- **Required**: Yes

### TerminationProtected
- **Type**: <class 'bool'>
- **Required**: Yes


# SetUnhealthyNodeReplacementInput

### JobFlowIds
- **Type**: typing.List[str]
- **Required**: Yes

### UnhealthyNodeReplacement
- **Type**: <class 'bool'>
- **Required**: Yes


# SetVisibleToAllUsersInput

### JobFlowIds
- **Type**: typing.List[str]
- **Required**: Yes

### VisibleToAllUsers
- **Type**: <class 'bool'>
- **Required**: Yes


# ShrinkPolicy

### DecommissionTimeout
- **Type**: typing.Optional[int]

### InstanceResizePolicy
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceResizePolicy, aws_resource_validator.pydantic_models.emr.emr_classes.InstanceResizePolicyOutput, NoneType]


# ShrinkPolicyOutput

### DecommissionTimeout
- **Type**: typing.Optional[int]

### InstanceResizePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.InstanceResizePolicyOutput]


# SimpleScalingPolicyConfiguration

### ScalingAdjustment
- **Type**: <class 'int'>
- **Required**: Yes

### AdjustmentType
- **Type**: typing.Optional[typing.Literal['CHANGE_IN_CAPACITY', 'EXACT_CAPACITY', 'PERCENT_CHANGE_IN_CAPACITY']]

### CoolDown
- **Type**: typing.Optional[int]


# SimplifiedApplication

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# SpotProvisioningSpecification

### TimeoutDurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### TimeoutAction
- **Type**: typing.Literal['SWITCH_TO_ON_DEMAND', 'TERMINATE_CLUSTER']
- **Required**: Yes

### BlockDurationMinutes
- **Type**: typing.Optional[int]

### AllocationStrategy
- **Type**: typing.Optional[typing.Literal['capacity-optimized', 'capacity-optimized-prioritized', 'diversified', 'lowest-price', 'price-capacity-optimized']]


# SpotResizingSpecification

### TimeoutDurationMinutes
- **Type**: typing.Optional[int]

### AllocationStrategy
- **Type**: typing.Optional[typing.Literal['capacity-optimized', 'capacity-optimized-prioritized', 'diversified', 'lowest-price', 'price-capacity-optimized']]


# StartNotebookExecutionInput

### ExecutionEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ExecutionEngineConfig'>
- **Required**: Yes

### ServiceRole
- **Type**: <class 'str'>
- **Required**: Yes

### EditorId
- **Type**: typing.Optional[str]

### RelativePath
- **Type**: typing.Optional[str]

### NotebookExecutionName
- **Type**: typing.Optional[str]

### NotebookParams
- **Type**: typing.Optional[str]

### NotebookInstanceSecurityGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Tag]]

### NotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.NotebookS3LocationFromInput]

### OutputNotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.OutputNotebookS3LocationFromInput]

### OutputNotebookFormat
- **Type**: typing.Optional[typing.Literal['HTML']]

### EnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartNotebookExecutionOutput

### NotebookExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.ResponseMetadata'>
- **Required**: Yes


# Step

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.HadoopStepConfig]

### ActionOnFailure
- **Type**: typing.Optional[typing.Literal['CANCEL_AND_WAIT', 'CONTINUE', 'TERMINATE_CLUSTER', 'TERMINATE_JOB_FLOW']]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.StepStatus]

### ExecutionRoleArn
- **Type**: typing.Optional[str]


# StepConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HadoopJarStep
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr.emr_classes.HadoopJarStepConfig, aws_resource_validator.pydantic_models.emr.emr_classes.HadoopJarStepConfigOutput]
- **Required**: Yes

### ActionOnFailure
- **Type**: typing.Optional[typing.Literal['CANCEL_AND_WAIT', 'CONTINUE', 'TERMINATE_CLUSTER', 'TERMINATE_JOB_FLOW']]


# StepConfigOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HadoopJarStep
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.HadoopJarStepConfigOutput'>
- **Required**: Yes

### ActionOnFailure
- **Type**: typing.Optional[typing.Literal['CANCEL_AND_WAIT', 'CONTINUE', 'TERMINATE_CLUSTER', 'TERMINATE_JOB_FLOW']]


# StepDetail

### StepConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.StepConfigOutput'>
- **Required**: Yes

### ExecutionStatusDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.emr.emr_classes.StepExecutionStatusDetail'>
- **Required**: Yes


# StepExecutionStatusDetail

### State
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'CONTINUE', 'FAILED', 'INTERRUPTED', 'PENDING', 'RUNNING']
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]

### LastStateChangeReason
- **Type**: typing.Optional[str]


# StepStateChangeReason

### Code
- **Type**: typing.Optional[typing.Literal['NONE']]

### Message
- **Type**: typing.Optional[str]


# StepStatus

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'INTERRUPTED', 'PENDING', 'RUNNING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.StepStateChangeReason]

### FailureDetails
- **Type**: <class 'NoneType'>

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.StepTimeline]


# StepSummary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.HadoopStepConfig]

### ActionOnFailure
- **Type**: typing.Optional[typing.Literal['CANCEL_AND_WAIT', 'CONTINUE', 'TERMINATE_CLUSTER', 'TERMINATE_JOB_FLOW']]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr.emr_classes.StepStatus]


# StepTimeline

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### StartDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# StopNotebookExecutionInput

### NotebookExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# Studio

### StudioId
- **Type**: typing.Optional[str]

### StudioArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### AuthMode
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### ServiceRole
- **Type**: typing.Optional[str]

### UserRole
- **Type**: typing.Optional[str]

### WorkspaceSecurityGroupId
- **Type**: typing.Optional[str]

### EngineSecurityGroupId
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### DefaultS3Location
- **Type**: typing.Optional[str]

### IdpAuthUrl
- **Type**: typing.Optional[str]

### IdpRelayStateParameterName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr.emr_classes.Tag]]

### IdcInstanceArn
- **Type**: typing.Optional[str]

### TrustedIdentityPropagationEnabled
- **Type**: typing.Optional[bool]

### IdcUserAssignment
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRED']]

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# StudioSummary

### StudioId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### AuthMode
- **Type**: typing.Optional[typing.Literal['IAM', 'SSO']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]


# SupportedInstanceType

### Type
- **Type**: typing.Optional[str]

### MemoryGB
- **Type**: typing.Optional[float]

### StorageGB
- **Type**: typing.Optional[int]

### VCPU
- **Type**: typing.Optional[int]

### Is64BitsOnly
- **Type**: typing.Optional[bool]

### InstanceFamilyId
- **Type**: typing.Optional[str]

### EbsOptimizedAvailable
- **Type**: typing.Optional[bool]

### EbsOptimizedByDefault
- **Type**: typing.Optional[bool]

### NumberOfDisks
- **Type**: typing.Optional[int]

### EbsStorageOnly
- **Type**: typing.Optional[bool]

### Architecture
- **Type**: typing.Optional[str]


# SupportedProductConfig

### Name
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TerminateJobFlowsInput

### JobFlowIds
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateStudioInput

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### DefaultS3Location
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# UpdateStudioSessionMappingInput

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### SessionPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityId
- **Type**: typing.Optional[str]

### IdentityName
- **Type**: typing.Optional[str]


# UsernamePassword

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# VolumeSpecification

### VolumeType
- **Type**: <class 'str'>
- **Required**: Yes

### SizeInGB
- **Type**: <class 'int'>
- **Required**: Yes

### Iops
- **Type**: typing.Optional[int]

### Throughput
- **Type**: typing.Optional[int]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



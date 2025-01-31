# emr_classes

# AddInstanceFleetInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceFleet
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.InstanceFleetConfigTypeDef'>
- **Required**: Yes


# AddInstanceFleetOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddInstanceGroupsInputRequestTypeDef

### InstanceGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.InstanceGroupConfigTypeDef]
- **Required**: Yes

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes


# AddInstanceGroupsOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddJobFlowStepsInputRequestTypeDef

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Steps
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.emr_classes.StepConfigTypeDef, aws_resource_validator.pydantic_models.emr_classes.StepConfigOutputTypeDef]]
- **Required**: Yes

### ExecutionRoleArn
- **Type**: typing.Optional[str]


# AddJobFlowStepsOutputTypeDef

### StepIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddTagsInputRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.TagTypeDef]
- **Required**: Yes


# ApplicationOutputTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]

### AdditionalInfo
- **Type**: typing.Optional[typing.Dict[str, str]]


# ApplicationTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.Sequence[str]]

### AdditionalInfo
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AutoScalingPolicyDescriptionTypeDef

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.AutoScalingPolicyStatusTypeDef]

### Constraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ScalingConstraintsTypeDef]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.ScalingRuleOutputTypeDef]]


# AutoScalingPolicyStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['CLEANUP_FAILURE', 'PROVISION_FAILURE', 'USER_REQUEST']]

### Message
- **Type**: typing.Optional[str]


# AutoScalingPolicyStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['ATTACHED', 'ATTACHING', 'DETACHED', 'DETACHING', 'FAILED', 'PENDING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.AutoScalingPolicyStateChangeReasonTypeDef]


# AutoScalingPolicyTypeDef

### Constraints
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ScalingConstraintsTypeDef'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.ScalingRuleTypeDef]
- **Required**: Yes


# AutoTerminationPolicyTypeDef

### IdleTimeout
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockPublicAccessConfigurationMetadataTypeDef

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedByArn
- **Type**: <class 'str'>
- **Required**: Yes


# BlockPublicAccessConfigurationOutputTypeDef

### BlockPublicSecurityGroupRules
- **Type**: <class 'bool'>
- **Required**: Yes

### PermittedPublicSecurityGroupRuleRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.PortRangeTypeDef]]


# BlockPublicAccessConfigurationTypeDef

### BlockPublicSecurityGroupRules
- **Type**: <class 'bool'>
- **Required**: Yes

### PermittedPublicSecurityGroupRuleRanges
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.PortRangeTypeDef]]


# BootstrapActionConfigOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScriptBootstrapAction
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ScriptBootstrapActionConfigOutputTypeDef'>
- **Required**: Yes


# BootstrapActionConfigTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ScriptBootstrapAction
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ScriptBootstrapActionConfigTypeDef'>
- **Required**: Yes


# BootstrapActionDetailTypeDef

### BootstrapActionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.BootstrapActionConfigOutputTypeDef]


# CancelStepsInfoTypeDef

### StepId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'SUBMITTED']]

### Reason
- **Type**: typing.Optional[str]


# CancelStepsInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StepCancellationOption
- **Type**: typing.Optional[typing.Literal['SEND_INTERRUPT', 'TERMINATE_PROCESS']]


# CancelStepsOutputTypeDef

### CancelStepsInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.CancelStepsInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudWatchAlarmDefinitionOutputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.MetricDimensionTypeDef]]


# CloudWatchAlarmDefinitionTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.MetricDimensionTypeDef]]


# ClusterStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['ALL_STEPS_COMPLETED', 'BOOTSTRAP_FAILURE', 'INSTANCE_FAILURE', 'INSTANCE_FLEET_TIMEOUT', 'INTERNAL_ERROR', 'STEP_FAILURE', 'USER_REQUEST', 'VALIDATION_ERROR']]

### Message
- **Type**: typing.Optional[str]


# ClusterStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['BOOTSTRAPPING', 'RUNNING', 'STARTING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING', 'WAITING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ClusterStateChangeReasonTypeDef]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ClusterTimelineTypeDef]

### ErrorDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.ErrorDetailTypeDef]]


# ClusterSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ClusterStatusTypeDef]

### NormalizedInstanceHours
- **Type**: typing.Optional[int]

### ClusterArn
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]


# ClusterTimelineTypeDef

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# ClusterTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ClusterStatusTypeDef]

### Ec2InstanceAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.Ec2InstanceAttributesTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.ApplicationOutputTypeDef]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.TagTypeDef]]

### ServiceRole
- **Type**: typing.Optional[str]

### NormalizedInstanceHours
- **Type**: typing.Optional[int]

### MasterPublicDnsName
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.ConfigurationOutputTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.KerberosAttributesTypeDef]

### ClusterArn
- **Type**: typing.Optional[str]

### OutpostArn
- **Type**: typing.Optional[str]

### StepConcurrencyLevel
- **Type**: typing.Optional[int]

### PlacementGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.PlacementGroupConfigTypeDef]]

### OSReleaseLabel
- **Type**: typing.Optional[str]

### EbsRootVolumeIops
- **Type**: typing.Optional[int]

### EbsRootVolumeThroughput
- **Type**: typing.Optional[int]


# CommandTypeDef

### Name
- **Type**: typing.Optional[str]

### ScriptPath
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]


# ComputeLimitsTypeDef

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


# ConfigurationExtraOutputTypeDef

### Classification
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConfigurationOutputTypeDef

### Classification
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConfigurationTypeDef

### Classification
- **Type**: typing.Optional[str]

### Configurations
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### Properties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSecurityConfigurationInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityConfiguration
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSecurityConfigurationOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreationDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStudioInputRequestTypeDef

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
- **Type**: typing.Sequence[str]
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.TagTypeDef]]

### TrustedIdentityPropagationEnabled
- **Type**: typing.Optional[bool]

### IdcUserAssignment
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRED']]

### IdcInstanceArn
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# CreateStudioOutputTypeDef

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStudioSessionMappingInputRequestTypeDef

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


# CredentialsTypeDef

### UsernamePassword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.UsernamePasswordTypeDef]


# DeleteSecurityConfigurationInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStudioInputRequestTypeDef

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStudioSessionMappingInputRequestTypeDef

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


# DescribeClusterInputClusterRunningWaitTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.WaiterConfigTypeDef]


# DescribeClusterInputClusterTerminatedWaitTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.WaiterConfigTypeDef]


# DescribeClusterInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterOutputTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeJobFlowsInputRequestTypeDef

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### JobFlowIds
- **Type**: typing.Optional[typing.Sequence[str]]

### JobFlowStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOOTSTRAPPING', 'COMPLETED', 'FAILED', 'RUNNING', 'SHUTTING_DOWN', 'STARTING', 'TERMINATED', 'WAITING']]]


# DescribeJobFlowsOutputTypeDef

### JobFlows
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.JobFlowDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNotebookExecutionInputRequestTypeDef

### NotebookExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNotebookExecutionOutputTypeDef

### NotebookExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.NotebookExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReleaseLabelInputRequestTypeDef

### ReleaseLabel
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeReleaseLabelOutputTypeDef

### ReleaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.SimplifiedApplicationTypeDef]
- **Required**: Yes

### AvailableOSReleases
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.OSReleaseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSecurityConfigurationInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSecurityConfigurationOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStepInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStepInputStepCompleteWaitTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.WaiterConfigTypeDef]


# DescribeStepOutputTypeDef

### Step
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.StepTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStudioInputRequestTypeDef

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStudioOutputTypeDef

### Studio
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.StudioTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EbsBlockDeviceConfigTypeDef

### VolumeSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.VolumeSpecificationTypeDef'>
- **Required**: Yes

### VolumesPerInstance
- **Type**: typing.Optional[int]


# EbsBlockDeviceTypeDef

### VolumeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.VolumeSpecificationTypeDef]

### Device
- **Type**: typing.Optional[str]


# EbsConfigurationTypeDef

### EbsBlockDeviceConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.EbsBlockDeviceConfigTypeDef]]

### EbsOptimized
- **Type**: typing.Optional[bool]


# EbsVolumeTypeDef

### Device
- **Type**: typing.Optional[str]

### VolumeId
- **Type**: typing.Optional[str]


# Ec2InstanceAttributesTypeDef

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


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ErrorDetailTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorData
- **Type**: typing.Optional[typing.List[typing.Dict[str, str]]]

### ErrorMessage
- **Type**: typing.Optional[str]


# ExecutionEngineConfigTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['EMR']]

### MasterInstanceSecurityGroupId
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]


# FailureDetailsTypeDef

### Reason
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### LogFile
- **Type**: typing.Optional[str]


# GetAutoTerminationPolicyInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAutoTerminationPolicyOutputTypeDef

### AutoTerminationPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.AutoTerminationPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBlockPublicAccessConfigurationOutputTypeDef

### BlockPublicAccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.BlockPublicAccessConfigurationOutputTypeDef'>
- **Required**: Yes

### BlockPublicAccessConfigurationMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.BlockPublicAccessConfigurationMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetClusterSessionCredentialsInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: typing.Optional[str]


# GetClusterSessionCredentialsOutputTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.CredentialsTypeDef'>
- **Required**: Yes

### ExpiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetManagedScalingPolicyInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedScalingPolicyOutputTypeDef

### ManagedScalingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ManagedScalingPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStudioSessionMappingInputRequestTypeDef

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


# GetStudioSessionMappingOutputTypeDef

### SessionMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.SessionMappingDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HadoopJarStepConfigOutputTypeDef

### Jar
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.KeyValueTypeDef]]

### MainClass
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]


# HadoopJarStepConfigTypeDef

### Jar
- **Type**: <class 'str'>
- **Required**: Yes

### Properties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.KeyValueTypeDef]]

### MainClass
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.Sequence[str]]


# HadoopStepConfigTypeDef

### Jar
- **Type**: typing.Optional[str]

### Properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### MainClass
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.List[str]]


# InstanceFleetConfigTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.InstanceTypeConfigTypeDef]]

### LaunchSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetProvisioningSpecificationsTypeDef]

### ResizeSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetResizingSpecificationsTypeDef]


# InstanceFleetModifyConfigTypeDef

### InstanceFleetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetOnDemandCapacity
- **Type**: typing.Optional[int]

### TargetSpotCapacity
- **Type**: typing.Optional[int]

### ResizeSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetResizingSpecificationsTypeDef]


# InstanceFleetProvisioningSpecificationsTypeDef

### SpotSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.SpotProvisioningSpecificationTypeDef]

### OnDemandSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.OnDemandProvisioningSpecificationTypeDef]


# InstanceFleetResizingSpecificationsTypeDef

### SpotResizeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.SpotResizingSpecificationTypeDef]

### OnDemandResizeSpecification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.OnDemandResizingSpecificationTypeDef]


# InstanceFleetStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['CLUSTER_TERMINATED', 'INSTANCE_FAILURE', 'INTERNAL_ERROR', 'VALIDATION_ERROR']]

### Message
- **Type**: typing.Optional[str]


# InstanceFleetStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['BOOTSTRAPPING', 'PROVISIONING', 'RESIZING', 'RUNNING', 'SUSPENDED', 'TERMINATED', 'TERMINATING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetStateChangeReasonTypeDef]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetTimelineTypeDef]


# InstanceFleetTimelineTypeDef

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# InstanceFleetTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetStatusTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.InstanceTypeSpecificationTypeDef]]

### LaunchSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetProvisioningSpecificationsTypeDef]

### ResizeSpecifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetResizingSpecificationsTypeDef]


# InstanceGroupConfigTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.ConfigurationTypeDef]]

### EbsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.EbsConfigurationTypeDef]

### AutoScalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.AutoScalingPolicyTypeDef]

### CustomAmiId
- **Type**: typing.Optional[str]


# InstanceGroupDetailTypeDef

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


# InstanceGroupModifyConfigTypeDef

### InstanceGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceCount
- **Type**: typing.Optional[int]

### EC2InstanceIdsToTerminate
- **Type**: typing.Optional[typing.Sequence[str]]

### ShrinkPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ShrinkPolicyTypeDef]

### ReconfigurationType
- **Type**: typing.Optional[typing.Literal['MERGE', 'OVERWRITE']]

### Configurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.ConfigurationTypeDef]]


# InstanceGroupStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['CLUSTER_TERMINATED', 'INSTANCE_FAILURE', 'INTERNAL_ERROR', 'VALIDATION_ERROR']]

### Message
- **Type**: typing.Optional[str]


# InstanceGroupStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['ARRESTED', 'BOOTSTRAPPING', 'ENDED', 'PROVISIONING', 'RECONFIGURING', 'RESIZING', 'RUNNING', 'SHUTTING_DOWN', 'SUSPENDED', 'TERMINATED', 'TERMINATING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceGroupStateChangeReasonTypeDef]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceGroupTimelineTypeDef]


# InstanceGroupTimelineTypeDef

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# InstanceGroupTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceGroupStatusTypeDef]

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.ConfigurationOutputTypeDef]]

### ConfigurationsVersion
- **Type**: typing.Optional[int]

### LastSuccessfullyAppliedConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.ConfigurationOutputTypeDef]]

### LastSuccessfullyAppliedConfigurationsVersion
- **Type**: typing.Optional[int]

### EbsBlockDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.EbsBlockDeviceTypeDef]]

### EbsOptimized
- **Type**: typing.Optional[bool]

### ShrinkPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ShrinkPolicyOutputTypeDef]

### AutoScalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.AutoScalingPolicyDescriptionTypeDef]

### CustomAmiId
- **Type**: typing.Optional[str]


# InstanceResizePolicyOutputTypeDef

### InstancesToTerminate
- **Type**: typing.Optional[typing.List[str]]

### InstancesToProtect
- **Type**: typing.Optional[typing.List[str]]

### InstanceTerminationTimeout
- **Type**: typing.Optional[int]


# InstanceResizePolicyTypeDef

### InstancesToTerminate
- **Type**: typing.Optional[typing.Sequence[str]]

### InstancesToProtect
- **Type**: typing.Optional[typing.Sequence[str]]

### InstanceTerminationTimeout
- **Type**: typing.Optional[int]


# InstanceStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['BOOTSTRAP_FAILURE', 'CLUSTER_TERMINATED', 'INSTANCE_FAILURE', 'INTERNAL_ERROR', 'VALIDATION_ERROR']]

### Message
- **Type**: typing.Optional[str]


# InstanceStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['AWAITING_FULFILLMENT', 'BOOTSTRAPPING', 'PROVISIONING', 'RUNNING', 'TERMINATED']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceStateChangeReasonTypeDef]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceTimelineTypeDef]


# InstanceTimelineTypeDef

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### ReadyDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# InstanceTypeConfigTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.EbsConfigurationTypeDef]

### Configurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.ConfigurationTypeDef]]

### CustomAmiId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[float]


# InstanceTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceStatusTypeDef]

### InstanceGroupId
- **Type**: typing.Optional[str]

### InstanceFleetId
- **Type**: typing.Optional[str]

### Market
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]

### InstanceType
- **Type**: typing.Optional[str]

### EbsVolumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.EbsVolumeTypeDef]]


# InstanceTypeSpecificationTypeDef

### InstanceType
- **Type**: typing.Optional[str]

### WeightedCapacity
- **Type**: typing.Optional[int]

### BidPrice
- **Type**: typing.Optional[str]

### BidPriceAsPercentageOfOnDemandPrice
- **Type**: typing.Optional[float]

### Configurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.ConfigurationOutputTypeDef]]

### EbsBlockDevices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.EbsBlockDeviceTypeDef]]

### EbsOptimized
- **Type**: typing.Optional[bool]

### CustomAmiId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[float]


# JobFlowDetailTypeDef

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionStatusDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.JobFlowExecutionStatusDetailTypeDef'>
- **Required**: Yes

### Instances
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.JobFlowInstancesDetailTypeDef'>
- **Required**: Yes

### LogUri
- **Type**: typing.Optional[str]

### LogEncryptionKmsKeyId
- **Type**: typing.Optional[str]

### AmiVersion
- **Type**: typing.Optional[str]

### Steps
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.StepDetailTypeDef]]

### BootstrapActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.BootstrapActionDetailTypeDef]]

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


# JobFlowExecutionStatusDetailTypeDef

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


# JobFlowInstancesConfigTypeDef

### MasterInstanceType
- **Type**: typing.Optional[str]

### SlaveInstanceType
- **Type**: typing.Optional[str]

### InstanceCount
- **Type**: typing.Optional[int]

### InstanceGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.InstanceGroupConfigTypeDef]]

### InstanceFleets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetConfigTypeDef]]

### Ec2KeyName
- **Type**: typing.Optional[str]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PlacementTypeTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[str]]

### EmrManagedMasterSecurityGroup
- **Type**: typing.Optional[str]

### EmrManagedSlaveSecurityGroup
- **Type**: typing.Optional[str]

### ServiceAccessSecurityGroup
- **Type**: typing.Optional[str]

### AdditionalMasterSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### AdditionalSlaveSecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# JobFlowInstancesDetailTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.InstanceGroupDetailTypeDef]]

### NormalizedInstanceHours
- **Type**: typing.Optional[int]

### Ec2KeyName
- **Type**: typing.Optional[str]

### Ec2SubnetId
- **Type**: typing.Optional[str]

### Placement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PlacementTypeOutputTypeDef]

### KeepJobFlowAliveWhenNoSteps
- **Type**: typing.Optional[bool]

### TerminationProtected
- **Type**: typing.Optional[bool]

### UnhealthyNodeReplacement
- **Type**: typing.Optional[bool]

### HadoopVersion
- **Type**: typing.Optional[str]


# KerberosAttributesTypeDef

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


# KeyValueTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ListBootstrapActionsInputListBootstrapActionsPaginateTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListBootstrapActionsInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListBootstrapActionsOutputTypeDef

### BootstrapActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.CommandTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListClustersInputListClustersPaginateTypeDef

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ClusterStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOOTSTRAPPING', 'RUNNING', 'STARTING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING', 'WAITING']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListClustersInputRequestTypeDef

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ClusterStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BOOTSTRAPPING', 'RUNNING', 'STARTING', 'TERMINATED', 'TERMINATED_WITH_ERRORS', 'TERMINATING', 'WAITING']]]

### Marker
- **Type**: typing.Optional[str]


# ListClustersOutputTypeDef

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.ClusterSummaryTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstanceFleetsInputListInstanceFleetsPaginateTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListInstanceFleetsInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListInstanceFleetsOutputTypeDef

### InstanceFleets
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.InstanceFleetTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstanceGroupsInputListInstanceGroupsPaginateTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListInstanceGroupsInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListInstanceGroupsOutputTypeDef

### InstanceGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.InstanceGroupTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstancesInputListInstancesPaginateTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: typing.Optional[str]

### InstanceGroupTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CORE', 'MASTER', 'TASK']]]

### InstanceFleetId
- **Type**: typing.Optional[str]

### InstanceFleetType
- **Type**: typing.Optional[typing.Literal['CORE', 'MASTER', 'TASK']]

### InstanceStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWAITING_FULFILLMENT', 'BOOTSTRAPPING', 'PROVISIONING', 'RUNNING', 'TERMINATED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListInstancesInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: typing.Optional[str]

### InstanceGroupTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CORE', 'MASTER', 'TASK']]]

### InstanceFleetId
- **Type**: typing.Optional[str]

### InstanceFleetType
- **Type**: typing.Optional[typing.Literal['CORE', 'MASTER', 'TASK']]

### InstanceStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWAITING_FULFILLMENT', 'BOOTSTRAPPING', 'PROVISIONING', 'RUNNING', 'TERMINATED']]]

### Marker
- **Type**: typing.Optional[str]


# ListInstancesOutputTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.InstanceTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNotebookExecutionsInputListNotebookExecutionsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListNotebookExecutionsInputRequestTypeDef

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


# ListNotebookExecutionsOutputTypeDef

### NotebookExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.NotebookExecutionSummaryTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReleaseLabelsInputRequestTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ReleaseLabelFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListReleaseLabelsOutputTypeDef

### ReleaseLabels
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsInputListSecurityConfigurationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListSecurityConfigurationsInputRequestTypeDef

### Marker
- **Type**: typing.Optional[str]


# ListSecurityConfigurationsOutputTypeDef

### SecurityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.SecurityConfigurationSummaryTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStepsInputListStepsPaginateTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'INTERRUPTED', 'PENDING', 'RUNNING']]]

### StepIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListStepsInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepStates
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'INTERRUPTED', 'PENDING', 'RUNNING']]]

### StepIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]


# ListStepsOutputTypeDef

### Steps
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.StepSummaryTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStudioSessionMappingsInputListStudioSessionMappingsPaginateTypeDef

### StudioId
- **Type**: typing.Optional[str]

### IdentityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListStudioSessionMappingsInputRequestTypeDef

### StudioId
- **Type**: typing.Optional[str]

### IdentityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### Marker
- **Type**: typing.Optional[str]


# ListStudioSessionMappingsOutputTypeDef

### SessionMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.SessionMappingSummaryTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStudiosInputListStudiosPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.PaginatorConfigTypeDef]


# ListStudiosInputRequestTypeDef

### Marker
- **Type**: typing.Optional[str]


# ListStudiosOutputTypeDef

### Studios
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.StudioSummaryTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSupportedInstanceTypesInputRequestTypeDef

### ReleaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListSupportedInstanceTypesOutputTypeDef

### SupportedInstanceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_classes.SupportedInstanceTypeTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagedScalingPolicyTypeDef

### ComputeLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ComputeLimitsTypeDef]


# MetricDimensionTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ModifyClusterInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### StepConcurrencyLevel
- **Type**: typing.Optional[int]


# ModifyClusterOutputTypeDef

### StepConcurrencyLevel
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyInstanceFleetInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceFleet
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.InstanceFleetModifyConfigTypeDef'>
- **Required**: Yes


# ModifyInstanceGroupsInputRequestTypeDef

### ClusterId
- **Type**: typing.Optional[str]

### InstanceGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.InstanceGroupModifyConfigTypeDef]]


# NotebookExecutionSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.NotebookS3LocationForOutputTypeDef]

### ExecutionEngineId
- **Type**: typing.Optional[str]


# NotebookExecutionTypeDef

### NotebookExecutionId
- **Type**: typing.Optional[str]

### EditorId
- **Type**: typing.Optional[str]

### ExecutionEngine
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ExecutionEngineConfigTypeDef]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.TagTypeDef]]

### NotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.NotebookS3LocationForOutputTypeDef]

### OutputNotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.OutputNotebookS3LocationForOutputTypeDef]

### OutputNotebookFormat
- **Type**: typing.Optional[typing.Literal['HTML']]

### EnvironmentVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# NotebookS3LocationForOutputTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# NotebookS3LocationFromInputTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# OSReleaseTypeDef

### Label
- **Type**: typing.Optional[str]


# OnDemandCapacityReservationOptionsTypeDef

### UsageStrategy
- **Type**: typing.Optional[typing.Literal['use-capacity-reservations-first']]

### CapacityReservationPreference
- **Type**: typing.Optional[typing.Literal['none', 'open']]

### CapacityReservationResourceGroupArn
- **Type**: typing.Optional[str]


# OnDemandProvisioningSpecificationTypeDef

### AllocationStrategy
- **Type**: typing.Literal['lowest-price', 'prioritized']
- **Required**: Yes

### CapacityReservationOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.OnDemandCapacityReservationOptionsTypeDef]


# OnDemandResizingSpecificationTypeDef

### TimeoutDurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# OutputNotebookS3LocationForOutputTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# OutputNotebookS3LocationFromInputTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlacementGroupConfigTypeDef

### InstanceRole
- **Type**: typing.Literal['CORE', 'MASTER', 'TASK']
- **Required**: Yes

### PlacementStrategy
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'NONE', 'PARTITION', 'SPREAD']]


# PlacementTypeOutputTypeDef

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]


# PlacementTypeTypeDef

### AvailabilityZone
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]


# PortRangeTypeDef

### MinRange
- **Type**: <class 'int'>
- **Required**: Yes

### MaxRange
- **Type**: typing.Optional[int]


# PutAutoScalingPolicyInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.AutoScalingPolicyTypeDef'>
- **Required**: Yes


# PutAutoScalingPolicyOutputTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoScalingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.AutoScalingPolicyDescriptionTypeDef'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutAutoTerminationPolicyInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### AutoTerminationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.AutoTerminationPolicyTypeDef]


# PutBlockPublicAccessConfigurationInputRequestTypeDef

### BlockPublicAccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.BlockPublicAccessConfigurationTypeDef'>
- **Required**: Yes


# PutManagedScalingPolicyInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedScalingPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ManagedScalingPolicyTypeDef'>
- **Required**: Yes


# ReleaseLabelFilterTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Application
- **Type**: typing.Optional[str]


# RemoveAutoScalingPolicyInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveAutoTerminationPolicyInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveManagedScalingPolicyInputRequestTypeDef

### ClusterId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsInputRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


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


# RunJobFlowInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.JobFlowInstancesConfigTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.emr_classes.StepConfigTypeDef, aws_resource_validator.pydantic_models.emr_classes.StepConfigOutputTypeDef]]]

### BootstrapActions
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.emr_classes.BootstrapActionConfigTypeDef, aws_resource_validator.pydantic_models.emr_classes.BootstrapActionConfigOutputTypeDef]]]

### SupportedProducts
- **Type**: typing.Optional[typing.Sequence[str]]

### NewSupportedProducts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.SupportedProductConfigTypeDef]]

### Applications
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.emr_classes.ApplicationTypeDef, aws_resource_validator.pydantic_models.emr_classes.ApplicationOutputTypeDef]]]

### Configurations
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.emr_classes.ConfigurationTypeDef, aws_resource_validator.pydantic_models.emr_classes.ConfigurationExtraOutputTypeDef]]]

### VisibleToAllUsers
- **Type**: typing.Optional[bool]

### JobFlowRole
- **Type**: typing.Optional[str]

### ServiceRole
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.TagTypeDef]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.KerberosAttributesTypeDef]

### StepConcurrencyLevel
- **Type**: typing.Optional[int]

### ManagedScalingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.ManagedScalingPolicyTypeDef]

### PlacementGroupConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.PlacementGroupConfigTypeDef]]

### AutoTerminationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.AutoTerminationPolicyTypeDef]

### OSReleaseLabel
- **Type**: typing.Optional[str]

### EbsRootVolumeIops
- **Type**: typing.Optional[int]

### EbsRootVolumeThroughput
- **Type**: typing.Optional[int]


# RunJobFlowOutputTypeDef

### JobFlowId
- **Type**: <class 'str'>
- **Required**: Yes

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ScalingActionTypeDef

### SimpleScalingPolicyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.SimpleScalingPolicyConfigurationTypeDef'>
- **Required**: Yes

### Market
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'SPOT']]


# ScalingConstraintsTypeDef

### MinCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### MaxCapacity
- **Type**: <class 'int'>
- **Required**: Yes


# ScalingRuleOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ScalingActionTypeDef'>
- **Required**: Yes

### Trigger
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ScalingTriggerOutputTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ScalingRuleTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ScalingActionTypeDef'>
- **Required**: Yes

### Trigger
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ScalingTriggerTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ScalingTriggerOutputTypeDef

### CloudWatchAlarmDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.CloudWatchAlarmDefinitionOutputTypeDef'>
- **Required**: Yes


# ScalingTriggerTypeDef

### CloudWatchAlarmDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.CloudWatchAlarmDefinitionTypeDef'>
- **Required**: Yes


# ScriptBootstrapActionConfigOutputTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Args
- **Type**: typing.Optional[typing.List[str]]


# ScriptBootstrapActionConfigTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Args
- **Type**: typing.Optional[typing.Sequence[str]]


# SecurityConfigurationSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]


# SessionMappingDetailTypeDef

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


# SessionMappingSummaryTypeDef

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


# SetKeepJobFlowAliveWhenNoStepsInputRequestTypeDef

### JobFlowIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### KeepJobFlowAliveWhenNoSteps
- **Type**: <class 'bool'>
- **Required**: Yes


# SetTerminationProtectionInputRequestTypeDef

### JobFlowIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TerminationProtected
- **Type**: <class 'bool'>
- **Required**: Yes


# SetUnhealthyNodeReplacementInputRequestTypeDef

### JobFlowIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UnhealthyNodeReplacement
- **Type**: <class 'bool'>
- **Required**: Yes


# SetVisibleToAllUsersInputRequestTypeDef

### JobFlowIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### VisibleToAllUsers
- **Type**: <class 'bool'>
- **Required**: Yes


# ShrinkPolicyOutputTypeDef

### DecommissionTimeout
- **Type**: typing.Optional[int]

### InstanceResizePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceResizePolicyOutputTypeDef]


# ShrinkPolicyTypeDef

### DecommissionTimeout
- **Type**: typing.Optional[int]

### InstanceResizePolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.InstanceResizePolicyTypeDef]


# SimpleScalingPolicyConfigurationTypeDef

### ScalingAdjustment
- **Type**: <class 'int'>
- **Required**: Yes

### AdjustmentType
- **Type**: typing.Optional[typing.Literal['CHANGE_IN_CAPACITY', 'EXACT_CAPACITY', 'PERCENT_CHANGE_IN_CAPACITY']]

### CoolDown
- **Type**: typing.Optional[int]


# SimplifiedApplicationTypeDef

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# SpotProvisioningSpecificationTypeDef

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


# SpotResizingSpecificationTypeDef

### TimeoutDurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# StartNotebookExecutionInputRequestTypeDef

### ExecutionEngine
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ExecutionEngineConfigTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_classes.TagTypeDef]]

### NotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.NotebookS3LocationFromInputTypeDef]

### OutputNotebookS3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.OutputNotebookS3LocationFromInputTypeDef]

### OutputNotebookFormat
- **Type**: typing.Optional[typing.Literal['HTML']]

### EnvironmentVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartNotebookExecutionOutputTypeDef

### NotebookExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StepConfigOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HadoopJarStep
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.HadoopJarStepConfigOutputTypeDef'>
- **Required**: Yes

### ActionOnFailure
- **Type**: typing.Optional[typing.Literal['CANCEL_AND_WAIT', 'CONTINUE', 'TERMINATE_CLUSTER', 'TERMINATE_JOB_FLOW']]


# StepConfigTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HadoopJarStep
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.HadoopJarStepConfigTypeDef'>
- **Required**: Yes

### ActionOnFailure
- **Type**: typing.Optional[typing.Literal['CANCEL_AND_WAIT', 'CONTINUE', 'TERMINATE_CLUSTER', 'TERMINATE_JOB_FLOW']]


# StepDetailTypeDef

### StepConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.StepConfigOutputTypeDef'>
- **Required**: Yes

### ExecutionStatusDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_classes.StepExecutionStatusDetailTypeDef'>
- **Required**: Yes


# StepExecutionStatusDetailTypeDef

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


# StepStateChangeReasonTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['NONE']]

### Message
- **Type**: typing.Optional[str]


# StepStatusTypeDef

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'CANCEL_PENDING', 'COMPLETED', 'FAILED', 'INTERRUPTED', 'PENDING', 'RUNNING']]

### StateChangeReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.StepStateChangeReasonTypeDef]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.FailureDetailsTypeDef]

### Timeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.StepTimelineTypeDef]


# StepSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.HadoopStepConfigTypeDef]

### ActionOnFailure
- **Type**: typing.Optional[typing.Literal['CANCEL_AND_WAIT', 'CONTINUE', 'TERMINATE_CLUSTER', 'TERMINATE_JOB_FLOW']]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.StepStatusTypeDef]


# StepTimelineTypeDef

### CreationDateTime
- **Type**: typing.Optional[datetime.datetime]

### StartDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# StepTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.HadoopStepConfigTypeDef]

### ActionOnFailure
- **Type**: typing.Optional[typing.Literal['CANCEL_AND_WAIT', 'CONTINUE', 'TERMINATE_CLUSTER', 'TERMINATE_JOB_FLOW']]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_classes.StepStatusTypeDef]

### ExecutionRoleArn
- **Type**: typing.Optional[str]


# StopNotebookExecutionInputRequestTypeDef

### NotebookExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# StudioSummaryTypeDef

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


# StudioTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_classes.TagTypeDef]]

### IdcInstanceArn
- **Type**: typing.Optional[str]

### TrustedIdentityPropagationEnabled
- **Type**: typing.Optional[bool]

### IdcUserAssignment
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRED']]

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# SupportedInstanceTypeTypeDef

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


# SupportedProductConfigTypeDef

### Name
- **Type**: typing.Optional[str]

### Args
- **Type**: typing.Optional[typing.Sequence[str]]


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TerminateJobFlowsInputRequestTypeDef

### JobFlowIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateStudioInputRequestTypeDef

### StudioId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DefaultS3Location
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# UpdateStudioSessionMappingInputRequestTypeDef

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


# UsernamePasswordTypeDef

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# VolumeSpecificationTypeDef

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


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



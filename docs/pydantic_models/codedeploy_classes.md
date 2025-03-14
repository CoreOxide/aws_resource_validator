# Codedeploy Classes

# AddTagsToOnPremisesInstancesInputTypeDef

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagTypeDef]
- **Required**: Yes

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AlarmConfigurationOutputTypeDef

### enabled
- **Type**: typing.Optional[bool]

### ignorePollAlarmFailure
- **Type**: typing.Optional[bool]

### alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmTypeDef]]


# AlarmConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]

### ignorePollAlarmFailure
- **Type**: typing.Optional[bool]

### alarms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmTypeDef]]


# AlarmConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AlarmTypeDef

### name
- **Type**: typing.Optional[str]


# AppSpecContentTypeDef

### content
- **Type**: typing.Optional[str]

### sha256
- **Type**: typing.Optional[str]


# ApplicationInfoTypeDef

### applicationId
- **Type**: typing.Optional[str]

### applicationName
- **Type**: typing.Optional[str]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### linkedToGitHub
- **Type**: typing.Optional[bool]

### gitHubAccountName
- **Type**: typing.Optional[str]

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]


# AutoRollbackConfigurationOutputTypeDef

### enabled
- **Type**: typing.Optional[bool]

### events
- **Type**: typing.Optional[typing.List[typing.Literal['DEPLOYMENT_FAILURE', 'DEPLOYMENT_STOP_ON_ALARM', 'DEPLOYMENT_STOP_ON_REQUEST']]]


# AutoRollbackConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]

### events
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEPLOYMENT_FAILURE', 'DEPLOYMENT_STOP_ON_ALARM', 'DEPLOYMENT_STOP_ON_REQUEST']]]


# AutoRollbackConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoScalingGroupTypeDef

### name
- **Type**: typing.Optional[str]

### hook
- **Type**: typing.Optional[str]

### terminationHook
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetApplicationRevisionsInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### revisions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef]
- **Required**: Yes


# BatchGetApplicationRevisionsOutputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetApplicationsInputTypeDef

### applicationNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetApplicationsOutputTypeDef

### applicationsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.ApplicationInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetDeploymentGroupsInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDeploymentGroupsOutputTypeDef

### deploymentGroupsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentGroupInfoTypeDef]
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetDeploymentInstancesInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDeploymentInstancesOutputTypeDef

### instancesSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.InstanceSummaryTypeDef]
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetDeploymentTargetsInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### targetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDeploymentTargetsOutputTypeDef

### deploymentTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetDeploymentsInputTypeDef

### deploymentIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDeploymentsOutputTypeDef

### deploymentsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetOnPremisesInstancesInputTypeDef

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetOnPremisesInstancesOutputTypeDef

### instanceInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.InstanceInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlueGreenDeploymentConfigurationTypeDef

### terminateBlueInstancesOnDeploymentSuccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueInstanceTerminationOptionTypeDef]

### deploymentReadyOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentReadyOptionTypeDef]

### greenFleetProvisioningOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.GreenFleetProvisioningOptionTypeDef]


# BlueInstanceTerminationOptionTypeDef

### action
- **Type**: typing.Optional[typing.Literal['KEEP_ALIVE', 'TERMINATE']]

### terminationWaitTimeInMinutes
- **Type**: typing.Optional[int]


# CloudFormationTargetTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### targetId
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEventTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]

### resourceType
- **Type**: typing.Optional[str]

### targetVersionWeight
- **Type**: typing.Optional[float]


# ContinueDeploymentInputTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### deploymentWaitType
- **Type**: typing.Optional[typing.Literal['READY_WAIT', 'TERMINATION_WAIT']]


# CreateApplicationInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagTypeDef]]


# CreateApplicationOutputTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentConfigInputTypeDef

### deploymentConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### minimumHealthyHosts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.MinimumHealthyHostsTypeDef]

### trafficRoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRoutingConfigTypeDef]

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### zonalConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.ZonalConfigTypeDef]


# CreateDeploymentConfigOutputTypeDef

### deploymentConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentGroupInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### serviceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentConfigName
- **Type**: typing.Optional[str]

### ec2TagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilterTypeDef]]

### onPremisesInstanceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilterTypeDef]]

### autoScalingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### triggerConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TriggerConfigUnionTypeDef]]

### alarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationUnionTypeDef]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationUnionTypeDef]

### outdatedInstancesStrategy
- **Type**: typing.Optional[typing.Literal['IGNORE', 'UPDATE']]

### deploymentStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentStyleTypeDef]

### blueGreenDeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueGreenDeploymentConfigurationTypeDef]

### loadBalancerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LoadBalancerInfoUnionTypeDef]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetUnionTypeDef]

### ecsServices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.ECSServiceTypeDef]]

### onPremisesTagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.OnPremisesTagSetUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagTypeDef]]

### terminationHookEnabled
- **Type**: typing.Optional[bool]


# CreateDeploymentGroupOutputTypeDef

### deploymentGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDeploymentInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupName
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef]

### deploymentConfigName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ignoreApplicationStopFailures
- **Type**: typing.Optional[bool]

### targetInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TargetInstancesUnionTypeDef]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationUnionTypeDef]

### updateOutdatedInstancesOnly
- **Type**: typing.Optional[bool]

### fileExistsBehavior
- **Type**: typing.Optional[typing.Literal['DISALLOW', 'OVERWRITE', 'RETAIN']]

### overrideAlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationUnionTypeDef]


# CreateDeploymentOutputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentConfigInputTypeDef

### deploymentConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentGroupInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentGroupOutputTypeDef

### hooksNotCleanedUp
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.AutoScalingGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGitHubAccountTokenInputTypeDef

### tokenName
- **Type**: typing.Optional[str]


# DeleteGitHubAccountTokenOutputTypeDef

### tokenName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourcesByExternalIdInputTypeDef

### externalId
- **Type**: typing.Optional[str]


# DeploymentConfigInfoTypeDef

### deploymentConfigId
- **Type**: typing.Optional[str]

### deploymentConfigName
- **Type**: typing.Optional[str]

### minimumHealthyHosts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.MinimumHealthyHostsTypeDef]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### trafficRoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRoutingConfigTypeDef]

### zonalConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.ZonalConfigTypeDef]


# DeploymentGroupInfoTypeDef

### applicationName
- **Type**: typing.Optional[str]

### deploymentGroupId
- **Type**: typing.Optional[str]

### deploymentGroupName
- **Type**: typing.Optional[str]

### deploymentConfigName
- **Type**: typing.Optional[str]

### ec2TagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilterTypeDef]]

### onPremisesInstanceTagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilterTypeDef]]

### autoScalingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.AutoScalingGroupTypeDef]]

### serviceRoleArn
- **Type**: typing.Optional[str]

### targetRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef]

### triggerConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TriggerConfigOutputTypeDef]]

### alarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationOutputTypeDef]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationOutputTypeDef]

### deploymentStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentStyleTypeDef]

### outdatedInstancesStrategy
- **Type**: typing.Optional[typing.Literal['IGNORE', 'UPDATE']]

### blueGreenDeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueGreenDeploymentConfigurationTypeDef]

### loadBalancerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LoadBalancerInfoOutputTypeDef]

### lastSuccessfulDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LastDeploymentInfoTypeDef]

### lastAttemptedDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LastDeploymentInfoTypeDef]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetOutputTypeDef]

### onPremisesTagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.OnPremisesTagSetOutputTypeDef]

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### ecsServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.ECSServiceTypeDef]]

### terminationHookEnabled
- **Type**: typing.Optional[bool]


# DeploymentInfoTypeDef

### applicationName
- **Type**: typing.Optional[str]

### deploymentGroupName
- **Type**: typing.Optional[str]

### deploymentConfigName
- **Type**: typing.Optional[str]

### deploymentId
- **Type**: typing.Optional[str]

### previousRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef]

### revision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['Baking', 'Created', 'Failed', 'InProgress', 'Queued', 'Ready', 'Stopped', 'Succeeded']]

### errorInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.ErrorInformationTypeDef]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### completeTime
- **Type**: typing.Optional[datetime.datetime]

### deploymentOverview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentOverviewTypeDef]

### description
- **Type**: typing.Optional[str]

### creator
- **Type**: typing.Optional[typing.Literal['CloudFormation', 'CloudFormationRollback', 'CodeDeploy', 'CodeDeployAutoUpdate', 'autoscaling', 'autoscalingTermination', 'codeDeployRollback', 'user']]

### ignoreApplicationStopFailures
- **Type**: typing.Optional[bool]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationOutputTypeDef]

### updateOutdatedInstancesOnly
- **Type**: typing.Optional[bool]

### rollbackInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RollbackInfoTypeDef]

### deploymentStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentStyleTypeDef]

### targetInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TargetInstancesOutputTypeDef]

### instanceTerminationWaitTimeStarted
- **Type**: typing.Optional[bool]

### blueGreenDeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueGreenDeploymentConfigurationTypeDef]

### loadBalancerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LoadBalancerInfoOutputTypeDef]

### additionalDeploymentStatusInfo
- **Type**: typing.Optional[str]

### fileExistsBehavior
- **Type**: typing.Optional[typing.Literal['DISALLOW', 'OVERWRITE', 'RETAIN']]

### deploymentStatusMessages
- **Type**: typing.Optional[typing.List[str]]

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### externalId
- **Type**: typing.Optional[str]

### relatedDeployments
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RelatedDeploymentsTypeDef]

### overrideAlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationOutputTypeDef]


# DeploymentOverviewTypeDef

### Pending
- **Type**: typing.Optional[int]

### InProgress
- **Type**: typing.Optional[int]

### Succeeded
- **Type**: typing.Optional[int]

### Failed
- **Type**: typing.Optional[int]

### Skipped
- **Type**: typing.Optional[int]

### Ready
- **Type**: typing.Optional[int]


# DeploymentReadyOptionTypeDef

### actionOnTimeout
- **Type**: typing.Optional[typing.Literal['CONTINUE_DEPLOYMENT', 'STOP_DEPLOYMENT']]

### waitTimeInMinutes
- **Type**: typing.Optional[int]


# DeploymentStyleTypeDef

### deploymentType
- **Type**: typing.Optional[typing.Literal['BLUE_GREEN', 'IN_PLACE']]

### deploymentOption
- **Type**: typing.Optional[typing.Literal['WITHOUT_TRAFFIC_CONTROL', 'WITH_TRAFFIC_CONTROL']]


# DeploymentTargetTypeDef

### deploymentTargetType
- **Type**: typing.Optional[typing.Literal['CloudFormationTarget', 'ECSTarget', 'InstanceTarget', 'LambdaTarget']]

### instanceTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.InstanceTargetTypeDef]

### lambdaTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LambdaTargetTypeDef]

### ecsTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.ECSTargetTypeDef]

### cloudFormationTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.CloudFormationTargetTypeDef]


# DeregisterOnPremisesInstanceInputTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# DiagnosticsTypeDef

### errorCode
- **Type**: typing.Optional[typing.Literal['ScriptFailed', 'ScriptMissing', 'ScriptNotExecutable', 'ScriptTimedOut', 'Success', 'UnknownError']]

### scriptName
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]

### logTail
- **Type**: typing.Optional[str]


# EC2TagFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EC2TagSetOutputTypeDef

### ec2TagSetList
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilterTypeDef]]]


# EC2TagSetTypeDef

### ec2TagSetList
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilterTypeDef]]]


# EC2TagSetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ECSServiceTypeDef

### serviceName
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]


# ECSTargetTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### targetId
- **Type**: typing.Optional[str]

### targetArn
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEventTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]

### taskSetsInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.ECSTaskSetTypeDef]]


# ECSTaskSetTypeDef

### identifer
- **Type**: typing.Optional[str]

### desiredCount
- **Type**: typing.Optional[int]

### pendingCount
- **Type**: typing.Optional[int]

### runningCount
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[str]

### trafficWeight
- **Type**: typing.Optional[float]

### targetGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfoTypeDef]

### taskSetLabel
- **Type**: typing.Optional[typing.Literal['Blue', 'Green']]


# ELBInfoTypeDef

### name
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ErrorInformationTypeDef

### code
- **Type**: typing.Optional[typing.Literal['AGENT_ISSUE', 'ALARM_ACTIVE', 'APPLICATION_MISSING', 'AUTOSCALING_VALIDATION_ERROR', 'AUTO_SCALING_CONFIGURATION', 'AUTO_SCALING_IAM_ROLE_PERMISSIONS', 'CLOUDFORMATION_STACK_FAILURE', 'CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND', 'CUSTOMER_APPLICATION_UNHEALTHY', 'DEPLOYMENT_GROUP_MISSING', 'ECS_UPDATE_ERROR', 'ELASTIC_LOAD_BALANCING_INVALID', 'ELB_INVALID_INSTANCE', 'HEALTH_CONSTRAINTS', 'HEALTH_CONSTRAINTS_INVALID', 'HOOK_EXECUTION_FAILURE', 'IAM_ROLE_MISSING', 'IAM_ROLE_PERMISSIONS', 'INTERNAL_ERROR', 'INVALID_ECS_SERVICE', 'INVALID_LAMBDA_CONFIGURATION', 'INVALID_LAMBDA_FUNCTION', 'INVALID_REVISION', 'MANUAL_STOP', 'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION', 'MISSING_ELB_INFORMATION', 'MISSING_GITHUB_TOKEN', 'NO_EC2_SUBSCRIPTION', 'NO_INSTANCES', 'OVER_MAX_INSTANCES', 'RESOURCE_LIMIT_EXCEEDED', 'REVISION_MISSING', 'THROTTLED', 'TIMEOUT']]

### message
- **Type**: typing.Optional[str]


# GenericRevisionInfoTypeDef

### description
- **Type**: typing.Optional[str]

### deploymentGroups
- **Type**: typing.Optional[typing.List[str]]

### firstUsedTime
- **Type**: typing.Optional[datetime.datetime]

### lastUsedTime
- **Type**: typing.Optional[datetime.datetime]

### registerTime
- **Type**: typing.Optional[datetime.datetime]


# GetApplicationInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationOutputTypeDef

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ApplicationInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationRevisionInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef'>
- **Required**: Yes


# GetApplicationRevisionOutputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef'>
- **Required**: Yes

### revisionInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.GenericRevisionInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentConfigInputTypeDef

### deploymentConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentConfigOutputTypeDef

### deploymentConfigInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentConfigInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentGroupInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentGroupOutputTypeDef

### deploymentGroupInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentGroupInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentInputWaitTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.WaiterConfigTypeDef]


# GetDeploymentInstanceInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentInstanceOutputTypeDef

### instanceSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.InstanceSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentOutputTypeDef

### deploymentInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeploymentTargetInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### targetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentTargetOutputTypeDef

### deploymentTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentTargetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOnPremisesInstanceInputTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetOnPremisesInstanceOutputTypeDef

### instanceInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.InstanceInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GitHubLocationTypeDef

### repository
- **Type**: typing.Optional[str]

### commitId
- **Type**: typing.Optional[str]


# GreenFleetProvisioningOptionTypeDef

### action
- **Type**: typing.Optional[typing.Literal['COPY_AUTO_SCALING_GROUP', 'DISCOVER_EXISTING']]


# InstanceInfoTypeDef

### instanceName
- **Type**: typing.Optional[str]

### iamSessionArn
- **Type**: typing.Optional[str]

### iamUserArn
- **Type**: typing.Optional[str]

### instanceArn
- **Type**: typing.Optional[str]

### registerTime
- **Type**: typing.Optional[datetime.datetime]

### deregisterTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TagTypeDef]]


# InstanceSummaryTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### instanceId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEventTypeDef]]

### instanceType
- **Type**: typing.Optional[typing.Literal['Blue', 'Green']]


# InstanceTargetTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### targetId
- **Type**: typing.Optional[str]

### targetArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEventTypeDef]]

### instanceLabel
- **Type**: typing.Optional[typing.Literal['Blue', 'Green']]


# LambdaFunctionInfoTypeDef

### functionName
- **Type**: typing.Optional[str]

### functionAlias
- **Type**: typing.Optional[str]

### currentVersion
- **Type**: typing.Optional[str]

### targetVersion
- **Type**: typing.Optional[str]

### targetVersionWeight
- **Type**: typing.Optional[float]


# LambdaTargetTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### targetId
- **Type**: typing.Optional[str]

### targetArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEventTypeDef]]

### lambdaFunctionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LambdaFunctionInfoTypeDef]


# LastDeploymentInfoTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Baking', 'Created', 'Failed', 'InProgress', 'Queued', 'Ready', 'Stopped', 'Succeeded']]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### createTime
- **Type**: typing.Optional[datetime.datetime]


# LifecycleEventTypeDef

### lifecycleEventName
- **Type**: typing.Optional[str]

### diagnostics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DiagnosticsTypeDef]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Skipped', 'Succeeded', 'Unknown']]


# ListApplicationRevisionsInputPaginateTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[typing.Literal['firstUsedTime', 'lastUsedTime', 'registerTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ascending', 'descending']]

### s3Bucket
- **Type**: typing.Optional[str]

### s3KeyPrefix
- **Type**: typing.Optional[str]

### deployed
- **Type**: typing.Optional[typing.Literal['exclude', 'ignore', 'include']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListApplicationRevisionsInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[typing.Literal['firstUsedTime', 'lastUsedTime', 'registerTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['ascending', 'descending']]

### s3Bucket
- **Type**: typing.Optional[str]

### s3KeyPrefix
- **Type**: typing.Optional[str]

### deployed
- **Type**: typing.Optional[typing.Literal['exclude', 'ignore', 'include']]

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationRevisionsOutputTypeDef

### revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListApplicationsInputTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsOutputTypeDef

### applications
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentConfigsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListDeploymentConfigsInputTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentConfigsOutputTypeDef

### deploymentConfigsList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentGroupsInputPaginateTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListDeploymentGroupsInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentGroupsOutputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentInstancesInputPaginateTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]]

### instanceTypeFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Blue', 'Green']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListDeploymentInstancesInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### instanceStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]]

### instanceTypeFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Blue', 'Green']]]


# ListDeploymentInstancesOutputTypeDef

### instancesList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentTargetsInputPaginateTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### targetFilters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ServerInstanceLabel', 'TargetStatus'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListDeploymentTargetsInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### targetFilters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ServerInstanceLabel', 'TargetStatus'], typing.Sequence[str]]]


# ListDeploymentTargetsOutputTypeDef

### targetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsInputPaginateTypeDef

### applicationName
- **Type**: typing.Optional[str]

### deploymentGroupName
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### includeOnlyStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Baking', 'Created', 'Failed', 'InProgress', 'Queued', 'Ready', 'Stopped', 'Succeeded']]]

### createTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TimeRangeTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListDeploymentsInputTypeDef

### applicationName
- **Type**: typing.Optional[str]

### deploymentGroupName
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### includeOnlyStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Baking', 'Created', 'Failed', 'InProgress', 'Queued', 'Ready', 'Stopped', 'Succeeded']]]

### createTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TimeRangeTypeDef]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsOutputTypeDef

### deployments
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGitHubAccountTokenNamesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListGitHubAccountTokenNamesInputTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListGitHubAccountTokenNamesOutputTypeDef

### tokenNameList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOnPremisesInstancesInputPaginateTypeDef

### registrationStatus
- **Type**: typing.Optional[typing.Literal['Deregistered', 'Registered']]

### tagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfigTypeDef]


# ListOnPremisesInstancesInputTypeDef

### registrationStatus
- **Type**: typing.Optional[typing.Literal['Deregistered', 'Registered']]

### tagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]


# ListOnPremisesInstancesOutputTypeDef

### instanceNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoadBalancerInfoOutputTypeDef

### elbInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.ELBInfoTypeDef]]

### targetGroupInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfoTypeDef]]

### targetGroupPairInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupPairInfoOutputTypeDef]]


# LoadBalancerInfoTypeDef

### elbInfoList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.ELBInfoTypeDef]]

### targetGroupInfoList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfoTypeDef]]

### targetGroupPairInfoList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupPairInfoTypeDef]]


# LoadBalancerInfoUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MinimumHealthyHostsPerZoneTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MinimumHealthyHostsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OnPremisesTagSetOutputTypeDef

### onPremisesTagSetList
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilterTypeDef]]]


# OnPremisesTagSetTypeDef

### onPremisesTagSetList
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilterTypeDef]]]


# OnPremisesTagSetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutLifecycleEventHookExecutionStatusInputTypeDef

### deploymentId
- **Type**: typing.Optional[str]

### lifecycleEventHookExecutionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Skipped', 'Succeeded', 'Unknown']]


# PutLifecycleEventHookExecutionStatusOutputTypeDef

### lifecycleEventHookExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RawStringTypeDef

### content
- **Type**: typing.Optional[str]

### sha256
- **Type**: typing.Optional[str]


# RegisterApplicationRevisionInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# RegisterOnPremisesInstanceInputTypeDef

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### iamSessionArn
- **Type**: typing.Optional[str]

### iamUserArn
- **Type**: typing.Optional[str]


# RelatedDeploymentsTypeDef

### autoUpdateOutdatedInstancesRootDeploymentId
- **Type**: typing.Optional[str]

### autoUpdateOutdatedInstancesDeploymentIds
- **Type**: typing.Optional[typing.List[str]]


# RemoveTagsFromOnPremisesInstancesInputTypeDef

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagTypeDef]
- **Required**: Yes

### instanceNames
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


# RevisionInfoTypeDef

### revisionLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocationTypeDef]

### genericRevisionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.GenericRevisionInfoTypeDef]


# RevisionLocationTypeDef

### revisionType
- **Type**: typing.Optional[typing.Literal['AppSpecContent', 'GitHub', 'S3', 'String']]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.S3LocationTypeDef]

### gitHubLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.GitHubLocationTypeDef]

### string
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RawStringTypeDef]

### appSpecContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AppSpecContentTypeDef]


# RollbackInfoTypeDef

### rollbackDeploymentId
- **Type**: typing.Optional[str]

### rollbackTriggeringDeploymentId
- **Type**: typing.Optional[str]

### rollbackMessage
- **Type**: typing.Optional[str]


# S3LocationTypeDef

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### bundleType
- **Type**: typing.Optional[typing.Literal['JSON', 'YAML', 'tar', 'tgz', 'zip']]

### version
- **Type**: typing.Optional[str]

### eTag
- **Type**: typing.Optional[str]


# SkipWaitTimeForInstanceTerminationInputTypeDef

### deploymentId
- **Type**: typing.Optional[str]


# StopDeploymentInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### autoRollbackEnabled
- **Type**: typing.Optional[bool]


# StopDeploymentOutputTypeDef

### status
- **Type**: typing.Literal['Pending', 'Succeeded']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TargetGroupInfoTypeDef

### name
- **Type**: typing.Optional[str]


# TargetGroupPairInfoOutputTypeDef

### targetGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfoTypeDef]]

### prodTrafficRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRouteOutputTypeDef]

### testTrafficRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRouteOutputTypeDef]


# TargetGroupPairInfoTypeDef

### targetGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfoTypeDef]]

### prodTrafficRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRouteTypeDef]

### testTrafficRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRouteTypeDef]


# TargetInstancesOutputTypeDef

### tagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilterTypeDef]]

### autoScalingGroups
- **Type**: typing.Optional[typing.List[str]]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetOutputTypeDef]


# TargetInstancesTypeDef

### tagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilterTypeDef]]

### autoScalingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetTypeDef]


# TargetInstancesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeBasedCanaryTypeDef

### canaryPercentage
- **Type**: typing.Optional[int]

### canaryInterval
- **Type**: typing.Optional[int]


# TimeBasedLinearTypeDef

### linearPercentage
- **Type**: typing.Optional[int]

### linearInterval
- **Type**: typing.Optional[int]


# TimeRangeTypeDef

### start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TimestampTypeDef]

### end
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TimestampTypeDef]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrafficRouteOutputTypeDef

### listenerArns
- **Type**: typing.Optional[typing.List[str]]


# TrafficRouteTypeDef

### listenerArns
- **Type**: typing.Optional[typing.Sequence[str]]


# TrafficRoutingConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TriggerConfigOutputTypeDef

### triggerName
- **Type**: typing.Optional[str]

### triggerTargetArn
- **Type**: typing.Optional[str]

### triggerEvents
- **Type**: typing.Optional[typing.List[typing.Literal['DeploymentFailure', 'DeploymentReady', 'DeploymentRollback', 'DeploymentStart', 'DeploymentStop', 'DeploymentSuccess', 'InstanceFailure', 'InstanceReady', 'InstanceStart', 'InstanceSuccess']]]


# TriggerConfigTypeDef

### triggerName
- **Type**: typing.Optional[str]

### triggerTargetArn
- **Type**: typing.Optional[str]

### triggerEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DeploymentFailure', 'DeploymentReady', 'DeploymentRollback', 'DeploymentStart', 'DeploymentStop', 'DeploymentSuccess', 'InstanceFailure', 'InstanceReady', 'InstanceStart', 'InstanceSuccess']]]


# TriggerConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationInputTypeDef

### applicationName
- **Type**: typing.Optional[str]

### newApplicationName
- **Type**: typing.Optional[str]


# UpdateDeploymentGroupInputTypeDef

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### currentDeploymentGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### newDeploymentGroupName
- **Type**: typing.Optional[str]

### deploymentConfigName
- **Type**: typing.Optional[str]

### ec2TagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilterTypeDef]]

### onPremisesInstanceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilterTypeDef]]

### autoScalingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### serviceRoleArn
- **Type**: typing.Optional[str]

### triggerConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TriggerConfigUnionTypeDef]]

### alarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationUnionTypeDef]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationUnionTypeDef]

### outdatedInstancesStrategy
- **Type**: typing.Optional[typing.Literal['IGNORE', 'UPDATE']]

### deploymentStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentStyleTypeDef]

### blueGreenDeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueGreenDeploymentConfigurationTypeDef]

### loadBalancerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LoadBalancerInfoUnionTypeDef]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetUnionTypeDef]

### ecsServices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.ECSServiceTypeDef]]

### onPremisesTagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.OnPremisesTagSetUnionTypeDef]

### terminationHookEnabled
- **Type**: typing.Optional[bool]


# UpdateDeploymentGroupOutputTypeDef

### hooksNotCleanedUp
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.AutoScalingGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# ZonalConfigTypeDef

### firstZoneMonitorDurationInSeconds
- **Type**: typing.Optional[int]

### monitorDurationInSeconds
- **Type**: typing.Optional[int]

### minimumHealthyHostsPerZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.MinimumHealthyHostsPerZoneTypeDef]



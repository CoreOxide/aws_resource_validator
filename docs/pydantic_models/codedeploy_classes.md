# Codedeploy Classes

# AddTagsToOnPremisesInstancesInput

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.Tag]
- **Required**: Yes

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# Alarm

### name
- **Type**: typing.Optional[str]


# AlarmConfiguration

### enabled
- **Type**: typing.Optional[bool]

### ignorePollAlarmFailure
- **Type**: typing.Optional[bool]

### alarms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.Alarm]]


# AlarmConfigurationOutput

### enabled
- **Type**: typing.Optional[bool]

### ignorePollAlarmFailure
- **Type**: typing.Optional[bool]

### alarms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.Alarm]]


# AlarmConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppSpecContent

### content
- **Type**: typing.Optional[str]

### sha256
- **Type**: typing.Optional[str]


# ApplicationInfo

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


# AutoRollbackConfiguration

### enabled
- **Type**: typing.Optional[bool]

### events
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEPLOYMENT_FAILURE', 'DEPLOYMENT_STOP_ON_ALARM', 'DEPLOYMENT_STOP_ON_REQUEST']]]


# AutoRollbackConfigurationOutput

### enabled
- **Type**: typing.Optional[bool]

### events
- **Type**: typing.Optional[typing.List[typing.Literal['DEPLOYMENT_FAILURE', 'DEPLOYMENT_STOP_ON_ALARM', 'DEPLOYMENT_STOP_ON_REQUEST']]]


# AutoRollbackConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoScalingGroup

### name
- **Type**: typing.Optional[str]

### hook
- **Type**: typing.Optional[str]

### terminationHook
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetApplicationRevisionsInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### revisions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation]
- **Required**: Yes


# BatchGetApplicationRevisionsOutput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetApplicationsInput

### applicationNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetApplicationsOutput

### applicationsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.ApplicationInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDeploymentGroupsInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDeploymentGroupsOutput

### deploymentGroupsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentGroupInfo]
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDeploymentInstancesInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDeploymentInstancesOutput

### instancesSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.InstanceSummary]
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDeploymentTargetsInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### targetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDeploymentTargetsOutput

### deploymentTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDeploymentsInput

### deploymentIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetDeploymentsOutput

### deploymentsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetOnPremisesInstancesInput

### instanceNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetOnPremisesInstancesOutput

### instanceInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.InstanceInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# BlueGreenDeploymentConfiguration

### terminateBlueInstancesOnDeploymentSuccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueInstanceTerminationOption]

### deploymentReadyOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentReadyOption]

### greenFleetProvisioningOption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.GreenFleetProvisioningOption]


# BlueInstanceTerminationOption

### action
- **Type**: typing.Optional[typing.Literal['KEEP_ALIVE', 'TERMINATE']]

### terminationWaitTimeInMinutes
- **Type**: typing.Optional[int]


# CloudFormationTarget

### deploymentId
- **Type**: typing.Optional[str]

### targetId
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEvent]]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]

### resourceType
- **Type**: typing.Optional[str]

### targetVersionWeight
- **Type**: typing.Optional[float]


# ContinueDeploymentInput

### deploymentId
- **Type**: typing.Optional[str]

### deploymentWaitType
- **Type**: typing.Optional[typing.Literal['READY_WAIT', 'TERMINATION_WAIT']]


# CreateApplicationInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.Tag]]


# CreateApplicationOutput

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentConfigInput

### deploymentConfigName
- **Type**: <class 'str'>
- **Required**: Yes

### minimumHealthyHosts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.MinimumHealthyHosts]

### trafficRoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRoutingConfig]

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### zonalConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.ZonalConfig]


# CreateDeploymentConfigOutput

### deploymentConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentGroupInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilter]]

### onPremisesInstanceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilter]]

### autoScalingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### triggerConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TriggerConfigUnion]]

### alarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationUnion]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationUnion]

### outdatedInstancesStrategy
- **Type**: typing.Optional[typing.Literal['IGNORE', 'UPDATE']]

### deploymentStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentStyle]

### blueGreenDeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueGreenDeploymentConfiguration]

### loadBalancerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LoadBalancerInfoUnion]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetUnion]

### ecsServices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.ECSService]]

### onPremisesTagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.OnPremisesTagSetUnion]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.Tag]]

### terminationHookEnabled
- **Type**: typing.Optional[bool]


# CreateDeploymentGroupOutput

### deploymentGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDeploymentInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupName
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation]

### deploymentConfigName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ignoreApplicationStopFailures
- **Type**: typing.Optional[bool]

### targetInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TargetInstancesUnion]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationUnion]

### updateOutdatedInstancesOnly
- **Type**: typing.Optional[bool]

### fileExistsBehavior
- **Type**: typing.Optional[typing.Literal['DISALLOW', 'OVERWRITE', 'RETAIN']]

### overrideAlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationUnion]


# CreateDeploymentOutput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentConfigInput

### deploymentConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentGroupInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentGroupOutput

### hooksNotCleanedUp
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.AutoScalingGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGitHubAccountTokenInput

### tokenName
- **Type**: typing.Optional[str]


# DeleteGitHubAccountTokenOutput

### tokenName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourcesByExternalIdInput

### externalId
- **Type**: typing.Optional[str]


# DeploymentConfigInfo

### deploymentConfigId
- **Type**: typing.Optional[str]

### deploymentConfigName
- **Type**: typing.Optional[str]

### minimumHealthyHosts
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.MinimumHealthyHosts]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### trafficRoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRoutingConfig]

### zonalConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.ZonalConfig]


# DeploymentGroupInfo

### applicationName
- **Type**: typing.Optional[str]

### deploymentGroupId
- **Type**: typing.Optional[str]

### deploymentGroupName
- **Type**: typing.Optional[str]

### deploymentConfigName
- **Type**: typing.Optional[str]

### ec2TagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilter]]

### onPremisesInstanceTagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilter]]

### autoScalingGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.AutoScalingGroup]]

### serviceRoleArn
- **Type**: typing.Optional[str]

### targetRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation]

### triggerConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TriggerConfigOutput]]

### alarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationOutput]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationOutput]

### deploymentStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentStyle]

### outdatedInstancesStrategy
- **Type**: typing.Optional[typing.Literal['IGNORE', 'UPDATE']]

### blueGreenDeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueGreenDeploymentConfiguration]

### loadBalancerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LoadBalancerInfoOutput]

### lastSuccessfulDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LastDeploymentInfo]

### lastAttemptedDeployment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LastDeploymentInfo]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetOutput]

### onPremisesTagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.OnPremisesTagSetOutput]

### computePlatform
- **Type**: typing.Optional[typing.Literal['ECS', 'Lambda', 'Server']]

### ecsServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.ECSService]]

### terminationHookEnabled
- **Type**: typing.Optional[bool]


# DeploymentInfo

### applicationName
- **Type**: typing.Optional[str]

### deploymentGroupName
- **Type**: typing.Optional[str]

### deploymentConfigName
- **Type**: typing.Optional[str]

### deploymentId
- **Type**: typing.Optional[str]

### previousRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation]

### revision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation]

### status
- **Type**: typing.Optional[typing.Literal['Baking', 'Created', 'Failed', 'InProgress', 'Queued', 'Ready', 'Stopped', 'Succeeded']]

### errorInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.ErrorInformation]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### completeTime
- **Type**: typing.Optional[datetime.datetime]

### deploymentOverview
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentOverview]

### description
- **Type**: typing.Optional[str]

### creator
- **Type**: typing.Optional[typing.Literal['CloudFormation', 'CloudFormationRollback', 'CodeDeploy', 'CodeDeployAutoUpdate', 'autoscaling', 'autoscalingTermination', 'codeDeployRollback', 'user']]

### ignoreApplicationStopFailures
- **Type**: typing.Optional[bool]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationOutput]

### updateOutdatedInstancesOnly
- **Type**: typing.Optional[bool]

### rollbackInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RollbackInfo]

### deploymentStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentStyle]

### targetInstances
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TargetInstancesOutput]

### instanceTerminationWaitTimeStarted
- **Type**: typing.Optional[bool]

### blueGreenDeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueGreenDeploymentConfiguration]

### loadBalancerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LoadBalancerInfoOutput]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RelatedDeployments]

### overrideAlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationOutput]


# DeploymentOverview

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


# DeploymentReadyOption

### actionOnTimeout
- **Type**: typing.Optional[typing.Literal['CONTINUE_DEPLOYMENT', 'STOP_DEPLOYMENT']]

### waitTimeInMinutes
- **Type**: typing.Optional[int]


# DeploymentStyle

### deploymentType
- **Type**: typing.Optional[typing.Literal['BLUE_GREEN', 'IN_PLACE']]

### deploymentOption
- **Type**: typing.Optional[typing.Literal['WITHOUT_TRAFFIC_CONTROL', 'WITH_TRAFFIC_CONTROL']]


# DeploymentTarget

### deploymentTargetType
- **Type**: typing.Optional[typing.Literal['CloudFormationTarget', 'ECSTarget', 'InstanceTarget', 'LambdaTarget']]

### instanceTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.InstanceTarget]

### lambdaTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LambdaTarget]

### ecsTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.ECSTarget]

### cloudFormationTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.CloudFormationTarget]


# DeregisterOnPremisesInstanceInput

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# Diagnostics

### errorCode
- **Type**: typing.Optional[typing.Literal['ScriptFailed', 'ScriptMissing', 'ScriptNotExecutable', 'ScriptTimedOut', 'Success', 'UnknownError']]

### scriptName
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]

### logTail
- **Type**: typing.Optional[str]


# EC2TagFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EC2TagSet

### ec2TagSetList
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilter]]]


# EC2TagSetOutput

### ec2TagSetList
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilter]]]


# EC2TagSetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ECSService

### serviceName
- **Type**: typing.Optional[str]

### clusterName
- **Type**: typing.Optional[str]


# ECSTarget

### deploymentId
- **Type**: typing.Optional[str]

### targetId
- **Type**: typing.Optional[str]

### targetArn
- **Type**: typing.Optional[str]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEvent]]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]

### taskSetsInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.ECSTaskSet]]


# ECSTaskSet

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfo]

### taskSetLabel
- **Type**: typing.Optional[typing.Literal['Blue', 'Green']]


# ELBInfo

### name
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# ErrorInformation

### code
- **Type**: typing.Optional[typing.Literal['AGENT_ISSUE', 'ALARM_ACTIVE', 'APPLICATION_MISSING', 'AUTOSCALING_VALIDATION_ERROR', 'AUTO_SCALING_CONFIGURATION', 'AUTO_SCALING_IAM_ROLE_PERMISSIONS', 'CLOUDFORMATION_STACK_FAILURE', 'CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND', 'CUSTOMER_APPLICATION_UNHEALTHY', 'DEPLOYMENT_GROUP_MISSING', 'ECS_UPDATE_ERROR', 'ELASTIC_LOAD_BALANCING_INVALID', 'ELB_INVALID_INSTANCE', 'HEALTH_CONSTRAINTS', 'HEALTH_CONSTRAINTS_INVALID', 'HOOK_EXECUTION_FAILURE', 'IAM_ROLE_MISSING', 'IAM_ROLE_PERMISSIONS', 'INTERNAL_ERROR', 'INVALID_ECS_SERVICE', 'INVALID_LAMBDA_CONFIGURATION', 'INVALID_LAMBDA_FUNCTION', 'INVALID_REVISION', 'MANUAL_STOP', 'MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION', 'MISSING_ELB_INFORMATION', 'MISSING_GITHUB_TOKEN', 'NO_EC2_SUBSCRIPTION', 'NO_INSTANCES', 'OVER_MAX_INSTANCES', 'RESOURCE_LIMIT_EXCEEDED', 'REVISION_MISSING', 'THROTTLED', 'TIMEOUT']]

### message
- **Type**: typing.Optional[str]


# GenericRevisionInfo

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


# GetApplicationInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationOutput

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ApplicationInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationRevisionInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation'>
- **Required**: Yes


# GetApplicationRevisionOutput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation'>
- **Required**: Yes

### revisionInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.GenericRevisionInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentConfigInput

### deploymentConfigName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentConfigOutput

### deploymentConfigInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentConfigInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentGroupInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentGroupOutput

### deploymentGroupInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentGroupInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentInputWait

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetDeploymentInstanceInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentInstanceOutput

### instanceSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.InstanceSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentOutput

### deploymentInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeploymentTargetInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### targetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentTargetOutput

### deploymentTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentTarget'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# GetOnPremisesInstanceInput

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetOnPremisesInstanceOutput

### instanceInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.InstanceInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# GitHubLocation

### repository
- **Type**: typing.Optional[str]

### commitId
- **Type**: typing.Optional[str]


# GreenFleetProvisioningOption

### action
- **Type**: typing.Optional[typing.Literal['COPY_AUTO_SCALING_GROUP', 'DISCOVER_EXISTING']]


# InstanceInfo

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.Tag]]


# InstanceSummary

### deploymentId
- **Type**: typing.Optional[str]

### instanceId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### lifecycleEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEvent]]

### instanceType
- **Type**: typing.Optional[typing.Literal['Blue', 'Green']]


# InstanceTarget

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEvent]]

### instanceLabel
- **Type**: typing.Optional[typing.Literal['Blue', 'Green']]


# LambdaFunctionInfo

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


# LambdaTarget

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.LifecycleEvent]]

### lambdaFunctionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LambdaFunctionInfo]


# LastDeploymentInfo

### deploymentId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Baking', 'Created', 'Failed', 'InProgress', 'Queued', 'Ready', 'Stopped', 'Succeeded']]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### createTime
- **Type**: typing.Optional[datetime.datetime]


# LifecycleEvent

### lifecycleEventName
- **Type**: typing.Optional[str]

### diagnostics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.Diagnostics]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Skipped', 'Succeeded', 'Unknown']]


# ListApplicationRevisionsInput

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


# ListApplicationRevisionsInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListApplicationRevisionsOutput

### revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsInput

### nextToken
- **Type**: typing.Optional[str]


# ListApplicationsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListApplicationsOutput

### applications
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentConfigsInput

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentConfigsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListDeploymentConfigsOutput

### deploymentConfigsList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentGroupsInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentGroupsInputPaginate

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListDeploymentGroupsOutput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentInstancesInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### instanceStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]]

### instanceTypeFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Blue', 'Green']]]


# ListDeploymentInstancesInputPaginate

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### instanceStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Failed', 'InProgress', 'Pending', 'Ready', 'Skipped', 'Succeeded', 'Unknown']]]

### instanceTypeFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Blue', 'Green']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListDeploymentInstancesOutput

### instancesList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentTargetsInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### targetFilters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ServerInstanceLabel', 'TargetStatus'], typing.Sequence[str]]]


# ListDeploymentTargetsInputPaginate

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### targetFilters
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ServerInstanceLabel', 'TargetStatus'], typing.Sequence[str]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListDeploymentTargetsOutput

### targetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsInput

### applicationName
- **Type**: typing.Optional[str]

### deploymentGroupName
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### includeOnlyStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Baking', 'Created', 'Failed', 'InProgress', 'Queued', 'Ready', 'Stopped', 'Succeeded']]]

### createTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TimeRange]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsInputPaginate

### applicationName
- **Type**: typing.Optional[str]

### deploymentGroupName
- **Type**: typing.Optional[str]

### externalId
- **Type**: typing.Optional[str]

### includeOnlyStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Baking', 'Created', 'Failed', 'InProgress', 'Queued', 'Ready', 'Stopped', 'Succeeded']]]

### createTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TimeRange]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListDeploymentsOutput

### deployments
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListGitHubAccountTokenNamesInput

### nextToken
- **Type**: typing.Optional[str]


# ListGitHubAccountTokenNamesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListGitHubAccountTokenNamesOutput

### tokenNameList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOnPremisesInstancesInput

### registrationStatus
- **Type**: typing.Optional[typing.Literal['Deregistered', 'Registered']]

### tagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilter]]

### nextToken
- **Type**: typing.Optional[str]


# ListOnPremisesInstancesInputPaginate

### registrationStatus
- **Type**: typing.Optional[typing.Literal['Deregistered', 'Registered']]

### tagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.PaginatorConfig]


# ListOnPremisesInstancesOutput

### instanceNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoadBalancerInfo

### elbInfoList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.ELBInfo]]

### targetGroupInfoList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfo]]

### targetGroupPairInfoList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupPairInfo]]


# LoadBalancerInfoOutput

### elbInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.ELBInfo]]

### targetGroupInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfo]]

### targetGroupPairInfoList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupPairInfoOutput]]


# LoadBalancerInfoUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MinimumHealthyHosts

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MinimumHealthyHostsPerZone

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OnPremisesTagSet

### onPremisesTagSetList
- **Type**: typing.Optional[typing.Sequence[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilter]]]


# OnPremisesTagSetOutput

### onPremisesTagSetList
- **Type**: typing.Optional[typing.List[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilter]]]


# OnPremisesTagSetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutLifecycleEventHookExecutionStatusInput

### deploymentId
- **Type**: typing.Optional[str]

### lifecycleEventHookExecutionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Pending', 'Skipped', 'Succeeded', 'Unknown']]


# PutLifecycleEventHookExecutionStatusOutput

### lifecycleEventHookExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# RawString

### content
- **Type**: typing.Optional[str]

### sha256
- **Type**: typing.Optional[str]


# RegisterApplicationRevisionInput

### applicationName
- **Type**: <class 'str'>
- **Required**: Yes

### revision
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# RegisterOnPremisesInstanceInput

### instanceName
- **Type**: <class 'str'>
- **Required**: Yes

### iamSessionArn
- **Type**: typing.Optional[str]

### iamUserArn
- **Type**: typing.Optional[str]


# RelatedDeployments

### autoUpdateOutdatedInstancesRootDeploymentId
- **Type**: typing.Optional[str]

### autoUpdateOutdatedInstancesDeploymentIds
- **Type**: typing.Optional[typing.List[str]]


# RemoveTagsFromOnPremisesInstancesInput

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.Tag]
- **Required**: Yes

### instanceNames
- **Type**: typing.Sequence[str]
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


# RevisionInfo

### revisionLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RevisionLocation]

### genericRevisionInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.GenericRevisionInfo]


# RevisionLocation

### revisionType
- **Type**: typing.Optional[typing.Literal['AppSpecContent', 'GitHub', 'S3', 'String']]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.S3Location]

### gitHubLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.GitHubLocation]

### string
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.RawString]

### appSpecContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AppSpecContent]


# RollbackInfo

### rollbackDeploymentId
- **Type**: typing.Optional[str]

### rollbackTriggeringDeploymentId
- **Type**: typing.Optional[str]

### rollbackMessage
- **Type**: typing.Optional[str]


# S3Location

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


# SkipWaitTimeForInstanceTerminationInput

### deploymentId
- **Type**: typing.Optional[str]


# StopDeploymentInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### autoRollbackEnabled
- **Type**: typing.Optional[bool]


# StopDeploymentOutput

### status
- **Type**: typing.Literal['Pending', 'Succeeded']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.Tag]
- **Required**: Yes


# TargetGroupInfo

### name
- **Type**: typing.Optional[str]


# TargetGroupPairInfo

### targetGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfo]]

### prodTrafficRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRoute]

### testTrafficRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRoute]


# TargetGroupPairInfoOutput

### targetGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.TargetGroupInfo]]

### prodTrafficRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRouteOutput]

### testTrafficRoute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.TrafficRouteOutput]


# TargetInstances

### tagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilter]]

### autoScalingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSet]


# TargetInstancesOutput

### tagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilter]]

### autoScalingGroups
- **Type**: typing.Optional[typing.List[str]]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetOutput]


# TargetInstancesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeBasedCanary

### canaryPercentage
- **Type**: typing.Optional[int]

### canaryInterval
- **Type**: typing.Optional[int]


# TimeBasedLinear

### linearPercentage
- **Type**: typing.Optional[int]

### linearInterval
- **Type**: typing.Optional[int]


# TimeRange

### start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.Timestamp]

### end
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.Timestamp]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrafficRoute

### listenerArns
- **Type**: typing.Optional[typing.Sequence[str]]


# TrafficRouteOutput

### listenerArns
- **Type**: typing.Optional[typing.List[str]]


# TrafficRoutingConfig

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TriggerConfig

### triggerName
- **Type**: typing.Optional[str]

### triggerTargetArn
- **Type**: typing.Optional[str]

### triggerEvents
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DeploymentFailure', 'DeploymentReady', 'DeploymentRollback', 'DeploymentStart', 'DeploymentStop', 'DeploymentSuccess', 'InstanceFailure', 'InstanceReady', 'InstanceStart', 'InstanceSuccess']]]


# TriggerConfigOutput

### triggerName
- **Type**: typing.Optional[str]

### triggerTargetArn
- **Type**: typing.Optional[str]

### triggerEvents
- **Type**: typing.Optional[typing.List[typing.Literal['DeploymentFailure', 'DeploymentReady', 'DeploymentRollback', 'DeploymentStart', 'DeploymentStop', 'DeploymentSuccess', 'InstanceFailure', 'InstanceReady', 'InstanceStart', 'InstanceSuccess']]]


# TriggerConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationInput

### applicationName
- **Type**: typing.Optional[str]

### newApplicationName
- **Type**: typing.Optional[str]


# UpdateDeploymentGroupInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagFilter]]

### onPremisesInstanceTagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TagFilter]]

### autoScalingGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### serviceRoleArn
- **Type**: typing.Optional[str]

### triggerConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.TriggerConfigUnion]]

### alarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AlarmConfigurationUnion]

### autoRollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.AutoRollbackConfigurationUnion]

### outdatedInstancesStrategy
- **Type**: typing.Optional[typing.Literal['IGNORE', 'UPDATE']]

### deploymentStyle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.DeploymentStyle]

### blueGreenDeploymentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.BlueGreenDeploymentConfiguration]

### loadBalancerInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.LoadBalancerInfoUnion]

### ec2TagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.EC2TagSetUnion]

### ecsServices
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codedeploy_classes.ECSService]]

### onPremisesTagSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.OnPremisesTagSetUnion]

### terminationHookEnabled
- **Type**: typing.Optional[bool]


# UpdateDeploymentGroupOutput

### hooksNotCleanedUp
- **Type**: typing.List[aws_resource_validator.pydantic_models.codedeploy_classes.AutoScalingGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codedeploy_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# ZonalConfig

### firstZoneMonitorDurationInSeconds
- **Type**: typing.Optional[int]

### monitorDurationInSeconds
- **Type**: typing.Optional[int]

### minimumHealthyHostsPerZone
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codedeploy_classes.MinimumHealthyHostsPerZone]



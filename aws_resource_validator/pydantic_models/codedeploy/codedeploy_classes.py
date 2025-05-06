from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codedeploy.codedeploy_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class Alarm(BaseValidatorModel):
    name: Optional[str] = None


class AppSpecContent(BaseValidatorModel):
    content: Optional[str] = None
    sha256: Optional[str] = None


class ApplicationInfo(BaseValidatorModel):
    applicationId: Optional[str] = None
    applicationName: Optional[str] = None
    createTime: Optional[datetime] = None
    linkedToGitHub: Optional[bool] = None
    gitHubAccountName: Optional[str] = None
    computePlatform: Optional[ComputePlatformType] = None


class AutoRollbackConfigurationOutput(BaseValidatorModel):
    enabled: Optional[bool] = None
    events: Optional[List[AutoRollbackEventType]] = None


class AutoRollbackConfiguration(BaseValidatorModel):
    enabled: Optional[bool] = None
    events: Optional[List[AutoRollbackEventType]] = None


class AutoScalingGroup(BaseValidatorModel):
    name: Optional[str] = None
    hook: Optional[str] = None
    terminationHook: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetApplicationsInput(BaseValidatorModel):
    applicationNames: List[str]


class BatchGetDeploymentGroupsInput(BaseValidatorModel):
    applicationName: str
    deploymentGroupNames: List[str]


class BatchGetDeploymentInstancesInput(BaseValidatorModel):
    deploymentId: str
    instanceIds: List[str]


class BatchGetDeploymentTargetsInput(BaseValidatorModel):
    deploymentId: str
    targetIds: List[str]


class BatchGetDeploymentsInput(BaseValidatorModel):
    deploymentIds: List[str]


class BatchGetOnPremisesInstancesInput(BaseValidatorModel):
    instanceNames: List[str]


class BlueInstanceTerminationOption(BaseValidatorModel):
    action: Optional[InstanceActionType] = None
    terminationWaitTimeInMinutes: Optional[int] = None


class DeploymentReadyOption(BaseValidatorModel):
    actionOnTimeout: Optional[DeploymentReadyActionType] = None
    waitTimeInMinutes: Optional[int] = None


class GreenFleetProvisioningOption(BaseValidatorModel):
    action: Optional[GreenFleetProvisioningActionType] = None


class ContinueDeploymentInput(BaseValidatorModel):
    deploymentId: Optional[str] = None
    deploymentWaitType: Optional[DeploymentWaitTypeType] = None


class MinimumHealthyHosts(BaseValidatorModel):
    type: Optional[MinimumHealthyHostsTypeType] = None
    value: Optional[int] = None


class DeploymentStyle(BaseValidatorModel):
    deploymentType: Optional[DeploymentTypeType] = None
    deploymentOption: Optional[DeploymentOptionType] = None


class EC2TagFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Type: Optional[EC2TagFilterTypeType] = None


class ECSService(BaseValidatorModel):
    serviceName: Optional[str] = None
    clusterName: Optional[str] = None


class TagFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Type: Optional[TagFilterTypeType] = None


class DeleteApplicationInput(BaseValidatorModel):
    applicationName: str


class DeleteDeploymentConfigInput(BaseValidatorModel):
    deploymentConfigName: str


class DeleteDeploymentGroupInput(BaseValidatorModel):
    applicationName: str
    deploymentGroupName: str


class DeleteGitHubAccountTokenInput(BaseValidatorModel):
    tokenName: Optional[str] = None


class DeleteResourcesByExternalIdInput(BaseValidatorModel):
    externalId: Optional[str] = None


class LastDeploymentInfo(BaseValidatorModel):
    deploymentId: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    endTime: Optional[datetime] = None
    createTime: Optional[datetime] = None


class TriggerConfigOutput(BaseValidatorModel):
    triggerName: Optional[str] = None
    triggerTargetArn: Optional[str] = None
    triggerEvents: Optional[List[TriggerEventTypeType]] = None


class DeploymentOverview(BaseValidatorModel):
    Pending: Optional[int] = None
    InProgress: Optional[int] = None
    Succeeded: Optional[int] = None
    Failed: Optional[int] = None
    Skipped: Optional[int] = None
    Ready: Optional[int] = None


class ErrorInformation(BaseValidatorModel):
    code: Optional[ErrorCodeType] = None
    message: Optional[str] = None


class RelatedDeployments(BaseValidatorModel):
    autoUpdateOutdatedInstancesRootDeploymentId: Optional[str] = None
    autoUpdateOutdatedInstancesDeploymentIds: Optional[List[str]] = None


class RollbackInfo(BaseValidatorModel):
    rollbackDeploymentId: Optional[str] = None
    rollbackTriggeringDeploymentId: Optional[str] = None
    rollbackMessage: Optional[str] = None


class DeregisterOnPremisesInstanceInput(BaseValidatorModel):
    instanceName: str


class Diagnostics(BaseValidatorModel):
    errorCode: Optional[LifecycleErrorCodeType] = None
    scriptName: Optional[str] = None
    message: Optional[str] = None
    logTail: Optional[str] = None


class TargetGroupInfo(BaseValidatorModel):
    name: Optional[str] = None


class ELBInfo(BaseValidatorModel):
    name: Optional[str] = None


class GenericRevisionInfo(BaseValidatorModel):
    description: Optional[str] = None
    deploymentGroups: Optional[List[str]] = None
    firstUsedTime: Optional[datetime] = None
    lastUsedTime: Optional[datetime] = None
    registerTime: Optional[datetime] = None


class GetApplicationInput(BaseValidatorModel):
    applicationName: str


class GetDeploymentConfigInput(BaseValidatorModel):
    deploymentConfigName: str


class GetDeploymentGroupInput(BaseValidatorModel):
    applicationName: str
    deploymentGroupName: str


class GetDeploymentInput(BaseValidatorModel):
    deploymentId: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetDeploymentInstanceInput(BaseValidatorModel):
    deploymentId: str
    instanceId: str


class GetDeploymentTargetInput(BaseValidatorModel):
    deploymentId: str
    targetId: str


class GetOnPremisesInstanceInput(BaseValidatorModel):
    instanceName: str


class GitHubLocation(BaseValidatorModel):
    repository: Optional[str] = None
    commitId: Optional[str] = None


class LambdaFunctionInfo(BaseValidatorModel):
    functionName: Optional[str] = None
    functionAlias: Optional[str] = None
    currentVersion: Optional[str] = None
    targetVersion: Optional[str] = None
    targetVersionWeight: Optional[float] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationRevisionsInput(BaseValidatorModel):
    applicationName: str
    sortBy: Optional[ApplicationRevisionSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    s3Bucket: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    deployed: Optional[ListStateFilterActionType] = None
    nextToken: Optional[str] = None


class ListApplicationsInput(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListDeploymentConfigsInput(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListDeploymentGroupsInput(BaseValidatorModel):
    applicationName: str
    nextToken: Optional[str] = None


class ListDeploymentInstancesInput(BaseValidatorModel):
    deploymentId: str
    nextToken: Optional[str] = None
    instanceStatusFilter: Optional[List[InstanceStatusType]] = None
    instanceTypeFilter: Optional[List[InstanceTypeType]] = None


class ListDeploymentTargetsInput(BaseValidatorModel):
    deploymentId: str
    nextToken: Optional[str] = None
    targetFilters: Optional[Dict[TargetFilterNameType, List[str]]] = None


class ListGitHubAccountTokenNamesInput(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None


class MinimumHealthyHostsPerZone(BaseValidatorModel):
    type: Optional[MinimumHealthyHostsPerZoneTypeType] = None
    value: Optional[int] = None


class PutLifecycleEventHookExecutionStatusInput(BaseValidatorModel):
    deploymentId: Optional[str] = None
    lifecycleEventHookExecutionId: Optional[str] = None
    status: Optional[LifecycleEventStatusType] = None


class RawString(BaseValidatorModel):
    content: Optional[str] = None
    sha256: Optional[str] = None


class RegisterOnPremisesInstanceInput(BaseValidatorModel):
    instanceName: str
    iamSessionArn: Optional[str] = None
    iamUserArn: Optional[str] = None


class S3Location(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    bundleType: Optional[BundleTypeType] = None
    version: Optional[str] = None
    eTag: Optional[str] = None


class SkipWaitTimeForInstanceTerminationInput(BaseValidatorModel):
    deploymentId: Optional[str] = None


class StopDeploymentInput(BaseValidatorModel):
    deploymentId: str
    autoRollbackEnabled: Optional[bool] = None


class TrafficRouteOutput(BaseValidatorModel):
    listenerArns: Optional[List[str]] = None


class TrafficRoute(BaseValidatorModel):
    listenerArns: Optional[List[str]] = None


class TimeBasedCanary(BaseValidatorModel):
    canaryPercentage: Optional[int] = None
    canaryInterval: Optional[int] = None


class TimeBasedLinear(BaseValidatorModel):
    linearPercentage: Optional[int] = None
    linearInterval: Optional[int] = None

Timestamp = Union[datetime, str]


class TriggerConfig(BaseValidatorModel):
    triggerName: Optional[str] = None
    triggerTargetArn: Optional[str] = None
    triggerEvents: Optional[List[TriggerEventTypeType]] = None


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateApplicationInput(BaseValidatorModel):
    applicationName: Optional[str] = None
    newApplicationName: Optional[str] = None


class AddTagsToOnPremisesInstancesInput(BaseValidatorModel):
    tags: List[Tag]
    instanceNames: List[str]


class CreateApplicationInput(BaseValidatorModel):
    applicationName: str
    computePlatform: Optional[ComputePlatformType] = None
    tags: Optional[List[Tag]] = None


class InstanceInfo(BaseValidatorModel):
    instanceName: Optional[str] = None
    iamSessionArn: Optional[str] = None
    iamUserArn: Optional[str] = None
    instanceArn: Optional[str] = None
    registerTime: Optional[datetime] = None
    deregisterTime: Optional[datetime] = None
    tags: Optional[List[Tag]] = None


class RemoveTagsFromOnPremisesInstancesInput(BaseValidatorModel):
    tags: List[Tag]
    instanceNames: List[str]


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class AlarmConfigurationOutput(BaseValidatorModel):
    enabled: Optional[bool] = None
    ignorePollAlarmFailure: Optional[bool] = None
    alarms: Optional[List[Alarm]] = None


class AlarmConfiguration(BaseValidatorModel):
    enabled: Optional[bool] = None
    ignorePollAlarmFailure: Optional[bool] = None
    alarms: Optional[List[Alarm]] = None

AutoRollbackConfigurationUnion = Union[AutoRollbackConfiguration, AutoRollbackConfigurationOutput]


class BatchGetApplicationsOutput(BaseValidatorModel):
    applicationsInfo: List[ApplicationInfo]
    ResponseMetadata: ResponseMetadata


class CreateApplicationOutput(BaseValidatorModel):
    applicationId: str
    ResponseMetadata: ResponseMetadata


class CreateDeploymentConfigOutput(BaseValidatorModel):
    deploymentConfigId: str
    ResponseMetadata: ResponseMetadata


class CreateDeploymentGroupOutput(BaseValidatorModel):
    deploymentGroupId: str
    ResponseMetadata: ResponseMetadata


class CreateDeploymentOutput(BaseValidatorModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadata


class DeleteDeploymentGroupOutput(BaseValidatorModel):
    hooksNotCleanedUp: List[AutoScalingGroup]
    ResponseMetadata: ResponseMetadata


class DeleteGitHubAccountTokenOutput(BaseValidatorModel):
    tokenName: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetApplicationOutput(BaseValidatorModel):
    application: ApplicationInfo
    ResponseMetadata: ResponseMetadata


class ListApplicationsOutput(BaseValidatorModel):
    applications: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeploymentConfigsOutput(BaseValidatorModel):
    deploymentConfigsList: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeploymentGroupsOutput(BaseValidatorModel):
    applicationName: str
    deploymentGroups: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeploymentInstancesOutput(BaseValidatorModel):
    instancesList: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeploymentTargetsOutput(BaseValidatorModel):
    targetIds: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDeploymentsOutput(BaseValidatorModel):
    deployments: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListGitHubAccountTokenNamesOutput(BaseValidatorModel):
    tokenNameList: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListOnPremisesInstancesOutput(BaseValidatorModel):
    instanceNames: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutLifecycleEventHookExecutionStatusOutput(BaseValidatorModel):
    lifecycleEventHookExecutionId: str
    ResponseMetadata: ResponseMetadata


class StopDeploymentOutput(BaseValidatorModel):
    status: StopStatusType
    statusMessage: str
    ResponseMetadata: ResponseMetadata


class UpdateDeploymentGroupOutput(BaseValidatorModel):
    hooksNotCleanedUp: List[AutoScalingGroup]
    ResponseMetadata: ResponseMetadata


class BlueGreenDeploymentConfiguration(BaseValidatorModel):
    terminateBlueInstancesOnDeploymentSuccess: Optional[BlueInstanceTerminationOption] = None
    deploymentReadyOption: Optional[DeploymentReadyOption] = None
    greenFleetProvisioningOption: Optional[GreenFleetProvisioningOption] = None


class EC2TagSetOutput(BaseValidatorModel):
    ec2TagSetList: Optional[List[List[EC2TagFilter]]] = None


class EC2TagSet(BaseValidatorModel):
    ec2TagSetList: Optional[List[List[EC2TagFilter]]] = None


class ListOnPremisesInstancesInput(BaseValidatorModel):
    registrationStatus: Optional[RegistrationStatusType] = None
    tagFilters: Optional[List[TagFilter]] = None
    nextToken: Optional[str] = None


class OnPremisesTagSetOutput(BaseValidatorModel):
    onPremisesTagSetList: Optional[List[List[TagFilter]]] = None


class OnPremisesTagSet(BaseValidatorModel):
    onPremisesTagSetList: Optional[List[List[TagFilter]]] = None


class LifecycleEvent(BaseValidatorModel):
    lifecycleEventName: Optional[str] = None
    diagnostics: Optional[Diagnostics] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    status: Optional[LifecycleEventStatusType] = None


class ECSTaskSet(BaseValidatorModel):
    identifer: Optional[str] = None
    desiredCount: Optional[int] = None
    pendingCount: Optional[int] = None
    runningCount: Optional[int] = None
    status: Optional[str] = None
    trafficWeight: Optional[float] = None
    targetGroup: Optional[TargetGroupInfo] = None
    taskSetLabel: Optional[TargetLabelType] = None


class GetDeploymentInputWait(BaseValidatorModel):
    deploymentId: str
    WaiterConfig: Optional[WaiterConfig] = None


class ListApplicationRevisionsInputPaginate(BaseValidatorModel):
    applicationName: str
    sortBy: Optional[ApplicationRevisionSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    s3Bucket: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    deployed: Optional[ListStateFilterActionType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentConfigsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentGroupsInputPaginate(BaseValidatorModel):
    applicationName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentInstancesInputPaginate(BaseValidatorModel):
    deploymentId: str
    instanceStatusFilter: Optional[List[InstanceStatusType]] = None
    instanceTypeFilter: Optional[List[InstanceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentTargetsInputPaginate(BaseValidatorModel):
    deploymentId: str
    targetFilters: Optional[Dict[TargetFilterNameType, List[str]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGitHubAccountTokenNamesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOnPremisesInstancesInputPaginate(BaseValidatorModel):
    registrationStatus: Optional[RegistrationStatusType] = None
    tagFilters: Optional[List[TagFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ZonalConfig(BaseValidatorModel):
    firstZoneMonitorDurationInSeconds: Optional[int] = None
    monitorDurationInSeconds: Optional[int] = None
    minimumHealthyHostsPerZone: Optional[MinimumHealthyHostsPerZone] = None


class RevisionLocation(BaseValidatorModel):
    revisionType: Optional[RevisionLocationTypeType] = None
    s3Location: Optional[S3Location] = None
    gitHubLocation: Optional[GitHubLocation] = None
    string: Optional[RawString] = None
    appSpecContent: Optional[AppSpecContent] = None


class TargetGroupPairInfoOutput(BaseValidatorModel):
    targetGroups: Optional[List[TargetGroupInfo]] = None
    prodTrafficRoute: Optional[TrafficRouteOutput] = None
    testTrafficRoute: Optional[TrafficRouteOutput] = None


class TargetGroupPairInfo(BaseValidatorModel):
    targetGroups: Optional[List[TargetGroupInfo]] = None
    prodTrafficRoute: Optional[TrafficRoute] = None
    testTrafficRoute: Optional[TrafficRoute] = None


class TrafficRoutingConfig(BaseValidatorModel):
    type: Optional[TrafficRoutingTypeType] = None
    timeBasedCanary: Optional[TimeBasedCanary] = None
    timeBasedLinear: Optional[TimeBasedLinear] = None


class TimeRange(BaseValidatorModel):
    start: Optional[Timestamp] = None
    end: Optional[Timestamp] = None

TriggerConfigUnion = Union[TriggerConfig, TriggerConfigOutput]


class BatchGetOnPremisesInstancesOutput(BaseValidatorModel):
    instanceInfos: List[InstanceInfo]
    ResponseMetadata: ResponseMetadata


class GetOnPremisesInstanceOutput(BaseValidatorModel):
    instanceInfo: InstanceInfo
    ResponseMetadata: ResponseMetadata

AlarmConfigurationUnion = Union[AlarmConfiguration, AlarmConfigurationOutput]


class TargetInstancesOutput(BaseValidatorModel):
    tagFilters: Optional[List[EC2TagFilter]] = None
    autoScalingGroups: Optional[List[str]] = None
    ec2TagSet: Optional[EC2TagSetOutput] = None

EC2TagSetUnion = Union[EC2TagSet, EC2TagSetOutput]


class TargetInstances(BaseValidatorModel):
    tagFilters: Optional[List[EC2TagFilter]] = None
    autoScalingGroups: Optional[List[str]] = None
    ec2TagSet: Optional[EC2TagSet] = None

OnPremisesTagSetUnion = Union[OnPremisesTagSet, OnPremisesTagSetOutput]


class CloudFormationTarget(BaseValidatorModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEvent]] = None
    status: Optional[TargetStatusType] = None
    resourceType: Optional[str] = None
    targetVersionWeight: Optional[float] = None


class InstanceSummary(BaseValidatorModel):
    deploymentId: Optional[str] = None
    instanceId: Optional[str] = None
    status: Optional[InstanceStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEvent]] = None
    instanceType: Optional[InstanceTypeType] = None


class InstanceTarget(BaseValidatorModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[TargetStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEvent]] = None
    instanceLabel: Optional[TargetLabelType] = None


class LambdaTarget(BaseValidatorModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[TargetStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEvent]] = None
    lambdaFunctionInfo: Optional[LambdaFunctionInfo] = None


class ECSTarget(BaseValidatorModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEvent]] = None
    status: Optional[TargetStatusType] = None
    taskSetsInfo: Optional[List[ECSTaskSet]] = None


class BatchGetApplicationRevisionsInput(BaseValidatorModel):
    applicationName: str
    revisions: List[RevisionLocation]


class GetApplicationRevisionInput(BaseValidatorModel):
    applicationName: str
    revision: RevisionLocation


class GetApplicationRevisionOutput(BaseValidatorModel):
    applicationName: str
    revision: RevisionLocation
    revisionInfo: GenericRevisionInfo
    ResponseMetadata: ResponseMetadata


class ListApplicationRevisionsOutput(BaseValidatorModel):
    revisions: List[RevisionLocation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RegisterApplicationRevisionInput(BaseValidatorModel):
    applicationName: str
    revision: RevisionLocation
    description: Optional[str] = None


class RevisionInfo(BaseValidatorModel):
    revisionLocation: Optional[RevisionLocation] = None
    genericRevisionInfo: Optional[GenericRevisionInfo] = None


class LoadBalancerInfoOutput(BaseValidatorModel):
    elbInfoList: Optional[List[ELBInfo]] = None
    targetGroupInfoList: Optional[List[TargetGroupInfo]] = None
    targetGroupPairInfoList: Optional[List[TargetGroupPairInfoOutput]] = None


class LoadBalancerInfo(BaseValidatorModel):
    elbInfoList: Optional[List[ELBInfo]] = None
    targetGroupInfoList: Optional[List[TargetGroupInfo]] = None
    targetGroupPairInfoList: Optional[List[TargetGroupPairInfo]] = None


class CreateDeploymentConfigInput(BaseValidatorModel):
    deploymentConfigName: str
    minimumHealthyHosts: Optional[MinimumHealthyHosts] = None
    trafficRoutingConfig: Optional[TrafficRoutingConfig] = None
    computePlatform: Optional[ComputePlatformType] = None
    zonalConfig: Optional[ZonalConfig] = None


class DeploymentConfigInfo(BaseValidatorModel):
    deploymentConfigId: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    minimumHealthyHosts: Optional[MinimumHealthyHosts] = None
    createTime: Optional[datetime] = None
    computePlatform: Optional[ComputePlatformType] = None
    trafficRoutingConfig: Optional[TrafficRoutingConfig] = None
    zonalConfig: Optional[ZonalConfig] = None


class ListDeploymentsInputPaginate(BaseValidatorModel):
    applicationName: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    externalId: Optional[str] = None
    includeOnlyStatuses: Optional[List[DeploymentStatusType]] = None
    createTimeRange: Optional[TimeRange] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentsInput(BaseValidatorModel):
    applicationName: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    externalId: Optional[str] = None
    includeOnlyStatuses: Optional[List[DeploymentStatusType]] = None
    createTimeRange: Optional[TimeRange] = None
    nextToken: Optional[str] = None

TargetInstancesUnion = Union[TargetInstances, TargetInstancesOutput]


class BatchGetDeploymentInstancesOutput(BaseValidatorModel):
    instancesSummary: List[InstanceSummary]
    errorMessage: str
    ResponseMetadata: ResponseMetadata


class GetDeploymentInstanceOutput(BaseValidatorModel):
    instanceSummary: InstanceSummary
    ResponseMetadata: ResponseMetadata


class DeploymentTarget(BaseValidatorModel):
    deploymentTargetType: Optional[DeploymentTargetTypeType] = None
    instanceTarget: Optional[InstanceTarget] = None
    lambdaTarget: Optional[LambdaTarget] = None
    ecsTarget: Optional[ECSTarget] = None
    cloudFormationTarget: Optional[CloudFormationTarget] = None


class BatchGetApplicationRevisionsOutput(BaseValidatorModel):
    applicationName: str
    errorMessage: str
    revisions: List[RevisionInfo]
    ResponseMetadata: ResponseMetadata


class DeploymentGroupInfo(BaseValidatorModel):
    applicationName: Optional[str] = None
    deploymentGroupId: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    ec2TagFilters: Optional[List[EC2TagFilter]] = None
    onPremisesInstanceTagFilters: Optional[List[TagFilter]] = None
    autoScalingGroups: Optional[List[AutoScalingGroup]] = None
    serviceRoleArn: Optional[str] = None
    targetRevision: Optional[RevisionLocation] = None
    triggerConfigurations: Optional[List[TriggerConfigOutput]] = None
    alarmConfiguration: Optional[AlarmConfigurationOutput] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationOutput] = None
    deploymentStyle: Optional[DeploymentStyle] = None
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategyType] = None
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration] = None
    loadBalancerInfo: Optional[LoadBalancerInfoOutput] = None
    lastSuccessfulDeployment: Optional[LastDeploymentInfo] = None
    lastAttemptedDeployment: Optional[LastDeploymentInfo] = None
    ec2TagSet: Optional[EC2TagSetOutput] = None
    onPremisesTagSet: Optional[OnPremisesTagSetOutput] = None
    computePlatform: Optional[ComputePlatformType] = None
    ecsServices: Optional[List[ECSService]] = None
    terminationHookEnabled: Optional[bool] = None


class DeploymentInfo(BaseValidatorModel):
    applicationName: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    deploymentId: Optional[str] = None
    previousRevision: Optional[RevisionLocation] = None
    revision: Optional[RevisionLocation] = None
    status: Optional[DeploymentStatusType] = None
    errorInformation: Optional[ErrorInformation] = None
    createTime: Optional[datetime] = None
    startTime: Optional[datetime] = None
    completeTime: Optional[datetime] = None
    deploymentOverview: Optional[DeploymentOverview] = None
    description: Optional[str] = None
    creator: Optional[DeploymentCreatorType] = None
    ignoreApplicationStopFailures: Optional[bool] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationOutput] = None
    updateOutdatedInstancesOnly: Optional[bool] = None
    rollbackInfo: Optional[RollbackInfo] = None
    deploymentStyle: Optional[DeploymentStyle] = None
    targetInstances: Optional[TargetInstancesOutput] = None
    instanceTerminationWaitTimeStarted: Optional[bool] = None
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration] = None
    loadBalancerInfo: Optional[LoadBalancerInfoOutput] = None
    additionalDeploymentStatusInfo: Optional[str] = None
    fileExistsBehavior: Optional[FileExistsBehaviorType] = None
    deploymentStatusMessages: Optional[List[str]] = None
    computePlatform: Optional[ComputePlatformType] = None
    externalId: Optional[str] = None
    relatedDeployments: Optional[RelatedDeployments] = None
    overrideAlarmConfiguration: Optional[AlarmConfigurationOutput] = None

LoadBalancerInfoUnion = Union[LoadBalancerInfo, LoadBalancerInfoOutput]


class GetDeploymentConfigOutput(BaseValidatorModel):
    deploymentConfigInfo: DeploymentConfigInfo
    ResponseMetadata: ResponseMetadata


class CreateDeploymentInput(BaseValidatorModel):
    applicationName: str
    deploymentGroupName: Optional[str] = None
    revision: Optional[RevisionLocation] = None
    deploymentConfigName: Optional[str] = None
    description: Optional[str] = None
    ignoreApplicationStopFailures: Optional[bool] = None
    targetInstances: Optional[TargetInstancesUnion] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationUnion] = None
    updateOutdatedInstancesOnly: Optional[bool] = None
    fileExistsBehavior: Optional[FileExistsBehaviorType] = None
    overrideAlarmConfiguration: Optional[AlarmConfigurationUnion] = None


class BatchGetDeploymentTargetsOutput(BaseValidatorModel):
    deploymentTargets: List[DeploymentTarget]
    ResponseMetadata: ResponseMetadata


class GetDeploymentTargetOutput(BaseValidatorModel):
    deploymentTarget: DeploymentTarget
    ResponseMetadata: ResponseMetadata


class BatchGetDeploymentGroupsOutput(BaseValidatorModel):
    deploymentGroupsInfo: List[DeploymentGroupInfo]
    errorMessage: str
    ResponseMetadata: ResponseMetadata


class GetDeploymentGroupOutput(BaseValidatorModel):
    deploymentGroupInfo: DeploymentGroupInfo
    ResponseMetadata: ResponseMetadata


class BatchGetDeploymentsOutput(BaseValidatorModel):
    deploymentsInfo: List[DeploymentInfo]
    ResponseMetadata: ResponseMetadata


class GetDeploymentOutput(BaseValidatorModel):
    deploymentInfo: DeploymentInfo
    ResponseMetadata: ResponseMetadata


class CreateDeploymentGroupInput(BaseValidatorModel):
    applicationName: str
    deploymentGroupName: str
    serviceRoleArn: str
    deploymentConfigName: Optional[str] = None
    ec2TagFilters: Optional[List[EC2TagFilter]] = None
    onPremisesInstanceTagFilters: Optional[List[TagFilter]] = None
    autoScalingGroups: Optional[List[str]] = None
    triggerConfigurations: Optional[List[TriggerConfigUnion]] = None
    alarmConfiguration: Optional[AlarmConfigurationUnion] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationUnion] = None
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategyType] = None
    deploymentStyle: Optional[DeploymentStyle] = None
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration] = None
    loadBalancerInfo: Optional[LoadBalancerInfoUnion] = None
    ec2TagSet: Optional[EC2TagSetUnion] = None
    ecsServices: Optional[List[ECSService]] = None
    onPremisesTagSet: Optional[OnPremisesTagSetUnion] = None
    tags: Optional[List[Tag]] = None
    terminationHookEnabled: Optional[bool] = None


class UpdateDeploymentGroupInput(BaseValidatorModel):
    applicationName: str
    currentDeploymentGroupName: str
    newDeploymentGroupName: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    ec2TagFilters: Optional[List[EC2TagFilter]] = None
    onPremisesInstanceTagFilters: Optional[List[TagFilter]] = None
    autoScalingGroups: Optional[List[str]] = None
    serviceRoleArn: Optional[str] = None
    triggerConfigurations: Optional[List[TriggerConfigUnion]] = None
    alarmConfiguration: Optional[AlarmConfigurationUnion] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationUnion] = None
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategyType] = None
    deploymentStyle: Optional[DeploymentStyle] = None
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfiguration] = None
    loadBalancerInfo: Optional[LoadBalancerInfoUnion] = None
    ec2TagSet: Optional[EC2TagSetUnion] = None
    ecsServices: Optional[List[ECSService]] = None
    onPremisesTagSet: Optional[OnPremisesTagSetUnion] = None
    terminationHookEnabled: Optional[bool] = None
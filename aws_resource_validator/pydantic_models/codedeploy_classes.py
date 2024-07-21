from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.codedeploy_constants import *

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AlarmTypeDef(BaseModel):
    name: Optional[str] = None

class AppSpecContentTypeDef(BaseModel):
    content: Optional[str] = None
    sha256: Optional[str] = None

class ApplicationInfoTypeDef(BaseModel):
    applicationId: Optional[str] = None
    applicationName: Optional[str] = None
    createTime: Optional[datetime] = None
    linkedToGitHub: Optional[bool] = None
    gitHubAccountName: Optional[str] = None
    computePlatform: Optional[ComputePlatformType] = None

class AutoRollbackConfigurationOutputTypeDef(BaseModel):
    enabled: Optional[bool] = None
    events: Optional[List[AutoRollbackEventType]] = None

class AutoRollbackConfigurationTypeDef(BaseModel):
    enabled: Optional[bool] = None
    events: Optional[Sequence[AutoRollbackEventType]] = None

class AutoScalingGroupTypeDef(BaseModel):
    name: Optional[str] = None
    hook: Optional[str] = None
    terminationHook: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchGetApplicationsInputRequestTypeDef(BaseModel):
    applicationNames: Sequence[str]

class BatchGetDeploymentGroupsInputRequestTypeDef(BaseModel):
    applicationName: str
    deploymentGroupNames: Sequence[str]

class BatchGetDeploymentInstancesInputRequestTypeDef(BaseModel):
    deploymentId: str
    instanceIds: Sequence[str]

class BatchGetDeploymentTargetsInputRequestTypeDef(BaseModel):
    deploymentId: str
    targetIds: Sequence[str]

class BatchGetDeploymentsInputRequestTypeDef(BaseModel):
    deploymentIds: Sequence[str]

class BatchGetOnPremisesInstancesInputRequestTypeDef(BaseModel):
    instanceNames: Sequence[str]

class BlueInstanceTerminationOptionTypeDef(BaseModel):
    action: Optional[InstanceActionType] = None
    terminationWaitTimeInMinutes: Optional[int] = None

class DeploymentReadyOptionTypeDef(BaseModel):
    actionOnTimeout: Optional[DeploymentReadyActionType] = None
    waitTimeInMinutes: Optional[int] = None

class GreenFleetProvisioningOptionTypeDef(BaseModel):
    action: Optional[GreenFleetProvisioningActionType] = None

class ContinueDeploymentInputRequestTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    deploymentWaitType: Optional[DeploymentWaitTypeType] = None

class MinimumHealthyHostsTypeDef(BaseModel):
    type: Optional[MinimumHealthyHostsTypeType] = None
    value: Optional[int] = None

class DeploymentStyleTypeDef(BaseModel):
    deploymentType: Optional[DeploymentTypeType] = None
    deploymentOption: Optional[DeploymentOptionType] = None

class EC2TagFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Type: Optional[EC2TagFilterTypeType] = None

class ECSServiceTypeDef(BaseModel):
    serviceName: Optional[str] = None
    clusterName: Optional[str] = None

class TagFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Type: Optional[TagFilterTypeType] = None

class DeleteApplicationInputRequestTypeDef(BaseModel):
    applicationName: str

class DeleteDeploymentConfigInputRequestTypeDef(BaseModel):
    deploymentConfigName: str

class DeleteDeploymentGroupInputRequestTypeDef(BaseModel):
    applicationName: str
    deploymentGroupName: str

class DeleteGitHubAccountTokenInputRequestTypeDef(BaseModel):
    tokenName: Optional[str] = None

class DeleteResourcesByExternalIdInputRequestTypeDef(BaseModel):
    externalId: Optional[str] = None

class LastDeploymentInfoTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    endTime: Optional[datetime] = None
    createTime: Optional[datetime] = None

class TriggerConfigOutputTypeDef(BaseModel):
    triggerName: Optional[str] = None
    triggerTargetArn: Optional[str] = None
    triggerEvents: Optional[List[TriggerEventTypeType]] = None

class DeploymentOverviewTypeDef(BaseModel):
    Pending: Optional[int] = None
    InProgress: Optional[int] = None
    Succeeded: Optional[int] = None
    Failed: Optional[int] = None
    Skipped: Optional[int] = None
    Ready: Optional[int] = None

class ErrorInformationTypeDef(BaseModel):
    code: Optional[ErrorCodeType] = None
    message: Optional[str] = None

class RelatedDeploymentsTypeDef(BaseModel):
    autoUpdateOutdatedInstancesRootDeploymentId: Optional[str] = None
    autoUpdateOutdatedInstancesDeploymentIds: Optional[List[str]] = None

class RollbackInfoTypeDef(BaseModel):
    rollbackDeploymentId: Optional[str] = None
    rollbackTriggeringDeploymentId: Optional[str] = None
    rollbackMessage: Optional[str] = None

class DeregisterOnPremisesInstanceInputRequestTypeDef(BaseModel):
    instanceName: str

class DiagnosticsTypeDef(BaseModel):
    errorCode: Optional[LifecycleErrorCodeType] = None
    scriptName: Optional[str] = None
    message: Optional[str] = None
    logTail: Optional[str] = None

class TargetGroupInfoTypeDef(BaseModel):
    name: Optional[str] = None

class ELBInfoTypeDef(BaseModel):
    name: Optional[str] = None

class GenericRevisionInfoTypeDef(BaseModel):
    description: Optional[str] = None
    deploymentGroups: Optional[List[str]] = None
    firstUsedTime: Optional[datetime] = None
    lastUsedTime: Optional[datetime] = None
    registerTime: Optional[datetime] = None

class GetApplicationInputRequestTypeDef(BaseModel):
    applicationName: str

class GetDeploymentConfigInputRequestTypeDef(BaseModel):
    deploymentConfigName: str

class GetDeploymentGroupInputRequestTypeDef(BaseModel):
    applicationName: str
    deploymentGroupName: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetDeploymentInputRequestTypeDef(BaseModel):
    deploymentId: str

class GetDeploymentInstanceInputRequestTypeDef(BaseModel):
    deploymentId: str
    instanceId: str

class GetDeploymentTargetInputRequestTypeDef(BaseModel):
    deploymentId: str
    targetId: str

class GetOnPremisesInstanceInputRequestTypeDef(BaseModel):
    instanceName: str

class GitHubLocationTypeDef(BaseModel):
    repository: Optional[str] = None
    commitId: Optional[str] = None

class LambdaFunctionInfoTypeDef(BaseModel):
    functionName: Optional[str] = None
    functionAlias: Optional[str] = None
    currentVersion: Optional[str] = None
    targetVersion: Optional[str] = None
    targetVersionWeight: Optional[float] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationRevisionsInputRequestTypeDef(BaseModel):
    applicationName: str
    sortBy: Optional[ApplicationRevisionSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    s3Bucket: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    deployed: Optional[ListStateFilterActionType] = None
    nextToken: Optional[str] = None

class ListApplicationsInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ListDeploymentConfigsInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ListDeploymentGroupsInputRequestTypeDef(BaseModel):
    applicationName: str
    nextToken: Optional[str] = None

class ListDeploymentInstancesInputRequestTypeDef(BaseModel):
    deploymentId: str
    nextToken: Optional[str] = None
    instanceStatusFilter: Optional[Sequence[InstanceStatusType]] = None
    instanceTypeFilter: Optional[Sequence[InstanceTypeType]] = None

class ListDeploymentTargetsInputRequestTypeDef(BaseModel):
    deploymentId: str
    nextToken: Optional[str] = None
    targetFilters: Optional[Mapping[TargetFilterNameType, Sequence[str]]] = None

class ListGitHubAccountTokenNamesInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None

class MinimumHealthyHostsPerZoneTypeDef(BaseModel):
    type: Optional[MinimumHealthyHostsPerZoneTypeType] = None
    value: Optional[int] = None

class PutLifecycleEventHookExecutionStatusInputRequestTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    lifecycleEventHookExecutionId: Optional[str] = None
    status: Optional[LifecycleEventStatusType] = None

class RawStringTypeDef(BaseModel):
    content: Optional[str] = None
    sha256: Optional[str] = None

class RegisterOnPremisesInstanceInputRequestTypeDef(BaseModel):
    instanceName: str
    iamSessionArn: Optional[str] = None
    iamUserArn: Optional[str] = None

class S3LocationTypeDef(BaseModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    bundleType: Optional[BundleTypeType] = None
    version: Optional[str] = None
    eTag: Optional[str] = None

class SkipWaitTimeForInstanceTerminationInputRequestTypeDef(BaseModel):
    deploymentId: Optional[str] = None

class StopDeploymentInputRequestTypeDef(BaseModel):
    deploymentId: str
    autoRollbackEnabled: Optional[bool] = None

class TrafficRouteOutputTypeDef(BaseModel):
    listenerArns: Optional[List[str]] = None

class TrafficRouteTypeDef(BaseModel):
    listenerArns: Optional[Sequence[str]] = None

class TimeBasedCanaryTypeDef(BaseModel):
    canaryPercentage: Optional[int] = None
    canaryInterval: Optional[int] = None

class TimeBasedLinearTypeDef(BaseModel):
    linearPercentage: Optional[int] = None
    linearInterval: Optional[int] = None

class TriggerConfigTypeDef(BaseModel):
    triggerName: Optional[str] = None
    triggerTargetArn: Optional[str] = None
    triggerEvents: Optional[Sequence[TriggerEventTypeType]] = None

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApplicationInputRequestTypeDef(BaseModel):
    applicationName: Optional[str] = None
    newApplicationName: Optional[str] = None

class AddTagsToOnPremisesInstancesInputRequestTypeDef(BaseModel):
    tags: Sequence[TagTypeDef]
    instanceNames: Sequence[str]

class CreateApplicationInputRequestTypeDef(BaseModel):
    applicationName: str
    computePlatform: Optional[ComputePlatformType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class InstanceInfoTypeDef(BaseModel):
    instanceName: Optional[str] = None
    iamSessionArn: Optional[str] = None
    iamUserArn: Optional[str] = None
    instanceArn: Optional[str] = None
    registerTime: Optional[datetime] = None
    deregisterTime: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None

class RemoveTagsFromOnPremisesInstancesInputRequestTypeDef(BaseModel):
    tags: Sequence[TagTypeDef]
    instanceNames: Sequence[str]

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class AlarmConfigurationOutputTypeDef(BaseModel):
    enabled: Optional[bool] = None
    ignorePollAlarmFailure: Optional[bool] = None
    alarms: Optional[List[AlarmTypeDef]] = None

class AlarmConfigurationTypeDef(BaseModel):
    enabled: Optional[bool] = None
    ignorePollAlarmFailure: Optional[bool] = None
    alarms: Optional[Sequence[AlarmTypeDef]] = None

class BatchGetApplicationsOutputTypeDef(BaseModel):
    applicationsInfo: List[ApplicationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationOutputTypeDef(BaseModel):
    applicationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentConfigOutputTypeDef(BaseModel):
    deploymentConfigId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentGroupOutputTypeDef(BaseModel):
    deploymentGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentOutputTypeDef(BaseModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeploymentGroupOutputTypeDef(BaseModel):
    hooksNotCleanedUp: List[AutoScalingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGitHubAccountTokenOutputTypeDef(BaseModel):
    tokenName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationOutputTypeDef(BaseModel):
    application: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsOutputTypeDef(BaseModel):
    applications: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentConfigsOutputTypeDef(BaseModel):
    deploymentConfigsList: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentGroupsOutputTypeDef(BaseModel):
    applicationName: str
    deploymentGroups: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentInstancesOutputTypeDef(BaseModel):
    instancesList: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentTargetsOutputTypeDef(BaseModel):
    targetIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentsOutputTypeDef(BaseModel):
    deployments: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGitHubAccountTokenNamesOutputTypeDef(BaseModel):
    tokenNameList: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOnPremisesInstancesOutputTypeDef(BaseModel):
    instanceNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutLifecycleEventHookExecutionStatusOutputTypeDef(BaseModel):
    lifecycleEventHookExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopDeploymentOutputTypeDef(BaseModel):
    status: StopStatusType
    statusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeploymentGroupOutputTypeDef(BaseModel):
    hooksNotCleanedUp: List[AutoScalingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BlueGreenDeploymentConfigurationTypeDef(BaseModel):
    terminateBlueInstancesOnDeploymentSuccess: Optional[       BlueInstanceTerminationOptionTypeDef     ] = None
    deploymentReadyOption: Optional[DeploymentReadyOptionTypeDef] = None
    greenFleetProvisioningOption: Optional[GreenFleetProvisioningOptionTypeDef] = None

class EC2TagSetOutputTypeDef(BaseModel):
    ec2TagSetList: Optional[List[List[EC2TagFilterTypeDef]]] = None

class EC2TagSetTypeDef(BaseModel):
    ec2TagSetList: Optional[Sequence[Sequence[EC2TagFilterTypeDef]]] = None

class ListOnPremisesInstancesInputRequestTypeDef(BaseModel):
    registrationStatus: Optional[RegistrationStatusType] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    nextToken: Optional[str] = None

class OnPremisesTagSetOutputTypeDef(BaseModel):
    onPremisesTagSetList: Optional[List[List[TagFilterTypeDef]]] = None

class OnPremisesTagSetTypeDef(BaseModel):
    onPremisesTagSetList: Optional[Sequence[Sequence[TagFilterTypeDef]]] = None

class LifecycleEventTypeDef(BaseModel):
    lifecycleEventName: Optional[str] = None
    diagnostics: Optional[DiagnosticsTypeDef] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    status: Optional[LifecycleEventStatusType] = None

class ECSTaskSetTypeDef(BaseModel):
    identifer: Optional[str] = None
    desiredCount: Optional[int] = None
    pendingCount: Optional[int] = None
    runningCount: Optional[int] = None
    status: Optional[str] = None
    trafficWeight: Optional[float] = None
    targetGroup: Optional[TargetGroupInfoTypeDef] = None
    taskSetLabel: Optional[TargetLabelType] = None

class GetDeploymentInputDeploymentSuccessfulWaitTypeDef(BaseModel):
    deploymentId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListApplicationRevisionsInputListApplicationRevisionsPaginateTypeDef(BaseModel):
    applicationName: str
    sortBy: Optional[ApplicationRevisionSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    s3Bucket: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    deployed: Optional[ListStateFilterActionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsInputListApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentConfigsInputListDeploymentConfigsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentGroupsInputListDeploymentGroupsPaginateTypeDef(BaseModel):
    applicationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentInstancesInputListDeploymentInstancesPaginateTypeDef(BaseModel):
    deploymentId: str
    instanceStatusFilter: Optional[Sequence[InstanceStatusType]] = None
    instanceTypeFilter: Optional[Sequence[InstanceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentTargetsInputListDeploymentTargetsPaginateTypeDef(BaseModel):
    deploymentId: str
    targetFilters: Optional[Mapping[TargetFilterNameType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGitHubAccountTokenNamesInputListGitHubAccountTokenNamesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOnPremisesInstancesInputListOnPremisesInstancesPaginateTypeDef(BaseModel):
    registrationStatus: Optional[RegistrationStatusType] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ZonalConfigTypeDef(BaseModel):
    firstZoneMonitorDurationInSeconds: Optional[int] = None
    monitorDurationInSeconds: Optional[int] = None
    minimumHealthyHostsPerZone: Optional[MinimumHealthyHostsPerZoneTypeDef] = None

class RevisionLocationTypeDef(BaseModel):
    revisionType: Optional[RevisionLocationTypeType] = None
    s3Location: Optional[S3LocationTypeDef] = None
    gitHubLocation: Optional[GitHubLocationTypeDef] = None
    string: Optional[RawStringTypeDef] = None
    appSpecContent: Optional[AppSpecContentTypeDef] = None

class TargetGroupPairInfoOutputTypeDef(BaseModel):
    targetGroups: Optional[List[TargetGroupInfoTypeDef]] = None
    prodTrafficRoute: Optional[TrafficRouteOutputTypeDef] = None
    testTrafficRoute: Optional[TrafficRouteOutputTypeDef] = None

class TargetGroupPairInfoTypeDef(BaseModel):
    targetGroups: Optional[Sequence[TargetGroupInfoTypeDef]] = None
    prodTrafficRoute: Optional[TrafficRouteTypeDef] = None
    testTrafficRoute: Optional[TrafficRouteTypeDef] = None

class TrafficRoutingConfigTypeDef(BaseModel):
    type: Optional[TrafficRoutingTypeType] = None
    timeBasedCanary: Optional[TimeBasedCanaryTypeDef] = None
    timeBasedLinear: Optional[TimeBasedLinearTypeDef] = None

class TimeRangeTypeDef(BaseModel):
    start: Optional[TimestampTypeDef] = None
    end: Optional[TimestampTypeDef] = None

class BatchGetOnPremisesInstancesOutputTypeDef(BaseModel):
    instanceInfos: List[InstanceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOnPremisesInstanceOutputTypeDef(BaseModel):
    instanceInfo: InstanceInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TargetInstancesOutputTypeDef(BaseModel):
    tagFilters: Optional[List[EC2TagFilterTypeDef]] = None
    autoScalingGroups: Optional[List[str]] = None
    ec2TagSet: Optional[EC2TagSetOutputTypeDef] = None

class TargetInstancesTypeDef(BaseModel):
    tagFilters: Optional[Sequence[EC2TagFilterTypeDef]] = None
    autoScalingGroups: Optional[Sequence[str]] = None
    ec2TagSet: Optional[EC2TagSetTypeDef] = None

class CloudFormationTargetTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    status: Optional[TargetStatusType] = None
    resourceType: Optional[str] = None
    targetVersionWeight: Optional[float] = None

class InstanceSummaryTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    instanceId: Optional[str] = None
    status: Optional[InstanceStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    instanceType: Optional[InstanceTypeType] = None

class InstanceTargetTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[TargetStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    instanceLabel: Optional[TargetLabelType] = None

class LambdaTargetTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[TargetStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    lambdaFunctionInfo: Optional[LambdaFunctionInfoTypeDef] = None

class ECSTargetTypeDef(BaseModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    status: Optional[TargetStatusType] = None
    taskSetsInfo: Optional[List[ECSTaskSetTypeDef]] = None

class BatchGetApplicationRevisionsInputRequestTypeDef(BaseModel):
    applicationName: str
    revisions: Sequence[RevisionLocationTypeDef]

class GetApplicationRevisionInputRequestTypeDef(BaseModel):
    applicationName: str
    revision: RevisionLocationTypeDef

class GetApplicationRevisionOutputTypeDef(BaseModel):
    applicationName: str
    revision: RevisionLocationTypeDef
    revisionInfo: GenericRevisionInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationRevisionsOutputTypeDef(BaseModel):
    revisions: List[RevisionLocationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterApplicationRevisionInputRequestTypeDef(BaseModel):
    applicationName: str
    revision: RevisionLocationTypeDef
    description: Optional[str] = None

class RevisionInfoTypeDef(BaseModel):
    revisionLocation: Optional[RevisionLocationTypeDef] = None
    genericRevisionInfo: Optional[GenericRevisionInfoTypeDef] = None

class LoadBalancerInfoOutputTypeDef(BaseModel):
    elbInfoList: Optional[List[ELBInfoTypeDef]] = None
    targetGroupInfoList: Optional[List[TargetGroupInfoTypeDef]] = None
    targetGroupPairInfoList: Optional[List[TargetGroupPairInfoOutputTypeDef]] = None

class LoadBalancerInfoTypeDef(BaseModel):
    elbInfoList: Optional[Sequence[ELBInfoTypeDef]] = None
    targetGroupInfoList: Optional[Sequence[TargetGroupInfoTypeDef]] = None
    targetGroupPairInfoList: Optional[Sequence[TargetGroupPairInfoTypeDef]] = None

class CreateDeploymentConfigInputRequestTypeDef(BaseModel):
    deploymentConfigName: str
    minimumHealthyHosts: Optional[MinimumHealthyHostsTypeDef] = None
    trafficRoutingConfig: Optional[TrafficRoutingConfigTypeDef] = None
    computePlatform: Optional[ComputePlatformType] = None
    zonalConfig: Optional[ZonalConfigTypeDef] = None

class DeploymentConfigInfoTypeDef(BaseModel):
    deploymentConfigId: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    minimumHealthyHosts: Optional[MinimumHealthyHostsTypeDef] = None
    createTime: Optional[datetime] = None
    computePlatform: Optional[ComputePlatformType] = None
    trafficRoutingConfig: Optional[TrafficRoutingConfigTypeDef] = None
    zonalConfig: Optional[ZonalConfigTypeDef] = None

class ListDeploymentsInputListDeploymentsPaginateTypeDef(BaseModel):
    applicationName: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    externalId: Optional[str] = None
    includeOnlyStatuses: Optional[Sequence[DeploymentStatusType]] = None
    createTimeRange: Optional[TimeRangeTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsInputRequestTypeDef(BaseModel):
    applicationName: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    externalId: Optional[str] = None
    includeOnlyStatuses: Optional[Sequence[DeploymentStatusType]] = None
    createTimeRange: Optional[TimeRangeTypeDef] = None
    nextToken: Optional[str] = None

class CreateDeploymentInputRequestTypeDef(BaseModel):
    applicationName: str
    deploymentGroupName: Optional[str] = None
    revision: Optional[RevisionLocationTypeDef] = None
    deploymentConfigName: Optional[str] = None
    description: Optional[str] = None
    ignoreApplicationStopFailures: Optional[bool] = None
    targetInstances: Optional[TargetInstancesTypeDef] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationTypeDef] = None
    updateOutdatedInstancesOnly: Optional[bool] = None
    fileExistsBehavior: Optional[FileExistsBehaviorType] = None
    overrideAlarmConfiguration: Optional[AlarmConfigurationTypeDef] = None

class BatchGetDeploymentInstancesOutputTypeDef(BaseModel):
    instancesSummary: List[InstanceSummaryTypeDef]
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentInstanceOutputTypeDef(BaseModel):
    instanceSummary: InstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentTargetTypeDef(BaseModel):
    deploymentTargetType: Optional[DeploymentTargetTypeType] = None
    instanceTarget: Optional[InstanceTargetTypeDef] = None
    lambdaTarget: Optional[LambdaTargetTypeDef] = None
    ecsTarget: Optional[ECSTargetTypeDef] = None
    cloudFormationTarget: Optional[CloudFormationTargetTypeDef] = None

class BatchGetApplicationRevisionsOutputTypeDef(BaseModel):
    applicationName: str
    errorMessage: str
    revisions: List[RevisionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentGroupInfoTypeDef(BaseModel):
    applicationName: Optional[str] = None
    deploymentGroupId: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    ec2TagFilters: Optional[List[EC2TagFilterTypeDef]] = None
    onPremisesInstanceTagFilters: Optional[List[TagFilterTypeDef]] = None
    autoScalingGroups: Optional[List[AutoScalingGroupTypeDef]] = None
    serviceRoleArn: Optional[str] = None
    targetRevision: Optional[RevisionLocationTypeDef] = None
    triggerConfigurations: Optional[List[TriggerConfigOutputTypeDef]] = None
    alarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationOutputTypeDef] = None
    deploymentStyle: Optional[DeploymentStyleTypeDef] = None
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategyType] = None
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfigurationTypeDef] = None
    loadBalancerInfo: Optional[LoadBalancerInfoOutputTypeDef] = None
    lastSuccessfulDeployment: Optional[LastDeploymentInfoTypeDef] = None
    lastAttemptedDeployment: Optional[LastDeploymentInfoTypeDef] = None
    ec2TagSet: Optional[EC2TagSetOutputTypeDef] = None
    onPremisesTagSet: Optional[OnPremisesTagSetOutputTypeDef] = None
    computePlatform: Optional[ComputePlatformType] = None
    ecsServices: Optional[List[ECSServiceTypeDef]] = None
    terminationHookEnabled: Optional[bool] = None

class DeploymentInfoTypeDef(BaseModel):
    applicationName: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    deploymentId: Optional[str] = None
    previousRevision: Optional[RevisionLocationTypeDef] = None
    revision: Optional[RevisionLocationTypeDef] = None
    status: Optional[DeploymentStatusType] = None
    errorInformation: Optional[ErrorInformationTypeDef] = None
    createTime: Optional[datetime] = None
    startTime: Optional[datetime] = None
    completeTime: Optional[datetime] = None
    deploymentOverview: Optional[DeploymentOverviewTypeDef] = None
    description: Optional[str] = None
    creator: Optional[DeploymentCreatorType] = None
    ignoreApplicationStopFailures: Optional[bool] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationOutputTypeDef] = None
    updateOutdatedInstancesOnly: Optional[bool] = None
    rollbackInfo: Optional[RollbackInfoTypeDef] = None
    deploymentStyle: Optional[DeploymentStyleTypeDef] = None
    targetInstances: Optional[TargetInstancesOutputTypeDef] = None
    instanceTerminationWaitTimeStarted: Optional[bool] = None
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfigurationTypeDef] = None
    loadBalancerInfo: Optional[LoadBalancerInfoOutputTypeDef] = None
    additionalDeploymentStatusInfo: Optional[str] = None
    fileExistsBehavior: Optional[FileExistsBehaviorType] = None
    deploymentStatusMessages: Optional[List[str]] = None
    computePlatform: Optional[ComputePlatformType] = None
    externalId: Optional[str] = None
    relatedDeployments: Optional[RelatedDeploymentsTypeDef] = None
    overrideAlarmConfiguration: Optional[AlarmConfigurationOutputTypeDef] = None

class CreateDeploymentGroupInputRequestTypeDef(BaseModel):
    applicationName: str
    deploymentGroupName: str
    serviceRoleArn: str
    deploymentConfigName: Optional[str] = None
    ec2TagFilters: Optional[Sequence[EC2TagFilterTypeDef]] = None
    onPremisesInstanceTagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    autoScalingGroups: Optional[Sequence[str]] = None
    triggerConfigurations: Optional[Sequence[TriggerConfigUnionTypeDef]] = None
    alarmConfiguration: Optional[AlarmConfigurationTypeDef] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationTypeDef] = None
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategyType] = None
    deploymentStyle: Optional[DeploymentStyleTypeDef] = None
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfigurationTypeDef] = None
    loadBalancerInfo: Optional[LoadBalancerInfoTypeDef] = None
    ec2TagSet: Optional[EC2TagSetTypeDef] = None
    ecsServices: Optional[Sequence[ECSServiceTypeDef]] = None
    onPremisesTagSet: Optional[OnPremisesTagSetTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    terminationHookEnabled: Optional[bool] = None

class UpdateDeploymentGroupInputRequestTypeDef(BaseModel):
    applicationName: str
    currentDeploymentGroupName: str
    newDeploymentGroupName: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    ec2TagFilters: Optional[Sequence[EC2TagFilterTypeDef]] = None
    onPremisesInstanceTagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    autoScalingGroups: Optional[Sequence[str]] = None
    serviceRoleArn: Optional[str] = None
    triggerConfigurations: Optional[Sequence[TriggerConfigUnionTypeDef]] = None
    alarmConfiguration: Optional[AlarmConfigurationTypeDef] = None
    autoRollbackConfiguration: Optional[AutoRollbackConfigurationTypeDef] = None
    outdatedInstancesStrategy: Optional[OutdatedInstancesStrategyType] = None
    deploymentStyle: Optional[DeploymentStyleTypeDef] = None
    blueGreenDeploymentConfiguration: Optional[BlueGreenDeploymentConfigurationTypeDef] = None
    loadBalancerInfo: Optional[LoadBalancerInfoTypeDef] = None
    ec2TagSet: Optional[EC2TagSetTypeDef] = None
    ecsServices: Optional[Sequence[ECSServiceTypeDef]] = None
    onPremisesTagSet: Optional[OnPremisesTagSetTypeDef] = None
    terminationHookEnabled: Optional[bool] = None

class GetDeploymentConfigOutputTypeDef(BaseModel):
    deploymentConfigInfo: DeploymentConfigInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetDeploymentTargetsOutputTypeDef(BaseModel):
    deploymentTargets: List[DeploymentTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentTargetOutputTypeDef(BaseModel):
    deploymentTarget: DeploymentTargetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetDeploymentGroupsOutputTypeDef(BaseModel):
    deploymentGroupsInfo: List[DeploymentGroupInfoTypeDef]
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentGroupOutputTypeDef(BaseModel):
    deploymentGroupInfo: DeploymentGroupInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetDeploymentsOutputTypeDef(BaseModel):
    deploymentsInfo: List[DeploymentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentOutputTypeDef(BaseModel):
    deploymentInfo: DeploymentInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AlarmTypeDef(BaseValidatorModel):
    name: Optional[str] = None

class AppSpecContentTypeDef(BaseValidatorModel):
    content: Optional[str] = None
    sha256: Optional[str] = None

class ApplicationInfoTypeDef(BaseValidatorModel):
    applicationId: Optional[str] = None
    applicationName: Optional[str] = None
    createTime: Optional[datetime] = None
    linkedToGitHub: Optional[bool] = None
    gitHubAccountName: Optional[str] = None
    computePlatform: Optional[ComputePlatformType] = None

class AutoRollbackConfigurationOutputTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    events: Optional[List[AutoRollbackEventType]] = None

class AutoRollbackConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    events: Optional[Sequence[AutoRollbackEventType]] = None

class AutoScalingGroupTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    hook: Optional[str] = None
    terminationHook: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchGetApplicationsInputRequestTypeDef(BaseValidatorModel):
    applicationNames: Sequence[str]

class BatchGetDeploymentGroupsInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    deploymentGroupNames: Sequence[str]

class BatchGetDeploymentInstancesInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str
    instanceIds: Sequence[str]

class BatchGetDeploymentTargetsInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str
    targetIds: Sequence[str]

class BatchGetDeploymentsInputRequestTypeDef(BaseValidatorModel):
    deploymentIds: Sequence[str]

class BatchGetOnPremisesInstancesInputRequestTypeDef(BaseValidatorModel):
    instanceNames: Sequence[str]

class BlueInstanceTerminationOptionTypeDef(BaseValidatorModel):
    action: Optional[InstanceActionType] = None
    terminationWaitTimeInMinutes: Optional[int] = None

class DeploymentReadyOptionTypeDef(BaseValidatorModel):
    actionOnTimeout: Optional[DeploymentReadyActionType] = None
    waitTimeInMinutes: Optional[int] = None

class GreenFleetProvisioningOptionTypeDef(BaseValidatorModel):
    action: Optional[GreenFleetProvisioningActionType] = None

class ContinueDeploymentInputRequestTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    deploymentWaitType: Optional[DeploymentWaitTypeType] = None

class MinimumHealthyHostsTypeDef(BaseValidatorModel):
    type: Optional[MinimumHealthyHostsTypeType] = None
    value: Optional[int] = None

class DeploymentStyleTypeDef(BaseValidatorModel):
    deploymentType: Optional[DeploymentTypeType] = None
    deploymentOption: Optional[DeploymentOptionType] = None

class EC2TagFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Type: Optional[EC2TagFilterTypeType] = None

class ECSServiceTypeDef(BaseValidatorModel):
    serviceName: Optional[str] = None
    clusterName: Optional[str] = None

class TagFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Type: Optional[TagFilterTypeType] = None

class DeleteApplicationInputRequestTypeDef(BaseValidatorModel):
    applicationName: str

class DeleteDeploymentConfigInputRequestTypeDef(BaseValidatorModel):
    deploymentConfigName: str

class DeleteDeploymentGroupInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    deploymentGroupName: str

class DeleteGitHubAccountTokenInputRequestTypeDef(BaseValidatorModel):
    tokenName: Optional[str] = None

class DeleteResourcesByExternalIdInputRequestTypeDef(BaseValidatorModel):
    externalId: Optional[str] = None

class LastDeploymentInfoTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    status: Optional[DeploymentStatusType] = None
    endTime: Optional[datetime] = None
    createTime: Optional[datetime] = None

class TriggerConfigOutputTypeDef(BaseValidatorModel):
    triggerName: Optional[str] = None
    triggerTargetArn: Optional[str] = None
    triggerEvents: Optional[List[TriggerEventTypeType]] = None

class DeploymentOverviewTypeDef(BaseValidatorModel):
    Pending: Optional[int] = None
    InProgress: Optional[int] = None
    Succeeded: Optional[int] = None
    Failed: Optional[int] = None
    Skipped: Optional[int] = None
    Ready: Optional[int] = None

class ErrorInformationTypeDef(BaseValidatorModel):
    code: Optional[ErrorCodeType] = None
    message: Optional[str] = None

class RelatedDeploymentsTypeDef(BaseValidatorModel):
    autoUpdateOutdatedInstancesRootDeploymentId: Optional[str] = None
    autoUpdateOutdatedInstancesDeploymentIds: Optional[List[str]] = None

class RollbackInfoTypeDef(BaseValidatorModel):
    rollbackDeploymentId: Optional[str] = None
    rollbackTriggeringDeploymentId: Optional[str] = None
    rollbackMessage: Optional[str] = None

class DeregisterOnPremisesInstanceInputRequestTypeDef(BaseValidatorModel):
    instanceName: str

class DiagnosticsTypeDef(BaseValidatorModel):
    errorCode: Optional[LifecycleErrorCodeType] = None
    scriptName: Optional[str] = None
    message: Optional[str] = None
    logTail: Optional[str] = None

class TargetGroupInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None

class ELBInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None

class GenericRevisionInfoTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    deploymentGroups: Optional[List[str]] = None
    firstUsedTime: Optional[datetime] = None
    lastUsedTime: Optional[datetime] = None
    registerTime: Optional[datetime] = None

class GetApplicationInputRequestTypeDef(BaseValidatorModel):
    applicationName: str

class GetDeploymentConfigInputRequestTypeDef(BaseValidatorModel):
    deploymentConfigName: str

class GetDeploymentGroupInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    deploymentGroupName: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class GetDeploymentInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str

class GetDeploymentInstanceInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str
    instanceId: str

class GetDeploymentTargetInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str
    targetId: str

class GetOnPremisesInstanceInputRequestTypeDef(BaseValidatorModel):
    instanceName: str

class GitHubLocationTypeDef(BaseValidatorModel):
    repository: Optional[str] = None
    commitId: Optional[str] = None

class LambdaFunctionInfoTypeDef(BaseValidatorModel):
    functionName: Optional[str] = None
    functionAlias: Optional[str] = None
    currentVersion: Optional[str] = None
    targetVersion: Optional[str] = None
    targetVersionWeight: Optional[float] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationRevisionsInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    sortBy: Optional[ApplicationRevisionSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    s3Bucket: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    deployed: Optional[ListStateFilterActionType] = None
    nextToken: Optional[str] = None

class ListApplicationsInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ListDeploymentConfigsInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ListDeploymentGroupsInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    nextToken: Optional[str] = None

class ListDeploymentInstancesInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str
    nextToken: Optional[str] = None
    instanceStatusFilter: Optional[Sequence[InstanceStatusType]] = None
    instanceTypeFilter: Optional[Sequence[InstanceTypeType]] = None

class ListDeploymentTargetsInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str
    nextToken: Optional[str] = None
    targetFilters: Optional[Mapping[TargetFilterNameType, Sequence[str]]] = None

class ListGitHubAccountTokenNamesInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None

class MinimumHealthyHostsPerZoneTypeDef(BaseValidatorModel):
    type: Optional[MinimumHealthyHostsPerZoneTypeType] = None
    value: Optional[int] = None

class PutLifecycleEventHookExecutionStatusInputRequestTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    lifecycleEventHookExecutionId: Optional[str] = None
    status: Optional[LifecycleEventStatusType] = None

class RawStringTypeDef(BaseValidatorModel):
    content: Optional[str] = None
    sha256: Optional[str] = None

class RegisterOnPremisesInstanceInputRequestTypeDef(BaseValidatorModel):
    instanceName: str
    iamSessionArn: Optional[str] = None
    iamUserArn: Optional[str] = None

class S3LocationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None
    bundleType: Optional[BundleTypeType] = None
    version: Optional[str] = None
    eTag: Optional[str] = None

class SkipWaitTimeForInstanceTerminationInputRequestTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None

class StopDeploymentInputRequestTypeDef(BaseValidatorModel):
    deploymentId: str
    autoRollbackEnabled: Optional[bool] = None

class TrafficRouteOutputTypeDef(BaseValidatorModel):
    listenerArns: Optional[List[str]] = None

class TrafficRouteTypeDef(BaseValidatorModel):
    listenerArns: Optional[Sequence[str]] = None

class TimeBasedCanaryTypeDef(BaseValidatorModel):
    canaryPercentage: Optional[int] = None
    canaryInterval: Optional[int] = None

class TimeBasedLinearTypeDef(BaseValidatorModel):
    linearPercentage: Optional[int] = None
    linearInterval: Optional[int] = None

class TriggerConfigTypeDef(BaseValidatorModel):
    triggerName: Optional[str] = None
    triggerTargetArn: Optional[str] = None
    triggerEvents: Optional[Sequence[TriggerEventTypeType]] = None

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateApplicationInputRequestTypeDef(BaseValidatorModel):
    applicationName: Optional[str] = None
    newApplicationName: Optional[str] = None

class AddTagsToOnPremisesInstancesInputRequestTypeDef(BaseValidatorModel):
    tags: Sequence[TagTypeDef]
    instanceNames: Sequence[str]

class CreateApplicationInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    computePlatform: Optional[ComputePlatformType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class InstanceInfoTypeDef(BaseValidatorModel):
    instanceName: Optional[str] = None
    iamSessionArn: Optional[str] = None
    iamUserArn: Optional[str] = None
    instanceArn: Optional[str] = None
    registerTime: Optional[datetime] = None
    deregisterTime: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None

class RemoveTagsFromOnPremisesInstancesInputRequestTypeDef(BaseValidatorModel):
    tags: Sequence[TagTypeDef]
    instanceNames: Sequence[str]

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class AlarmConfigurationOutputTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    ignorePollAlarmFailure: Optional[bool] = None
    alarms: Optional[List[AlarmTypeDef]] = None

class AlarmConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    ignorePollAlarmFailure: Optional[bool] = None
    alarms: Optional[Sequence[AlarmTypeDef]] = None

class BatchGetApplicationsOutputTypeDef(BaseValidatorModel):
    applicationsInfo: List[ApplicationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationOutputTypeDef(BaseValidatorModel):
    applicationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentConfigOutputTypeDef(BaseValidatorModel):
    deploymentConfigId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentGroupOutputTypeDef(BaseValidatorModel):
    deploymentGroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentOutputTypeDef(BaseValidatorModel):
    deploymentId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeploymentGroupOutputTypeDef(BaseValidatorModel):
    hooksNotCleanedUp: List[AutoScalingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGitHubAccountTokenOutputTypeDef(BaseValidatorModel):
    tokenName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationOutputTypeDef(BaseValidatorModel):
    application: ApplicationInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsOutputTypeDef(BaseValidatorModel):
    applications: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentConfigsOutputTypeDef(BaseValidatorModel):
    deploymentConfigsList: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentGroupsOutputTypeDef(BaseValidatorModel):
    applicationName: str
    deploymentGroups: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentInstancesOutputTypeDef(BaseValidatorModel):
    instancesList: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentTargetsOutputTypeDef(BaseValidatorModel):
    targetIds: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeploymentsOutputTypeDef(BaseValidatorModel):
    deployments: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListGitHubAccountTokenNamesOutputTypeDef(BaseValidatorModel):
    tokenNameList: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOnPremisesInstancesOutputTypeDef(BaseValidatorModel):
    instanceNames: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutLifecycleEventHookExecutionStatusOutputTypeDef(BaseValidatorModel):
    lifecycleEventHookExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopDeploymentOutputTypeDef(BaseValidatorModel):
    status: StopStatusType
    statusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeploymentGroupOutputTypeDef(BaseValidatorModel):
    hooksNotCleanedUp: List[AutoScalingGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BlueGreenDeploymentConfigurationTypeDef(BaseValidatorModel):
    terminateBlueInstancesOnDeploymentSuccess: Optional[       BlueInstanceTerminationOptionTypeDef     ] = None
    deploymentReadyOption: Optional[DeploymentReadyOptionTypeDef] = None
    greenFleetProvisioningOption: Optional[GreenFleetProvisioningOptionTypeDef] = None

class EC2TagSetOutputTypeDef(BaseValidatorModel):
    ec2TagSetList: Optional[List[List[EC2TagFilterTypeDef]]] = None

class EC2TagSetTypeDef(BaseValidatorModel):
    ec2TagSetList: Optional[Sequence[Sequence[EC2TagFilterTypeDef]]] = None

class ListOnPremisesInstancesInputRequestTypeDef(BaseValidatorModel):
    registrationStatus: Optional[RegistrationStatusType] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    nextToken: Optional[str] = None

class OnPremisesTagSetOutputTypeDef(BaseValidatorModel):
    onPremisesTagSetList: Optional[List[List[TagFilterTypeDef]]] = None

class OnPremisesTagSetTypeDef(BaseValidatorModel):
    onPremisesTagSetList: Optional[Sequence[Sequence[TagFilterTypeDef]]] = None

class LifecycleEventTypeDef(BaseValidatorModel):
    lifecycleEventName: Optional[str] = None
    diagnostics: Optional[DiagnosticsTypeDef] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    status: Optional[LifecycleEventStatusType] = None

class ECSTaskSetTypeDef(BaseValidatorModel):
    identifer: Optional[str] = None
    desiredCount: Optional[int] = None
    pendingCount: Optional[int] = None
    runningCount: Optional[int] = None
    status: Optional[str] = None
    trafficWeight: Optional[float] = None
    targetGroup: Optional[TargetGroupInfoTypeDef] = None
    taskSetLabel: Optional[TargetLabelType] = None

class GetDeploymentInputDeploymentSuccessfulWaitTypeDef(BaseValidatorModel):
    deploymentId: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class ListApplicationRevisionsInputListApplicationRevisionsPaginateTypeDef(BaseValidatorModel):
    applicationName: str
    sortBy: Optional[ApplicationRevisionSortByType] = None
    sortOrder: Optional[SortOrderType] = None
    s3Bucket: Optional[str] = None
    s3KeyPrefix: Optional[str] = None
    deployed: Optional[ListStateFilterActionType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsInputListApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentConfigsInputListDeploymentConfigsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentGroupsInputListDeploymentGroupsPaginateTypeDef(BaseValidatorModel):
    applicationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentInstancesInputListDeploymentInstancesPaginateTypeDef(BaseValidatorModel):
    deploymentId: str
    instanceStatusFilter: Optional[Sequence[InstanceStatusType]] = None
    instanceTypeFilter: Optional[Sequence[InstanceTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentTargetsInputListDeploymentTargetsPaginateTypeDef(BaseValidatorModel):
    deploymentId: str
    targetFilters: Optional[Mapping[TargetFilterNameType, Sequence[str]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGitHubAccountTokenNamesInputListGitHubAccountTokenNamesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOnPremisesInstancesInputListOnPremisesInstancesPaginateTypeDef(BaseValidatorModel):
    registrationStatus: Optional[RegistrationStatusType] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ZonalConfigTypeDef(BaseValidatorModel):
    firstZoneMonitorDurationInSeconds: Optional[int] = None
    monitorDurationInSeconds: Optional[int] = None
    minimumHealthyHostsPerZone: Optional[MinimumHealthyHostsPerZoneTypeDef] = None

class RevisionLocationTypeDef(BaseValidatorModel):
    revisionType: Optional[RevisionLocationTypeType] = None
    s3Location: Optional[S3LocationTypeDef] = None
    gitHubLocation: Optional[GitHubLocationTypeDef] = None
    string: Optional[RawStringTypeDef] = None
    appSpecContent: Optional[AppSpecContentTypeDef] = None

class TargetGroupPairInfoOutputTypeDef(BaseValidatorModel):
    targetGroups: Optional[List[TargetGroupInfoTypeDef]] = None
    prodTrafficRoute: Optional[TrafficRouteOutputTypeDef] = None
    testTrafficRoute: Optional[TrafficRouteOutputTypeDef] = None

class TargetGroupPairInfoTypeDef(BaseValidatorModel):
    targetGroups: Optional[Sequence[TargetGroupInfoTypeDef]] = None
    prodTrafficRoute: Optional[TrafficRouteTypeDef] = None
    testTrafficRoute: Optional[TrafficRouteTypeDef] = None

class TrafficRoutingConfigTypeDef(BaseValidatorModel):
    type: Optional[TrafficRoutingTypeType] = None
    timeBasedCanary: Optional[TimeBasedCanaryTypeDef] = None
    timeBasedLinear: Optional[TimeBasedLinearTypeDef] = None

class TimeRangeTypeDef(BaseValidatorModel):
    start: Optional[TimestampTypeDef] = None
    end: Optional[TimestampTypeDef] = None

class BatchGetOnPremisesInstancesOutputTypeDef(BaseValidatorModel):
    instanceInfos: List[InstanceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOnPremisesInstanceOutputTypeDef(BaseValidatorModel):
    instanceInfo: InstanceInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TargetInstancesOutputTypeDef(BaseValidatorModel):
    tagFilters: Optional[List[EC2TagFilterTypeDef]] = None
    autoScalingGroups: Optional[List[str]] = None
    ec2TagSet: Optional[EC2TagSetOutputTypeDef] = None

class TargetInstancesTypeDef(BaseValidatorModel):
    tagFilters: Optional[Sequence[EC2TagFilterTypeDef]] = None
    autoScalingGroups: Optional[Sequence[str]] = None
    ec2TagSet: Optional[EC2TagSetTypeDef] = None

class CloudFormationTargetTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    status: Optional[TargetStatusType] = None
    resourceType: Optional[str] = None
    targetVersionWeight: Optional[float] = None

class InstanceSummaryTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    instanceId: Optional[str] = None
    status: Optional[InstanceStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    instanceType: Optional[InstanceTypeType] = None

class InstanceTargetTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[TargetStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    instanceLabel: Optional[TargetLabelType] = None

class LambdaTargetTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    status: Optional[TargetStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    lambdaFunctionInfo: Optional[LambdaFunctionInfoTypeDef] = None

class ECSTargetTypeDef(BaseValidatorModel):
    deploymentId: Optional[str] = None
    targetId: Optional[str] = None
    targetArn: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    lifecycleEvents: Optional[List[LifecycleEventTypeDef]] = None
    status: Optional[TargetStatusType] = None
    taskSetsInfo: Optional[List[ECSTaskSetTypeDef]] = None

class BatchGetApplicationRevisionsInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    revisions: Sequence[RevisionLocationTypeDef]

class GetApplicationRevisionInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    revision: RevisionLocationTypeDef

class GetApplicationRevisionOutputTypeDef(BaseValidatorModel):
    applicationName: str
    revision: RevisionLocationTypeDef
    revisionInfo: GenericRevisionInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationRevisionsOutputTypeDef(BaseValidatorModel):
    revisions: List[RevisionLocationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterApplicationRevisionInputRequestTypeDef(BaseValidatorModel):
    applicationName: str
    revision: RevisionLocationTypeDef
    description: Optional[str] = None

class RevisionInfoTypeDef(BaseValidatorModel):
    revisionLocation: Optional[RevisionLocationTypeDef] = None
    genericRevisionInfo: Optional[GenericRevisionInfoTypeDef] = None

class LoadBalancerInfoOutputTypeDef(BaseValidatorModel):
    elbInfoList: Optional[List[ELBInfoTypeDef]] = None
    targetGroupInfoList: Optional[List[TargetGroupInfoTypeDef]] = None
    targetGroupPairInfoList: Optional[List[TargetGroupPairInfoOutputTypeDef]] = None

class LoadBalancerInfoTypeDef(BaseValidatorModel):
    elbInfoList: Optional[Sequence[ELBInfoTypeDef]] = None
    targetGroupInfoList: Optional[Sequence[TargetGroupInfoTypeDef]] = None
    targetGroupPairInfoList: Optional[Sequence[TargetGroupPairInfoTypeDef]] = None

class CreateDeploymentConfigInputRequestTypeDef(BaseValidatorModel):
    deploymentConfigName: str
    minimumHealthyHosts: Optional[MinimumHealthyHostsTypeDef] = None
    trafficRoutingConfig: Optional[TrafficRoutingConfigTypeDef] = None
    computePlatform: Optional[ComputePlatformType] = None
    zonalConfig: Optional[ZonalConfigTypeDef] = None

class DeploymentConfigInfoTypeDef(BaseValidatorModel):
    deploymentConfigId: Optional[str] = None
    deploymentConfigName: Optional[str] = None
    minimumHealthyHosts: Optional[MinimumHealthyHostsTypeDef] = None
    createTime: Optional[datetime] = None
    computePlatform: Optional[ComputePlatformType] = None
    trafficRoutingConfig: Optional[TrafficRoutingConfigTypeDef] = None
    zonalConfig: Optional[ZonalConfigTypeDef] = None

class ListDeploymentsInputListDeploymentsPaginateTypeDef(BaseValidatorModel):
    applicationName: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    externalId: Optional[str] = None
    includeOnlyStatuses: Optional[Sequence[DeploymentStatusType]] = None
    createTimeRange: Optional[TimeRangeTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsInputRequestTypeDef(BaseValidatorModel):
    applicationName: Optional[str] = None
    deploymentGroupName: Optional[str] = None
    externalId: Optional[str] = None
    includeOnlyStatuses: Optional[Sequence[DeploymentStatusType]] = None
    createTimeRange: Optional[TimeRangeTypeDef] = None
    nextToken: Optional[str] = None

class CreateDeploymentInputRequestTypeDef(BaseValidatorModel):
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

class BatchGetDeploymentInstancesOutputTypeDef(BaseValidatorModel):
    instancesSummary: List[InstanceSummaryTypeDef]
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentInstanceOutputTypeDef(BaseValidatorModel):
    instanceSummary: InstanceSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentTargetTypeDef(BaseValidatorModel):
    deploymentTargetType: Optional[DeploymentTargetTypeType] = None
    instanceTarget: Optional[InstanceTargetTypeDef] = None
    lambdaTarget: Optional[LambdaTargetTypeDef] = None
    ecsTarget: Optional[ECSTargetTypeDef] = None
    cloudFormationTarget: Optional[CloudFormationTargetTypeDef] = None

class BatchGetApplicationRevisionsOutputTypeDef(BaseValidatorModel):
    applicationName: str
    errorMessage: str
    revisions: List[RevisionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentGroupInfoTypeDef(BaseValidatorModel):
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

class DeploymentInfoTypeDef(BaseValidatorModel):
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

class CreateDeploymentGroupInputRequestTypeDef(BaseValidatorModel):
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

class UpdateDeploymentGroupInputRequestTypeDef(BaseValidatorModel):
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

class GetDeploymentConfigOutputTypeDef(BaseValidatorModel):
    deploymentConfigInfo: DeploymentConfigInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetDeploymentTargetsOutputTypeDef(BaseValidatorModel):
    deploymentTargets: List[DeploymentTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentTargetOutputTypeDef(BaseValidatorModel):
    deploymentTarget: DeploymentTargetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetDeploymentGroupsOutputTypeDef(BaseValidatorModel):
    deploymentGroupsInfo: List[DeploymentGroupInfoTypeDef]
    errorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentGroupOutputTypeDef(BaseValidatorModel):
    deploymentGroupInfo: DeploymentGroupInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetDeploymentsOutputTypeDef(BaseValidatorModel):
    deploymentsInfo: List[DeploymentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeploymentOutputTypeDef(BaseValidatorModel):
    deploymentInfo: DeploymentInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


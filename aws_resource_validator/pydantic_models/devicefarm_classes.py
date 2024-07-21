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
from aws_resource_validator.pydantic_models.devicefarm_constants import *

class TrialMinutesTypeDef(BaseModel):
    total: Optional[float] = None
    remaining: Optional[float] = None

class ArtifactTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[ArtifactTypeType] = None
    extension: Optional[str] = None
    url: Optional[str] = None

class CPUTypeDef(BaseModel):
    frequency: Optional[str] = None
    architecture: Optional[str] = None
    clock: Optional[float] = None

class CountersTypeDef(BaseModel):
    total: Optional[int] = None
    passed: Optional[int] = None
    failed: Optional[int] = None
    warned: Optional[int] = None
    errored: Optional[int] = None
    stopped: Optional[int] = None
    skipped: Optional[int] = None

class RuleTypeDef(BaseModel):
    attribute: Optional[DeviceAttributeType] = None
    operator: Optional[RuleOperatorType] = None
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateInstanceProfileRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[Sequence[str]] = None
    rebootAfterUse: Optional[bool] = None

class InstanceProfileTypeDef(BaseModel):
    arn: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[List[str]] = None
    rebootAfterUse: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None

class CreateNetworkProfileRequestRequestTypeDef(BaseModel):
    projectArn: str
    name: str
    description: Optional[str] = None
    type: Optional[NetworkProfileTypeType] = None
    uplinkBandwidthBits: Optional[int] = None
    downlinkBandwidthBits: Optional[int] = None
    uplinkDelayMs: Optional[int] = None
    downlinkDelayMs: Optional[int] = None
    uplinkJitterMs: Optional[int] = None
    downlinkJitterMs: Optional[int] = None
    uplinkLossPercent: Optional[int] = None
    downlinkLossPercent: Optional[int] = None

class NetworkProfileTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[NetworkProfileTypeType] = None
    uplinkBandwidthBits: Optional[int] = None
    downlinkBandwidthBits: Optional[int] = None
    uplinkDelayMs: Optional[int] = None
    downlinkDelayMs: Optional[int] = None
    uplinkJitterMs: Optional[int] = None
    downlinkJitterMs: Optional[int] = None
    uplinkLossPercent: Optional[int] = None
    downlinkLossPercent: Optional[int] = None

class VpcConfigTypeDef(BaseModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str

class CreateRemoteAccessSessionConfigurationTypeDef(BaseModel):
    billingMethod: Optional[BillingMethodType] = None
    vpceConfigurationArns: Optional[Sequence[str]] = None

class TestGridVpcConfigTypeDef(BaseModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str

class CreateTestGridUrlRequestRequestTypeDef(BaseModel):
    projectArn: str
    expiresInSeconds: int

class CreateUploadRequestRequestTypeDef(BaseModel):
    projectArn: str
    name: str
    type: UploadTypeType
    contentType: Optional[str] = None

class UploadTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    created: Optional[datetime] = None
    type: Optional[UploadTypeType] = None
    status: Optional[UploadStatusType] = None
    url: Optional[str] = None
    metadata: Optional[str] = None
    contentType: Optional[str] = None
    message: Optional[str] = None
    category: Optional[UploadCategoryType] = None

class CreateVPCEConfigurationRequestRequestTypeDef(BaseModel):
    vpceConfigurationName: str
    vpceServiceName: str
    serviceDnsName: str
    vpceConfigurationDescription: Optional[str] = None

class VPCEConfigurationTypeDef(BaseModel):
    arn: Optional[str] = None
    vpceConfigurationName: Optional[str] = None
    vpceServiceName: Optional[str] = None
    serviceDnsName: Optional[str] = None
    vpceConfigurationDescription: Optional[str] = None

class CustomerArtifactPathsOutputTypeDef(BaseModel):
    iosPaths: Optional[List[str]] = None
    androidPaths: Optional[List[str]] = None
    deviceHostPaths: Optional[List[str]] = None

class CustomerArtifactPathsTypeDef(BaseModel):
    iosPaths: Optional[Sequence[str]] = None
    androidPaths: Optional[Sequence[str]] = None
    deviceHostPaths: Optional[Sequence[str]] = None

class DeleteDevicePoolRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteInstanceProfileRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteNetworkProfileRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteProjectRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteRemoteAccessSessionRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteRunRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteTestGridProjectRequestRequestTypeDef(BaseModel):
    projectArn: str

class DeleteUploadRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteVPCEConfigurationRequestRequestTypeDef(BaseModel):
    arn: str

class DeviceFilterExtraOutputTypeDef(BaseModel):
    attribute: DeviceFilterAttributeType
    operator: RuleOperatorType
    values: List[str]

class DeviceFilterOutputTypeDef(BaseModel):
    attribute: DeviceFilterAttributeType
    operator: RuleOperatorType
    values: List[str]

class DeviceFilterTypeDef(BaseModel):
    attribute: DeviceFilterAttributeType
    operator: RuleOperatorType
    values: Sequence[str]

class DeviceMinutesTypeDef(BaseModel):
    total: Optional[float] = None
    metered: Optional[float] = None
    unmetered: Optional[float] = None

class IncompatibilityMessageTypeDef(BaseModel):
    message: Optional[str] = None
    type: Optional[DeviceAttributeType] = None

class ResolutionTypeDef(BaseModel):
    width: Optional[int] = None
    height: Optional[int] = None

class ExecutionConfigurationTypeDef(BaseModel):
    jobTimeoutMinutes: Optional[int] = None
    accountsCleanup: Optional[bool] = None
    appPackagesCleanup: Optional[bool] = None
    videoCapture: Optional[bool] = None
    skipAppResign: Optional[bool] = None

class GetDeviceInstanceRequestRequestTypeDef(BaseModel):
    arn: str

class ScheduleRunTestTypeDef(BaseModel):
    type: TestTypeType
    testPackageArn: Optional[str] = None
    testSpecArn: Optional[str] = None
    filter: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None

class GetDevicePoolRequestRequestTypeDef(BaseModel):
    arn: str

class GetDeviceRequestRequestTypeDef(BaseModel):
    arn: str

class GetInstanceProfileRequestRequestTypeDef(BaseModel):
    arn: str

class GetJobRequestRequestTypeDef(BaseModel):
    arn: str

class GetNetworkProfileRequestRequestTypeDef(BaseModel):
    arn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetOfferingStatusRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class GetProjectRequestRequestTypeDef(BaseModel):
    arn: str

class GetRemoteAccessSessionRequestRequestTypeDef(BaseModel):
    arn: str

class GetRunRequestRequestTypeDef(BaseModel):
    arn: str

class GetSuiteRequestRequestTypeDef(BaseModel):
    arn: str

class GetTestGridProjectRequestRequestTypeDef(BaseModel):
    projectArn: str

class GetTestGridSessionRequestRequestTypeDef(BaseModel):
    projectArn: Optional[str] = None
    sessionId: Optional[str] = None
    sessionArn: Optional[str] = None

class TestGridSessionTypeDef(BaseModel):
    arn: Optional[str] = None
    status: Optional[TestGridSessionStatusType] = None
    created: Optional[datetime] = None
    ended: Optional[datetime] = None
    billingMinutes: Optional[float] = None
    seleniumProperties: Optional[str] = None

class GetTestRequestRequestTypeDef(BaseModel):
    arn: str

class GetUploadRequestRequestTypeDef(BaseModel):
    arn: str

class GetVPCEConfigurationRequestRequestTypeDef(BaseModel):
    arn: str

class InstallToRemoteAccessSessionRequestRequestTypeDef(BaseModel):
    remoteAccessSessionArn: str
    appArn: str

class ListArtifactsRequestRequestTypeDef(BaseModel):
    arn: str
    type: ArtifactCategoryType
    nextToken: Optional[str] = None

class ListDeviceInstancesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDevicePoolsRequestRequestTypeDef(BaseModel):
    arn: str
    type: Optional[DevicePoolTypeType] = None
    nextToken: Optional[str] = None

class ListInstanceProfilesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    arn: str
    nextToken: Optional[str] = None

class ListNetworkProfilesRequestRequestTypeDef(BaseModel):
    arn: str
    type: Optional[NetworkProfileTypeType] = None
    nextToken: Optional[str] = None

class ListOfferingPromotionsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class OfferingPromotionTypeDef(BaseModel):
    id: Optional[str] = None
    description: Optional[str] = None

class ListOfferingTransactionsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ListOfferingsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None

class ListProjectsRequestRequestTypeDef(BaseModel):
    arn: Optional[str] = None
    nextToken: Optional[str] = None

class ListRemoteAccessSessionsRequestRequestTypeDef(BaseModel):
    arn: str
    nextToken: Optional[str] = None

class ListRunsRequestRequestTypeDef(BaseModel):
    arn: str
    nextToken: Optional[str] = None

class ListSamplesRequestRequestTypeDef(BaseModel):
    arn: str
    nextToken: Optional[str] = None

class SampleTypeDef(BaseModel):
    arn: Optional[str] = None
    type: Optional[SampleTypeType] = None
    url: Optional[str] = None

class ListSuitesRequestRequestTypeDef(BaseModel):
    arn: str
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ListTestGridProjectsRequestRequestTypeDef(BaseModel):
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None

class ListTestGridSessionActionsRequestRequestTypeDef(BaseModel):
    sessionArn: str
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None

class TestGridSessionActionTypeDef(BaseModel):
    action: Optional[str] = None
    started: Optional[datetime] = None
    duration: Optional[int] = None
    statusCode: Optional[str] = None
    requestMethod: Optional[str] = None

class ListTestGridSessionArtifactsRequestRequestTypeDef(BaseModel):
    sessionArn: str
    type: Optional[TestGridSessionArtifactCategoryType] = None
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None

class TestGridSessionArtifactTypeDef(BaseModel):
    filename: Optional[str] = None
    type: Optional[TestGridSessionArtifactTypeType] = None
    url: Optional[str] = None

class ListTestsRequestRequestTypeDef(BaseModel):
    arn: str
    nextToken: Optional[str] = None

class ListUniqueProblemsRequestRequestTypeDef(BaseModel):
    arn: str
    nextToken: Optional[str] = None

class ListUploadsRequestRequestTypeDef(BaseModel):
    arn: str
    type: Optional[UploadTypeType] = None
    nextToken: Optional[str] = None

class ListVPCEConfigurationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class LocationTypeDef(BaseModel):
    latitude: float
    longitude: float

class MonetaryAmountTypeDef(BaseModel):
    amount: Optional[float] = None
    currencyCode: Optional[Literal["USD"]] = None

class ProblemDetailTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None

class VpcConfigOutputTypeDef(BaseModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str

class PurchaseOfferingRequestRequestTypeDef(BaseModel):
    offeringId: str
    quantity: int
    offeringPromotionId: Optional[str] = None

class RadiosTypeDef(BaseModel):
    wifi: Optional[bool] = None
    bluetooth: Optional[bool] = None
    nfc: Optional[bool] = None
    gps: Optional[bool] = None

class RenewOfferingRequestRequestTypeDef(BaseModel):
    offeringId: str
    quantity: int

class StopJobRequestRequestTypeDef(BaseModel):
    arn: str

class StopRemoteAccessSessionRequestRequestTypeDef(BaseModel):
    arn: str

class StopRunRequestRequestTypeDef(BaseModel):
    arn: str

class TestGridVpcConfigOutputTypeDef(BaseModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateDeviceInstanceRequestRequestTypeDef(BaseModel):
    arn: str
    profileArn: Optional[str] = None
    labels: Optional[Sequence[str]] = None

class UpdateInstanceProfileRequestRequestTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[Sequence[str]] = None
    rebootAfterUse: Optional[bool] = None

class UpdateNetworkProfileRequestRequestTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[NetworkProfileTypeType] = None
    uplinkBandwidthBits: Optional[int] = None
    downlinkBandwidthBits: Optional[int] = None
    uplinkDelayMs: Optional[int] = None
    downlinkDelayMs: Optional[int] = None
    uplinkJitterMs: Optional[int] = None
    downlinkJitterMs: Optional[int] = None
    uplinkLossPercent: Optional[int] = None
    downlinkLossPercent: Optional[int] = None

class UpdateUploadRequestRequestTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    contentType: Optional[str] = None
    editContent: Optional[bool] = None

class UpdateVPCEConfigurationRequestRequestTypeDef(BaseModel):
    arn: str
    vpceConfigurationName: Optional[str] = None
    vpceServiceName: Optional[str] = None
    serviceDnsName: Optional[str] = None
    vpceConfigurationDescription: Optional[str] = None

class VpcConfigExtraOutputTypeDef(BaseModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str

class AccountSettingsTypeDef(BaseModel):
    awsAccountNumber: Optional[str] = None
    unmeteredDevices: Optional[Dict[DevicePlatformType, int]] = None
    unmeteredRemoteAccessDevices: Optional[Dict[DevicePlatformType, int]] = None
    maxJobTimeoutMinutes: Optional[int] = None
    trialMinutes: Optional[TrialMinutesTypeDef] = None
    maxSlots: Optional[Dict[str, int]] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    skipAppResign: Optional[bool] = None

class CreateDevicePoolRequestRequestTypeDef(BaseModel):
    projectArn: str
    name: str
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    maxDevices: Optional[int] = None

class DevicePoolTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[DevicePoolTypeType] = None
    rules: Optional[List[RuleTypeDef]] = None
    maxDevices: Optional[int] = None

class UpdateDevicePoolRequestRequestTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    rules: Optional[Sequence[RuleTypeDef]] = None
    maxDevices: Optional[int] = None
    clearMaxDevices: Optional[bool] = None

class CreateTestGridUrlResultTypeDef(BaseModel):
    url: str
    expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListArtifactsResultTypeDef(BaseModel):
    artifacts: List[ArtifactTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileResultTypeDef(BaseModel):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceInstanceTypeDef(BaseModel):
    arn: Optional[str] = None
    deviceArn: Optional[str] = None
    labels: Optional[List[str]] = None
    status: Optional[InstanceStatusType] = None
    udid: Optional[str] = None
    instanceProfile: Optional[InstanceProfileTypeDef] = None

class GetInstanceProfileResultTypeDef(BaseModel):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesResultTypeDef(BaseModel):
    instanceProfiles: List[InstanceProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInstanceProfileResultTypeDef(BaseModel):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkProfileResultTypeDef(BaseModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkProfileResultTypeDef(BaseModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkProfilesResultTypeDef(BaseModel):
    networkProfiles: List[NetworkProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkProfileResultTypeDef(BaseModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectRequestRequestTypeDef(BaseModel):
    name: str
    defaultJobTimeoutMinutes: Optional[int] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None

class UpdateProjectRequestRequestTypeDef(BaseModel):
    arn: str
    name: Optional[str] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None

class CreateRemoteAccessSessionRequestRequestTypeDef(BaseModel):
    projectArn: str
    deviceArn: str
    instanceArn: Optional[str] = None
    sshPublicKey: Optional[str] = None
    remoteDebugEnabled: Optional[bool] = None
    remoteRecordEnabled: Optional[bool] = None
    remoteRecordAppArn: Optional[str] = None
    name: Optional[str] = None
    clientId: Optional[str] = None
    configuration: Optional[CreateRemoteAccessSessionConfigurationTypeDef] = None
    interactionMode: Optional[InteractionModeType] = None
    skipAppResign: Optional[bool] = None

class CreateTestGridProjectRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigTypeDef] = None

class UpdateTestGridProjectRequestRequestTypeDef(BaseModel):
    projectArn: str
    name: Optional[str] = None
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigTypeDef] = None

class CreateUploadResultTypeDef(BaseModel):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUploadResultTypeDef(BaseModel):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstallToRemoteAccessSessionResultTypeDef(BaseModel):
    appUpload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUploadsResultTypeDef(BaseModel):
    uploads: List[UploadTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUploadResultTypeDef(BaseModel):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVPCEConfigurationResultTypeDef(BaseModel):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVPCEConfigurationResultTypeDef(BaseModel):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVPCEConfigurationsResultTypeDef(BaseModel):
    vpceConfigurations: List[VPCEConfigurationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVPCEConfigurationResultTypeDef(BaseModel):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceSelectionResultTypeDef(BaseModel):
    filters: Optional[List[DeviceFilterOutputTypeDef]] = None
    matchedDevicesCount: Optional[int] = None
    maxDevices: Optional[int] = None

class DeviceSelectionConfigurationTypeDef(BaseModel):
    filters: Sequence[DeviceFilterTypeDef]
    maxDevices: int

class SuiteTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[TestTypeType] = None
    created: Optional[datetime] = None
    status: Optional[ExecutionStatusType] = None
    result: Optional[ExecutionResultType] = None
    started: Optional[datetime] = None
    stopped: Optional[datetime] = None
    counters: Optional[CountersTypeDef] = None
    message: Optional[str] = None
    deviceMinutes: Optional[DeviceMinutesTypeDef] = None

class TestTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[TestTypeType] = None
    created: Optional[datetime] = None
    status: Optional[ExecutionStatusType] = None
    result: Optional[ExecutionResultType] = None
    started: Optional[datetime] = None
    stopped: Optional[datetime] = None
    counters: Optional[CountersTypeDef] = None
    message: Optional[str] = None
    deviceMinutes: Optional[DeviceMinutesTypeDef] = None

class GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArtifactsRequestListArtifactsPaginateTypeDef(BaseModel):
    arn: str
    type: ArtifactCategoryType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicePoolsRequestListDevicePoolsPaginateTypeDef(BaseModel):
    arn: str
    type: Optional[DevicePoolTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef(BaseModel):
    arn: str
    type: Optional[NetworkProfileTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingsRequestListOfferingsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    arn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef(BaseModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRunsRequestListRunsPaginateTypeDef(BaseModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSamplesRequestListSamplesPaginateTypeDef(BaseModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSuitesRequestListSuitesPaginateTypeDef(BaseModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTestsRequestListTestsPaginateTypeDef(BaseModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef(BaseModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUploadsRequestListUploadsPaginateTypeDef(BaseModel):
    arn: str
    type: Optional[UploadTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTestGridSessionResultTypeDef(BaseModel):
    testGridSession: TestGridSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridSessionsResultTypeDef(BaseModel):
    testGridSessions: List[TestGridSessionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingPromotionsResultTypeDef(BaseModel):
    offeringPromotions: List[OfferingPromotionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSamplesResultTypeDef(BaseModel):
    samples: List[SampleTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ListTestGridSessionActionsResultTypeDef(BaseModel):
    actions: List[TestGridSessionActionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridSessionArtifactsResultTypeDef(BaseModel):
    artifacts: List[TestGridSessionArtifactTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridSessionsRequestRequestTypeDef(BaseModel):
    projectArn: str
    status: Optional[TestGridSessionStatusType] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    endTimeAfter: Optional[TimestampTypeDef] = None
    endTimeBefore: Optional[TimestampTypeDef] = None
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None

class RecurringChargeTypeDef(BaseModel):
    cost: Optional[MonetaryAmountTypeDef] = None
    frequency: Optional[Literal["MONTHLY"]] = None

class ProjectTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    created: Optional[datetime] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None

class ScheduleRunConfigurationTypeDef(BaseModel):
    extraDataPackageArn: Optional[str] = None
    networkProfileArn: Optional[str] = None
    locale: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    vpceConfigurationArns: Optional[Sequence[str]] = None
    customerArtifactPaths: Optional[CustomerArtifactPathsTypeDef] = None
    radios: Optional[RadiosTypeDef] = None
    auxiliaryApps: Optional[Sequence[str]] = None
    billingMethod: Optional[BillingMethodType] = None

class TestGridProjectTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigOutputTypeDef] = None
    created: Optional[datetime] = None

class GetAccountSettingsResultTypeDef(BaseModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevicePoolResultTypeDef(BaseModel):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicePoolResultTypeDef(BaseModel):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicePoolsResultTypeDef(BaseModel):
    devicePools: List[DevicePoolTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDevicePoolResultTypeDef(BaseModel):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    modelId: Optional[str] = None
    formFactor: Optional[DeviceFormFactorType] = None
    platform: Optional[DevicePlatformType] = None
    os: Optional[str] = None
    cpu: Optional[CPUTypeDef] = None
    resolution: Optional[ResolutionTypeDef] = None
    heapSize: Optional[int] = None
    memory: Optional[int] = None
    image: Optional[str] = None
    carrier: Optional[str] = None
    radio: Optional[str] = None
    remoteAccessEnabled: Optional[bool] = None
    remoteDebugEnabled: Optional[bool] = None
    fleetType: Optional[str] = None
    fleetName: Optional[str] = None
    instances: Optional[List[DeviceInstanceTypeDef]] = None
    availability: Optional[DeviceAvailabilityType] = None

class GetDeviceInstanceResultTypeDef(BaseModel):
    deviceInstance: DeviceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceInstancesResultTypeDef(BaseModel):
    deviceInstances: List[DeviceInstanceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceInstanceResultTypeDef(BaseModel):
    deviceInstance: DeviceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RunTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[TestTypeType] = None
    platform: Optional[DevicePlatformType] = None
    created: Optional[datetime] = None
    status: Optional[ExecutionStatusType] = None
    result: Optional[ExecutionResultType] = None
    started: Optional[datetime] = None
    stopped: Optional[datetime] = None
    counters: Optional[CountersTypeDef] = None
    message: Optional[str] = None
    totalJobs: Optional[int] = None
    completedJobs: Optional[int] = None
    billingMethod: Optional[BillingMethodType] = None
    deviceMinutes: Optional[DeviceMinutesTypeDef] = None
    networkProfile: Optional[NetworkProfileTypeDef] = None
    parsingResultUrl: Optional[str] = None
    resultCode: Optional[ExecutionResultCodeType] = None
    seed: Optional[int] = None
    appUpload: Optional[str] = None
    eventCount: Optional[int] = None
    jobTimeoutMinutes: Optional[int] = None
    devicePoolArn: Optional[str] = None
    locale: Optional[str] = None
    radios: Optional[RadiosTypeDef] = None
    location: Optional[LocationTypeDef] = None
    customerArtifactPaths: Optional[CustomerArtifactPathsOutputTypeDef] = None
    webUrl: Optional[str] = None
    skipAppResign: Optional[bool] = None
    testSpecArn: Optional[str] = None
    deviceSelectionResult: Optional[DeviceSelectionResultTypeDef] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None

class ListDevicesRequestListDevicesPaginateTypeDef(BaseModel):
    arn: Optional[str] = None
    filters: Optional[Sequence[DeviceFilterUnionTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicesRequestRequestTypeDef(BaseModel):
    arn: Optional[str] = None
    nextToken: Optional[str] = None
    filters: Optional[Sequence[DeviceFilterUnionTypeDef]] = None

class GetSuiteResultTypeDef(BaseModel):
    suite: SuiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSuitesResultTypeDef(BaseModel):
    suites: List[SuiteTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestResultTypeDef(BaseModel):
    test: TestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestsResultTypeDef(BaseModel):
    tests: List[TestTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OfferingTypeDef(BaseModel):
    id: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Literal["RECURRING"]] = None
    platform: Optional[DevicePlatformType] = None
    recurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class CreateProjectResultTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProjectResultTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResultTypeDef(BaseModel):
    projects: List[ProjectTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResultTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicePoolCompatibilityRequestRequestTypeDef(BaseModel):
    devicePoolArn: str
    appArn: Optional[str] = None
    testType: Optional[TestTypeType] = None
    test: Optional[ScheduleRunTestTypeDef] = None
    configuration: Optional[ScheduleRunConfigurationTypeDef] = None

class ScheduleRunRequestRequestTypeDef(BaseModel):
    projectArn: str
    test: ScheduleRunTestTypeDef
    appArn: Optional[str] = None
    devicePoolArn: Optional[str] = None
    deviceSelectionConfiguration: Optional[DeviceSelectionConfigurationTypeDef] = None
    name: Optional[str] = None
    configuration: Optional[ScheduleRunConfigurationTypeDef] = None
    executionConfiguration: Optional[ExecutionConfigurationTypeDef] = None

class CreateTestGridProjectResultTypeDef(BaseModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestGridProjectResultTypeDef(BaseModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridProjectsResultTypeDef(BaseModel):
    testGridProjects: List[TestGridProjectTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTestGridProjectResultTypeDef(BaseModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DevicePoolCompatibilityResultTypeDef(BaseModel):
    device: Optional[DeviceTypeDef] = None
    compatible: Optional[bool] = None
    incompatibilityMessages: Optional[List[IncompatibilityMessageTypeDef]] = None

class GetDeviceResultTypeDef(BaseModel):
    device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[TestTypeType] = None
    created: Optional[datetime] = None
    status: Optional[ExecutionStatusType] = None
    result: Optional[ExecutionResultType] = None
    started: Optional[datetime] = None
    stopped: Optional[datetime] = None
    counters: Optional[CountersTypeDef] = None
    message: Optional[str] = None
    device: Optional[DeviceTypeDef] = None
    instanceArn: Optional[str] = None
    deviceMinutes: Optional[DeviceMinutesTypeDef] = None
    videoEndpoint: Optional[str] = None
    videoCapture: Optional[bool] = None

class ListDevicesResultTypeDef(BaseModel):
    devices: List[DeviceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProblemTypeDef(BaseModel):
    run: Optional[ProblemDetailTypeDef] = None
    job: Optional[ProblemDetailTypeDef] = None
    suite: Optional[ProblemDetailTypeDef] = None
    test: Optional[ProblemDetailTypeDef] = None
    device: Optional[DeviceTypeDef] = None
    result: Optional[ExecutionResultType] = None
    message: Optional[str] = None

class RemoteAccessSessionTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    created: Optional[datetime] = None
    status: Optional[ExecutionStatusType] = None
    result: Optional[ExecutionResultType] = None
    message: Optional[str] = None
    started: Optional[datetime] = None
    stopped: Optional[datetime] = None
    device: Optional[DeviceTypeDef] = None
    instanceArn: Optional[str] = None
    remoteDebugEnabled: Optional[bool] = None
    remoteRecordEnabled: Optional[bool] = None
    remoteRecordAppArn: Optional[str] = None
    hostAddress: Optional[str] = None
    clientId: Optional[str] = None
    billingMethod: Optional[BillingMethodType] = None
    deviceMinutes: Optional[DeviceMinutesTypeDef] = None
    endpoint: Optional[str] = None
    deviceUdid: Optional[str] = None
    interactionMode: Optional[InteractionModeType] = None
    skipAppResign: Optional[bool] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None

class GetRunResultTypeDef(BaseModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunsResultTypeDef(BaseModel):
    runs: List[RunTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduleRunResultTypeDef(BaseModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopRunResultTypeDef(BaseModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingsResultTypeDef(BaseModel):
    offerings: List[OfferingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OfferingStatusTypeDef(BaseModel):
    type: Optional[OfferingTransactionTypeType] = None
    offering: Optional[OfferingTypeDef] = None
    quantity: Optional[int] = None
    effectiveOn: Optional[datetime] = None

class GetDevicePoolCompatibilityResultTypeDef(BaseModel):
    compatibleDevices: List[DevicePoolCompatibilityResultTypeDef]
    incompatibleDevices: List[DevicePoolCompatibilityResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobResultTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResultTypeDef(BaseModel):
    jobs: List[JobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopJobResultTypeDef(BaseModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UniqueProblemTypeDef(BaseModel):
    message: Optional[str] = None
    problems: Optional[List[ProblemTypeDef]] = None

class CreateRemoteAccessSessionResultTypeDef(BaseModel):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRemoteAccessSessionResultTypeDef(BaseModel):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRemoteAccessSessionsResultTypeDef(BaseModel):
    remoteAccessSessions: List[RemoteAccessSessionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopRemoteAccessSessionResultTypeDef(BaseModel):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOfferingStatusResultTypeDef(BaseModel):
    current: Dict[str, OfferingStatusTypeDef]
    nextPeriod: Dict[str, OfferingStatusTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OfferingTransactionTypeDef(BaseModel):
    offeringStatus: Optional[OfferingStatusTypeDef] = None
    transactionId: Optional[str] = None
    offeringPromotionId: Optional[str] = None
    createdOn: Optional[datetime] = None
    cost: Optional[MonetaryAmountTypeDef] = None

class ListUniqueProblemsResultTypeDef(BaseModel):
    uniqueProblems: Dict[ExecutionResultType, List[UniqueProblemTypeDef]]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingTransactionsResultTypeDef(BaseModel):
    offeringTransactions: List[OfferingTransactionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseOfferingResultTypeDef(BaseModel):
    offeringTransaction: OfferingTransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RenewOfferingResultTypeDef(BaseModel):
    offeringTransaction: OfferingTransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


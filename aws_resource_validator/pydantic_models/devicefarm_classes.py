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
from aws_resource_validator.pydantic_models.devicefarm_constants import *

class TrialMinutesTypeDef(BaseValidatorModel):
    total: Optional[float] = None
    remaining: Optional[float] = None

class ArtifactTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[ArtifactTypeType] = None
    extension: Optional[str] = None
    url: Optional[str] = None

class CPUTypeDef(BaseValidatorModel):
    frequency: Optional[str] = None
    architecture: Optional[str] = None
    clock: Optional[float] = None

class CountersTypeDef(BaseValidatorModel):
    total: Optional[int] = None
    passed: Optional[int] = None
    failed: Optional[int] = None
    warned: Optional[int] = None
    errored: Optional[int] = None
    stopped: Optional[int] = None
    skipped: Optional[int] = None

class RuleTypeDef(BaseValidatorModel):
    attribute: Optional[DeviceAttributeType] = None
    operator: Optional[RuleOperatorType] = None
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[Sequence[str]] = None
    rebootAfterUse: Optional[bool] = None

class InstanceProfileTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[List[str]] = None
    rebootAfterUse: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None

class CreateNetworkProfileRequestRequestTypeDef(BaseValidatorModel):
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

class NetworkProfileTypeDef(BaseValidatorModel):
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

class VpcConfigTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str

class CreateRemoteAccessSessionConfigurationTypeDef(BaseValidatorModel):
    billingMethod: Optional[BillingMethodType] = None
    vpceConfigurationArns: Optional[Sequence[str]] = None

class TestGridVpcConfigTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str

class CreateTestGridUrlRequestRequestTypeDef(BaseValidatorModel):
    projectArn: str
    expiresInSeconds: int

class CreateUploadRequestRequestTypeDef(BaseValidatorModel):
    projectArn: str
    name: str
    type: UploadTypeType
    contentType: Optional[str] = None

class UploadTypeDef(BaseValidatorModel):
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

class CreateVPCEConfigurationRequestRequestTypeDef(BaseValidatorModel):
    vpceConfigurationName: str
    vpceServiceName: str
    serviceDnsName: str
    vpceConfigurationDescription: Optional[str] = None

class VPCEConfigurationTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    vpceConfigurationName: Optional[str] = None
    vpceServiceName: Optional[str] = None
    serviceDnsName: Optional[str] = None
    vpceConfigurationDescription: Optional[str] = None

class CustomerArtifactPathsOutputTypeDef(BaseValidatorModel):
    iosPaths: Optional[List[str]] = None
    androidPaths: Optional[List[str]] = None
    deviceHostPaths: Optional[List[str]] = None

class CustomerArtifactPathsTypeDef(BaseValidatorModel):
    iosPaths: Optional[Sequence[str]] = None
    androidPaths: Optional[Sequence[str]] = None
    deviceHostPaths: Optional[Sequence[str]] = None

class DeleteDevicePoolRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteNetworkProfileRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteRemoteAccessSessionRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteRunRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteTestGridProjectRequestRequestTypeDef(BaseValidatorModel):
    projectArn: str

class DeleteUploadRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteVPCEConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeviceFilterExtraOutputTypeDef(BaseValidatorModel):
    attribute: DeviceFilterAttributeType
    operator: RuleOperatorType
    values: List[str]

class DeviceFilterOutputTypeDef(BaseValidatorModel):
    attribute: DeviceFilterAttributeType
    operator: RuleOperatorType
    values: List[str]

class DeviceFilterTypeDef(BaseValidatorModel):
    attribute: DeviceFilterAttributeType
    operator: RuleOperatorType
    values: Sequence[str]

class DeviceMinutesTypeDef(BaseValidatorModel):
    total: Optional[float] = None
    metered: Optional[float] = None
    unmetered: Optional[float] = None

class IncompatibilityMessageTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    type: Optional[DeviceAttributeType] = None

class ResolutionTypeDef(BaseValidatorModel):
    width: Optional[int] = None
    height: Optional[int] = None

class ExecutionConfigurationTypeDef(BaseValidatorModel):
    jobTimeoutMinutes: Optional[int] = None
    accountsCleanup: Optional[bool] = None
    appPackagesCleanup: Optional[bool] = None
    videoCapture: Optional[bool] = None
    skipAppResign: Optional[bool] = None

class GetDeviceInstanceRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class ScheduleRunTestTypeDef(BaseValidatorModel):
    type: TestTypeType
    testPackageArn: Optional[str] = None
    testSpecArn: Optional[str] = None
    filter: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None

class GetDevicePoolRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetDeviceRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetJobRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetNetworkProfileRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetOfferingStatusRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class GetProjectRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetRemoteAccessSessionRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetRunRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetSuiteRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetTestGridProjectRequestRequestTypeDef(BaseValidatorModel):
    projectArn: str

class GetTestGridSessionRequestRequestTypeDef(BaseValidatorModel):
    projectArn: Optional[str] = None
    sessionId: Optional[str] = None
    sessionArn: Optional[str] = None

class TestGridSessionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    status: Optional[TestGridSessionStatusType] = None
    created: Optional[datetime] = None
    ended: Optional[datetime] = None
    billingMinutes: Optional[float] = None
    seleniumProperties: Optional[str] = None

class GetTestRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetUploadRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetVPCEConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class InstallToRemoteAccessSessionRequestRequestTypeDef(BaseValidatorModel):
    remoteAccessSessionArn: str
    appArn: str

class ListArtifactsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    type: ArtifactCategoryType
    nextToken: Optional[str] = None

class ListDeviceInstancesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDevicePoolsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    type: Optional[DevicePoolTypeType] = None
    nextToken: Optional[str] = None

class ListInstanceProfilesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListJobsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None

class ListNetworkProfilesRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    type: Optional[NetworkProfileTypeType] = None
    nextToken: Optional[str] = None

class ListOfferingPromotionsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class OfferingPromotionTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None

class ListOfferingTransactionsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ListOfferingsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    nextToken: Optional[str] = None

class ListRemoteAccessSessionsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None

class ListRunsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None

class ListSamplesRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None

class SampleTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    type: Optional[SampleTypeType] = None
    url: Optional[str] = None

class ListSuitesRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ListTestGridProjectsRequestRequestTypeDef(BaseValidatorModel):
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None

class ListTestGridSessionActionsRequestRequestTypeDef(BaseValidatorModel):
    sessionArn: str
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None

class TestGridSessionActionTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    started: Optional[datetime] = None
    duration: Optional[int] = None
    statusCode: Optional[str] = None
    requestMethod: Optional[str] = None

class ListTestGridSessionArtifactsRequestRequestTypeDef(BaseValidatorModel):
    sessionArn: str
    type: Optional[TestGridSessionArtifactCategoryType] = None
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None

class TestGridSessionArtifactTypeDef(BaseValidatorModel):
    filename: Optional[str] = None
    type: Optional[TestGridSessionArtifactTypeType] = None
    url: Optional[str] = None

class ListTestsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None

class ListUniqueProblemsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None

class ListUploadsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    type: Optional[UploadTypeType] = None
    nextToken: Optional[str] = None

class ListVPCEConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class LocationTypeDef(BaseValidatorModel):
    latitude: float
    longitude: float

class MonetaryAmountTypeDef(BaseValidatorModel):
    amount: Optional[float] = None
    currencyCode: Optional[Literal["USD"]] = None

class ProblemDetailTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None

class VpcConfigOutputTypeDef(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str

class PurchaseOfferingRequestRequestTypeDef(BaseValidatorModel):
    offeringId: str
    quantity: int
    offeringPromotionId: Optional[str] = None

class RadiosTypeDef(BaseValidatorModel):
    wifi: Optional[bool] = None
    bluetooth: Optional[bool] = None
    nfc: Optional[bool] = None
    gps: Optional[bool] = None

class RenewOfferingRequestRequestTypeDef(BaseValidatorModel):
    offeringId: str
    quantity: int

class StopJobRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class StopRemoteAccessSessionRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class StopRunRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class TestGridVpcConfigOutputTypeDef(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateDeviceInstanceRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    profileArn: Optional[str] = None
    labels: Optional[Sequence[str]] = None

class UpdateInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[Sequence[str]] = None
    rebootAfterUse: Optional[bool] = None

class UpdateNetworkProfileRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateUploadRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    contentType: Optional[str] = None
    editContent: Optional[bool] = None

class UpdateVPCEConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    vpceConfigurationName: Optional[str] = None
    vpceServiceName: Optional[str] = None
    serviceDnsName: Optional[str] = None
    vpceConfigurationDescription: Optional[str] = None

class VpcConfigExtraOutputTypeDef(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str

class AccountSettingsTypeDef(BaseValidatorModel):
    awsAccountNumber: Optional[str] = None
    unmeteredDevices: Optional[Dict[DevicePlatformType, int]] = None
    unmeteredRemoteAccessDevices: Optional[Dict[DevicePlatformType, int]] = None
    maxJobTimeoutMinutes: Optional[int] = None
    trialMinutes: Optional[TrialMinutesTypeDef] = None
    maxSlots: Optional[Dict[str, int]] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    skipAppResign: Optional[bool] = None

class CreateDevicePoolRequestRequestTypeDef(BaseValidatorModel):
    projectArn: str
    name: str
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    maxDevices: Optional[int] = None

class DevicePoolTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[DevicePoolTypeType] = None
    rules: Optional[List[RuleTypeDef]] = None
    maxDevices: Optional[int] = None

class UpdateDevicePoolRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    rules: Optional[Sequence[RuleTypeDef]] = None
    maxDevices: Optional[int] = None
    clearMaxDevices: Optional[bool] = None

class CreateTestGridUrlResultTypeDef(BaseValidatorModel):
    url: str
    expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListArtifactsResultTypeDef(BaseValidatorModel):
    artifacts: List[ArtifactTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceProfileResultTypeDef(BaseValidatorModel):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceInstanceTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    deviceArn: Optional[str] = None
    labels: Optional[List[str]] = None
    status: Optional[InstanceStatusType] = None
    udid: Optional[str] = None
    instanceProfile: Optional[InstanceProfileTypeDef] = None

class GetInstanceProfileResultTypeDef(BaseValidatorModel):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceProfilesResultTypeDef(BaseValidatorModel):
    instanceProfiles: List[InstanceProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInstanceProfileResultTypeDef(BaseValidatorModel):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkProfileResultTypeDef(BaseValidatorModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkProfileResultTypeDef(BaseValidatorModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListNetworkProfilesResultTypeDef(BaseValidatorModel):
    networkProfiles: List[NetworkProfileTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkProfileResultTypeDef(BaseValidatorModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
    name: str
    defaultJobTimeoutMinutes: Optional[int] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None

class UpdateProjectRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None

class CreateRemoteAccessSessionRequestRequestTypeDef(BaseValidatorModel):
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

class CreateTestGridProjectRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigTypeDef] = None

class UpdateTestGridProjectRequestRequestTypeDef(BaseValidatorModel):
    projectArn: str
    name: Optional[str] = None
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigTypeDef] = None

class CreateUploadResultTypeDef(BaseValidatorModel):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUploadResultTypeDef(BaseValidatorModel):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstallToRemoteAccessSessionResultTypeDef(BaseValidatorModel):
    appUpload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUploadsResultTypeDef(BaseValidatorModel):
    uploads: List[UploadTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUploadResultTypeDef(BaseValidatorModel):
    upload: UploadTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVPCEConfigurationResultTypeDef(BaseValidatorModel):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVPCEConfigurationResultTypeDef(BaseValidatorModel):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVPCEConfigurationsResultTypeDef(BaseValidatorModel):
    vpceConfigurations: List[VPCEConfigurationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVPCEConfigurationResultTypeDef(BaseValidatorModel):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceSelectionResultTypeDef(BaseValidatorModel):
    filters: Optional[List[DeviceFilterOutputTypeDef]] = None
    matchedDevicesCount: Optional[int] = None
    maxDevices: Optional[int] = None

class DeviceSelectionConfigurationTypeDef(BaseValidatorModel):
    filters: Sequence[DeviceFilterTypeDef]
    maxDevices: int

class SuiteTypeDef(BaseValidatorModel):
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

class TestTypeDef(BaseValidatorModel):
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

class GetOfferingStatusRequestGetOfferingStatusPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListArtifactsRequestListArtifactsPaginateTypeDef(BaseValidatorModel):
    arn: str
    type: ArtifactCategoryType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeviceInstancesRequestListDeviceInstancesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicePoolsRequestListDevicePoolsPaginateTypeDef(BaseValidatorModel):
    arn: str
    type: Optional[DevicePoolTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNetworkProfilesRequestListNetworkProfilesPaginateTypeDef(BaseValidatorModel):
    arn: str
    type: Optional[NetworkProfileTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingPromotionsRequestListOfferingPromotionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingTransactionsRequestListOfferingTransactionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOfferingsRequestListOfferingsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRemoteAccessSessionsRequestListRemoteAccessSessionsPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRunsRequestListRunsPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSamplesRequestListSamplesPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSuitesRequestListSuitesPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTestsRequestListTestsPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUniqueProblemsRequestListUniqueProblemsPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUploadsRequestListUploadsPaginateTypeDef(BaseValidatorModel):
    arn: str
    type: Optional[UploadTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListVPCEConfigurationsRequestListVPCEConfigurationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTestGridSessionResultTypeDef(BaseValidatorModel):
    testGridSession: TestGridSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridSessionsResultTypeDef(BaseValidatorModel):
    testGridSessions: List[TestGridSessionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingPromotionsResultTypeDef(BaseValidatorModel):
    offeringPromotions: List[OfferingPromotionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSamplesResultTypeDef(BaseValidatorModel):
    samples: List[SampleTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class ListTestGridSessionActionsResultTypeDef(BaseValidatorModel):
    actions: List[TestGridSessionActionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridSessionArtifactsResultTypeDef(BaseValidatorModel):
    artifacts: List[TestGridSessionArtifactTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridSessionsRequestRequestTypeDef(BaseValidatorModel):
    projectArn: str
    status: Optional[TestGridSessionStatusType] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    endTimeAfter: Optional[TimestampTypeDef] = None
    endTimeBefore: Optional[TimestampTypeDef] = None
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None

class RecurringChargeTypeDef(BaseValidatorModel):
    cost: Optional[MonetaryAmountTypeDef] = None
    frequency: Optional[Literal["MONTHLY"]] = None

class ProjectTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    created: Optional[datetime] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None

class ScheduleRunConfigurationTypeDef(BaseValidatorModel):
    extraDataPackageArn: Optional[str] = None
    networkProfileArn: Optional[str] = None
    locale: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    vpceConfigurationArns: Optional[Sequence[str]] = None
    customerArtifactPaths: Optional[CustomerArtifactPathsTypeDef] = None
    radios: Optional[RadiosTypeDef] = None
    auxiliaryApps: Optional[Sequence[str]] = None
    billingMethod: Optional[BillingMethodType] = None

class TestGridProjectTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigOutputTypeDef] = None
    created: Optional[datetime] = None

class GetAccountSettingsResultTypeDef(BaseValidatorModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevicePoolResultTypeDef(BaseValidatorModel):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicePoolResultTypeDef(BaseValidatorModel):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDevicePoolsResultTypeDef(BaseValidatorModel):
    devicePools: List[DevicePoolTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDevicePoolResultTypeDef(BaseValidatorModel):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeviceTypeDef(BaseValidatorModel):
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

class GetDeviceInstanceResultTypeDef(BaseValidatorModel):
    deviceInstance: DeviceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDeviceInstancesResultTypeDef(BaseValidatorModel):
    deviceInstances: List[DeviceInstanceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDeviceInstanceResultTypeDef(BaseValidatorModel):
    deviceInstance: DeviceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RunTypeDef(BaseValidatorModel):
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

class ListDevicesRequestListDevicesPaginateTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    filters: Optional[Sequence[DeviceFilterUnionTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDevicesRequestRequestTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    nextToken: Optional[str] = None
    filters: Optional[Sequence[DeviceFilterUnionTypeDef]] = None

class GetSuiteResultTypeDef(BaseValidatorModel):
    suite: SuiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSuitesResultTypeDef(BaseValidatorModel):
    suites: List[SuiteTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestResultTypeDef(BaseValidatorModel):
    test: TestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestsResultTypeDef(BaseValidatorModel):
    tests: List[TestTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OfferingTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Literal["RECURRING"]] = None
    platform: Optional[DevicePlatformType] = None
    recurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class CreateProjectResultTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProjectResultTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProjectsResultTypeDef(BaseValidatorModel):
    projects: List[ProjectTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResultTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicePoolCompatibilityRequestRequestTypeDef(BaseValidatorModel):
    devicePoolArn: str
    appArn: Optional[str] = None
    testType: Optional[TestTypeType] = None
    test: Optional[ScheduleRunTestTypeDef] = None
    configuration: Optional[ScheduleRunConfigurationTypeDef] = None

class ScheduleRunRequestRequestTypeDef(BaseValidatorModel):
    projectArn: str
    test: ScheduleRunTestTypeDef
    appArn: Optional[str] = None
    devicePoolArn: Optional[str] = None
    deviceSelectionConfiguration: Optional[DeviceSelectionConfigurationTypeDef] = None
    name: Optional[str] = None
    configuration: Optional[ScheduleRunConfigurationTypeDef] = None
    executionConfiguration: Optional[ExecutionConfigurationTypeDef] = None

class CreateTestGridProjectResultTypeDef(BaseValidatorModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTestGridProjectResultTypeDef(BaseValidatorModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListTestGridProjectsResultTypeDef(BaseValidatorModel):
    testGridProjects: List[TestGridProjectTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTestGridProjectResultTypeDef(BaseValidatorModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DevicePoolCompatibilityResultTypeDef(BaseValidatorModel):
    device: Optional[DeviceTypeDef] = None
    compatible: Optional[bool] = None
    incompatibilityMessages: Optional[List[IncompatibilityMessageTypeDef]] = None

class GetDeviceResultTypeDef(BaseValidatorModel):
    device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class JobTypeDef(BaseValidatorModel):
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

class ListDevicesResultTypeDef(BaseValidatorModel):
    devices: List[DeviceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ProblemTypeDef(BaseValidatorModel):
    run: Optional[ProblemDetailTypeDef] = None
    job: Optional[ProblemDetailTypeDef] = None
    suite: Optional[ProblemDetailTypeDef] = None
    test: Optional[ProblemDetailTypeDef] = None
    device: Optional[DeviceTypeDef] = None
    result: Optional[ExecutionResultType] = None
    message: Optional[str] = None

class RemoteAccessSessionTypeDef(BaseValidatorModel):
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

class GetRunResultTypeDef(BaseValidatorModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRunsResultTypeDef(BaseValidatorModel):
    runs: List[RunTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduleRunResultTypeDef(BaseValidatorModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopRunResultTypeDef(BaseValidatorModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingsResultTypeDef(BaseValidatorModel):
    offerings: List[OfferingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OfferingStatusTypeDef(BaseValidatorModel):
    type: Optional[OfferingTransactionTypeType] = None
    offering: Optional[OfferingTypeDef] = None
    quantity: Optional[int] = None
    effectiveOn: Optional[datetime] = None

class GetDevicePoolCompatibilityResultTypeDef(BaseValidatorModel):
    compatibleDevices: List[DevicePoolCompatibilityResultTypeDef]
    incompatibleDevices: List[DevicePoolCompatibilityResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobResultTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResultTypeDef(BaseValidatorModel):
    jobs: List[JobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopJobResultTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UniqueProblemTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    problems: Optional[List[ProblemTypeDef]] = None

class CreateRemoteAccessSessionResultTypeDef(BaseValidatorModel):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRemoteAccessSessionResultTypeDef(BaseValidatorModel):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRemoteAccessSessionsResultTypeDef(BaseValidatorModel):
    remoteAccessSessions: List[RemoteAccessSessionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopRemoteAccessSessionResultTypeDef(BaseValidatorModel):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOfferingStatusResultTypeDef(BaseValidatorModel):
    current: Dict[str, OfferingStatusTypeDef]
    nextPeriod: Dict[str, OfferingStatusTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class OfferingTransactionTypeDef(BaseValidatorModel):
    offeringStatus: Optional[OfferingStatusTypeDef] = None
    transactionId: Optional[str] = None
    offeringPromotionId: Optional[str] = None
    createdOn: Optional[datetime] = None
    cost: Optional[MonetaryAmountTypeDef] = None

class ListUniqueProblemsResultTypeDef(BaseValidatorModel):
    uniqueProblems: Dict[ExecutionResultType, List[UniqueProblemTypeDef]]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListOfferingTransactionsResultTypeDef(BaseValidatorModel):
    offeringTransactions: List[OfferingTransactionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseOfferingResultTypeDef(BaseValidatorModel):
    offeringTransaction: OfferingTransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RenewOfferingResultTypeDef(BaseValidatorModel):
    offeringTransaction: OfferingTransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


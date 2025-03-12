from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateInstanceProfileRequestTypeDef(BaseValidatorModel):
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


class DeviceProxyTypeDef(BaseValidatorModel):
    host: str
    port: int


class CreateTestGridUrlRequestTypeDef(BaseValidatorModel):
    projectArn: str
    expiresInSeconds: int


class CreateVPCEConfigurationRequestTypeDef(BaseValidatorModel):
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


class DeleteDevicePoolRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteInstanceProfileRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteNetworkProfileRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteProjectRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteRemoteAccessSessionRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteRunRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteTestGridProjectRequestTypeDef(BaseValidatorModel):
    projectArn: str


class DeleteUploadRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteVPCEConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class DeviceMinutesTypeDef(BaseValidatorModel):
    total: Optional[float] = None
    metered: Optional[float] = None
    unmetered: Optional[float] = None


class ResolutionTypeDef(BaseValidatorModel):
    width: Optional[int] = None
    height: Optional[int] = None


class ExecutionConfigurationTypeDef(BaseValidatorModel):
    jobTimeoutMinutes: Optional[int] = None
    accountsCleanup: Optional[bool] = None
    appPackagesCleanup: Optional[bool] = None
    videoCapture: Optional[bool] = None
    skipAppResign: Optional[bool] = None


class GetDeviceInstanceRequestTypeDef(BaseValidatorModel):
    arn: str


class GetDevicePoolRequestTypeDef(BaseValidatorModel):
    arn: str


class GetDeviceRequestTypeDef(BaseValidatorModel):
    arn: str


class GetInstanceProfileRequestTypeDef(BaseValidatorModel):
    arn: str


class GetJobRequestTypeDef(BaseValidatorModel):
    arn: str


class GetNetworkProfileRequestTypeDef(BaseValidatorModel):
    arn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetOfferingStatusRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class GetProjectRequestTypeDef(BaseValidatorModel):
    arn: str


class GetRemoteAccessSessionRequestTypeDef(BaseValidatorModel):
    arn: str


class GetRunRequestTypeDef(BaseValidatorModel):
    arn: str


class GetSuiteRequestTypeDef(BaseValidatorModel):
    arn: str


class GetTestGridProjectRequestTypeDef(BaseValidatorModel):
    projectArn: str


class GetTestGridSessionRequestTypeDef(BaseValidatorModel):
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


class GetTestRequestTypeDef(BaseValidatorModel):
    arn: str


class GetUploadRequestTypeDef(BaseValidatorModel):
    arn: str


class GetVPCEConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class InstallToRemoteAccessSessionRequestTypeDef(BaseValidatorModel):
    remoteAccessSessionArn: str
    appArn: str


class ListDeviceInstancesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInstanceProfilesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListOfferingPromotionsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListOfferingTransactionsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListOfferingsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListProjectsRequestTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    nextToken: Optional[str] = None


class ListRemoteAccessSessionsRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListRunsRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListSamplesRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListSuitesRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ListTestGridProjectsRequestTypeDef(BaseValidatorModel):
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None


class ListTestGridSessionActionsRequestTypeDef(BaseValidatorModel):
    sessionArn: str
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None


class TestGridSessionActionTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    started: Optional[datetime] = None
    duration: Optional[int] = None
    statusCode: Optional[str] = None
    requestMethod: Optional[str] = None


class ListTestsRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListUniqueProblemsRequestTypeDef(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListVPCEConfigurationsRequestTypeDef(BaseValidatorModel):
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


class PurchaseOfferingRequestTypeDef(BaseValidatorModel):
    offeringId: str
    quantity: int
    offeringPromotionId: Optional[str] = None


class RadiosTypeDef(BaseValidatorModel):
    wifi: Optional[bool] = None
    bluetooth: Optional[bool] = None
    nfc: Optional[bool] = None
    gps: Optional[bool] = None


class RenewOfferingRequestTypeDef(BaseValidatorModel):
    offeringId: str
    quantity: int


class StopJobRequestTypeDef(BaseValidatorModel):
    arn: str


class StopRemoteAccessSessionRequestTypeDef(BaseValidatorModel):
    arn: str


class StopRunRequestTypeDef(BaseValidatorModel):
    arn: str


class TestGridVpcConfigOutputTypeDef(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str


class TestGridVpcConfigTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateDeviceInstanceRequestTypeDef(BaseValidatorModel):
    arn: str
    profileArn: Optional[str] = None
    labels: Optional[Sequence[str]] = None


class UpdateInstanceProfileRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[Sequence[str]] = None
    rebootAfterUse: Optional[bool] = None


class UpdateUploadRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    contentType: Optional[str] = None
    editContent: Optional[bool] = None


class UpdateVPCEConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str
    vpceConfigurationName: Optional[str] = None
    vpceServiceName: Optional[str] = None
    serviceDnsName: Optional[str] = None
    vpceConfigurationDescription: Optional[str] = None


class VpcConfigTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
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


class RuleTypeDef(BaseValidatorModel):
    pass


class CreateDevicePoolRequestTypeDef(BaseValidatorModel):
    projectArn: str
    name: str
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    maxDevices: Optional[int] = None


class UpdateDevicePoolRequestTypeDef(BaseValidatorModel):
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


class ArtifactTypeDef(BaseValidatorModel):
    pass


class ListArtifactsResultTypeDef(BaseValidatorModel):
    artifacts: List[ArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateInstanceProfileResultTypeDef(BaseValidatorModel):
    instanceProfile: InstanceProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class NetworkProfileTypeDef(BaseValidatorModel):
    pass


class CreateNetworkProfileResultTypeDef(BaseValidatorModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetNetworkProfileResultTypeDef(BaseValidatorModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListNetworkProfilesResultTypeDef(BaseValidatorModel):
    networkProfiles: List[NetworkProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateNetworkProfileResultTypeDef(BaseValidatorModel):
    networkProfile: NetworkProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRemoteAccessSessionConfigurationTypeDef(BaseValidatorModel):
    billingMethod: Optional[BillingMethodType] = None
    vpceConfigurationArns: Optional[Sequence[str]] = None
    deviceProxy: Optional[DeviceProxyTypeDef] = None


class UploadTypeDef(BaseValidatorModel):
    pass


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateVPCEConfigurationResultTypeDef(BaseValidatorModel):
    vpceConfiguration: VPCEConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeviceFilterOutputTypeDef(BaseValidatorModel):
    pass


class DeviceSelectionResultTypeDef(BaseValidatorModel):
    filters: Optional[List[DeviceFilterOutputTypeDef]] = None
    matchedDevicesCount: Optional[int] = None
    maxDevices: Optional[int] = None


class GetOfferingStatusRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDeviceInstancesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstanceProfilesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOfferingPromotionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOfferingTransactionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOfferingsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsRequestPaginateTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRemoteAccessSessionsRequestPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRunsRequestPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSamplesRequestPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSuitesRequestPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTestsRequestPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUniqueProblemsRequestPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListVPCEConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTestGridSessionResultTypeDef(BaseValidatorModel):
    testGridSession: TestGridSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTestGridSessionsResultTypeDef(BaseValidatorModel):
    testGridSessions: List[TestGridSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class OfferingPromotionTypeDef(BaseValidatorModel):
    pass


class ListOfferingPromotionsResultTypeDef(BaseValidatorModel):
    offeringPromotions: List[OfferingPromotionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SampleTypeDef(BaseValidatorModel):
    pass


class ListSamplesResultTypeDef(BaseValidatorModel):
    samples: List[SampleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class ListTestGridSessionActionsResultTypeDef(BaseValidatorModel):
    actions: List[TestGridSessionActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TestGridSessionArtifactTypeDef(BaseValidatorModel):
    pass


class ListTestGridSessionArtifactsResultTypeDef(BaseValidatorModel):
    artifacts: List[TestGridSessionArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListTestGridSessionsRequestTypeDef(BaseValidatorModel):
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


class TestGridProjectTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigOutputTypeDef] = None
    created: Optional[datetime] = None


class GetAccountSettingsResultTypeDef(BaseValidatorModel):
    accountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DevicePoolTypeDef(BaseValidatorModel):
    pass


class CreateDevicePoolResultTypeDef(BaseValidatorModel):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDevicePoolResultTypeDef(BaseValidatorModel):
    devicePool: DevicePoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDevicePoolsResultTypeDef(BaseValidatorModel):
    devicePools: List[DevicePoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDeviceInstanceResultTypeDef(BaseValidatorModel):
    deviceInstance: DeviceInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRemoteAccessSessionRequestTypeDef(BaseValidatorModel):
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


class CustomerArtifactPathsUnionTypeDef(BaseValidatorModel):
    pass


class ScheduleRunConfigurationTypeDef(BaseValidatorModel):
    extraDataPackageArn: Optional[str] = None
    networkProfileArn: Optional[str] = None
    locale: Optional[str] = None
    location: Optional[LocationTypeDef] = None
    vpceConfigurationArns: Optional[Sequence[str]] = None
    deviceProxy: Optional[DeviceProxyTypeDef] = None
    customerArtifactPaths: Optional[CustomerArtifactPathsUnionTypeDef] = None
    radios: Optional[RadiosTypeDef] = None
    auxiliaryApps: Optional[Sequence[str]] = None
    billingMethod: Optional[BillingMethodType] = None


class DeviceFilterUnionTypeDef(BaseValidatorModel):
    pass


class DeviceSelectionConfigurationTypeDef(BaseValidatorModel):
    filters: Sequence[DeviceFilterUnionTypeDef]
    maxDevices: int


class ListDevicesRequestPaginateTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    filters: Optional[Sequence[DeviceFilterUnionTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDevicesRequestTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    nextToken: Optional[str] = None
    filters: Optional[Sequence[DeviceFilterUnionTypeDef]] = None


class SuiteTypeDef(BaseValidatorModel):
    pass


class GetSuiteResultTypeDef(BaseValidatorModel):
    suite: SuiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSuitesResultTypeDef(BaseValidatorModel):
    suites: List[SuiteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TestTypeDef(BaseValidatorModel):
    pass


class GetTestResultTypeDef(BaseValidatorModel):
    test: TestTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTestsResultTypeDef(BaseValidatorModel):
    tests: List[TestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateProjectResultTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetProjectResultTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListProjectsResultTypeDef(BaseValidatorModel):
    projects: List[ProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateProjectResultTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTestGridProjectResultTypeDef(BaseValidatorModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTestGridProjectResultTypeDef(BaseValidatorModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListTestGridProjectsResultTypeDef(BaseValidatorModel):
    testGridProjects: List[TestGridProjectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateTestGridProjectResultTypeDef(BaseValidatorModel):
    testGridProject: TestGridProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TestGridVpcConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateTestGridProjectRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigUnionTypeDef] = None


class UpdateTestGridProjectRequestTypeDef(BaseValidatorModel):
    projectArn: str
    name: Optional[str] = None
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigUnionTypeDef] = None


class VpcConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateProjectRequestTypeDef(BaseValidatorModel):
    name: str
    defaultJobTimeoutMinutes: Optional[int] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None


class UpdateProjectRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None


class IncompatibilityMessageTypeDef(BaseValidatorModel):
    pass


class DevicePoolCompatibilityResultTypeDef(BaseValidatorModel):
    device: Optional[DeviceTypeDef] = None
    compatible: Optional[bool] = None
    incompatibilityMessages: Optional[List[IncompatibilityMessageTypeDef]] = None


class GetDeviceResultTypeDef(BaseValidatorModel):
    device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDevicesResultTypeDef(BaseValidatorModel):
    devices: List[DeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    deviceProxy: Optional[DeviceProxyTypeDef] = None


class ScheduleRunTestTypeDef(BaseValidatorModel):
    pass


class GetDevicePoolCompatibilityRequestTypeDef(BaseValidatorModel):
    devicePoolArn: str
    appArn: Optional[str] = None
    testType: Optional[TestTypeType] = None
    test: Optional[ScheduleRunTestTypeDef] = None
    configuration: Optional[ScheduleRunConfigurationTypeDef] = None


class RunTypeDef(BaseValidatorModel):
    pass


class GetRunResultTypeDef(BaseValidatorModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRunsResultTypeDef(BaseValidatorModel):
    runs: List[RunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ScheduleRunResultTypeDef(BaseValidatorModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopRunResultTypeDef(BaseValidatorModel):
    run: RunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ScheduleRunRequestTypeDef(BaseValidatorModel):
    projectArn: str
    test: ScheduleRunTestTypeDef
    appArn: Optional[str] = None
    devicePoolArn: Optional[str] = None
    deviceSelectionConfiguration: Optional[DeviceSelectionConfigurationTypeDef] = None
    name: Optional[str] = None
    configuration: Optional[ScheduleRunConfigurationTypeDef] = None
    executionConfiguration: Optional[ExecutionConfigurationTypeDef] = None


class OfferingTypeDef(BaseValidatorModel):
    pass


class ListOfferingsResultTypeDef(BaseValidatorModel):
    offerings: List[OfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetDevicePoolCompatibilityResultTypeDef(BaseValidatorModel):
    compatibleDevices: List[DevicePoolCompatibilityResultTypeDef]
    incompatibleDevices: List[DevicePoolCompatibilityResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class JobTypeDef(BaseValidatorModel):
    pass


class GetJobResultTypeDef(BaseValidatorModel):
    job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobsResultTypeDef(BaseValidatorModel):
    jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StopRemoteAccessSessionResultTypeDef(BaseValidatorModel):
    remoteAccessSession: RemoteAccessSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OfferingStatusTypeDef(BaseValidatorModel):
    pass


class GetOfferingStatusResultTypeDef(BaseValidatorModel):
    current: Dict[str, OfferingStatusTypeDef]
    nextPeriod: Dict[str, OfferingStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class OfferingTransactionTypeDef(BaseValidatorModel):
    offeringStatus: Optional[OfferingStatusTypeDef] = None
    transactionId: Optional[str] = None
    offeringPromotionId: Optional[str] = None
    createdOn: Optional[datetime] = None
    cost: Optional[MonetaryAmountTypeDef] = None


class ListUniqueProblemsResultTypeDef(BaseValidatorModel):
    uniqueProblems: Dict[ExecutionResultType, List[UniqueProblemTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListOfferingTransactionsResultTypeDef(BaseValidatorModel):
    offeringTransactions: List[OfferingTransactionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PurchaseOfferingResultTypeDef(BaseValidatorModel):
    offeringTransaction: OfferingTransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RenewOfferingResultTypeDef(BaseValidatorModel):
    offeringTransaction: OfferingTransactionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



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

class TrialMinutes(BaseValidatorModel):
    total: Optional[float] = None
    remaining: Optional[float] = None


class CPU(BaseValidatorModel):
    frequency: Optional[str] = None
    architecture: Optional[str] = None
    clock: Optional[float] = None


class Counters(BaseValidatorModel):
    total: Optional[int] = None
    passed: Optional[int] = None
    failed: Optional[int] = None
    warned: Optional[int] = None
    errored: Optional[int] = None
    stopped: Optional[int] = None
    skipped: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateInstanceProfileRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[Sequence[str]] = None
    rebootAfterUse: Optional[bool] = None


class InstanceProfile(BaseValidatorModel):
    arn: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[List[str]] = None
    rebootAfterUse: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None


class DeviceProxy(BaseValidatorModel):
    host: str
    port: int


class CreateTestGridUrlRequest(BaseValidatorModel):
    projectArn: str
    expiresInSeconds: int


class CreateVPCEConfigurationRequest(BaseValidatorModel):
    vpceConfigurationName: str
    vpceServiceName: str
    serviceDnsName: str
    vpceConfigurationDescription: Optional[str] = None


class VPCEConfiguration(BaseValidatorModel):
    arn: Optional[str] = None
    vpceConfigurationName: Optional[str] = None
    vpceServiceName: Optional[str] = None
    serviceDnsName: Optional[str] = None
    vpceConfigurationDescription: Optional[str] = None


class CustomerArtifactPathsOutput(BaseValidatorModel):
    iosPaths: Optional[List[str]] = None
    androidPaths: Optional[List[str]] = None
    deviceHostPaths: Optional[List[str]] = None


class CustomerArtifactPaths(BaseValidatorModel):
    iosPaths: Optional[Sequence[str]] = None
    androidPaths: Optional[Sequence[str]] = None
    deviceHostPaths: Optional[Sequence[str]] = None


class DeleteDevicePoolRequest(BaseValidatorModel):
    arn: str


class DeleteInstanceProfileRequest(BaseValidatorModel):
    arn: str


class DeleteNetworkProfileRequest(BaseValidatorModel):
    arn: str


class DeleteProjectRequest(BaseValidatorModel):
    arn: str


class DeleteRemoteAccessSessionRequest(BaseValidatorModel):
    arn: str


class DeleteRunRequest(BaseValidatorModel):
    arn: str


class DeleteTestGridProjectRequest(BaseValidatorModel):
    projectArn: str


class DeleteUploadRequest(BaseValidatorModel):
    arn: str


class DeleteVPCEConfigurationRequest(BaseValidatorModel):
    arn: str


class DeviceMinutes(BaseValidatorModel):
    total: Optional[float] = None
    metered: Optional[float] = None
    unmetered: Optional[float] = None


class Resolution(BaseValidatorModel):
    width: Optional[int] = None
    height: Optional[int] = None


class ExecutionConfiguration(BaseValidatorModel):
    jobTimeoutMinutes: Optional[int] = None
    accountsCleanup: Optional[bool] = None
    appPackagesCleanup: Optional[bool] = None
    videoCapture: Optional[bool] = None
    skipAppResign: Optional[bool] = None


class GetDeviceInstanceRequest(BaseValidatorModel):
    arn: str


class GetDevicePoolRequest(BaseValidatorModel):
    arn: str


class GetDeviceRequest(BaseValidatorModel):
    arn: str


class GetInstanceProfileRequest(BaseValidatorModel):
    arn: str


class GetJobRequest(BaseValidatorModel):
    arn: str


class GetNetworkProfileRequest(BaseValidatorModel):
    arn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetOfferingStatusRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class GetProjectRequest(BaseValidatorModel):
    arn: str


class GetRemoteAccessSessionRequest(BaseValidatorModel):
    arn: str


class GetRunRequest(BaseValidatorModel):
    arn: str


class GetSuiteRequest(BaseValidatorModel):
    arn: str


class GetTestGridProjectRequest(BaseValidatorModel):
    projectArn: str


class GetTestGridSessionRequest(BaseValidatorModel):
    projectArn: Optional[str] = None
    sessionId: Optional[str] = None
    sessionArn: Optional[str] = None


class TestGridSession(BaseValidatorModel):
    arn: Optional[str] = None
    status: Optional[TestGridSessionStatusType] = None
    created: Optional[datetime] = None
    ended: Optional[datetime] = None
    billingMinutes: Optional[float] = None
    seleniumProperties: Optional[str] = None


class GetTestRequest(BaseValidatorModel):
    arn: str


class GetUploadRequest(BaseValidatorModel):
    arn: str


class GetVPCEConfigurationRequest(BaseValidatorModel):
    arn: str


class InstallToRemoteAccessSessionRequest(BaseValidatorModel):
    remoteAccessSessionArn: str
    appArn: str


class ListDeviceInstancesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInstanceProfilesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsRequest(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListOfferingPromotionsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListOfferingTransactionsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListOfferingsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None


class ListProjectsRequest(BaseValidatorModel):
    arn: Optional[str] = None
    nextToken: Optional[str] = None


class ListRemoteAccessSessionsRequest(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListRunsRequest(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListSamplesRequest(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListSuitesRequest(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ListTestGridProjectsRequest(BaseValidatorModel):
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None


class ListTestGridSessionActionsRequest(BaseValidatorModel):
    sessionArn: str
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None


class TestGridSessionAction(BaseValidatorModel):
    action: Optional[str] = None
    started: Optional[datetime] = None
    duration: Optional[int] = None
    statusCode: Optional[str] = None
    requestMethod: Optional[str] = None


class ListTestsRequest(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListUniqueProblemsRequest(BaseValidatorModel):
    arn: str
    nextToken: Optional[str] = None


class ListVPCEConfigurationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class Location(BaseValidatorModel):
    latitude: float
    longitude: float


class MonetaryAmount(BaseValidatorModel):
    amount: Optional[float] = None
    currencyCode: Optional[Literal["USD"]] = None


class ProblemDetail(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None


class VpcConfigOutput(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str


class PurchaseOfferingRequest(BaseValidatorModel):
    offeringId: str
    quantity: int
    offeringPromotionId: Optional[str] = None


class Radios(BaseValidatorModel):
    wifi: Optional[bool] = None
    bluetooth: Optional[bool] = None
    nfc: Optional[bool] = None
    gps: Optional[bool] = None


class RenewOfferingRequest(BaseValidatorModel):
    offeringId: str
    quantity: int


class StopJobRequest(BaseValidatorModel):
    arn: str


class StopRemoteAccessSessionRequest(BaseValidatorModel):
    arn: str


class StopRunRequest(BaseValidatorModel):
    arn: str


class TestGridVpcConfigOutput(BaseValidatorModel):
    securityGroupIds: List[str]
    subnetIds: List[str]
    vpcId: str


class TestGridVpcConfig(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateDeviceInstanceRequest(BaseValidatorModel):
    arn: str
    profileArn: Optional[str] = None
    labels: Optional[Sequence[str]] = None


class UpdateInstanceProfileRequest(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    packageCleanup: Optional[bool] = None
    excludeAppPackagesFromCleanup: Optional[Sequence[str]] = None
    rebootAfterUse: Optional[bool] = None


class UpdateUploadRequest(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    contentType: Optional[str] = None
    editContent: Optional[bool] = None


class UpdateVPCEConfigurationRequest(BaseValidatorModel):
    arn: str
    vpceConfigurationName: Optional[str] = None
    vpceServiceName: Optional[str] = None
    serviceDnsName: Optional[str] = None
    vpceConfigurationDescription: Optional[str] = None


class VpcConfig(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    subnetIds: Sequence[str]
    vpcId: str


class AccountSettings(BaseValidatorModel):
    awsAccountNumber: Optional[str] = None
    unmeteredDevices: Optional[Dict[DevicePlatformType, int]] = None
    unmeteredRemoteAccessDevices: Optional[Dict[DevicePlatformType, int]] = None
    maxJobTimeoutMinutes: Optional[int] = None
    trialMinutes: Optional[TrialMinutes] = None
    maxSlots: Optional[Dict[str, int]] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    skipAppResign: Optional[bool] = None


class Rule(BaseValidatorModel):
    pass


class CreateDevicePoolRequest(BaseValidatorModel):
    projectArn: str
    name: str
    rules: Sequence[Rule]
    description: Optional[str] = None
    maxDevices: Optional[int] = None


class UpdateDevicePoolRequest(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    rules: Optional[Sequence[Rule]] = None
    maxDevices: Optional[int] = None
    clearMaxDevices: Optional[bool] = None


class CreateTestGridUrlResult(BaseValidatorModel):
    url: str
    expires: datetime
    ResponseMetadata: ResponseMetadata


class Artifact(BaseValidatorModel):
    pass


class ListArtifactsResult(BaseValidatorModel):
    artifacts: List[Artifact]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateInstanceProfileResult(BaseValidatorModel):
    instanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


class DeviceInstance(BaseValidatorModel):
    arn: Optional[str] = None
    deviceArn: Optional[str] = None
    labels: Optional[List[str]] = None
    status: Optional[InstanceStatusType] = None
    udid: Optional[str] = None
    instanceProfile: Optional[InstanceProfile] = None


class GetInstanceProfileResult(BaseValidatorModel):
    instanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


class ListInstanceProfilesResult(BaseValidatorModel):
    instanceProfiles: List[InstanceProfile]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateInstanceProfileResult(BaseValidatorModel):
    instanceProfile: InstanceProfile
    ResponseMetadata: ResponseMetadata


class NetworkProfile(BaseValidatorModel):
    pass


class CreateNetworkProfileResult(BaseValidatorModel):
    networkProfile: NetworkProfile
    ResponseMetadata: ResponseMetadata


class GetNetworkProfileResult(BaseValidatorModel):
    networkProfile: NetworkProfile
    ResponseMetadata: ResponseMetadata


class ListNetworkProfilesResult(BaseValidatorModel):
    networkProfiles: List[NetworkProfile]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateNetworkProfileResult(BaseValidatorModel):
    networkProfile: NetworkProfile
    ResponseMetadata: ResponseMetadata


class CreateRemoteAccessSessionConfiguration(BaseValidatorModel):
    billingMethod: Optional[BillingMethodType] = None
    vpceConfigurationArns: Optional[Sequence[str]] = None
    deviceProxy: Optional[DeviceProxy] = None


class Upload(BaseValidatorModel):
    pass


class CreateUploadResult(BaseValidatorModel):
    upload: Upload
    ResponseMetadata: ResponseMetadata


class GetUploadResult(BaseValidatorModel):
    upload: Upload
    ResponseMetadata: ResponseMetadata


class InstallToRemoteAccessSessionResult(BaseValidatorModel):
    appUpload: Upload
    ResponseMetadata: ResponseMetadata


class ListUploadsResult(BaseValidatorModel):
    uploads: List[Upload]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateUploadResult(BaseValidatorModel):
    upload: Upload
    ResponseMetadata: ResponseMetadata


class CreateVPCEConfigurationResult(BaseValidatorModel):
    vpceConfiguration: VPCEConfiguration
    ResponseMetadata: ResponseMetadata


class GetVPCEConfigurationResult(BaseValidatorModel):
    vpceConfiguration: VPCEConfiguration
    ResponseMetadata: ResponseMetadata


class ListVPCEConfigurationsResult(BaseValidatorModel):
    vpceConfigurations: List[VPCEConfiguration]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateVPCEConfigurationResult(BaseValidatorModel):
    vpceConfiguration: VPCEConfiguration
    ResponseMetadata: ResponseMetadata


class DeviceFilterOutput(BaseValidatorModel):
    pass


class DeviceSelectionResult(BaseValidatorModel):
    filters: Optional[List[DeviceFilterOutput]] = None
    matchedDevicesCount: Optional[int] = None
    maxDevices: Optional[int] = None


class GetOfferingStatusRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeviceInstancesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstanceProfilesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOfferingPromotionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOfferingTransactionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOfferingsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsRequestPaginate(BaseValidatorModel):
    arn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRemoteAccessSessionsRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRunsRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSamplesRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSuitesRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTestsRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUniqueProblemsRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListVPCEConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTestGridSessionResult(BaseValidatorModel):
    testGridSession: TestGridSession
    ResponseMetadata: ResponseMetadata


class ListTestGridSessionsResult(BaseValidatorModel):
    testGridSessions: List[TestGridSession]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class OfferingPromotion(BaseValidatorModel):
    pass


class ListOfferingPromotionsResult(BaseValidatorModel):
    offeringPromotions: List[OfferingPromotion]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Sample(BaseValidatorModel):
    pass


class ListSamplesResult(BaseValidatorModel):
    samples: List[Sample]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class ListTestGridSessionActionsResult(BaseValidatorModel):
    actions: List[TestGridSessionAction]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TestGridSessionArtifact(BaseValidatorModel):
    pass


class ListTestGridSessionArtifactsResult(BaseValidatorModel):
    artifacts: List[TestGridSessionArtifact]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class ListTestGridSessionsRequest(BaseValidatorModel):
    projectArn: str
    status: Optional[TestGridSessionStatusType] = None
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    endTimeAfter: Optional[Timestamp] = None
    endTimeBefore: Optional[Timestamp] = None
    maxResult: Optional[int] = None
    nextToken: Optional[str] = None


class RecurringCharge(BaseValidatorModel):
    cost: Optional[MonetaryAmount] = None
    frequency: Optional[Literal["MONTHLY"]] = None


class Project(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    created: Optional[datetime] = None
    vpcConfig: Optional[VpcConfigOutput] = None


class TestGridProject(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigOutput] = None
    created: Optional[datetime] = None


class GetAccountSettingsResult(BaseValidatorModel):
    accountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class DevicePool(BaseValidatorModel):
    pass


class CreateDevicePoolResult(BaseValidatorModel):
    devicePool: DevicePool
    ResponseMetadata: ResponseMetadata


class GetDevicePoolResult(BaseValidatorModel):
    devicePool: DevicePool
    ResponseMetadata: ResponseMetadata


class ListDevicePoolsResult(BaseValidatorModel):
    devicePools: List[DevicePool]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateDevicePoolResult(BaseValidatorModel):
    devicePool: DevicePool
    ResponseMetadata: ResponseMetadata


class Device(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    modelId: Optional[str] = None
    formFactor: Optional[DeviceFormFactorType] = None
    platform: Optional[DevicePlatformType] = None
    os: Optional[str] = None
    cpu: Optional[CPU] = None
    resolution: Optional[Resolution] = None
    heapSize: Optional[int] = None
    memory: Optional[int] = None
    image: Optional[str] = None
    carrier: Optional[str] = None
    radio: Optional[str] = None
    remoteAccessEnabled: Optional[bool] = None
    remoteDebugEnabled: Optional[bool] = None
    fleetType: Optional[str] = None
    fleetName: Optional[str] = None
    instances: Optional[List[DeviceInstance]] = None
    availability: Optional[DeviceAvailabilityType] = None


class GetDeviceInstanceResult(BaseValidatorModel):
    deviceInstance: DeviceInstance
    ResponseMetadata: ResponseMetadata


class ListDeviceInstancesResult(BaseValidatorModel):
    deviceInstances: List[DeviceInstance]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateDeviceInstanceResult(BaseValidatorModel):
    deviceInstance: DeviceInstance
    ResponseMetadata: ResponseMetadata


class CreateRemoteAccessSessionRequest(BaseValidatorModel):
    projectArn: str
    deviceArn: str
    instanceArn: Optional[str] = None
    sshPublicKey: Optional[str] = None
    remoteDebugEnabled: Optional[bool] = None
    remoteRecordEnabled: Optional[bool] = None
    remoteRecordAppArn: Optional[str] = None
    name: Optional[str] = None
    clientId: Optional[str] = None
    configuration: Optional[CreateRemoteAccessSessionConfiguration] = None
    interactionMode: Optional[InteractionModeType] = None
    skipAppResign: Optional[bool] = None


class CustomerArtifactPathsUnion(BaseValidatorModel):
    pass


class ScheduleRunConfiguration(BaseValidatorModel):
    extraDataPackageArn: Optional[str] = None
    networkProfileArn: Optional[str] = None
    locale: Optional[str] = None
    location: Optional[Location] = None
    vpceConfigurationArns: Optional[Sequence[str]] = None
    deviceProxy: Optional[DeviceProxy] = None
    customerArtifactPaths: Optional[CustomerArtifactPathsUnion] = None
    radios: Optional[Radios] = None
    auxiliaryApps: Optional[Sequence[str]] = None
    billingMethod: Optional[BillingMethodType] = None


class DeviceFilterUnion(BaseValidatorModel):
    pass


class DeviceSelectionConfiguration(BaseValidatorModel):
    filters: Sequence[DeviceFilterUnion]
    maxDevices: int


class ListDevicesRequestPaginate(BaseValidatorModel):
    arn: Optional[str] = None
    filters: Optional[Sequence[DeviceFilterUnion]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDevicesRequest(BaseValidatorModel):
    arn: Optional[str] = None
    nextToken: Optional[str] = None
    filters: Optional[Sequence[DeviceFilterUnion]] = None


class Suite(BaseValidatorModel):
    pass


class GetSuiteResult(BaseValidatorModel):
    suite: Suite
    ResponseMetadata: ResponseMetadata


class ListSuitesResult(BaseValidatorModel):
    suites: List[Suite]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Test(BaseValidatorModel):
    pass


class GetTestResult(BaseValidatorModel):
    test: Test
    ResponseMetadata: ResponseMetadata


class ListTestsResult(BaseValidatorModel):
    tests: List[Test]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateProjectResult(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class GetProjectResult(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class ListProjectsResult(BaseValidatorModel):
    projects: List[Project]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateProjectResult(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class CreateTestGridProjectResult(BaseValidatorModel):
    testGridProject: TestGridProject
    ResponseMetadata: ResponseMetadata


class GetTestGridProjectResult(BaseValidatorModel):
    testGridProject: TestGridProject
    ResponseMetadata: ResponseMetadata


class ListTestGridProjectsResult(BaseValidatorModel):
    testGridProjects: List[TestGridProject]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateTestGridProjectResult(BaseValidatorModel):
    testGridProject: TestGridProject
    ResponseMetadata: ResponseMetadata


class TestGridVpcConfigUnion(BaseValidatorModel):
    pass


class CreateTestGridProjectRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigUnion] = None


class UpdateTestGridProjectRequest(BaseValidatorModel):
    projectArn: str
    name: Optional[str] = None
    description: Optional[str] = None
    vpcConfig: Optional[TestGridVpcConfigUnion] = None


class VpcConfigUnion(BaseValidatorModel):
    pass


class CreateProjectRequest(BaseValidatorModel):
    name: str
    defaultJobTimeoutMinutes: Optional[int] = None
    vpcConfig: Optional[VpcConfigUnion] = None


class UpdateProjectRequest(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    defaultJobTimeoutMinutes: Optional[int] = None
    vpcConfig: Optional[VpcConfigUnion] = None


class IncompatibilityMessage(BaseValidatorModel):
    pass


class DevicePoolCompatibilityResult(BaseValidatorModel):
    device: Optional[Device] = None
    compatible: Optional[bool] = None
    incompatibilityMessages: Optional[List[IncompatibilityMessage]] = None


class GetDeviceResult(BaseValidatorModel):
    device: Device
    ResponseMetadata: ResponseMetadata


class ListDevicesResult(BaseValidatorModel):
    devices: List[Device]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Problem(BaseValidatorModel):
    run: Optional[ProblemDetail] = None
    job: Optional[ProblemDetail] = None
    suite: Optional[ProblemDetail] = None
    test: Optional[ProblemDetail] = None
    device: Optional[Device] = None
    result: Optional[ExecutionResultType] = None
    message: Optional[str] = None


class RemoteAccessSession(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    created: Optional[datetime] = None
    status: Optional[ExecutionStatusType] = None
    result: Optional[ExecutionResultType] = None
    message: Optional[str] = None
    started: Optional[datetime] = None
    stopped: Optional[datetime] = None
    device: Optional[Device] = None
    instanceArn: Optional[str] = None
    remoteDebugEnabled: Optional[bool] = None
    remoteRecordEnabled: Optional[bool] = None
    remoteRecordAppArn: Optional[str] = None
    hostAddress: Optional[str] = None
    clientId: Optional[str] = None
    billingMethod: Optional[BillingMethodType] = None
    deviceMinutes: Optional[DeviceMinutes] = None
    endpoint: Optional[str] = None
    deviceUdid: Optional[str] = None
    interactionMode: Optional[InteractionModeType] = None
    skipAppResign: Optional[bool] = None
    vpcConfig: Optional[VpcConfigOutput] = None
    deviceProxy: Optional[DeviceProxy] = None


class ScheduleRunTest(BaseValidatorModel):
    pass


class GetDevicePoolCompatibilityRequest(BaseValidatorModel):
    devicePoolArn: str
    appArn: Optional[str] = None
    testType: Optional[TestTypeType] = None
    test: Optional[ScheduleRunTest] = None
    configuration: Optional[ScheduleRunConfiguration] = None


class Run(BaseValidatorModel):
    pass


class GetRunResult(BaseValidatorModel):
    run: Run
    ResponseMetadata: ResponseMetadata


class ListRunsResult(BaseValidatorModel):
    runs: List[Run]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ScheduleRunResult(BaseValidatorModel):
    run: Run
    ResponseMetadata: ResponseMetadata


class StopRunResult(BaseValidatorModel):
    run: Run
    ResponseMetadata: ResponseMetadata


class ScheduleRunRequest(BaseValidatorModel):
    projectArn: str
    test: ScheduleRunTest
    appArn: Optional[str] = None
    devicePoolArn: Optional[str] = None
    deviceSelectionConfiguration: Optional[DeviceSelectionConfiguration] = None
    name: Optional[str] = None
    configuration: Optional[ScheduleRunConfiguration] = None
    executionConfiguration: Optional[ExecutionConfiguration] = None


class Offering(BaseValidatorModel):
    pass


class ListOfferingsResult(BaseValidatorModel):
    offerings: List[Offering]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetDevicePoolCompatibilityResult(BaseValidatorModel):
    compatibleDevices: List[DevicePoolCompatibilityResult]
    incompatibleDevices: List[DevicePoolCompatibilityResult]
    ResponseMetadata: ResponseMetadata


class Job(BaseValidatorModel):
    pass


class GetJobResult(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


class ListJobsResult(BaseValidatorModel):
    jobs: List[Job]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StopJobResult(BaseValidatorModel):
    job: Job
    ResponseMetadata: ResponseMetadata


class UniqueProblem(BaseValidatorModel):
    message: Optional[str] = None
    problems: Optional[List[Problem]] = None


class CreateRemoteAccessSessionResult(BaseValidatorModel):
    remoteAccessSession: RemoteAccessSession
    ResponseMetadata: ResponseMetadata


class GetRemoteAccessSessionResult(BaseValidatorModel):
    remoteAccessSession: RemoteAccessSession
    ResponseMetadata: ResponseMetadata


class ListRemoteAccessSessionsResult(BaseValidatorModel):
    remoteAccessSessions: List[RemoteAccessSession]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StopRemoteAccessSessionResult(BaseValidatorModel):
    remoteAccessSession: RemoteAccessSession
    ResponseMetadata: ResponseMetadata


class OfferingStatus(BaseValidatorModel):
    pass


class GetOfferingStatusResult(BaseValidatorModel):
    current: Dict[str, OfferingStatus]
    nextPeriod: Dict[str, OfferingStatus]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class OfferingTransaction(BaseValidatorModel):
    offeringStatus: Optional[OfferingStatus] = None
    transactionId: Optional[str] = None
    offeringPromotionId: Optional[str] = None
    createdOn: Optional[datetime] = None
    cost: Optional[MonetaryAmount] = None


class ListUniqueProblemsResult(BaseValidatorModel):
    uniqueProblems: Dict[ExecutionResultType, List[UniqueProblem]]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListOfferingTransactionsResult(BaseValidatorModel):
    offeringTransactions: List[OfferingTransaction]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PurchaseOfferingResult(BaseValidatorModel):
    offeringTransaction: OfferingTransaction
    ResponseMetadata: ResponseMetadata


class RenewOfferingResult(BaseValidatorModel):
    offeringTransaction: OfferingTransaction
    ResponseMetadata: ResponseMetadata



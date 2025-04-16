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
from aws_resource_validator.pydantic_models.lightsail_constants import *

class AccessKeyLastUsed(BaseValidatorModel):
    lastUsedDate: Optional[datetime] = None
    region: Optional[str] = None
    serviceName: Optional[str] = None


class AccessRules(BaseValidatorModel):
    getObject: Optional[AccessTypeType] = None
    allowPublicOverrides: Optional[bool] = None


class AccountLevelBpaSync(BaseValidatorModel):
    status: Optional[AccountLevelBpaSyncStatusType] = None
    lastSyncedAt: Optional[datetime] = None
    message: Optional[BPAStatusMessageType] = None
    bpaImpactsLightsail: Optional[bool] = None


class AutoSnapshotAddOnRequest(BaseValidatorModel):
    snapshotTimeOfDay: Optional[str] = None


class StopInstanceOnIdleRequest(BaseValidatorModel):
    threshold: Optional[str] = None
    duration: Optional[str] = None


class AddOn(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[str] = None
    snapshotTimeOfDay: Optional[str] = None
    nextSnapshotTimeOfDay: Optional[str] = None
    threshold: Optional[str] = None
    duration: Optional[str] = None


class MonitoredResourceInfo(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None


class ResourceLocation(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    regionName: Optional[RegionNameType] = None


class AllocateStaticIpRequest(BaseValidatorModel):
    staticIpName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AttachCertificateToDistributionRequest(BaseValidatorModel):
    distributionName: str
    certificateName: str


class AttachDiskRequest(BaseValidatorModel):
    diskName: str
    instanceName: str
    diskPath: str
    autoMounting: Optional[bool] = None


class AttachInstancesToLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str
    instanceNames: Sequence[str]


class AttachLoadBalancerTlsCertificateRequest(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str


class AttachStaticIpRequest(BaseValidatorModel):
    staticIpName: str
    instanceName: str


class AttachedDisk(BaseValidatorModel):
    path: Optional[str] = None
    sizeInGb: Optional[int] = None


class AvailabilityZone(BaseValidatorModel):
    zoneName: Optional[str] = None
    state: Optional[str] = None


class BucketAccessLogConfig(BaseValidatorModel):
    enabled: bool
    destination: Optional[str] = None
    prefix: Optional[str] = None


class BucketBundle(BaseValidatorModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    storagePerMonthInGb: Optional[int] = None
    transferPerMonthInGb: Optional[int] = None
    isActive: Optional[bool] = None


class BucketState(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class ResourceReceivingAccess(BaseValidatorModel):
    name: Optional[str] = None
    resourceType: Optional[str] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class Bundle(BaseValidatorModel):
    price: Optional[float] = None
    cpuCount: Optional[int] = None
    diskSizeInGb: Optional[int] = None
    bundleId: Optional[str] = None
    instanceType: Optional[str] = None
    isActive: Optional[bool] = None
    name: Optional[str] = None
    power: Optional[int] = None
    ramSizeInGb: Optional[float] = None
    transferPerMonthInGb: Optional[int] = None
    supportedPlatforms: Optional[List[InstancePlatformType]] = None
    supportedAppCategories: Optional[List[Literal["LfR"]]] = None
    publicIpv4AddressCount: Optional[int] = None


class CacheBehaviorPerPath(BaseValidatorModel):
    path: Optional[str] = None
    behavior: Optional[BehaviorEnumType] = None


class CacheBehavior(BaseValidatorModel):
    behavior: Optional[BehaviorEnumType] = None


class CookieObjectOutput(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    cookiesAllowList: Optional[List[str]] = None


class HeaderObjectOutput(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    headersAllowList: Optional[List[HeaderEnumType]] = None


class QueryStringObjectOutput(BaseValidatorModel):
    option: Optional[bool] = None
    queryStringsAllowList: Optional[List[str]] = None


class CookieObject(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    cookiesAllowList: Optional[Sequence[str]] = None


class HeaderObject(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    headersAllowList: Optional[Sequence[HeaderEnumType]] = None


class QueryStringObject(BaseValidatorModel):
    option: Optional[bool] = None
    queryStringsAllowList: Optional[Sequence[str]] = None


class PortInfo(BaseValidatorModel):
    fromPort: Optional[int] = None
    toPort: Optional[int] = None
    protocol: Optional[NetworkProtocolType] = None
    cidrs: Optional[Sequence[str]] = None
    ipv6Cidrs: Optional[Sequence[str]] = None
    cidrListAliases: Optional[Sequence[str]] = None


class CloudFormationStackRecordSourceInfo(BaseValidatorModel):
    resourceType: Optional[Literal["ExportSnapshotRecord"]] = None
    name: Optional[str] = None
    arn: Optional[str] = None


class ContainerImage(BaseValidatorModel):
    image: Optional[str] = None
    digest: Optional[str] = None
    createdAt: Optional[datetime] = None


class ContainerOutput(BaseValidatorModel):
    image: Optional[str] = None
    command: Optional[List[str]] = None
    environment: Optional[Dict[str, str]] = None
    ports: Optional[Dict[str, ContainerServiceProtocolType]] = None


class ContainerServiceECRImagePullerRoleRequest(BaseValidatorModel):
    isActive: Optional[bool] = None


class ContainerServiceECRImagePullerRole(BaseValidatorModel):
    isActive: Optional[bool] = None
    principalArn: Optional[str] = None


class ContainerServiceHealthCheckConfig(BaseValidatorModel):
    healthyThreshold: Optional[int] = None
    unhealthyThreshold: Optional[int] = None
    timeoutSeconds: Optional[int] = None
    intervalSeconds: Optional[int] = None
    path: Optional[str] = None
    successCodes: Optional[str] = None


class ContainerServiceLogEvent(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    message: Optional[str] = None


class ContainerServicePower(BaseValidatorModel):
    powerId: Optional[str] = None
    price: Optional[float] = None
    cpuCount: Optional[float] = None
    ramSizeInGb: Optional[float] = None
    name: Optional[str] = None
    isActive: Optional[bool] = None


class ContainerServiceRegistryLogin(BaseValidatorModel):
    username: Optional[str] = None
    password: Optional[str] = None
    expiresAt: Optional[datetime] = None
    registry: Optional[str] = None


class ContainerServiceStateDetail(BaseValidatorModel):
    code: Optional[ContainerServiceStateDetailCodeType] = None
    message: Optional[str] = None


class Container(BaseValidatorModel):
    image: Optional[str] = None
    command: Optional[Sequence[str]] = None
    environment: Optional[Mapping[str, str]] = None
    ports: Optional[Mapping[str, ContainerServiceProtocolType]] = None


class CopySnapshotRequest(BaseValidatorModel):
    targetSnapshotName: str
    sourceRegion: RegionNameType
    sourceSnapshotName: Optional[str] = None
    sourceResourceName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None


class CreateBucketAccessKeyRequest(BaseValidatorModel):
    bucketName: str


class InstanceEntry(BaseValidatorModel):
    sourceName: str
    instanceType: str
    portInfoSource: PortInfoSourceTypeType
    availabilityZone: str
    userData: Optional[str] = None


class CreateContactMethodRequest(BaseValidatorModel):
    protocol: ContactProtocolType
    contactEndpoint: str


class InputOrigin(BaseValidatorModel):
    name: Optional[str] = None
    regionName: Optional[RegionNameType] = None
    protocolPolicy: Optional[OriginProtocolPolicyEnumType] = None
    responseTimeout: Optional[int] = None


class CreateGUISessionAccessDetailsRequest(BaseValidatorModel):
    resourceName: str


class Session(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None
    isPrimary: Optional[bool] = None


class DiskMap(BaseValidatorModel):
    originalDiskPath: Optional[str] = None
    newDiskName: Optional[str] = None


class DeleteAlarmRequest(BaseValidatorModel):
    alarmName: str


class DeleteAutoSnapshotRequest(BaseValidatorModel):
    resourceName: str
    date: str


class DeleteBucketAccessKeyRequest(BaseValidatorModel):
    bucketName: str
    accessKeyId: str


class DeleteBucketRequest(BaseValidatorModel):
    bucketName: str
    forceDelete: Optional[bool] = None


class DeleteCertificateRequest(BaseValidatorModel):
    certificateName: str


class DeleteContactMethodRequest(BaseValidatorModel):
    protocol: ContactProtocolType


class DeleteContainerImageRequest(BaseValidatorModel):
    serviceName: str
    image: str


class DeleteContainerServiceRequest(BaseValidatorModel):
    serviceName: str


class DeleteDiskRequest(BaseValidatorModel):
    diskName: str
    forceDeleteAddOns: Optional[bool] = None


class DeleteDiskSnapshotRequest(BaseValidatorModel):
    diskSnapshotName: str


class DeleteDistributionRequest(BaseValidatorModel):
    distributionName: Optional[str] = None


class DeleteDomainRequest(BaseValidatorModel):
    domainName: str


class DeleteInstanceRequest(BaseValidatorModel):
    instanceName: str
    forceDeleteAddOns: Optional[bool] = None


class DeleteInstanceSnapshotRequest(BaseValidatorModel):
    instanceSnapshotName: str


class DeleteKeyPairRequest(BaseValidatorModel):
    keyPairName: str
    expectedFingerprint: Optional[str] = None


class DeleteKnownHostKeysRequest(BaseValidatorModel):
    instanceName: str


class DeleteLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str


class DeleteLoadBalancerTlsCertificateRequest(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str
    force: Optional[bool] = None


class DeleteRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str
    skipFinalSnapshot: Optional[bool] = None
    finalRelationalDatabaseSnapshotName: Optional[str] = None


class DeleteRelationalDatabaseSnapshotRequest(BaseValidatorModel):
    relationalDatabaseSnapshotName: str


class DetachCertificateFromDistributionRequest(BaseValidatorModel):
    distributionName: str


class DetachDiskRequest(BaseValidatorModel):
    diskName: str


class DetachInstancesFromLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str
    instanceNames: Sequence[str]


class DetachStaticIpRequest(BaseValidatorModel):
    staticIpName: str


class DisableAddOnRequest(BaseValidatorModel):
    addOnType: AddOnTypeType
    resourceName: str


class DiskInfo(BaseValidatorModel):
    name: Optional[str] = None
    path: Optional[str] = None
    sizeInGb: Optional[int] = None
    isSystemDisk: Optional[bool] = None


class DiskSnapshotInfo(BaseValidatorModel):
    sizeInGb: Optional[int] = None


class DistributionBundle(BaseValidatorModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    transferPerMonthInGb: Optional[int] = None
    isActive: Optional[bool] = None


class DnsRecordCreationState(BaseValidatorModel):
    code: Optional[DnsRecordCreationStateCodeType] = None
    message: Optional[str] = None


class TimePeriod(BaseValidatorModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class ExportSnapshotRequest(BaseValidatorModel):
    sourceSnapshotName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetActiveNamesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetAlarmsRequest(BaseValidatorModel):
    alarmName: Optional[str] = None
    pageToken: Optional[str] = None
    monitoredResourceName: Optional[str] = None


class GetAutoSnapshotsRequest(BaseValidatorModel):
    resourceName: str


class GetBlueprintsRequest(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    pageToken: Optional[str] = None
    appCategory: Optional[Literal["LfR"]] = None


class GetBucketAccessKeysRequest(BaseValidatorModel):
    bucketName: str


class GetBucketBundlesRequest(BaseValidatorModel):
    includeInactive: Optional[bool] = None


class GetBucketsRequest(BaseValidatorModel):
    bucketName: Optional[str] = None
    pageToken: Optional[str] = None
    includeConnectedResources: Optional[bool] = None


class GetBundlesRequest(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    pageToken: Optional[str] = None
    appCategory: Optional[Literal["LfR"]] = None


class GetCertificatesRequest(BaseValidatorModel):
    certificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    includeCertificateDetails: Optional[bool] = None
    certificateName: Optional[str] = None
    pageToken: Optional[str] = None


class GetCloudFormationStackRecordsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetContactMethodsRequest(BaseValidatorModel):
    protocols: Optional[Sequence[ContactProtocolType]] = None


class GetContainerImagesRequest(BaseValidatorModel):
    serviceName: str


class GetContainerServiceDeploymentsRequest(BaseValidatorModel):
    serviceName: str


class GetContainerServicesRequest(BaseValidatorModel):
    serviceName: Optional[str] = None


class GetDiskRequest(BaseValidatorModel):
    diskName: str


class GetDiskSnapshotRequest(BaseValidatorModel):
    diskSnapshotName: str


class GetDiskSnapshotsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetDisksRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetDistributionLatestCacheResetRequest(BaseValidatorModel):
    distributionName: Optional[str] = None


class GetDistributionsRequest(BaseValidatorModel):
    distributionName: Optional[str] = None
    pageToken: Optional[str] = None


class GetDomainRequest(BaseValidatorModel):
    domainName: str


class GetDomainsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetExportSnapshotRecordsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetInstanceAccessDetailsRequest(BaseValidatorModel):
    instanceName: str
    protocol: Optional[InstanceAccessProtocolType] = None


class GetInstancePortStatesRequest(BaseValidatorModel):
    instanceName: str


class InstancePortState(BaseValidatorModel):
    fromPort: Optional[int] = None
    toPort: Optional[int] = None
    protocol: Optional[NetworkProtocolType] = None
    state: Optional[PortStateType] = None
    cidrs: Optional[List[str]] = None
    ipv6Cidrs: Optional[List[str]] = None
    cidrListAliases: Optional[List[str]] = None


class GetInstanceRequest(BaseValidatorModel):
    instanceName: str


class GetInstanceSnapshotRequest(BaseValidatorModel):
    instanceSnapshotName: str


class GetInstanceSnapshotsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetInstanceStateRequest(BaseValidatorModel):
    instanceName: str


class InstanceState(BaseValidatorModel):
    code: Optional[int] = None
    name: Optional[str] = None


class GetInstancesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetKeyPairRequest(BaseValidatorModel):
    keyPairName: str


class GetKeyPairsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None
    includeDefaultKeyPair: Optional[bool] = None


class GetLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str


class GetLoadBalancerTlsCertificatesRequest(BaseValidatorModel):
    loadBalancerName: str


class GetLoadBalancerTlsPoliciesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class LoadBalancerTlsPolicy(BaseValidatorModel):
    name: Optional[str] = None
    isDefault: Optional[bool] = None
    description: Optional[str] = None
    protocols: Optional[List[str]] = None
    ciphers: Optional[List[str]] = None


class GetLoadBalancersRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetOperationRequest(BaseValidatorModel):
    operationId: str


class GetOperationsForResourceRequest(BaseValidatorModel):
    resourceName: str
    pageToken: Optional[str] = None


class GetOperationsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetRegionsRequest(BaseValidatorModel):
    includeAvailabilityZones: Optional[bool] = None
    includeRelationalDatabaseAvailabilityZones: Optional[bool] = None


class GetRelationalDatabaseBlueprintsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class RelationalDatabaseBlueprint(BaseValidatorModel):
    blueprintId: Optional[str] = None
    engine: Optional[Literal["mysql"]] = None
    engineVersion: Optional[str] = None
    engineDescription: Optional[str] = None
    engineVersionDescription: Optional[str] = None
    isEngineDefault: Optional[bool] = None


class GetRelationalDatabaseBundlesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None
    includeInactive: Optional[bool] = None


class RelationalDatabaseBundle(BaseValidatorModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    ramSizeInGb: Optional[float] = None
    diskSizeInGb: Optional[int] = None
    transferPerMonthInGb: Optional[int] = None
    cpuCount: Optional[int] = None
    isEncrypted: Optional[bool] = None
    isActive: Optional[bool] = None


class GetRelationalDatabaseEventsRequest(BaseValidatorModel):
    relationalDatabaseName: str
    durationInMinutes: Optional[int] = None
    pageToken: Optional[str] = None


class RelationalDatabaseEvent(BaseValidatorModel):
    resource: Optional[str] = None
    createdAt: Optional[datetime] = None
    message: Optional[str] = None
    eventCategories: Optional[List[str]] = None


class LogEvent(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    message: Optional[str] = None


class GetRelationalDatabaseLogStreamsRequest(BaseValidatorModel):
    relationalDatabaseName: str


class GetRelationalDatabaseMasterUserPasswordRequest(BaseValidatorModel):
    relationalDatabaseName: str
    passwordVersion: Optional[RelationalDatabasePasswordVersionType] = None


class GetRelationalDatabaseParametersRequest(BaseValidatorModel):
    relationalDatabaseName: str
    pageToken: Optional[str] = None


class RelationalDatabaseParameter(BaseValidatorModel):
    allowedValues: Optional[str] = None
    applyMethod: Optional[str] = None
    applyType: Optional[str] = None
    dataType: Optional[str] = None
    description: Optional[str] = None
    isModifiable: Optional[bool] = None
    parameterName: Optional[str] = None
    parameterValue: Optional[str] = None


class GetRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str


class GetRelationalDatabaseSnapshotRequest(BaseValidatorModel):
    relationalDatabaseSnapshotName: str


class GetRelationalDatabaseSnapshotsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetRelationalDatabasesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetSetupHistoryRequest(BaseValidatorModel):
    resourceName: str
    pageToken: Optional[str] = None


class GetStaticIpRequest(BaseValidatorModel):
    staticIpName: str


class GetStaticIpsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class HostKeyAttributes(BaseValidatorModel):
    algorithm: Optional[str] = None
    publicKey: Optional[str] = None
    witnessedAt: Optional[datetime] = None
    fingerprintSHA1: Optional[str] = None
    fingerprintSHA256: Optional[str] = None
    notValidBefore: Optional[datetime] = None
    notValidAfter: Optional[datetime] = None


class ImportKeyPairRequest(BaseValidatorModel):
    keyPairName: str
    publicKeyBase64: str


class PasswordData(BaseValidatorModel):
    ciphertext: Optional[str] = None
    keyPairName: Optional[str] = None


class InstanceHealthSummary(BaseValidatorModel):
    instanceName: Optional[str] = None
    instanceHealth: Optional[InstanceHealthStateType] = None
    instanceHealthReason: Optional[InstanceHealthReasonType] = None


class InstanceMetadataOptions(BaseValidatorModel):
    state: Optional[InstanceMetadataStateType] = None
    httpTokens: Optional[HttpTokensType] = None
    httpEndpoint: Optional[HttpEndpointType] = None
    httpPutResponseHopLimit: Optional[int] = None
    httpProtocolIpv6: Optional[HttpProtocolIpv6Type] = None


class InstancePortInfo(BaseValidatorModel):
    fromPort: Optional[int] = None
    toPort: Optional[int] = None
    protocol: Optional[NetworkProtocolType] = None
    accessFrom: Optional[str] = None
    accessType: Optional[PortAccessTypeType] = None
    commonName: Optional[str] = None
    accessDirection: Optional[AccessDirectionType] = None
    cidrs: Optional[List[str]] = None
    ipv6Cidrs: Optional[List[str]] = None
    cidrListAliases: Optional[List[str]] = None


class MonthlyTransfer(BaseValidatorModel):
    gbPerMonthAllocated: Optional[int] = None


class Origin(BaseValidatorModel):
    name: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    regionName: Optional[RegionNameType] = None
    protocolPolicy: Optional[OriginProtocolPolicyEnumType] = None
    responseTimeout: Optional[int] = None


class LoadBalancerTlsCertificateDnsRecordCreationState(BaseValidatorModel):
    code: Optional[LoadBalancerTlsCertificateDnsRecordCreationStateCodeType] = None
    message: Optional[str] = None


class LoadBalancerTlsCertificateDomainValidationOption(BaseValidatorModel):
    domainName: Optional[str] = None
    validationStatus: Optional[LoadBalancerTlsCertificateDomainStatusType] = None


class LoadBalancerTlsCertificateSummary(BaseValidatorModel):
    name: Optional[str] = None
    isAttached: Optional[bool] = None


class NameServersUpdateState(BaseValidatorModel):
    code: Optional[NameServersUpdateStateCodeType] = None
    message: Optional[str] = None


class PendingMaintenanceAction(BaseValidatorModel):
    action: Optional[str] = None
    description: Optional[str] = None
    currentApplyDate: Optional[datetime] = None


class PendingModifiedRelationalDatabaseValues(BaseValidatorModel):
    masterUserPassword: Optional[str] = None
    engineVersion: Optional[str] = None
    backupRetentionEnabled: Optional[bool] = None


class PutAlarmRequest(BaseValidatorModel):
    alarmName: str
    metricName: MetricNameType
    monitoredResourceName: str
    comparisonOperator: ComparisonOperatorType
    threshold: float
    evaluationPeriods: int
    datapointsToAlarm: Optional[int] = None
    treatMissingData: Optional[TreatMissingDataType] = None
    contactProtocols: Optional[Sequence[ContactProtocolType]] = None
    notificationTriggers: Optional[Sequence[AlarmStateType]] = None
    notificationEnabled: Optional[bool] = None


class R53HostedZoneDeletionState(BaseValidatorModel):
    code: Optional[R53HostedZoneDeletionStateCodeType] = None
    message: Optional[str] = None


class RebootInstanceRequest(BaseValidatorModel):
    instanceName: str


class RebootRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str


class RegisterContainerImageRequest(BaseValidatorModel):
    serviceName: str
    label: str
    digest: str


class RelationalDatabaseEndpoint(BaseValidatorModel):
    port: Optional[int] = None
    address: Optional[str] = None


class RelationalDatabaseHardware(BaseValidatorModel):
    cpuCount: Optional[int] = None
    diskSizeInGb: Optional[int] = None
    ramSizeInGb: Optional[float] = None


class ReleaseStaticIpRequest(BaseValidatorModel):
    staticIpName: str


class ResetDistributionCacheRequest(BaseValidatorModel):
    distributionName: Optional[str] = None


class SendContactMethodVerificationRequest(BaseValidatorModel):
    protocol: Literal["Email"]


class SetIpAddressTypeRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceName: str
    ipAddressType: IpAddressTypeType
    acceptBundleUpdate: Optional[bool] = None


class SetResourceAccessForBucketRequest(BaseValidatorModel):
    resourceName: str
    bucketName: str
    access: ResourceBucketAccessType


class SetupExecutionDetails(BaseValidatorModel):
    command: Optional[str] = None
    dateTime: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[SetupStatusType] = None
    standardError: Optional[str] = None
    standardOutput: Optional[str] = None
    version: Optional[str] = None


class SetupRequest(BaseValidatorModel):
    instanceName: Optional[str] = None
    domainNames: Optional[List[str]] = None
    certificateProvider: Optional[Literal["LetsEncrypt"]] = None


class SetupInstanceHttpsRequest(BaseValidatorModel):
    instanceName: str
    emailAddress: str
    domainNames: Sequence[str]
    certificateProvider: Literal["LetsEncrypt"]


class StartGUISessionRequest(BaseValidatorModel):
    resourceName: str


class StartInstanceRequest(BaseValidatorModel):
    instanceName: str


class StartRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str


class StopGUISessionRequest(BaseValidatorModel):
    resourceName: str


class StopInstanceRequest(BaseValidatorModel):
    instanceName: str
    force: Optional[bool] = None


class StopRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str
    relationalDatabaseSnapshotName: Optional[str] = None


class TestAlarmRequest(BaseValidatorModel):
    alarmName: str
    state: AlarmStateType


class UntagResourceRequest(BaseValidatorModel):
    resourceName: str
    tagKeys: Sequence[str]
    resourceArn: Optional[str] = None


class UpdateBucketBundleRequest(BaseValidatorModel):
    bucketName: str
    bundleId: str


class UpdateDistributionBundleRequest(BaseValidatorModel):
    distributionName: Optional[str] = None
    bundleId: Optional[str] = None


class UpdateInstanceMetadataOptionsRequest(BaseValidatorModel):
    instanceName: str
    httpTokens: Optional[HttpTokensType] = None
    httpEndpoint: Optional[HttpEndpointType] = None
    httpPutResponseHopLimit: Optional[int] = None
    httpProtocolIpv6: Optional[HttpProtocolIpv6Type] = None


class UpdateLoadBalancerAttributeRequest(BaseValidatorModel):
    loadBalancerName: str
    attributeName: LoadBalancerAttributeNameType
    attributeValue: str


class UpdateRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str
    masterUserPassword: Optional[str] = None
    rotateMasterUserPassword: Optional[bool] = None
    preferredBackupWindow: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None
    enableBackupRetention: Optional[bool] = None
    disableBackupRetention: Optional[bool] = None
    publiclyAccessible: Optional[bool] = None
    applyImmediately: Optional[bool] = None
    caCertificateIdentifier: Optional[str] = None
    relationalDatabaseBlueprintId: Optional[str] = None


class AccessKey(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    status: Optional[StatusTypeType] = None
    createdAt: Optional[datetime] = None
    lastUsed: Optional[AccessKeyLastUsed] = None


class AddOnRequest(BaseValidatorModel):
    addOnType: AddOnTypeType
    autoSnapshotAddOnRequest: Optional[AutoSnapshotAddOnRequest] = None
    stopInstanceOnIdleRequest: Optional[StopInstanceOnIdleRequest] = None


class Alarm(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    supportCode: Optional[str] = None
    monitoredResourceInfo: Optional[MonitoredResourceInfo] = None
    comparisonOperator: Optional[ComparisonOperatorType] = None
    evaluationPeriods: Optional[int] = None
    period: Optional[int] = None
    threshold: Optional[float] = None
    datapointsToAlarm: Optional[int] = None
    treatMissingData: Optional[TreatMissingDataType] = None
    statistic: Optional[MetricStatisticType] = None
    metricName: Optional[MetricNameType] = None
    state: Optional[AlarmStateType] = None
    unit: Optional[MetricUnitType] = None
    contactProtocols: Optional[List[ContactProtocolType]] = None
    notificationTriggers: Optional[List[AlarmStateType]] = None
    notificationEnabled: Optional[bool] = None


class ContactMethod(BaseValidatorModel):
    contactEndpoint: Optional[str] = None
    status: Optional[ContactMethodStatusType] = None
    protocol: Optional[ContactProtocolType] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    supportCode: Optional[str] = None


class SetupHistoryResource(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None


class StaticIp(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    ipAddress: Optional[str] = None
    attachedTo: Optional[str] = None
    isAttached: Optional[bool] = None


class DownloadDefaultKeyPairResult(BaseValidatorModel):
    publicKeyBase64: str
    privateKeyBase64: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


class GetActiveNamesResult(BaseValidatorModel):
    activeNames: List[str]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetContainerAPIMetadataResult(BaseValidatorModel):
    metadata: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata


class GetDistributionLatestCacheResetResult(BaseValidatorModel):
    status: str
    createTime: datetime
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseLogStreamsResult(BaseValidatorModel):
    logStreams: List[str]
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseMasterUserPasswordResult(BaseValidatorModel):
    masterUserPassword: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


class IsVpcPeeredResult(BaseValidatorModel):
    isPeered: bool
    ResponseMetadata: ResponseMetadata


class AutoSnapshotDetails(BaseValidatorModel):
    date: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[AutoSnapshotStatusType] = None
    fromAttachedDisks: Optional[List[AttachedDisk]] = None


class Region(BaseValidatorModel):
    continentCode: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    name: Optional[RegionNameType] = None
    availabilityZones: Optional[List[AvailabilityZone]] = None
    relationalDatabaseAvailabilityZones: Optional[List[AvailabilityZone]] = None


class Blueprint(BaseValidatorModel):
    pass


class GetBlueprintsResult(BaseValidatorModel):
    blueprints: List[Blueprint]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdateBucketRequest(BaseValidatorModel):
    bucketName: str
    accessRules: Optional[AccessRules] = None
    versioning: Optional[str] = None
    readonlyAccessAccounts: Optional[Sequence[str]] = None
    accessLogConfig: Optional[BucketAccessLogConfig] = None


class GetBucketBundlesResult(BaseValidatorModel):
    bundles: List[BucketBundle]
    ResponseMetadata: ResponseMetadata


class Bucket(BaseValidatorModel):
    resourceType: Optional[str] = None
    accessRules: Optional[AccessRules] = None
    arn: Optional[str] = None
    bundleId: Optional[str] = None
    createdAt: Optional[datetime] = None
    url: Optional[str] = None
    location: Optional[ResourceLocation] = None
    name: Optional[str] = None
    supportCode: Optional[str] = None
    tags: Optional[List[Tag]] = None
    objectVersioning: Optional[str] = None
    ableToUpdateBundle: Optional[bool] = None
    readonlyAccessAccounts: Optional[List[str]] = None
    resourcesReceivingAccess: Optional[List[ResourceReceivingAccess]] = None
    state: Optional[BucketState] = None
    accessLogConfig: Optional[BucketAccessLogConfig] = None


class CreateBucketRequest(BaseValidatorModel):
    bucketName: str
    bundleId: str
    tags: Optional[Sequence[Tag]] = None
    enableObjectVersioning: Optional[bool] = None


class CreateCertificateRequest(BaseValidatorModel):
    certificateName: str
    domainName: str
    subjectAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[Tag]] = None


class CreateDiskSnapshotRequest(BaseValidatorModel):
    diskSnapshotName: str
    diskName: Optional[str] = None
    instanceName: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class CreateDomainRequest(BaseValidatorModel):
    domainName: str
    tags: Optional[Sequence[Tag]] = None


class CreateInstanceSnapshotRequest(BaseValidatorModel):
    instanceSnapshotName: str
    instanceName: str
    tags: Optional[Sequence[Tag]] = None


class CreateKeyPairRequest(BaseValidatorModel):
    keyPairName: str
    tags: Optional[Sequence[Tag]] = None


class CreateLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str
    instancePort: int
    healthCheckPath: Optional[str] = None
    certificateName: Optional[str] = None
    certificateDomainName: Optional[str] = None
    certificateAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[Tag]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tlsPolicyName: Optional[str] = None


class CreateLoadBalancerTlsCertificateRequest(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str
    certificateDomainName: str
    certificateAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[Tag]] = None


class CreateRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str
    relationalDatabaseBlueprintId: str
    relationalDatabaseBundleId: str
    masterDatabaseName: str
    masterUsername: str
    availabilityZone: Optional[str] = None
    masterUserPassword: Optional[str] = None
    preferredBackupWindow: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    tags: Optional[Sequence[Tag]] = None


class CreateRelationalDatabaseSnapshotRequest(BaseValidatorModel):
    relationalDatabaseName: str
    relationalDatabaseSnapshotName: str
    tags: Optional[Sequence[Tag]] = None


class DiskSnapshot(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    sizeInGb: Optional[int] = None
    state: Optional[DiskSnapshotStateType] = None
    progress: Optional[str] = None
    fromDiskName: Optional[str] = None
    fromDiskArn: Optional[str] = None
    fromInstanceName: Optional[str] = None
    fromInstanceArn: Optional[str] = None
    isFromAutoSnapshot: Optional[bool] = None


class Disk(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    addOns: Optional[List[AddOn]] = None
    sizeInGb: Optional[int] = None
    isSystemDisk: Optional[bool] = None
    iops: Optional[int] = None
    path: Optional[str] = None
    state: Optional[DiskStateType] = None
    attachedTo: Optional[str] = None
    isAttached: Optional[bool] = None
    attachmentState: Optional[str] = None
    gbInUse: Optional[int] = None
    autoMountStatus: Optional[AutoMountStatusType] = None


class KeyPair(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    fingerprint: Optional[str] = None


class RelationalDatabaseSnapshot(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    engine: Optional[str] = None
    engineVersion: Optional[str] = None
    sizeInGb: Optional[int] = None
    state: Optional[str] = None
    fromRelationalDatabaseName: Optional[str] = None
    fromRelationalDatabaseArn: Optional[str] = None
    fromRelationalDatabaseBundleId: Optional[str] = None
    fromRelationalDatabaseBlueprintId: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceName: str
    tags: Sequence[Tag]
    resourceArn: Optional[str] = None


class GetBundlesResult(BaseValidatorModel):
    bundles: List[Bundle]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class CacheSettingsOutput(BaseValidatorModel):
    defaultTTL: Optional[int] = None
    minimumTTL: Optional[int] = None
    maximumTTL: Optional[int] = None
    allowedHTTPMethods: Optional[str] = None
    cachedHTTPMethods: Optional[str] = None
    forwardedCookies: Optional[CookieObjectOutput] = None
    forwardedHeaders: Optional[HeaderObjectOutput] = None
    forwardedQueryStrings: Optional[QueryStringObjectOutput] = None


class CacheSettings(BaseValidatorModel):
    defaultTTL: Optional[int] = None
    minimumTTL: Optional[int] = None
    maximumTTL: Optional[int] = None
    allowedHTTPMethods: Optional[str] = None
    cachedHTTPMethods: Optional[str] = None
    forwardedCookies: Optional[CookieObject] = None
    forwardedHeaders: Optional[HeaderObject] = None
    forwardedQueryStrings: Optional[QueryStringObject] = None


class CloseInstancePublicPortsRequest(BaseValidatorModel):
    portInfo: PortInfo
    instanceName: str


class OpenInstancePublicPortsRequest(BaseValidatorModel):
    portInfo: PortInfo
    instanceName: str


class PutInstancePublicPortsRequest(BaseValidatorModel):
    portInfos: Sequence[PortInfo]
    instanceName: str


class DestinationInfo(BaseValidatorModel):
    pass


class CloudFormationStackRecord(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    state: Optional[RecordStateType] = None
    sourceInfo: Optional[List[CloudFormationStackRecordSourceInfo]] = None
    destinationInfo: Optional[DestinationInfo] = None


class GetContainerImagesResult(BaseValidatorModel):
    containerImages: List[ContainerImage]
    ResponseMetadata: ResponseMetadata


class RegisterContainerImageResult(BaseValidatorModel):
    containerImage: ContainerImage
    ResponseMetadata: ResponseMetadata


class PrivateRegistryAccessRequest(BaseValidatorModel):
    ecrImagePullerRole: Optional[ContainerServiceECRImagePullerRoleRequest] = None


class PrivateRegistryAccess(BaseValidatorModel):
    ecrImagePullerRole: Optional[ContainerServiceECRImagePullerRole] = None


class ContainerServiceEndpoint(BaseValidatorModel):
    containerName: Optional[str] = None
    containerPort: Optional[int] = None
    healthCheck: Optional[ContainerServiceHealthCheckConfig] = None


class EndpointRequest(BaseValidatorModel):
    containerName: str
    containerPort: int
    healthCheck: Optional[ContainerServiceHealthCheckConfig] = None


class GetContainerLogResult(BaseValidatorModel):
    logEvents: List[ContainerServiceLogEvent]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetContainerServicePowersResult(BaseValidatorModel):
    powers: List[ContainerServicePower]
    ResponseMetadata: ResponseMetadata


class CreateContainerServiceRegistryLoginResult(BaseValidatorModel):
    registryLogin: ContainerServiceRegistryLogin
    ResponseMetadata: ResponseMetadata


class CreateCloudFormationStackRequest(BaseValidatorModel):
    instances: Sequence[InstanceEntry]


class CreateGUISessionAccessDetailsResult(BaseValidatorModel):
    resourceName: str
    status: StatusType
    percentageComplete: int
    failureReason: str
    sessions: List[Session]
    ResponseMetadata: ResponseMetadata


class Timestamp(BaseValidatorModel):
    pass


class CreateRelationalDatabaseFromSnapshotRequest(BaseValidatorModel):
    relationalDatabaseName: str
    availabilityZone: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    relationalDatabaseSnapshotName: Optional[str] = None
    relationalDatabaseBundleId: Optional[str] = None
    sourceRelationalDatabaseName: Optional[str] = None
    restoreTime: Optional[Timestamp] = None
    useLatestRestorableTime: Optional[bool] = None
    tags: Optional[Sequence[Tag]] = None


class GetBucketMetricDataRequest(BaseValidatorModel):
    bucketName: str
    metricName: BucketMetricNameType
    startTime: Timestamp
    endTime: Timestamp
    period: int
    statistics: Sequence[MetricStatisticType]
    unit: MetricUnitType


class GetContainerLogRequest(BaseValidatorModel):
    serviceName: str
    containerName: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    filterPattern: Optional[str] = None
    pageToken: Optional[str] = None


class GetContainerServiceMetricDataRequest(BaseValidatorModel):
    serviceName: str
    metricName: ContainerServiceMetricNameType
    startTime: Timestamp
    endTime: Timestamp
    period: int
    statistics: Sequence[MetricStatisticType]


class GetCostEstimateRequest(BaseValidatorModel):
    resourceName: str
    startTime: Timestamp
    endTime: Timestamp


class GetDistributionMetricDataRequest(BaseValidatorModel):
    distributionName: str
    metricName: DistributionMetricNameType
    startTime: Timestamp
    endTime: Timestamp
    period: int
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]


class GetInstanceMetricDataRequest(BaseValidatorModel):
    instanceName: str
    metricName: InstanceMetricNameType
    period: int
    startTime: Timestamp
    endTime: Timestamp
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]


class GetLoadBalancerMetricDataRequest(BaseValidatorModel):
    loadBalancerName: str
    metricName: LoadBalancerMetricNameType
    period: int
    startTime: Timestamp
    endTime: Timestamp
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]


class GetRelationalDatabaseLogEventsRequest(BaseValidatorModel):
    relationalDatabaseName: str
    logStreamName: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    startFromHead: Optional[bool] = None
    pageToken: Optional[str] = None


class GetRelationalDatabaseMetricDataRequest(BaseValidatorModel):
    relationalDatabaseName: str
    metricName: RelationalDatabaseMetricNameType
    period: int
    startTime: Timestamp
    endTime: Timestamp
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]


class InstanceSnapshotInfo(BaseValidatorModel):
    fromBundleId: Optional[str] = None
    fromBlueprintId: Optional[str] = None
    fromDiskInfo: Optional[List[DiskInfo]] = None


class GetDistributionBundlesResult(BaseValidatorModel):
    bundles: List[DistributionBundle]
    ResponseMetadata: ResponseMetadata


class ResourceRecord(BaseValidatorModel):
    pass


class DomainValidationRecord(BaseValidatorModel):
    domainName: Optional[str] = None
    resourceRecord: Optional[ResourceRecord] = None
    dnsRecordCreationState: Optional[DnsRecordCreationState] = None
    validationStatus: Optional[CertificateDomainValidationStatusType] = None


class EstimateByTime(BaseValidatorModel):
    usageCost: Optional[float] = None
    pricingUnit: Optional[PricingUnitType] = None
    unit: Optional[float] = None
    currency: Optional[Literal["USD"]] = None
    timePeriod: Optional[TimePeriod] = None


class GetActiveNamesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBlueprintsRequestPaginate(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    appCategory: Optional[Literal["LfR"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBundlesRequestPaginate(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    appCategory: Optional[Literal["LfR"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCloudFormationStackRecordsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDiskSnapshotsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDisksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDomainsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetExportSnapshotRecordsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetInstanceSnapshotsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetInstancesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetKeyPairsRequestPaginate(BaseValidatorModel):
    includeDefaultKeyPair: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetLoadBalancersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetOperationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRelationalDatabaseBlueprintsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRelationalDatabaseBundlesRequestPaginate(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRelationalDatabaseEventsRequestPaginate(BaseValidatorModel):
    relationalDatabaseName: str
    durationInMinutes: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRelationalDatabaseParametersRequestPaginate(BaseValidatorModel):
    relationalDatabaseName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRelationalDatabaseSnapshotsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetRelationalDatabasesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetStaticIpsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class MetricDatapoint(BaseValidatorModel):
    pass


class GetBucketMetricDataResult(BaseValidatorModel):
    metricName: BucketMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


class GetContainerServiceMetricDataResult(BaseValidatorModel):
    metricName: ContainerServiceMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


class GetDistributionMetricDataResult(BaseValidatorModel):
    metricName: DistributionMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


class GetInstanceMetricDataResult(BaseValidatorModel):
    metricName: InstanceMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


class GetLoadBalancerMetricDataResult(BaseValidatorModel):
    metricName: LoadBalancerMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseMetricDataResult(BaseValidatorModel):
    metricName: RelationalDatabaseMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


class GetInstancePortStatesResult(BaseValidatorModel):
    portStates: List[InstancePortState]
    ResponseMetadata: ResponseMetadata


class GetInstanceStateResult(BaseValidatorModel):
    state: InstanceState
    ResponseMetadata: ResponseMetadata


class GetLoadBalancerTlsPoliciesResult(BaseValidatorModel):
    tlsPolicies: List[LoadBalancerTlsPolicy]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseBlueprintsResult(BaseValidatorModel):
    blueprints: List[RelationalDatabaseBlueprint]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseBundlesResult(BaseValidatorModel):
    bundles: List[RelationalDatabaseBundle]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseEventsResult(BaseValidatorModel):
    relationalDatabaseEvents: List[RelationalDatabaseEvent]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseLogEventsResult(BaseValidatorModel):
    resourceLogEvents: List[LogEvent]
    nextBackwardToken: str
    nextForwardToken: str
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseParametersResult(BaseValidatorModel):
    parameters: List[RelationalDatabaseParameter]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdateRelationalDatabaseParametersRequest(BaseValidatorModel):
    relationalDatabaseName: str
    parameters: Sequence[RelationalDatabaseParameter]


class InstanceAccessDetails(BaseValidatorModel):
    certKey: Optional[str] = None
    expiresAt: Optional[datetime] = None
    ipAddress: Optional[str] = None
    ipv6Addresses: Optional[List[str]] = None
    password: Optional[str] = None
    passwordData: Optional[PasswordData] = None
    privateKey: Optional[str] = None
    protocol: Optional[InstanceAccessProtocolType] = None
    instanceName: Optional[str] = None
    username: Optional[str] = None
    hostKeys: Optional[List[HostKeyAttributes]] = None


class InstanceNetworking(BaseValidatorModel):
    monthlyTransfer: Optional[MonthlyTransfer] = None
    ports: Optional[List[InstancePortInfo]] = None


class LoadBalancerTlsCertificateRenewalSummary(BaseValidatorModel):
    renewalStatus: Optional[LoadBalancerTlsCertificateRenewalStatusType] = None
    domainValidationOptions: Optional[ List[LoadBalancerTlsCertificateDomainValidationOption] ] = None


class LoadBalancer(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    dnsName: Optional[str] = None
    state: Optional[LoadBalancerStateType] = None
    protocol: Optional[LoadBalancerProtocolType] = None
    publicPorts: Optional[List[int]] = None
    healthCheckPath: Optional[str] = None
    instancePort: Optional[int] = None
    instanceHealthSummary: Optional[List[InstanceHealthSummary]] = None
    tlsCertificateSummaries: Optional[List[LoadBalancerTlsCertificateSummary]] = None
    configurationOptions: Optional[Dict[LoadBalancerAttributeNameType, str]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    httpsRedirectionEnabled: Optional[bool] = None
    tlsPolicyName: Optional[str] = None


class RegisteredDomainDelegationInfo(BaseValidatorModel):
    nameServersUpdateState: Optional[NameServersUpdateState] = None
    r53HostedZoneDeletionState: Optional[R53HostedZoneDeletionState] = None


class RelationalDatabase(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    relationalDatabaseBlueprintId: Optional[str] = None
    relationalDatabaseBundleId: Optional[str] = None
    masterDatabaseName: Optional[str] = None
    hardware: Optional[RelationalDatabaseHardware] = None
    state: Optional[str] = None
    secondaryAvailabilityZone: Optional[str] = None
    backupRetentionEnabled: Optional[bool] = None
    pendingModifiedValues: Optional[PendingModifiedRelationalDatabaseValues] = None
    engine: Optional[str] = None
    engineVersion: Optional[str] = None
    latestRestorableTime: Optional[datetime] = None
    masterUsername: Optional[str] = None
    parameterApplyStatus: Optional[str] = None
    preferredBackupWindow: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    masterEndpoint: Optional[RelationalDatabaseEndpoint] = None
    pendingMaintenanceActions: Optional[List[PendingMaintenanceAction]] = None
    caCertificateIdentifier: Optional[str] = None


class GetBucketAccessKeysResult(BaseValidatorModel):
    accessKeys: List[AccessKey]
    ResponseMetadata: ResponseMetadata


class CreateDiskFromSnapshotRequest(BaseValidatorModel):
    diskName: str
    availabilityZone: str
    sizeInGb: int
    diskSnapshotName: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    addOns: Optional[Sequence[AddOnRequest]] = None
    sourceDiskName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None


class CreateDiskRequest(BaseValidatorModel):
    diskName: str
    availabilityZone: str
    sizeInGb: int
    tags: Optional[Sequence[Tag]] = None
    addOns: Optional[Sequence[AddOnRequest]] = None


class CreateInstancesFromSnapshotRequest(BaseValidatorModel):
    instanceNames: Sequence[str]
    availabilityZone: str
    bundleId: str
    attachedDiskMapping: Optional[Mapping[str, Sequence[DiskMap]]] = None
    instanceSnapshotName: Optional[str] = None
    userData: Optional[str] = None
    keyPairName: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    addOns: Optional[Sequence[AddOnRequest]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    sourceInstanceName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None


class CreateInstancesRequest(BaseValidatorModel):
    instanceNames: Sequence[str]
    availabilityZone: str
    blueprintId: str
    bundleId: str
    customImageName: Optional[str] = None
    userData: Optional[str] = None
    keyPairName: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    addOns: Optional[Sequence[AddOnRequest]] = None
    ipAddressType: Optional[IpAddressTypeType] = None


class EnableAddOnRequest(BaseValidatorModel):
    resourceName: str
    addOnRequest: AddOnRequest


class GetAlarmsResult(BaseValidatorModel):
    alarms: List[Alarm]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetContactMethodsResult(BaseValidatorModel):
    contactMethods: List[ContactMethod]
    ResponseMetadata: ResponseMetadata


class Operation(BaseValidatorModel):
    pass


class AllocateStaticIpResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class AttachCertificateToDistributionResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class AttachDiskResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class AttachInstancesToLoadBalancerResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class AttachLoadBalancerTlsCertificateResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class AttachStaticIpResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CloseInstancePublicPortsResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class CopySnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateBucketAccessKeyResult(BaseValidatorModel):
    accessKey: AccessKey
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateCloudFormationStackResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateContactMethodResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateDiskFromSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateDiskResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateDiskSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateDomainEntryResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class CreateDomainResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class CreateInstanceSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateInstancesFromSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateInstancesResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateLoadBalancerResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateLoadBalancerTlsCertificateResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateRelationalDatabaseFromSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class CreateRelationalDatabaseSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteAlarmResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteAutoSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteBucketAccessKeyResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteBucketResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteCertificateResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteContactMethodResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteDiskResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteDiskSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteDistributionResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class DeleteDomainEntryResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class DeleteDomainResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class DeleteInstanceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteInstanceSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteKeyPairResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class DeleteKnownHostKeysResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteLoadBalancerResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteLoadBalancerTlsCertificateResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DeleteRelationalDatabaseSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DetachCertificateFromDistributionResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class DetachDiskResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DetachInstancesFromLoadBalancerResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DetachStaticIpResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class DisableAddOnResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class EnableAddOnResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class ExportSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class GetOperationResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class GetOperationsForResourceResult(BaseValidatorModel):
    operations: List[Operation]
    nextPageCount: str
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetOperationsResult(BaseValidatorModel):
    operations: List[Operation]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class ImportKeyPairResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class OpenInstancePublicPortsResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class PeerVpcResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class PutAlarmResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class PutInstancePublicPortsResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class RebootInstanceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class RebootRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class ReleaseStaticIpResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class ResetDistributionCacheResult(BaseValidatorModel):
    status: str
    createTime: datetime
    operation: Operation
    ResponseMetadata: ResponseMetadata


class SendContactMethodVerificationResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class SetIpAddressTypeResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class SetResourceAccessForBucketResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class SetupInstanceHttpsResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class StartGUISessionResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class StartInstanceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class StartRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class StopGUISessionResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class StopInstanceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class StopRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class TagResourceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class TestAlarmResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class UnpeerVpcResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class UntagResourceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class UpdateBucketBundleResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class UpdateDistributionBundleResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class UpdateDistributionResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class UpdateDomainEntryResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class UpdateInstanceMetadataOptionsResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class UpdateLoadBalancerAttributeResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class UpdateRelationalDatabaseParametersResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class UpdateRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class SetupHistory(BaseValidatorModel):
    operationId: Optional[str] = None
    request: Optional[SetupRequest] = None
    resource: Optional[SetupHistoryResource] = None
    executionDetails: Optional[List[SetupExecutionDetails]] = None
    status: Optional[SetupStatusType] = None


class GetStaticIpResult(BaseValidatorModel):
    staticIp: StaticIp
    ResponseMetadata: ResponseMetadata


class GetStaticIpsResult(BaseValidatorModel):
    staticIps: List[StaticIp]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetAutoSnapshotsResult(BaseValidatorModel):
    resourceName: str
    resourceType: ResourceTypeType
    autoSnapshots: List[AutoSnapshotDetails]
    ResponseMetadata: ResponseMetadata


class GetRegionsResult(BaseValidatorModel):
    regions: List[Region]
    ResponseMetadata: ResponseMetadata


class CreateBucketResult(BaseValidatorModel):
    bucket: Bucket
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class GetBucketsResult(BaseValidatorModel):
    buckets: List[Bucket]
    nextPageToken: str
    accountLevelBpaSync: AccountLevelBpaSync
    ResponseMetadata: ResponseMetadata


class UpdateBucketResult(BaseValidatorModel):
    bucket: Bucket
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class GetDiskSnapshotResult(BaseValidatorModel):
    diskSnapshot: DiskSnapshot
    ResponseMetadata: ResponseMetadata


class GetDiskSnapshotsResult(BaseValidatorModel):
    diskSnapshots: List[DiskSnapshot]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetDiskResult(BaseValidatorModel):
    disk: Disk
    ResponseMetadata: ResponseMetadata


class GetDisksResult(BaseValidatorModel):
    disks: List[Disk]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class InstanceHardware(BaseValidatorModel):
    cpuCount: Optional[int] = None
    disks: Optional[List[Disk]] = None
    ramSizeInGb: Optional[float] = None


class InstanceSnapshot(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    state: Optional[InstanceSnapshotStateType] = None
    progress: Optional[str] = None
    fromAttachedDisks: Optional[List[Disk]] = None
    fromInstanceName: Optional[str] = None
    fromInstanceArn: Optional[str] = None
    fromBlueprintId: Optional[str] = None
    fromBundleId: Optional[str] = None
    isFromAutoSnapshot: Optional[bool] = None
    sizeInGb: Optional[int] = None


class CreateKeyPairResult(BaseValidatorModel):
    keyPair: KeyPair
    publicKeyBase64: str
    privateKeyBase64: str
    operation: Operation
    ResponseMetadata: ResponseMetadata


class GetKeyPairResult(BaseValidatorModel):
    keyPair: KeyPair
    ResponseMetadata: ResponseMetadata


class GetKeyPairsResult(BaseValidatorModel):
    keyPairs: List[KeyPair]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseSnapshotResult(BaseValidatorModel):
    relationalDatabaseSnapshot: RelationalDatabaseSnapshot
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabaseSnapshotsResult(BaseValidatorModel):
    relationalDatabaseSnapshots: List[RelationalDatabaseSnapshot]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class LightsailDistribution(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    alternativeDomainNames: Optional[List[str]] = None
    status: Optional[str] = None
    isEnabled: Optional[bool] = None
    domainName: Optional[str] = None
    bundleId: Optional[str] = None
    certificateName: Optional[str] = None
    origin: Optional[Origin] = None
    originPublicDNS: Optional[str] = None
    defaultCacheBehavior: Optional[CacheBehavior] = None
    cacheBehaviorSettings: Optional[CacheSettingsOutput] = None
    cacheBehaviors: Optional[List[CacheBehaviorPerPath]] = None
    ableToUpdateBundle: Optional[bool] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tags: Optional[List[Tag]] = None
    viewerMinimumTlsProtocolVersion: Optional[str] = None


class GetCloudFormationStackRecordsResult(BaseValidatorModel):
    cloudFormationStackRecords: List[CloudFormationStackRecord]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class UpdateContainerServiceRequest(BaseValidatorModel):
    serviceName: str
    power: Optional[ContainerServicePowerNameType] = None
    scale: Optional[int] = None
    isDisabled: Optional[bool] = None
    publicDomainNames: Optional[Mapping[str, Sequence[str]]] = None
    privateRegistryAccess: Optional[PrivateRegistryAccessRequest] = None


class ContainerServiceDeployment(BaseValidatorModel):
    version: Optional[int] = None
    state: Optional[ContainerServiceDeploymentStateType] = None
    containers: Optional[Dict[str, ContainerOutput]] = None
    publicEndpoint: Optional[ContainerServiceEndpoint] = None
    createdAt: Optional[datetime] = None


class ContainerUnion(BaseValidatorModel):
    pass


class ContainerServiceDeploymentRequest(BaseValidatorModel):
    containers: Optional[Mapping[str, ContainerUnion]] = None
    publicEndpoint: Optional[EndpointRequest] = None


class CreateContainerServiceDeploymentRequest(BaseValidatorModel):
    serviceName: str
    containers: Optional[Mapping[str, ContainerUnion]] = None
    publicEndpoint: Optional[EndpointRequest] = None


class ExportSnapshotRecordSourceInfo(BaseValidatorModel):
    resourceType: Optional[ExportSnapshotRecordSourceTypeType] = None
    createdAt: Optional[datetime] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    fromResourceName: Optional[str] = None
    fromResourceArn: Optional[str] = None
    instanceSnapshotInfo: Optional[InstanceSnapshotInfo] = None
    diskSnapshotInfo: Optional[DiskSnapshotInfo] = None


class DomainEntryUnion(BaseValidatorModel):
    pass


class CreateDomainEntryRequest(BaseValidatorModel):
    domainName: str
    domainEntry: DomainEntryUnion


class DeleteDomainEntryRequest(BaseValidatorModel):
    domainName: str
    domainEntry: DomainEntryUnion


class UpdateDomainEntryRequest(BaseValidatorModel):
    domainName: str
    domainEntry: DomainEntryUnion


class RenewalSummary(BaseValidatorModel):
    domainValidationRecords: Optional[List[DomainValidationRecord]] = None
    renewalStatus: Optional[RenewalStatusType] = None
    renewalStatusReason: Optional[str] = None
    updatedAt: Optional[datetime] = None


class CostEstimate(BaseValidatorModel):
    usageType: Optional[str] = None
    resultsByTime: Optional[List[EstimateByTime]] = None


class GetInstanceAccessDetailsResult(BaseValidatorModel):
    accessDetails: InstanceAccessDetails
    ResponseMetadata: ResponseMetadata


class LoadBalancerTlsCertificateDomainValidationRecord(BaseValidatorModel):
    pass


class LoadBalancerTlsCertificate(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    loadBalancerName: Optional[str] = None
    isAttached: Optional[bool] = None
    status: Optional[LoadBalancerTlsCertificateStatusType] = None
    domainName: Optional[str] = None
    domainValidationRecords: Optional[ List[LoadBalancerTlsCertificateDomainValidationRecord] ] = None
    failureReason: Optional[LoadBalancerTlsCertificateFailureReasonType] = None
    issuedAt: Optional[datetime] = None
    issuer: Optional[str] = None
    keyAlgorithm: Optional[str] = None
    notAfter: Optional[datetime] = None
    notBefore: Optional[datetime] = None
    renewalSummary: Optional[LoadBalancerTlsCertificateRenewalSummary] = None
    revocationReason: Optional[LoadBalancerTlsCertificateRevocationReasonType] = None
    revokedAt: Optional[datetime] = None
    serial: Optional[str] = None
    signatureAlgorithm: Optional[str] = None
    subject: Optional[str] = None
    subjectAlternativeNames: Optional[List[str]] = None


class GetLoadBalancerResult(BaseValidatorModel):
    loadBalancer: LoadBalancer
    ResponseMetadata: ResponseMetadata


class GetLoadBalancersResult(BaseValidatorModel):
    loadBalancers: List[LoadBalancer]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class DomainEntryOutput(BaseValidatorModel):
    pass


class Domain(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    domainEntries: Optional[List[DomainEntryOutput]] = None
    registeredDomainDelegationInfo: Optional[RegisteredDomainDelegationInfo] = None


class GetRelationalDatabaseResult(BaseValidatorModel):
    relationalDatabase: RelationalDatabase
    ResponseMetadata: ResponseMetadata


class GetRelationalDatabasesResult(BaseValidatorModel):
    relationalDatabases: List[RelationalDatabase]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetSetupHistoryResult(BaseValidatorModel):
    setupHistory: List[SetupHistory]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class Instance(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    blueprintId: Optional[str] = None
    blueprintName: Optional[str] = None
    bundleId: Optional[str] = None
    addOns: Optional[List[AddOn]] = None
    isStaticIp: Optional[bool] = None
    privateIpAddress: Optional[str] = None
    publicIpAddress: Optional[str] = None
    ipv6Addresses: Optional[List[str]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    hardware: Optional[InstanceHardware] = None
    networking: Optional[InstanceNetworking] = None
    state: Optional[InstanceState] = None
    username: Optional[str] = None
    sshKeyName: Optional[str] = None
    metadataOptions: Optional[InstanceMetadataOptions] = None


class GetInstanceSnapshotResult(BaseValidatorModel):
    instanceSnapshot: InstanceSnapshot
    ResponseMetadata: ResponseMetadata


class GetInstanceSnapshotsResult(BaseValidatorModel):
    instanceSnapshots: List[InstanceSnapshot]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class CreateDistributionResult(BaseValidatorModel):
    distribution: LightsailDistribution
    operation: Operation
    ResponseMetadata: ResponseMetadata


class GetDistributionsResult(BaseValidatorModel):
    distributions: List[LightsailDistribution]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class CacheSettingsUnion(BaseValidatorModel):
    pass


class CreateDistributionRequest(BaseValidatorModel):
    distributionName: str
    origin: InputOrigin
    defaultCacheBehavior: CacheBehavior
    bundleId: str
    cacheBehaviorSettings: Optional[CacheSettingsUnion] = None
    cacheBehaviors: Optional[Sequence[CacheBehaviorPerPath]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tags: Optional[Sequence[Tag]] = None
    certificateName: Optional[str] = None
    viewerMinimumTlsProtocolVersion: Optional[ViewerMinimumTlsProtocolVersionEnumType] = None


class UpdateDistributionRequest(BaseValidatorModel):
    distributionName: str
    origin: Optional[InputOrigin] = None
    defaultCacheBehavior: Optional[CacheBehavior] = None
    cacheBehaviorSettings: Optional[CacheSettingsUnion] = None
    cacheBehaviors: Optional[Sequence[CacheBehaviorPerPath]] = None
    isEnabled: Optional[bool] = None
    viewerMinimumTlsProtocolVersion: Optional[ViewerMinimumTlsProtocolVersionEnumType] = None
    certificateName: Optional[str] = None
    useDefaultCertificate: Optional[bool] = None


class ContainerService(BaseValidatorModel):
    containerServiceName: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[Tag]] = None
    power: Optional[ContainerServicePowerNameType] = None
    powerId: Optional[str] = None
    state: Optional[ContainerServiceStateType] = None
    stateDetail: Optional[ContainerServiceStateDetail] = None
    scale: Optional[int] = None
    currentDeployment: Optional[ContainerServiceDeployment] = None
    nextDeployment: Optional[ContainerServiceDeployment] = None
    isDisabled: Optional[bool] = None
    principalArn: Optional[str] = None
    privateDomainName: Optional[str] = None
    publicDomainNames: Optional[Dict[str, List[str]]] = None
    url: Optional[str] = None
    privateRegistryAccess: Optional[PrivateRegistryAccess] = None


class GetContainerServiceDeploymentsResult(BaseValidatorModel):
    deployments: List[ContainerServiceDeployment]
    ResponseMetadata: ResponseMetadata


class CreateContainerServiceRequest(BaseValidatorModel):
    serviceName: str
    power: ContainerServicePowerNameType
    scale: int
    tags: Optional[Sequence[Tag]] = None
    publicDomainNames: Optional[Mapping[str, Sequence[str]]] = None
    deployment: Optional[ContainerServiceDeploymentRequest] = None
    privateRegistryAccess: Optional[PrivateRegistryAccessRequest] = None


class ExportSnapshotRecord(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    state: Optional[RecordStateType] = None
    sourceInfo: Optional[ExportSnapshotRecordSourceInfo] = None
    destinationInfo: Optional[DestinationInfo] = None


class Certificate(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    domainName: Optional[str] = None
    status: Optional[CertificateStatusType] = None
    serialNumber: Optional[str] = None
    subjectAlternativeNames: Optional[List[str]] = None
    domainValidationRecords: Optional[List[DomainValidationRecord]] = None
    requestFailureReason: Optional[str] = None
    inUseResourceCount: Optional[int] = None
    keyAlgorithm: Optional[str] = None
    createdAt: Optional[datetime] = None
    issuedAt: Optional[datetime] = None
    issuerCA: Optional[str] = None
    notBefore: Optional[datetime] = None
    notAfter: Optional[datetime] = None
    eligibleToRenew: Optional[str] = None
    renewalSummary: Optional[RenewalSummary] = None
    revokedAt: Optional[datetime] = None
    revocationReason: Optional[str] = None
    tags: Optional[List[Tag]] = None
    supportCode: Optional[str] = None


class ResourceBudgetEstimate(BaseValidatorModel):
    resourceName: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    costEstimates: Optional[List[CostEstimate]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetLoadBalancerTlsCertificatesResult(BaseValidatorModel):
    tlsCertificates: List[LoadBalancerTlsCertificate]
    ResponseMetadata: ResponseMetadata


class GetDomainResult(BaseValidatorModel):
    domain: Domain
    ResponseMetadata: ResponseMetadata


class GetDomainsResult(BaseValidatorModel):
    domains: List[Domain]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetInstanceResult(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


class GetInstancesResult(BaseValidatorModel):
    instances: List[Instance]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class ContainerServicesListResult(BaseValidatorModel):
    containerServices: List[ContainerService]
    ResponseMetadata: ResponseMetadata


class CreateContainerServiceDeploymentResult(BaseValidatorModel):
    containerService: ContainerService
    ResponseMetadata: ResponseMetadata


class CreateContainerServiceResult(BaseValidatorModel):
    containerService: ContainerService
    ResponseMetadata: ResponseMetadata


class UpdateContainerServiceResult(BaseValidatorModel):
    containerService: ContainerService
    ResponseMetadata: ResponseMetadata


class GetExportSnapshotRecordsResult(BaseValidatorModel):
    exportSnapshotRecords: List[ExportSnapshotRecord]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class CertificateSummary(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateName: Optional[str] = None
    domainName: Optional[str] = None
    certificateDetail: Optional[Certificate] = None
    tags: Optional[List[Tag]] = None


class GetCostEstimateResult(BaseValidatorModel):
    resourcesBudgetEstimate: List[ResourceBudgetEstimate]
    ResponseMetadata: ResponseMetadata


class CreateCertificateResult(BaseValidatorModel):
    certificate: CertificateSummary
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class GetCertificatesResult(BaseValidatorModel):
    certificates: List[CertificateSummary]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata



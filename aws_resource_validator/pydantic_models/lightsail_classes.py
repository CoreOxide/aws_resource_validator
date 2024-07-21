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
from aws_resource_validator.pydantic_models.lightsail_constants import *

class AccessKeyLastUsedTypeDef(BaseModel):
    lastUsedDate: Optional[datetime] = None
    region: Optional[str] = None
    serviceName: Optional[str] = None

class AccessRulesTypeDef(BaseModel):
    getObject: Optional[AccessTypeType] = None
    allowPublicOverrides: Optional[bool] = None

class AccountLevelBpaSyncTypeDef(BaseModel):
    status: Optional[AccountLevelBpaSyncStatusType] = None
    lastSyncedAt: Optional[datetime] = None
    message: Optional[BPAStatusMessageType] = None
    bpaImpactsLightsail: Optional[bool] = None

class AutoSnapshotAddOnRequestTypeDef(BaseModel):
    snapshotTimeOfDay: Optional[str] = None

class StopInstanceOnIdleRequestTypeDef(BaseModel):
    threshold: Optional[str] = None
    duration: Optional[str] = None

class AddOnTypeDef(BaseModel):
    name: Optional[str] = None
    status: Optional[str] = None
    snapshotTimeOfDay: Optional[str] = None
    nextSnapshotTimeOfDay: Optional[str] = None
    threshold: Optional[str] = None
    duration: Optional[str] = None

class MonitoredResourceInfoTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None

class ResourceLocationTypeDef(BaseModel):
    availabilityZone: Optional[str] = None
    regionName: Optional[RegionNameType] = None

class AllocateStaticIpRequestRequestTypeDef(BaseModel):
    staticIpName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AttachCertificateToDistributionRequestRequestTypeDef(BaseModel):
    distributionName: str
    certificateName: str

class AttachDiskRequestRequestTypeDef(BaseModel):
    diskName: str
    instanceName: str
    diskPath: str
    autoMounting: Optional[bool] = None

class AttachInstancesToLoadBalancerRequestRequestTypeDef(BaseModel):
    loadBalancerName: str
    instanceNames: Sequence[str]

class AttachLoadBalancerTlsCertificateRequestRequestTypeDef(BaseModel):
    loadBalancerName: str
    certificateName: str

class AttachStaticIpRequestRequestTypeDef(BaseModel):
    staticIpName: str
    instanceName: str

class AttachedDiskTypeDef(BaseModel):
    path: Optional[str] = None
    sizeInGb: Optional[int] = None

class AvailabilityZoneTypeDef(BaseModel):
    zoneName: Optional[str] = None
    state: Optional[str] = None

class BlueprintTypeDef(BaseModel):
    blueprintId: Optional[str] = None
    name: Optional[str] = None
    group: Optional[str] = None
    type: Optional[BlueprintTypeType] = None
    description: Optional[str] = None
    isActive: Optional[bool] = None
    minPower: Optional[int] = None
    version: Optional[str] = None
    versionCode: Optional[str] = None
    productUrl: Optional[str] = None
    licenseUrl: Optional[str] = None
    platform: Optional[InstancePlatformType] = None
    appCategory: Optional[Literal["LfR"]] = None

class BucketAccessLogConfigTypeDef(BaseModel):
    enabled: bool
    destination: Optional[str] = None
    prefix: Optional[str] = None

class BucketBundleTypeDef(BaseModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    storagePerMonthInGb: Optional[int] = None
    transferPerMonthInGb: Optional[int] = None
    isActive: Optional[bool] = None

class BucketStateTypeDef(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

class ResourceReceivingAccessTypeDef(BaseModel):
    name: Optional[str] = None
    resourceType: Optional[str] = None

class TagTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class BundleTypeDef(BaseModel):
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

class CacheBehaviorPerPathTypeDef(BaseModel):
    path: Optional[str] = None
    behavior: Optional[BehaviorEnumType] = None

class CacheBehaviorTypeDef(BaseModel):
    behavior: Optional[BehaviorEnumType] = None

class CookieObjectOutputTypeDef(BaseModel):
    option: Optional[ForwardValuesType] = None
    cookiesAllowList: Optional[List[str]] = None

class HeaderObjectOutputTypeDef(BaseModel):
    option: Optional[ForwardValuesType] = None
    headersAllowList: Optional[List[HeaderEnumType]] = None

class QueryStringObjectOutputTypeDef(BaseModel):
    option: Optional[bool] = None
    queryStringsAllowList: Optional[List[str]] = None

class CookieObjectTypeDef(BaseModel):
    option: Optional[ForwardValuesType] = None
    cookiesAllowList: Optional[Sequence[str]] = None

class HeaderObjectTypeDef(BaseModel):
    option: Optional[ForwardValuesType] = None
    headersAllowList: Optional[Sequence[HeaderEnumType]] = None

class QueryStringObjectTypeDef(BaseModel):
    option: Optional[bool] = None
    queryStringsAllowList: Optional[Sequence[str]] = None

class PortInfoTypeDef(BaseModel):
    fromPort: Optional[int] = None
    toPort: Optional[int] = None
    protocol: Optional[NetworkProtocolType] = None
    cidrs: Optional[Sequence[str]] = None
    ipv6Cidrs: Optional[Sequence[str]] = None
    cidrListAliases: Optional[Sequence[str]] = None

class CloudFormationStackRecordSourceInfoTypeDef(BaseModel):
    resourceType: Optional[Literal["ExportSnapshotRecord"]] = None
    name: Optional[str] = None
    arn: Optional[str] = None

class DestinationInfoTypeDef(BaseModel):
    id: Optional[str] = None
    service: Optional[str] = None

class ContainerImageTypeDef(BaseModel):
    image: Optional[str] = None
    digest: Optional[str] = None
    createdAt: Optional[datetime] = None

class ContainerOutputTypeDef(BaseModel):
    image: Optional[str] = None
    command: Optional[List[str]] = None
    environment: Optional[Dict[str, str]] = None
    ports: Optional[Dict[str, ContainerServiceProtocolType]] = None

class ContainerTypeDef(BaseModel):
    image: Optional[str] = None
    command: Optional[Sequence[str]] = None
    environment: Optional[Mapping[str, str]] = None
    ports: Optional[Mapping[str, ContainerServiceProtocolType]] = None

class ContainerServiceECRImagePullerRoleRequestTypeDef(BaseModel):
    isActive: Optional[bool] = None

class ContainerServiceECRImagePullerRoleTypeDef(BaseModel):
    isActive: Optional[bool] = None
    principalArn: Optional[str] = None

class ContainerServiceHealthCheckConfigTypeDef(BaseModel):
    healthyThreshold: Optional[int] = None
    unhealthyThreshold: Optional[int] = None
    timeoutSeconds: Optional[int] = None
    intervalSeconds: Optional[int] = None
    path: Optional[str] = None
    successCodes: Optional[str] = None

class ContainerServiceLogEventTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    message: Optional[str] = None

class ContainerServicePowerTypeDef(BaseModel):
    powerId: Optional[str] = None
    price: Optional[float] = None
    cpuCount: Optional[float] = None
    ramSizeInGb: Optional[float] = None
    name: Optional[str] = None
    isActive: Optional[bool] = None

class ContainerServiceRegistryLoginTypeDef(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    expiresAt: Optional[datetime] = None
    registry: Optional[str] = None

class ContainerServiceStateDetailTypeDef(BaseModel):
    code: Optional[ContainerServiceStateDetailCodeType] = None
    message: Optional[str] = None

class CopySnapshotRequestRequestTypeDef(BaseModel):
    targetSnapshotName: str
    sourceRegion: RegionNameType
    sourceSnapshotName: Optional[str] = None
    sourceResourceName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None

class CreateBucketAccessKeyRequestRequestTypeDef(BaseModel):
    bucketName: str

class InstanceEntryTypeDef(BaseModel):
    sourceName: str
    instanceType: str
    portInfoSource: PortInfoSourceTypeType
    availabilityZone: str
    userData: Optional[str] = None

class CreateContactMethodRequestRequestTypeDef(BaseModel):
    protocol: ContactProtocolType
    contactEndpoint: str

class InputOriginTypeDef(BaseModel):
    name: Optional[str] = None
    regionName: Optional[RegionNameType] = None
    protocolPolicy: Optional[OriginProtocolPolicyEnumType] = None
    responseTimeout: Optional[int] = None

class DomainEntryTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    target: Optional[str] = None
    isAlias: Optional[bool] = None
    type: Optional[str] = None
    options: Optional[Mapping[str, str]] = None

class CreateGUISessionAccessDetailsRequestRequestTypeDef(BaseModel):
    resourceName: str

class SessionTypeDef(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None
    isPrimary: Optional[bool] = None

class DiskMapTypeDef(BaseModel):
    originalDiskPath: Optional[str] = None
    newDiskName: Optional[str] = None

class DeleteAlarmRequestRequestTypeDef(BaseModel):
    alarmName: str

class DeleteAutoSnapshotRequestRequestTypeDef(BaseModel):
    resourceName: str
    date: str

class DeleteBucketAccessKeyRequestRequestTypeDef(BaseModel):
    bucketName: str
    accessKeyId: str

class DeleteBucketRequestRequestTypeDef(BaseModel):
    bucketName: str
    forceDelete: Optional[bool] = None

class DeleteCertificateRequestRequestTypeDef(BaseModel):
    certificateName: str

class DeleteContactMethodRequestRequestTypeDef(BaseModel):
    protocol: ContactProtocolType

class DeleteContainerImageRequestRequestTypeDef(BaseModel):
    serviceName: str
    image: str

class DeleteContainerServiceRequestRequestTypeDef(BaseModel):
    serviceName: str

class DeleteDiskRequestRequestTypeDef(BaseModel):
    diskName: str
    forceDeleteAddOns: Optional[bool] = None

class DeleteDiskSnapshotRequestRequestTypeDef(BaseModel):
    diskSnapshotName: str

class DeleteDistributionRequestRequestTypeDef(BaseModel):
    distributionName: Optional[str] = None

class DeleteDomainRequestRequestTypeDef(BaseModel):
    domainName: str

class DeleteInstanceRequestRequestTypeDef(BaseModel):
    instanceName: str
    forceDeleteAddOns: Optional[bool] = None

class DeleteInstanceSnapshotRequestRequestTypeDef(BaseModel):
    instanceSnapshotName: str

class DeleteKeyPairRequestRequestTypeDef(BaseModel):
    keyPairName: str
    expectedFingerprint: Optional[str] = None

class DeleteKnownHostKeysRequestRequestTypeDef(BaseModel):
    instanceName: str

class DeleteLoadBalancerRequestRequestTypeDef(BaseModel):
    loadBalancerName: str

class DeleteLoadBalancerTlsCertificateRequestRequestTypeDef(BaseModel):
    loadBalancerName: str
    certificateName: str
    force: Optional[bool] = None

class DeleteRelationalDatabaseRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    skipFinalSnapshot: Optional[bool] = None
    finalRelationalDatabaseSnapshotName: Optional[str] = None

class DeleteRelationalDatabaseSnapshotRequestRequestTypeDef(BaseModel):
    relationalDatabaseSnapshotName: str

class DetachCertificateFromDistributionRequestRequestTypeDef(BaseModel):
    distributionName: str

class DetachDiskRequestRequestTypeDef(BaseModel):
    diskName: str

class DetachInstancesFromLoadBalancerRequestRequestTypeDef(BaseModel):
    loadBalancerName: str
    instanceNames: Sequence[str]

class DetachStaticIpRequestRequestTypeDef(BaseModel):
    staticIpName: str

class DisableAddOnRequestRequestTypeDef(BaseModel):
    addOnType: AddOnTypeType
    resourceName: str

class DiskInfoTypeDef(BaseModel):
    name: Optional[str] = None
    path: Optional[str] = None
    sizeInGb: Optional[int] = None
    isSystemDisk: Optional[bool] = None

class DiskSnapshotInfoTypeDef(BaseModel):
    sizeInGb: Optional[int] = None

class DistributionBundleTypeDef(BaseModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    transferPerMonthInGb: Optional[int] = None
    isActive: Optional[bool] = None

class DnsRecordCreationStateTypeDef(BaseModel):
    code: Optional[DnsRecordCreationStateCodeType] = None
    message: Optional[str] = None

class DomainEntryExtraOutputTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    target: Optional[str] = None
    isAlias: Optional[bool] = None
    type: Optional[str] = None
    options: Optional[Dict[str, str]] = None

class DomainEntryOutputTypeDef(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    target: Optional[str] = None
    isAlias: Optional[bool] = None
    type: Optional[str] = None
    options: Optional[Dict[str, str]] = None

class ResourceRecordTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None

class TimePeriodTypeDef(BaseModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None

class ExportSnapshotRequestRequestTypeDef(BaseModel):
    sourceSnapshotName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetActiveNamesRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetAlarmsRequestRequestTypeDef(BaseModel):
    alarmName: Optional[str] = None
    pageToken: Optional[str] = None
    monitoredResourceName: Optional[str] = None

class GetAutoSnapshotsRequestRequestTypeDef(BaseModel):
    resourceName: str

class GetBlueprintsRequestRequestTypeDef(BaseModel):
    includeInactive: Optional[bool] = None
    pageToken: Optional[str] = None
    appCategory: Optional[Literal["LfR"]] = None

class GetBucketAccessKeysRequestRequestTypeDef(BaseModel):
    bucketName: str

class GetBucketBundlesRequestRequestTypeDef(BaseModel):
    includeInactive: Optional[bool] = None

class MetricDatapointTypeDef(BaseModel):
    average: Optional[float] = None
    maximum: Optional[float] = None
    minimum: Optional[float] = None
    sampleCount: Optional[float] = None
    sum: Optional[float] = None
    timestamp: Optional[datetime] = None
    unit: Optional[MetricUnitType] = None

class GetBucketsRequestRequestTypeDef(BaseModel):
    bucketName: Optional[str] = None
    pageToken: Optional[str] = None
    includeConnectedResources: Optional[bool] = None

class GetBundlesRequestRequestTypeDef(BaseModel):
    includeInactive: Optional[bool] = None
    pageToken: Optional[str] = None
    appCategory: Optional[Literal["LfR"]] = None

class GetCertificatesRequestRequestTypeDef(BaseModel):
    certificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    includeCertificateDetails: Optional[bool] = None
    certificateName: Optional[str] = None
    pageToken: Optional[str] = None

class GetCloudFormationStackRecordsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetContactMethodsRequestRequestTypeDef(BaseModel):
    protocols: Optional[Sequence[ContactProtocolType]] = None

class GetContainerImagesRequestRequestTypeDef(BaseModel):
    serviceName: str

class GetContainerServiceDeploymentsRequestRequestTypeDef(BaseModel):
    serviceName: str

class GetContainerServicesRequestRequestTypeDef(BaseModel):
    serviceName: Optional[str] = None

class GetDiskRequestRequestTypeDef(BaseModel):
    diskName: str

class GetDiskSnapshotRequestRequestTypeDef(BaseModel):
    diskSnapshotName: str

class GetDiskSnapshotsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetDisksRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetDistributionLatestCacheResetRequestRequestTypeDef(BaseModel):
    distributionName: Optional[str] = None

class GetDistributionsRequestRequestTypeDef(BaseModel):
    distributionName: Optional[str] = None
    pageToken: Optional[str] = None

class GetDomainRequestRequestTypeDef(BaseModel):
    domainName: str

class GetDomainsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetExportSnapshotRecordsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetInstanceAccessDetailsRequestRequestTypeDef(BaseModel):
    instanceName: str
    protocol: Optional[InstanceAccessProtocolType] = None

class GetInstancePortStatesRequestRequestTypeDef(BaseModel):
    instanceName: str

class InstancePortStateTypeDef(BaseModel):
    fromPort: Optional[int] = None
    toPort: Optional[int] = None
    protocol: Optional[NetworkProtocolType] = None
    state: Optional[PortStateType] = None
    cidrs: Optional[List[str]] = None
    ipv6Cidrs: Optional[List[str]] = None
    cidrListAliases: Optional[List[str]] = None

class GetInstanceRequestRequestTypeDef(BaseModel):
    instanceName: str

class GetInstanceSnapshotRequestRequestTypeDef(BaseModel):
    instanceSnapshotName: str

class GetInstanceSnapshotsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetInstanceStateRequestRequestTypeDef(BaseModel):
    instanceName: str

class InstanceStateTypeDef(BaseModel):
    code: Optional[int] = None
    name: Optional[str] = None

class GetInstancesRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetKeyPairRequestRequestTypeDef(BaseModel):
    keyPairName: str

class GetKeyPairsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None
    includeDefaultKeyPair: Optional[bool] = None

class GetLoadBalancerRequestRequestTypeDef(BaseModel):
    loadBalancerName: str

class GetLoadBalancerTlsCertificatesRequestRequestTypeDef(BaseModel):
    loadBalancerName: str

class GetLoadBalancerTlsPoliciesRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class LoadBalancerTlsPolicyTypeDef(BaseModel):
    name: Optional[str] = None
    isDefault: Optional[bool] = None
    description: Optional[str] = None
    protocols: Optional[List[str]] = None
    ciphers: Optional[List[str]] = None

class GetLoadBalancersRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetOperationRequestRequestTypeDef(BaseModel):
    operationId: str

class GetOperationsForResourceRequestRequestTypeDef(BaseModel):
    resourceName: str
    pageToken: Optional[str] = None

class GetOperationsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetRegionsRequestRequestTypeDef(BaseModel):
    includeAvailabilityZones: Optional[bool] = None
    includeRelationalDatabaseAvailabilityZones: Optional[bool] = None

class GetRelationalDatabaseBlueprintsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class RelationalDatabaseBlueprintTypeDef(BaseModel):
    blueprintId: Optional[str] = None
    engine: Optional[Literal["mysql"]] = None
    engineVersion: Optional[str] = None
    engineDescription: Optional[str] = None
    engineVersionDescription: Optional[str] = None
    isEngineDefault: Optional[bool] = None

class GetRelationalDatabaseBundlesRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None
    includeInactive: Optional[bool] = None

class RelationalDatabaseBundleTypeDef(BaseModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    ramSizeInGb: Optional[float] = None
    diskSizeInGb: Optional[int] = None
    transferPerMonthInGb: Optional[int] = None
    cpuCount: Optional[int] = None
    isEncrypted: Optional[bool] = None
    isActive: Optional[bool] = None

class GetRelationalDatabaseEventsRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    durationInMinutes: Optional[int] = None
    pageToken: Optional[str] = None

class RelationalDatabaseEventTypeDef(BaseModel):
    resource: Optional[str] = None
    createdAt: Optional[datetime] = None
    message: Optional[str] = None
    eventCategories: Optional[List[str]] = None

class LogEventTypeDef(BaseModel):
    createdAt: Optional[datetime] = None
    message: Optional[str] = None

class GetRelationalDatabaseLogStreamsRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str

class GetRelationalDatabaseMasterUserPasswordRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    passwordVersion: Optional[RelationalDatabasePasswordVersionType] = None

class GetRelationalDatabaseParametersRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    pageToken: Optional[str] = None

class RelationalDatabaseParameterTypeDef(BaseModel):
    allowedValues: Optional[str] = None
    applyMethod: Optional[str] = None
    applyType: Optional[str] = None
    dataType: Optional[str] = None
    description: Optional[str] = None
    isModifiable: Optional[bool] = None
    parameterName: Optional[str] = None
    parameterValue: Optional[str] = None

class GetRelationalDatabaseRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str

class GetRelationalDatabaseSnapshotRequestRequestTypeDef(BaseModel):
    relationalDatabaseSnapshotName: str

class GetRelationalDatabaseSnapshotsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetRelationalDatabasesRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class GetSetupHistoryRequestRequestTypeDef(BaseModel):
    resourceName: str
    pageToken: Optional[str] = None

class GetStaticIpRequestRequestTypeDef(BaseModel):
    staticIpName: str

class GetStaticIpsRequestRequestTypeDef(BaseModel):
    pageToken: Optional[str] = None

class HostKeyAttributesTypeDef(BaseModel):
    algorithm: Optional[str] = None
    publicKey: Optional[str] = None
    witnessedAt: Optional[datetime] = None
    fingerprintSHA1: Optional[str] = None
    fingerprintSHA256: Optional[str] = None
    notValidBefore: Optional[datetime] = None
    notValidAfter: Optional[datetime] = None

class ImportKeyPairRequestRequestTypeDef(BaseModel):
    keyPairName: str
    publicKeyBase64: str

class PasswordDataTypeDef(BaseModel):
    ciphertext: Optional[str] = None
    keyPairName: Optional[str] = None

class InstanceHealthSummaryTypeDef(BaseModel):
    instanceName: Optional[str] = None
    instanceHealth: Optional[InstanceHealthStateType] = None
    instanceHealthReason: Optional[InstanceHealthReasonType] = None

class InstanceMetadataOptionsTypeDef(BaseModel):
    state: Optional[InstanceMetadataStateType] = None
    httpTokens: Optional[HttpTokensType] = None
    httpEndpoint: Optional[HttpEndpointType] = None
    httpPutResponseHopLimit: Optional[int] = None
    httpProtocolIpv6: Optional[HttpProtocolIpv6Type] = None

class InstancePortInfoTypeDef(BaseModel):
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

class MonthlyTransferTypeDef(BaseModel):
    gbPerMonthAllocated: Optional[int] = None

class OriginTypeDef(BaseModel):
    name: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    regionName: Optional[RegionNameType] = None
    protocolPolicy: Optional[OriginProtocolPolicyEnumType] = None
    responseTimeout: Optional[int] = None

class LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef(BaseModel):
    code: Optional[LoadBalancerTlsCertificateDnsRecordCreationStateCodeType] = None
    message: Optional[str] = None

class LoadBalancerTlsCertificateDomainValidationOptionTypeDef(BaseModel):
    domainName: Optional[str] = None
    validationStatus: Optional[LoadBalancerTlsCertificateDomainStatusType] = None

class LoadBalancerTlsCertificateSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    isAttached: Optional[bool] = None

class NameServersUpdateStateTypeDef(BaseModel):
    code: Optional[NameServersUpdateStateCodeType] = None
    message: Optional[str] = None

class PendingMaintenanceActionTypeDef(BaseModel):
    action: Optional[str] = None
    description: Optional[str] = None
    currentApplyDate: Optional[datetime] = None

class PendingModifiedRelationalDatabaseValuesTypeDef(BaseModel):
    masterUserPassword: Optional[str] = None
    engineVersion: Optional[str] = None
    backupRetentionEnabled: Optional[bool] = None

class PutAlarmRequestRequestTypeDef(BaseModel):
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

class R53HostedZoneDeletionStateTypeDef(BaseModel):
    code: Optional[R53HostedZoneDeletionStateCodeType] = None
    message: Optional[str] = None

class RebootInstanceRequestRequestTypeDef(BaseModel):
    instanceName: str

class RebootRelationalDatabaseRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str

class RegisterContainerImageRequestRequestTypeDef(BaseModel):
    serviceName: str
    label: str
    digest: str

class RelationalDatabaseEndpointTypeDef(BaseModel):
    port: Optional[int] = None
    address: Optional[str] = None

class RelationalDatabaseHardwareTypeDef(BaseModel):
    cpuCount: Optional[int] = None
    diskSizeInGb: Optional[int] = None
    ramSizeInGb: Optional[float] = None

class ReleaseStaticIpRequestRequestTypeDef(BaseModel):
    staticIpName: str

class ResetDistributionCacheRequestRequestTypeDef(BaseModel):
    distributionName: Optional[str] = None

class SendContactMethodVerificationRequestRequestTypeDef(BaseModel):
    protocol: Literal["Email"]

class SetIpAddressTypeRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    resourceName: str
    ipAddressType: IpAddressTypeType
    acceptBundleUpdate: Optional[bool] = None

class SetResourceAccessForBucketRequestRequestTypeDef(BaseModel):
    resourceName: str
    bucketName: str
    access: ResourceBucketAccessType

class SetupExecutionDetailsTypeDef(BaseModel):
    command: Optional[str] = None
    dateTime: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[SetupStatusType] = None
    standardError: Optional[str] = None
    standardOutput: Optional[str] = None
    version: Optional[str] = None

class SetupRequestTypeDef(BaseModel):
    instanceName: Optional[str] = None
    domainNames: Optional[List[str]] = None
    certificateProvider: Optional[Literal["LetsEncrypt"]] = None

class SetupInstanceHttpsRequestRequestTypeDef(BaseModel):
    instanceName: str
    emailAddress: str
    domainNames: Sequence[str]
    certificateProvider: Literal["LetsEncrypt"]

class StartGUISessionRequestRequestTypeDef(BaseModel):
    resourceName: str

class StartInstanceRequestRequestTypeDef(BaseModel):
    instanceName: str

class StartRelationalDatabaseRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str

class StopGUISessionRequestRequestTypeDef(BaseModel):
    resourceName: str

class StopInstanceRequestRequestTypeDef(BaseModel):
    instanceName: str
    force: Optional[bool] = None

class StopRelationalDatabaseRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    relationalDatabaseSnapshotName: Optional[str] = None

class TestAlarmRequestRequestTypeDef(BaseModel):
    alarmName: str
    state: AlarmStateType

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceName: str
    tagKeys: Sequence[str]
    resourceArn: Optional[str] = None

class UpdateBucketBundleRequestRequestTypeDef(BaseModel):
    bucketName: str
    bundleId: str

class UpdateDistributionBundleRequestRequestTypeDef(BaseModel):
    distributionName: Optional[str] = None
    bundleId: Optional[str] = None

class UpdateInstanceMetadataOptionsRequestRequestTypeDef(BaseModel):
    instanceName: str
    httpTokens: Optional[HttpTokensType] = None
    httpEndpoint: Optional[HttpEndpointType] = None
    httpPutResponseHopLimit: Optional[int] = None
    httpProtocolIpv6: Optional[HttpProtocolIpv6Type] = None

class UpdateLoadBalancerAttributeRequestRequestTypeDef(BaseModel):
    loadBalancerName: str
    attributeName: LoadBalancerAttributeNameType
    attributeValue: str

class UpdateRelationalDatabaseRequestRequestTypeDef(BaseModel):
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

class AccessKeyTypeDef(BaseModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    status: Optional[StatusTypeType] = None
    createdAt: Optional[datetime] = None
    lastUsed: Optional[AccessKeyLastUsedTypeDef] = None

class AddOnRequestTypeDef(BaseModel):
    addOnType: AddOnTypeType
    autoSnapshotAddOnRequest: Optional[AutoSnapshotAddOnRequestTypeDef] = None
    stopInstanceOnIdleRequest: Optional[StopInstanceOnIdleRequestTypeDef] = None

class AlarmTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    supportCode: Optional[str] = None
    monitoredResourceInfo: Optional[MonitoredResourceInfoTypeDef] = None
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

class ContactMethodTypeDef(BaseModel):
    contactEndpoint: Optional[str] = None
    status: Optional[ContactMethodStatusType] = None
    protocol: Optional[ContactProtocolType] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    supportCode: Optional[str] = None

class OperationTypeDef(BaseModel):
    id: Optional[str] = None
    resourceName: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    isTerminal: Optional[bool] = None
    operationDetails: Optional[str] = None
    operationType: Optional[OperationTypeType] = None
    status: Optional[OperationStatusType] = None
    statusChangedAt: Optional[datetime] = None
    errorCode: Optional[str] = None
    errorDetails: Optional[str] = None

class SetupHistoryResourceTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None

class StaticIpTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    ipAddress: Optional[str] = None
    attachedTo: Optional[str] = None
    isAttached: Optional[bool] = None

class DownloadDefaultKeyPairResultTypeDef(BaseModel):
    publicKeyBase64: str
    privateKeyBase64: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetActiveNamesResultTypeDef(BaseModel):
    activeNames: List[str]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContainerAPIMetadataResultTypeDef(BaseModel):
    metadata: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionLatestCacheResetResultTypeDef(BaseModel):
    status: str
    createTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseLogStreamsResultTypeDef(BaseModel):
    logStreams: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseMasterUserPasswordResultTypeDef(BaseModel):
    masterUserPassword: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class IsVpcPeeredResultTypeDef(BaseModel):
    isPeered: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AutoSnapshotDetailsTypeDef(BaseModel):
    date: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[AutoSnapshotStatusType] = None
    fromAttachedDisks: Optional[List[AttachedDiskTypeDef]] = None

class RegionTypeDef(BaseModel):
    continentCode: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    name: Optional[RegionNameType] = None
    availabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    relationalDatabaseAvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None

class GetBlueprintsResultTypeDef(BaseModel):
    blueprints: List[BlueprintTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBucketRequestRequestTypeDef(BaseModel):
    bucketName: str
    accessRules: Optional[AccessRulesTypeDef] = None
    versioning: Optional[str] = None
    readonlyAccessAccounts: Optional[Sequence[str]] = None
    accessLogConfig: Optional[BucketAccessLogConfigTypeDef] = None

class GetBucketBundlesResultTypeDef(BaseModel):
    bundles: List[BucketBundleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BucketTypeDef(BaseModel):
    resourceType: Optional[str] = None
    accessRules: Optional[AccessRulesTypeDef] = None
    arn: Optional[str] = None
    bundleId: Optional[str] = None
    createdAt: Optional[datetime] = None
    url: Optional[str] = None
    location: Optional[ResourceLocationTypeDef] = None
    name: Optional[str] = None
    supportCode: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None
    objectVersioning: Optional[str] = None
    ableToUpdateBundle: Optional[bool] = None
    readonlyAccessAccounts: Optional[List[str]] = None
    resourcesReceivingAccess: Optional[List[ResourceReceivingAccessTypeDef]] = None
    state: Optional[BucketStateTypeDef] = None
    accessLogConfig: Optional[BucketAccessLogConfigTypeDef] = None

class CreateBucketRequestRequestTypeDef(BaseModel):
    bucketName: str
    bundleId: str
    tags: Optional[Sequence[TagTypeDef]] = None
    enableObjectVersioning: Optional[bool] = None

class CreateCertificateRequestRequestTypeDef(BaseModel):
    certificateName: str
    domainName: str
    subjectAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateDiskSnapshotRequestRequestTypeDef(BaseModel):
    diskSnapshotName: str
    diskName: Optional[str] = None
    instanceName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateDomainRequestRequestTypeDef(BaseModel):
    domainName: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateInstanceSnapshotRequestRequestTypeDef(BaseModel):
    instanceSnapshotName: str
    instanceName: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateKeyPairRequestRequestTypeDef(BaseModel):
    keyPairName: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateLoadBalancerRequestRequestTypeDef(BaseModel):
    loadBalancerName: str
    instancePort: int
    healthCheckPath: Optional[str] = None
    certificateName: Optional[str] = None
    certificateDomainName: Optional[str] = None
    certificateAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tlsPolicyName: Optional[str] = None

class CreateLoadBalancerTlsCertificateRequestRequestTypeDef(BaseModel):
    loadBalancerName: str
    certificateName: str
    certificateDomainName: str
    certificateAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRelationalDatabaseRequestRequestTypeDef(BaseModel):
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
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRelationalDatabaseSnapshotRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    relationalDatabaseSnapshotName: str
    tags: Optional[Sequence[TagTypeDef]] = None

class DiskSnapshotTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    sizeInGb: Optional[int] = None
    state: Optional[DiskSnapshotStateType] = None
    progress: Optional[str] = None
    fromDiskName: Optional[str] = None
    fromDiskArn: Optional[str] = None
    fromInstanceName: Optional[str] = None
    fromInstanceArn: Optional[str] = None
    isFromAutoSnapshot: Optional[bool] = None

class DiskTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    addOns: Optional[List[AddOnTypeDef]] = None
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

class KeyPairTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    fingerprint: Optional[str] = None

class RelationalDatabaseSnapshotTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    engine: Optional[str] = None
    engineVersion: Optional[str] = None
    sizeInGb: Optional[int] = None
    state: Optional[str] = None
    fromRelationalDatabaseName: Optional[str] = None
    fromRelationalDatabaseArn: Optional[str] = None
    fromRelationalDatabaseBundleId: Optional[str] = None
    fromRelationalDatabaseBlueprintId: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceName: str
    tags: Sequence[TagTypeDef]
    resourceArn: Optional[str] = None

class GetBundlesResultTypeDef(BaseModel):
    bundles: List[BundleTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSettingsOutputTypeDef(BaseModel):
    defaultTTL: Optional[int] = None
    minimumTTL: Optional[int] = None
    maximumTTL: Optional[int] = None
    allowedHTTPMethods: Optional[str] = None
    cachedHTTPMethods: Optional[str] = None
    forwardedCookies: Optional[CookieObjectOutputTypeDef] = None
    forwardedHeaders: Optional[HeaderObjectOutputTypeDef] = None
    forwardedQueryStrings: Optional[QueryStringObjectOutputTypeDef] = None

class CacheSettingsTypeDef(BaseModel):
    defaultTTL: Optional[int] = None
    minimumTTL: Optional[int] = None
    maximumTTL: Optional[int] = None
    allowedHTTPMethods: Optional[str] = None
    cachedHTTPMethods: Optional[str] = None
    forwardedCookies: Optional[CookieObjectTypeDef] = None
    forwardedHeaders: Optional[HeaderObjectTypeDef] = None
    forwardedQueryStrings: Optional[QueryStringObjectTypeDef] = None

class CloseInstancePublicPortsRequestRequestTypeDef(BaseModel):
    portInfo: PortInfoTypeDef
    instanceName: str

class OpenInstancePublicPortsRequestRequestTypeDef(BaseModel):
    portInfo: PortInfoTypeDef
    instanceName: str

class PutInstancePublicPortsRequestRequestTypeDef(BaseModel):
    portInfos: Sequence[PortInfoTypeDef]
    instanceName: str

class CloudFormationStackRecordTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    state: Optional[RecordStateType] = None
    sourceInfo: Optional[List[CloudFormationStackRecordSourceInfoTypeDef]] = None
    destinationInfo: Optional[DestinationInfoTypeDef] = None

class GetContainerImagesResultTypeDef(BaseModel):
    containerImages: List[ContainerImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterContainerImageResultTypeDef(BaseModel):
    containerImage: ContainerImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PrivateRegistryAccessRequestTypeDef(BaseModel):
    ecrImagePullerRole: Optional[ContainerServiceECRImagePullerRoleRequestTypeDef] = None

class PrivateRegistryAccessTypeDef(BaseModel):
    ecrImagePullerRole: Optional[ContainerServiceECRImagePullerRoleTypeDef] = None

class ContainerServiceEndpointTypeDef(BaseModel):
    containerName: Optional[str] = None
    containerPort: Optional[int] = None
    healthCheck: Optional[ContainerServiceHealthCheckConfigTypeDef] = None

class EndpointRequestTypeDef(BaseModel):
    containerName: str
    containerPort: int
    healthCheck: Optional[ContainerServiceHealthCheckConfigTypeDef] = None

class GetContainerLogResultTypeDef(BaseModel):
    logEvents: List[ContainerServiceLogEventTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContainerServicePowersResultTypeDef(BaseModel):
    powers: List[ContainerServicePowerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContainerServiceRegistryLoginResultTypeDef(BaseModel):
    registryLogin: ContainerServiceRegistryLoginTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudFormationStackRequestRequestTypeDef(BaseModel):
    instances: Sequence[InstanceEntryTypeDef]

class CreateDomainEntryRequestRequestTypeDef(BaseModel):
    domainName: str
    domainEntry: DomainEntryTypeDef

class DeleteDomainEntryRequestRequestTypeDef(BaseModel):
    domainName: str
    domainEntry: DomainEntryTypeDef

class UpdateDomainEntryRequestRequestTypeDef(BaseModel):
    domainName: str
    domainEntry: DomainEntryTypeDef

class CreateGUISessionAccessDetailsResultTypeDef(BaseModel):
    resourceName: str
    status: StatusType
    percentageComplete: int
    failureReason: str
    sessions: List[SessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelationalDatabaseFromSnapshotRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    availabilityZone: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    relationalDatabaseSnapshotName: Optional[str] = None
    relationalDatabaseBundleId: Optional[str] = None
    sourceRelationalDatabaseName: Optional[str] = None
    restoreTime: Optional[TimestampTypeDef] = None
    useLatestRestorableTime: Optional[bool] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class GetBucketMetricDataRequestRequestTypeDef(BaseModel):
    bucketName: str
    metricName: BucketMetricNameType
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    period: int
    statistics: Sequence[MetricStatisticType]
    unit: MetricUnitType

class GetContainerLogRequestRequestTypeDef(BaseModel):
    serviceName: str
    containerName: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    filterPattern: Optional[str] = None
    pageToken: Optional[str] = None

class GetContainerServiceMetricDataRequestRequestTypeDef(BaseModel):
    serviceName: str
    metricName: ContainerServiceMetricNameType
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    period: int
    statistics: Sequence[MetricStatisticType]

class GetCostEstimateRequestRequestTypeDef(BaseModel):
    resourceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef

class GetDistributionMetricDataRequestRequestTypeDef(BaseModel):
    distributionName: str
    metricName: DistributionMetricNameType
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    period: int
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]

class GetInstanceMetricDataRequestRequestTypeDef(BaseModel):
    instanceName: str
    metricName: InstanceMetricNameType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]

class GetLoadBalancerMetricDataRequestRequestTypeDef(BaseModel):
    loadBalancerName: str
    metricName: LoadBalancerMetricNameType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]

class GetRelationalDatabaseLogEventsRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    logStreamName: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    startFromHead: Optional[bool] = None
    pageToken: Optional[str] = None

class GetRelationalDatabaseMetricDataRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    metricName: RelationalDatabaseMetricNameType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]

class InstanceSnapshotInfoTypeDef(BaseModel):
    fromBundleId: Optional[str] = None
    fromBlueprintId: Optional[str] = None
    fromDiskInfo: Optional[List[DiskInfoTypeDef]] = None

class GetDistributionBundlesResultTypeDef(BaseModel):
    bundles: List[DistributionBundleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DomainValidationRecordTypeDef(BaseModel):
    domainName: Optional[str] = None
    resourceRecord: Optional[ResourceRecordTypeDef] = None
    dnsRecordCreationState: Optional[DnsRecordCreationStateTypeDef] = None
    validationStatus: Optional[CertificateDomainValidationStatusType] = None

class EstimateByTimeTypeDef(BaseModel):
    usageCost: Optional[float] = None
    pricingUnit: Optional[PricingUnitType] = None
    unit: Optional[float] = None
    currency: Optional[Literal["USD"]] = None
    timePeriod: Optional[TimePeriodTypeDef] = None

class GetActiveNamesRequestGetActiveNamesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBlueprintsRequestGetBlueprintsPaginateTypeDef(BaseModel):
    includeInactive: Optional[bool] = None
    appCategory: Optional[Literal["LfR"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBundlesRequestGetBundlesPaginateTypeDef(BaseModel):
    includeInactive: Optional[bool] = None
    appCategory: Optional[Literal["LfR"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCloudFormationStackRecordsRequestGetCloudFormationStackRecordsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDiskSnapshotsRequestGetDiskSnapshotsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDisksRequestGetDisksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDomainsRequestGetDomainsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetExportSnapshotRecordsRequestGetExportSnapshotRecordsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInstanceSnapshotsRequestGetInstanceSnapshotsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInstancesRequestGetInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetKeyPairsRequestGetKeyPairsPaginateTypeDef(BaseModel):
    includeDefaultKeyPair: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetLoadBalancersRequestGetLoadBalancersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetOperationsRequestGetOperationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRelationalDatabaseBlueprintsRequestGetRelationalDatabaseBlueprintsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRelationalDatabaseBundlesRequestGetRelationalDatabaseBundlesPaginateTypeDef(BaseModel):
    includeInactive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRelationalDatabaseEventsRequestGetRelationalDatabaseEventsPaginateTypeDef(BaseModel):
    relationalDatabaseName: str
    durationInMinutes: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRelationalDatabaseParametersRequestGetRelationalDatabaseParametersPaginateTypeDef(BaseModel):
    relationalDatabaseName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRelationalDatabaseSnapshotsRequestGetRelationalDatabaseSnapshotsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetRelationalDatabasesRequestGetRelationalDatabasesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetStaticIpsRequestGetStaticIpsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetBucketMetricDataResultTypeDef(BaseModel):
    metricName: BucketMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetContainerServiceMetricDataResultTypeDef(BaseModel):
    metricName: ContainerServiceMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionMetricDataResultTypeDef(BaseModel):
    metricName: DistributionMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceMetricDataResultTypeDef(BaseModel):
    metricName: InstanceMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoadBalancerMetricDataResultTypeDef(BaseModel):
    metricName: LoadBalancerMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseMetricDataResultTypeDef(BaseModel):
    metricName: RelationalDatabaseMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstancePortStatesResultTypeDef(BaseModel):
    portStates: List[InstancePortStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceStateResultTypeDef(BaseModel):
    state: InstanceStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoadBalancerTlsPoliciesResultTypeDef(BaseModel):
    tlsPolicies: List[LoadBalancerTlsPolicyTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseBlueprintsResultTypeDef(BaseModel):
    blueprints: List[RelationalDatabaseBlueprintTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseBundlesResultTypeDef(BaseModel):
    bundles: List[RelationalDatabaseBundleTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseEventsResultTypeDef(BaseModel):
    relationalDatabaseEvents: List[RelationalDatabaseEventTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseLogEventsResultTypeDef(BaseModel):
    resourceLogEvents: List[LogEventTypeDef]
    nextBackwardToken: str
    nextForwardToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseParametersResultTypeDef(BaseModel):
    parameters: List[RelationalDatabaseParameterTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRelationalDatabaseParametersRequestRequestTypeDef(BaseModel):
    relationalDatabaseName: str
    parameters: Sequence[RelationalDatabaseParameterTypeDef]

class InstanceAccessDetailsTypeDef(BaseModel):
    certKey: Optional[str] = None
    expiresAt: Optional[datetime] = None
    ipAddress: Optional[str] = None
    ipv6Addresses: Optional[List[str]] = None
    password: Optional[str] = None
    passwordData: Optional[PasswordDataTypeDef] = None
    privateKey: Optional[str] = None
    protocol: Optional[InstanceAccessProtocolType] = None
    instanceName: Optional[str] = None
    username: Optional[str] = None
    hostKeys: Optional[List[HostKeyAttributesTypeDef]] = None

class InstanceNetworkingTypeDef(BaseModel):
    monthlyTransfer: Optional[MonthlyTransferTypeDef] = None
    ports: Optional[List[InstancePortInfoTypeDef]] = None

class LoadBalancerTlsCertificateDomainValidationRecordTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    validationStatus: Optional[LoadBalancerTlsCertificateDomainStatusType] = None
    domainName: Optional[str] = None
    dnsRecordCreationState: Optional[       LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef     ] = None

class LoadBalancerTlsCertificateRenewalSummaryTypeDef(BaseModel):
    renewalStatus: Optional[LoadBalancerTlsCertificateRenewalStatusType] = None
    domainValidationOptions: Optional[       List[LoadBalancerTlsCertificateDomainValidationOptionTypeDef]     ] = None

class LoadBalancerTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    dnsName: Optional[str] = None
    state: Optional[LoadBalancerStateType] = None
    protocol: Optional[LoadBalancerProtocolType] = None
    publicPorts: Optional[List[int]] = None
    healthCheckPath: Optional[str] = None
    instancePort: Optional[int] = None
    instanceHealthSummary: Optional[List[InstanceHealthSummaryTypeDef]] = None
    tlsCertificateSummaries: Optional[List[LoadBalancerTlsCertificateSummaryTypeDef]] = None
    configurationOptions: Optional[Dict[LoadBalancerAttributeNameType, str]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    httpsRedirectionEnabled: Optional[bool] = None
    tlsPolicyName: Optional[str] = None

class RegisteredDomainDelegationInfoTypeDef(BaseModel):
    nameServersUpdateState: Optional[NameServersUpdateStateTypeDef] = None
    r53HostedZoneDeletionState: Optional[R53HostedZoneDeletionStateTypeDef] = None

class RelationalDatabaseTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    relationalDatabaseBlueprintId: Optional[str] = None
    relationalDatabaseBundleId: Optional[str] = None
    masterDatabaseName: Optional[str] = None
    hardware: Optional[RelationalDatabaseHardwareTypeDef] = None
    state: Optional[str] = None
    secondaryAvailabilityZone: Optional[str] = None
    backupRetentionEnabled: Optional[bool] = None
    pendingModifiedValues: Optional[PendingModifiedRelationalDatabaseValuesTypeDef] = None
    engine: Optional[str] = None
    engineVersion: Optional[str] = None
    latestRestorableTime: Optional[datetime] = None
    masterUsername: Optional[str] = None
    parameterApplyStatus: Optional[str] = None
    preferredBackupWindow: Optional[str] = None
    preferredMaintenanceWindow: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    masterEndpoint: Optional[RelationalDatabaseEndpointTypeDef] = None
    pendingMaintenanceActions: Optional[List[PendingMaintenanceActionTypeDef]] = None
    caCertificateIdentifier: Optional[str] = None

class GetBucketAccessKeysResultTypeDef(BaseModel):
    accessKeys: List[AccessKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDiskFromSnapshotRequestRequestTypeDef(BaseModel):
    diskName: str
    availabilityZone: str
    sizeInGb: int
    diskSnapshotName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    addOns: Optional[Sequence[AddOnRequestTypeDef]] = None
    sourceDiskName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None

class CreateDiskRequestRequestTypeDef(BaseModel):
    diskName: str
    availabilityZone: str
    sizeInGb: int
    tags: Optional[Sequence[TagTypeDef]] = None
    addOns: Optional[Sequence[AddOnRequestTypeDef]] = None

class CreateInstancesFromSnapshotRequestRequestTypeDef(BaseModel):
    instanceNames: Sequence[str]
    availabilityZone: str
    bundleId: str
    attachedDiskMapping: Optional[Mapping[str, Sequence[DiskMapTypeDef]]] = None
    instanceSnapshotName: Optional[str] = None
    userData: Optional[str] = None
    keyPairName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    addOns: Optional[Sequence[AddOnRequestTypeDef]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    sourceInstanceName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None

class CreateInstancesRequestRequestTypeDef(BaseModel):
    instanceNames: Sequence[str]
    availabilityZone: str
    blueprintId: str
    bundleId: str
    customImageName: Optional[str] = None
    userData: Optional[str] = None
    keyPairName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    addOns: Optional[Sequence[AddOnRequestTypeDef]] = None
    ipAddressType: Optional[IpAddressTypeType] = None

class EnableAddOnRequestRequestTypeDef(BaseModel):
    resourceName: str
    addOnRequest: AddOnRequestTypeDef

class GetAlarmsResultTypeDef(BaseModel):
    alarms: List[AlarmTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactMethodsResultTypeDef(BaseModel):
    contactMethods: List[ContactMethodTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateStaticIpResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AttachCertificateToDistributionResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttachDiskResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AttachInstancesToLoadBalancerResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AttachLoadBalancerTlsCertificateResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AttachStaticIpResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CloseInstancePublicPortsResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopySnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBucketAccessKeyResultTypeDef(BaseModel):
    accessKey: AccessKeyTypeDef
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudFormationStackResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactMethodResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDiskFromSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDiskResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDiskSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainEntryResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstancesFromSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstancesResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoadBalancerResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLoadBalancerTlsCertificateResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelationalDatabaseFromSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelationalDatabaseResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRelationalDatabaseSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAlarmResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAutoSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBucketAccessKeyResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBucketResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCertificateResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteContactMethodResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDiskResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDiskSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDistributionResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainEntryResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInstanceResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInstanceSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeyPairResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKnownHostKeysResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLoadBalancerResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLoadBalancerTlsCertificateResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRelationalDatabaseResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRelationalDatabaseSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetachCertificateFromDistributionResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DetachDiskResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetachInstancesFromLoadBalancerResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DetachStaticIpResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisableAddOnResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EnableAddOnResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportSnapshotResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOperationResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOperationsForResourceResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    nextPageCount: str
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetOperationsResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportKeyPairResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class OpenInstancePublicPortsResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PeerVpcResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAlarmResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutInstancePublicPortsResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootInstanceResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RebootRelationalDatabaseResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReleaseStaticIpResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetDistributionCacheResultTypeDef(BaseModel):
    status: str
    createTime: datetime
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SendContactMethodVerificationResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetIpAddressTypeResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetResourceAccessForBucketResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetupInstanceHttpsResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartGUISessionResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartInstanceResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartRelationalDatabaseResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopGUISessionResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopInstanceResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopRelationalDatabaseResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TestAlarmResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UnpeerVpcResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBucketBundleResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionBundleResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDomainEntryResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInstanceMetadataOptionsResultTypeDef(BaseModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLoadBalancerAttributeResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRelationalDatabaseParametersResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRelationalDatabaseResultTypeDef(BaseModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SetupHistoryTypeDef(BaseModel):
    operationId: Optional[str] = None
    request: Optional[SetupRequestTypeDef] = None
    resource: Optional[SetupHistoryResourceTypeDef] = None
    executionDetails: Optional[List[SetupExecutionDetailsTypeDef]] = None
    status: Optional[SetupStatusType] = None

class GetStaticIpResultTypeDef(BaseModel):
    staticIp: StaticIpTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStaticIpsResultTypeDef(BaseModel):
    staticIps: List[StaticIpTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAutoSnapshotsResultTypeDef(BaseModel):
    resourceName: str
    resourceType: ResourceTypeType
    autoSnapshots: List[AutoSnapshotDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegionsResultTypeDef(BaseModel):
    regions: List[RegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBucketResultTypeDef(BaseModel):
    bucket: BucketTypeDef
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBucketsResultTypeDef(BaseModel):
    buckets: List[BucketTypeDef]
    nextPageToken: str
    accountLevelBpaSync: AccountLevelBpaSyncTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBucketResultTypeDef(BaseModel):
    bucket: BucketTypeDef
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDiskSnapshotResultTypeDef(BaseModel):
    diskSnapshot: DiskSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDiskSnapshotsResultTypeDef(BaseModel):
    diskSnapshots: List[DiskSnapshotTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDiskResultTypeDef(BaseModel):
    disk: DiskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDisksResultTypeDef(BaseModel):
    disks: List[DiskTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceHardwareTypeDef(BaseModel):
    cpuCount: Optional[int] = None
    disks: Optional[List[DiskTypeDef]] = None
    ramSizeInGb: Optional[float] = None

class InstanceSnapshotTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    state: Optional[InstanceSnapshotStateType] = None
    progress: Optional[str] = None
    fromAttachedDisks: Optional[List[DiskTypeDef]] = None
    fromInstanceName: Optional[str] = None
    fromInstanceArn: Optional[str] = None
    fromBlueprintId: Optional[str] = None
    fromBundleId: Optional[str] = None
    isFromAutoSnapshot: Optional[bool] = None
    sizeInGb: Optional[int] = None

class CreateKeyPairResultTypeDef(BaseModel):
    keyPair: KeyPairTypeDef
    publicKeyBase64: str
    privateKeyBase64: str
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyPairResultTypeDef(BaseModel):
    keyPair: KeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKeyPairsResultTypeDef(BaseModel):
    keyPairs: List[KeyPairTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseSnapshotResultTypeDef(BaseModel):
    relationalDatabaseSnapshot: RelationalDatabaseSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabaseSnapshotsResultTypeDef(BaseModel):
    relationalDatabaseSnapshots: List[RelationalDatabaseSnapshotTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LightsailDistributionTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    alternativeDomainNames: Optional[List[str]] = None
    status: Optional[str] = None
    isEnabled: Optional[bool] = None
    domainName: Optional[str] = None
    bundleId: Optional[str] = None
    certificateName: Optional[str] = None
    origin: Optional[OriginTypeDef] = None
    originPublicDNS: Optional[str] = None
    defaultCacheBehavior: Optional[CacheBehaviorTypeDef] = None
    cacheBehaviorSettings: Optional[CacheSettingsOutputTypeDef] = None
    cacheBehaviors: Optional[List[CacheBehaviorPerPathTypeDef]] = None
    ableToUpdateBundle: Optional[bool] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    viewerMinimumTlsProtocolVersion: Optional[str] = None

class CreateDistributionRequestRequestTypeDef(BaseModel):
    distributionName: str
    origin: InputOriginTypeDef
    defaultCacheBehavior: CacheBehaviorTypeDef
    bundleId: str
    cacheBehaviorSettings: Optional[CacheSettingsTypeDef] = None
    cacheBehaviors: Optional[Sequence[CacheBehaviorPerPathTypeDef]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    certificateName: Optional[str] = None
    viewerMinimumTlsProtocolVersion: Optional[ViewerMinimumTlsProtocolVersionEnumType] = None

class UpdateDistributionRequestRequestTypeDef(BaseModel):
    distributionName: str
    origin: Optional[InputOriginTypeDef] = None
    defaultCacheBehavior: Optional[CacheBehaviorTypeDef] = None
    cacheBehaviorSettings: Optional[CacheSettingsTypeDef] = None
    cacheBehaviors: Optional[Sequence[CacheBehaviorPerPathTypeDef]] = None
    isEnabled: Optional[bool] = None
    viewerMinimumTlsProtocolVersion: Optional[ViewerMinimumTlsProtocolVersionEnumType] = None
    certificateName: Optional[str] = None
    useDefaultCertificate: Optional[bool] = None

class GetCloudFormationStackRecordsResultTypeDef(BaseModel):
    cloudFormationStackRecords: List[CloudFormationStackRecordTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContainerServiceRequestRequestTypeDef(BaseModel):
    serviceName: str
    power: Optional[ContainerServicePowerNameType] = None
    scale: Optional[int] = None
    isDisabled: Optional[bool] = None
    publicDomainNames: Optional[Mapping[str, Sequence[str]]] = None
    privateRegistryAccess: Optional[PrivateRegistryAccessRequestTypeDef] = None

class ContainerServiceDeploymentTypeDef(BaseModel):
    version: Optional[int] = None
    state: Optional[ContainerServiceDeploymentStateType] = None
    containers: Optional[Dict[str, ContainerOutputTypeDef]] = None
    publicEndpoint: Optional[ContainerServiceEndpointTypeDef] = None
    createdAt: Optional[datetime] = None

class ContainerServiceDeploymentRequestTypeDef(BaseModel):
    containers: Optional[Mapping[str, ContainerTypeDef]] = None
    publicEndpoint: Optional[EndpointRequestTypeDef] = None

class CreateContainerServiceDeploymentRequestRequestTypeDef(BaseModel):
    serviceName: str
    containers: Optional[Mapping[str, ContainerUnionTypeDef]] = None
    publicEndpoint: Optional[EndpointRequestTypeDef] = None

class ExportSnapshotRecordSourceInfoTypeDef(BaseModel):
    resourceType: Optional[ExportSnapshotRecordSourceTypeType] = None
    createdAt: Optional[datetime] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    fromResourceName: Optional[str] = None
    fromResourceArn: Optional[str] = None
    instanceSnapshotInfo: Optional[InstanceSnapshotInfoTypeDef] = None
    diskSnapshotInfo: Optional[DiskSnapshotInfoTypeDef] = None

class RenewalSummaryTypeDef(BaseModel):
    domainValidationRecords: Optional[List[DomainValidationRecordTypeDef]] = None
    renewalStatus: Optional[RenewalStatusType] = None
    renewalStatusReason: Optional[str] = None
    updatedAt: Optional[datetime] = None

class CostEstimateTypeDef(BaseModel):
    usageType: Optional[str] = None
    resultsByTime: Optional[List[EstimateByTimeTypeDef]] = None

class GetInstanceAccessDetailsResultTypeDef(BaseModel):
    accessDetails: InstanceAccessDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LoadBalancerTlsCertificateTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    loadBalancerName: Optional[str] = None
    isAttached: Optional[bool] = None
    status: Optional[LoadBalancerTlsCertificateStatusType] = None
    domainName: Optional[str] = None
    domainValidationRecords: Optional[       List[LoadBalancerTlsCertificateDomainValidationRecordTypeDef]     ] = None
    failureReason: Optional[LoadBalancerTlsCertificateFailureReasonType] = None
    issuedAt: Optional[datetime] = None
    issuer: Optional[str] = None
    keyAlgorithm: Optional[str] = None
    notAfter: Optional[datetime] = None
    notBefore: Optional[datetime] = None
    renewalSummary: Optional[LoadBalancerTlsCertificateRenewalSummaryTypeDef] = None
    revocationReason: Optional[LoadBalancerTlsCertificateRevocationReasonType] = None
    revokedAt: Optional[datetime] = None
    serial: Optional[str] = None
    signatureAlgorithm: Optional[str] = None
    subject: Optional[str] = None
    subjectAlternativeNames: Optional[List[str]] = None

class GetLoadBalancerResultTypeDef(BaseModel):
    loadBalancer: LoadBalancerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLoadBalancersResultTypeDef(BaseModel):
    loadBalancers: List[LoadBalancerTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DomainTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    domainEntries: Optional[List[DomainEntryOutputTypeDef]] = None
    registeredDomainDelegationInfo: Optional[RegisteredDomainDelegationInfoTypeDef] = None

class GetRelationalDatabaseResultTypeDef(BaseModel):
    relationalDatabase: RelationalDatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRelationalDatabasesResultTypeDef(BaseModel):
    relationalDatabases: List[RelationalDatabaseTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSetupHistoryResultTypeDef(BaseModel):
    setupHistory: List[SetupHistoryTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    blueprintId: Optional[str] = None
    blueprintName: Optional[str] = None
    bundleId: Optional[str] = None
    addOns: Optional[List[AddOnTypeDef]] = None
    isStaticIp: Optional[bool] = None
    privateIpAddress: Optional[str] = None
    publicIpAddress: Optional[str] = None
    ipv6Addresses: Optional[List[str]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    hardware: Optional[InstanceHardwareTypeDef] = None
    networking: Optional[InstanceNetworkingTypeDef] = None
    state: Optional[InstanceStateTypeDef] = None
    username: Optional[str] = None
    sshKeyName: Optional[str] = None
    metadataOptions: Optional[InstanceMetadataOptionsTypeDef] = None

class GetInstanceSnapshotResultTypeDef(BaseModel):
    instanceSnapshot: InstanceSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceSnapshotsResultTypeDef(BaseModel):
    instanceSnapshots: List[InstanceSnapshotTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDistributionResultTypeDef(BaseModel):
    distribution: LightsailDistributionTypeDef
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionsResultTypeDef(BaseModel):
    distributions: List[LightsailDistributionTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContainerServiceTypeDef(BaseModel):
    containerServiceName: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    power: Optional[ContainerServicePowerNameType] = None
    powerId: Optional[str] = None
    state: Optional[ContainerServiceStateType] = None
    stateDetail: Optional[ContainerServiceStateDetailTypeDef] = None
    scale: Optional[int] = None
    currentDeployment: Optional[ContainerServiceDeploymentTypeDef] = None
    nextDeployment: Optional[ContainerServiceDeploymentTypeDef] = None
    isDisabled: Optional[bool] = None
    principalArn: Optional[str] = None
    privateDomainName: Optional[str] = None
    publicDomainNames: Optional[Dict[str, List[str]]] = None
    url: Optional[str] = None
    privateRegistryAccess: Optional[PrivateRegistryAccessTypeDef] = None

class GetContainerServiceDeploymentsResultTypeDef(BaseModel):
    deployments: List[ContainerServiceDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContainerServiceRequestRequestTypeDef(BaseModel):
    serviceName: str
    power: ContainerServicePowerNameType
    scale: int
    tags: Optional[Sequence[TagTypeDef]] = None
    publicDomainNames: Optional[Mapping[str, Sequence[str]]] = None
    deployment: Optional[ContainerServiceDeploymentRequestTypeDef] = None
    privateRegistryAccess: Optional[PrivateRegistryAccessRequestTypeDef] = None

class ExportSnapshotRecordTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    state: Optional[RecordStateType] = None
    sourceInfo: Optional[ExportSnapshotRecordSourceInfoTypeDef] = None
    destinationInfo: Optional[DestinationInfoTypeDef] = None

class CertificateTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    domainName: Optional[str] = None
    status: Optional[CertificateStatusType] = None
    serialNumber: Optional[str] = None
    subjectAlternativeNames: Optional[List[str]] = None
    domainValidationRecords: Optional[List[DomainValidationRecordTypeDef]] = None
    requestFailureReason: Optional[str] = None
    inUseResourceCount: Optional[int] = None
    keyAlgorithm: Optional[str] = None
    createdAt: Optional[datetime] = None
    issuedAt: Optional[datetime] = None
    issuerCA: Optional[str] = None
    notBefore: Optional[datetime] = None
    notAfter: Optional[datetime] = None
    eligibleToRenew: Optional[str] = None
    renewalSummary: Optional[RenewalSummaryTypeDef] = None
    revokedAt: Optional[datetime] = None
    revocationReason: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None
    supportCode: Optional[str] = None

class ResourceBudgetEstimateTypeDef(BaseModel):
    resourceName: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    costEstimates: Optional[List[CostEstimateTypeDef]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class GetLoadBalancerTlsCertificatesResultTypeDef(BaseModel):
    tlsCertificates: List[LoadBalancerTlsCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainResultTypeDef(BaseModel):
    domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainsResultTypeDef(BaseModel):
    domains: List[DomainTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceResultTypeDef(BaseModel):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstancesResultTypeDef(BaseModel):
    instances: List[InstanceTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContainerServicesListResultTypeDef(BaseModel):
    containerServices: List[ContainerServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContainerServiceDeploymentResultTypeDef(BaseModel):
    containerService: ContainerServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContainerServiceResultTypeDef(BaseModel):
    containerService: ContainerServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContainerServiceResultTypeDef(BaseModel):
    containerService: ContainerServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExportSnapshotRecordsResultTypeDef(BaseModel):
    exportSnapshotRecords: List[ExportSnapshotRecordTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CertificateSummaryTypeDef(BaseModel):
    certificateArn: Optional[str] = None
    certificateName: Optional[str] = None
    domainName: Optional[str] = None
    certificateDetail: Optional[CertificateTypeDef] = None
    tags: Optional[List[TagTypeDef]] = None

class GetCostEstimateResultTypeDef(BaseModel):
    resourcesBudgetEstimate: List[ResourceBudgetEstimateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCertificateResultTypeDef(BaseModel):
    certificate: CertificateSummaryTypeDef
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCertificatesResultTypeDef(BaseModel):
    certificates: List[CertificateSummaryTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


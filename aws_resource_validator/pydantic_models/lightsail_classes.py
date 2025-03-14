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

class AccessKeyLastUsedTypeDef(BaseValidatorModel):
    lastUsedDate: Optional[datetime] = None
    region: Optional[str] = None
    serviceName: Optional[str] = None


class AccessRulesTypeDef(BaseValidatorModel):
    getObject: Optional[AccessTypeType] = None
    allowPublicOverrides: Optional[bool] = None


class AccountLevelBpaSyncTypeDef(BaseValidatorModel):
    status: Optional[AccountLevelBpaSyncStatusType] = None
    lastSyncedAt: Optional[datetime] = None
    message: Optional[BPAStatusMessageType] = None
    bpaImpactsLightsail: Optional[bool] = None


class AutoSnapshotAddOnRequestTypeDef(BaseValidatorModel):
    snapshotTimeOfDay: Optional[str] = None


class StopInstanceOnIdleRequestTypeDef(BaseValidatorModel):
    threshold: Optional[str] = None
    duration: Optional[str] = None


class AddOnTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[str] = None
    snapshotTimeOfDay: Optional[str] = None
    nextSnapshotTimeOfDay: Optional[str] = None
    threshold: Optional[str] = None
    duration: Optional[str] = None


class MonitoredResourceInfoTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None


class ResourceLocationTypeDef(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    regionName: Optional[RegionNameType] = None


class AllocateStaticIpRequestTypeDef(BaseValidatorModel):
    staticIpName: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AttachCertificateToDistributionRequestTypeDef(BaseValidatorModel):
    distributionName: str
    certificateName: str


class AttachDiskRequestTypeDef(BaseValidatorModel):
    diskName: str
    instanceName: str
    diskPath: str
    autoMounting: Optional[bool] = None


class AttachInstancesToLoadBalancerRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str
    instanceNames: Sequence[str]


class AttachLoadBalancerTlsCertificateRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str


class AttachStaticIpRequestTypeDef(BaseValidatorModel):
    staticIpName: str
    instanceName: str


class AttachedDiskTypeDef(BaseValidatorModel):
    path: Optional[str] = None
    sizeInGb: Optional[int] = None


class AvailabilityZoneTypeDef(BaseValidatorModel):
    zoneName: Optional[str] = None
    state: Optional[str] = None


class BucketAccessLogConfigTypeDef(BaseValidatorModel):
    enabled: bool
    destination: Optional[str] = None
    prefix: Optional[str] = None


class BucketBundleTypeDef(BaseValidatorModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    storagePerMonthInGb: Optional[int] = None
    transferPerMonthInGb: Optional[int] = None
    isActive: Optional[bool] = None


class BucketStateTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class ResourceReceivingAccessTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    resourceType: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class BundleTypeDef(BaseValidatorModel):
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


class CacheBehaviorPerPathTypeDef(BaseValidatorModel):
    path: Optional[str] = None
    behavior: Optional[BehaviorEnumType] = None


class CacheBehaviorTypeDef(BaseValidatorModel):
    behavior: Optional[BehaviorEnumType] = None


class CookieObjectOutputTypeDef(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    cookiesAllowList: Optional[List[str]] = None


class HeaderObjectOutputTypeDef(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    headersAllowList: Optional[List[HeaderEnumType]] = None


class QueryStringObjectOutputTypeDef(BaseValidatorModel):
    option: Optional[bool] = None
    queryStringsAllowList: Optional[List[str]] = None


class CookieObjectTypeDef(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    cookiesAllowList: Optional[Sequence[str]] = None


class HeaderObjectTypeDef(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    headersAllowList: Optional[Sequence[HeaderEnumType]] = None


class QueryStringObjectTypeDef(BaseValidatorModel):
    option: Optional[bool] = None
    queryStringsAllowList: Optional[Sequence[str]] = None


class PortInfoTypeDef(BaseValidatorModel):
    fromPort: Optional[int] = None
    toPort: Optional[int] = None
    protocol: Optional[NetworkProtocolType] = None
    cidrs: Optional[Sequence[str]] = None
    ipv6Cidrs: Optional[Sequence[str]] = None
    cidrListAliases: Optional[Sequence[str]] = None


class CloudFormationStackRecordSourceInfoTypeDef(BaseValidatorModel):
    resourceType: Optional[Literal["ExportSnapshotRecord"]] = None
    name: Optional[str] = None
    arn: Optional[str] = None


class ContainerImageTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    digest: Optional[str] = None
    createdAt: Optional[datetime] = None


class ContainerOutputTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    command: Optional[List[str]] = None
    environment: Optional[Dict[str, str]] = None
    ports: Optional[Dict[str, ContainerServiceProtocolType]] = None


class ContainerServiceECRImagePullerRoleRequestTypeDef(BaseValidatorModel):
    isActive: Optional[bool] = None


class ContainerServiceECRImagePullerRoleTypeDef(BaseValidatorModel):
    isActive: Optional[bool] = None
    principalArn: Optional[str] = None


class ContainerServiceHealthCheckConfigTypeDef(BaseValidatorModel):
    healthyThreshold: Optional[int] = None
    unhealthyThreshold: Optional[int] = None
    timeoutSeconds: Optional[int] = None
    intervalSeconds: Optional[int] = None
    path: Optional[str] = None
    successCodes: Optional[str] = None


class ContainerServiceLogEventTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    message: Optional[str] = None


class ContainerServicePowerTypeDef(BaseValidatorModel):
    powerId: Optional[str] = None
    price: Optional[float] = None
    cpuCount: Optional[float] = None
    ramSizeInGb: Optional[float] = None
    name: Optional[str] = None
    isActive: Optional[bool] = None


class ContainerServiceRegistryLoginTypeDef(BaseValidatorModel):
    username: Optional[str] = None
    password: Optional[str] = None
    expiresAt: Optional[datetime] = None
    registry: Optional[str] = None


class ContainerServiceStateDetailTypeDef(BaseValidatorModel):
    code: Optional[ContainerServiceStateDetailCodeType] = None
    message: Optional[str] = None


class ContainerTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    command: Optional[Sequence[str]] = None
    environment: Optional[Mapping[str, str]] = None
    ports: Optional[Mapping[str, ContainerServiceProtocolType]] = None


class CopySnapshotRequestTypeDef(BaseValidatorModel):
    targetSnapshotName: str
    sourceRegion: RegionNameType
    sourceSnapshotName: Optional[str] = None
    sourceResourceName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None


class CreateBucketAccessKeyRequestTypeDef(BaseValidatorModel):
    bucketName: str


class InstanceEntryTypeDef(BaseValidatorModel):
    sourceName: str
    instanceType: str
    portInfoSource: PortInfoSourceTypeType
    availabilityZone: str
    userData: Optional[str] = None


class CreateContactMethodRequestTypeDef(BaseValidatorModel):
    protocol: ContactProtocolType
    contactEndpoint: str


class InputOriginTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    regionName: Optional[RegionNameType] = None
    protocolPolicy: Optional[OriginProtocolPolicyEnumType] = None
    responseTimeout: Optional[int] = None


class CreateGUISessionAccessDetailsRequestTypeDef(BaseValidatorModel):
    resourceName: str


class SessionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None
    isPrimary: Optional[bool] = None


class DiskMapTypeDef(BaseValidatorModel):
    originalDiskPath: Optional[str] = None
    newDiskName: Optional[str] = None


class DeleteAlarmRequestTypeDef(BaseValidatorModel):
    alarmName: str


class DeleteAutoSnapshotRequestTypeDef(BaseValidatorModel):
    resourceName: str
    date: str


class DeleteBucketAccessKeyRequestTypeDef(BaseValidatorModel):
    bucketName: str
    accessKeyId: str


class DeleteBucketRequestTypeDef(BaseValidatorModel):
    bucketName: str
    forceDelete: Optional[bool] = None


class DeleteCertificateRequestTypeDef(BaseValidatorModel):
    certificateName: str


class DeleteContactMethodRequestTypeDef(BaseValidatorModel):
    protocol: ContactProtocolType


class DeleteContainerImageRequestTypeDef(BaseValidatorModel):
    serviceName: str
    image: str


class DeleteContainerServiceRequestTypeDef(BaseValidatorModel):
    serviceName: str


class DeleteDiskRequestTypeDef(BaseValidatorModel):
    diskName: str
    forceDeleteAddOns: Optional[bool] = None


class DeleteDiskSnapshotRequestTypeDef(BaseValidatorModel):
    diskSnapshotName: str


class DeleteDistributionRequestTypeDef(BaseValidatorModel):
    distributionName: Optional[str] = None


class DeleteDomainRequestTypeDef(BaseValidatorModel):
    domainName: str


class DeleteInstanceRequestTypeDef(BaseValidatorModel):
    instanceName: str
    forceDeleteAddOns: Optional[bool] = None


class DeleteInstanceSnapshotRequestTypeDef(BaseValidatorModel):
    instanceSnapshotName: str


class DeleteKeyPairRequestTypeDef(BaseValidatorModel):
    keyPairName: str
    expectedFingerprint: Optional[str] = None


class DeleteKnownHostKeysRequestTypeDef(BaseValidatorModel):
    instanceName: str


class DeleteLoadBalancerRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str


class DeleteLoadBalancerTlsCertificateRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str
    force: Optional[bool] = None


class DeleteRelationalDatabaseRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    skipFinalSnapshot: Optional[bool] = None
    finalRelationalDatabaseSnapshotName: Optional[str] = None


class DeleteRelationalDatabaseSnapshotRequestTypeDef(BaseValidatorModel):
    relationalDatabaseSnapshotName: str


class DetachCertificateFromDistributionRequestTypeDef(BaseValidatorModel):
    distributionName: str


class DetachDiskRequestTypeDef(BaseValidatorModel):
    diskName: str


class DetachInstancesFromLoadBalancerRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str
    instanceNames: Sequence[str]


class DetachStaticIpRequestTypeDef(BaseValidatorModel):
    staticIpName: str


class DisableAddOnRequestTypeDef(BaseValidatorModel):
    addOnType: AddOnTypeType
    resourceName: str


class DiskInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    path: Optional[str] = None
    sizeInGb: Optional[int] = None
    isSystemDisk: Optional[bool] = None


class DiskSnapshotInfoTypeDef(BaseValidatorModel):
    sizeInGb: Optional[int] = None


class DistributionBundleTypeDef(BaseValidatorModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    transferPerMonthInGb: Optional[int] = None
    isActive: Optional[bool] = None


class DnsRecordCreationStateTypeDef(BaseValidatorModel):
    code: Optional[DnsRecordCreationStateCodeType] = None
    message: Optional[str] = None


class TimePeriodTypeDef(BaseValidatorModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class ExportSnapshotRequestTypeDef(BaseValidatorModel):
    sourceSnapshotName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetActiveNamesRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetAlarmsRequestTypeDef(BaseValidatorModel):
    alarmName: Optional[str] = None
    pageToken: Optional[str] = None
    monitoredResourceName: Optional[str] = None


class GetAutoSnapshotsRequestTypeDef(BaseValidatorModel):
    resourceName: str


class GetBlueprintsRequestTypeDef(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    pageToken: Optional[str] = None
    appCategory: Optional[Literal["LfR"]] = None


class GetBucketAccessKeysRequestTypeDef(BaseValidatorModel):
    bucketName: str


class GetBucketBundlesRequestTypeDef(BaseValidatorModel):
    includeInactive: Optional[bool] = None


class GetBucketsRequestTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    pageToken: Optional[str] = None
    includeConnectedResources: Optional[bool] = None


class GetBundlesRequestTypeDef(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    pageToken: Optional[str] = None
    appCategory: Optional[Literal["LfR"]] = None


class GetCertificatesRequestTypeDef(BaseValidatorModel):
    certificateStatuses: Optional[Sequence[CertificateStatusType]] = None
    includeCertificateDetails: Optional[bool] = None
    certificateName: Optional[str] = None
    pageToken: Optional[str] = None


class GetCloudFormationStackRecordsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetContactMethodsRequestTypeDef(BaseValidatorModel):
    protocols: Optional[Sequence[ContactProtocolType]] = None


class GetContainerImagesRequestTypeDef(BaseValidatorModel):
    serviceName: str


class GetContainerServiceDeploymentsRequestTypeDef(BaseValidatorModel):
    serviceName: str


class GetContainerServicesRequestTypeDef(BaseValidatorModel):
    serviceName: Optional[str] = None


class GetDiskRequestTypeDef(BaseValidatorModel):
    diskName: str


class GetDiskSnapshotRequestTypeDef(BaseValidatorModel):
    diskSnapshotName: str


class GetDiskSnapshotsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetDisksRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetDistributionLatestCacheResetRequestTypeDef(BaseValidatorModel):
    distributionName: Optional[str] = None


class GetDistributionsRequestTypeDef(BaseValidatorModel):
    distributionName: Optional[str] = None
    pageToken: Optional[str] = None


class GetDomainRequestTypeDef(BaseValidatorModel):
    domainName: str


class GetDomainsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetExportSnapshotRecordsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetInstanceAccessDetailsRequestTypeDef(BaseValidatorModel):
    instanceName: str
    protocol: Optional[InstanceAccessProtocolType] = None


class GetInstancePortStatesRequestTypeDef(BaseValidatorModel):
    instanceName: str


class InstancePortStateTypeDef(BaseValidatorModel):
    fromPort: Optional[int] = None
    toPort: Optional[int] = None
    protocol: Optional[NetworkProtocolType] = None
    state: Optional[PortStateType] = None
    cidrs: Optional[List[str]] = None
    ipv6Cidrs: Optional[List[str]] = None
    cidrListAliases: Optional[List[str]] = None


class GetInstanceRequestTypeDef(BaseValidatorModel):
    instanceName: str


class GetInstanceSnapshotRequestTypeDef(BaseValidatorModel):
    instanceSnapshotName: str


class GetInstanceSnapshotsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetInstanceStateRequestTypeDef(BaseValidatorModel):
    instanceName: str


class InstanceStateTypeDef(BaseValidatorModel):
    code: Optional[int] = None
    name: Optional[str] = None


class GetInstancesRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetKeyPairRequestTypeDef(BaseValidatorModel):
    keyPairName: str


class GetKeyPairsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None
    includeDefaultKeyPair: Optional[bool] = None


class GetLoadBalancerRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str


class GetLoadBalancerTlsCertificatesRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str


class GetLoadBalancerTlsPoliciesRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class LoadBalancerTlsPolicyTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    isDefault: Optional[bool] = None
    description: Optional[str] = None
    protocols: Optional[List[str]] = None
    ciphers: Optional[List[str]] = None


class GetLoadBalancersRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetOperationRequestTypeDef(BaseValidatorModel):
    operationId: str


class GetOperationsForResourceRequestTypeDef(BaseValidatorModel):
    resourceName: str
    pageToken: Optional[str] = None


class GetOperationsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetRegionsRequestTypeDef(BaseValidatorModel):
    includeAvailabilityZones: Optional[bool] = None
    includeRelationalDatabaseAvailabilityZones: Optional[bool] = None


class GetRelationalDatabaseBlueprintsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class RelationalDatabaseBlueprintTypeDef(BaseValidatorModel):
    blueprintId: Optional[str] = None
    engine: Optional[Literal["mysql"]] = None
    engineVersion: Optional[str] = None
    engineDescription: Optional[str] = None
    engineVersionDescription: Optional[str] = None
    isEngineDefault: Optional[bool] = None


class GetRelationalDatabaseBundlesRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None
    includeInactive: Optional[bool] = None


class RelationalDatabaseBundleTypeDef(BaseValidatorModel):
    bundleId: Optional[str] = None
    name: Optional[str] = None
    price: Optional[float] = None
    ramSizeInGb: Optional[float] = None
    diskSizeInGb: Optional[int] = None
    transferPerMonthInGb: Optional[int] = None
    cpuCount: Optional[int] = None
    isEncrypted: Optional[bool] = None
    isActive: Optional[bool] = None


class GetRelationalDatabaseEventsRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    durationInMinutes: Optional[int] = None
    pageToken: Optional[str] = None


class RelationalDatabaseEventTypeDef(BaseValidatorModel):
    resource: Optional[str] = None
    createdAt: Optional[datetime] = None
    message: Optional[str] = None
    eventCategories: Optional[List[str]] = None


class LogEventTypeDef(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    message: Optional[str] = None


class GetRelationalDatabaseLogStreamsRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str


class GetRelationalDatabaseMasterUserPasswordRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    passwordVersion: Optional[RelationalDatabasePasswordVersionType] = None


class GetRelationalDatabaseParametersRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    pageToken: Optional[str] = None


class RelationalDatabaseParameterTypeDef(BaseValidatorModel):
    allowedValues: Optional[str] = None
    applyMethod: Optional[str] = None
    applyType: Optional[str] = None
    dataType: Optional[str] = None
    description: Optional[str] = None
    isModifiable: Optional[bool] = None
    parameterName: Optional[str] = None
    parameterValue: Optional[str] = None


class GetRelationalDatabaseRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str


class GetRelationalDatabaseSnapshotRequestTypeDef(BaseValidatorModel):
    relationalDatabaseSnapshotName: str


class GetRelationalDatabaseSnapshotsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetRelationalDatabasesRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class GetSetupHistoryRequestTypeDef(BaseValidatorModel):
    resourceName: str
    pageToken: Optional[str] = None


class GetStaticIpRequestTypeDef(BaseValidatorModel):
    staticIpName: str


class GetStaticIpsRequestTypeDef(BaseValidatorModel):
    pageToken: Optional[str] = None


class HostKeyAttributesTypeDef(BaseValidatorModel):
    algorithm: Optional[str] = None
    publicKey: Optional[str] = None
    witnessedAt: Optional[datetime] = None
    fingerprintSHA1: Optional[str] = None
    fingerprintSHA256: Optional[str] = None
    notValidBefore: Optional[datetime] = None
    notValidAfter: Optional[datetime] = None


class ImportKeyPairRequestTypeDef(BaseValidatorModel):
    keyPairName: str
    publicKeyBase64: str


class PasswordDataTypeDef(BaseValidatorModel):
    ciphertext: Optional[str] = None
    keyPairName: Optional[str] = None


class InstanceHealthSummaryTypeDef(BaseValidatorModel):
    instanceName: Optional[str] = None
    instanceHealth: Optional[InstanceHealthStateType] = None
    instanceHealthReason: Optional[InstanceHealthReasonType] = None


class InstanceMetadataOptionsTypeDef(BaseValidatorModel):
    state: Optional[InstanceMetadataStateType] = None
    httpTokens: Optional[HttpTokensType] = None
    httpEndpoint: Optional[HttpEndpointType] = None
    httpPutResponseHopLimit: Optional[int] = None
    httpProtocolIpv6: Optional[HttpProtocolIpv6Type] = None


class InstancePortInfoTypeDef(BaseValidatorModel):
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


class MonthlyTransferTypeDef(BaseValidatorModel):
    gbPerMonthAllocated: Optional[int] = None


class OriginTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    regionName: Optional[RegionNameType] = None
    protocolPolicy: Optional[OriginProtocolPolicyEnumType] = None
    responseTimeout: Optional[int] = None


class LoadBalancerTlsCertificateDnsRecordCreationStateTypeDef(BaseValidatorModel):
    code: Optional[LoadBalancerTlsCertificateDnsRecordCreationStateCodeType] = None
    message: Optional[str] = None


class LoadBalancerTlsCertificateDomainValidationOptionTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None
    validationStatus: Optional[LoadBalancerTlsCertificateDomainStatusType] = None


class LoadBalancerTlsCertificateSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    isAttached: Optional[bool] = None


class NameServersUpdateStateTypeDef(BaseValidatorModel):
    code: Optional[NameServersUpdateStateCodeType] = None
    message: Optional[str] = None


class PendingMaintenanceActionTypeDef(BaseValidatorModel):
    action: Optional[str] = None
    description: Optional[str] = None
    currentApplyDate: Optional[datetime] = None


class PendingModifiedRelationalDatabaseValuesTypeDef(BaseValidatorModel):
    masterUserPassword: Optional[str] = None
    engineVersion: Optional[str] = None
    backupRetentionEnabled: Optional[bool] = None


class PutAlarmRequestTypeDef(BaseValidatorModel):
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


class R53HostedZoneDeletionStateTypeDef(BaseValidatorModel):
    code: Optional[R53HostedZoneDeletionStateCodeType] = None
    message: Optional[str] = None


class RebootInstanceRequestTypeDef(BaseValidatorModel):
    instanceName: str


class RebootRelationalDatabaseRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str


class RegisterContainerImageRequestTypeDef(BaseValidatorModel):
    serviceName: str
    label: str
    digest: str


class RelationalDatabaseEndpointTypeDef(BaseValidatorModel):
    port: Optional[int] = None
    address: Optional[str] = None


class RelationalDatabaseHardwareTypeDef(BaseValidatorModel):
    cpuCount: Optional[int] = None
    diskSizeInGb: Optional[int] = None
    ramSizeInGb: Optional[float] = None


class ReleaseStaticIpRequestTypeDef(BaseValidatorModel):
    staticIpName: str


class ResetDistributionCacheRequestTypeDef(BaseValidatorModel):
    distributionName: Optional[str] = None


class SendContactMethodVerificationRequestTypeDef(BaseValidatorModel):
    protocol: Literal["Email"]


class SetIpAddressTypeRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceName: str
    ipAddressType: IpAddressTypeType
    acceptBundleUpdate: Optional[bool] = None


class SetResourceAccessForBucketRequestTypeDef(BaseValidatorModel):
    resourceName: str
    bucketName: str
    access: ResourceBucketAccessType


class SetupExecutionDetailsTypeDef(BaseValidatorModel):
    command: Optional[str] = None
    dateTime: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[SetupStatusType] = None
    standardError: Optional[str] = None
    standardOutput: Optional[str] = None
    version: Optional[str] = None


class SetupRequestTypeDef(BaseValidatorModel):
    instanceName: Optional[str] = None
    domainNames: Optional[List[str]] = None
    certificateProvider: Optional[Literal["LetsEncrypt"]] = None


class SetupInstanceHttpsRequestTypeDef(BaseValidatorModel):
    instanceName: str
    emailAddress: str
    domainNames: Sequence[str]
    certificateProvider: Literal["LetsEncrypt"]


class StartGUISessionRequestTypeDef(BaseValidatorModel):
    resourceName: str


class StartInstanceRequestTypeDef(BaseValidatorModel):
    instanceName: str


class StartRelationalDatabaseRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str


class StopGUISessionRequestTypeDef(BaseValidatorModel):
    resourceName: str


class StopInstanceRequestTypeDef(BaseValidatorModel):
    instanceName: str
    force: Optional[bool] = None


class StopRelationalDatabaseRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    relationalDatabaseSnapshotName: Optional[str] = None


class TestAlarmRequestTypeDef(BaseValidatorModel):
    alarmName: str
    state: AlarmStateType


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceName: str
    tagKeys: Sequence[str]
    resourceArn: Optional[str] = None


class UpdateBucketBundleRequestTypeDef(BaseValidatorModel):
    bucketName: str
    bundleId: str


class UpdateDistributionBundleRequestTypeDef(BaseValidatorModel):
    distributionName: Optional[str] = None
    bundleId: Optional[str] = None


class UpdateInstanceMetadataOptionsRequestTypeDef(BaseValidatorModel):
    instanceName: str
    httpTokens: Optional[HttpTokensType] = None
    httpEndpoint: Optional[HttpEndpointType] = None
    httpPutResponseHopLimit: Optional[int] = None
    httpProtocolIpv6: Optional[HttpProtocolIpv6Type] = None


class UpdateLoadBalancerAttributeRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str
    attributeName: LoadBalancerAttributeNameType
    attributeValue: str


class UpdateRelationalDatabaseRequestTypeDef(BaseValidatorModel):
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


class AccessKeyTypeDef(BaseValidatorModel):
    accessKeyId: Optional[str] = None
    secretAccessKey: Optional[str] = None
    status: Optional[StatusTypeType] = None
    createdAt: Optional[datetime] = None
    lastUsed: Optional[AccessKeyLastUsedTypeDef] = None


class AddOnRequestTypeDef(BaseValidatorModel):
    addOnType: AddOnTypeType
    autoSnapshotAddOnRequest: Optional[AutoSnapshotAddOnRequestTypeDef] = None
    stopInstanceOnIdleRequest: Optional[StopInstanceOnIdleRequestTypeDef] = None


class AlarmTypeDef(BaseValidatorModel):
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


class ContactMethodTypeDef(BaseValidatorModel):
    contactEndpoint: Optional[str] = None
    status: Optional[ContactMethodStatusType] = None
    protocol: Optional[ContactProtocolType] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    supportCode: Optional[str] = None


class SetupHistoryResourceTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None


class StaticIpTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    ipAddress: Optional[str] = None
    attachedTo: Optional[str] = None
    isAttached: Optional[bool] = None


class DownloadDefaultKeyPairResultTypeDef(BaseValidatorModel):
    publicKeyBase64: str
    privateKeyBase64: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetActiveNamesResultTypeDef(BaseValidatorModel):
    activeNames: List[str]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetContainerAPIMetadataResultTypeDef(BaseValidatorModel):
    metadata: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDistributionLatestCacheResetResultTypeDef(BaseValidatorModel):
    status: str
    createTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseLogStreamsResultTypeDef(BaseValidatorModel):
    logStreams: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseMasterUserPasswordResultTypeDef(BaseValidatorModel):
    masterUserPassword: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class IsVpcPeeredResultTypeDef(BaseValidatorModel):
    isPeered: bool
    ResponseMetadata: ResponseMetadataTypeDef


class AutoSnapshotDetailsTypeDef(BaseValidatorModel):
    date: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[AutoSnapshotStatusType] = None
    fromAttachedDisks: Optional[List[AttachedDiskTypeDef]] = None


class RegionTypeDef(BaseValidatorModel):
    continentCode: Optional[str] = None
    description: Optional[str] = None
    displayName: Optional[str] = None
    name: Optional[RegionNameType] = None
    availabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    relationalDatabaseAvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None


class BlueprintTypeDef(BaseValidatorModel):
    pass


class GetBlueprintsResultTypeDef(BaseValidatorModel):
    blueprints: List[BlueprintTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBucketRequestTypeDef(BaseValidatorModel):
    bucketName: str
    accessRules: Optional[AccessRulesTypeDef] = None
    versioning: Optional[str] = None
    readonlyAccessAccounts: Optional[Sequence[str]] = None
    accessLogConfig: Optional[BucketAccessLogConfigTypeDef] = None


class GetBucketBundlesResultTypeDef(BaseValidatorModel):
    bundles: List[BucketBundleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BucketTypeDef(BaseValidatorModel):
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


class CreateBucketRequestTypeDef(BaseValidatorModel):
    bucketName: str
    bundleId: str
    tags: Optional[Sequence[TagTypeDef]] = None
    enableObjectVersioning: Optional[bool] = None


class CreateCertificateRequestTypeDef(BaseValidatorModel):
    certificateName: str
    domainName: str
    subjectAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateDiskSnapshotRequestTypeDef(BaseValidatorModel):
    diskSnapshotName: str
    diskName: Optional[str] = None
    instanceName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateDomainRequestTypeDef(BaseValidatorModel):
    domainName: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateInstanceSnapshotRequestTypeDef(BaseValidatorModel):
    instanceSnapshotName: str
    instanceName: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateKeyPairRequestTypeDef(BaseValidatorModel):
    keyPairName: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateLoadBalancerRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str
    instancePort: int
    healthCheckPath: Optional[str] = None
    certificateName: Optional[str] = None
    certificateDomainName: Optional[str] = None
    certificateAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tlsPolicyName: Optional[str] = None


class CreateLoadBalancerTlsCertificateRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str
    certificateDomainName: str
    certificateAlternativeNames: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateRelationalDatabaseRequestTypeDef(BaseValidatorModel):
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


class CreateRelationalDatabaseSnapshotRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    relationalDatabaseSnapshotName: str
    tags: Optional[Sequence[TagTypeDef]] = None


class DiskSnapshotTypeDef(BaseValidatorModel):
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


class DiskTypeDef(BaseValidatorModel):
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


class KeyPairTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    fingerprint: Optional[str] = None


class RelationalDatabaseSnapshotTypeDef(BaseValidatorModel):
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


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceName: str
    tags: Sequence[TagTypeDef]
    resourceArn: Optional[str] = None


class GetBundlesResultTypeDef(BaseValidatorModel):
    bundles: List[BundleTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CacheSettingsOutputTypeDef(BaseValidatorModel):
    defaultTTL: Optional[int] = None
    minimumTTL: Optional[int] = None
    maximumTTL: Optional[int] = None
    allowedHTTPMethods: Optional[str] = None
    cachedHTTPMethods: Optional[str] = None
    forwardedCookies: Optional[CookieObjectOutputTypeDef] = None
    forwardedHeaders: Optional[HeaderObjectOutputTypeDef] = None
    forwardedQueryStrings: Optional[QueryStringObjectOutputTypeDef] = None


class CacheSettingsTypeDef(BaseValidatorModel):
    defaultTTL: Optional[int] = None
    minimumTTL: Optional[int] = None
    maximumTTL: Optional[int] = None
    allowedHTTPMethods: Optional[str] = None
    cachedHTTPMethods: Optional[str] = None
    forwardedCookies: Optional[CookieObjectTypeDef] = None
    forwardedHeaders: Optional[HeaderObjectTypeDef] = None
    forwardedQueryStrings: Optional[QueryStringObjectTypeDef] = None


class CloseInstancePublicPortsRequestTypeDef(BaseValidatorModel):
    portInfo: PortInfoTypeDef
    instanceName: str


class OpenInstancePublicPortsRequestTypeDef(BaseValidatorModel):
    portInfo: PortInfoTypeDef
    instanceName: str


class PutInstancePublicPortsRequestTypeDef(BaseValidatorModel):
    portInfos: Sequence[PortInfoTypeDef]
    instanceName: str


class DestinationInfoTypeDef(BaseValidatorModel):
    pass


class CloudFormationStackRecordTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    state: Optional[RecordStateType] = None
    sourceInfo: Optional[List[CloudFormationStackRecordSourceInfoTypeDef]] = None
    destinationInfo: Optional[DestinationInfoTypeDef] = None


class GetContainerImagesResultTypeDef(BaseValidatorModel):
    containerImages: List[ContainerImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterContainerImageResultTypeDef(BaseValidatorModel):
    containerImage: ContainerImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PrivateRegistryAccessRequestTypeDef(BaseValidatorModel):
    ecrImagePullerRole: Optional[ContainerServiceECRImagePullerRoleRequestTypeDef] = None


class PrivateRegistryAccessTypeDef(BaseValidatorModel):
    ecrImagePullerRole: Optional[ContainerServiceECRImagePullerRoleTypeDef] = None


class ContainerServiceEndpointTypeDef(BaseValidatorModel):
    containerName: Optional[str] = None
    containerPort: Optional[int] = None
    healthCheck: Optional[ContainerServiceHealthCheckConfigTypeDef] = None


class EndpointRequestTypeDef(BaseValidatorModel):
    containerName: str
    containerPort: int
    healthCheck: Optional[ContainerServiceHealthCheckConfigTypeDef] = None


class GetContainerLogResultTypeDef(BaseValidatorModel):
    logEvents: List[ContainerServiceLogEventTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetContainerServicePowersResultTypeDef(BaseValidatorModel):
    powers: List[ContainerServicePowerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContainerServiceRegistryLoginResultTypeDef(BaseValidatorModel):
    registryLogin: ContainerServiceRegistryLoginTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCloudFormationStackRequestTypeDef(BaseValidatorModel):
    instances: Sequence[InstanceEntryTypeDef]


class CreateGUISessionAccessDetailsResultTypeDef(BaseValidatorModel):
    resourceName: str
    status: StatusType
    percentageComplete: int
    failureReason: str
    sessions: List[SessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateRelationalDatabaseFromSnapshotRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    availabilityZone: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    relationalDatabaseSnapshotName: Optional[str] = None
    relationalDatabaseBundleId: Optional[str] = None
    sourceRelationalDatabaseName: Optional[str] = None
    restoreTime: Optional[TimestampTypeDef] = None
    useLatestRestorableTime: Optional[bool] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class GetBucketMetricDataRequestTypeDef(BaseValidatorModel):
    bucketName: str
    metricName: BucketMetricNameType
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    period: int
    statistics: Sequence[MetricStatisticType]
    unit: MetricUnitType


class GetContainerLogRequestTypeDef(BaseValidatorModel):
    serviceName: str
    containerName: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    filterPattern: Optional[str] = None
    pageToken: Optional[str] = None


class GetContainerServiceMetricDataRequestTypeDef(BaseValidatorModel):
    serviceName: str
    metricName: ContainerServiceMetricNameType
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    period: int
    statistics: Sequence[MetricStatisticType]


class GetCostEstimateRequestTypeDef(BaseValidatorModel):
    resourceName: str
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef


class GetDistributionMetricDataRequestTypeDef(BaseValidatorModel):
    distributionName: str
    metricName: DistributionMetricNameType
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    period: int
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]


class GetInstanceMetricDataRequestTypeDef(BaseValidatorModel):
    instanceName: str
    metricName: InstanceMetricNameType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]


class GetLoadBalancerMetricDataRequestTypeDef(BaseValidatorModel):
    loadBalancerName: str
    metricName: LoadBalancerMetricNameType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]


class GetRelationalDatabaseLogEventsRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    logStreamName: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    startFromHead: Optional[bool] = None
    pageToken: Optional[str] = None


class GetRelationalDatabaseMetricDataRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    metricName: RelationalDatabaseMetricNameType
    period: int
    startTime: TimestampTypeDef
    endTime: TimestampTypeDef
    unit: MetricUnitType
    statistics: Sequence[MetricStatisticType]


class InstanceSnapshotInfoTypeDef(BaseValidatorModel):
    fromBundleId: Optional[str] = None
    fromBlueprintId: Optional[str] = None
    fromDiskInfo: Optional[List[DiskInfoTypeDef]] = None


class GetDistributionBundlesResultTypeDef(BaseValidatorModel):
    bundles: List[DistributionBundleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ResourceRecordTypeDef(BaseValidatorModel):
    pass


class DomainValidationRecordTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None
    resourceRecord: Optional[ResourceRecordTypeDef] = None
    dnsRecordCreationState: Optional[DnsRecordCreationStateTypeDef] = None
    validationStatus: Optional[CertificateDomainValidationStatusType] = None


class EstimateByTimeTypeDef(BaseValidatorModel):
    usageCost: Optional[float] = None
    pricingUnit: Optional[PricingUnitType] = None
    unit: Optional[float] = None
    currency: Optional[Literal["USD"]] = None
    timePeriod: Optional[TimePeriodTypeDef] = None


class GetActiveNamesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetBlueprintsRequestPaginateTypeDef(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    appCategory: Optional[Literal["LfR"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetBundlesRequestPaginateTypeDef(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    appCategory: Optional[Literal["LfR"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCloudFormationStackRecordsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDiskSnapshotsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDisksRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDomainsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetExportSnapshotRecordsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetInstanceSnapshotsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetInstancesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetKeyPairsRequestPaginateTypeDef(BaseValidatorModel):
    includeDefaultKeyPair: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetLoadBalancersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetOperationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRelationalDatabaseBlueprintsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRelationalDatabaseBundlesRequestPaginateTypeDef(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRelationalDatabaseEventsRequestPaginateTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    durationInMinutes: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRelationalDatabaseParametersRequestPaginateTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRelationalDatabaseSnapshotsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetRelationalDatabasesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetStaticIpsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MetricDatapointTypeDef(BaseValidatorModel):
    pass


class GetBucketMetricDataResultTypeDef(BaseValidatorModel):
    metricName: BucketMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetContainerServiceMetricDataResultTypeDef(BaseValidatorModel):
    metricName: ContainerServiceMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDistributionMetricDataResultTypeDef(BaseValidatorModel):
    metricName: DistributionMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstanceMetricDataResultTypeDef(BaseValidatorModel):
    metricName: InstanceMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetLoadBalancerMetricDataResultTypeDef(BaseValidatorModel):
    metricName: LoadBalancerMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseMetricDataResultTypeDef(BaseValidatorModel):
    metricName: RelationalDatabaseMetricNameType
    metricData: List[MetricDatapointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstancePortStatesResultTypeDef(BaseValidatorModel):
    portStates: List[InstancePortStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstanceStateResultTypeDef(BaseValidatorModel):
    state: InstanceStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLoadBalancerTlsPoliciesResultTypeDef(BaseValidatorModel):
    tlsPolicies: List[LoadBalancerTlsPolicyTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseBlueprintsResultTypeDef(BaseValidatorModel):
    blueprints: List[RelationalDatabaseBlueprintTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseBundlesResultTypeDef(BaseValidatorModel):
    bundles: List[RelationalDatabaseBundleTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseEventsResultTypeDef(BaseValidatorModel):
    relationalDatabaseEvents: List[RelationalDatabaseEventTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseLogEventsResultTypeDef(BaseValidatorModel):
    resourceLogEvents: List[LogEventTypeDef]
    nextBackwardToken: str
    nextForwardToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseParametersResultTypeDef(BaseValidatorModel):
    parameters: List[RelationalDatabaseParameterTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRelationalDatabaseParametersRequestTypeDef(BaseValidatorModel):
    relationalDatabaseName: str
    parameters: Sequence[RelationalDatabaseParameterTypeDef]


class InstanceAccessDetailsTypeDef(BaseValidatorModel):
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


class InstanceNetworkingTypeDef(BaseValidatorModel):
    monthlyTransfer: Optional[MonthlyTransferTypeDef] = None
    ports: Optional[List[InstancePortInfoTypeDef]] = None


class LoadBalancerTlsCertificateRenewalSummaryTypeDef(BaseValidatorModel):
    renewalStatus: Optional[LoadBalancerTlsCertificateRenewalStatusType] = None
    domainValidationOptions: Optional[ List[LoadBalancerTlsCertificateDomainValidationOptionTypeDef] ] = None


class LoadBalancerTypeDef(BaseValidatorModel):
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


class RegisteredDomainDelegationInfoTypeDef(BaseValidatorModel):
    nameServersUpdateState: Optional[NameServersUpdateStateTypeDef] = None
    r53HostedZoneDeletionState: Optional[R53HostedZoneDeletionStateTypeDef] = None


class RelationalDatabaseTypeDef(BaseValidatorModel):
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


class GetBucketAccessKeysResultTypeDef(BaseValidatorModel):
    accessKeys: List[AccessKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDiskFromSnapshotRequestTypeDef(BaseValidatorModel):
    diskName: str
    availabilityZone: str
    sizeInGb: int
    diskSnapshotName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    addOns: Optional[Sequence[AddOnRequestTypeDef]] = None
    sourceDiskName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None


class CreateDiskRequestTypeDef(BaseValidatorModel):
    diskName: str
    availabilityZone: str
    sizeInGb: int
    tags: Optional[Sequence[TagTypeDef]] = None
    addOns: Optional[Sequence[AddOnRequestTypeDef]] = None


class CreateInstancesFromSnapshotRequestTypeDef(BaseValidatorModel):
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


class CreateInstancesRequestTypeDef(BaseValidatorModel):
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


class EnableAddOnRequestTypeDef(BaseValidatorModel):
    resourceName: str
    addOnRequest: AddOnRequestTypeDef


class GetAlarmsResultTypeDef(BaseValidatorModel):
    alarms: List[AlarmTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetContactMethodsResultTypeDef(BaseValidatorModel):
    contactMethods: List[ContactMethodTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class OperationTypeDef(BaseValidatorModel):
    pass


class AllocateStaticIpResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AttachCertificateToDistributionResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AttachDiskResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AttachInstancesToLoadBalancerResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AttachLoadBalancerTlsCertificateResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AttachStaticIpResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CloseInstancePublicPortsResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CopySnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBucketAccessKeyResultTypeDef(BaseValidatorModel):
    accessKey: AccessKeyTypeDef
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCloudFormationStackResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContactMethodResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDiskFromSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDiskResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDiskSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDomainEntryResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDomainResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInstanceSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInstancesFromSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInstancesResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLoadBalancerResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLoadBalancerTlsCertificateResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRelationalDatabaseFromSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRelationalDatabaseResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRelationalDatabaseSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAlarmResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAutoSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBucketAccessKeyResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBucketResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCertificateResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteContactMethodResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDiskResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDiskSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDistributionResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDomainEntryResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDomainResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInstanceResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInstanceSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteKeyPairResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteKnownHostKeysResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteLoadBalancerResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteLoadBalancerTlsCertificateResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRelationalDatabaseResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRelationalDatabaseSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DetachCertificateFromDistributionResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DetachDiskResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DetachInstancesFromLoadBalancerResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DetachStaticIpResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DisableAddOnResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EnableAddOnResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ExportSnapshotResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetOperationResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetOperationsForResourceResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    nextPageCount: str
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetOperationsResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportKeyPairResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OpenInstancePublicPortsResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PeerVpcResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutAlarmResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutInstancePublicPortsResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RebootInstanceResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RebootRelationalDatabaseResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ReleaseStaticIpResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ResetDistributionCacheResultTypeDef(BaseValidatorModel):
    status: str
    createTime: datetime
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SendContactMethodVerificationResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SetIpAddressTypeResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SetResourceAccessForBucketResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SetupInstanceHttpsResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartGUISessionResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartInstanceResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartRelationalDatabaseResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StopGUISessionResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StopInstanceResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StopRelationalDatabaseResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TestAlarmResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UnpeerVpcResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UntagResourceResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBucketBundleResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDistributionBundleResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDistributionResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDomainEntryResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateInstanceMetadataOptionsResultTypeDef(BaseValidatorModel):
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLoadBalancerAttributeResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRelationalDatabaseParametersResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRelationalDatabaseResultTypeDef(BaseValidatorModel):
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SetupHistoryTypeDef(BaseValidatorModel):
    operationId: Optional[str] = None
    request: Optional[SetupRequestTypeDef] = None
    resource: Optional[SetupHistoryResourceTypeDef] = None
    executionDetails: Optional[List[SetupExecutionDetailsTypeDef]] = None
    status: Optional[SetupStatusType] = None


class GetStaticIpResultTypeDef(BaseValidatorModel):
    staticIp: StaticIpTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetStaticIpsResultTypeDef(BaseValidatorModel):
    staticIps: List[StaticIpTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAutoSnapshotsResultTypeDef(BaseValidatorModel):
    resourceName: str
    resourceType: ResourceTypeType
    autoSnapshots: List[AutoSnapshotDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetRegionsResultTypeDef(BaseValidatorModel):
    regions: List[RegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBucketResultTypeDef(BaseValidatorModel):
    bucket: BucketTypeDef
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetBucketsResultTypeDef(BaseValidatorModel):
    buckets: List[BucketTypeDef]
    nextPageToken: str
    accountLevelBpaSync: AccountLevelBpaSyncTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBucketResultTypeDef(BaseValidatorModel):
    bucket: BucketTypeDef
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDiskSnapshotResultTypeDef(BaseValidatorModel):
    diskSnapshot: DiskSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDiskSnapshotsResultTypeDef(BaseValidatorModel):
    diskSnapshots: List[DiskSnapshotTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDiskResultTypeDef(BaseValidatorModel):
    disk: DiskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDisksResultTypeDef(BaseValidatorModel):
    disks: List[DiskTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class InstanceHardwareTypeDef(BaseValidatorModel):
    cpuCount: Optional[int] = None
    disks: Optional[List[DiskTypeDef]] = None
    ramSizeInGb: Optional[float] = None


class InstanceSnapshotTypeDef(BaseValidatorModel):
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


class CreateKeyPairResultTypeDef(BaseValidatorModel):
    keyPair: KeyPairTypeDef
    publicKeyBase64: str
    privateKeyBase64: str
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetKeyPairResultTypeDef(BaseValidatorModel):
    keyPair: KeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetKeyPairsResultTypeDef(BaseValidatorModel):
    keyPairs: List[KeyPairTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseSnapshotResultTypeDef(BaseValidatorModel):
    relationalDatabaseSnapshot: RelationalDatabaseSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabaseSnapshotsResultTypeDef(BaseValidatorModel):
    relationalDatabaseSnapshots: List[RelationalDatabaseSnapshotTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class LightsailDistributionTypeDef(BaseValidatorModel):
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


class GetCloudFormationStackRecordsResultTypeDef(BaseValidatorModel):
    cloudFormationStackRecords: List[CloudFormationStackRecordTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContainerServiceRequestTypeDef(BaseValidatorModel):
    serviceName: str
    power: Optional[ContainerServicePowerNameType] = None
    scale: Optional[int] = None
    isDisabled: Optional[bool] = None
    publicDomainNames: Optional[Mapping[str, Sequence[str]]] = None
    privateRegistryAccess: Optional[PrivateRegistryAccessRequestTypeDef] = None


class ContainerServiceDeploymentTypeDef(BaseValidatorModel):
    version: Optional[int] = None
    state: Optional[ContainerServiceDeploymentStateType] = None
    containers: Optional[Dict[str, ContainerOutputTypeDef]] = None
    publicEndpoint: Optional[ContainerServiceEndpointTypeDef] = None
    createdAt: Optional[datetime] = None


class ContainerUnionTypeDef(BaseValidatorModel):
    pass


class ContainerServiceDeploymentRequestTypeDef(BaseValidatorModel):
    containers: Optional[Mapping[str, ContainerUnionTypeDef]] = None
    publicEndpoint: Optional[EndpointRequestTypeDef] = None


class CreateContainerServiceDeploymentRequestTypeDef(BaseValidatorModel):
    serviceName: str
    containers: Optional[Mapping[str, ContainerUnionTypeDef]] = None
    publicEndpoint: Optional[EndpointRequestTypeDef] = None


class ExportSnapshotRecordSourceInfoTypeDef(BaseValidatorModel):
    resourceType: Optional[ExportSnapshotRecordSourceTypeType] = None
    createdAt: Optional[datetime] = None
    name: Optional[str] = None
    arn: Optional[str] = None
    fromResourceName: Optional[str] = None
    fromResourceArn: Optional[str] = None
    instanceSnapshotInfo: Optional[InstanceSnapshotInfoTypeDef] = None
    diskSnapshotInfo: Optional[DiskSnapshotInfoTypeDef] = None


class DomainEntryUnionTypeDef(BaseValidatorModel):
    pass


class CreateDomainEntryRequestTypeDef(BaseValidatorModel):
    domainName: str
    domainEntry: DomainEntryUnionTypeDef


class DeleteDomainEntryRequestTypeDef(BaseValidatorModel):
    domainName: str
    domainEntry: DomainEntryUnionTypeDef


class UpdateDomainEntryRequestTypeDef(BaseValidatorModel):
    domainName: str
    domainEntry: DomainEntryUnionTypeDef


class RenewalSummaryTypeDef(BaseValidatorModel):
    domainValidationRecords: Optional[List[DomainValidationRecordTypeDef]] = None
    renewalStatus: Optional[RenewalStatusType] = None
    renewalStatusReason: Optional[str] = None
    updatedAt: Optional[datetime] = None


class CostEstimateTypeDef(BaseValidatorModel):
    usageType: Optional[str] = None
    resultsByTime: Optional[List[EstimateByTimeTypeDef]] = None


class GetInstanceAccessDetailsResultTypeDef(BaseValidatorModel):
    accessDetails: InstanceAccessDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LoadBalancerTlsCertificateDomainValidationRecordTypeDef(BaseValidatorModel):
    pass


class LoadBalancerTlsCertificateTypeDef(BaseValidatorModel):
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
    domainValidationRecords: Optional[ List[LoadBalancerTlsCertificateDomainValidationRecordTypeDef] ] = None
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


class GetLoadBalancerResultTypeDef(BaseValidatorModel):
    loadBalancer: LoadBalancerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLoadBalancersResultTypeDef(BaseValidatorModel):
    loadBalancers: List[LoadBalancerTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class DomainEntryOutputTypeDef(BaseValidatorModel):
    pass


class DomainTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    supportCode: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    tags: Optional[List[TagTypeDef]] = None
    domainEntries: Optional[List[DomainEntryOutputTypeDef]] = None
    registeredDomainDelegationInfo: Optional[RegisteredDomainDelegationInfoTypeDef] = None


class GetRelationalDatabaseResultTypeDef(BaseValidatorModel):
    relationalDatabase: RelationalDatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRelationalDatabasesResultTypeDef(BaseValidatorModel):
    relationalDatabases: List[RelationalDatabaseTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSetupHistoryResultTypeDef(BaseValidatorModel):
    setupHistory: List[SetupHistoryTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class InstanceTypeDef(BaseValidatorModel):
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


class GetInstanceSnapshotResultTypeDef(BaseValidatorModel):
    instanceSnapshot: InstanceSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstanceSnapshotsResultTypeDef(BaseValidatorModel):
    instanceSnapshots: List[InstanceSnapshotTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDistributionResultTypeDef(BaseValidatorModel):
    distribution: LightsailDistributionTypeDef
    operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDistributionsResultTypeDef(BaseValidatorModel):
    distributions: List[LightsailDistributionTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CacheSettingsUnionTypeDef(BaseValidatorModel):
    pass


class CreateDistributionRequestTypeDef(BaseValidatorModel):
    distributionName: str
    origin: InputOriginTypeDef
    defaultCacheBehavior: CacheBehaviorTypeDef
    bundleId: str
    cacheBehaviorSettings: Optional[CacheSettingsUnionTypeDef] = None
    cacheBehaviors: Optional[Sequence[CacheBehaviorPerPathTypeDef]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    certificateName: Optional[str] = None
    viewerMinimumTlsProtocolVersion: Optional[ViewerMinimumTlsProtocolVersionEnumType] = None


class UpdateDistributionRequestTypeDef(BaseValidatorModel):
    distributionName: str
    origin: Optional[InputOriginTypeDef] = None
    defaultCacheBehavior: Optional[CacheBehaviorTypeDef] = None
    cacheBehaviorSettings: Optional[CacheSettingsUnionTypeDef] = None
    cacheBehaviors: Optional[Sequence[CacheBehaviorPerPathTypeDef]] = None
    isEnabled: Optional[bool] = None
    viewerMinimumTlsProtocolVersion: Optional[ViewerMinimumTlsProtocolVersionEnumType] = None
    certificateName: Optional[str] = None
    useDefaultCertificate: Optional[bool] = None


class ContainerServiceTypeDef(BaseValidatorModel):
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


class GetContainerServiceDeploymentsResultTypeDef(BaseValidatorModel):
    deployments: List[ContainerServiceDeploymentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContainerServiceRequestTypeDef(BaseValidatorModel):
    serviceName: str
    power: ContainerServicePowerNameType
    scale: int
    tags: Optional[Sequence[TagTypeDef]] = None
    publicDomainNames: Optional[Mapping[str, Sequence[str]]] = None
    deployment: Optional[ContainerServiceDeploymentRequestTypeDef] = None
    privateRegistryAccess: Optional[PrivateRegistryAccessRequestTypeDef] = None


class ExportSnapshotRecordTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocationTypeDef] = None
    resourceType: Optional[ResourceTypeType] = None
    state: Optional[RecordStateType] = None
    sourceInfo: Optional[ExportSnapshotRecordSourceInfoTypeDef] = None
    destinationInfo: Optional[DestinationInfoTypeDef] = None


class CertificateTypeDef(BaseValidatorModel):
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


class ResourceBudgetEstimateTypeDef(BaseValidatorModel):
    resourceName: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    costEstimates: Optional[List[CostEstimateTypeDef]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetLoadBalancerTlsCertificatesResultTypeDef(BaseValidatorModel):
    tlsCertificates: List[LoadBalancerTlsCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDomainResultTypeDef(BaseValidatorModel):
    domain: DomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDomainsResultTypeDef(BaseValidatorModel):
    domains: List[DomainTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstanceResultTypeDef(BaseValidatorModel):
    instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetInstancesResultTypeDef(BaseValidatorModel):
    instances: List[InstanceTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ContainerServicesListResultTypeDef(BaseValidatorModel):
    containerServices: List[ContainerServiceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContainerServiceDeploymentResultTypeDef(BaseValidatorModel):
    containerService: ContainerServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContainerServiceResultTypeDef(BaseValidatorModel):
    containerService: ContainerServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContainerServiceResultTypeDef(BaseValidatorModel):
    containerService: ContainerServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetExportSnapshotRecordsResultTypeDef(BaseValidatorModel):
    exportSnapshotRecords: List[ExportSnapshotRecordTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CertificateSummaryTypeDef(BaseValidatorModel):
    certificateArn: Optional[str] = None
    certificateName: Optional[str] = None
    domainName: Optional[str] = None
    certificateDetail: Optional[CertificateTypeDef] = None
    tags: Optional[List[TagTypeDef]] = None


class GetCostEstimateResultTypeDef(BaseValidatorModel):
    resourcesBudgetEstimate: List[ResourceBudgetEstimateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCertificateResultTypeDef(BaseValidatorModel):
    certificate: CertificateSummaryTypeDef
    operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetCertificatesResultTypeDef(BaseValidatorModel):
    certificates: List[CertificateSummaryTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef



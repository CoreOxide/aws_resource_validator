from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.lightsail.lightsail_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'allocate_static_ip' function.
class AllocateStaticIpRequest(BaseValidatorModel):
    staticIpName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'attach_certificate_to_distribution' function.
class AttachCertificateToDistributionRequest(BaseValidatorModel):
    distributionName: str
    certificateName: str


# This class is the input for the 'attach_disk' function.
class AttachDiskRequest(BaseValidatorModel):
    diskName: str
    instanceName: str
    diskPath: str
    autoMounting: Optional[bool] = None


# This class is the input for the 'attach_instances_to_load_balancer' function.
class AttachInstancesToLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str
    instanceNames: List[str]


# This class is the input for the 'attach_load_balancer_tls_certificate' function.
class AttachLoadBalancerTlsCertificateRequest(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str


# This class is the input for the 'attach_static_ip' function.
class AttachStaticIpRequest(BaseValidatorModel):
    staticIpName: str
    instanceName: str


class AttachedDisk(BaseValidatorModel):
    path: Optional[str] = None
    sizeInGb: Optional[int] = None


class AvailabilityZone(BaseValidatorModel):
    zoneName: Optional[str] = None
    state: Optional[str] = None


class Blueprint(BaseValidatorModel):
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
    appCategory: Optional[Literal['LfR']] = None


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
    supportedAppCategories: Optional[List[Literal['LfR']]] = None
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
    cookiesAllowList: Optional[List[str]] = None


class HeaderObject(BaseValidatorModel):
    option: Optional[ForwardValuesType] = None
    headersAllowList: Optional[List[HeaderEnumType]] = None


class QueryStringObject(BaseValidatorModel):
    option: Optional[bool] = None
    queryStringsAllowList: Optional[List[str]] = None


class PortInfo(BaseValidatorModel):
    fromPort: Optional[int] = None
    toPort: Optional[int] = None
    protocol: Optional[NetworkProtocolType] = None
    cidrs: Optional[List[str]] = None
    ipv6Cidrs: Optional[List[str]] = None
    cidrListAliases: Optional[List[str]] = None


class CloudFormationStackRecordSourceInfo(BaseValidatorModel):
    resourceType: Optional[Literal['ExportSnapshotRecord']] = None
    name: Optional[str] = None
    arn: Optional[str] = None


class DestinationInfo(BaseValidatorModel):
    id: Optional[str] = None
    service: Optional[str] = None


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
    command: Optional[List[str]] = None
    environment: Optional[Dict[str, str]] = None
    ports: Optional[Dict[str, ContainerServiceProtocolType]] = None


# This class is the input for the 'copy_snapshot' function.
class CopySnapshotRequest(BaseValidatorModel):
    targetSnapshotName: str
    sourceRegion: RegionNameType
    sourceSnapshotName: Optional[str] = None
    sourceResourceName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None


# This class is the input for the 'create_bucket_access_key' function.
class CreateBucketAccessKeyRequest(BaseValidatorModel):
    bucketName: str


class InstanceEntry(BaseValidatorModel):
    sourceName: str
    instanceType: str
    portInfoSource: PortInfoSourceTypeType
    availabilityZone: str
    userData: Optional[str] = None


# This class is the input for the 'create_contact_method' function.
class CreateContactMethodRequest(BaseValidatorModel):
    protocol: ContactProtocolType
    contactEndpoint: str


class InputOrigin(BaseValidatorModel):
    name: Optional[str] = None
    regionName: Optional[RegionNameType] = None
    protocolPolicy: Optional[OriginProtocolPolicyEnumType] = None
    responseTimeout: Optional[int] = None


# This class is the input for the 'create_gui_session_access_details' function.
class CreateGUISessionAccessDetailsRequest(BaseValidatorModel):
    resourceName: str


class Session(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None
    isPrimary: Optional[bool] = None


class DiskMap(BaseValidatorModel):
    originalDiskPath: Optional[str] = None
    newDiskName: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'delete_alarm' function.
class DeleteAlarmRequest(BaseValidatorModel):
    alarmName: str


# This class is the input for the 'delete_auto_snapshot' function.
class DeleteAutoSnapshotRequest(BaseValidatorModel):
    resourceName: str
    date: str


# This class is the input for the 'delete_bucket_access_key' function.
class DeleteBucketAccessKeyRequest(BaseValidatorModel):
    bucketName: str
    accessKeyId: str


# This class is the input for the 'delete_bucket' function.
class DeleteBucketRequest(BaseValidatorModel):
    bucketName: str
    forceDelete: Optional[bool] = None


# This class is the input for the 'delete_certificate' function.
class DeleteCertificateRequest(BaseValidatorModel):
    certificateName: str


# This class is the input for the 'delete_contact_method' function.
class DeleteContactMethodRequest(BaseValidatorModel):
    protocol: ContactProtocolType


class DeleteContainerImageRequest(BaseValidatorModel):
    serviceName: str
    image: str


class DeleteContainerServiceRequest(BaseValidatorModel):
    serviceName: str


# This class is the input for the 'delete_disk' function.
class DeleteDiskRequest(BaseValidatorModel):
    diskName: str
    forceDeleteAddOns: Optional[bool] = None


# This class is the input for the 'delete_disk_snapshot' function.
class DeleteDiskSnapshotRequest(BaseValidatorModel):
    diskSnapshotName: str


# This class is the input for the 'delete_distribution' function.
class DeleteDistributionRequest(BaseValidatorModel):
    distributionName: Optional[str] = None


# This class is the input for the 'delete_domain' function.
class DeleteDomainRequest(BaseValidatorModel):
    domainName: str


# This class is the input for the 'delete_instance' function.
class DeleteInstanceRequest(BaseValidatorModel):
    instanceName: str
    forceDeleteAddOns: Optional[bool] = None


# This class is the input for the 'delete_instance_snapshot' function.
class DeleteInstanceSnapshotRequest(BaseValidatorModel):
    instanceSnapshotName: str


# This class is the input for the 'delete_key_pair' function.
class DeleteKeyPairRequest(BaseValidatorModel):
    keyPairName: str
    expectedFingerprint: Optional[str] = None


# This class is the input for the 'delete_known_host_keys' function.
class DeleteKnownHostKeysRequest(BaseValidatorModel):
    instanceName: str


# This class is the input for the 'delete_load_balancer' function.
class DeleteLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str


# This class is the input for the 'delete_load_balancer_tls_certificate' function.
class DeleteLoadBalancerTlsCertificateRequest(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str
    force: Optional[bool] = None


# This class is the input for the 'delete_relational_database' function.
class DeleteRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str
    skipFinalSnapshot: Optional[bool] = None
    finalRelationalDatabaseSnapshotName: Optional[str] = None


# This class is the input for the 'delete_relational_database_snapshot' function.
class DeleteRelationalDatabaseSnapshotRequest(BaseValidatorModel):
    relationalDatabaseSnapshotName: str


# This class is the input for the 'detach_certificate_from_distribution' function.
class DetachCertificateFromDistributionRequest(BaseValidatorModel):
    distributionName: str


# This class is the input for the 'detach_disk' function.
class DetachDiskRequest(BaseValidatorModel):
    diskName: str


# This class is the input for the 'detach_instances_from_load_balancer' function.
class DetachInstancesFromLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str
    instanceNames: List[str]


# This class is the input for the 'detach_static_ip' function.
class DetachStaticIpRequest(BaseValidatorModel):
    staticIpName: str


# This class is the input for the 'disable_add_on' function.
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


class DomainEntryOutput(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    target: Optional[str] = None
    isAlias: Optional[bool] = None
    type: Optional[str] = None
    options: Optional[Dict[str, str]] = None


class DomainEntry(BaseValidatorModel):
    id: Optional[str] = None
    name: Optional[str] = None
    target: Optional[str] = None
    isAlias: Optional[bool] = None
    type: Optional[str] = None
    options: Optional[Dict[str, str]] = None


class ResourceRecord(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None


class TimePeriod(BaseValidatorModel):
    start: Optional[datetime] = None
    end: Optional[datetime] = None


# This class is the input for the 'export_snapshot' function.
class ExportSnapshotRequest(BaseValidatorModel):
    sourceSnapshotName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_active_names' function.
class GetActiveNamesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_alarms' function.
class GetAlarmsRequest(BaseValidatorModel):
    alarmName: Optional[str] = None
    pageToken: Optional[str] = None
    monitoredResourceName: Optional[str] = None


# This class is the input for the 'get_auto_snapshots' function.
class GetAutoSnapshotsRequest(BaseValidatorModel):
    resourceName: str


# This class is the input for the 'get_blueprints' function.
class GetBlueprintsRequest(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    pageToken: Optional[str] = None
    appCategory: Optional[Literal['LfR']] = None


# This class is the input for the 'get_bucket_access_keys' function.
class GetBucketAccessKeysRequest(BaseValidatorModel):
    bucketName: str


# This class is the input for the 'get_bucket_bundles' function.
class GetBucketBundlesRequest(BaseValidatorModel):
    includeInactive: Optional[bool] = None


class MetricDatapoint(BaseValidatorModel):
    average: Optional[float] = None
    maximum: Optional[float] = None
    minimum: Optional[float] = None
    sampleCount: Optional[float] = None
    sum: Optional[float] = None
    timestamp: Optional[datetime] = None
    unit: Optional[MetricUnitType] = None


# This class is the input for the 'get_buckets' function.
class GetBucketsRequest(BaseValidatorModel):
    bucketName: Optional[str] = None
    pageToken: Optional[str] = None
    includeConnectedResources: Optional[bool] = None


# This class is the input for the 'get_bundles' function.
class GetBundlesRequest(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    pageToken: Optional[str] = None
    appCategory: Optional[Literal['LfR']] = None


# This class is the input for the 'get_certificates' function.
class GetCertificatesRequest(BaseValidatorModel):
    certificateStatuses: Optional[List[CertificateStatusType]] = None
    includeCertificateDetails: Optional[bool] = None
    certificateName: Optional[str] = None
    pageToken: Optional[str] = None


# This class is the input for the 'get_cloud_formation_stack_records' function.
class GetCloudFormationStackRecordsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_contact_methods' function.
class GetContactMethodsRequest(BaseValidatorModel):
    protocols: Optional[List[ContactProtocolType]] = None


# This class is the input for the 'get_container_images' function.
class GetContainerImagesRequest(BaseValidatorModel):
    serviceName: str


# This class is the input for the 'get_container_service_deployments' function.
class GetContainerServiceDeploymentsRequest(BaseValidatorModel):
    serviceName: str


# This class is the input for the 'get_container_services' function.
class GetContainerServicesRequest(BaseValidatorModel):
    serviceName: Optional[str] = None


# This class is the input for the 'get_disk' function.
class GetDiskRequest(BaseValidatorModel):
    diskName: str


# This class is the input for the 'get_disk_snapshot' function.
class GetDiskSnapshotRequest(BaseValidatorModel):
    diskSnapshotName: str


# This class is the input for the 'get_disk_snapshots' function.
class GetDiskSnapshotsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_disks' function.
class GetDisksRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_distribution_latest_cache_reset' function.
class GetDistributionLatestCacheResetRequest(BaseValidatorModel):
    distributionName: Optional[str] = None


# This class is the input for the 'get_distributions' function.
class GetDistributionsRequest(BaseValidatorModel):
    distributionName: Optional[str] = None
    pageToken: Optional[str] = None


# This class is the input for the 'get_domain' function.
class GetDomainRequest(BaseValidatorModel):
    domainName: str


# This class is the input for the 'get_domains' function.
class GetDomainsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_export_snapshot_records' function.
class GetExportSnapshotRecordsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_instance_access_details' function.
class GetInstanceAccessDetailsRequest(BaseValidatorModel):
    instanceName: str
    protocol: Optional[InstanceAccessProtocolType] = None


# This class is the input for the 'get_instance_port_states' function.
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


# This class is the input for the 'get_instance' function.
class GetInstanceRequest(BaseValidatorModel):
    instanceName: str


# This class is the input for the 'get_instance_snapshot' function.
class GetInstanceSnapshotRequest(BaseValidatorModel):
    instanceSnapshotName: str


# This class is the input for the 'get_instance_snapshots' function.
class GetInstanceSnapshotsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_instance_state' function.
class GetInstanceStateRequest(BaseValidatorModel):
    instanceName: str


class InstanceState(BaseValidatorModel):
    code: Optional[int] = None
    name: Optional[str] = None


# This class is the input for the 'get_instances' function.
class GetInstancesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_key_pair' function.
class GetKeyPairRequest(BaseValidatorModel):
    keyPairName: str


# This class is the input for the 'get_key_pairs' function.
class GetKeyPairsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None
    includeDefaultKeyPair: Optional[bool] = None


# This class is the input for the 'get_load_balancer' function.
class GetLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str


# This class is the input for the 'get_load_balancer_tls_certificates' function.
class GetLoadBalancerTlsCertificatesRequest(BaseValidatorModel):
    loadBalancerName: str


# This class is the input for the 'get_load_balancer_tls_policies' function.
class GetLoadBalancerTlsPoliciesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class LoadBalancerTlsPolicy(BaseValidatorModel):
    name: Optional[str] = None
    isDefault: Optional[bool] = None
    description: Optional[str] = None
    protocols: Optional[List[str]] = None
    ciphers: Optional[List[str]] = None


# This class is the input for the 'get_load_balancers' function.
class GetLoadBalancersRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_operation' function.
class GetOperationRequest(BaseValidatorModel):
    operationId: str


# This class is the input for the 'get_operations_for_resource' function.
class GetOperationsForResourceRequest(BaseValidatorModel):
    resourceName: str
    pageToken: Optional[str] = None


# This class is the input for the 'get_operations' function.
class GetOperationsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_regions' function.
class GetRegionsRequest(BaseValidatorModel):
    includeAvailabilityZones: Optional[bool] = None
    includeRelationalDatabaseAvailabilityZones: Optional[bool] = None


# This class is the input for the 'get_relational_database_blueprints' function.
class GetRelationalDatabaseBlueprintsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


class RelationalDatabaseBlueprint(BaseValidatorModel):
    blueprintId: Optional[str] = None
    engine: Optional[Literal['mysql']] = None
    engineVersion: Optional[str] = None
    engineDescription: Optional[str] = None
    engineVersionDescription: Optional[str] = None
    isEngineDefault: Optional[bool] = None


# This class is the input for the 'get_relational_database_bundles' function.
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


# This class is the input for the 'get_relational_database_events' function.
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


# This class is the input for the 'get_relational_database_log_streams' function.
class GetRelationalDatabaseLogStreamsRequest(BaseValidatorModel):
    relationalDatabaseName: str


# This class is the input for the 'get_relational_database_master_user_password' function.
class GetRelationalDatabaseMasterUserPasswordRequest(BaseValidatorModel):
    relationalDatabaseName: str
    passwordVersion: Optional[RelationalDatabasePasswordVersionType] = None


# This class is the input for the 'get_relational_database_parameters' function.
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


# This class is the input for the 'get_relational_database' function.
class GetRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str


# This class is the input for the 'get_relational_database_snapshot' function.
class GetRelationalDatabaseSnapshotRequest(BaseValidatorModel):
    relationalDatabaseSnapshotName: str


# This class is the input for the 'get_relational_database_snapshots' function.
class GetRelationalDatabaseSnapshotsRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_relational_databases' function.
class GetRelationalDatabasesRequest(BaseValidatorModel):
    pageToken: Optional[str] = None


# This class is the input for the 'get_setup_history' function.
class GetSetupHistoryRequest(BaseValidatorModel):
    resourceName: str
    pageToken: Optional[str] = None


# This class is the input for the 'get_static_ip' function.
class GetStaticIpRequest(BaseValidatorModel):
    staticIpName: str


# This class is the input for the 'get_static_ips' function.
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


# This class is the input for the 'import_key_pair' function.
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


# This class is the input for the 'put_alarm' function.
class PutAlarmRequest(BaseValidatorModel):
    alarmName: str
    metricName: MetricNameType
    monitoredResourceName: str
    comparisonOperator: ComparisonOperatorType
    threshold: float
    evaluationPeriods: int
    datapointsToAlarm: Optional[int] = None
    treatMissingData: Optional[TreatMissingDataType] = None
    contactProtocols: Optional[List[ContactProtocolType]] = None
    notificationTriggers: Optional[List[AlarmStateType]] = None
    notificationEnabled: Optional[bool] = None


class R53HostedZoneDeletionState(BaseValidatorModel):
    code: Optional[R53HostedZoneDeletionStateCodeType] = None
    message: Optional[str] = None


# This class is the input for the 'reboot_instance' function.
class RebootInstanceRequest(BaseValidatorModel):
    instanceName: str


# This class is the input for the 'reboot_relational_database' function.
class RebootRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str


# This class is the input for the 'register_container_image' function.
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


# This class is the input for the 'release_static_ip' function.
class ReleaseStaticIpRequest(BaseValidatorModel):
    staticIpName: str


# This class is the input for the 'reset_distribution_cache' function.
class ResetDistributionCacheRequest(BaseValidatorModel):
    distributionName: Optional[str] = None


# This class is the input for the 'send_contact_method_verification' function.
class SendContactMethodVerificationRequest(BaseValidatorModel):
    protocol: Literal['Email']


# This class is the input for the 'set_ip_address_type' function.
class SetIpAddressTypeRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    resourceName: str
    ipAddressType: IpAddressTypeType
    acceptBundleUpdate: Optional[bool] = None


# This class is the input for the 'set_resource_access_for_bucket' function.
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
    certificateProvider: Optional[Literal['LetsEncrypt']] = None


# This class is the input for the 'setup_instance_https' function.
class SetupInstanceHttpsRequest(BaseValidatorModel):
    instanceName: str
    emailAddress: str
    domainNames: List[str]
    certificateProvider: Literal['LetsEncrypt']


# This class is the input for the 'start_gui_session' function.
class StartGUISessionRequest(BaseValidatorModel):
    resourceName: str


# This class is the input for the 'start_instance' function.
class StartInstanceRequest(BaseValidatorModel):
    instanceName: str


# This class is the input for the 'start_relational_database' function.
class StartRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str


# This class is the input for the 'stop_gui_session' function.
class StopGUISessionRequest(BaseValidatorModel):
    resourceName: str


# This class is the input for the 'stop_instance' function.
class StopInstanceRequest(BaseValidatorModel):
    instanceName: str
    force: Optional[bool] = None


# This class is the input for the 'stop_relational_database' function.
class StopRelationalDatabaseRequest(BaseValidatorModel):
    relationalDatabaseName: str
    relationalDatabaseSnapshotName: Optional[str] = None


# This class is the input for the 'test_alarm' function.
class TestAlarmRequest(BaseValidatorModel):
    alarmName: str
    state: AlarmStateType


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    resourceName: str
    tagKeys: List[str]
    resourceArn: Optional[str] = None


# This class is the input for the 'update_bucket_bundle' function.
class UpdateBucketBundleRequest(BaseValidatorModel):
    bucketName: str
    bundleId: str


# This class is the input for the 'update_distribution_bundle' function.
class UpdateDistributionBundleRequest(BaseValidatorModel):
    distributionName: Optional[str] = None
    bundleId: Optional[str] = None


# This class is the input for the 'update_instance_metadata_options' function.
class UpdateInstanceMetadataOptionsRequest(BaseValidatorModel):
    instanceName: str
    httpTokens: Optional[HttpTokensType] = None
    httpEndpoint: Optional[HttpEndpointType] = None
    httpPutResponseHopLimit: Optional[int] = None
    httpProtocolIpv6: Optional[HttpProtocolIpv6Type] = None


# This class is the input for the 'update_load_balancer_attribute' function.
class UpdateLoadBalancerAttributeRequest(BaseValidatorModel):
    loadBalancerName: str
    attributeName: LoadBalancerAttributeNameType
    attributeValue: str


# This class is the input for the 'update_relational_database' function.
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


class Operation(BaseValidatorModel):
    id: Optional[str] = None
    resourceName: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    isTerminal: Optional[bool] = None
    operationDetails: Optional[str] = None
    operationType: Optional[OperationTypeType] = None
    status: Optional[OperationStatusType] = None
    statusChangedAt: Optional[datetime] = None
    errorCode: Optional[str] = None
    errorDetails: Optional[str] = None


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


# This class is the output for the 'get_active_names' function.
class GetActiveNamesResult(BaseValidatorModel):
    activeNames: List[str]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class GetContainerAPIMetadataResult(BaseValidatorModel):
    metadata: List[Dict[str, str]]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_distribution_latest_cache_reset' function.
class GetDistributionLatestCacheResetResult(BaseValidatorModel):
    status: str
    createTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_log_streams' function.
class GetRelationalDatabaseLogStreamsResult(BaseValidatorModel):
    logStreams: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_master_user_password' function.
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


# This class is the output for the 'get_blueprints' function.
class GetBlueprintsResult(BaseValidatorModel):
    blueprints: List[Blueprint]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_bucket' function.
class UpdateBucketRequest(BaseValidatorModel):
    bucketName: str
    accessRules: Optional[AccessRules] = None
    versioning: Optional[str] = None
    readonlyAccessAccounts: Optional[List[str]] = None
    accessLogConfig: Optional[BucketAccessLogConfig] = None


# This class is the output for the 'get_bucket_bundles' function.
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


# This class is the input for the 'create_bucket' function.
class CreateBucketRequest(BaseValidatorModel):
    bucketName: str
    bundleId: str
    tags: Optional[List[Tag]] = None
    enableObjectVersioning: Optional[bool] = None


# This class is the input for the 'create_certificate' function.
class CreateCertificateRequest(BaseValidatorModel):
    certificateName: str
    domainName: str
    subjectAlternativeNames: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_disk_snapshot' function.
class CreateDiskSnapshotRequest(BaseValidatorModel):
    diskSnapshotName: str
    diskName: Optional[str] = None
    instanceName: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_domain' function.
class CreateDomainRequest(BaseValidatorModel):
    domainName: str
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_instance_snapshot' function.
class CreateInstanceSnapshotRequest(BaseValidatorModel):
    instanceSnapshotName: str
    instanceName: str
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_key_pair' function.
class CreateKeyPairRequest(BaseValidatorModel):
    keyPairName: str
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_load_balancer' function.
class CreateLoadBalancerRequest(BaseValidatorModel):
    loadBalancerName: str
    instancePort: int
    healthCheckPath: Optional[str] = None
    certificateName: Optional[str] = None
    certificateDomainName: Optional[str] = None
    certificateAlternativeNames: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tlsPolicyName: Optional[str] = None


# This class is the input for the 'create_load_balancer_tls_certificate' function.
class CreateLoadBalancerTlsCertificateRequest(BaseValidatorModel):
    loadBalancerName: str
    certificateName: str
    certificateDomainName: str
    certificateAlternativeNames: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_relational_database' function.
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
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_relational_database_snapshot' function.
class CreateRelationalDatabaseSnapshotRequest(BaseValidatorModel):
    relationalDatabaseName: str
    relationalDatabaseSnapshotName: str
    tags: Optional[List[Tag]] = None


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


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    resourceName: str
    tags: List[Tag]
    resourceArn: Optional[str] = None


# This class is the output for the 'get_bundles' function.
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


# This class is the input for the 'close_instance_public_ports' function.
class CloseInstancePublicPortsRequest(BaseValidatorModel):
    portInfo: PortInfo
    instanceName: str


# This class is the input for the 'open_instance_public_ports' function.
class OpenInstancePublicPortsRequest(BaseValidatorModel):
    portInfo: PortInfo
    instanceName: str


# This class is the input for the 'put_instance_public_ports' function.
class PutInstancePublicPortsRequest(BaseValidatorModel):
    portInfos: List[PortInfo]
    instanceName: str


class CloudFormationStackRecord(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    location: Optional[ResourceLocation] = None
    resourceType: Optional[ResourceTypeType] = None
    state: Optional[RecordStateType] = None
    sourceInfo: Optional[List[CloudFormationStackRecordSourceInfo]] = None
    destinationInfo: Optional[DestinationInfo] = None


# This class is the output for the 'get_container_images' function.
class GetContainerImagesResult(BaseValidatorModel):
    containerImages: List[ContainerImage]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_container_image' function.
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


# This class is the output for the 'get_container_log' function.
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

ContainerUnion = Union[Container, ContainerOutput]


# This class is the input for the 'create_cloud_formation_stack' function.
class CreateCloudFormationStackRequest(BaseValidatorModel):
    instances: List[InstanceEntry]


# This class is the output for the 'create_gui_session_access_details' function.
class CreateGUISessionAccessDetailsResult(BaseValidatorModel):
    resourceName: str
    status: StatusType
    percentageComplete: int
    failureReason: str
    sessions: List[Session]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_relational_database_from_snapshot' function.
class CreateRelationalDatabaseFromSnapshotRequest(BaseValidatorModel):
    relationalDatabaseName: str
    availabilityZone: Optional[str] = None
    publiclyAccessible: Optional[bool] = None
    relationalDatabaseSnapshotName: Optional[str] = None
    relationalDatabaseBundleId: Optional[str] = None
    sourceRelationalDatabaseName: Optional[str] = None
    restoreTime: Optional[Timestamp] = None
    useLatestRestorableTime: Optional[bool] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'get_bucket_metric_data' function.
class GetBucketMetricDataRequest(BaseValidatorModel):
    bucketName: str
    metricName: BucketMetricNameType
    startTime: Timestamp
    endTime: Timestamp
    period: int
    statistics: List[MetricStatisticType]
    unit: MetricUnitType


# This class is the input for the 'get_container_log' function.
class GetContainerLogRequest(BaseValidatorModel):
    serviceName: str
    containerName: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    filterPattern: Optional[str] = None
    pageToken: Optional[str] = None


# This class is the input for the 'get_container_service_metric_data' function.
class GetContainerServiceMetricDataRequest(BaseValidatorModel):
    serviceName: str
    metricName: ContainerServiceMetricNameType
    startTime: Timestamp
    endTime: Timestamp
    period: int
    statistics: List[MetricStatisticType]


# This class is the input for the 'get_cost_estimate' function.
class GetCostEstimateRequest(BaseValidatorModel):
    resourceName: str
    startTime: Timestamp
    endTime: Timestamp


# This class is the input for the 'get_distribution_metric_data' function.
class GetDistributionMetricDataRequest(BaseValidatorModel):
    distributionName: str
    metricName: DistributionMetricNameType
    startTime: Timestamp
    endTime: Timestamp
    period: int
    unit: MetricUnitType
    statistics: List[MetricStatisticType]


# This class is the input for the 'get_instance_metric_data' function.
class GetInstanceMetricDataRequest(BaseValidatorModel):
    instanceName: str
    metricName: InstanceMetricNameType
    period: int
    startTime: Timestamp
    endTime: Timestamp
    unit: MetricUnitType
    statistics: List[MetricStatisticType]


# This class is the input for the 'get_load_balancer_metric_data' function.
class GetLoadBalancerMetricDataRequest(BaseValidatorModel):
    loadBalancerName: str
    metricName: LoadBalancerMetricNameType
    period: int
    startTime: Timestamp
    endTime: Timestamp
    unit: MetricUnitType
    statistics: List[MetricStatisticType]


# This class is the input for the 'get_relational_database_log_events' function.
class GetRelationalDatabaseLogEventsRequest(BaseValidatorModel):
    relationalDatabaseName: str
    logStreamName: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    startFromHead: Optional[bool] = None
    pageToken: Optional[str] = None


# This class is the input for the 'get_relational_database_metric_data' function.
class GetRelationalDatabaseMetricDataRequest(BaseValidatorModel):
    relationalDatabaseName: str
    metricName: RelationalDatabaseMetricNameType
    period: int
    startTime: Timestamp
    endTime: Timestamp
    unit: MetricUnitType
    statistics: List[MetricStatisticType]


class InstanceSnapshotInfo(BaseValidatorModel):
    fromBundleId: Optional[str] = None
    fromBlueprintId: Optional[str] = None
    fromDiskInfo: Optional[List[DiskInfo]] = None


class GetDistributionBundlesResult(BaseValidatorModel):
    bundles: List[DistributionBundle]
    ResponseMetadata: ResponseMetadata

DomainEntryUnion = Union[DomainEntry, DomainEntryOutput]


class DomainValidationRecord(BaseValidatorModel):
    domainName: Optional[str] = None
    resourceRecord: Optional[ResourceRecord] = None
    dnsRecordCreationState: Optional[DnsRecordCreationState] = None
    validationStatus: Optional[CertificateDomainValidationStatusType] = None


class EstimateByTime(BaseValidatorModel):
    usageCost: Optional[float] = None
    pricingUnit: Optional[PricingUnitType] = None
    unit: Optional[float] = None
    currency: Optional[Literal['USD']] = None
    timePeriod: Optional[TimePeriod] = None


class GetActiveNamesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBlueprintsRequestPaginate(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    appCategory: Optional[Literal['LfR']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetBundlesRequestPaginate(BaseValidatorModel):
    includeInactive: Optional[bool] = None
    appCategory: Optional[Literal['LfR']] = None
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


# This class is the output for the 'get_bucket_metric_data' function.
class GetBucketMetricDataResult(BaseValidatorModel):
    metricName: BucketMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_container_service_metric_data' function.
class GetContainerServiceMetricDataResult(BaseValidatorModel):
    metricName: ContainerServiceMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_distribution_metric_data' function.
class GetDistributionMetricDataResult(BaseValidatorModel):
    metricName: DistributionMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_metric_data' function.
class GetInstanceMetricDataResult(BaseValidatorModel):
    metricName: InstanceMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_load_balancer_metric_data' function.
class GetLoadBalancerMetricDataResult(BaseValidatorModel):
    metricName: LoadBalancerMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_metric_data' function.
class GetRelationalDatabaseMetricDataResult(BaseValidatorModel):
    metricName: RelationalDatabaseMetricNameType
    metricData: List[MetricDatapoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_port_states' function.
class GetInstancePortStatesResult(BaseValidatorModel):
    portStates: List[InstancePortState]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_state' function.
class GetInstanceStateResult(BaseValidatorModel):
    state: InstanceState
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_load_balancer_tls_policies' function.
class GetLoadBalancerTlsPoliciesResult(BaseValidatorModel):
    tlsPolicies: List[LoadBalancerTlsPolicy]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_blueprints' function.
class GetRelationalDatabaseBlueprintsResult(BaseValidatorModel):
    blueprints: List[RelationalDatabaseBlueprint]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_bundles' function.
class GetRelationalDatabaseBundlesResult(BaseValidatorModel):
    bundles: List[RelationalDatabaseBundle]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_events' function.
class GetRelationalDatabaseEventsResult(BaseValidatorModel):
    relationalDatabaseEvents: List[RelationalDatabaseEvent]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_log_events' function.
class GetRelationalDatabaseLogEventsResult(BaseValidatorModel):
    resourceLogEvents: List[LogEvent]
    nextBackwardToken: str
    nextForwardToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_parameters' function.
class GetRelationalDatabaseParametersResult(BaseValidatorModel):
    parameters: List[RelationalDatabaseParameter]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_relational_database_parameters' function.
class UpdateRelationalDatabaseParametersRequest(BaseValidatorModel):
    relationalDatabaseName: str
    parameters: List[RelationalDatabaseParameter]


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


class LoadBalancerTlsCertificateDomainValidationRecord(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    validationStatus: Optional[LoadBalancerTlsCertificateDomainStatusType] = None
    domainName: Optional[str] = None
    dnsRecordCreationState: Optional[LoadBalancerTlsCertificateDnsRecordCreationState] = None


class LoadBalancerTlsCertificateRenewalSummary(BaseValidatorModel):
    renewalStatus: Optional[LoadBalancerTlsCertificateRenewalStatusType] = None
    domainValidationOptions: Optional[List[LoadBalancerTlsCertificateDomainValidationOption]] = None


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


# This class is the output for the 'get_bucket_access_keys' function.
class GetBucketAccessKeysResult(BaseValidatorModel):
    accessKeys: List[AccessKey]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_disk_from_snapshot' function.
class CreateDiskFromSnapshotRequest(BaseValidatorModel):
    diskName: str
    availabilityZone: str
    sizeInGb: int
    diskSnapshotName: Optional[str] = None
    tags: Optional[List[Tag]] = None
    addOns: Optional[List[AddOnRequest]] = None
    sourceDiskName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None


# This class is the input for the 'create_disk' function.
class CreateDiskRequest(BaseValidatorModel):
    diskName: str
    availabilityZone: str
    sizeInGb: int
    tags: Optional[List[Tag]] = None
    addOns: Optional[List[AddOnRequest]] = None


# This class is the input for the 'create_instances_from_snapshot' function.
class CreateInstancesFromSnapshotRequest(BaseValidatorModel):
    instanceNames: List[str]
    availabilityZone: str
    bundleId: str
    attachedDiskMapping: Optional[Dict[str, List[DiskMap]]] = None
    instanceSnapshotName: Optional[str] = None
    userData: Optional[str] = None
    keyPairName: Optional[str] = None
    tags: Optional[List[Tag]] = None
    addOns: Optional[List[AddOnRequest]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    sourceInstanceName: Optional[str] = None
    restoreDate: Optional[str] = None
    useLatestRestorableAutoSnapshot: Optional[bool] = None


# This class is the input for the 'create_instances' function.
class CreateInstancesRequest(BaseValidatorModel):
    instanceNames: List[str]
    availabilityZone: str
    blueprintId: str
    bundleId: str
    customImageName: Optional[str] = None
    userData: Optional[str] = None
    keyPairName: Optional[str] = None
    tags: Optional[List[Tag]] = None
    addOns: Optional[List[AddOnRequest]] = None
    ipAddressType: Optional[IpAddressTypeType] = None


# This class is the input for the 'enable_add_on' function.
class EnableAddOnRequest(BaseValidatorModel):
    resourceName: str
    addOnRequest: AddOnRequest


# This class is the output for the 'get_alarms' function.
class GetAlarmsResult(BaseValidatorModel):
    alarms: List[Alarm]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_contact_methods' function.
class GetContactMethodsResult(BaseValidatorModel):
    contactMethods: List[ContactMethod]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'allocate_static_ip' function.
class AllocateStaticIpResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_certificate_to_distribution' function.
class AttachCertificateToDistributionResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_disk' function.
class AttachDiskResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_instances_to_load_balancer' function.
class AttachInstancesToLoadBalancerResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_load_balancer_tls_certificate' function.
class AttachLoadBalancerTlsCertificateResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_static_ip' function.
class AttachStaticIpResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'close_instance_public_ports' function.
class CloseInstancePublicPortsResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_snapshot' function.
class CopySnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_bucket_access_key' function.
class CreateBucketAccessKeyResult(BaseValidatorModel):
    accessKey: AccessKey
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cloud_formation_stack' function.
class CreateCloudFormationStackResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_contact_method' function.
class CreateContactMethodResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_disk_from_snapshot' function.
class CreateDiskFromSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_disk' function.
class CreateDiskResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_disk_snapshot' function.
class CreateDiskSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_domain_entry' function.
class CreateDomainEntryResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_domain' function.
class CreateDomainResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_instance_snapshot' function.
class CreateInstanceSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_instances_from_snapshot' function.
class CreateInstancesFromSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_instances' function.
class CreateInstancesResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_load_balancer' function.
class CreateLoadBalancerResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_load_balancer_tls_certificate' function.
class CreateLoadBalancerTlsCertificateResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_relational_database_from_snapshot' function.
class CreateRelationalDatabaseFromSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_relational_database' function.
class CreateRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_relational_database_snapshot' function.
class CreateRelationalDatabaseSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_alarm' function.
class DeleteAlarmResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_auto_snapshot' function.
class DeleteAutoSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bucket_access_key' function.
class DeleteBucketAccessKeyResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bucket' function.
class DeleteBucketResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_certificate' function.
class DeleteCertificateResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_contact_method' function.
class DeleteContactMethodResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_disk' function.
class DeleteDiskResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_disk_snapshot' function.
class DeleteDiskSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_distribution' function.
class DeleteDistributionResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_domain_entry' function.
class DeleteDomainEntryResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_domain' function.
class DeleteDomainResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_instance' function.
class DeleteInstanceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_instance_snapshot' function.
class DeleteInstanceSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_key_pair' function.
class DeleteKeyPairResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_known_host_keys' function.
class DeleteKnownHostKeysResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_load_balancer' function.
class DeleteLoadBalancerResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_load_balancer_tls_certificate' function.
class DeleteLoadBalancerTlsCertificateResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_relational_database' function.
class DeleteRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_relational_database_snapshot' function.
class DeleteRelationalDatabaseSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_certificate_from_distribution' function.
class DetachCertificateFromDistributionResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_disk' function.
class DetachDiskResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_instances_from_load_balancer' function.
class DetachInstancesFromLoadBalancerResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_static_ip' function.
class DetachStaticIpResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_add_on' function.
class DisableAddOnResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_add_on' function.
class EnableAddOnResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_snapshot' function.
class ExportSnapshotResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_operation' function.
class GetOperationResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_operations_for_resource' function.
class GetOperationsForResourceResult(BaseValidatorModel):
    operations: List[Operation]
    nextPageCount: str
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_operations' function.
class GetOperationsResult(BaseValidatorModel):
    operations: List[Operation]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_key_pair' function.
class ImportKeyPairResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'open_instance_public_ports' function.
class OpenInstancePublicPortsResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


class PeerVpcResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_alarm' function.
class PutAlarmResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_instance_public_ports' function.
class PutInstancePublicPortsResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reboot_instance' function.
class RebootInstanceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reboot_relational_database' function.
class RebootRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'release_static_ip' function.
class ReleaseStaticIpResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_distribution_cache' function.
class ResetDistributionCacheResult(BaseValidatorModel):
    status: str
    createTime: datetime
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_contact_method_verification' function.
class SendContactMethodVerificationResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_ip_address_type' function.
class SetIpAddressTypeResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_resource_access_for_bucket' function.
class SetResourceAccessForBucketResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'setup_instance_https' function.
class SetupInstanceHttpsResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_gui_session' function.
class StartGUISessionResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_instance' function.
class StartInstanceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_relational_database' function.
class StartRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_gui_session' function.
class StopGUISessionResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_instance' function.
class StopInstanceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_relational_database' function.
class StopRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'tag_resource' function.
class TagResourceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_alarm' function.
class TestAlarmResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class UnpeerVpcResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class UntagResourceResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bucket_bundle' function.
class UpdateBucketBundleResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_distribution_bundle' function.
class UpdateDistributionBundleResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_distribution' function.
class UpdateDistributionResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_entry' function.
class UpdateDomainEntryResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_instance_metadata_options' function.
class UpdateInstanceMetadataOptionsResult(BaseValidatorModel):
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_load_balancer_attribute' function.
class UpdateLoadBalancerAttributeResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_relational_database_parameters' function.
class UpdateRelationalDatabaseParametersResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_relational_database' function.
class UpdateRelationalDatabaseResult(BaseValidatorModel):
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


class SetupHistory(BaseValidatorModel):
    operationId: Optional[str] = None
    request: Optional[SetupRequest] = None
    resource: Optional[SetupHistoryResource] = None
    executionDetails: Optional[List[SetupExecutionDetails]] = None
    status: Optional[SetupStatusType] = None


# This class is the output for the 'get_static_ip' function.
class GetStaticIpResult(BaseValidatorModel):
    staticIp: StaticIp
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_static_ips' function.
class GetStaticIpsResult(BaseValidatorModel):
    staticIps: List[StaticIp]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_auto_snapshots' function.
class GetAutoSnapshotsResult(BaseValidatorModel):
    resourceName: str
    resourceType: ResourceTypeType
    autoSnapshots: List[AutoSnapshotDetails]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_regions' function.
class GetRegionsResult(BaseValidatorModel):
    regions: List[Region]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_bucket' function.
class CreateBucketResult(BaseValidatorModel):
    bucket: Bucket
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_buckets' function.
class GetBucketsResult(BaseValidatorModel):
    buckets: List[Bucket]
    nextPageToken: str
    accountLevelBpaSync: AccountLevelBpaSync
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bucket' function.
class UpdateBucketResult(BaseValidatorModel):
    bucket: Bucket
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_disk_snapshot' function.
class GetDiskSnapshotResult(BaseValidatorModel):
    diskSnapshot: DiskSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_disk_snapshots' function.
class GetDiskSnapshotsResult(BaseValidatorModel):
    diskSnapshots: List[DiskSnapshot]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_disk' function.
class GetDiskResult(BaseValidatorModel):
    disk: Disk
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_disks' function.
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


# This class is the output for the 'create_key_pair' function.
class CreateKeyPairResult(BaseValidatorModel):
    keyPair: KeyPair
    publicKeyBase64: str
    privateKeyBase64: str
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_key_pair' function.
class GetKeyPairResult(BaseValidatorModel):
    keyPair: KeyPair
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_key_pairs' function.
class GetKeyPairsResult(BaseValidatorModel):
    keyPairs: List[KeyPair]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_snapshot' function.
class GetRelationalDatabaseSnapshotResult(BaseValidatorModel):
    relationalDatabaseSnapshot: RelationalDatabaseSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_database_snapshots' function.
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

CacheSettingsUnion = Union[CacheSettings, CacheSettingsOutput]


# This class is the output for the 'get_cloud_formation_stack_records' function.
class GetCloudFormationStackRecordsResult(BaseValidatorModel):
    cloudFormationStackRecords: List[CloudFormationStackRecord]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_container_service' function.
class UpdateContainerServiceRequest(BaseValidatorModel):
    serviceName: str
    power: Optional[ContainerServicePowerNameType] = None
    scale: Optional[int] = None
    isDisabled: Optional[bool] = None
    publicDomainNames: Optional[Dict[str, List[str]]] = None
    privateRegistryAccess: Optional[PrivateRegistryAccessRequest] = None


class ContainerServiceDeployment(BaseValidatorModel):
    version: Optional[int] = None
    state: Optional[ContainerServiceDeploymentStateType] = None
    containers: Optional[Dict[str, ContainerOutput]] = None
    publicEndpoint: Optional[ContainerServiceEndpoint] = None
    createdAt: Optional[datetime] = None


class ContainerServiceDeploymentRequest(BaseValidatorModel):
    containers: Optional[Dict[str, ContainerUnion]] = None
    publicEndpoint: Optional[EndpointRequest] = None


# This class is the input for the 'create_container_service_deployment' function.
class CreateContainerServiceDeploymentRequest(BaseValidatorModel):
    serviceName: str
    containers: Optional[Dict[str, ContainerUnion]] = None
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


# This class is the input for the 'create_domain_entry' function.
class CreateDomainEntryRequest(BaseValidatorModel):
    domainName: str
    domainEntry: DomainEntryUnion


# This class is the input for the 'delete_domain_entry' function.
class DeleteDomainEntryRequest(BaseValidatorModel):
    domainName: str
    domainEntry: DomainEntryUnion


# This class is the input for the 'update_domain_entry' function.
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


# This class is the output for the 'get_instance_access_details' function.
class GetInstanceAccessDetailsResult(BaseValidatorModel):
    accessDetails: InstanceAccessDetails
    ResponseMetadata: ResponseMetadata


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
    domainValidationRecords: Optional[List[LoadBalancerTlsCertificateDomainValidationRecord]] = None
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


# This class is the output for the 'get_load_balancer' function.
class GetLoadBalancerResult(BaseValidatorModel):
    loadBalancer: LoadBalancer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_load_balancers' function.
class GetLoadBalancersResult(BaseValidatorModel):
    loadBalancers: List[LoadBalancer]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


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


# This class is the output for the 'get_relational_database' function.
class GetRelationalDatabaseResult(BaseValidatorModel):
    relationalDatabase: RelationalDatabase
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_relational_databases' function.
class GetRelationalDatabasesResult(BaseValidatorModel):
    relationalDatabases: List[RelationalDatabase]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_setup_history' function.
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


# This class is the output for the 'get_instance_snapshot' function.
class GetInstanceSnapshotResult(BaseValidatorModel):
    instanceSnapshot: InstanceSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_snapshots' function.
class GetInstanceSnapshotsResult(BaseValidatorModel):
    instanceSnapshots: List[InstanceSnapshot]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_distribution' function.
class CreateDistributionResult(BaseValidatorModel):
    distribution: LightsailDistribution
    operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_distributions' function.
class GetDistributionsResult(BaseValidatorModel):
    distributions: List[LightsailDistribution]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_distribution' function.
class CreateDistributionRequest(BaseValidatorModel):
    distributionName: str
    origin: InputOrigin
    defaultCacheBehavior: CacheBehavior
    bundleId: str
    cacheBehaviorSettings: Optional[CacheSettingsUnion] = None
    cacheBehaviors: Optional[List[CacheBehaviorPerPath]] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    tags: Optional[List[Tag]] = None
    certificateName: Optional[str] = None
    viewerMinimumTlsProtocolVersion: Optional[ViewerMinimumTlsProtocolVersionEnumType] = None


# This class is the input for the 'update_distribution' function.
class UpdateDistributionRequest(BaseValidatorModel):
    distributionName: str
    origin: Optional[InputOrigin] = None
    defaultCacheBehavior: Optional[CacheBehavior] = None
    cacheBehaviorSettings: Optional[CacheSettingsUnion] = None
    cacheBehaviors: Optional[List[CacheBehaviorPerPath]] = None
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


# This class is the output for the 'get_container_service_deployments' function.
class GetContainerServiceDeploymentsResult(BaseValidatorModel):
    deployments: List[ContainerServiceDeployment]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_container_service' function.
class CreateContainerServiceRequest(BaseValidatorModel):
    serviceName: str
    power: ContainerServicePowerNameType
    scale: int
    tags: Optional[List[Tag]] = None
    publicDomainNames: Optional[Dict[str, List[str]]] = None
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


# This class is the output for the 'get_load_balancer_tls_certificates' function.
class GetLoadBalancerTlsCertificatesResult(BaseValidatorModel):
    tlsCertificates: List[LoadBalancerTlsCertificate]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain' function.
class GetDomainResult(BaseValidatorModel):
    domain: Domain
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domains' function.
class GetDomainsResult(BaseValidatorModel):
    domains: List[Domain]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance' function.
class GetInstanceResult(BaseValidatorModel):
    instance: Instance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instances' function.
class GetInstancesResult(BaseValidatorModel):
    instances: List[Instance]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_container_services' function.
class ContainerServicesListResult(BaseValidatorModel):
    containerServices: List[ContainerService]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_container_service_deployment' function.
class CreateContainerServiceDeploymentResult(BaseValidatorModel):
    containerService: ContainerService
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_container_service' function.
class CreateContainerServiceResult(BaseValidatorModel):
    containerService: ContainerService
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_container_service' function.
class UpdateContainerServiceResult(BaseValidatorModel):
    containerService: ContainerService
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_export_snapshot_records' function.
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


# This class is the output for the 'get_cost_estimate' function.
class GetCostEstimateResult(BaseValidatorModel):
    resourcesBudgetEstimate: List[ResourceBudgetEstimate]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_certificate' function.
class CreateCertificateResult(BaseValidatorModel):
    certificate: CertificateSummary
    operations: List[Operation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_certificates' function.
class GetCertificatesResult(BaseValidatorModel):
    certificates: List[CertificateSummary]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata
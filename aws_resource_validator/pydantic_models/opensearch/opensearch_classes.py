from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.opensearch.opensearch_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class NaturalLanguageQueryGenerationOptionsInput(BaseValidatorModel):
    DesiredState: Optional[NaturalLanguageQueryGenerationDesiredStateType] = None


class NaturalLanguageQueryGenerationOptionsOutput(BaseValidatorModel):
    DesiredState: Optional[NaturalLanguageQueryGenerationDesiredStateType] = None
    CurrentState: Optional[NaturalLanguageQueryGenerationCurrentStateType] = None


class OptionStatus(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None


class AWSDomainInformation(BaseValidatorModel):
    DomainName: str
    OwnerId: Optional[str] = None
    Region: Optional[str] = None


# This class is the input for the 'accept_inbound_connection' function.
class AcceptInboundConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class AdditionalLimit(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


class JWTOptionsInput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    PublicKey: Optional[str] = None


class MasterUserOptions(BaseValidatorModel):
    MasterUserARN: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None


class JWTOptionsOutput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    PublicKey: Optional[str] = None


class AppConfig(BaseValidatorModel):
    key: Optional[AppConfigTypeType] = None
    value: Optional[str] = None


class ApplicationSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    endpoint: Optional[str] = None
    status: Optional[ApplicationStatusType] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None


# This class is the input for the 'authorize_vpc_endpoint_access' function.
class AuthorizeVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    Account: Optional[str] = None
    Service: Optional[Literal['application.opensearchservice.amazonaws.com']] = None


class AuthorizedPrincipal(BaseValidatorModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None


class ScheduledAutoTuneDetails(BaseValidatorModel):
    Date: Optional[datetime] = None
    ActionType: Optional[ScheduledAutoTuneActionTypeType] = None
    Action: Optional[str] = None
    Severity: Optional[ScheduledAutoTuneSeverityTypeType] = None


class Duration(BaseValidatorModel):
    Value: Optional[int] = None
    Unit: Optional[Literal['HOURS']] = None

Timestamp = Union[datetime, str]


class AutoTuneOptionsOutput(BaseValidatorModel):
    State: Optional[AutoTuneStateType] = None
    ErrorMessage: Optional[str] = None
    UseOffPeakWindow: Optional[bool] = None


class AutoTuneStatus(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: Optional[int] = None
    ErrorMessage: Optional[str] = None
    PendingDeletion: Optional[bool] = None


class AvailabilityZoneInfo(BaseValidatorModel):
    AvailabilityZoneName: Optional[str] = None
    ZoneStatus: Optional[ZoneStatusType] = None
    ConfiguredDataNodeCount: Optional[str] = None
    AvailableDataNodeCount: Optional[str] = None
    TotalShards: Optional[str] = None
    TotalUnAssignedShards: Optional[str] = None


# This class is the input for the 'cancel_domain_config_change' function.
class CancelDomainConfigChangeRequest(BaseValidatorModel):
    DomainName: str
    DryRun: Optional[bool] = None


class CancelledChangeProperty(BaseValidatorModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None


# This class is the input for the 'cancel_service_software_update' function.
class CancelServiceSoftwareUpdateRequest(BaseValidatorModel):
    DomainName: str


class ServiceSoftwareOptions(BaseValidatorModel):
    CurrentVersion: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    Cancellable: Optional[bool] = None
    UpdateStatus: Optional[DeploymentStatusType] = None
    Description: Optional[str] = None
    AutomatedUpdateDate: Optional[datetime] = None
    OptionalDeployment: Optional[bool] = None


class ChangeProgressDetails(BaseValidatorModel):
    ChangeId: Optional[str] = None
    Message: Optional[str] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    InitiatedBy: Optional[InitiatedByType] = None
    StartTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class ChangeProgressStage(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None


class CloudWatchDirectQueryDataSource(BaseValidatorModel):
    RoleArn: str


class ColdStorageOptions(BaseValidatorModel):
    Enabled: bool


class ZoneAwarenessConfig(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None


class CognitoOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    UserPoolId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    RoleArn: Optional[str] = None


class CompatibleVersionsMap(BaseValidatorModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None


class CrossClusterSearchConnectionProperties(BaseValidatorModel):
    SkipUnavailable: Optional[SkipUnavailableStatusType] = None


class DataSource(BaseValidatorModel):
    dataSourceArn: Optional[str] = None
    dataSourceDescription: Optional[str] = None


class IamIdentityCenterOptionsInput(BaseValidatorModel):
    enabled: Optional[bool] = None
    iamIdentityCenterInstanceArn: Optional[str] = None
    iamRoleForIdentityCenterApplicationArn: Optional[str] = None


class IamIdentityCenterOptions(BaseValidatorModel):
    enabled: Optional[bool] = None
    iamIdentityCenterInstanceArn: Optional[str] = None
    iamRoleForIdentityCenterApplicationArn: Optional[str] = None
    iamIdentityCenterApplicationArn: Optional[str] = None


class DomainEndpointOptions(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[TLSSecurityPolicyType] = None
    CustomEndpointEnabled: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    CustomEndpointCertificateArn: Optional[str] = None


class EBSOptions(BaseValidatorModel):
    EBSEnabled: Optional[bool] = None
    VolumeType: Optional[VolumeTypeType] = None
    VolumeSize: Optional[int] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None


class EncryptionAtRestOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None


class IdentityCenterOptionsInput(BaseValidatorModel):
    EnabledAPIAccess: Optional[bool] = None
    IdentityCenterInstanceARN: Optional[str] = None
    SubjectKey: Optional[SubjectKeyIdCOptionType] = None
    RolesKey: Optional[RolesKeyIdCOptionType] = None


class LogPublishingOption(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None


class NodeToNodeEncryptionOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None


class SnapshotOptions(BaseValidatorModel):
    AutomatedSnapshotStartHour: Optional[int] = None


class SoftwareUpdateOptions(BaseValidatorModel):
    AutoSoftwareUpdateEnabled: Optional[bool] = None


class VPCOptions(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class OutboundConnectionStatus(BaseValidatorModel):
    StatusCode: Optional[OutboundConnectionStatusCodeType] = None
    Message: Optional[str] = None


class PackageConfiguration(BaseValidatorModel):
    LicenseRequirement: RequirementLevelType
    ConfigurationRequirement: RequirementLevelType
    LicenseFilepath: Optional[str] = None
    RequiresRestartForConfigurationUpdate: Optional[bool] = None


class PackageEncryptionOptions(BaseValidatorModel):
    EncryptionEnabled: bool
    KmsKeyIdentifier: Optional[str] = None


class PackageSource(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Key: Optional[str] = None


class PackageVendingOptions(BaseValidatorModel):
    VendingEnabled: bool


class S3GlueDataCatalog(BaseValidatorModel):
    RoleArn: Optional[str] = None


class DeleteApplicationRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_data_source' function.
class DeleteDataSourceRequest(BaseValidatorModel):
    DomainName: str
    Name: str


# This class is the input for the 'delete_direct_query_data_source' function.
class DeleteDirectQueryDataSourceRequest(BaseValidatorModel):
    DataSourceName: str


# This class is the input for the 'delete_domain' function.
class DeleteDomainRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'delete_inbound_connection' function.
class DeleteInboundConnectionRequest(BaseValidatorModel):
    ConnectionId: str


# This class is the input for the 'delete_outbound_connection' function.
class DeleteOutboundConnectionRequest(BaseValidatorModel):
    ConnectionId: str


# This class is the input for the 'delete_package' function.
class DeletePackageRequest(BaseValidatorModel):
    PackageID: str


# This class is the input for the 'delete_vpc_endpoint' function.
class DeleteVpcEndpointRequest(BaseValidatorModel):
    VpcEndpointId: str


class VpcEndpointSummary(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    Status: Optional[VpcEndpointStatusType] = None


# This class is the input for the 'describe_domain_auto_tunes' function.
class DescribeDomainAutoTunesRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_domain_change_progress' function.
class DescribeDomainChangeProgressRequest(BaseValidatorModel):
    DomainName: str
    ChangeId: Optional[str] = None


# This class is the input for the 'describe_domain_config' function.
class DescribeDomainConfigRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'describe_domain_health' function.
class DescribeDomainHealthRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'describe_domain_nodes' function.
class DescribeDomainNodesRequest(BaseValidatorModel):
    DomainName: str


class DomainNodesStatus(BaseValidatorModel):
    NodeId: Optional[str] = None
    NodeType: Optional[NodeTypeType] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    NodeStatus: Optional[NodeStatusType] = None
    StorageType: Optional[str] = None
    StorageVolumeType: Optional[VolumeTypeType] = None
    StorageSize: Optional[str] = None


# This class is the input for the 'describe_domain' function.
class DescribeDomainRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'describe_domains' function.
class DescribeDomainsRequest(BaseValidatorModel):
    DomainNames: List[str]


# This class is the input for the 'describe_dry_run_progress' function.
class DescribeDryRunProgressRequest(BaseValidatorModel):
    DomainName: str
    DryRunId: Optional[str] = None
    LoadDryRunConfig: Optional[bool] = None


class DryRunResults(BaseValidatorModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[List[str]] = None


# This class is the input for the 'describe_instance_type_limits' function.
class DescribeInstanceTypeLimitsRequest(BaseValidatorModel):
    InstanceType: OpenSearchPartitionInstanceTypeType
    EngineVersion: str
    DomainName: Optional[str] = None


class DescribePackagesFilter(BaseValidatorModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[List[str]] = None


# This class is the input for the 'describe_reserved_instance_offerings' function.
class DescribeReservedInstanceOfferingsRequest(BaseValidatorModel):
    ReservedInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_reserved_instances' function.
class DescribeReservedInstancesRequest(BaseValidatorModel):
    ReservedInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_vpc_endpoints' function.
class DescribeVpcEndpointsRequest(BaseValidatorModel):
    VpcEndpointIds: List[str]


class VpcEndpointError(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    ErrorCode: Optional[VpcEndpointErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class SecurityLakeDirectQueryDataSource(BaseValidatorModel):
    RoleArn: str


# This class is the input for the 'dissociate_package' function.
class DissociatePackageRequest(BaseValidatorModel):
    PackageID: str
    DomainName: str


# This class is the input for the 'dissociate_packages' function.
class DissociatePackagesRequest(BaseValidatorModel):
    PackageList: List[str]
    DomainName: str


class ModifyingProperties(BaseValidatorModel):
    Name: Optional[str] = None
    ActiveValue: Optional[str] = None
    PendingValue: Optional[str] = None
    ValueType: Optional[PropertyValueTypeType] = None


class DomainInfo(BaseValidatorModel):
    DomainName: Optional[str] = None
    EngineType: Optional[EngineTypeType] = None


class DomainMaintenanceDetails(BaseValidatorModel):
    MaintenanceId: Optional[str] = None
    DomainName: Optional[str] = None
    Action: Optional[MaintenanceTypeType] = None
    NodeId: Optional[str] = None
    Status: Optional[MaintenanceStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class ErrorDetails(BaseValidatorModel):
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None


class IdentityCenterOptions(BaseValidatorModel):
    EnabledAPIAccess: Optional[bool] = None
    IdentityCenterInstanceARN: Optional[str] = None
    SubjectKey: Optional[SubjectKeyIdCOptionType] = None
    RolesKey: Optional[RolesKeyIdCOptionType] = None
    IdentityCenterApplicationARN: Optional[str] = None
    IdentityStoreId: Optional[str] = None


class VPCDerivedInfo(BaseValidatorModel):
    VPCId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class ValidationFailure(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


# This class is the input for the 'get_application' function.
class GetApplicationRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_compatible_versions' function.
class GetCompatibleVersionsRequest(BaseValidatorModel):
    DomainName: Optional[str] = None


# This class is the input for the 'get_data_source' function.
class GetDataSourceRequest(BaseValidatorModel):
    DomainName: str
    Name: str


# This class is the input for the 'get_direct_query_data_source' function.
class GetDirectQueryDataSourceRequest(BaseValidatorModel):
    DataSourceName: str


# This class is the input for the 'get_domain_maintenance_status' function.
class GetDomainMaintenanceStatusRequest(BaseValidatorModel):
    DomainName: str
    MaintenanceId: str


# This class is the input for the 'get_package_version_history' function.
class GetPackageVersionHistoryRequest(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_upgrade_history' function.
class GetUpgradeHistoryRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_upgrade_status' function.
class GetUpgradeStatusRequest(BaseValidatorModel):
    DomainName: str


class InboundConnectionStatus(BaseValidatorModel):
    StatusCode: Optional[InboundConnectionStatusCodeType] = None
    Message: Optional[str] = None


class InstanceCountLimits(BaseValidatorModel):
    MinimumInstanceCount: Optional[int] = None
    MaximumInstanceCount: Optional[int] = None


class InstanceTypeDetails(BaseValidatorModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    EncryptionEnabled: Optional[bool] = None
    CognitoEnabled: Optional[bool] = None
    AppLogsEnabled: Optional[bool] = None
    AdvancedSecurityEnabled: Optional[bool] = None
    WarmEnabled: Optional[bool] = None
    InstanceRole: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None


class KeyStoreAccessOption(BaseValidatorModel):
    KeyStoreAccessEnabled: bool
    KeyAccessRoleArn: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    statuses: Optional[List[ApplicationStatusType]] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_data_sources' function.
class ListDataSourcesRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'list_direct_query_data_sources' function.
class ListDirectQueryDataSourcesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'list_domain_maintenances' function.
class ListDomainMaintenancesRequest(BaseValidatorModel):
    DomainName: str
    Action: Optional[MaintenanceTypeType] = None
    Status: Optional[MaintenanceStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_domain_names' function.
class ListDomainNamesRequest(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None


# This class is the input for the 'list_domains_for_package' function.
class ListDomainsForPackageRequest(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_instance_type_details' function.
class ListInstanceTypeDetailsRequest(BaseValidatorModel):
    EngineVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RetrieveAZs: Optional[bool] = None
    InstanceType: Optional[str] = None


# This class is the input for the 'list_packages_for_domain' function.
class ListPackagesForDomainRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_scheduled_actions' function.
class ListScheduledActionsRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ScheduledAction(BaseValidatorModel):
    Id: str
    Type: ActionTypeType
    Severity: ActionSeverityType
    ScheduledTime: int
    Description: Optional[str] = None
    ScheduledBy: Optional[ScheduledByType] = None
    Status: Optional[ActionStatusType] = None
    Mandatory: Optional[bool] = None
    Cancellable: Optional[bool] = None


# This class is the input for the 'list_tags' function.
class ListTagsRequest(BaseValidatorModel):
    ARN: str


# This class is the input for the 'list_versions' function.
class ListVersionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_vpc_endpoint_access' function.
class ListVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_vpc_endpoints_for_domain' function.
class ListVpcEndpointsForDomainRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_vpc_endpoints' function.
class ListVpcEndpointsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class NodeConfig(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Type: Optional[OpenSearchPartitionInstanceTypeType] = None
    Count: Optional[int] = None


class WindowStartTime(BaseValidatorModel):
    Hours: int
    Minutes: int


class PluginProperties(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    ClassName: Optional[str] = None
    UncompressedSizeInBytes: Optional[int] = None


# This class is the input for the 'purchase_reserved_instance_offering' function.
class PurchaseReservedInstanceOfferingRequest(BaseValidatorModel):
    ReservedInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


# This class is the input for the 'reject_inbound_connection' function.
class RejectInboundConnectionRequest(BaseValidatorModel):
    ConnectionId: str


# This class is the input for the 'remove_tags' function.
class RemoveTagsRequest(BaseValidatorModel):
    ARN: str
    TagKeys: List[str]


class RevokeVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    Account: Optional[str] = None
    Service: Optional[Literal['application.opensearchservice.amazonaws.com']] = None


class SAMLIdp(BaseValidatorModel):
    MetadataContent: str
    EntityId: str


# This class is the input for the 'start_domain_maintenance' function.
class StartDomainMaintenanceRequest(BaseValidatorModel):
    DomainName: str
    Action: MaintenanceTypeType
    NodeId: Optional[str] = None


# This class is the input for the 'start_service_software_update' function.
class StartServiceSoftwareUpdateRequest(BaseValidatorModel):
    DomainName: str
    ScheduleAt: Optional[ScheduleAtType] = None
    DesiredStartTime: Optional[int] = None


class StorageTypeLimit(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


# This class is the input for the 'update_package_scope' function.
class UpdatePackageScopeRequest(BaseValidatorModel):
    PackageID: str
    Operation: PackageScopeOperationEnumType
    PackageUserList: List[str]


# This class is the input for the 'update_scheduled_action' function.
class UpdateScheduledActionRequest(BaseValidatorModel):
    DomainName: str
    ActionID: str
    ActionType: ActionTypeType
    ScheduleAt: ScheduleAtType
    DesiredStartTime: Optional[int] = None


# This class is the input for the 'upgrade_domain' function.
class UpgradeDomainRequest(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None
    AdvancedOptions: Optional[Dict[str, str]] = None


class UpgradeStepItem(BaseValidatorModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None


class AIMLOptionsInput(BaseValidatorModel):
    NaturalLanguageQueryGenerationOptions: Optional[NaturalLanguageQueryGenerationOptionsInput] = None


class AIMLOptionsOutput(BaseValidatorModel):
    NaturalLanguageQueryGenerationOptions: Optional[NaturalLanguageQueryGenerationOptionsOutput] = None


class AccessPoliciesStatus(BaseValidatorModel):
    Options: str
    Status: OptionStatus


class AdvancedOptionsStatus(BaseValidatorModel):
    Options: Dict[str, str]
    Status: OptionStatus


class IPAddressTypeStatus(BaseValidatorModel):
    Options: IPAddressTypeType
    Status: OptionStatus


class VersionStatus(BaseValidatorModel):
    Options: str
    Status: OptionStatus


class DomainInformationContainer(BaseValidatorModel):
    AWSDomainInformation: Optional[AWSDomainInformation] = None


# This class is the output for the 'add_data_source' function.
class AddDataSourceResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'add_direct_query_data_source' function.
class AddDirectQueryDataSourceResponse(BaseValidatorModel):
    DataSourceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_data_source' function.
class DeleteDataSourceResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_tags' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain_maintenance_status' function.
class GetDomainMaintenanceStatusResponse(BaseValidatorModel):
    Status: MaintenanceStatusType
    StatusMessage: str
    NodeId: str
    Action: MaintenanceTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_upgrade_status' function.
class GetUpgradeStatusResponse(BaseValidatorModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_versions' function.
class ListVersionsResponse(BaseValidatorModel):
    Versions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'purchase_reserved_instance_offering' function.
class PurchaseReservedInstanceOfferingResponse(BaseValidatorModel):
    ReservedInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_domain_maintenance' function.
class StartDomainMaintenanceResponse(BaseValidatorModel):
    MaintenanceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_data_source' function.
class UpdateDataSourceResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_direct_query_data_source' function.
class UpdateDirectQueryDataSourceResponse(BaseValidatorModel):
    DataSourceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_package_scope' function.
class UpdatePackageScopeResponse(BaseValidatorModel):
    PackageID: str
    Operation: PackageScopeOperationEnumType
    PackageUserList: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'add_tags' function.
class AddTagsRequest(BaseValidatorModel):
    ARN: str
    TagList: List[Tag]


# This class is the output for the 'list_tags' function.
class ListTagsResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_applications' function.
class ListApplicationsResponse(BaseValidatorModel):
    ApplicationSummaries: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'authorize_vpc_endpoint_access' function.
class AuthorizeVpcEndpointAccessResponse(BaseValidatorModel):
    AuthorizedPrincipal: AuthorizedPrincipal
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_vpc_endpoint_access' function.
class ListVpcEndpointAccessResponse(BaseValidatorModel):
    AuthorizedPrincipalList: List[AuthorizedPrincipal]
    NextToken: str
    ResponseMetadata: ResponseMetadata


class AutoTuneDetails(BaseValidatorModel):
    ScheduledAutoTuneDetails: Optional[ScheduledAutoTuneDetails] = None


class AutoTuneMaintenanceScheduleOutput(BaseValidatorModel):
    StartAt: Optional[datetime] = None
    Duration: Optional[Duration] = None
    CronExpressionForRecurrence: Optional[str] = None


class AutoTuneMaintenanceSchedule(BaseValidatorModel):
    StartAt: Optional[Timestamp] = None
    Duration: Optional[Duration] = None
    CronExpressionForRecurrence: Optional[str] = None


class EnvironmentInfo(BaseValidatorModel):
    AvailabilityZoneInformation: Optional[List[AvailabilityZoneInfo]] = None


# This class is the output for the 'cancel_domain_config_change' function.
class CancelDomainConfigChangeResponse(BaseValidatorModel):
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangeProperty]
    DryRun: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_service_software_update' function.
class CancelServiceSoftwareUpdateResponse(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptions
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_service_software_update' function.
class StartServiceSoftwareUpdateResponse(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptions
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upgrade_domain' function.
class UpgradeDomainResponse(BaseValidatorModel):
    UpgradeId: str
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
    AdvancedOptions: Dict[str, str]
    ChangeProgressDetails: ChangeProgressDetails
    ResponseMetadata: ResponseMetadata


class ChangeProgressStatusDetails(BaseValidatorModel):
    ChangeId: Optional[str] = None
    StartTime: Optional[datetime] = None
    Status: Optional[OverallChangeStatusType] = None
    PendingProperties: Optional[List[str]] = None
    CompletedProperties: Optional[List[str]] = None
    TotalNumberOfStages: Optional[int] = None
    ChangeProgressStages: Optional[List[ChangeProgressStage]] = None
    LastUpdatedTime: Optional[datetime] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    InitiatedBy: Optional[InitiatedByType] = None


class CognitoOptionsStatus(BaseValidatorModel):
    Options: CognitoOptions
    Status: OptionStatus


# This class is the output for the 'get_compatible_versions' function.
class GetCompatibleVersionsResponse(BaseValidatorModel):
    CompatibleVersions: List[CompatibleVersionsMap]
    ResponseMetadata: ResponseMetadata


class ConnectionProperties(BaseValidatorModel):
    Endpoint: Optional[str] = None
    CrossClusterSearch: Optional[CrossClusterSearchConnectionProperties] = None


# This class is the input for the 'update_application' function.
class UpdateApplicationRequest(BaseValidatorModel):
    id: str
    dataSources: Optional[List[DataSource]] = None
    appConfigs: Optional[List[AppConfig]] = None


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    dataSources: Optional[List[DataSource]] = None
    iamIdentityCenterOptions: Optional[IamIdentityCenterOptionsInput] = None
    appConfigs: Optional[List[AppConfig]] = None
    tagList: Optional[List[Tag]] = None


# This class is the output for the 'create_application' function.
class CreateApplicationResponse(BaseValidatorModel):
    id: str
    name: str
    arn: str
    dataSources: List[DataSource]
    iamIdentityCenterOptions: IamIdentityCenterOptions
    appConfigs: List[AppConfig]
    tagList: List[Tag]
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_application' function.
class GetApplicationResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    endpoint: str
    status: ApplicationStatusType
    iamIdentityCenterOptions: IamIdentityCenterOptions
    dataSources: List[DataSource]
    appConfigs: List[AppConfig]
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_application' function.
class UpdateApplicationResponse(BaseValidatorModel):
    id: str
    name: str
    arn: str
    dataSources: List[DataSource]
    iamIdentityCenterOptions: IamIdentityCenterOptions
    appConfigs: List[AppConfig]
    createdAt: datetime
    lastUpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class DomainEndpointOptionsStatus(BaseValidatorModel):
    Options: DomainEndpointOptions
    Status: OptionStatus


class EBSOptionsStatus(BaseValidatorModel):
    Options: EBSOptions
    Status: OptionStatus


class EncryptionAtRestOptionsStatus(BaseValidatorModel):
    Options: EncryptionAtRestOptions
    Status: OptionStatus


class LogPublishingOptionsStatus(BaseValidatorModel):
    Options: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    Status: Optional[OptionStatus] = None


class NodeToNodeEncryptionOptionsStatus(BaseValidatorModel):
    Options: NodeToNodeEncryptionOptions
    Status: OptionStatus


class SnapshotOptionsStatus(BaseValidatorModel):
    Options: SnapshotOptions
    Status: OptionStatus


class SoftwareUpdateOptionsStatus(BaseValidatorModel):
    Options: Optional[SoftwareUpdateOptions] = None
    Status: Optional[OptionStatus] = None


# This class is the input for the 'create_vpc_endpoint' function.
class CreateVpcEndpointRequest(BaseValidatorModel):
    DomainArn: str
    VpcOptions: VPCOptions
    ClientToken: Optional[str] = None


# This class is the input for the 'update_vpc_endpoint' function.
class UpdateVpcEndpointRequest(BaseValidatorModel):
    VpcEndpointId: str
    VpcOptions: VPCOptions


# This class is the input for the 'update_package' function.
class UpdatePackageRequest(BaseValidatorModel):
    PackageID: str
    PackageSource: PackageSource
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None
    PackageConfiguration: Optional[PackageConfiguration] = None
    PackageEncryptionOptions: Optional[PackageEncryptionOptions] = None


# This class is the input for the 'create_package' function.
class CreatePackageRequest(BaseValidatorModel):
    PackageName: str
    PackageType: PackageTypeType
    PackageSource: PackageSource
    PackageDescription: Optional[str] = None
    PackageConfiguration: Optional[PackageConfiguration] = None
    EngineVersion: Optional[str] = None
    PackageVendingOptions: Optional[PackageVendingOptions] = None
    PackageEncryptionOptions: Optional[PackageEncryptionOptions] = None


class DataSourceType(BaseValidatorModel):
    S3GlueDataCatalog: Optional[S3GlueDataCatalog] = None


# This class is the output for the 'delete_vpc_endpoint' function.
class DeleteVpcEndpointResponse(BaseValidatorModel):
    VpcEndpointSummary: VpcEndpointSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_vpc_endpoints_for_domain' function.
class ListVpcEndpointsForDomainResponse(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummary]
    NextToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_vpc_endpoints' function.
class ListVpcEndpointsResponse(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummary]
    NextToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domain_nodes' function.
class DescribeDomainNodesResponse(BaseValidatorModel):
    DomainNodesStatusList: List[DomainNodesStatus]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'describe_inbound_connections' function.
class DescribeInboundConnectionsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_outbound_connections' function.
class DescribeOutboundConnectionsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_packages' function.
class DescribePackagesRequest(BaseValidatorModel):
    Filters: Optional[List[DescribePackagesFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DirectQueryDataSourceType(BaseValidatorModel):
    CloudWatchLog: Optional[CloudWatchDirectQueryDataSource] = None
    SecurityLake: Optional[SecurityLakeDirectQueryDataSource] = None


# This class is the output for the 'list_domain_names' function.
class ListDomainNamesResponse(BaseValidatorModel):
    DomainNames: List[DomainInfo]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_domain_maintenances' function.
class ListDomainMaintenancesResponse(BaseValidatorModel):
    DomainMaintenances: List[DomainMaintenanceDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IdentityCenterOptionsStatus(BaseValidatorModel):
    Options: IdentityCenterOptions
    Status: OptionStatus


class VPCDerivedInfoStatus(BaseValidatorModel):
    Options: VPCDerivedInfo
    Status: OptionStatus


class VpcEndpoint(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    VpcOptions: Optional[VPCDerivedInfo] = None
    Status: Optional[VpcEndpointStatusType] = None
    Endpoint: Optional[str] = None


class DryRunProgressStatus(BaseValidatorModel):
    DryRunId: str
    DryRunStatus: str
    CreationDate: str
    UpdateDate: str
    ValidationFailures: Optional[List[ValidationFailure]] = None


class InstanceLimits(BaseValidatorModel):
    InstanceCountLimits: Optional[InstanceCountLimits] = None


# This class is the output for the 'list_instance_type_details' function.
class ListInstanceTypeDetailsResponse(BaseValidatorModel):
    InstanceTypeDetails: List[InstanceTypeDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PackageAssociationConfiguration(BaseValidatorModel):
    KeyStoreAccessOption: Optional[KeyStoreAccessOption] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    statuses: Optional[List[ApplicationStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_scheduled_actions' function.
class ListScheduledActionsResponse(BaseValidatorModel):
    ScheduledActions: List[ScheduledAction]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_scheduled_action' function.
class UpdateScheduledActionResponse(BaseValidatorModel):
    ScheduledAction: ScheduledAction
    ResponseMetadata: ResponseMetadata


class NodeOption(BaseValidatorModel):
    NodeType: Optional[Literal['coordinator']] = None
    NodeConfig: Optional[NodeConfig] = None


class OffPeakWindow(BaseValidatorModel):
    WindowStartTime: Optional[WindowStartTime] = None


class PackageDetails(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[PackageTypeType] = None
    PackageDescription: Optional[str] = None
    PackageStatus: Optional[PackageStatusType] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    AvailablePackageVersion: Optional[str] = None
    ErrorDetails: Optional[ErrorDetails] = None
    EngineVersion: Optional[str] = None
    AvailablePluginProperties: Optional[PluginProperties] = None
    AvailablePackageConfiguration: Optional[PackageConfiguration] = None
    AllowListedUserList: Optional[List[str]] = None
    PackageOwner: Optional[str] = None
    PackageVendingOptions: Optional[PackageVendingOptions] = None
    PackageEncryptionOptions: Optional[PackageEncryptionOptions] = None


class PackageVersionHistory(BaseValidatorModel):
    PackageVersion: Optional[str] = None
    CommitMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    PluginProperties: Optional[PluginProperties] = None
    PackageConfiguration: Optional[PackageConfiguration] = None


class ReservedInstanceOffering(BaseValidatorModel):
    ReservedInstanceOfferingId: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    PaymentOption: Optional[ReservedInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None


class ReservedInstance(BaseValidatorModel):
    ReservationName: Optional[str] = None
    ReservedInstanceId: Optional[str] = None
    BillingSubscriptionId: Optional[int] = None
    ReservedInstanceOfferingId: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    InstanceCount: Optional[int] = None
    State: Optional[str] = None
    PaymentOption: Optional[ReservedInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None


class SAMLOptionsInput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdp] = None
    MasterUserName: Optional[str] = None
    MasterBackendRole: Optional[str] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None


class SAMLOptionsOutput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdp] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None


class StorageType(BaseValidatorModel):
    StorageTypeName: Optional[str] = None
    StorageSubTypeName: Optional[str] = None
    StorageTypeLimits: Optional[List[StorageTypeLimit]] = None


class UpgradeHistory(BaseValidatorModel):
    UpgradeName: Optional[str] = None
    StartTimestamp: Optional[datetime] = None
    UpgradeStatus: Optional[UpgradeStatusType] = None
    StepsList: Optional[List[UpgradeStepItem]] = None


class AIMLOptionsStatus(BaseValidatorModel):
    Options: Optional[AIMLOptionsOutput] = None
    Status: Optional[OptionStatus] = None


class InboundConnection(BaseValidatorModel):
    LocalDomainInfo: Optional[DomainInformationContainer] = None
    RemoteDomainInfo: Optional[DomainInformationContainer] = None
    ConnectionId: Optional[str] = None
    ConnectionStatus: Optional[InboundConnectionStatus] = None
    ConnectionMode: Optional[ConnectionModeType] = None


class AutoTune(BaseValidatorModel):
    AutoTuneType: Optional[Literal['SCHEDULED_ACTION']] = None
    AutoTuneDetails: Optional[AutoTuneDetails] = None


class AutoTuneOptionsExtra(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutput]] = None
    UseOffPeakWindow: Optional[bool] = None

AutoTuneMaintenanceScheduleUnion = Union[AutoTuneMaintenanceSchedule, AutoTuneMaintenanceScheduleOutput]


class AutoTuneOptions(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceSchedule]] = None
    UseOffPeakWindow: Optional[bool] = None


# This class is the output for the 'describe_domain_health' function.
class DescribeDomainHealthResponse(BaseValidatorModel):
    DomainState: DomainStateType
    AvailabilityZoneCount: str
    ActiveAvailabilityZoneCount: str
    StandByAvailabilityZoneCount: str
    DataNodeCount: str
    DedicatedMaster: bool
    MasterEligibleNodeCount: str
    WarmNodeCount: str
    MasterNode: MasterNodeStatusType
    ClusterHealth: DomainHealthType
    TotalShards: str
    TotalUnAssignedShards: str
    EnvironmentInformation: List[EnvironmentInfo]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domain_change_progress' function.
class DescribeDomainChangeProgressResponse(BaseValidatorModel):
    ChangeProgressStatus: ChangeProgressStatusDetails
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_outbound_connection' function.
class CreateOutboundConnectionRequest(BaseValidatorModel):
    LocalDomainInfo: DomainInformationContainer
    RemoteDomainInfo: DomainInformationContainer
    ConnectionAlias: str
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionProperties] = None


# This class is the output for the 'create_outbound_connection' function.
class CreateOutboundConnectionResponse(BaseValidatorModel):
    LocalDomainInfo: DomainInformationContainer
    RemoteDomainInfo: DomainInformationContainer
    ConnectionAlias: str
    ConnectionStatus: OutboundConnectionStatus
    ConnectionId: str
    ConnectionMode: ConnectionModeType
    ConnectionProperties: ConnectionProperties
    ResponseMetadata: ResponseMetadata


class OutboundConnection(BaseValidatorModel):
    LocalDomainInfo: Optional[DomainInformationContainer] = None
    RemoteDomainInfo: Optional[DomainInformationContainer] = None
    ConnectionId: Optional[str] = None
    ConnectionAlias: Optional[str] = None
    ConnectionStatus: Optional[OutboundConnectionStatus] = None
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionProperties] = None


# This class is the input for the 'add_data_source' function.
class AddDataSourceRequest(BaseValidatorModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceType
    Description: Optional[str] = None


class DataSourceDetails(BaseValidatorModel):
    DataSourceType: Optional[DataSourceType] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None


# This class is the output for the 'get_data_source' function.
class GetDataSourceResponse(BaseValidatorModel):
    DataSourceType: DataSourceType
    Name: str
    Description: str
    Status: DataSourceStatusType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_data_source' function.
class UpdateDataSourceRequest(BaseValidatorModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceType
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None


# This class is the input for the 'add_direct_query_data_source' function.
class AddDirectQueryDataSourceRequest(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceType
    OpenSearchArns: List[str]
    Description: Optional[str] = None
    TagList: Optional[List[Tag]] = None


class DirectQueryDataSource(BaseValidatorModel):
    DataSourceName: Optional[str] = None
    DataSourceType: Optional[DirectQueryDataSourceType] = None
    Description: Optional[str] = None
    OpenSearchArns: Optional[List[str]] = None
    DataSourceArn: Optional[str] = None
    TagList: Optional[List[Tag]] = None


# This class is the output for the 'get_direct_query_data_source' function.
class GetDirectQueryDataSourceResponse(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceType
    Description: str
    OpenSearchArns: List[str]
    DataSourceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_direct_query_data_source' function.
class UpdateDirectQueryDataSourceRequest(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceType
    OpenSearchArns: List[str]
    Description: Optional[str] = None


# This class is the output for the 'create_vpc_endpoint' function.
class CreateVpcEndpointResponse(BaseValidatorModel):
    VpcEndpoint: VpcEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_endpoints' function.
class DescribeVpcEndpointsResponse(BaseValidatorModel):
    VpcEndpoints: List[VpcEndpoint]
    VpcEndpointErrors: List[VpcEndpointError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vpc_endpoint' function.
class UpdateVpcEndpointResponse(BaseValidatorModel):
    VpcEndpoint: VpcEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'associate_package' function.
class AssociatePackageRequest(BaseValidatorModel):
    PackageID: str
    DomainName: str
    PrerequisitePackageIDList: Optional[List[str]] = None
    AssociationConfiguration: Optional[PackageAssociationConfiguration] = None


class DomainPackageDetails(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[PackageTypeType] = None
    LastUpdated: Optional[datetime] = None
    DomainName: Optional[str] = None
    DomainPackageStatus: Optional[DomainPackageStatusType] = None
    PackageVersion: Optional[str] = None
    PrerequisitePackageIDList: Optional[List[str]] = None
    ReferencePath: Optional[str] = None
    ErrorDetails: Optional[ErrorDetails] = None
    AssociationConfiguration: Optional[PackageAssociationConfiguration] = None


class PackageDetailsForAssociation(BaseValidatorModel):
    PackageID: str
    PrerequisitePackageIDList: Optional[List[str]] = None
    AssociationConfiguration: Optional[PackageAssociationConfiguration] = None


class ClusterConfigOutput(BaseValidatorModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ZoneAwarenessConfig] = None
    DedicatedMasterType: Optional[OpenSearchPartitionInstanceTypeType] = None
    DedicatedMasterCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmType: Optional[OpenSearchWarmPartitionInstanceTypeType] = None
    WarmCount: Optional[int] = None
    ColdStorageOptions: Optional[ColdStorageOptions] = None
    MultiAZWithStandbyEnabled: Optional[bool] = None
    NodeOptions: Optional[List[NodeOption]] = None


class ClusterConfig(BaseValidatorModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ZoneAwarenessConfig] = None
    DedicatedMasterType: Optional[OpenSearchPartitionInstanceTypeType] = None
    DedicatedMasterCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmType: Optional[OpenSearchWarmPartitionInstanceTypeType] = None
    WarmCount: Optional[int] = None
    ColdStorageOptions: Optional[ColdStorageOptions] = None
    MultiAZWithStandbyEnabled: Optional[bool] = None
    NodeOptions: Optional[List[NodeOption]] = None


class OffPeakWindowOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    OffPeakWindow: Optional[OffPeakWindow] = None


# This class is the output for the 'create_package' function.
class CreatePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_package' function.
class DeletePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_packages' function.
class DescribePackagesResponse(BaseValidatorModel):
    PackageDetailsList: List[PackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_package' function.
class UpdatePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_package_version_history' function.
class GetPackageVersionHistoryResponse(BaseValidatorModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_reserved_instance_offerings' function.
class DescribeReservedInstanceOfferingsResponse(BaseValidatorModel):
    ReservedInstanceOfferings: List[ReservedInstanceOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_reserved_instances' function.
class DescribeReservedInstancesResponse(BaseValidatorModel):
    ReservedInstances: List[ReservedInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AdvancedSecurityOptionsInput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[MasterUserOptions] = None
    SAMLOptions: Optional[SAMLOptionsInput] = None
    JWTOptions: Optional[JWTOptionsInput] = None
    AnonymousAuthEnabled: Optional[bool] = None


class AdvancedSecurityOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    SAMLOptions: Optional[SAMLOptionsOutput] = None
    JWTOptions: Optional[JWTOptionsOutput] = None
    AnonymousAuthDisableDate: Optional[datetime] = None
    AnonymousAuthEnabled: Optional[bool] = None


class Limits(BaseValidatorModel):
    StorageTypes: Optional[List[StorageType]] = None
    InstanceLimits: Optional[InstanceLimits] = None
    AdditionalLimits: Optional[List[AdditionalLimit]] = None


# This class is the output for the 'get_upgrade_history' function.
class GetUpgradeHistoryResponse(BaseValidatorModel):
    UpgradeHistories: List[UpgradeHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'accept_inbound_connection' function.
class AcceptInboundConnectionResponse(BaseValidatorModel):
    Connection: InboundConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_inbound_connection' function.
class DeleteInboundConnectionResponse(BaseValidatorModel):
    Connection: InboundConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_inbound_connections' function.
class DescribeInboundConnectionsResponse(BaseValidatorModel):
    Connections: List[InboundConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'reject_inbound_connection' function.
class RejectInboundConnectionResponse(BaseValidatorModel):
    Connection: InboundConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domain_auto_tunes' function.
class DescribeDomainAutoTunesResponse(BaseValidatorModel):
    AutoTunes: List[AutoTune]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AutoTuneOptionsStatus(BaseValidatorModel):
    Options: Optional[AutoTuneOptionsExtra] = None
    Status: Optional[AutoTuneStatus] = None


class AutoTuneOptionsInput(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleUnion]] = None
    UseOffPeakWindow: Optional[bool] = None

AutoTuneOptionsUnion = Union[AutoTuneOptions, AutoTuneOptionsExtra]


# This class is the output for the 'delete_outbound_connection' function.
class DeleteOutboundConnectionResponse(BaseValidatorModel):
    Connection: OutboundConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_outbound_connections' function.
class DescribeOutboundConnectionsResponse(BaseValidatorModel):
    Connections: List[OutboundConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_data_sources' function.
class ListDataSourcesResponse(BaseValidatorModel):
    DataSources: List[DataSourceDetails]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_direct_query_data_sources' function.
class ListDirectQueryDataSourcesResponse(BaseValidatorModel):
    DirectQueryDataSources: List[DirectQueryDataSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_package' function.
class AssociatePackageResponse(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_packages' function.
class AssociatePackagesResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'dissociate_package' function.
class DissociatePackageResponse(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'dissociate_packages' function.
class DissociatePackagesResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_domains_for_package' function.
class ListDomainsForPackageResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_packages_for_domain' function.
class ListPackagesForDomainResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'associate_packages' function.
class AssociatePackagesRequest(BaseValidatorModel):
    PackageList: List[PackageDetailsForAssociation]
    DomainName: str


class ClusterConfigStatus(BaseValidatorModel):
    Options: ClusterConfigOutput
    Status: OptionStatus

ClusterConfigUnion = Union[ClusterConfig, ClusterConfigOutput]


class OffPeakWindowOptionsStatus(BaseValidatorModel):
    Options: Optional[OffPeakWindowOptions] = None
    Status: Optional[OptionStatus] = None


class AdvancedSecurityOptionsStatus(BaseValidatorModel):
    Options: AdvancedSecurityOptions
    Status: OptionStatus


class DomainStatus(BaseValidatorModel):
    DomainId: str
    DomainName: str
    ARN: str
    ClusterConfig: ClusterConfigOutput
    Created: Optional[bool] = None
    Deleted: Optional[bool] = None
    Endpoint: Optional[str] = None
    EndpointV2: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    DomainEndpointV2HostedZoneId: Optional[str] = None
    Processing: Optional[bool] = None
    UpgradeProcessing: Optional[bool] = None
    EngineVersion: Optional[str] = None
    EBSOptions: Optional[EBSOptions] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCDerivedInfo] = None
    CognitoOptions: Optional[CognitoOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptions] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    ServiceSoftwareOptions: Optional[ServiceSoftwareOptions] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptions] = None
    IdentityCenterOptions: Optional[IdentityCenterOptions] = None
    AutoTuneOptions: Optional[AutoTuneOptionsOutput] = None
    ChangeProgressDetails: Optional[ChangeProgressDetails] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptions] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptions] = None
    DomainProcessingStatus: Optional[DomainProcessingStatusTypeType] = None
    ModifyingProperties: Optional[List[ModifyingProperties]] = None
    AIMLOptions: Optional[AIMLOptionsOutput] = None


# This class is the output for the 'describe_instance_type_limits' function.
class DescribeInstanceTypeLimitsResponse(BaseValidatorModel):
    LimitsByRole: Dict[str, Limits]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_domain' function.
class CreateDomainRequest(BaseValidatorModel):
    DomainName: str
    EngineVersion: Optional[str] = None
    ClusterConfig: Optional[ClusterConfigUnion] = None
    EBSOptions: Optional[EBSOptions] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCOptions] = None
    CognitoOptions: Optional[CognitoOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptions] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInput] = None
    IdentityCenterOptions: Optional[IdentityCenterOptionsInput] = None
    TagList: Optional[List[Tag]] = None
    AutoTuneOptions: Optional[AutoTuneOptionsInput] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptions] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptions] = None
    AIMLOptions: Optional[AIMLOptionsInput] = None


# This class is the input for the 'update_domain_config' function.
class UpdateDomainConfigRequest(BaseValidatorModel):
    DomainName: str
    ClusterConfig: Optional[ClusterConfigUnion] = None
    EBSOptions: Optional[EBSOptions] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCOptions] = None
    CognitoOptions: Optional[CognitoOptions] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInput] = None
    IdentityCenterOptions: Optional[IdentityCenterOptionsInput] = None
    AutoTuneOptions: Optional[AutoTuneOptionsUnion] = None
    DryRun: Optional[bool] = None
    DryRunMode: Optional[DryRunModeType] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptions] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptions] = None
    AIMLOptions: Optional[AIMLOptionsInput] = None


class DomainConfig(BaseValidatorModel):
    EngineVersion: Optional[VersionStatus] = None
    ClusterConfig: Optional[ClusterConfigStatus] = None
    EBSOptions: Optional[EBSOptionsStatus] = None
    AccessPolicies: Optional[AccessPoliciesStatus] = None
    IPAddressType: Optional[IPAddressTypeStatus] = None
    SnapshotOptions: Optional[SnapshotOptionsStatus] = None
    VPCOptions: Optional[VPCDerivedInfoStatus] = None
    CognitoOptions: Optional[CognitoOptionsStatus] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsStatus] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsStatus] = None
    AdvancedOptions: Optional[AdvancedOptionsStatus] = None
    LogPublishingOptions: Optional[LogPublishingOptionsStatus] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsStatus] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsStatus] = None
    IdentityCenterOptions: Optional[IdentityCenterOptionsStatus] = None
    AutoTuneOptions: Optional[AutoTuneOptionsStatus] = None
    ChangeProgressDetails: Optional[ChangeProgressDetails] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsStatus] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsStatus] = None
    ModifyingProperties: Optional[List[ModifyingProperties]] = None
    AIMLOptions: Optional[AIMLOptionsStatus] = None


# This class is the output for the 'create_domain' function.
class CreateDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_domain' function.
class DeleteDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domain' function.
class DescribeDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domains' function.
class DescribeDomainsResponse(BaseValidatorModel):
    DomainStatusList: List[DomainStatus]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_dry_run_progress' function.
class DescribeDryRunProgressResponse(BaseValidatorModel):
    DryRunProgressStatus: DryRunProgressStatus
    DryRunConfig: DomainStatus
    DryRunResults: DryRunResults
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domain_config' function.
class DescribeDomainConfigResponse(BaseValidatorModel):
    DomainConfig: DomainConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_domain_config' function.
class UpdateDomainConfigResponse(BaseValidatorModel):
    DomainConfig: DomainConfig
    DryRunResults: DryRunResults
    DryRunProgressStatus: DryRunProgressStatus
    ResponseMetadata: ResponseMetadata
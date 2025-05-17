from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.es.es_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_inbound_cross_cluster_search_connection' function.
class AcceptInboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    CrossClusterSearchConnectionId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class OptionStatus(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class AdditionalLimit(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


class MasterUserOptions(BaseValidatorModel):
    MasterUserARN: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None


# This class is the input for the 'associate_package' function.
class AssociatePackageRequest(BaseValidatorModel):
    PackageID: str
    DomainName: str


# This class is the input for the 'authorize_vpc_endpoint_access' function.
class AuthorizeVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    Account: str


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


class AutoTuneStatus(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: Optional[int] = None
    ErrorMessage: Optional[str] = None
    PendingDeletion: Optional[bool] = None


# This class is the input for the 'cancel_domain_config_change' function.
class CancelDomainConfigChangeRequest(BaseValidatorModel):
    DomainName: str
    DryRun: Optional[bool] = None


class CancelledChangeProperty(BaseValidatorModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None


# This class is the input for the 'cancel_elasticsearch_service_software_update' function.
class CancelElasticsearchServiceSoftwareUpdateRequest(BaseValidatorModel):
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
    StartTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    InitiatedBy: Optional[InitiatedByType] = None


class ChangeProgressStage(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None


class CognitoOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    UserPoolId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    RoleArn: Optional[str] = None


class ColdStorageOptions(BaseValidatorModel):
    Enabled: bool


class CompatibleVersionsMap(BaseValidatorModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None


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


class LogPublishingOption(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None


class NodeToNodeEncryptionOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None


class SnapshotOptions(BaseValidatorModel):
    AutomatedSnapshotStartHour: Optional[int] = None


class VPCOptions(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class DomainInformation(BaseValidatorModel):
    DomainName: str
    OwnerId: Optional[str] = None
    Region: Optional[str] = None


class OutboundCrossClusterSearchConnectionStatus(BaseValidatorModel):
    StatusCode: Optional[OutboundCrossClusterSearchConnectionStatusCodeType] = None
    Message: Optional[str] = None


class PackageSource(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Key: Optional[str] = None


# This class is the input for the 'delete_elasticsearch_domain' function.
class DeleteElasticsearchDomainRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'delete_inbound_cross_cluster_search_connection' function.
class DeleteInboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    CrossClusterSearchConnectionId: str


# This class is the input for the 'delete_outbound_cross_cluster_search_connection' function.
class DeleteOutboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    CrossClusterSearchConnectionId: str


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


# This class is the input for the 'describe_elasticsearch_domain_config' function.
class DescribeElasticsearchDomainConfigRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'describe_elasticsearch_domain' function.
class DescribeElasticsearchDomainRequest(BaseValidatorModel):
    DomainName: str


# This class is the input for the 'describe_elasticsearch_domains' function.
class DescribeElasticsearchDomainsRequest(BaseValidatorModel):
    DomainNames: List[str]


# This class is the input for the 'describe_elasticsearch_instance_type_limits' function.
class DescribeElasticsearchInstanceTypeLimitsRequest(BaseValidatorModel):
    InstanceType: ESPartitionInstanceTypeType
    ElasticsearchVersion: str
    DomainName: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[List[str]] = None


class DescribePackagesFilter(BaseValidatorModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_reserved_elasticsearch_instance_offerings' function.
class DescribeReservedElasticsearchInstanceOfferingsRequest(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_reserved_elasticsearch_instances' function.
class DescribeReservedElasticsearchInstancesRequest(BaseValidatorModel):
    ReservedElasticsearchInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_vpc_endpoints' function.
class DescribeVpcEndpointsRequest(BaseValidatorModel):
    VpcEndpointIds: List[str]


class VpcEndpointError(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    ErrorCode: Optional[VpcEndpointErrorCodeType] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'dissociate_package' function.
class DissociatePackageRequest(BaseValidatorModel):
    PackageID: str
    DomainName: str


class DomainInfo(BaseValidatorModel):
    DomainName: Optional[str] = None
    EngineType: Optional[EngineTypeType] = None


class ErrorDetails(BaseValidatorModel):
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None


class DryRunResults(BaseValidatorModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None


class ZoneAwarenessConfig(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None


class ModifyingProperties(BaseValidatorModel):
    Name: Optional[str] = None
    ActiveValue: Optional[str] = None
    PendingValue: Optional[str] = None
    ValueType: Optional[PropertyValueTypeType] = None


class VPCDerivedInfo(BaseValidatorModel):
    VPCId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


# This class is the input for the 'get_compatible_elasticsearch_versions' function.
class GetCompatibleElasticsearchVersionsRequest(BaseValidatorModel):
    DomainName: Optional[str] = None


# This class is the input for the 'get_package_version_history' function.
class GetPackageVersionHistoryRequest(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PackageVersionHistory(BaseValidatorModel):
    PackageVersion: Optional[str] = None
    CommitMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None


# This class is the input for the 'get_upgrade_history' function.
class GetUpgradeHistoryRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_upgrade_status' function.
class GetUpgradeStatusRequest(BaseValidatorModel):
    DomainName: str


class InboundCrossClusterSearchConnectionStatus(BaseValidatorModel):
    StatusCode: Optional[InboundCrossClusterSearchConnectionStatusCodeType] = None
    Message: Optional[str] = None


class InstanceCountLimits(BaseValidatorModel):
    MinimumInstanceCount: Optional[int] = None
    MaximumInstanceCount: Optional[int] = None


# This class is the input for the 'list_domain_names' function.
class ListDomainNamesRequest(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None


# This class is the input for the 'list_domains_for_package' function.
class ListDomainsForPackageRequest(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_elasticsearch_instance_types' function.
class ListElasticsearchInstanceTypesRequest(BaseValidatorModel):
    ElasticsearchVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_elasticsearch_versions' function.
class ListElasticsearchVersionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_packages_for_domain' function.
class ListPackagesForDomainRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags' function.
class ListTagsRequest(BaseValidatorModel):
    ARN: str


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


# This class is the input for the 'purchase_reserved_elasticsearch_instance_offering' function.
class PurchaseReservedElasticsearchInstanceOfferingRequest(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


# This class is the input for the 'reject_inbound_cross_cluster_search_connection' function.
class RejectInboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    CrossClusterSearchConnectionId: str


# This class is the input for the 'remove_tags' function.
class RemoveTagsRequest(BaseValidatorModel):
    ARN: str
    TagKeys: List[str]


class RevokeVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    Account: str


class SAMLIdp(BaseValidatorModel):
    MetadataContent: str
    EntityId: str


# This class is the input for the 'start_elasticsearch_service_software_update' function.
class StartElasticsearchServiceSoftwareUpdateRequest(BaseValidatorModel):
    DomainName: str


class StorageTypeLimit(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


# This class is the input for the 'upgrade_elasticsearch_domain' function.
class UpgradeElasticsearchDomainRequest(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None


class UpgradeStepItem(BaseValidatorModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None


# This class is the output for the 'remove_tags' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_upgrade_status' function.
class GetUpgradeStatusResponse(BaseValidatorModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_elasticsearch_instance_types' function.
class ListElasticsearchInstanceTypesResponse(BaseValidatorModel):
    ElasticsearchInstanceTypes: List[ESPartitionInstanceTypeType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_elasticsearch_versions' function.
class ListElasticsearchVersionsResponse(BaseValidatorModel):
    ElasticsearchVersions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'purchase_reserved_elasticsearch_instance_offering' function.
class PurchaseReservedElasticsearchInstanceOfferingResponse(BaseValidatorModel):
    ReservedElasticsearchInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadata


class AccessPoliciesStatus(BaseValidatorModel):
    Options: str
    Status: OptionStatus


class AdvancedOptionsStatus(BaseValidatorModel):
    Options: Dict[str, str]
    Status: OptionStatus


class ElasticsearchVersionStatus(BaseValidatorModel):
    Options: str
    Status: OptionStatus


# This class is the input for the 'add_tags' function.
class AddTagsRequest(BaseValidatorModel):
    ARN: str
    TagList: List[Tag]


# This class is the output for the 'list_tags' function.
class ListTagsResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


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


# This class is the output for the 'cancel_domain_config_change' function.
class CancelDomainConfigChangeResponse(BaseValidatorModel):
    DryRun: bool
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangeProperty]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_elasticsearch_service_software_update' function.
class CancelElasticsearchServiceSoftwareUpdateResponse(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptions
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_elasticsearch_service_software_update' function.
class StartElasticsearchServiceSoftwareUpdateResponse(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptions
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upgrade_elasticsearch_domain' function.
class UpgradeElasticsearchDomainResponse(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
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
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    LastUpdatedTime: Optional[datetime] = None
    InitiatedBy: Optional[InitiatedByType] = None


class CognitoOptionsStatus(BaseValidatorModel):
    Options: CognitoOptions
    Status: OptionStatus


# This class is the output for the 'get_compatible_elasticsearch_versions' function.
class GetCompatibleElasticsearchVersionsResponse(BaseValidatorModel):
    CompatibleElasticsearchVersions: List[CompatibleVersionsMap]
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


# This class is the input for the 'create_vpc_endpoint' function.
class CreateVpcEndpointRequest(BaseValidatorModel):
    DomainArn: str
    VpcOptions: VPCOptions
    ClientToken: Optional[str] = None


# This class is the input for the 'update_vpc_endpoint' function.
class UpdateVpcEndpointRequest(BaseValidatorModel):
    VpcEndpointId: str
    VpcOptions: VPCOptions


# This class is the input for the 'create_outbound_cross_cluster_search_connection' function.
class CreateOutboundCrossClusterSearchConnectionRequest(BaseValidatorModel):
    SourceDomainInfo: DomainInformation
    DestinationDomainInfo: DomainInformation
    ConnectionAlias: str


# This class is the output for the 'create_outbound_cross_cluster_search_connection' function.
class CreateOutboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    SourceDomainInfo: DomainInformation
    DestinationDomainInfo: DomainInformation
    ConnectionAlias: str
    ConnectionStatus: OutboundCrossClusterSearchConnectionStatus
    CrossClusterSearchConnectionId: str
    ResponseMetadata: ResponseMetadata


class OutboundCrossClusterSearchConnection(BaseValidatorModel):
    SourceDomainInfo: Optional[DomainInformation] = None
    DestinationDomainInfo: Optional[DomainInformation] = None
    CrossClusterSearchConnectionId: Optional[str] = None
    ConnectionAlias: Optional[str] = None
    ConnectionStatus: Optional[OutboundCrossClusterSearchConnectionStatus] = None


# This class is the input for the 'create_package' function.
class CreatePackageRequest(BaseValidatorModel):
    PackageName: str
    PackageType: Literal['TXT-DICTIONARY']
    PackageSource: PackageSource
    PackageDescription: Optional[str] = None


# This class is the input for the 'update_package' function.
class UpdatePackageRequest(BaseValidatorModel):
    PackageID: str
    PackageSource: PackageSource
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None


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


# This class is the input for the 'describe_inbound_cross_cluster_search_connections' function.
class DescribeInboundCrossClusterSearchConnectionsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_outbound_cross_cluster_search_connections' function.
class DescribeOutboundCrossClusterSearchConnectionsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_packages' function.
class DescribePackagesRequest(BaseValidatorModel):
    Filters: Optional[List[DescribePackagesFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReservedElasticsearchInstanceOfferingsRequestPaginate(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedElasticsearchInstancesRequestPaginate(BaseValidatorModel):
    ReservedElasticsearchInstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetUpgradeHistoryRequestPaginate(BaseValidatorModel):
    DomainName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListElasticsearchInstanceTypesRequestPaginate(BaseValidatorModel):
    ElasticsearchVersion: str
    DomainName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListElasticsearchVersionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_domain_names' function.
class ListDomainNamesResponse(BaseValidatorModel):
    DomainNames: List[DomainInfo]
    ResponseMetadata: ResponseMetadata


class DomainPackageDetails(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[Literal['TXT-DICTIONARY']] = None
    LastUpdated: Optional[datetime] = None
    DomainName: Optional[str] = None
    DomainPackageStatus: Optional[DomainPackageStatusType] = None
    PackageVersion: Optional[str] = None
    ReferencePath: Optional[str] = None
    ErrorDetails: Optional[ErrorDetails] = None


class PackageDetails(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[Literal['TXT-DICTIONARY']] = None
    PackageDescription: Optional[str] = None
    PackageStatus: Optional[PackageStatusType] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    AvailablePackageVersion: Optional[str] = None
    ErrorDetails: Optional[ErrorDetails] = None


class ElasticsearchClusterConfig(BaseValidatorModel):
    InstanceType: Optional[ESPartitionInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ZoneAwarenessConfig] = None
    DedicatedMasterType: Optional[ESPartitionInstanceTypeType] = None
    DedicatedMasterCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmType: Optional[ESWarmPartitionInstanceTypeType] = None
    WarmCount: Optional[int] = None
    ColdStorageOptions: Optional[ColdStorageOptions] = None


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


# This class is the output for the 'get_package_version_history' function.
class GetPackageVersionHistoryResponse(BaseValidatorModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InboundCrossClusterSearchConnection(BaseValidatorModel):
    SourceDomainInfo: Optional[DomainInformation] = None
    DestinationDomainInfo: Optional[DomainInformation] = None
    CrossClusterSearchConnectionId: Optional[str] = None
    ConnectionStatus: Optional[InboundCrossClusterSearchConnectionStatus] = None


class InstanceLimits(BaseValidatorModel):
    InstanceCountLimits: Optional[InstanceCountLimits] = None


class ReservedElasticsearchInstanceOffering(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    ElasticsearchInstanceType: Optional[ESPartitionInstanceTypeType] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    PaymentOption: Optional[ReservedElasticsearchInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None


class ReservedElasticsearchInstance(BaseValidatorModel):
    ReservationName: Optional[str] = None
    ReservedElasticsearchInstanceId: Optional[str] = None
    ReservedElasticsearchInstanceOfferingId: Optional[str] = None
    ElasticsearchInstanceType: Optional[ESPartitionInstanceTypeType] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    ElasticsearchInstanceCount: Optional[int] = None
    State: Optional[str] = None
    PaymentOption: Optional[ReservedElasticsearchInstancePaymentOptionType] = None
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


class AutoTune(BaseValidatorModel):
    AutoTuneType: Optional[Literal['SCHEDULED_ACTION']] = None
    AutoTuneDetails: Optional[AutoTuneDetails] = None


class AutoTuneOptionsExtra(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutput]] = None

AutoTuneMaintenanceScheduleUnion = Union[AutoTuneMaintenanceSchedule, AutoTuneMaintenanceScheduleOutput]


class AutoTuneOptions(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceSchedule]] = None


# This class is the output for the 'describe_domain_change_progress' function.
class DescribeDomainChangeProgressResponse(BaseValidatorModel):
    ChangeProgressStatus: ChangeProgressStatusDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_outbound_cross_cluster_search_connection' function.
class DeleteOutboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    CrossClusterSearchConnection: OutboundCrossClusterSearchConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_outbound_cross_cluster_search_connections' function.
class DescribeOutboundCrossClusterSearchConnectionsResponse(BaseValidatorModel):
    CrossClusterSearchConnections: List[OutboundCrossClusterSearchConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_package' function.
class AssociatePackageResponse(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'dissociate_package' function.
class DissociatePackageResponse(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetails
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


class ElasticsearchClusterConfigStatus(BaseValidatorModel):
    Options: ElasticsearchClusterConfig
    Status: OptionStatus


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


# This class is the output for the 'accept_inbound_cross_cluster_search_connection' function.
class AcceptInboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_inbound_cross_cluster_search_connection' function.
class DeleteInboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_inbound_cross_cluster_search_connections' function.
class DescribeInboundCrossClusterSearchConnectionsResponse(BaseValidatorModel):
    CrossClusterSearchConnections: List[InboundCrossClusterSearchConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'reject_inbound_cross_cluster_search_connection' function.
class RejectInboundCrossClusterSearchConnectionResponse(BaseValidatorModel):
    CrossClusterSearchConnection: InboundCrossClusterSearchConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_elasticsearch_instance_offerings' function.
class DescribeReservedElasticsearchInstanceOfferingsResponse(BaseValidatorModel):
    ReservedElasticsearchInstanceOfferings: List[ReservedElasticsearchInstanceOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_reserved_elasticsearch_instances' function.
class DescribeReservedElasticsearchInstancesResponse(BaseValidatorModel):
    ReservedElasticsearchInstances: List[ReservedElasticsearchInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AdvancedSecurityOptionsInput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[MasterUserOptions] = None
    SAMLOptions: Optional[SAMLOptionsInput] = None
    AnonymousAuthEnabled: Optional[bool] = None


class AdvancedSecurityOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    SAMLOptions: Optional[SAMLOptionsOutput] = None
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

AutoTuneOptionsUnion = Union[AutoTuneOptions, AutoTuneOptionsExtra]


class AdvancedSecurityOptionsStatus(BaseValidatorModel):
    Options: AdvancedSecurityOptions
    Status: OptionStatus


class ElasticsearchDomainStatus(BaseValidatorModel):
    DomainId: str
    DomainName: str
    ARN: str
    ElasticsearchClusterConfig: ElasticsearchClusterConfig
    Created: Optional[bool] = None
    Deleted: Optional[bool] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    Processing: Optional[bool] = None
    UpgradeProcessing: Optional[bool] = None
    ElasticsearchVersion: Optional[str] = None
    EBSOptions: Optional[EBSOptions] = None
    AccessPolicies: Optional[str] = None
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
    AutoTuneOptions: Optional[AutoTuneOptionsOutput] = None
    ChangeProgressDetails: Optional[ChangeProgressDetails] = None
    DomainProcessingStatus: Optional[DomainProcessingStatusTypeType] = None
    ModifyingProperties: Optional[List[ModifyingProperties]] = None


# This class is the output for the 'describe_elasticsearch_instance_type_limits' function.
class DescribeElasticsearchInstanceTypeLimitsResponse(BaseValidatorModel):
    LimitsByRole: Dict[str, Limits]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_elasticsearch_domain' function.
class CreateElasticsearchDomainRequest(BaseValidatorModel):
    DomainName: str
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfig] = None
    EBSOptions: Optional[EBSOptions] = None
    AccessPolicies: Optional[str] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCOptions] = None
    CognitoOptions: Optional[CognitoOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptions] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInput] = None
    AutoTuneOptions: Optional[AutoTuneOptionsInput] = None
    TagList: Optional[List[Tag]] = None


# This class is the input for the 'update_elasticsearch_domain_config' function.
class UpdateElasticsearchDomainConfigRequest(BaseValidatorModel):
    DomainName: str
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfig] = None
    EBSOptions: Optional[EBSOptions] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCOptions] = None
    CognitoOptions: Optional[CognitoOptions] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    AccessPolicies: Optional[str] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOption]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInput] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptions] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptions] = None
    AutoTuneOptions: Optional[AutoTuneOptionsUnion] = None
    DryRun: Optional[bool] = None


class ElasticsearchDomainConfig(BaseValidatorModel):
    ElasticsearchVersion: Optional[ElasticsearchVersionStatus] = None
    ElasticsearchClusterConfig: Optional[ElasticsearchClusterConfigStatus] = None
    EBSOptions: Optional[EBSOptionsStatus] = None
    AccessPolicies: Optional[AccessPoliciesStatus] = None
    SnapshotOptions: Optional[SnapshotOptionsStatus] = None
    VPCOptions: Optional[VPCDerivedInfoStatus] = None
    CognitoOptions: Optional[CognitoOptionsStatus] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsStatus] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsStatus] = None
    AdvancedOptions: Optional[AdvancedOptionsStatus] = None
    LogPublishingOptions: Optional[LogPublishingOptionsStatus] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsStatus] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsStatus] = None
    AutoTuneOptions: Optional[AutoTuneOptionsStatus] = None
    ChangeProgressDetails: Optional[ChangeProgressDetails] = None
    ModifyingProperties: Optional[List[ModifyingProperties]] = None


# This class is the output for the 'create_elasticsearch_domain' function.
class CreateElasticsearchDomainResponse(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_elasticsearch_domain' function.
class DeleteElasticsearchDomainResponse(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_elasticsearch_domain' function.
class DescribeElasticsearchDomainResponse(BaseValidatorModel):
    DomainStatus: ElasticsearchDomainStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_elasticsearch_domains' function.
class DescribeElasticsearchDomainsResponse(BaseValidatorModel):
    DomainStatusList: List[ElasticsearchDomainStatus]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_elasticsearch_domain_config' function.
class DescribeElasticsearchDomainConfigResponse(BaseValidatorModel):
    DomainConfig: ElasticsearchDomainConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_elasticsearch_domain_config' function.
class UpdateElasticsearchDomainConfigResponse(BaseValidatorModel):
    DomainConfig: ElasticsearchDomainConfig
    DryRunResults: DryRunResults
    ResponseMetadata: ResponseMetadata
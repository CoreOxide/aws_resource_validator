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
from aws_resource_validator.pydantic_models.opensearch_constants import *

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


class AuthorizeVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    Account: Optional[str] = None
    Service: Optional[Literal["application.opensearchservice.amazonaws.com"]] = None


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
    Unit: Optional[Literal["HOURS"]] = None


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


class CancelDomainConfigChangeRequest(BaseValidatorModel):
    DomainName: str
    DryRun: Optional[bool] = None


class CancelledChangeProperty(BaseValidatorModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None


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
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None


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


class DeleteDataSourceRequest(BaseValidatorModel):
    DomainName: str
    Name: str


class DeleteDirectQueryDataSourceRequest(BaseValidatorModel):
    DataSourceName: str


class DeleteDomainRequest(BaseValidatorModel):
    DomainName: str


class DeleteInboundConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class DeleteOutboundConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class DeletePackageRequest(BaseValidatorModel):
    PackageID: str


class DeleteVpcEndpointRequest(BaseValidatorModel):
    VpcEndpointId: str


class VpcEndpointSummary(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    Status: Optional[VpcEndpointStatusType] = None


class DescribeDomainAutoTunesRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDomainChangeProgressRequest(BaseValidatorModel):
    DomainName: str
    ChangeId: Optional[str] = None


class DescribeDomainConfigRequest(BaseValidatorModel):
    DomainName: str


class DescribeDomainHealthRequest(BaseValidatorModel):
    DomainName: str


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


class DescribeDomainRequest(BaseValidatorModel):
    DomainName: str


class DescribeDomainsRequest(BaseValidatorModel):
    DomainNames: Sequence[str]


class DescribeDryRunProgressRequest(BaseValidatorModel):
    DomainName: str
    DryRunId: Optional[str] = None
    LoadDryRunConfig: Optional[bool] = None


class DryRunResults(BaseValidatorModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class DescribeInstanceTypeLimitsRequest(BaseValidatorModel):
    InstanceType: OpenSearchPartitionInstanceTypeType
    EngineVersion: str
    DomainName: Optional[str] = None


class DescribePackagesFilter(BaseValidatorModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[Sequence[str]] = None


class DescribeReservedInstanceOfferingsRequest(BaseValidatorModel):
    ReservedInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReservedInstancesRequest(BaseValidatorModel):
    ReservedInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcEndpointsRequest(BaseValidatorModel):
    VpcEndpointIds: Sequence[str]


class VpcEndpointError(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    ErrorCode: Optional[VpcEndpointErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class SecurityLakeDirectQueryDataSource(BaseValidatorModel):
    RoleArn: str


class DissociatePackageRequest(BaseValidatorModel):
    PackageID: str
    DomainName: str


class DissociatePackagesRequest(BaseValidatorModel):
    PackageList: Sequence[str]
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


class GetCompatibleVersionsRequest(BaseValidatorModel):
    DomainName: Optional[str] = None


class GetDataSourceRequest(BaseValidatorModel):
    DomainName: str
    Name: str


class GetDirectQueryDataSourceRequest(BaseValidatorModel):
    DataSourceName: str


class GetDomainMaintenanceStatusRequest(BaseValidatorModel):
    DomainName: str
    MaintenanceId: str


class GetPackageVersionHistoryRequest(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetUpgradeHistoryRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


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


class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    statuses: Optional[Sequence[ApplicationStatusType]] = None
    maxResults: Optional[int] = None


class ListDataSourcesRequest(BaseValidatorModel):
    DomainName: str


class ListDirectQueryDataSourcesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListDomainMaintenancesRequest(BaseValidatorModel):
    DomainName: str
    Action: Optional[MaintenanceTypeType] = None
    Status: Optional[MaintenanceStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDomainNamesRequest(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None


class ListDomainsForPackageRequest(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInstanceTypeDetailsRequest(BaseValidatorModel):
    EngineVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RetrieveAZs: Optional[bool] = None
    InstanceType: Optional[str] = None


class ListPackagesForDomainRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListScheduledActionsRequest(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsRequest(BaseValidatorModel):
    ARN: str


class ListVersionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None


class ListVpcEndpointsForDomainRequest(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None


class ListVpcEndpointsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class WindowStartTime(BaseValidatorModel):
    Hours: int
    Minutes: int


class PluginProperties(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    ClassName: Optional[str] = None
    UncompressedSizeInBytes: Optional[int] = None


class PurchaseReservedInstanceOfferingRequest(BaseValidatorModel):
    ReservedInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class RejectInboundConnectionRequest(BaseValidatorModel):
    ConnectionId: str


class RemoveTagsRequest(BaseValidatorModel):
    ARN: str
    TagKeys: Sequence[str]


class RevokeVpcEndpointAccessRequest(BaseValidatorModel):
    DomainName: str
    Account: Optional[str] = None
    Service: Optional[Literal["application.opensearchservice.amazonaws.com"]] = None


class SAMLIdp(BaseValidatorModel):
    MetadataContent: str
    EntityId: str


class StartDomainMaintenanceRequest(BaseValidatorModel):
    DomainName: str
    Action: MaintenanceTypeType
    NodeId: Optional[str] = None


class StartServiceSoftwareUpdateRequest(BaseValidatorModel):
    DomainName: str
    ScheduleAt: Optional[ScheduleAtType] = None
    DesiredStartTime: Optional[int] = None


class StorageTypeLimit(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


class UpdatePackageScopeRequest(BaseValidatorModel):
    PackageID: str
    Operation: PackageScopeOperationEnumType
    PackageUserList: Sequence[str]


class UpdateScheduledActionRequest(BaseValidatorModel):
    DomainName: str
    ActionID: str
    ActionType: ActionTypeType
    ScheduleAt: ScheduleAtType
    DesiredStartTime: Optional[int] = None


class UpgradeDomainRequest(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None


class UpgradeStepItem(BaseValidatorModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None


class AIMLOptionsInput(BaseValidatorModel):
    NaturalLanguageQueryGenerationOptions: Optional[ NaturalLanguageQueryGenerationOptionsInput ] = None


class AIMLOptionsOutput(BaseValidatorModel):
    NaturalLanguageQueryGenerationOptions: Optional[ NaturalLanguageQueryGenerationOptionsOutput ] = None


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


class AddDataSourceResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class AddDirectQueryDataSourceResponse(BaseValidatorModel):
    DataSourceArn: str
    ResponseMetadata: ResponseMetadata


class DeleteDataSourceResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetDomainMaintenanceStatusResponse(BaseValidatorModel):
    Status: MaintenanceStatusType
    StatusMessage: str
    NodeId: str
    Action: MaintenanceTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetUpgradeStatusResponse(BaseValidatorModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadata


class ListVersionsResponse(BaseValidatorModel):
    Versions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PurchaseReservedInstanceOfferingResponse(BaseValidatorModel):
    ReservedInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadata


class StartDomainMaintenanceResponse(BaseValidatorModel):
    MaintenanceId: str
    ResponseMetadata: ResponseMetadata


class UpdateDataSourceResponse(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadata


class UpdateDirectQueryDataSourceResponse(BaseValidatorModel):
    DataSourceArn: str
    ResponseMetadata: ResponseMetadata


class UpdatePackageScopeResponse(BaseValidatorModel):
    PackageID: str
    Operation: PackageScopeOperationEnumType
    PackageUserList: List[str]
    ResponseMetadata: ResponseMetadata


class AddTagsRequest(BaseValidatorModel):
    ARN: str
    TagList: Sequence[Tag]


class ListTagsResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class ApplicationSummary(BaseValidatorModel):
    pass


class ListApplicationsResponse(BaseValidatorModel):
    ApplicationSummaries: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AuthorizeVpcEndpointAccessResponse(BaseValidatorModel):
    AuthorizedPrincipal: AuthorizedPrincipal
    ResponseMetadata: ResponseMetadata


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


class Timestamp(BaseValidatorModel):
    pass


class AutoTuneMaintenanceSchedule(BaseValidatorModel):
    StartAt: Optional[Timestamp] = None
    Duration: Optional[Duration] = None
    CronExpressionForRecurrence: Optional[str] = None


class EnvironmentInfo(BaseValidatorModel):
    AvailabilityZoneInformation: Optional[List[AvailabilityZoneInfo]] = None


class CancelDomainConfigChangeResponse(BaseValidatorModel):
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangeProperty]
    DryRun: bool
    ResponseMetadata: ResponseMetadata


class CancelServiceSoftwareUpdateResponse(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptions
    ResponseMetadata: ResponseMetadata


class StartServiceSoftwareUpdateResponse(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptions
    ResponseMetadata: ResponseMetadata


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


class GetCompatibleVersionsResponse(BaseValidatorModel):
    CompatibleVersions: List[CompatibleVersionsMap]
    ResponseMetadata: ResponseMetadata


class ConnectionProperties(BaseValidatorModel):
    Endpoint: Optional[str] = None
    CrossClusterSearch: Optional[CrossClusterSearchConnectionProperties] = None


class CreateApplicationRequest(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    dataSources: Optional[Sequence[DataSource]] = None
    iamIdentityCenterOptions: Optional[IamIdentityCenterOptionsInput] = None
    appConfigs: Optional[Sequence[AppConfig]] = None
    tagList: Optional[Sequence[Tag]] = None


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


class CreateVpcEndpointRequest(BaseValidatorModel):
    DomainArn: str
    VpcOptions: VPCOptions
    ClientToken: Optional[str] = None


class UpdateVpcEndpointRequest(BaseValidatorModel):
    VpcEndpointId: str
    VpcOptions: VPCOptions


class UpdatePackageRequest(BaseValidatorModel):
    PackageID: str
    PackageSource: PackageSource
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None
    PackageConfiguration: Optional[PackageConfiguration] = None
    PackageEncryptionOptions: Optional[PackageEncryptionOptions] = None


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


class DeleteVpcEndpointResponse(BaseValidatorModel):
    VpcEndpointSummary: VpcEndpointSummary
    ResponseMetadata: ResponseMetadata


class ListVpcEndpointsForDomainResponse(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummary]
    NextToken: str
    ResponseMetadata: ResponseMetadata


class ListVpcEndpointsResponse(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummary]
    NextToken: str
    ResponseMetadata: ResponseMetadata


class DescribeDomainNodesResponse(BaseValidatorModel):
    DomainNodesStatusList: List[DomainNodesStatus]
    ResponseMetadata: ResponseMetadata


class DescribeInboundConnectionsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeOutboundConnectionsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePackagesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[DescribePackagesFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DirectQueryDataSourceType(BaseValidatorModel):
    CloudWatchLog: Optional[CloudWatchDirectQueryDataSource] = None
    SecurityLake: Optional[SecurityLakeDirectQueryDataSource] = None


class ListDomainNamesResponse(BaseValidatorModel):
    DomainNames: List[DomainInfo]
    ResponseMetadata: ResponseMetadata


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


class ListInstanceTypeDetailsResponse(BaseValidatorModel):
    InstanceTypeDetails: List[InstanceTypeDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PackageAssociationConfiguration(BaseValidatorModel):
    KeyStoreAccessOption: Optional[KeyStoreAccessOption] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    statuses: Optional[Sequence[ApplicationStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ScheduledAction(BaseValidatorModel):
    pass


class ListScheduledActionsResponse(BaseValidatorModel):
    ScheduledActions: List[ScheduledAction]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateScheduledActionResponse(BaseValidatorModel):
    ScheduledAction: ScheduledAction
    ResponseMetadata: ResponseMetadata


class NodeConfig(BaseValidatorModel):
    pass


class NodeOption(BaseValidatorModel):
    NodeType: Optional[Literal["coordinator"]] = None
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
    AutoTuneType: Optional[Literal["SCHEDULED_ACTION"]] = None
    AutoTuneDetails: Optional[AutoTuneDetails] = None


class AutoTuneOptionsExtra(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutput]] = None
    UseOffPeakWindow: Optional[bool] = None


class AutoTuneOptions(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceSchedule]] = None
    UseOffPeakWindow: Optional[bool] = None


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


class DescribeDomainChangeProgressResponse(BaseValidatorModel):
    ChangeProgressStatus: ChangeProgressStatusDetails
    ResponseMetadata: ResponseMetadata


class CreateOutboundConnectionRequest(BaseValidatorModel):
    LocalDomainInfo: DomainInformationContainer
    RemoteDomainInfo: DomainInformationContainer
    ConnectionAlias: str
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionProperties] = None


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


class GetDataSourceResponse(BaseValidatorModel):
    DataSourceType: DataSourceType
    Name: str
    Description: str
    Status: DataSourceStatusType
    ResponseMetadata: ResponseMetadata


class UpdateDataSourceRequest(BaseValidatorModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceType
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None


class AddDirectQueryDataSourceRequest(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceType
    OpenSearchArns: Sequence[str]
    Description: Optional[str] = None
    TagList: Optional[Sequence[Tag]] = None


class DirectQueryDataSource(BaseValidatorModel):
    DataSourceName: Optional[str] = None
    DataSourceType: Optional[DirectQueryDataSourceType] = None
    Description: Optional[str] = None
    OpenSearchArns: Optional[List[str]] = None
    DataSourceArn: Optional[str] = None
    TagList: Optional[List[Tag]] = None


class GetDirectQueryDataSourceResponse(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceType
    Description: str
    OpenSearchArns: List[str]
    DataSourceArn: str
    ResponseMetadata: ResponseMetadata


class UpdateDirectQueryDataSourceRequest(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceType
    OpenSearchArns: Sequence[str]
    Description: Optional[str] = None


class CreateVpcEndpointResponse(BaseValidatorModel):
    VpcEndpoint: VpcEndpoint
    ResponseMetadata: ResponseMetadata


class DescribeVpcEndpointsResponse(BaseValidatorModel):
    VpcEndpoints: List[VpcEndpoint]
    VpcEndpointErrors: List[VpcEndpointError]
    ResponseMetadata: ResponseMetadata


class UpdateVpcEndpointResponse(BaseValidatorModel):
    VpcEndpoint: VpcEndpoint
    ResponseMetadata: ResponseMetadata


class AssociatePackageRequest(BaseValidatorModel):
    PackageID: str
    DomainName: str
    PrerequisitePackageIDList: Optional[Sequence[str]] = None
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
    PrerequisitePackageIDList: Optional[Sequence[str]] = None
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
    NodeOptions: Optional[Sequence[NodeOption]] = None


class OffPeakWindowOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    OffPeakWindow: Optional[OffPeakWindow] = None


class CreatePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


class DeletePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


class DescribePackagesResponse(BaseValidatorModel):
    PackageDetailsList: List[PackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdatePackageResponse(BaseValidatorModel):
    PackageDetails: PackageDetails
    ResponseMetadata: ResponseMetadata


class GetPackageVersionHistoryResponse(BaseValidatorModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeReservedInstanceOfferingsResponse(BaseValidatorModel):
    ReservedInstanceOfferings: List[ReservedInstanceOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class GetUpgradeHistoryResponse(BaseValidatorModel):
    UpgradeHistories: List[UpgradeHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AcceptInboundConnectionResponse(BaseValidatorModel):
    Connection: InboundConnection
    ResponseMetadata: ResponseMetadata


class DeleteInboundConnectionResponse(BaseValidatorModel):
    Connection: InboundConnection
    ResponseMetadata: ResponseMetadata


class DescribeInboundConnectionsResponse(BaseValidatorModel):
    Connections: List[InboundConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RejectInboundConnectionResponse(BaseValidatorModel):
    Connection: InboundConnection
    ResponseMetadata: ResponseMetadata


class DescribeDomainAutoTunesResponse(BaseValidatorModel):
    AutoTunes: List[AutoTune]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AutoTuneOptionsStatus(BaseValidatorModel):
    Options: Optional[AutoTuneOptionsExtra] = None
    Status: Optional[AutoTuneStatus] = None


class AutoTuneMaintenanceScheduleUnion(BaseValidatorModel):
    pass


class AutoTuneOptionsInput(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleUnion]] = None
    UseOffPeakWindow: Optional[bool] = None


class DeleteOutboundConnectionResponse(BaseValidatorModel):
    Connection: OutboundConnection
    ResponseMetadata: ResponseMetadata


class DescribeOutboundConnectionsResponse(BaseValidatorModel):
    Connections: List[OutboundConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDataSourcesResponse(BaseValidatorModel):
    DataSources: List[DataSourceDetails]
    ResponseMetadata: ResponseMetadata


class ListDirectQueryDataSourcesResponse(BaseValidatorModel):
    DirectQueryDataSources: List[DirectQueryDataSource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociatePackageResponse(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetails
    ResponseMetadata: ResponseMetadata


class AssociatePackagesResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata


class DissociatePackageResponse(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetails
    ResponseMetadata: ResponseMetadata


class DissociatePackagesResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata


class ListDomainsForPackageResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPackagesForDomainResponse(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociatePackagesRequest(BaseValidatorModel):
    PackageList: Sequence[PackageDetailsForAssociation]
    DomainName: str


class ClusterConfigStatus(BaseValidatorModel):
    Options: ClusterConfigOutput
    Status: OptionStatus


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


class DescribeInstanceTypeLimitsResponse(BaseValidatorModel):
    LimitsByRole: Dict[str, Limits]
    ResponseMetadata: ResponseMetadata


class ClusterConfigUnion(BaseValidatorModel):
    pass


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
    AdvancedOptions: Optional[Mapping[str, str]] = None
    LogPublishingOptions: Optional[Mapping[LogTypeType, LogPublishingOption]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptions] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInput] = None
    IdentityCenterOptions: Optional[IdentityCenterOptionsInput] = None
    TagList: Optional[Sequence[Tag]] = None
    AutoTuneOptions: Optional[AutoTuneOptionsInput] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptions] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptions] = None
    AIMLOptions: Optional[AIMLOptionsInput] = None


class AutoTuneOptionsUnion(BaseValidatorModel):
    pass


class UpdateDomainConfigRequest(BaseValidatorModel):
    DomainName: str
    ClusterConfig: Optional[ClusterConfigUnion] = None
    EBSOptions: Optional[EBSOptions] = None
    SnapshotOptions: Optional[SnapshotOptions] = None
    VPCOptions: Optional[VPCOptions] = None
    CognitoOptions: Optional[CognitoOptions] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    LogPublishingOptions: Optional[Mapping[LogTypeType, LogPublishingOption]] = None
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


class CreateDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


class DeleteDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


class DescribeDomainResponse(BaseValidatorModel):
    DomainStatus: DomainStatus
    ResponseMetadata: ResponseMetadata


class DescribeDomainsResponse(BaseValidatorModel):
    DomainStatusList: List[DomainStatus]
    ResponseMetadata: ResponseMetadata


class DescribeDryRunProgressResponse(BaseValidatorModel):
    DryRunProgressStatus: DryRunProgressStatus
    DryRunConfig: DomainStatus
    DryRunResults: DryRunResults
    ResponseMetadata: ResponseMetadata


class DescribeDomainConfigResponse(BaseValidatorModel):
    DomainConfig: DomainConfig
    ResponseMetadata: ResponseMetadata


class UpdateDomainConfigResponse(BaseValidatorModel):
    DomainConfig: DomainConfig
    DryRunResults: DryRunResults
    DryRunProgressStatus: DryRunProgressStatus
    ResponseMetadata: ResponseMetadata



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

class NaturalLanguageQueryGenerationOptionsInputTypeDef(BaseValidatorModel):
    DesiredState: Optional[NaturalLanguageQueryGenerationDesiredStateType] = None


class NaturalLanguageQueryGenerationOptionsOutputTypeDef(BaseValidatorModel):
    DesiredState: Optional[NaturalLanguageQueryGenerationDesiredStateType] = None
    CurrentState: Optional[NaturalLanguageQueryGenerationCurrentStateType] = None


class OptionStatusTypeDef(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionStateType
    UpdateVersion: Optional[int] = None
    PendingDeletion: Optional[bool] = None


class AWSDomainInformationTypeDef(BaseValidatorModel):
    DomainName: str
    OwnerId: Optional[str] = None
    Region: Optional[str] = None


class AcceptInboundConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class AdditionalLimitTypeDef(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


class JWTOptionsInputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    PublicKey: Optional[str] = None


class MasterUserOptionsTypeDef(BaseValidatorModel):
    MasterUserARN: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None


class JWTOptionsOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    PublicKey: Optional[str] = None


class AppConfigTypeDef(BaseValidatorModel):
    key: Optional[AppConfigTypeType] = None
    value: Optional[str] = None


class AuthorizeVpcEndpointAccessRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Account: Optional[str] = None
    Service: Optional[Literal["application.opensearchservice.amazonaws.com"]] = None


class AuthorizedPrincipalTypeDef(BaseValidatorModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None


class ScheduledAutoTuneDetailsTypeDef(BaseValidatorModel):
    Date: Optional[datetime] = None
    ActionType: Optional[ScheduledAutoTuneActionTypeType] = None
    Action: Optional[str] = None
    Severity: Optional[ScheduledAutoTuneSeverityTypeType] = None


class DurationTypeDef(BaseValidatorModel):
    Value: Optional[int] = None
    Unit: Optional[Literal["HOURS"]] = None


class AutoTuneOptionsOutputTypeDef(BaseValidatorModel):
    State: Optional[AutoTuneStateType] = None
    ErrorMessage: Optional[str] = None
    UseOffPeakWindow: Optional[bool] = None


class AutoTuneStatusTypeDef(BaseValidatorModel):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneStateType
    UpdateVersion: Optional[int] = None
    ErrorMessage: Optional[str] = None
    PendingDeletion: Optional[bool] = None


class AvailabilityZoneInfoTypeDef(BaseValidatorModel):
    AvailabilityZoneName: Optional[str] = None
    ZoneStatus: Optional[ZoneStatusType] = None
    ConfiguredDataNodeCount: Optional[str] = None
    AvailableDataNodeCount: Optional[str] = None
    TotalShards: Optional[str] = None
    TotalUnAssignedShards: Optional[str] = None


class CancelDomainConfigChangeRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DryRun: Optional[bool] = None


class CancelledChangePropertyTypeDef(BaseValidatorModel):
    PropertyName: Optional[str] = None
    CancelledValue: Optional[str] = None
    ActiveValue: Optional[str] = None


class CancelServiceSoftwareUpdateRequestTypeDef(BaseValidatorModel):
    DomainName: str


class ServiceSoftwareOptionsTypeDef(BaseValidatorModel):
    CurrentVersion: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    Cancellable: Optional[bool] = None
    UpdateStatus: Optional[DeploymentStatusType] = None
    Description: Optional[str] = None
    AutomatedUpdateDate: Optional[datetime] = None
    OptionalDeployment: Optional[bool] = None


class ChangeProgressDetailsTypeDef(BaseValidatorModel):
    ChangeId: Optional[str] = None
    Message: Optional[str] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    InitiatedBy: Optional[InitiatedByType] = None
    StartTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


class ChangeProgressStageTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Description: Optional[str] = None
    LastUpdated: Optional[datetime] = None


class CloudWatchDirectQueryDataSourceTypeDef(BaseValidatorModel):
    RoleArn: str


class ColdStorageOptionsTypeDef(BaseValidatorModel):
    Enabled: bool


class ZoneAwarenessConfigTypeDef(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None


class CognitoOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    UserPoolId: Optional[str] = None
    IdentityPoolId: Optional[str] = None
    RoleArn: Optional[str] = None


class CompatibleVersionsMapTypeDef(BaseValidatorModel):
    SourceVersion: Optional[str] = None
    TargetVersions: Optional[List[str]] = None


class CrossClusterSearchConnectionPropertiesTypeDef(BaseValidatorModel):
    SkipUnavailable: Optional[SkipUnavailableStatusType] = None


class DataSourceTypeDef(BaseValidatorModel):
    dataSourceArn: Optional[str] = None
    dataSourceDescription: Optional[str] = None


class IamIdentityCenterOptionsInputTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    iamIdentityCenterInstanceArn: Optional[str] = None
    iamRoleForIdentityCenterApplicationArn: Optional[str] = None


class IamIdentityCenterOptionsTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    iamIdentityCenterInstanceArn: Optional[str] = None
    iamRoleForIdentityCenterApplicationArn: Optional[str] = None
    iamIdentityCenterApplicationArn: Optional[str] = None


class DomainEndpointOptionsTypeDef(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[TLSSecurityPolicyType] = None
    CustomEndpointEnabled: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    CustomEndpointCertificateArn: Optional[str] = None


class EBSOptionsTypeDef(BaseValidatorModel):
    EBSEnabled: Optional[bool] = None
    VolumeType: Optional[VolumeTypeType] = None
    VolumeSize: Optional[int] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None


class EncryptionAtRestOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None


class IdentityCenterOptionsInputTypeDef(BaseValidatorModel):
    EnabledAPIAccess: Optional[bool] = None
    IdentityCenterInstanceARN: Optional[str] = None
    SubjectKey: Optional[SubjectKeyIdCOptionType] = None
    RolesKey: Optional[RolesKeyIdCOptionType] = None


class LogPublishingOptionTypeDef(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None


class NodeToNodeEncryptionOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None


class SnapshotOptionsTypeDef(BaseValidatorModel):
    AutomatedSnapshotStartHour: Optional[int] = None


class SoftwareUpdateOptionsTypeDef(BaseValidatorModel):
    AutoSoftwareUpdateEnabled: Optional[bool] = None


class VPCOptionsTypeDef(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None


class OutboundConnectionStatusTypeDef(BaseValidatorModel):
    StatusCode: Optional[OutboundConnectionStatusCodeType] = None
    Message: Optional[str] = None


class PackageConfigurationTypeDef(BaseValidatorModel):
    LicenseRequirement: RequirementLevelType
    ConfigurationRequirement: RequirementLevelType
    LicenseFilepath: Optional[str] = None
    RequiresRestartForConfigurationUpdate: Optional[bool] = None


class PackageEncryptionOptionsTypeDef(BaseValidatorModel):
    EncryptionEnabled: bool
    KmsKeyIdentifier: Optional[str] = None


class PackageSourceTypeDef(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    S3Key: Optional[str] = None


class PackageVendingOptionsTypeDef(BaseValidatorModel):
    VendingEnabled: bool


class S3GlueDataCatalogTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None


class DeleteDataSourceRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Name: str


class DeleteDirectQueryDataSourceRequestTypeDef(BaseValidatorModel):
    DataSourceName: str


class DeleteDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str


class DeleteInboundConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionId: str


class DeleteOutboundConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionId: str


class DeletePackageRequestTypeDef(BaseValidatorModel):
    PackageID: str


class DeleteVpcEndpointRequestTypeDef(BaseValidatorModel):
    VpcEndpointId: str


class VpcEndpointSummaryTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    Status: Optional[VpcEndpointStatusType] = None


class DescribeDomainAutoTunesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDomainChangeProgressRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ChangeId: Optional[str] = None


class DescribeDomainConfigRequestTypeDef(BaseValidatorModel):
    DomainName: str


class DescribeDomainHealthRequestTypeDef(BaseValidatorModel):
    DomainName: str


class DescribeDomainNodesRequestTypeDef(BaseValidatorModel):
    DomainName: str


class DomainNodesStatusTypeDef(BaseValidatorModel):
    NodeId: Optional[str] = None
    NodeType: Optional[NodeTypeType] = None
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    NodeStatus: Optional[NodeStatusType] = None
    StorageType: Optional[str] = None
    StorageVolumeType: Optional[VolumeTypeType] = None
    StorageSize: Optional[str] = None


class DescribeDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str


class DescribeDomainsRequestTypeDef(BaseValidatorModel):
    DomainNames: Sequence[str]


class DescribeDryRunProgressRequestTypeDef(BaseValidatorModel):
    DomainName: str
    DryRunId: Optional[str] = None
    LoadDryRunConfig: Optional[bool] = None


class DryRunResultsTypeDef(BaseValidatorModel):
    DeploymentType: Optional[str] = None
    Message: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class DescribeInstanceTypeLimitsRequestTypeDef(BaseValidatorModel):
    InstanceType: OpenSearchPartitionInstanceTypeType
    EngineVersion: str
    DomainName: Optional[str] = None


class DescribePackagesFilterTypeDef(BaseValidatorModel):
    Name: Optional[DescribePackagesFilterNameType] = None
    Value: Optional[Sequence[str]] = None


class DescribeReservedInstanceOfferingsRequestTypeDef(BaseValidatorModel):
    ReservedInstanceOfferingId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReservedInstancesRequestTypeDef(BaseValidatorModel):
    ReservedInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcEndpointsRequestTypeDef(BaseValidatorModel):
    VpcEndpointIds: Sequence[str]


class VpcEndpointErrorTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    ErrorCode: Optional[VpcEndpointErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class SecurityLakeDirectQueryDataSourceTypeDef(BaseValidatorModel):
    RoleArn: str


class DissociatePackageRequestTypeDef(BaseValidatorModel):
    PackageID: str
    DomainName: str


class DissociatePackagesRequestTypeDef(BaseValidatorModel):
    PackageList: Sequence[str]
    DomainName: str


class ModifyingPropertiesTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ActiveValue: Optional[str] = None
    PendingValue: Optional[str] = None
    ValueType: Optional[PropertyValueTypeType] = None


class DomainInfoTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    EngineType: Optional[EngineTypeType] = None


class DomainMaintenanceDetailsTypeDef(BaseValidatorModel):
    MaintenanceId: Optional[str] = None
    DomainName: Optional[str] = None
    Action: Optional[MaintenanceTypeType] = None
    NodeId: Optional[str] = None
    Status: Optional[MaintenanceStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class ErrorDetailsTypeDef(BaseValidatorModel):
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None


class IdentityCenterOptionsTypeDef(BaseValidatorModel):
    EnabledAPIAccess: Optional[bool] = None
    IdentityCenterInstanceARN: Optional[str] = None
    SubjectKey: Optional[SubjectKeyIdCOptionType] = None
    RolesKey: Optional[RolesKeyIdCOptionType] = None
    IdentityCenterApplicationARN: Optional[str] = None
    IdentityStoreId: Optional[str] = None


class VPCDerivedInfoTypeDef(BaseValidatorModel):
    VPCId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class ValidationFailureTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class GetCompatibleVersionsRequestTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None


class GetDataSourceRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Name: str


class GetDirectQueryDataSourceRequestTypeDef(BaseValidatorModel):
    DataSourceName: str


class GetDomainMaintenanceStatusRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaintenanceId: str


class GetPackageVersionHistoryRequestTypeDef(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetUpgradeHistoryRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetUpgradeStatusRequestTypeDef(BaseValidatorModel):
    DomainName: str


class InboundConnectionStatusTypeDef(BaseValidatorModel):
    StatusCode: Optional[InboundConnectionStatusCodeType] = None
    Message: Optional[str] = None


class InstanceCountLimitsTypeDef(BaseValidatorModel):
    MinimumInstanceCount: Optional[int] = None
    MaximumInstanceCount: Optional[int] = None


class InstanceTypeDetailsTypeDef(BaseValidatorModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    EncryptionEnabled: Optional[bool] = None
    CognitoEnabled: Optional[bool] = None
    AppLogsEnabled: Optional[bool] = None
    AdvancedSecurityEnabled: Optional[bool] = None
    WarmEnabled: Optional[bool] = None
    InstanceRole: Optional[List[str]] = None
    AvailabilityZones: Optional[List[str]] = None


class KeyStoreAccessOptionTypeDef(BaseValidatorModel):
    KeyStoreAccessEnabled: bool
    KeyAccessRoleArn: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    statuses: Optional[Sequence[ApplicationStatusType]] = None
    maxResults: Optional[int] = None


class ListDataSourcesRequestTypeDef(BaseValidatorModel):
    DomainName: str


class ListDirectQueryDataSourcesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class ListDomainMaintenancesRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Action: Optional[MaintenanceTypeType] = None
    Status: Optional[MaintenanceStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDomainNamesRequestTypeDef(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None


class ListDomainsForPackageRequestTypeDef(BaseValidatorModel):
    PackageID: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListInstanceTypeDetailsRequestTypeDef(BaseValidatorModel):
    EngineVersion: str
    DomainName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    RetrieveAZs: Optional[bool] = None
    InstanceType: Optional[str] = None


class ListPackagesForDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListScheduledActionsRequestTypeDef(BaseValidatorModel):
    DomainName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsRequestTypeDef(BaseValidatorModel):
    ARN: str


class ListVersionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListVpcEndpointAccessRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None


class ListVpcEndpointsForDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str
    NextToken: Optional[str] = None


class ListVpcEndpointsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class WindowStartTimeTypeDef(BaseValidatorModel):
    Hours: int
    Minutes: int


class PluginPropertiesTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    ClassName: Optional[str] = None
    UncompressedSizeInBytes: Optional[int] = None


class PurchaseReservedInstanceOfferingRequestTypeDef(BaseValidatorModel):
    ReservedInstanceOfferingId: str
    ReservationName: str
    InstanceCount: Optional[int] = None


class RecurringChargeTypeDef(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class RejectInboundConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionId: str


class RemoveTagsRequestTypeDef(BaseValidatorModel):
    ARN: str
    TagKeys: Sequence[str]


class RevokeVpcEndpointAccessRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Account: Optional[str] = None
    Service: Optional[Literal["application.opensearchservice.amazonaws.com"]] = None


class SAMLIdpTypeDef(BaseValidatorModel):
    MetadataContent: str
    EntityId: str


class StartDomainMaintenanceRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Action: MaintenanceTypeType
    NodeId: Optional[str] = None


class StartServiceSoftwareUpdateRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ScheduleAt: Optional[ScheduleAtType] = None
    DesiredStartTime: Optional[int] = None


class StorageTypeLimitTypeDef(BaseValidatorModel):
    LimitName: Optional[str] = None
    LimitValues: Optional[List[str]] = None


class UpdatePackageScopeRequestTypeDef(BaseValidatorModel):
    PackageID: str
    Operation: PackageScopeOperationEnumType
    PackageUserList: Sequence[str]


class UpdateScheduledActionRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ActionID: str
    ActionType: ActionTypeType
    ScheduleAt: ScheduleAtType
    DesiredStartTime: Optional[int] = None


class UpgradeDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: Optional[bool] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None


class UpgradeStepItemTypeDef(BaseValidatorModel):
    UpgradeStep: Optional[UpgradeStepType] = None
    UpgradeStepStatus: Optional[UpgradeStatusType] = None
    Issues: Optional[List[str]] = None
    ProgressPercent: Optional[float] = None


class AIMLOptionsInputTypeDef(BaseValidatorModel):
    NaturalLanguageQueryGenerationOptions: Optional[ NaturalLanguageQueryGenerationOptionsInputTypeDef ] = None


class AIMLOptionsOutputTypeDef(BaseValidatorModel):
    NaturalLanguageQueryGenerationOptions: Optional[ NaturalLanguageQueryGenerationOptionsOutputTypeDef ] = None


class AccessPoliciesStatusTypeDef(BaseValidatorModel):
    Options: str
    Status: OptionStatusTypeDef


class AdvancedOptionsStatusTypeDef(BaseValidatorModel):
    Options: Dict[str, str]
    Status: OptionStatusTypeDef


class IPAddressTypeStatusTypeDef(BaseValidatorModel):
    Options: IPAddressTypeType
    Status: OptionStatusTypeDef


class VersionStatusTypeDef(BaseValidatorModel):
    Options: str
    Status: OptionStatusTypeDef


class DomainInformationContainerTypeDef(BaseValidatorModel):
    AWSDomainInformation: Optional[AWSDomainInformationTypeDef] = None


class AddDataSourceResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class AddDirectQueryDataSourceResponseTypeDef(BaseValidatorModel):
    DataSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDataSourceResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetDomainMaintenanceStatusResponseTypeDef(BaseValidatorModel):
    Status: MaintenanceStatusType
    StatusMessage: str
    NodeId: str
    Action: MaintenanceTypeType
    CreatedAt: datetime
    UpdatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetUpgradeStatusResponseTypeDef(BaseValidatorModel):
    UpgradeStep: UpgradeStepType
    StepStatus: UpgradeStatusType
    UpgradeName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListVersionsResponseTypeDef(BaseValidatorModel):
    Versions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PurchaseReservedInstanceOfferingResponseTypeDef(BaseValidatorModel):
    ReservedInstanceId: str
    ReservationName: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDomainMaintenanceResponseTypeDef(BaseValidatorModel):
    MaintenanceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataSourceResponseTypeDef(BaseValidatorModel):
    Message: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDirectQueryDataSourceResponseTypeDef(BaseValidatorModel):
    DataSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePackageScopeResponseTypeDef(BaseValidatorModel):
    PackageID: str
    Operation: PackageScopeOperationEnumType
    PackageUserList: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class AddTagsRequestTypeDef(BaseValidatorModel):
    ARN: str
    TagList: Sequence[TagTypeDef]


class ListTagsResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ApplicationSummaryTypeDef(BaseValidatorModel):
    pass


class ListApplicationsResponseTypeDef(BaseValidatorModel):
    ApplicationSummaries: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AuthorizeVpcEndpointAccessResponseTypeDef(BaseValidatorModel):
    AuthorizedPrincipal: AuthorizedPrincipalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListVpcEndpointAccessResponseTypeDef(BaseValidatorModel):
    AuthorizedPrincipalList: List[AuthorizedPrincipalTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class AutoTuneDetailsTypeDef(BaseValidatorModel):
    ScheduledAutoTuneDetails: Optional[ScheduledAutoTuneDetailsTypeDef] = None


class AutoTuneMaintenanceScheduleOutputTypeDef(BaseValidatorModel):
    StartAt: Optional[datetime] = None
    Duration: Optional[DurationTypeDef] = None
    CronExpressionForRecurrence: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class AutoTuneMaintenanceScheduleTypeDef(BaseValidatorModel):
    StartAt: Optional[TimestampTypeDef] = None
    Duration: Optional[DurationTypeDef] = None
    CronExpressionForRecurrence: Optional[str] = None


class EnvironmentInfoTypeDef(BaseValidatorModel):
    AvailabilityZoneInformation: Optional[List[AvailabilityZoneInfoTypeDef]] = None


class CancelDomainConfigChangeResponseTypeDef(BaseValidatorModel):
    CancelledChangeIds: List[str]
    CancelledChangeProperties: List[CancelledChangePropertyTypeDef]
    DryRun: bool
    ResponseMetadata: ResponseMetadataTypeDef


class CancelServiceSoftwareUpdateResponseTypeDef(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartServiceSoftwareUpdateResponseTypeDef(BaseValidatorModel):
    ServiceSoftwareOptions: ServiceSoftwareOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpgradeDomainResponseTypeDef(BaseValidatorModel):
    UpgradeId: str
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool
    AdvancedOptions: Dict[str, str]
    ChangeProgressDetails: ChangeProgressDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ChangeProgressStatusDetailsTypeDef(BaseValidatorModel):
    ChangeId: Optional[str] = None
    StartTime: Optional[datetime] = None
    Status: Optional[OverallChangeStatusType] = None
    PendingProperties: Optional[List[str]] = None
    CompletedProperties: Optional[List[str]] = None
    TotalNumberOfStages: Optional[int] = None
    ChangeProgressStages: Optional[List[ChangeProgressStageTypeDef]] = None
    LastUpdatedTime: Optional[datetime] = None
    ConfigChangeStatus: Optional[ConfigChangeStatusType] = None
    InitiatedBy: Optional[InitiatedByType] = None


class CognitoOptionsStatusTypeDef(BaseValidatorModel):
    Options: CognitoOptionsTypeDef
    Status: OptionStatusTypeDef


class GetCompatibleVersionsResponseTypeDef(BaseValidatorModel):
    CompatibleVersions: List[CompatibleVersionsMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ConnectionPropertiesTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None
    CrossClusterSearch: Optional[CrossClusterSearchConnectionPropertiesTypeDef] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: Optional[str] = None
    dataSources: Optional[Sequence[DataSourceTypeDef]] = None
    iamIdentityCenterOptions: Optional[IamIdentityCenterOptionsInputTypeDef] = None
    appConfigs: Optional[Sequence[AppConfigTypeDef]] = None
    tagList: Optional[Sequence[TagTypeDef]] = None


class DomainEndpointOptionsStatusTypeDef(BaseValidatorModel):
    Options: DomainEndpointOptionsTypeDef
    Status: OptionStatusTypeDef


class EBSOptionsStatusTypeDef(BaseValidatorModel):
    Options: EBSOptionsTypeDef
    Status: OptionStatusTypeDef


class EncryptionAtRestOptionsStatusTypeDef(BaseValidatorModel):
    Options: EncryptionAtRestOptionsTypeDef
    Status: OptionStatusTypeDef


class LogPublishingOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[Dict[LogTypeType, LogPublishingOptionTypeDef]] = None
    Status: Optional[OptionStatusTypeDef] = None


class NodeToNodeEncryptionOptionsStatusTypeDef(BaseValidatorModel):
    Options: NodeToNodeEncryptionOptionsTypeDef
    Status: OptionStatusTypeDef


class SnapshotOptionsStatusTypeDef(BaseValidatorModel):
    Options: SnapshotOptionsTypeDef
    Status: OptionStatusTypeDef


class SoftwareUpdateOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[SoftwareUpdateOptionsTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None


class CreateVpcEndpointRequestTypeDef(BaseValidatorModel):
    DomainArn: str
    VpcOptions: VPCOptionsTypeDef
    ClientToken: Optional[str] = None


class UpdateVpcEndpointRequestTypeDef(BaseValidatorModel):
    VpcEndpointId: str
    VpcOptions: VPCOptionsTypeDef


class UpdatePackageRequestTypeDef(BaseValidatorModel):
    PackageID: str
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None
    CommitMessage: Optional[str] = None
    PackageConfiguration: Optional[PackageConfigurationTypeDef] = None
    PackageEncryptionOptions: Optional[PackageEncryptionOptionsTypeDef] = None


class CreatePackageRequestTypeDef(BaseValidatorModel):
    PackageName: str
    PackageType: PackageTypeType
    PackageSource: PackageSourceTypeDef
    PackageDescription: Optional[str] = None
    PackageConfiguration: Optional[PackageConfigurationTypeDef] = None
    EngineVersion: Optional[str] = None
    PackageVendingOptions: Optional[PackageVendingOptionsTypeDef] = None
    PackageEncryptionOptions: Optional[PackageEncryptionOptionsTypeDef] = None


class DataSourceTypeTypeDef(BaseValidatorModel):
    S3GlueDataCatalog: Optional[S3GlueDataCatalogTypeDef] = None


class DeleteVpcEndpointResponseTypeDef(BaseValidatorModel):
    VpcEndpointSummary: VpcEndpointSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListVpcEndpointsForDomainResponseTypeDef(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListVpcEndpointsResponseTypeDef(BaseValidatorModel):
    VpcEndpointSummaryList: List[VpcEndpointSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainNodesResponseTypeDef(BaseValidatorModel):
    DomainNodesStatusList: List[DomainNodesStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInboundConnectionsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeOutboundConnectionsRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribePackagesRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[DescribePackagesFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DirectQueryDataSourceTypeTypeDef(BaseValidatorModel):
    CloudWatchLog: Optional[CloudWatchDirectQueryDataSourceTypeDef] = None
    SecurityLake: Optional[SecurityLakeDirectQueryDataSourceTypeDef] = None


class ListDomainNamesResponseTypeDef(BaseValidatorModel):
    DomainNames: List[DomainInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDomainMaintenancesResponseTypeDef(BaseValidatorModel):
    DomainMaintenances: List[DomainMaintenanceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IdentityCenterOptionsStatusTypeDef(BaseValidatorModel):
    Options: IdentityCenterOptionsTypeDef
    Status: OptionStatusTypeDef


class VPCDerivedInfoStatusTypeDef(BaseValidatorModel):
    Options: VPCDerivedInfoTypeDef
    Status: OptionStatusTypeDef


class VpcEndpointTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    DomainArn: Optional[str] = None
    VpcOptions: Optional[VPCDerivedInfoTypeDef] = None
    Status: Optional[VpcEndpointStatusType] = None
    Endpoint: Optional[str] = None


class DryRunProgressStatusTypeDef(BaseValidatorModel):
    DryRunId: str
    DryRunStatus: str
    CreationDate: str
    UpdateDate: str
    ValidationFailures: Optional[List[ValidationFailureTypeDef]] = None


class InstanceLimitsTypeDef(BaseValidatorModel):
    InstanceCountLimits: Optional[InstanceCountLimitsTypeDef] = None


class ListInstanceTypeDetailsResponseTypeDef(BaseValidatorModel):
    InstanceTypeDetails: List[InstanceTypeDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PackageAssociationConfigurationTypeDef(BaseValidatorModel):
    KeyStoreAccessOption: Optional[KeyStoreAccessOptionTypeDef] = None


class ListApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    statuses: Optional[Sequence[ApplicationStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ScheduledActionTypeDef(BaseValidatorModel):
    pass


class ListScheduledActionsResponseTypeDef(BaseValidatorModel):
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateScheduledActionResponseTypeDef(BaseValidatorModel):
    ScheduledAction: ScheduledActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class NodeConfigTypeDef(BaseValidatorModel):
    pass


class NodeOptionTypeDef(BaseValidatorModel):
    NodeType: Optional[Literal["coordinator"]] = None
    NodeConfig: Optional[NodeConfigTypeDef] = None


class OffPeakWindowTypeDef(BaseValidatorModel):
    WindowStartTime: Optional[WindowStartTimeTypeDef] = None


class PackageDetailsTypeDef(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[PackageTypeType] = None
    PackageDescription: Optional[str] = None
    PackageStatus: Optional[PackageStatusType] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    AvailablePackageVersion: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None
    EngineVersion: Optional[str] = None
    AvailablePluginProperties: Optional[PluginPropertiesTypeDef] = None
    AvailablePackageConfiguration: Optional[PackageConfigurationTypeDef] = None
    AllowListedUserList: Optional[List[str]] = None
    PackageOwner: Optional[str] = None
    PackageVendingOptions: Optional[PackageVendingOptionsTypeDef] = None
    PackageEncryptionOptions: Optional[PackageEncryptionOptionsTypeDef] = None


class PackageVersionHistoryTypeDef(BaseValidatorModel):
    PackageVersion: Optional[str] = None
    CommitMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    PluginProperties: Optional[PluginPropertiesTypeDef] = None
    PackageConfiguration: Optional[PackageConfigurationTypeDef] = None


class ReservedInstanceOfferingTypeDef(BaseValidatorModel):
    ReservedInstanceOfferingId: Optional[str] = None
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    PaymentOption: Optional[ReservedInstancePaymentOptionType] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None


class ReservedInstanceTypeDef(BaseValidatorModel):
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
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None


class SAMLOptionsInputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdpTypeDef] = None
    MasterUserName: Optional[str] = None
    MasterBackendRole: Optional[str] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None


class SAMLOptionsOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Idp: Optional[SAMLIdpTypeDef] = None
    SubjectKey: Optional[str] = None
    RolesKey: Optional[str] = None
    SessionTimeoutMinutes: Optional[int] = None


class StorageTypeTypeDef(BaseValidatorModel):
    StorageTypeName: Optional[str] = None
    StorageSubTypeName: Optional[str] = None
    StorageTypeLimits: Optional[List[StorageTypeLimitTypeDef]] = None


class UpgradeHistoryTypeDef(BaseValidatorModel):
    UpgradeName: Optional[str] = None
    StartTimestamp: Optional[datetime] = None
    UpgradeStatus: Optional[UpgradeStatusType] = None
    StepsList: Optional[List[UpgradeStepItemTypeDef]] = None


class AIMLOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[AIMLOptionsOutputTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None


class InboundConnectionTypeDef(BaseValidatorModel):
    LocalDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    RemoteDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    ConnectionId: Optional[str] = None
    ConnectionStatus: Optional[InboundConnectionStatusTypeDef] = None
    ConnectionMode: Optional[ConnectionModeType] = None


class AutoTuneTypeDef(BaseValidatorModel):
    AutoTuneType: Optional[Literal["SCHEDULED_ACTION"]] = None
    AutoTuneDetails: Optional[AutoTuneDetailsTypeDef] = None


class AutoTuneOptionsExtraTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[List[AutoTuneMaintenanceScheduleOutputTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None


class AutoTuneOptionsTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    RollbackOnDisable: Optional[RollbackOnDisableType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None


class DescribeDomainHealthResponseTypeDef(BaseValidatorModel):
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
    EnvironmentInformation: List[EnvironmentInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainChangeProgressResponseTypeDef(BaseValidatorModel):
    ChangeProgressStatus: ChangeProgressStatusDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateOutboundConnectionRequestTypeDef(BaseValidatorModel):
    LocalDomainInfo: DomainInformationContainerTypeDef
    RemoteDomainInfo: DomainInformationContainerTypeDef
    ConnectionAlias: str
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionPropertiesTypeDef] = None


class CreateOutboundConnectionResponseTypeDef(BaseValidatorModel):
    LocalDomainInfo: DomainInformationContainerTypeDef
    RemoteDomainInfo: DomainInformationContainerTypeDef
    ConnectionAlias: str
    ConnectionStatus: OutboundConnectionStatusTypeDef
    ConnectionId: str
    ConnectionMode: ConnectionModeType
    ConnectionProperties: ConnectionPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OutboundConnectionTypeDef(BaseValidatorModel):
    LocalDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    RemoteDomainInfo: Optional[DomainInformationContainerTypeDef] = None
    ConnectionId: Optional[str] = None
    ConnectionAlias: Optional[str] = None
    ConnectionStatus: Optional[OutboundConnectionStatusTypeDef] = None
    ConnectionMode: Optional[ConnectionModeType] = None
    ConnectionProperties: Optional[ConnectionPropertiesTypeDef] = None


class AddDataSourceRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceTypeTypeDef
    Description: Optional[str] = None


class DataSourceDetailsTypeDef(BaseValidatorModel):
    DataSourceType: Optional[DataSourceTypeTypeDef] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None


class GetDataSourceResponseTypeDef(BaseValidatorModel):
    DataSourceType: DataSourceTypeTypeDef
    Name: str
    Description: str
    Status: DataSourceStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataSourceRequestTypeDef(BaseValidatorModel):
    DomainName: str
    Name: str
    DataSourceType: DataSourceTypeTypeDef
    Description: Optional[str] = None
    Status: Optional[DataSourceStatusType] = None


class AddDirectQueryDataSourceRequestTypeDef(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceTypeTypeDef
    OpenSearchArns: Sequence[str]
    Description: Optional[str] = None
    TagList: Optional[Sequence[TagTypeDef]] = None


class DirectQueryDataSourceTypeDef(BaseValidatorModel):
    DataSourceName: Optional[str] = None
    DataSourceType: Optional[DirectQueryDataSourceTypeTypeDef] = None
    Description: Optional[str] = None
    OpenSearchArns: Optional[List[str]] = None
    DataSourceArn: Optional[str] = None
    TagList: Optional[List[TagTypeDef]] = None


class GetDirectQueryDataSourceResponseTypeDef(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceTypeTypeDef
    Description: str
    OpenSearchArns: List[str]
    DataSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDirectQueryDataSourceRequestTypeDef(BaseValidatorModel):
    DataSourceName: str
    DataSourceType: DirectQueryDataSourceTypeTypeDef
    OpenSearchArns: Sequence[str]
    Description: Optional[str] = None


class CreateVpcEndpointResponseTypeDef(BaseValidatorModel):
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeVpcEndpointsResponseTypeDef(BaseValidatorModel):
    VpcEndpoints: List[VpcEndpointTypeDef]
    VpcEndpointErrors: List[VpcEndpointErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateVpcEndpointResponseTypeDef(BaseValidatorModel):
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociatePackageRequestTypeDef(BaseValidatorModel):
    PackageID: str
    DomainName: str
    PrerequisitePackageIDList: Optional[Sequence[str]] = None
    AssociationConfiguration: Optional[PackageAssociationConfigurationTypeDef] = None


class DomainPackageDetailsTypeDef(BaseValidatorModel):
    PackageID: Optional[str] = None
    PackageName: Optional[str] = None
    PackageType: Optional[PackageTypeType] = None
    LastUpdated: Optional[datetime] = None
    DomainName: Optional[str] = None
    DomainPackageStatus: Optional[DomainPackageStatusType] = None
    PackageVersion: Optional[str] = None
    PrerequisitePackageIDList: Optional[List[str]] = None
    ReferencePath: Optional[str] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None
    AssociationConfiguration: Optional[PackageAssociationConfigurationTypeDef] = None


class PackageDetailsForAssociationTypeDef(BaseValidatorModel):
    PackageID: str
    PrerequisitePackageIDList: Optional[Sequence[str]] = None
    AssociationConfiguration: Optional[PackageAssociationConfigurationTypeDef] = None


class ClusterConfigOutputTypeDef(BaseValidatorModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ZoneAwarenessConfigTypeDef] = None
    DedicatedMasterType: Optional[OpenSearchPartitionInstanceTypeType] = None
    DedicatedMasterCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmType: Optional[OpenSearchWarmPartitionInstanceTypeType] = None
    WarmCount: Optional[int] = None
    ColdStorageOptions: Optional[ColdStorageOptionsTypeDef] = None
    MultiAZWithStandbyEnabled: Optional[bool] = None
    NodeOptions: Optional[List[NodeOptionTypeDef]] = None


class ClusterConfigTypeDef(BaseValidatorModel):
    InstanceType: Optional[OpenSearchPartitionInstanceTypeType] = None
    InstanceCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ZoneAwarenessConfigTypeDef] = None
    DedicatedMasterType: Optional[OpenSearchPartitionInstanceTypeType] = None
    DedicatedMasterCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmType: Optional[OpenSearchWarmPartitionInstanceTypeType] = None
    WarmCount: Optional[int] = None
    ColdStorageOptions: Optional[ColdStorageOptionsTypeDef] = None
    MultiAZWithStandbyEnabled: Optional[bool] = None
    NodeOptions: Optional[Sequence[NodeOptionTypeDef]] = None


class OffPeakWindowOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    OffPeakWindow: Optional[OffPeakWindowTypeDef] = None


class CreatePackageResponseTypeDef(BaseValidatorModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePackageResponseTypeDef(BaseValidatorModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePackagesResponseTypeDef(BaseValidatorModel):
    PackageDetailsList: List[PackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdatePackageResponseTypeDef(BaseValidatorModel):
    PackageDetails: PackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPackageVersionHistoryResponseTypeDef(BaseValidatorModel):
    PackageID: str
    PackageVersionHistoryList: List[PackageVersionHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeReservedInstanceOfferingsResponseTypeDef(BaseValidatorModel):
    ReservedInstanceOfferings: List[ReservedInstanceOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeReservedInstancesResponseTypeDef(BaseValidatorModel):
    ReservedInstances: List[ReservedInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AdvancedSecurityOptionsInputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[MasterUserOptionsTypeDef] = None
    SAMLOptions: Optional[SAMLOptionsInputTypeDef] = None
    JWTOptions: Optional[JWTOptionsInputTypeDef] = None
    AnonymousAuthEnabled: Optional[bool] = None


class AdvancedSecurityOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    SAMLOptions: Optional[SAMLOptionsOutputTypeDef] = None
    JWTOptions: Optional[JWTOptionsOutputTypeDef] = None
    AnonymousAuthDisableDate: Optional[datetime] = None
    AnonymousAuthEnabled: Optional[bool] = None


class LimitsTypeDef(BaseValidatorModel):
    StorageTypes: Optional[List[StorageTypeTypeDef]] = None
    InstanceLimits: Optional[InstanceLimitsTypeDef] = None
    AdditionalLimits: Optional[List[AdditionalLimitTypeDef]] = None


class GetUpgradeHistoryResponseTypeDef(BaseValidatorModel):
    UpgradeHistories: List[UpgradeHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AcceptInboundConnectionResponseTypeDef(BaseValidatorModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInboundConnectionResponseTypeDef(BaseValidatorModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInboundConnectionsResponseTypeDef(BaseValidatorModel):
    Connections: List[InboundConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RejectInboundConnectionResponseTypeDef(BaseValidatorModel):
    Connection: InboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainAutoTunesResponseTypeDef(BaseValidatorModel):
    AutoTunes: List[AutoTuneTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AutoTuneOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[AutoTuneOptionsExtraTypeDef] = None
    Status: Optional[AutoTuneStatusTypeDef] = None


class AutoTuneMaintenanceScheduleUnionTypeDef(BaseValidatorModel):
    pass


class AutoTuneOptionsInputTypeDef(BaseValidatorModel):
    DesiredState: Optional[AutoTuneDesiredStateType] = None
    MaintenanceSchedules: Optional[Sequence[AutoTuneMaintenanceScheduleUnionTypeDef]] = None
    UseOffPeakWindow: Optional[bool] = None


class DeleteOutboundConnectionResponseTypeDef(BaseValidatorModel):
    Connection: OutboundConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeOutboundConnectionsResponseTypeDef(BaseValidatorModel):
    Connections: List[OutboundConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    DataSources: List[DataSourceDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDirectQueryDataSourcesResponseTypeDef(BaseValidatorModel):
    DirectQueryDataSources: List[DirectQueryDataSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssociatePackageResponseTypeDef(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociatePackagesResponseTypeDef(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DissociatePackageResponseTypeDef(BaseValidatorModel):
    DomainPackageDetails: DomainPackageDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DissociatePackagesResponseTypeDef(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDomainsForPackageResponseTypeDef(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListPackagesForDomainResponseTypeDef(BaseValidatorModel):
    DomainPackageDetailsList: List[DomainPackageDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssociatePackagesRequestTypeDef(BaseValidatorModel):
    PackageList: Sequence[PackageDetailsForAssociationTypeDef]
    DomainName: str


class ClusterConfigStatusTypeDef(BaseValidatorModel):
    Options: ClusterConfigOutputTypeDef
    Status: OptionStatusTypeDef


class OffPeakWindowOptionsStatusTypeDef(BaseValidatorModel):
    Options: Optional[OffPeakWindowOptionsTypeDef] = None
    Status: Optional[OptionStatusTypeDef] = None


class AdvancedSecurityOptionsStatusTypeDef(BaseValidatorModel):
    Options: AdvancedSecurityOptionsTypeDef
    Status: OptionStatusTypeDef


class DomainStatusTypeDef(BaseValidatorModel):
    DomainId: str
    DomainName: str
    ARN: str
    ClusterConfig: ClusterConfigOutputTypeDef
    Created: Optional[bool] = None
    Deleted: Optional[bool] = None
    Endpoint: Optional[str] = None
    EndpointV2: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    DomainEndpointV2HostedZoneId: Optional[str] = None
    Processing: Optional[bool] = None
    UpgradeProcessing: Optional[bool] = None
    EngineVersion: Optional[str] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    SnapshotOptions: Optional[SnapshotOptionsTypeDef] = None
    VPCOptions: Optional[VPCDerivedInfoTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsTypeDef] = None
    AdvancedOptions: Optional[Dict[str, str]] = None
    LogPublishingOptions: Optional[Dict[LogTypeType, LogPublishingOptionTypeDef]] = None
    ServiceSoftwareOptions: Optional[ServiceSoftwareOptionsTypeDef] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsTypeDef] = None
    IdentityCenterOptions: Optional[IdentityCenterOptionsTypeDef] = None
    AutoTuneOptions: Optional[AutoTuneOptionsOutputTypeDef] = None
    ChangeProgressDetails: Optional[ChangeProgressDetailsTypeDef] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsTypeDef] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsTypeDef] = None
    DomainProcessingStatus: Optional[DomainProcessingStatusTypeType] = None
    ModifyingProperties: Optional[List[ModifyingPropertiesTypeDef]] = None
    AIMLOptions: Optional[AIMLOptionsOutputTypeDef] = None


class DescribeInstanceTypeLimitsResponseTypeDef(BaseValidatorModel):
    LimitsByRole: Dict[str, LimitsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ClusterConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateDomainRequestTypeDef(BaseValidatorModel):
    DomainName: str
    EngineVersion: Optional[str] = None
    ClusterConfig: Optional[ClusterConfigUnionTypeDef] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    SnapshotOptions: Optional[SnapshotOptionsTypeDef] = None
    VPCOptions: Optional[VPCOptionsTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsTypeDef] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None
    LogPublishingOptions: Optional[Mapping[LogTypeType, LogPublishingOptionTypeDef]] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInputTypeDef] = None
    IdentityCenterOptions: Optional[IdentityCenterOptionsInputTypeDef] = None
    TagList: Optional[Sequence[TagTypeDef]] = None
    AutoTuneOptions: Optional[AutoTuneOptionsInputTypeDef] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsTypeDef] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsTypeDef] = None
    AIMLOptions: Optional[AIMLOptionsInputTypeDef] = None


class AutoTuneOptionsUnionTypeDef(BaseValidatorModel):
    pass


class UpdateDomainConfigRequestTypeDef(BaseValidatorModel):
    DomainName: str
    ClusterConfig: Optional[ClusterConfigUnionTypeDef] = None
    EBSOptions: Optional[EBSOptionsTypeDef] = None
    SnapshotOptions: Optional[SnapshotOptionsTypeDef] = None
    VPCOptions: Optional[VPCOptionsTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsTypeDef] = None
    AdvancedOptions: Optional[Mapping[str, str]] = None
    AccessPolicies: Optional[str] = None
    IPAddressType: Optional[IPAddressTypeType] = None
    LogPublishingOptions: Optional[Mapping[LogTypeType, LogPublishingOptionTypeDef]] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsTypeDef] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsInputTypeDef] = None
    IdentityCenterOptions: Optional[IdentityCenterOptionsInputTypeDef] = None
    AutoTuneOptions: Optional[AutoTuneOptionsUnionTypeDef] = None
    DryRun: Optional[bool] = None
    DryRunMode: Optional[DryRunModeType] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsTypeDef] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsTypeDef] = None
    AIMLOptions: Optional[AIMLOptionsInputTypeDef] = None


class DomainConfigTypeDef(BaseValidatorModel):
    EngineVersion: Optional[VersionStatusTypeDef] = None
    ClusterConfig: Optional[ClusterConfigStatusTypeDef] = None
    EBSOptions: Optional[EBSOptionsStatusTypeDef] = None
    AccessPolicies: Optional[AccessPoliciesStatusTypeDef] = None
    IPAddressType: Optional[IPAddressTypeStatusTypeDef] = None
    SnapshotOptions: Optional[SnapshotOptionsStatusTypeDef] = None
    VPCOptions: Optional[VPCDerivedInfoStatusTypeDef] = None
    CognitoOptions: Optional[CognitoOptionsStatusTypeDef] = None
    EncryptionAtRestOptions: Optional[EncryptionAtRestOptionsStatusTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[NodeToNodeEncryptionOptionsStatusTypeDef] = None
    AdvancedOptions: Optional[AdvancedOptionsStatusTypeDef] = None
    LogPublishingOptions: Optional[LogPublishingOptionsStatusTypeDef] = None
    DomainEndpointOptions: Optional[DomainEndpointOptionsStatusTypeDef] = None
    AdvancedSecurityOptions: Optional[AdvancedSecurityOptionsStatusTypeDef] = None
    IdentityCenterOptions: Optional[IdentityCenterOptionsStatusTypeDef] = None
    AutoTuneOptions: Optional[AutoTuneOptionsStatusTypeDef] = None
    ChangeProgressDetails: Optional[ChangeProgressDetailsTypeDef] = None
    OffPeakWindowOptions: Optional[OffPeakWindowOptionsStatusTypeDef] = None
    SoftwareUpdateOptions: Optional[SoftwareUpdateOptionsStatusTypeDef] = None
    ModifyingProperties: Optional[List[ModifyingPropertiesTypeDef]] = None
    AIMLOptions: Optional[AIMLOptionsStatusTypeDef] = None


class CreateDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainResponseTypeDef(BaseValidatorModel):
    DomainStatus: DomainStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainsResponseTypeDef(BaseValidatorModel):
    DomainStatusList: List[DomainStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDryRunProgressResponseTypeDef(BaseValidatorModel):
    DryRunProgressStatus: DryRunProgressStatusTypeDef
    DryRunConfig: DomainStatusTypeDef
    DryRunResults: DryRunResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDomainConfigResponseTypeDef(BaseValidatorModel):
    DomainConfig: DomainConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDomainConfigResponseTypeDef(BaseValidatorModel):
    DomainConfig: DomainConfigTypeDef
    DryRunResults: DryRunResultsTypeDef
    DryRunProgressStatus: DryRunProgressStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



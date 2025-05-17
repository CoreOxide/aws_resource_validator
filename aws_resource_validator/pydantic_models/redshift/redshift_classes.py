from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.redshift.redshift_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_reserved_node_exchange' function.
class AcceptReservedNodeExchangeInputMessage(BaseValidatorModel):
    ReservedNodeId: str
    TargetReservedNodeOfferingId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AttributeValueTarget(BaseValidatorModel):
    AttributeValue: Optional[str] = None


class AccountWithRestoreAccess(BaseValidatorModel):
    AccountId: Optional[str] = None
    AccountAlias: Optional[str] = None


class AquaConfiguration(BaseValidatorModel):
    AquaStatus: Optional[AquaStatusType] = None
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None


# This class is the input for the 'associate_data_share_consumer' function.
class AssociateDataShareConsumerMessage(BaseValidatorModel):
    DataShareArn: str
    AssociateEntireAccount: Optional[bool] = None
    ConsumerArn: Optional[str] = None
    ConsumerRegion: Optional[str] = None
    AllowWrites: Optional[bool] = None


class CertificateAssociation(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None


class AuthenticationProfile(BaseValidatorModel):
    AuthenticationProfileName: Optional[str] = None
    AuthenticationProfileContent: Optional[str] = None


# This class is the input for the 'authorize_cluster_security_group_ingress' function.
class AuthorizeClusterSecurityGroupIngressMessage(BaseValidatorModel):
    ClusterSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


# This class is the input for the 'authorize_data_share' function.
class AuthorizeDataShareMessage(BaseValidatorModel):
    DataShareArn: str
    ConsumerIdentifier: str
    AllowWrites: Optional[bool] = None


# This class is the input for the 'authorize_endpoint_access' function.
class AuthorizeEndpointAccessMessage(BaseValidatorModel):
    Account: str
    ClusterIdentifier: Optional[str] = None
    VpcIds: Optional[List[str]] = None


# This class is the input for the 'authorize_snapshot_access' function.
class AuthorizeSnapshotAccessMessage(BaseValidatorModel):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None


class AuthorizedTokenIssuerOutput(BaseValidatorModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[List[str]] = None


class AuthorizedTokenIssuer(BaseValidatorModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[List[str]] = None


class SupportedPlatform(BaseValidatorModel):
    Name: Optional[str] = None


class DeleteClusterSnapshotMessage(BaseValidatorModel):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: Optional[str] = None


class SnapshotErrorMessage(BaseValidatorModel):
    SnapshotIdentifier: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None


# This class is the input for the 'batch_modify_cluster_snapshots' function.
class BatchModifyClusterSnapshotsMessage(BaseValidatorModel):
    SnapshotIdentifierList: List[str]
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Force: Optional[bool] = None


# This class is the input for the 'cancel_resize' function.
class CancelResizeMessage(BaseValidatorModel):
    ClusterIdentifier: str


class ClusterAssociatedToSchedule(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleAssociationState: Optional[ScheduleStateType] = None


class RevisionTarget(BaseValidatorModel):
    DatabaseRevision: Optional[str] = None
    Description: Optional[str] = None
    DatabaseRevisionReleaseDate: Optional[datetime] = None


class ClusterIamRole(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    ApplyStatus: Optional[str] = None


class ClusterNode(BaseValidatorModel):
    NodeRole: Optional[str] = None
    PrivateIPAddress: Optional[str] = None
    PublicIPAddress: Optional[str] = None


class Parameter(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    ApplyType: Optional[ParameterApplyTypeType] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None


class ClusterParameterStatus(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterApplyErrorDescription: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ClusterSecurityGroupMembership(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None


class ClusterSnapshotCopyStatus(BaseValidatorModel):
    DestinationRegion: Optional[str] = None
    RetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None


class DataTransferProgress(BaseValidatorModel):
    Status: Optional[str] = None
    CurrentRateInMegaBytesPerSecond: Optional[float] = None
    TotalDataInMegaBytes: Optional[int] = None
    DataTransferredInMegaBytes: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None


class DeferredMaintenanceWindow(BaseValidatorModel):
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[datetime] = None
    DeferMaintenanceEndTime: Optional[datetime] = None


class ElasticIpStatus(BaseValidatorModel):
    ElasticIp: Optional[str] = None
    Status: Optional[str] = None


class HsmStatus(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    Status: Optional[str] = None


class PendingModifiedValues(BaseValidatorModel):
    MasterUserPassword: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    ClusterType: Optional[str] = None
    ClusterVersion: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ClusterIdentifier: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    EncryptionType: Optional[str] = None


class ReservedNodeExchangeStatus(BaseValidatorModel):
    ReservedNodeExchangeRequestId: Optional[str] = None
    Status: Optional[ReservedNodeExchangeStatusTypeType] = None
    RequestTime: Optional[datetime] = None
    SourceReservedNodeId: Optional[str] = None
    SourceReservedNodeType: Optional[str] = None
    SourceReservedNodeCount: Optional[int] = None
    TargetReservedNodeOfferingId: Optional[str] = None
    TargetReservedNodeType: Optional[str] = None
    TargetReservedNodeCount: Optional[int] = None


class ResizeInfo(BaseValidatorModel):
    ResizeType: Optional[str] = None
    AllowCancelResize: Optional[bool] = None


class RestoreStatus(BaseValidatorModel):
    Status: Optional[str] = None
    CurrentRestoreRateInMegaBytesPerSecond: Optional[float] = None
    SnapshotSizeInMegaBytes: Optional[int] = None
    ProgressInMegaBytes: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None


class VpcSecurityGroupMembership(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class ClusterVersion(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'copy_cluster_snapshot' function.
class CopyClusterSnapshotMessage(BaseValidatorModel):
    SourceSnapshotIdentifier: str
    TargetSnapshotIdentifier: str
    SourceSnapshotClusterIdentifier: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None


# This class is the input for the 'create_authentication_profile' function.
class CreateAuthenticationProfileMessage(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str


# This class is the input for the 'create_custom_domain_association' function.
class CreateCustomDomainAssociationMessage(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str


# This class is the input for the 'create_endpoint_access' function.
class CreateEndpointAccessMessage(BaseValidatorModel):
    EndpointName: str
    SubnetGroupName: str
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None

Timestamp = Union[datetime, str]


class DataShareAssociation(BaseValidatorModel):
    ConsumerIdentifier: Optional[str] = None
    Status: Optional[DataShareStatusType] = None
    ConsumerRegion: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    StatusChangeDate: Optional[datetime] = None
    ProducerAllowedWrites: Optional[bool] = None
    ConsumerAcceptedWrites: Optional[bool] = None


# This class is the input for the 'deauthorize_data_share' function.
class DeauthorizeDataShareMessage(BaseValidatorModel):
    DataShareArn: str
    ConsumerIdentifier: str


# This class is the input for the 'delete_authentication_profile' function.
class DeleteAuthenticationProfileMessage(BaseValidatorModel):
    AuthenticationProfileName: str


# This class is the input for the 'delete_cluster' function.
class DeleteClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str
    SkipFinalClusterSnapshot: Optional[bool] = None
    FinalClusterSnapshotIdentifier: Optional[str] = None
    FinalClusterSnapshotRetentionPeriod: Optional[int] = None


# This class is the input for the 'delete_cluster_parameter_group' function.
class DeleteClusterParameterGroupMessage(BaseValidatorModel):
    ParameterGroupName: str


# This class is the input for the 'delete_cluster_security_group' function.
class DeleteClusterSecurityGroupMessage(BaseValidatorModel):
    ClusterSecurityGroupName: str


# This class is the input for the 'delete_cluster_snapshot' function.
class DeleteClusterSnapshotMessageRequest(BaseValidatorModel):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: Optional[str] = None


# This class is the input for the 'delete_cluster_subnet_group' function.
class DeleteClusterSubnetGroupMessage(BaseValidatorModel):
    ClusterSubnetGroupName: str


# This class is the input for the 'delete_custom_domain_association' function.
class DeleteCustomDomainAssociationMessage(BaseValidatorModel):
    ClusterIdentifier: str
    CustomDomainName: str


# This class is the input for the 'delete_endpoint_access' function.
class DeleteEndpointAccessMessage(BaseValidatorModel):
    EndpointName: str


# This class is the input for the 'delete_event_subscription' function.
class DeleteEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str


# This class is the input for the 'delete_hsm_client_certificate' function.
class DeleteHsmClientCertificateMessage(BaseValidatorModel):
    HsmClientCertificateIdentifier: str


# This class is the input for the 'delete_hsm_configuration' function.
class DeleteHsmConfigurationMessage(BaseValidatorModel):
    HsmConfigurationIdentifier: str


# This class is the input for the 'delete_integration' function.
class DeleteIntegrationMessage(BaseValidatorModel):
    IntegrationArn: str


# This class is the input for the 'delete_redshift_idc_application' function.
class DeleteRedshiftIdcApplicationMessage(BaseValidatorModel):
    RedshiftIdcApplicationArn: str


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyMessage(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'delete_scheduled_action' function.
class DeleteScheduledActionMessage(BaseValidatorModel):
    ScheduledActionName: str


# This class is the input for the 'delete_snapshot_copy_grant' function.
class DeleteSnapshotCopyGrantMessage(BaseValidatorModel):
    SnapshotCopyGrantName: str


# This class is the input for the 'delete_snapshot_schedule' function.
class DeleteSnapshotScheduleMessage(BaseValidatorModel):
    ScheduleIdentifier: str


# This class is the input for the 'delete_tags' function.
class DeleteTagsMessage(BaseValidatorModel):
    ResourceName: str
    TagKeys: List[str]


# This class is the input for the 'delete_usage_limit' function.
class DeleteUsageLimitMessage(BaseValidatorModel):
    UsageLimitId: str


# This class is the input for the 'describe_account_attributes' function.
class DescribeAccountAttributesMessage(BaseValidatorModel):
    AttributeNames: Optional[List[str]] = None


# This class is the input for the 'describe_authentication_profiles' function.
class DescribeAuthenticationProfilesMessage(BaseValidatorModel):
    AuthenticationProfileName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_cluster_db_revisions' function.
class DescribeClusterDbRevisionsMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_cluster_parameter_groups' function.
class DescribeClusterParameterGroupsMessage(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'describe_cluster_parameters' function.
class DescribeClusterParametersMessage(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_cluster_security_groups' function.
class DescribeClusterSecurityGroupsMessage(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


class SnapshotSortingEntity(BaseValidatorModel):
    Attribute: SnapshotAttributeToSortByType
    SortOrder: Optional[SortByOrderType] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_cluster_subnet_groups' function.
class DescribeClusterSubnetGroupsMessage(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'describe_cluster_tracks' function.
class DescribeClusterTracksMessage(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_cluster_versions' function.
class DescribeClusterVersionsMessage(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_clusters' function.
class DescribeClustersMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'describe_custom_domain_associations' function.
class DescribeCustomDomainAssociationsMessage(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_data_shares_for_consumer' function.
class DescribeDataSharesForConsumerMessage(BaseValidatorModel):
    ConsumerArn: Optional[str] = None
    Status: Optional[DataShareStatusForConsumerType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_data_shares_for_producer' function.
class DescribeDataSharesForProducerMessage(BaseValidatorModel):
    ProducerArn: Optional[str] = None
    Status: Optional[DataShareStatusForProducerType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_data_shares' function.
class DescribeDataSharesMessage(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_default_cluster_parameters' function.
class DescribeDefaultClusterParametersMessage(BaseValidatorModel):
    ParameterGroupFamily: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_endpoint_access' function.
class DescribeEndpointAccessMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    EndpointName: Optional[str] = None
    VpcId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_endpoint_authorization' function.
class DescribeEndpointAuthorizationMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    Grantee: Optional[bool] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_event_categories' function.
class DescribeEventCategoriesMessage(BaseValidatorModel):
    SourceType: Optional[str] = None


# This class is the input for the 'describe_event_subscriptions' function.
class DescribeEventSubscriptionsMessage(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'describe_hsm_client_certificates' function.
class DescribeHsmClientCertificatesMessage(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'describe_hsm_configurations' function.
class DescribeHsmConfigurationsMessage(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'describe_inbound_integrations' function.
class DescribeInboundIntegrationsMessage(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    TargetArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeIntegrationsFilter(BaseValidatorModel):
    Name: DescribeIntegrationsFilterNameType
    Values: List[str]


# This class is the input for the 'describe_logging_status' function.
class DescribeLoggingStatusMessage(BaseValidatorModel):
    ClusterIdentifier: str


class NodeConfigurationOptionsFilter(BaseValidatorModel):
    Name: Optional[NodeConfigurationOptionsFilterNameType] = None
    Operator: Optional[OperatorTypeType] = None
    Values: Optional[List[str]] = None


# This class is the input for the 'describe_orderable_cluster_options' function.
class DescribeOrderableClusterOptionsMessage(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    NodeType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_partners' function.
class DescribePartnersInputMessage(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: Optional[str] = None
    PartnerName: Optional[str] = None


class PartnerIntegrationInfo(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    PartnerName: Optional[str] = None
    Status: Optional[PartnerIntegrationStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


# This class is the input for the 'describe_redshift_idc_applications' function.
class DescribeRedshiftIdcApplicationsMessage(BaseValidatorModel):
    RedshiftIdcApplicationArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_reserved_node_exchange_status' function.
class DescribeReservedNodeExchangeStatusInputMessage(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeExchangeRequestId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_reserved_node_offerings' function.
class DescribeReservedNodeOfferingsMessage(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_reserved_nodes' function.
class DescribeReservedNodesMessage(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_resize' function.
class DescribeResizeMessage(BaseValidatorModel):
    ClusterIdentifier: str


class ScheduledActionFilter(BaseValidatorModel):
    Name: ScheduledActionFilterNameType
    Values: List[str]


# This class is the input for the 'describe_snapshot_copy_grants' function.
class DescribeSnapshotCopyGrantsMessage(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'describe_snapshot_schedules' function.
class DescribeSnapshotSchedulesMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'describe_table_restore_status' function.
class DescribeTableRestoreStatusMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TableRestoreRequestId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsMessage(BaseValidatorModel):
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'describe_usage_limits' function.
class DescribeUsageLimitsMessage(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None


# This class is the input for the 'disable_logging' function.
class DisableLoggingMessage(BaseValidatorModel):
    ClusterIdentifier: str


# This class is the input for the 'disable_snapshot_copy' function.
class DisableSnapshotCopyMessage(BaseValidatorModel):
    ClusterIdentifier: str


# This class is the input for the 'disassociate_data_share_consumer' function.
class DisassociateDataShareConsumerMessage(BaseValidatorModel):
    DataShareArn: str
    DisassociateEntireAccount: Optional[bool] = None
    ConsumerArn: Optional[str] = None
    ConsumerRegion: Optional[str] = None


# This class is the input for the 'enable_logging' function.
class EnableLoggingMessage(BaseValidatorModel):
    ClusterIdentifier: str
    BucketName: Optional[str] = None
    S3KeyPrefix: Optional[str] = None
    LogDestinationType: Optional[LogDestinationTypeType] = None
    LogExports: Optional[List[str]] = None


# This class is the input for the 'enable_snapshot_copy' function.
class EnableSnapshotCopyMessage(BaseValidatorModel):
    ClusterIdentifier: str
    DestinationRegion: str
    RetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None


class EndpointAuthorization(BaseValidatorModel):
    Grantor: Optional[str] = None
    Grantee: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    AuthorizeTime: Optional[datetime] = None
    ClusterStatus: Optional[str] = None
    Status: Optional[AuthorizationStatusType] = None
    AllowedAllVPCs: Optional[bool] = None
    AllowedVPCs: Optional[List[str]] = None
    EndpointCount: Optional[int] = None


class EventInfoMap(BaseValidatorModel):
    EventId: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    EventDescription: Optional[str] = None
    Severity: Optional[str] = None


class Event(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Severity: Optional[str] = None
    Date: Optional[datetime] = None
    EventId: Optional[str] = None


# This class is the input for the 'failover_primary_compute' function.
class FailoverPrimaryComputeInputMessage(BaseValidatorModel):
    ClusterIdentifier: str


# This class is the input for the 'get_cluster_credentials' function.
class GetClusterCredentialsMessage(BaseValidatorModel):
    DbUser: str
    DbName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DurationSeconds: Optional[int] = None
    AutoCreate: Optional[bool] = None
    DbGroups: Optional[List[str]] = None
    CustomDomainName: Optional[str] = None


# This class is the input for the 'get_cluster_credentials_with_iam' function.
class GetClusterCredentialsWithIAMMessage(BaseValidatorModel):
    DbName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DurationSeconds: Optional[int] = None
    CustomDomainName: Optional[str] = None


# This class is the input for the 'get_reserved_node_exchange_configuration_options' function.
class GetReservedNodeExchangeConfigurationOptionsInputMessage(BaseValidatorModel):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'get_reserved_node_exchange_offerings' function.
class GetReservedNodeExchangeOfferingsInputMessage(BaseValidatorModel):
    ReservedNodeId: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyMessage(BaseValidatorModel):
    ResourceArn: str


class ResourcePolicy(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None


class IntegrationError(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: Optional[str] = None


class LakeFormationQuery(BaseValidatorModel):
    Authorization: ServiceAuthorizationType


# This class is the input for the 'list_recommendations' function.
class ListRecommendationsMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'modify_aqua_configuration' function.
class ModifyAquaInputMessage(BaseValidatorModel):
    ClusterIdentifier: str
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None


# This class is the input for the 'modify_authentication_profile' function.
class ModifyAuthenticationProfileMessage(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str


# This class is the input for the 'modify_cluster_db_revision' function.
class ModifyClusterDbRevisionMessage(BaseValidatorModel):
    ClusterIdentifier: str
    RevisionTarget: str


# This class is the input for the 'modify_cluster_iam_roles' function.
class ModifyClusterIamRolesMessage(BaseValidatorModel):
    ClusterIdentifier: str
    AddIamRoles: Optional[List[str]] = None
    RemoveIamRoles: Optional[List[str]] = None
    DefaultIamRoleArn: Optional[str] = None


# This class is the input for the 'modify_cluster' function.
class ModifyClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    ClusterSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    MasterUserPassword: Optional[str] = None
    ClusterParameterGroupName: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ClusterVersion: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    NewClusterIdentifier: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ElasticIp: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    AvailabilityZoneRelocation: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    Port: Optional[int] = None
    ManageMasterPassword: Optional[bool] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[bool] = None


# This class is the input for the 'modify_cluster_snapshot' function.
class ModifyClusterSnapshotMessage(BaseValidatorModel):
    SnapshotIdentifier: str
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Force: Optional[bool] = None


# This class is the input for the 'modify_cluster_snapshot_schedule' function.
class ModifyClusterSnapshotScheduleMessage(BaseValidatorModel):
    ClusterIdentifier: str
    ScheduleIdentifier: Optional[str] = None
    DisassociateSchedule: Optional[bool] = None


# This class is the input for the 'modify_cluster_subnet_group' function.
class ModifyClusterSubnetGroupMessage(BaseValidatorModel):
    ClusterSubnetGroupName: str
    SubnetIds: List[str]
    Description: Optional[str] = None


# This class is the input for the 'modify_custom_domain_association' function.
class ModifyCustomDomainAssociationMessage(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str


# This class is the input for the 'modify_endpoint_access' function.
class ModifyEndpointAccessMessage(BaseValidatorModel):
    EndpointName: str
    VpcSecurityGroupIds: Optional[List[str]] = None


# This class is the input for the 'modify_event_subscription' function.
class ModifyEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    SourceIds: Optional[List[str]] = None
    EventCategories: Optional[List[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None


# This class is the input for the 'modify_integration' function.
class ModifyIntegrationMessage(BaseValidatorModel):
    IntegrationArn: str
    Description: Optional[str] = None
    IntegrationName: Optional[str] = None


# This class is the input for the 'modify_snapshot_copy_retention_period' function.
class ModifySnapshotCopyRetentionPeriodMessage(BaseValidatorModel):
    ClusterIdentifier: str
    RetentionPeriod: int
    Manual: Optional[bool] = None


# This class is the input for the 'modify_snapshot_schedule' function.
class ModifySnapshotScheduleMessage(BaseValidatorModel):
    ScheduleIdentifier: str
    ScheduleDefinitions: List[str]


# This class is the input for the 'modify_usage_limit' function.
class ModifyUsageLimitMessage(BaseValidatorModel):
    UsageLimitId: str
    Amount: Optional[int] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None


class ProvisionedIdentifier(BaseValidatorModel):
    ClusterIdentifier: str


class ServerlessIdentifier(BaseValidatorModel):
    NamespaceIdentifier: str
    WorkgroupIdentifier: str


class NetworkInterface(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    SubnetId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Ipv6Address: Optional[str] = None


class NodeConfigurationOption(BaseValidatorModel):
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    EstimatedDiskUtilizationPercent: Optional[float] = None
    Mode: Optional[ModeType] = None


# This class is the input for the 'delete_partner' function.
class PartnerIntegrationInputMessageRequest(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str


# This class is the input for the 'add_partner' function.
class PartnerIntegrationInputMessage(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str


# This class is the input for the 'pause_cluster' function.
class PauseClusterMessageRequest(BaseValidatorModel):
    ClusterIdentifier: str


class PauseClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str


# This class is the input for the 'purchase_reserved_node_offering' function.
class PurchaseReservedNodeOfferingMessage(BaseValidatorModel):
    ReservedNodeOfferingId: str
    NodeCount: Optional[int] = None


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyMessage(BaseValidatorModel):
    ResourceArn: str
    Policy: str


class ReadWriteAccess(BaseValidatorModel):
    Authorization: ServiceAuthorizationType


# This class is the input for the 'reboot_cluster' function.
class RebootClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str


class RecommendedAction(BaseValidatorModel):
    Text: Optional[str] = None
    Database: Optional[str] = None
    Command: Optional[str] = None
    Type: Optional[RecommendedActionTypeType] = None


class ReferenceLink(BaseValidatorModel):
    Text: Optional[str] = None
    Link: Optional[str] = None


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


# This class is the input for the 'reject_data_share' function.
class RejectDataShareMessage(BaseValidatorModel):
    DataShareArn: str


# This class is the input for the 'resize_cluster' function.
class ResizeClusterMessageRequest(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    Classic: Optional[bool] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None


class ResizeClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    Classic: Optional[bool] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None


# This class is the input for the 'restore_from_cluster_snapshot' function.
class RestoreFromClusterSnapshotMessage(BaseValidatorModel):
    ClusterIdentifier: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    ClusterSubnetGroupName: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    OwnerAccount: Optional[str] = None
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    ElasticIp: Optional[str] = None
    ClusterParameterGroupName: Optional[str] = None
    ClusterSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    KmsKeyId: Optional[str] = None
    NodeType: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    IamRoles: Optional[List[str]] = None
    MaintenanceTrackName: Optional[str] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    AvailabilityZoneRelocation: Optional[bool] = None
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None
    DefaultIamRoleArn: Optional[str] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None
    Encrypted: Optional[bool] = None
    ManageMasterPassword: Optional[bool] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[bool] = None


# This class is the input for the 'restore_table_from_cluster_snapshot' function.
class RestoreTableFromClusterSnapshotMessage(BaseValidatorModel):
    ClusterIdentifier: str
    SnapshotIdentifier: str
    SourceDatabaseName: str
    SourceTableName: str
    NewTableName: str
    SourceSchemaName: Optional[str] = None
    TargetDatabaseName: Optional[str] = None
    TargetSchemaName: Optional[str] = None
    EnableCaseSensitiveIdentifier: Optional[bool] = None


class TableRestoreStatus(BaseValidatorModel):
    TableRestoreRequestId: Optional[str] = None
    Status: Optional[TableRestoreStatusTypeType] = None
    Message: Optional[str] = None
    RequestTime: Optional[datetime] = None
    ProgressInMegaBytes: Optional[int] = None
    TotalDataInMegaBytes: Optional[int] = None
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SourceDatabaseName: Optional[str] = None
    SourceSchemaName: Optional[str] = None
    SourceTableName: Optional[str] = None
    TargetDatabaseName: Optional[str] = None
    TargetSchemaName: Optional[str] = None
    NewTableName: Optional[str] = None


# This class is the input for the 'resume_cluster' function.
class ResumeClusterMessageRequest(BaseValidatorModel):
    ClusterIdentifier: str


class ResumeClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str


# This class is the input for the 'revoke_cluster_security_group_ingress' function.
class RevokeClusterSecurityGroupIngressMessage(BaseValidatorModel):
    ClusterSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


# This class is the input for the 'revoke_endpoint_access' function.
class RevokeEndpointAccessMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    VpcIds: Optional[List[str]] = None
    Force: Optional[bool] = None


# This class is the input for the 'revoke_snapshot_access' function.
class RevokeSnapshotAccessMessage(BaseValidatorModel):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None


# This class is the input for the 'rotate_encryption_key' function.
class RotateEncryptionKeyMessage(BaseValidatorModel):
    ClusterIdentifier: str


class SupportedOperation(BaseValidatorModel):
    OperationName: Optional[str] = None


# This class is the input for the 'update_partner_status' function.
class UpdatePartnerStatusInputMessage(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str
    Status: PartnerIntegrationStatusType
    StatusMessage: Optional[str] = None


# This class is the output for the 'get_cluster_credentials' function.
class ClusterCredentials(BaseValidatorModel):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cluster_credentials_with_iam' function.
class ClusterExtendedCredentials(BaseValidatorModel):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    NextRefreshTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_cluster_parameter_group' function.
class ClusterParameterGroupNameMessage(BaseValidatorModel):
    ParameterGroupName: str
    ParameterGroupStatus: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_authentication_profile' function.
class CreateAuthenticationProfileResult(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_custom_domain_association' function.
class CreateCustomDomainAssociationResult(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadata


class CustomerStorageMessage(BaseValidatorModel):
    TotalBackupSizeInMegaBytes: float
    TotalProvisionedStorageInMegaBytes: float
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_authentication_profile' function.
class DeleteAuthenticationProfileResult(BaseValidatorModel):
    AuthenticationProfileName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_namespace' function.
class DeregisterNamespaceOutputMessage(BaseValidatorModel):
    Status: NamespaceRegistrationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cluster_snapshot_schedule' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'revoke_endpoint_access' function.
class EndpointAuthorizationResponse(BaseValidatorModel):
    Grantor: str
    Grantee: str
    ClusterIdentifier: str
    AuthorizeTime: datetime
    ClusterStatus: str
    Status: AuthorizationStatusType
    AllowedAllVPCs: bool
    AllowedVPCs: List[str]
    EndpointCount: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_logging' function.
class LoggingStatus(BaseValidatorModel):
    LoggingEnabled: bool
    BucketName: str
    S3KeyPrefix: str
    LastSuccessfulDeliveryTime: datetime
    LastFailureTime: datetime
    LastFailureMessage: str
    LogDestinationType: LogDestinationTypeType
    LogExports: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_authentication_profile' function.
class ModifyAuthenticationProfileResult(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_custom_domain_association' function.
class ModifyCustomDomainAssociationResult(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_partner_status' function.
class PartnerIntegrationOutputMessage(BaseValidatorModel):
    DatabaseName: str
    PartnerName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_namespace' function.
class RegisterNamespaceOutputMessage(BaseValidatorModel):
    Status: NamespaceRegistrationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_resize' function.
class ResizeProgressMessage(BaseValidatorModel):
    TargetNodeType: str
    TargetNumberOfNodes: int
    TargetClusterType: str
    Status: str
    ImportTablesCompleted: List[str]
    ImportTablesInProgress: List[str]
    ImportTablesNotStarted: List[str]
    AvgResizeRateInMegaBytesPerSecond: float
    TotalResizeDataInMegaBytes: int
    ProgressInMegaBytes: int
    ElapsedTimeInSeconds: int
    EstimatedTimeToCompletionInSeconds: int
    ResizeType: str
    Message: str
    TargetEncryptionType: str
    DataTransferProgressPercent: float
    ResponseMetadata: ResponseMetadata


class AccountAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[AttributeValueTarget]] = None


# This class is the output for the 'modify_aqua_configuration' function.
class ModifyAquaOutputMessage(BaseValidatorModel):
    AquaConfiguration: AquaConfiguration
    ResponseMetadata: ResponseMetadata


class Association(BaseValidatorModel):
    CustomDomainCertificateArn: Optional[str] = None
    CustomDomainCertificateExpiryDate: Optional[datetime] = None
    CertificateAssociations: Optional[List[CertificateAssociation]] = None


# This class is the output for the 'describe_authentication_profiles' function.
class DescribeAuthenticationProfilesResult(BaseValidatorModel):
    AuthenticationProfiles: List[AuthenticationProfile]
    ResponseMetadata: ResponseMetadata

AuthorizedTokenIssuerUnion = Union[AuthorizedTokenIssuer, AuthorizedTokenIssuerOutput]


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None
    SupportedPlatforms: Optional[List[SupportedPlatform]] = None


# This class is the input for the 'batch_delete_cluster_snapshots' function.
class BatchDeleteClusterSnapshotsRequest(BaseValidatorModel):
    Identifiers: List[DeleteClusterSnapshotMessage]


# This class is the output for the 'batch_delete_cluster_snapshots' function.
class BatchDeleteClusterSnapshotsResult(BaseValidatorModel):
    Resources: List[str]
    Errors: List[SnapshotErrorMessage]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_modify_cluster_snapshots' function.
class BatchModifyClusterSnapshotsOutputMessage(BaseValidatorModel):
    Resources: List[str]
    Errors: List[SnapshotErrorMessage]
    ResponseMetadata: ResponseMetadata


class ClusterDbRevision(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    CurrentDatabaseRevision: Optional[str] = None
    DatabaseRevisionReleaseDate: Optional[datetime] = None
    RevisionTargets: Optional[List[RevisionTarget]] = None


class SecondaryClusterInfo(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    ClusterNodes: Optional[List[ClusterNode]] = None


# This class is the output for the 'describe_cluster_parameters' function.
class ClusterParameterGroupDetails(BaseValidatorModel):
    Parameters: List[Parameter]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DefaultClusterParameters(BaseValidatorModel):
    ParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None


# This class is the input for the 'modify_cluster_parameter_group' function.
class ModifyClusterParameterGroupMessage(BaseValidatorModel):
    ParameterGroupName: str
    Parameters: List[Parameter]


# This class is the input for the 'reset_cluster_parameter_group' function.
class ResetClusterParameterGroupMessage(BaseValidatorModel):
    ParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[List[Parameter]] = None


class ClusterParameterGroupStatus(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ClusterParameterStatusList: Optional[List[ClusterParameterStatus]] = None


class ClusterParameterGroup(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cluster' function.
class CreateClusterMessage(BaseValidatorModel):
    ClusterIdentifier: str
    NodeType: str
    MasterUsername: str
    DBName: Optional[str] = None
    ClusterType: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    ClusterSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    ClusterSubnetGroupName: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ClusterParameterGroupName: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Port: Optional[int] = None
    ClusterVersion: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    NumberOfNodes: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    Encrypted: Optional[bool] = None
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    ElasticIp: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    IamRoles: Optional[List[str]] = None
    MaintenanceTrackName: Optional[str] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    AvailabilityZoneRelocation: Optional[bool] = None
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None
    DefaultIamRoleArn: Optional[str] = None
    LoadSampleData: Optional[str] = None
    ManageMasterPassword: Optional[bool] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[bool] = None
    RedshiftIdcApplicationArn: Optional[str] = None


# This class is the input for the 'create_cluster_parameter_group' function.
class CreateClusterParameterGroupMessage(BaseValidatorModel):
    ParameterGroupName: str
    ParameterGroupFamily: str
    Description: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cluster_security_group' function.
class CreateClusterSecurityGroupMessage(BaseValidatorModel):
    ClusterSecurityGroupName: str
    Description: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cluster_snapshot' function.
class CreateClusterSnapshotMessage(BaseValidatorModel):
    SnapshotIdentifier: str
    ClusterIdentifier: str
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cluster_subnet_group' function.
class CreateClusterSubnetGroupMessage(BaseValidatorModel):
    ClusterSubnetGroupName: str
    Description: str
    SubnetIds: List[str]
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_event_subscription' function.
class CreateEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    SourceIds: Optional[List[str]] = None
    EventCategories: Optional[List[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_hsm_client_certificate' function.
class CreateHsmClientCertificateMessage(BaseValidatorModel):
    HsmClientCertificateIdentifier: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_hsm_configuration' function.
class CreateHsmConfigurationMessage(BaseValidatorModel):
    HsmConfigurationIdentifier: str
    Description: str
    HsmIpAddress: str
    HsmPartitionName: str
    HsmPartitionPassword: str
    HsmServerPublicCertificate: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_integration' function.
class CreateIntegrationMessage(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    KMSKeyId: Optional[str] = None
    TagList: Optional[List[Tag]] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Description: Optional[str] = None


# This class is the input for the 'create_snapshot_copy_grant' function.
class CreateSnapshotCopyGrantMessage(BaseValidatorModel):
    SnapshotCopyGrantName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_snapshot_schedule' function.
class CreateSnapshotScheduleMessage(BaseValidatorModel):
    ScheduleDefinitions: Optional[List[str]] = None
    ScheduleIdentifier: Optional[str] = None
    ScheduleDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DryRun: Optional[bool] = None
    NextInvocations: Optional[int] = None


# This class is the input for the 'create_tags' function.
class CreateTagsMessage(BaseValidatorModel):
    ResourceName: str
    Tags: List[Tag]


# This class is the input for the 'create_usage_limit' function.
class CreateUsageLimitMessage(BaseValidatorModel):
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: Optional[UsageLimitPeriodType] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None
    Tags: Optional[List[Tag]] = None


class EC2SecurityGroup(BaseValidatorModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class EventSubscription(BaseValidatorModel):
    CustomerAwsId: Optional[str] = None
    CustSubscriptionId: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[datetime] = None
    SourceType: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    EventCategoriesList: Optional[List[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class HsmClientCertificate(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmClientCertificatePublicKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class HsmConfiguration(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    Description: Optional[str] = None
    HsmIpAddress: Optional[str] = None
    HsmPartitionName: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class IPRange(BaseValidatorModel):
    Status: Optional[str] = None
    CIDRIP: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class SnapshotCopyGrant(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'modify_snapshot_schedule' function.
class SnapshotScheduleResponse(BaseValidatorModel):
    ScheduleDefinitions: List[str]
    ScheduleIdentifier: str
    ScheduleDescription: str
    Tags: List[Tag]
    NextInvocations: List[datetime]
    AssociatedClusterCount: int
    AssociatedClusters: List[ClusterAssociatedToSchedule]
    ResponseMetadata: ResponseMetadata


class SnapshotSchedule(BaseValidatorModel):
    ScheduleDefinitions: Optional[List[str]] = None
    ScheduleIdentifier: Optional[str] = None
    ScheduleDescription: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    NextInvocations: Optional[List[datetime]] = None
    AssociatedClusterCount: Optional[int] = None
    AssociatedClusters: Optional[List[ClusterAssociatedToSchedule]] = None


class Snapshot(BaseValidatorModel):
    SnapshotIdentifier: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[datetime] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    ClusterVersion: Optional[str] = None
    EngineFullVersion: Optional[str] = None
    SnapshotType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    DBName: Optional[str] = None
    VpcId: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    EncryptedWithHSM: Optional[bool] = None
    AccountsWithRestoreAccess: Optional[List[AccountWithRestoreAccess]] = None
    OwnerAccount: Optional[str] = None
    TotalBackupSizeInMegaBytes: Optional[float] = None
    ActualIncrementalBackupSizeInMegaBytes: Optional[float] = None
    BackupProgressInMegaBytes: Optional[float] = None
    CurrentBackupRateInMegaBytesPerSecond: Optional[float] = None
    EstimatedSecondsToCompletion: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None
    SourceRegion: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    RestorableNodeTypes: Optional[List[str]] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRemainingDays: Optional[int] = None
    SnapshotRetentionStartTime: Optional[datetime] = None
    MasterPasswordSecretArn: Optional[str] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    SnapshotArn: Optional[str] = None


class TaggedResource(BaseValidatorModel):
    Tag: Optional[Tag] = None
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None


# This class is the output for the 'modify_usage_limit' function.
class UsageLimitResponse(BaseValidatorModel):
    UsageLimitId: str
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: UsageLimitPeriodType
    BreachAction: UsageLimitBreachActionType
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UsageLimit(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    LimitType: Optional[UsageLimitLimitTypeType] = None
    Amount: Optional[int] = None
    Period: Optional[UsageLimitPeriodType] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_reserved_node_exchange_status' function.
class DescribeReservedNodeExchangeStatusOutputMessage(BaseValidatorModel):
    ReservedNodeExchangeStatusDetails: List[ReservedNodeExchangeStatus]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cluster_versions' function.
class ClusterVersionsMessage(BaseValidatorModel):
    Marker: str
    ClusterVersions: List[ClusterVersion]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'describe_events' function.
class DescribeEventsMessage(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'modify_cluster_maintenance' function.
class ModifyClusterMaintenanceMessage(BaseValidatorModel):
    ClusterIdentifier: str
    DeferMaintenance: Optional[bool] = None
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[Timestamp] = None
    DeferMaintenanceEndTime: Optional[Timestamp] = None
    DeferMaintenanceDuration: Optional[int] = None


# This class is the output for the 'reject_data_share' function.
class DataShareResponse(BaseValidatorModel):
    DataShareArn: str
    ProducerArn: str
    AllowPubliclyAccessibleConsumers: bool
    DataShareAssociations: List[DataShareAssociation]
    ManagedBy: str
    DataShareType: Literal['INTERNAL']
    ResponseMetadata: ResponseMetadata


class DataShare(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    ProducerArn: Optional[str] = None
    AllowPubliclyAccessibleConsumers: Optional[bool] = None
    DataShareAssociations: Optional[List[DataShareAssociation]] = None
    ManagedBy: Optional[str] = None
    DataShareType: Optional[Literal['INTERNAL']] = None


class DescribeClusterDbRevisionsMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterParameterGroupsMessagePaginate(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterParametersMessagePaginate(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterSecurityGroupsMessagePaginate(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterSubnetGroupsMessagePaginate(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterTracksMessagePaginate(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterVersionsMessagePaginate(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClustersMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCustomDomainAssociationsMessagePaginate(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDataSharesForConsumerMessagePaginate(BaseValidatorModel):
    ConsumerArn: Optional[str] = None
    Status: Optional[DataShareStatusForConsumerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDataSharesForProducerMessagePaginate(BaseValidatorModel):
    ProducerArn: Optional[str] = None
    Status: Optional[DataShareStatusForProducerType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDataSharesMessagePaginate(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDefaultClusterParametersMessagePaginate(BaseValidatorModel):
    ParameterGroupFamily: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEndpointAccessMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    EndpointName: Optional[str] = None
    VpcId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEndpointAuthorizationMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    Grantee: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventSubscriptionsMessagePaginate(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsMessagePaginate(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeHsmClientCertificatesMessagePaginate(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeHsmConfigurationsMessagePaginate(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeInboundIntegrationsMessagePaginate(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    TargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrderableClusterOptionsMessagePaginate(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    NodeType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRedshiftIdcApplicationsMessagePaginate(BaseValidatorModel):
    RedshiftIdcApplicationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedNodeExchangeStatusInputMessagePaginate(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeExchangeRequestId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedNodeOfferingsMessagePaginate(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedNodesMessagePaginate(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotCopyGrantsMessagePaginate(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotSchedulesMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleIdentifier: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTableRestoreStatusMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TableRestoreRequestId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTagsMessagePaginate(BaseValidatorModel):
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUsageLimitsMessagePaginate(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetReservedNodeExchangeConfigurationOptionsInputMessagePaginate(BaseValidatorModel):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetReservedNodeExchangeOfferingsInputMessagePaginate(BaseValidatorModel):
    ReservedNodeId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecommendationsMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClusterSnapshotsMessagePaginate(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[List[SnapshotSortingEntity]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_cluster_snapshots' function.
class DescribeClusterSnapshotsMessage(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[List[SnapshotSortingEntity]] = None


class DescribeClusterSnapshotsMessageWait(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[List[SnapshotSortingEntity]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClustersMessageWaitExtraExtra(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClustersMessageWaitExtra(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClustersMessageWait(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[List[str]] = None
    TagValues: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeIntegrationsMessagePaginate(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    Filters: Optional[List[DescribeIntegrationsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_integrations' function.
class DescribeIntegrationsMessage(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    Filters: Optional[List[DescribeIntegrationsFilter]] = None


class DescribeNodeConfigurationOptionsMessagePaginate(BaseValidatorModel):
    ActionType: ActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    Filters: Optional[List[NodeConfigurationOptionsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_node_configuration_options' function.
class DescribeNodeConfigurationOptionsMessage(BaseValidatorModel):
    ActionType: ActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    Filters: Optional[List[NodeConfigurationOptionsFilter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the output for the 'describe_partners' function.
class DescribePartnersOutputMessage(BaseValidatorModel):
    PartnerIntegrationInfoList: List[PartnerIntegrationInfo]
    ResponseMetadata: ResponseMetadata


class DescribeScheduledActionsMessagePaginate(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetActionType: Optional[ScheduledActionTypeValuesType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Active: Optional[bool] = None
    Filters: Optional[List[ScheduledActionFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_scheduled_actions' function.
class DescribeScheduledActionsMessage(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetActionType: Optional[ScheduledActionTypeValuesType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Active: Optional[bool] = None
    Filters: Optional[List[ScheduledActionFilter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the output for the 'describe_endpoint_authorization' function.
class EndpointAuthorizationList(BaseValidatorModel):
    EndpointAuthorizationList: List[EndpointAuthorization]
    Marker: str
    ResponseMetadata: ResponseMetadata


class EventCategoriesMap(BaseValidatorModel):
    SourceType: Optional[str] = None
    Events: Optional[List[EventInfoMap]] = None


# This class is the output for the 'describe_events' function.
class EventsMessage(BaseValidatorModel):
    Marker: str
    Events: List[Event]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResult(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResult(BaseValidatorModel):
    ResourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class InboundIntegration(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    SourceArn: Optional[str] = None
    TargetArn: Optional[str] = None
    Status: Optional[ZeroETLIntegrationStatusType] = None
    Errors: Optional[List[IntegrationError]] = None
    CreateTime: Optional[datetime] = None


# This class is the output for the 'modify_integration' function.
class IntegrationResponse(BaseValidatorModel):
    IntegrationArn: str
    IntegrationName: str
    SourceArn: str
    TargetArn: str
    Status: ZeroETLIntegrationStatusType
    Errors: List[IntegrationError]
    CreateTime: datetime
    Description: str
    KMSKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class Integration(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    IntegrationName: Optional[str] = None
    SourceArn: Optional[str] = None
    TargetArn: Optional[str] = None
    Status: Optional[ZeroETLIntegrationStatusType] = None
    Errors: Optional[List[IntegrationError]] = None
    CreateTime: Optional[datetime] = None
    Description: Optional[str] = None
    KMSKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None


class LakeFormationScopeUnion(BaseValidatorModel):
    LakeFormationQuery: Optional[LakeFormationQuery] = None


class NamespaceIdentifierUnion(BaseValidatorModel):
    ServerlessIdentifier: Optional[ServerlessIdentifier] = None
    ProvisionedIdentifier: Optional[ProvisionedIdentifier] = None


class VpcEndpoint(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    NetworkInterfaces: Optional[List[NetworkInterface]] = None


# This class is the output for the 'describe_node_configuration_options' function.
class NodeConfigurationOptionsMessage(BaseValidatorModel):
    NodeConfigurationOptionList: List[NodeConfigurationOption]
    Marker: str
    ResponseMetadata: ResponseMetadata


class S3AccessGrantsScopeUnion(BaseValidatorModel):
    ReadWriteAccess: Optional[ReadWriteAccess] = None


class Recommendation(BaseValidatorModel):
    Id: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    RecommendationType: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    Observation: Optional[str] = None
    ImpactRanking: Optional[ImpactRankingTypeType] = None
    RecommendationText: Optional[str] = None
    RecommendedActions: Optional[List[RecommendedAction]] = None
    ReferenceLinks: Optional[List[ReferenceLink]] = None


class ReservedNodeOffering(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None
    ReservedNodeOfferingType: Optional[ReservedNodeOfferingTypeType] = None


class ReservedNode(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    NodeCount: Optional[int] = None
    State: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None
    ReservedNodeOfferingType: Optional[ReservedNodeOfferingTypeType] = None


# This class is the output for the 'restore_table_from_cluster_snapshot' function.
class RestoreTableFromClusterSnapshotResult(BaseValidatorModel):
    TableRestoreStatus: TableRestoreStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_table_restore_status' function.
class TableRestoreStatusMessage(BaseValidatorModel):
    TableRestoreStatusDetails: List[TableRestoreStatus]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ScheduledActionType(BaseValidatorModel):
    ResizeCluster: Optional[ResizeClusterMessage] = None
    PauseCluster: Optional[PauseClusterMessage] = None
    ResumeCluster: Optional[ResumeClusterMessage] = None


class UpdateTarget(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    DatabaseVersion: Optional[str] = None
    SupportedOperations: Optional[List[SupportedOperation]] = None


# This class is the output for the 'describe_account_attributes' function.
class AccountAttributeList(BaseValidatorModel):
    AccountAttributes: List[AccountAttribute]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_custom_domain_associations' function.
class CustomDomainAssociationsMessage(BaseValidatorModel):
    Marker: str
    Associations: List[Association]
    ResponseMetadata: ResponseMetadata


class OrderableClusterOption(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZone]] = None


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZone] = None
    SubnetStatus: Optional[str] = None


# This class is the output for the 'describe_cluster_db_revisions' function.
class ClusterDbRevisionsMessage(BaseValidatorModel):
    Marker: str
    ClusterDbRevisions: List[ClusterDbRevision]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_default_cluster_parameters' function.
class DescribeDefaultClusterParametersResult(BaseValidatorModel):
    DefaultClusterParameters: DefaultClusterParameters
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cluster_parameter_groups' function.
class ClusterParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    ParameterGroups: List[ClusterParameterGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster_parameter_group' function.
class CreateClusterParameterGroupResult(BaseValidatorModel):
    ClusterParameterGroup: ClusterParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_event_subscription' function.
class CreateEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_subscriptions' function.
class EventSubscriptionsMessage(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscription]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_event_subscription' function.
class ModifyEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hsm_client_certificate' function.
class CreateHsmClientCertificateResult(BaseValidatorModel):
    HsmClientCertificate: HsmClientCertificate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_hsm_client_certificates' function.
class HsmClientCertificateMessage(BaseValidatorModel):
    Marker: str
    HsmClientCertificates: List[HsmClientCertificate]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hsm_configuration' function.
class CreateHsmConfigurationResult(BaseValidatorModel):
    HsmConfiguration: HsmConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_hsm_configurations' function.
class HsmConfigurationMessage(BaseValidatorModel):
    Marker: str
    HsmConfigurations: List[HsmConfiguration]
    ResponseMetadata: ResponseMetadata


class ClusterSecurityGroup(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Description: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroup]] = None
    IPRanges: Optional[List[IPRange]] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_snapshot_copy_grant' function.
class CreateSnapshotCopyGrantResult(BaseValidatorModel):
    SnapshotCopyGrant: SnapshotCopyGrant
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_snapshot_copy_grants' function.
class SnapshotCopyGrantMessage(BaseValidatorModel):
    Marker: str
    SnapshotCopyGrants: List[SnapshotCopyGrant]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_snapshot_schedules' function.
class DescribeSnapshotSchedulesOutputMessage(BaseValidatorModel):
    SnapshotSchedules: List[SnapshotSchedule]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'authorize_snapshot_access' function.
class AuthorizeSnapshotAccessResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_cluster_snapshot' function.
class CopyClusterSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster_snapshot' function.
class CreateClusterSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cluster_snapshot' function.
class DeleteClusterSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cluster_snapshot' function.
class ModifyClusterSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'revoke_snapshot_access' function.
class RevokeSnapshotAccessResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cluster_snapshots' function.
class SnapshotMessage(BaseValidatorModel):
    Marker: str
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_tags' function.
class TaggedResourceListMessage(BaseValidatorModel):
    TaggedResources: List[TaggedResource]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_usage_limits' function.
class UsageLimitList(BaseValidatorModel):
    UsageLimits: List[UsageLimit]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_data_shares_for_consumer' function.
class DescribeDataSharesForConsumerResult(BaseValidatorModel):
    DataShares: List[DataShare]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_data_shares_for_producer' function.
class DescribeDataSharesForProducerResult(BaseValidatorModel):
    DataShares: List[DataShare]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_data_shares' function.
class DescribeDataSharesResult(BaseValidatorModel):
    DataShares: List[DataShare]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_categories' function.
class EventCategoriesMessage(BaseValidatorModel):
    EventCategoriesMapList: List[EventCategoriesMap]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_inbound_integrations' function.
class InboundIntegrationsMessage(BaseValidatorModel):
    Marker: str
    InboundIntegrations: List[InboundIntegration]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_integrations' function.
class IntegrationsMessage(BaseValidatorModel):
    Marker: str
    Integrations: List[Integration]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'deregister_namespace' function.
class DeregisterNamespaceInputMessage(BaseValidatorModel):
    NamespaceIdentifier: NamespaceIdentifierUnion
    ConsumerIdentifiers: List[str]


# This class is the input for the 'register_namespace' function.
class RegisterNamespaceInputMessage(BaseValidatorModel):
    NamespaceIdentifier: NamespaceIdentifierUnion
    ConsumerIdentifiers: List[str]


# This class is the output for the 'modify_endpoint_access' function.
class EndpointAccessResponse(BaseValidatorModel):
    ClusterIdentifier: str
    ResourceOwner: str
    SubnetGroupName: str
    EndpointStatus: str
    EndpointName: str
    EndpointCreateTime: datetime
    Port: int
    Address: str
    VpcSecurityGroups: List[VpcSecurityGroupMembership]
    VpcEndpoint: VpcEndpoint
    ResponseMetadata: ResponseMetadata


class EndpointAccess(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    SubnetGroupName: Optional[str] = None
    EndpointStatus: Optional[str] = None
    EndpointName: Optional[str] = None
    EndpointCreateTime: Optional[datetime] = None
    Port: Optional[int] = None
    Address: Optional[str] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    VpcEndpoint: Optional[VpcEndpoint] = None


class Endpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    VpcEndpoints: Optional[List[VpcEndpoint]] = None


class ServiceIntegrationsUnionOutput(BaseValidatorModel):
    LakeFormation: Optional[List[LakeFormationScopeUnion]] = None
    S3AccessGrants: Optional[List[S3AccessGrantsScopeUnion]] = None


class ServiceIntegrationsUnion(BaseValidatorModel):
    LakeFormation: Optional[List[LakeFormationScopeUnion]] = None
    S3AccessGrants: Optional[List[S3AccessGrantsScopeUnion]] = None


# This class is the output for the 'list_recommendations' function.
class ListRecommendationsResult(BaseValidatorModel):
    Recommendations: List[Recommendation]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_reserved_node_exchange_offerings' function.
class GetReservedNodeExchangeOfferingsOutputMessage(BaseValidatorModel):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOffering]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_node_offerings' function.
class ReservedNodeOfferingsMessage(BaseValidatorModel):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOffering]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_reserved_node_exchange' function.
class AcceptReservedNodeExchangeOutputMessage(BaseValidatorModel):
    ExchangedReservedNode: ReservedNode
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'purchase_reserved_node_offering' function.
class PurchaseReservedNodeOfferingResult(BaseValidatorModel):
    ReservedNode: ReservedNode
    ResponseMetadata: ResponseMetadata


class ReservedNodeConfigurationOption(BaseValidatorModel):
    SourceReservedNode: Optional[ReservedNode] = None
    TargetReservedNodeCount: Optional[int] = None
    TargetReservedNodeOffering: Optional[ReservedNodeOffering] = None


# This class is the output for the 'describe_reserved_nodes' function.
class ReservedNodesMessage(BaseValidatorModel):
    Marker: str
    ReservedNodes: List[ReservedNode]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_scheduled_action' function.
class CreateScheduledActionMessage(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: ScheduledActionType
    Schedule: str
    IamRole: str
    ScheduledActionDescription: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Enable: Optional[bool] = None


# This class is the input for the 'modify_scheduled_action' function.
class ModifyScheduledActionMessage(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: Optional[ScheduledActionType] = None
    Schedule: Optional[str] = None
    IamRole: Optional[str] = None
    ScheduledActionDescription: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Enable: Optional[bool] = None


# This class is the output for the 'modify_scheduled_action' function.
class ScheduledActionResponse(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: ScheduledActionType
    Schedule: str
    IamRole: str
    ScheduledActionDescription: str
    State: ScheduledActionStateType
    NextInvocations: List[datetime]
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadata


class ScheduledAction(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetAction: Optional[ScheduledActionType] = None
    Schedule: Optional[str] = None
    IamRole: Optional[str] = None
    ScheduledActionDescription: Optional[str] = None
    State: Optional[ScheduledActionStateType] = None
    NextInvocations: Optional[List[datetime]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class MaintenanceTrack(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    DatabaseVersion: Optional[str] = None
    UpdateTargets: Optional[List[UpdateTarget]] = None


# This class is the output for the 'describe_orderable_cluster_options' function.
class OrderableClusterOptionsMessage(BaseValidatorModel):
    OrderableClusterOptions: List[OrderableClusterOption]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ClusterSubnetGroup(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[Subnet]] = None
    Tags: Optional[List[Tag]] = None
    SupportedClusterIpAddressTypes: Optional[List[str]] = None


# This class is the output for the 'authorize_cluster_security_group_ingress' function.
class AuthorizeClusterSecurityGroupIngressResult(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cluster_security_groups' function.
class ClusterSecurityGroupMessage(BaseValidatorModel):
    Marker: str
    ClusterSecurityGroups: List[ClusterSecurityGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster_security_group' function.
class CreateClusterSecurityGroupResult(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'revoke_cluster_security_group_ingress' function.
class RevokeClusterSecurityGroupIngressResult(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_endpoint_access' function.
class EndpointAccessList(BaseValidatorModel):
    EndpointAccessList: List[EndpointAccess]
    Marker: str
    ResponseMetadata: ResponseMetadata


class Cluster(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NodeType: Optional[str] = None
    ClusterStatus: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ModifyStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    DBName: Optional[str] = None
    Endpoint: Optional[Endpoint] = None
    ClusterCreateTime: Optional[datetime] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    ClusterSecurityGroups: Optional[List[ClusterSecurityGroupMembership]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    ClusterParameterGroups: Optional[List[ClusterParameterGroupStatus]] = None
    ClusterSubnetGroupName: Optional[str] = None
    VpcId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValues] = None
    ClusterVersion: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    NumberOfNodes: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    Encrypted: Optional[bool] = None
    RestoreStatus: Optional[RestoreStatus] = None
    DataTransferProgress: Optional[DataTransferProgress] = None
    HsmStatus: Optional[HsmStatus] = None
    ClusterSnapshotCopyStatus: Optional[ClusterSnapshotCopyStatus] = None
    ClusterPublicKey: Optional[str] = None
    ClusterNodes: Optional[List[ClusterNode]] = None
    ElasticIpStatus: Optional[ElasticIpStatus] = None
    ClusterRevisionNumber: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    IamRoles: Optional[List[ClusterIamRole]] = None
    PendingActions: Optional[List[str]] = None
    MaintenanceTrackName: Optional[str] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    DeferredMaintenanceWindows: Optional[List[DeferredMaintenanceWindow]] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[ScheduleStateType] = None
    ExpectedNextSnapshotScheduleTime: Optional[datetime] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[datetime] = None
    ResizeInfo: Optional[ResizeInfo] = None
    AvailabilityZoneRelocationStatus: Optional[str] = None
    ClusterNamespaceArn: Optional[str] = None
    TotalStorageCapacityInMegaBytes: Optional[int] = None
    AquaConfiguration: Optional[AquaConfiguration] = None
    DefaultIamRoleArn: Optional[str] = None
    ReservedNodeExchangeStatus: Optional[ReservedNodeExchangeStatus] = None
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    CustomDomainCertificateExpiryDate: Optional[datetime] = None
    MasterPasswordSecretArn: Optional[str] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[str] = None
    MultiAZSecondary: Optional[SecondaryClusterInfo] = None


class RedshiftIdcApplication(BaseValidatorModel):
    IdcInstanceArn: Optional[str] = None
    RedshiftIdcApplicationName: Optional[str] = None
    RedshiftIdcApplicationArn: Optional[str] = None
    IdentityNamespace: Optional[str] = None
    IdcDisplayName: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IdcManagedApplicationArn: Optional[str] = None
    IdcOnboardStatus: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[List[AuthorizedTokenIssuerOutput]] = None
    ServiceIntegrations: Optional[List[ServiceIntegrationsUnionOutput]] = None

ServiceIntegrationsUnionUnion = Union[ServiceIntegrationsUnion, ServiceIntegrationsUnionOutput]


# This class is the output for the 'get_reserved_node_exchange_configuration_options' function.
class GetReservedNodeExchangeConfigurationOptionsOutputMessage(BaseValidatorModel):
    Marker: str
    ReservedNodeConfigurationOptionList: List[ReservedNodeConfigurationOption]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_scheduled_actions' function.
class ScheduledActionsMessage(BaseValidatorModel):
    Marker: str
    ScheduledActions: List[ScheduledAction]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cluster_tracks' function.
class TrackListMessage(BaseValidatorModel):
    MaintenanceTracks: List[MaintenanceTrack]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cluster_subnet_groups' function.
class ClusterSubnetGroupMessage(BaseValidatorModel):
    Marker: str
    ClusterSubnetGroups: List[ClusterSubnetGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster_subnet_group' function.
class CreateClusterSubnetGroupResult(BaseValidatorModel):
    ClusterSubnetGroup: ClusterSubnetGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cluster_subnet_group' function.
class ModifyClusterSubnetGroupResult(BaseValidatorModel):
    ClusterSubnetGroup: ClusterSubnetGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_clusters' function.
class ClustersMessage(BaseValidatorModel):
    Marker: str
    Clusters: List[Cluster]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster' function.
class CreateClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cluster' function.
class DeleteClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_snapshot_copy' function.
class DisableSnapshotCopyResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_snapshot_copy' function.
class EnableSnapshotCopyResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'failover_primary_compute' function.
class FailoverPrimaryComputeResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cluster_db_revision' function.
class ModifyClusterDbRevisionResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cluster_iam_roles' function.
class ModifyClusterIamRolesResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cluster_maintenance' function.
class ModifyClusterMaintenanceResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cluster' function.
class ModifyClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_snapshot_copy_retention_period' function.
class ModifySnapshotCopyRetentionPeriodResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'pause_cluster' function.
class PauseClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reboot_cluster' function.
class RebootClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'resize_cluster' function.
class ResizeClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_from_cluster_snapshot' function.
class RestoreFromClusterSnapshotResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'resume_cluster' function.
class ResumeClusterResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rotate_encryption_key' function.
class RotateEncryptionKeyResult(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_redshift_idc_application' function.
class CreateRedshiftIdcApplicationResult(BaseValidatorModel):
    RedshiftIdcApplication: RedshiftIdcApplication
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_redshift_idc_applications' function.
class DescribeRedshiftIdcApplicationsResult(BaseValidatorModel):
    RedshiftIdcApplications: List[RedshiftIdcApplication]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_redshift_idc_application' function.
class ModifyRedshiftIdcApplicationResult(BaseValidatorModel):
    RedshiftIdcApplication: RedshiftIdcApplication
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_redshift_idc_application' function.
class CreateRedshiftIdcApplicationMessage(BaseValidatorModel):
    IdcInstanceArn: str
    RedshiftIdcApplicationName: str
    IdcDisplayName: str
    IamRoleArn: str
    IdentityNamespace: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[List[AuthorizedTokenIssuerUnion]] = None
    ServiceIntegrations: Optional[List[ServiceIntegrationsUnionUnion]] = None


# This class is the input for the 'modify_redshift_idc_application' function.
class ModifyRedshiftIdcApplicationMessage(BaseValidatorModel):
    RedshiftIdcApplicationArn: str
    IdentityNamespace: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IdcDisplayName: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[List[AuthorizedTokenIssuerUnion]] = None
    ServiceIntegrations: Optional[List[ServiceIntegrationsUnionUnion]] = None
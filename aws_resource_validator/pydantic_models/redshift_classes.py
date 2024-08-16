from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.redshift_constants import *

class AcceptReservedNodeExchangeInputMessageRequestTypeDef(BaseValidatorModel):
    ReservedNodeId: str
    TargetReservedNodeOfferingId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AttributeValueTargetTypeDef(BaseValidatorModel):
    AttributeValue: Optional[str] = None

class AccountWithRestoreAccessTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    AccountAlias: Optional[str] = None

class AquaConfigurationTypeDef(BaseValidatorModel):
    AquaStatus: Optional[AquaStatusType] = None
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None

class AssociateDataShareConsumerMessageRequestTypeDef(BaseValidatorModel):
    DataShareArn: str
    AssociateEntireAccount: Optional[bool] = None
    ConsumerArn: Optional[str] = None
    ConsumerRegion: Optional[str] = None
    AllowWrites: Optional[bool] = None

class CertificateAssociationTypeDef(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None

class AuthenticationProfileTypeDef(BaseValidatorModel):
    AuthenticationProfileName: Optional[str] = None
    AuthenticationProfileContent: Optional[str] = None

class AuthorizeClusterSecurityGroupIngressMessageRequestTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class AuthorizeDataShareMessageRequestTypeDef(BaseValidatorModel):
    DataShareArn: str
    ConsumerIdentifier: str
    AllowWrites: Optional[bool] = None

class AuthorizeEndpointAccessMessageRequestTypeDef(BaseValidatorModel):
    Account: str
    ClusterIdentifier: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None

class AuthorizeSnapshotAccessMessageRequestTypeDef(BaseValidatorModel):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None

class AuthorizedTokenIssuerExtraOutputTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[List[str]] = None

class AuthorizedTokenIssuerOutputTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[List[str]] = None

class AuthorizedTokenIssuerTypeDef(BaseValidatorModel):
    TrustedTokenIssuerArn: Optional[str] = None
    AuthorizedAudiencesList: Optional[Sequence[str]] = None

class SupportedPlatformTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class DeleteClusterSnapshotMessageTypeDef(BaseValidatorModel):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: Optional[str] = None

class SnapshotErrorMessageTypeDef(BaseValidatorModel):
    SnapshotIdentifier: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None
    FailureCode: Optional[str] = None
    FailureReason: Optional[str] = None

class BatchModifyClusterSnapshotsMessageRequestTypeDef(BaseValidatorModel):
    SnapshotIdentifierList: Sequence[str]
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Force: Optional[bool] = None

class CancelResizeMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class ClusterAssociatedToScheduleTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleAssociationState: Optional[ScheduleStateType] = None

class RevisionTargetTypeDef(BaseValidatorModel):
    DatabaseRevision: Optional[str] = None
    Description: Optional[str] = None
    DatabaseRevisionReleaseDate: Optional[datetime] = None

class ClusterIamRoleTypeDef(BaseValidatorModel):
    IamRoleArn: Optional[str] = None
    ApplyStatus: Optional[str] = None

class ClusterNodeTypeDef(BaseValidatorModel):
    NodeRole: Optional[str] = None
    PrivateIPAddress: Optional[str] = None
    PublicIPAddress: Optional[str] = None

class ParameterTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    ApplyType: Optional[ParameterApplyTypeType] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None

class ClusterParameterStatusTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterApplyErrorDescription: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ClusterSecurityGroupMembershipTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class ClusterSnapshotCopyStatusTypeDef(BaseValidatorModel):
    DestinationRegion: Optional[str] = None
    RetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None

class DataTransferProgressTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    CurrentRateInMegaBytesPerSecond: Optional[float] = None
    TotalDataInMegaBytes: Optional[int] = None
    DataTransferredInMegaBytes: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None

class DeferredMaintenanceWindowTypeDef(BaseValidatorModel):
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[datetime] = None
    DeferMaintenanceEndTime: Optional[datetime] = None

class ElasticIpStatusTypeDef(BaseValidatorModel):
    ElasticIp: Optional[str] = None
    Status: Optional[str] = None

class HsmStatusTypeDef(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    Status: Optional[str] = None

class PendingModifiedValuesTypeDef(BaseValidatorModel):
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

class ReservedNodeExchangeStatusTypeDef(BaseValidatorModel):
    ReservedNodeExchangeRequestId: Optional[str] = None
    Status: Optional[ReservedNodeExchangeStatusTypeType] = None
    RequestTime: Optional[datetime] = None
    SourceReservedNodeId: Optional[str] = None
    SourceReservedNodeType: Optional[str] = None
    SourceReservedNodeCount: Optional[int] = None
    TargetReservedNodeOfferingId: Optional[str] = None
    TargetReservedNodeType: Optional[str] = None
    TargetReservedNodeCount: Optional[int] = None

class ResizeInfoTypeDef(BaseValidatorModel):
    ResizeType: Optional[str] = None
    AllowCancelResize: Optional[bool] = None

class RestoreStatusTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    CurrentRestoreRateInMegaBytesPerSecond: Optional[float] = None
    SnapshotSizeInMegaBytes: Optional[int] = None
    ProgressInMegaBytes: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None

class VpcSecurityGroupMembershipTypeDef(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class ClusterVersionTypeDef(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None

class CopyClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    SourceSnapshotIdentifier: str
    TargetSnapshotIdentifier: str
    SourceSnapshotClusterIdentifier: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None

class CreateAuthenticationProfileMessageRequestTypeDef(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str

class CreateCustomDomainAssociationMessageRequestTypeDef(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str

class CreateEndpointAccessMessageRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    SubnetGroupName: str
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None

class DataShareAssociationTypeDef(BaseValidatorModel):
    ConsumerIdentifier: Optional[str] = None
    Status: Optional[DataShareStatusType] = None
    ConsumerRegion: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    StatusChangeDate: Optional[datetime] = None
    ProducerAllowedWrites: Optional[bool] = None
    ConsumerAcceptedWrites: Optional[bool] = None

class DeauthorizeDataShareMessageRequestTypeDef(BaseValidatorModel):
    DataShareArn: str
    ConsumerIdentifier: str

class DeleteAuthenticationProfileMessageRequestTypeDef(BaseValidatorModel):
    AuthenticationProfileName: str

class DeleteClusterMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    SkipFinalClusterSnapshot: Optional[bool] = None
    FinalClusterSnapshotIdentifier: Optional[str] = None
    FinalClusterSnapshotRetentionPeriod: Optional[int] = None

class DeleteClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str

class DeleteClusterSecurityGroupMessageRequestTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: str

class DeleteClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: Optional[str] = None

class DeleteClusterSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    ClusterSubnetGroupName: str

class DeleteCustomDomainAssociationMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    CustomDomainName: str

class DeleteEndpointAccessMessageRequestTypeDef(BaseValidatorModel):
    EndpointName: str

class DeleteEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str

class DeleteHsmClientCertificateMessageRequestTypeDef(BaseValidatorModel):
    HsmClientCertificateIdentifier: str

class DeleteHsmConfigurationMessageRequestTypeDef(BaseValidatorModel):
    HsmConfigurationIdentifier: str

class DeleteRedshiftIdcApplicationMessageRequestTypeDef(BaseValidatorModel):
    RedshiftIdcApplicationArn: str

class DeleteResourcePolicyMessageRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DeleteScheduledActionMessageRequestTypeDef(BaseValidatorModel):
    ScheduledActionName: str

class DeleteSnapshotCopyGrantMessageRequestTypeDef(BaseValidatorModel):
    SnapshotCopyGrantName: str

class DeleteSnapshotScheduleMessageRequestTypeDef(BaseValidatorModel):
    ScheduleIdentifier: str

class DeleteTagsMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]

class DeleteUsageLimitMessageRequestTypeDef(BaseValidatorModel):
    UsageLimitId: str

class DescribeAccountAttributesMessageRequestTypeDef(BaseValidatorModel):
    AttributeNames: Optional[Sequence[str]] = None

class DescribeAuthenticationProfilesMessageRequestTypeDef(BaseValidatorModel):
    AuthenticationProfileName: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeClusterDbRevisionsMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeClusterParameterGroupsMessageRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeClusterParametersMessageRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeClusterSecurityGroupsMessageRequestTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class SnapshotSortingEntityTypeDef(BaseValidatorModel):
    Attribute: SnapshotAttributeToSortByType
    SortOrder: Optional[SortByOrderType] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeClusterSubnetGroupsMessageRequestTypeDef(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeClusterTracksMessageRequestTypeDef(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeClusterVersionsMessageRequestTypeDef(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeClustersMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeCustomDomainAssociationsMessageRequestTypeDef(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDataSharesForConsumerMessageRequestTypeDef(BaseValidatorModel):
    ConsumerArn: Optional[str] = None
    Status: Optional[DataShareStatusForConsumerType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDataSharesForProducerMessageRequestTypeDef(BaseValidatorModel):
    ProducerArn: Optional[str] = None
    Status: Optional[DataShareStatusForProducerType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDataSharesMessageRequestTypeDef(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDefaultClusterParametersMessageRequestTypeDef(BaseValidatorModel):
    ParameterGroupFamily: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEndpointAccessMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    EndpointName: Optional[str] = None
    VpcId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEndpointAuthorizationMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    Grantee: Optional[bool] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEventCategoriesMessageRequestTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None

class DescribeEventSubscriptionsMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeHsmClientCertificatesMessageRequestTypeDef(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeHsmConfigurationsMessageRequestTypeDef(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeInboundIntegrationsMessageRequestTypeDef(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    TargetArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeLoggingStatusMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class NodeConfigurationOptionsFilterTypeDef(BaseValidatorModel):
    Name: Optional[NodeConfigurationOptionsFilterNameType] = None
    Operator: Optional[OperatorTypeType] = None
    Values: Optional[Sequence[str]] = None

class DescribeOrderableClusterOptionsMessageRequestTypeDef(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    NodeType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribePartnersInputMessageRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: Optional[str] = None
    PartnerName: Optional[str] = None

class PartnerIntegrationInfoTypeDef(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    PartnerName: Optional[str] = None
    Status: Optional[PartnerIntegrationStatusType] = None
    StatusMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class DescribeRedshiftIdcApplicationsMessageRequestTypeDef(BaseValidatorModel):
    RedshiftIdcApplicationArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedNodeExchangeStatusInputMessageRequestTypeDef(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeExchangeRequestId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedNodeOfferingsMessageRequestTypeDef(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedNodesMessageRequestTypeDef(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeResizeMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class ScheduledActionFilterTypeDef(BaseValidatorModel):
    Name: ScheduledActionFilterNameType
    Values: Sequence[str]

class DescribeSnapshotCopyGrantsMessageRequestTypeDef(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeSnapshotSchedulesMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribeTableRestoreStatusMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TableRestoreRequestId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeTagsMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DescribeUsageLimitsMessageRequestTypeDef(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None

class DisableLoggingMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class DisableSnapshotCopyMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class DisassociateDataShareConsumerMessageRequestTypeDef(BaseValidatorModel):
    DataShareArn: str
    DisassociateEntireAccount: Optional[bool] = None
    ConsumerArn: Optional[str] = None
    ConsumerRegion: Optional[str] = None

class EnableLoggingMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    BucketName: Optional[str] = None
    S3KeyPrefix: Optional[str] = None
    LogDestinationType: Optional[LogDestinationTypeType] = None
    LogExports: Optional[Sequence[str]] = None

class EnableSnapshotCopyMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    DestinationRegion: str
    RetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None

class EndpointAuthorizationTypeDef(BaseValidatorModel):
    Grantor: Optional[str] = None
    Grantee: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    AuthorizeTime: Optional[datetime] = None
    ClusterStatus: Optional[str] = None
    Status: Optional[AuthorizationStatusType] = None
    AllowedAllVPCs: Optional[bool] = None
    AllowedVPCs: Optional[List[str]] = None
    EndpointCount: Optional[int] = None

class EventInfoMapTypeDef(BaseValidatorModel):
    EventId: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    EventDescription: Optional[str] = None
    Severity: Optional[str] = None

class EventTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Severity: Optional[str] = None
    Date: Optional[datetime] = None
    EventId: Optional[str] = None

class FailoverPrimaryComputeInputMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class GetClusterCredentialsMessageRequestTypeDef(BaseValidatorModel):
    DbUser: str
    DbName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DurationSeconds: Optional[int] = None
    AutoCreate: Optional[bool] = None
    DbGroups: Optional[Sequence[str]] = None
    CustomDomainName: Optional[str] = None

class GetClusterCredentialsWithIAMMessageRequestTypeDef(BaseValidatorModel):
    DbName: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    DurationSeconds: Optional[int] = None
    CustomDomainName: Optional[str] = None

class GetReservedNodeExchangeConfigurationOptionsInputMessageRequestTypeDef(BaseValidatorModel):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class GetReservedNodeExchangeOfferingsInputMessageRequestTypeDef(BaseValidatorModel):
    ReservedNodeId: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class GetResourcePolicyMessageRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ResourcePolicyTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Policy: Optional[str] = None

class IntegrationErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    ErrorMessage: Optional[str] = None

class LakeFormationQueryTypeDef(BaseValidatorModel):
    Authorization: ServiceAuthorizationType

class ListRecommendationsMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class ModifyAquaInputMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    AquaConfigurationStatus: Optional[AquaConfigurationStatusType] = None

class ModifyAuthenticationProfileMessageRequestTypeDef(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str

class ModifyClusterDbRevisionMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    RevisionTarget: str

class ModifyClusterIamRolesMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    AddIamRoles: Optional[Sequence[str]] = None
    RemoveIamRoles: Optional[Sequence[str]] = None
    DefaultIamRoleArn: Optional[str] = None

class ModifyClusterMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    ClusterSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
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

class ModifyClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    SnapshotIdentifier: str
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Force: Optional[bool] = None

class ModifyClusterSnapshotScheduleMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    ScheduleIdentifier: Optional[str] = None
    DisassociateSchedule: Optional[bool] = None

class ModifyClusterSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    ClusterSubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None

class ModifyCustomDomainAssociationMessageRequestTypeDef(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str

class ModifyEndpointAccessMessageRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    VpcSecurityGroupIds: Optional[Sequence[str]] = None

class ModifyEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    SourceIds: Optional[Sequence[str]] = None
    EventCategories: Optional[Sequence[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None

class ModifySnapshotCopyRetentionPeriodMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    RetentionPeriod: int
    Manual: Optional[bool] = None

class ModifySnapshotScheduleMessageRequestTypeDef(BaseValidatorModel):
    ScheduleIdentifier: str
    ScheduleDefinitions: Sequence[str]

class ModifyUsageLimitMessageRequestTypeDef(BaseValidatorModel):
    UsageLimitId: str
    Amount: Optional[int] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None

class NetworkInterfaceTypeDef(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    SubnetId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Ipv6Address: Optional[str] = None

class NodeConfigurationOptionTypeDef(BaseValidatorModel):
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    EstimatedDiskUtilizationPercent: Optional[float] = None
    Mode: Optional[ModeType] = None

class PartnerIntegrationInputMessageRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str

class PauseClusterMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class PauseClusterMessageTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class PurchaseReservedNodeOfferingMessageRequestTypeDef(BaseValidatorModel):
    ReservedNodeOfferingId: str
    NodeCount: Optional[int] = None

class PutResourcePolicyMessageRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str

class RebootClusterMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class RecommendedActionTypeDef(BaseValidatorModel):
    Text: Optional[str] = None
    Database: Optional[str] = None
    Command: Optional[str] = None
    Type: Optional[RecommendedActionTypeType] = None

class ReferenceLinkTypeDef(BaseValidatorModel):
    Text: Optional[str] = None
    Link: Optional[str] = None

class RecurringChargeTypeDef(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class RejectDataShareMessageRequestTypeDef(BaseValidatorModel):
    DataShareArn: str

class ResizeClusterMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    Classic: Optional[bool] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None

class ResizeClusterMessageTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    Classic: Optional[bool] = None
    ReservedNodeId: Optional[str] = None
    TargetReservedNodeOfferingId: Optional[str] = None

class RestoreFromClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
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
    ClusterSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    KmsKeyId: Optional[str] = None
    NodeType: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    IamRoles: Optional[Sequence[str]] = None
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

class RestoreTableFromClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    SnapshotIdentifier: str
    SourceDatabaseName: str
    SourceTableName: str
    NewTableName: str
    SourceSchemaName: Optional[str] = None
    TargetDatabaseName: Optional[str] = None
    TargetSchemaName: Optional[str] = None
    EnableCaseSensitiveIdentifier: Optional[bool] = None

class TableRestoreStatusTypeDef(BaseValidatorModel):
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

class ResumeClusterMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class ResumeClusterMessageTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class RevokeClusterSecurityGroupIngressMessageRequestTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: str
    CIDRIP: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class RevokeEndpointAccessMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None
    Force: Optional[bool] = None

class RevokeSnapshotAccessMessageRequestTypeDef(BaseValidatorModel):
    AccountWithRestoreAccess: str
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotClusterIdentifier: Optional[str] = None

class RotateEncryptionKeyMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str

class SupportedOperationTypeDef(BaseValidatorModel):
    OperationName: Optional[str] = None

class UpdatePartnerStatusInputMessageRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ClusterIdentifier: str
    DatabaseName: str
    PartnerName: str
    Status: PartnerIntegrationStatusType
    StatusMessage: Optional[str] = None

class ClusterCredentialsTypeDef(BaseValidatorModel):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterExtendedCredentialsTypeDef(BaseValidatorModel):
    DbUser: str
    DbPassword: str
    Expiration: datetime
    NextRefreshTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterParameterGroupNameMessageTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    ParameterGroupStatus: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAuthenticationProfileResultTypeDef(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomDomainAssociationResultTypeDef(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class CustomerStorageMessageTypeDef(BaseValidatorModel):
    TotalBackupSizeInMegaBytes: float
    TotalProvisionedStorageInMegaBytes: float
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAuthenticationProfileResultTypeDef(BaseValidatorModel):
    AuthenticationProfileName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointAuthorizationResponseTypeDef(BaseValidatorModel):
    Grantor: str
    Grantee: str
    ClusterIdentifier: str
    AuthorizeTime: datetime
    ClusterStatus: str
    Status: AuthorizationStatusType
    AllowedAllVPCs: bool
    AllowedVPCs: List[str]
    EndpointCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingStatusTypeDef(BaseValidatorModel):
    LoggingEnabled: bool
    BucketName: str
    S3KeyPrefix: str
    LastSuccessfulDeliveryTime: datetime
    LastFailureTime: datetime
    LastFailureMessage: str
    LogDestinationType: LogDestinationTypeType
    LogExports: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyAuthenticationProfileResultTypeDef(BaseValidatorModel):
    AuthenticationProfileName: str
    AuthenticationProfileContent: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCustomDomainAssociationResultTypeDef(BaseValidatorModel):
    CustomDomainName: str
    CustomDomainCertificateArn: str
    ClusterIdentifier: str
    CustomDomainCertExpiryTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class PartnerIntegrationOutputMessageTypeDef(BaseValidatorModel):
    DatabaseName: str
    PartnerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResizeProgressMessageTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class AccountAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[AttributeValueTargetTypeDef]] = None

class ModifyAquaOutputMessageTypeDef(BaseValidatorModel):
    AquaConfiguration: AquaConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociationTypeDef(BaseValidatorModel):
    CustomDomainCertificateArn: Optional[str] = None
    CustomDomainCertificateExpiryDate: Optional[datetime] = None
    CertificateAssociations: Optional[List[CertificateAssociationTypeDef]] = None

class DescribeAuthenticationProfilesResultTypeDef(BaseValidatorModel):
    AuthenticationProfiles: List[AuthenticationProfileTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    SupportedPlatforms: Optional[List[SupportedPlatformTypeDef]] = None

class BatchDeleteClusterSnapshotsRequestRequestTypeDef(BaseValidatorModel):
    Identifiers: Sequence[DeleteClusterSnapshotMessageTypeDef]

class BatchDeleteClusterSnapshotsResultTypeDef(BaseValidatorModel):
    Resources: List[str]
    Errors: List[SnapshotErrorMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchModifyClusterSnapshotsOutputMessageTypeDef(BaseValidatorModel):
    Resources: List[str]
    Errors: List[SnapshotErrorMessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterDbRevisionTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    CurrentDatabaseRevision: Optional[str] = None
    DatabaseRevisionReleaseDate: Optional[datetime] = None
    RevisionTargets: Optional[List[RevisionTargetTypeDef]] = None

class SecondaryClusterInfoTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    ClusterNodes: Optional[List[ClusterNodeTypeDef]] = None

class ClusterParameterGroupDetailsTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DefaultClusterParametersTypeDef(BaseValidatorModel):
    ParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None

class ModifyClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ResetClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None

class ClusterParameterGroupStatusTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ClusterParameterStatusList: Optional[List[ClusterParameterStatusTypeDef]] = None

class ClusterParameterGroupTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateClusterMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    NodeType: str
    MasterUsername: str
    DBName: Optional[str] = None
    ClusterType: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    ClusterSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
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
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    IamRoles: Optional[Sequence[str]] = None
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

class CreateClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    ParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateClusterSecurityGroupMessageRequestTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    SnapshotIdentifier: str
    ClusterIdentifier: str
    ManualSnapshotRetentionPeriod: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateClusterSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    ClusterSubnetGroupName: str
    Description: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    SourceIds: Optional[Sequence[str]] = None
    EventCategories: Optional[Sequence[str]] = None
    Severity: Optional[str] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateHsmClientCertificateMessageRequestTypeDef(BaseValidatorModel):
    HsmClientCertificateIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateHsmConfigurationMessageRequestTypeDef(BaseValidatorModel):
    HsmConfigurationIdentifier: str
    Description: str
    HsmIpAddress: str
    HsmPartitionName: str
    HsmPartitionPassword: str
    HsmServerPublicCertificate: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotCopyGrantMessageRequestTypeDef(BaseValidatorModel):
    SnapshotCopyGrantName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotScheduleMessageRequestTypeDef(BaseValidatorModel):
    ScheduleDefinitions: Optional[Sequence[str]] = None
    ScheduleIdentifier: Optional[str] = None
    ScheduleDescription: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None
    NextInvocations: Optional[int] = None

class CreateTagsMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CreateUsageLimitMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: Optional[UsageLimitPeriodType] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class EC2SecurityGroupTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class EventSubscriptionTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None

class HsmClientCertificateTypeDef(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmClientCertificatePublicKey: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class HsmConfigurationTypeDef(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    Description: Optional[str] = None
    HsmIpAddress: Optional[str] = None
    HsmPartitionName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class IPRangeTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    CIDRIP: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class SnapshotCopyGrantTypeDef(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class SnapshotScheduleResponseTypeDef(BaseValidatorModel):
    ScheduleDefinitions: List[str]
    ScheduleIdentifier: str
    ScheduleDescription: str
    Tags: List[TagTypeDef]
    NextInvocations: List[datetime]
    AssociatedClusterCount: int
    AssociatedClusters: List[ClusterAssociatedToScheduleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotScheduleTypeDef(BaseValidatorModel):
    ScheduleDefinitions: Optional[List[str]] = None
    ScheduleIdentifier: Optional[str] = None
    ScheduleDescription: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    NextInvocations: Optional[List[datetime]] = None
    AssociatedClusterCount: Optional[int] = None
    AssociatedClusters: Optional[List[ClusterAssociatedToScheduleTypeDef]] = None

class SnapshotTypeDef(BaseValidatorModel):
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
    AccountsWithRestoreAccess: Optional[List[AccountWithRestoreAccessTypeDef]] = None
    OwnerAccount: Optional[str] = None
    TotalBackupSizeInMegaBytes: Optional[float] = None
    ActualIncrementalBackupSizeInMegaBytes: Optional[float] = None
    BackupProgressInMegaBytes: Optional[float] = None
    CurrentBackupRateInMegaBytesPerSecond: Optional[float] = None
    EstimatedSecondsToCompletion: Optional[int] = None
    ElapsedTimeInSeconds: Optional[int] = None
    SourceRegion: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    RestorableNodeTypes: Optional[List[str]] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRemainingDays: Optional[int] = None
    SnapshotRetentionStartTime: Optional[datetime] = None
    MasterPasswordSecretArn: Optional[str] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    SnapshotArn: Optional[str] = None

class TaggedResourceTypeDef(BaseValidatorModel):
    Tag: Optional[TagTypeDef] = None
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None

class UsageLimitResponseTypeDef(BaseValidatorModel):
    UsageLimitId: str
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureTypeType
    LimitType: UsageLimitLimitTypeType
    Amount: int
    Period: UsageLimitPeriodType
    BreachAction: UsageLimitBreachActionType
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UsageLimitTypeDef(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    LimitType: Optional[UsageLimitLimitTypeType] = None
    Amount: Optional[int] = None
    Period: Optional[UsageLimitPeriodType] = None
    BreachAction: Optional[UsageLimitBreachActionType] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeReservedNodeExchangeStatusOutputMessageTypeDef(BaseValidatorModel):
    ReservedNodeExchangeStatusDetails: List[ReservedNodeExchangeStatusTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterVersionsMessageTypeDef(BaseValidatorModel):
    Marker: str
    ClusterVersions: List[ClusterVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsMessageRequestTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class ModifyClusterMaintenanceMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    DeferMaintenance: Optional[bool] = None
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[TimestampTypeDef] = None
    DeferMaintenanceEndTime: Optional[TimestampTypeDef] = None
    DeferMaintenanceDuration: Optional[int] = None

class DataShareResponseTypeDef(BaseValidatorModel):
    DataShareArn: str
    ProducerArn: str
    AllowPubliclyAccessibleConsumers: bool
    DataShareAssociations: List[DataShareAssociationTypeDef]
    ManagedBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataShareTypeDef(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    ProducerArn: Optional[str] = None
    AllowPubliclyAccessibleConsumers: Optional[bool] = None
    DataShareAssociations: Optional[List[DataShareAssociationTypeDef]] = None
    ManagedBy: Optional[str] = None

class DescribeClusterDbRevisionsMessageDescribeClusterDbRevisionsPaginateTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterParameterGroupsMessageDescribeClusterParameterGroupsPaginateTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterParametersMessageDescribeClusterParametersPaginateTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterSecurityGroupsMessageDescribeClusterSecurityGroupsPaginateTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterSubnetGroupsMessageDescribeClusterSubnetGroupsPaginateTypeDef(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterTracksMessageDescribeClusterTracksPaginateTypeDef(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterVersionsMessageDescribeClusterVersionsPaginateTypeDef(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterParameterGroupFamily: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClustersMessageDescribeClustersPaginateTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCustomDomainAssociationsMessageDescribeCustomDomainAssociationsPaginateTypeDef(BaseValidatorModel):
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDataSharesForConsumerMessageDescribeDataSharesForConsumerPaginateTypeDef(BaseValidatorModel):
    ConsumerArn: Optional[str] = None
    Status: Optional[DataShareStatusForConsumerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDataSharesForProducerMessageDescribeDataSharesForProducerPaginateTypeDef(BaseValidatorModel):
    ProducerArn: Optional[str] = None
    Status: Optional[DataShareStatusForProducerType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDataSharesMessageDescribeDataSharesPaginateTypeDef(BaseValidatorModel):
    DataShareArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDefaultClusterParametersMessageDescribeDefaultClusterParametersPaginateTypeDef(BaseValidatorModel):
    ParameterGroupFamily: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEndpointAccessMessageDescribeEndpointAccessPaginateTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    EndpointName: Optional[str] = None
    VpcId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEndpointAuthorizationMessageDescribeEndpointAuthorizationPaginateTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    Account: Optional[str] = None
    Grantee: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHsmClientCertificatesMessageDescribeHsmClientCertificatesPaginateTypeDef(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHsmConfigurationsMessageDescribeHsmConfigurationsPaginateTypeDef(BaseValidatorModel):
    HsmConfigurationIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInboundIntegrationsMessageDescribeInboundIntegrationsPaginateTypeDef(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    TargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrderableClusterOptionsMessageDescribeOrderableClusterOptionsPaginateTypeDef(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    NodeType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRedshiftIdcApplicationsMessageDescribeRedshiftIdcApplicationsPaginateTypeDef(BaseValidatorModel):
    RedshiftIdcApplicationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodeExchangeStatusInputMessageDescribeReservedNodeExchangeStatusPaginateTypeDef(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    ReservedNodeExchangeRequestId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodeOfferingsMessageDescribeReservedNodeOfferingsPaginateTypeDef(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodesMessageDescribeReservedNodesPaginateTypeDef(BaseValidatorModel):
    ReservedNodeId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotCopyGrantsMessageDescribeSnapshotCopyGrantsPaginateTypeDef(BaseValidatorModel):
    SnapshotCopyGrantName: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotSchedulesMessageDescribeSnapshotSchedulesPaginateTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ScheduleIdentifier: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTableRestoreStatusMessageDescribeTableRestoreStatusPaginateTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    TableRestoreRequestId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTagsMessageDescribeTagsPaginateTypeDef(BaseValidatorModel):
    ResourceName: Optional[str] = None
    ResourceType: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsageLimitsMessageDescribeUsageLimitsPaginateTypeDef(BaseValidatorModel):
    UsageLimitId: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    FeatureType: Optional[UsageLimitFeatureTypeType] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReservedNodeExchangeConfigurationOptionsInputMessageGetReservedNodeExchangeConfigurationOptionsPaginateTypeDef(BaseValidatorModel):
    ActionType: ReservedNodeExchangeActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetReservedNodeExchangeOfferingsInputMessageGetReservedNodeExchangeOfferingsPaginateTypeDef(BaseValidatorModel):
    ReservedNodeId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendationsMessageListRecommendationsPaginateTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NamespaceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterSnapshotsMessageDescribeClusterSnapshotsPaginateTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[Sequence[SnapshotSortingEntityTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClusterSnapshotsMessageRequestTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[Sequence[SnapshotSortingEntityTypeDef]] = None

class DescribeClusterSnapshotsMessageSnapshotAvailableWaitTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    SnapshotType: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    OwnerAccount: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    ClusterExists: Optional[bool] = None
    SortingEntities: Optional[Sequence[SnapshotSortingEntityTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClustersMessageClusterAvailableWaitTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClustersMessageClusterDeletedWaitTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClustersMessageClusterRestoredWaitTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    TagKeys: Optional[Sequence[str]] = None
    TagValues: Optional[Sequence[str]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNodeConfigurationOptionsMessageDescribeNodeConfigurationOptionsPaginateTypeDef(BaseValidatorModel):
    ActionType: ActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    Filters: Optional[Sequence[NodeConfigurationOptionsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNodeConfigurationOptionsMessageRequestTypeDef(BaseValidatorModel):
    ActionType: ActionTypeType
    ClusterIdentifier: Optional[str] = None
    SnapshotIdentifier: Optional[str] = None
    SnapshotArn: Optional[str] = None
    OwnerAccount: Optional[str] = None
    Filters: Optional[Sequence[NodeConfigurationOptionsFilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class DescribePartnersOutputMessageTypeDef(BaseValidatorModel):
    PartnerIntegrationInfoList: List[PartnerIntegrationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeScheduledActionsMessageDescribeScheduledActionsPaginateTypeDef(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetActionType: Optional[ScheduledActionTypeValuesType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Active: Optional[bool] = None
    Filters: Optional[Sequence[ScheduledActionFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledActionsMessageRequestTypeDef(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetActionType: Optional[ScheduledActionTypeValuesType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Active: Optional[bool] = None
    Filters: Optional[Sequence[ScheduledActionFilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class EndpointAuthorizationListTypeDef(BaseValidatorModel):
    EndpointAuthorizationList: List[EndpointAuthorizationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventCategoriesMapTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    Events: Optional[List[EventInfoMapTypeDef]] = None

class EventsMessageTypeDef(BaseValidatorModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResultTypeDef(BaseValidatorModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResultTypeDef(BaseValidatorModel):
    ResourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InboundIntegrationTypeDef(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    SourceArn: Optional[str] = None
    TargetArn: Optional[str] = None
    Status: Optional[ZeroETLIntegrationStatusType] = None
    Errors: Optional[List[IntegrationErrorTypeDef]] = None
    CreateTime: Optional[datetime] = None

class LakeFormationScopeUnionTypeDef(BaseValidatorModel):
    LakeFormationQuery: Optional[LakeFormationQueryTypeDef] = None

class VpcEndpointTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcId: Optional[str] = None
    NetworkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None

class NodeConfigurationOptionsMessageTypeDef(BaseValidatorModel):
    NodeConfigurationOptionList: List[NodeConfigurationOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecommendationTypeDef(BaseValidatorModel):
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
    RecommendedActions: Optional[List[RecommendedActionTypeDef]] = None
    ReferenceLinks: Optional[List[ReferenceLinkTypeDef]] = None

class ReservedNodeOfferingTypeDef(BaseValidatorModel):
    ReservedNodeOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    ReservedNodeOfferingType: Optional[ReservedNodeOfferingTypeType] = None

class ReservedNodeTypeDef(BaseValidatorModel):
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
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    ReservedNodeOfferingType: Optional[ReservedNodeOfferingTypeType] = None

class RestoreTableFromClusterSnapshotResultTypeDef(BaseValidatorModel):
    TableRestoreStatus: TableRestoreStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TableRestoreStatusMessageTypeDef(BaseValidatorModel):
    TableRestoreStatusDetails: List[TableRestoreStatusTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionTypeTypeDef(BaseValidatorModel):
    ResizeCluster: Optional[ResizeClusterMessageTypeDef] = None
    PauseCluster: Optional[PauseClusterMessageTypeDef] = None
    ResumeCluster: Optional[ResumeClusterMessageTypeDef] = None

class UpdateTargetTypeDef(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    DatabaseVersion: Optional[str] = None
    SupportedOperations: Optional[List[SupportedOperationTypeDef]] = None

class AccountAttributeListTypeDef(BaseValidatorModel):
    AccountAttributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CustomDomainAssociationsMessageTypeDef(BaseValidatorModel):
    Marker: str
    Associations: List[AssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableClusterOptionTypeDef(BaseValidatorModel):
    ClusterVersion: Optional[str] = None
    ClusterType: Optional[str] = None
    NodeType: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None

class SubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None

class ClusterDbRevisionsMessageTypeDef(BaseValidatorModel):
    Marker: str
    ClusterDbRevisions: List[ClusterDbRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDefaultClusterParametersResultTypeDef(BaseValidatorModel):
    DefaultClusterParameters: DefaultClusterParametersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterParameterGroupsMessageTypeDef(BaseValidatorModel):
    Marker: str
    ParameterGroups: List[ClusterParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterParameterGroupResultTypeDef(BaseValidatorModel):
    ClusterParameterGroup: ClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventSubscriptionsMessageTypeDef(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmClientCertificateResultTypeDef(BaseValidatorModel):
    HsmClientCertificate: HsmClientCertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HsmClientCertificateMessageTypeDef(BaseValidatorModel):
    Marker: str
    HsmClientCertificates: List[HsmClientCertificateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHsmConfigurationResultTypeDef(BaseValidatorModel):
    HsmConfiguration: HsmConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HsmConfigurationMessageTypeDef(BaseValidatorModel):
    Marker: str
    HsmConfigurations: List[HsmConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSecurityGroupTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Description: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroupTypeDef]] = None
    IPRanges: Optional[List[IPRangeTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateSnapshotCopyGrantResultTypeDef(BaseValidatorModel):
    SnapshotCopyGrant: SnapshotCopyGrantTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotCopyGrantMessageTypeDef(BaseValidatorModel):
    Marker: str
    SnapshotCopyGrants: List[SnapshotCopyGrantTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotSchedulesOutputMessageTypeDef(BaseValidatorModel):
    SnapshotSchedules: List[SnapshotScheduleTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeSnapshotAccessResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyClusterSnapshotResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSnapshotResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterSnapshotResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterSnapshotResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeSnapshotAccessResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotMessageTypeDef(BaseValidatorModel):
    Marker: str
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TaggedResourceListMessageTypeDef(BaseValidatorModel):
    TaggedResources: List[TaggedResourceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class UsageLimitListTypeDef(BaseValidatorModel):
    UsageLimits: List[UsageLimitTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesForConsumerResultTypeDef(BaseValidatorModel):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesForProducerResultTypeDef(BaseValidatorModel):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDataSharesResultTypeDef(BaseValidatorModel):
    DataShares: List[DataShareTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventCategoriesMessageTypeDef(BaseValidatorModel):
    EventCategoriesMapList: List[EventCategoriesMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InboundIntegrationsMessageTypeDef(BaseValidatorModel):
    Marker: str
    InboundIntegrations: List[InboundIntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceIntegrationsUnionExtraOutputTypeDef(BaseValidatorModel):
    LakeFormation: Optional[List[LakeFormationScopeUnionTypeDef]] = None

class ServiceIntegrationsUnionOutputTypeDef(BaseValidatorModel):
    LakeFormation: Optional[List[LakeFormationScopeUnionTypeDef]] = None

class ServiceIntegrationsUnionTypeDef(BaseValidatorModel):
    LakeFormation: Optional[Sequence[LakeFormationScopeUnionTypeDef]] = None

class EndpointAccessResponseTypeDef(BaseValidatorModel):
    ClusterIdentifier: str
    ResourceOwner: str
    SubnetGroupName: str
    EndpointStatus: str
    EndpointName: str
    EndpointCreateTime: datetime
    Port: int
    Address: str
    VpcSecurityGroups: List[VpcSecurityGroupMembershipTypeDef]
    VpcEndpoint: VpcEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EndpointAccessTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    ResourceOwner: Optional[str] = None
    SubnetGroupName: Optional[str] = None
    EndpointStatus: Optional[str] = None
    EndpointName: Optional[str] = None
    EndpointCreateTime: Optional[datetime] = None
    Port: Optional[int] = None
    Address: Optional[str] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    VpcEndpoint: Optional[VpcEndpointTypeDef] = None

class EndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    VpcEndpoints: Optional[List[VpcEndpointTypeDef]] = None

class ListRecommendationsResultTypeDef(BaseValidatorModel):
    Recommendations: List[RecommendationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReservedNodeExchangeOfferingsOutputMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedNodeOfferingsMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReservedNodeOfferings: List[ReservedNodeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptReservedNodeExchangeOutputMessageTypeDef(BaseValidatorModel):
    ExchangedReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedNodeOfferingResultTypeDef(BaseValidatorModel):
    ReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedNodeConfigurationOptionTypeDef(BaseValidatorModel):
    SourceReservedNode: Optional[ReservedNodeTypeDef] = None
    TargetReservedNodeCount: Optional[int] = None
    TargetReservedNodeOffering: Optional[ReservedNodeOfferingTypeDef] = None

class ReservedNodesMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReservedNodes: List[ReservedNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduledActionMessageRequestTypeDef(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: ScheduledActionTypeTypeDef
    Schedule: str
    IamRole: str
    ScheduledActionDescription: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Enable: Optional[bool] = None

class ModifyScheduledActionMessageRequestTypeDef(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: Optional[ScheduledActionTypeTypeDef] = None
    Schedule: Optional[str] = None
    IamRole: Optional[str] = None
    ScheduledActionDescription: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Enable: Optional[bool] = None

class ScheduledActionResponseTypeDef(BaseValidatorModel):
    ScheduledActionName: str
    TargetAction: ScheduledActionTypeTypeDef
    Schedule: str
    IamRole: str
    ScheduledActionDescription: str
    State: ScheduledActionStateType
    NextInvocations: List[datetime]
    StartTime: datetime
    EndTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionTypeDef(BaseValidatorModel):
    ScheduledActionName: Optional[str] = None
    TargetAction: Optional[ScheduledActionTypeTypeDef] = None
    Schedule: Optional[str] = None
    IamRole: Optional[str] = None
    ScheduledActionDescription: Optional[str] = None
    State: Optional[ScheduledActionStateType] = None
    NextInvocations: Optional[List[datetime]] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class MaintenanceTrackTypeDef(BaseValidatorModel):
    MaintenanceTrackName: Optional[str] = None
    DatabaseVersion: Optional[str] = None
    UpdateTargets: Optional[List[UpdateTargetTypeDef]] = None

class OrderableClusterOptionsMessageTypeDef(BaseValidatorModel):
    OrderableClusterOptions: List[OrderableClusterOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSubnetGroupTypeDef(BaseValidatorModel):
    ClusterSubnetGroupName: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    SupportedClusterIpAddressTypes: Optional[List[str]] = None

class AuthorizeClusterSecurityGroupIngressResultTypeDef(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSecurityGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    ClusterSecurityGroups: List[ClusterSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSecurityGroupResultTypeDef(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeClusterSecurityGroupIngressResultTypeDef(BaseValidatorModel):
    ClusterSecurityGroup: ClusterSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RedshiftIdcApplicationTypeDef(BaseValidatorModel):
    IdcInstanceArn: Optional[str] = None
    RedshiftIdcApplicationName: Optional[str] = None
    RedshiftIdcApplicationArn: Optional[str] = None
    IdentityNamespace: Optional[str] = None
    IdcDisplayName: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IdcManagedApplicationArn: Optional[str] = None
    IdcOnboardStatus: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[List[AuthorizedTokenIssuerOutputTypeDef]] = None
    ServiceIntegrations: Optional[List[ServiceIntegrationsUnionOutputTypeDef]] = None

class EndpointAccessListTypeDef(BaseValidatorModel):
    EndpointAccessList: List[EndpointAccessTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterTypeDef(BaseValidatorModel):
    ClusterIdentifier: Optional[str] = None
    NodeType: Optional[str] = None
    ClusterStatus: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ModifyStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    DBName: Optional[str] = None
    Endpoint: Optional[EndpointTypeDef] = None
    ClusterCreateTime: Optional[datetime] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    ClusterSecurityGroups: Optional[List[ClusterSecurityGroupMembershipTypeDef]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    ClusterParameterGroups: Optional[List[ClusterParameterGroupStatusTypeDef]] = None
    ClusterSubnetGroupName: Optional[str] = None
    VpcId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValuesTypeDef] = None
    ClusterVersion: Optional[str] = None
    AllowVersionUpgrade: Optional[bool] = None
    NumberOfNodes: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    Encrypted: Optional[bool] = None
    RestoreStatus: Optional[RestoreStatusTypeDef] = None
    DataTransferProgress: Optional[DataTransferProgressTypeDef] = None
    HsmStatus: Optional[HsmStatusTypeDef] = None
    ClusterSnapshotCopyStatus: Optional[ClusterSnapshotCopyStatusTypeDef] = None
    ClusterPublicKey: Optional[str] = None
    ClusterNodes: Optional[List[ClusterNodeTypeDef]] = None
    ElasticIpStatus: Optional[ElasticIpStatusTypeDef] = None
    ClusterRevisionNumber: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    IamRoles: Optional[List[ClusterIamRoleTypeDef]] = None
    PendingActions: Optional[List[str]] = None
    MaintenanceTrackName: Optional[str] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    DeferredMaintenanceWindows: Optional[List[DeferredMaintenanceWindowTypeDef]] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[ScheduleStateType] = None
    ExpectedNextSnapshotScheduleTime: Optional[datetime] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[datetime] = None
    ResizeInfo: Optional[ResizeInfoTypeDef] = None
    AvailabilityZoneRelocationStatus: Optional[str] = None
    ClusterNamespaceArn: Optional[str] = None
    TotalStorageCapacityInMegaBytes: Optional[int] = None
    AquaConfiguration: Optional[AquaConfigurationTypeDef] = None
    DefaultIamRoleArn: Optional[str] = None
    ReservedNodeExchangeStatus: Optional[ReservedNodeExchangeStatusTypeDef] = None
    CustomDomainName: Optional[str] = None
    CustomDomainCertificateArn: Optional[str] = None
    CustomDomainCertificateExpiryDate: Optional[datetime] = None
    MasterPasswordSecretArn: Optional[str] = None
    MasterPasswordSecretKmsKeyId: Optional[str] = None
    IpAddressType: Optional[str] = None
    MultiAZ: Optional[str] = None
    MultiAZSecondary: Optional[SecondaryClusterInfoTypeDef] = None

class GetReservedNodeExchangeConfigurationOptionsOutputMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReservedNodeConfigurationOptionList: List[ReservedNodeConfigurationOptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledActionsMessageTypeDef(BaseValidatorModel):
    Marker: str
    ScheduledActions: List[ScheduledActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TrackListMessageTypeDef(BaseValidatorModel):
    MaintenanceTracks: List[MaintenanceTrackTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterSubnetGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    ClusterSubnetGroups: List[ClusterSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterSubnetGroupResultTypeDef(BaseValidatorModel):
    ClusterSubnetGroup: ClusterSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterSubnetGroupResultTypeDef(BaseValidatorModel):
    ClusterSubnetGroup: ClusterSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRedshiftIdcApplicationResultTypeDef(BaseValidatorModel):
    RedshiftIdcApplication: RedshiftIdcApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRedshiftIdcApplicationsResultTypeDef(BaseValidatorModel):
    RedshiftIdcApplications: List[RedshiftIdcApplicationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyRedshiftIdcApplicationResultTypeDef(BaseValidatorModel):
    RedshiftIdcApplication: RedshiftIdcApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRedshiftIdcApplicationMessageRequestTypeDef(BaseValidatorModel):
    IdcInstanceArn: str
    RedshiftIdcApplicationName: str
    IdcDisplayName: str
    IamRoleArn: str
    IdentityNamespace: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[Sequence[AuthorizedTokenIssuerUnionTypeDef]] = None
    ServiceIntegrations: Optional[Sequence[ServiceIntegrationsUnionUnionTypeDef]] = None

class ModifyRedshiftIdcApplicationMessageRequestTypeDef(BaseValidatorModel):
    RedshiftIdcApplicationArn: str
    IdentityNamespace: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IdcDisplayName: Optional[str] = None
    AuthorizedTokenIssuerList: Optional[Sequence[AuthorizedTokenIssuerUnionTypeDef]] = None
    ServiceIntegrations: Optional[Sequence[ServiceIntegrationsUnionUnionTypeDef]] = None

class ClustersMessageTypeDef(BaseValidatorModel):
    Marker: str
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisableSnapshotCopyResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSnapshotCopyResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverPrimaryComputeResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterDbRevisionResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterIamRolesResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterMaintenanceResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClusterResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySnapshotCopyRetentionPeriodResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PauseClusterResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootClusterResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResizeClusterResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreFromClusterSnapshotResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResumeClusterResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RotateEncryptionKeyResultTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


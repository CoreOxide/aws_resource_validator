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
from aws_resource_validator.pydantic_models.securityhub_constants import *

class AcceptAdministratorInvitationRequest(BaseValidatorModel):
    AdministratorId: str
    InvitationId: str


class AcceptInvitationRequest(BaseValidatorModel):
    MasterId: str
    InvitationId: str


class AccountDetails(BaseValidatorModel):
    AccountId: str
    Email: Optional[str] = None


class ActionLocalIpDetails(BaseValidatorModel):
    IpAddressV4: Optional[str] = None


class ActionLocalPortDetails(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None


class City(BaseValidatorModel):
    CityName: Optional[str] = None


class Country(BaseValidatorModel):
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None


class GeoLocation(BaseValidatorModel):
    Lon: Optional[float] = None
    Lat: Optional[float] = None


class IpOrganizationDetails(BaseValidatorModel):
    Asn: Optional[int] = None
    AsnOrg: Optional[str] = None
    Isp: Optional[str] = None
    Org: Optional[str] = None


class ActionRemotePortDetails(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None


class ActionTarget(BaseValidatorModel):
    ActionTargetArn: str
    Name: str
    Description: str


class ActorSession(BaseValidatorModel):
    Uid: Optional[str] = None
    MfaStatus: Optional[ActorSessionMfaStatusType] = None
    CreatedTime: Optional[int] = None
    Issuer: Optional[str] = None


class UserAccount(BaseValidatorModel):
    Uid: Optional[str] = None
    Name: Optional[str] = None


class Adjustment(BaseValidatorModel):
    Metric: Optional[str] = None
    Reason: Optional[str] = None


class AdminAccount(BaseValidatorModel):
    AccountId: Optional[str] = None
    Status: Optional[AdminStatusType] = None


class AssociatedStandard(BaseValidatorModel):
    StandardsId: Optional[str] = None


class AssociationFilters(BaseValidatorModel):
    ConfigurationPolicyId: Optional[str] = None
    AssociationType: Optional[AssociationTypeType] = None
    AssociationStatus: Optional[ConfigurationPolicyAssociationStatusType] = None


class AssociationStateDetails(BaseValidatorModel):
    State: Optional[str] = None
    StatusMessage: Optional[str] = None


class RelatedFinding(BaseValidatorModel):
    ProductArn: str
    Id: str


class SeverityUpdate(BaseValidatorModel):
    Normalized: Optional[int] = None
    Product: Optional[float] = None
    Label: Optional[SeverityLabelType] = None


class WorkflowUpdate(BaseValidatorModel):
    Status: Optional[WorkflowStatusType] = None


class MapFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Comparison: Optional[MapFilterComparisonType] = None


class NumberFilter(BaseValidatorModel):
    Gte: Optional[float] = None
    Lte: Optional[float] = None
    Eq: Optional[float] = None
    Gt: Optional[float] = None
    Lt: Optional[float] = None


class StringFilter(BaseValidatorModel):
    Value: Optional[str] = None
    Comparison: Optional[StringFilterComparisonType] = None


class AutomationRulesMetadata(BaseValidatorModel):
    RuleArn: Optional[str] = None
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    RuleName: Optional[str] = None
    Description: Optional[str] = None
    IsTerminal: Optional[bool] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None


class AvailabilityZone(BaseValidatorModel):
    ZoneName: Optional[str] = None
    SubnetId: Optional[str] = None


class AwsAmazonMqBrokerEncryptionOptionsDetails(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    UseAwsOwnedKey: Optional[bool] = None


class AwsAmazonMqBrokerLdapServerMetadataDetailsOutput(BaseValidatorModel):
    Hosts: Optional[List[str]] = None
    RoleBase: Optional[str] = None
    RoleName: Optional[str] = None
    RoleSearchMatching: Optional[str] = None
    RoleSearchSubtree: Optional[bool] = None
    ServiceAccountUsername: Optional[str] = None
    UserBase: Optional[str] = None
    UserRoleName: Optional[str] = None
    UserSearchMatching: Optional[str] = None
    UserSearchSubtree: Optional[bool] = None


class AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails(BaseValidatorModel):
    DayOfWeek: Optional[str] = None
    TimeOfDay: Optional[str] = None
    TimeZone: Optional[str] = None


class AwsAmazonMqBrokerUsersDetails(BaseValidatorModel):
    PendingChange: Optional[str] = None
    Username: Optional[str] = None


class AwsAmazonMqBrokerLdapServerMetadataDetails(BaseValidatorModel):
    Hosts: Optional[Sequence[str]] = None
    RoleBase: Optional[str] = None
    RoleName: Optional[str] = None
    RoleSearchMatching: Optional[str] = None
    RoleSearchSubtree: Optional[bool] = None
    ServiceAccountUsername: Optional[str] = None
    UserBase: Optional[str] = None
    UserRoleName: Optional[str] = None
    UserSearchMatching: Optional[str] = None
    UserSearchSubtree: Optional[bool] = None


class AwsAmazonMqBrokerLogsPendingDetails(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None


class AwsApiCallActionDomainDetails(BaseValidatorModel):
    Domain: Optional[str] = None


class AwsApiGatewayAccessLogSettings(BaseValidatorModel):
    Format: Optional[str] = None
    DestinationArn: Optional[str] = None


class AwsApiGatewayCanarySettingsOutput(BaseValidatorModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Dict[str, str]] = None
    UseStageCache: Optional[bool] = None


class AwsApiGatewayCanarySettings(BaseValidatorModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Mapping[str, str]] = None
    UseStageCache: Optional[bool] = None


class AwsApiGatewayEndpointConfigurationOutput(BaseValidatorModel):
    Types: Optional[List[str]] = None


class AwsApiGatewayEndpointConfiguration(BaseValidatorModel):
    Types: Optional[Sequence[str]] = None


class AwsApiGatewayMethodSettings(BaseValidatorModel):
    MetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[str] = None
    DataTraceEnabled: Optional[bool] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None
    CachingEnabled: Optional[bool] = None
    CacheTtlInSeconds: Optional[int] = None
    CacheDataEncrypted: Optional[bool] = None
    RequireAuthorizationForCacheControl: Optional[bool] = None
    UnauthorizedCacheControlHeaderStrategy: Optional[str] = None
    HttpMethod: Optional[str] = None
    ResourcePath: Optional[str] = None


class AwsCorsConfigurationOutput(BaseValidatorModel):
    AllowOrigins: Optional[List[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[List[str]] = None
    AllowHeaders: Optional[List[str]] = None


class AwsApiGatewayV2RouteSettings(BaseValidatorModel):
    DetailedMetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[str] = None
    DataTraceEnabled: Optional[bool] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None


class AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails(BaseValidatorModel):
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerUri: Optional[str] = None
    IdentityValidationExpression: Optional[str] = None


class AwsAppSyncGraphQlApiOpenIdConnectConfigDetails(BaseValidatorModel):
    AuthTtL: Optional[int] = None
    ClientId: Optional[str] = None
    IatTtL: Optional[int] = None
    Issuer: Optional[str] = None


class AwsAppSyncGraphQlApiUserPoolConfigDetails(BaseValidatorModel):
    AppIdClientRegex: Optional[str] = None
    AwsRegion: Optional[str] = None
    DefaultAction: Optional[str] = None
    UserPoolId: Optional[str] = None


class AwsAppSyncGraphQlApiLogConfigDetails(BaseValidatorModel):
    CloudWatchLogsRoleArn: Optional[str] = None
    ExcludeVerboseContent: Optional[bool] = None
    FieldLogLevel: Optional[str] = None


class AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails(BaseValidatorModel):
    Value: Optional[str] = None


class AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None


class AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsAutoScalingLaunchConfigurationMetadataOptions(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpTokens: Optional[str] = None


class AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutput(BaseValidatorModel):
    BackupOptions: Optional[Dict[str, str]] = None
    ResourceType: Optional[str] = None


class AwsBackupBackupPlanAdvancedBackupSettingsDetails(BaseValidatorModel):
    BackupOptions: Optional[Mapping[str, str]] = None
    ResourceType: Optional[str] = None


class AwsBackupBackupPlanLifecycleDetails(BaseValidatorModel):
    DeleteAfterDays: Optional[int] = None
    MoveToColdStorageAfterDays: Optional[int] = None


class AwsBackupBackupVaultNotificationsDetailsOutput(BaseValidatorModel):
    BackupVaultEvents: Optional[List[str]] = None
    SnsTopicArn: Optional[str] = None


class AwsBackupBackupVaultNotificationsDetails(BaseValidatorModel):
    BackupVaultEvents: Optional[Sequence[str]] = None
    SnsTopicArn: Optional[str] = None


class AwsBackupRecoveryPointCalculatedLifecycleDetails(BaseValidatorModel):
    DeleteAt: Optional[str] = None
    MoveToColdStorageAt: Optional[str] = None


class AwsBackupRecoveryPointCreatedByDetails(BaseValidatorModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    BackupPlanVersion: Optional[str] = None
    BackupRuleId: Optional[str] = None


class AwsBackupRecoveryPointLifecycleDetails(BaseValidatorModel):
    DeleteAfterDays: Optional[int] = None
    MoveToColdStorageAfterDays: Optional[int] = None


class AwsCertificateManagerCertificateExtendedKeyUsage(BaseValidatorModel):
    Name: Optional[str] = None
    OId: Optional[str] = None


class AwsCertificateManagerCertificateKeyUsage(BaseValidatorModel):
    Name: Optional[str] = None


class AwsCertificateManagerCertificateOptions(BaseValidatorModel):
    CertificateTransparencyLoggingPreference: Optional[str] = None


class AwsCloudFormationStackDriftInformationDetails(BaseValidatorModel):
    StackDriftStatus: Optional[str] = None


class AwsCloudFormationStackOutputsDetails(BaseValidatorModel):
    Description: Optional[str] = None
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None


class AwsCloudFrontDistributionCacheBehavior(BaseValidatorModel):
    ViewerProtocolPolicy: Optional[str] = None


class AwsCloudFrontDistributionDefaultCacheBehavior(BaseValidatorModel):
    ViewerProtocolPolicy: Optional[str] = None


class AwsCloudFrontDistributionLogging(BaseValidatorModel):
    Bucket: Optional[str] = None
    Enabled: Optional[bool] = None
    IncludeCookies: Optional[bool] = None
    Prefix: Optional[str] = None


class AwsCloudFrontDistributionViewerCertificate(BaseValidatorModel):
    AcmCertificateArn: Optional[str] = None
    Certificate: Optional[str] = None
    CertificateSource: Optional[str] = None
    CloudFrontDefaultCertificate: Optional[bool] = None
    IamCertificateId: Optional[str] = None
    MinimumProtocolVersion: Optional[str] = None
    SslSupportMethod: Optional[str] = None


class AwsCloudFrontDistributionOriginSslProtocolsOutput(BaseValidatorModel):
    Items: Optional[List[str]] = None
    Quantity: Optional[int] = None


class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutput(BaseValidatorModel):
    Items: Optional[List[int]] = None
    Quantity: Optional[int] = None


class AwsCloudFrontDistributionOriginGroupFailoverStatusCodes(BaseValidatorModel):
    Items: Optional[Sequence[int]] = None
    Quantity: Optional[int] = None


class AwsCloudFrontDistributionOriginS3OriginConfig(BaseValidatorModel):
    OriginAccessIdentity: Optional[str] = None


class AwsCloudFrontDistributionOriginSslProtocols(BaseValidatorModel):
    Items: Optional[Sequence[str]] = None
    Quantity: Optional[int] = None


class AwsCloudTrailTrailDetails(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    CloudWatchLogsRoleArn: Optional[str] = None
    HasCustomEventSelectors: Optional[bool] = None
    HomeRegion: Optional[str] = None
    IncludeGlobalServiceEvents: Optional[bool] = None
    IsMultiRegionTrail: Optional[bool] = None
    IsOrganizationTrail: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    LogFileValidationEnabled: Optional[bool] = None
    Name: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3KeyPrefix: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SnsTopicName: Optional[str] = None
    TrailArn: Optional[str] = None


class AwsCloudWatchAlarmDimensionsDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsCodeBuildProjectVpcConfigOutput(BaseValidatorModel):
    VpcId: Optional[str] = None
    Subnets: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class AwsCodeBuildProjectEnvironmentRegistryCredential(BaseValidatorModel):
    Credential: Optional[str] = None
    CredentialProvider: Optional[str] = None


class AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails(BaseValidatorModel):
    GroupName: Optional[str] = None
    Status: Optional[str] = None
    StreamName: Optional[str] = None


class AwsCodeBuildProjectLogsConfigS3LogsDetails(BaseValidatorModel):
    EncryptionDisabled: Optional[bool] = None
    Location: Optional[str] = None
    Status: Optional[str] = None


class AwsCodeBuildProjectVpcConfig(BaseValidatorModel):
    VpcId: Optional[str] = None
    Subnets: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None


class AwsCorsConfiguration(BaseValidatorModel):
    AllowOrigins: Optional[Sequence[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowHeaders: Optional[Sequence[str]] = None


class AwsDmsEndpointDetails(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DatabaseName: Optional[str] = None
    EndpointArn: Optional[str] = None
    EndpointIdentifier: Optional[str] = None
    EndpointType: Optional[str] = None
    EngineName: Optional[str] = None
    ExternalId: Optional[str] = None
    ExtraConnectionAttributes: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Port: Optional[int] = None
    ServerName: Optional[str] = None
    SslMode: Optional[str] = None
    Username: Optional[str] = None


class AwsDmsReplicationInstanceReplicationSubnetGroupDetails(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: Optional[str] = None


class AwsDmsReplicationInstanceVpcSecurityGroupsDetails(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None


class AwsDmsReplicationTaskDetails(BaseValidatorModel):
    CdcStartPosition: Optional[str] = None
    CdcStartTime: Optional[str] = None
    CdcStopPosition: Optional[str] = None
    MigrationType: Optional[str] = None
    Id: Optional[str] = None
    ResourceIdentifier: Optional[str] = None
    ReplicationInstanceArn: Optional[str] = None
    ReplicationTaskIdentifier: Optional[str] = None
    ReplicationTaskSettings: Optional[str] = None
    SourceEndpointArn: Optional[str] = None
    TableMappings: Optional[str] = None
    TargetEndpointArn: Optional[str] = None
    TaskData: Optional[str] = None


class AwsDynamoDbTableAttributeDefinition(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[str] = None


class AwsDynamoDbTableBillingModeSummary(BaseValidatorModel):
    BillingMode: Optional[str] = None
    LastUpdateToPayPerRequestDateTime: Optional[str] = None


class AwsDynamoDbTableKeySchema(BaseValidatorModel):
    AttributeName: Optional[str] = None
    KeyType: Optional[str] = None


class AwsDynamoDbTableProvisionedThroughput(BaseValidatorModel):
    LastDecreaseDateTime: Optional[str] = None
    LastIncreaseDateTime: Optional[str] = None
    NumberOfDecreasesToday: Optional[int] = None
    ReadCapacityUnits: Optional[int] = None
    WriteCapacityUnits: Optional[int] = None


class AwsDynamoDbTableRestoreSummary(BaseValidatorModel):
    SourceBackupArn: Optional[str] = None
    SourceTableArn: Optional[str] = None
    RestoreDateTime: Optional[str] = None
    RestoreInProgress: Optional[bool] = None


class AwsDynamoDbTableSseDescription(BaseValidatorModel):
    InaccessibleEncryptionDateTime: Optional[str] = None
    Status: Optional[str] = None
    SseType: Optional[str] = None
    KmsMasterKeyArn: Optional[str] = None


class AwsDynamoDbTableStreamSpecification(BaseValidatorModel):
    StreamEnabled: Optional[bool] = None
    StreamViewType: Optional[str] = None


class AwsDynamoDbTableProjectionOutput(BaseValidatorModel):
    NonKeyAttributes: Optional[List[str]] = None
    ProjectionType: Optional[str] = None


class AwsDynamoDbTableProjection(BaseValidatorModel):
    NonKeyAttributes: Optional[Sequence[str]] = None
    ProjectionType: Optional[str] = None


class AwsDynamoDbTableProvisionedThroughputOverride(BaseValidatorModel):
    ReadCapacityUnits: Optional[int] = None


class AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetails(BaseValidatorModel):
    DirectoryId: Optional[str] = None


class AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetails(BaseValidatorModel):
    SamlProviderArn: Optional[str] = None
    SelfServiceSamlProviderArn: Optional[str] = None


class AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetails(BaseValidatorModel):
    ClientRootCertificateChain: Optional[str] = None


class AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None


class AwsEc2ClientVpnEndpointConnectionLogOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None


class AwsEc2EipDetails(BaseValidatorModel):
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    AssociationId: Optional[str] = None
    Domain: Optional[str] = None
    PublicIpv4Pool: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfaceOwnerId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None


class AwsEc2InstanceMetadataOptions(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpProtocolIpv6: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpTokens: Optional[str] = None
    InstanceMetadataTags: Optional[str] = None


class AwsEc2InstanceMonitoringDetails(BaseValidatorModel):
    State: Optional[str] = None


class AwsEc2InstanceNetworkInterfacesDetails(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None


class AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    Throughput: Optional[int] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None


class AwsEc2LaunchTemplateDataCpuOptionsDetails(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None


class AwsEc2LaunchTemplateDataCreditSpecificationDetails(BaseValidatorModel):
    CpuCredits: Optional[str] = None


class AwsEc2LaunchTemplateDataEnclaveOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsEc2LaunchTemplateDataHibernationOptionsDetails(BaseValidatorModel):
    Configured: Optional[bool] = None


class AwsEc2LaunchTemplateDataIamInstanceProfileDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class AwsEc2LaunchTemplateDataLicenseSetDetails(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None


class AwsEc2LaunchTemplateDataMaintenanceOptionsDetails(BaseValidatorModel):
    AutoRecovery: Optional[str] = None


class AwsEc2LaunchTemplateDataMetadataOptionsDetails(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpProtocolIpv6: Optional[str] = None
    HttpTokens: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    InstanceMetadataTags: Optional[str] = None


class AwsEc2LaunchTemplateDataMonitoringDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsEc2LaunchTemplateDataPlacementDetails(BaseValidatorModel):
    Affinity: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    SpreadDomain: Optional[str] = None
    Tenancy: Optional[str] = None


class AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails(BaseValidatorModel):
    EnableResourceNameDnsAAAARecord: Optional[bool] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    HostnameType: Optional[str] = None


class AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails(BaseValidatorModel):
    BlockDurationMinutes: Optional[int] = None
    InstanceInterruptionBehavior: Optional[str] = None
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[str] = None
    ValidUntil: Optional[str] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails(BaseValidatorModel):
    Max: Optional[float] = None
    Min: Optional[float] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails(BaseValidatorModel):
    Max: Optional[float] = None
    Min: Optional[float] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails(BaseValidatorModel):
    Ipv6Address: Optional[str] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails(BaseValidatorModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None


class AwsEc2NetworkAclAssociation(BaseValidatorModel):
    NetworkAclAssociationId: Optional[str] = None
    NetworkAclId: Optional[str] = None
    SubnetId: Optional[str] = None


class PortRangeFromTo(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None


class AwsEc2NetworkInterfaceAttachment(BaseValidatorModel):
    AttachTime: Optional[str] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    Status: Optional[str] = None


class AwsEc2NetworkInterfaceIpV6AddressDetail(BaseValidatorModel):
    IpV6Address: Optional[str] = None


class AwsEc2NetworkInterfacePrivateIpAddressDetail(BaseValidatorModel):
    PrivateIpAddress: Optional[str] = None
    PrivateDnsName: Optional[str] = None


class AwsEc2NetworkInterfaceSecurityGroup(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None


class PropagatingVgwSetDetails(BaseValidatorModel):
    GatewayId: Optional[str] = None


class RouteSetDetails(BaseValidatorModel):
    CarrierGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    GatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    NatGatewayId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    Origin: Optional[str] = None
    State: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None


class AwsEc2SecurityGroupIpRange(BaseValidatorModel):
    CidrIp: Optional[str] = None


class AwsEc2SecurityGroupIpv6Range(BaseValidatorModel):
    CidrIpv6: Optional[str] = None


class AwsEc2SecurityGroupPrefixListId(BaseValidatorModel):
    PrefixListId: Optional[str] = None


class AwsEc2SecurityGroupUserIdGroupPair(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None


class Ipv6CidrBlockAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    CidrBlockState: Optional[str] = None


class AwsEc2TransitGatewayDetailsOutput(BaseValidatorModel):
    Id: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteTablePropagation: Optional[str] = None
    AutoAcceptSharedAttachments: Optional[str] = None
    DefaultRouteTableAssociation: Optional[str] = None
    TransitGatewayCidrBlocks: Optional[List[str]] = None
    AssociationDefaultRouteTableId: Optional[str] = None
    PropagationDefaultRouteTableId: Optional[str] = None
    VpnEcmpSupport: Optional[str] = None
    DnsSupport: Optional[str] = None
    MulticastSupport: Optional[str] = None
    AmazonSideAsn: Optional[int] = None


class AwsEc2TransitGatewayDetails(BaseValidatorModel):
    Id: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteTablePropagation: Optional[str] = None
    AutoAcceptSharedAttachments: Optional[str] = None
    DefaultRouteTableAssociation: Optional[str] = None
    TransitGatewayCidrBlocks: Optional[Sequence[str]] = None
    AssociationDefaultRouteTableId: Optional[str] = None
    PropagationDefaultRouteTableId: Optional[str] = None
    VpnEcmpSupport: Optional[str] = None
    DnsSupport: Optional[str] = None
    MulticastSupport: Optional[str] = None
    AmazonSideAsn: Optional[int] = None


class AwsEc2VolumeAttachment(BaseValidatorModel):
    AttachTime: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    InstanceId: Optional[str] = None
    Status: Optional[str] = None


class CidrBlockAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    CidrBlock: Optional[str] = None
    CidrBlockState: Optional[str] = None


class AwsEc2VpcEndpointServiceServiceTypeDetails(BaseValidatorModel):
    ServiceType: Optional[str] = None


class AwsEc2VpcPeeringConnectionStatusDetails(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class VpcInfoCidrBlockSetDetails(BaseValidatorModel):
    CidrBlock: Optional[str] = None


class VpcInfoIpv6CidrBlockSetDetails(BaseValidatorModel):
    Ipv6CidrBlock: Optional[str] = None


class VpcInfoPeeringOptionsDetails(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None


class AwsEc2VpnConnectionRoutesDetails(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    State: Optional[str] = None


class AwsEc2VpnConnectionVgwTelemetryDetails(BaseValidatorModel):
    AcceptedRouteCount: Optional[int] = None
    CertificateArn: Optional[str] = None
    LastStatusChange: Optional[str] = None
    OutsideIpAddress: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None


class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutput(BaseValidatorModel):
    DpdTimeoutSeconds: Optional[int] = None
    IkeVersions: Optional[List[str]] = None
    OutsideIpAddress: Optional[str] = None
    Phase1DhGroupNumbers: Optional[List[int]] = None
    Phase1EncryptionAlgorithms: Optional[List[str]] = None
    Phase1IntegrityAlgorithms: Optional[List[str]] = None
    Phase1LifetimeSeconds: Optional[int] = None
    Phase2DhGroupNumbers: Optional[List[int]] = None
    Phase2EncryptionAlgorithms: Optional[List[str]] = None
    Phase2IntegrityAlgorithms: Optional[List[str]] = None
    Phase2LifetimeSeconds: Optional[int] = None
    PreSharedKey: Optional[str] = None
    RekeyFuzzPercentage: Optional[int] = None
    RekeyMarginTimeSeconds: Optional[int] = None
    ReplayWindowSize: Optional[int] = None
    TunnelInsideCidr: Optional[str] = None


class AwsEc2VpnConnectionOptionsTunnelOptionsDetails(BaseValidatorModel):
    DpdTimeoutSeconds: Optional[int] = None
    IkeVersions: Optional[Sequence[str]] = None
    OutsideIpAddress: Optional[str] = None
    Phase1DhGroupNumbers: Optional[Sequence[int]] = None
    Phase1EncryptionAlgorithms: Optional[Sequence[str]] = None
    Phase1IntegrityAlgorithms: Optional[Sequence[str]] = None
    Phase1LifetimeSeconds: Optional[int] = None
    Phase2DhGroupNumbers: Optional[Sequence[int]] = None
    Phase2EncryptionAlgorithms: Optional[Sequence[str]] = None
    Phase2IntegrityAlgorithms: Optional[Sequence[str]] = None
    Phase2LifetimeSeconds: Optional[int] = None
    PreSharedKey: Optional[str] = None
    RekeyFuzzPercentage: Optional[int] = None
    RekeyMarginTimeSeconds: Optional[int] = None
    ReplayWindowSize: Optional[int] = None
    TunnelInsideCidr: Optional[str] = None


class AwsEcrContainerImageDetailsOutput(BaseValidatorModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[List[str]] = None
    ImagePublishedAt: Optional[str] = None


class AwsEcrContainerImageDetails(BaseValidatorModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[Sequence[str]] = None
    ImagePublishedAt: Optional[str] = None


class AwsEcrRepositoryImageScanningConfigurationDetails(BaseValidatorModel):
    ScanOnPush: Optional[bool] = None


class AwsEcrRepositoryLifecyclePolicyDetails(BaseValidatorModel):
    LifecyclePolicyText: Optional[str] = None
    RegistryId: Optional[str] = None


class AwsEcsClusterClusterSettingsDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsClusterDefaultCapacityProviderStrategyDetails(BaseValidatorModel):
    Base: Optional[int] = None
    CapacityProvider: Optional[str] = None
    Weight: Optional[int] = None


class AwsMountPoint(BaseValidatorModel):
    SourceVolume: Optional[str] = None
    ContainerPath: Optional[str] = None


class AwsEcsServiceCapacityProviderStrategyDetails(BaseValidatorModel):
    Base: Optional[int] = None
    CapacityProvider: Optional[str] = None
    Weight: Optional[int] = None


class AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails(BaseValidatorModel):
    Enable: Optional[bool] = None
    Rollback: Optional[bool] = None


class AwsEcsServiceLoadBalancersDetails(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerPort: Optional[int] = None
    LoadBalancerName: Optional[str] = None
    TargetGroupArn: Optional[str] = None


class AwsEcsServiceServiceRegistriesDetails(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerPort: Optional[int] = None
    Port: Optional[int] = None
    RegistryArn: Optional[str] = None


class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutput(BaseValidatorModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None


class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetails(BaseValidatorModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    Subnets: Optional[Sequence[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails(BaseValidatorModel):
    Condition: Optional[str] = None
    ContainerName: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails(BaseValidatorModel):
    Hostname: Optional[str] = None
    IpAddress: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutput(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails(BaseValidatorModel):
    CredentialsParameter: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails(BaseValidatorModel):
    Name: Optional[str] = None
    ValueFrom: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails(BaseValidatorModel):
    Namespace: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails(BaseValidatorModel):
    HardLimit: Optional[int] = None
    Name: Optional[str] = None
    SoftLimit: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetails(BaseValidatorModel):
    Command: Optional[Sequence[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetails(BaseValidatorModel):
    Add: Optional[Sequence[str]] = None
    Drop: Optional[Sequence[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutput(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[List[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutput(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[List[str]] = None
    Size: Optional[int] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetails(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[Sequence[str]] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetails(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[Sequence[str]] = None
    Size: Optional[int] = None


class AwsEcsTaskDefinitionInferenceAcceleratorsDetails(BaseValidatorModel):
    DeviceName: Optional[str] = None
    DeviceType: Optional[str] = None


class AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutput(BaseValidatorModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Dict[str, str]] = None
    Labels: Optional[Dict[str, str]] = None
    Scope: Optional[str] = None


class AwsEcsTaskDefinitionVolumesHostDetails(BaseValidatorModel):
    SourcePath: Optional[str] = None


class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails(BaseValidatorModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Mapping[str, str]] = None
    Labels: Optional[Mapping[str, str]] = None
    Scope: Optional[str] = None


class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Iam: Optional[str] = None


class AwsEcsTaskVolumeHostDetails(BaseValidatorModel):
    SourcePath: Optional[str] = None


class AwsEfsAccessPointPosixUserDetailsOutput(BaseValidatorModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[List[str]] = None
    Uid: Optional[str] = None


class AwsEfsAccessPointPosixUserDetails(BaseValidatorModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[Sequence[str]] = None
    Uid: Optional[str] = None


class AwsEfsAccessPointRootDirectoryCreationInfoDetails(BaseValidatorModel):
    OwnerGid: Optional[str] = None
    OwnerUid: Optional[str] = None
    Permissions: Optional[str] = None


class AwsEksClusterResourcesVpcConfigDetailsOutput(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    EndpointPublicAccess: Optional[bool] = None


class AwsEksClusterLoggingClusterLoggingDetailsOutput(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Types: Optional[List[str]] = None


class AwsEksClusterLoggingClusterLoggingDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Types: Optional[Sequence[str]] = None


class AwsEksClusterResourcesVpcConfigDetails(BaseValidatorModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    EndpointPublicAccess: Optional[bool] = None


class AwsElasticBeanstalkEnvironmentEnvironmentLink(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    LinkName: Optional[str] = None


class AwsElasticBeanstalkEnvironmentOptionSetting(BaseValidatorModel):
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None
    ResourceName: Optional[str] = None
    Value: Optional[str] = None


class AwsElasticsearchDomainDomainEndpointOptions(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[str] = None


class AwsElasticsearchDomainEncryptionAtRestOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None


class AwsElasticsearchDomainNodeToNodeEncryptionOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsElasticsearchDomainServiceSoftwareOptions(BaseValidatorModel):
    AutomatedUpdateDate: Optional[str] = None
    Cancellable: Optional[bool] = None
    CurrentVersion: Optional[str] = None
    Description: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    UpdateStatus: Optional[str] = None


class AwsElasticsearchDomainVPCOptionsOutput(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VPCId: Optional[str] = None


class AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None


class AwsElasticsearchDomainLogPublishingOptionsLogConfig(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None


class AwsElasticsearchDomainVPCOptions(BaseValidatorModel):
    AvailabilityZones: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VPCId: Optional[str] = None


class AwsElbAppCookieStickinessPolicy(BaseValidatorModel):
    CookieName: Optional[str] = None
    PolicyName: Optional[str] = None


class AwsElbLbCookieStickinessPolicy(BaseValidatorModel):
    CookieExpirationPeriod: Optional[int] = None
    PolicyName: Optional[str] = None


class AwsElbLoadBalancerAccessLog(BaseValidatorModel):
    EmitInterval: Optional[int] = None
    Enabled: Optional[bool] = None
    S3BucketName: Optional[str] = None
    S3BucketPrefix: Optional[str] = None


class AwsElbLoadBalancerAdditionalAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class AwsElbLoadBalancerConnectionDraining(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Timeout: Optional[int] = None


class AwsElbLoadBalancerConnectionSettings(BaseValidatorModel):
    IdleTimeout: Optional[int] = None


class AwsElbLoadBalancerCrossZoneLoadBalancing(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsElbLoadBalancerBackendServerDescriptionOutput(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None


class AwsElbLoadBalancerBackendServerDescription(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[Sequence[str]] = None


class AwsElbLoadBalancerHealthCheck(BaseValidatorModel):
    HealthyThreshold: Optional[int] = None
    Interval: Optional[int] = None
    Target: Optional[str] = None
    Timeout: Optional[int] = None
    UnhealthyThreshold: Optional[int] = None


class AwsElbLoadBalancerInstance(BaseValidatorModel):
    InstanceId: Optional[str] = None


class AwsElbLoadBalancerSourceSecurityGroup(BaseValidatorModel):
    GroupName: Optional[str] = None
    OwnerAlias: Optional[str] = None


class AwsElbv2LoadBalancerAttribute(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class LoadBalancerState(BaseValidatorModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None


class AwsEventSchemasRegistryDetails(BaseValidatorModel):
    Description: Optional[str] = None
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None


class AwsEventsEndpointEventBusesDetails(BaseValidatorModel):
    EventBusArn: Optional[str] = None


class AwsEventsEndpointReplicationConfigDetails(BaseValidatorModel):
    State: Optional[str] = None


class AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails(BaseValidatorModel):
    HealthCheck: Optional[str] = None


class AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails(BaseValidatorModel):
    Route: Optional[str] = None


class AwsEventsEventbusDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Policy: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesCloudTrailDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesDnsLogsDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesFlowLogsDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesS3LogsDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails(BaseValidatorModel):
    Status: Optional[str] = None


class AwsGuardDutyDetectorFeaturesDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None


class AwsIamAccessKeySessionContextAttributes(BaseValidatorModel):
    MfaAuthenticated: Optional[bool] = None
    CreationDate: Optional[str] = None


class AwsIamAttachedManagedPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None


class AwsIamGroupPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None


class AwsIamInstanceProfileRole(BaseValidatorModel):
    Arn: Optional[str] = None
    AssumeRolePolicyDocument: Optional[str] = None
    CreateDate: Optional[str] = None
    Path: Optional[str] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None


class AwsIamPermissionsBoundary(BaseValidatorModel):
    PermissionsBoundaryArn: Optional[str] = None
    PermissionsBoundaryType: Optional[str] = None


class AwsIamPolicyVersion(BaseValidatorModel):
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    CreateDate: Optional[str] = None


class AwsIamRolePolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None


class AwsIamUserPolicy(BaseValidatorModel):
    PolicyName: Optional[str] = None


class AwsKinesisStreamStreamEncryptionDetails(BaseValidatorModel):
    EncryptionType: Optional[str] = None
    KeyId: Optional[str] = None


class AwsKmsKeyDetails(BaseValidatorModel):
    AWSAccountId: Optional[str] = None
    CreationDate: Optional[float] = None
    KeyId: Optional[str] = None
    KeyManager: Optional[str] = None
    KeyState: Optional[str] = None
    Origin: Optional[str] = None
    Description: Optional[str] = None
    KeyRotationStatus: Optional[bool] = None


class AwsLambdaFunctionCode(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ZipFile: Optional[str] = None


class AwsLambdaFunctionDeadLetterConfig(BaseValidatorModel):
    TargetArn: Optional[str] = None


class AwsLambdaFunctionLayer(BaseValidatorModel):
    Arn: Optional[str] = None
    CodeSize: Optional[int] = None


class AwsLambdaFunctionTracingConfig(BaseValidatorModel):
    Mode: Optional[str] = None


class AwsLambdaFunctionVpcConfigOutput(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None


class AwsLambdaFunctionEnvironmentError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None


class AwsLambdaFunctionVpcConfig(BaseValidatorModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None


class AwsLambdaLayerVersionDetailsOutput(BaseValidatorModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[List[str]] = None
    CreatedDate: Optional[str] = None


class AwsLambdaLayerVersionDetails(BaseValidatorModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[Sequence[str]] = None
    CreatedDate: Optional[str] = None


class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutput(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoClientAuthenticationTlsDetails(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None


class AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails(BaseValidatorModel):
    DataVolumeKMSKeyId: Optional[str] = None


class AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails(BaseValidatorModel):
    InCluster: Optional[bool] = None
    ClientBroker: Optional[str] = None


class AwsNetworkFirewallFirewallSubnetMappingsDetails(BaseValidatorModel):
    SubnetId: Optional[str] = None


class AwsOpenSearchServiceDomainMasterUserOptionsDetails(BaseValidatorModel):
    MasterUserArn: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None


class AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None


class AwsOpenSearchServiceDomainDomainEndpointOptionsDetails(BaseValidatorModel):
    CustomEndpointCertificateArn: Optional[str] = None
    CustomEndpointEnabled: Optional[bool] = None
    EnforceHTTPS: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    TLSSecurityPolicy: Optional[str] = None


class AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None


class AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails(BaseValidatorModel):
    AutomatedUpdateDate: Optional[str] = None
    Cancellable: Optional[bool] = None
    CurrentVersion: Optional[str] = None
    Description: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    UpdateStatus: Optional[str] = None
    OptionalDeployment: Optional[bool] = None


class AwsOpenSearchServiceDomainVpcOptionsDetailsOutput(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None


class AwsOpenSearchServiceDomainLogPublishingOption(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None


class AwsOpenSearchServiceDomainVpcOptionsDetails(BaseValidatorModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None


class AwsRdsDbClusterAssociatedRole(BaseValidatorModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbClusterMember(BaseValidatorModel):
    IsClusterWriter: Optional[bool] = None
    PromotionTier: Optional[int] = None
    DbInstanceIdentifier: Optional[str] = None
    DbClusterParameterGroupStatus: Optional[str] = None


class AwsRdsDbClusterOptionGroupMembership(BaseValidatorModel):
    DbClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbDomainMembership(BaseValidatorModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    Fqdn: Optional[str] = None
    IamRoleName: Optional[str] = None


class AwsRdsDbInstanceVpcSecurityGroup(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutput(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None


class AwsRdsDbClusterSnapshotDbClusterSnapshotAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[Sequence[str]] = None


class AwsRdsDbInstanceAssociatedRole(BaseValidatorModel):
    RoleArn: Optional[str] = None
    FeatureName: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbInstanceEndpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None


class AwsRdsDbOptionGroupMembership(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbParameterGroup(BaseValidatorModel):
    DbParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None


class AwsRdsDbProcessorFeature(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsRdsDbStatusInfo(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class AwsRdsPendingCloudWatchLogsExportsOutput(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None


class AwsRdsDbSecurityGroupEc2SecurityGroup(BaseValidatorModel):
    Ec2SecurityGroupId: Optional[str] = None
    Ec2SecurityGroupName: Optional[str] = None
    Ec2SecurityGroupOwnerId: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbSecurityGroupIpRange(BaseValidatorModel):
    CidrIp: Optional[str] = None
    Status: Optional[str] = None


class AwsRdsDbSubnetGroupSubnetAvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class AwsRdsEventSubscriptionDetailsOutput(BaseValidatorModel):
    CustSubscriptionId: Optional[str] = None
    CustomerAwsId: Optional[str] = None
    Enabled: Optional[bool] = None
    EventCategoriesList: Optional[List[str]] = None
    EventSubscriptionArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    SourceType: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None


class AwsRdsEventSubscriptionDetails(BaseValidatorModel):
    CustSubscriptionId: Optional[str] = None
    CustomerAwsId: Optional[str] = None
    Enabled: Optional[bool] = None
    EventCategoriesList: Optional[Sequence[str]] = None
    EventSubscriptionArn: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SourceIdsList: Optional[Sequence[str]] = None
    SourceType: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None


class AwsRdsPendingCloudWatchLogsExports(BaseValidatorModel):
    LogTypesToEnable: Optional[Sequence[str]] = None
    LogTypesToDisable: Optional[Sequence[str]] = None


class AwsRedshiftClusterClusterNode(BaseValidatorModel):
    NodeRole: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PublicIpAddress: Optional[str] = None


class AwsRedshiftClusterClusterParameterStatus(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterApplyErrorDescription: Optional[str] = None


class AwsRedshiftClusterClusterSecurityGroup(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None


class AwsRedshiftClusterClusterSnapshotCopyStatus(BaseValidatorModel):
    DestinationRegion: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    RetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None


class AwsRedshiftClusterDeferredMaintenanceWindow(BaseValidatorModel):
    DeferMaintenanceEndTime: Optional[str] = None
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[str] = None


class AwsRedshiftClusterElasticIpStatus(BaseValidatorModel):
    ElasticIp: Optional[str] = None
    Status: Optional[str] = None


class AwsRedshiftClusterEndpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None


class AwsRedshiftClusterHsmStatus(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    Status: Optional[str] = None


class AwsRedshiftClusterIamRole(BaseValidatorModel):
    ApplyStatus: Optional[str] = None
    IamRoleArn: Optional[str] = None


class AwsRedshiftClusterLoggingStatus(BaseValidatorModel):
    BucketName: Optional[str] = None
    LastFailureMessage: Optional[str] = None
    LastFailureTime: Optional[str] = None
    LastSuccessfulDeliveryTime: Optional[str] = None
    LoggingEnabled: Optional[bool] = None
    S3KeyPrefix: Optional[str] = None


class AwsRedshiftClusterPendingModifiedValues(BaseValidatorModel):
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    ClusterIdentifier: Optional[str] = None
    ClusterType: Optional[str] = None
    ClusterVersion: Optional[str] = None
    EncryptionType: Optional[str] = None
    EnhancedVpcRouting: Optional[bool] = None
    MaintenanceTrackName: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None


class AwsRedshiftClusterResizeInfo(BaseValidatorModel):
    AllowCancelResize: Optional[bool] = None
    ResizeType: Optional[str] = None


class AwsRedshiftClusterRestoreStatus(BaseValidatorModel):
    CurrentRestoreRateInMegaBytesPerSecond: Optional[float] = None
    ElapsedTimeInSeconds: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None
    ProgressInMegaBytes: Optional[int] = None
    SnapshotSizeInMegaBytes: Optional[int] = None
    Status: Optional[str] = None


class AwsRedshiftClusterVpcSecurityGroup(BaseValidatorModel):
    Status: Optional[str] = None
    VpcSecurityGroupId: Optional[str] = None


class AwsRoute53HostedZoneConfigDetails(BaseValidatorModel):
    Comment: Optional[str] = None


class AwsRoute53HostedZoneVpcDetails(BaseValidatorModel):
    Id: Optional[str] = None
    Region: Optional[str] = None


class CloudWatchLogsLogGroupArnConfigDetails(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    HostedZoneId: Optional[str] = None
    Id: Optional[str] = None


class AwsS3AccessPointVpcConfigurationDetails(BaseValidatorModel):
    VpcId: Optional[str] = None


class AwsS3AccountPublicAccessBlockDetails(BaseValidatorModel):
    BlockPublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None


class AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails(BaseValidatorModel):
    Date: Optional[str] = None
    Days: Optional[int] = None
    StorageClass: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetails(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class AwsS3BucketBucketVersioningConfiguration(BaseValidatorModel):
    IsMfaDeleteEnabled: Optional[bool] = None
    Status: Optional[str] = None


class AwsS3BucketLoggingConfiguration(BaseValidatorModel):
    DestinationBucketName: Optional[str] = None
    LogFilePrefix: Optional[str] = None


class AwsS3BucketNotificationConfigurationS3KeyFilterRule(BaseValidatorModel):
    Name: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType] = None
    Value: Optional[str] = None


class AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails(BaseValidatorModel):
    Days: Optional[int] = None
    Mode: Optional[str] = None
    Years: Optional[int] = None


class AwsS3BucketServerSideEncryptionByDefault(BaseValidatorModel):
    SSEAlgorithm: Optional[str] = None
    KMSMasterKeyID: Optional[str] = None


class AwsS3BucketWebsiteConfigurationRoutingRuleCondition(BaseValidatorModel):
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None


class AwsS3ObjectDetails(BaseValidatorModel):
    LastModified: Optional[str] = None
    ETag: Optional[str] = None
    VersionId: Optional[str] = None
    ContentType: Optional[str] = None
    ServerSideEncryption: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None


class AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails(BaseValidatorModel):
    MinimumInstanceMetadataServiceVersion: Optional[str] = None


class AwsSecretsManagerSecretRotationRules(BaseValidatorModel):
    AutomaticallyAfterDays: Optional[int] = None


class BooleanFilter(BaseValidatorModel):
    Value: Optional[bool] = None


class IpFilter(BaseValidatorModel):
    Cidr: Optional[str] = None


class KeywordFilter(BaseValidatorModel):
    Value: Optional[str] = None


class AwsSecurityFindingIdentifier(BaseValidatorModel):
    Id: str
    ProductArn: str


class GeneratorDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[List[str]] = None


class PatchSummary(BaseValidatorModel):
    Id: str
    InstalledCount: Optional[int] = None
    MissingCount: Optional[int] = None
    FailedCount: Optional[int] = None
    InstalledOtherCount: Optional[int] = None
    InstalledRejectedCount: Optional[int] = None
    InstalledPendingReboot: Optional[int] = None
    OperationStartTime: Optional[str] = None
    OperationEndTime: Optional[str] = None
    RebootOption: Optional[str] = None
    Operation: Optional[str] = None


class ProcessDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Path: Optional[str] = None
    Pid: Optional[int] = None
    ParentPid: Optional[int] = None
    LaunchedAt: Optional[str] = None
    TerminatedAt: Optional[str] = None


class Severity(BaseValidatorModel):
    Product: Optional[float] = None
    Label: Optional[SeverityLabelType] = None
    Normalized: Optional[int] = None
    Original: Optional[str] = None


class Workflow(BaseValidatorModel):
    Status: Optional[WorkflowStatusType] = None


class AwsSqsQueueDetails(BaseValidatorModel):
    KmsDataKeyReusePeriodSeconds: Optional[int] = None
    KmsMasterKeyId: Optional[str] = None
    QueueName: Optional[str] = None
    DeadLetterTargetArn: Optional[str] = None


class AwsSsmComplianceSummary(BaseValidatorModel):
    Status: Optional[str] = None
    CompliantCriticalCount: Optional[int] = None
    CompliantHighCount: Optional[int] = None
    CompliantMediumCount: Optional[int] = None
    ExecutionType: Optional[str] = None
    NonCompliantCriticalCount: Optional[int] = None
    CompliantInformationalCount: Optional[int] = None
    NonCompliantInformationalCount: Optional[int] = None
    CompliantUnspecifiedCount: Optional[int] = None
    NonCompliantLowCount: Optional[int] = None
    NonCompliantHighCount: Optional[int] = None
    CompliantLowCount: Optional[int] = None
    ComplianceType: Optional[str] = None
    PatchBaselineId: Optional[str] = None
    OverallSeverity: Optional[str] = None
    NonCompliantMediumCount: Optional[int] = None
    NonCompliantUnspecifiedCount: Optional[int] = None
    PatchGroup: Optional[str] = None


class AwsStepFunctionStateMachineTracingConfigurationDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None


class WafExcludedRule(BaseValidatorModel):
    RuleId: Optional[str] = None


class AwsWafv2CustomHttpHeader(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class AwsWafv2VisibilityConfigDetails(BaseValidatorModel):
    CloudWatchMetricsEnabled: Optional[bool] = None
    MetricName: Optional[str] = None
    SampledRequestsEnabled: Optional[bool] = None


class AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails(BaseValidatorModel):
    ImmunityTime: Optional[int] = None


class BatchDeleteAutomationRulesRequest(BaseValidatorModel):
    AutomationRulesArns: Sequence[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnprocessedAutomationRule(BaseValidatorModel):
    RuleArn: Optional[str] = None
    ErrorCode: Optional[int] = None
    ErrorMessage: Optional[str] = None


class BatchDisableStandardsRequest(BaseValidatorModel):
    StandardsSubscriptionArns: Sequence[str]


class StandardsSubscriptionRequest(BaseValidatorModel):
    StandardsArn: str
    StandardsInput: Optional[Mapping[str, str]] = None


class BatchGetAutomationRulesRequest(BaseValidatorModel):
    AutomationRulesArns: Sequence[str]


class ConfigurationPolicyAssociationSummary(BaseValidatorModel):
    ConfigurationPolicyId: Optional[str] = None
    TargetId: Optional[str] = None
    TargetType: Optional[TargetTypeType] = None
    AssociationType: Optional[AssociationTypeType] = None
    UpdatedAt: Optional[datetime] = None
    AssociationStatus: Optional[ConfigurationPolicyAssociationStatusType] = None
    AssociationStatusMessage: Optional[str] = None


class BatchGetSecurityControlsRequest(BaseValidatorModel):
    SecurityControlIds: Sequence[str]


class UnprocessedSecurityControl(BaseValidatorModel):
    SecurityControlId: str
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None


class StandardsControlAssociationId(BaseValidatorModel):
    SecurityControlId: str
    StandardsArn: str


class StandardsControlAssociationDetail(BaseValidatorModel):
    StandardsArn: str
    SecurityControlId: str
    SecurityControlArn: str
    AssociationStatus: AssociationStatusType
    RelatedRequirements: Optional[List[str]] = None
    UpdatedAt: Optional[datetime] = None
    UpdatedReason: Optional[str] = None
    StandardsControlTitle: Optional[str] = None
    StandardsControlDescription: Optional[str] = None
    StandardsControlArns: Optional[List[str]] = None


class ImportFindingsError(BaseValidatorModel):
    Id: str
    ErrorCode: str
    ErrorMessage: str


class StandardsControlAssociationUpdate(BaseValidatorModel):
    StandardsArn: str
    SecurityControlId: str
    AssociationStatus: AssociationStatusType
    UpdatedReason: Optional[str] = None


class BooleanConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[bool] = None


class Cell(BaseValidatorModel):
    Column: Optional[int] = None
    Row: Optional[int] = None
    ColumnName: Optional[str] = None
    CellReference: Optional[str] = None


class ClassificationStatus(BaseValidatorModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None


class CodeVulnerabilitiesFilePath(BaseValidatorModel):
    EndLine: Optional[int] = None
    FileName: Optional[str] = None
    FilePath: Optional[str] = None
    StartLine: Optional[int] = None


class SecurityControlParameterOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[List[str]] = None


class StatusReason(BaseValidatorModel):
    ReasonCode: str
    Description: Optional[str] = None


class DoubleConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[float] = None
    Min: Optional[float] = None
    Max: Optional[float] = None


class EnumConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[List[str]] = None


class EnumListConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[List[str]] = None
    MaxItems: Optional[int] = None
    AllowedValues: Optional[List[str]] = None


class IntegerConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[int] = None
    Min: Optional[int] = None
    Max: Optional[int] = None


class IntegerListConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[List[int]] = None
    Min: Optional[int] = None
    Max: Optional[int] = None
    MaxItems: Optional[int] = None


class StringConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    Re2Expression: Optional[str] = None
    ExpressionDescription: Optional[str] = None


class StringListConfigurationOptions(BaseValidatorModel):
    DefaultValue: Optional[List[str]] = None
    Re2Expression: Optional[str] = None
    MaxItems: Optional[int] = None
    ExpressionDescription: Optional[str] = None


class Target(BaseValidatorModel):
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    RootId: Optional[str] = None


class ConfigurationPolicySummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    ServiceEnabled: Optional[bool] = None


class VolumeMount(BaseValidatorModel):
    Name: Optional[str] = None
    MountPath: Optional[str] = None


class CreateActionTargetRequest(BaseValidatorModel):
    Name: str
    Description: str
    Id: str


class CreateFindingAggregatorRequest(BaseValidatorModel):
    RegionLinkingMode: str
    Regions: Optional[Sequence[str]] = None


class Result(BaseValidatorModel):
    AccountId: Optional[str] = None
    ProcessingResult: Optional[str] = None


class DateRange(BaseValidatorModel):
    Value: Optional[int] = None
    Unit: Optional[Literal["DAYS"]] = None


class DeclineInvitationsRequest(BaseValidatorModel):
    AccountIds: Sequence[str]


class DeleteActionTargetRequest(BaseValidatorModel):
    ActionTargetArn: str


class DeleteConfigurationPolicyRequest(BaseValidatorModel):
    Identifier: str


class DeleteFindingAggregatorRequest(BaseValidatorModel):
    FindingAggregatorArn: str


class DeleteInsightRequest(BaseValidatorModel):
    InsightArn: str


class DeleteInvitationsRequest(BaseValidatorModel):
    AccountIds: Sequence[str]


class DeleteMembersRequest(BaseValidatorModel):
    AccountIds: Sequence[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeActionTargetsRequest(BaseValidatorModel):
    ActionTargetArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeHubRequest(BaseValidatorModel):
    HubArn: Optional[str] = None


class OrganizationConfiguration(BaseValidatorModel):
    ConfigurationType: Optional[OrganizationConfigurationConfigurationTypeType] = None
    Status: Optional[OrganizationConfigurationStatusType] = None
    StatusMessage: Optional[str] = None


class DescribeProductsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProductArn: Optional[str] = None


class Product(BaseValidatorModel):
    ProductArn: str
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Description: Optional[str] = None
    Categories: Optional[List[str]] = None
    IntegrationTypes: Optional[List[IntegrationTypeType]] = None
    MarketplaceUrl: Optional[str] = None
    ActivationUrl: Optional[str] = None
    ProductSubscriptionResourcePolicy: Optional[str] = None


class DescribeStandardsControlsRequest(BaseValidatorModel):
    StandardsSubscriptionArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StandardsControl(BaseValidatorModel):
    StandardsControlArn: Optional[str] = None
    ControlStatus: Optional[ControlStatusType] = None
    DisabledReason: Optional[str] = None
    ControlStatusUpdatedAt: Optional[datetime] = None
    ControlId: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None
    RemediationUrl: Optional[str] = None
    SeverityRating: Optional[SeverityRatingType] = None
    RelatedRequirements: Optional[List[str]] = None


class DescribeStandardsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DisableImportFindingsForProductRequest(BaseValidatorModel):
    ProductSubscriptionArn: str


class DisableOrganizationAdminAccountRequest(BaseValidatorModel):
    AdminAccountId: str


class DisassociateMembersRequest(BaseValidatorModel):
    AccountIds: Sequence[str]


class EnableImportFindingsForProductRequest(BaseValidatorModel):
    ProductArn: str


class EnableOrganizationAdminAccountRequest(BaseValidatorModel):
    AdminAccountId: str


class EnableSecurityHubRequest(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    EnableDefaultStandards: Optional[bool] = None
    ControlFindingGenerator: Optional[ControlFindingGeneratorType] = None


class FilePaths(BaseValidatorModel):
    FilePath: Optional[str] = None
    FileName: Optional[str] = None
    ResourceId: Optional[str] = None
    Hash: Optional[str] = None


class FindingAggregator(BaseValidatorModel):
    FindingAggregatorArn: Optional[str] = None


class FindingHistoryUpdate(BaseValidatorModel):
    UpdatedField: Optional[str] = None
    OldValue: Optional[str] = None
    NewValue: Optional[str] = None


class FindingProviderSeverity(BaseValidatorModel):
    Label: Optional[SeverityLabelType] = None
    Original: Optional[str] = None


class FirewallPolicyStatefulRuleGroupReferencesDetails(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class FirewallPolicyStatelessRuleGroupReferencesDetails(BaseValidatorModel):
    Priority: Optional[int] = None
    ResourceArn: Optional[str] = None


class GeneratorDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[Sequence[str]] = None


class Invitation(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    InvitedAt: Optional[datetime] = None
    MemberStatus: Optional[str] = None


class GetConfigurationPolicyRequest(BaseValidatorModel):
    Identifier: str


class GetEnabledStandardsRequest(BaseValidatorModel):
    StandardsSubscriptionArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetFindingAggregatorRequest(BaseValidatorModel):
    FindingAggregatorArn: str


class SortCriterion(BaseValidatorModel):
    Field: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None


class GetInsightResultsRequest(BaseValidatorModel):
    InsightArn: str


class GetInsightsRequest(BaseValidatorModel):
    InsightArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetMembersRequest(BaseValidatorModel):
    AccountIds: Sequence[str]


class Member(BaseValidatorModel):
    AccountId: Optional[str] = None
    Email: Optional[str] = None
    MasterId: Optional[str] = None
    AdministratorId: Optional[str] = None
    MemberStatus: Optional[str] = None
    InvitedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None


class GetSecurityControlDefinitionRequest(BaseValidatorModel):
    SecurityControlId: str


class InsightResultValue(BaseValidatorModel):
    GroupByAttributeValue: str
    Count: int


class InviteMembersRequest(BaseValidatorModel):
    AccountIds: Sequence[str]


class ListAutomationRulesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListConfigurationPoliciesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEnabledProductsForImportRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListFindingAggregatorsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInvitationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListMembersRequest(BaseValidatorModel):
    OnlyAssociated: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListOrganizationAdminAccountsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSecurityControlDefinitionsRequest(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListStandardsControlAssociationsRequest(BaseValidatorModel):
    SecurityControlId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class StandardsControlAssociationSummary(BaseValidatorModel):
    StandardsArn: str
    SecurityControlId: str
    SecurityControlArn: str
    AssociationStatus: AssociationStatusType
    RelatedRequirements: Optional[List[str]] = None
    UpdatedAt: Optional[datetime] = None
    UpdatedReason: Optional[str] = None
    StandardsControlTitle: Optional[str] = None
    StandardsControlDescription: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class NetworkAutonomousSystem(BaseValidatorModel):
    Name: Optional[str] = None
    Number: Optional[int] = None


class NetworkConnection(BaseValidatorModel):
    Direction: Optional[ConnectionDirectionType] = None


class NetworkGeoLocation(BaseValidatorModel):
    City: Optional[str] = None
    Country: Optional[str] = None
    Lat: Optional[float] = None
    Lon: Optional[float] = None


class PortRange(BaseValidatorModel):
    Begin: Optional[int] = None
    End: Optional[int] = None


class Range(BaseValidatorModel):
    Start: Optional[int] = None
    End: Optional[int] = None
    StartColumn: Optional[int] = None


class Record(BaseValidatorModel):
    JsonPath: Optional[str] = None
    RecordIndex: Optional[int] = None


class ParameterValueOutput(BaseValidatorModel):
    Integer: Optional[int] = None
    IntegerList: Optional[List[int]] = None
    Double: Optional[float] = None
    String: Optional[str] = None
    StringList: Optional[List[str]] = None
    Boolean: Optional[bool] = None
    Enum: Optional[str] = None
    EnumList: Optional[List[str]] = None


class ParameterValue(BaseValidatorModel):
    Integer: Optional[int] = None
    IntegerList: Optional[Sequence[int]] = None
    Double: Optional[float] = None
    String: Optional[str] = None
    StringList: Optional[Sequence[str]] = None
    Boolean: Optional[bool] = None
    Enum: Optional[str] = None
    EnumList: Optional[Sequence[str]] = None


class RuleGroupSourceListDetailsOutput(BaseValidatorModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[List[str]] = None
    Targets: Optional[List[str]] = None


class RuleGroupSourceListDetails(BaseValidatorModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[str]] = None


class RuleGroupSourceStatefulRulesOptionsDetailsOutput(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None


class RuleGroupSourceStatefulRulesOptionsDetails(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[Sequence[str]] = None


class RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class RuleGroupSourceStatelessRuleMatchAttributesDestinations(BaseValidatorModel):
    AddressDefinition: Optional[str] = None


class RuleGroupSourceStatelessRuleMatchAttributesSourcePorts(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class RuleGroupSourceStatelessRuleMatchAttributesSources(BaseValidatorModel):
    AddressDefinition: Optional[str] = None


class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutput(BaseValidatorModel):
    Flags: Optional[List[str]] = None
    Masks: Optional[List[str]] = None


class RuleGroupSourceStatelessRuleMatchAttributesTcpFlags(BaseValidatorModel):
    Flags: Optional[Sequence[str]] = None
    Masks: Optional[Sequence[str]] = None


class RuleGroupVariablesIpSetsDetailsOutput(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class RuleGroupVariablesIpSetsDetails(BaseValidatorModel):
    Definition: Optional[Sequence[str]] = None


class RuleGroupVariablesPortSetsDetailsOutput(BaseValidatorModel):
    Definition: Optional[List[str]] = None


class RuleGroupVariablesPortSetsDetails(BaseValidatorModel):
    Definition: Optional[Sequence[str]] = None


class SecurityControlParameter(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[Sequence[str]] = None


class SoftwarePackage(BaseValidatorModel):
    Name: Optional[str] = None
    Version: Optional[str] = None
    Epoch: Optional[str] = None
    Release: Optional[str] = None
    Architecture: Optional[str] = None
    PackageManager: Optional[str] = None
    FilePath: Optional[str] = None
    FixedInVersion: Optional[str] = None
    Remediation: Optional[str] = None
    SourceLayerHash: Optional[str] = None
    SourceLayerArn: Optional[str] = None


class StandardsManagedBy(BaseValidatorModel):
    Company: Optional[str] = None
    Product: Optional[str] = None


class StandardsStatusReason(BaseValidatorModel):
    StatusReasonCode: StatusReasonCodeType


class StatelessCustomPublishMetricActionDimension(BaseValidatorModel):
    Value: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateActionTargetRequest(BaseValidatorModel):
    ActionTargetArn: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateFindingAggregatorRequest(BaseValidatorModel):
    FindingAggregatorArn: str
    RegionLinkingMode: str
    Regions: Optional[Sequence[str]] = None


class UpdateSecurityHubConfigurationRequest(BaseValidatorModel):
    AutoEnableControls: Optional[bool] = None
    ControlFindingGenerator: Optional[ControlFindingGeneratorType] = None


class UpdateStandardsControlRequest(BaseValidatorModel):
    StandardsControlArn: str
    ControlStatus: Optional[ControlStatusType] = None
    DisabledReason: Optional[str] = None


class VulnerabilityVendor(BaseValidatorModel):
    Name: str
    Url: Optional[str] = None
    VendorSeverity: Optional[str] = None
    VendorCreatedAt: Optional[str] = None
    VendorUpdatedAt: Optional[str] = None


class CreateMembersRequest(BaseValidatorModel):
    AccountDetails: Sequence[AccountDetails]


class ActionRemoteIpDetails(BaseValidatorModel):
    IpAddressV4: Optional[str] = None
    Organization: Optional[IpOrganizationDetails] = None
    Country: Optional[Country] = None
    City: Optional[City] = None
    GeoLocation: Optional[GeoLocation] = None


class CvssOutput(BaseValidatorModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[List[Adjustment]] = None


class Cvss(BaseValidatorModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[Sequence[Adjustment]] = None


class ListConfigurationPolicyAssociationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[AssociationFilters] = None


class AssociationSetDetails(BaseValidatorModel):
    AssociationState: Optional[AssociationStateDetails] = None
    GatewayId: Optional[str] = None
    Main: Optional[bool] = None
    RouteTableAssociationId: Optional[str] = None
    RouteTableId: Optional[str] = None
    SubnetId: Optional[str] = None


class NoteUpdate(BaseValidatorModel):
    pass


class AutomationRulesFindingFieldsUpdateOutput(BaseValidatorModel):
    Note: Optional[NoteUpdate] = None
    Severity: Optional[SeverityUpdate] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[List[str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Workflow: Optional[WorkflowUpdate] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None


class AutomationRulesFindingFieldsUpdate(BaseValidatorModel):
    Note: Optional[NoteUpdate] = None
    Severity: Optional[SeverityUpdate] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[Sequence[str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Workflow: Optional[WorkflowUpdate] = None
    RelatedFindings: Optional[Sequence[RelatedFinding]] = None


class AwsAmazonMqBrokerLogsDetails(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None
    AuditLogGroup: Optional[str] = None
    GeneralLogGroup: Optional[str] = None
    Pending: Optional[AwsAmazonMqBrokerLogsPendingDetails] = None


class AwsApiGatewayRestApiDetailsOutput(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[List[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationOutput] = None


class AwsApiGatewayStageDetailsOutput(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[List[AwsApiGatewayMethodSettings]] = None
    Variables: Optional[Dict[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettings] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsOutput] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None


class AwsApiGatewayV2ApiDetailsOutput(BaseValidatorModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationOutput] = None


class AwsApiGatewayV2StageDetailsOutput(BaseValidatorModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettings] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettings] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Dict[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettings] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None


class AwsApiGatewayV2StageDetails(BaseValidatorModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettings] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettings] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Mapping[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettings] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None


class AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails(BaseValidatorModel):
    AuthenticationType: Optional[str] = None
    LambdaAuthorizerConfig: Optional[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetails] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetails] = None


class AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails(BaseValidatorModel):
    pass


class AwsAthenaWorkGroupConfigurationResultConfigurationDetails(BaseValidatorModel):
    EncryptionConfiguration: Optional[ AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetails ] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification(BaseValidatorModel):
    pass


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails(BaseValidatorModel):
    pass


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetails(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[ AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecification ] = None
    Overrides: Optional[ Sequence[ AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails ] ] = None


class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetails] = None
    NoDevice: Optional[bool] = None
    VirtualName: Optional[str] = None


class AwsBackupBackupPlanRuleCopyActionsDetails(BaseValidatorModel):
    DestinationBackupVaultArn: Optional[str] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetails] = None


class AwsBackupBackupVaultDetailsOutput(BaseValidatorModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsOutput] = None
    AccessPolicy: Optional[str] = None


class AwsBackupRecoveryPointDetails(BaseValidatorModel):
    BackupSizeInBytes: Optional[int] = None
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    CalculatedLifecycle: Optional[AwsBackupRecoveryPointCalculatedLifecycleDetails] = None
    CompletionDate: Optional[str] = None
    CreatedBy: Optional[AwsBackupRecoveryPointCreatedByDetails] = None
    CreationDate: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IsEncrypted: Optional[bool] = None
    LastRestoreTime: Optional[str] = None
    Lifecycle: Optional[AwsBackupRecoveryPointLifecycleDetails] = None
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    SourceBackupVaultArn: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    StorageClass: Optional[str] = None


class AwsCertificateManagerCertificateResourceRecord(BaseValidatorModel):
    pass


class AwsCertificateManagerCertificateDomainValidationOptionOutput(BaseValidatorModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecord] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[List[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None


class AwsCertificateManagerCertificateDomainValidationOption(BaseValidatorModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecord] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[Sequence[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None


class AwsCloudFormationStackDetailsOutput(BaseValidatorModel):
    Capabilities: Optional[List[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetails] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    Outputs: Optional[List[AwsCloudFormationStackOutputsDetails]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None


class AwsCloudFormationStackDetails(BaseValidatorModel):
    Capabilities: Optional[Sequence[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetails] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[Sequence[str]] = None
    Outputs: Optional[Sequence[AwsCloudFormationStackOutputsDetails]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None


class AwsCloudFrontDistributionCacheBehaviorsOutput(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionCacheBehavior]] = None


class AwsCloudFrontDistributionCacheBehaviors(BaseValidatorModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionCacheBehavior]] = None


class AwsCloudFrontDistributionOriginCustomOriginConfigOutput(BaseValidatorModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[AwsCloudFrontDistributionOriginSslProtocolsOutput] = None


class AwsCloudFrontDistributionOriginGroupFailoverOutput(BaseValidatorModel):
    StatusCodes: Optional[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutput] = None


class AwsCloudWatchAlarmDetailsOutput(BaseValidatorModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[List[AwsCloudWatchAlarmDimensionsDetails]] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    EvaluationPeriods: Optional[int] = None
    ExtendedStatistic: Optional[str] = None
    InsufficientDataActions: Optional[List[str]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    OkActions: Optional[List[str]] = None
    Period: Optional[int] = None
    Statistic: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdMetricId: Optional[str] = None
    TreatMissingData: Optional[str] = None
    Unit: Optional[str] = None


class AwsCloudWatchAlarmDetails(BaseValidatorModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[Sequence[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[Sequence[AwsCloudWatchAlarmDimensionsDetails]] = None
    EvaluateLowSampleCountPercentile: Optional[str] = None
    EvaluationPeriods: Optional[int] = None
    ExtendedStatistic: Optional[str] = None
    InsufficientDataActions: Optional[Sequence[str]] = None
    MetricName: Optional[str] = None
    Namespace: Optional[str] = None
    OkActions: Optional[Sequence[str]] = None
    Period: Optional[int] = None
    Statistic: Optional[str] = None
    Threshold: Optional[float] = None
    ThresholdMetricId: Optional[str] = None
    TreatMissingData: Optional[str] = None
    Unit: Optional[str] = None


class AwsCodeBuildProjectLogsConfigDetails(BaseValidatorModel):
    CloudWatchLogs: Optional[AwsCodeBuildProjectLogsConfigCloudWatchLogsDetails] = None
    S3Logs: Optional[AwsCodeBuildProjectLogsConfigS3LogsDetails] = None


class AwsDmsReplicationInstanceDetailsOutput(BaseValidatorModel):
    AllocatedStorage: Optional[int] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    EngineVersion: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ReplicationInstanceClass: Optional[str] = None
    ReplicationInstanceIdentifier: Optional[str] = None
    ReplicationSubnetGroup: Optional[ AwsDmsReplicationInstanceReplicationSubnetGroupDetails ] = None
    VpcSecurityGroups: Optional[List[AwsDmsReplicationInstanceVpcSecurityGroupsDetails]] = None


class AwsDmsReplicationInstanceDetails(BaseValidatorModel):
    AllocatedStorage: Optional[int] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    EngineVersion: Optional[str] = None
    KmsKeyId: Optional[str] = None
    MultiAZ: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ReplicationInstanceClass: Optional[str] = None
    ReplicationInstanceIdentifier: Optional[str] = None
    ReplicationSubnetGroup: Optional[ AwsDmsReplicationInstanceReplicationSubnetGroupDetails ] = None
    VpcSecurityGroups: Optional[ Sequence[AwsDmsReplicationInstanceVpcSecurityGroupsDetails] ] = None


class AwsDynamoDbTableGlobalSecondaryIndexOutput(BaseValidatorModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    Projection: Optional[AwsDynamoDbTableProjectionOutput] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughput] = None


class AwsDynamoDbTableLocalSecondaryIndexOutput(BaseValidatorModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    Projection: Optional[AwsDynamoDbTableProjectionOutput] = None


class AwsDynamoDbTableReplicaGlobalSecondaryIndex(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedThroughputOverride: Optional[AwsDynamoDbTableProvisionedThroughputOverride] = None


class AwsEc2ClientVpnEndpointClientConnectOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None
    Status: Optional[AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetails] = None


class AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetails] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None


class AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails(BaseValidatorModel):
    pass


class AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails(BaseValidatorModel):
    CapacityReservationPreference: Optional[str] = None
    CapacityReservationTarget: Optional[ AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails ] = None


class AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails(BaseValidatorModel):
    MarketType: Optional[str] = None
    SpotOptions: Optional[AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails(BaseValidatorModel):
    pass


class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutput(BaseValidatorModel):
    AcceleratorCount: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails ] = None
    AcceleratorManufacturers: Optional[List[str]] = None
    AcceleratorNames: Optional[List[str]] = None
    AcceleratorTotalMemoryMiB: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails ] = None
    AcceleratorTypes: Optional[List[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails ] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[List[str]] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[List[str]] = None
    MemoryGiBPerVCpu: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails ] = None
    MemoryMiB: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails] = None
    NetworkInterfaceCount: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails ] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails ] = None
    VCpuCount: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails] = None


class AwsEc2LaunchTemplateDataInstanceRequirementsDetails(BaseValidatorModel):
    AcceleratorCount: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetails ] = None
    AcceleratorManufacturers: Optional[Sequence[str]] = None
    AcceleratorNames: Optional[Sequence[str]] = None
    AcceleratorTotalMemoryMiB: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetails ] = None
    AcceleratorTypes: Optional[Sequence[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetails ] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[Sequence[str]] = None
    ExcludedInstanceTypes: Optional[Sequence[str]] = None
    InstanceGenerations: Optional[Sequence[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[Sequence[str]] = None
    MemoryGiBPerVCpu: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetails ] = None
    MemoryMiB: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetails] = None
    NetworkInterfaceCount: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetails ] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetails ] = None
    VCpuCount: Optional[AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetails] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutput(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[ List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails] ] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[ List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails] ] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[ List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails] ] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[ List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails] ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetails(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[Sequence[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[ Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails] ] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[ Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetails] ] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[ Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetails] ] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[ Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetails] ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None


class AwsEc2NetworkInterfaceDetailsOutput(BaseValidatorModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachment] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[List[AwsEc2NetworkInterfaceSecurityGroup]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[List[AwsEc2NetworkInterfaceIpV6AddressDetail]] = None
    PrivateIpAddresses: Optional[List[AwsEc2NetworkInterfacePrivateIpAddressDetail]] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None


class AwsEc2NetworkInterfaceDetails(BaseValidatorModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachment] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[Sequence[AwsEc2NetworkInterfaceSecurityGroup]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[Sequence[AwsEc2NetworkInterfaceIpV6AddressDetail]] = None
    PrivateIpAddresses: Optional[Sequence[AwsEc2NetworkInterfacePrivateIpAddressDetail]] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None


class AwsEc2SecurityGroupIpPermissionOutput(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[AwsEc2SecurityGroupUserIdGroupPair]] = None
    IpRanges: Optional[List[AwsEc2SecurityGroupIpRange]] = None
    Ipv6Ranges: Optional[List[AwsEc2SecurityGroupIpv6Range]] = None
    PrefixListIds: Optional[List[AwsEc2SecurityGroupPrefixListId]] = None


class AwsEc2SecurityGroupIpPermission(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[Sequence[AwsEc2SecurityGroupUserIdGroupPair]] = None
    IpRanges: Optional[Sequence[AwsEc2SecurityGroupIpRange]] = None
    Ipv6Ranges: Optional[Sequence[AwsEc2SecurityGroupIpv6Range]] = None
    PrefixListIds: Optional[Sequence[AwsEc2SecurityGroupPrefixListId]] = None


class AwsEc2SubnetDetailsOutput(BaseValidatorModel):
    AssignIpv6AddressOnCreation: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    AvailableIpAddressCount: Optional[int] = None
    CidrBlock: Optional[str] = None
    DefaultForAz: Optional[bool] = None
    MapPublicIpOnLaunch: Optional[bool] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    SubnetArn: Optional[str] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociation]] = None


class AwsEc2SubnetDetails(BaseValidatorModel):
    AssignIpv6AddressOnCreation: Optional[bool] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    AvailableIpAddressCount: Optional[int] = None
    CidrBlock: Optional[str] = None
    DefaultForAz: Optional[bool] = None
    MapPublicIpOnLaunch: Optional[bool] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    SubnetArn: Optional[str] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    Ipv6CidrBlockAssociationSet: Optional[Sequence[Ipv6CidrBlockAssociation]] = None


class AwsEc2VolumeDetailsOutput(BaseValidatorModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[List[AwsEc2VolumeAttachment]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None


class AwsEc2VolumeDetails(BaseValidatorModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[Sequence[AwsEc2VolumeAttachment]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None


class AwsEc2VpcDetailsOutput(BaseValidatorModel):
    CidrBlockAssociationSet: Optional[List[CidrBlockAssociation]] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociation]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None


class AwsEc2VpcDetails(BaseValidatorModel):
    CidrBlockAssociationSet: Optional[Sequence[CidrBlockAssociation]] = None
    Ipv6CidrBlockAssociationSet: Optional[Sequence[Ipv6CidrBlockAssociation]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None


class AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[List[VpcInfoCidrBlockSetDetails]] = None
    Ipv6CidrBlockSet: Optional[List[VpcInfoIpv6CidrBlockSetDetails]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetails] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None


class AwsEc2VpcPeeringConnectionVpcInfoDetails(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[Sequence[VpcInfoCidrBlockSetDetails]] = None
    Ipv6CidrBlockSet: Optional[Sequence[VpcInfoIpv6CidrBlockSetDetails]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetails] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None


class AwsEc2VpnConnectionOptionsDetailsOutput(BaseValidatorModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutput]] = None


class AwsEcrRepositoryDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    ImageScanningConfiguration: Optional[ AwsEcrRepositoryImageScanningConfigurationDetails ] = None
    ImageTagMutability: Optional[str] = None
    LifecyclePolicy: Optional[AwsEcrRepositoryLifecyclePolicyDetails] = None
    RepositoryName: Optional[str] = None
    RepositoryPolicyText: Optional[str] = None


class AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails(BaseValidatorModel):
    pass


class AwsEcsClusterConfigurationExecuteCommandConfigurationDetails(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    LogConfiguration: Optional[ AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails ] = None
    Logging: Optional[str] = None


class AwsEcsContainerDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[List[AwsMountPoint]] = None
    Privileged: Optional[bool] = None


class AwsEcsContainerDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[Sequence[AwsMountPoint]] = None
    Privileged: Optional[bool] = None


class AwsEcsServiceDeploymentConfigurationDetails(BaseValidatorModel):
    DeploymentCircuitBreaker: Optional[ AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails ] = None
    MaximumPercent: Optional[int] = None
    MinimumHealthyPercent: Optional[int] = None


class AwsEcsServiceNetworkConfigurationDetailsOutput(BaseValidatorModel):
    AwsVpcConfiguration: Optional[ AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutput ] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutput(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutput(BaseValidatorModel):
    Capabilities: Optional[ AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutput ] = None
    Devices: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutput] ] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutput] ] = None


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutput(BaseValidatorModel):
    LogDriver: Optional[str] = None
    Options: Optional[Dict[str, str]] = None
    SecretOptions: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails] ] = None


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails(BaseValidatorModel):
    LogDriver: Optional[str] = None
    Options: Optional[Mapping[str, str]] = None
    SecretOptions: Optional[ Sequence[ AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetails ] ] = None


class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails(BaseValidatorModel):
    AuthorizationConfig: Optional[ AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetails ] = None
    FilesystemId: Optional[str] = None
    RootDirectory: Optional[str] = None
    TransitEncryption: Optional[str] = None
    TransitEncryptionPort: Optional[int] = None


class AwsEcsTaskVolumeDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Host: Optional[AwsEcsTaskVolumeHostDetails] = None


class AwsEfsAccessPointRootDirectoryDetails(BaseValidatorModel):
    CreationInfo: Optional[AwsEfsAccessPointRootDirectoryCreationInfoDetails] = None
    Path: Optional[str] = None


class AwsEksClusterLoggingDetailsOutput(BaseValidatorModel):
    ClusterLogging: Optional[List[AwsEksClusterLoggingClusterLoggingDetailsOutput]] = None


class AwsElasticBeanstalkEnvironmentTier(BaseValidatorModel):
    pass


class AwsElasticBeanstalkEnvironmentDetailsOutput(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[List[AwsElasticBeanstalkEnvironmentEnvironmentLink]] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[List[AwsElasticBeanstalkEnvironmentOptionSetting]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTier] = None
    VersionLabel: Optional[str] = None


class AwsElasticBeanstalkEnvironmentDetails(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[Sequence[AwsElasticBeanstalkEnvironmentEnvironmentLink]] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[Sequence[AwsElasticBeanstalkEnvironmentOptionSetting]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTier] = None
    VersionLabel: Optional[str] = None


class AwsElasticsearchDomainElasticsearchClusterConfigDetails(BaseValidatorModel):
    DedicatedMasterCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    DedicatedMasterType: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[str] = None
    ZoneAwarenessConfig: Optional[ AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetails ] = None
    ZoneAwarenessEnabled: Optional[bool] = None


class AwsElasticsearchDomainLogPublishingOptions(BaseValidatorModel):
    IndexSlowLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfig] = None
    SearchSlowLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfig] = None
    AuditLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfig] = None


class AwsElbLoadBalancerPoliciesOutput(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[List[AwsElbAppCookieStickinessPolicy]] = None
    LbCookieStickinessPolicies: Optional[List[AwsElbLbCookieStickinessPolicy]] = None
    OtherPolicies: Optional[List[str]] = None


class AwsElbLoadBalancerPolicies(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[Sequence[AwsElbAppCookieStickinessPolicy]] = None
    LbCookieStickinessPolicies: Optional[Sequence[AwsElbLbCookieStickinessPolicy]] = None
    OtherPolicies: Optional[Sequence[str]] = None


class AwsElbLoadBalancerAttributesOutput(BaseValidatorModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLog] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDraining] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettings] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancing] = None
    AdditionalAttributes: Optional[List[AwsElbLoadBalancerAdditionalAttribute]] = None


class AwsElbLoadBalancerAttributes(BaseValidatorModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLog] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDraining] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettings] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancing] = None
    AdditionalAttributes: Optional[Sequence[AwsElbLoadBalancerAdditionalAttribute]] = None


class AwsElbLoadBalancerListener(BaseValidatorModel):
    pass


class AwsElbLoadBalancerListenerDescriptionOutput(BaseValidatorModel):
    Listener: Optional[AwsElbLoadBalancerListener] = None
    PolicyNames: Optional[List[str]] = None


class AwsElbLoadBalancerListenerDescription(BaseValidatorModel):
    Listener: Optional[AwsElbLoadBalancerListener] = None
    PolicyNames: Optional[Sequence[str]] = None


class AwsEventsEndpointRoutingConfigFailoverConfigDetails(BaseValidatorModel):
    Primary: Optional[AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails] = None
    Secondary: Optional[AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails] = None


class AwsGuardDutyDetectorDataSourcesKubernetesDetails(BaseValidatorModel):
    AuditLogs: Optional[AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetails] = None


class AwsIamAccessKeySessionContextSessionIssuer(BaseValidatorModel):
    pass


class AwsIamAccessKeySessionContext(BaseValidatorModel):
    Attributes: Optional[AwsIamAccessKeySessionContextAttributes] = None
    SessionIssuer: Optional[AwsIamAccessKeySessionContextSessionIssuer] = None


class AwsIamGroupDetailsOutput(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[List[AwsIamGroupPolicy]] = None
    Path: Optional[str] = None


class AwsIamGroupDetails(BaseValidatorModel):
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[Sequence[AwsIamGroupPolicy]] = None
    Path: Optional[str] = None


class AwsIamInstanceProfileOutput(BaseValidatorModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[List[AwsIamInstanceProfileRole]] = None


class AwsIamInstanceProfile(BaseValidatorModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[Sequence[AwsIamInstanceProfileRole]] = None


class AwsIamPolicyDetailsOutput(BaseValidatorModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[List[AwsIamPolicyVersion]] = None
    UpdateDate: Optional[str] = None


class AwsIamPolicyDetails(BaseValidatorModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[Sequence[AwsIamPolicyVersion]] = None
    UpdateDate: Optional[str] = None


class AwsIamUserDetailsOutput(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[List[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundary] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[List[AwsIamUserPolicy]] = None


class AwsIamUserDetails(BaseValidatorModel):
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[Sequence[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundary] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[Sequence[AwsIamUserPolicy]] = None


class AwsKinesisStreamDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    StreamEncryption: Optional[AwsKinesisStreamStreamEncryptionDetails] = None
    ShardCount: Optional[int] = None
    RetentionPeriodHours: Optional[int] = None


class AwsLambdaFunctionEnvironmentOutput(BaseValidatorModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentError] = None


class AwsLambdaFunctionEnvironment(BaseValidatorModel):
    Variables: Optional[Mapping[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentError] = None


class AwsMskClusterClusterInfoClientAuthenticationSaslDetails(BaseValidatorModel):
    Iam: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslIamDetails] = None
    Scram: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslScramDetails] = None


class AwsMskClusterClusterInfoEncryptionInfoDetails(BaseValidatorModel):
    EncryptionInTransit: Optional[ AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetails ] = None
    EncryptionAtRest: Optional[ AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails ] = None


class AwsNetworkFirewallFirewallDetailsOutput(BaseValidatorModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[List[AwsNetworkFirewallFirewallSubnetMappingsDetails]] = None
    VpcId: Optional[str] = None


class AwsNetworkFirewallFirewallDetails(BaseValidatorModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[Sequence[AwsNetworkFirewallFirewallSubnetMappingsDetails]] = None
    VpcId: Optional[str] = None


class AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[AwsOpenSearchServiceDomainMasterUserOptionsDetails] = None


class AwsOpenSearchServiceDomainClusterConfigDetails(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[ AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetails ] = None
    DedicatedMasterCount: Optional[int] = None
    InstanceType: Optional[str] = None
    WarmType: Optional[str] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    DedicatedMasterType: Optional[str] = None


class AwsOpenSearchServiceDomainLogPublishingOptionsDetails(BaseValidatorModel):
    IndexSlowLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOption] = None
    SearchSlowLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOption] = None
    AuditLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOption] = None


class AwsRdsDbClusterDetailsOutput(BaseValidatorModel):
    AllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    DatabaseName: Optional[str] = None
    Status: Optional[str] = None
    Endpoint: Optional[str] = None
    ReaderEndpoint: Optional[str] = None
    CustomEndpoints: Optional[List[str]] = None
    MultiAz: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReadReplicaIdentifiers: Optional[List[str]] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroup]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[List[AwsRdsDbClusterAssociatedRole]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembership]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[List[AwsRdsDbClusterOptionGroupMembership]] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[List[AwsRdsDbClusterMember]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None


class AwsRdsDbClusterDetails(BaseValidatorModel):
    AllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[Sequence[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    DatabaseName: Optional[str] = None
    Status: Optional[str] = None
    Endpoint: Optional[str] = None
    ReaderEndpoint: Optional[str] = None
    CustomEndpoints: Optional[Sequence[str]] = None
    MultiAz: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReadReplicaIdentifiers: Optional[Sequence[str]] = None
    VpcSecurityGroups: Optional[Sequence[AwsRdsDbInstanceVpcSecurityGroup]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[Sequence[AwsRdsDbClusterAssociatedRole]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[Sequence[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[Sequence[AwsRdsDbDomainMembership]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[ Sequence[AwsRdsDbClusterOptionGroupMembership] ] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[Sequence[AwsRdsDbClusterMember]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None


class AwsRdsDbClusterSnapshotDetailsOutput(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    SnapshotCreateTime: Optional[str] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    PercentProgress: Optional[int] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterSnapshotIdentifier: Optional[str] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    DbClusterSnapshotAttributes: Optional[ List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutput] ] = None


class AwsRdsDbSnapshotDetailsOutput(BaseValidatorModel):
    DbSnapshotIdentifier: Optional[str] = None
    DbInstanceIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[str] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    VpcId: Optional[str] = None
    InstanceCreateTime: Optional[str] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    PercentProgress: Optional[int] = None
    SourceRegion: Optional[str] = None
    SourceDbSnapshotIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    Timezone: Optional[str] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None
    DbiResourceId: Optional[str] = None


class AwsRdsDbSnapshotDetails(BaseValidatorModel):
    DbSnapshotIdentifier: Optional[str] = None
    DbInstanceIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[str] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    VpcId: Optional[str] = None
    InstanceCreateTime: Optional[str] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    PercentProgress: Optional[int] = None
    SourceRegion: Optional[str] = None
    SourceDbSnapshotIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    Timezone: Optional[str] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeature]] = None
    DbiResourceId: Optional[str] = None


class AwsRdsDbPendingModifiedValuesOutput(BaseValidatorModel):
    DbInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    Port: Optional[int] = None
    BackupRetentionPeriod: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    DbInstanceIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    CaCertificateIdentifier: Optional[str] = None
    DbSubnetGroupName: Optional[str] = None
    PendingCloudWatchLogsExports: Optional[AwsRdsPendingCloudWatchLogsExportsOutput] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None


class AwsRdsDbSecurityGroupDetailsOutput(BaseValidatorModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[List[AwsRdsDbSecurityGroupEc2SecurityGroup]] = None
    IpRanges: Optional[List[AwsRdsDbSecurityGroupIpRange]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None


class AwsRdsDbSecurityGroupDetails(BaseValidatorModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[Sequence[AwsRdsDbSecurityGroupEc2SecurityGroup]] = None
    IpRanges: Optional[Sequence[AwsRdsDbSecurityGroupIpRange]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None


class AwsRdsDbSubnetGroupSubnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AwsRdsDbSubnetGroupSubnetAvailabilityZone] = None
    SubnetStatus: Optional[str] = None


class AwsRedshiftClusterClusterParameterGroupOutput(BaseValidatorModel):
    ClusterParameterStatusList: Optional[List[AwsRedshiftClusterClusterParameterStatus]] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None


class AwsRedshiftClusterClusterParameterGroup(BaseValidatorModel):
    ClusterParameterStatusList: Optional[ Sequence[AwsRedshiftClusterClusterParameterStatus] ] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None


class AwsRoute53HostedZoneObjectDetails(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[AwsRoute53HostedZoneConfigDetails] = None


class AwsRoute53QueryLoggingConfigDetails(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[CloudWatchLogsLogGroupArnConfigDetails] = None


class AwsS3AccessPointDetails(BaseValidatorModel):
    AccessPointArn: Optional[str] = None
    Alias: Optional[str] = None
    Bucket: Optional[str] = None
    BucketAccountId: Optional[str] = None
    Name: Optional[str] = None
    NetworkOrigin: Optional[str] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetails] = None
    VpcConfiguration: Optional[AwsS3AccessPointVpcConfigurationDetails] = None


class AwsS3BucketNotificationConfigurationS3KeyFilterOutput(BaseValidatorModel):
    FilterRules: Optional[List[AwsS3BucketNotificationConfigurationS3KeyFilterRule]] = None


class AwsS3BucketNotificationConfigurationS3KeyFilter(BaseValidatorModel):
    FilterRules: Optional[Sequence[AwsS3BucketNotificationConfigurationS3KeyFilterRule]] = None


class AwsS3BucketObjectLockConfigurationRuleDetails(BaseValidatorModel):
    DefaultRetention: Optional[ AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetails ] = None


class AwsS3BucketServerSideEncryptionRule(BaseValidatorModel):
    ApplyServerSideEncryptionByDefault: Optional[AwsS3BucketServerSideEncryptionByDefault] = None


class AwsS3BucketWebsiteConfigurationRoutingRuleRedirect(BaseValidatorModel):
    pass


class AwsS3BucketWebsiteConfigurationRoutingRule(BaseValidatorModel):
    Condition: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleCondition] = None
    Redirect: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleRedirect] = None


class AwsSageMakerNotebookInstanceDetailsOutput(BaseValidatorModel):
    AcceleratorTypes: Optional[List[str]] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[ AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails ] = None
    InstanceType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NotebookInstanceArn: Optional[str] = None
    NotebookInstanceLifecycleConfigName: Optional[str] = None
    NotebookInstanceName: Optional[str] = None
    NotebookInstanceStatus: Optional[str] = None
    PlatformIdentifier: Optional[str] = None
    RoleArn: Optional[str] = None
    RootAccess: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SubnetId: Optional[str] = None
    Url: Optional[str] = None
    VolumeSizeInGB: Optional[int] = None


class AwsSageMakerNotebookInstanceDetails(BaseValidatorModel):
    AcceleratorTypes: Optional[Sequence[str]] = None
    AdditionalCodeRepositories: Optional[Sequence[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[ AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetails ] = None
    InstanceType: Optional[str] = None
    KmsKeyId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NotebookInstanceArn: Optional[str] = None
    NotebookInstanceLifecycleConfigName: Optional[str] = None
    NotebookInstanceName: Optional[str] = None
    NotebookInstanceStatus: Optional[str] = None
    PlatformIdentifier: Optional[str] = None
    RoleArn: Optional[str] = None
    RootAccess: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SubnetId: Optional[str] = None
    Url: Optional[str] = None
    VolumeSizeInGB: Optional[int] = None


class AwsSecretsManagerSecretDetails(BaseValidatorModel):
    RotationRules: Optional[AwsSecretsManagerSecretRotationRules] = None
    RotationOccurredWithinFrequency: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    RotationEnabled: Optional[bool] = None
    RotationLambdaArn: Optional[str] = None
    Deleted: Optional[bool] = None
    Name: Optional[str] = None
    Description: Optional[str] = None


class BatchUpdateFindingsRequest(BaseValidatorModel):
    FindingIdentifiers: Sequence[AwsSecurityFindingIdentifier]
    Note: Optional[NoteUpdate] = None
    Severity: Optional[SeverityUpdate] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[Sequence[str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Workflow: Optional[WorkflowUpdate] = None
    RelatedFindings: Optional[Sequence[RelatedFinding]] = None


class BatchUpdateFindingsUnprocessedFinding(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifier
    ErrorCode: str
    ErrorMessage: str


class AwsSnsTopicSubscription(BaseValidatorModel):
    pass


class AwsSnsTopicDetailsOutput(BaseValidatorModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[List[AwsSnsTopicSubscription]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None


class AwsSnsTopicDetails(BaseValidatorModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[Sequence[AwsSnsTopicSubscription]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None


class AwsSsmPatch(BaseValidatorModel):
    ComplianceSummary: Optional[AwsSsmComplianceSummary] = None


class AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails(BaseValidatorModel):
    pass


class AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails(BaseValidatorModel):
    CloudWatchLogsLogGroup: Optional[ AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails ] = None


class AwsWafRateBasedRuleMatchPredicate(BaseValidatorModel):
    pass


class AwsWafRateBasedRuleDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRateBasedRuleMatchPredicate]] = None


class AwsWafRateBasedRuleDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[Sequence[AwsWafRateBasedRuleMatchPredicate]] = None


class AwsWafRegionalRateBasedRuleMatchPredicate(BaseValidatorModel):
    pass


class AwsWafRegionalRateBasedRuleDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRegionalRateBasedRuleMatchPredicate]] = None


class AwsWafRegionalRateBasedRuleDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[Sequence[AwsWafRegionalRateBasedRuleMatchPredicate]] = None


class AwsWafRegionalRulePredicateListDetails(BaseValidatorModel):
    pass


class AwsWafRegionalRuleDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRegionalRulePredicateListDetails]] = None
    RuleId: Optional[str] = None


class AwsWafRegionalRuleDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[Sequence[AwsWafRegionalRulePredicateListDetails]] = None
    RuleId: Optional[str] = None


class AwsWafRulePredicateListDetails(BaseValidatorModel):
    pass


class AwsWafRuleDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRulePredicateListDetails]] = None
    RuleId: Optional[str] = None


class AwsWafRuleDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[Sequence[AwsWafRulePredicateListDetails]] = None
    RuleId: Optional[str] = None


class AwsWafv2CustomRequestHandlingDetailsOutput(BaseValidatorModel):
    InsertHeaders: Optional[List[AwsWafv2CustomHttpHeader]] = None


class AwsWafv2CustomRequestHandlingDetails(BaseValidatorModel):
    InsertHeaders: Optional[Sequence[AwsWafv2CustomHttpHeader]] = None


class AwsWafv2CustomResponseDetailsOutput(BaseValidatorModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[List[AwsWafv2CustomHttpHeader]] = None


class AwsWafv2CustomResponseDetails(BaseValidatorModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[Sequence[AwsWafv2CustomHttpHeader]] = None


class AwsWafv2WebAclCaptchaConfigDetails(BaseValidatorModel):
    ImmunityTimeProperty: Optional[AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails] = None


class CreateActionTargetResponse(BaseValidatorModel):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadata


class CreateAutomationRuleResponse(BaseValidatorModel):
    RuleArn: str
    ResponseMetadata: ResponseMetadata


class CreateFindingAggregatorResponse(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadata


class CreateInsightResponse(BaseValidatorModel):
    InsightArn: str
    ResponseMetadata: ResponseMetadata


class DeleteActionTargetResponse(BaseValidatorModel):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadata


class DeleteInsightResponse(BaseValidatorModel):
    InsightArn: str
    ResponseMetadata: ResponseMetadata


class DescribeActionTargetsResponse(BaseValidatorModel):
    ActionTargets: List[ActionTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeHubResponse(BaseValidatorModel):
    HubArn: str
    SubscribedAt: str
    AutoEnableControls: bool
    ControlFindingGenerator: ControlFindingGeneratorType
    ResponseMetadata: ResponseMetadata


class EnableImportFindingsForProductResponse(BaseValidatorModel):
    ProductSubscriptionArn: str
    ResponseMetadata: ResponseMetadata


class GetConfigurationPolicyAssociationResponse(BaseValidatorModel):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadata


class GetFindingAggregatorResponse(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadata


class GetInvitationsCountResponse(BaseValidatorModel):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadata


class ListAutomationRulesResponse(BaseValidatorModel):
    AutomationRulesMetadata: List[AutomationRulesMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEnabledProductsForImportResponse(BaseValidatorModel):
    ProductSubscriptions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListOrganizationAdminAccountsResponse(BaseValidatorModel):
    AdminAccounts: List[AdminAccount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartConfigurationPolicyAssociationResponse(BaseValidatorModel):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadata


class UpdateFindingAggregatorResponse(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadata


class BatchDeleteAutomationRulesResponse(BaseValidatorModel):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRule]
    ResponseMetadata: ResponseMetadata


class BatchUpdateAutomationRulesResponse(BaseValidatorModel):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRule]
    ResponseMetadata: ResponseMetadata


class BatchEnableStandardsRequest(BaseValidatorModel):
    StandardsSubscriptionRequests: Sequence[StandardsSubscriptionRequest]


class ListConfigurationPolicyAssociationsResponse(BaseValidatorModel):
    ConfigurationPolicyAssociationSummaries: List[ConfigurationPolicyAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchGetStandardsControlAssociationsRequest(BaseValidatorModel):
    StandardsControlAssociationIds: Sequence[StandardsControlAssociationId]


class UnprocessedStandardsControlAssociation(BaseValidatorModel):
    StandardsControlAssociationId: StandardsControlAssociationId
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None


class BatchImportFindingsResponse(BaseValidatorModel):
    FailedCount: int
    SuccessCount: int
    FailedFindings: List[ImportFindingsError]
    ResponseMetadata: ResponseMetadata


class BatchUpdateStandardsControlAssociationsRequest(BaseValidatorModel):
    StandardsControlAssociationUpdates: Sequence[StandardsControlAssociationUpdate]


class UnprocessedStandardsControlAssociationUpdate(BaseValidatorModel):
    StandardsControlAssociationUpdate: StandardsControlAssociationUpdate
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None


class VulnerabilityCodeVulnerabilitiesOutput(BaseValidatorModel):
    Cwes: Optional[List[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePath] = None
    SourceArn: Optional[str] = None


class VulnerabilityCodeVulnerabilities(BaseValidatorModel):
    Cwes: Optional[Sequence[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePath] = None
    SourceArn: Optional[str] = None


class ComplianceOutput(BaseValidatorModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[List[str]] = None
    StatusReasons: Optional[List[StatusReason]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[List[AssociatedStandard]] = None
    SecurityControlParameters: Optional[List[SecurityControlParameterOutput]] = None


class ConfigurationOptions(BaseValidatorModel):
    Integer: Optional[IntegerConfigurationOptions] = None
    IntegerList: Optional[IntegerListConfigurationOptions] = None
    Double: Optional[DoubleConfigurationOptions] = None
    String: Optional[StringConfigurationOptions] = None
    StringList: Optional[StringListConfigurationOptions] = None
    Boolean: Optional[BooleanConfigurationOptions] = None
    Enum: Optional[EnumConfigurationOptions] = None
    EnumList: Optional[EnumListConfigurationOptions] = None


class ConfigurationPolicyAssociation(BaseValidatorModel):
    Target: Optional[Target] = None


class GetConfigurationPolicyAssociationRequest(BaseValidatorModel):
    Target: Target


class StartConfigurationPolicyAssociationRequest(BaseValidatorModel):
    ConfigurationPolicyIdentifier: str
    Target: Target


class StartConfigurationPolicyDisassociationRequest(BaseValidatorModel):
    ConfigurationPolicyIdentifier: str
    Target: Optional[Target] = None


class ListConfigurationPoliciesResponse(BaseValidatorModel):
    ConfigurationPolicySummaries: List[ConfigurationPolicySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ContainerDetailsOutput(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMount]] = None
    Privileged: Optional[bool] = None


class ContainerDetails(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[Sequence[VolumeMount]] = None
    Privileged: Optional[bool] = None


class CreateMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class DeclineInvitationsResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class DeleteInvitationsResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class DeleteMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class InviteMembersResponse(BaseValidatorModel):
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class DateFilter(BaseValidatorModel):
    Start: Optional[str] = None
    End: Optional[str] = None
    DateRange: Optional[DateRange] = None


class DescribeActionTargetsRequestPaginate(BaseValidatorModel):
    ActionTargetArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeProductsRequestPaginate(BaseValidatorModel):
    ProductArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStandardsControlsRequestPaginate(BaseValidatorModel):
    StandardsSubscriptionArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStandardsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetEnabledStandardsRequestPaginate(BaseValidatorModel):
    StandardsSubscriptionArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetInsightsRequestPaginate(BaseValidatorModel):
    InsightArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationPoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfigurationPolicyAssociationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[AssociationFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEnabledProductsForImportRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFindingAggregatorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInvitationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMembersRequestPaginate(BaseValidatorModel):
    OnlyAssociated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOrganizationAdminAccountsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityControlDefinitionsRequestPaginate(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStandardsControlAssociationsRequestPaginate(BaseValidatorModel):
    SecurityControlId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrganizationConfigurationResponse(BaseValidatorModel):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    AutoEnableStandards: AutoEnableStandardsType
    OrganizationConfiguration: OrganizationConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateOrganizationConfigurationRequest(BaseValidatorModel):
    AutoEnable: bool
    AutoEnableStandards: Optional[AutoEnableStandardsType] = None
    OrganizationConfiguration: Optional[OrganizationConfiguration] = None


class DescribeProductsResponse(BaseValidatorModel):
    Products: List[Product]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeStandardsControlsResponse(BaseValidatorModel):
    Controls: List[StandardsControl]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ThreatOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[FilePaths]] = None


class Threat(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[Sequence[FilePaths]] = None


class ListFindingAggregatorsResponse(BaseValidatorModel):
    FindingAggregators: List[FindingAggregator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FindingHistoryUpdateSource(BaseValidatorModel):
    pass


class FindingHistoryRecord(BaseValidatorModel):
    FindingIdentifier: Optional[AwsSecurityFindingIdentifier] = None
    UpdateTime: Optional[datetime] = None
    FindingCreated: Optional[bool] = None
    UpdateSource: Optional[FindingHistoryUpdateSource] = None
    Updates: Optional[List[FindingHistoryUpdate]] = None
    NextToken: Optional[str] = None


class FindingProviderFieldsOutput(BaseValidatorModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None
    Severity: Optional[FindingProviderSeverity] = None
    Types: Optional[List[str]] = None


class FindingProviderFields(BaseValidatorModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[Sequence[RelatedFinding]] = None
    Severity: Optional[FindingProviderSeverity] = None
    Types: Optional[Sequence[str]] = None


class GetAdministratorAccountResponse(BaseValidatorModel):
    Administrator: Invitation
    ResponseMetadata: ResponseMetadata


class GetMasterAccountResponse(BaseValidatorModel):
    Master: Invitation
    ResponseMetadata: ResponseMetadata


class ListInvitationsResponse(BaseValidatorModel):
    Invitations: List[Invitation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class GetFindingHistoryRequestPaginate(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifier
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetFindingHistoryRequest(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifier
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetMembersResponse(BaseValidatorModel):
    Members: List[Member]
    UnprocessedAccounts: List[Result]
    ResponseMetadata: ResponseMetadata


class ListMembersResponse(BaseValidatorModel):
    Members: List[Member]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InsightResults(BaseValidatorModel):
    InsightArn: str
    GroupByAttribute: str
    ResultValues: List[InsightResultValue]


class ListStandardsControlAssociationsResponse(BaseValidatorModel):
    StandardsControlAssociationSummaries: List[StandardsControlAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NetworkEndpoint(BaseValidatorModel):
    Id: Optional[str] = None
    Ip: Optional[str] = None
    Domain: Optional[str] = None
    Port: Optional[int] = None
    Location: Optional[NetworkGeoLocation] = None
    AutonomousSystem: Optional[NetworkAutonomousSystem] = None
    Connection: Optional[NetworkConnection] = None


class NetworkPathComponentDetailsOutput(BaseValidatorModel):
    Address: Optional[List[str]] = None
    PortRanges: Optional[List[PortRange]] = None


class NetworkPathComponentDetails(BaseValidatorModel):
    Address: Optional[Sequence[str]] = None
    PortRanges: Optional[Sequence[PortRange]] = None


class Page(BaseValidatorModel):
    PageNumber: Optional[int] = None
    LineRange: Optional[Range] = None
    OffsetRange: Optional[Range] = None


class ParameterConfigurationOutput(BaseValidatorModel):
    ValueType: ParameterValueTypeType
    Value: Optional[ParameterValueOutput] = None


class Recommendation(BaseValidatorModel):
    pass


class Remediation(BaseValidatorModel):
    Recommendation: Optional[Recommendation] = None


class RuleGroupSourceStatefulRulesHeaderDetails(BaseValidatorModel):
    pass


class RuleGroupSourceStatefulRulesDetailsOutput(BaseValidatorModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetails] = None
    RuleOptions: Optional[List[RuleGroupSourceStatefulRulesOptionsDetailsOutput]] = None


class RuleGroupSourceStatelessRuleMatchAttributesOutput(BaseValidatorModel):
    DestinationPorts: Optional[ List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts] ] = None
    Destinations: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesDestinations]] = None
    Protocols: Optional[List[int]] = None
    SourcePorts: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSourcePorts]] = None
    Sources: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSources]] = None
    TcpFlags: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutput]] = None


class RuleGroupVariablesOutput(BaseValidatorModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsOutput] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsOutput] = None


class Standard(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    EnabledByDefault: Optional[bool] = None
    StandardsManagedBy: Optional[StandardsManagedBy] = None


class StandardsSubscription(BaseValidatorModel):
    StandardsSubscriptionArn: str
    StandardsArn: str
    StandardsInput: Dict[str, str]
    StandardsStatus: StandardsStatusType
    StandardsControlsUpdatable: Optional[StandardsControlsUpdatableType] = None
    StandardsStatusReason: Optional[StandardsStatusReason] = None


class StatelessCustomPublishMetricActionOutput(BaseValidatorModel):
    Dimensions: Optional[List[StatelessCustomPublishMetricActionDimension]] = None


class StatelessCustomPublishMetricAction(BaseValidatorModel):
    Dimensions: Optional[Sequence[StatelessCustomPublishMetricActionDimension]] = None


class PortProbeDetail(BaseValidatorModel):
    LocalPortDetails: Optional[ActionLocalPortDetails] = None
    LocalIpDetails: Optional[ActionLocalIpDetails] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetails] = None


class ActorUser(BaseValidatorModel):
    pass


class Actor(BaseValidatorModel):
    Id: Optional[str] = None
    User: Optional[ActorUser] = None
    Session: Optional[ActorSession] = None


class AwsEc2RouteTableDetailsOutput(BaseValidatorModel):
    AssociationSet: Optional[List[AssociationSetDetails]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[List[PropagatingVgwSetDetails]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[List[RouteSetDetails]] = None
    VpcId: Optional[str] = None


class AwsEc2RouteTableDetails(BaseValidatorModel):
    AssociationSet: Optional[Sequence[AssociationSetDetails]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[Sequence[PropagatingVgwSetDetails]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[Sequence[RouteSetDetails]] = None
    VpcId: Optional[str] = None


class AwsAmazonMqBrokerDetailsOutput(BaseValidatorModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetails] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[AwsAmazonMqBrokerLdapServerMetadataDetailsOutput] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetails] = None
    MaintenanceWindowStartTime: Optional[ AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails ] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[List[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    Users: Optional[List[AwsAmazonMqBrokerUsersDetails]] = None


class AwsAmazonMqBrokerLdapServerMetadataDetailsUnion(BaseValidatorModel):
    pass


class AwsAmazonMqBrokerDetails(BaseValidatorModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetails] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[AwsAmazonMqBrokerLdapServerMetadataDetailsUnion] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetails] = None
    MaintenanceWindowStartTime: Optional[ AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails ] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[Sequence[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    Users: Optional[Sequence[AwsAmazonMqBrokerUsersDetails]] = None


class AwsApiGatewayCanarySettingsUnion(BaseValidatorModel):
    pass


class AwsApiGatewayStageDetails(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[Sequence[AwsApiGatewayMethodSettings]] = None
    Variables: Optional[Mapping[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettings] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsUnion] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None


class AwsApiGatewayEndpointConfigurationUnion(BaseValidatorModel):
    pass


class AwsApiGatewayRestApiDetails(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[Sequence[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationUnion] = None


class AwsAppSyncGraphQlApiDetailsOutput(BaseValidatorModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetails] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetails] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetails] = None
    AdditionalAuthenticationProviders: Optional[ List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails] ] = None
    WafWebAclArn: Optional[str] = None


class AwsAppSyncGraphQlApiDetails(BaseValidatorModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetails] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetails] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetails] = None
    AdditionalAuthenticationProviders: Optional[ Sequence[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetails] ] = None
    WafWebAclArn: Optional[str] = None


class AwsAthenaWorkGroupConfigurationDetails(BaseValidatorModel):
    ResultConfiguration: Optional[ AwsAthenaWorkGroupConfigurationResultConfigurationDetails ] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails(BaseValidatorModel):
    pass


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutput(BaseValidatorModel):
    pass


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutput(BaseValidatorModel):
    InstancesDistribution: Optional[ AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails ] = None
    LaunchTemplate: Optional[ AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutput ] = None


class AwsAutoScalingLaunchConfigurationDetailsOutput(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[ List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails] ] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[ AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptions] = None


class AwsAutoScalingLaunchConfigurationDetails(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[ Sequence[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetails] ] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[Sequence[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[ AwsAutoScalingLaunchConfigurationInstanceMonitoringDetails ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptions] = None


class AwsBackupBackupPlanRuleDetailsOutput(BaseValidatorModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[List[AwsBackupBackupPlanRuleCopyActionsDetails]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetails] = None


class AwsBackupBackupPlanRuleDetails(BaseValidatorModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[Sequence[AwsBackupBackupPlanRuleCopyActionsDetails]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetails] = None


class AwsBackupBackupVaultNotificationsDetailsUnion(BaseValidatorModel):
    pass


class AwsBackupBackupVaultDetails(BaseValidatorModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsUnion] = None
    AccessPolicy: Optional[str] = None


class AwsCertificateManagerCertificateRenewalSummaryOutput(BaseValidatorModel):
    DomainValidationOptions: Optional[ List[AwsCertificateManagerCertificateDomainValidationOptionOutput] ] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None


class AwsCertificateManagerCertificateRenewalSummary(BaseValidatorModel):
    DomainValidationOptions: Optional[ Sequence[AwsCertificateManagerCertificateDomainValidationOption] ] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None


class AwsCloudFrontDistributionOriginItemOutput(BaseValidatorModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfig] = None
    CustomOriginConfig: Optional[AwsCloudFrontDistributionOriginCustomOriginConfigOutput] = None


class AwsCloudFrontDistributionOriginGroupOutput(BaseValidatorModel):
    FailoverCriteria: Optional[AwsCloudFrontDistributionOriginGroupFailoverOutput] = None


class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionOriginGroupFailover(BaseValidatorModel):
    StatusCodes: Optional[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesUnion] = None


class AwsCloudFrontDistributionOriginSslProtocolsUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionOriginCustomOriginConfig(BaseValidatorModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[AwsCloudFrontDistributionOriginSslProtocolsUnion] = None


class AwsCodeBuildProjectEnvironmentOutput(BaseValidatorModel):
    pass


class AwsCodeBuildProjectSource(BaseValidatorModel):
    pass


class AwsCodeBuildProjectArtifactsDetails(BaseValidatorModel):
    pass


class AwsCodeBuildProjectDetailsOutput(BaseValidatorModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[List[AwsCodeBuildProjectArtifactsDetails]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentOutput] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSource] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetails] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigOutput] = None
    SecondaryArtifacts: Optional[List[AwsCodeBuildProjectArtifactsDetails]] = None


class AwsCorsConfigurationUnion(BaseValidatorModel):
    pass


class AwsApiGatewayV2ApiDetails(BaseValidatorModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationUnion] = None


class AwsDynamoDbTableProjectionUnion(BaseValidatorModel):
    pass


class AwsDynamoDbTableGlobalSecondaryIndex(BaseValidatorModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchema]] = None
    Projection: Optional[AwsDynamoDbTableProjectionUnion] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughput] = None


class AwsDynamoDbTableLocalSecondaryIndex(BaseValidatorModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchema]] = None
    Projection: Optional[AwsDynamoDbTableProjectionUnion] = None


class AwsEc2ClientVpnEndpointAuthenticationOptionsDetails(BaseValidatorModel):
    pass


class AwsEc2ClientVpnEndpointDetailsOutput(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[ List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetails] ] = None
    ConnectionLogOptions: Optional[AwsEc2ClientVpnEndpointConnectionLogOptionsDetails] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[AwsEc2ClientVpnEndpointClientConnectOptionsDetails] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[ AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails ] = None


class AwsEc2ClientVpnEndpointDetails(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[Sequence[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[ Sequence[AwsEc2ClientVpnEndpointAuthenticationOptionsDetails] ] = None
    ConnectionLogOptions: Optional[AwsEc2ClientVpnEndpointConnectionLogOptionsDetails] = None
    SecurityGroupIdSet: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[AwsEc2ClientVpnEndpointClientConnectOptionsDetails] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[ AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetails ] = None


class AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails(BaseValidatorModel):
    pass


class AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails(BaseValidatorModel):
    pass


class AwsEc2LaunchTemplateDataDetailsOutput(BaseValidatorModel):
    BlockDeviceMappingSet: Optional[ List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails] ] = None
    CapacityReservationSpecification: Optional[ AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails ] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetails] = None
    CreditSpecification: Optional[AwsEc2LaunchTemplateDataCreditSpecificationDetails] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[ List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails] ] = None
    ElasticInferenceAcceleratorSet: Optional[ List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails] ] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetails] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetails] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetails] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails] = None
    InstanceRequirements: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutput ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[List[AwsEc2LaunchTemplateDataLicenseSetDetails]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetails] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetails] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetails] = None
    NetworkInterfaceSet: Optional[ List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutput] ] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetails] = None
    PrivateDnsNameOptions: Optional[AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    SecurityGroupSet: Optional[List[str]] = None
    UserData: Optional[str] = None


class AwsEc2NetworkAclEntry(BaseValidatorModel):
    pass


class AwsEc2NetworkAclDetailsOutput(BaseValidatorModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[List[AwsEc2NetworkAclAssociation]] = None
    Entries: Optional[List[AwsEc2NetworkAclEntry]] = None


class AwsEc2NetworkAclDetails(BaseValidatorModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[Sequence[AwsEc2NetworkAclAssociation]] = None
    Entries: Optional[Sequence[AwsEc2NetworkAclEntry]] = None


class AwsEc2SecurityGroupDetailsOutput(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[List[AwsEc2SecurityGroupIpPermissionOutput]] = None
    IpPermissionsEgress: Optional[List[AwsEc2SecurityGroupIpPermissionOutput]] = None


class AwsEc2VpcPeeringConnectionDetailsOutput(BaseValidatorModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutput] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetails] = None
    VpcPeeringConnectionId: Optional[str] = None


class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnion(BaseValidatorModel):
    pass


class AwsEc2VpnConnectionOptionsDetails(BaseValidatorModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[Sequence[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsUnion]] = None


class AwsEcsClusterConfigurationDetails(BaseValidatorModel):
    ExecuteCommandConfiguration: Optional[ AwsEcsClusterConfigurationExecuteCommandConfigurationDetails ] = None


class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsServiceNetworkConfigurationDetails(BaseValidatorModel):
    AwsVpcConfiguration: Optional[ AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsUnion ] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetails(BaseValidatorModel):
    Capabilities: Optional[ AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsUnion ] = None
    Devices: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsUnion] ] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsUnion] ] = None


class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutput(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsDetailsOutput(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails]] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[List[str]] = None
    DnsServers: Optional[List[str]] = None
    DockerLabels: Optional[Dict[str, str]] = None
    DockerSecurityOptions: Optional[List[str]] = None
    EntryPoint: Optional[List[str]] = None
    Environment: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails] ] = None
    EnvironmentFiles: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails] ] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails]] = None
    FirelensConfiguration: Optional[ AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutput ] = None
    HealthCheck: Optional[ AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutput ] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[List[str]] = None
    LinuxParameters: Optional[ AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutput ] = None
    LogConfiguration: Optional[ AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutput ] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails] ] = None
    Name: Optional[str] = None
    PortMappings: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails] ] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[ AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails ] = None
    ResourceRequirements: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails] ] = None
    Secrets: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails]] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails] ] = None
    Ulimits: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails]] = None
    User: Optional[str] = None
    VolumesFrom: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails] ] = None
    WorkingDirectory: Optional[str] = None


class AwsEcsTaskDefinitionVolumesDetailsOutput(BaseValidatorModel):
    DockerVolumeConfiguration: Optional[ AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutput ] = None
    EfsVolumeConfiguration: Optional[ AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails ] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetails] = None
    Name: Optional[str] = None


class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionVolumesDetails(BaseValidatorModel):
    DockerVolumeConfiguration: Optional[ AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsUnion ] = None
    EfsVolumeConfiguration: Optional[ AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetails ] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetails] = None
    Name: Optional[str] = None


class AwsEcsTaskDetailsOutput(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskVolumeDetails]] = None
    Containers: Optional[List[AwsEcsContainerDetailsOutput]] = None


class AwsEfsAccessPointDetailsOutput(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsOutput] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetails] = None


class AwsEfsAccessPointPosixUserDetailsUnion(BaseValidatorModel):
    pass


class AwsEfsAccessPointDetails(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsUnion] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetails] = None


class AwsEksClusterDetailsOutput(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsOutput] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsOutput] = None


class AwsEksClusterLoggingClusterLoggingDetailsUnion(BaseValidatorModel):
    pass


class AwsEksClusterLoggingDetails(BaseValidatorModel):
    ClusterLogging: Optional[Sequence[AwsEksClusterLoggingClusterLoggingDetailsUnion]] = None


class AwsElasticsearchDomainDetailsOutput(BaseValidatorModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptions] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[ AwsElasticsearchDomainElasticsearchClusterConfigDetails ] = None
    EncryptionAtRestOptions: Optional[AwsElasticsearchDomainEncryptionAtRestOptions] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptions] = None
    NodeToNodeEncryptionOptions: Optional[ AwsElasticsearchDomainNodeToNodeEncryptionOptions ] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptions] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsOutput] = None


class AwsElasticsearchDomainVPCOptionsUnion(BaseValidatorModel):
    pass


class AwsElasticsearchDomainDetails(BaseValidatorModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptions] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Mapping[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[ AwsElasticsearchDomainElasticsearchClusterConfigDetails ] = None
    EncryptionAtRestOptions: Optional[AwsElasticsearchDomainEncryptionAtRestOptions] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptions] = None
    NodeToNodeEncryptionOptions: Optional[ AwsElasticsearchDomainNodeToNodeEncryptionOptions ] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptions] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsUnion] = None


class AwsElbLoadBalancerDetailsOutput(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    BackendServerDescriptions: Optional[ List[AwsElbLoadBalancerBackendServerDescriptionOutput] ] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheck] = None
    Instances: Optional[List[AwsElbLoadBalancerInstance]] = None
    ListenerDescriptions: Optional[List[AwsElbLoadBalancerListenerDescriptionOutput]] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesOutput] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesOutput] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroup] = None
    Subnets: Optional[List[str]] = None
    VpcId: Optional[str] = None


class AwsEventsEndpointRoutingConfigDetails(BaseValidatorModel):
    FailoverConfig: Optional[AwsEventsEndpointRoutingConfigFailoverConfigDetails] = None


class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetails(BaseValidatorModel):
    pass


class AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[ AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetails ] = None
    ServiceRole: Optional[str] = None


class AwsIamAccessKeyDetails(BaseValidatorModel):
    UserName: Optional[str] = None
    Status: Optional[AwsIamAccessKeyStatusType] = None
    CreatedAt: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[str] = None
    PrincipalName: Optional[str] = None
    AccountId: Optional[str] = None
    AccessKeyId: Optional[str] = None
    SessionContext: Optional[AwsIamAccessKeySessionContext] = None


class AwsIamRoleDetailsOutput(BaseValidatorModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[List[AwsIamInstanceProfileOutput]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundary] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[List[AwsIamRolePolicy]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None


class AwsLambdaFunctionDetailsOutput(BaseValidatorModel):
    Code: Optional[AwsLambdaFunctionCode] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfig] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentOutput] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[List[AwsLambdaFunctionLayer]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfig] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigOutput] = None
    Version: Optional[str] = None
    Architectures: Optional[List[str]] = None
    PackageType: Optional[str] = None


class AwsMskClusterClusterInfoClientAuthenticationDetailsOutput(BaseValidatorModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetails] = None
    Unauthenticated: Optional[ AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails ] = None
    Tls: Optional[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutput] = None


class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnion(BaseValidatorModel):
    pass


class AwsMskClusterClusterInfoClientAuthenticationDetails(BaseValidatorModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetails] = None
    Unauthenticated: Optional[ AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetails ] = None
    Tls: Optional[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsUnion] = None


class AwsOpenSearchServiceDomainDetailsOutput(BaseValidatorModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[ AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails ] = None
    NodeToNodeEncryptionOptions: Optional[ AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails ] = None
    ServiceSoftwareOptions: Optional[ AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails ] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetails] = None
    DomainEndpointOptions: Optional[ AwsOpenSearchServiceDomainDomainEndpointOptionsDetails ] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsOutput] = None
    LogPublishingOptions: Optional[AwsOpenSearchServiceDomainLogPublishingOptionsDetails] = None
    DomainEndpoints: Optional[Dict[str, str]] = None
    AdvancedSecurityOptions: Optional[ AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails ] = None


class AwsOpenSearchServiceDomainVpcOptionsDetailsUnion(BaseValidatorModel):
    pass


class AwsOpenSearchServiceDomainDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[ AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetails ] = None
    NodeToNodeEncryptionOptions: Optional[ AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetails ] = None
    ServiceSoftwareOptions: Optional[ AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails ] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetails] = None
    DomainEndpointOptions: Optional[ AwsOpenSearchServiceDomainDomainEndpointOptionsDetails ] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsUnion] = None
    LogPublishingOptions: Optional[AwsOpenSearchServiceDomainLogPublishingOptionsDetails] = None
    DomainEndpoints: Optional[Mapping[str, str]] = None
    AdvancedSecurityOptions: Optional[ AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails ] = None


class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnion(BaseValidatorModel):
    pass


class AwsRdsDbClusterSnapshotDetails(BaseValidatorModel):
    AvailabilityZones: Optional[Sequence[str]] = None
    SnapshotCreateTime: Optional[str] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    PercentProgress: Optional[int] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterSnapshotIdentifier: Optional[str] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    DbClusterSnapshotAttributes: Optional[ Sequence[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeUnion] ] = None


class AwsRdsDbSubnetGroupOutput(BaseValidatorModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[AwsRdsDbSubnetGroupSubnet]] = None
    DbSubnetGroupArn: Optional[str] = None


class AwsRdsDbSubnetGroup(BaseValidatorModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[Sequence[AwsRdsDbSubnetGroupSubnet]] = None
    DbSubnetGroupArn: Optional[str] = None


class AwsRdsPendingCloudWatchLogsExportsUnion(BaseValidatorModel):
    pass


class AwsRdsDbPendingModifiedValues(BaseValidatorModel):
    DbInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    Port: Optional[int] = None
    BackupRetentionPeriod: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    DbInstanceIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    CaCertificateIdentifier: Optional[str] = None
    DbSubnetGroupName: Optional[str] = None
    PendingCloudWatchLogsExports: Optional[AwsRdsPendingCloudWatchLogsExportsUnion] = None
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeature]] = None


class AwsRedshiftClusterDetailsOutput(BaseValidatorModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[List[AwsRedshiftClusterClusterNode]] = None
    ClusterParameterGroups: Optional[List[AwsRedshiftClusterClusterParameterGroupOutput]] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[List[AwsRedshiftClusterClusterSecurityGroup]] = None
    ClusterSnapshotCopyStatus: Optional[AwsRedshiftClusterClusterSnapshotCopyStatus] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[ List[AwsRedshiftClusterDeferredMaintenanceWindow] ] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatus] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpoint] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatus] = None
    IamRoles: Optional[List[AwsRedshiftClusterIamRole]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[List[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValues] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfo] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatus] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRedshiftClusterVpcSecurityGroup]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatus] = None


class AwsRoute53HostedZoneDetailsOutput(BaseValidatorModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetails] = None
    Vpcs: Optional[List[AwsRoute53HostedZoneVpcDetails]] = None
    NameServers: Optional[List[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetails] = None


class AwsRoute53HostedZoneDetails(BaseValidatorModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetails] = None
    Vpcs: Optional[Sequence[AwsRoute53HostedZoneVpcDetails]] = None
    NameServers: Optional[Sequence[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetails] = None


class AwsS3BucketNotificationConfigurationFilterOutput(BaseValidatorModel):
    S3KeyFilter: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterOutput] = None


class AwsS3BucketObjectLockConfiguration(BaseValidatorModel):
    ObjectLockEnabled: Optional[str] = None
    Rule: Optional[AwsS3BucketObjectLockConfigurationRuleDetails] = None


class AwsS3BucketServerSideEncryptionConfigurationOutput(BaseValidatorModel):
    Rules: Optional[List[AwsS3BucketServerSideEncryptionRule]] = None


class AwsS3BucketServerSideEncryptionConfiguration(BaseValidatorModel):
    Rules: Optional[Sequence[AwsS3BucketServerSideEncryptionRule]] = None


class AwsS3BucketWebsiteConfigurationRedirectTo(BaseValidatorModel):
    pass


class AwsS3BucketWebsiteConfigurationOutput(BaseValidatorModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectTo] = None
    RoutingRules: Optional[List[AwsS3BucketWebsiteConfigurationRoutingRule]] = None


class AwsS3BucketWebsiteConfiguration(BaseValidatorModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectTo] = None
    RoutingRules: Optional[Sequence[AwsS3BucketWebsiteConfigurationRoutingRule]] = None


class BatchUpdateFindingsResponse(BaseValidatorModel):
    ProcessedFindings: List[AwsSecurityFindingIdentifier]
    UnprocessedFindings: List[BatchUpdateFindingsUnprocessedFinding]
    ResponseMetadata: ResponseMetadata


class AwsSsmPatchComplianceDetails(BaseValidatorModel):
    Patch: Optional[AwsSsmPatch] = None


class AwsStepFunctionStateMachineLoggingConfigurationDetailsOutput(BaseValidatorModel):
    Destinations: Optional[ List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails] ] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None


class AwsStepFunctionStateMachineLoggingConfigurationDetails(BaseValidatorModel):
    Destinations: Optional[ Sequence[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails] ] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None


class AwsWafRegionalRuleGroupRulesDetails(BaseValidatorModel):
    pass


class AwsWafRegionalRuleGroupDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRegionalRuleGroupRulesDetails]] = None


class AwsWafRegionalRuleGroupDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[Sequence[AwsWafRegionalRuleGroupRulesDetails]] = None


class AwsWafRegionalWebAclRulesListDetails(BaseValidatorModel):
    pass


class AwsWafRegionalWebAclDetailsOutput(BaseValidatorModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[List[AwsWafRegionalWebAclRulesListDetails]] = None
    WebAclId: Optional[str] = None


class AwsWafRegionalWebAclDetails(BaseValidatorModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[Sequence[AwsWafRegionalWebAclRulesListDetails]] = None
    WebAclId: Optional[str] = None


class AwsWafRuleGroupRulesDetails(BaseValidatorModel):
    pass


class AwsWafRuleGroupDetailsOutput(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRuleGroupRulesDetails]] = None


class AwsWafRuleGroupDetails(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[Sequence[AwsWafRuleGroupRulesDetails]] = None


class AwsWafWebAclRuleOutput(BaseValidatorModel):
    pass


class AwsWafWebAclDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[List[AwsWafWebAclRuleOutput]] = None
    WebAclId: Optional[str] = None


class AwsWafv2ActionAllowDetailsOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutput] = None


class AwsWafv2RulesActionCaptchaDetailsOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutput] = None


class AwsWafv2RulesActionCountDetailsOutput(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutput] = None


class AwsWafv2ActionBlockDetailsOutput(BaseValidatorModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsOutput] = None


class BatchGetStandardsControlAssociationsResponse(BaseValidatorModel):
    StandardsControlAssociationDetails: List[StandardsControlAssociationDetail]
    UnprocessedAssociations: List[UnprocessedStandardsControlAssociation]
    ResponseMetadata: ResponseMetadata


class BatchUpdateStandardsControlAssociationsResponse(BaseValidatorModel):
    UnprocessedAssociationUpdates: List[UnprocessedStandardsControlAssociationUpdate]
    ResponseMetadata: ResponseMetadata


class VulnerabilityOutput(BaseValidatorModel):
    Id: str
    VulnerablePackages: Optional[List[SoftwarePackage]] = None
    Cvss: Optional[List[CvssOutput]] = None
    RelatedVulnerabilities: Optional[List[str]] = None
    Vendor: Optional[VulnerabilityVendor] = None
    ReferenceUrls: Optional[List[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[List[VulnerabilityCodeVulnerabilitiesOutput]] = None


class ParameterDefinition(BaseValidatorModel):
    Description: str
    ConfigurationOptions: ConfigurationOptions


class BatchGetConfigurationPolicyAssociationsRequest(BaseValidatorModel):
    ConfigurationPolicyAssociationIdentifiers: Sequence[ConfigurationPolicyAssociation]


class UnprocessedConfigurationPolicyAssociation(BaseValidatorModel):
    ConfigurationPolicyAssociationIdentifiers: Optional[ConfigurationPolicyAssociation] = None
    ErrorCode: Optional[str] = None
    ErrorReason: Optional[str] = None


class GetFindingHistoryResponse(BaseValidatorModel):
    Records: List[FindingHistoryRecord]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetInsightResultsResponse(BaseValidatorModel):
    InsightResults: InsightResults
    ResponseMetadata: ResponseMetadata


class OccurrencesOutput(BaseValidatorModel):
    LineRanges: Optional[List[Range]] = None
    OffsetRanges: Optional[List[Range]] = None
    Pages: Optional[List[Page]] = None
    Records: Optional[List[Record]] = None
    Cells: Optional[List[Cell]] = None


class Occurrences(BaseValidatorModel):
    LineRanges: Optional[Sequence[Range]] = None
    OffsetRanges: Optional[Sequence[Range]] = None
    Pages: Optional[Sequence[Page]] = None
    Records: Optional[Sequence[Record]] = None
    Cells: Optional[Sequence[Cell]] = None


class SecurityControlCustomParameterOutput(BaseValidatorModel):
    SecurityControlId: Optional[str] = None
    Parameters: Optional[Dict[str, ParameterConfigurationOutput]] = None


class SecurityControl(BaseValidatorModel):
    SecurityControlId: str
    SecurityControlArn: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    SecurityControlStatus: ControlStatusType
    UpdateStatus: Optional[UpdateStatusType] = None
    Parameters: Optional[Dict[str, ParameterConfigurationOutput]] = None
    LastUpdateReason: Optional[str] = None


class ParameterValueUnion(BaseValidatorModel):
    pass


class ParameterConfiguration(BaseValidatorModel):
    ValueType: ParameterValueTypeType
    Value: Optional[ParameterValueUnion] = None


class RuleGroupSourceStatefulRulesOptionsDetailsUnion(BaseValidatorModel):
    pass


class RuleGroupSourceStatefulRulesDetails(BaseValidatorModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetails] = None
    RuleOptions: Optional[Sequence[RuleGroupSourceStatefulRulesOptionsDetailsUnion]] = None


class RuleGroupSourceStatelessRuleDefinitionOutput(BaseValidatorModel):
    Actions: Optional[List[str]] = None
    MatchAttributes: Optional[RuleGroupSourceStatelessRuleMatchAttributesOutput] = None


class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnion(BaseValidatorModel):
    pass


class RuleGroupSourceStatelessRuleMatchAttributes(BaseValidatorModel):
    DestinationPorts: Optional[ Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationPorts] ] = None
    Destinations: Optional[ Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinations] ] = None
    Protocols: Optional[Sequence[int]] = None
    SourcePorts: Optional[ Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcePorts] ] = None
    Sources: Optional[Sequence[RuleGroupSourceStatelessRuleMatchAttributesSources]] = None
    TcpFlags: Optional[Sequence[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsUnion]] = None


class RuleGroupVariablesPortSetsDetailsUnion(BaseValidatorModel):
    pass


class RuleGroupVariablesIpSetsDetailsUnion(BaseValidatorModel):
    pass


class RuleGroupVariables(BaseValidatorModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsUnion] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsUnion] = None


class SecurityControlParameterUnion(BaseValidatorModel):
    pass


class Compliance(BaseValidatorModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[Sequence[str]] = None
    StatusReasons: Optional[Sequence[StatusReason]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[Sequence[AssociatedStandard]] = None
    SecurityControlParameters: Optional[Sequence[SecurityControlParameterUnion]] = None


class DescribeStandardsResponse(BaseValidatorModel):
    Standards: List[Standard]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchDisableStandardsResponse(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscription]
    ResponseMetadata: ResponseMetadata


class BatchEnableStandardsResponse(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscription]
    ResponseMetadata: ResponseMetadata


class GetEnabledStandardsResponse(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StatelessCustomActionDefinitionOutput(BaseValidatorModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionOutput] = None


class PortProbeActionOutput(BaseValidatorModel):
    PortProbeDetails: Optional[List[PortProbeDetail]] = None
    Blocked: Optional[bool] = None


class PortProbeAction(BaseValidatorModel):
    PortProbeDetails: Optional[Sequence[PortProbeDetail]] = None
    Blocked: Optional[bool] = None


class IndicatorOutput(BaseValidatorModel):
    pass


class SignalOutput(BaseValidatorModel):
    pass


class SequenceOutput(BaseValidatorModel):
    Uid: Optional[str] = None
    Actors: Optional[List[Actor]] = None
    Endpoints: Optional[List[NetworkEndpoint]] = None
    Signals: Optional[List[SignalOutput]] = None
    SequenceIndicators: Optional[List[IndicatorOutput]] = None


class AwsAthenaWorkGroupDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[str] = None
    Configuration: Optional[AwsAthenaWorkGroupConfigurationDetails] = None


class AwsAutoScalingAutoScalingGroupDetailsOutput(BaseValidatorModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[ AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutput ] = None
    AvailabilityZones: Optional[ List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails] ] = None
    LaunchTemplate: Optional[ AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification ] = None
    CapacityRebalance: Optional[bool] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnion(BaseValidatorModel):
    pass


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetails(BaseValidatorModel):
    InstancesDistribution: Optional[ AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetails ] = None
    LaunchTemplate: Optional[ AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsUnion ] = None


class AwsBackupBackupPlanBackupPlanDetailsOutput(BaseValidatorModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[ List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutput] ] = None
    BackupPlanRule: Optional[List[AwsBackupBackupPlanRuleDetailsOutput]] = None


class AwsCloudFrontDistributionOriginsOutput(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginItemOutput]] = None


class AwsCloudFrontDistributionOriginGroupsOutput(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginGroupOutput]] = None


class AwsCodeBuildProjectEnvironmentUnion(BaseValidatorModel):
    pass


class AwsCodeBuildProjectVpcConfigUnion(BaseValidatorModel):
    pass


class AwsCodeBuildProjectDetails(BaseValidatorModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[Sequence[AwsCodeBuildProjectArtifactsDetails]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentUnion] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSource] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetails] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigUnion] = None
    SecondaryArtifacts: Optional[Sequence[AwsCodeBuildProjectArtifactsDetails]] = None


class AwsDynamoDbTableReplicaOutput(BaseValidatorModel):
    pass


class AwsDynamoDbTableDetailsOutput(BaseValidatorModel):
    AttributeDefinitions: Optional[List[AwsDynamoDbTableAttributeDefinition]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummary] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[List[AwsDynamoDbTableGlobalSecondaryIndexOutput]] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchema]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[List[AwsDynamoDbTableLocalSecondaryIndexOutput]] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughput] = None
    Replicas: Optional[List[AwsDynamoDbTableReplicaOutput]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummary] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescription] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecification] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None


class AwsEc2LaunchTemplateDetailsOutput(BaseValidatorModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsOutput] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None


class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnion(BaseValidatorModel):
    pass


class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnion(BaseValidatorModel):
    pass


class AwsEc2LaunchTemplateDataDetails(BaseValidatorModel):
    BlockDeviceMappingSet: Optional[ Sequence[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetails] ] = None
    CapacityReservationSpecification: Optional[ AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetails ] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetails] = None
    CreditSpecification: Optional[AwsEc2LaunchTemplateDataCreditSpecificationDetails] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[ Sequence[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetails] ] = None
    ElasticInferenceAcceleratorSet: Optional[ Sequence[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetails] ] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetails] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetails] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetails] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[AwsEc2LaunchTemplateDataInstanceMarketOptionsDetails] = None
    InstanceRequirements: Optional[ AwsEc2LaunchTemplateDataInstanceRequirementsDetailsUnion ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[Sequence[AwsEc2LaunchTemplateDataLicenseSetDetails]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetails] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetails] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetails] = None
    NetworkInterfaceSet: Optional[ Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsUnion] ] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetails] = None
    PrivateDnsNameOptions: Optional[AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetails] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[Sequence[str]] = None
    SecurityGroupSet: Optional[Sequence[str]] = None
    UserData: Optional[str] = None


class AwsEc2SecurityGroupIpPermissionUnion(BaseValidatorModel):
    pass


class AwsEc2SecurityGroupDetails(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[Sequence[AwsEc2SecurityGroupIpPermissionUnion]] = None
    IpPermissionsEgress: Optional[Sequence[AwsEc2SecurityGroupIpPermission]] = None


class AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion(BaseValidatorModel):
    pass


class AwsEc2VpcPeeringConnectionDetails(BaseValidatorModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsUnion] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetails] = None
    VpcPeeringConnectionId: Optional[str] = None


class AwsEcsClusterDetailsOutput(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[List[str]] = None
    ClusterSettings: Optional[List[AwsEcsClusterClusterSettingsDetails]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetails] = None
    DefaultCapacityProviderStrategy: Optional[ List[AwsEcsClusterDefaultCapacityProviderStrategyDetails] ] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None


class AwsEcsClusterDetails(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[Sequence[str]] = None
    ClusterSettings: Optional[Sequence[AwsEcsClusterClusterSettingsDetails]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetails] = None
    DefaultCapacityProviderStrategy: Optional[ Sequence[AwsEcsClusterDefaultCapacityProviderStrategyDetails] ] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None


class AwsEcsContainerDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDetails(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[Sequence[AwsEcsTaskVolumeDetails]] = None
    Containers: Optional[Sequence[AwsEcsContainerDetailsUnion]] = None


class AwsEcsTaskDefinitionProxyConfigurationDetailsOutput(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionPlacementConstraintsDetails(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionDetailsOutput(BaseValidatorModel):
    ContainerDefinitions: Optional[ List[AwsEcsTaskDefinitionContainerDefinitionsDetailsOutput] ] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[ List[AwsEcsTaskDefinitionInferenceAcceleratorsDetails] ] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[List[AwsEcsTaskDefinitionPlacementConstraintsDetails]] = None
    ProxyConfiguration: Optional[AwsEcsTaskDefinitionProxyConfigurationDetailsOutput] = None
    RequiresCompatibilities: Optional[List[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskDefinitionVolumesDetailsOutput]] = None
    Status: Optional[str] = None


class AwsElbLoadBalancerListenerDescriptionUnion(BaseValidatorModel):
    pass


class AwsElbLoadBalancerBackendServerDescriptionUnion(BaseValidatorModel):
    pass


class AwsElbLoadBalancerPoliciesUnion(BaseValidatorModel):
    pass


class AwsElbLoadBalancerAttributesUnion(BaseValidatorModel):
    pass


class AwsElbLoadBalancerDetails(BaseValidatorModel):
    AvailabilityZones: Optional[Sequence[str]] = None
    BackendServerDescriptions: Optional[ Sequence[AwsElbLoadBalancerBackendServerDescriptionUnion] ] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheck] = None
    Instances: Optional[Sequence[AwsElbLoadBalancerInstance]] = None
    ListenerDescriptions: Optional[Sequence[AwsElbLoadBalancerListenerDescriptionUnion]] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesUnion] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesUnion] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroup] = None
    Subnets: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None


class AwsEventsEndpointDetailsOutput(BaseValidatorModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[List[AwsEventsEndpointEventBusesDetails]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetails] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetails] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


class AwsEventsEndpointDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[Sequence[AwsEventsEndpointEventBusesDetails]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetails] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetails] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None


class AwsGuardDutyDetectorDataSourcesDetails(BaseValidatorModel):
    CloudTrail: Optional[AwsGuardDutyDetectorDataSourcesCloudTrailDetails] = None
    DnsLogs: Optional[AwsGuardDutyDetectorDataSourcesDnsLogsDetails] = None
    FlowLogs: Optional[AwsGuardDutyDetectorDataSourcesFlowLogsDetails] = None
    Kubernetes: Optional[AwsGuardDutyDetectorDataSourcesKubernetesDetails] = None
    MalwareProtection: Optional[AwsGuardDutyDetectorDataSourcesMalwareProtectionDetails] = None
    S3Logs: Optional[AwsGuardDutyDetectorDataSourcesS3LogsDetails] = None


class AwsIamInstanceProfileUnion(BaseValidatorModel):
    pass


class AwsIamRoleDetails(BaseValidatorModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicy]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[Sequence[AwsIamInstanceProfileUnion]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundary] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[Sequence[AwsIamRolePolicy]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None


class AwsLambdaFunctionVpcConfigUnion(BaseValidatorModel):
    pass


class AwsLambdaFunctionEnvironmentUnion(BaseValidatorModel):
    pass


class AwsLambdaFunctionDetails(BaseValidatorModel):
    Code: Optional[AwsLambdaFunctionCode] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfig] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentUnion] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[Sequence[AwsLambdaFunctionLayer]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfig] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigUnion] = None
    Version: Optional[str] = None
    Architectures: Optional[Sequence[str]] = None
    PackageType: Optional[str] = None


class AwsMskClusterClusterInfoDetailsOutput(BaseValidatorModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetails] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[ AwsMskClusterClusterInfoClientAuthenticationDetailsOutput ] = None
    EnhancedMonitoring: Optional[str] = None


class AwsRdsDbInstanceDetailsOutput(BaseValidatorModel):
    AssociatedRoles: Optional[List[AwsRdsDbInstanceAssociatedRole]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpoint] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroup]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[List[str]] = None
    DbParameterGroups: Optional[List[AwsRdsDbParameterGroup]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupOutput] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesOutput] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[AwsRdsDbOptionGroupMembership]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[List[AwsRdsDbStatusInfo]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembership]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeature]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpoint] = None
    MaxAllocatedStorage: Optional[int] = None


class AwsRedshiftClusterClusterParameterGroupUnion(BaseValidatorModel):
    pass


class AwsRedshiftClusterDetails(BaseValidatorModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[Sequence[AwsRedshiftClusterClusterNode]] = None
    ClusterParameterGroups: Optional[ Sequence[AwsRedshiftClusterClusterParameterGroupUnion] ] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[Sequence[AwsRedshiftClusterClusterSecurityGroup]] = None
    ClusterSnapshotCopyStatus: Optional[AwsRedshiftClusterClusterSnapshotCopyStatus] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[ Sequence[AwsRedshiftClusterDeferredMaintenanceWindow] ] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatus] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpoint] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatus] = None
    IamRoles: Optional[Sequence[AwsRedshiftClusterIamRole]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[Sequence[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValues] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfo] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatus] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[AwsRedshiftClusterVpcSecurityGroup]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatus] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutput(BaseValidatorModel):
    pass


class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutput(BaseValidatorModel):
    Predicate: Optional[ AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutput ] = None


class AwsS3BucketNotificationConfigurationS3KeyFilterUnion(BaseValidatorModel):
    pass


class AwsS3BucketNotificationConfigurationFilter(BaseValidatorModel):
    S3KeyFilter: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterUnion] = None


class AwsWafWebAclRuleUnion(BaseValidatorModel):
    pass


class AwsWafWebAclDetails(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[Sequence[AwsWafWebAclRuleUnion]] = None
    WebAclId: Optional[str] = None


class AwsWafv2CustomRequestHandlingDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2ActionAllowDetails(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsUnion] = None


class AwsWafv2RulesActionCaptchaDetails(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsUnion] = None


class AwsWafv2RulesActionCountDetails(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsUnion] = None


class AwsWafv2RulesActionDetailsOutput(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsOutput] = None
    Block: Optional[AwsWafv2ActionBlockDetailsOutput] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsOutput] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsOutput] = None


class AwsWafv2WebAclActionDetailsOutput(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsOutput] = None
    Block: Optional[AwsWafv2ActionBlockDetailsOutput] = None


class AwsWafv2CustomResponseDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2ActionBlockDetails(BaseValidatorModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsUnion] = None


class VulnerabilityCodeVulnerabilitiesUnion(BaseValidatorModel):
    pass


class CvssUnion(BaseValidatorModel):
    pass


class Vulnerability(BaseValidatorModel):
    Id: str
    VulnerablePackages: Optional[Sequence[SoftwarePackage]] = None
    Cvss: Optional[Sequence[CvssUnion]] = None
    RelatedVulnerabilities: Optional[Sequence[str]] = None
    Vendor: Optional[VulnerabilityVendor] = None
    ReferenceUrls: Optional[Sequence[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[Sequence[VulnerabilityCodeVulnerabilitiesUnion]] = None


class SecurityControlDefinition(BaseValidatorModel):
    SecurityControlId: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    CurrentRegionAvailability: RegionAvailabilityStatusType
    CustomizableProperties: Optional[List[Literal["Parameters"]]] = None
    ParameterDefinitions: Optional[Dict[str, ParameterDefinition]] = None


class BatchGetConfigurationPolicyAssociationsResponse(BaseValidatorModel):
    ConfigurationPolicyAssociations: List[ConfigurationPolicyAssociationSummary]
    UnprocessedConfigurationPolicyAssociations: List[ UnprocessedConfigurationPolicyAssociation ]
    ResponseMetadata: ResponseMetadata


class AutomationRulesActionOutput(BaseValidatorModel):
    pass


class AutomationRulesFindingFiltersOutput(BaseValidatorModel):
    pass


class AutomationRulesConfig(BaseValidatorModel):
    RuleArn: Optional[str] = None
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    RuleName: Optional[str] = None
    Description: Optional[str] = None
    IsTerminal: Optional[bool] = None
    Criteria: Optional[AutomationRulesFindingFiltersOutput] = None
    Actions: Optional[List[AutomationRulesActionOutput]] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None


class AwsSecurityFindingFiltersOutput(BaseValidatorModel):
    pass


class Insight(BaseValidatorModel):
    InsightArn: str
    Name: str
    Filters: AwsSecurityFindingFiltersOutput
    GroupByAttribute: str


class IndicatorUnion(BaseValidatorModel):
    pass


class SignalUnion(BaseValidatorModel):
    pass


class SequenceType(BaseValidatorModel):
    Uid: Optional[str] = None
    Actors: Optional[Sequence[Actor]] = None
    Endpoints: Optional[Sequence[NetworkEndpoint]] = None
    Signals: Optional[Sequence[SignalUnion]] = None
    SequenceIndicators: Optional[Sequence[IndicatorUnion]] = None


class NetworkHeaderOutput(BaseValidatorModel):
    pass


class NetworkPathComponentOutput(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderOutput] = None
    Ingress: Optional[NetworkHeaderOutput] = None


class CustomDataIdentifiersDetectionsOutput(BaseValidatorModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesOutput] = None


class SecurityControlsConfigurationOutput(BaseValidatorModel):
    EnabledSecurityControlIdentifiers: Optional[List[str]] = None
    DisabledSecurityControlIdentifiers: Optional[List[str]] = None
    SecurityControlCustomParameters: Optional[List[SecurityControlCustomParameterOutput]] = None


class BatchGetSecurityControlsResponse(BaseValidatorModel):
    SecurityControls: List[SecurityControl]
    UnprocessedIds: List[UnprocessedSecurityControl]
    ResponseMetadata: ResponseMetadata


class SecurityControlCustomParameter(BaseValidatorModel):
    SecurityControlId: Optional[str] = None
    Parameters: Optional[Mapping[str, ParameterConfiguration]] = None


class RuleGroupSourceStatelessRulesDetailsOutput(BaseValidatorModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionOutput] = None


class FirewallPolicyStatelessCustomActionsDetailsOutput(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionOutput] = None
    ActionName: Optional[str] = None


class RuleGroupSourceCustomActionsDetailsOutput(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionOutput] = None
    ActionName: Optional[str] = None


class StatelessCustomPublishMetricActionUnion(BaseValidatorModel):
    pass


class StatelessCustomActionDefinition(BaseValidatorModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionUnion] = None


class NetworkConnectionAction(BaseValidatorModel):
    pass


class DnsRequestAction(BaseValidatorModel):
    pass


class AwsApiCallActionOutput(BaseValidatorModel):
    pass


class ActionOutput(BaseValidatorModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionAction] = None
    AwsApiCallAction: Optional[AwsApiCallActionOutput] = None
    DnsRequestAction: Optional[DnsRequestAction] = None
    PortProbeAction: Optional[PortProbeActionOutput] = None


class AwsBackupBackupPlanDetailsOutput(BaseValidatorModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsOutput] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None


class AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnion(BaseValidatorModel):
    pass


class AwsBackupBackupPlanRuleDetailsUnion(BaseValidatorModel):
    pass


class AwsBackupBackupPlanBackupPlanDetails(BaseValidatorModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[ Sequence[AwsBackupBackupPlanAdvancedBackupSettingsDetailsUnion] ] = None
    BackupPlanRule: Optional[Sequence[AwsBackupBackupPlanRuleDetailsUnion]] = None


class AwsCloudFrontDistributionDetailsOutput(BaseValidatorModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsOutput] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehavior] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLogging] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsOutput] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsOutput] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificate] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None


class AwsCloudFrontDistributionOriginGroupFailoverUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionOriginGroup(BaseValidatorModel):
    FailoverCriteria: Optional[AwsCloudFrontDistributionOriginGroupFailoverUnion] = None


class AwsCloudFrontDistributionOriginCustomOriginConfigUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionOriginItem(BaseValidatorModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfig] = None
    CustomOriginConfig: Optional[AwsCloudFrontDistributionOriginCustomOriginConfigUnion] = None


class AwsDynamoDbTableLocalSecondaryIndexUnion(BaseValidatorModel):
    pass


class AwsDynamoDbTableGlobalSecondaryIndexUnion(BaseValidatorModel):
    pass


class AwsDynamoDbTableReplicaUnion(BaseValidatorModel):
    pass


class AwsDynamoDbTableDetails(BaseValidatorModel):
    AttributeDefinitions: Optional[Sequence[AwsDynamoDbTableAttributeDefinition]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummary] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[Sequence[AwsDynamoDbTableGlobalSecondaryIndexUnion]] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchema]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[Sequence[AwsDynamoDbTableLocalSecondaryIndexUnion]] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughput] = None
    Replicas: Optional[Sequence[AwsDynamoDbTableReplicaUnion]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummary] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescription] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecification] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None


class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsDetails(BaseValidatorModel):
    Command: Optional[Sequence[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetails] ] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[Sequence[str]] = None
    DnsServers: Optional[Sequence[str]] = None
    DockerLabels: Optional[Mapping[str, str]] = None
    DockerSecurityOptions: Optional[Sequence[str]] = None
    EntryPoint: Optional[Sequence[str]] = None
    Environment: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetails] ] = None
    EnvironmentFiles: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetails] ] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetails] ] = None
    FirelensConfiguration: Optional[ AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsUnion ] = None
    HealthCheck: Optional[AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsUnion] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[Sequence[str]] = None
    LinuxParameters: Optional[ AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsUnion ] = None
    LogConfiguration: Optional[ AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsUnion ] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetails] ] = None
    Name: Optional[str] = None
    PortMappings: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails] ] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[ AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetails ] = None
    ResourceRequirements: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetails] ] = None
    Secrets: Optional[Sequence[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetails]] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetails] ] = None
    Ulimits: Optional[Sequence[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails]] = None
    User: Optional[str] = None
    VolumesFrom: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails] ] = None
    WorkingDirectory: Optional[str] = None


class AwsEksClusterLoggingDetailsUnion(BaseValidatorModel):
    pass


class AwsEksClusterResourcesVpcConfigDetailsUnion(BaseValidatorModel):
    pass


class AwsEksClusterDetails(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsUnion] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsUnion] = None


class AwsGuardDutyDetectorDetailsOutput(BaseValidatorModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetails] = None
    Features: Optional[List[AwsGuardDutyDetectorFeaturesDetails]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None


class AwsGuardDutyDetectorDetails(BaseValidatorModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetails] = None
    Features: Optional[Sequence[AwsGuardDutyDetectorFeaturesDetails]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None


class AwsMskClusterDetailsOutput(BaseValidatorModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsOutput] = None


class AwsMskClusterClusterInfoClientAuthenticationDetailsUnion(BaseValidatorModel):
    pass


class AwsMskClusterClusterInfoDetails(BaseValidatorModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetails] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[ AwsMskClusterClusterInfoClientAuthenticationDetailsUnion ] = None
    EnhancedMonitoring: Optional[str] = None


class AwsRdsDbPendingModifiedValuesUnion(BaseValidatorModel):
    pass


class AwsRdsDbSubnetGroupUnion(BaseValidatorModel):
    pass


class AwsRdsDbInstanceDetails(BaseValidatorModel):
    AssociatedRoles: Optional[Sequence[AwsRdsDbInstanceAssociatedRole]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpoint] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[AwsRdsDbInstanceVpcSecurityGroup]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[Sequence[str]] = None
    DbParameterGroups: Optional[Sequence[AwsRdsDbParameterGroup]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupUnion] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesUnion] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[Sequence[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[Sequence[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[Sequence[AwsRdsDbOptionGroupMembership]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[Sequence[AwsRdsDbStatusInfo]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[Sequence[AwsRdsDbDomainMembership]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[Sequence[str]] = None
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeature]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpoint] = None
    MaxAllocatedStorage: Optional[int] = None


class AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails(BaseValidatorModel):
    pass


class AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails(BaseValidatorModel):
    pass


class AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutput(BaseValidatorModel):
    AbortIncompleteMultipartUpload: Optional[ AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails ] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutput] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[ List[AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails] ] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[ List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails] ] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnion(BaseValidatorModel):
    pass


class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetails(BaseValidatorModel):
    Predicate: Optional[ AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsUnion ] = None


class AwsS3BucketNotificationConfigurationDetailOutput(BaseValidatorModel):
    pass


class AwsS3BucketNotificationConfigurationOutput(BaseValidatorModel):
    Configurations: Optional[List[AwsS3BucketNotificationConfigurationDetailOutput]] = None


class AwsWafv2RulesDetailsOutput(BaseValidatorModel):
    Action: Optional[AwsWafv2RulesActionDetailsOutput] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class GetSecurityControlDefinitionResponse(BaseValidatorModel):
    SecurityControlDefinition: SecurityControlDefinition
    ResponseMetadata: ResponseMetadata


class ListSecurityControlDefinitionsResponse(BaseValidatorModel):
    SecurityControlDefinitions: List[SecurityControlDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchGetAutomationRulesResponse(BaseValidatorModel):
    Rules: List[AutomationRulesConfig]
    UnprocessedAutomationRules: List[UnprocessedAutomationRule]
    ResponseMetadata: ResponseMetadata


class GetInsightsResponse(BaseValidatorModel):
    Insights: List[Insight]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AwsSecurityFindingFiltersUnion(BaseValidatorModel):
    pass


class CreateInsightRequest(BaseValidatorModel):
    Name: str
    Filters: AwsSecurityFindingFiltersUnion
    GroupByAttribute: str


class GetFindingsRequestPaginate(BaseValidatorModel):
    Filters: Optional[AwsSecurityFindingFiltersUnion] = None
    SortCriteria: Optional[Sequence[SortCriterion]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetFindingsRequest(BaseValidatorModel):
    Filters: Optional[AwsSecurityFindingFiltersUnion] = None
    SortCriteria: Optional[Sequence[SortCriterion]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UpdateFindingsRequest(BaseValidatorModel):
    Filters: AwsSecurityFindingFiltersUnion
    Note: Optional[NoteUpdate] = None
    RecordState: Optional[RecordStateType] = None


class UpdateInsightRequest(BaseValidatorModel):
    InsightArn: str
    Name: Optional[str] = None
    Filters: Optional[AwsSecurityFindingFiltersUnion] = None
    GroupByAttribute: Optional[str] = None


class CustomDataIdentifiersResultOutput(BaseValidatorModel):
    Detections: Optional[List[CustomDataIdentifiersDetectionsOutput]] = None
    TotalCount: Optional[int] = None


class SensitiveDataDetectionsOutput(BaseValidatorModel):
    pass


class SensitiveDataResultOutput(BaseValidatorModel):
    Category: Optional[str] = None
    Detections: Optional[List[SensitiveDataDetectionsOutput]] = None
    TotalCount: Optional[int] = None


class OccurrencesUnion(BaseValidatorModel):
    pass


class CustomDataIdentifiersDetections(BaseValidatorModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesUnion] = None


class SecurityHubPolicyOutput(BaseValidatorModel):
    ServiceEnabled: Optional[bool] = None
    EnabledStandardIdentifiers: Optional[List[str]] = None
    SecurityControlsConfiguration: Optional[SecurityControlsConfigurationOutput] = None


class ParameterConfigurationUnion(BaseValidatorModel):
    pass


class UpdateSecurityControlRequest(BaseValidatorModel):
    SecurityControlId: str
    Parameters: Mapping[str, ParameterConfigurationUnion]
    LastUpdateReason: Optional[str] = None


class SecurityControlsConfiguration(BaseValidatorModel):
    EnabledSecurityControlIdentifiers: Optional[Sequence[str]] = None
    DisabledSecurityControlIdentifiers: Optional[Sequence[str]] = None
    SecurityControlCustomParameters: Optional[Sequence[SecurityControlCustomParameter]] = None


class RuleGroupSourceStatelessRuleMatchAttributesUnion(BaseValidatorModel):
    pass


class RuleGroupSourceStatelessRuleDefinition(BaseValidatorModel):
    Actions: Optional[Sequence[str]] = None
    MatchAttributes: Optional[RuleGroupSourceStatelessRuleMatchAttributesUnion] = None


class FirewallPolicyDetailsOutput(BaseValidatorModel):
    StatefulRuleGroupReferences: Optional[ List[FirewallPolicyStatefulRuleGroupReferencesDetails] ] = None
    StatelessCustomActions: Optional[ List[FirewallPolicyStatelessCustomActionsDetailsOutput] ] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessRuleGroupReferences: Optional[ List[FirewallPolicyStatelessRuleGroupReferencesDetails] ] = None


class RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutput(BaseValidatorModel):
    CustomActions: Optional[List[RuleGroupSourceCustomActionsDetailsOutput]] = None
    StatelessRules: Optional[List[RuleGroupSourceStatelessRulesDetailsOutput]] = None


class AwsApiCallActionUnion(BaseValidatorModel):
    pass


class PortProbeActionUnion(BaseValidatorModel):
    pass


class Action(BaseValidatorModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionAction] = None
    AwsApiCallAction: Optional[AwsApiCallActionUnion] = None
    DnsRequestAction: Optional[DnsRequestAction] = None
    PortProbeAction: Optional[PortProbeActionUnion] = None


class AutomationRulesFindingFiltersUnion(BaseValidatorModel):
    pass


class AutomationRulesActionUnion(BaseValidatorModel):
    pass


class CreateAutomationRuleRequest(BaseValidatorModel):
    RuleOrder: int
    RuleName: str
    Description: str
    Criteria: AutomationRulesFindingFiltersUnion
    Actions: Sequence[AutomationRulesActionUnion]
    Tags: Optional[Mapping[str, str]] = None
    RuleStatus: Optional[RuleStatusType] = None
    IsTerminal: Optional[bool] = None


class UpdateAutomationRulesRequestItem(BaseValidatorModel):
    RuleArn: str
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    Description: Optional[str] = None
    RuleName: Optional[str] = None
    IsTerminal: Optional[bool] = None
    Criteria: Optional[AutomationRulesFindingFiltersUnion] = None
    Actions: Optional[Sequence[AutomationRulesActionUnion]] = None


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnion(BaseValidatorModel):
    pass


class AwsAutoScalingAutoScalingGroupDetails(BaseValidatorModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[Sequence[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[ AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsUnion ] = None
    AvailabilityZones: Optional[ Sequence[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails] ] = None
    LaunchTemplate: Optional[ AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecification ] = None
    CapacityRebalance: Optional[bool] = None


class AwsEc2LaunchTemplateDataDetailsUnion(BaseValidatorModel):
    pass


class AwsEc2LaunchTemplateDetails(BaseValidatorModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsUnion] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None


class AwsS3BucketBucketLifecycleConfigurationDetailsOutput(BaseValidatorModel):
    Rules: Optional[List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutput]] = None


class AwsWafv2RuleGroupDetailsOutput(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsOutput]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class AwsWafv2WebAclDetailsOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetails] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsOutput] = None
    Description: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsOutput]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class AwsWafv2ActionAllowDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2RulesActionCaptchaDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2RulesActionCountDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2ActionBlockDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2RulesActionDetails(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsUnion] = None
    Block: Optional[AwsWafv2ActionBlockDetailsUnion] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsUnion] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsUnion] = None


class AwsWafv2WebAclActionDetails(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsUnion] = None
    Block: Optional[AwsWafv2ActionBlockDetailsUnion] = None


class NetworkHeaderUnion(BaseValidatorModel):
    pass


class NetworkPathComponent(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderUnion] = None
    Ingress: Optional[NetworkHeaderUnion] = None


class ClassificationResultOutput(BaseValidatorModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatus] = None
    SensitiveData: Optional[List[SensitiveDataResultOutput]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultOutput] = None


class PolicyOutput(BaseValidatorModel):
    SecurityHub: Optional[SecurityHubPolicyOutput] = None


class SecurityHubPolicy(BaseValidatorModel):
    ServiceEnabled: Optional[bool] = None
    EnabledStandardIdentifiers: Optional[Sequence[str]] = None
    SecurityControlsConfiguration: Optional[SecurityControlsConfiguration] = None


class AwsNetworkFirewallFirewallPolicyDetailsOutput(BaseValidatorModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsOutput] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None


class RuleGroupSourceOutput(BaseValidatorModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsOutput] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[List[RuleGroupSourceStatefulRulesDetailsOutput]] = None
    StatelessRulesAndCustomActions: Optional[ RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutput ] = None


class StatelessCustomActionDefinitionUnion(BaseValidatorModel):
    pass


class FirewallPolicyStatelessCustomActionsDetails(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionUnion] = None
    ActionName: Optional[str] = None


class RuleGroupSourceCustomActionsDetails(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionUnion] = None
    ActionName: Optional[str] = None


class BatchUpdateAutomationRulesRequest(BaseValidatorModel):
    UpdateAutomationRulesRequestItems: Sequence[UpdateAutomationRulesRequestItem]


class AwsBackupBackupPlanBackupPlanDetailsUnion(BaseValidatorModel):
    pass


class AwsBackupBackupPlanDetails(BaseValidatorModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsUnion] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None


class AwsCloudFrontDistributionOriginGroupUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionOriginGroups(BaseValidatorModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionOriginGroupUnion]] = None


class AwsCloudFrontDistributionOriginItemUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionOrigins(BaseValidatorModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionOriginItemUnion]] = None


class AwsEcsTaskDefinitionVolumesDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionProxyConfigurationDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionContainerDefinitionsDetailsUnion(BaseValidatorModel):
    pass


class AwsEcsTaskDefinitionDetails(BaseValidatorModel):
    ContainerDefinitions: Optional[ Sequence[AwsEcsTaskDefinitionContainerDefinitionsDetailsUnion] ] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[ Sequence[AwsEcsTaskDefinitionInferenceAcceleratorsDetails] ] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[ Sequence[AwsEcsTaskDefinitionPlacementConstraintsDetails] ] = None
    ProxyConfiguration: Optional[AwsEcsTaskDefinitionProxyConfigurationDetailsUnion] = None
    RequiresCompatibilities: Optional[Sequence[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[Sequence[AwsEcsTaskDefinitionVolumesDetailsUnion]] = None
    Status: Optional[str] = None


class AwsMskClusterClusterInfoDetailsUnion(BaseValidatorModel):
    pass


class AwsMskClusterDetails(BaseValidatorModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsUnion] = None


class AwsS3BucketDetailsOutput(BaseValidatorModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ AwsS3BucketServerSideEncryptionConfigurationOutput ] = None
    BucketLifecycleConfiguration: Optional[ AwsS3BucketBucketLifecycleConfigurationDetailsOutput ] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetails] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfiguration] = None
    BucketWebsiteConfiguration: Optional[AwsS3BucketWebsiteConfigurationOutput] = None
    BucketNotificationConfiguration: Optional[AwsS3BucketNotificationConfigurationOutput] = None
    BucketVersioningConfiguration: Optional[AwsS3BucketBucketVersioningConfiguration] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfiguration] = None
    Name: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnion(BaseValidatorModel):
    pass


class AwsS3BucketBucketLifecycleConfigurationRulesDetails(BaseValidatorModel):
    AbortIncompleteMultipartUpload: Optional[ AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetails ] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsUnion] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[ Sequence[ AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetails ] ] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[ Sequence[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails] ] = None


class DataClassificationDetailsOutput(BaseValidatorModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultOutput] = None


class CustomDataIdentifiersDetectionsUnion(BaseValidatorModel):
    pass


class CustomDataIdentifiersResult(BaseValidatorModel):
    Detections: Optional[Sequence[CustomDataIdentifiersDetectionsUnion]] = None
    TotalCount: Optional[int] = None


class SensitiveDataDetectionsUnion(BaseValidatorModel):
    pass


class SensitiveDataResult(BaseValidatorModel):
    Category: Optional[str] = None
    Detections: Optional[Sequence[SensitiveDataDetectionsUnion]] = None
    TotalCount: Optional[int] = None


class CreateConfigurationPolicyResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutput
    ResponseMetadata: ResponseMetadata


class GetConfigurationPolicyResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutput
    ResponseMetadata: ResponseMetadata


class UpdateConfigurationPolicyResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutput
    ResponseMetadata: ResponseMetadata


class Policy(BaseValidatorModel):
    SecurityHub: Optional[SecurityHubPolicy] = None


class RuleGroupSourceStatelessRuleDefinitionUnion(BaseValidatorModel):
    pass


class RuleGroupSourceStatelessRulesDetails(BaseValidatorModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionUnion] = None


class RuleGroupDetailsOutput(BaseValidatorModel):
    RuleVariables: Optional[RuleGroupVariablesOutput] = None
    RulesSource: Optional[RuleGroupSourceOutput] = None


class AwsS3BucketNotificationConfigurationDetailUnion(BaseValidatorModel):
    pass


class AwsS3BucketNotificationConfiguration(BaseValidatorModel):
    Configurations: Optional[Sequence[AwsS3BucketNotificationConfigurationDetailUnion]] = None


class AwsWafv2RulesActionDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2RulesDetails(BaseValidatorModel):
    Action: Optional[AwsWafv2RulesActionDetailsUnion] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class FirewallPolicyStatelessCustomActionsDetailsUnion(BaseValidatorModel):
    pass


class FirewallPolicyDetails(BaseValidatorModel):
    StatefulRuleGroupReferences: Optional[ Sequence[FirewallPolicyStatefulRuleGroupReferencesDetails] ] = None
    StatelessCustomActions: Optional[ Sequence[FirewallPolicyStatelessCustomActionsDetailsUnion] ] = None
    StatelessDefaultActions: Optional[Sequence[str]] = None
    StatelessFragmentDefaultActions: Optional[Sequence[str]] = None
    StatelessRuleGroupReferences: Optional[ Sequence[FirewallPolicyStatelessRuleGroupReferencesDetails] ] = None


class AwsCloudFrontDistributionCacheBehaviorsUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionOriginGroupsUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionOriginsUnion(BaseValidatorModel):
    pass


class AwsCloudFrontDistributionDetails(BaseValidatorModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsUnion] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehavior] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLogging] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsUnion] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsUnion] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificate] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None


class AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnion(BaseValidatorModel):
    pass


class AwsS3BucketBucketLifecycleConfigurationDetails(BaseValidatorModel):
    Rules: Optional[Sequence[AwsS3BucketBucketLifecycleConfigurationRulesDetailsUnion]] = None


class AwsWafv2WebAclActionDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2WebAclDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetails] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsUnion] = None
    Description: Optional[str] = None
    Rules: Optional[Sequence[AwsWafv2RulesDetails]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class SensitiveDataResultUnion(BaseValidatorModel):
    pass


class CustomDataIdentifiersResultUnion(BaseValidatorModel):
    pass


class ClassificationResult(BaseValidatorModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatus] = None
    SensitiveData: Optional[Sequence[SensitiveDataResultUnion]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultUnion] = None


class PolicyUnion(BaseValidatorModel):
    pass


class CreateConfigurationPolicyRequest(BaseValidatorModel):
    Name: str
    ConfigurationPolicy: PolicyUnion
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateConfigurationPolicyRequest(BaseValidatorModel):
    Identifier: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    UpdatedReason: Optional[str] = None
    ConfigurationPolicy: Optional[PolicyUnion] = None


class RuleGroupSourceCustomActionsDetailsUnion(BaseValidatorModel):
    pass


class RuleGroupSourceStatelessRulesDetailsUnion(BaseValidatorModel):
    pass


class RuleGroupSourceStatelessRulesAndCustomActionsDetails(BaseValidatorModel):
    CustomActions: Optional[Sequence[RuleGroupSourceCustomActionsDetailsUnion]] = None
    StatelessRules: Optional[Sequence[RuleGroupSourceStatelessRulesDetailsUnion]] = None


class AwsWafv2RulesDetailsUnion(BaseValidatorModel):
    pass


class AwsWafv2RuleGroupDetails(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[Sequence[AwsWafv2RulesDetailsUnion]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetails] = None


class FirewallPolicyDetailsUnion(BaseValidatorModel):
    pass


class AwsNetworkFirewallFirewallPolicyDetails(BaseValidatorModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsUnion] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None


class AwsS3BucketWebsiteConfigurationUnion(BaseValidatorModel):
    pass


class AwsS3BucketNotificationConfigurationUnion(BaseValidatorModel):
    pass


class AwsS3BucketServerSideEncryptionConfigurationUnion(BaseValidatorModel):
    pass


class AwsS3BucketBucketLifecycleConfigurationDetailsUnion(BaseValidatorModel):
    pass


class AwsS3BucketDetails(BaseValidatorModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[ AwsS3BucketServerSideEncryptionConfigurationUnion ] = None
    BucketLifecycleConfiguration: Optional[ AwsS3BucketBucketLifecycleConfigurationDetailsUnion ] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetails] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfiguration] = None
    BucketWebsiteConfiguration: Optional[AwsS3BucketWebsiteConfigurationUnion] = None
    BucketNotificationConfiguration: Optional[AwsS3BucketNotificationConfigurationUnion] = None
    BucketVersioningConfiguration: Optional[AwsS3BucketBucketVersioningConfiguration] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfiguration] = None
    Name: Optional[str] = None


class ClassificationResultUnion(BaseValidatorModel):
    pass


class DataClassificationDetails(BaseValidatorModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultUnion] = None


class RuleGroupSourceStatefulRulesDetailsUnion(BaseValidatorModel):
    pass


class RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnion(BaseValidatorModel):
    pass


class RuleGroupSourceListDetailsUnion(BaseValidatorModel):
    pass


class RuleGroupSource(BaseValidatorModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsUnion] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[Sequence[RuleGroupSourceStatefulRulesDetailsUnion]] = None
    StatelessRulesAndCustomActions: Optional[ RuleGroupSourceStatelessRulesAndCustomActionsDetailsUnion ] = None


class Note(BaseValidatorModel):
    pass


class Network(BaseValidatorModel):
    pass


class ThreatIntelIndicator(BaseValidatorModel):
    pass


class ResourceOutput(BaseValidatorModel):
    pass


class DetectionOutput(BaseValidatorModel):
    pass


class Malware(BaseValidatorModel):
    pass


class AwsSecurityFindingOutput(BaseValidatorModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List[ResourceOutput]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[List[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[Severity] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[Remediation] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Dict[str, str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Malware: Optional[List[Malware]] = None
    Network: Optional[Network] = None
    NetworkPath: Optional[List[NetworkPathComponentOutput]] = None
    Process: Optional[ProcessDetails] = None
    Threats: Optional[List[ThreatOutput]] = None
    ThreatIntelIndicators: Optional[List[ThreatIntelIndicator]] = None
    Compliance: Optional[ComplianceOutput] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[Workflow] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[List[RelatedFinding]] = None
    Note: Optional[Note] = None
    Vulnerabilities: Optional[List[VulnerabilityOutput]] = None
    PatchSummary: Optional[PatchSummary] = None
    Action: Optional[ActionOutput] = None
    FindingProviderFields: Optional[FindingProviderFieldsOutput] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsOutput] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None
    Detection: Optional[DetectionOutput] = None


class GetFindingsResponse(BaseValidatorModel):
    Findings: List[AwsSecurityFindingOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RuleGroupSourceUnion(BaseValidatorModel):
    pass


class RuleGroupVariablesUnion(BaseValidatorModel):
    pass


class RuleGroupDetails(BaseValidatorModel):
    RuleVariables: Optional[RuleGroupVariablesUnion] = None
    RulesSource: Optional[RuleGroupSourceUnion] = None


class DetectionUnion(BaseValidatorModel):
    pass


class NetworkPathComponentUnion(BaseValidatorModel):
    pass


class ActionUnion(BaseValidatorModel):
    pass


class ThreatUnion(BaseValidatorModel):
    pass


class GeneratorDetailsUnion(BaseValidatorModel):
    pass


class ResourceUnion(BaseValidatorModel):
    pass


class ComplianceUnion(BaseValidatorModel):
    pass


class FindingProviderFieldsUnion(BaseValidatorModel):
    pass


class VulnerabilityUnion(BaseValidatorModel):
    pass


class AwsSecurityFinding(BaseValidatorModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: Sequence[ResourceUnion]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[Sequence[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[Severity] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[Remediation] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Mapping[str, str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Malware: Optional[Sequence[Malware]] = None
    Network: Optional[Network] = None
    NetworkPath: Optional[Sequence[NetworkPathComponentUnion]] = None
    Process: Optional[ProcessDetails] = None
    Threats: Optional[Sequence[ThreatUnion]] = None
    ThreatIntelIndicators: Optional[Sequence[ThreatIntelIndicator]] = None
    Compliance: Optional[ComplianceUnion] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[Workflow] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[Sequence[RelatedFinding]] = None
    Note: Optional[Note] = None
    Vulnerabilities: Optional[Sequence[VulnerabilityUnion]] = None
    PatchSummary: Optional[PatchSummary] = None
    Action: Optional[ActionUnion] = None
    FindingProviderFields: Optional[FindingProviderFieldsUnion] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsUnion] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None
    Detection: Optional[DetectionUnion] = None


class AwsSecurityFindingUnion(BaseValidatorModel):
    pass


class BatchImportFindingsRequest(BaseValidatorModel):
    Findings: Sequence[AwsSecurityFindingUnion]



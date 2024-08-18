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
from aws_resource_validator.pydantic_models.securityhub_constants import *

class AcceptAdministratorInvitationRequestRequestTypeDef(BaseValidatorModel):
    AdministratorId: str
    InvitationId: str

class AcceptInvitationRequestRequestTypeDef(BaseValidatorModel):
    MasterId: str
    InvitationId: str

class AccountDetailsTypeDef(BaseValidatorModel):
    AccountId: str
    Email: Optional[str] = None

class DnsRequestActionTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    Protocol: Optional[str] = None
    Blocked: Optional[bool] = None

class ActionLocalIpDetailsTypeDef(BaseValidatorModel):
    IpAddressV4: Optional[str] = None

class ActionLocalPortDetailsTypeDef(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None

class CityTypeDef(BaseValidatorModel):
    CityName: Optional[str] = None

class CountryTypeDef(BaseValidatorModel):
    CountryCode: Optional[str] = None
    CountryName: Optional[str] = None

class GeoLocationTypeDef(BaseValidatorModel):
    Lon: Optional[float] = None
    Lat: Optional[float] = None

class IpOrganizationDetailsTypeDef(BaseValidatorModel):
    Asn: Optional[int] = None
    AsnOrg: Optional[str] = None
    Isp: Optional[str] = None
    Org: Optional[str] = None

class ActionRemotePortDetailsTypeDef(BaseValidatorModel):
    Port: Optional[int] = None
    PortName: Optional[str] = None

class ActionTargetTypeDef(BaseValidatorModel):
    ActionTargetArn: str
    Name: str
    Description: str

class AdjustmentTypeDef(BaseValidatorModel):
    Metric: Optional[str] = None
    Reason: Optional[str] = None

class AdminAccountTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Status: Optional[AdminStatusType] = None

class AssociatedStandardTypeDef(BaseValidatorModel):
    StandardsId: Optional[str] = None

class AssociationFiltersTypeDef(BaseValidatorModel):
    ConfigurationPolicyId: Optional[str] = None
    AssociationType: Optional[AssociationTypeType] = None
    AssociationStatus: Optional[ConfigurationPolicyAssociationStatusType] = None

class AssociationStateDetailsTypeDef(BaseValidatorModel):
    State: Optional[str] = None
    StatusMessage: Optional[str] = None

class NoteUpdateTypeDef(BaseValidatorModel):
    Text: str
    UpdatedBy: str

class RelatedFindingTypeDef(BaseValidatorModel):
    ProductArn: str
    Id: str

class SeverityUpdateTypeDef(BaseValidatorModel):
    Normalized: Optional[int] = None
    Product: Optional[float] = None
    Label: Optional[SeverityLabelType] = None

class WorkflowUpdateTypeDef(BaseValidatorModel):
    Status: Optional[WorkflowStatusType] = None

class MapFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Comparison: Optional[MapFilterComparisonType] = None

class NumberFilterTypeDef(BaseValidatorModel):
    Gte: Optional[float] = None
    Lte: Optional[float] = None
    Gt: Optional[float] = None
    Lt: Optional[float] = None
    Eq: Optional[float] = None

class StringFilterTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Comparison: Optional[StringFilterComparisonType] = None

class AutomationRulesMetadataTypeDef(BaseValidatorModel):
    RuleArn: Optional[str] = None
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    RuleName: Optional[str] = None
    Description: Optional[str] = None
    IsTerminal: Optional[bool] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None

class AvailabilityZoneTypeDef(BaseValidatorModel):
    ZoneName: Optional[str] = None
    SubnetId: Optional[str] = None

class AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    UseAwsOwnedKey: Optional[bool] = None

class AwsAmazonMqBrokerLdapServerMetadataDetailsExtraOutputTypeDef(BaseValidatorModel):
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

class AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef(BaseValidatorModel):
    DayOfWeek: Optional[str] = None
    TimeOfDay: Optional[str] = None
    TimeZone: Optional[str] = None

class AwsAmazonMqBrokerUsersDetailsTypeDef(BaseValidatorModel):
    PendingChange: Optional[str] = None
    Username: Optional[str] = None

class AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef(BaseValidatorModel):
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

class AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef(BaseValidatorModel):
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

class AwsAmazonMqBrokerLogsPendingDetailsTypeDef(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None

class AwsApiCallActionDomainDetailsTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None

class AwsApiGatewayAccessLogSettingsTypeDef(BaseValidatorModel):
    Format: Optional[str] = None
    DestinationArn: Optional[str] = None

class AwsApiGatewayCanarySettingsExtraOutputTypeDef(BaseValidatorModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Dict[str, str]] = None
    UseStageCache: Optional[bool] = None

class AwsApiGatewayCanarySettingsOutputTypeDef(BaseValidatorModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Dict[str, str]] = None
    UseStageCache: Optional[bool] = None

class AwsApiGatewayCanarySettingsTypeDef(BaseValidatorModel):
    PercentTraffic: Optional[float] = None
    DeploymentId: Optional[str] = None
    StageVariableOverrides: Optional[Mapping[str, str]] = None
    UseStageCache: Optional[bool] = None

class AwsApiGatewayEndpointConfigurationExtraOutputTypeDef(BaseValidatorModel):
    Types: Optional[List[str]] = None

class AwsApiGatewayEndpointConfigurationOutputTypeDef(BaseValidatorModel):
    Types: Optional[List[str]] = None

class AwsApiGatewayEndpointConfigurationTypeDef(BaseValidatorModel):
    Types: Optional[Sequence[str]] = None

class AwsApiGatewayMethodSettingsTypeDef(BaseValidatorModel):
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

class AwsCorsConfigurationExtraOutputTypeDef(BaseValidatorModel):
    AllowOrigins: Optional[List[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[List[str]] = None
    AllowHeaders: Optional[List[str]] = None

class AwsCorsConfigurationOutputTypeDef(BaseValidatorModel):
    AllowOrigins: Optional[List[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[List[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[List[str]] = None
    AllowHeaders: Optional[List[str]] = None

class AwsCorsConfigurationTypeDef(BaseValidatorModel):
    AllowOrigins: Optional[Sequence[str]] = None
    AllowCredentials: Optional[bool] = None
    ExposeHeaders: Optional[Sequence[str]] = None
    MaxAge: Optional[int] = None
    AllowMethods: Optional[Sequence[str]] = None
    AllowHeaders: Optional[Sequence[str]] = None

class AwsApiGatewayV2RouteSettingsTypeDef(BaseValidatorModel):
    DetailedMetricsEnabled: Optional[bool] = None
    LoggingLevel: Optional[str] = None
    DataTraceEnabled: Optional[bool] = None
    ThrottlingBurstLimit: Optional[int] = None
    ThrottlingRateLimit: Optional[float] = None

class AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef(BaseValidatorModel):
    AuthorizerResultTtlInSeconds: Optional[int] = None
    AuthorizerUri: Optional[str] = None
    IdentityValidationExpression: Optional[str] = None

class AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef(BaseValidatorModel):
    AuthTtL: Optional[int] = None
    ClientId: Optional[str] = None
    IatTtL: Optional[int] = None
    Issuer: Optional[str] = None

class AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef(BaseValidatorModel):
    AppIdClientRegex: Optional[str] = None
    AwsRegion: Optional[str] = None
    DefaultAction: Optional[str] = None
    UserPoolId: Optional[str] = None

class AwsAppSyncGraphQlApiLogConfigDetailsTypeDef(BaseValidatorModel):
    CloudWatchLogsRoleArn: Optional[str] = None
    ExcludeVerboseContent: Optional[bool] = None
    FieldLogLevel: Optional[str] = None

class AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef(BaseValidatorModel):
    EncryptionOption: Optional[str] = None
    KmsKey: Optional[str] = None

class AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef(BaseValidatorModel):
    OnDemandAllocationStrategy: Optional[str] = None
    OnDemandBaseCapacity: Optional[int] = None
    OnDemandPercentageAboveBaseCapacity: Optional[int] = None
    SpotAllocationStrategy: Optional[str] = None
    SpotInstancePools: Optional[int] = None
    SpotMaxPrice: Optional[str] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef(BaseValidatorModel):
    InstanceType: Optional[str] = None
    WeightedCapacity: Optional[str] = None

class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None

class AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpTokens: Optional[str] = None

class AwsBackupBackupPlanAdvancedBackupSettingsDetailsExtraOutputTypeDef(BaseValidatorModel):
    BackupOptions: Optional[Dict[str, str]] = None
    ResourceType: Optional[str] = None

class AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef(BaseValidatorModel):
    BackupOptions: Optional[Dict[str, str]] = None
    ResourceType: Optional[str] = None

class AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef(BaseValidatorModel):
    BackupOptions: Optional[Mapping[str, str]] = None
    ResourceType: Optional[str] = None

class AwsBackupBackupPlanLifecycleDetailsTypeDef(BaseValidatorModel):
    DeleteAfterDays: Optional[int] = None
    MoveToColdStorageAfterDays: Optional[int] = None

class AwsBackupBackupVaultNotificationsDetailsExtraOutputTypeDef(BaseValidatorModel):
    BackupVaultEvents: Optional[List[str]] = None
    SnsTopicArn: Optional[str] = None

class AwsBackupBackupVaultNotificationsDetailsOutputTypeDef(BaseValidatorModel):
    BackupVaultEvents: Optional[List[str]] = None
    SnsTopicArn: Optional[str] = None

class AwsBackupBackupVaultNotificationsDetailsTypeDef(BaseValidatorModel):
    BackupVaultEvents: Optional[Sequence[str]] = None
    SnsTopicArn: Optional[str] = None

class AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef(BaseValidatorModel):
    DeleteAt: Optional[str] = None
    MoveToColdStorageAt: Optional[str] = None

class AwsBackupRecoveryPointCreatedByDetailsTypeDef(BaseValidatorModel):
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    BackupPlanVersion: Optional[str] = None
    BackupRuleId: Optional[str] = None

class AwsBackupRecoveryPointLifecycleDetailsTypeDef(BaseValidatorModel):
    DeleteAfterDays: Optional[int] = None
    MoveToColdStorageAfterDays: Optional[int] = None

class AwsCertificateManagerCertificateExtendedKeyUsageTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    OId: Optional[str] = None

class AwsCertificateManagerCertificateKeyUsageTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class AwsCertificateManagerCertificateOptionsTypeDef(BaseValidatorModel):
    CertificateTransparencyLoggingPreference: Optional[str] = None

class AwsCertificateManagerCertificateResourceRecordTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None

class AwsCloudFormationStackDriftInformationDetailsTypeDef(BaseValidatorModel):
    StackDriftStatus: Optional[str] = None

class AwsCloudFormationStackOutputsDetailsTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    OutputKey: Optional[str] = None
    OutputValue: Optional[str] = None

class AwsCloudFrontDistributionCacheBehaviorTypeDef(BaseValidatorModel):
    ViewerProtocolPolicy: Optional[str] = None

class AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef(BaseValidatorModel):
    ViewerProtocolPolicy: Optional[str] = None

class AwsCloudFrontDistributionLoggingTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Enabled: Optional[bool] = None
    IncludeCookies: Optional[bool] = None
    Prefix: Optional[str] = None

class AwsCloudFrontDistributionViewerCertificateTypeDef(BaseValidatorModel):
    AcmCertificateArn: Optional[str] = None
    Certificate: Optional[str] = None
    CertificateSource: Optional[str] = None
    CloudFrontDefaultCertificate: Optional[bool] = None
    IamCertificateId: Optional[str] = None
    MinimumProtocolVersion: Optional[str] = None
    SslSupportMethod: Optional[str] = None

class AwsCloudFrontDistributionOriginSslProtocolsExtraOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[str]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[str]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginSslProtocolsTypeDef(BaseValidatorModel):
    Items: Optional[Sequence[str]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesExtraOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[int]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[int]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef(BaseValidatorModel):
    Items: Optional[Sequence[int]] = None
    Quantity: Optional[int] = None

class AwsCloudFrontDistributionOriginS3OriginConfigTypeDef(BaseValidatorModel):
    OriginAccessIdentity: Optional[str] = None

class AwsCloudTrailTrailDetailsTypeDef(BaseValidatorModel):
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

class AwsCloudWatchAlarmDimensionsDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsCodeBuildProjectArtifactsDetailsTypeDef(BaseValidatorModel):
    ArtifactIdentifier: Optional[str] = None
    EncryptionDisabled: Optional[bool] = None
    Location: Optional[str] = None
    Name: Optional[str] = None
    NamespaceType: Optional[str] = None
    OverrideArtifactName: Optional[bool] = None
    Packaging: Optional[str] = None
    Path: Optional[str] = None
    Type: Optional[str] = None

class AwsCodeBuildProjectSourceTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Location: Optional[str] = None
    GitCloneDepth: Optional[int] = None
    InsecureSsl: Optional[bool] = None

class AwsCodeBuildProjectVpcConfigExtraOutputTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None
    Subnets: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class AwsCodeBuildProjectVpcConfigOutputTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None
    Subnets: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class AwsCodeBuildProjectVpcConfigTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None
    Subnets: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Value: Optional[str] = None

class AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef(BaseValidatorModel):
    Credential: Optional[str] = None
    CredentialProvider: Optional[str] = None

class AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Status: Optional[str] = None
    StreamName: Optional[str] = None

class AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef(BaseValidatorModel):
    EncryptionDisabled: Optional[bool] = None
    Location: Optional[str] = None
    Status: Optional[str] = None

class AwsDmsEndpointDetailsTypeDef(BaseValidatorModel):
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

class AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef(BaseValidatorModel):
    ReplicationSubnetGroupIdentifier: Optional[str] = None

class AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None

class AwsDmsReplicationTaskDetailsTypeDef(BaseValidatorModel):
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

class AwsDynamoDbTableAttributeDefinitionTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeType: Optional[str] = None

class AwsDynamoDbTableBillingModeSummaryTypeDef(BaseValidatorModel):
    BillingMode: Optional[str] = None
    LastUpdateToPayPerRequestDateTime: Optional[str] = None

class AwsDynamoDbTableKeySchemaTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    KeyType: Optional[str] = None

class AwsDynamoDbTableProvisionedThroughputTypeDef(BaseValidatorModel):
    LastDecreaseDateTime: Optional[str] = None
    LastIncreaseDateTime: Optional[str] = None
    NumberOfDecreasesToday: Optional[int] = None
    ReadCapacityUnits: Optional[int] = None
    WriteCapacityUnits: Optional[int] = None

class AwsDynamoDbTableRestoreSummaryTypeDef(BaseValidatorModel):
    SourceBackupArn: Optional[str] = None
    SourceTableArn: Optional[str] = None
    RestoreDateTime: Optional[str] = None
    RestoreInProgress: Optional[bool] = None

class AwsDynamoDbTableSseDescriptionTypeDef(BaseValidatorModel):
    InaccessibleEncryptionDateTime: Optional[str] = None
    Status: Optional[str] = None
    SseType: Optional[str] = None
    KmsMasterKeyArn: Optional[str] = None

class AwsDynamoDbTableStreamSpecificationTypeDef(BaseValidatorModel):
    StreamEnabled: Optional[bool] = None
    StreamViewType: Optional[str] = None

class AwsDynamoDbTableProjectionExtraOutputTypeDef(BaseValidatorModel):
    NonKeyAttributes: Optional[List[str]] = None
    ProjectionType: Optional[str] = None

class AwsDynamoDbTableProjectionOutputTypeDef(BaseValidatorModel):
    NonKeyAttributes: Optional[List[str]] = None
    ProjectionType: Optional[str] = None

class AwsDynamoDbTableProjectionTypeDef(BaseValidatorModel):
    NonKeyAttributes: Optional[Sequence[str]] = None
    ProjectionType: Optional[str] = None

class AwsDynamoDbTableProvisionedThroughputOverrideTypeDef(BaseValidatorModel):
    ReadCapacityUnits: Optional[int] = None

class AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None

class AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef(BaseValidatorModel):
    SamlProviderArn: Optional[str] = None
    SelfServiceSamlProviderArn: Optional[str] = None

class AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef(BaseValidatorModel):
    ClientRootCertificateChain: Optional[str] = None

class AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None

class AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None

class AwsEc2EipDetailsTypeDef(BaseValidatorModel):
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

class AwsEc2InstanceMetadataOptionsTypeDef(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpProtocolIpv6: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpTokens: Optional[str] = None
    InstanceMetadataTags: Optional[str] = None

class AwsEc2InstanceMonitoringDetailsTypeDef(BaseValidatorModel):
    State: Optional[str] = None

class AwsEc2InstanceNetworkInterfacesDetailsTypeDef(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None

class AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    Throughput: Optional[int] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None

class AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None

class AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None

class AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef(BaseValidatorModel):
    CpuCredits: Optional[str] = None

class AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Type: Optional[str] = None

class AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef(BaseValidatorModel):
    Configured: Optional[bool] = None

class AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None

class AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef(BaseValidatorModel):
    AutoRecovery: Optional[str] = None

class AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef(BaseValidatorModel):
    HttpEndpoint: Optional[str] = None
    HttpProtocolIpv6: Optional[str] = None
    HttpTokens: Optional[str] = None
    HttpPutResponseHopLimit: Optional[int] = None
    InstanceMetadataTags: Optional[str] = None

class AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsEc2LaunchTemplateDataPlacementDetailsTypeDef(BaseValidatorModel):
    Affinity: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    SpreadDomain: Optional[str] = None
    Tenancy: Optional[str] = None

class AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef(BaseValidatorModel):
    EnableResourceNameDnsAAAARecord: Optional[bool] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    HostnameType: Optional[str] = None

class AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef(BaseValidatorModel):
    BlockDurationMinutes: Optional[int] = None
    InstanceInterruptionBehavior: Optional[str] = None
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[str] = None
    ValidUntil: Optional[str] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef(BaseValidatorModel):
    Max: Optional[float] = None
    Min: Optional[float] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef(BaseValidatorModel):
    Max: Optional[float] = None
    Min: Optional[float] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef(BaseValidatorModel):
    Max: Optional[int] = None
    Min: Optional[int] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef(BaseValidatorModel):
    Ipv6Address: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef(BaseValidatorModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None

class AwsEc2NetworkAclAssociationTypeDef(BaseValidatorModel):
    NetworkAclAssociationId: Optional[str] = None
    NetworkAclId: Optional[str] = None
    SubnetId: Optional[str] = None

class IcmpTypeCodeTypeDef(BaseValidatorModel):
    Code: Optional[int] = None
    Type: Optional[int] = None

class PortRangeFromToTypeDef(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None

class AwsEc2NetworkInterfaceAttachmentTypeDef(BaseValidatorModel):
    AttachTime: Optional[str] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    Status: Optional[str] = None

class AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef(BaseValidatorModel):
    IpV6Address: Optional[str] = None

class AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef(BaseValidatorModel):
    PrivateIpAddress: Optional[str] = None
    PrivateDnsName: Optional[str] = None

class AwsEc2NetworkInterfaceSecurityGroupTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None

class PropagatingVgwSetDetailsTypeDef(BaseValidatorModel):
    GatewayId: Optional[str] = None

class RouteSetDetailsTypeDef(BaseValidatorModel):
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

class AwsEc2SecurityGroupIpRangeTypeDef(BaseValidatorModel):
    CidrIp: Optional[str] = None

class AwsEc2SecurityGroupIpv6RangeTypeDef(BaseValidatorModel):
    CidrIpv6: Optional[str] = None

class AwsEc2SecurityGroupPrefixListIdTypeDef(BaseValidatorModel):
    PrefixListId: Optional[str] = None

class AwsEc2SecurityGroupUserIdGroupPairTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None

class Ipv6CidrBlockAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    CidrBlockState: Optional[str] = None

class AwsEc2TransitGatewayDetailsExtraOutputTypeDef(BaseValidatorModel):
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

class AwsEc2TransitGatewayDetailsOutputTypeDef(BaseValidatorModel):
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

class AwsEc2TransitGatewayDetailsTypeDef(BaseValidatorModel):
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

class AwsEc2VolumeAttachmentTypeDef(BaseValidatorModel):
    AttachTime: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    InstanceId: Optional[str] = None
    Status: Optional[str] = None

class CidrBlockAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    CidrBlock: Optional[str] = None
    CidrBlockState: Optional[str] = None

class AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef(BaseValidatorModel):
    ServiceType: Optional[str] = None

class AwsEc2VpcPeeringConnectionStatusDetailsTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class VpcInfoCidrBlockSetDetailsTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None

class VpcInfoIpv6CidrBlockSetDetailsTypeDef(BaseValidatorModel):
    Ipv6CidrBlock: Optional[str] = None

class VpcInfoPeeringOptionsDetailsTypeDef(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None

class AwsEc2VpnConnectionRoutesDetailsTypeDef(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    State: Optional[str] = None

class AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef(BaseValidatorModel):
    AcceptedRouteCount: Optional[int] = None
    CertificateArn: Optional[str] = None
    LastStatusChange: Optional[str] = None
    OutsideIpAddress: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None

class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsExtraOutputTypeDef(BaseValidatorModel):
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

class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef(BaseValidatorModel):
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

class AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef(BaseValidatorModel):
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

class AwsEcrContainerImageDetailsExtraOutputTypeDef(BaseValidatorModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[List[str]] = None
    ImagePublishedAt: Optional[str] = None

class AwsEcrContainerImageDetailsOutputTypeDef(BaseValidatorModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[List[str]] = None
    ImagePublishedAt: Optional[str] = None

class AwsEcrContainerImageDetailsTypeDef(BaseValidatorModel):
    RegistryId: Optional[str] = None
    RepositoryName: Optional[str] = None
    Architecture: Optional[str] = None
    ImageDigest: Optional[str] = None
    ImageTags: Optional[Sequence[str]] = None
    ImagePublishedAt: Optional[str] = None

class AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef(BaseValidatorModel):
    ScanOnPush: Optional[bool] = None

class AwsEcrRepositoryLifecyclePolicyDetailsTypeDef(BaseValidatorModel):
    LifecyclePolicyText: Optional[str] = None
    RegistryId: Optional[str] = None

class AwsEcsClusterClusterSettingsDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef(BaseValidatorModel):
    CloudWatchEncryptionEnabled: Optional[bool] = None
    CloudWatchLogGroupName: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3EncryptionEnabled: Optional[bool] = None
    S3KeyPrefix: Optional[str] = None

class AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef(BaseValidatorModel):
    Base: Optional[int] = None
    CapacityProvider: Optional[str] = None
    Weight: Optional[int] = None

class AwsMountPointTypeDef(BaseValidatorModel):
    SourceVolume: Optional[str] = None
    ContainerPath: Optional[str] = None

class AwsEcsServiceCapacityProviderStrategyDetailsTypeDef(BaseValidatorModel):
    Base: Optional[int] = None
    CapacityProvider: Optional[str] = None
    Weight: Optional[int] = None

class AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef(BaseValidatorModel):
    Enable: Optional[bool] = None
    Rollback: Optional[bool] = None

class AwsEcsServiceDeploymentControllerDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class AwsEcsServiceLoadBalancersDetailsTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerPort: Optional[int] = None
    LoadBalancerName: Optional[str] = None
    TargetGroupArn: Optional[str] = None

class AwsEcsServicePlacementConstraintsDetailsTypeDef(BaseValidatorModel):
    Expression: Optional[str] = None
    Type: Optional[str] = None

class AwsEcsServicePlacementStrategiesDetailsTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    Type: Optional[str] = None

class AwsEcsServiceServiceRegistriesDetailsTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ContainerPort: Optional[int] = None
    Port: Optional[int] = None
    RegistryArn: Optional[str] = None

class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None

class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    Subnets: Optional[List[str]] = None

class AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef(BaseValidatorModel):
    AssignPublicIp: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    Subnets: Optional[Sequence[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef(BaseValidatorModel):
    Condition: Optional[str] = None
    ContainerName: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef(BaseValidatorModel):
    Hostname: Optional[str] = None
    IpAddress: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    Options: Optional[Dict[str, str]] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsExtraOutputTypeDef(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    ReadOnly: Optional[bool] = None
    SourceVolume: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef(BaseValidatorModel):
    ContainerPort: Optional[int] = None
    HostPort: Optional[int] = None
    Protocol: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef(BaseValidatorModel):
    CredentialsParameter: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ValueFrom: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef(BaseValidatorModel):
    HardLimit: Optional[int] = None
    Name: Optional[str] = None
    SoftLimit: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef(BaseValidatorModel):
    ReadOnly: Optional[bool] = None
    SourceContainer: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    Options: Optional[Dict[str, str]] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef(BaseValidatorModel):
    Options: Optional[Mapping[str, str]] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef(BaseValidatorModel):
    Command: Optional[Sequence[str]] = None
    Interval: Optional[int] = None
    Retries: Optional[int] = None
    StartPeriod: Optional[int] = None
    Timeout: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsExtraOutputTypeDef(BaseValidatorModel):
    Add: Optional[List[str]] = None
    Drop: Optional[List[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef(BaseValidatorModel):
    Add: Optional[List[str]] = None
    Drop: Optional[List[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef(BaseValidatorModel):
    Add: Optional[Sequence[str]] = None
    Drop: Optional[Sequence[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsExtraOutputTypeDef(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[List[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsExtraOutputTypeDef(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[List[str]] = None
    Size: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[List[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[List[str]] = None
    Size: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    HostPath: Optional[str] = None
    Permissions: Optional[Sequence[str]] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef(BaseValidatorModel):
    ContainerPath: Optional[str] = None
    MountOptions: Optional[Sequence[str]] = None
    Size: Optional[int] = None

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ValueFrom: Optional[str] = None

class AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    DeviceType: Optional[str] = None

class AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef(BaseValidatorModel):
    Expression: Optional[str] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Dict[str, str]] = None
    Labels: Optional[Dict[str, str]] = None
    Scope: Optional[str] = None

class AwsEcsTaskDefinitionVolumesHostDetailsTypeDef(BaseValidatorModel):
    SourcePath: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Dict[str, str]] = None
    Labels: Optional[Dict[str, str]] = None
    Scope: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef(BaseValidatorModel):
    Autoprovision: Optional[bool] = None
    Driver: Optional[str] = None
    DriverOpts: Optional[Mapping[str, str]] = None
    Labels: Optional[Mapping[str, str]] = None
    Scope: Optional[str] = None

class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Iam: Optional[str] = None

class AwsEcsTaskVolumeHostDetailsTypeDef(BaseValidatorModel):
    SourcePath: Optional[str] = None

class AwsEfsAccessPointPosixUserDetailsExtraOutputTypeDef(BaseValidatorModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[List[str]] = None
    Uid: Optional[str] = None

class AwsEfsAccessPointPosixUserDetailsOutputTypeDef(BaseValidatorModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[List[str]] = None
    Uid: Optional[str] = None

class AwsEfsAccessPointPosixUserDetailsTypeDef(BaseValidatorModel):
    Gid: Optional[str] = None
    SecondaryGids: Optional[Sequence[str]] = None
    Uid: Optional[str] = None

class AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef(BaseValidatorModel):
    OwnerGid: Optional[str] = None
    OwnerUid: Optional[str] = None
    Permissions: Optional[str] = None

class AwsEksClusterResourcesVpcConfigDetailsExtraOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    EndpointPublicAccess: Optional[bool] = None

class AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    EndpointPublicAccess: Optional[bool] = None

class AwsEksClusterResourcesVpcConfigDetailsTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    EndpointPublicAccess: Optional[bool] = None

class AwsEksClusterLoggingClusterLoggingDetailsExtraOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Types: Optional[List[str]] = None

class AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Types: Optional[List[str]] = None

class AwsEksClusterLoggingClusterLoggingDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Types: Optional[Sequence[str]] = None

class AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef(BaseValidatorModel):
    EnvironmentName: Optional[str] = None
    LinkName: Optional[str] = None

class AwsElasticBeanstalkEnvironmentOptionSettingTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    OptionName: Optional[str] = None
    ResourceName: Optional[str] = None
    Value: Optional[str] = None

class AwsElasticBeanstalkEnvironmentTierTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional[str] = None
    Version: Optional[str] = None

class AwsElasticsearchDomainDomainEndpointOptionsTypeDef(BaseValidatorModel):
    EnforceHTTPS: Optional[bool] = None
    TLSSecurityPolicy: Optional[str] = None

class AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None

class AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsElasticsearchDomainServiceSoftwareOptionsTypeDef(BaseValidatorModel):
    AutomatedUpdateDate: Optional[str] = None
    Cancellable: Optional[bool] = None
    CurrentVersion: Optional[str] = None
    Description: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    UpdateStatus: Optional[str] = None

class AwsElasticsearchDomainVPCOptionsExtraOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VPCId: Optional[str] = None

class AwsElasticsearchDomainVPCOptionsOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VPCId: Optional[str] = None

class AwsElasticsearchDomainVPCOptionsTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VPCId: Optional[str] = None

class AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None

class AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None

class AwsElbAppCookieStickinessPolicyTypeDef(BaseValidatorModel):
    CookieName: Optional[str] = None
    PolicyName: Optional[str] = None

class AwsElbLbCookieStickinessPolicyTypeDef(BaseValidatorModel):
    CookieExpirationPeriod: Optional[int] = None
    PolicyName: Optional[str] = None

class AwsElbLoadBalancerAccessLogTypeDef(BaseValidatorModel):
    EmitInterval: Optional[int] = None
    Enabled: Optional[bool] = None
    S3BucketName: Optional[str] = None
    S3BucketPrefix: Optional[str] = None

class AwsElbLoadBalancerAdditionalAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AwsElbLoadBalancerConnectionDrainingTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    Timeout: Optional[int] = None

class AwsElbLoadBalancerConnectionSettingsTypeDef(BaseValidatorModel):
    IdleTimeout: Optional[int] = None

class AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsElbLoadBalancerBackendServerDescriptionExtraOutputTypeDef(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None

class AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[List[str]] = None

class AwsElbLoadBalancerBackendServerDescriptionTypeDef(BaseValidatorModel):
    InstancePort: Optional[int] = None
    PolicyNames: Optional[Sequence[str]] = None

class AwsElbLoadBalancerHealthCheckTypeDef(BaseValidatorModel):
    HealthyThreshold: Optional[int] = None
    Interval: Optional[int] = None
    Target: Optional[str] = None
    Timeout: Optional[int] = None
    UnhealthyThreshold: Optional[int] = None

class AwsElbLoadBalancerInstanceTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None

class AwsElbLoadBalancerSourceSecurityGroupTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    OwnerAlias: Optional[str] = None

class AwsElbLoadBalancerListenerTypeDef(BaseValidatorModel):
    InstancePort: Optional[int] = None
    InstanceProtocol: Optional[str] = None
    LoadBalancerPort: Optional[int] = None
    Protocol: Optional[str] = None
    SslCertificateId: Optional[str] = None

class AwsElbv2LoadBalancerAttributeTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class LoadBalancerStateTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None

class AwsEventSchemasRegistryDetailsTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    RegistryArn: Optional[str] = None
    RegistryName: Optional[str] = None

class AwsEventsEndpointEventBusesDetailsTypeDef(BaseValidatorModel):
    EventBusArn: Optional[str] = None

class AwsEventsEndpointReplicationConfigDetailsTypeDef(BaseValidatorModel):
    State: Optional[str] = None

class AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef(BaseValidatorModel):
    HealthCheck: Optional[str] = None

class AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef(BaseValidatorModel):
    Route: Optional[str] = None

class AwsEventsEventbusDetailsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Policy: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef(BaseValidatorModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef(BaseValidatorModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef(BaseValidatorModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef(BaseValidatorModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef(BaseValidatorModel):
    Status: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef(BaseValidatorModel):
    Reason: Optional[str] = None
    Status: Optional[str] = None

class AwsGuardDutyDetectorFeaturesDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None

class AwsIamAccessKeySessionContextAttributesTypeDef(BaseValidatorModel):
    MfaAuthenticated: Optional[bool] = None
    CreationDate: Optional[str] = None

class AwsIamAccessKeySessionContextSessionIssuerTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    PrincipalId: Optional[str] = None
    Arn: Optional[str] = None
    AccountId: Optional[str] = None
    UserName: Optional[str] = None

class AwsIamAttachedManagedPolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    PolicyArn: Optional[str] = None

class AwsIamGroupPolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None

class AwsIamInstanceProfileRoleTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AssumeRolePolicyDocument: Optional[str] = None
    CreateDate: Optional[str] = None
    Path: Optional[str] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None

class AwsIamPermissionsBoundaryTypeDef(BaseValidatorModel):
    PermissionsBoundaryArn: Optional[str] = None
    PermissionsBoundaryType: Optional[str] = None

class AwsIamPolicyVersionTypeDef(BaseValidatorModel):
    VersionId: Optional[str] = None
    IsDefaultVersion: Optional[bool] = None
    CreateDate: Optional[str] = None

class AwsIamRolePolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None

class AwsIamUserPolicyTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None

class AwsKinesisStreamStreamEncryptionDetailsTypeDef(BaseValidatorModel):
    EncryptionType: Optional[str] = None
    KeyId: Optional[str] = None

class AwsKmsKeyDetailsTypeDef(BaseValidatorModel):
    AWSAccountId: Optional[str] = None
    CreationDate: Optional[float] = None
    KeyId: Optional[str] = None
    KeyManager: Optional[str] = None
    KeyState: Optional[str] = None
    Origin: Optional[str] = None
    Description: Optional[str] = None
    KeyRotationStatus: Optional[bool] = None

class AwsLambdaFunctionCodeTypeDef(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None
    S3ObjectVersion: Optional[str] = None
    ZipFile: Optional[str] = None

class AwsLambdaFunctionDeadLetterConfigTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None

class AwsLambdaFunctionLayerTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CodeSize: Optional[int] = None

class AwsLambdaFunctionTracingConfigTypeDef(BaseValidatorModel):
    Mode: Optional[str] = None

class AwsLambdaFunctionVpcConfigExtraOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None

class AwsLambdaFunctionVpcConfigOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    VpcId: Optional[str] = None

class AwsLambdaFunctionVpcConfigTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None

class AwsLambdaFunctionEnvironmentErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    Message: Optional[str] = None

class AwsLambdaLayerVersionDetailsExtraOutputTypeDef(BaseValidatorModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[List[str]] = None
    CreatedDate: Optional[str] = None

class AwsLambdaLayerVersionDetailsOutputTypeDef(BaseValidatorModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[List[str]] = None
    CreatedDate: Optional[str] = None

class AwsLambdaLayerVersionDetailsTypeDef(BaseValidatorModel):
    Version: Optional[int] = None
    CompatibleRuntimes: Optional[Sequence[str]] = None
    CreatedDate: Optional[str] = None

class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsExtraOutputTypeDef(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[List[str]] = None
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef(BaseValidatorModel):
    CertificateAuthorityArnList: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef(BaseValidatorModel):
    DataVolumeKMSKeyId: Optional[str] = None

class AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef(BaseValidatorModel):
    InCluster: Optional[bool] = None
    ClientBroker: Optional[str] = None

class AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None

class AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef(BaseValidatorModel):
    MasterUserArn: Optional[str] = None
    MasterUserName: Optional[str] = None
    MasterUserPassword: Optional[str] = None

class AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef(BaseValidatorModel):
    AvailabilityZoneCount: Optional[int] = None

class AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef(BaseValidatorModel):
    CustomEndpointCertificateArn: Optional[str] = None
    CustomEndpointEnabled: Optional[bool] = None
    EnforceHTTPS: Optional[bool] = None
    CustomEndpoint: Optional[str] = None
    TLSSecurityPolicy: Optional[str] = None

class AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None

class AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef(BaseValidatorModel):
    AutomatedUpdateDate: Optional[str] = None
    Cancellable: Optional[bool] = None
    CurrentVersion: Optional[str] = None
    Description: Optional[str] = None
    NewVersion: Optional[str] = None
    UpdateAvailable: Optional[bool] = None
    UpdateStatus: Optional[str] = None
    OptionalDeployment: Optional[bool] = None

class AwsOpenSearchServiceDomainVpcOptionsDetailsExtraOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None

class AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None

class AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None

class AwsOpenSearchServiceDomainLogPublishingOptionTypeDef(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    Enabled: Optional[bool] = None

class AwsRdsDbClusterAssociatedRoleTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbClusterMemberTypeDef(BaseValidatorModel):
    IsClusterWriter: Optional[bool] = None
    PromotionTier: Optional[int] = None
    DbInstanceIdentifier: Optional[str] = None
    DbClusterParameterGroupStatus: Optional[str] = None

class AwsRdsDbClusterOptionGroupMembershipTypeDef(BaseValidatorModel):
    DbClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbDomainMembershipTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    Fqdn: Optional[str] = None
    IamRoleName: Optional[str] = None

class AwsRdsDbInstanceVpcSecurityGroupTypeDef(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeExtraOutputTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[Sequence[str]] = None

class AwsRdsDbInstanceAssociatedRoleTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    FeatureName: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbInstanceEndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None

class AwsRdsDbOptionGroupMembershipTypeDef(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbParameterGroupTypeDef(BaseValidatorModel):
    DbParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None

class AwsRdsDbProcessorFeatureTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsRdsDbStatusInfoTypeDef(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class AwsRdsPendingCloudWatchLogsExportsExtraOutputTypeDef(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None

class AwsRdsPendingCloudWatchLogsExportsOutputTypeDef(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None

class AwsRdsPendingCloudWatchLogsExportsTypeDef(BaseValidatorModel):
    LogTypesToEnable: Optional[Sequence[str]] = None
    LogTypesToDisable: Optional[Sequence[str]] = None

class AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef(BaseValidatorModel):
    Ec2SecurityGroupId: Optional[str] = None
    Ec2SecurityGroupName: Optional[str] = None
    Ec2SecurityGroupOwnerId: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbSecurityGroupIpRangeTypeDef(BaseValidatorModel):
    CidrIp: Optional[str] = None
    Status: Optional[str] = None

class AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class AwsRdsEventSubscriptionDetailsExtraOutputTypeDef(BaseValidatorModel):
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

class AwsRdsEventSubscriptionDetailsOutputTypeDef(BaseValidatorModel):
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

class AwsRdsEventSubscriptionDetailsTypeDef(BaseValidatorModel):
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

class AwsRedshiftClusterClusterNodeTypeDef(BaseValidatorModel):
    NodeRole: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PublicIpAddress: Optional[str] = None

class AwsRedshiftClusterClusterParameterStatusTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterApplyErrorDescription: Optional[str] = None

class AwsRedshiftClusterClusterSecurityGroupTypeDef(BaseValidatorModel):
    ClusterSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef(BaseValidatorModel):
    DestinationRegion: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    RetentionPeriod: Optional[int] = None
    SnapshotCopyGrantName: Optional[str] = None

class AwsRedshiftClusterDeferredMaintenanceWindowTypeDef(BaseValidatorModel):
    DeferMaintenanceEndTime: Optional[str] = None
    DeferMaintenanceIdentifier: Optional[str] = None
    DeferMaintenanceStartTime: Optional[str] = None

class AwsRedshiftClusterElasticIpStatusTypeDef(BaseValidatorModel):
    ElasticIp: Optional[str] = None
    Status: Optional[str] = None

class AwsRedshiftClusterEndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None

class AwsRedshiftClusterHsmStatusTypeDef(BaseValidatorModel):
    HsmClientCertificateIdentifier: Optional[str] = None
    HsmConfigurationIdentifier: Optional[str] = None
    Status: Optional[str] = None

class AwsRedshiftClusterIamRoleTypeDef(BaseValidatorModel):
    ApplyStatus: Optional[str] = None
    IamRoleArn: Optional[str] = None

class AwsRedshiftClusterLoggingStatusTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    LastFailureMessage: Optional[str] = None
    LastFailureTime: Optional[str] = None
    LastSuccessfulDeliveryTime: Optional[str] = None
    LoggingEnabled: Optional[bool] = None
    S3KeyPrefix: Optional[str] = None

class AwsRedshiftClusterPendingModifiedValuesTypeDef(BaseValidatorModel):
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

class AwsRedshiftClusterResizeInfoTypeDef(BaseValidatorModel):
    AllowCancelResize: Optional[bool] = None
    ResizeType: Optional[str] = None

class AwsRedshiftClusterRestoreStatusTypeDef(BaseValidatorModel):
    CurrentRestoreRateInMegaBytesPerSecond: Optional[float] = None
    ElapsedTimeInSeconds: Optional[int] = None
    EstimatedTimeToCompletionInSeconds: Optional[int] = None
    ProgressInMegaBytes: Optional[int] = None
    SnapshotSizeInMegaBytes: Optional[int] = None
    Status: Optional[str] = None

class AwsRedshiftClusterVpcSecurityGroupTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    VpcSecurityGroupId: Optional[str] = None

class AwsRoute53HostedZoneConfigDetailsTypeDef(BaseValidatorModel):
    Comment: Optional[str] = None

class AwsRoute53HostedZoneVpcDetailsTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Region: Optional[str] = None

class CloudWatchLogsLogGroupArnConfigDetailsTypeDef(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[str] = None
    HostedZoneId: Optional[str] = None
    Id: Optional[str] = None

class AwsS3AccessPointVpcConfigurationDetailsTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None

class AwsS3AccountPublicAccessBlockDetailsTypeDef(BaseValidatorModel):
    BlockPublicAcls: Optional[bool] = None
    BlockPublicPolicy: Optional[bool] = None
    IgnorePublicAcls: Optional[bool] = None
    RestrictPublicBuckets: Optional[bool] = None

class AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef(BaseValidatorModel):
    Days: Optional[int] = None
    StorageClass: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef(BaseValidatorModel):
    Date: Optional[str] = None
    Days: Optional[int] = None
    StorageClass: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AwsS3BucketBucketVersioningConfigurationTypeDef(BaseValidatorModel):
    IsMfaDeleteEnabled: Optional[bool] = None
    Status: Optional[str] = None

class AwsS3BucketLoggingConfigurationTypeDef(BaseValidatorModel):
    DestinationBucketName: Optional[str] = None
    LogFilePrefix: Optional[str] = None

class AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef(BaseValidatorModel):
    Name: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterRuleNameType] = None
    Value: Optional[str] = None

class AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef(BaseValidatorModel):
    Days: Optional[int] = None
    Mode: Optional[str] = None
    Years: Optional[int] = None

class AwsS3BucketServerSideEncryptionByDefaultTypeDef(BaseValidatorModel):
    SSEAlgorithm: Optional[str] = None
    KMSMasterKeyID: Optional[str] = None

class AwsS3BucketWebsiteConfigurationRedirectToTypeDef(BaseValidatorModel):
    Hostname: Optional[str] = None
    Protocol: Optional[str] = None

class AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef(BaseValidatorModel):
    HttpErrorCodeReturnedEquals: Optional[str] = None
    KeyPrefixEquals: Optional[str] = None

class AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef(BaseValidatorModel):
    Hostname: Optional[str] = None
    HttpRedirectCode: Optional[str] = None
    Protocol: Optional[str] = None
    ReplaceKeyPrefixWith: Optional[str] = None
    ReplaceKeyWith: Optional[str] = None

class AwsS3ObjectDetailsTypeDef(BaseValidatorModel):
    LastModified: Optional[str] = None
    ETag: Optional[str] = None
    VersionId: Optional[str] = None
    ContentType: Optional[str] = None
    ServerSideEncryption: Optional[str] = None
    SSEKMSKeyId: Optional[str] = None

class AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef(BaseValidatorModel):
    MinimumInstanceMetadataServiceVersion: Optional[str] = None

class AwsSecretsManagerSecretRotationRulesTypeDef(BaseValidatorModel):
    AutomaticallyAfterDays: Optional[int] = None

class GeneratorDetailsExtraOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[List[str]] = None

class MalwareTypeDef(BaseValidatorModel):
    Name: str
    Type: Optional[MalwareTypeType] = None
    Path: Optional[str] = None
    State: Optional[MalwareStateType] = None

class NoteTypeDef(BaseValidatorModel):
    Text: str
    UpdatedBy: str
    UpdatedAt: str

class PatchSummaryTypeDef(BaseValidatorModel):
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

class ProcessDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Path: Optional[str] = None
    Pid: Optional[int] = None
    ParentPid: Optional[int] = None
    LaunchedAt: Optional[str] = None
    TerminatedAt: Optional[str] = None

class SeverityTypeDef(BaseValidatorModel):
    Product: Optional[float] = None
    Label: Optional[SeverityLabelType] = None
    Normalized: Optional[int] = None
    Original: Optional[str] = None

class ThreatIntelIndicatorTypeDef(BaseValidatorModel):
    Type: Optional[ThreatIntelIndicatorTypeType] = None
    Value: Optional[str] = None
    Category: Optional[ThreatIntelIndicatorCategoryType] = None
    LastObservedAt: Optional[str] = None
    Source: Optional[str] = None
    SourceUrl: Optional[str] = None

class WorkflowTypeDef(BaseValidatorModel):
    Status: Optional[WorkflowStatusType] = None

class BooleanFilterTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None

class IpFilterTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None

class KeywordFilterTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class AwsSecurityFindingIdentifierTypeDef(BaseValidatorModel):
    Id: str
    ProductArn: str

class GeneratorDetailsOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[List[str]] = None

class GeneratorDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Labels: Optional[Sequence[str]] = None

class AwsSnsTopicSubscriptionTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None
    Protocol: Optional[str] = None

class AwsSqsQueueDetailsTypeDef(BaseValidatorModel):
    KmsDataKeyReusePeriodSeconds: Optional[int] = None
    KmsMasterKeyId: Optional[str] = None
    QueueName: Optional[str] = None
    DeadLetterTargetArn: Optional[str] = None

class AwsSsmComplianceSummaryTypeDef(BaseValidatorModel):
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

class AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef(BaseValidatorModel):
    LogGroupArn: Optional[str] = None

class AwsWafRateBasedRuleMatchPredicateTypeDef(BaseValidatorModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None

class AwsWafRegionalRateBasedRuleMatchPredicateTypeDef(BaseValidatorModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None

class AwsWafRegionalRulePredicateListDetailsTypeDef(BaseValidatorModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None

class AwsWafRegionalRuleGroupRulesActionDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class AwsWafRegionalWebAclRulesListActionDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class AwsWafRulePredicateListDetailsTypeDef(BaseValidatorModel):
    DataId: Optional[str] = None
    Negated: Optional[bool] = None
    Type: Optional[str] = None

class AwsWafRuleGroupRulesActionDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class WafActionTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class WafExcludedRuleTypeDef(BaseValidatorModel):
    RuleId: Optional[str] = None

class WafOverrideActionTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class AwsWafv2CustomHttpHeaderTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class AwsWafv2VisibilityConfigDetailsTypeDef(BaseValidatorModel):
    CloudWatchMetricsEnabled: Optional[bool] = None
    MetricName: Optional[str] = None
    SampledRequestsEnabled: Optional[bool] = None

class AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef(BaseValidatorModel):
    ImmunityTime: Optional[int] = None

class AwsXrayEncryptionConfigDetailsTypeDef(BaseValidatorModel):
    KeyId: Optional[str] = None
    Status: Optional[str] = None
    Type: Optional[str] = None

class BatchDeleteAutomationRulesRequestRequestTypeDef(BaseValidatorModel):
    AutomationRulesArns: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class UnprocessedAutomationRuleTypeDef(BaseValidatorModel):
    RuleArn: Optional[str] = None
    ErrorCode: Optional[int] = None
    ErrorMessage: Optional[str] = None

class BatchDisableStandardsRequestRequestTypeDef(BaseValidatorModel):
    StandardsSubscriptionArns: Sequence[str]

class StandardsSubscriptionRequestTypeDef(BaseValidatorModel):
    StandardsArn: str
    StandardsInput: Optional[Mapping[str, str]] = None

class BatchGetAutomationRulesRequestRequestTypeDef(BaseValidatorModel):
    AutomationRulesArns: Sequence[str]

class ConfigurationPolicyAssociationSummaryTypeDef(BaseValidatorModel):
    ConfigurationPolicyId: Optional[str] = None
    TargetId: Optional[str] = None
    TargetType: Optional[TargetTypeType] = None
    AssociationType: Optional[AssociationTypeType] = None
    UpdatedAt: Optional[datetime] = None
    AssociationStatus: Optional[ConfigurationPolicyAssociationStatusType] = None
    AssociationStatusMessage: Optional[str] = None

class BatchGetSecurityControlsRequestRequestTypeDef(BaseValidatorModel):
    SecurityControlIds: Sequence[str]

class UnprocessedSecurityControlTypeDef(BaseValidatorModel):
    SecurityControlId: str
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None

class StandardsControlAssociationIdTypeDef(BaseValidatorModel):
    SecurityControlId: str
    StandardsArn: str

class StandardsControlAssociationDetailTypeDef(BaseValidatorModel):
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

class ImportFindingsErrorTypeDef(BaseValidatorModel):
    Id: str
    ErrorCode: str
    ErrorMessage: str

class StandardsControlAssociationUpdateTypeDef(BaseValidatorModel):
    StandardsArn: str
    SecurityControlId: str
    AssociationStatus: AssociationStatusType
    UpdatedReason: Optional[str] = None

class BooleanConfigurationOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[bool] = None

class CellTypeDef(BaseValidatorModel):
    Column: Optional[int] = None
    Row: Optional[int] = None
    ColumnName: Optional[str] = None
    CellReference: Optional[str] = None

class ClassificationStatusTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Reason: Optional[str] = None

class CodeVulnerabilitiesFilePathTypeDef(BaseValidatorModel):
    EndLine: Optional[int] = None
    FileName: Optional[str] = None
    FilePath: Optional[str] = None
    StartLine: Optional[int] = None

class SecurityControlParameterExtraOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[List[str]] = None

class StatusReasonTypeDef(BaseValidatorModel):
    ReasonCode: str
    Description: Optional[str] = None

class SecurityControlParameterOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[List[str]] = None

class SecurityControlParameterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[Sequence[str]] = None

class DoubleConfigurationOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[float] = None
    Min: Optional[float] = None
    Max: Optional[float] = None

class EnumConfigurationOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[List[str]] = None

class EnumListConfigurationOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[List[str]] = None
    MaxItems: Optional[int] = None
    AllowedValues: Optional[List[str]] = None

class IntegerConfigurationOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[int] = None
    Min: Optional[int] = None
    Max: Optional[int] = None

class IntegerListConfigurationOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[List[int]] = None
    Min: Optional[int] = None
    Max: Optional[int] = None
    MaxItems: Optional[int] = None

class StringConfigurationOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    Re2Expression: Optional[str] = None
    ExpressionDescription: Optional[str] = None

class StringListConfigurationOptionsTypeDef(BaseValidatorModel):
    DefaultValue: Optional[List[str]] = None
    Re2Expression: Optional[str] = None
    MaxItems: Optional[int] = None
    ExpressionDescription: Optional[str] = None

class TargetTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    OrganizationalUnitId: Optional[str] = None
    RootId: Optional[str] = None

class ConfigurationPolicySummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    UpdatedAt: Optional[datetime] = None
    ServiceEnabled: Optional[bool] = None

class VolumeMountTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    MountPath: Optional[str] = None

class CreateActionTargetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    Id: str

class CreateFindingAggregatorRequestRequestTypeDef(BaseValidatorModel):
    RegionLinkingMode: str
    Regions: Optional[Sequence[str]] = None

class ResultTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    ProcessingResult: Optional[str] = None

class DateRangeTypeDef(BaseValidatorModel):
    Value: Optional[int] = None
    Unit: Optional[Literal["DAYS"]] = None

class DeclineInvitationsRequestRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]

class DeleteActionTargetRequestRequestTypeDef(BaseValidatorModel):
    ActionTargetArn: str

class DeleteConfigurationPolicyRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class DeleteFindingAggregatorRequestRequestTypeDef(BaseValidatorModel):
    FindingAggregatorArn: str

class DeleteInsightRequestRequestTypeDef(BaseValidatorModel):
    InsightArn: str

class DeleteInvitationsRequestRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]

class DeleteMembersRequestRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeActionTargetsRequestRequestTypeDef(BaseValidatorModel):
    ActionTargetArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeHubRequestRequestTypeDef(BaseValidatorModel):
    HubArn: Optional[str] = None

class OrganizationConfigurationTypeDef(BaseValidatorModel):
    ConfigurationType: Optional[OrganizationConfigurationConfigurationTypeType] = None
    Status: Optional[OrganizationConfigurationStatusType] = None
    StatusMessage: Optional[str] = None

class DescribeProductsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ProductArn: Optional[str] = None

class ProductTypeDef(BaseValidatorModel):
    ProductArn: str
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Description: Optional[str] = None
    Categories: Optional[List[str]] = None
    IntegrationTypes: Optional[List[IntegrationTypeType]] = None
    MarketplaceUrl: Optional[str] = None
    ActivationUrl: Optional[str] = None
    ProductSubscriptionResourcePolicy: Optional[str] = None

class DescribeStandardsControlsRequestRequestTypeDef(BaseValidatorModel):
    StandardsSubscriptionArn: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StandardsControlTypeDef(BaseValidatorModel):
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

class DescribeStandardsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DisableImportFindingsForProductRequestRequestTypeDef(BaseValidatorModel):
    ProductSubscriptionArn: str

class DisableOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    AdminAccountId: str

class DisassociateMembersRequestRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]

class EnableImportFindingsForProductRequestRequestTypeDef(BaseValidatorModel):
    ProductArn: str

class EnableOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    AdminAccountId: str

class EnableSecurityHubRequestRequestTypeDef(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    EnableDefaultStandards: Optional[bool] = None
    ControlFindingGenerator: Optional[ControlFindingGeneratorType] = None

class FilePathsTypeDef(BaseValidatorModel):
    FilePath: Optional[str] = None
    FileName: Optional[str] = None
    ResourceId: Optional[str] = None
    Hash: Optional[str] = None

class FindingAggregatorTypeDef(BaseValidatorModel):
    FindingAggregatorArn: Optional[str] = None

class FindingHistoryUpdateSourceTypeDef(BaseValidatorModel):
    Type: Optional[FindingHistoryUpdateSourceTypeType] = None
    Identity: Optional[str] = None

class FindingHistoryUpdateTypeDef(BaseValidatorModel):
    UpdatedField: Optional[str] = None
    OldValue: Optional[str] = None
    NewValue: Optional[str] = None

class FindingProviderSeverityTypeDef(BaseValidatorModel):
    Label: Optional[SeverityLabelType] = None
    Original: Optional[str] = None

class FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None

class FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef(BaseValidatorModel):
    Priority: Optional[int] = None
    ResourceArn: Optional[str] = None

class InvitationTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    InvitationId: Optional[str] = None
    InvitedAt: Optional[datetime] = None
    MemberStatus: Optional[str] = None

class GetConfigurationPolicyRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetEnabledStandardsRequestRequestTypeDef(BaseValidatorModel):
    StandardsSubscriptionArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetFindingAggregatorRequestRequestTypeDef(BaseValidatorModel):
    FindingAggregatorArn: str

class SortCriterionTypeDef(BaseValidatorModel):
    Field: Optional[str] = None
    SortOrder: Optional[SortOrderType] = None

class GetInsightResultsRequestRequestTypeDef(BaseValidatorModel):
    InsightArn: str

class GetInsightsRequestRequestTypeDef(BaseValidatorModel):
    InsightArns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetMembersRequestRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]

class MemberTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Email: Optional[str] = None
    MasterId: Optional[str] = None
    AdministratorId: Optional[str] = None
    MemberStatus: Optional[str] = None
    InvitedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None

class GetSecurityControlDefinitionRequestRequestTypeDef(BaseValidatorModel):
    SecurityControlId: str

class InsightResultValueTypeDef(BaseValidatorModel):
    GroupByAttributeValue: str
    Count: int

class InviteMembersRequestRequestTypeDef(BaseValidatorModel):
    AccountIds: Sequence[str]

class ListAutomationRulesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListConfigurationPoliciesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEnabledProductsForImportRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListFindingAggregatorsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInvitationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListMembersRequestRequestTypeDef(BaseValidatorModel):
    OnlyAssociated: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOrganizationAdminAccountsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSecurityControlDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListStandardsControlAssociationsRequestRequestTypeDef(BaseValidatorModel):
    SecurityControlId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StandardsControlAssociationSummaryTypeDef(BaseValidatorModel):
    StandardsArn: str
    SecurityControlId: str
    SecurityControlArn: str
    AssociationStatus: AssociationStatusType
    RelatedRequirements: Optional[List[str]] = None
    UpdatedAt: Optional[datetime] = None
    UpdatedReason: Optional[str] = None
    StandardsControlTitle: Optional[str] = None
    StandardsControlDescription: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class PortRangeTypeDef(BaseValidatorModel):
    Begin: Optional[int] = None
    End: Optional[int] = None

class RangeTypeDef(BaseValidatorModel):
    Start: Optional[int] = None
    End: Optional[int] = None
    StartColumn: Optional[int] = None

class RecordTypeDef(BaseValidatorModel):
    JsonPath: Optional[str] = None
    RecordIndex: Optional[int] = None

class ParameterValueOutputTypeDef(BaseValidatorModel):
    Integer: Optional[int] = None
    IntegerList: Optional[List[int]] = None
    Double: Optional[float] = None
    String: Optional[str] = None
    StringList: Optional[List[str]] = None
    Boolean: Optional[bool] = None
    Enum: Optional[str] = None
    EnumList: Optional[List[str]] = None

class ParameterValueTypeDef(BaseValidatorModel):
    Integer: Optional[int] = None
    IntegerList: Optional[Sequence[int]] = None
    Double: Optional[float] = None
    String: Optional[str] = None
    StringList: Optional[Sequence[str]] = None
    Boolean: Optional[bool] = None
    Enum: Optional[str] = None
    EnumList: Optional[Sequence[str]] = None

class RecommendationTypeDef(BaseValidatorModel):
    Text: Optional[str] = None
    Url: Optional[str] = None

class RuleGroupSourceListDetailsExtraOutputTypeDef(BaseValidatorModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[List[str]] = None
    Targets: Optional[List[str]] = None

class RuleGroupSourceListDetailsOutputTypeDef(BaseValidatorModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[List[str]] = None
    Targets: Optional[List[str]] = None

class RuleGroupSourceListDetailsTypeDef(BaseValidatorModel):
    GeneratedRulesType: Optional[str] = None
    TargetTypes: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[str]] = None

class RuleGroupSourceStatefulRulesHeaderDetailsTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None
    DestinationPort: Optional[str] = None
    Direction: Optional[str] = None
    Protocol: Optional[str] = None
    Source: Optional[str] = None
    SourcePort: Optional[str] = None

class RuleGroupSourceStatefulRulesOptionsDetailsExtraOutputTypeDef(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None

class RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None

class RuleGroupSourceStatefulRulesOptionsDetailsTypeDef(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[Sequence[str]] = None

class RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef(BaseValidatorModel):
    AddressDefinition: Optional[str] = None

class RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef(BaseValidatorModel):
    AddressDefinition: Optional[str] = None

class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsExtraOutputTypeDef(BaseValidatorModel):
    Flags: Optional[List[str]] = None
    Masks: Optional[List[str]] = None

class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef(BaseValidatorModel):
    Flags: Optional[List[str]] = None
    Masks: Optional[List[str]] = None

class RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef(BaseValidatorModel):
    Flags: Optional[Sequence[str]] = None
    Masks: Optional[Sequence[str]] = None

class RuleGroupVariablesIpSetsDetailsExtraOutputTypeDef(BaseValidatorModel):
    Definition: Optional[List[str]] = None

class RuleGroupVariablesPortSetsDetailsExtraOutputTypeDef(BaseValidatorModel):
    Definition: Optional[List[str]] = None

class RuleGroupVariablesIpSetsDetailsOutputTypeDef(BaseValidatorModel):
    Definition: Optional[List[str]] = None

class RuleGroupVariablesIpSetsDetailsTypeDef(BaseValidatorModel):
    Definition: Optional[Sequence[str]] = None

class RuleGroupVariablesPortSetsDetailsOutputTypeDef(BaseValidatorModel):
    Definition: Optional[List[str]] = None

class RuleGroupVariablesPortSetsDetailsTypeDef(BaseValidatorModel):
    Definition: Optional[Sequence[str]] = None

class SoftwarePackageTypeDef(BaseValidatorModel):
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

class StandardsManagedByTypeDef(BaseValidatorModel):
    Company: Optional[str] = None
    Product: Optional[str] = None

class StandardsStatusReasonTypeDef(BaseValidatorModel):
    StatusReasonCode: StatusReasonCodeType

class StatelessCustomPublishMetricActionDimensionTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateActionTargetRequestRequestTypeDef(BaseValidatorModel):
    ActionTargetArn: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateFindingAggregatorRequestRequestTypeDef(BaseValidatorModel):
    FindingAggregatorArn: str
    RegionLinkingMode: str
    Regions: Optional[Sequence[str]] = None

class UpdateSecurityHubConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AutoEnableControls: Optional[bool] = None
    ControlFindingGenerator: Optional[ControlFindingGeneratorType] = None

class UpdateStandardsControlRequestRequestTypeDef(BaseValidatorModel):
    StandardsControlArn: str
    ControlStatus: Optional[ControlStatusType] = None
    DisabledReason: Optional[str] = None

class VulnerabilityVendorTypeDef(BaseValidatorModel):
    Name: str
    Url: Optional[str] = None
    VendorSeverity: Optional[str] = None
    VendorCreatedAt: Optional[str] = None
    VendorUpdatedAt: Optional[str] = None

class CreateMembersRequestRequestTypeDef(BaseValidatorModel):
    AccountDetails: Sequence[AccountDetailsTypeDef]

class ActionRemoteIpDetailsTypeDef(BaseValidatorModel):
    IpAddressV4: Optional[str] = None
    Organization: Optional[IpOrganizationDetailsTypeDef] = None
    Country: Optional[CountryTypeDef] = None
    City: Optional[CityTypeDef] = None
    GeoLocation: Optional[GeoLocationTypeDef] = None

class CvssExtraOutputTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[List[AdjustmentTypeDef]] = None

class CvssOutputTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[List[AdjustmentTypeDef]] = None

class CvssTypeDef(BaseValidatorModel):
    Version: Optional[str] = None
    BaseScore: Optional[float] = None
    BaseVector: Optional[str] = None
    Source: Optional[str] = None
    Adjustments: Optional[Sequence[AdjustmentTypeDef]] = None

class ListConfigurationPolicyAssociationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[AssociationFiltersTypeDef] = None

class AssociationSetDetailsTypeDef(BaseValidatorModel):
    AssociationState: Optional[AssociationStateDetailsTypeDef] = None
    GatewayId: Optional[str] = None
    Main: Optional[bool] = None
    RouteTableAssociationId: Optional[str] = None
    RouteTableId: Optional[str] = None
    SubnetId: Optional[str] = None

class AutomationRulesFindingFieldsUpdateOutputTypeDef(BaseValidatorModel):
    Note: Optional[NoteUpdateTypeDef] = None
    Severity: Optional[SeverityUpdateTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[List[str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Workflow: Optional[WorkflowUpdateTypeDef] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None

class AutomationRulesFindingFieldsUpdateTypeDef(BaseValidatorModel):
    Note: Optional[NoteUpdateTypeDef] = None
    Severity: Optional[SeverityUpdateTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[Sequence[str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Workflow: Optional[WorkflowUpdateTypeDef] = None
    RelatedFindings: Optional[Sequence[RelatedFindingTypeDef]] = None

class AwsAmazonMqBrokerLogsDetailsTypeDef(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None
    AuditLogGroup: Optional[str] = None
    GeneralLogGroup: Optional[str] = None
    Pending: Optional[AwsAmazonMqBrokerLogsPendingDetailsTypeDef] = None

class AwsApiGatewayRestApiDetailsExtraOutputTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[List[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationExtraOutputTypeDef] = None

class AwsApiGatewayRestApiDetailsOutputTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[List[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationOutputTypeDef] = None

class AwsApiGatewayRestApiDetailsTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedDate: Optional[str] = None
    Version: Optional[str] = None
    BinaryMediaTypes: Optional[Sequence[str]] = None
    MinimumCompressionSize: Optional[int] = None
    ApiKeySource: Optional[str] = None
    EndpointConfiguration: Optional[AwsApiGatewayEndpointConfigurationTypeDef] = None

class AwsApiGatewayStageDetailsExtraOutputTypeDef(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[List[AwsApiGatewayMethodSettingsTypeDef]] = None
    Variables: Optional[Dict[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsExtraOutputTypeDef] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None

class AwsApiGatewayStageDetailsOutputTypeDef(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[List[AwsApiGatewayMethodSettingsTypeDef]] = None
    Variables: Optional[Dict[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsOutputTypeDef] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None

class AwsApiGatewayStageDetailsTypeDef(BaseValidatorModel):
    DeploymentId: Optional[str] = None
    ClientCertificateId: Optional[str] = None
    StageName: Optional[str] = None
    Description: Optional[str] = None
    CacheClusterEnabled: Optional[bool] = None
    CacheClusterSize: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    MethodSettings: Optional[Sequence[AwsApiGatewayMethodSettingsTypeDef]] = None
    Variables: Optional[Mapping[str, str]] = None
    DocumentationVersion: Optional[str] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    CanarySettings: Optional[AwsApiGatewayCanarySettingsTypeDef] = None
    TracingEnabled: Optional[bool] = None
    CreatedDate: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    WebAclArn: Optional[str] = None

class AwsApiGatewayV2ApiDetailsExtraOutputTypeDef(BaseValidatorModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationExtraOutputTypeDef] = None

class AwsApiGatewayV2ApiDetailsOutputTypeDef(BaseValidatorModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationOutputTypeDef] = None

class AwsApiGatewayV2ApiDetailsTypeDef(BaseValidatorModel):
    ApiEndpoint: Optional[str] = None
    ApiId: Optional[str] = None
    ApiKeySelectionExpression: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    Version: Optional[str] = None
    Name: Optional[str] = None
    ProtocolType: Optional[str] = None
    RouteSelectionExpression: Optional[str] = None
    CorsConfiguration: Optional[AwsCorsConfigurationTypeDef] = None

class AwsApiGatewayV2StageDetailsExtraOutputTypeDef(BaseValidatorModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Dict[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None

class AwsApiGatewayV2StageDetailsOutputTypeDef(BaseValidatorModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Dict[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None

class AwsApiGatewayV2StageDetailsTypeDef(BaseValidatorModel):
    ClientCertificateId: Optional[str] = None
    CreatedDate: Optional[str] = None
    Description: Optional[str] = None
    DefaultRouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    DeploymentId: Optional[str] = None
    LastUpdatedDate: Optional[str] = None
    RouteSettings: Optional[AwsApiGatewayV2RouteSettingsTypeDef] = None
    StageName: Optional[str] = None
    StageVariables: Optional[Mapping[str, str]] = None
    AccessLogSettings: Optional[AwsApiGatewayAccessLogSettingsTypeDef] = None
    AutoDeploy: Optional[bool] = None
    LastDeploymentStatusMessage: Optional[str] = None
    ApiGatewayManaged: Optional[bool] = None

class AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef(BaseValidatorModel):
    AuthenticationType: Optional[str] = None
    LambdaAuthorizerConfig: Optional[       AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef     ] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef] = None

class AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef(BaseValidatorModel):
    EncryptionConfiguration: Optional[       AwsAthenaWorkGroupConfigurationResultConfigurationEncryptionConfigurationDetailsTypeDef     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsExtraOutputTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    Overrides: Optional[       List[         AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef       ]     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    Overrides: Optional[       List[         AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef       ]     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    Overrides: Optional[       Sequence[         AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetailsTypeDef       ]     ] = None

class AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsEbsDetailsTypeDef] = None
    NoDevice: Optional[bool] = None
    VirtualName: Optional[str] = None

class AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef(BaseValidatorModel):
    DestinationBackupVaultArn: Optional[str] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsTypeDef] = None

class AwsBackupBackupVaultDetailsExtraOutputTypeDef(BaseValidatorModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsExtraOutputTypeDef] = None
    AccessPolicy: Optional[str] = None

class AwsBackupBackupVaultDetailsOutputTypeDef(BaseValidatorModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsOutputTypeDef] = None
    AccessPolicy: Optional[str] = None

class AwsBackupBackupVaultDetailsTypeDef(BaseValidatorModel):
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    Notifications: Optional[AwsBackupBackupVaultNotificationsDetailsTypeDef] = None
    AccessPolicy: Optional[str] = None

class AwsBackupRecoveryPointDetailsTypeDef(BaseValidatorModel):
    BackupSizeInBytes: Optional[int] = None
    BackupVaultArn: Optional[str] = None
    BackupVaultName: Optional[str] = None
    CalculatedLifecycle: Optional[AwsBackupRecoveryPointCalculatedLifecycleDetailsTypeDef] = None
    CompletionDate: Optional[str] = None
    CreatedBy: Optional[AwsBackupRecoveryPointCreatedByDetailsTypeDef] = None
    CreationDate: Optional[str] = None
    EncryptionKeyArn: Optional[str] = None
    IamRoleArn: Optional[str] = None
    IsEncrypted: Optional[bool] = None
    LastRestoreTime: Optional[str] = None
    Lifecycle: Optional[AwsBackupRecoveryPointLifecycleDetailsTypeDef] = None
    RecoveryPointArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    SourceBackupVaultArn: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    StorageClass: Optional[str] = None

class AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecordTypeDef] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[List[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None

class AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecordTypeDef] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[List[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None

class AwsCertificateManagerCertificateDomainValidationOptionTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    ResourceRecord: Optional[AwsCertificateManagerCertificateResourceRecordTypeDef] = None
    ValidationDomain: Optional[str] = None
    ValidationEmails: Optional[Sequence[str]] = None
    ValidationMethod: Optional[str] = None
    ValidationStatus: Optional[str] = None

class AwsCloudFormationStackDetailsExtraOutputTypeDef(BaseValidatorModel):
    Capabilities: Optional[List[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetailsTypeDef] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    Outputs: Optional[List[AwsCloudFormationStackOutputsDetailsTypeDef]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None

class AwsCloudFormationStackDetailsOutputTypeDef(BaseValidatorModel):
    Capabilities: Optional[List[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetailsTypeDef] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[List[str]] = None
    Outputs: Optional[List[AwsCloudFormationStackOutputsDetailsTypeDef]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None

class AwsCloudFormationStackDetailsTypeDef(BaseValidatorModel):
    Capabilities: Optional[Sequence[str]] = None
    CreationTime: Optional[str] = None
    Description: Optional[str] = None
    DisableRollback: Optional[bool] = None
    DriftInformation: Optional[AwsCloudFormationStackDriftInformationDetailsTypeDef] = None
    EnableTerminationProtection: Optional[bool] = None
    LastUpdatedTime: Optional[str] = None
    NotificationArns: Optional[Sequence[str]] = None
    Outputs: Optional[Sequence[AwsCloudFormationStackOutputsDetailsTypeDef]] = None
    RoleArn: Optional[str] = None
    StackId: Optional[str] = None
    StackName: Optional[str] = None
    StackStatus: Optional[str] = None
    StackStatusReason: Optional[str] = None
    TimeoutInMinutes: Optional[int] = None

class AwsCloudFrontDistributionCacheBehaviorsExtraOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionCacheBehaviorTypeDef]] = None

class AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionCacheBehaviorTypeDef]] = None

class AwsCloudFrontDistributionCacheBehaviorsTypeDef(BaseValidatorModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionCacheBehaviorTypeDef]] = None

class AwsCloudFrontDistributionOriginCustomOriginConfigExtraOutputTypeDef(BaseValidatorModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[       AwsCloudFrontDistributionOriginSslProtocolsExtraOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef(BaseValidatorModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[AwsCloudFrontDistributionOriginSslProtocolsOutputTypeDef] = None

class AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef(BaseValidatorModel):
    HttpPort: Optional[int] = None
    HttpsPort: Optional[int] = None
    OriginKeepaliveTimeout: Optional[int] = None
    OriginProtocolPolicy: Optional[str] = None
    OriginReadTimeout: Optional[int] = None
    OriginSslProtocols: Optional[AwsCloudFrontDistributionOriginSslProtocolsTypeDef] = None

class AwsCloudFrontDistributionOriginGroupFailoverExtraOutputTypeDef(BaseValidatorModel):
    StatusCodes: Optional[       AwsCloudFrontDistributionOriginGroupFailoverStatusCodesExtraOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef(BaseValidatorModel):
    StatusCodes: Optional[       AwsCloudFrontDistributionOriginGroupFailoverStatusCodesOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginGroupFailoverTypeDef(BaseValidatorModel):
    StatusCodes: Optional[AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef] = None

class AwsCloudWatchAlarmDetailsExtraOutputTypeDef(BaseValidatorModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[List[AwsCloudWatchAlarmDimensionsDetailsTypeDef]] = None
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

class AwsCloudWatchAlarmDetailsOutputTypeDef(BaseValidatorModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[List[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[List[AwsCloudWatchAlarmDimensionsDetailsTypeDef]] = None
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

class AwsCloudWatchAlarmDetailsTypeDef(BaseValidatorModel):
    ActionsEnabled: Optional[bool] = None
    AlarmActions: Optional[Sequence[str]] = None
    AlarmArn: Optional[str] = None
    AlarmConfigurationUpdatedTimestamp: Optional[str] = None
    AlarmDescription: Optional[str] = None
    AlarmName: Optional[str] = None
    ComparisonOperator: Optional[str] = None
    DatapointsToAlarm: Optional[int] = None
    Dimensions: Optional[Sequence[AwsCloudWatchAlarmDimensionsDetailsTypeDef]] = None
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

class AwsCodeBuildProjectEnvironmentExtraOutputTypeDef(BaseValidatorModel):
    Certificate: Optional[str] = None
    EnvironmentVariables: Optional[       List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]     ] = None
    PrivilegedMode: Optional[bool] = None
    ImagePullCredentialsType: Optional[str] = None
    RegistryCredential: Optional[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef] = None
    Type: Optional[str] = None

class AwsCodeBuildProjectEnvironmentOutputTypeDef(BaseValidatorModel):
    Certificate: Optional[str] = None
    EnvironmentVariables: Optional[       List[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]     ] = None
    PrivilegedMode: Optional[bool] = None
    ImagePullCredentialsType: Optional[str] = None
    RegistryCredential: Optional[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef] = None
    Type: Optional[str] = None

class AwsCodeBuildProjectEnvironmentTypeDef(BaseValidatorModel):
    Certificate: Optional[str] = None
    EnvironmentVariables: Optional[       Sequence[AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetailsTypeDef]     ] = None
    PrivilegedMode: Optional[bool] = None
    ImagePullCredentialsType: Optional[str] = None
    RegistryCredential: Optional[AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef] = None
    Type: Optional[str] = None

class AwsCodeBuildProjectLogsConfigDetailsTypeDef(BaseValidatorModel):
    CloudWatchLogs: Optional[AwsCodeBuildProjectLogsConfigCloudWatchLogsDetailsTypeDef] = None
    S3Logs: Optional[AwsCodeBuildProjectLogsConfigS3LogsDetailsTypeDef] = None

class AwsDmsReplicationInstanceDetailsExtraOutputTypeDef(BaseValidatorModel):
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
    ReplicationSubnetGroup: Optional[       AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef     ] = None
    VpcSecurityGroups: Optional[       List[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]     ] = None

class AwsDmsReplicationInstanceDetailsOutputTypeDef(BaseValidatorModel):
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
    ReplicationSubnetGroup: Optional[       AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef     ] = None
    VpcSecurityGroups: Optional[       List[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]     ] = None

class AwsDmsReplicationInstanceDetailsTypeDef(BaseValidatorModel):
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
    ReplicationSubnetGroup: Optional[       AwsDmsReplicationInstanceReplicationSubnetGroupDetailsTypeDef     ] = None
    VpcSecurityGroups: Optional[       Sequence[AwsDmsReplicationInstanceVpcSecurityGroupsDetailsTypeDef]     ] = None

class AwsDynamoDbTableGlobalSecondaryIndexExtraOutputTypeDef(BaseValidatorModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionExtraOutputTypeDef] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None

class AwsDynamoDbTableLocalSecondaryIndexExtraOutputTypeDef(BaseValidatorModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionExtraOutputTypeDef] = None

class AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef(BaseValidatorModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionOutputTypeDef] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None

class AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef(BaseValidatorModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionOutputTypeDef] = None

class AwsDynamoDbTableGlobalSecondaryIndexTypeDef(BaseValidatorModel):
    Backfilling: Optional[bool] = None
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    IndexSizeBytes: Optional[int] = None
    IndexStatus: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionTypeDef] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None

class AwsDynamoDbTableLocalSecondaryIndexTypeDef(BaseValidatorModel):
    IndexArn: Optional[str] = None
    IndexName: Optional[str] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchemaTypeDef]] = None
    Projection: Optional[AwsDynamoDbTableProjectionTypeDef] = None

class AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedThroughputOverride: Optional[       AwsDynamoDbTableProvisionedThroughputOverrideTypeDef     ] = None

class AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    ActiveDirectory: Optional[       AwsEc2ClientVpnEndpointAuthenticationOptionsActiveDirectoryDetailsTypeDef     ] = None
    MutualAuthentication: Optional[       AwsEc2ClientVpnEndpointAuthenticationOptionsMutualAuthenticationDetailsTypeDef     ] = None
    FederatedAuthentication: Optional[       AwsEc2ClientVpnEndpointAuthenticationOptionsFederatedAuthenticationDetailsTypeDef     ] = None

class AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None
    Status: Optional[AwsEc2ClientVpnEndpointClientConnectOptionsStatusDetailsTypeDef] = None

class AwsEc2InstanceDetailsExtraOutputTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    ImageId: Optional[str] = None
    IpV4Addresses: Optional[List[str]] = None
    IpV6Addresses: Optional[List[str]] = None
    KeyName: Optional[str] = None
    IamInstanceProfileArn: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    LaunchedAt: Optional[str] = None
    NetworkInterfaces: Optional[List[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]] = None
    VirtualizationType: Optional[str] = None
    MetadataOptions: Optional[AwsEc2InstanceMetadataOptionsTypeDef] = None
    Monitoring: Optional[AwsEc2InstanceMonitoringDetailsTypeDef] = None

class AwsEc2InstanceDetailsOutputTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    ImageId: Optional[str] = None
    IpV4Addresses: Optional[List[str]] = None
    IpV6Addresses: Optional[List[str]] = None
    KeyName: Optional[str] = None
    IamInstanceProfileArn: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    LaunchedAt: Optional[str] = None
    NetworkInterfaces: Optional[List[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]] = None
    VirtualizationType: Optional[str] = None
    MetadataOptions: Optional[AwsEc2InstanceMetadataOptionsTypeDef] = None
    Monitoring: Optional[AwsEc2InstanceMonitoringDetailsTypeDef] = None

class AwsEc2InstanceDetailsTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    ImageId: Optional[str] = None
    IpV4Addresses: Optional[Sequence[str]] = None
    IpV6Addresses: Optional[Sequence[str]] = None
    KeyName: Optional[str] = None
    IamInstanceProfileArn: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    LaunchedAt: Optional[str] = None
    NetworkInterfaces: Optional[Sequence[AwsEc2InstanceNetworkInterfacesDetailsTypeDef]] = None
    VirtualizationType: Optional[str] = None
    MetadataOptions: Optional[AwsEc2InstanceMetadataOptionsTypeDef] = None
    Monitoring: Optional[AwsEc2InstanceMonitoringDetailsTypeDef] = None

class AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[AwsEc2LaunchTemplateDataBlockDeviceMappingSetEbsDetailsTypeDef] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None

class AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef(BaseValidatorModel):
    CapacityReservationPreference: Optional[str] = None
    CapacityReservationTarget: Optional[       AwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef(BaseValidatorModel):
    MarketType: Optional[str] = None
    SpotOptions: Optional[       AwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsExtraOutputTypeDef(BaseValidatorModel):
    AcceleratorCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef     ] = None
    AcceleratorManufacturers: Optional[List[str]] = None
    AcceleratorNames: Optional[List[str]] = None
    AcceleratorTotalMemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef     ] = None
    AcceleratorTypes: Optional[List[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef     ] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[List[str]] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[List[str]] = None
    MemoryGiBPerVCpu: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef     ] = None
    MemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef     ] = None
    NetworkInterfaceCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef     ] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef     ] = None
    VCpuCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef(BaseValidatorModel):
    AcceleratorCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef     ] = None
    AcceleratorManufacturers: Optional[List[str]] = None
    AcceleratorNames: Optional[List[str]] = None
    AcceleratorTotalMemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef     ] = None
    AcceleratorTypes: Optional[List[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef     ] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[List[str]] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[List[str]] = None
    MemoryGiBPerVCpu: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef     ] = None
    MemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef     ] = None
    NetworkInterfaceCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef     ] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef     ] = None
    VCpuCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef(BaseValidatorModel):
    AcceleratorCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorCountDetailsTypeDef     ] = None
    AcceleratorManufacturers: Optional[Sequence[str]] = None
    AcceleratorNames: Optional[Sequence[str]] = None
    AcceleratorTotalMemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsAcceleratorTotalMemoryMiBDetailsTypeDef     ] = None
    AcceleratorTypes: Optional[Sequence[str]] = None
    BareMetal: Optional[str] = None
    BaselineEbsBandwidthMbps: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsBaselineEbsBandwidthMbpsDetailsTypeDef     ] = None
    BurstablePerformance: Optional[str] = None
    CpuManufacturers: Optional[Sequence[str]] = None
    ExcludedInstanceTypes: Optional[Sequence[str]] = None
    InstanceGenerations: Optional[Sequence[str]] = None
    LocalStorage: Optional[str] = None
    LocalStorageTypes: Optional[Sequence[str]] = None
    MemoryGiBPerVCpu: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryGiBPerVCpuDetailsTypeDef     ] = None
    MemoryMiB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsMemoryMiBDetailsTypeDef     ] = None
    NetworkInterfaceCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsNetworkInterfaceCountDetailsTypeDef     ] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    RequireHibernateSupport: Optional[bool] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    TotalLocalStorageGB: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsTotalLocalStorageGBDetailsTypeDef     ] = None
    VCpuCount: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsVCpuCountDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsExtraOutputTypeDef(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]     ] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]     ] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]     ] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]     ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]     ] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]     ] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]     ] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]     ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None

class AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[Sequence[str]] = None
    InterfaceType: Optional[str] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv4Prefixes: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetailsTypeDef]     ] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6AddressesDetailsTypeDef]     ] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv6PrefixesDetailsTypeDef]     ] = None
    NetworkCardIndex: Optional[int] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetPrivateIpAddressesDetailsTypeDef]     ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None

class AwsEc2NetworkAclEntryTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    Egress: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeFromToTypeDef] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    RuleNumber: Optional[int] = None

class AwsEc2NetworkInterfaceDetailsExtraOutputTypeDef(BaseValidatorModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachmentTypeDef] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[List[AwsEc2NetworkInterfaceSecurityGroupTypeDef]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[List[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]] = None
    PrivateIpAddresses: Optional[       List[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]     ] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None

class AwsEc2NetworkInterfaceDetailsOutputTypeDef(BaseValidatorModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachmentTypeDef] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[List[AwsEc2NetworkInterfaceSecurityGroupTypeDef]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[List[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]] = None
    PrivateIpAddresses: Optional[       List[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]     ] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None

class AwsEc2NetworkInterfaceDetailsTypeDef(BaseValidatorModel):
    Attachment: Optional[AwsEc2NetworkInterfaceAttachmentTypeDef] = None
    NetworkInterfaceId: Optional[str] = None
    SecurityGroups: Optional[Sequence[AwsEc2NetworkInterfaceSecurityGroupTypeDef]] = None
    SourceDestCheck: Optional[bool] = None
    IpV6Addresses: Optional[Sequence[AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef]] = None
    PrivateIpAddresses: Optional[       Sequence[AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef]     ] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None

class AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[AwsEc2SecurityGroupUserIdGroupPairTypeDef]] = None
    IpRanges: Optional[List[AwsEc2SecurityGroupIpRangeTypeDef]] = None
    Ipv6Ranges: Optional[List[AwsEc2SecurityGroupIpv6RangeTypeDef]] = None
    PrefixListIds: Optional[List[AwsEc2SecurityGroupPrefixListIdTypeDef]] = None

class AwsEc2SecurityGroupIpPermissionOutputTypeDef(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[AwsEc2SecurityGroupUserIdGroupPairTypeDef]] = None
    IpRanges: Optional[List[AwsEc2SecurityGroupIpRangeTypeDef]] = None
    Ipv6Ranges: Optional[List[AwsEc2SecurityGroupIpv6RangeTypeDef]] = None
    PrefixListIds: Optional[List[AwsEc2SecurityGroupPrefixListIdTypeDef]] = None

class AwsEc2SecurityGroupIpPermissionTypeDef(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[Sequence[AwsEc2SecurityGroupUserIdGroupPairTypeDef]] = None
    IpRanges: Optional[Sequence[AwsEc2SecurityGroupIpRangeTypeDef]] = None
    Ipv6Ranges: Optional[Sequence[AwsEc2SecurityGroupIpv6RangeTypeDef]] = None
    PrefixListIds: Optional[Sequence[AwsEc2SecurityGroupPrefixListIdTypeDef]] = None

class AwsEc2SubnetDetailsExtraOutputTypeDef(BaseValidatorModel):
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
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociationTypeDef]] = None

class AwsEc2SubnetDetailsOutputTypeDef(BaseValidatorModel):
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
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociationTypeDef]] = None

class AwsEc2SubnetDetailsTypeDef(BaseValidatorModel):
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
    Ipv6CidrBlockAssociationSet: Optional[Sequence[Ipv6CidrBlockAssociationTypeDef]] = None

class AwsEc2VolumeDetailsExtraOutputTypeDef(BaseValidatorModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[List[AwsEc2VolumeAttachmentTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None

class AwsEc2VolumeDetailsOutputTypeDef(BaseValidatorModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[List[AwsEc2VolumeAttachmentTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None

class AwsEc2VolumeDetailsTypeDef(BaseValidatorModel):
    CreateTime: Optional[str] = None
    DeviceName: Optional[str] = None
    Encrypted: Optional[bool] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Attachments: Optional[Sequence[AwsEc2VolumeAttachmentTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeType: Optional[str] = None
    VolumeScanStatus: Optional[str] = None

class AwsEc2VpcDetailsExtraOutputTypeDef(BaseValidatorModel):
    CidrBlockAssociationSet: Optional[List[CidrBlockAssociationTypeDef]] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociationTypeDef]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None

class AwsEc2VpcDetailsOutputTypeDef(BaseValidatorModel):
    CidrBlockAssociationSet: Optional[List[CidrBlockAssociationTypeDef]] = None
    Ipv6CidrBlockAssociationSet: Optional[List[Ipv6CidrBlockAssociationTypeDef]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None

class AwsEc2VpcDetailsTypeDef(BaseValidatorModel):
    CidrBlockAssociationSet: Optional[Sequence[CidrBlockAssociationTypeDef]] = None
    Ipv6CidrBlockAssociationSet: Optional[Sequence[Ipv6CidrBlockAssociationTypeDef]] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[str] = None

class AwsEc2VpcEndpointServiceDetailsExtraOutputTypeDef(BaseValidatorModel):
    AcceptanceRequired: Optional[bool] = None
    AvailabilityZones: Optional[List[str]] = None
    BaseEndpointDnsNames: Optional[List[str]] = None
    ManagesVpcEndpoints: Optional[bool] = None
    GatewayLoadBalancerArns: Optional[List[str]] = None
    NetworkLoadBalancerArns: Optional[List[str]] = None
    PrivateDnsName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceState: Optional[str] = None
    ServiceType: Optional[List[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]] = None

class AwsEc2VpcEndpointServiceDetailsOutputTypeDef(BaseValidatorModel):
    AcceptanceRequired: Optional[bool] = None
    AvailabilityZones: Optional[List[str]] = None
    BaseEndpointDnsNames: Optional[List[str]] = None
    ManagesVpcEndpoints: Optional[bool] = None
    GatewayLoadBalancerArns: Optional[List[str]] = None
    NetworkLoadBalancerArns: Optional[List[str]] = None
    PrivateDnsName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceState: Optional[str] = None
    ServiceType: Optional[List[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]] = None

class AwsEc2VpcEndpointServiceDetailsTypeDef(BaseValidatorModel):
    AcceptanceRequired: Optional[bool] = None
    AvailabilityZones: Optional[Sequence[str]] = None
    BaseEndpointDnsNames: Optional[Sequence[str]] = None
    ManagesVpcEndpoints: Optional[bool] = None
    GatewayLoadBalancerArns: Optional[Sequence[str]] = None
    NetworkLoadBalancerArns: Optional[Sequence[str]] = None
    PrivateDnsName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceState: Optional[str] = None
    ServiceType: Optional[Sequence[AwsEc2VpcEndpointServiceServiceTypeDetailsTypeDef]] = None

class AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[List[VpcInfoCidrBlockSetDetailsTypeDef]] = None
    Ipv6CidrBlockSet: Optional[List[VpcInfoIpv6CidrBlockSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetailsTypeDef] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None

class AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[List[VpcInfoCidrBlockSetDetailsTypeDef]] = None
    Ipv6CidrBlockSet: Optional[List[VpcInfoIpv6CidrBlockSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetailsTypeDef] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None

class AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    CidrBlockSet: Optional[Sequence[VpcInfoCidrBlockSetDetailsTypeDef]] = None
    Ipv6CidrBlockSet: Optional[Sequence[VpcInfoIpv6CidrBlockSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcInfoPeeringOptionsDetailsTypeDef] = None
    Region: Optional[str] = None
    VpcId: Optional[str] = None

class AwsEc2VpnConnectionOptionsDetailsExtraOutputTypeDef(BaseValidatorModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[       List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsExtraOutputTypeDef]     ] = None

class AwsEc2VpnConnectionOptionsDetailsOutputTypeDef(BaseValidatorModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[       List[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsOutputTypeDef]     ] = None

class AwsEc2VpnConnectionOptionsDetailsTypeDef(BaseValidatorModel):
    StaticRoutesOnly: Optional[bool] = None
    TunnelOptions: Optional[       Sequence[AwsEc2VpnConnectionOptionsTunnelOptionsDetailsTypeDef]     ] = None

class AwsEcrRepositoryDetailsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    ImageScanningConfiguration: Optional[       AwsEcrRepositoryImageScanningConfigurationDetailsTypeDef     ] = None
    ImageTagMutability: Optional[str] = None
    LifecyclePolicy: Optional[AwsEcrRepositoryLifecyclePolicyDetailsTypeDef] = None
    RepositoryName: Optional[str] = None
    RepositoryPolicyText: Optional[str] = None

class AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef(BaseValidatorModel):
    KmsKeyId: Optional[str] = None
    LogConfiguration: Optional[       AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetailsTypeDef     ] = None
    Logging: Optional[str] = None

class AwsEcsContainerDetailsExtraOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[List[AwsMountPointTypeDef]] = None
    Privileged: Optional[bool] = None

class AwsEcsContainerDetailsOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[List[AwsMountPointTypeDef]] = None
    Privileged: Optional[bool] = None

class AwsEcsContainerDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Image: Optional[str] = None
    MountPoints: Optional[Sequence[AwsMountPointTypeDef]] = None
    Privileged: Optional[bool] = None

class AwsEcsServiceDeploymentConfigurationDetailsTypeDef(BaseValidatorModel):
    DeploymentCircuitBreaker: Optional[       AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetailsTypeDef     ] = None
    MaximumPercent: Optional[int] = None
    MinimumHealthyPercent: Optional[int] = None

class AwsEcsServiceNetworkConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    AwsVpcConfiguration: Optional[       AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsExtraOutputTypeDef     ] = None

class AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    AwsVpcConfiguration: Optional[       AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsOutputTypeDef     ] = None

class AwsEcsServiceNetworkConfigurationDetailsTypeDef(BaseValidatorModel):
    AwsVpcConfiguration: Optional[       AwsEcsServiceNetworkConfigurationAwsVpcConfigurationDetailsTypeDef     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsExtraOutputTypeDef(BaseValidatorModel):
    Capabilities: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsExtraOutputTypeDef     ] = None
    Devices: Optional[       List[         AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsExtraOutputTypeDef       ]     ] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[       List[         AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsExtraOutputTypeDef       ]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef(BaseValidatorModel):
    Capabilities: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsOutputTypeDef     ] = None
    Devices: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsOutputTypeDef]     ] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsOutputTypeDef]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef(BaseValidatorModel):
    Capabilities: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersCapabilitiesDetailsTypeDef     ] = None
    Devices: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDevicesDetailsTypeDef]     ] = None
    InitProcessEnabled: Optional[bool] = None
    MaxSwap: Optional[int] = None
    SharedMemorySize: Optional[int] = None
    Swappiness: Optional[int] = None
    Tmpfs: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersTmpfsDetailsTypeDef]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    LogDriver: Optional[str] = None
    Options: Optional[Dict[str, str]] = None
    SecretOptions: Optional[       List[         AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef       ]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    LogDriver: Optional[str] = None
    Options: Optional[Dict[str, str]] = None
    SecretOptions: Optional[       List[         AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef       ]     ] = None

class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef(BaseValidatorModel):
    LogDriver: Optional[str] = None
    Options: Optional[Mapping[str, str]] = None
    SecretOptions: Optional[       Sequence[         AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsDetailsTypeDef       ]     ] = None

class AwsEcsTaskDefinitionProxyConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ProxyConfigurationProperties: Optional[       List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]     ] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ProxyConfigurationProperties: Optional[       List[AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef]     ] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef(BaseValidatorModel):
    ContainerName: Optional[str] = None
    ProxyConfigurationProperties: Optional[       Sequence[         AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetailsTypeDef       ]     ] = None
    Type: Optional[str] = None

class AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef(BaseValidatorModel):
    AuthorizationConfig: Optional[       AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationAuthorizationConfigDetailsTypeDef     ] = None
    FilesystemId: Optional[str] = None
    RootDirectory: Optional[str] = None
    TransitEncryption: Optional[str] = None
    TransitEncryptionPort: Optional[int] = None

class AwsEcsTaskVolumeDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Host: Optional[AwsEcsTaskVolumeHostDetailsTypeDef] = None

class AwsEfsAccessPointRootDirectoryDetailsTypeDef(BaseValidatorModel):
    CreationInfo: Optional[AwsEfsAccessPointRootDirectoryCreationInfoDetailsTypeDef] = None
    Path: Optional[str] = None

class AwsEksClusterLoggingDetailsExtraOutputTypeDef(BaseValidatorModel):
    ClusterLogging: Optional[       List[AwsEksClusterLoggingClusterLoggingDetailsExtraOutputTypeDef]     ] = None

class AwsEksClusterLoggingDetailsOutputTypeDef(BaseValidatorModel):
    ClusterLogging: Optional[List[AwsEksClusterLoggingClusterLoggingDetailsOutputTypeDef]] = None

class AwsEksClusterLoggingDetailsTypeDef(BaseValidatorModel):
    ClusterLogging: Optional[Sequence[AwsEksClusterLoggingClusterLoggingDetailsTypeDef]] = None

class AwsElasticBeanstalkEnvironmentDetailsExtraOutputTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[List[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[List[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTierTypeDef] = None
    VersionLabel: Optional[str] = None

class AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[List[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[List[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTierTypeDef] = None
    VersionLabel: Optional[str] = None

class AwsElasticBeanstalkEnvironmentDetailsTypeDef(BaseValidatorModel):
    ApplicationName: Optional[str] = None
    Cname: Optional[str] = None
    DateCreated: Optional[str] = None
    DateUpdated: Optional[str] = None
    Description: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EnvironmentArn: Optional[str] = None
    EnvironmentId: Optional[str] = None
    EnvironmentLinks: Optional[       Sequence[AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef]     ] = None
    EnvironmentName: Optional[str] = None
    OptionSettings: Optional[Sequence[AwsElasticBeanstalkEnvironmentOptionSettingTypeDef]] = None
    PlatformArn: Optional[str] = None
    SolutionStackName: Optional[str] = None
    Status: Optional[str] = None
    Tier: Optional[AwsElasticBeanstalkEnvironmentTierTypeDef] = None
    VersionLabel: Optional[str] = None

class AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef(BaseValidatorModel):
    DedicatedMasterCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    DedicatedMasterType: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[str] = None
    ZoneAwarenessConfig: Optional[       AwsElasticsearchDomainElasticsearchClusterConfigZoneAwarenessConfigDetailsTypeDef     ] = None
    ZoneAwarenessEnabled: Optional[bool] = None

class AwsElasticsearchDomainLogPublishingOptionsTypeDef(BaseValidatorModel):
    IndexSlowLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef] = None
    SearchSlowLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef] = None
    AuditLogs: Optional[AwsElasticsearchDomainLogPublishingOptionsLogConfigTypeDef] = None

class AwsElbLoadBalancerPoliciesExtraOutputTypeDef(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[List[AwsElbAppCookieStickinessPolicyTypeDef]] = None
    LbCookieStickinessPolicies: Optional[List[AwsElbLbCookieStickinessPolicyTypeDef]] = None
    OtherPolicies: Optional[List[str]] = None

class AwsElbLoadBalancerPoliciesOutputTypeDef(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[List[AwsElbAppCookieStickinessPolicyTypeDef]] = None
    LbCookieStickinessPolicies: Optional[List[AwsElbLbCookieStickinessPolicyTypeDef]] = None
    OtherPolicies: Optional[List[str]] = None

class AwsElbLoadBalancerPoliciesTypeDef(BaseValidatorModel):
    AppCookieStickinessPolicies: Optional[       Sequence[AwsElbAppCookieStickinessPolicyTypeDef]     ] = None
    LbCookieStickinessPolicies: Optional[Sequence[AwsElbLbCookieStickinessPolicyTypeDef]] = None
    OtherPolicies: Optional[Sequence[str]] = None

class AwsElbLoadBalancerAttributesExtraOutputTypeDef(BaseValidatorModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLogTypeDef] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettingsTypeDef] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef] = None
    AdditionalAttributes: Optional[List[AwsElbLoadBalancerAdditionalAttributeTypeDef]] = None

class AwsElbLoadBalancerAttributesOutputTypeDef(BaseValidatorModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLogTypeDef] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettingsTypeDef] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef] = None
    AdditionalAttributes: Optional[List[AwsElbLoadBalancerAdditionalAttributeTypeDef]] = None

class AwsElbLoadBalancerAttributesTypeDef(BaseValidatorModel):
    AccessLog: Optional[AwsElbLoadBalancerAccessLogTypeDef] = None
    ConnectionDraining: Optional[AwsElbLoadBalancerConnectionDrainingTypeDef] = None
    ConnectionSettings: Optional[AwsElbLoadBalancerConnectionSettingsTypeDef] = None
    CrossZoneLoadBalancing: Optional[AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef] = None
    AdditionalAttributes: Optional[Sequence[AwsElbLoadBalancerAdditionalAttributeTypeDef]] = None

class AwsElbLoadBalancerListenerDescriptionExtraOutputTypeDef(BaseValidatorModel):
    Listener: Optional[AwsElbLoadBalancerListenerTypeDef] = None
    PolicyNames: Optional[List[str]] = None

class AwsElbLoadBalancerListenerDescriptionOutputTypeDef(BaseValidatorModel):
    Listener: Optional[AwsElbLoadBalancerListenerTypeDef] = None
    PolicyNames: Optional[List[str]] = None

class AwsElbLoadBalancerListenerDescriptionTypeDef(BaseValidatorModel):
    Listener: Optional[AwsElbLoadBalancerListenerTypeDef] = None
    PolicyNames: Optional[Sequence[str]] = None

class AwsElbv2LoadBalancerDetailsExtraOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[str] = None
    DNSName: Optional[str] = None
    IpAddressType: Optional[str] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    State: Optional[LoadBalancerStateTypeDef] = None
    Type: Optional[str] = None
    VpcId: Optional[str] = None
    LoadBalancerAttributes: Optional[List[AwsElbv2LoadBalancerAttributeTypeDef]] = None

class AwsElbv2LoadBalancerDetailsOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[str] = None
    DNSName: Optional[str] = None
    IpAddressType: Optional[str] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    State: Optional[LoadBalancerStateTypeDef] = None
    Type: Optional[str] = None
    VpcId: Optional[str] = None
    LoadBalancerAttributes: Optional[List[AwsElbv2LoadBalancerAttributeTypeDef]] = None

class AwsElbv2LoadBalancerDetailsTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[Sequence[AvailabilityZoneTypeDef]] = None
    CanonicalHostedZoneId: Optional[str] = None
    CreatedTime: Optional[str] = None
    DNSName: Optional[str] = None
    IpAddressType: Optional[str] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    State: Optional[LoadBalancerStateTypeDef] = None
    Type: Optional[str] = None
    VpcId: Optional[str] = None
    LoadBalancerAttributes: Optional[Sequence[AwsElbv2LoadBalancerAttributeTypeDef]] = None

class AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef(BaseValidatorModel):
    Primary: Optional[AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetailsTypeDef] = None
    Secondary: Optional[       AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetailsTypeDef     ] = None

class AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef(BaseValidatorModel):
    AuditLogs: Optional[AwsGuardDutyDetectorDataSourcesKubernetesAuditLogsDetailsTypeDef] = None

class AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef(BaseValidatorModel):
    EbsVolumes: Optional[       AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsEbsVolumesDetailsTypeDef     ] = None

class AwsIamAccessKeySessionContextTypeDef(BaseValidatorModel):
    Attributes: Optional[AwsIamAccessKeySessionContextAttributesTypeDef] = None
    SessionIssuer: Optional[AwsIamAccessKeySessionContextSessionIssuerTypeDef] = None

class AwsIamGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[List[AwsIamGroupPolicyTypeDef]] = None
    Path: Optional[str] = None

class AwsIamGroupDetailsOutputTypeDef(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[List[AwsIamGroupPolicyTypeDef]] = None
    Path: Optional[str] = None

class AwsIamGroupDetailsTypeDef(BaseValidatorModel):
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupPolicyList: Optional[Sequence[AwsIamGroupPolicyTypeDef]] = None
    Path: Optional[str] = None

class AwsIamInstanceProfileExtraOutputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[List[AwsIamInstanceProfileRoleTypeDef]] = None

class AwsIamInstanceProfileOutputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[List[AwsIamInstanceProfileRoleTypeDef]] = None

class AwsIamInstanceProfileTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CreateDate: Optional[str] = None
    InstanceProfileId: Optional[str] = None
    InstanceProfileName: Optional[str] = None
    Path: Optional[str] = None
    Roles: Optional[Sequence[AwsIamInstanceProfileRoleTypeDef]] = None

class AwsIamPolicyDetailsExtraOutputTypeDef(BaseValidatorModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[List[AwsIamPolicyVersionTypeDef]] = None
    UpdateDate: Optional[str] = None

class AwsIamPolicyDetailsOutputTypeDef(BaseValidatorModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[List[AwsIamPolicyVersionTypeDef]] = None
    UpdateDate: Optional[str] = None

class AwsIamPolicyDetailsTypeDef(BaseValidatorModel):
    AttachmentCount: Optional[int] = None
    CreateDate: Optional[str] = None
    DefaultVersionId: Optional[str] = None
    Description: Optional[str] = None
    IsAttachable: Optional[bool] = None
    Path: Optional[str] = None
    PermissionsBoundaryUsageCount: Optional[int] = None
    PolicyId: Optional[str] = None
    PolicyName: Optional[str] = None
    PolicyVersionList: Optional[Sequence[AwsIamPolicyVersionTypeDef]] = None
    UpdateDate: Optional[str] = None

class AwsIamUserDetailsExtraOutputTypeDef(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[List[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[List[AwsIamUserPolicyTypeDef]] = None

class AwsIamUserDetailsOutputTypeDef(BaseValidatorModel):
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[List[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[List[AwsIamUserPolicyTypeDef]] = None

class AwsIamUserDetailsTypeDef(BaseValidatorModel):
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    GroupList: Optional[Sequence[str]] = None
    Path: Optional[str] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    UserPolicyList: Optional[Sequence[AwsIamUserPolicyTypeDef]] = None

class AwsKinesisStreamDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    StreamEncryption: Optional[AwsKinesisStreamStreamEncryptionDetailsTypeDef] = None
    ShardCount: Optional[int] = None
    RetentionPeriodHours: Optional[int] = None

class AwsLambdaFunctionEnvironmentExtraOutputTypeDef(BaseValidatorModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentErrorTypeDef] = None

class AwsLambdaFunctionEnvironmentOutputTypeDef(BaseValidatorModel):
    Variables: Optional[Dict[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentErrorTypeDef] = None

class AwsLambdaFunctionEnvironmentTypeDef(BaseValidatorModel):
    Variables: Optional[Mapping[str, str]] = None
    Error: Optional[AwsLambdaFunctionEnvironmentErrorTypeDef] = None

class AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef(BaseValidatorModel):
    Iam: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslIamDetailsTypeDef] = None
    Scram: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslScramDetailsTypeDef] = None

class AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef(BaseValidatorModel):
    EncryptionInTransit: Optional[       AwsMskClusterClusterInfoEncryptionInfoEncryptionInTransitDetailsTypeDef     ] = None
    EncryptionAtRest: Optional[       AwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetailsTypeDef     ] = None

class AwsNetworkFirewallFirewallDetailsExtraOutputTypeDef(BaseValidatorModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[List[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AwsNetworkFirewallFirewallDetailsOutputTypeDef(BaseValidatorModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[List[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AwsNetworkFirewallFirewallDetailsTypeDef(BaseValidatorModel):
    DeleteProtection: Optional[bool] = None
    Description: Optional[str] = None
    FirewallArn: Optional[str] = None
    FirewallId: Optional[str] = None
    FirewallName: Optional[str] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyChangeProtection: Optional[bool] = None
    SubnetChangeProtection: Optional[bool] = None
    SubnetMappings: Optional[       Sequence[AwsNetworkFirewallFirewallSubnetMappingsDetailsTypeDef]     ] = None
    VpcId: Optional[str] = None

class AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    InternalUserDatabaseEnabled: Optional[bool] = None
    MasterUserOptions: Optional[AwsOpenSearchServiceDomainMasterUserOptionsDetailsTypeDef] = None

class AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    WarmEnabled: Optional[bool] = None
    WarmCount: Optional[int] = None
    DedicatedMasterEnabled: Optional[bool] = None
    ZoneAwarenessConfig: Optional[       AwsOpenSearchServiceDomainClusterConfigZoneAwarenessConfigDetailsTypeDef     ] = None
    DedicatedMasterCount: Optional[int] = None
    InstanceType: Optional[str] = None
    WarmType: Optional[str] = None
    ZoneAwarenessEnabled: Optional[bool] = None
    DedicatedMasterType: Optional[str] = None

class AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef(BaseValidatorModel):
    IndexSlowLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef] = None
    SearchSlowLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef] = None
    AuditLogs: Optional[AwsOpenSearchServiceDomainLogPublishingOptionTypeDef] = None

class AwsRdsDbClusterDetailsExtraOutputTypeDef(BaseValidatorModel):
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
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[List[AwsRdsDbClusterAssociatedRoleTypeDef]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembershipTypeDef]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[       List[AwsRdsDbClusterOptionGroupMembershipTypeDef]     ] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[List[AwsRdsDbClusterMemberTypeDef]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None

class AwsRdsDbClusterDetailsOutputTypeDef(BaseValidatorModel):
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
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[List[AwsRdsDbClusterAssociatedRoleTypeDef]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembershipTypeDef]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[       List[AwsRdsDbClusterOptionGroupMembershipTypeDef]     ] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[List[AwsRdsDbClusterMemberTypeDef]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None

class AwsRdsDbClusterDetailsTypeDef(BaseValidatorModel):
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
    VpcSecurityGroups: Optional[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    AssociatedRoles: Optional[Sequence[AwsRdsDbClusterAssociatedRoleTypeDef]] = None
    ClusterCreateTime: Optional[str] = None
    EnabledCloudWatchLogsExports: Optional[Sequence[str]] = None
    EngineMode: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    HttpEndpointEnabled: Optional[bool] = None
    ActivityStreamStatus: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    DomainMemberships: Optional[Sequence[AwsRdsDbDomainMembershipTypeDef]] = None
    DbClusterParameterGroup: Optional[str] = None
    DbSubnetGroup: Optional[str] = None
    DbClusterOptionGroupMemberships: Optional[       Sequence[AwsRdsDbClusterOptionGroupMembershipTypeDef]     ] = None
    DbClusterIdentifier: Optional[str] = None
    DbClusterMembers: Optional[Sequence[AwsRdsDbClusterMemberTypeDef]] = None
    IamDatabaseAuthenticationEnabled: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None

class AwsRdsDbClusterSnapshotDetailsExtraOutputTypeDef(BaseValidatorModel):
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
    DbClusterSnapshotAttributes: Optional[       List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeExtraOutputTypeDef]     ] = None

class AwsRdsDbClusterSnapshotDetailsOutputTypeDef(BaseValidatorModel):
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
    DbClusterSnapshotAttributes: Optional[       List[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeOutputTypeDef]     ] = None

class AwsRdsDbClusterSnapshotDetailsTypeDef(BaseValidatorModel):
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
    DbClusterSnapshotAttributes: Optional[       Sequence[AwsRdsDbClusterSnapshotDbClusterSnapshotAttributeTypeDef]     ] = None

class AwsRdsDbSnapshotDetailsExtraOutputTypeDef(BaseValidatorModel):
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
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None
    DbiResourceId: Optional[str] = None

class AwsRdsDbSnapshotDetailsOutputTypeDef(BaseValidatorModel):
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
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None
    DbiResourceId: Optional[str] = None

class AwsRdsDbSnapshotDetailsTypeDef(BaseValidatorModel):
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
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeatureTypeDef]] = None
    DbiResourceId: Optional[str] = None

class AwsRdsDbPendingModifiedValuesExtraOutputTypeDef(BaseValidatorModel):
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
    PendingCloudWatchLogsExports: Optional[       AwsRdsPendingCloudWatchLogsExportsExtraOutputTypeDef     ] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None

class AwsRdsDbPendingModifiedValuesOutputTypeDef(BaseValidatorModel):
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
    PendingCloudWatchLogsExports: Optional[       AwsRdsPendingCloudWatchLogsExportsOutputTypeDef     ] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None

class AwsRdsDbPendingModifiedValuesTypeDef(BaseValidatorModel):
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
    PendingCloudWatchLogsExports: Optional[AwsRdsPendingCloudWatchLogsExportsTypeDef] = None
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeatureTypeDef]] = None

class AwsRdsDbSecurityGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[List[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]] = None
    IpRanges: Optional[List[AwsRdsDbSecurityGroupIpRangeTypeDef]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None

class AwsRdsDbSecurityGroupDetailsOutputTypeDef(BaseValidatorModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[List[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]] = None
    IpRanges: Optional[List[AwsRdsDbSecurityGroupIpRangeTypeDef]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None

class AwsRdsDbSecurityGroupDetailsTypeDef(BaseValidatorModel):
    DbSecurityGroupArn: Optional[str] = None
    DbSecurityGroupDescription: Optional[str] = None
    DbSecurityGroupName: Optional[str] = None
    Ec2SecurityGroups: Optional[Sequence[AwsRdsDbSecurityGroupEc2SecurityGroupTypeDef]] = None
    IpRanges: Optional[Sequence[AwsRdsDbSecurityGroupIpRangeTypeDef]] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None

class AwsRdsDbSubnetGroupSubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None

class AwsRedshiftClusterClusterParameterGroupExtraOutputTypeDef(BaseValidatorModel):
    ClusterParameterStatusList: Optional[       List[AwsRedshiftClusterClusterParameterStatusTypeDef]     ] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None

class AwsRedshiftClusterClusterParameterGroupOutputTypeDef(BaseValidatorModel):
    ClusterParameterStatusList: Optional[       List[AwsRedshiftClusterClusterParameterStatusTypeDef]     ] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None

class AwsRedshiftClusterClusterParameterGroupTypeDef(BaseValidatorModel):
    ClusterParameterStatusList: Optional[       Sequence[AwsRedshiftClusterClusterParameterStatusTypeDef]     ] = None
    ParameterApplyStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None

class AwsRoute53HostedZoneObjectDetailsTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Name: Optional[str] = None
    Config: Optional[AwsRoute53HostedZoneConfigDetailsTypeDef] = None

class AwsRoute53QueryLoggingConfigDetailsTypeDef(BaseValidatorModel):
    CloudWatchLogsLogGroupArn: Optional[CloudWatchLogsLogGroupArnConfigDetailsTypeDef] = None

class AwsS3AccessPointDetailsTypeDef(BaseValidatorModel):
    AccessPointArn: Optional[str] = None
    Alias: Optional[str] = None
    Bucket: Optional[str] = None
    BucketAccountId: Optional[str] = None
    Name: Optional[str] = None
    NetworkOrigin: Optional[str] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    VpcConfiguration: Optional[AwsS3AccessPointVpcConfigurationDetailsTypeDef] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef(BaseValidatorModel):
    Prefix: Optional[str] = None
    Tag: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsTagDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsS3BucketNotificationConfigurationS3KeyFilterExtraOutputTypeDef(BaseValidatorModel):
    FilterRules: Optional[       List[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef(BaseValidatorModel):
    FilterRules: Optional[       List[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef(BaseValidatorModel):
    FilterRules: Optional[       Sequence[AwsS3BucketNotificationConfigurationS3KeyFilterRuleTypeDef]     ] = None

class AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef(BaseValidatorModel):
    DefaultRetention: Optional[       AwsS3BucketObjectLockConfigurationRuleDefaultRetentionDetailsTypeDef     ] = None

class AwsS3BucketServerSideEncryptionRuleTypeDef(BaseValidatorModel):
    ApplyServerSideEncryptionByDefault: Optional[       AwsS3BucketServerSideEncryptionByDefaultTypeDef     ] = None

class AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef(BaseValidatorModel):
    Condition: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleConditionTypeDef] = None
    Redirect: Optional[AwsS3BucketWebsiteConfigurationRoutingRuleRedirectTypeDef] = None

class AwsSageMakerNotebookInstanceDetailsExtraOutputTypeDef(BaseValidatorModel):
    AcceleratorTypes: Optional[List[str]] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[       AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef     ] = None
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

class AwsSageMakerNotebookInstanceDetailsOutputTypeDef(BaseValidatorModel):
    AcceleratorTypes: Optional[List[str]] = None
    AdditionalCodeRepositories: Optional[List[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[       AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef     ] = None
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

class AwsSageMakerNotebookInstanceDetailsTypeDef(BaseValidatorModel):
    AcceleratorTypes: Optional[Sequence[str]] = None
    AdditionalCodeRepositories: Optional[Sequence[str]] = None
    DefaultCodeRepository: Optional[str] = None
    DirectInternetAccess: Optional[str] = None
    FailureReason: Optional[str] = None
    InstanceMetadataServiceConfiguration: Optional[       AwsSageMakerNotebookInstanceMetadataServiceConfigurationDetailsTypeDef     ] = None
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

class AwsSecretsManagerSecretDetailsTypeDef(BaseValidatorModel):
    RotationRules: Optional[AwsSecretsManagerSecretRotationRulesTypeDef] = None
    RotationOccurredWithinFrequency: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    RotationEnabled: Optional[bool] = None
    RotationLambdaArn: Optional[str] = None
    Deleted: Optional[bool] = None
    Name: Optional[str] = None
    Description: Optional[str] = None

class BatchUpdateFindingsRequestRequestTypeDef(BaseValidatorModel):
    FindingIdentifiers: Sequence[AwsSecurityFindingIdentifierTypeDef]
    Note: Optional[NoteUpdateTypeDef] = None
    Severity: Optional[SeverityUpdateTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Types: Optional[Sequence[str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Workflow: Optional[WorkflowUpdateTypeDef] = None
    RelatedFindings: Optional[Sequence[RelatedFindingTypeDef]] = None

class BatchUpdateFindingsUnprocessedFindingTypeDef(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    ErrorCode: str
    ErrorMessage: str

class AwsSnsTopicDetailsExtraOutputTypeDef(BaseValidatorModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[List[AwsSnsTopicSubscriptionTypeDef]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None

class AwsSnsTopicDetailsOutputTypeDef(BaseValidatorModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[List[AwsSnsTopicSubscriptionTypeDef]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None

class AwsSnsTopicDetailsTypeDef(BaseValidatorModel):
    KmsMasterKeyId: Optional[str] = None
    Subscription: Optional[Sequence[AwsSnsTopicSubscriptionTypeDef]] = None
    TopicName: Optional[str] = None
    Owner: Optional[str] = None
    SqsSuccessFeedbackRoleArn: Optional[str] = None
    SqsFailureFeedbackRoleArn: Optional[str] = None
    ApplicationSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseSuccessFeedbackRoleArn: Optional[str] = None
    FirehoseFailureFeedbackRoleArn: Optional[str] = None
    HttpSuccessFeedbackRoleArn: Optional[str] = None
    HttpFailureFeedbackRoleArn: Optional[str] = None

class AwsSsmPatchTypeDef(BaseValidatorModel):
    ComplianceSummary: Optional[AwsSsmComplianceSummaryTypeDef] = None

class AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef(BaseValidatorModel):
    CloudWatchLogsLogGroup: Optional[       AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetailsTypeDef     ] = None

class AwsWafRateBasedRuleDetailsExtraOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRateBasedRuleDetailsOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRateBasedRuleDetailsTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[Sequence[AwsWafRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRegionalRateBasedRuleDetailsExtraOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRegionalRateBasedRuleDetailsOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[List[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRegionalRateBasedRuleDetailsTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RateKey: Optional[str] = None
    RateLimit: Optional[int] = None
    RuleId: Optional[str] = None
    MatchPredicates: Optional[Sequence[AwsWafRegionalRateBasedRuleMatchPredicateTypeDef]] = None

class AwsWafRegionalRuleDetailsExtraOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRegionalRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRegionalRuleDetailsOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRegionalRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRegionalRuleDetailsTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[Sequence[AwsWafRegionalRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRegionalRuleGroupRulesDetailsTypeDef(BaseValidatorModel):
    Action: Optional[AwsWafRegionalRuleGroupRulesActionDetailsTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafRegionalWebAclRulesListDetailsTypeDef(BaseValidatorModel):
    Action: Optional[AwsWafRegionalWebAclRulesListActionDetailsTypeDef] = None
    OverrideAction: Optional[AwsWafRegionalWebAclRulesListOverrideActionDetailsTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafRuleDetailsExtraOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRuleDetailsOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[List[AwsWafRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRuleDetailsTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    PredicateList: Optional[Sequence[AwsWafRulePredicateListDetailsTypeDef]] = None
    RuleId: Optional[str] = None

class AwsWafRuleGroupRulesDetailsTypeDef(BaseValidatorModel):
    Action: Optional[AwsWafRuleGroupRulesActionDetailsTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafWebAclRuleExtraOutputTypeDef(BaseValidatorModel):
    Action: Optional[WafActionTypeDef] = None
    ExcludedRules: Optional[List[WafExcludedRuleTypeDef]] = None
    OverrideAction: Optional[WafOverrideActionTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafWebAclRuleOutputTypeDef(BaseValidatorModel):
    Action: Optional[WafActionTypeDef] = None
    ExcludedRules: Optional[List[WafExcludedRuleTypeDef]] = None
    OverrideAction: Optional[WafOverrideActionTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafWebAclRuleTypeDef(BaseValidatorModel):
    Action: Optional[WafActionTypeDef] = None
    ExcludedRules: Optional[Sequence[WafExcludedRuleTypeDef]] = None
    OverrideAction: Optional[WafOverrideActionTypeDef] = None
    Priority: Optional[int] = None
    RuleId: Optional[str] = None
    Type: Optional[str] = None

class AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef(BaseValidatorModel):
    InsertHeaders: Optional[List[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomRequestHandlingDetailsOutputTypeDef(BaseValidatorModel):
    InsertHeaders: Optional[List[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomRequestHandlingDetailsTypeDef(BaseValidatorModel):
    InsertHeaders: Optional[Sequence[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomResponseDetailsExtraOutputTypeDef(BaseValidatorModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[List[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomResponseDetailsOutputTypeDef(BaseValidatorModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[List[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2CustomResponseDetailsTypeDef(BaseValidatorModel):
    CustomResponseBodyKey: Optional[str] = None
    ResponseCode: Optional[int] = None
    ResponseHeaders: Optional[Sequence[AwsWafv2CustomHttpHeaderTypeDef]] = None

class AwsWafv2WebAclCaptchaConfigDetailsTypeDef(BaseValidatorModel):
    ImmunityTimeProperty: Optional[       AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetailsTypeDef     ] = None

class CreateActionTargetResponseTypeDef(BaseValidatorModel):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAutomationRuleResponseTypeDef(BaseValidatorModel):
    RuleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFindingAggregatorResponseTypeDef(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInsightResponseTypeDef(BaseValidatorModel):
    InsightArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteActionTargetResponseTypeDef(BaseValidatorModel):
    ActionTargetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInsightResponseTypeDef(BaseValidatorModel):
    InsightArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActionTargetsResponseTypeDef(BaseValidatorModel):
    ActionTargets: List[ActionTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeHubResponseTypeDef(BaseValidatorModel):
    HubArn: str
    SubscribedAt: str
    AutoEnableControls: bool
    ControlFindingGenerator: ControlFindingGeneratorType
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImportFindingsForProductResponseTypeDef(BaseValidatorModel):
    ProductSubscriptionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigurationPolicyAssociationResponseTypeDef(BaseValidatorModel):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetFindingAggregatorResponseTypeDef(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetInvitationsCountResponseTypeDef(BaseValidatorModel):
    InvitationsCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutomationRulesResponseTypeDef(BaseValidatorModel):
    AutomationRulesMetadata: List[AutomationRulesMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEnabledProductsForImportResponseTypeDef(BaseValidatorModel):
    ProductSubscriptions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListOrganizationAdminAccountsResponseTypeDef(BaseValidatorModel):
    AdminAccounts: List[AdminAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartConfigurationPolicyAssociationResponseTypeDef(BaseValidatorModel):
    ConfigurationPolicyId: str
    TargetId: str
    TargetType: TargetTypeType
    AssociationType: AssociationTypeType
    UpdatedAt: datetime
    AssociationStatus: ConfigurationPolicyAssociationStatusType
    AssociationStatusMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFindingAggregatorResponseTypeDef(BaseValidatorModel):
    FindingAggregatorArn: str
    FindingAggregationRegion: str
    RegionLinkingMode: str
    Regions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteAutomationRulesResponseTypeDef(BaseValidatorModel):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateAutomationRulesResponseTypeDef(BaseValidatorModel):
    ProcessedAutomationRules: List[str]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableStandardsRequestRequestTypeDef(BaseValidatorModel):
    StandardsSubscriptionRequests: Sequence[StandardsSubscriptionRequestTypeDef]

class ListConfigurationPolicyAssociationsResponseTypeDef(BaseValidatorModel):
    ConfigurationPolicyAssociationSummaries: List[       ConfigurationPolicyAssociationSummaryTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetStandardsControlAssociationsRequestRequestTypeDef(BaseValidatorModel):
    StandardsControlAssociationIds: Sequence[StandardsControlAssociationIdTypeDef]

class UnprocessedStandardsControlAssociationTypeDef(BaseValidatorModel):
    StandardsControlAssociationId: StandardsControlAssociationIdTypeDef
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None

class BatchImportFindingsResponseTypeDef(BaseValidatorModel):
    FailedCount: int
    SuccessCount: int
    FailedFindings: List[ImportFindingsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateStandardsControlAssociationsRequestRequestTypeDef(BaseValidatorModel):
    StandardsControlAssociationUpdates: Sequence[StandardsControlAssociationUpdateTypeDef]

class UnprocessedStandardsControlAssociationUpdateTypeDef(BaseValidatorModel):
    StandardsControlAssociationUpdate: StandardsControlAssociationUpdateTypeDef
    ErrorCode: UnprocessedErrorCodeType
    ErrorReason: Optional[str] = None

class VulnerabilityCodeVulnerabilitiesExtraOutputTypeDef(BaseValidatorModel):
    Cwes: Optional[List[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePathTypeDef] = None
    SourceArn: Optional[str] = None

class VulnerabilityCodeVulnerabilitiesOutputTypeDef(BaseValidatorModel):
    Cwes: Optional[List[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePathTypeDef] = None
    SourceArn: Optional[str] = None

class VulnerabilityCodeVulnerabilitiesTypeDef(BaseValidatorModel):
    Cwes: Optional[Sequence[str]] = None
    FilePath: Optional[CodeVulnerabilitiesFilePathTypeDef] = None
    SourceArn: Optional[str] = None

class ComplianceExtraOutputTypeDef(BaseValidatorModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[List[str]] = None
    StatusReasons: Optional[List[StatusReasonTypeDef]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[List[AssociatedStandardTypeDef]] = None
    SecurityControlParameters: Optional[List[SecurityControlParameterExtraOutputTypeDef]] = None

class ComplianceOutputTypeDef(BaseValidatorModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[List[str]] = None
    StatusReasons: Optional[List[StatusReasonTypeDef]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[List[AssociatedStandardTypeDef]] = None
    SecurityControlParameters: Optional[List[SecurityControlParameterOutputTypeDef]] = None

class ComplianceTypeDef(BaseValidatorModel):
    Status: Optional[ComplianceStatusType] = None
    RelatedRequirements: Optional[Sequence[str]] = None
    StatusReasons: Optional[Sequence[StatusReasonTypeDef]] = None
    SecurityControlId: Optional[str] = None
    AssociatedStandards: Optional[Sequence[AssociatedStandardTypeDef]] = None
    SecurityControlParameters: Optional[Sequence[SecurityControlParameterTypeDef]] = None

class ConfigurationOptionsTypeDef(BaseValidatorModel):
    Integer: Optional[IntegerConfigurationOptionsTypeDef] = None
    IntegerList: Optional[IntegerListConfigurationOptionsTypeDef] = None
    Double: Optional[DoubleConfigurationOptionsTypeDef] = None
    String: Optional[StringConfigurationOptionsTypeDef] = None
    StringList: Optional[StringListConfigurationOptionsTypeDef] = None
    Boolean: Optional[BooleanConfigurationOptionsTypeDef] = None
    Enum: Optional[EnumConfigurationOptionsTypeDef] = None
    EnumList: Optional[EnumListConfigurationOptionsTypeDef] = None

class ConfigurationPolicyAssociationTypeDef(BaseValidatorModel):
    Target: Optional[TargetTypeDef] = None

class GetConfigurationPolicyAssociationRequestRequestTypeDef(BaseValidatorModel):
    Target: TargetTypeDef

class StartConfigurationPolicyAssociationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationPolicyIdentifier: str
    Target: TargetTypeDef

class StartConfigurationPolicyDisassociationRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationPolicyIdentifier: str
    Target: Optional[TargetTypeDef] = None

class ListConfigurationPoliciesResponseTypeDef(BaseValidatorModel):
    ConfigurationPolicySummaries: List[ConfigurationPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContainerDetailsExtraOutputTypeDef(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMountTypeDef]] = None
    Privileged: Optional[bool] = None

class ContainerDetailsOutputTypeDef(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[List[VolumeMountTypeDef]] = None
    Privileged: Optional[bool] = None

class ContainerDetailsTypeDef(BaseValidatorModel):
    ContainerRuntime: Optional[str] = None
    Name: Optional[str] = None
    ImageId: Optional[str] = None
    ImageName: Optional[str] = None
    LaunchedAt: Optional[str] = None
    VolumeMounts: Optional[Sequence[VolumeMountTypeDef]] = None
    Privileged: Optional[bool] = None

class CreateMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeclineInvitationsResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInvitationsResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InviteMembersResponseTypeDef(BaseValidatorModel):
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DateFilterTypeDef(BaseValidatorModel):
    Start: Optional[str] = None
    End: Optional[str] = None
    DateRange: Optional[DateRangeTypeDef] = None

class DescribeActionTargetsRequestDescribeActionTargetsPaginateTypeDef(BaseValidatorModel):
    ActionTargetArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeProductsRequestDescribeProductsPaginateTypeDef(BaseValidatorModel):
    ProductArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStandardsControlsRequestDescribeStandardsControlsPaginateTypeDef(BaseValidatorModel):
    StandardsSubscriptionArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStandardsRequestDescribeStandardsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetEnabledStandardsRequestGetEnabledStandardsPaginateTypeDef(BaseValidatorModel):
    StandardsSubscriptionArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInsightsRequestGetInsightsPaginateTypeDef(BaseValidatorModel):
    InsightArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationPoliciesRequestListConfigurationPoliciesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfigurationPolicyAssociationsRequestListConfigurationPolicyAssociationsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[AssociationFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEnabledProductsForImportRequestListEnabledProductsForImportPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFindingAggregatorsRequestListFindingAggregatorsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInvitationsRequestListInvitationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMembersRequestListMembersPaginateTypeDef(BaseValidatorModel):
    OnlyAssociated: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityControlDefinitionsRequestListSecurityControlDefinitionsPaginateTypeDef(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStandardsControlAssociationsRequestListStandardsControlAssociationsPaginateTypeDef(BaseValidatorModel):
    SecurityControlId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrganizationConfigurationResponseTypeDef(BaseValidatorModel):
    AutoEnable: bool
    MemberAccountLimitReached: bool
    AutoEnableStandards: AutoEnableStandardsType
    OrganizationConfiguration: OrganizationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOrganizationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AutoEnable: bool
    AutoEnableStandards: Optional[AutoEnableStandardsType] = None
    OrganizationConfiguration: Optional[OrganizationConfigurationTypeDef] = None

class DescribeProductsResponseTypeDef(BaseValidatorModel):
    Products: List[ProductTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStandardsControlsResponseTypeDef(BaseValidatorModel):
    Controls: List[StandardsControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ThreatExtraOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[FilePathsTypeDef]] = None

class ThreatOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[List[FilePathsTypeDef]] = None

class ThreatTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Severity: Optional[str] = None
    ItemCount: Optional[int] = None
    FilePaths: Optional[Sequence[FilePathsTypeDef]] = None

class ListFindingAggregatorsResponseTypeDef(BaseValidatorModel):
    FindingAggregators: List[FindingAggregatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FindingHistoryRecordTypeDef(BaseValidatorModel):
    FindingIdentifier: Optional[AwsSecurityFindingIdentifierTypeDef] = None
    UpdateTime: Optional[datetime] = None
    FindingCreated: Optional[bool] = None
    UpdateSource: Optional[FindingHistoryUpdateSourceTypeDef] = None
    Updates: Optional[List[FindingHistoryUpdateTypeDef]] = None
    NextToken: Optional[str] = None

class FindingProviderFieldsExtraOutputTypeDef(BaseValidatorModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None
    Severity: Optional[FindingProviderSeverityTypeDef] = None
    Types: Optional[List[str]] = None

class FindingProviderFieldsOutputTypeDef(BaseValidatorModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None
    Severity: Optional[FindingProviderSeverityTypeDef] = None
    Types: Optional[List[str]] = None

class FindingProviderFieldsTypeDef(BaseValidatorModel):
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    RelatedFindings: Optional[Sequence[RelatedFindingTypeDef]] = None
    Severity: Optional[FindingProviderSeverityTypeDef] = None
    Types: Optional[Sequence[str]] = None

class GetAdministratorAccountResponseTypeDef(BaseValidatorModel):
    Administrator: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMasterAccountResponseTypeDef(BaseValidatorModel):
    Master: InvitationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInvitationsResponseTypeDef(BaseValidatorModel):
    Invitations: List[InvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetFindingHistoryRequestGetFindingHistoryPaginateTypeDef(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetFindingHistoryRequestRequestTypeDef(BaseValidatorModel):
    FindingIdentifier: AwsSecurityFindingIdentifierTypeDef
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetMembersResponseTypeDef(BaseValidatorModel):
    Members: List[MemberTypeDef]
    UnprocessedAccounts: List[ResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMembersResponseTypeDef(BaseValidatorModel):
    Members: List[MemberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InsightResultsTypeDef(BaseValidatorModel):
    InsightArn: str
    GroupByAttribute: str
    ResultValues: List[InsightResultValueTypeDef]

class ListStandardsControlAssociationsResponseTypeDef(BaseValidatorModel):
    StandardsControlAssociationSummaries: List[StandardsControlAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NetworkPathComponentDetailsExtraOutputTypeDef(BaseValidatorModel):
    Address: Optional[List[str]] = None
    PortRanges: Optional[List[PortRangeTypeDef]] = None

class NetworkPathComponentDetailsOutputTypeDef(BaseValidatorModel):
    Address: Optional[List[str]] = None
    PortRanges: Optional[List[PortRangeTypeDef]] = None

class NetworkPathComponentDetailsTypeDef(BaseValidatorModel):
    Address: Optional[Sequence[str]] = None
    PortRanges: Optional[Sequence[PortRangeTypeDef]] = None

class NetworkTypeDef(BaseValidatorModel):
    Direction: Optional[NetworkDirectionType] = None
    Protocol: Optional[str] = None
    OpenPortRange: Optional[PortRangeTypeDef] = None
    SourceIpV4: Optional[str] = None
    SourceIpV6: Optional[str] = None
    SourcePort: Optional[int] = None
    SourceDomain: Optional[str] = None
    SourceMac: Optional[str] = None
    DestinationIpV4: Optional[str] = None
    DestinationIpV6: Optional[str] = None
    DestinationPort: Optional[int] = None
    DestinationDomain: Optional[str] = None

class PageTypeDef(BaseValidatorModel):
    PageNumber: Optional[int] = None
    LineRange: Optional[RangeTypeDef] = None
    OffsetRange: Optional[RangeTypeDef] = None

class ParameterConfigurationOutputTypeDef(BaseValidatorModel):
    ValueType: ParameterValueTypeType
    Value: Optional[ParameterValueOutputTypeDef] = None

class ParameterConfigurationTypeDef(BaseValidatorModel):
    ValueType: ParameterValueTypeType
    Value: Optional[ParameterValueTypeDef] = None

class RemediationTypeDef(BaseValidatorModel):
    Recommendation: Optional[RecommendationTypeDef] = None

class RuleGroupSourceStatefulRulesDetailsExtraOutputTypeDef(BaseValidatorModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef] = None
    RuleOptions: Optional[       List[RuleGroupSourceStatefulRulesOptionsDetailsExtraOutputTypeDef]     ] = None

class RuleGroupSourceStatefulRulesDetailsOutputTypeDef(BaseValidatorModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef] = None
    RuleOptions: Optional[List[RuleGroupSourceStatefulRulesOptionsDetailsOutputTypeDef]] = None

class RuleGroupSourceStatefulRulesDetailsTypeDef(BaseValidatorModel):
    Action: Optional[str] = None
    Header: Optional[RuleGroupSourceStatefulRulesHeaderDetailsTypeDef] = None
    RuleOptions: Optional[Sequence[RuleGroupSourceStatefulRulesOptionsDetailsTypeDef]] = None

class RuleGroupSourceStatelessRuleMatchAttributesExtraOutputTypeDef(BaseValidatorModel):
    DestinationPorts: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]     ] = None
    Destinations: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]     ] = None
    Protocols: Optional[List[int]] = None
    SourcePorts: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]     ] = None
    Sources: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]] = None
    TcpFlags: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsExtraOutputTypeDef]     ] = None

class RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef(BaseValidatorModel):
    DestinationPorts: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]     ] = None
    Destinations: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]     ] = None
    Protocols: Optional[List[int]] = None
    SourcePorts: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]     ] = None
    Sources: Optional[List[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]] = None
    TcpFlags: Optional[       List[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsOutputTypeDef]     ] = None

class RuleGroupSourceStatelessRuleMatchAttributesTypeDef(BaseValidatorModel):
    DestinationPorts: Optional[       Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationPortsTypeDef]     ] = None
    Destinations: Optional[       Sequence[RuleGroupSourceStatelessRuleMatchAttributesDestinationsTypeDef]     ] = None
    Protocols: Optional[Sequence[int]] = None
    SourcePorts: Optional[       Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcePortsTypeDef]     ] = None
    Sources: Optional[Sequence[RuleGroupSourceStatelessRuleMatchAttributesSourcesTypeDef]] = None
    TcpFlags: Optional[       Sequence[RuleGroupSourceStatelessRuleMatchAttributesTcpFlagsTypeDef]     ] = None

class RuleGroupVariablesExtraOutputTypeDef(BaseValidatorModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsExtraOutputTypeDef] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsExtraOutputTypeDef] = None

class RuleGroupVariablesOutputTypeDef(BaseValidatorModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsOutputTypeDef] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsOutputTypeDef] = None

class RuleGroupVariablesTypeDef(BaseValidatorModel):
    IpSets: Optional[RuleGroupVariablesIpSetsDetailsTypeDef] = None
    PortSets: Optional[RuleGroupVariablesPortSetsDetailsTypeDef] = None

class StandardTypeDef(BaseValidatorModel):
    StandardsArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    EnabledByDefault: Optional[bool] = None
    StandardsManagedBy: Optional[StandardsManagedByTypeDef] = None

class StandardsSubscriptionTypeDef(BaseValidatorModel):
    StandardsSubscriptionArn: str
    StandardsArn: str
    StandardsInput: Dict[str, str]
    StandardsStatus: StandardsStatusType
    StandardsStatusReason: Optional[StandardsStatusReasonTypeDef] = None

class StatelessCustomPublishMetricActionExtraOutputTypeDef(BaseValidatorModel):
    Dimensions: Optional[List[StatelessCustomPublishMetricActionDimensionTypeDef]] = None

class StatelessCustomPublishMetricActionOutputTypeDef(BaseValidatorModel):
    Dimensions: Optional[List[StatelessCustomPublishMetricActionDimensionTypeDef]] = None

class StatelessCustomPublishMetricActionTypeDef(BaseValidatorModel):
    Dimensions: Optional[Sequence[StatelessCustomPublishMetricActionDimensionTypeDef]] = None

class AwsApiCallActionExtraOutputTypeDef(BaseValidatorModel):
    Api: Optional[str] = None
    ServiceName: Optional[str] = None
    CallerType: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None
    DomainDetails: Optional[AwsApiCallActionDomainDetailsTypeDef] = None
    AffectedResources: Optional[Dict[str, str]] = None
    FirstSeen: Optional[str] = None
    LastSeen: Optional[str] = None

class AwsApiCallActionOutputTypeDef(BaseValidatorModel):
    Api: Optional[str] = None
    ServiceName: Optional[str] = None
    CallerType: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None
    DomainDetails: Optional[AwsApiCallActionDomainDetailsTypeDef] = None
    AffectedResources: Optional[Dict[str, str]] = None
    FirstSeen: Optional[str] = None
    LastSeen: Optional[str] = None

class AwsApiCallActionTypeDef(BaseValidatorModel):
    Api: Optional[str] = None
    ServiceName: Optional[str] = None
    CallerType: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None
    DomainDetails: Optional[AwsApiCallActionDomainDetailsTypeDef] = None
    AffectedResources: Optional[Mapping[str, str]] = None
    FirstSeen: Optional[str] = None
    LastSeen: Optional[str] = None

class NetworkConnectionActionTypeDef(BaseValidatorModel):
    ConnectionDirection: Optional[str] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None
    RemotePortDetails: Optional[ActionRemotePortDetailsTypeDef] = None
    LocalPortDetails: Optional[ActionLocalPortDetailsTypeDef] = None
    Protocol: Optional[str] = None
    Blocked: Optional[bool] = None

class PortProbeDetailTypeDef(BaseValidatorModel):
    LocalPortDetails: Optional[ActionLocalPortDetailsTypeDef] = None
    LocalIpDetails: Optional[ActionLocalIpDetailsTypeDef] = None
    RemoteIpDetails: Optional[ActionRemoteIpDetailsTypeDef] = None

class AwsEc2RouteTableDetailsExtraOutputTypeDef(BaseValidatorModel):
    AssociationSet: Optional[List[AssociationSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[List[PropagatingVgwSetDetailsTypeDef]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[List[RouteSetDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AwsEc2RouteTableDetailsOutputTypeDef(BaseValidatorModel):
    AssociationSet: Optional[List[AssociationSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[List[PropagatingVgwSetDetailsTypeDef]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[List[RouteSetDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AwsEc2RouteTableDetailsTypeDef(BaseValidatorModel):
    AssociationSet: Optional[Sequence[AssociationSetDetailsTypeDef]] = None
    OwnerId: Optional[str] = None
    PropagatingVgwSet: Optional[Sequence[PropagatingVgwSetDetailsTypeDef]] = None
    RouteTableId: Optional[str] = None
    RouteSet: Optional[Sequence[RouteSetDetailsTypeDef]] = None
    VpcId: Optional[str] = None

class AutomationRulesActionOutputTypeDef(BaseValidatorModel):
    Type: Optional[Literal["FINDING_FIELDS_UPDATE"]] = None
    FindingFieldsUpdate: Optional[AutomationRulesFindingFieldsUpdateOutputTypeDef] = None

class AutomationRulesActionTypeDef(BaseValidatorModel):
    Type: Optional[Literal["FINDING_FIELDS_UPDATE"]] = None
    FindingFieldsUpdate: Optional[AutomationRulesFindingFieldsUpdateTypeDef] = None

class AwsAmazonMqBrokerDetailsExtraOutputTypeDef(BaseValidatorModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[       AwsAmazonMqBrokerLdapServerMetadataDetailsExtraOutputTypeDef     ] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetailsTypeDef] = None
    MaintenanceWindowStartTime: Optional[       AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef     ] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[List[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    Users: Optional[List[AwsAmazonMqBrokerUsersDetailsTypeDef]] = None

class AwsAmazonMqBrokerDetailsOutputTypeDef(BaseValidatorModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[AwsAmazonMqBrokerLdapServerMetadataDetailsOutputTypeDef] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetailsTypeDef] = None
    MaintenanceWindowStartTime: Optional[       AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef     ] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[List[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    Users: Optional[List[AwsAmazonMqBrokerUsersDetailsTypeDef]] = None

class AwsAmazonMqBrokerDetailsTypeDef(BaseValidatorModel):
    AuthenticationStrategy: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    BrokerArn: Optional[str] = None
    BrokerName: Optional[str] = None
    DeploymentMode: Optional[str] = None
    EncryptionOptions: Optional[AwsAmazonMqBrokerEncryptionOptionsDetailsTypeDef] = None
    EngineType: Optional[str] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    BrokerId: Optional[str] = None
    LdapServerMetadata: Optional[AwsAmazonMqBrokerLdapServerMetadataDetailsTypeDef] = None
    Logs: Optional[AwsAmazonMqBrokerLogsDetailsTypeDef] = None
    MaintenanceWindowStartTime: Optional[       AwsAmazonMqBrokerMaintenanceWindowStartTimeDetailsTypeDef     ] = None
    PubliclyAccessible: Optional[bool] = None
    SecurityGroups: Optional[Sequence[str]] = None
    StorageType: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    Users: Optional[Sequence[AwsAmazonMqBrokerUsersDetailsTypeDef]] = None

class AwsAppSyncGraphQlApiDetailsExtraOutputTypeDef(BaseValidatorModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[       AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef     ] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef] = None
    AdditionalAuthenticationProviders: Optional[       List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]     ] = None
    WafWebAclArn: Optional[str] = None

class AwsAppSyncGraphQlApiDetailsOutputTypeDef(BaseValidatorModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[       AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef     ] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef] = None
    AdditionalAuthenticationProviders: Optional[       List[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]     ] = None
    WafWebAclArn: Optional[str] = None

class AwsAppSyncGraphQlApiDetailsTypeDef(BaseValidatorModel):
    ApiId: Optional[str] = None
    Id: Optional[str] = None
    OpenIdConnectConfig: Optional[AwsAppSyncGraphQlApiOpenIdConnectConfigDetailsTypeDef] = None
    Name: Optional[str] = None
    LambdaAuthorizerConfig: Optional[       AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetailsTypeDef     ] = None
    XrayEnabled: Optional[bool] = None
    Arn: Optional[str] = None
    UserPoolConfig: Optional[AwsAppSyncGraphQlApiUserPoolConfigDetailsTypeDef] = None
    AuthenticationType: Optional[str] = None
    LogConfig: Optional[AwsAppSyncGraphQlApiLogConfigDetailsTypeDef] = None
    AdditionalAuthenticationProviders: Optional[       Sequence[AwsAppSyncGraphQlApiAdditionalAuthenticationProvidersDetailsTypeDef]     ] = None
    WafWebAclArn: Optional[str] = None

class AwsAthenaWorkGroupConfigurationDetailsTypeDef(BaseValidatorModel):
    ResultConfiguration: Optional[       AwsAthenaWorkGroupConfigurationResultConfigurationDetailsTypeDef     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsExtraOutputTypeDef(BaseValidatorModel):
    InstancesDistribution: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsExtraOutputTypeDef     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef(BaseValidatorModel):
    InstancesDistribution: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsOutputTypeDef     ] = None

class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef(BaseValidatorModel):
    InstancesDistribution: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyInstancesDistributionDetailsTypeDef     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateDetailsTypeDef     ] = None

class AwsAutoScalingLaunchConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[       List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]     ] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[       AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef] = None

class AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[       List[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]     ] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[List[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[       AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef] = None

class AwsAutoScalingLaunchConfigurationDetailsTypeDef(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    BlockDeviceMappings: Optional[       Sequence[AwsAutoScalingLaunchConfigurationBlockDeviceMappingsDetailsTypeDef]     ] = None
    ClassicLinkVpcId: Optional[str] = None
    ClassicLinkVpcSecurityGroups: Optional[Sequence[str]] = None
    CreatedTime: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[str] = None
    ImageId: Optional[str] = None
    InstanceMonitoring: Optional[       AwsAutoScalingLaunchConfigurationInstanceMonitoringDetailsTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchConfigurationName: Optional[str] = None
    PlacementTenancy: Optional[str] = None
    RamdiskId: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SpotPrice: Optional[str] = None
    UserData: Optional[str] = None
    MetadataOptions: Optional[AwsAutoScalingLaunchConfigurationMetadataOptionsTypeDef] = None

class AwsBackupBackupPlanRuleDetailsExtraOutputTypeDef(BaseValidatorModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[List[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsTypeDef] = None

class AwsBackupBackupPlanRuleDetailsOutputTypeDef(BaseValidatorModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[List[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsTypeDef] = None

class AwsBackupBackupPlanRuleDetailsTypeDef(BaseValidatorModel):
    TargetBackupVault: Optional[str] = None
    StartWindowMinutes: Optional[int] = None
    ScheduleExpression: Optional[str] = None
    RuleName: Optional[str] = None
    RuleId: Optional[str] = None
    EnableContinuousBackup: Optional[bool] = None
    CompletionWindowMinutes: Optional[int] = None
    CopyActions: Optional[Sequence[AwsBackupBackupPlanRuleCopyActionsDetailsTypeDef]] = None
    Lifecycle: Optional[AwsBackupBackupPlanLifecycleDetailsTypeDef] = None

class AwsCertificateManagerCertificateRenewalSummaryExtraOutputTypeDef(BaseValidatorModel):
    DomainValidationOptions: Optional[       List[AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef]     ] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None

class AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef(BaseValidatorModel):
    DomainValidationOptions: Optional[       List[AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]     ] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None

class AwsCertificateManagerCertificateRenewalSummaryTypeDef(BaseValidatorModel):
    DomainValidationOptions: Optional[       Sequence[AwsCertificateManagerCertificateDomainValidationOptionTypeDef]     ] = None
    RenewalStatus: Optional[str] = None
    RenewalStatusReason: Optional[str] = None
    UpdatedAt: Optional[str] = None

class AwsCloudFrontDistributionOriginItemExtraOutputTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[       AwsCloudFrontDistributionOriginCustomOriginConfigExtraOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginItemOutputTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[       AwsCloudFrontDistributionOriginCustomOriginConfigOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginItemTypeDef(BaseValidatorModel):
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    OriginPath: Optional[str] = None
    S3OriginConfig: Optional[AwsCloudFrontDistributionOriginS3OriginConfigTypeDef] = None
    CustomOriginConfig: Optional[AwsCloudFrontDistributionOriginCustomOriginConfigTypeDef] = None

class AwsCloudFrontDistributionOriginGroupExtraOutputTypeDef(BaseValidatorModel):
    FailoverCriteria: Optional[       AwsCloudFrontDistributionOriginGroupFailoverExtraOutputTypeDef     ] = None

class AwsCloudFrontDistributionOriginGroupOutputTypeDef(BaseValidatorModel):
    FailoverCriteria: Optional[AwsCloudFrontDistributionOriginGroupFailoverOutputTypeDef] = None

class AwsCloudFrontDistributionOriginGroupTypeDef(BaseValidatorModel):
    FailoverCriteria: Optional[AwsCloudFrontDistributionOriginGroupFailoverTypeDef] = None

class AwsCodeBuildProjectDetailsExtraOutputTypeDef(BaseValidatorModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentExtraOutputTypeDef] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSourceTypeDef] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetailsTypeDef] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigExtraOutputTypeDef] = None
    SecondaryArtifacts: Optional[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None

class AwsCodeBuildProjectDetailsOutputTypeDef(BaseValidatorModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentOutputTypeDef] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSourceTypeDef] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetailsTypeDef] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigOutputTypeDef] = None
    SecondaryArtifacts: Optional[List[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None

class AwsCodeBuildProjectDetailsTypeDef(BaseValidatorModel):
    EncryptionKey: Optional[str] = None
    Artifacts: Optional[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None
    Environment: Optional[AwsCodeBuildProjectEnvironmentTypeDef] = None
    Name: Optional[str] = None
    Source: Optional[AwsCodeBuildProjectSourceTypeDef] = None
    ServiceRole: Optional[str] = None
    LogsConfig: Optional[AwsCodeBuildProjectLogsConfigDetailsTypeDef] = None
    VpcConfig: Optional[AwsCodeBuildProjectVpcConfigTypeDef] = None
    SecondaryArtifacts: Optional[Sequence[AwsCodeBuildProjectArtifactsDetailsTypeDef]] = None

class AwsDynamoDbTableReplicaExtraOutputTypeDef(BaseValidatorModel):
    GlobalSecondaryIndexes: Optional[       List[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]     ] = None
    KmsMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[       AwsDynamoDbTableProvisionedThroughputOverrideTypeDef     ] = None
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[str] = None
    ReplicaStatusDescription: Optional[str] = None

class AwsDynamoDbTableReplicaOutputTypeDef(BaseValidatorModel):
    GlobalSecondaryIndexes: Optional[       List[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]     ] = None
    KmsMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[       AwsDynamoDbTableProvisionedThroughputOverrideTypeDef     ] = None
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[str] = None
    ReplicaStatusDescription: Optional[str] = None

class AwsDynamoDbTableReplicaTypeDef(BaseValidatorModel):
    GlobalSecondaryIndexes: Optional[       Sequence[AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef]     ] = None
    KmsMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[       AwsDynamoDbTableProvisionedThroughputOverrideTypeDef     ] = None
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[str] = None
    ReplicaStatusDescription: Optional[str] = None

class AwsEc2ClientVpnEndpointDetailsExtraOutputTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[       List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]     ] = None
    ConnectionLogOptions: Optional[       AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef     ] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[       AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef     ] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[       AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef     ] = None

class AwsEc2ClientVpnEndpointDetailsOutputTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[       List[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]     ] = None
    ConnectionLogOptions: Optional[       AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef     ] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[       AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef     ] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[       AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef     ] = None

class AwsEc2ClientVpnEndpointDetailsTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServer: Optional[Sequence[str]] = None
    SplitTunnel: Optional[bool] = None
    TransportProtocol: Optional[str] = None
    VpnPort: Optional[int] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[       Sequence[AwsEc2ClientVpnEndpointAuthenticationOptionsDetailsTypeDef]     ] = None
    ConnectionLogOptions: Optional[       AwsEc2ClientVpnEndpointConnectionLogOptionsDetailsTypeDef     ] = None
    SecurityGroupIdSet: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[       AwsEc2ClientVpnEndpointClientConnectOptionsDetailsTypeDef     ] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[       AwsEc2ClientVpnEndpointClientLoginBannerOptionsDetailsTypeDef     ] = None

class AwsEc2LaunchTemplateDataDetailsExtraOutputTypeDef(BaseValidatorModel):
    BlockDeviceMappingSet: Optional[       List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]     ] = None
    CapacityReservationSpecification: Optional[       AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef     ] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef] = None
    CreditSpecification: Optional[       AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef     ] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[       List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]     ] = None
    ElasticInferenceAcceleratorSet: Optional[       List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]     ] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[       AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef     ] = None
    InstanceRequirements: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsDetailsExtraOutputTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[List[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef] = None
    NetworkInterfaceSet: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsExtraOutputTypeDef]     ] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef] = None
    PrivateDnsNameOptions: Optional[       AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef     ] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    SecurityGroupSet: Optional[List[str]] = None
    UserData: Optional[str] = None

class AwsEc2LaunchTemplateDataDetailsOutputTypeDef(BaseValidatorModel):
    BlockDeviceMappingSet: Optional[       List[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]     ] = None
    CapacityReservationSpecification: Optional[       AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef     ] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef] = None
    CreditSpecification: Optional[       AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef     ] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[       List[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]     ] = None
    ElasticInferenceAcceleratorSet: Optional[       List[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]     ] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[       AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef     ] = None
    InstanceRequirements: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsDetailsOutputTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[List[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef] = None
    NetworkInterfaceSet: Optional[       List[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsOutputTypeDef]     ] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef] = None
    PrivateDnsNameOptions: Optional[       AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef     ] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[List[str]] = None
    SecurityGroupSet: Optional[List[str]] = None
    UserData: Optional[str] = None

class AwsEc2LaunchTemplateDataDetailsTypeDef(BaseValidatorModel):
    BlockDeviceMappingSet: Optional[       Sequence[AwsEc2LaunchTemplateDataBlockDeviceMappingSetDetailsTypeDef]     ] = None
    CapacityReservationSpecification: Optional[       AwsEc2LaunchTemplateDataCapacityReservationSpecificationDetailsTypeDef     ] = None
    CpuOptions: Optional[AwsEc2LaunchTemplateDataCpuOptionsDetailsTypeDef] = None
    CreditSpecification: Optional[       AwsEc2LaunchTemplateDataCreditSpecificationDetailsTypeDef     ] = None
    DisableApiStop: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    ElasticGpuSpecificationSet: Optional[       Sequence[AwsEc2LaunchTemplateDataElasticGpuSpecificationSetDetailsTypeDef]     ] = None
    ElasticInferenceAcceleratorSet: Optional[       Sequence[AwsEc2LaunchTemplateDataElasticInferenceAcceleratorSetDetailsTypeDef]     ] = None
    EnclaveOptions: Optional[AwsEc2LaunchTemplateDataEnclaveOptionsDetailsTypeDef] = None
    HibernationOptions: Optional[AwsEc2LaunchTemplateDataHibernationOptionsDetailsTypeDef] = None
    IamInstanceProfile: Optional[AwsEc2LaunchTemplateDataIamInstanceProfileDetailsTypeDef] = None
    ImageId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[str] = None
    InstanceMarketOptions: Optional[       AwsEc2LaunchTemplateDataInstanceMarketOptionsDetailsTypeDef     ] = None
    InstanceRequirements: Optional[       AwsEc2LaunchTemplateDataInstanceRequirementsDetailsTypeDef     ] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LicenseSet: Optional[Sequence[AwsEc2LaunchTemplateDataLicenseSetDetailsTypeDef]] = None
    MaintenanceOptions: Optional[AwsEc2LaunchTemplateDataMaintenanceOptionsDetailsTypeDef] = None
    MetadataOptions: Optional[AwsEc2LaunchTemplateDataMetadataOptionsDetailsTypeDef] = None
    Monitoring: Optional[AwsEc2LaunchTemplateDataMonitoringDetailsTypeDef] = None
    NetworkInterfaceSet: Optional[       Sequence[AwsEc2LaunchTemplateDataNetworkInterfaceSetDetailsTypeDef]     ] = None
    Placement: Optional[AwsEc2LaunchTemplateDataPlacementDetailsTypeDef] = None
    PrivateDnsNameOptions: Optional[       AwsEc2LaunchTemplateDataPrivateDnsNameOptionsDetailsTypeDef     ] = None
    RamDiskId: Optional[str] = None
    SecurityGroupIdSet: Optional[Sequence[str]] = None
    SecurityGroupSet: Optional[Sequence[str]] = None
    UserData: Optional[str] = None

class AwsEc2NetworkAclDetailsExtraOutputTypeDef(BaseValidatorModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[List[AwsEc2NetworkAclAssociationTypeDef]] = None
    Entries: Optional[List[AwsEc2NetworkAclEntryTypeDef]] = None

class AwsEc2NetworkAclDetailsOutputTypeDef(BaseValidatorModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[List[AwsEc2NetworkAclAssociationTypeDef]] = None
    Entries: Optional[List[AwsEc2NetworkAclEntryTypeDef]] = None

class AwsEc2NetworkAclDetailsTypeDef(BaseValidatorModel):
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    Associations: Optional[Sequence[AwsEc2NetworkAclAssociationTypeDef]] = None
    Entries: Optional[Sequence[AwsEc2NetworkAclEntryTypeDef]] = None

class AwsEc2SecurityGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[List[AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef]] = None
    IpPermissionsEgress: Optional[List[AwsEc2SecurityGroupIpPermissionExtraOutputTypeDef]] = None

class AwsEc2SecurityGroupDetailsOutputTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[List[AwsEc2SecurityGroupIpPermissionOutputTypeDef]] = None
    IpPermissionsEgress: Optional[List[AwsEc2SecurityGroupIpPermissionOutputTypeDef]] = None

class AwsEc2SecurityGroupDetailsTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    OwnerId: Optional[str] = None
    VpcId: Optional[str] = None
    IpPermissions: Optional[Sequence[AwsEc2SecurityGroupIpPermissionTypeDef]] = None
    IpPermissionsEgress: Optional[Sequence[AwsEc2SecurityGroupIpPermissionTypeDef]] = None

class AwsEc2VpcPeeringConnectionDetailsExtraOutputTypeDef(BaseValidatorModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsExtraOutputTypeDef] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef] = None
    VpcPeeringConnectionId: Optional[str] = None

class AwsEc2VpcPeeringConnectionDetailsOutputTypeDef(BaseValidatorModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsOutputTypeDef] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef] = None
    VpcPeeringConnectionId: Optional[str] = None

class AwsEc2VpcPeeringConnectionDetailsTypeDef(BaseValidatorModel):
    AccepterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef] = None
    ExpirationTime: Optional[str] = None
    RequesterVpcInfo: Optional[AwsEc2VpcPeeringConnectionVpcInfoDetailsTypeDef] = None
    Status: Optional[AwsEc2VpcPeeringConnectionStatusDetailsTypeDef] = None
    VpcPeeringConnectionId: Optional[str] = None

class AwsEc2VpnConnectionDetailsExtraOutputTypeDef(BaseValidatorModel):
    VpnConnectionId: Optional[str] = None
    State: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    Category: Optional[str] = None
    VgwTelemetry: Optional[List[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]] = None
    Options: Optional[AwsEc2VpnConnectionOptionsDetailsExtraOutputTypeDef] = None
    Routes: Optional[List[AwsEc2VpnConnectionRoutesDetailsTypeDef]] = None
    TransitGatewayId: Optional[str] = None

class AwsEc2VpnConnectionDetailsOutputTypeDef(BaseValidatorModel):
    VpnConnectionId: Optional[str] = None
    State: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    Category: Optional[str] = None
    VgwTelemetry: Optional[List[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]] = None
    Options: Optional[AwsEc2VpnConnectionOptionsDetailsOutputTypeDef] = None
    Routes: Optional[List[AwsEc2VpnConnectionRoutesDetailsTypeDef]] = None
    TransitGatewayId: Optional[str] = None

class AwsEc2VpnConnectionDetailsTypeDef(BaseValidatorModel):
    VpnConnectionId: Optional[str] = None
    State: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    Category: Optional[str] = None
    VgwTelemetry: Optional[Sequence[AwsEc2VpnConnectionVgwTelemetryDetailsTypeDef]] = None
    Options: Optional[AwsEc2VpnConnectionOptionsDetailsTypeDef] = None
    Routes: Optional[Sequence[AwsEc2VpnConnectionRoutesDetailsTypeDef]] = None
    TransitGatewayId: Optional[str] = None

class AwsEcsClusterConfigurationDetailsTypeDef(BaseValidatorModel):
    ExecuteCommandConfiguration: Optional[       AwsEcsClusterConfigurationExecuteCommandConfigurationDetailsTypeDef     ] = None

class AwsEcsServiceDetailsExtraOutputTypeDef(BaseValidatorModel):
    CapacityProviderStrategy: Optional[       List[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]     ] = None
    Cluster: Optional[str] = None
    DeploymentConfiguration: Optional[AwsEcsServiceDeploymentConfigurationDetailsTypeDef] = None
    DeploymentController: Optional[AwsEcsServiceDeploymentControllerDetailsTypeDef] = None
    DesiredCount: Optional[int] = None
    EnableEcsManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    HealthCheckGracePeriodSeconds: Optional[int] = None
    LaunchType: Optional[str] = None
    LoadBalancers: Optional[List[AwsEcsServiceLoadBalancersDetailsTypeDef]] = None
    Name: Optional[str] = None
    NetworkConfiguration: Optional[       AwsEcsServiceNetworkConfigurationDetailsExtraOutputTypeDef     ] = None
    PlacementConstraints: Optional[List[AwsEcsServicePlacementConstraintsDetailsTypeDef]] = None
    PlacementStrategies: Optional[List[AwsEcsServicePlacementStrategiesDetailsTypeDef]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[str] = None
    Role: Optional[str] = None
    SchedulingStrategy: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceRegistries: Optional[List[AwsEcsServiceServiceRegistriesDetailsTypeDef]] = None
    TaskDefinition: Optional[str] = None

class AwsEcsServiceDetailsOutputTypeDef(BaseValidatorModel):
    CapacityProviderStrategy: Optional[       List[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]     ] = None
    Cluster: Optional[str] = None
    DeploymentConfiguration: Optional[AwsEcsServiceDeploymentConfigurationDetailsTypeDef] = None
    DeploymentController: Optional[AwsEcsServiceDeploymentControllerDetailsTypeDef] = None
    DesiredCount: Optional[int] = None
    EnableEcsManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    HealthCheckGracePeriodSeconds: Optional[int] = None
    LaunchType: Optional[str] = None
    LoadBalancers: Optional[List[AwsEcsServiceLoadBalancersDetailsTypeDef]] = None
    Name: Optional[str] = None
    NetworkConfiguration: Optional[AwsEcsServiceNetworkConfigurationDetailsOutputTypeDef] = None
    PlacementConstraints: Optional[List[AwsEcsServicePlacementConstraintsDetailsTypeDef]] = None
    PlacementStrategies: Optional[List[AwsEcsServicePlacementStrategiesDetailsTypeDef]] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[str] = None
    Role: Optional[str] = None
    SchedulingStrategy: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceRegistries: Optional[List[AwsEcsServiceServiceRegistriesDetailsTypeDef]] = None
    TaskDefinition: Optional[str] = None

class AwsEcsServiceDetailsTypeDef(BaseValidatorModel):
    CapacityProviderStrategy: Optional[       Sequence[AwsEcsServiceCapacityProviderStrategyDetailsTypeDef]     ] = None
    Cluster: Optional[str] = None
    DeploymentConfiguration: Optional[AwsEcsServiceDeploymentConfigurationDetailsTypeDef] = None
    DeploymentController: Optional[AwsEcsServiceDeploymentControllerDetailsTypeDef] = None
    DesiredCount: Optional[int] = None
    EnableEcsManagedTags: Optional[bool] = None
    EnableExecuteCommand: Optional[bool] = None
    HealthCheckGracePeriodSeconds: Optional[int] = None
    LaunchType: Optional[str] = None
    LoadBalancers: Optional[Sequence[AwsEcsServiceLoadBalancersDetailsTypeDef]] = None
    Name: Optional[str] = None
    NetworkConfiguration: Optional[AwsEcsServiceNetworkConfigurationDetailsTypeDef] = None
    PlacementConstraints: Optional[       Sequence[AwsEcsServicePlacementConstraintsDetailsTypeDef]     ] = None
    PlacementStrategies: Optional[       Sequence[AwsEcsServicePlacementStrategiesDetailsTypeDef]     ] = None
    PlatformVersion: Optional[str] = None
    PropagateTags: Optional[str] = None
    Role: Optional[str] = None
    SchedulingStrategy: Optional[str] = None
    ServiceArn: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceRegistries: Optional[Sequence[AwsEcsServiceServiceRegistriesDetailsTypeDef]] = None
    TaskDefinition: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsDetailsExtraOutputTypeDef(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]     ] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[List[str]] = None
    DnsServers: Optional[List[str]] = None
    DockerLabels: Optional[Dict[str, str]] = None
    DockerSecurityOptions: Optional[List[str]] = None
    EntryPoint: Optional[List[str]] = None
    Environment: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]     ] = None
    EnvironmentFiles: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]     ] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]     ] = None
    FirelensConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsExtraOutputTypeDef     ] = None
    HealthCheck: Optional[       AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsExtraOutputTypeDef     ] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[List[str]] = None
    LinuxParameters: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsExtraOutputTypeDef     ] = None
    LogConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsExtraOutputTypeDef     ] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]     ] = None
    Name: Optional[str] = None
    PortMappings: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]     ] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[       AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef     ] = None
    ResourceRequirements: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]     ] = None
    Secrets: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]     ] = None
    Ulimits: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]] = None
    User: Optional[str] = None
    VolumesFrom: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]     ] = None
    WorkingDirectory: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef(BaseValidatorModel):
    Command: Optional[List[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]     ] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[List[str]] = None
    DnsServers: Optional[List[str]] = None
    DockerLabels: Optional[Dict[str, str]] = None
    DockerSecurityOptions: Optional[List[str]] = None
    EntryPoint: Optional[List[str]] = None
    Environment: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]     ] = None
    EnvironmentFiles: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]     ] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]     ] = None
    FirelensConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsOutputTypeDef     ] = None
    HealthCheck: Optional[       AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsOutputTypeDef     ] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[List[str]] = None
    LinuxParameters: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsOutputTypeDef     ] = None
    LogConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsOutputTypeDef     ] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]     ] = None
    Name: Optional[str] = None
    PortMappings: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]     ] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[       AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef     ] = None
    ResourceRequirements: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]     ] = None
    Secrets: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]     ] = None
    Ulimits: Optional[List[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]] = None
    User: Optional[str] = None
    VolumesFrom: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]     ] = None
    WorkingDirectory: Optional[str] = None

class AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef(BaseValidatorModel):
    Command: Optional[Sequence[str]] = None
    Cpu: Optional[int] = None
    DependsOn: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsDependsOnDetailsTypeDef]     ] = None
    DisableNetworking: Optional[bool] = None
    DnsSearchDomains: Optional[Sequence[str]] = None
    DnsServers: Optional[Sequence[str]] = None
    DockerLabels: Optional[Mapping[str, str]] = None
    DockerSecurityOptions: Optional[Sequence[str]] = None
    EntryPoint: Optional[Sequence[str]] = None
    Environment: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentDetailsTypeDef]     ] = None
    EnvironmentFiles: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsEnvironmentFilesDetailsTypeDef]     ] = None
    Essential: Optional[bool] = None
    ExtraHosts: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsExtraHostsDetailsTypeDef]     ] = None
    FirelensConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsFirelensConfigurationDetailsTypeDef     ] = None
    HealthCheck: Optional[       AwsEcsTaskDefinitionContainerDefinitionsHealthCheckDetailsTypeDef     ] = None
    Hostname: Optional[str] = None
    Image: Optional[str] = None
    Interactive: Optional[bool] = None
    Links: Optional[Sequence[str]] = None
    LinuxParameters: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLinuxParametersDetailsTypeDef     ] = None
    LogConfiguration: Optional[       AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetailsTypeDef     ] = None
    Memory: Optional[int] = None
    MemoryReservation: Optional[int] = None
    MountPoints: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsMountPointsDetailsTypeDef]     ] = None
    Name: Optional[str] = None
    PortMappings: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetailsTypeDef]     ] = None
    Privileged: Optional[bool] = None
    PseudoTerminal: Optional[bool] = None
    ReadonlyRootFilesystem: Optional[bool] = None
    RepositoryCredentials: Optional[       AwsEcsTaskDefinitionContainerDefinitionsRepositoryCredentialsDetailsTypeDef     ] = None
    ResourceRequirements: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsResourceRequirementsDetailsTypeDef]     ] = None
    Secrets: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsSecretsDetailsTypeDef]     ] = None
    StartTimeout: Optional[int] = None
    StopTimeout: Optional[int] = None
    SystemControls: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsSystemControlsDetailsTypeDef]     ] = None
    Ulimits: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetailsTypeDef]     ] = None
    User: Optional[str] = None
    VolumesFrom: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetailsTypeDef]     ] = None
    WorkingDirectory: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDetailsExtraOutputTypeDef(BaseValidatorModel):
    DockerVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsExtraOutputTypeDef     ] = None
    EfsVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef     ] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef] = None
    Name: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef(BaseValidatorModel):
    DockerVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsOutputTypeDef     ] = None
    EfsVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef     ] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef] = None
    Name: Optional[str] = None

class AwsEcsTaskDefinitionVolumesDetailsTypeDef(BaseValidatorModel):
    DockerVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetailsTypeDef     ] = None
    EfsVolumeConfiguration: Optional[       AwsEcsTaskDefinitionVolumesEfsVolumeConfigurationDetailsTypeDef     ] = None
    Host: Optional[AwsEcsTaskDefinitionVolumesHostDetailsTypeDef] = None
    Name: Optional[str] = None

class AwsEcsTaskDetailsExtraOutputTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskVolumeDetailsTypeDef]] = None
    Containers: Optional[List[AwsEcsContainerDetailsExtraOutputTypeDef]] = None

class AwsEcsTaskDetailsOutputTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskVolumeDetailsTypeDef]] = None
    Containers: Optional[List[AwsEcsContainerDetailsOutputTypeDef]] = None

class AwsEcsTaskDetailsTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    TaskDefinitionArn: Optional[str] = None
    Version: Optional[str] = None
    CreatedAt: Optional[str] = None
    StartedAt: Optional[str] = None
    StartedBy: Optional[str] = None
    Group: Optional[str] = None
    Volumes: Optional[Sequence[AwsEcsTaskVolumeDetailsTypeDef]] = None
    Containers: Optional[Sequence[AwsEcsContainerDetailsTypeDef]] = None

class AwsEfsAccessPointDetailsExtraOutputTypeDef(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsExtraOutputTypeDef] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetailsTypeDef] = None

class AwsEfsAccessPointDetailsOutputTypeDef(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsOutputTypeDef] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetailsTypeDef] = None

class AwsEfsAccessPointDetailsTypeDef(BaseValidatorModel):
    AccessPointId: Optional[str] = None
    Arn: Optional[str] = None
    ClientToken: Optional[str] = None
    FileSystemId: Optional[str] = None
    PosixUser: Optional[AwsEfsAccessPointPosixUserDetailsTypeDef] = None
    RootDirectory: Optional[AwsEfsAccessPointRootDirectoryDetailsTypeDef] = None

class AwsEksClusterDetailsExtraOutputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsExtraOutputTypeDef] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsExtraOutputTypeDef] = None

class AwsEksClusterDetailsOutputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsOutputTypeDef] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsOutputTypeDef] = None

class AwsEksClusterDetailsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    CertificateAuthorityData: Optional[str] = None
    ClusterStatus: Optional[str] = None
    Endpoint: Optional[str] = None
    Name: Optional[str] = None
    ResourcesVpcConfig: Optional[AwsEksClusterResourcesVpcConfigDetailsTypeDef] = None
    RoleArn: Optional[str] = None
    Version: Optional[str] = None
    Logging: Optional[AwsEksClusterLoggingDetailsTypeDef] = None

class AwsElasticsearchDomainDetailsExtraOutputTypeDef(BaseValidatorModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptionsTypeDef] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[       AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef     ] = None
    EncryptionAtRestOptions: Optional[       AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef     ] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[       AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsExtraOutputTypeDef] = None

class AwsElasticsearchDomainDetailsOutputTypeDef(BaseValidatorModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptionsTypeDef] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Dict[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[       AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef     ] = None
    EncryptionAtRestOptions: Optional[       AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef     ] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[       AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsOutputTypeDef] = None

class AwsElasticsearchDomainDetailsTypeDef(BaseValidatorModel):
    AccessPolicies: Optional[str] = None
    DomainEndpointOptions: Optional[AwsElasticsearchDomainDomainEndpointOptionsTypeDef] = None
    DomainId: Optional[str] = None
    DomainName: Optional[str] = None
    Endpoint: Optional[str] = None
    Endpoints: Optional[Mapping[str, str]] = None
    ElasticsearchVersion: Optional[str] = None
    ElasticsearchClusterConfig: Optional[       AwsElasticsearchDomainElasticsearchClusterConfigDetailsTypeDef     ] = None
    EncryptionAtRestOptions: Optional[       AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef     ] = None
    LogPublishingOptions: Optional[AwsElasticsearchDomainLogPublishingOptionsTypeDef] = None
    NodeToNodeEncryptionOptions: Optional[       AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[AwsElasticsearchDomainServiceSoftwareOptionsTypeDef] = None
    VPCOptions: Optional[AwsElasticsearchDomainVPCOptionsTypeDef] = None

class AwsElbLoadBalancerDetailsExtraOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    BackendServerDescriptions: Optional[       List[AwsElbLoadBalancerBackendServerDescriptionExtraOutputTypeDef]     ] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheckTypeDef] = None
    Instances: Optional[List[AwsElbLoadBalancerInstanceTypeDef]] = None
    ListenerDescriptions: Optional[       List[AwsElbLoadBalancerListenerDescriptionExtraOutputTypeDef]     ] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesExtraOutputTypeDef] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesExtraOutputTypeDef] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroupTypeDef] = None
    Subnets: Optional[List[str]] = None
    VpcId: Optional[str] = None

class AwsElbLoadBalancerDetailsOutputTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    BackendServerDescriptions: Optional[       List[AwsElbLoadBalancerBackendServerDescriptionOutputTypeDef]     ] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheckTypeDef] = None
    Instances: Optional[List[AwsElbLoadBalancerInstanceTypeDef]] = None
    ListenerDescriptions: Optional[       List[AwsElbLoadBalancerListenerDescriptionOutputTypeDef]     ] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesOutputTypeDef] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesOutputTypeDef] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[List[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroupTypeDef] = None
    Subnets: Optional[List[str]] = None
    VpcId: Optional[str] = None

class AwsElbLoadBalancerDetailsTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[Sequence[str]] = None
    BackendServerDescriptions: Optional[       Sequence[AwsElbLoadBalancerBackendServerDescriptionTypeDef]     ] = None
    CanonicalHostedZoneName: Optional[str] = None
    CanonicalHostedZoneNameID: Optional[str] = None
    CreatedTime: Optional[str] = None
    DnsName: Optional[str] = None
    HealthCheck: Optional[AwsElbLoadBalancerHealthCheckTypeDef] = None
    Instances: Optional[Sequence[AwsElbLoadBalancerInstanceTypeDef]] = None
    ListenerDescriptions: Optional[Sequence[AwsElbLoadBalancerListenerDescriptionTypeDef]] = None
    LoadBalancerAttributes: Optional[AwsElbLoadBalancerAttributesTypeDef] = None
    LoadBalancerName: Optional[str] = None
    Policies: Optional[AwsElbLoadBalancerPoliciesTypeDef] = None
    Scheme: Optional[str] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SourceSecurityGroup: Optional[AwsElbLoadBalancerSourceSecurityGroupTypeDef] = None
    Subnets: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None

class AwsEventsEndpointRoutingConfigDetailsTypeDef(BaseValidatorModel):
    FailoverConfig: Optional[AwsEventsEndpointRoutingConfigFailoverConfigDetailsTypeDef] = None

class AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef(BaseValidatorModel):
    ScanEc2InstanceWithFindings: Optional[       AwsGuardDutyDetectorDataSourcesMalwareProtectionScanEc2InstanceWithFindingsDetailsTypeDef     ] = None
    ServiceRole: Optional[str] = None

class AwsIamAccessKeyDetailsTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Status: Optional[AwsIamAccessKeyStatusType] = None
    CreatedAt: Optional[str] = None
    PrincipalId: Optional[str] = None
    PrincipalType: Optional[str] = None
    PrincipalName: Optional[str] = None
    AccountId: Optional[str] = None
    AccessKeyId: Optional[str] = None
    SessionContext: Optional[AwsIamAccessKeySessionContextTypeDef] = None

class AwsIamRoleDetailsExtraOutputTypeDef(BaseValidatorModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[List[AwsIamInstanceProfileExtraOutputTypeDef]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[List[AwsIamRolePolicyTypeDef]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None

class AwsIamRoleDetailsOutputTypeDef(BaseValidatorModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[List[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[List[AwsIamInstanceProfileOutputTypeDef]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[List[AwsIamRolePolicyTypeDef]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None

class AwsIamRoleDetailsTypeDef(BaseValidatorModel):
    AssumeRolePolicyDocument: Optional[str] = None
    AttachedManagedPolicies: Optional[Sequence[AwsIamAttachedManagedPolicyTypeDef]] = None
    CreateDate: Optional[str] = None
    InstanceProfileList: Optional[Sequence[AwsIamInstanceProfileTypeDef]] = None
    PermissionsBoundary: Optional[AwsIamPermissionsBoundaryTypeDef] = None
    RoleId: Optional[str] = None
    RoleName: Optional[str] = None
    RolePolicyList: Optional[Sequence[AwsIamRolePolicyTypeDef]] = None
    MaxSessionDuration: Optional[int] = None
    Path: Optional[str] = None

class AwsLambdaFunctionDetailsExtraOutputTypeDef(BaseValidatorModel):
    Code: Optional[AwsLambdaFunctionCodeTypeDef] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfigTypeDef] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentExtraOutputTypeDef] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[List[AwsLambdaFunctionLayerTypeDef]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfigTypeDef] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigExtraOutputTypeDef] = None
    Version: Optional[str] = None
    Architectures: Optional[List[str]] = None
    PackageType: Optional[str] = None

class AwsLambdaFunctionDetailsOutputTypeDef(BaseValidatorModel):
    Code: Optional[AwsLambdaFunctionCodeTypeDef] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfigTypeDef] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentOutputTypeDef] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[List[AwsLambdaFunctionLayerTypeDef]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfigTypeDef] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigOutputTypeDef] = None
    Version: Optional[str] = None
    Architectures: Optional[List[str]] = None
    PackageType: Optional[str] = None

class AwsLambdaFunctionDetailsTypeDef(BaseValidatorModel):
    Code: Optional[AwsLambdaFunctionCodeTypeDef] = None
    CodeSha256: Optional[str] = None
    DeadLetterConfig: Optional[AwsLambdaFunctionDeadLetterConfigTypeDef] = None
    Environment: Optional[AwsLambdaFunctionEnvironmentTypeDef] = None
    FunctionName: Optional[str] = None
    Handler: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    LastModified: Optional[str] = None
    Layers: Optional[Sequence[AwsLambdaFunctionLayerTypeDef]] = None
    MasterArn: Optional[str] = None
    MemorySize: Optional[int] = None
    RevisionId: Optional[str] = None
    Role: Optional[str] = None
    Runtime: Optional[str] = None
    Timeout: Optional[int] = None
    TracingConfig: Optional[AwsLambdaFunctionTracingConfigTypeDef] = None
    VpcConfig: Optional[AwsLambdaFunctionVpcConfigTypeDef] = None
    Version: Optional[str] = None
    Architectures: Optional[Sequence[str]] = None
    PackageType: Optional[str] = None

class AwsMskClusterClusterInfoClientAuthenticationDetailsExtraOutputTypeDef(BaseValidatorModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef] = None
    Unauthenticated: Optional[       AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef     ] = None
    Tls: Optional[       AwsMskClusterClusterInfoClientAuthenticationTlsDetailsExtraOutputTypeDef     ] = None

class AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef(BaseValidatorModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef] = None
    Unauthenticated: Optional[       AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef     ] = None
    Tls: Optional[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsOutputTypeDef] = None

class AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef(BaseValidatorModel):
    Sasl: Optional[AwsMskClusterClusterInfoClientAuthenticationSaslDetailsTypeDef] = None
    Unauthenticated: Optional[       AwsMskClusterClusterInfoClientAuthenticationUnauthenticatedDetailsTypeDef     ] = None
    Tls: Optional[AwsMskClusterClusterInfoClientAuthenticationTlsDetailsTypeDef] = None

class AwsOpenSearchServiceDomainDetailsExtraOutputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[       AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef     ] = None
    NodeToNodeEncryptionOptions: Optional[       AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[       AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef     ] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef] = None
    DomainEndpointOptions: Optional[       AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef     ] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsExtraOutputTypeDef] = None
    LogPublishingOptions: Optional[       AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef     ] = None
    DomainEndpoints: Optional[Dict[str, str]] = None
    AdvancedSecurityOptions: Optional[       AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef     ] = None

class AwsOpenSearchServiceDomainDetailsOutputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[       AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef     ] = None
    NodeToNodeEncryptionOptions: Optional[       AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[       AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef     ] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef] = None
    DomainEndpointOptions: Optional[       AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef     ] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsOutputTypeDef] = None
    LogPublishingOptions: Optional[       AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef     ] = None
    DomainEndpoints: Optional[Dict[str, str]] = None
    AdvancedSecurityOptions: Optional[       AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef     ] = None

class AwsOpenSearchServiceDomainDetailsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    AccessPolicies: Optional[str] = None
    DomainName: Optional[str] = None
    Id: Optional[str] = None
    DomainEndpoint: Optional[str] = None
    EngineVersion: Optional[str] = None
    EncryptionAtRestOptions: Optional[       AwsOpenSearchServiceDomainEncryptionAtRestOptionsDetailsTypeDef     ] = None
    NodeToNodeEncryptionOptions: Optional[       AwsOpenSearchServiceDomainNodeToNodeEncryptionOptionsDetailsTypeDef     ] = None
    ServiceSoftwareOptions: Optional[       AwsOpenSearchServiceDomainServiceSoftwareOptionsDetailsTypeDef     ] = None
    ClusterConfig: Optional[AwsOpenSearchServiceDomainClusterConfigDetailsTypeDef] = None
    DomainEndpointOptions: Optional[       AwsOpenSearchServiceDomainDomainEndpointOptionsDetailsTypeDef     ] = None
    VpcOptions: Optional[AwsOpenSearchServiceDomainVpcOptionsDetailsTypeDef] = None
    LogPublishingOptions: Optional[       AwsOpenSearchServiceDomainLogPublishingOptionsDetailsTypeDef     ] = None
    DomainEndpoints: Optional[Mapping[str, str]] = None
    AdvancedSecurityOptions: Optional[       AwsOpenSearchServiceDomainAdvancedSecurityOptionsDetailsTypeDef     ] = None

class AwsRdsDbSubnetGroupExtraOutputTypeDef(BaseValidatorModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[AwsRdsDbSubnetGroupSubnetTypeDef]] = None
    DbSubnetGroupArn: Optional[str] = None

class AwsRdsDbSubnetGroupOutputTypeDef(BaseValidatorModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[AwsRdsDbSubnetGroupSubnetTypeDef]] = None
    DbSubnetGroupArn: Optional[str] = None

class AwsRdsDbSubnetGroupTypeDef(BaseValidatorModel):
    DbSubnetGroupName: Optional[str] = None
    DbSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[Sequence[AwsRdsDbSubnetGroupSubnetTypeDef]] = None
    DbSubnetGroupArn: Optional[str] = None

class AwsRedshiftClusterDetailsExtraOutputTypeDef(BaseValidatorModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[List[AwsRedshiftClusterClusterNodeTypeDef]] = None
    ClusterParameterGroups: Optional[       List[AwsRedshiftClusterClusterParameterGroupExtraOutputTypeDef]     ] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[List[AwsRedshiftClusterClusterSecurityGroupTypeDef]] = None
    ClusterSnapshotCopyStatus: Optional[       AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef     ] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[       List[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]     ] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatusTypeDef] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpointTypeDef] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatusTypeDef] = None
    IamRoles: Optional[List[AwsRedshiftClusterIamRoleTypeDef]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[List[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValuesTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfoTypeDef] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatusTypeDef] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRedshiftClusterVpcSecurityGroupTypeDef]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatusTypeDef] = None

class AwsRedshiftClusterDetailsOutputTypeDef(BaseValidatorModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[List[AwsRedshiftClusterClusterNodeTypeDef]] = None
    ClusterParameterGroups: Optional[       List[AwsRedshiftClusterClusterParameterGroupOutputTypeDef]     ] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[List[AwsRedshiftClusterClusterSecurityGroupTypeDef]] = None
    ClusterSnapshotCopyStatus: Optional[       AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef     ] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[       List[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]     ] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatusTypeDef] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpointTypeDef] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatusTypeDef] = None
    IamRoles: Optional[List[AwsRedshiftClusterIamRoleTypeDef]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[List[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValuesTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfoTypeDef] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatusTypeDef] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRedshiftClusterVpcSecurityGroupTypeDef]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatusTypeDef] = None

class AwsRedshiftClusterDetailsTypeDef(BaseValidatorModel):
    AllowVersionUpgrade: Optional[bool] = None
    AutomatedSnapshotRetentionPeriod: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    ClusterAvailabilityStatus: Optional[str] = None
    ClusterCreateTime: Optional[str] = None
    ClusterIdentifier: Optional[str] = None
    ClusterNodes: Optional[Sequence[AwsRedshiftClusterClusterNodeTypeDef]] = None
    ClusterParameterGroups: Optional[       Sequence[AwsRedshiftClusterClusterParameterGroupTypeDef]     ] = None
    ClusterPublicKey: Optional[str] = None
    ClusterRevisionNumber: Optional[str] = None
    ClusterSecurityGroups: Optional[       Sequence[AwsRedshiftClusterClusterSecurityGroupTypeDef]     ] = None
    ClusterSnapshotCopyStatus: Optional[       AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef     ] = None
    ClusterStatus: Optional[str] = None
    ClusterSubnetGroupName: Optional[str] = None
    ClusterVersion: Optional[str] = None
    DBName: Optional[str] = None
    DeferredMaintenanceWindows: Optional[       Sequence[AwsRedshiftClusterDeferredMaintenanceWindowTypeDef]     ] = None
    ElasticIpStatus: Optional[AwsRedshiftClusterElasticIpStatusTypeDef] = None
    ElasticResizeNumberOfNodeOptions: Optional[str] = None
    Encrypted: Optional[bool] = None
    Endpoint: Optional[AwsRedshiftClusterEndpointTypeDef] = None
    EnhancedVpcRouting: Optional[bool] = None
    ExpectedNextSnapshotScheduleTime: Optional[str] = None
    ExpectedNextSnapshotScheduleTimeStatus: Optional[str] = None
    HsmStatus: Optional[AwsRedshiftClusterHsmStatusTypeDef] = None
    IamRoles: Optional[Sequence[AwsRedshiftClusterIamRoleTypeDef]] = None
    KmsKeyId: Optional[str] = None
    MaintenanceTrackName: Optional[str] = None
    ManualSnapshotRetentionPeriod: Optional[int] = None
    MasterUsername: Optional[str] = None
    NextMaintenanceWindowStartTime: Optional[str] = None
    NodeType: Optional[str] = None
    NumberOfNodes: Optional[int] = None
    PendingActions: Optional[Sequence[str]] = None
    PendingModifiedValues: Optional[AwsRedshiftClusterPendingModifiedValuesTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    ResizeInfo: Optional[AwsRedshiftClusterResizeInfoTypeDef] = None
    RestoreStatus: Optional[AwsRedshiftClusterRestoreStatusTypeDef] = None
    SnapshotScheduleIdentifier: Optional[str] = None
    SnapshotScheduleState: Optional[str] = None
    VpcId: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[AwsRedshiftClusterVpcSecurityGroupTypeDef]] = None
    LoggingStatus: Optional[AwsRedshiftClusterLoggingStatusTypeDef] = None

class AwsRoute53HostedZoneDetailsExtraOutputTypeDef(BaseValidatorModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetailsTypeDef] = None
    Vpcs: Optional[List[AwsRoute53HostedZoneVpcDetailsTypeDef]] = None
    NameServers: Optional[List[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetailsTypeDef] = None

class AwsRoute53HostedZoneDetailsOutputTypeDef(BaseValidatorModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetailsTypeDef] = None
    Vpcs: Optional[List[AwsRoute53HostedZoneVpcDetailsTypeDef]] = None
    NameServers: Optional[List[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetailsTypeDef] = None

class AwsRoute53HostedZoneDetailsTypeDef(BaseValidatorModel):
    HostedZone: Optional[AwsRoute53HostedZoneObjectDetailsTypeDef] = None
    Vpcs: Optional[Sequence[AwsRoute53HostedZoneVpcDetailsTypeDef]] = None
    NameServers: Optional[Sequence[str]] = None
    QueryLoggingConfig: Optional[AwsRoute53QueryLoggingConfigDetailsTypeDef] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsExtraOutputTypeDef(BaseValidatorModel):
    Operands: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]     ] = None
    Prefix: Optional[str] = None
    Tag: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef(BaseValidatorModel):
    Operands: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef]     ] = None
    Prefix: Optional[str] = None
    Tag: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef(BaseValidatorModel):
    Operands: Optional[       Sequence[         AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateOperandsDetailsTypeDef       ]     ] = None
    Prefix: Optional[str] = None
    Tag: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateTagDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsS3BucketNotificationConfigurationFilterExtraOutputTypeDef(BaseValidatorModel):
    S3KeyFilter: Optional[       AwsS3BucketNotificationConfigurationS3KeyFilterExtraOutputTypeDef     ] = None

class AwsS3BucketNotificationConfigurationFilterOutputTypeDef(BaseValidatorModel):
    S3KeyFilter: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterOutputTypeDef] = None

class AwsS3BucketNotificationConfigurationFilterTypeDef(BaseValidatorModel):
    S3KeyFilter: Optional[AwsS3BucketNotificationConfigurationS3KeyFilterTypeDef] = None

class AwsS3BucketObjectLockConfigurationTypeDef(BaseValidatorModel):
    ObjectLockEnabled: Optional[str] = None
    Rule: Optional[AwsS3BucketObjectLockConfigurationRuleDetailsTypeDef] = None

class AwsS3BucketServerSideEncryptionConfigurationExtraOutputTypeDef(BaseValidatorModel):
    Rules: Optional[List[AwsS3BucketServerSideEncryptionRuleTypeDef]] = None

class AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef(BaseValidatorModel):
    Rules: Optional[List[AwsS3BucketServerSideEncryptionRuleTypeDef]] = None

class AwsS3BucketServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    Rules: Optional[Sequence[AwsS3BucketServerSideEncryptionRuleTypeDef]] = None

class AwsS3BucketWebsiteConfigurationExtraOutputTypeDef(BaseValidatorModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectToTypeDef] = None
    RoutingRules: Optional[List[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]] = None

class AwsS3BucketWebsiteConfigurationOutputTypeDef(BaseValidatorModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectToTypeDef] = None
    RoutingRules: Optional[List[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]] = None

class AwsS3BucketWebsiteConfigurationTypeDef(BaseValidatorModel):
    ErrorDocument: Optional[str] = None
    IndexDocumentSuffix: Optional[str] = None
    RedirectAllRequestsTo: Optional[AwsS3BucketWebsiteConfigurationRedirectToTypeDef] = None
    RoutingRules: Optional[Sequence[AwsS3BucketWebsiteConfigurationRoutingRuleTypeDef]] = None

class BatchUpdateFindingsResponseTypeDef(BaseValidatorModel):
    ProcessedFindings: List[AwsSecurityFindingIdentifierTypeDef]
    UnprocessedFindings: List[BatchUpdateFindingsUnprocessedFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AwsSsmPatchComplianceDetailsTypeDef(BaseValidatorModel):
    Patch: Optional[AwsSsmPatchTypeDef] = None

class AwsStepFunctionStateMachineLoggingConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    Destinations: Optional[       List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]     ] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None

class AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    Destinations: Optional[       List[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]     ] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None

class AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef(BaseValidatorModel):
    Destinations: Optional[       Sequence[AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetailsTypeDef]     ] = None
    IncludeExecutionData: Optional[bool] = None
    Level: Optional[str] = None

class AwsWafRegionalRuleGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRegionalRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRegionalRuleGroupDetailsOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRegionalRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRegionalRuleGroupDetailsTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[Sequence[AwsWafRegionalRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRegionalWebAclDetailsExtraOutputTypeDef(BaseValidatorModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[List[AwsWafRegionalWebAclRulesListDetailsTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafRegionalWebAclDetailsOutputTypeDef(BaseValidatorModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[List[AwsWafRegionalWebAclRulesListDetailsTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafRegionalWebAclDetailsTypeDef(BaseValidatorModel):
    DefaultAction: Optional[str] = None
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RulesList: Optional[Sequence[AwsWafRegionalWebAclRulesListDetailsTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafRuleGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRuleGroupDetailsOutputTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[List[AwsWafRuleGroupRulesDetailsTypeDef]] = None

class AwsWafRuleGroupDetailsTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    Name: Optional[str] = None
    RuleGroupId: Optional[str] = None
    Rules: Optional[Sequence[AwsWafRuleGroupRulesDetailsTypeDef]] = None

class AwsWafWebAclDetailsExtraOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[List[AwsWafWebAclRuleExtraOutputTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafWebAclDetailsOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[List[AwsWafWebAclRuleOutputTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafWebAclDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DefaultAction: Optional[str] = None
    Rules: Optional[Sequence[AwsWafWebAclRuleTypeDef]] = None
    WebAclId: Optional[str] = None

class AwsWafv2ActionAllowDetailsExtraOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[       AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef     ] = None

class AwsWafv2RulesActionCaptchaDetailsExtraOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[       AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef     ] = None

class AwsWafv2RulesActionCountDetailsExtraOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[       AwsWafv2CustomRequestHandlingDetailsExtraOutputTypeDef     ] = None

class AwsWafv2ActionAllowDetailsOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef] = None

class AwsWafv2RulesActionCaptchaDetailsOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef] = None

class AwsWafv2RulesActionCountDetailsOutputTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsOutputTypeDef] = None

class AwsWafv2ActionAllowDetailsTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsTypeDef] = None

class AwsWafv2RulesActionCaptchaDetailsTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsTypeDef] = None

class AwsWafv2RulesActionCountDetailsTypeDef(BaseValidatorModel):
    CustomRequestHandling: Optional[AwsWafv2CustomRequestHandlingDetailsTypeDef] = None

class AwsWafv2ActionBlockDetailsExtraOutputTypeDef(BaseValidatorModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsExtraOutputTypeDef] = None

class AwsWafv2ActionBlockDetailsOutputTypeDef(BaseValidatorModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsOutputTypeDef] = None

class AwsWafv2ActionBlockDetailsTypeDef(BaseValidatorModel):
    CustomResponse: Optional[AwsWafv2CustomResponseDetailsTypeDef] = None

class BatchGetStandardsControlAssociationsResponseTypeDef(BaseValidatorModel):
    StandardsControlAssociationDetails: List[StandardsControlAssociationDetailTypeDef]
    UnprocessedAssociations: List[UnprocessedStandardsControlAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateStandardsControlAssociationsResponseTypeDef(BaseValidatorModel):
    UnprocessedAssociationUpdates: List[UnprocessedStandardsControlAssociationUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VulnerabilityExtraOutputTypeDef(BaseValidatorModel):
    Id: str
    VulnerablePackages: Optional[List[SoftwarePackageTypeDef]] = None
    Cvss: Optional[List[CvssExtraOutputTypeDef]] = None
    RelatedVulnerabilities: Optional[List[str]] = None
    Vendor: Optional[VulnerabilityVendorTypeDef] = None
    ReferenceUrls: Optional[List[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[       List[VulnerabilityCodeVulnerabilitiesExtraOutputTypeDef]     ] = None

class VulnerabilityOutputTypeDef(BaseValidatorModel):
    Id: str
    VulnerablePackages: Optional[List[SoftwarePackageTypeDef]] = None
    Cvss: Optional[List[CvssOutputTypeDef]] = None
    RelatedVulnerabilities: Optional[List[str]] = None
    Vendor: Optional[VulnerabilityVendorTypeDef] = None
    ReferenceUrls: Optional[List[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[List[VulnerabilityCodeVulnerabilitiesOutputTypeDef]] = None

class VulnerabilityTypeDef(BaseValidatorModel):
    Id: str
    VulnerablePackages: Optional[Sequence[SoftwarePackageTypeDef]] = None
    Cvss: Optional[Sequence[CvssTypeDef]] = None
    RelatedVulnerabilities: Optional[Sequence[str]] = None
    Vendor: Optional[VulnerabilityVendorTypeDef] = None
    ReferenceUrls: Optional[Sequence[str]] = None
    FixAvailable: Optional[VulnerabilityFixAvailableType] = None
    EpssScore: Optional[float] = None
    ExploitAvailable: Optional[VulnerabilityExploitAvailableType] = None
    LastKnownExploitAt: Optional[str] = None
    CodeVulnerabilities: Optional[Sequence[VulnerabilityCodeVulnerabilitiesTypeDef]] = None

class ParameterDefinitionTypeDef(BaseValidatorModel):
    Description: str
    ConfigurationOptions: ConfigurationOptionsTypeDef

class BatchGetConfigurationPolicyAssociationsRequestRequestTypeDef(BaseValidatorModel):
    ConfigurationPolicyAssociationIdentifiers: Sequence[       ConfigurationPolicyAssociationTypeDef     ]

class UnprocessedConfigurationPolicyAssociationTypeDef(BaseValidatorModel):
    ConfigurationPolicyAssociationIdentifiers: Optional[       ConfigurationPolicyAssociationTypeDef     ] = None
    ErrorCode: Optional[str] = None
    ErrorReason: Optional[str] = None

class AutomationRulesFindingFiltersOutputTypeDef(BaseValidatorModel):
    ProductArn: Optional[List[StringFilterTypeDef]] = None
    AwsAccountId: Optional[List[StringFilterTypeDef]] = None
    Id: Optional[List[StringFilterTypeDef]] = None
    GeneratorId: Optional[List[StringFilterTypeDef]] = None
    Type: Optional[List[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[List[DateFilterTypeDef]] = None
    LastObservedAt: Optional[List[DateFilterTypeDef]] = None
    CreatedAt: Optional[List[DateFilterTypeDef]] = None
    UpdatedAt: Optional[List[DateFilterTypeDef]] = None
    Confidence: Optional[List[NumberFilterTypeDef]] = None
    Criticality: Optional[List[NumberFilterTypeDef]] = None
    Title: Optional[List[StringFilterTypeDef]] = None
    Description: Optional[List[StringFilterTypeDef]] = None
    SourceUrl: Optional[List[StringFilterTypeDef]] = None
    ProductName: Optional[List[StringFilterTypeDef]] = None
    CompanyName: Optional[List[StringFilterTypeDef]] = None
    SeverityLabel: Optional[List[StringFilterTypeDef]] = None
    ResourceType: Optional[List[StringFilterTypeDef]] = None
    ResourceId: Optional[List[StringFilterTypeDef]] = None
    ResourcePartition: Optional[List[StringFilterTypeDef]] = None
    ResourceRegion: Optional[List[StringFilterTypeDef]] = None
    ResourceTags: Optional[List[MapFilterTypeDef]] = None
    ResourceDetailsOther: Optional[List[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[List[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilterTypeDef]] = None
    VerificationState: Optional[List[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[List[StringFilterTypeDef]] = None
    RecordState: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    NoteText: Optional[List[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[List[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[List[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[List[MapFilterTypeDef]] = None
    ResourceApplicationArn: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[List[StringFilterTypeDef]] = None
    AwsAccountName: Optional[List[StringFilterTypeDef]] = None

class AutomationRulesFindingFiltersTypeDef(BaseValidatorModel):
    ProductArn: Optional[Sequence[StringFilterTypeDef]] = None
    AwsAccountId: Optional[Sequence[StringFilterTypeDef]] = None
    Id: Optional[Sequence[StringFilterTypeDef]] = None
    GeneratorId: Optional[Sequence[StringFilterTypeDef]] = None
    Type: Optional[Sequence[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    LastObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    CreatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    UpdatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    Confidence: Optional[Sequence[NumberFilterTypeDef]] = None
    Criticality: Optional[Sequence[NumberFilterTypeDef]] = None
    Title: Optional[Sequence[StringFilterTypeDef]] = None
    Description: Optional[Sequence[StringFilterTypeDef]] = None
    SourceUrl: Optional[Sequence[StringFilterTypeDef]] = None
    ProductName: Optional[Sequence[StringFilterTypeDef]] = None
    CompanyName: Optional[Sequence[StringFilterTypeDef]] = None
    SeverityLabel: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceType: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourcePartition: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceRegion: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceTags: Optional[Sequence[MapFilterTypeDef]] = None
    ResourceDetailsOther: Optional[Sequence[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[Sequence[StringFilterTypeDef]] = None
    VerificationState: Optional[Sequence[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[Sequence[StringFilterTypeDef]] = None
    RecordState: Optional[Sequence[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[Sequence[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[Sequence[StringFilterTypeDef]] = None
    NoteText: Optional[Sequence[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[Sequence[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[Sequence[MapFilterTypeDef]] = None
    ResourceApplicationArn: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[Sequence[StringFilterTypeDef]] = None
    AwsAccountName: Optional[Sequence[StringFilterTypeDef]] = None

class AwsSecurityFindingFiltersExtraOutputTypeDef(BaseValidatorModel):
    ProductArn: Optional[List[StringFilterTypeDef]] = None
    AwsAccountId: Optional[List[StringFilterTypeDef]] = None
    Id: Optional[List[StringFilterTypeDef]] = None
    GeneratorId: Optional[List[StringFilterTypeDef]] = None
    Region: Optional[List[StringFilterTypeDef]] = None
    Type: Optional[List[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[List[DateFilterTypeDef]] = None
    LastObservedAt: Optional[List[DateFilterTypeDef]] = None
    CreatedAt: Optional[List[DateFilterTypeDef]] = None
    UpdatedAt: Optional[List[DateFilterTypeDef]] = None
    SeverityProduct: Optional[List[NumberFilterTypeDef]] = None
    SeverityNormalized: Optional[List[NumberFilterTypeDef]] = None
    SeverityLabel: Optional[List[StringFilterTypeDef]] = None
    Confidence: Optional[List[NumberFilterTypeDef]] = None
    Criticality: Optional[List[NumberFilterTypeDef]] = None
    Title: Optional[List[StringFilterTypeDef]] = None
    Description: Optional[List[StringFilterTypeDef]] = None
    RecommendationText: Optional[List[StringFilterTypeDef]] = None
    SourceUrl: Optional[List[StringFilterTypeDef]] = None
    ProductFields: Optional[List[MapFilterTypeDef]] = None
    ProductName: Optional[List[StringFilterTypeDef]] = None
    CompanyName: Optional[List[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[List[MapFilterTypeDef]] = None
    MalwareName: Optional[List[StringFilterTypeDef]] = None
    MalwareType: Optional[List[StringFilterTypeDef]] = None
    MalwarePath: Optional[List[StringFilterTypeDef]] = None
    MalwareState: Optional[List[StringFilterTypeDef]] = None
    NetworkDirection: Optional[List[StringFilterTypeDef]] = None
    NetworkProtocol: Optional[List[StringFilterTypeDef]] = None
    NetworkSourceIpV4: Optional[List[IpFilterTypeDef]] = None
    NetworkSourceIpV6: Optional[List[IpFilterTypeDef]] = None
    NetworkSourcePort: Optional[List[NumberFilterTypeDef]] = None
    NetworkSourceDomain: Optional[List[StringFilterTypeDef]] = None
    NetworkSourceMac: Optional[List[StringFilterTypeDef]] = None
    NetworkDestinationIpV4: Optional[List[IpFilterTypeDef]] = None
    NetworkDestinationIpV6: Optional[List[IpFilterTypeDef]] = None
    NetworkDestinationPort: Optional[List[NumberFilterTypeDef]] = None
    NetworkDestinationDomain: Optional[List[StringFilterTypeDef]] = None
    ProcessName: Optional[List[StringFilterTypeDef]] = None
    ProcessPath: Optional[List[StringFilterTypeDef]] = None
    ProcessPid: Optional[List[NumberFilterTypeDef]] = None
    ProcessParentPid: Optional[List[NumberFilterTypeDef]] = None
    ProcessLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ProcessTerminatedAt: Optional[List[DateFilterTypeDef]] = None
    ThreatIntelIndicatorType: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorValue: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorCategory: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorLastObservedAt: Optional[List[DateFilterTypeDef]] = None
    ThreatIntelIndicatorSource: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorSourceUrl: Optional[List[StringFilterTypeDef]] = None
    ResourceType: Optional[List[StringFilterTypeDef]] = None
    ResourceId: Optional[List[StringFilterTypeDef]] = None
    ResourcePartition: Optional[List[StringFilterTypeDef]] = None
    ResourceRegion: Optional[List[StringFilterTypeDef]] = None
    ResourceTags: Optional[List[MapFilterTypeDef]] = None
    ResourceAwsEc2InstanceType: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceImageId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV4Addresses: Optional[List[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV6Addresses: Optional[List[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceKeyName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceVpcId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceSubnetId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyUserName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyPrincipalName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyStatus: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyCreatedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceAwsIamUserUserName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerImageId: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerImageName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceDetailsOther: Optional[List[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[List[StringFilterTypeDef]] = None
    VerificationState: Optional[List[StringFilterTypeDef]] = None
    WorkflowState: Optional[List[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[List[StringFilterTypeDef]] = None
    RecordState: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    NoteText: Optional[List[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[List[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[List[StringFilterTypeDef]] = None
    Keyword: Optional[List[KeywordFilterTypeDef]] = None
    FindingProviderFieldsConfidence: Optional[List[NumberFilterTypeDef]] = None
    FindingProviderFieldsCriticality: Optional[List[NumberFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityLabel: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityOriginal: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsTypes: Optional[List[StringFilterTypeDef]] = None
    Sample: Optional[List[BooleanFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[List[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilterTypeDef]] = None
    VulnerabilitiesExploitAvailable: Optional[List[StringFilterTypeDef]] = None
    VulnerabilitiesFixAvailable: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersName: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersValue: Optional[List[StringFilterTypeDef]] = None
    AwsAccountName: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationArn: Optional[List[StringFilterTypeDef]] = None

class AwsSecurityFindingFiltersOutputTypeDef(BaseValidatorModel):
    ProductArn: Optional[List[StringFilterTypeDef]] = None
    AwsAccountId: Optional[List[StringFilterTypeDef]] = None
    Id: Optional[List[StringFilterTypeDef]] = None
    GeneratorId: Optional[List[StringFilterTypeDef]] = None
    Region: Optional[List[StringFilterTypeDef]] = None
    Type: Optional[List[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[List[DateFilterTypeDef]] = None
    LastObservedAt: Optional[List[DateFilterTypeDef]] = None
    CreatedAt: Optional[List[DateFilterTypeDef]] = None
    UpdatedAt: Optional[List[DateFilterTypeDef]] = None
    SeverityProduct: Optional[List[NumberFilterTypeDef]] = None
    SeverityNormalized: Optional[List[NumberFilterTypeDef]] = None
    SeverityLabel: Optional[List[StringFilterTypeDef]] = None
    Confidence: Optional[List[NumberFilterTypeDef]] = None
    Criticality: Optional[List[NumberFilterTypeDef]] = None
    Title: Optional[List[StringFilterTypeDef]] = None
    Description: Optional[List[StringFilterTypeDef]] = None
    RecommendationText: Optional[List[StringFilterTypeDef]] = None
    SourceUrl: Optional[List[StringFilterTypeDef]] = None
    ProductFields: Optional[List[MapFilterTypeDef]] = None
    ProductName: Optional[List[StringFilterTypeDef]] = None
    CompanyName: Optional[List[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[List[MapFilterTypeDef]] = None
    MalwareName: Optional[List[StringFilterTypeDef]] = None
    MalwareType: Optional[List[StringFilterTypeDef]] = None
    MalwarePath: Optional[List[StringFilterTypeDef]] = None
    MalwareState: Optional[List[StringFilterTypeDef]] = None
    NetworkDirection: Optional[List[StringFilterTypeDef]] = None
    NetworkProtocol: Optional[List[StringFilterTypeDef]] = None
    NetworkSourceIpV4: Optional[List[IpFilterTypeDef]] = None
    NetworkSourceIpV6: Optional[List[IpFilterTypeDef]] = None
    NetworkSourcePort: Optional[List[NumberFilterTypeDef]] = None
    NetworkSourceDomain: Optional[List[StringFilterTypeDef]] = None
    NetworkSourceMac: Optional[List[StringFilterTypeDef]] = None
    NetworkDestinationIpV4: Optional[List[IpFilterTypeDef]] = None
    NetworkDestinationIpV6: Optional[List[IpFilterTypeDef]] = None
    NetworkDestinationPort: Optional[List[NumberFilterTypeDef]] = None
    NetworkDestinationDomain: Optional[List[StringFilterTypeDef]] = None
    ProcessName: Optional[List[StringFilterTypeDef]] = None
    ProcessPath: Optional[List[StringFilterTypeDef]] = None
    ProcessPid: Optional[List[NumberFilterTypeDef]] = None
    ProcessParentPid: Optional[List[NumberFilterTypeDef]] = None
    ProcessLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ProcessTerminatedAt: Optional[List[DateFilterTypeDef]] = None
    ThreatIntelIndicatorType: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorValue: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorCategory: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorLastObservedAt: Optional[List[DateFilterTypeDef]] = None
    ThreatIntelIndicatorSource: Optional[List[StringFilterTypeDef]] = None
    ThreatIntelIndicatorSourceUrl: Optional[List[StringFilterTypeDef]] = None
    ResourceType: Optional[List[StringFilterTypeDef]] = None
    ResourceId: Optional[List[StringFilterTypeDef]] = None
    ResourcePartition: Optional[List[StringFilterTypeDef]] = None
    ResourceRegion: Optional[List[StringFilterTypeDef]] = None
    ResourceTags: Optional[List[MapFilterTypeDef]] = None
    ResourceAwsEc2InstanceType: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceImageId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV4Addresses: Optional[List[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV6Addresses: Optional[List[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceKeyName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceVpcId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceSubnetId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerId: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyUserName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyPrincipalName: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyStatus: Optional[List[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyCreatedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceAwsIamUserUserName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerImageId: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerImageName: Optional[List[StringFilterTypeDef]] = None
    ResourceContainerLaunchedAt: Optional[List[DateFilterTypeDef]] = None
    ResourceDetailsOther: Optional[List[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[List[StringFilterTypeDef]] = None
    VerificationState: Optional[List[StringFilterTypeDef]] = None
    WorkflowState: Optional[List[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[List[StringFilterTypeDef]] = None
    RecordState: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    NoteText: Optional[List[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[List[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[List[StringFilterTypeDef]] = None
    Keyword: Optional[List[KeywordFilterTypeDef]] = None
    FindingProviderFieldsConfidence: Optional[List[NumberFilterTypeDef]] = None
    FindingProviderFieldsCriticality: Optional[List[NumberFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsId: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsProductArn: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityLabel: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityOriginal: Optional[List[StringFilterTypeDef]] = None
    FindingProviderFieldsTypes: Optional[List[StringFilterTypeDef]] = None
    Sample: Optional[List[BooleanFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[List[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[List[StringFilterTypeDef]] = None
    VulnerabilitiesExploitAvailable: Optional[List[StringFilterTypeDef]] = None
    VulnerabilitiesFixAvailable: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersName: Optional[List[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersValue: Optional[List[StringFilterTypeDef]] = None
    AwsAccountName: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[List[StringFilterTypeDef]] = None
    ResourceApplicationArn: Optional[List[StringFilterTypeDef]] = None

class AwsSecurityFindingFiltersTypeDef(BaseValidatorModel):
    ProductArn: Optional[Sequence[StringFilterTypeDef]] = None
    AwsAccountId: Optional[Sequence[StringFilterTypeDef]] = None
    Id: Optional[Sequence[StringFilterTypeDef]] = None
    GeneratorId: Optional[Sequence[StringFilterTypeDef]] = None
    Region: Optional[Sequence[StringFilterTypeDef]] = None
    Type: Optional[Sequence[StringFilterTypeDef]] = None
    FirstObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    LastObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    CreatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    UpdatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    SeverityProduct: Optional[Sequence[NumberFilterTypeDef]] = None
    SeverityNormalized: Optional[Sequence[NumberFilterTypeDef]] = None
    SeverityLabel: Optional[Sequence[StringFilterTypeDef]] = None
    Confidence: Optional[Sequence[NumberFilterTypeDef]] = None
    Criticality: Optional[Sequence[NumberFilterTypeDef]] = None
    Title: Optional[Sequence[StringFilterTypeDef]] = None
    Description: Optional[Sequence[StringFilterTypeDef]] = None
    RecommendationText: Optional[Sequence[StringFilterTypeDef]] = None
    SourceUrl: Optional[Sequence[StringFilterTypeDef]] = None
    ProductFields: Optional[Sequence[MapFilterTypeDef]] = None
    ProductName: Optional[Sequence[StringFilterTypeDef]] = None
    CompanyName: Optional[Sequence[StringFilterTypeDef]] = None
    UserDefinedFields: Optional[Sequence[MapFilterTypeDef]] = None
    MalwareName: Optional[Sequence[StringFilterTypeDef]] = None
    MalwareType: Optional[Sequence[StringFilterTypeDef]] = None
    MalwarePath: Optional[Sequence[StringFilterTypeDef]] = None
    MalwareState: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkDirection: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkProtocol: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkSourceIpV4: Optional[Sequence[IpFilterTypeDef]] = None
    NetworkSourceIpV6: Optional[Sequence[IpFilterTypeDef]] = None
    NetworkSourcePort: Optional[Sequence[NumberFilterTypeDef]] = None
    NetworkSourceDomain: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkSourceMac: Optional[Sequence[StringFilterTypeDef]] = None
    NetworkDestinationIpV4: Optional[Sequence[IpFilterTypeDef]] = None
    NetworkDestinationIpV6: Optional[Sequence[IpFilterTypeDef]] = None
    NetworkDestinationPort: Optional[Sequence[NumberFilterTypeDef]] = None
    NetworkDestinationDomain: Optional[Sequence[StringFilterTypeDef]] = None
    ProcessName: Optional[Sequence[StringFilterTypeDef]] = None
    ProcessPath: Optional[Sequence[StringFilterTypeDef]] = None
    ProcessPid: Optional[Sequence[NumberFilterTypeDef]] = None
    ProcessParentPid: Optional[Sequence[NumberFilterTypeDef]] = None
    ProcessLaunchedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ProcessTerminatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ThreatIntelIndicatorType: Optional[Sequence[StringFilterTypeDef]] = None
    ThreatIntelIndicatorValue: Optional[Sequence[StringFilterTypeDef]] = None
    ThreatIntelIndicatorCategory: Optional[Sequence[StringFilterTypeDef]] = None
    ThreatIntelIndicatorLastObservedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ThreatIntelIndicatorSource: Optional[Sequence[StringFilterTypeDef]] = None
    ThreatIntelIndicatorSourceUrl: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceType: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourcePartition: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceRegion: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceTags: Optional[Sequence[MapFilterTypeDef]] = None
    ResourceAwsEc2InstanceType: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceImageId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV4Addresses: Optional[Sequence[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceIpV6Addresses: Optional[Sequence[IpFilterTypeDef]] = None
    ResourceAwsEc2InstanceKeyName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceIamInstanceProfileArn: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceVpcId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceSubnetId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsEc2InstanceLaunchedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsS3BucketOwnerName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyUserName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyPrincipalName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyStatus: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceAwsIamAccessKeyCreatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ResourceAwsIamUserUserName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceContainerName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceContainerImageId: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceContainerImageName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceContainerLaunchedAt: Optional[Sequence[DateFilterTypeDef]] = None
    ResourceDetailsOther: Optional[Sequence[MapFilterTypeDef]] = None
    ComplianceStatus: Optional[Sequence[StringFilterTypeDef]] = None
    VerificationState: Optional[Sequence[StringFilterTypeDef]] = None
    WorkflowState: Optional[Sequence[StringFilterTypeDef]] = None
    WorkflowStatus: Optional[Sequence[StringFilterTypeDef]] = None
    RecordState: Optional[Sequence[StringFilterTypeDef]] = None
    RelatedFindingsProductArn: Optional[Sequence[StringFilterTypeDef]] = None
    RelatedFindingsId: Optional[Sequence[StringFilterTypeDef]] = None
    NoteText: Optional[Sequence[StringFilterTypeDef]] = None
    NoteUpdatedAt: Optional[Sequence[DateFilterTypeDef]] = None
    NoteUpdatedBy: Optional[Sequence[StringFilterTypeDef]] = None
    Keyword: Optional[Sequence[KeywordFilterTypeDef]] = None
    FindingProviderFieldsConfidence: Optional[Sequence[NumberFilterTypeDef]] = None
    FindingProviderFieldsCriticality: Optional[Sequence[NumberFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsId: Optional[Sequence[StringFilterTypeDef]] = None
    FindingProviderFieldsRelatedFindingsProductArn: Optional[       Sequence[StringFilterTypeDef]     ] = None
    FindingProviderFieldsSeverityLabel: Optional[Sequence[StringFilterTypeDef]] = None
    FindingProviderFieldsSeverityOriginal: Optional[Sequence[StringFilterTypeDef]] = None
    FindingProviderFieldsTypes: Optional[Sequence[StringFilterTypeDef]] = None
    Sample: Optional[Sequence[BooleanFilterTypeDef]] = None
    ComplianceSecurityControlId: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceAssociatedStandardsId: Optional[Sequence[StringFilterTypeDef]] = None
    VulnerabilitiesExploitAvailable: Optional[Sequence[StringFilterTypeDef]] = None
    VulnerabilitiesFixAvailable: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersName: Optional[Sequence[StringFilterTypeDef]] = None
    ComplianceSecurityControlParametersValue: Optional[Sequence[StringFilterTypeDef]] = None
    AwsAccountName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceApplicationName: Optional[Sequence[StringFilterTypeDef]] = None
    ResourceApplicationArn: Optional[Sequence[StringFilterTypeDef]] = None

class GetFindingHistoryResponseTypeDef(BaseValidatorModel):
    Records: List[FindingHistoryRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetInsightResultsResponseTypeDef(BaseValidatorModel):
    InsightResults: InsightResultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkHeaderExtraOutputTypeDef(BaseValidatorModel):
    Protocol: Optional[str] = None
    Destination: Optional[NetworkPathComponentDetailsExtraOutputTypeDef] = None
    Source: Optional[NetworkPathComponentDetailsExtraOutputTypeDef] = None

class NetworkHeaderOutputTypeDef(BaseValidatorModel):
    Protocol: Optional[str] = None
    Destination: Optional[NetworkPathComponentDetailsOutputTypeDef] = None
    Source: Optional[NetworkPathComponentDetailsOutputTypeDef] = None

class NetworkHeaderTypeDef(BaseValidatorModel):
    Protocol: Optional[str] = None
    Destination: Optional[NetworkPathComponentDetailsTypeDef] = None
    Source: Optional[NetworkPathComponentDetailsTypeDef] = None

class OccurrencesExtraOutputTypeDef(BaseValidatorModel):
    LineRanges: Optional[List[RangeTypeDef]] = None
    OffsetRanges: Optional[List[RangeTypeDef]] = None
    Pages: Optional[List[PageTypeDef]] = None
    Records: Optional[List[RecordTypeDef]] = None
    Cells: Optional[List[CellTypeDef]] = None

class OccurrencesOutputTypeDef(BaseValidatorModel):
    LineRanges: Optional[List[RangeTypeDef]] = None
    OffsetRanges: Optional[List[RangeTypeDef]] = None
    Pages: Optional[List[PageTypeDef]] = None
    Records: Optional[List[RecordTypeDef]] = None
    Cells: Optional[List[CellTypeDef]] = None

class OccurrencesTypeDef(BaseValidatorModel):
    LineRanges: Optional[Sequence[RangeTypeDef]] = None
    OffsetRanges: Optional[Sequence[RangeTypeDef]] = None
    Pages: Optional[Sequence[PageTypeDef]] = None
    Records: Optional[Sequence[RecordTypeDef]] = None
    Cells: Optional[Sequence[CellTypeDef]] = None

class SecurityControlCustomParameterOutputTypeDef(BaseValidatorModel):
    SecurityControlId: Optional[str] = None
    Parameters: Optional[Dict[str, ParameterConfigurationOutputTypeDef]] = None

class SecurityControlTypeDef(BaseValidatorModel):
    SecurityControlId: str
    SecurityControlArn: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    SecurityControlStatus: ControlStatusType
    UpdateStatus: Optional[UpdateStatusType] = None
    Parameters: Optional[Dict[str, ParameterConfigurationOutputTypeDef]] = None
    LastUpdateReason: Optional[str] = None

class SecurityControlCustomParameterTypeDef(BaseValidatorModel):
    SecurityControlId: Optional[str] = None
    Parameters: Optional[Mapping[str, ParameterConfigurationTypeDef]] = None

class RuleGroupSourceStatelessRuleDefinitionExtraOutputTypeDef(BaseValidatorModel):
    Actions: Optional[List[str]] = None
    MatchAttributes: Optional[       RuleGroupSourceStatelessRuleMatchAttributesExtraOutputTypeDef     ] = None

class RuleGroupSourceStatelessRuleDefinitionOutputTypeDef(BaseValidatorModel):
    Actions: Optional[List[str]] = None
    MatchAttributes: Optional[RuleGroupSourceStatelessRuleMatchAttributesOutputTypeDef] = None

class RuleGroupSourceStatelessRuleDefinitionTypeDef(BaseValidatorModel):
    Actions: Optional[Sequence[str]] = None
    MatchAttributes: Optional[RuleGroupSourceStatelessRuleMatchAttributesTypeDef] = None

class DescribeStandardsResponseTypeDef(BaseValidatorModel):
    Standards: List[StandardTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchDisableStandardsResponseTypeDef(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchEnableStandardsResponseTypeDef(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetEnabledStandardsResponseTypeDef(BaseValidatorModel):
    StandardsSubscriptions: List[StandardsSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StatelessCustomActionDefinitionExtraOutputTypeDef(BaseValidatorModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionExtraOutputTypeDef] = None

class StatelessCustomActionDefinitionOutputTypeDef(BaseValidatorModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionOutputTypeDef] = None

class StatelessCustomActionDefinitionTypeDef(BaseValidatorModel):
    PublishMetricAction: Optional[StatelessCustomPublishMetricActionTypeDef] = None

class PortProbeActionExtraOutputTypeDef(BaseValidatorModel):
    PortProbeDetails: Optional[List[PortProbeDetailTypeDef]] = None
    Blocked: Optional[bool] = None

class PortProbeActionOutputTypeDef(BaseValidatorModel):
    PortProbeDetails: Optional[List[PortProbeDetailTypeDef]] = None
    Blocked: Optional[bool] = None

class PortProbeActionTypeDef(BaseValidatorModel):
    PortProbeDetails: Optional[Sequence[PortProbeDetailTypeDef]] = None
    Blocked: Optional[bool] = None

class AwsAthenaWorkGroupDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[str] = None
    Configuration: Optional[AwsAthenaWorkGroupConfigurationDetailsTypeDef] = None

class AwsAutoScalingAutoScalingGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsExtraOutputTypeDef     ] = None
    AvailabilityZones: Optional[       List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    CapacityRebalance: Optional[bool] = None

class AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef(BaseValidatorModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[List[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsOutputTypeDef     ] = None
    AvailabilityZones: Optional[       List[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    CapacityRebalance: Optional[bool] = None

class AwsAutoScalingAutoScalingGroupDetailsTypeDef(BaseValidatorModel):
    LaunchConfigurationName: Optional[str] = None
    LoadBalancerNames: Optional[Sequence[str]] = None
    HealthCheckType: Optional[str] = None
    HealthCheckGracePeriod: Optional[int] = None
    CreatedTime: Optional[str] = None
    MixedInstancesPolicy: Optional[       AwsAutoScalingAutoScalingGroupMixedInstancesPolicyDetailsTypeDef     ] = None
    AvailabilityZones: Optional[       Sequence[AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetailsTypeDef]     ] = None
    LaunchTemplate: Optional[       AwsAutoScalingAutoScalingGroupLaunchTemplateLaunchTemplateSpecificationTypeDef     ] = None
    CapacityRebalance: Optional[bool] = None

class AwsBackupBackupPlanBackupPlanDetailsExtraOutputTypeDef(BaseValidatorModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[       List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsExtraOutputTypeDef]     ] = None
    BackupPlanRule: Optional[List[AwsBackupBackupPlanRuleDetailsExtraOutputTypeDef]] = None

class AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef(BaseValidatorModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[       List[AwsBackupBackupPlanAdvancedBackupSettingsDetailsOutputTypeDef]     ] = None
    BackupPlanRule: Optional[List[AwsBackupBackupPlanRuleDetailsOutputTypeDef]] = None

class AwsBackupBackupPlanBackupPlanDetailsTypeDef(BaseValidatorModel):
    BackupPlanName: Optional[str] = None
    AdvancedBackupSettings: Optional[       Sequence[AwsBackupBackupPlanAdvancedBackupSettingsDetailsTypeDef]     ] = None
    BackupPlanRule: Optional[Sequence[AwsBackupBackupPlanRuleDetailsTypeDef]] = None

class AwsCertificateManagerCertificateDetailsExtraOutputTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    DomainValidationOptions: Optional[       List[AwsCertificateManagerCertificateDomainValidationOptionExtraOutputTypeDef]     ] = None
    ExtendedKeyUsages: Optional[       List[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]     ] = None
    FailureReason: Optional[str] = None
    ImportedAt: Optional[str] = None
    InUseBy: Optional[List[str]] = None
    IssuedAt: Optional[str] = None
    Issuer: Optional[str] = None
    KeyAlgorithm: Optional[str] = None
    KeyUsages: Optional[List[AwsCertificateManagerCertificateKeyUsageTypeDef]] = None
    NotAfter: Optional[str] = None
    NotBefore: Optional[str] = None
    Options: Optional[AwsCertificateManagerCertificateOptionsTypeDef] = None
    RenewalEligibility: Optional[str] = None
    RenewalSummary: Optional[       AwsCertificateManagerCertificateRenewalSummaryExtraOutputTypeDef     ] = None
    Serial: Optional[str] = None
    SignatureAlgorithm: Optional[str] = None
    Status: Optional[str] = None
    Subject: Optional[str] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    Type: Optional[str] = None

class AwsCertificateManagerCertificateDetailsOutputTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    DomainValidationOptions: Optional[       List[AwsCertificateManagerCertificateDomainValidationOptionOutputTypeDef]     ] = None
    ExtendedKeyUsages: Optional[       List[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]     ] = None
    FailureReason: Optional[str] = None
    ImportedAt: Optional[str] = None
    InUseBy: Optional[List[str]] = None
    IssuedAt: Optional[str] = None
    Issuer: Optional[str] = None
    KeyAlgorithm: Optional[str] = None
    KeyUsages: Optional[List[AwsCertificateManagerCertificateKeyUsageTypeDef]] = None
    NotAfter: Optional[str] = None
    NotBefore: Optional[str] = None
    Options: Optional[AwsCertificateManagerCertificateOptionsTypeDef] = None
    RenewalEligibility: Optional[str] = None
    RenewalSummary: Optional[AwsCertificateManagerCertificateRenewalSummaryOutputTypeDef] = None
    Serial: Optional[str] = None
    SignatureAlgorithm: Optional[str] = None
    Status: Optional[str] = None
    Subject: Optional[str] = None
    SubjectAlternativeNames: Optional[List[str]] = None
    Type: Optional[str] = None

class AwsCertificateManagerCertificateDetailsTypeDef(BaseValidatorModel):
    CertificateAuthorityArn: Optional[str] = None
    CreatedAt: Optional[str] = None
    DomainName: Optional[str] = None
    DomainValidationOptions: Optional[       Sequence[AwsCertificateManagerCertificateDomainValidationOptionTypeDef]     ] = None
    ExtendedKeyUsages: Optional[       Sequence[AwsCertificateManagerCertificateExtendedKeyUsageTypeDef]     ] = None
    FailureReason: Optional[str] = None
    ImportedAt: Optional[str] = None
    InUseBy: Optional[Sequence[str]] = None
    IssuedAt: Optional[str] = None
    Issuer: Optional[str] = None
    KeyAlgorithm: Optional[str] = None
    KeyUsages: Optional[Sequence[AwsCertificateManagerCertificateKeyUsageTypeDef]] = None
    NotAfter: Optional[str] = None
    NotBefore: Optional[str] = None
    Options: Optional[AwsCertificateManagerCertificateOptionsTypeDef] = None
    RenewalEligibility: Optional[str] = None
    RenewalSummary: Optional[AwsCertificateManagerCertificateRenewalSummaryTypeDef] = None
    Serial: Optional[str] = None
    SignatureAlgorithm: Optional[str] = None
    Status: Optional[str] = None
    Subject: Optional[str] = None
    SubjectAlternativeNames: Optional[Sequence[str]] = None
    Type: Optional[str] = None

class AwsCloudFrontDistributionOriginsExtraOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginItemExtraOutputTypeDef]] = None

class AwsCloudFrontDistributionOriginsOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginItemOutputTypeDef]] = None

class AwsCloudFrontDistributionOriginsTypeDef(BaseValidatorModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionOriginItemTypeDef]] = None

class AwsCloudFrontDistributionOriginGroupsExtraOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginGroupExtraOutputTypeDef]] = None

class AwsCloudFrontDistributionOriginGroupsOutputTypeDef(BaseValidatorModel):
    Items: Optional[List[AwsCloudFrontDistributionOriginGroupOutputTypeDef]] = None

class AwsCloudFrontDistributionOriginGroupsTypeDef(BaseValidatorModel):
    Items: Optional[Sequence[AwsCloudFrontDistributionOriginGroupTypeDef]] = None

class AwsDynamoDbTableDetailsExtraOutputTypeDef(BaseValidatorModel):
    AttributeDefinitions: Optional[List[AwsDynamoDbTableAttributeDefinitionTypeDef]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummaryTypeDef] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[       List[AwsDynamoDbTableGlobalSecondaryIndexExtraOutputTypeDef]     ] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[       List[AwsDynamoDbTableLocalSecondaryIndexExtraOutputTypeDef]     ] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None
    Replicas: Optional[List[AwsDynamoDbTableReplicaExtraOutputTypeDef]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummaryTypeDef] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescriptionTypeDef] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecificationTypeDef] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

class AwsDynamoDbTableDetailsOutputTypeDef(BaseValidatorModel):
    AttributeDefinitions: Optional[List[AwsDynamoDbTableAttributeDefinitionTypeDef]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummaryTypeDef] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[       List[AwsDynamoDbTableGlobalSecondaryIndexOutputTypeDef]     ] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[List[AwsDynamoDbTableKeySchemaTypeDef]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[       List[AwsDynamoDbTableLocalSecondaryIndexOutputTypeDef]     ] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None
    Replicas: Optional[List[AwsDynamoDbTableReplicaOutputTypeDef]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummaryTypeDef] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescriptionTypeDef] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecificationTypeDef] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

class AwsDynamoDbTableDetailsTypeDef(BaseValidatorModel):
    AttributeDefinitions: Optional[Sequence[AwsDynamoDbTableAttributeDefinitionTypeDef]] = None
    BillingModeSummary: Optional[AwsDynamoDbTableBillingModeSummaryTypeDef] = None
    CreationDateTime: Optional[str] = None
    GlobalSecondaryIndexes: Optional[       Sequence[AwsDynamoDbTableGlobalSecondaryIndexTypeDef]     ] = None
    GlobalTableVersion: Optional[str] = None
    ItemCount: Optional[int] = None
    KeySchema: Optional[Sequence[AwsDynamoDbTableKeySchemaTypeDef]] = None
    LatestStreamArn: Optional[str] = None
    LatestStreamLabel: Optional[str] = None
    LocalSecondaryIndexes: Optional[Sequence[AwsDynamoDbTableLocalSecondaryIndexTypeDef]] = None
    ProvisionedThroughput: Optional[AwsDynamoDbTableProvisionedThroughputTypeDef] = None
    Replicas: Optional[Sequence[AwsDynamoDbTableReplicaTypeDef]] = None
    RestoreSummary: Optional[AwsDynamoDbTableRestoreSummaryTypeDef] = None
    SseDescription: Optional[AwsDynamoDbTableSseDescriptionTypeDef] = None
    StreamSpecification: Optional[AwsDynamoDbTableStreamSpecificationTypeDef] = None
    TableId: Optional[str] = None
    TableName: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    TableStatus: Optional[str] = None
    DeletionProtectionEnabled: Optional[bool] = None

class AwsEc2LaunchTemplateDetailsExtraOutputTypeDef(BaseValidatorModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsExtraOutputTypeDef] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None

class AwsEc2LaunchTemplateDetailsOutputTypeDef(BaseValidatorModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsOutputTypeDef] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None

class AwsEc2LaunchTemplateDetailsTypeDef(BaseValidatorModel):
    LaunchTemplateName: Optional[str] = None
    Id: Optional[str] = None
    LaunchTemplateData: Optional[AwsEc2LaunchTemplateDataDetailsTypeDef] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None

class AwsEcsClusterDetailsExtraOutputTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[List[str]] = None
    ClusterSettings: Optional[List[AwsEcsClusterClusterSettingsDetailsTypeDef]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetailsTypeDef] = None
    DefaultCapacityProviderStrategy: Optional[       List[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]     ] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None

class AwsEcsClusterDetailsOutputTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[List[str]] = None
    ClusterSettings: Optional[List[AwsEcsClusterClusterSettingsDetailsTypeDef]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetailsTypeDef] = None
    DefaultCapacityProviderStrategy: Optional[       List[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]     ] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None

class AwsEcsClusterDetailsTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ActiveServicesCount: Optional[int] = None
    CapacityProviders: Optional[Sequence[str]] = None
    ClusterSettings: Optional[Sequence[AwsEcsClusterClusterSettingsDetailsTypeDef]] = None
    Configuration: Optional[AwsEcsClusterConfigurationDetailsTypeDef] = None
    DefaultCapacityProviderStrategy: Optional[       Sequence[AwsEcsClusterDefaultCapacityProviderStrategyDetailsTypeDef]     ] = None
    ClusterName: Optional[str] = None
    RegisteredContainerInstancesCount: Optional[int] = None
    RunningTasksCount: Optional[int] = None
    Status: Optional[str] = None

class AwsEcsTaskDefinitionDetailsExtraOutputTypeDef(BaseValidatorModel):
    ContainerDefinitions: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsDetailsExtraOutputTypeDef]     ] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[       List[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]     ] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[       List[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]     ] = None
    ProxyConfiguration: Optional[       AwsEcsTaskDefinitionProxyConfigurationDetailsExtraOutputTypeDef     ] = None
    RequiresCompatibilities: Optional[List[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskDefinitionVolumesDetailsExtraOutputTypeDef]] = None
    Status: Optional[str] = None

class AwsEcsTaskDefinitionDetailsOutputTypeDef(BaseValidatorModel):
    ContainerDefinitions: Optional[       List[AwsEcsTaskDefinitionContainerDefinitionsDetailsOutputTypeDef]     ] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[       List[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]     ] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[       List[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]     ] = None
    ProxyConfiguration: Optional[       AwsEcsTaskDefinitionProxyConfigurationDetailsOutputTypeDef     ] = None
    RequiresCompatibilities: Optional[List[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[List[AwsEcsTaskDefinitionVolumesDetailsOutputTypeDef]] = None
    Status: Optional[str] = None

class AwsEcsTaskDefinitionDetailsTypeDef(BaseValidatorModel):
    ContainerDefinitions: Optional[       Sequence[AwsEcsTaskDefinitionContainerDefinitionsDetailsTypeDef]     ] = None
    Cpu: Optional[str] = None
    ExecutionRoleArn: Optional[str] = None
    Family: Optional[str] = None
    InferenceAccelerators: Optional[       Sequence[AwsEcsTaskDefinitionInferenceAcceleratorsDetailsTypeDef]     ] = None
    IpcMode: Optional[str] = None
    Memory: Optional[str] = None
    NetworkMode: Optional[str] = None
    PidMode: Optional[str] = None
    PlacementConstraints: Optional[       Sequence[AwsEcsTaskDefinitionPlacementConstraintsDetailsTypeDef]     ] = None
    ProxyConfiguration: Optional[AwsEcsTaskDefinitionProxyConfigurationDetailsTypeDef] = None
    RequiresCompatibilities: Optional[Sequence[str]] = None
    TaskRoleArn: Optional[str] = None
    Volumes: Optional[Sequence[AwsEcsTaskDefinitionVolumesDetailsTypeDef]] = None
    Status: Optional[str] = None

class AwsEventsEndpointDetailsExtraOutputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[List[AwsEventsEndpointEventBusesDetailsTypeDef]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetailsTypeDef] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetailsTypeDef] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None

class AwsEventsEndpointDetailsOutputTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[List[AwsEventsEndpointEventBusesDetailsTypeDef]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetailsTypeDef] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetailsTypeDef] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None

class AwsEventsEndpointDetailsTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Description: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointUrl: Optional[str] = None
    EventBuses: Optional[Sequence[AwsEventsEndpointEventBusesDetailsTypeDef]] = None
    Name: Optional[str] = None
    ReplicationConfig: Optional[AwsEventsEndpointReplicationConfigDetailsTypeDef] = None
    RoleArn: Optional[str] = None
    RoutingConfig: Optional[AwsEventsEndpointRoutingConfigDetailsTypeDef] = None
    State: Optional[str] = None
    StateReason: Optional[str] = None

class AwsGuardDutyDetectorDataSourcesDetailsTypeDef(BaseValidatorModel):
    CloudTrail: Optional[AwsGuardDutyDetectorDataSourcesCloudTrailDetailsTypeDef] = None
    DnsLogs: Optional[AwsGuardDutyDetectorDataSourcesDnsLogsDetailsTypeDef] = None
    FlowLogs: Optional[AwsGuardDutyDetectorDataSourcesFlowLogsDetailsTypeDef] = None
    Kubernetes: Optional[AwsGuardDutyDetectorDataSourcesKubernetesDetailsTypeDef] = None
    MalwareProtection: Optional[       AwsGuardDutyDetectorDataSourcesMalwareProtectionDetailsTypeDef     ] = None
    S3Logs: Optional[AwsGuardDutyDetectorDataSourcesS3LogsDetailsTypeDef] = None

class AwsMskClusterClusterInfoDetailsExtraOutputTypeDef(BaseValidatorModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[       AwsMskClusterClusterInfoClientAuthenticationDetailsExtraOutputTypeDef     ] = None
    EnhancedMonitoring: Optional[str] = None

class AwsMskClusterClusterInfoDetailsOutputTypeDef(BaseValidatorModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[       AwsMskClusterClusterInfoClientAuthenticationDetailsOutputTypeDef     ] = None
    EnhancedMonitoring: Optional[str] = None

class AwsMskClusterClusterInfoDetailsTypeDef(BaseValidatorModel):
    EncryptionInfo: Optional[AwsMskClusterClusterInfoEncryptionInfoDetailsTypeDef] = None
    CurrentVersion: Optional[str] = None
    NumberOfBrokerNodes: Optional[int] = None
    ClusterName: Optional[str] = None
    ClientAuthentication: Optional[       AwsMskClusterClusterInfoClientAuthenticationDetailsTypeDef     ] = None
    EnhancedMonitoring: Optional[str] = None

class AwsRdsDbInstanceDetailsExtraOutputTypeDef(BaseValidatorModel):
    AssociatedRoles: Optional[List[AwsRdsDbInstanceAssociatedRoleTypeDef]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[List[str]] = None
    DbParameterGroups: Optional[List[AwsRdsDbParameterGroupTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupExtraOutputTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesExtraOutputTypeDef] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[AwsRdsDbOptionGroupMembershipTypeDef]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[List[AwsRdsDbStatusInfoTypeDef]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembershipTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    MaxAllocatedStorage: Optional[int] = None

class AwsRdsDbInstanceDetailsOutputTypeDef(BaseValidatorModel):
    AssociatedRoles: Optional[List[AwsRdsDbInstanceAssociatedRoleTypeDef]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[List[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[List[str]] = None
    DbParameterGroups: Optional[List[AwsRdsDbParameterGroupTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupOutputTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesOutputTypeDef] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[AwsRdsDbOptionGroupMembershipTypeDef]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[List[AwsRdsDbStatusInfoTypeDef]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[List[AwsRdsDbDomainMembershipTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[List[str]] = None
    ProcessorFeatures: Optional[List[AwsRdsDbProcessorFeatureTypeDef]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    MaxAllocatedStorage: Optional[int] = None

class AwsRdsDbInstanceDetailsTypeDef(BaseValidatorModel):
    AssociatedRoles: Optional[Sequence[AwsRdsDbInstanceAssociatedRoleTypeDef]] = None
    CACertificateIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DbiResourceId: Optional[str] = None
    DBName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    Endpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    InstanceCreateTime: Optional[str] = None
    KmsKeyId: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None
    TdeCredentialArn: Optional[str] = None
    VpcSecurityGroups: Optional[Sequence[AwsRdsDbInstanceVpcSecurityGroupTypeDef]] = None
    MultiAz: Optional[bool] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    DbInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DbSecurityGroups: Optional[Sequence[str]] = None
    DbParameterGroups: Optional[Sequence[AwsRdsDbParameterGroupTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DbSubnetGroup: Optional[AwsRdsDbSubnetGroupTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[AwsRdsDbPendingModifiedValuesTypeDef] = None
    LatestRestorableTime: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[Sequence[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[Sequence[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[Sequence[AwsRdsDbOptionGroupMembershipTypeDef]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    StatusInfos: Optional[Sequence[AwsRdsDbStatusInfoTypeDef]] = None
    StorageType: Optional[str] = None
    DomainMemberships: Optional[Sequence[AwsRdsDbDomainMembershipTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKmsKeyId: Optional[str] = None
    PerformanceInsightsRetentionPeriod: Optional[int] = None
    EnabledCloudWatchLogsExports: Optional[Sequence[str]] = None
    ProcessorFeatures: Optional[Sequence[AwsRdsDbProcessorFeatureTypeDef]] = None
    ListenerEndpoint: Optional[AwsRdsDbInstanceEndpointTypeDef] = None
    MaxAllocatedStorage: Optional[int] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsExtraOutputTypeDef(BaseValidatorModel):
    Predicate: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsExtraOutputTypeDef     ] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef(BaseValidatorModel):
    Predicate: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsOutputTypeDef     ] = None

class AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef(BaseValidatorModel):
    Predicate: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterPredicateDetailsTypeDef     ] = None

class AwsS3BucketNotificationConfigurationDetailExtraOutputTypeDef(BaseValidatorModel):
    Events: Optional[List[str]] = None
    Filter: Optional[AwsS3BucketNotificationConfigurationFilterExtraOutputTypeDef] = None
    Destination: Optional[str] = None
    Type: Optional[str] = None

class AwsS3BucketNotificationConfigurationDetailOutputTypeDef(BaseValidatorModel):
    Events: Optional[List[str]] = None
    Filter: Optional[AwsS3BucketNotificationConfigurationFilterOutputTypeDef] = None
    Destination: Optional[str] = None
    Type: Optional[str] = None

class AwsS3BucketNotificationConfigurationDetailTypeDef(BaseValidatorModel):
    Events: Optional[Sequence[str]] = None
    Filter: Optional[AwsS3BucketNotificationConfigurationFilterTypeDef] = None
    Destination: Optional[str] = None
    Type: Optional[str] = None

class AwsStepFunctionStateMachineDetailsExtraOutputTypeDef(BaseValidatorModel):
    Label: Optional[str] = None
    LoggingConfiguration: Optional[       AwsStepFunctionStateMachineLoggingConfigurationDetailsExtraOutputTypeDef     ] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    StateMachineArn: Optional[str] = None
    Status: Optional[str] = None
    TracingConfiguration: Optional[       AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsStepFunctionStateMachineDetailsOutputTypeDef(BaseValidatorModel):
    Label: Optional[str] = None
    LoggingConfiguration: Optional[       AwsStepFunctionStateMachineLoggingConfigurationDetailsOutputTypeDef     ] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    StateMachineArn: Optional[str] = None
    Status: Optional[str] = None
    TracingConfiguration: Optional[       AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsStepFunctionStateMachineDetailsTypeDef(BaseValidatorModel):
    Label: Optional[str] = None
    LoggingConfiguration: Optional[       AwsStepFunctionStateMachineLoggingConfigurationDetailsTypeDef     ] = None
    Name: Optional[str] = None
    RoleArn: Optional[str] = None
    StateMachineArn: Optional[str] = None
    Status: Optional[str] = None
    TracingConfiguration: Optional[       AwsStepFunctionStateMachineTracingConfigurationDetailsTypeDef     ] = None
    Type: Optional[str] = None

class AwsWafv2RulesActionDetailsExtraOutputTypeDef(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsExtraOutputTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsExtraOutputTypeDef] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsExtraOutputTypeDef] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsExtraOutputTypeDef] = None

class AwsWafv2WebAclActionDetailsExtraOutputTypeDef(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsExtraOutputTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsExtraOutputTypeDef] = None

class AwsWafv2RulesActionDetailsOutputTypeDef(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsOutputTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsOutputTypeDef] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsOutputTypeDef] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsOutputTypeDef] = None

class AwsWafv2WebAclActionDetailsOutputTypeDef(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsOutputTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsOutputTypeDef] = None

class AwsWafv2RulesActionDetailsTypeDef(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsTypeDef] = None
    Captcha: Optional[AwsWafv2RulesActionCaptchaDetailsTypeDef] = None
    Count: Optional[AwsWafv2RulesActionCountDetailsTypeDef] = None

class AwsWafv2WebAclActionDetailsTypeDef(BaseValidatorModel):
    Allow: Optional[AwsWafv2ActionAllowDetailsTypeDef] = None
    Block: Optional[AwsWafv2ActionBlockDetailsTypeDef] = None

class SecurityControlDefinitionTypeDef(BaseValidatorModel):
    SecurityControlId: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRatingType
    CurrentRegionAvailability: RegionAvailabilityStatusType
    CustomizableProperties: Optional[List[Literal["Parameters"]]] = None
    ParameterDefinitions: Optional[Dict[str, ParameterDefinitionTypeDef]] = None

class BatchGetConfigurationPolicyAssociationsResponseTypeDef(BaseValidatorModel):
    ConfigurationPolicyAssociations: List[ConfigurationPolicyAssociationSummaryTypeDef]
    UnprocessedConfigurationPolicyAssociations: List[       UnprocessedConfigurationPolicyAssociationTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class AutomationRulesConfigTypeDef(BaseValidatorModel):
    RuleArn: Optional[str] = None
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    RuleName: Optional[str] = None
    Description: Optional[str] = None
    IsTerminal: Optional[bool] = None
    Criteria: Optional[AutomationRulesFindingFiltersOutputTypeDef] = None
    Actions: Optional[List[AutomationRulesActionOutputTypeDef]] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None

class UpdateAutomationRulesRequestItemTypeDef(BaseValidatorModel):
    RuleArn: str
    RuleStatus: Optional[RuleStatusType] = None
    RuleOrder: Optional[int] = None
    Description: Optional[str] = None
    RuleName: Optional[str] = None
    IsTerminal: Optional[bool] = None
    Criteria: Optional[AutomationRulesFindingFiltersTypeDef] = None
    Actions: Optional[Sequence[AutomationRulesActionTypeDef]] = None

class InsightTypeDef(BaseValidatorModel):
    InsightArn: str
    Name: str
    Filters: AwsSecurityFindingFiltersOutputTypeDef
    GroupByAttribute: str

class CreateInsightRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Filters: AwsSecurityFindingFiltersTypeDef
    GroupByAttribute: str

class GetFindingsRequestGetFindingsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[AwsSecurityFindingFiltersTypeDef] = None
    SortCriteria: Optional[Sequence[SortCriterionTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetFindingsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[AwsSecurityFindingFiltersTypeDef] = None
    SortCriteria: Optional[Sequence[SortCriterionTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UpdateFindingsRequestRequestTypeDef(BaseValidatorModel):
    Filters: AwsSecurityFindingFiltersTypeDef
    Note: Optional[NoteUpdateTypeDef] = None
    RecordState: Optional[RecordStateType] = None

class UpdateInsightRequestRequestTypeDef(BaseValidatorModel):
    InsightArn: str
    Name: Optional[str] = None
    Filters: Optional[AwsSecurityFindingFiltersTypeDef] = None
    GroupByAttribute: Optional[str] = None

class NetworkPathComponentExtraOutputTypeDef(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderExtraOutputTypeDef] = None
    Ingress: Optional[NetworkHeaderExtraOutputTypeDef] = None

class NetworkPathComponentOutputTypeDef(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderOutputTypeDef] = None
    Ingress: Optional[NetworkHeaderOutputTypeDef] = None

class NetworkPathComponentTypeDef(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentType: Optional[str] = None
    Egress: Optional[NetworkHeaderTypeDef] = None
    Ingress: Optional[NetworkHeaderTypeDef] = None

class CustomDataIdentifiersDetectionsExtraOutputTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesExtraOutputTypeDef] = None

class SensitiveDataDetectionsExtraOutputTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Type: Optional[str] = None
    Occurrences: Optional[OccurrencesExtraOutputTypeDef] = None

class CustomDataIdentifiersDetectionsOutputTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesOutputTypeDef] = None

class SensitiveDataDetectionsOutputTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Type: Optional[str] = None
    Occurrences: Optional[OccurrencesOutputTypeDef] = None

class CustomDataIdentifiersDetectionsTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Occurrences: Optional[OccurrencesTypeDef] = None

class SensitiveDataDetectionsTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Type: Optional[str] = None
    Occurrences: Optional[OccurrencesTypeDef] = None

class SecurityControlsConfigurationOutputTypeDef(BaseValidatorModel):
    EnabledSecurityControlIdentifiers: Optional[List[str]] = None
    DisabledSecurityControlIdentifiers: Optional[List[str]] = None
    SecurityControlCustomParameters: Optional[       List[SecurityControlCustomParameterOutputTypeDef]     ] = None

class BatchGetSecurityControlsResponseTypeDef(BaseValidatorModel):
    SecurityControls: List[SecurityControlTypeDef]
    UnprocessedIds: List[UnprocessedSecurityControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityControlRequestRequestTypeDef(BaseValidatorModel):
    SecurityControlId: str
    Parameters: Mapping[str, ParameterConfigurationUnionTypeDef]
    LastUpdateReason: Optional[str] = None

class SecurityControlsConfigurationTypeDef(BaseValidatorModel):
    EnabledSecurityControlIdentifiers: Optional[Sequence[str]] = None
    DisabledSecurityControlIdentifiers: Optional[Sequence[str]] = None
    SecurityControlCustomParameters: Optional[       Sequence[SecurityControlCustomParameterTypeDef]     ] = None

class RuleGroupSourceStatelessRulesDetailsExtraOutputTypeDef(BaseValidatorModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionExtraOutputTypeDef] = None

class RuleGroupSourceStatelessRulesDetailsOutputTypeDef(BaseValidatorModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionOutputTypeDef] = None

class RuleGroupSourceStatelessRulesDetailsTypeDef(BaseValidatorModel):
    Priority: Optional[int] = None
    RuleDefinition: Optional[RuleGroupSourceStatelessRuleDefinitionTypeDef] = None

class FirewallPolicyStatelessCustomActionsDetailsExtraOutputTypeDef(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionExtraOutputTypeDef] = None
    ActionName: Optional[str] = None

class RuleGroupSourceCustomActionsDetailsExtraOutputTypeDef(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionExtraOutputTypeDef] = None
    ActionName: Optional[str] = None

class FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionOutputTypeDef] = None
    ActionName: Optional[str] = None

class RuleGroupSourceCustomActionsDetailsOutputTypeDef(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionOutputTypeDef] = None
    ActionName: Optional[str] = None

class FirewallPolicyStatelessCustomActionsDetailsTypeDef(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionTypeDef] = None
    ActionName: Optional[str] = None

class RuleGroupSourceCustomActionsDetailsTypeDef(BaseValidatorModel):
    ActionDefinition: Optional[StatelessCustomActionDefinitionTypeDef] = None
    ActionName: Optional[str] = None

class ActionExtraOutputTypeDef(BaseValidatorModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionActionTypeDef] = None
    AwsApiCallAction: Optional[AwsApiCallActionExtraOutputTypeDef] = None
    DnsRequestAction: Optional[DnsRequestActionTypeDef] = None
    PortProbeAction: Optional[PortProbeActionExtraOutputTypeDef] = None

class ActionOutputTypeDef(BaseValidatorModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionActionTypeDef] = None
    AwsApiCallAction: Optional[AwsApiCallActionOutputTypeDef] = None
    DnsRequestAction: Optional[DnsRequestActionTypeDef] = None
    PortProbeAction: Optional[PortProbeActionOutputTypeDef] = None

class ActionTypeDef(BaseValidatorModel):
    ActionType: Optional[str] = None
    NetworkConnectionAction: Optional[NetworkConnectionActionTypeDef] = None
    AwsApiCallAction: Optional[AwsApiCallActionTypeDef] = None
    DnsRequestAction: Optional[DnsRequestActionTypeDef] = None
    PortProbeAction: Optional[PortProbeActionTypeDef] = None

class CreateAutomationRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleOrder: int
    RuleName: str
    Description: str
    Criteria: AutomationRulesFindingFiltersTypeDef
    Actions: Sequence[AutomationRulesActionUnionTypeDef]
    Tags: Optional[Mapping[str, str]] = None
    RuleStatus: Optional[RuleStatusType] = None
    IsTerminal: Optional[bool] = None

class AwsBackupBackupPlanDetailsExtraOutputTypeDef(BaseValidatorModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsExtraOutputTypeDef] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None

class AwsBackupBackupPlanDetailsOutputTypeDef(BaseValidatorModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsOutputTypeDef] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None

class AwsBackupBackupPlanDetailsTypeDef(BaseValidatorModel):
    BackupPlan: Optional[AwsBackupBackupPlanBackupPlanDetailsTypeDef] = None
    BackupPlanArn: Optional[str] = None
    BackupPlanId: Optional[str] = None
    VersionId: Optional[str] = None

class AwsCloudFrontDistributionDetailsExtraOutputTypeDef(BaseValidatorModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsExtraOutputTypeDef] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLoggingTypeDef] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsExtraOutputTypeDef] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsExtraOutputTypeDef] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificateTypeDef] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None

class AwsCloudFrontDistributionDetailsOutputTypeDef(BaseValidatorModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsOutputTypeDef] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLoggingTypeDef] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsOutputTypeDef] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsOutputTypeDef] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificateTypeDef] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None

class AwsCloudFrontDistributionDetailsTypeDef(BaseValidatorModel):
    CacheBehaviors: Optional[AwsCloudFrontDistributionCacheBehaviorsTypeDef] = None
    DefaultCacheBehavior: Optional[AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef] = None
    DefaultRootObject: Optional[str] = None
    DomainName: Optional[str] = None
    ETag: Optional[str] = None
    LastModifiedTime: Optional[str] = None
    Logging: Optional[AwsCloudFrontDistributionLoggingTypeDef] = None
    Origins: Optional[AwsCloudFrontDistributionOriginsTypeDef] = None
    OriginGroups: Optional[AwsCloudFrontDistributionOriginGroupsTypeDef] = None
    ViewerCertificate: Optional[AwsCloudFrontDistributionViewerCertificateTypeDef] = None
    Status: Optional[str] = None
    WebAclId: Optional[str] = None

class AwsGuardDutyDetectorDetailsExtraOutputTypeDef(BaseValidatorModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetailsTypeDef] = None
    Features: Optional[List[AwsGuardDutyDetectorFeaturesDetailsTypeDef]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None

class AwsGuardDutyDetectorDetailsOutputTypeDef(BaseValidatorModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetailsTypeDef] = None
    Features: Optional[List[AwsGuardDutyDetectorFeaturesDetailsTypeDef]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None

class AwsGuardDutyDetectorDetailsTypeDef(BaseValidatorModel):
    DataSources: Optional[AwsGuardDutyDetectorDataSourcesDetailsTypeDef] = None
    Features: Optional[Sequence[AwsGuardDutyDetectorFeaturesDetailsTypeDef]] = None
    FindingPublishingFrequency: Optional[str] = None
    ServiceRole: Optional[str] = None
    Status: Optional[str] = None

class AwsMskClusterDetailsExtraOutputTypeDef(BaseValidatorModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsExtraOutputTypeDef] = None

class AwsMskClusterDetailsOutputTypeDef(BaseValidatorModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsOutputTypeDef] = None

class AwsMskClusterDetailsTypeDef(BaseValidatorModel):
    ClusterInfo: Optional[AwsMskClusterClusterInfoDetailsTypeDef] = None

class AwsS3BucketBucketLifecycleConfigurationRulesDetailsExtraOutputTypeDef(BaseValidatorModel):
    AbortIncompleteMultipartUpload: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef     ] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsExtraOutputTypeDef     ] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[       List[         AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef       ]     ] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]     ] = None

class AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef(BaseValidatorModel):
    AbortIncompleteMultipartUpload: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef     ] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsOutputTypeDef     ] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[       List[         AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef       ]     ] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]     ] = None

class AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef(BaseValidatorModel):
    AbortIncompleteMultipartUpload: Optional[       AwsS3BucketBucketLifecycleConfigurationRulesAbortIncompleteMultipartUploadDetailsTypeDef     ] = None
    ExpirationDate: Optional[str] = None
    ExpirationInDays: Optional[int] = None
    ExpiredObjectDeleteMarker: Optional[bool] = None
    Filter: Optional[AwsS3BucketBucketLifecycleConfigurationRulesFilterDetailsTypeDef] = None
    ID: Optional[str] = None
    NoncurrentVersionExpirationInDays: Optional[int] = None
    NoncurrentVersionTransitions: Optional[       Sequence[         AwsS3BucketBucketLifecycleConfigurationRulesNoncurrentVersionTransitionsDetailsTypeDef       ]     ] = None
    Prefix: Optional[str] = None
    Status: Optional[str] = None
    Transitions: Optional[       Sequence[AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetailsTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationExtraOutputTypeDef(BaseValidatorModel):
    Configurations: Optional[       List[AwsS3BucketNotificationConfigurationDetailExtraOutputTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationOutputTypeDef(BaseValidatorModel):
    Configurations: Optional[       List[AwsS3BucketNotificationConfigurationDetailOutputTypeDef]     ] = None

class AwsS3BucketNotificationConfigurationTypeDef(BaseValidatorModel):
    Configurations: Optional[Sequence[AwsS3BucketNotificationConfigurationDetailTypeDef]] = None

class AwsWafv2RulesDetailsExtraOutputTypeDef(BaseValidatorModel):
    Action: Optional[AwsWafv2RulesActionDetailsExtraOutputTypeDef] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2RulesDetailsOutputTypeDef(BaseValidatorModel):
    Action: Optional[AwsWafv2RulesActionDetailsOutputTypeDef] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2RulesDetailsTypeDef(BaseValidatorModel):
    Action: Optional[AwsWafv2RulesActionDetailsTypeDef] = None
    Name: Optional[str] = None
    OverrideAction: Optional[str] = None
    Priority: Optional[int] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class GetSecurityControlDefinitionResponseTypeDef(BaseValidatorModel):
    SecurityControlDefinition: SecurityControlDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSecurityControlDefinitionsResponseTypeDef(BaseValidatorModel):
    SecurityControlDefinitions: List[SecurityControlDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetAutomationRulesResponseTypeDef(BaseValidatorModel):
    Rules: List[AutomationRulesConfigTypeDef]
    UnprocessedAutomationRules: List[UnprocessedAutomationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateAutomationRulesRequestRequestTypeDef(BaseValidatorModel):
    UpdateAutomationRulesRequestItems: Sequence[UpdateAutomationRulesRequestItemTypeDef]

class GetInsightsResponseTypeDef(BaseValidatorModel):
    Insights: List[InsightTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CustomDataIdentifiersResultExtraOutputTypeDef(BaseValidatorModel):
    Detections: Optional[List[CustomDataIdentifiersDetectionsExtraOutputTypeDef]] = None
    TotalCount: Optional[int] = None

class SensitiveDataResultExtraOutputTypeDef(BaseValidatorModel):
    Category: Optional[str] = None
    Detections: Optional[List[SensitiveDataDetectionsExtraOutputTypeDef]] = None
    TotalCount: Optional[int] = None

class CustomDataIdentifiersResultOutputTypeDef(BaseValidatorModel):
    Detections: Optional[List[CustomDataIdentifiersDetectionsOutputTypeDef]] = None
    TotalCount: Optional[int] = None

class SensitiveDataResultOutputTypeDef(BaseValidatorModel):
    Category: Optional[str] = None
    Detections: Optional[List[SensitiveDataDetectionsOutputTypeDef]] = None
    TotalCount: Optional[int] = None

class CustomDataIdentifiersResultTypeDef(BaseValidatorModel):
    Detections: Optional[Sequence[CustomDataIdentifiersDetectionsTypeDef]] = None
    TotalCount: Optional[int] = None

class SensitiveDataResultTypeDef(BaseValidatorModel):
    Category: Optional[str] = None
    Detections: Optional[Sequence[SensitiveDataDetectionsTypeDef]] = None
    TotalCount: Optional[int] = None

class SecurityHubPolicyOutputTypeDef(BaseValidatorModel):
    ServiceEnabled: Optional[bool] = None
    EnabledStandardIdentifiers: Optional[List[str]] = None
    SecurityControlsConfiguration: Optional[SecurityControlsConfigurationOutputTypeDef] = None

class SecurityHubPolicyTypeDef(BaseValidatorModel):
    ServiceEnabled: Optional[bool] = None
    EnabledStandardIdentifiers: Optional[Sequence[str]] = None
    SecurityControlsConfiguration: Optional[SecurityControlsConfigurationTypeDef] = None

class FirewallPolicyDetailsExtraOutputTypeDef(BaseValidatorModel):
    StatefulRuleGroupReferences: Optional[       List[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]     ] = None
    StatelessCustomActions: Optional[       List[FirewallPolicyStatelessCustomActionsDetailsExtraOutputTypeDef]     ] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessRuleGroupReferences: Optional[       List[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]     ] = None

class RuleGroupSourceStatelessRulesAndCustomActionsDetailsExtraOutputTypeDef(BaseValidatorModel):
    CustomActions: Optional[List[RuleGroupSourceCustomActionsDetailsExtraOutputTypeDef]] = None
    StatelessRules: Optional[List[RuleGroupSourceStatelessRulesDetailsExtraOutputTypeDef]] = None

class FirewallPolicyDetailsOutputTypeDef(BaseValidatorModel):
    StatefulRuleGroupReferences: Optional[       List[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]     ] = None
    StatelessCustomActions: Optional[       List[FirewallPolicyStatelessCustomActionsDetailsOutputTypeDef]     ] = None
    StatelessDefaultActions: Optional[List[str]] = None
    StatelessFragmentDefaultActions: Optional[List[str]] = None
    StatelessRuleGroupReferences: Optional[       List[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]     ] = None

class RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef(BaseValidatorModel):
    CustomActions: Optional[List[RuleGroupSourceCustomActionsDetailsOutputTypeDef]] = None
    StatelessRules: Optional[List[RuleGroupSourceStatelessRulesDetailsOutputTypeDef]] = None

class FirewallPolicyDetailsTypeDef(BaseValidatorModel):
    StatefulRuleGroupReferences: Optional[       Sequence[FirewallPolicyStatefulRuleGroupReferencesDetailsTypeDef]     ] = None
    StatelessCustomActions: Optional[       Sequence[FirewallPolicyStatelessCustomActionsDetailsTypeDef]     ] = None
    StatelessDefaultActions: Optional[Sequence[str]] = None
    StatelessFragmentDefaultActions: Optional[Sequence[str]] = None
    StatelessRuleGroupReferences: Optional[       Sequence[FirewallPolicyStatelessRuleGroupReferencesDetailsTypeDef]     ] = None

class RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef(BaseValidatorModel):
    CustomActions: Optional[Sequence[RuleGroupSourceCustomActionsDetailsTypeDef]] = None
    StatelessRules: Optional[Sequence[RuleGroupSourceStatelessRulesDetailsTypeDef]] = None

class AwsS3BucketBucketLifecycleConfigurationDetailsExtraOutputTypeDef(BaseValidatorModel):
    Rules: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsExtraOutputTypeDef]     ] = None

class AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef(BaseValidatorModel):
    Rules: Optional[       List[AwsS3BucketBucketLifecycleConfigurationRulesDetailsOutputTypeDef]     ] = None

class AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef(BaseValidatorModel):
    Rules: Optional[Sequence[AwsS3BucketBucketLifecycleConfigurationRulesDetailsTypeDef]] = None

class AwsWafv2RuleGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsExtraOutputTypeDef]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2WebAclDetailsExtraOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetailsTypeDef] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsExtraOutputTypeDef] = None
    Description: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsExtraOutputTypeDef]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2RuleGroupDetailsOutputTypeDef(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsOutputTypeDef]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2WebAclDetailsOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetailsTypeDef] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsOutputTypeDef] = None
    Description: Optional[str] = None
    Rules: Optional[List[AwsWafv2RulesDetailsOutputTypeDef]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2RuleGroupDetailsTypeDef(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Arn: Optional[str] = None
    Rules: Optional[Sequence[AwsWafv2RulesDetailsTypeDef]] = None
    Scope: Optional[str] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class AwsWafv2WebAclDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None
    ManagedbyFirewallManager: Optional[bool] = None
    Id: Optional[str] = None
    Capacity: Optional[int] = None
    CaptchaConfig: Optional[AwsWafv2WebAclCaptchaConfigDetailsTypeDef] = None
    DefaultAction: Optional[AwsWafv2WebAclActionDetailsTypeDef] = None
    Description: Optional[str] = None
    Rules: Optional[Sequence[AwsWafv2RulesDetailsTypeDef]] = None
    VisibilityConfig: Optional[AwsWafv2VisibilityConfigDetailsTypeDef] = None

class ClassificationResultExtraOutputTypeDef(BaseValidatorModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatusTypeDef] = None
    SensitiveData: Optional[List[SensitiveDataResultExtraOutputTypeDef]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultExtraOutputTypeDef] = None

class ClassificationResultOutputTypeDef(BaseValidatorModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatusTypeDef] = None
    SensitiveData: Optional[List[SensitiveDataResultOutputTypeDef]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultOutputTypeDef] = None

class ClassificationResultTypeDef(BaseValidatorModel):
    MimeType: Optional[str] = None
    SizeClassified: Optional[int] = None
    AdditionalOccurrences: Optional[bool] = None
    Status: Optional[ClassificationStatusTypeDef] = None
    SensitiveData: Optional[Sequence[SensitiveDataResultTypeDef]] = None
    CustomDataIdentifiers: Optional[CustomDataIdentifiersResultTypeDef] = None

class PolicyOutputTypeDef(BaseValidatorModel):
    SecurityHub: Optional[SecurityHubPolicyOutputTypeDef] = None

class PolicyTypeDef(BaseValidatorModel):
    SecurityHub: Optional[SecurityHubPolicyTypeDef] = None

class AwsNetworkFirewallFirewallPolicyDetailsExtraOutputTypeDef(BaseValidatorModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsExtraOutputTypeDef] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None

class RuleGroupSourceExtraOutputTypeDef(BaseValidatorModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsExtraOutputTypeDef] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[List[RuleGroupSourceStatefulRulesDetailsExtraOutputTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[       RuleGroupSourceStatelessRulesAndCustomActionsDetailsExtraOutputTypeDef     ] = None

class AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef(BaseValidatorModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsOutputTypeDef] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None

class RuleGroupSourceOutputTypeDef(BaseValidatorModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsOutputTypeDef] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[List[RuleGroupSourceStatefulRulesDetailsOutputTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[       RuleGroupSourceStatelessRulesAndCustomActionsDetailsOutputTypeDef     ] = None

class AwsNetworkFirewallFirewallPolicyDetailsTypeDef(BaseValidatorModel):
    FirewallPolicy: Optional[FirewallPolicyDetailsTypeDef] = None
    FirewallPolicyArn: Optional[str] = None
    FirewallPolicyId: Optional[str] = None
    FirewallPolicyName: Optional[str] = None
    Description: Optional[str] = None

class RuleGroupSourceTypeDef(BaseValidatorModel):
    RulesSourceList: Optional[RuleGroupSourceListDetailsTypeDef] = None
    RulesString: Optional[str] = None
    StatefulRules: Optional[Sequence[RuleGroupSourceStatefulRulesDetailsTypeDef]] = None
    StatelessRulesAndCustomActions: Optional[       RuleGroupSourceStatelessRulesAndCustomActionsDetailsTypeDef     ] = None

class AwsS3BucketDetailsExtraOutputTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[       AwsS3BucketServerSideEncryptionConfigurationExtraOutputTypeDef     ] = None
    BucketLifecycleConfiguration: Optional[       AwsS3BucketBucketLifecycleConfigurationDetailsExtraOutputTypeDef     ] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfigurationTypeDef] = None
    BucketWebsiteConfiguration: Optional[       AwsS3BucketWebsiteConfigurationExtraOutputTypeDef     ] = None
    BucketNotificationConfiguration: Optional[       AwsS3BucketNotificationConfigurationExtraOutputTypeDef     ] = None
    BucketVersioningConfiguration: Optional[       AwsS3BucketBucketVersioningConfigurationTypeDef     ] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfigurationTypeDef] = None
    Name: Optional[str] = None

class AwsS3BucketDetailsOutputTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[       AwsS3BucketServerSideEncryptionConfigurationOutputTypeDef     ] = None
    BucketLifecycleConfiguration: Optional[       AwsS3BucketBucketLifecycleConfigurationDetailsOutputTypeDef     ] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfigurationTypeDef] = None
    BucketWebsiteConfiguration: Optional[AwsS3BucketWebsiteConfigurationOutputTypeDef] = None
    BucketNotificationConfiguration: Optional[       AwsS3BucketNotificationConfigurationOutputTypeDef     ] = None
    BucketVersioningConfiguration: Optional[       AwsS3BucketBucketVersioningConfigurationTypeDef     ] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfigurationTypeDef] = None
    Name: Optional[str] = None

class AwsS3BucketDetailsTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    CreatedAt: Optional[str] = None
    ServerSideEncryptionConfiguration: Optional[       AwsS3BucketServerSideEncryptionConfigurationTypeDef     ] = None
    BucketLifecycleConfiguration: Optional[       AwsS3BucketBucketLifecycleConfigurationDetailsTypeDef     ] = None
    PublicAccessBlockConfiguration: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AccessControlList: Optional[str] = None
    BucketLoggingConfiguration: Optional[AwsS3BucketLoggingConfigurationTypeDef] = None
    BucketWebsiteConfiguration: Optional[AwsS3BucketWebsiteConfigurationTypeDef] = None
    BucketNotificationConfiguration: Optional[AwsS3BucketNotificationConfigurationTypeDef] = None
    BucketVersioningConfiguration: Optional[       AwsS3BucketBucketVersioningConfigurationTypeDef     ] = None
    ObjectLockConfiguration: Optional[AwsS3BucketObjectLockConfigurationTypeDef] = None
    Name: Optional[str] = None

class DataClassificationDetailsExtraOutputTypeDef(BaseValidatorModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultExtraOutputTypeDef] = None

class DataClassificationDetailsOutputTypeDef(BaseValidatorModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultOutputTypeDef] = None

class DataClassificationDetailsTypeDef(BaseValidatorModel):
    DetailedResultsLocation: Optional[str] = None
    Result: Optional[ClassificationResultTypeDef] = None

class CreateConfigurationPolicyResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfigurationPolicyResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfigurationPolicyResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    UpdatedAt: datetime
    CreatedAt: datetime
    ConfigurationPolicy: PolicyOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationPolicyRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ConfigurationPolicy: PolicyTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateConfigurationPolicyRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    UpdatedReason: Optional[str] = None
    ConfigurationPolicy: Optional[PolicyTypeDef] = None

class RuleGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    RuleVariables: Optional[RuleGroupVariablesExtraOutputTypeDef] = None
    RulesSource: Optional[RuleGroupSourceExtraOutputTypeDef] = None

class RuleGroupDetailsOutputTypeDef(BaseValidatorModel):
    RuleVariables: Optional[RuleGroupVariablesOutputTypeDef] = None
    RulesSource: Optional[RuleGroupSourceOutputTypeDef] = None

class RuleGroupDetailsTypeDef(BaseValidatorModel):
    RuleVariables: Optional[RuleGroupVariablesTypeDef] = None
    RulesSource: Optional[RuleGroupSourceTypeDef] = None

class AwsNetworkFirewallRuleGroupDetailsExtraOutputTypeDef(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    RuleGroup: Optional[RuleGroupDetailsExtraOutputTypeDef] = None
    RuleGroupArn: Optional[str] = None
    RuleGroupId: Optional[str] = None
    RuleGroupName: Optional[str] = None
    Type: Optional[str] = None

class AwsNetworkFirewallRuleGroupDetailsOutputTypeDef(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    RuleGroup: Optional[RuleGroupDetailsOutputTypeDef] = None
    RuleGroupArn: Optional[str] = None
    RuleGroupId: Optional[str] = None
    RuleGroupName: Optional[str] = None
    Type: Optional[str] = None

class AwsNetworkFirewallRuleGroupDetailsTypeDef(BaseValidatorModel):
    Capacity: Optional[int] = None
    Description: Optional[str] = None
    RuleGroup: Optional[RuleGroupDetailsTypeDef] = None
    RuleGroupArn: Optional[str] = None
    RuleGroupId: Optional[str] = None
    RuleGroupName: Optional[str] = None
    Type: Optional[str] = None

class ResourceDetailsExtraOutputTypeDef(BaseValidatorModel):
    AwsAutoScalingAutoScalingGroup: Optional[       AwsAutoScalingAutoScalingGroupDetailsExtraOutputTypeDef     ] = None
    AwsCodeBuildProject: Optional[AwsCodeBuildProjectDetailsExtraOutputTypeDef] = None
    AwsCloudFrontDistribution: Optional[       AwsCloudFrontDistributionDetailsExtraOutputTypeDef     ] = None
    AwsEc2Instance: Optional[AwsEc2InstanceDetailsExtraOutputTypeDef] = None
    AwsEc2NetworkInterface: Optional[AwsEc2NetworkInterfaceDetailsExtraOutputTypeDef] = None
    AwsEc2SecurityGroup: Optional[AwsEc2SecurityGroupDetailsExtraOutputTypeDef] = None
    AwsEc2Volume: Optional[AwsEc2VolumeDetailsExtraOutputTypeDef] = None
    AwsEc2Vpc: Optional[AwsEc2VpcDetailsExtraOutputTypeDef] = None
    AwsEc2Eip: Optional[AwsEc2EipDetailsTypeDef] = None
    AwsEc2Subnet: Optional[AwsEc2SubnetDetailsExtraOutputTypeDef] = None
    AwsEc2NetworkAcl: Optional[AwsEc2NetworkAclDetailsExtraOutputTypeDef] = None
    AwsElbv2LoadBalancer: Optional[AwsElbv2LoadBalancerDetailsExtraOutputTypeDef] = None
    AwsElasticBeanstalkEnvironment: Optional[       AwsElasticBeanstalkEnvironmentDetailsExtraOutputTypeDef     ] = None
    AwsElasticsearchDomain: Optional[AwsElasticsearchDomainDetailsExtraOutputTypeDef] = None
    AwsS3Bucket: Optional[AwsS3BucketDetailsExtraOutputTypeDef] = None
    AwsS3AccountPublicAccessBlock: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AwsS3Object: Optional[AwsS3ObjectDetailsTypeDef] = None
    AwsSecretsManagerSecret: Optional[AwsSecretsManagerSecretDetailsTypeDef] = None
    AwsIamAccessKey: Optional[AwsIamAccessKeyDetailsTypeDef] = None
    AwsIamUser: Optional[AwsIamUserDetailsExtraOutputTypeDef] = None
    AwsIamPolicy: Optional[AwsIamPolicyDetailsExtraOutputTypeDef] = None
    AwsApiGatewayV2Stage: Optional[AwsApiGatewayV2StageDetailsExtraOutputTypeDef] = None
    AwsApiGatewayV2Api: Optional[AwsApiGatewayV2ApiDetailsExtraOutputTypeDef] = None
    AwsDynamoDbTable: Optional[AwsDynamoDbTableDetailsExtraOutputTypeDef] = None
    AwsApiGatewayStage: Optional[AwsApiGatewayStageDetailsExtraOutputTypeDef] = None
    AwsApiGatewayRestApi: Optional[AwsApiGatewayRestApiDetailsExtraOutputTypeDef] = None
    AwsCloudTrailTrail: Optional[AwsCloudTrailTrailDetailsTypeDef] = None
    AwsSsmPatchCompliance: Optional[AwsSsmPatchComplianceDetailsTypeDef] = None
    AwsCertificateManagerCertificate: Optional[       AwsCertificateManagerCertificateDetailsExtraOutputTypeDef     ] = None
    AwsRedshiftCluster: Optional[AwsRedshiftClusterDetailsExtraOutputTypeDef] = None
    AwsElbLoadBalancer: Optional[AwsElbLoadBalancerDetailsExtraOutputTypeDef] = None
    AwsIamGroup: Optional[AwsIamGroupDetailsExtraOutputTypeDef] = None
    AwsIamRole: Optional[AwsIamRoleDetailsExtraOutputTypeDef] = None
    AwsKmsKey: Optional[AwsKmsKeyDetailsTypeDef] = None
    AwsLambdaFunction: Optional[AwsLambdaFunctionDetailsExtraOutputTypeDef] = None
    AwsLambdaLayerVersion: Optional[AwsLambdaLayerVersionDetailsExtraOutputTypeDef] = None
    AwsRdsDbInstance: Optional[AwsRdsDbInstanceDetailsExtraOutputTypeDef] = None
    AwsSnsTopic: Optional[AwsSnsTopicDetailsExtraOutputTypeDef] = None
    AwsSqsQueue: Optional[AwsSqsQueueDetailsTypeDef] = None
    AwsWafWebAcl: Optional[AwsWafWebAclDetailsExtraOutputTypeDef] = None
    AwsRdsDbSnapshot: Optional[AwsRdsDbSnapshotDetailsExtraOutputTypeDef] = None
    AwsRdsDbClusterSnapshot: Optional[AwsRdsDbClusterSnapshotDetailsExtraOutputTypeDef] = None
    AwsRdsDbCluster: Optional[AwsRdsDbClusterDetailsExtraOutputTypeDef] = None
    AwsEcsCluster: Optional[AwsEcsClusterDetailsExtraOutputTypeDef] = None
    AwsEcsContainer: Optional[AwsEcsContainerDetailsExtraOutputTypeDef] = None
    AwsEcsTaskDefinition: Optional[AwsEcsTaskDefinitionDetailsExtraOutputTypeDef] = None
    Container: Optional[ContainerDetailsExtraOutputTypeDef] = None
    Other: Optional[Dict[str, str]] = None
    AwsRdsEventSubscription: Optional[AwsRdsEventSubscriptionDetailsExtraOutputTypeDef] = None
    AwsEcsService: Optional[AwsEcsServiceDetailsExtraOutputTypeDef] = None
    AwsAutoScalingLaunchConfiguration: Optional[       AwsAutoScalingLaunchConfigurationDetailsExtraOutputTypeDef     ] = None
    AwsEc2VpnConnection: Optional[AwsEc2VpnConnectionDetailsExtraOutputTypeDef] = None
    AwsEcrContainerImage: Optional[AwsEcrContainerImageDetailsExtraOutputTypeDef] = None
    AwsOpenSearchServiceDomain: Optional[       AwsOpenSearchServiceDomainDetailsExtraOutputTypeDef     ] = None
    AwsEc2VpcEndpointService: Optional[AwsEc2VpcEndpointServiceDetailsExtraOutputTypeDef] = None
    AwsXrayEncryptionConfig: Optional[AwsXrayEncryptionConfigDetailsTypeDef] = None
    AwsWafRateBasedRule: Optional[AwsWafRateBasedRuleDetailsExtraOutputTypeDef] = None
    AwsWafRegionalRateBasedRule: Optional[       AwsWafRegionalRateBasedRuleDetailsExtraOutputTypeDef     ] = None
    AwsEcrRepository: Optional[AwsEcrRepositoryDetailsTypeDef] = None
    AwsEksCluster: Optional[AwsEksClusterDetailsExtraOutputTypeDef] = None
    AwsNetworkFirewallFirewallPolicy: Optional[       AwsNetworkFirewallFirewallPolicyDetailsExtraOutputTypeDef     ] = None
    AwsNetworkFirewallFirewall: Optional[       AwsNetworkFirewallFirewallDetailsExtraOutputTypeDef     ] = None
    AwsNetworkFirewallRuleGroup: Optional[       AwsNetworkFirewallRuleGroupDetailsExtraOutputTypeDef     ] = None
    AwsRdsDbSecurityGroup: Optional[AwsRdsDbSecurityGroupDetailsExtraOutputTypeDef] = None
    AwsKinesisStream: Optional[AwsKinesisStreamDetailsTypeDef] = None
    AwsEc2TransitGateway: Optional[AwsEc2TransitGatewayDetailsExtraOutputTypeDef] = None
    AwsEfsAccessPoint: Optional[AwsEfsAccessPointDetailsExtraOutputTypeDef] = None
    AwsCloudFormationStack: Optional[AwsCloudFormationStackDetailsExtraOutputTypeDef] = None
    AwsCloudWatchAlarm: Optional[AwsCloudWatchAlarmDetailsExtraOutputTypeDef] = None
    AwsEc2VpcPeeringConnection: Optional[       AwsEc2VpcPeeringConnectionDetailsExtraOutputTypeDef     ] = None
    AwsWafRegionalRuleGroup: Optional[AwsWafRegionalRuleGroupDetailsExtraOutputTypeDef] = None
    AwsWafRegionalRule: Optional[AwsWafRegionalRuleDetailsExtraOutputTypeDef] = None
    AwsWafRegionalWebAcl: Optional[AwsWafRegionalWebAclDetailsExtraOutputTypeDef] = None
    AwsWafRule: Optional[AwsWafRuleDetailsExtraOutputTypeDef] = None
    AwsWafRuleGroup: Optional[AwsWafRuleGroupDetailsExtraOutputTypeDef] = None
    AwsEcsTask: Optional[AwsEcsTaskDetailsExtraOutputTypeDef] = None
    AwsBackupBackupVault: Optional[AwsBackupBackupVaultDetailsExtraOutputTypeDef] = None
    AwsBackupBackupPlan: Optional[AwsBackupBackupPlanDetailsExtraOutputTypeDef] = None
    AwsBackupRecoveryPoint: Optional[AwsBackupRecoveryPointDetailsTypeDef] = None
    AwsEc2LaunchTemplate: Optional[AwsEc2LaunchTemplateDetailsExtraOutputTypeDef] = None
    AwsSageMakerNotebookInstance: Optional[       AwsSageMakerNotebookInstanceDetailsExtraOutputTypeDef     ] = None
    AwsWafv2WebAcl: Optional[AwsWafv2WebAclDetailsExtraOutputTypeDef] = None
    AwsWafv2RuleGroup: Optional[AwsWafv2RuleGroupDetailsExtraOutputTypeDef] = None
    AwsEc2RouteTable: Optional[AwsEc2RouteTableDetailsExtraOutputTypeDef] = None
    AwsAmazonMqBroker: Optional[AwsAmazonMqBrokerDetailsExtraOutputTypeDef] = None
    AwsAppSyncGraphQlApi: Optional[AwsAppSyncGraphQlApiDetailsExtraOutputTypeDef] = None
    AwsEventSchemasRegistry: Optional[AwsEventSchemasRegistryDetailsTypeDef] = None
    AwsGuardDutyDetector: Optional[AwsGuardDutyDetectorDetailsExtraOutputTypeDef] = None
    AwsStepFunctionStateMachine: Optional[       AwsStepFunctionStateMachineDetailsExtraOutputTypeDef     ] = None
    AwsAthenaWorkGroup: Optional[AwsAthenaWorkGroupDetailsTypeDef] = None
    AwsEventsEventbus: Optional[AwsEventsEventbusDetailsTypeDef] = None
    AwsDmsEndpoint: Optional[AwsDmsEndpointDetailsTypeDef] = None
    AwsEventsEndpoint: Optional[AwsEventsEndpointDetailsExtraOutputTypeDef] = None
    AwsDmsReplicationTask: Optional[AwsDmsReplicationTaskDetailsTypeDef] = None
    AwsDmsReplicationInstance: Optional[       AwsDmsReplicationInstanceDetailsExtraOutputTypeDef     ] = None
    AwsRoute53HostedZone: Optional[AwsRoute53HostedZoneDetailsExtraOutputTypeDef] = None
    AwsMskCluster: Optional[AwsMskClusterDetailsExtraOutputTypeDef] = None
    AwsS3AccessPoint: Optional[AwsS3AccessPointDetailsTypeDef] = None
    AwsEc2ClientVpnEndpoint: Optional[AwsEc2ClientVpnEndpointDetailsExtraOutputTypeDef] = None

class ResourceDetailsOutputTypeDef(BaseValidatorModel):
    AwsAutoScalingAutoScalingGroup: Optional[       AwsAutoScalingAutoScalingGroupDetailsOutputTypeDef     ] = None
    AwsCodeBuildProject: Optional[AwsCodeBuildProjectDetailsOutputTypeDef] = None
    AwsCloudFrontDistribution: Optional[AwsCloudFrontDistributionDetailsOutputTypeDef] = None
    AwsEc2Instance: Optional[AwsEc2InstanceDetailsOutputTypeDef] = None
    AwsEc2NetworkInterface: Optional[AwsEc2NetworkInterfaceDetailsOutputTypeDef] = None
    AwsEc2SecurityGroup: Optional[AwsEc2SecurityGroupDetailsOutputTypeDef] = None
    AwsEc2Volume: Optional[AwsEc2VolumeDetailsOutputTypeDef] = None
    AwsEc2Vpc: Optional[AwsEc2VpcDetailsOutputTypeDef] = None
    AwsEc2Eip: Optional[AwsEc2EipDetailsTypeDef] = None
    AwsEc2Subnet: Optional[AwsEc2SubnetDetailsOutputTypeDef] = None
    AwsEc2NetworkAcl: Optional[AwsEc2NetworkAclDetailsOutputTypeDef] = None
    AwsElbv2LoadBalancer: Optional[AwsElbv2LoadBalancerDetailsOutputTypeDef] = None
    AwsElasticBeanstalkEnvironment: Optional[       AwsElasticBeanstalkEnvironmentDetailsOutputTypeDef     ] = None
    AwsElasticsearchDomain: Optional[AwsElasticsearchDomainDetailsOutputTypeDef] = None
    AwsS3Bucket: Optional[AwsS3BucketDetailsOutputTypeDef] = None
    AwsS3AccountPublicAccessBlock: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AwsS3Object: Optional[AwsS3ObjectDetailsTypeDef] = None
    AwsSecretsManagerSecret: Optional[AwsSecretsManagerSecretDetailsTypeDef] = None
    AwsIamAccessKey: Optional[AwsIamAccessKeyDetailsTypeDef] = None
    AwsIamUser: Optional[AwsIamUserDetailsOutputTypeDef] = None
    AwsIamPolicy: Optional[AwsIamPolicyDetailsOutputTypeDef] = None
    AwsApiGatewayV2Stage: Optional[AwsApiGatewayV2StageDetailsOutputTypeDef] = None
    AwsApiGatewayV2Api: Optional[AwsApiGatewayV2ApiDetailsOutputTypeDef] = None
    AwsDynamoDbTable: Optional[AwsDynamoDbTableDetailsOutputTypeDef] = None
    AwsApiGatewayStage: Optional[AwsApiGatewayStageDetailsOutputTypeDef] = None
    AwsApiGatewayRestApi: Optional[AwsApiGatewayRestApiDetailsOutputTypeDef] = None
    AwsCloudTrailTrail: Optional[AwsCloudTrailTrailDetailsTypeDef] = None
    AwsSsmPatchCompliance: Optional[AwsSsmPatchComplianceDetailsTypeDef] = None
    AwsCertificateManagerCertificate: Optional[       AwsCertificateManagerCertificateDetailsOutputTypeDef     ] = None
    AwsRedshiftCluster: Optional[AwsRedshiftClusterDetailsOutputTypeDef] = None
    AwsElbLoadBalancer: Optional[AwsElbLoadBalancerDetailsOutputTypeDef] = None
    AwsIamGroup: Optional[AwsIamGroupDetailsOutputTypeDef] = None
    AwsIamRole: Optional[AwsIamRoleDetailsOutputTypeDef] = None
    AwsKmsKey: Optional[AwsKmsKeyDetailsTypeDef] = None
    AwsLambdaFunction: Optional[AwsLambdaFunctionDetailsOutputTypeDef] = None
    AwsLambdaLayerVersion: Optional[AwsLambdaLayerVersionDetailsOutputTypeDef] = None
    AwsRdsDbInstance: Optional[AwsRdsDbInstanceDetailsOutputTypeDef] = None
    AwsSnsTopic: Optional[AwsSnsTopicDetailsOutputTypeDef] = None
    AwsSqsQueue: Optional[AwsSqsQueueDetailsTypeDef] = None
    AwsWafWebAcl: Optional[AwsWafWebAclDetailsOutputTypeDef] = None
    AwsRdsDbSnapshot: Optional[AwsRdsDbSnapshotDetailsOutputTypeDef] = None
    AwsRdsDbClusterSnapshot: Optional[AwsRdsDbClusterSnapshotDetailsOutputTypeDef] = None
    AwsRdsDbCluster: Optional[AwsRdsDbClusterDetailsOutputTypeDef] = None
    AwsEcsCluster: Optional[AwsEcsClusterDetailsOutputTypeDef] = None
    AwsEcsContainer: Optional[AwsEcsContainerDetailsOutputTypeDef] = None
    AwsEcsTaskDefinition: Optional[AwsEcsTaskDefinitionDetailsOutputTypeDef] = None
    Container: Optional[ContainerDetailsOutputTypeDef] = None
    Other: Optional[Dict[str, str]] = None
    AwsRdsEventSubscription: Optional[AwsRdsEventSubscriptionDetailsOutputTypeDef] = None
    AwsEcsService: Optional[AwsEcsServiceDetailsOutputTypeDef] = None
    AwsAutoScalingLaunchConfiguration: Optional[       AwsAutoScalingLaunchConfigurationDetailsOutputTypeDef     ] = None
    AwsEc2VpnConnection: Optional[AwsEc2VpnConnectionDetailsOutputTypeDef] = None
    AwsEcrContainerImage: Optional[AwsEcrContainerImageDetailsOutputTypeDef] = None
    AwsOpenSearchServiceDomain: Optional[AwsOpenSearchServiceDomainDetailsOutputTypeDef] = None
    AwsEc2VpcEndpointService: Optional[AwsEc2VpcEndpointServiceDetailsOutputTypeDef] = None
    AwsXrayEncryptionConfig: Optional[AwsXrayEncryptionConfigDetailsTypeDef] = None
    AwsWafRateBasedRule: Optional[AwsWafRateBasedRuleDetailsOutputTypeDef] = None
    AwsWafRegionalRateBasedRule: Optional[AwsWafRegionalRateBasedRuleDetailsOutputTypeDef] = None
    AwsEcrRepository: Optional[AwsEcrRepositoryDetailsTypeDef] = None
    AwsEksCluster: Optional[AwsEksClusterDetailsOutputTypeDef] = None
    AwsNetworkFirewallFirewallPolicy: Optional[       AwsNetworkFirewallFirewallPolicyDetailsOutputTypeDef     ] = None
    AwsNetworkFirewallFirewall: Optional[AwsNetworkFirewallFirewallDetailsOutputTypeDef] = None
    AwsNetworkFirewallRuleGroup: Optional[AwsNetworkFirewallRuleGroupDetailsOutputTypeDef] = None
    AwsRdsDbSecurityGroup: Optional[AwsRdsDbSecurityGroupDetailsOutputTypeDef] = None
    AwsKinesisStream: Optional[AwsKinesisStreamDetailsTypeDef] = None
    AwsEc2TransitGateway: Optional[AwsEc2TransitGatewayDetailsOutputTypeDef] = None
    AwsEfsAccessPoint: Optional[AwsEfsAccessPointDetailsOutputTypeDef] = None
    AwsCloudFormationStack: Optional[AwsCloudFormationStackDetailsOutputTypeDef] = None
    AwsCloudWatchAlarm: Optional[AwsCloudWatchAlarmDetailsOutputTypeDef] = None
    AwsEc2VpcPeeringConnection: Optional[AwsEc2VpcPeeringConnectionDetailsOutputTypeDef] = None
    AwsWafRegionalRuleGroup: Optional[AwsWafRegionalRuleGroupDetailsOutputTypeDef] = None
    AwsWafRegionalRule: Optional[AwsWafRegionalRuleDetailsOutputTypeDef] = None
    AwsWafRegionalWebAcl: Optional[AwsWafRegionalWebAclDetailsOutputTypeDef] = None
    AwsWafRule: Optional[AwsWafRuleDetailsOutputTypeDef] = None
    AwsWafRuleGroup: Optional[AwsWafRuleGroupDetailsOutputTypeDef] = None
    AwsEcsTask: Optional[AwsEcsTaskDetailsOutputTypeDef] = None
    AwsBackupBackupVault: Optional[AwsBackupBackupVaultDetailsOutputTypeDef] = None
    AwsBackupBackupPlan: Optional[AwsBackupBackupPlanDetailsOutputTypeDef] = None
    AwsBackupRecoveryPoint: Optional[AwsBackupRecoveryPointDetailsTypeDef] = None
    AwsEc2LaunchTemplate: Optional[AwsEc2LaunchTemplateDetailsOutputTypeDef] = None
    AwsSageMakerNotebookInstance: Optional[       AwsSageMakerNotebookInstanceDetailsOutputTypeDef     ] = None
    AwsWafv2WebAcl: Optional[AwsWafv2WebAclDetailsOutputTypeDef] = None
    AwsWafv2RuleGroup: Optional[AwsWafv2RuleGroupDetailsOutputTypeDef] = None
    AwsEc2RouteTable: Optional[AwsEc2RouteTableDetailsOutputTypeDef] = None
    AwsAmazonMqBroker: Optional[AwsAmazonMqBrokerDetailsOutputTypeDef] = None
    AwsAppSyncGraphQlApi: Optional[AwsAppSyncGraphQlApiDetailsOutputTypeDef] = None
    AwsEventSchemasRegistry: Optional[AwsEventSchemasRegistryDetailsTypeDef] = None
    AwsGuardDutyDetector: Optional[AwsGuardDutyDetectorDetailsOutputTypeDef] = None
    AwsStepFunctionStateMachine: Optional[AwsStepFunctionStateMachineDetailsOutputTypeDef] = None
    AwsAthenaWorkGroup: Optional[AwsAthenaWorkGroupDetailsTypeDef] = None
    AwsEventsEventbus: Optional[AwsEventsEventbusDetailsTypeDef] = None
    AwsDmsEndpoint: Optional[AwsDmsEndpointDetailsTypeDef] = None
    AwsEventsEndpoint: Optional[AwsEventsEndpointDetailsOutputTypeDef] = None
    AwsDmsReplicationTask: Optional[AwsDmsReplicationTaskDetailsTypeDef] = None
    AwsDmsReplicationInstance: Optional[AwsDmsReplicationInstanceDetailsOutputTypeDef] = None
    AwsRoute53HostedZone: Optional[AwsRoute53HostedZoneDetailsOutputTypeDef] = None
    AwsMskCluster: Optional[AwsMskClusterDetailsOutputTypeDef] = None
    AwsS3AccessPoint: Optional[AwsS3AccessPointDetailsTypeDef] = None
    AwsEc2ClientVpnEndpoint: Optional[AwsEc2ClientVpnEndpointDetailsOutputTypeDef] = None

class ResourceDetailsTypeDef(BaseValidatorModel):
    AwsAutoScalingAutoScalingGroup: Optional[AwsAutoScalingAutoScalingGroupDetailsTypeDef] = None
    AwsCodeBuildProject: Optional[AwsCodeBuildProjectDetailsTypeDef] = None
    AwsCloudFrontDistribution: Optional[AwsCloudFrontDistributionDetailsTypeDef] = None
    AwsEc2Instance: Optional[AwsEc2InstanceDetailsTypeDef] = None
    AwsEc2NetworkInterface: Optional[AwsEc2NetworkInterfaceDetailsTypeDef] = None
    AwsEc2SecurityGroup: Optional[AwsEc2SecurityGroupDetailsTypeDef] = None
    AwsEc2Volume: Optional[AwsEc2VolumeDetailsTypeDef] = None
    AwsEc2Vpc: Optional[AwsEc2VpcDetailsTypeDef] = None
    AwsEc2Eip: Optional[AwsEc2EipDetailsTypeDef] = None
    AwsEc2Subnet: Optional[AwsEc2SubnetDetailsTypeDef] = None
    AwsEc2NetworkAcl: Optional[AwsEc2NetworkAclDetailsTypeDef] = None
    AwsElbv2LoadBalancer: Optional[AwsElbv2LoadBalancerDetailsTypeDef] = None
    AwsElasticBeanstalkEnvironment: Optional[AwsElasticBeanstalkEnvironmentDetailsTypeDef] = None
    AwsElasticsearchDomain: Optional[AwsElasticsearchDomainDetailsTypeDef] = None
    AwsS3Bucket: Optional[AwsS3BucketDetailsTypeDef] = None
    AwsS3AccountPublicAccessBlock: Optional[AwsS3AccountPublicAccessBlockDetailsTypeDef] = None
    AwsS3Object: Optional[AwsS3ObjectDetailsTypeDef] = None
    AwsSecretsManagerSecret: Optional[AwsSecretsManagerSecretDetailsTypeDef] = None
    AwsIamAccessKey: Optional[AwsIamAccessKeyDetailsTypeDef] = None
    AwsIamUser: Optional[AwsIamUserDetailsTypeDef] = None
    AwsIamPolicy: Optional[AwsIamPolicyDetailsTypeDef] = None
    AwsApiGatewayV2Stage: Optional[AwsApiGatewayV2StageDetailsTypeDef] = None
    AwsApiGatewayV2Api: Optional[AwsApiGatewayV2ApiDetailsTypeDef] = None
    AwsDynamoDbTable: Optional[AwsDynamoDbTableDetailsTypeDef] = None
    AwsApiGatewayStage: Optional[AwsApiGatewayStageDetailsTypeDef] = None
    AwsApiGatewayRestApi: Optional[AwsApiGatewayRestApiDetailsTypeDef] = None
    AwsCloudTrailTrail: Optional[AwsCloudTrailTrailDetailsTypeDef] = None
    AwsSsmPatchCompliance: Optional[AwsSsmPatchComplianceDetailsTypeDef] = None
    AwsCertificateManagerCertificate: Optional[       AwsCertificateManagerCertificateDetailsTypeDef     ] = None
    AwsRedshiftCluster: Optional[AwsRedshiftClusterDetailsTypeDef] = None
    AwsElbLoadBalancer: Optional[AwsElbLoadBalancerDetailsTypeDef] = None
    AwsIamGroup: Optional[AwsIamGroupDetailsTypeDef] = None
    AwsIamRole: Optional[AwsIamRoleDetailsTypeDef] = None
    AwsKmsKey: Optional[AwsKmsKeyDetailsTypeDef] = None
    AwsLambdaFunction: Optional[AwsLambdaFunctionDetailsTypeDef] = None
    AwsLambdaLayerVersion: Optional[AwsLambdaLayerVersionDetailsTypeDef] = None
    AwsRdsDbInstance: Optional[AwsRdsDbInstanceDetailsTypeDef] = None
    AwsSnsTopic: Optional[AwsSnsTopicDetailsTypeDef] = None
    AwsSqsQueue: Optional[AwsSqsQueueDetailsTypeDef] = None
    AwsWafWebAcl: Optional[AwsWafWebAclDetailsTypeDef] = None
    AwsRdsDbSnapshot: Optional[AwsRdsDbSnapshotDetailsTypeDef] = None
    AwsRdsDbClusterSnapshot: Optional[AwsRdsDbClusterSnapshotDetailsTypeDef] = None
    AwsRdsDbCluster: Optional[AwsRdsDbClusterDetailsTypeDef] = None
    AwsEcsCluster: Optional[AwsEcsClusterDetailsTypeDef] = None
    AwsEcsContainer: Optional[AwsEcsContainerDetailsTypeDef] = None
    AwsEcsTaskDefinition: Optional[AwsEcsTaskDefinitionDetailsTypeDef] = None
    Container: Optional[ContainerDetailsTypeDef] = None
    Other: Optional[Mapping[str, str]] = None
    AwsRdsEventSubscription: Optional[AwsRdsEventSubscriptionDetailsTypeDef] = None
    AwsEcsService: Optional[AwsEcsServiceDetailsTypeDef] = None
    AwsAutoScalingLaunchConfiguration: Optional[       AwsAutoScalingLaunchConfigurationDetailsTypeDef     ] = None
    AwsEc2VpnConnection: Optional[AwsEc2VpnConnectionDetailsTypeDef] = None
    AwsEcrContainerImage: Optional[AwsEcrContainerImageDetailsTypeDef] = None
    AwsOpenSearchServiceDomain: Optional[AwsOpenSearchServiceDomainDetailsTypeDef] = None
    AwsEc2VpcEndpointService: Optional[AwsEc2VpcEndpointServiceDetailsTypeDef] = None
    AwsXrayEncryptionConfig: Optional[AwsXrayEncryptionConfigDetailsTypeDef] = None
    AwsWafRateBasedRule: Optional[AwsWafRateBasedRuleDetailsTypeDef] = None
    AwsWafRegionalRateBasedRule: Optional[AwsWafRegionalRateBasedRuleDetailsTypeDef] = None
    AwsEcrRepository: Optional[AwsEcrRepositoryDetailsTypeDef] = None
    AwsEksCluster: Optional[AwsEksClusterDetailsTypeDef] = None
    AwsNetworkFirewallFirewallPolicy: Optional[       AwsNetworkFirewallFirewallPolicyDetailsTypeDef     ] = None
    AwsNetworkFirewallFirewall: Optional[AwsNetworkFirewallFirewallDetailsTypeDef] = None
    AwsNetworkFirewallRuleGroup: Optional[AwsNetworkFirewallRuleGroupDetailsTypeDef] = None
    AwsRdsDbSecurityGroup: Optional[AwsRdsDbSecurityGroupDetailsTypeDef] = None
    AwsKinesisStream: Optional[AwsKinesisStreamDetailsTypeDef] = None
    AwsEc2TransitGateway: Optional[AwsEc2TransitGatewayDetailsTypeDef] = None
    AwsEfsAccessPoint: Optional[AwsEfsAccessPointDetailsTypeDef] = None
    AwsCloudFormationStack: Optional[AwsCloudFormationStackDetailsTypeDef] = None
    AwsCloudWatchAlarm: Optional[AwsCloudWatchAlarmDetailsTypeDef] = None
    AwsEc2VpcPeeringConnection: Optional[AwsEc2VpcPeeringConnectionDetailsTypeDef] = None
    AwsWafRegionalRuleGroup: Optional[AwsWafRegionalRuleGroupDetailsTypeDef] = None
    AwsWafRegionalRule: Optional[AwsWafRegionalRuleDetailsTypeDef] = None
    AwsWafRegionalWebAcl: Optional[AwsWafRegionalWebAclDetailsTypeDef] = None
    AwsWafRule: Optional[AwsWafRuleDetailsTypeDef] = None
    AwsWafRuleGroup: Optional[AwsWafRuleGroupDetailsTypeDef] = None
    AwsEcsTask: Optional[AwsEcsTaskDetailsTypeDef] = None
    AwsBackupBackupVault: Optional[AwsBackupBackupVaultDetailsTypeDef] = None
    AwsBackupBackupPlan: Optional[AwsBackupBackupPlanDetailsTypeDef] = None
    AwsBackupRecoveryPoint: Optional[AwsBackupRecoveryPointDetailsTypeDef] = None
    AwsEc2LaunchTemplate: Optional[AwsEc2LaunchTemplateDetailsTypeDef] = None
    AwsSageMakerNotebookInstance: Optional[AwsSageMakerNotebookInstanceDetailsTypeDef] = None
    AwsWafv2WebAcl: Optional[AwsWafv2WebAclDetailsTypeDef] = None
    AwsWafv2RuleGroup: Optional[AwsWafv2RuleGroupDetailsTypeDef] = None
    AwsEc2RouteTable: Optional[AwsEc2RouteTableDetailsTypeDef] = None
    AwsAmazonMqBroker: Optional[AwsAmazonMqBrokerDetailsTypeDef] = None
    AwsAppSyncGraphQlApi: Optional[AwsAppSyncGraphQlApiDetailsTypeDef] = None
    AwsEventSchemasRegistry: Optional[AwsEventSchemasRegistryDetailsTypeDef] = None
    AwsGuardDutyDetector: Optional[AwsGuardDutyDetectorDetailsTypeDef] = None
    AwsStepFunctionStateMachine: Optional[AwsStepFunctionStateMachineDetailsTypeDef] = None
    AwsAthenaWorkGroup: Optional[AwsAthenaWorkGroupDetailsTypeDef] = None
    AwsEventsEventbus: Optional[AwsEventsEventbusDetailsTypeDef] = None
    AwsDmsEndpoint: Optional[AwsDmsEndpointDetailsTypeDef] = None
    AwsEventsEndpoint: Optional[AwsEventsEndpointDetailsTypeDef] = None
    AwsDmsReplicationTask: Optional[AwsDmsReplicationTaskDetailsTypeDef] = None
    AwsDmsReplicationInstance: Optional[AwsDmsReplicationInstanceDetailsTypeDef] = None
    AwsRoute53HostedZone: Optional[AwsRoute53HostedZoneDetailsTypeDef] = None
    AwsMskCluster: Optional[AwsMskClusterDetailsTypeDef] = None
    AwsS3AccessPoint: Optional[AwsS3AccessPointDetailsTypeDef] = None
    AwsEc2ClientVpnEndpoint: Optional[AwsEc2ClientVpnEndpointDetailsTypeDef] = None

class ResourceExtraOutputTypeDef(BaseValidatorModel):
    Type: str
    Id: str
    Partition: Optional[PartitionType] = None
    Region: Optional[str] = None
    ResourceRole: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DataClassification: Optional[DataClassificationDetailsExtraOutputTypeDef] = None
    Details: Optional[ResourceDetailsExtraOutputTypeDef] = None
    ApplicationName: Optional[str] = None
    ApplicationArn: Optional[str] = None

class ResourceOutputTypeDef(BaseValidatorModel):
    Type: str
    Id: str
    Partition: Optional[PartitionType] = None
    Region: Optional[str] = None
    ResourceRole: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    DataClassification: Optional[DataClassificationDetailsOutputTypeDef] = None
    Details: Optional[ResourceDetailsOutputTypeDef] = None
    ApplicationName: Optional[str] = None
    ApplicationArn: Optional[str] = None

class ResourceTypeDef(BaseValidatorModel):
    Type: str
    Id: str
    Partition: Optional[PartitionType] = None
    Region: Optional[str] = None
    ResourceRole: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    DataClassification: Optional[DataClassificationDetailsTypeDef] = None
    Details: Optional[ResourceDetailsTypeDef] = None
    ApplicationName: Optional[str] = None
    ApplicationArn: Optional[str] = None

class AwsSecurityFindingExtraOutputTypeDef(BaseValidatorModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List[ResourceExtraOutputTypeDef]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[List[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[SeverityTypeDef] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[RemediationTypeDef] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Dict[str, str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Malware: Optional[List[MalwareTypeDef]] = None
    Network: Optional[NetworkTypeDef] = None
    NetworkPath: Optional[List[NetworkPathComponentExtraOutputTypeDef]] = None
    Process: Optional[ProcessDetailsTypeDef] = None
    Threats: Optional[List[ThreatExtraOutputTypeDef]] = None
    ThreatIntelIndicators: Optional[List[ThreatIntelIndicatorTypeDef]] = None
    Compliance: Optional[ComplianceExtraOutputTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[WorkflowTypeDef] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None
    Note: Optional[NoteTypeDef] = None
    Vulnerabilities: Optional[List[VulnerabilityExtraOutputTypeDef]] = None
    PatchSummary: Optional[PatchSummaryTypeDef] = None
    Action: Optional[ActionExtraOutputTypeDef] = None
    FindingProviderFields: Optional[FindingProviderFieldsExtraOutputTypeDef] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsExtraOutputTypeDef] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None

class AwsSecurityFindingOutputTypeDef(BaseValidatorModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List[ResourceOutputTypeDef]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[List[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[SeverityTypeDef] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[RemediationTypeDef] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Dict[str, str]] = None
    UserDefinedFields: Optional[Dict[str, str]] = None
    Malware: Optional[List[MalwareTypeDef]] = None
    Network: Optional[NetworkTypeDef] = None
    NetworkPath: Optional[List[NetworkPathComponentOutputTypeDef]] = None
    Process: Optional[ProcessDetailsTypeDef] = None
    Threats: Optional[List[ThreatOutputTypeDef]] = None
    ThreatIntelIndicators: Optional[List[ThreatIntelIndicatorTypeDef]] = None
    Compliance: Optional[ComplianceOutputTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[WorkflowTypeDef] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[List[RelatedFindingTypeDef]] = None
    Note: Optional[NoteTypeDef] = None
    Vulnerabilities: Optional[List[VulnerabilityOutputTypeDef]] = None
    PatchSummary: Optional[PatchSummaryTypeDef] = None
    Action: Optional[ActionOutputTypeDef] = None
    FindingProviderFields: Optional[FindingProviderFieldsOutputTypeDef] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsOutputTypeDef] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None

class AwsSecurityFindingTypeDef(BaseValidatorModel):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: Sequence[ResourceTypeDef]
    ProductName: Optional[str] = None
    CompanyName: Optional[str] = None
    Region: Optional[str] = None
    Types: Optional[Sequence[str]] = None
    FirstObservedAt: Optional[str] = None
    LastObservedAt: Optional[str] = None
    Severity: Optional[SeverityTypeDef] = None
    Confidence: Optional[int] = None
    Criticality: Optional[int] = None
    Remediation: Optional[RemediationTypeDef] = None
    SourceUrl: Optional[str] = None
    ProductFields: Optional[Mapping[str, str]] = None
    UserDefinedFields: Optional[Mapping[str, str]] = None
    Malware: Optional[Sequence[MalwareTypeDef]] = None
    Network: Optional[NetworkTypeDef] = None
    NetworkPath: Optional[Sequence[NetworkPathComponentTypeDef]] = None
    Process: Optional[ProcessDetailsTypeDef] = None
    Threats: Optional[Sequence[ThreatTypeDef]] = None
    ThreatIntelIndicators: Optional[Sequence[ThreatIntelIndicatorTypeDef]] = None
    Compliance: Optional[ComplianceTypeDef] = None
    VerificationState: Optional[VerificationStateType] = None
    WorkflowState: Optional[WorkflowStateType] = None
    Workflow: Optional[WorkflowTypeDef] = None
    RecordState: Optional[RecordStateType] = None
    RelatedFindings: Optional[Sequence[RelatedFindingTypeDef]] = None
    Note: Optional[NoteTypeDef] = None
    Vulnerabilities: Optional[Sequence[VulnerabilityTypeDef]] = None
    PatchSummary: Optional[PatchSummaryTypeDef] = None
    Action: Optional[ActionTypeDef] = None
    FindingProviderFields: Optional[FindingProviderFieldsTypeDef] = None
    Sample: Optional[bool] = None
    GeneratorDetails: Optional[GeneratorDetailsTypeDef] = None
    ProcessedAt: Optional[str] = None
    AwsAccountName: Optional[str] = None

class GetFindingsResponseTypeDef(BaseValidatorModel):
    Findings: List[AwsSecurityFindingOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchImportFindingsRequestRequestTypeDef(BaseValidatorModel):
    Findings: Sequence[AwsSecurityFindingUnionTypeDef]


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
from aws_resource_validator.pydantic_models.appstream_constants import *

class AccessEndpointTypeDef(BaseValidatorModel):
    EndpointType: Literal["STREAMING"]
    VpceId: Optional[str] = None

class AppBlockBuilderAppBlockAssociationTypeDef(BaseValidatorModel):
    AppBlockArn: str
    AppBlockBuilderName: str

class AppBlockBuilderStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[Literal["INTERNAL_ERROR"]] = None
    Message: Optional[str] = None

class ResourceErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[FleetErrorCodeType] = None
    ErrorMessage: Optional[str] = None
    ErrorTimestamp: Optional[datetime] = None

class VpcConfigTypeDef(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class ErrorDetailsTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class S3LocationTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3Key: Optional[str] = None

class ApplicationFleetAssociationTypeDef(BaseValidatorModel):
    FleetName: str
    ApplicationArn: str

class ApplicationSettingsResponseTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SettingsGroup: Optional[str] = None
    S3BucketName: Optional[str] = None

class ApplicationSettingsTypeDef(BaseValidatorModel):
    Enabled: bool
    SettingsGroup: Optional[str] = None

class AssociateAppBlockBuilderAppBlockRequestRequestTypeDef(BaseValidatorModel):
    AppBlockArn: str
    AppBlockBuilderName: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateApplicationFleetRequestRequestTypeDef(BaseValidatorModel):
    FleetName: str
    ApplicationArn: str

class AssociateApplicationToEntitlementRequestRequestTypeDef(BaseValidatorModel):
    StackName: str
    EntitlementName: str
    ApplicationIdentifier: str

class AssociateFleetRequestRequestTypeDef(BaseValidatorModel):
    FleetName: str
    StackName: str

class UserStackAssociationTypeDef(BaseValidatorModel):
    StackName: str
    UserName: str
    AuthenticationType: AuthenticationTypeType
    SendEmailNotification: Optional[bool] = None

class CertificateBasedAuthPropertiesTypeDef(BaseValidatorModel):
    Status: Optional[CertificateBasedAuthStatusType] = None
    CertificateAuthorityArn: Optional[str] = None

class ComputeCapacityStatusTypeDef(BaseValidatorModel):
    Desired: int
    Running: Optional[int] = None
    InUse: Optional[int] = None
    Available: Optional[int] = None
    DesiredUserSessions: Optional[int] = None
    AvailableUserSessions: Optional[int] = None
    ActiveUserSessions: Optional[int] = None
    ActualUserSessions: Optional[int] = None

class ComputeCapacityTypeDef(BaseValidatorModel):
    DesiredInstances: Optional[int] = None
    DesiredSessions: Optional[int] = None

class CopyImageRequestRequestTypeDef(BaseValidatorModel):
    SourceImageName: str
    DestinationImageName: str
    DestinationRegion: str
    DestinationImageDescription: Optional[str] = None

class CreateAppBlockBuilderStreamingURLRequestRequestTypeDef(BaseValidatorModel):
    AppBlockBuilderName: str
    Validity: Optional[int] = None

class ServiceAccountCredentialsTypeDef(BaseValidatorModel):
    AccountName: str
    AccountPassword: str

class EntitlementAttributeTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class DomainJoinInfoTypeDef(BaseValidatorModel):
    DirectoryName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None

class CreateImageBuilderStreamingURLRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Validity: Optional[int] = None

class StorageConnectorTypeDef(BaseValidatorModel):
    ConnectorType: StorageConnectorTypeType
    ResourceIdentifier: Optional[str] = None
    Domains: Optional[Sequence[str]] = None

class StreamingExperienceSettingsTypeDef(BaseValidatorModel):
    PreferredProtocol: Optional[PreferredProtocolType] = None

class UserSettingTypeDef(BaseValidatorModel):
    Action: ActionType
    Permission: PermissionType
    MaximumLength: Optional[int] = None

class CreateStreamingURLRequestRequestTypeDef(BaseValidatorModel):
    StackName: str
    FleetName: str
    UserId: str
    ApplicationId: Optional[str] = None
    Validity: Optional[int] = None
    SessionContext: Optional[str] = None

class CreateUpdatedImageRequestRequestTypeDef(BaseValidatorModel):
    existingImageName: str
    newImageName: str
    newImageDescription: Optional[str] = None
    newImageDisplayName: Optional[str] = None
    newImageTags: Optional[Mapping[str, str]] = None
    dryRun: Optional[bool] = None

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType
    MessageAction: Optional[MessageActionType] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

class DeleteAppBlockBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteAppBlockRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteDirectoryConfigRequestRequestTypeDef(BaseValidatorModel):
    DirectoryName: str

class DeleteEntitlementRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    StackName: str

class DeleteFleetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteImageBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteImagePermissionsRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    SharedAccountId: str

class DeleteImageRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteStackRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class DescribeAppBlockBuilderAppBlockAssociationsRequestRequestTypeDef(BaseValidatorModel):
    AppBlockArn: Optional[str] = None
    AppBlockBuilderName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeAppBlockBuildersRequestRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeAppBlocksRequestRequestTypeDef(BaseValidatorModel):
    Arns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeApplicationFleetAssociationsRequestRequestTypeDef(BaseValidatorModel):
    FleetName: Optional[str] = None
    ApplicationArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeApplicationsRequestRequestTypeDef(BaseValidatorModel):
    Arns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDirectoryConfigsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeEntitlementsRequestRequestTypeDef(BaseValidatorModel):
    StackName: str
    Name: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeFleetsRequestRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeImageBuildersRequestRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImagePermissionsRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    SharedAwsAccountIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeImagesRequestRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Arns: Optional[Sequence[str]] = None
    Type: Optional[VisibilityTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSessionsRequestRequestTypeDef(BaseValidatorModel):
    StackName: str
    FleetName: str
    UserId: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    InstanceId: Optional[str] = None

class DescribeStacksRequestRequestTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeUsageReportSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeUserStackAssociationsRequestRequestTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    UserName: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeUsersRequestRequestTypeDef(BaseValidatorModel):
    AuthenticationType: AuthenticationTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UserTypeDef(BaseValidatorModel):
    AuthenticationType: AuthenticationTypeType
    Arn: Optional[str] = None
    UserName: Optional[str] = None
    Enabled: Optional[bool] = None
    Status: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    CreatedTime: Optional[datetime] = None

class DisableUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class DisassociateAppBlockBuilderAppBlockRequestRequestTypeDef(BaseValidatorModel):
    AppBlockArn: str
    AppBlockBuilderName: str

class DisassociateApplicationFleetRequestRequestTypeDef(BaseValidatorModel):
    FleetName: str
    ApplicationArn: str

class DisassociateApplicationFromEntitlementRequestRequestTypeDef(BaseValidatorModel):
    StackName: str
    EntitlementName: str
    ApplicationIdentifier: str

class DisassociateFleetRequestRequestTypeDef(BaseValidatorModel):
    FleetName: str
    StackName: str

class EnableUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class EntitledApplicationTypeDef(BaseValidatorModel):
    ApplicationIdentifier: str

class ExpireSessionRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str

class FleetErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[FleetErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class VpcConfigPaginatorTypeDef(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class ImageBuilderStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[ImageBuilderStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class NetworkAccessConfigurationTypeDef(BaseValidatorModel):
    EniPrivateIpAddress: Optional[str] = None
    EniId: Optional[str] = None

class ImagePermissionsTypeDef(BaseValidatorModel):
    allowFleet: Optional[bool] = None
    allowImageBuilder: Optional[bool] = None

class ImageStateChangeReasonTypeDef(BaseValidatorModel):
    Code: Optional[ImageStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class LastReportGenerationExecutionErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[UsageReportExecutionErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class ListAssociatedFleetsRequestRequestTypeDef(BaseValidatorModel):
    StackName: str
    NextToken: Optional[str] = None

class ListAssociatedStacksRequestRequestTypeDef(BaseValidatorModel):
    FleetName: str
    NextToken: Optional[str] = None

class ListEntitledApplicationsRequestRequestTypeDef(BaseValidatorModel):
    StackName: str
    EntitlementName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class StackErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[StackErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class StorageConnectorPaginatorTypeDef(BaseValidatorModel):
    ConnectorType: StorageConnectorTypeType
    ResourceIdentifier: Optional[str] = None
    Domains: Optional[List[str]] = None

class StartAppBlockBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StartFleetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StartImageBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    AppstreamAgentVersion: Optional[str] = None

class StopAppBlockBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StopFleetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StopImageBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AppBlockBuilderTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    Platform: Literal["WINDOWS_SERVER_2019"]
    InstanceType: str
    VpcConfig: VpcConfigTypeDef
    State: AppBlockBuilderStateType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    IamRoleArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    AppBlockBuilderErrors: Optional[List[ResourceErrorTypeDef]] = None
    StateChangeReason: Optional[AppBlockBuilderStateChangeReasonTypeDef] = None
    AccessEndpoints: Optional[List[AccessEndpointTypeDef]] = None

class CreateAppBlockBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Platform: Literal["WINDOWS_SERVER_2019"]
    InstanceType: str
    VpcConfig: VpcConfigTypeDef
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    IamRoleArn: Optional[str] = None
    AccessEndpoints: Optional[Sequence[AccessEndpointTypeDef]] = None

class UpdateAppBlockBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Platform: Optional[PlatformTypeType] = None
    InstanceType: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    IamRoleArn: Optional[str] = None
    AccessEndpoints: Optional[Sequence[AccessEndpointTypeDef]] = None
    AttributesToDelete: Optional[Sequence[AppBlockBuilderAttributeType]] = None

class ApplicationTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DisplayName: Optional[str] = None
    IconURL: Optional[str] = None
    LaunchPath: Optional[str] = None
    LaunchParameters: Optional[str] = None
    Enabled: Optional[bool] = None
    Metadata: Optional[Dict[str, str]] = None
    WorkingDirectory: Optional[str] = None
    Description: Optional[str] = None
    Arn: Optional[str] = None
    AppBlockArn: Optional[str] = None
    IconS3Location: Optional[S3LocationTypeDef] = None
    Platforms: Optional[List[PlatformTypeType]] = None
    InstanceFamilies: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    IconS3Location: S3LocationTypeDef
    LaunchPath: str
    Platforms: Sequence[PlatformTypeType]
    InstanceFamilies: Sequence[str]
    AppBlockArn: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    WorkingDirectory: Optional[str] = None
    LaunchParameters: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ScriptDetailsTypeDef(BaseValidatorModel):
    ScriptS3Location: S3LocationTypeDef
    ExecutablePath: str
    TimeoutInSeconds: int
    ExecutableParameters: Optional[str] = None

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    IconS3Location: Optional[S3LocationTypeDef] = None
    LaunchPath: Optional[str] = None
    WorkingDirectory: Optional[str] = None
    LaunchParameters: Optional[str] = None
    AppBlockArn: Optional[str] = None
    AttributesToDelete: Optional[Sequence[ApplicationAttributeType]] = None

class AssociateAppBlockBuilderAppBlockResultTypeDef(BaseValidatorModel):
    AppBlockBuilderAppBlockAssociation: AppBlockBuilderAppBlockAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateApplicationFleetResultTypeDef(BaseValidatorModel):
    ApplicationFleetAssociation: ApplicationFleetAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyImageResponseTypeDef(BaseValidatorModel):
    DestinationImageName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppBlockBuilderStreamingURLResultTypeDef(BaseValidatorModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageBuilderStreamingURLResultTypeDef(BaseValidatorModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingURLResultTypeDef(BaseValidatorModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageReportSubscriptionResultTypeDef(BaseValidatorModel):
    S3BucketName: str
    Schedule: Literal["DAILY"]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef(BaseValidatorModel):
    AppBlockBuilderAppBlockAssociations: List[AppBlockBuilderAppBlockAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationFleetAssociationsResultTypeDef(BaseValidatorModel):
    ApplicationFleetAssociations: List[ApplicationFleetAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedFleetsResultTypeDef(BaseValidatorModel):
    Names: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedStacksResultTypeDef(BaseValidatorModel):
    Names: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateUserStackRequestRequestTypeDef(BaseValidatorModel):
    UserStackAssociations: Sequence[UserStackAssociationTypeDef]

class BatchDisassociateUserStackRequestRequestTypeDef(BaseValidatorModel):
    UserStackAssociations: Sequence[UserStackAssociationTypeDef]

class DescribeUserStackAssociationsResultTypeDef(BaseValidatorModel):
    UserStackAssociations: List[UserStackAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UserStackAssociationErrorTypeDef(BaseValidatorModel):
    UserStackAssociation: Optional[UserStackAssociationTypeDef] = None
    ErrorCode: Optional[UserStackAssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class CreateDirectoryConfigRequestRequestTypeDef(BaseValidatorModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Sequence[str]
    ServiceAccountCredentials: Optional[ServiceAccountCredentialsTypeDef] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None

class DirectoryConfigTypeDef(BaseValidatorModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Optional[List[str]] = None
    ServiceAccountCredentials: Optional[ServiceAccountCredentialsTypeDef] = None
    CreatedTime: Optional[datetime] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None

class UpdateDirectoryConfigRequestRequestTypeDef(BaseValidatorModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Optional[Sequence[str]] = None
    ServiceAccountCredentials: Optional[ServiceAccountCredentialsTypeDef] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None

class CreateEntitlementRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    StackName: str
    AppVisibility: AppVisibilityType
    Attributes: Sequence[EntitlementAttributeTypeDef]
    Description: Optional[str] = None

class EntitlementTypeDef(BaseValidatorModel):
    Name: str
    StackName: str
    AppVisibility: AppVisibilityType
    Attributes: List[EntitlementAttributeTypeDef]
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class UpdateEntitlementRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    StackName: str
    Description: Optional[str] = None
    AppVisibility: Optional[AppVisibilityType] = None
    Attributes: Optional[Sequence[EntitlementAttributeTypeDef]] = None

class CreateFleetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    InstanceType: str
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    ComputeCapacity: Optional[ComputeCapacityTypeDef] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    MaxUserDurationInSeconds: Optional[int] = None
    DisconnectTimeoutInSeconds: Optional[int] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfoTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    IamRoleArn: Optional[str] = None
    StreamView: Optional[StreamViewType] = None
    Platform: Optional[PlatformTypeType] = None
    MaxConcurrentSessions: Optional[int] = None
    UsbDeviceFilterStrings: Optional[Sequence[str]] = None
    SessionScriptS3Location: Optional[S3LocationTypeDef] = None
    MaxSessionsPerInstance: Optional[int] = None

class CreateImageBuilderRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    InstanceType: str
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    IamRoleArn: Optional[str] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfoTypeDef] = None
    AppstreamAgentVersion: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    AccessEndpoints: Optional[Sequence[AccessEndpointTypeDef]] = None

class UpdateFleetRequestRequestTypeDef(BaseValidatorModel):
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    Name: Optional[str] = None
    InstanceType: Optional[str] = None
    ComputeCapacity: Optional[ComputeCapacityTypeDef] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    MaxUserDurationInSeconds: Optional[int] = None
    DisconnectTimeoutInSeconds: Optional[int] = None
    DeleteVpcConfig: Optional[bool] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfoTypeDef] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    AttributesToDelete: Optional[Sequence[FleetAttributeType]] = None
    IamRoleArn: Optional[str] = None
    StreamView: Optional[StreamViewType] = None
    Platform: Optional[PlatformTypeType] = None
    MaxConcurrentSessions: Optional[int] = None
    UsbDeviceFilterStrings: Optional[Sequence[str]] = None
    SessionScriptS3Location: Optional[S3LocationTypeDef] = None
    MaxSessionsPerInstance: Optional[int] = None

class CreateStackRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    StorageConnectors: Optional[Sequence[StorageConnectorTypeDef]] = None
    RedirectURL: Optional[str] = None
    FeedbackURL: Optional[str] = None
    UserSettings: Optional[Sequence[UserSettingTypeDef]] = None
    ApplicationSettings: Optional[ApplicationSettingsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    AccessEndpoints: Optional[Sequence[AccessEndpointTypeDef]] = None
    EmbedHostDomains: Optional[Sequence[str]] = None
    StreamingExperienceSettings: Optional[StreamingExperienceSettingsTypeDef] = None

class UpdateStackRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    StorageConnectors: Optional[Sequence[StorageConnectorTypeDef]] = None
    DeleteStorageConnectors: Optional[bool] = None
    RedirectURL: Optional[str] = None
    FeedbackURL: Optional[str] = None
    AttributesToDelete: Optional[Sequence[StackAttributeType]] = None
    UserSettings: Optional[Sequence[UserSettingTypeDef]] = None
    ApplicationSettings: Optional[ApplicationSettingsTypeDef] = None
    AccessEndpoints: Optional[Sequence[AccessEndpointTypeDef]] = None
    EmbedHostDomains: Optional[Sequence[str]] = None
    StreamingExperienceSettings: Optional[StreamingExperienceSettingsTypeDef] = None

class DescribeDirectoryConfigsRequestDescribeDirectoryConfigsPaginateTypeDef(BaseValidatorModel):
    DirectoryNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetsRequestDescribeFleetsPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImageBuildersRequestDescribeImageBuildersPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImagesRequestDescribeImagesPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    Arns: Optional[Sequence[str]] = None
    Type: Optional[VisibilityTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSessionsRequestDescribeSessionsPaginateTypeDef(BaseValidatorModel):
    StackName: str
    FleetName: str
    UserId: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    InstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStacksRequestDescribeStacksPaginateTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUserStackAssociationsRequestDescribeUserStackAssociationsPaginateTypeDef(BaseValidatorModel):
    StackName: Optional[str] = None
    UserName: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsersRequestDescribeUsersPaginateTypeDef(BaseValidatorModel):
    AuthenticationType: AuthenticationTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedFleetsRequestListAssociatedFleetsPaginateTypeDef(BaseValidatorModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedStacksRequestListAssociatedStacksPaginateTypeDef(BaseValidatorModel):
    FleetName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetsRequestFleetStartedWaitTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFleetsRequestFleetStoppedWaitTypeDef(BaseValidatorModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeUsersResultTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitledApplicationsResultTypeDef(BaseValidatorModel):
    EntitledApplications: List[EntitledApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FleetTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    InstanceType: str
    ComputeCapacityStatus: ComputeCapacityStatusTypeDef
    State: FleetStateType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    MaxUserDurationInSeconds: Optional[int] = None
    DisconnectTimeoutInSeconds: Optional[int] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    CreatedTime: Optional[datetime] = None
    FleetErrors: Optional[List[FleetErrorTypeDef]] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfoTypeDef] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    IamRoleArn: Optional[str] = None
    StreamView: Optional[StreamViewType] = None
    Platform: Optional[PlatformTypeType] = None
    MaxConcurrentSessions: Optional[int] = None
    UsbDeviceFilterStrings: Optional[List[str]] = None
    SessionScriptS3Location: Optional[S3LocationTypeDef] = None
    MaxSessionsPerInstance: Optional[int] = None

class FleetPaginatorTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    InstanceType: str
    ComputeCapacityStatus: ComputeCapacityStatusTypeDef
    State: FleetStateType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    MaxUserDurationInSeconds: Optional[int] = None
    DisconnectTimeoutInSeconds: Optional[int] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None
    CreatedTime: Optional[datetime] = None
    FleetErrors: Optional[List[FleetErrorTypeDef]] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfoTypeDef] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    IamRoleArn: Optional[str] = None
    StreamView: Optional[StreamViewType] = None
    Platform: Optional[PlatformTypeType] = None
    MaxConcurrentSessions: Optional[int] = None
    UsbDeviceFilterStrings: Optional[List[str]] = None
    SessionScriptS3Location: Optional[S3LocationTypeDef] = None
    MaxSessionsPerInstance: Optional[int] = None

class ImageBuilderPaginatorTypeDef(BaseValidatorModel):
    Name: str
    Arn: Optional[str] = None
    ImageArn: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    VpcConfig: Optional[VpcConfigPaginatorTypeDef] = None
    InstanceType: Optional[str] = None
    Platform: Optional[PlatformTypeType] = None
    IamRoleArn: Optional[str] = None
    State: Optional[ImageBuilderStateType] = None
    StateChangeReason: Optional[ImageBuilderStateChangeReasonTypeDef] = None
    CreatedTime: Optional[datetime] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfoTypeDef] = None
    NetworkAccessConfiguration: Optional[NetworkAccessConfigurationTypeDef] = None
    ImageBuilderErrors: Optional[List[ResourceErrorTypeDef]] = None
    AppstreamAgentVersion: Optional[str] = None
    AccessEndpoints: Optional[List[AccessEndpointTypeDef]] = None

class ImageBuilderTypeDef(BaseValidatorModel):
    Name: str
    Arn: Optional[str] = None
    ImageArn: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    VpcConfig: Optional[VpcConfigTypeDef] = None
    InstanceType: Optional[str] = None
    Platform: Optional[PlatformTypeType] = None
    IamRoleArn: Optional[str] = None
    State: Optional[ImageBuilderStateType] = None
    StateChangeReason: Optional[ImageBuilderStateChangeReasonTypeDef] = None
    CreatedTime: Optional[datetime] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfoTypeDef] = None
    NetworkAccessConfiguration: Optional[NetworkAccessConfigurationTypeDef] = None
    ImageBuilderErrors: Optional[List[ResourceErrorTypeDef]] = None
    AppstreamAgentVersion: Optional[str] = None
    AccessEndpoints: Optional[List[AccessEndpointTypeDef]] = None

class SessionTypeDef(BaseValidatorModel):
    Id: str
    UserId: str
    StackName: str
    FleetName: str
    State: SessionStateType
    ConnectionState: Optional[SessionConnectionStateType] = None
    StartTime: Optional[datetime] = None
    MaxExpirationTime: Optional[datetime] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    NetworkAccessConfiguration: Optional[NetworkAccessConfigurationTypeDef] = None
    InstanceId: Optional[str] = None

class SharedImagePermissionsTypeDef(BaseValidatorModel):
    sharedAccountId: str
    imagePermissions: ImagePermissionsTypeDef

class UpdateImagePermissionsRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    SharedAccountId: str
    ImagePermissions: ImagePermissionsTypeDef

class UsageReportSubscriptionTypeDef(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    Schedule: Optional[Literal["DAILY"]] = None
    LastGeneratedReportDate: Optional[datetime] = None
    SubscriptionErrors: Optional[List[LastReportGenerationExecutionErrorTypeDef]] = None

class StackTypeDef(BaseValidatorModel):
    Name: str
    Arn: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    StorageConnectors: Optional[List[StorageConnectorTypeDef]] = None
    RedirectURL: Optional[str] = None
    FeedbackURL: Optional[str] = None
    StackErrors: Optional[List[StackErrorTypeDef]] = None
    UserSettings: Optional[List[UserSettingTypeDef]] = None
    ApplicationSettings: Optional[ApplicationSettingsResponseTypeDef] = None
    AccessEndpoints: Optional[List[AccessEndpointTypeDef]] = None
    EmbedHostDomains: Optional[List[str]] = None
    StreamingExperienceSettings: Optional[StreamingExperienceSettingsTypeDef] = None

class StackPaginatorTypeDef(BaseValidatorModel):
    Name: str
    Arn: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    StorageConnectors: Optional[List[StorageConnectorPaginatorTypeDef]] = None
    RedirectURL: Optional[str] = None
    FeedbackURL: Optional[str] = None
    StackErrors: Optional[List[StackErrorTypeDef]] = None
    UserSettings: Optional[List[UserSettingTypeDef]] = None
    ApplicationSettings: Optional[ApplicationSettingsResponseTypeDef] = None
    AccessEndpoints: Optional[List[AccessEndpointTypeDef]] = None
    EmbedHostDomains: Optional[List[str]] = None
    StreamingExperienceSettings: Optional[StreamingExperienceSettingsTypeDef] = None

class CreateAppBlockBuilderResultTypeDef(BaseValidatorModel):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlockBuildersResultTypeDef(BaseValidatorModel):
    AppBlockBuilders: List[AppBlockBuilderTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAppBlockBuilderResultTypeDef(BaseValidatorModel):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopAppBlockBuilderResultTypeDef(BaseValidatorModel):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppBlockBuilderResultTypeDef(BaseValidatorModel):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResultTypeDef(BaseValidatorModel):
    Application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationsResultTypeDef(BaseValidatorModel):
    Applications: List[ApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImageTypeDef(BaseValidatorModel):
    Name: str
    Arn: Optional[str] = None
    BaseImageArn: Optional[str] = None
    DisplayName: Optional[str] = None
    State: Optional[ImageStateType] = None
    Visibility: Optional[VisibilityTypeType] = None
    ImageBuilderSupported: Optional[bool] = None
    ImageBuilderName: Optional[str] = None
    Platform: Optional[PlatformTypeType] = None
    Description: Optional[str] = None
    StateChangeReason: Optional[ImageStateChangeReasonTypeDef] = None
    Applications: Optional[List[ApplicationTypeDef]] = None
    CreatedTime: Optional[datetime] = None
    PublicBaseImageReleasedDate: Optional[datetime] = None
    AppstreamAgentVersion: Optional[str] = None
    ImagePermissions: Optional[ImagePermissionsTypeDef] = None
    ImageErrors: Optional[List[ResourceErrorTypeDef]] = None

class UpdateApplicationResultTypeDef(BaseValidatorModel):
    Application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AppBlockTypeDef(BaseValidatorModel):
    Name: str
    Arn: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    SourceS3Location: Optional[S3LocationTypeDef] = None
    SetupScriptDetails: Optional[ScriptDetailsTypeDef] = None
    CreatedTime: Optional[datetime] = None
    PostSetupScriptDetails: Optional[ScriptDetailsTypeDef] = None
    PackagingType: Optional[PackagingTypeType] = None
    State: Optional[AppBlockStateType] = None
    AppBlockErrors: Optional[List[ErrorDetailsTypeDef]] = None

class CreateAppBlockRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    SourceS3Location: S3LocationTypeDef
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    SetupScriptDetails: Optional[ScriptDetailsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    PostSetupScriptDetails: Optional[ScriptDetailsTypeDef] = None
    PackagingType: Optional[PackagingTypeType] = None

class BatchAssociateUserStackResultTypeDef(BaseValidatorModel):
    errors: List[UserStackAssociationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateUserStackResultTypeDef(BaseValidatorModel):
    errors: List[UserStackAssociationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryConfigResultTypeDef(BaseValidatorModel):
    DirectoryConfig: DirectoryConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectoryConfigsResultTypeDef(BaseValidatorModel):
    DirectoryConfigs: List[DirectoryConfigTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDirectoryConfigResultTypeDef(BaseValidatorModel):
    DirectoryConfig: DirectoryConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntitlementResultTypeDef(BaseValidatorModel):
    Entitlement: EntitlementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntitlementsResultTypeDef(BaseValidatorModel):
    Entitlements: List[EntitlementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEntitlementResultTypeDef(BaseValidatorModel):
    Entitlement: EntitlementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResultTypeDef(BaseValidatorModel):
    Fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetsResultTypeDef(BaseValidatorModel):
    Fleets: List[FleetTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetResultTypeDef(BaseValidatorModel):
    Fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetsResultPaginatorTypeDef(BaseValidatorModel):
    Fleets: List[FleetPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageBuildersResultPaginatorTypeDef(BaseValidatorModel):
    ImageBuilders: List[ImageBuilderPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageBuilderResultTypeDef(BaseValidatorModel):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageBuilderResultTypeDef(BaseValidatorModel):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageBuildersResultTypeDef(BaseValidatorModel):
    ImageBuilders: List[ImageBuilderTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImageBuilderResultTypeDef(BaseValidatorModel):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopImageBuilderResultTypeDef(BaseValidatorModel):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSessionsResultTypeDef(BaseValidatorModel):
    Sessions: List[SessionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImagePermissionsResultTypeDef(BaseValidatorModel):
    Name: str
    SharedImagePermissionsList: List[SharedImagePermissionsTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsageReportSubscriptionsResultTypeDef(BaseValidatorModel):
    UsageReportSubscriptions: List[UsageReportSubscriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackResultTypeDef(BaseValidatorModel):
    Stack: StackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStacksResultTypeDef(BaseValidatorModel):
    Stacks: List[StackTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackResultTypeDef(BaseValidatorModel):
    Stack: StackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStacksResultPaginatorTypeDef(BaseValidatorModel):
    Stacks: List[StackPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUpdatedImageResultTypeDef(BaseValidatorModel):
    image: ImageTypeDef
    canUpdateImage: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageResultTypeDef(BaseValidatorModel):
    Image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImagesResultTypeDef(BaseValidatorModel):
    Images: List[ImageTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppBlockResultTypeDef(BaseValidatorModel):
    AppBlock: AppBlockTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlocksResultTypeDef(BaseValidatorModel):
    AppBlocks: List[AppBlockTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


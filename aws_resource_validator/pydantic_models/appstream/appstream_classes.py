from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.appstream.appstream_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessEndpoint(BaseValidatorModel):
    EndpointType: Literal['STREAMING']
    VpceId: Optional[str] = None


class AppBlockBuilderAppBlockAssociation(BaseValidatorModel):
    AppBlockArn: str
    AppBlockBuilderName: str


class AppBlockBuilderStateChangeReason(BaseValidatorModel):
    Code: Optional[Literal['INTERNAL_ERROR']] = None
    Message: Optional[str] = None


class ResourceError(BaseValidatorModel):
    ErrorCode: Optional[FleetErrorCodeType] = None
    ErrorMessage: Optional[str] = None
    ErrorTimestamp: Optional[datetime] = None


class VpcConfigOutput(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class ErrorDetails(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class S3Location(BaseValidatorModel):
    S3Bucket: str
    S3Key: Optional[str] = None


class ApplicationFleetAssociation(BaseValidatorModel):
    FleetName: str
    ApplicationArn: str


class ApplicationSettingsResponse(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SettingsGroup: Optional[str] = None
    S3BucketName: Optional[str] = None


class ApplicationSettings(BaseValidatorModel):
    Enabled: bool
    SettingsGroup: Optional[str] = None


# This class is the input for the 'associate_app_block_builder_app_block' function.
class AssociateAppBlockBuilderAppBlockRequest(BaseValidatorModel):
    AppBlockArn: str
    AppBlockBuilderName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'associate_application_fleet' function.
class AssociateApplicationFleetRequest(BaseValidatorModel):
    FleetName: str
    ApplicationArn: str


class AssociateApplicationToEntitlementRequest(BaseValidatorModel):
    StackName: str
    EntitlementName: str
    ApplicationIdentifier: str


class AssociateFleetRequest(BaseValidatorModel):
    FleetName: str
    StackName: str


class UserStackAssociation(BaseValidatorModel):
    StackName: str
    UserName: str
    AuthenticationType: AuthenticationTypeType
    SendEmailNotification: Optional[bool] = None


class CertificateBasedAuthProperties(BaseValidatorModel):
    Status: Optional[CertificateBasedAuthStatusType] = None
    CertificateAuthorityArn: Optional[str] = None


class ComputeCapacityStatus(BaseValidatorModel):
    Desired: int
    Running: Optional[int] = None
    InUse: Optional[int] = None
    Available: Optional[int] = None
    DesiredUserSessions: Optional[int] = None
    AvailableUserSessions: Optional[int] = None
    ActiveUserSessions: Optional[int] = None
    ActualUserSessions: Optional[int] = None


class ComputeCapacity(BaseValidatorModel):
    DesiredInstances: Optional[int] = None
    DesiredSessions: Optional[int] = None


# This class is the input for the 'copy_image' function.
class CopyImageRequest(BaseValidatorModel):
    SourceImageName: str
    DestinationImageName: str
    DestinationRegion: str
    DestinationImageDescription: Optional[str] = None


# This class is the input for the 'create_app_block_builder_streaming_url' function.
class CreateAppBlockBuilderStreamingURLRequest(BaseValidatorModel):
    AppBlockBuilderName: str
    Validity: Optional[int] = None


class ServiceAccountCredentials(BaseValidatorModel):
    AccountName: str
    AccountPassword: str


class EntitlementAttribute(BaseValidatorModel):
    Name: str
    Value: str


class DomainJoinInfo(BaseValidatorModel):
    DirectoryName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None


# This class is the input for the 'create_image_builder_streaming_url' function.
class CreateImageBuilderStreamingURLRequest(BaseValidatorModel):
    Name: str
    Validity: Optional[int] = None


class StreamingExperienceSettings(BaseValidatorModel):
    PreferredProtocol: Optional[PreferredProtocolType] = None


class UserSetting(BaseValidatorModel):
    Action: ActionType
    Permission: PermissionType
    MaximumLength: Optional[int] = None


# This class is the input for the 'create_streaming_url' function.
class CreateStreamingURLRequest(BaseValidatorModel):
    StackName: str
    FleetName: str
    UserId: str
    ApplicationId: Optional[str] = None
    Validity: Optional[int] = None
    SessionContext: Optional[str] = None


class ThemeFooterLink(BaseValidatorModel):
    DisplayName: Optional[str] = None
    FooterLinkURL: Optional[str] = None


# This class is the input for the 'create_updated_image' function.
class CreateUpdatedImageRequest(BaseValidatorModel):
    existingImageName: str
    newImageName: str
    newImageDescription: Optional[str] = None
    newImageDisplayName: Optional[str] = None
    newImageTags: Optional[Dict[str, str]] = None
    dryRun: Optional[bool] = None


class CreateUserRequest(BaseValidatorModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType
    MessageAction: Optional[MessageActionType] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None


class DeleteAppBlockBuilderRequest(BaseValidatorModel):
    Name: str


class DeleteAppBlockRequest(BaseValidatorModel):
    Name: str


class DeleteApplicationRequest(BaseValidatorModel):
    Name: str


class DeleteDirectoryConfigRequest(BaseValidatorModel):
    DirectoryName: str


class DeleteEntitlementRequest(BaseValidatorModel):
    Name: str
    StackName: str


class DeleteFleetRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'delete_image_builder' function.
class DeleteImageBuilderRequest(BaseValidatorModel):
    Name: str


class DeleteImagePermissionsRequest(BaseValidatorModel):
    Name: str
    SharedAccountId: str


# This class is the input for the 'delete_image' function.
class DeleteImageRequest(BaseValidatorModel):
    Name: str


class DeleteStackRequest(BaseValidatorModel):
    Name: str


class DeleteThemeForStackRequest(BaseValidatorModel):
    StackName: str


class DeleteUserRequest(BaseValidatorModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType


# This class is the input for the 'describe_app_block_builder_app_block_associations' function.
class DescribeAppBlockBuilderAppBlockAssociationsRequest(BaseValidatorModel):
    AppBlockArn: Optional[str] = None
    AppBlockBuilderName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_app_block_builders' function.
class DescribeAppBlockBuildersRequest(BaseValidatorModel):
    Names: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_app_blocks' function.
class DescribeAppBlocksRequest(BaseValidatorModel):
    Arns: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_application_fleet_associations' function.
class DescribeApplicationFleetAssociationsRequest(BaseValidatorModel):
    FleetName: Optional[str] = None
    ApplicationArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_applications' function.
class DescribeApplicationsRequest(BaseValidatorModel):
    Arns: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_directory_configs' function.
class DescribeDirectoryConfigsRequest(BaseValidatorModel):
    DirectoryNames: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_entitlements' function.
class DescribeEntitlementsRequest(BaseValidatorModel):
    StackName: str
    Name: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_fleets' function.
class DescribeFleetsRequest(BaseValidatorModel):
    Names: Optional[List[str]] = None
    NextToken: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_image_builders' function.
class DescribeImageBuildersRequest(BaseValidatorModel):
    Names: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_image_permissions' function.
class DescribeImagePermissionsRequest(BaseValidatorModel):
    Name: str
    MaxResults: Optional[int] = None
    SharedAwsAccountIds: Optional[List[str]] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_images' function.
class DescribeImagesRequest(BaseValidatorModel):
    Names: Optional[List[str]] = None
    Arns: Optional[List[str]] = None
    Type: Optional[VisibilityTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_sessions' function.
class DescribeSessionsRequest(BaseValidatorModel):
    StackName: str
    FleetName: str
    UserId: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    InstanceId: Optional[str] = None


# This class is the input for the 'describe_stacks' function.
class DescribeStacksRequest(BaseValidatorModel):
    Names: Optional[List[str]] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_theme_for_stack' function.
class DescribeThemeForStackRequest(BaseValidatorModel):
    StackName: str


# This class is the input for the 'describe_usage_report_subscriptions' function.
class DescribeUsageReportSubscriptionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_user_stack_associations' function.
class DescribeUserStackAssociationsRequest(BaseValidatorModel):
    StackName: Optional[str] = None
    UserName: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_users' function.
class DescribeUsersRequest(BaseValidatorModel):
    AuthenticationType: AuthenticationTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class User(BaseValidatorModel):
    AuthenticationType: AuthenticationTypeType
    Arn: Optional[str] = None
    UserName: Optional[str] = None
    Enabled: Optional[bool] = None
    Status: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    CreatedTime: Optional[datetime] = None


class DisableUserRequest(BaseValidatorModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType


class DisassociateAppBlockBuilderAppBlockRequest(BaseValidatorModel):
    AppBlockArn: str
    AppBlockBuilderName: str


class DisassociateApplicationFleetRequest(BaseValidatorModel):
    FleetName: str
    ApplicationArn: str


class DisassociateApplicationFromEntitlementRequest(BaseValidatorModel):
    StackName: str
    EntitlementName: str
    ApplicationIdentifier: str


class DisassociateFleetRequest(BaseValidatorModel):
    FleetName: str
    StackName: str


class EnableUserRequest(BaseValidatorModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType


class EntitledApplication(BaseValidatorModel):
    ApplicationIdentifier: str


class ExpireSessionRequest(BaseValidatorModel):
    SessionId: str


class FleetError(BaseValidatorModel):
    ErrorCode: Optional[FleetErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ImageBuilderStateChangeReason(BaseValidatorModel):
    Code: Optional[ImageBuilderStateChangeReasonCodeType] = None
    Message: Optional[str] = None


class NetworkAccessConfiguration(BaseValidatorModel):
    EniPrivateIpAddress: Optional[str] = None
    EniId: Optional[str] = None


class ImagePermissions(BaseValidatorModel):
    allowFleet: Optional[bool] = None
    allowImageBuilder: Optional[bool] = None


class ImageStateChangeReason(BaseValidatorModel):
    Code: Optional[ImageStateChangeReasonCodeType] = None
    Message: Optional[str] = None


class LastReportGenerationExecutionError(BaseValidatorModel):
    ErrorCode: Optional[UsageReportExecutionErrorCodeType] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'list_associated_fleets' function.
class ListAssociatedFleetsRequest(BaseValidatorModel):
    StackName: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_associated_stacks' function.
class ListAssociatedStacksRequest(BaseValidatorModel):
    FleetName: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_entitled_applications' function.
class ListEntitledApplicationsRequest(BaseValidatorModel):
    StackName: str
    EntitlementName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class StackError(BaseValidatorModel):
    ErrorCode: Optional[StackErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class StorageConnectorOutput(BaseValidatorModel):
    ConnectorType: StorageConnectorTypeType
    ResourceIdentifier: Optional[str] = None
    Domains: Optional[List[str]] = None
    DomainsRequireAdminConsent: Optional[List[str]] = None


# This class is the input for the 'start_app_block_builder' function.
class StartAppBlockBuilderRequest(BaseValidatorModel):
    Name: str


class StartFleetRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'start_image_builder' function.
class StartImageBuilderRequest(BaseValidatorModel):
    Name: str
    AppstreamAgentVersion: Optional[str] = None


# This class is the input for the 'stop_app_block_builder' function.
class StopAppBlockBuilderRequest(BaseValidatorModel):
    Name: str


class StopFleetRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'stop_image_builder' function.
class StopImageBuilderRequest(BaseValidatorModel):
    Name: str


class StorageConnector(BaseValidatorModel):
    ConnectorType: StorageConnectorTypeType
    ResourceIdentifier: Optional[str] = None
    Domains: Optional[List[str]] = None
    DomainsRequireAdminConsent: Optional[List[str]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class VpcConfig(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None


class AppBlockBuilder(BaseValidatorModel):
    Arn: str
    Name: str
    Platform: Literal['WINDOWS_SERVER_2019']
    InstanceType: str
    VpcConfig: VpcConfigOutput
    State: AppBlockBuilderStateType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    IamRoleArn: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    AppBlockBuilderErrors: Optional[List[ResourceError]] = None
    StateChangeReason: Optional[AppBlockBuilderStateChangeReason] = None
    AccessEndpoints: Optional[List[AccessEndpoint]] = None


class Application(BaseValidatorModel):
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
    IconS3Location: Optional[S3Location] = None
    Platforms: Optional[List[PlatformTypeType]] = None
    InstanceFamilies: Optional[List[str]] = None
    CreatedTime: Optional[datetime] = None


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    Name: str
    IconS3Location: S3Location
    LaunchPath: str
    Platforms: List[PlatformTypeType]
    InstanceFamilies: List[str]
    AppBlockArn: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    WorkingDirectory: Optional[str] = None
    LaunchParameters: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ScriptDetails(BaseValidatorModel):
    ScriptS3Location: S3Location
    ExecutablePath: str
    TimeoutInSeconds: int
    ExecutableParameters: Optional[str] = None


# This class is the input for the 'update_application' function.
class UpdateApplicationRequest(BaseValidatorModel):
    Name: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    IconS3Location: Optional[S3Location] = None
    LaunchPath: Optional[str] = None
    WorkingDirectory: Optional[str] = None
    LaunchParameters: Optional[str] = None
    AppBlockArn: Optional[str] = None
    AttributesToDelete: Optional[List[ApplicationAttributeType]] = None


# This class is the output for the 'associate_app_block_builder_app_block' function.
class AssociateAppBlockBuilderAppBlockResult(BaseValidatorModel):
    AppBlockBuilderAppBlockAssociation: AppBlockBuilderAppBlockAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_application_fleet' function.
class AssociateApplicationFleetResult(BaseValidatorModel):
    ApplicationFleetAssociation: ApplicationFleetAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_image' function.
class CopyImageResponse(BaseValidatorModel):
    DestinationImageName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_app_block_builder_streaming_url' function.
class CreateAppBlockBuilderStreamingURLResult(BaseValidatorModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_image_builder_streaming_url' function.
class CreateImageBuilderStreamingURLResult(BaseValidatorModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_streaming_url' function.
class CreateStreamingURLResult(BaseValidatorModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadata


class CreateUsageReportSubscriptionResult(BaseValidatorModel):
    S3BucketName: str
    Schedule: Literal['DAILY']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_block_builder_app_block_associations' function.
class DescribeAppBlockBuilderAppBlockAssociationsResult(BaseValidatorModel):
    AppBlockBuilderAppBlockAssociations: List[AppBlockBuilderAppBlockAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_application_fleet_associations' function.
class DescribeApplicationFleetAssociationsResult(BaseValidatorModel):
    ApplicationFleetAssociations: List[ApplicationFleetAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_associated_fleets' function.
class ListAssociatedFleetsResult(BaseValidatorModel):
    Names: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_associated_stacks' function.
class ListAssociatedStacksResult(BaseValidatorModel):
    Names: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_associate_user_stack' function.
class BatchAssociateUserStackRequest(BaseValidatorModel):
    UserStackAssociations: List[UserStackAssociation]


# This class is the input for the 'batch_disassociate_user_stack' function.
class BatchDisassociateUserStackRequest(BaseValidatorModel):
    UserStackAssociations: List[UserStackAssociation]


# This class is the output for the 'describe_user_stack_associations' function.
class DescribeUserStackAssociationsResult(BaseValidatorModel):
    UserStackAssociations: List[UserStackAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UserStackAssociationError(BaseValidatorModel):
    UserStackAssociation: Optional[UserStackAssociation] = None
    ErrorCode: Optional[UserStackAssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'create_directory_config' function.
class CreateDirectoryConfigRequest(BaseValidatorModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: List[str]
    ServiceAccountCredentials: Optional[ServiceAccountCredentials] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthProperties] = None


class DirectoryConfig(BaseValidatorModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Optional[List[str]] = None
    ServiceAccountCredentials: Optional[ServiceAccountCredentials] = None
    CreatedTime: Optional[datetime] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthProperties] = None


# This class is the input for the 'update_directory_config' function.
class UpdateDirectoryConfigRequest(BaseValidatorModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Optional[List[str]] = None
    ServiceAccountCredentials: Optional[ServiceAccountCredentials] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthProperties] = None


# This class is the input for the 'create_entitlement' function.
class CreateEntitlementRequest(BaseValidatorModel):
    Name: str
    StackName: str
    AppVisibility: AppVisibilityType
    Attributes: List[EntitlementAttribute]
    Description: Optional[str] = None


class Entitlement(BaseValidatorModel):
    Name: str
    StackName: str
    AppVisibility: AppVisibilityType
    Attributes: List[EntitlementAttribute]
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


# This class is the input for the 'update_entitlement' function.
class UpdateEntitlementRequest(BaseValidatorModel):
    Name: str
    StackName: str
    Description: Optional[str] = None
    AppVisibility: Optional[AppVisibilityType] = None
    Attributes: Optional[List[EntitlementAttribute]] = None


# This class is the input for the 'create_theme_for_stack' function.
class CreateThemeForStackRequest(BaseValidatorModel):
    StackName: str
    TitleText: str
    ThemeStyling: ThemeStylingType
    OrganizationLogoS3Location: S3Location
    FaviconS3Location: S3Location
    FooterLinks: Optional[List[ThemeFooterLink]] = None


class Theme(BaseValidatorModel):
    StackName: Optional[str] = None
    State: Optional[ThemeStateType] = None
    ThemeTitleText: Optional[str] = None
    ThemeStyling: Optional[ThemeStylingType] = None
    ThemeFooterLinks: Optional[List[ThemeFooterLink]] = None
    ThemeOrganizationLogoURL: Optional[str] = None
    ThemeFaviconURL: Optional[str] = None
    CreatedTime: Optional[datetime] = None


# This class is the input for the 'update_theme_for_stack' function.
class UpdateThemeForStackRequest(BaseValidatorModel):
    StackName: str
    FooterLinks: Optional[List[ThemeFooterLink]] = None
    TitleText: Optional[str] = None
    ThemeStyling: Optional[ThemeStylingType] = None
    OrganizationLogoS3Location: Optional[S3Location] = None
    FaviconS3Location: Optional[S3Location] = None
    State: Optional[ThemeStateType] = None
    AttributesToDelete: Optional[List[Literal['FOOTER_LINKS']]] = None


class DescribeDirectoryConfigsRequestPaginate(BaseValidatorModel):
    DirectoryNames: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFleetsRequestPaginate(BaseValidatorModel):
    Names: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeImageBuildersRequestPaginate(BaseValidatorModel):
    Names: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeImagesRequestPaginate(BaseValidatorModel):
    Names: Optional[List[str]] = None
    Arns: Optional[List[str]] = None
    Type: Optional[VisibilityTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSessionsRequestPaginate(BaseValidatorModel):
    StackName: str
    FleetName: str
    UserId: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    InstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStacksRequestPaginate(BaseValidatorModel):
    Names: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUserStackAssociationsRequestPaginate(BaseValidatorModel):
    StackName: Optional[str] = None
    UserName: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUsersRequestPaginate(BaseValidatorModel):
    AuthenticationType: AuthenticationTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociatedFleetsRequestPaginate(BaseValidatorModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociatedStacksRequestPaginate(BaseValidatorModel):
    FleetName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeFleetsRequestWaitExtra(BaseValidatorModel):
    Names: Optional[List[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeFleetsRequestWait(BaseValidatorModel):
    Names: Optional[List[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'describe_users' function.
class DescribeUsersResult(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_entitled_applications' function.
class ListEntitledApplicationsResult(BaseValidatorModel):
    EntitledApplications: List[EntitledApplication]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Fleet(BaseValidatorModel):
    Arn: str
    Name: str
    InstanceType: str
    ComputeCapacityStatus: ComputeCapacityStatus
    State: FleetStateType
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    MaxUserDurationInSeconds: Optional[int] = None
    DisconnectTimeoutInSeconds: Optional[int] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    CreatedTime: Optional[datetime] = None
    FleetErrors: Optional[List[FleetError]] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfo] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    IamRoleArn: Optional[str] = None
    StreamView: Optional[StreamViewType] = None
    Platform: Optional[PlatformTypeType] = None
    MaxConcurrentSessions: Optional[int] = None
    UsbDeviceFilterStrings: Optional[List[str]] = None
    SessionScriptS3Location: Optional[S3Location] = None
    MaxSessionsPerInstance: Optional[int] = None


class ImageBuilder(BaseValidatorModel):
    Name: str
    Arn: Optional[str] = None
    ImageArn: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    VpcConfig: Optional[VpcConfigOutput] = None
    InstanceType: Optional[str] = None
    Platform: Optional[PlatformTypeType] = None
    IamRoleArn: Optional[str] = None
    State: Optional[ImageBuilderStateType] = None
    StateChangeReason: Optional[ImageBuilderStateChangeReason] = None
    CreatedTime: Optional[datetime] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfo] = None
    NetworkAccessConfiguration: Optional[NetworkAccessConfiguration] = None
    ImageBuilderErrors: Optional[List[ResourceError]] = None
    AppstreamAgentVersion: Optional[str] = None
    AccessEndpoints: Optional[List[AccessEndpoint]] = None
    LatestAppstreamAgentVersion: Optional[LatestAppstreamAgentVersionType] = None


class Session(BaseValidatorModel):
    Id: str
    UserId: str
    StackName: str
    FleetName: str
    State: SessionStateType
    ConnectionState: Optional[SessionConnectionStateType] = None
    StartTime: Optional[datetime] = None
    MaxExpirationTime: Optional[datetime] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    NetworkAccessConfiguration: Optional[NetworkAccessConfiguration] = None
    InstanceId: Optional[str] = None


class SharedImagePermissions(BaseValidatorModel):
    sharedAccountId: str
    imagePermissions: ImagePermissions


class UpdateImagePermissionsRequest(BaseValidatorModel):
    Name: str
    SharedAccountId: str
    ImagePermissions: ImagePermissions


class UsageReportSubscription(BaseValidatorModel):
    S3BucketName: Optional[str] = None
    Schedule: Optional[Literal['DAILY']] = None
    LastGeneratedReportDate: Optional[datetime] = None
    SubscriptionErrors: Optional[List[LastReportGenerationExecutionError]] = None


class Stack(BaseValidatorModel):
    Name: str
    Arn: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    StorageConnectors: Optional[List[StorageConnectorOutput]] = None
    RedirectURL: Optional[str] = None
    FeedbackURL: Optional[str] = None
    StackErrors: Optional[List[StackError]] = None
    UserSettings: Optional[List[UserSetting]] = None
    ApplicationSettings: Optional[ApplicationSettingsResponse] = None
    AccessEndpoints: Optional[List[AccessEndpoint]] = None
    EmbedHostDomains: Optional[List[str]] = None
    StreamingExperienceSettings: Optional[StreamingExperienceSettings] = None

StorageConnectorUnion = Union[StorageConnector, StorageConnectorOutput]

VpcConfigUnion = Union[VpcConfig, VpcConfigOutput]


# This class is the output for the 'create_app_block_builder' function.
class CreateAppBlockBuilderResult(BaseValidatorModel):
    AppBlockBuilder: AppBlockBuilder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_block_builders' function.
class DescribeAppBlockBuildersResult(BaseValidatorModel):
    AppBlockBuilders: List[AppBlockBuilder]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_app_block_builder' function.
class StartAppBlockBuilderResult(BaseValidatorModel):
    AppBlockBuilder: AppBlockBuilder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_app_block_builder' function.
class StopAppBlockBuilderResult(BaseValidatorModel):
    AppBlockBuilder: AppBlockBuilder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_app_block_builder' function.
class UpdateAppBlockBuilderResult(BaseValidatorModel):
    AppBlockBuilder: AppBlockBuilder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_application' function.
class CreateApplicationResult(BaseValidatorModel):
    Application: Application
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_applications' function.
class DescribeApplicationsResult(BaseValidatorModel):
    Applications: List[Application]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Image(BaseValidatorModel):
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
    StateChangeReason: Optional[ImageStateChangeReason] = None
    Applications: Optional[List[Application]] = None
    CreatedTime: Optional[datetime] = None
    PublicBaseImageReleasedDate: Optional[datetime] = None
    AppstreamAgentVersion: Optional[str] = None
    ImagePermissions: Optional[ImagePermissions] = None
    ImageErrors: Optional[List[ResourceError]] = None
    LatestAppstreamAgentVersion: Optional[LatestAppstreamAgentVersionType] = None
    SupportedInstanceFamilies: Optional[List[str]] = None
    DynamicAppProvidersEnabled: Optional[DynamicAppProvidersEnabledType] = None
    ImageSharedWithOthers: Optional[ImageSharedWithOthersType] = None


# This class is the output for the 'update_application' function.
class UpdateApplicationResult(BaseValidatorModel):
    Application: Application
    ResponseMetadata: ResponseMetadata


class AppBlock(BaseValidatorModel):
    Name: str
    Arn: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    SourceS3Location: Optional[S3Location] = None
    SetupScriptDetails: Optional[ScriptDetails] = None
    CreatedTime: Optional[datetime] = None
    PostSetupScriptDetails: Optional[ScriptDetails] = None
    PackagingType: Optional[PackagingTypeType] = None
    State: Optional[AppBlockStateType] = None
    AppBlockErrors: Optional[List[ErrorDetails]] = None


# This class is the input for the 'create_app_block' function.
class CreateAppBlockRequest(BaseValidatorModel):
    Name: str
    SourceS3Location: S3Location
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    SetupScriptDetails: Optional[ScriptDetails] = None
    Tags: Optional[Dict[str, str]] = None
    PostSetupScriptDetails: Optional[ScriptDetails] = None
    PackagingType: Optional[PackagingTypeType] = None


# This class is the output for the 'batch_associate_user_stack' function.
class BatchAssociateUserStackResult(BaseValidatorModel):
    errors: List[UserStackAssociationError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_disassociate_user_stack' function.
class BatchDisassociateUserStackResult(BaseValidatorModel):
    errors: List[UserStackAssociationError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_directory_config' function.
class CreateDirectoryConfigResult(BaseValidatorModel):
    DirectoryConfig: DirectoryConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_directory_configs' function.
class DescribeDirectoryConfigsResult(BaseValidatorModel):
    DirectoryConfigs: List[DirectoryConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_directory_config' function.
class UpdateDirectoryConfigResult(BaseValidatorModel):
    DirectoryConfig: DirectoryConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_entitlement' function.
class CreateEntitlementResult(BaseValidatorModel):
    Entitlement: Entitlement
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_entitlements' function.
class DescribeEntitlementsResult(BaseValidatorModel):
    Entitlements: List[Entitlement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_entitlement' function.
class UpdateEntitlementResult(BaseValidatorModel):
    Entitlement: Entitlement
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_theme_for_stack' function.
class CreateThemeForStackResult(BaseValidatorModel):
    Theme: Theme
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_theme_for_stack' function.
class DescribeThemeForStackResult(BaseValidatorModel):
    Theme: Theme
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_theme_for_stack' function.
class UpdateThemeForStackResult(BaseValidatorModel):
    Theme: Theme
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_fleet' function.
class CreateFleetResult(BaseValidatorModel):
    Fleet: Fleet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fleets' function.
class DescribeFleetsResult(BaseValidatorModel):
    Fleets: List[Fleet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_fleet' function.
class UpdateFleetResult(BaseValidatorModel):
    Fleet: Fleet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_image_builder' function.
class CreateImageBuilderResult(BaseValidatorModel):
    ImageBuilder: ImageBuilder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_image_builder' function.
class DeleteImageBuilderResult(BaseValidatorModel):
    ImageBuilder: ImageBuilder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_image_builders' function.
class DescribeImageBuildersResult(BaseValidatorModel):
    ImageBuilders: List[ImageBuilder]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_image_builder' function.
class StartImageBuilderResult(BaseValidatorModel):
    ImageBuilder: ImageBuilder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_image_builder' function.
class StopImageBuilderResult(BaseValidatorModel):
    ImageBuilder: ImageBuilder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_sessions' function.
class DescribeSessionsResult(BaseValidatorModel):
    Sessions: List[Session]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_image_permissions' function.
class DescribeImagePermissionsResult(BaseValidatorModel):
    Name: str
    SharedImagePermissionsList: List[SharedImagePermissions]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_usage_report_subscriptions' function.
class DescribeUsageReportSubscriptionsResult(BaseValidatorModel):
    UsageReportSubscriptions: List[UsageReportSubscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_stack' function.
class CreateStackResult(BaseValidatorModel):
    Stack: Stack
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_stacks' function.
class DescribeStacksResult(BaseValidatorModel):
    Stacks: List[Stack]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_stack' function.
class UpdateStackResult(BaseValidatorModel):
    Stack: Stack
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_stack' function.
class CreateStackRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    StorageConnectors: Optional[List[StorageConnectorUnion]] = None
    RedirectURL: Optional[str] = None
    FeedbackURL: Optional[str] = None
    UserSettings: Optional[List[UserSetting]] = None
    ApplicationSettings: Optional[ApplicationSettings] = None
    Tags: Optional[Dict[str, str]] = None
    AccessEndpoints: Optional[List[AccessEndpoint]] = None
    EmbedHostDomains: Optional[List[str]] = None
    StreamingExperienceSettings: Optional[StreamingExperienceSettings] = None


# This class is the input for the 'update_stack' function.
class UpdateStackRequest(BaseValidatorModel):
    Name: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    StorageConnectors: Optional[List[StorageConnectorUnion]] = None
    DeleteStorageConnectors: Optional[bool] = None
    RedirectURL: Optional[str] = None
    FeedbackURL: Optional[str] = None
    AttributesToDelete: Optional[List[StackAttributeType]] = None
    UserSettings: Optional[List[UserSetting]] = None
    ApplicationSettings: Optional[ApplicationSettings] = None
    AccessEndpoints: Optional[List[AccessEndpoint]] = None
    EmbedHostDomains: Optional[List[str]] = None
    StreamingExperienceSettings: Optional[StreamingExperienceSettings] = None


# This class is the input for the 'create_app_block_builder' function.
class CreateAppBlockBuilderRequest(BaseValidatorModel):
    Name: str
    Platform: Literal['WINDOWS_SERVER_2019']
    InstanceType: str
    VpcConfig: VpcConfigUnion
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    IamRoleArn: Optional[str] = None
    AccessEndpoints: Optional[List[AccessEndpoint]] = None


# This class is the input for the 'create_fleet' function.
class CreateFleetRequest(BaseValidatorModel):
    Name: str
    InstanceType: str
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    FleetType: Optional[FleetTypeType] = None
    ComputeCapacity: Optional[ComputeCapacity] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    MaxUserDurationInSeconds: Optional[int] = None
    DisconnectTimeoutInSeconds: Optional[int] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfo] = None
    Tags: Optional[Dict[str, str]] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    IamRoleArn: Optional[str] = None
    StreamView: Optional[StreamViewType] = None
    Platform: Optional[PlatformTypeType] = None
    MaxConcurrentSessions: Optional[int] = None
    UsbDeviceFilterStrings: Optional[List[str]] = None
    SessionScriptS3Location: Optional[S3Location] = None
    MaxSessionsPerInstance: Optional[int] = None


# This class is the input for the 'create_image_builder' function.
class CreateImageBuilderRequest(BaseValidatorModel):
    Name: str
    InstanceType: str
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    IamRoleArn: Optional[str] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfo] = None
    AppstreamAgentVersion: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    AccessEndpoints: Optional[List[AccessEndpoint]] = None


# This class is the input for the 'update_app_block_builder' function.
class UpdateAppBlockBuilderRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Platform: Optional[PlatformTypeType] = None
    InstanceType: Optional[str] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    IamRoleArn: Optional[str] = None
    AccessEndpoints: Optional[List[AccessEndpoint]] = None
    AttributesToDelete: Optional[List[AppBlockBuilderAttributeType]] = None


# This class is the input for the 'update_fleet' function.
class UpdateFleetRequest(BaseValidatorModel):
    ImageName: Optional[str] = None
    ImageArn: Optional[str] = None
    Name: Optional[str] = None
    InstanceType: Optional[str] = None
    ComputeCapacity: Optional[ComputeCapacity] = None
    VpcConfig: Optional[VpcConfigUnion] = None
    MaxUserDurationInSeconds: Optional[int] = None
    DisconnectTimeoutInSeconds: Optional[int] = None
    DeleteVpcConfig: Optional[bool] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    EnableDefaultInternetAccess: Optional[bool] = None
    DomainJoinInfo: Optional[DomainJoinInfo] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    AttributesToDelete: Optional[List[FleetAttributeType]] = None
    IamRoleArn: Optional[str] = None
    StreamView: Optional[StreamViewType] = None
    Platform: Optional[PlatformTypeType] = None
    MaxConcurrentSessions: Optional[int] = None
    UsbDeviceFilterStrings: Optional[List[str]] = None
    SessionScriptS3Location: Optional[S3Location] = None
    MaxSessionsPerInstance: Optional[int] = None


# This class is the output for the 'create_updated_image' function.
class CreateUpdatedImageResult(BaseValidatorModel):
    image: Image
    canUpdateImage: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_image' function.
class DeleteImageResult(BaseValidatorModel):
    Image: Image
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_images' function.
class DescribeImagesResult(BaseValidatorModel):
    Images: List[Image]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_app_block' function.
class CreateAppBlockResult(BaseValidatorModel):
    AppBlock: AppBlock
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_app_blocks' function.
class DescribeAppBlocksResult(BaseValidatorModel):
    AppBlocks: List[AppBlock]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
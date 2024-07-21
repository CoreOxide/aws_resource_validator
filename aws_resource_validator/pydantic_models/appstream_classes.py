from datetime import datetime
from pydantic import BaseModel
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

class AccessEndpointTypeDef(BaseModel):
    EndpointType: Literal["STREAMING"]
    VpceId: Optional[str] = None

class AppBlockBuilderAppBlockAssociationTypeDef(BaseModel):
    AppBlockArn: str
    AppBlockBuilderName: str

class AppBlockBuilderStateChangeReasonTypeDef(BaseModel):
    Code: Optional[Literal["INTERNAL_ERROR"]] = None
    Message: Optional[str] = None

class ResourceErrorTypeDef(BaseModel):
    ErrorCode: Optional[FleetErrorCodeType] = None
    ErrorMessage: Optional[str] = None
    ErrorTimestamp: Optional[datetime] = None

class VpcConfigTypeDef(BaseModel):
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class ErrorDetailsTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class S3LocationTypeDef(BaseModel):
    S3Bucket: str
    S3Key: Optional[str] = None

class ApplicationFleetAssociationTypeDef(BaseModel):
    FleetName: str
    ApplicationArn: str

class ApplicationSettingsResponseTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    SettingsGroup: Optional[str] = None
    S3BucketName: Optional[str] = None

class ApplicationSettingsTypeDef(BaseModel):
    Enabled: bool
    SettingsGroup: Optional[str] = None

class AssociateAppBlockBuilderAppBlockRequestRequestTypeDef(BaseModel):
    AppBlockArn: str
    AppBlockBuilderName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateApplicationFleetRequestRequestTypeDef(BaseModel):
    FleetName: str
    ApplicationArn: str

class AssociateApplicationToEntitlementRequestRequestTypeDef(BaseModel):
    StackName: str
    EntitlementName: str
    ApplicationIdentifier: str

class AssociateFleetRequestRequestTypeDef(BaseModel):
    FleetName: str
    StackName: str

class UserStackAssociationTypeDef(BaseModel):
    StackName: str
    UserName: str
    AuthenticationType: AuthenticationTypeType
    SendEmailNotification: Optional[bool] = None

class CertificateBasedAuthPropertiesTypeDef(BaseModel):
    Status: Optional[CertificateBasedAuthStatusType] = None
    CertificateAuthorityArn: Optional[str] = None

class ComputeCapacityStatusTypeDef(BaseModel):
    Desired: int
    Running: Optional[int] = None
    InUse: Optional[int] = None
    Available: Optional[int] = None
    DesiredUserSessions: Optional[int] = None
    AvailableUserSessions: Optional[int] = None
    ActiveUserSessions: Optional[int] = None
    ActualUserSessions: Optional[int] = None

class ComputeCapacityTypeDef(BaseModel):
    DesiredInstances: Optional[int] = None
    DesiredSessions: Optional[int] = None

class CopyImageRequestRequestTypeDef(BaseModel):
    SourceImageName: str
    DestinationImageName: str
    DestinationRegion: str
    DestinationImageDescription: Optional[str] = None

class CreateAppBlockBuilderStreamingURLRequestRequestTypeDef(BaseModel):
    AppBlockBuilderName: str
    Validity: Optional[int] = None

class ServiceAccountCredentialsTypeDef(BaseModel):
    AccountName: str
    AccountPassword: str

class EntitlementAttributeTypeDef(BaseModel):
    Name: str
    Value: str

class DomainJoinInfoTypeDef(BaseModel):
    DirectoryName: Optional[str] = None
    OrganizationalUnitDistinguishedName: Optional[str] = None

class CreateImageBuilderStreamingURLRequestRequestTypeDef(BaseModel):
    Name: str
    Validity: Optional[int] = None

class StorageConnectorTypeDef(BaseModel):
    ConnectorType: StorageConnectorTypeType
    ResourceIdentifier: Optional[str] = None
    Domains: Optional[Sequence[str]] = None

class StreamingExperienceSettingsTypeDef(BaseModel):
    PreferredProtocol: Optional[PreferredProtocolType] = None

class UserSettingTypeDef(BaseModel):
    Action: ActionType
    Permission: PermissionType
    MaximumLength: Optional[int] = None

class CreateStreamingURLRequestRequestTypeDef(BaseModel):
    StackName: str
    FleetName: str
    UserId: str
    ApplicationId: Optional[str] = None
    Validity: Optional[int] = None
    SessionContext: Optional[str] = None

class CreateUpdatedImageRequestRequestTypeDef(BaseModel):
    existingImageName: str
    newImageName: str
    newImageDescription: Optional[str] = None
    newImageDisplayName: Optional[str] = None
    newImageTags: Optional[Mapping[str, str]] = None
    dryRun: Optional[bool] = None

class CreateUserRequestRequestTypeDef(BaseModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType
    MessageAction: Optional[MessageActionType] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

class DeleteAppBlockBuilderRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteAppBlockRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteDirectoryConfigRequestRequestTypeDef(BaseModel):
    DirectoryName: str

class DeleteEntitlementRequestRequestTypeDef(BaseModel):
    Name: str
    StackName: str

class DeleteFleetRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteImageBuilderRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteImagePermissionsRequestRequestTypeDef(BaseModel):
    Name: str
    SharedAccountId: str

class DeleteImageRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteStackRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class DescribeAppBlockBuilderAppBlockAssociationsRequestRequestTypeDef(BaseModel):
    AppBlockArn: Optional[str] = None
    AppBlockBuilderName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeAppBlockBuildersRequestRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeAppBlocksRequestRequestTypeDef(BaseModel):
    Arns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeApplicationFleetAssociationsRequestRequestTypeDef(BaseModel):
    FleetName: Optional[str] = None
    ApplicationArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeApplicationsRequestRequestTypeDef(BaseModel):
    Arns: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDirectoryConfigsRequestRequestTypeDef(BaseModel):
    DirectoryNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeEntitlementsRequestRequestTypeDef(BaseModel):
    StackName: str
    Name: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeFleetsRequestRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeImageBuildersRequestRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImagePermissionsRequestRequestTypeDef(BaseModel):
    Name: str
    MaxResults: Optional[int] = None
    SharedAwsAccountIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeImagesRequestRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    Arns: Optional[Sequence[str]] = None
    Type: Optional[VisibilityTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSessionsRequestRequestTypeDef(BaseModel):
    StackName: str
    FleetName: str
    UserId: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    InstanceId: Optional[str] = None

class DescribeStacksRequestRequestTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeUsageReportSubscriptionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeUserStackAssociationsRequestRequestTypeDef(BaseModel):
    StackName: Optional[str] = None
    UserName: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeUsersRequestRequestTypeDef(BaseModel):
    AuthenticationType: AuthenticationTypeType
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UserTypeDef(BaseModel):
    AuthenticationType: AuthenticationTypeType
    Arn: Optional[str] = None
    UserName: Optional[str] = None
    Enabled: Optional[bool] = None
    Status: Optional[str] = None
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    CreatedTime: Optional[datetime] = None

class DisableUserRequestRequestTypeDef(BaseModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class DisassociateAppBlockBuilderAppBlockRequestRequestTypeDef(BaseModel):
    AppBlockArn: str
    AppBlockBuilderName: str

class DisassociateApplicationFleetRequestRequestTypeDef(BaseModel):
    FleetName: str
    ApplicationArn: str

class DisassociateApplicationFromEntitlementRequestRequestTypeDef(BaseModel):
    StackName: str
    EntitlementName: str
    ApplicationIdentifier: str

class DisassociateFleetRequestRequestTypeDef(BaseModel):
    FleetName: str
    StackName: str

class EnableUserRequestRequestTypeDef(BaseModel):
    UserName: str
    AuthenticationType: AuthenticationTypeType

class EntitledApplicationTypeDef(BaseModel):
    ApplicationIdentifier: str

class ExpireSessionRequestRequestTypeDef(BaseModel):
    SessionId: str

class FleetErrorTypeDef(BaseModel):
    ErrorCode: Optional[FleetErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class VpcConfigPaginatorTypeDef(BaseModel):
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None

class ImageBuilderStateChangeReasonTypeDef(BaseModel):
    Code: Optional[ImageBuilderStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class NetworkAccessConfigurationTypeDef(BaseModel):
    EniPrivateIpAddress: Optional[str] = None
    EniId: Optional[str] = None

class ImagePermissionsTypeDef(BaseModel):
    allowFleet: Optional[bool] = None
    allowImageBuilder: Optional[bool] = None

class ImageStateChangeReasonTypeDef(BaseModel):
    Code: Optional[ImageStateChangeReasonCodeType] = None
    Message: Optional[str] = None

class LastReportGenerationExecutionErrorTypeDef(BaseModel):
    ErrorCode: Optional[UsageReportExecutionErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class ListAssociatedFleetsRequestRequestTypeDef(BaseModel):
    StackName: str
    NextToken: Optional[str] = None

class ListAssociatedStacksRequestRequestTypeDef(BaseModel):
    FleetName: str
    NextToken: Optional[str] = None

class ListEntitledApplicationsRequestRequestTypeDef(BaseModel):
    StackName: str
    EntitlementName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class StackErrorTypeDef(BaseModel):
    ErrorCode: Optional[StackErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class StorageConnectorPaginatorTypeDef(BaseModel):
    ConnectorType: StorageConnectorTypeType
    ResourceIdentifier: Optional[str] = None
    Domains: Optional[List[str]] = None

class StartAppBlockBuilderRequestRequestTypeDef(BaseModel):
    Name: str

class StartFleetRequestRequestTypeDef(BaseModel):
    Name: str

class StartImageBuilderRequestRequestTypeDef(BaseModel):
    Name: str
    AppstreamAgentVersion: Optional[str] = None

class StopAppBlockBuilderRequestRequestTypeDef(BaseModel):
    Name: str

class StopFleetRequestRequestTypeDef(BaseModel):
    Name: str

class StopImageBuilderRequestRequestTypeDef(BaseModel):
    Name: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class AppBlockBuilderTypeDef(BaseModel):
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

class CreateAppBlockBuilderRequestRequestTypeDef(BaseModel):
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

class UpdateAppBlockBuilderRequestRequestTypeDef(BaseModel):
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

class ApplicationTypeDef(BaseModel):
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

class CreateApplicationRequestRequestTypeDef(BaseModel):
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

class ScriptDetailsTypeDef(BaseModel):
    ScriptS3Location: S3LocationTypeDef
    ExecutablePath: str
    TimeoutInSeconds: int
    ExecutableParameters: Optional[str] = None

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    Name: str
    DisplayName: Optional[str] = None
    Description: Optional[str] = None
    IconS3Location: Optional[S3LocationTypeDef] = None
    LaunchPath: Optional[str] = None
    WorkingDirectory: Optional[str] = None
    LaunchParameters: Optional[str] = None
    AppBlockArn: Optional[str] = None
    AttributesToDelete: Optional[Sequence[ApplicationAttributeType]] = None

class AssociateAppBlockBuilderAppBlockResultTypeDef(BaseModel):
    AppBlockBuilderAppBlockAssociation: AppBlockBuilderAppBlockAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateApplicationFleetResultTypeDef(BaseModel):
    ApplicationFleetAssociation: ApplicationFleetAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyImageResponseTypeDef(BaseModel):
    DestinationImageName: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppBlockBuilderStreamingURLResultTypeDef(BaseModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageBuilderStreamingURLResultTypeDef(BaseModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamingURLResultTypeDef(BaseModel):
    StreamingURL: str
    Expires: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageReportSubscriptionResultTypeDef(BaseModel):
    S3BucketName: str
    Schedule: Literal["DAILY"]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlockBuilderAppBlockAssociationsResultTypeDef(BaseModel):
    AppBlockBuilderAppBlockAssociations: List[AppBlockBuilderAppBlockAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationFleetAssociationsResultTypeDef(BaseModel):
    ApplicationFleetAssociations: List[ApplicationFleetAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedFleetsResultTypeDef(BaseModel):
    Names: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedStacksResultTypeDef(BaseModel):
    Names: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateUserStackRequestRequestTypeDef(BaseModel):
    UserStackAssociations: Sequence[UserStackAssociationTypeDef]

class BatchDisassociateUserStackRequestRequestTypeDef(BaseModel):
    UserStackAssociations: Sequence[UserStackAssociationTypeDef]

class DescribeUserStackAssociationsResultTypeDef(BaseModel):
    UserStackAssociations: List[UserStackAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UserStackAssociationErrorTypeDef(BaseModel):
    UserStackAssociation: Optional[UserStackAssociationTypeDef] = None
    ErrorCode: Optional[UserStackAssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class CreateDirectoryConfigRequestRequestTypeDef(BaseModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Sequence[str]
    ServiceAccountCredentials: Optional[ServiceAccountCredentialsTypeDef] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None

class DirectoryConfigTypeDef(BaseModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Optional[List[str]] = None
    ServiceAccountCredentials: Optional[ServiceAccountCredentialsTypeDef] = None
    CreatedTime: Optional[datetime] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None

class UpdateDirectoryConfigRequestRequestTypeDef(BaseModel):
    DirectoryName: str
    OrganizationalUnitDistinguishedNames: Optional[Sequence[str]] = None
    ServiceAccountCredentials: Optional[ServiceAccountCredentialsTypeDef] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None

class CreateEntitlementRequestRequestTypeDef(BaseModel):
    Name: str
    StackName: str
    AppVisibility: AppVisibilityType
    Attributes: Sequence[EntitlementAttributeTypeDef]
    Description: Optional[str] = None

class EntitlementTypeDef(BaseModel):
    Name: str
    StackName: str
    AppVisibility: AppVisibilityType
    Attributes: List[EntitlementAttributeTypeDef]
    Description: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class UpdateEntitlementRequestRequestTypeDef(BaseModel):
    Name: str
    StackName: str
    Description: Optional[str] = None
    AppVisibility: Optional[AppVisibilityType] = None
    Attributes: Optional[Sequence[EntitlementAttributeTypeDef]] = None

class CreateFleetRequestRequestTypeDef(BaseModel):
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

class CreateImageBuilderRequestRequestTypeDef(BaseModel):
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

class UpdateFleetRequestRequestTypeDef(BaseModel):
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

class CreateStackRequestRequestTypeDef(BaseModel):
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

class UpdateStackRequestRequestTypeDef(BaseModel):
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

class DescribeDirectoryConfigsRequestDescribeDirectoryConfigsPaginateTypeDef(BaseModel):
    DirectoryNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetsRequestDescribeFleetsPaginateTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImageBuildersRequestDescribeImageBuildersPaginateTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImagesRequestDescribeImagesPaginateTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    Arns: Optional[Sequence[str]] = None
    Type: Optional[VisibilityTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSessionsRequestDescribeSessionsPaginateTypeDef(BaseModel):
    StackName: str
    FleetName: str
    UserId: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    InstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStacksRequestDescribeStacksPaginateTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUserStackAssociationsRequestDescribeUserStackAssociationsPaginateTypeDef(BaseModel):
    StackName: Optional[str] = None
    UserName: Optional[str] = None
    AuthenticationType: Optional[AuthenticationTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsersRequestDescribeUsersPaginateTypeDef(BaseModel):
    AuthenticationType: AuthenticationTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedFleetsRequestListAssociatedFleetsPaginateTypeDef(BaseModel):
    StackName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedStacksRequestListAssociatedStacksPaginateTypeDef(BaseModel):
    FleetName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetsRequestFleetStartedWaitTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFleetsRequestFleetStoppedWaitTypeDef(BaseModel):
    Names: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeUsersResultTypeDef(BaseModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEntitledApplicationsResultTypeDef(BaseModel):
    EntitledApplications: List[EntitledApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class FleetTypeDef(BaseModel):
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

class FleetPaginatorTypeDef(BaseModel):
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

class ImageBuilderPaginatorTypeDef(BaseModel):
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

class ImageBuilderTypeDef(BaseModel):
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

class SessionTypeDef(BaseModel):
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

class SharedImagePermissionsTypeDef(BaseModel):
    sharedAccountId: str
    imagePermissions: ImagePermissionsTypeDef

class UpdateImagePermissionsRequestRequestTypeDef(BaseModel):
    Name: str
    SharedAccountId: str
    ImagePermissions: ImagePermissionsTypeDef

class UsageReportSubscriptionTypeDef(BaseModel):
    S3BucketName: Optional[str] = None
    Schedule: Optional[Literal["DAILY"]] = None
    LastGeneratedReportDate: Optional[datetime] = None
    SubscriptionErrors: Optional[List[LastReportGenerationExecutionErrorTypeDef]] = None

class StackTypeDef(BaseModel):
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

class StackPaginatorTypeDef(BaseModel):
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

class CreateAppBlockBuilderResultTypeDef(BaseModel):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlockBuildersResultTypeDef(BaseModel):
    AppBlockBuilders: List[AppBlockBuilderTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAppBlockBuilderResultTypeDef(BaseModel):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopAppBlockBuilderResultTypeDef(BaseModel):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppBlockBuilderResultTypeDef(BaseModel):
    AppBlockBuilder: AppBlockBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResultTypeDef(BaseModel):
    Application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeApplicationsResultTypeDef(BaseModel):
    Applications: List[ApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImageTypeDef(BaseModel):
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

class UpdateApplicationResultTypeDef(BaseModel):
    Application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AppBlockTypeDef(BaseModel):
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

class CreateAppBlockRequestRequestTypeDef(BaseModel):
    Name: str
    SourceS3Location: S3LocationTypeDef
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    SetupScriptDetails: Optional[ScriptDetailsTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    PostSetupScriptDetails: Optional[ScriptDetailsTypeDef] = None
    PackagingType: Optional[PackagingTypeType] = None

class BatchAssociateUserStackResultTypeDef(BaseModel):
    errors: List[UserStackAssociationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateUserStackResultTypeDef(BaseModel):
    errors: List[UserStackAssociationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryConfigResultTypeDef(BaseModel):
    DirectoryConfig: DirectoryConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectoryConfigsResultTypeDef(BaseModel):
    DirectoryConfigs: List[DirectoryConfigTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDirectoryConfigResultTypeDef(BaseModel):
    DirectoryConfig: DirectoryConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEntitlementResultTypeDef(BaseModel):
    Entitlement: EntitlementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntitlementsResultTypeDef(BaseModel):
    Entitlements: List[EntitlementTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEntitlementResultTypeDef(BaseModel):
    Entitlement: EntitlementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFleetResultTypeDef(BaseModel):
    Fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetsResultTypeDef(BaseModel):
    Fleets: List[FleetTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFleetResultTypeDef(BaseModel):
    Fleet: FleetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFleetsResultPaginatorTypeDef(BaseModel):
    Fleets: List[FleetPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageBuildersResultPaginatorTypeDef(BaseModel):
    ImageBuilders: List[ImageBuilderPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageBuilderResultTypeDef(BaseModel):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageBuilderResultTypeDef(BaseModel):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageBuildersResultTypeDef(BaseModel):
    ImageBuilders: List[ImageBuilderTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImageBuilderResultTypeDef(BaseModel):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopImageBuilderResultTypeDef(BaseModel):
    ImageBuilder: ImageBuilderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSessionsResultTypeDef(BaseModel):
    Sessions: List[SessionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImagePermissionsResultTypeDef(BaseModel):
    Name: str
    SharedImagePermissionsList: List[SharedImagePermissionsTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsageReportSubscriptionsResultTypeDef(BaseModel):
    UsageReportSubscriptions: List[UsageReportSubscriptionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStackResultTypeDef(BaseModel):
    Stack: StackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStacksResultTypeDef(BaseModel):
    Stacks: List[StackTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStackResultTypeDef(BaseModel):
    Stack: StackTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStacksResultPaginatorTypeDef(BaseModel):
    Stacks: List[StackPaginatorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUpdatedImageResultTypeDef(BaseModel):
    image: ImageTypeDef
    canUpdateImage: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageResultTypeDef(BaseModel):
    Image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImagesResultTypeDef(BaseModel):
    Images: List[ImageTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppBlockResultTypeDef(BaseModel):
    AppBlock: AppBlockTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppBlocksResultTypeDef(BaseModel):
    AppBlocks: List[AppBlockTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


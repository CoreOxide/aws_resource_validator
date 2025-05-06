from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mq.mq_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActionRequired(BaseValidatorModel):
    ActionRequiredCode: Optional[str] = None
    ActionRequiredInfo: Optional[str] = None


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class EngineVersion(BaseValidatorModel):
    Name: Optional[str] = None


class BrokerInstance(BaseValidatorModel):
    ConsoleURL: Optional[str] = None
    Endpoints: Optional[List[str]] = None
    IpAddress: Optional[str] = None


class BrokerSummary(BaseValidatorModel):
    DeploymentMode: DeploymentModeType
    EngineType: EngineTypeType
    BrokerArn: Optional[str] = None
    BrokerId: Optional[str] = None
    BrokerName: Optional[str] = None
    BrokerState: Optional[BrokerStateType] = None
    Created: Optional[datetime] = None
    HostInstanceType: Optional[str] = None


class ConfigurationId(BaseValidatorModel):
    Id: str
    Revision: Optional[int] = None


class ConfigurationRevision(BaseValidatorModel):
    Created: datetime
    Revision: int
    Description: Optional[str] = None


class EncryptionOptions(BaseValidatorModel):
    UseAwsOwnedKey: bool
    KmsKeyId: Optional[str] = None


class LdapServerMetadataInput(BaseValidatorModel):
    Hosts: List[str]
    RoleBase: str
    RoleSearchMatching: str
    ServiceAccountPassword: str
    ServiceAccountUsername: str
    UserBase: str
    UserSearchMatching: str
    RoleName: Optional[str] = None
    RoleSearchSubtree: Optional[bool] = None
    UserRoleName: Optional[str] = None
    UserSearchSubtree: Optional[bool] = None


class Logs(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None


class User(BaseValidatorModel):
    Password: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[List[str]] = None
    ReplicationUser: Optional[bool] = None


class WeeklyStartTime(BaseValidatorModel):
    DayOfWeek: DayOfWeekType
    TimeOfDay: str
    TimeZone: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateConfigurationRequest(BaseValidatorModel):
    EngineType: EngineTypeType
    Name: str
    AuthenticationStrategy: Optional[AuthenticationStrategyType] = None
    EngineVersion: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class CreateTagsRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Optional[Dict[str, str]] = None


class CreateUserRequest(BaseValidatorModel):
    BrokerId: str
    Password: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[List[str]] = None
    ReplicationUser: Optional[bool] = None


class DataReplicationCounterpart(BaseValidatorModel):
    BrokerId: str
    Region: str


class DeleteBrokerRequest(BaseValidatorModel):
    BrokerId: str


class DeleteTagsRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class DeleteUserRequest(BaseValidatorModel):
    BrokerId: str
    Username: str


class DescribeBrokerEngineTypesRequest(BaseValidatorModel):
    EngineType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBrokerInstanceOptionsRequest(BaseValidatorModel):
    EngineType: Optional[str] = None
    HostInstanceType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StorageType: Optional[str] = None


class DescribeBrokerRequest(BaseValidatorModel):
    BrokerId: str


class LdapServerMetadataOutput(BaseValidatorModel):
    Hosts: List[str]
    RoleBase: str
    RoleSearchMatching: str
    ServiceAccountUsername: str
    UserBase: str
    UserSearchMatching: str
    RoleName: Optional[str] = None
    RoleSearchSubtree: Optional[bool] = None
    UserRoleName: Optional[str] = None
    UserSearchSubtree: Optional[bool] = None


class UserSummary(BaseValidatorModel):
    Username: str
    PendingChange: Optional[ChangeTypeType] = None


class DescribeConfigurationRequest(BaseValidatorModel):
    ConfigurationId: str


class DescribeConfigurationRevisionRequest(BaseValidatorModel):
    ConfigurationId: str
    ConfigurationRevision: str


class DescribeUserRequest(BaseValidatorModel):
    BrokerId: str
    Username: str


class UserPendingChanges(BaseValidatorModel):
    PendingChange: ChangeTypeType
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBrokersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConfigurationRevisionsRequest(BaseValidatorModel):
    ConfigurationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsRequest(BaseValidatorModel):
    ResourceArn: str


class ListUsersRequest(BaseValidatorModel):
    BrokerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PendingLogs(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None


class PromoteRequest(BaseValidatorModel):
    BrokerId: str
    Mode: PromoteModeType


class RebootBrokerRequest(BaseValidatorModel):
    BrokerId: str


class SanitizationWarning(BaseValidatorModel):
    Reason: SanitizationWarningReasonType
    AttributeName: Optional[str] = None
    ElementName: Optional[str] = None


class UpdateConfigurationRequest(BaseValidatorModel):
    ConfigurationId: str
    Data: str
    Description: Optional[str] = None


class UpdateUserRequest(BaseValidatorModel):
    BrokerId: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[List[str]] = None
    Password: Optional[str] = None
    ReplicationUser: Optional[bool] = None


class BrokerInstanceOption(BaseValidatorModel):
    AvailabilityZones: Optional[List[AvailabilityZone]] = None
    EngineType: Optional[EngineTypeType] = None
    HostInstanceType: Optional[str] = None
    StorageType: Optional[BrokerStorageTypeType] = None
    SupportedDeploymentModes: Optional[List[DeploymentModeType]] = None
    SupportedEngineVersions: Optional[List[str]] = None


class BrokerEngineType(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None
    EngineVersions: Optional[List[EngineVersion]] = None


class Configurations(BaseValidatorModel):
    Current: Optional[ConfigurationId] = None
    History: Optional[List[ConfigurationId]] = None
    Pending: Optional[ConfigurationId] = None


class Configuration(BaseValidatorModel):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Description: str
    EngineType: EngineTypeType
    EngineVersion: str
    Id: str
    LatestRevision: ConfigurationRevision
    Name: str
    Tags: Optional[Dict[str, str]] = None


class CreateBrokerRequest(BaseValidatorModel):
    BrokerName: str
    DeploymentMode: DeploymentModeType
    EngineType: EngineTypeType
    HostInstanceType: str
    PubliclyAccessible: bool
    Users: List[User]
    AuthenticationStrategy: Optional[AuthenticationStrategyType] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Configuration: Optional[ConfigurationId] = None
    CreatorRequestId: Optional[str] = None
    EncryptionOptions: Optional[EncryptionOptions] = None
    EngineVersion: Optional[str] = None
    LdapServerMetadata: Optional[LdapServerMetadataInput] = None
    Logs: Optional[Logs] = None
    MaintenanceWindowStartTime: Optional[WeeklyStartTime] = None
    SecurityGroups: Optional[List[str]] = None
    StorageType: Optional[BrokerStorageTypeType] = None
    SubnetIds: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    DataReplicationMode: Optional[DataReplicationModeType] = None
    DataReplicationPrimaryBrokerArn: Optional[str] = None


class UpdateBrokerRequest(BaseValidatorModel):
    BrokerId: str
    AuthenticationStrategy: Optional[AuthenticationStrategyType] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Configuration: Optional[ConfigurationId] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    LdapServerMetadata: Optional[LdapServerMetadataInput] = None
    Logs: Optional[Logs] = None
    MaintenanceWindowStartTime: Optional[WeeklyStartTime] = None
    SecurityGroups: Optional[List[str]] = None
    DataReplicationMode: Optional[DataReplicationModeType] = None


class CreateBrokerResponse(BaseValidatorModel):
    BrokerArn: str
    BrokerId: str
    ResponseMetadata: ResponseMetadata


class CreateConfigurationResponse(BaseValidatorModel):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Id: str
    LatestRevision: ConfigurationRevision
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteBrokerResponse(BaseValidatorModel):
    BrokerId: str
    ResponseMetadata: ResponseMetadata


class DescribeConfigurationResponse(BaseValidatorModel):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Description: str
    EngineType: EngineTypeType
    EngineVersion: str
    Id: str
    LatestRevision: ConfigurationRevision
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class DescribeConfigurationRevisionResponse(BaseValidatorModel):
    ConfigurationId: str
    Created: datetime
    Data: str
    Description: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListBrokersResponse(BaseValidatorModel):
    BrokerSummaries: List[BrokerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListConfigurationRevisionsResponse(BaseValidatorModel):
    ConfigurationId: str
    MaxResults: int
    Revisions: List[ConfigurationRevision]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PromoteResponse(BaseValidatorModel):
    BrokerId: str
    ResponseMetadata: ResponseMetadata


class DataReplicationMetadataOutput(BaseValidatorModel):
    DataReplicationRole: str
    DataReplicationCounterpart: Optional[DataReplicationCounterpart] = None


class ListUsersResponse(BaseValidatorModel):
    BrokerId: str
    MaxResults: int
    Users: List[UserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeUserResponse(BaseValidatorModel):
    BrokerId: str
    ConsoleAccess: bool
    Groups: List[str]
    Pending: UserPendingChanges
    Username: str
    ReplicationUser: bool
    ResponseMetadata: ResponseMetadata


class ListBrokersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class LogsSummary(BaseValidatorModel):
    General: bool
    GeneralLogGroup: str
    Audit: Optional[bool] = None
    AuditLogGroup: Optional[str] = None
    Pending: Optional[PendingLogs] = None


class UpdateConfigurationResponse(BaseValidatorModel):
    Arn: str
    Created: datetime
    Id: str
    LatestRevision: ConfigurationRevision
    Name: str
    Warnings: List[SanitizationWarning]
    ResponseMetadata: ResponseMetadata


class DescribeBrokerInstanceOptionsResponse(BaseValidatorModel):
    BrokerInstanceOptions: List[BrokerInstanceOption]
    MaxResults: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeBrokerEngineTypesResponse(BaseValidatorModel):
    BrokerEngineTypes: List[BrokerEngineType]
    MaxResults: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListConfigurationsResponse(BaseValidatorModel):
    Configurations: List[Configuration]
    MaxResults: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateBrokerResponse(BaseValidatorModel):
    AuthenticationStrategy: AuthenticationStrategyType
    AutoMinorVersionUpgrade: bool
    BrokerId: str
    Configuration: ConfigurationId
    EngineVersion: str
    HostInstanceType: str
    LdapServerMetadata: LdapServerMetadataOutput
    Logs: Logs
    MaintenanceWindowStartTime: WeeklyStartTime
    SecurityGroups: List[str]
    DataReplicationMetadata: DataReplicationMetadataOutput
    DataReplicationMode: DataReplicationModeType
    PendingDataReplicationMetadata: DataReplicationMetadataOutput
    PendingDataReplicationMode: DataReplicationModeType
    ResponseMetadata: ResponseMetadata


class DescribeBrokerResponse(BaseValidatorModel):
    ActionsRequired: List[ActionRequired]
    AuthenticationStrategy: AuthenticationStrategyType
    AutoMinorVersionUpgrade: bool
    BrokerArn: str
    BrokerId: str
    BrokerInstances: List[BrokerInstance]
    BrokerName: str
    BrokerState: BrokerStateType
    Configurations: Configurations
    Created: datetime
    DeploymentMode: DeploymentModeType
    EncryptionOptions: EncryptionOptions
    EngineType: EngineTypeType
    EngineVersion: str
    HostInstanceType: str
    LdapServerMetadata: LdapServerMetadataOutput
    Logs: LogsSummary
    MaintenanceWindowStartTime: WeeklyStartTime
    PendingAuthenticationStrategy: AuthenticationStrategyType
    PendingEngineVersion: str
    PendingHostInstanceType: str
    PendingLdapServerMetadata: LdapServerMetadataOutput
    PendingSecurityGroups: List[str]
    PubliclyAccessible: bool
    SecurityGroups: List[str]
    StorageType: BrokerStorageTypeType
    SubnetIds: List[str]
    Tags: Dict[str, str]
    Users: List[UserSummary]
    DataReplicationMetadata: DataReplicationMetadataOutput
    DataReplicationMode: DataReplicationModeType
    PendingDataReplicationMetadata: DataReplicationMetadataOutput
    PendingDataReplicationMode: DataReplicationModeType
    ResponseMetadata: ResponseMetadata
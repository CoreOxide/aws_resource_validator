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
from aws_resource_validator.pydantic_models.mq_constants import *

class ActionRequiredTypeDef(BaseModel):
    ActionRequiredCode: Optional[str] = None
    ActionRequiredInfo: Optional[str] = None

class AvailabilityZoneTypeDef(BaseModel):
    Name: Optional[str] = None

class EngineVersionTypeDef(BaseModel):
    Name: Optional[str] = None

class BrokerInstanceTypeDef(BaseModel):
    ConsoleURL: Optional[str] = None
    Endpoints: Optional[List[str]] = None
    IpAddress: Optional[str] = None

class BrokerSummaryTypeDef(BaseModel):
    DeploymentMode: DeploymentModeType
    EngineType: EngineTypeType
    BrokerArn: Optional[str] = None
    BrokerId: Optional[str] = None
    BrokerName: Optional[str] = None
    BrokerState: Optional[BrokerStateType] = None
    Created: Optional[datetime] = None
    HostInstanceType: Optional[str] = None

class ConfigurationIdTypeDef(BaseModel):
    Id: str
    Revision: Optional[int] = None

class ConfigurationRevisionTypeDef(BaseModel):
    Created: datetime
    Revision: int
    Description: Optional[str] = None

class EncryptionOptionsTypeDef(BaseModel):
    UseAwsOwnedKey: bool
    KmsKeyId: Optional[str] = None

class LdapServerMetadataInputTypeDef(BaseModel):
    Hosts: Sequence[str]
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

class LogsTypeDef(BaseModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None

class UserTypeDef(BaseModel):
    Password: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    ReplicationUser: Optional[bool] = None

class WeeklyStartTimeTypeDef(BaseModel):
    DayOfWeek: DayOfWeekType
    TimeOfDay: str
    TimeZone: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateConfigurationRequestRequestTypeDef(BaseModel):
    EngineType: EngineTypeType
    Name: str
    AuthenticationStrategy: Optional[AuthenticationStrategyType] = None
    EngineVersion: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateTagsRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Optional[Mapping[str, str]] = None

class CreateUserRequestRequestTypeDef(BaseModel):
    BrokerId: str
    Password: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    ReplicationUser: Optional[bool] = None

class DataReplicationCounterpartTypeDef(BaseModel):
    BrokerId: str
    Region: str

class DeleteBrokerRequestRequestTypeDef(BaseModel):
    BrokerId: str

class DeleteTagsRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class DeleteUserRequestRequestTypeDef(BaseModel):
    BrokerId: str
    Username: str

class DescribeBrokerEngineTypesRequestRequestTypeDef(BaseModel):
    EngineType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeBrokerInstanceOptionsRequestRequestTypeDef(BaseModel):
    EngineType: Optional[str] = None
    HostInstanceType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StorageType: Optional[str] = None

class DescribeBrokerRequestRequestTypeDef(BaseModel):
    BrokerId: str

class LdapServerMetadataOutputTypeDef(BaseModel):
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

class UserSummaryTypeDef(BaseModel):
    Username: str
    PendingChange: Optional[ChangeTypeType] = None

class DescribeConfigurationRequestRequestTypeDef(BaseModel):
    ConfigurationId: str

class DescribeConfigurationRevisionRequestRequestTypeDef(BaseModel):
    ConfigurationId: str
    ConfigurationRevision: str

class DescribeUserRequestRequestTypeDef(BaseModel):
    BrokerId: str
    Username: str

class UserPendingChangesTypeDef(BaseModel):
    PendingChange: ChangeTypeType
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBrokersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConfigurationRevisionsRequestRequestTypeDef(BaseModel):
    ConfigurationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ListUsersRequestRequestTypeDef(BaseModel):
    BrokerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PendingLogsTypeDef(BaseModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None

class PromoteRequestRequestTypeDef(BaseModel):
    BrokerId: str
    Mode: PromoteModeType

class RebootBrokerRequestRequestTypeDef(BaseModel):
    BrokerId: str

class SanitizationWarningTypeDef(BaseModel):
    Reason: SanitizationWarningReasonType
    AttributeName: Optional[str] = None
    ElementName: Optional[str] = None

class UpdateConfigurationRequestRequestTypeDef(BaseModel):
    ConfigurationId: str
    Data: str
    Description: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseModel):
    BrokerId: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    Password: Optional[str] = None
    ReplicationUser: Optional[bool] = None

class BrokerInstanceOptionTypeDef(BaseModel):
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    EngineType: Optional[EngineTypeType] = None
    HostInstanceType: Optional[str] = None
    StorageType: Optional[BrokerStorageTypeType] = None
    SupportedDeploymentModes: Optional[List[DeploymentModeType]] = None
    SupportedEngineVersions: Optional[List[str]] = None

class BrokerEngineTypeTypeDef(BaseModel):
    EngineType: Optional[EngineTypeType] = None
    EngineVersions: Optional[List[EngineVersionTypeDef]] = None

class ConfigurationsTypeDef(BaseModel):
    Current: Optional[ConfigurationIdTypeDef] = None
    History: Optional[List[ConfigurationIdTypeDef]] = None
    Pending: Optional[ConfigurationIdTypeDef] = None

class ConfigurationTypeDef(BaseModel):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Description: str
    EngineType: EngineTypeType
    EngineVersion: str
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    Tags: Optional[Dict[str, str]] = None

class CreateBrokerRequestRequestTypeDef(BaseModel):
    BrokerName: str
    DeploymentMode: DeploymentModeType
    EngineType: EngineTypeType
    HostInstanceType: str
    PubliclyAccessible: bool
    Users: Sequence[UserTypeDef]
    AuthenticationStrategy: Optional[AuthenticationStrategyType] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Configuration: Optional[ConfigurationIdTypeDef] = None
    CreatorRequestId: Optional[str] = None
    EncryptionOptions: Optional[EncryptionOptionsTypeDef] = None
    EngineVersion: Optional[str] = None
    LdapServerMetadata: Optional[LdapServerMetadataInputTypeDef] = None
    Logs: Optional[LogsTypeDef] = None
    MaintenanceWindowStartTime: Optional[WeeklyStartTimeTypeDef] = None
    SecurityGroups: Optional[Sequence[str]] = None
    StorageType: Optional[BrokerStorageTypeType] = None
    SubnetIds: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None
    DataReplicationMode: Optional[DataReplicationModeType] = None
    DataReplicationPrimaryBrokerArn: Optional[str] = None

class UpdateBrokerRequestRequestTypeDef(BaseModel):
    BrokerId: str
    AuthenticationStrategy: Optional[AuthenticationStrategyType] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Configuration: Optional[ConfigurationIdTypeDef] = None
    EngineVersion: Optional[str] = None
    HostInstanceType: Optional[str] = None
    LdapServerMetadata: Optional[LdapServerMetadataInputTypeDef] = None
    Logs: Optional[LogsTypeDef] = None
    MaintenanceWindowStartTime: Optional[WeeklyStartTimeTypeDef] = None
    SecurityGroups: Optional[Sequence[str]] = None
    DataReplicationMode: Optional[DataReplicationModeType] = None

class CreateBrokerResponseTypeDef(BaseModel):
    BrokerArn: str
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfigurationResponseTypeDef(BaseModel):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBrokerResponseTypeDef(BaseModel):
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationResponseTypeDef(BaseModel):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Description: str
    EngineType: EngineTypeType
    EngineVersion: str
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConfigurationRevisionResponseTypeDef(BaseModel):
    ConfigurationId: str
    Created: datetime
    Data: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListBrokersResponseTypeDef(BaseModel):
    BrokerSummaries: List[BrokerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListConfigurationRevisionsResponseTypeDef(BaseModel):
    ConfigurationId: str
    MaxResults: int
    Revisions: List[ConfigurationRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PromoteResponseTypeDef(BaseModel):
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataReplicationMetadataOutputTypeDef(BaseModel):
    DataReplicationRole: str
    DataReplicationCounterpart: Optional[DataReplicationCounterpartTypeDef] = None

class ListUsersResponseTypeDef(BaseModel):
    BrokerId: str
    MaxResults: int
    Users: List[UserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeUserResponseTypeDef(BaseModel):
    BrokerId: str
    ConsoleAccess: bool
    Groups: List[str]
    Pending: UserPendingChangesTypeDef
    Username: str
    ReplicationUser: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ListBrokersRequestListBrokersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LogsSummaryTypeDef(BaseModel):
    General: bool
    GeneralLogGroup: str
    Audit: Optional[bool] = None
    AuditLogGroup: Optional[str] = None
    Pending: Optional[PendingLogsTypeDef] = None

class UpdateConfigurationResponseTypeDef(BaseModel):
    Arn: str
    Created: datetime
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    Warnings: List[SanitizationWarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBrokerInstanceOptionsResponseTypeDef(BaseModel):
    BrokerInstanceOptions: List[BrokerInstanceOptionTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeBrokerEngineTypesResponseTypeDef(BaseModel):
    BrokerEngineTypes: List[BrokerEngineTypeTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListConfigurationsResponseTypeDef(BaseModel):
    Configurations: List[ConfigurationTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateBrokerResponseTypeDef(BaseModel):
    AuthenticationStrategy: AuthenticationStrategyType
    AutoMinorVersionUpgrade: bool
    BrokerId: str
    Configuration: ConfigurationIdTypeDef
    EngineVersion: str
    HostInstanceType: str
    LdapServerMetadata: LdapServerMetadataOutputTypeDef
    Logs: LogsTypeDef
    MaintenanceWindowStartTime: WeeklyStartTimeTypeDef
    SecurityGroups: List[str]
    DataReplicationMetadata: DataReplicationMetadataOutputTypeDef
    DataReplicationMode: DataReplicationModeType
    PendingDataReplicationMetadata: DataReplicationMetadataOutputTypeDef
    PendingDataReplicationMode: DataReplicationModeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBrokerResponseTypeDef(BaseModel):
    ActionsRequired: List[ActionRequiredTypeDef]
    AuthenticationStrategy: AuthenticationStrategyType
    AutoMinorVersionUpgrade: bool
    BrokerArn: str
    BrokerId: str
    BrokerInstances: List[BrokerInstanceTypeDef]
    BrokerName: str
    BrokerState: BrokerStateType
    Configurations: ConfigurationsTypeDef
    Created: datetime
    DeploymentMode: DeploymentModeType
    EncryptionOptions: EncryptionOptionsTypeDef
    EngineType: EngineTypeType
    EngineVersion: str
    HostInstanceType: str
    LdapServerMetadata: LdapServerMetadataOutputTypeDef
    Logs: LogsSummaryTypeDef
    MaintenanceWindowStartTime: WeeklyStartTimeTypeDef
    PendingAuthenticationStrategy: AuthenticationStrategyType
    PendingEngineVersion: str
    PendingHostInstanceType: str
    PendingLdapServerMetadata: LdapServerMetadataOutputTypeDef
    PendingSecurityGroups: List[str]
    PubliclyAccessible: bool
    SecurityGroups: List[str]
    StorageType: BrokerStorageTypeType
    SubnetIds: List[str]
    Tags: Dict[str, str]
    Users: List[UserSummaryTypeDef]
    DataReplicationMetadata: DataReplicationMetadataOutputTypeDef
    DataReplicationMode: DataReplicationModeType
    PendingDataReplicationMetadata: DataReplicationMetadataOutputTypeDef
    PendingDataReplicationMode: DataReplicationModeType
    ResponseMetadata: ResponseMetadataTypeDef


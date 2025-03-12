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
from aws_resource_validator.pydantic_models.mq_constants import *

class ActionRequiredTypeDef(BaseValidatorModel):
    ActionRequiredCode: Optional[str] = None
    ActionRequiredInfo: Optional[str] = None


class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class EngineVersionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class BrokerInstanceTypeDef(BaseValidatorModel):
    ConsoleURL: Optional[str] = None
    Endpoints: Optional[List[str]] = None
    IpAddress: Optional[str] = None


class BrokerSummaryTypeDef(BaseValidatorModel):
    DeploymentMode: DeploymentModeType
    EngineType: EngineTypeType
    BrokerArn: Optional[str] = None
    BrokerId: Optional[str] = None
    BrokerName: Optional[str] = None
    BrokerState: Optional[BrokerStateType] = None
    Created: Optional[datetime] = None
    HostInstanceType: Optional[str] = None


class ConfigurationIdTypeDef(BaseValidatorModel):
    Id: str
    Revision: Optional[int] = None


class ConfigurationRevisionTypeDef(BaseValidatorModel):
    Created: datetime
    Revision: int
    Description: Optional[str] = None


class EncryptionOptionsTypeDef(BaseValidatorModel):
    UseAwsOwnedKey: bool
    KmsKeyId: Optional[str] = None


class LdapServerMetadataInputTypeDef(BaseValidatorModel):
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


class LogsTypeDef(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None


class UserTypeDef(BaseValidatorModel):
    Password: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    ReplicationUser: Optional[bool] = None


class WeeklyStartTimeTypeDef(BaseValidatorModel):
    DayOfWeek: DayOfWeekType
    TimeOfDay: str
    TimeZone: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateConfigurationRequestTypeDef(BaseValidatorModel):
    EngineType: EngineTypeType
    Name: str
    AuthenticationStrategy: Optional[AuthenticationStrategyType] = None
    EngineVersion: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateTagsRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Optional[Mapping[str, str]] = None


class CreateUserRequestTypeDef(BaseValidatorModel):
    BrokerId: str
    Password: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    ReplicationUser: Optional[bool] = None


class DataReplicationCounterpartTypeDef(BaseValidatorModel):
    BrokerId: str
    Region: str


class DeleteBrokerRequestTypeDef(BaseValidatorModel):
    BrokerId: str


class DeleteTagsRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class DeleteUserRequestTypeDef(BaseValidatorModel):
    BrokerId: str
    Username: str


class DescribeBrokerEngineTypesRequestTypeDef(BaseValidatorModel):
    EngineType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeBrokerInstanceOptionsRequestTypeDef(BaseValidatorModel):
    EngineType: Optional[str] = None
    HostInstanceType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    StorageType: Optional[str] = None


class DescribeBrokerRequestTypeDef(BaseValidatorModel):
    BrokerId: str


class LdapServerMetadataOutputTypeDef(BaseValidatorModel):
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


class UserSummaryTypeDef(BaseValidatorModel):
    Username: str
    PendingChange: Optional[ChangeTypeType] = None


class DescribeConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigurationId: str


class DescribeConfigurationRevisionRequestTypeDef(BaseValidatorModel):
    ConfigurationId: str
    ConfigurationRevision: str


class DescribeUserRequestTypeDef(BaseValidatorModel):
    BrokerId: str
    Username: str


class UserPendingChangesTypeDef(BaseValidatorModel):
    PendingChange: ChangeTypeType
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[List[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBrokersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConfigurationRevisionsRequestTypeDef(BaseValidatorModel):
    ConfigurationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class ListUsersRequestTypeDef(BaseValidatorModel):
    BrokerId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PendingLogsTypeDef(BaseValidatorModel):
    Audit: Optional[bool] = None
    General: Optional[bool] = None


class PromoteRequestTypeDef(BaseValidatorModel):
    BrokerId: str
    Mode: PromoteModeType


class RebootBrokerRequestTypeDef(BaseValidatorModel):
    BrokerId: str


class SanitizationWarningTypeDef(BaseValidatorModel):
    Reason: SanitizationWarningReasonType
    AttributeName: Optional[str] = None
    ElementName: Optional[str] = None


class UpdateConfigurationRequestTypeDef(BaseValidatorModel):
    ConfigurationId: str
    Data: str
    Description: Optional[str] = None


class UpdateUserRequestTypeDef(BaseValidatorModel):
    BrokerId: str
    Username: str
    ConsoleAccess: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    Password: Optional[str] = None
    ReplicationUser: Optional[bool] = None


class BrokerInstanceOptionTypeDef(BaseValidatorModel):
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    EngineType: Optional[EngineTypeType] = None
    HostInstanceType: Optional[str] = None
    StorageType: Optional[BrokerStorageTypeType] = None
    SupportedDeploymentModes: Optional[List[DeploymentModeType]] = None
    SupportedEngineVersions: Optional[List[str]] = None


class BrokerEngineTypeTypeDef(BaseValidatorModel):
    EngineType: Optional[EngineTypeType] = None
    EngineVersions: Optional[List[EngineVersionTypeDef]] = None


class ConfigurationsTypeDef(BaseValidatorModel):
    Current: Optional[ConfigurationIdTypeDef] = None
    History: Optional[List[ConfigurationIdTypeDef]] = None
    Pending: Optional[ConfigurationIdTypeDef] = None


class ConfigurationTypeDef(BaseValidatorModel):
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


class CreateBrokerRequestTypeDef(BaseValidatorModel):
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


class UpdateBrokerRequestTypeDef(BaseValidatorModel):
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


class CreateBrokerResponseTypeDef(BaseValidatorModel):
    BrokerArn: str
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    AuthenticationStrategy: AuthenticationStrategyType
    Created: datetime
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBrokerResponseTypeDef(BaseValidatorModel):
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConfigurationResponseTypeDef(BaseValidatorModel):
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


class DescribeConfigurationRevisionResponseTypeDef(BaseValidatorModel):
    ConfigurationId: str
    Created: datetime
    Data: str
    Description: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListBrokersResponseTypeDef(BaseValidatorModel):
    BrokerSummaries: List[BrokerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListConfigurationRevisionsResponseTypeDef(BaseValidatorModel):
    ConfigurationId: str
    MaxResults: int
    Revisions: List[ConfigurationRevisionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PromoteResponseTypeDef(BaseValidatorModel):
    BrokerId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DataReplicationMetadataOutputTypeDef(BaseValidatorModel):
    DataReplicationRole: str
    DataReplicationCounterpart: Optional[DataReplicationCounterpartTypeDef] = None


class ListUsersResponseTypeDef(BaseValidatorModel):
    BrokerId: str
    MaxResults: int
    Users: List[UserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeUserResponseTypeDef(BaseValidatorModel):
    BrokerId: str
    ConsoleAccess: bool
    Groups: List[str]
    Pending: UserPendingChangesTypeDef
    Username: str
    ReplicationUser: bool
    ResponseMetadata: ResponseMetadataTypeDef


class ListBrokersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class LogsSummaryTypeDef(BaseValidatorModel):
    General: bool
    GeneralLogGroup: str
    Audit: Optional[bool] = None
    AuditLogGroup: Optional[str] = None
    Pending: Optional[PendingLogsTypeDef] = None


class UpdateConfigurationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Created: datetime
    Id: str
    LatestRevision: ConfigurationRevisionTypeDef
    Name: str
    Warnings: List[SanitizationWarningTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBrokerInstanceOptionsResponseTypeDef(BaseValidatorModel):
    BrokerInstanceOptions: List[BrokerInstanceOptionTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeBrokerEngineTypesResponseTypeDef(BaseValidatorModel):
    BrokerEngineTypes: List[BrokerEngineTypeTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListConfigurationsResponseTypeDef(BaseValidatorModel):
    Configurations: List[ConfigurationTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateBrokerResponseTypeDef(BaseValidatorModel):
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


class DescribeBrokerResponseTypeDef(BaseValidatorModel):
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



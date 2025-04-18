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
from aws_resource_validator.pydantic_models.ssm_sap_constants import *

class ApplicationCredential(BaseValidatorModel):
    DatabaseName: str
    CredentialType: Literal["ADMIN"]
    SecretId: str


class IpAddressMember(BaseValidatorModel):
    IpAddress: Optional[str] = None
    Primary: Optional[bool] = None
    AllocationType: Optional[AllocationTypeType] = None


class BackintConfig(BaseValidatorModel):
    BackintMode: Literal["AWSBackup"]
    EnsureNoBackupInProcess: bool


class ComponentInfo(BaseValidatorModel):
    ComponentType: ComponentTypeType
    Sid: str
    Ec2InstanceId: str


class ComponentSummary(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    ComponentType: Optional[ComponentTypeType] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None


class DatabaseConnection(BaseValidatorModel):
    DatabaseConnectionMethod: Optional[DatabaseConnectionMethodType] = None
    DatabaseArn: Optional[str] = None
    ConnectionIp: Optional[str] = None


class Host(BaseValidatorModel):
    HostName: Optional[str] = None
    HostIp: Optional[str] = None
    EC2InstanceId: Optional[str] = None
    InstanceId: Optional[str] = None
    HostRole: Optional[HostRoleType] = None
    OsVersion: Optional[str] = None


class Resilience(BaseValidatorModel):
    HsrTier: Optional[str] = None
    HsrReplicationMode: Optional[ReplicationModeType] = None
    HsrOperationMode: Optional[OperationModeType] = None
    ClusterStatus: Optional[ClusterStatusType] = None
    EnqueueReplication: Optional[bool] = None


class DatabaseSummary(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseType: Optional[DatabaseTypeType] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class DeleteResourcePermissionInput(BaseValidatorModel):
    ResourceArn: str
    ActionType: Optional[Literal["RESTORE"]] = None
    SourceResourceArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeregisterApplicationInput(BaseValidatorModel):
    ApplicationId: str


class Filter(BaseValidatorModel):
    Name: str
    Value: str
    Operator: FilterOperatorType


class GetApplicationInput(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ApplicationArn: Optional[str] = None
    AppRegistryArn: Optional[str] = None


class GetComponentInput(BaseValidatorModel):
    ApplicationId: str
    ComponentId: str


class GetDatabaseInput(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseArn: Optional[str] = None


class GetOperationInput(BaseValidatorModel):
    OperationId: str


class GetResourcePermissionInput(BaseValidatorModel):
    ResourceArn: str
    ActionType: Optional[Literal["RESTORE"]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListComponentsInput(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDatabasesInput(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class Resource(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None


class PutResourcePermissionInput(BaseValidatorModel):
    ActionType: Literal["RESTORE"]
    SourceResourceArn: str
    ResourceArn: str


class StartApplicationInput(BaseValidatorModel):
    ApplicationId: str


class StartApplicationRefreshInput(BaseValidatorModel):
    ApplicationId: str


class StopApplicationInput(BaseValidatorModel):
    ApplicationId: str
    StopConnectedEntity: Optional[Literal["DBMS"]] = None
    IncludeEc2InstanceShutdown: Optional[bool] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class Database(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    Credentials: Optional[List[ApplicationCredential]] = None
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    DatabaseType: Optional[DatabaseTypeType] = None
    Arn: Optional[str] = None
    Status: Optional[DatabaseStatusType] = None
    PrimaryHost: Optional[str] = None
    SQLPort: Optional[int] = None
    LastUpdated: Optional[datetime] = None
    ConnectedComponentArns: Optional[List[str]] = None


class AssociatedHost(BaseValidatorModel):
    Hostname: Optional[str] = None
    Ec2InstanceId: Optional[str] = None
    IpAddresses: Optional[List[IpAddressMember]] = None
    OsVersion: Optional[str] = None


class UpdateApplicationSettingsInput(BaseValidatorModel):
    ApplicationId: str
    CredentialsToAddOrUpdate: Optional[Sequence[ApplicationCredential]] = None
    CredentialsToRemove: Optional[Sequence[ApplicationCredential]] = None
    Backint: Optional[BackintConfig] = None
    DatabaseArn: Optional[str] = None


class RegisterApplicationInput(BaseValidatorModel):
    ApplicationId: str
    ApplicationType: ApplicationTypeType
    Instances: Sequence[str]
    SapInstanceNumber: Optional[str] = None
    Sid: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Credentials: Optional[Sequence[ApplicationCredential]] = None
    DatabaseArn: Optional[str] = None
    ComponentsInfo: Optional[Sequence[ComponentInfo]] = None


class DeleteResourcePermissionOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class Application(BaseValidatorModel):
    pass


class GetApplicationOutput(BaseValidatorModel):
    Application: Application
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetResourcePermissionOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class ApplicationSummary(BaseValidatorModel):
    pass


class ListApplicationsOutput(BaseValidatorModel):
    Applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListComponentsOutput(BaseValidatorModel):
    Components: List[ComponentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDatabasesOutput(BaseValidatorModel):
    Databases: List[DatabaseSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutResourcePermissionOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class RegisterApplicationOutput(BaseValidatorModel):
    Application: Application
    OperationId: str
    ResponseMetadata: ResponseMetadata


class StartApplicationOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class StartApplicationRefreshOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class StopApplicationOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


class UpdateApplicationSettingsOutput(BaseValidatorModel):
    Message: str
    OperationIds: List[str]
    ResponseMetadata: ResponseMetadata


class ListApplicationsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[Filter]] = None


class ListOperationEventsInput(BaseValidatorModel):
    OperationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None


class ListOperationsInput(BaseValidatorModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None


class Operation(BaseValidatorModel):
    pass


class GetOperationOutput(BaseValidatorModel):
    Operation: Operation
    ResponseMetadata: ResponseMetadata


class ListOperationsOutput(BaseValidatorModel):
    Operations: List[Operation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationsInputPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComponentsInputPaginate(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatabasesInputPaginate(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOperationEventsInputPaginate(BaseValidatorModel):
    OperationId: str
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOperationsInputPaginate(BaseValidatorModel):
    ApplicationId: str
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class OperationEvent(BaseValidatorModel):
    Description: Optional[str] = None
    Resource: Optional[Resource] = None
    Status: Optional[OperationEventStatusType] = None
    StatusMessage: Optional[str] = None
    Timestamp: Optional[datetime] = None


class GetDatabaseOutput(BaseValidatorModel):
    Database: Database
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Component(BaseValidatorModel):
    ComponentId: Optional[str] = None
    Sid: Optional[str] = None
    SystemNumber: Optional[str] = None
    ParentComponent: Optional[str] = None
    ChildComponents: Optional[List[str]] = None
    ApplicationId: Optional[str] = None
    ComponentType: Optional[ComponentTypeType] = None
    Status: Optional[ComponentStatusType] = None
    SapHostname: Optional[str] = None
    SapFeature: Optional[str] = None
    SapKernelVersion: Optional[str] = None
    HdbVersion: Optional[str] = None
    Resilience: Optional[Resilience] = None
    AssociatedHost: Optional[AssociatedHost] = None
    Databases: Optional[List[str]] = None
    Hosts: Optional[List[Host]] = None
    PrimaryHost: Optional[str] = None
    DatabaseConnection: Optional[DatabaseConnection] = None
    LastUpdated: Optional[datetime] = None
    Arn: Optional[str] = None


class ListOperationEventsOutput(BaseValidatorModel):
    OperationEvents: List[OperationEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetComponentOutput(BaseValidatorModel):
    Component: Component
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata



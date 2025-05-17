from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ssm_sap.ssm_sap_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApplicationCredential(BaseValidatorModel):
    DatabaseName: str
    CredentialType: Literal['ADMIN']
    SecretId: str


class ApplicationSummary(BaseValidatorModel):
    Id: Optional[str] = None
    DiscoveryStatus: Optional[ApplicationDiscoveryStatusType] = None
    Type: Optional[ApplicationTypeType] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class Application(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[ApplicationTypeType] = None
    Arn: Optional[str] = None
    AppRegistryArn: Optional[str] = None
    Status: Optional[ApplicationStatusType] = None
    DiscoveryStatus: Optional[ApplicationDiscoveryStatusType] = None
    Components: Optional[List[str]] = None
    LastUpdated: Optional[datetime] = None
    StatusMessage: Optional[str] = None
    AssociatedApplicationArns: Optional[List[str]] = None


class IpAddressMember(BaseValidatorModel):
    IpAddress: Optional[str] = None
    Primary: Optional[bool] = None
    AllocationType: Optional[AllocationTypeType] = None


class BackintConfig(BaseValidatorModel):
    BackintMode: Literal['AWSBackup']
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


# This class is the input for the 'delete_resource_permission' function.
class DeleteResourcePermissionInput(BaseValidatorModel):
    ResourceArn: str
    ActionType: Optional[Literal['RESTORE']] = None
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


# This class is the input for the 'get_application' function.
class GetApplicationInput(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ApplicationArn: Optional[str] = None
    AppRegistryArn: Optional[str] = None


# This class is the input for the 'get_component' function.
class GetComponentInput(BaseValidatorModel):
    ApplicationId: str
    ComponentId: str


# This class is the input for the 'get_database' function.
class GetDatabaseInput(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseArn: Optional[str] = None


# This class is the input for the 'get_operation' function.
class GetOperationInput(BaseValidatorModel):
    OperationId: str


class Operation(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[str] = None
    Status: Optional[OperationStatusType] = None
    StatusMessage: Optional[str] = None
    Properties: Optional[Dict[str, str]] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceArn: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None


# This class is the input for the 'get_resource_permission' function.
class GetResourcePermissionInput(BaseValidatorModel):
    ResourceArn: str
    ActionType: Optional[Literal['RESTORE']] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_components' function.
class ListComponentsInput(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_databases' function.
class ListDatabasesInput(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class Resource(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None


# This class is the input for the 'put_resource_permission' function.
class PutResourcePermissionInput(BaseValidatorModel):
    ActionType: Literal['RESTORE']
    SourceResourceArn: str
    ResourceArn: str


# This class is the input for the 'start_application' function.
class StartApplicationInput(BaseValidatorModel):
    ApplicationId: str


# This class is the input for the 'start_application_refresh' function.
class StartApplicationRefreshInput(BaseValidatorModel):
    ApplicationId: str


# This class is the input for the 'stop_application' function.
class StopApplicationInput(BaseValidatorModel):
    ApplicationId: str
    StopConnectedEntity: Optional[Literal['DBMS']] = None
    IncludeEc2InstanceShutdown: Optional[bool] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


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


# This class is the input for the 'update_application_settings' function.
class UpdateApplicationSettingsInput(BaseValidatorModel):
    ApplicationId: str
    CredentialsToAddOrUpdate: Optional[List[ApplicationCredential]] = None
    CredentialsToRemove: Optional[List[ApplicationCredential]] = None
    Backint: Optional[BackintConfig] = None
    DatabaseArn: Optional[str] = None


# This class is the input for the 'register_application' function.
class RegisterApplicationInput(BaseValidatorModel):
    ApplicationId: str
    ApplicationType: ApplicationTypeType
    Instances: List[str]
    SapInstanceNumber: Optional[str] = None
    Sid: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    Credentials: Optional[List[ApplicationCredential]] = None
    DatabaseArn: Optional[str] = None
    ComponentsInfo: Optional[List[ComponentInfo]] = None


# This class is the output for the 'delete_resource_permission' function.
class DeleteResourcePermissionOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_application' function.
class GetApplicationOutput(BaseValidatorModel):
    Application: Application
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_permission' function.
class GetResourcePermissionOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_applications' function.
class ListApplicationsOutput(BaseValidatorModel):
    Applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_components' function.
class ListComponentsOutput(BaseValidatorModel):
    Components: List[ComponentSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_databases' function.
class ListDatabasesOutput(BaseValidatorModel):
    Databases: List[DatabaseSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_permission' function.
class PutResourcePermissionOutput(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_application' function.
class RegisterApplicationOutput(BaseValidatorModel):
    Application: Application
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_application' function.
class StartApplicationOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_application_refresh' function.
class StartApplicationRefreshOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_application' function.
class StopApplicationOutput(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_application_settings' function.
class UpdateApplicationSettingsOutput(BaseValidatorModel):
    Message: str
    OperationIds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'list_applications' function.
class ListApplicationsInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'list_operation_events' function.
class ListOperationEventsInput(BaseValidatorModel):
    OperationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'list_operations' function.
class ListOperationsInput(BaseValidatorModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the output for the 'get_operation' function.
class GetOperationOutput(BaseValidatorModel):
    Operation: Operation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_operations' function.
class ListOperationsOutput(BaseValidatorModel):
    Operations: List[Operation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationsInputPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
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
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOperationsInputPaginate(BaseValidatorModel):
    ApplicationId: str
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class OperationEvent(BaseValidatorModel):
    Description: Optional[str] = None
    Resource: Optional[Resource] = None
    Status: Optional[OperationEventStatusType] = None
    StatusMessage: Optional[str] = None
    Timestamp: Optional[datetime] = None


# This class is the output for the 'get_database' function.
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


# This class is the output for the 'list_operation_events' function.
class ListOperationEventsOutput(BaseValidatorModel):
    OperationEvents: List[OperationEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_component' function.
class GetComponentOutput(BaseValidatorModel):
    Component: Component
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata
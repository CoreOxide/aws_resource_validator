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
from aws_resource_validator.pydantic_models.ssm_sap_constants import *

class ApplicationCredentialTypeDef(BaseModel):
    DatabaseName: str
    CredentialType: Literal["ADMIN"]
    SecretId: str

class ApplicationSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    DiscoveryStatus: Optional[ApplicationDiscoveryStatusType] = None
    Type: Optional[ApplicationTypeType] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ApplicationTypeDef(BaseModel):
    Id: Optional[str] = None
    Type: Optional[ApplicationTypeType] = None
    Arn: Optional[str] = None
    AppRegistryArn: Optional[str] = None
    Status: Optional[ApplicationStatusType] = None
    DiscoveryStatus: Optional[ApplicationDiscoveryStatusType] = None
    Components: Optional[List[str]] = None
    LastUpdated: Optional[datetime] = None
    StatusMessage: Optional[str] = None

class IpAddressMemberTypeDef(BaseModel):
    IpAddress: Optional[str] = None
    Primary: Optional[bool] = None
    AllocationType: Optional[AllocationTypeType] = None

class BackintConfigTypeDef(BaseModel):
    BackintMode: Literal["AWSBackup"]
    EnsureNoBackupInProcess: bool

class ComponentSummaryTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    ComponentType: Optional[ComponentTypeType] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None

class DatabaseConnectionTypeDef(BaseModel):
    DatabaseConnectionMethod: Optional[DatabaseConnectionMethodType] = None
    DatabaseArn: Optional[str] = None
    ConnectionIp: Optional[str] = None

class HostTypeDef(BaseModel):
    HostName: Optional[str] = None
    HostIp: Optional[str] = None
    EC2InstanceId: Optional[str] = None
    InstanceId: Optional[str] = None
    HostRole: Optional[HostRoleType] = None
    OsVersion: Optional[str] = None

class ResilienceTypeDef(BaseModel):
    HsrTier: Optional[str] = None
    HsrReplicationMode: Optional[ReplicationModeType] = None
    HsrOperationMode: Optional[OperationModeType] = None
    ClusterStatus: Optional[ClusterStatusType] = None
    EnqueueReplication: Optional[bool] = None

class DatabaseSummaryTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseType: Optional[DatabaseTypeType] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class DeleteResourcePermissionInputRequestTypeDef(BaseModel):
    ResourceArn: str
    ActionType: Optional[Literal["RESTORE"]] = None
    SourceResourceArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeregisterApplicationInputRequestTypeDef(BaseModel):
    ApplicationId: str

class FilterTypeDef(BaseModel):
    Name: str
    Value: str
    Operator: FilterOperatorType

class GetApplicationInputRequestTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ApplicationArn: Optional[str] = None
    AppRegistryArn: Optional[str] = None

class GetComponentInputRequestTypeDef(BaseModel):
    ApplicationId: str
    ComponentId: str

class GetDatabaseInputRequestTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseArn: Optional[str] = None

class GetOperationInputRequestTypeDef(BaseModel):
    OperationId: str

class OperationTypeDef(BaseModel):
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

class GetResourcePermissionInputRequestTypeDef(BaseModel):
    ResourceArn: str
    ActionType: Optional[Literal["RESTORE"]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListComponentsInputRequestTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDatabasesInputRequestTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ResourceTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None

class PutResourcePermissionInputRequestTypeDef(BaseModel):
    ActionType: Literal["RESTORE"]
    SourceResourceArn: str
    ResourceArn: str

class StartApplicationInputRequestTypeDef(BaseModel):
    ApplicationId: str

class StartApplicationRefreshInputRequestTypeDef(BaseModel):
    ApplicationId: str

class StopApplicationInputRequestTypeDef(BaseModel):
    ApplicationId: str
    StopConnectedEntity: Optional[Literal["DBMS"]] = None
    IncludeEc2InstanceShutdown: Optional[bool] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class DatabaseTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    Credentials: Optional[List[ApplicationCredentialTypeDef]] = None
    DatabaseId: Optional[str] = None
    DatabaseName: Optional[str] = None
    DatabaseType: Optional[DatabaseTypeType] = None
    Arn: Optional[str] = None
    Status: Optional[DatabaseStatusType] = None
    PrimaryHost: Optional[str] = None
    SQLPort: Optional[int] = None
    LastUpdated: Optional[datetime] = None

class RegisterApplicationInputRequestTypeDef(BaseModel):
    ApplicationId: str
    ApplicationType: ApplicationTypeType
    Instances: Sequence[str]
    SapInstanceNumber: Optional[str] = None
    Sid: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Credentials: Optional[Sequence[ApplicationCredentialTypeDef]] = None
    DatabaseArn: Optional[str] = None

class AssociatedHostTypeDef(BaseModel):
    Hostname: Optional[str] = None
    Ec2InstanceId: Optional[str] = None
    IpAddresses: Optional[List[IpAddressMemberTypeDef]] = None
    OsVersion: Optional[str] = None

class UpdateApplicationSettingsInputRequestTypeDef(BaseModel):
    ApplicationId: str
    CredentialsToAddOrUpdate: Optional[Sequence[ApplicationCredentialTypeDef]] = None
    CredentialsToRemove: Optional[Sequence[ApplicationCredentialTypeDef]] = None
    Backint: Optional[BackintConfigTypeDef] = None
    DatabaseArn: Optional[str] = None

class DeleteResourcePermissionOutputTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationOutputTypeDef(BaseModel):
    Application: ApplicationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePermissionOutputTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsOutputTypeDef(BaseModel):
    Applications: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListComponentsOutputTypeDef(BaseModel):
    Components: List[ComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDatabasesOutputTypeDef(BaseModel):
    Databases: List[DatabaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePermissionOutputTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterApplicationOutputTypeDef(BaseModel):
    Application: ApplicationTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartApplicationOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartApplicationRefreshOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopApplicationOutputTypeDef(BaseModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationSettingsOutputTypeDef(BaseModel):
    Message: str
    OperationIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListOperationEventsInputRequestTypeDef(BaseModel):
    OperationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListOperationsInputRequestTypeDef(BaseModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class GetOperationOutputTypeDef(BaseModel):
    Operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOperationsOutputTypeDef(BaseModel):
    Operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListApplicationsInputListApplicationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentsInputListComponentsPaginateTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatabasesInputListDatabasesPaginateTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationEventsInputListOperationEventsPaginateTypeDef(BaseModel):
    OperationId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationsInputListOperationsPaginateTypeDef(BaseModel):
    ApplicationId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class OperationEventTypeDef(BaseModel):
    Description: Optional[str] = None
    Resource: Optional[ResourceTypeDef] = None
    Status: Optional[OperationEventStatusType] = None
    StatusMessage: Optional[str] = None
    Timestamp: Optional[datetime] = None

class GetDatabaseOutputTypeDef(BaseModel):
    Database: DatabaseTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentTypeDef(BaseModel):
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
    Resilience: Optional[ResilienceTypeDef] = None
    AssociatedHost: Optional[AssociatedHostTypeDef] = None
    Databases: Optional[List[str]] = None
    Hosts: Optional[List[HostTypeDef]] = None
    PrimaryHost: Optional[str] = None
    DatabaseConnection: Optional[DatabaseConnectionTypeDef] = None
    LastUpdated: Optional[datetime] = None
    Arn: Optional[str] = None

class ListOperationEventsOutputTypeDef(BaseModel):
    OperationEvents: List[OperationEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetComponentOutputTypeDef(BaseModel):
    Component: ComponentTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


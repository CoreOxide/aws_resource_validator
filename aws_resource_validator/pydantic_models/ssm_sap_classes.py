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
from aws_resource_validator.pydantic_models.ssm_sap_constants import *

class ApplicationCredentialTypeDef(BaseValidatorModel):
    DatabaseName: str
    CredentialType: Literal["ADMIN"]
    SecretId: str

class ApplicationSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    DiscoveryStatus: Optional[ApplicationDiscoveryStatusType] = None
    Type: Optional[ApplicationTypeType] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ApplicationTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Type: Optional[ApplicationTypeType] = None
    Arn: Optional[str] = None
    AppRegistryArn: Optional[str] = None
    Status: Optional[ApplicationStatusType] = None
    DiscoveryStatus: Optional[ApplicationDiscoveryStatusType] = None
    Components: Optional[List[str]] = None
    LastUpdated: Optional[datetime] = None
    StatusMessage: Optional[str] = None

class IpAddressMemberTypeDef(BaseValidatorModel):
    IpAddress: Optional[str] = None
    Primary: Optional[bool] = None
    AllocationType: Optional[AllocationTypeType] = None

class BackintConfigTypeDef(BaseValidatorModel):
    BackintMode: Literal["AWSBackup"]
    EnsureNoBackupInProcess: bool

class ComponentSummaryTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    ComponentType: Optional[ComponentTypeType] = None
    Tags: Optional[Dict[str, str]] = None
    Arn: Optional[str] = None

class DatabaseConnectionTypeDef(BaseValidatorModel):
    DatabaseConnectionMethod: Optional[DatabaseConnectionMethodType] = None
    DatabaseArn: Optional[str] = None
    ConnectionIp: Optional[str] = None

class HostTypeDef(BaseValidatorModel):
    HostName: Optional[str] = None
    HostIp: Optional[str] = None
    EC2InstanceId: Optional[str] = None
    InstanceId: Optional[str] = None
    HostRole: Optional[HostRoleType] = None
    OsVersion: Optional[str] = None

class ResilienceTypeDef(BaseValidatorModel):
    HsrTier: Optional[str] = None
    HsrReplicationMode: Optional[ReplicationModeType] = None
    HsrOperationMode: Optional[OperationModeType] = None
    ClusterStatus: Optional[ClusterStatusType] = None
    EnqueueReplication: Optional[bool] = None

class DatabaseSummaryTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseType: Optional[DatabaseTypeType] = None
    Arn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class DeleteResourcePermissionInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ActionType: Optional[Literal["RESTORE"]] = None
    SourceResourceArn: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeregisterApplicationInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: str

class FilterTypeDef(BaseValidatorModel):
    Name: str
    Value: str
    Operator: FilterOperatorType

class GetApplicationInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ApplicationArn: Optional[str] = None
    AppRegistryArn: Optional[str] = None

class GetComponentInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ComponentId: str

class GetDatabaseInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    DatabaseId: Optional[str] = None
    DatabaseArn: Optional[str] = None

class GetOperationInputRequestTypeDef(BaseValidatorModel):
    OperationId: str

class OperationTypeDef(BaseValidatorModel):
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

class GetResourcePermissionInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ActionType: Optional[Literal["RESTORE"]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListComponentsInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDatabasesInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ResourceTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None

class PutResourcePermissionInputRequestTypeDef(BaseValidatorModel):
    ActionType: Literal["RESTORE"]
    SourceResourceArn: str
    ResourceArn: str

class StartApplicationInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: str

class StartApplicationRefreshInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: str

class StopApplicationInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    StopConnectedEntity: Optional[Literal["DBMS"]] = None
    IncludeEc2InstanceShutdown: Optional[bool] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class DatabaseTypeDef(BaseValidatorModel):
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

class RegisterApplicationInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    ApplicationType: ApplicationTypeType
    Instances: Sequence[str]
    SapInstanceNumber: Optional[str] = None
    Sid: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Credentials: Optional[Sequence[ApplicationCredentialTypeDef]] = None
    DatabaseArn: Optional[str] = None

class AssociatedHostTypeDef(BaseValidatorModel):
    Hostname: Optional[str] = None
    Ec2InstanceId: Optional[str] = None
    IpAddresses: Optional[List[IpAddressMemberTypeDef]] = None
    OsVersion: Optional[str] = None

class UpdateApplicationSettingsInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    CredentialsToAddOrUpdate: Optional[Sequence[ApplicationCredentialTypeDef]] = None
    CredentialsToRemove: Optional[Sequence[ApplicationCredentialTypeDef]] = None
    Backint: Optional[BackintConfigTypeDef] = None
    DatabaseArn: Optional[str] = None

class DeleteResourcePermissionOutputTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationOutputTypeDef(BaseValidatorModel):
    Application: ApplicationTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePermissionOutputTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsOutputTypeDef(BaseValidatorModel):
    Applications: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListComponentsOutputTypeDef(BaseValidatorModel):
    Components: List[ComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDatabasesOutputTypeDef(BaseValidatorModel):
    Databases: List[DatabaseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePermissionOutputTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterApplicationOutputTypeDef(BaseValidatorModel):
    Application: ApplicationTypeDef
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartApplicationOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartApplicationRefreshOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopApplicationOutputTypeDef(BaseValidatorModel):
    OperationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationSettingsOutputTypeDef(BaseValidatorModel):
    Message: str
    OperationIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListOperationEventsInputRequestTypeDef(BaseValidatorModel):
    OperationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class ListOperationsInputRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class GetOperationOutputTypeDef(BaseValidatorModel):
    Operation: OperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListOperationsOutputTypeDef(BaseValidatorModel):
    Operations: List[OperationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListApplicationsInputListApplicationsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentsInputListComponentsPaginateTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatabasesInputListDatabasesPaginateTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ComponentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationEventsInputListOperationEventsPaginateTypeDef(BaseValidatorModel):
    OperationId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOperationsInputListOperationsPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class OperationEventTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Resource: Optional[ResourceTypeDef] = None
    Status: Optional[OperationEventStatusType] = None
    StatusMessage: Optional[str] = None
    Timestamp: Optional[datetime] = None

class GetDatabaseOutputTypeDef(BaseValidatorModel):
    Database: DatabaseTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentTypeDef(BaseValidatorModel):
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

class ListOperationEventsOutputTypeDef(BaseValidatorModel):
    OperationEvents: List[OperationEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetComponentOutputTypeDef(BaseValidatorModel):
    Component: ComponentTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


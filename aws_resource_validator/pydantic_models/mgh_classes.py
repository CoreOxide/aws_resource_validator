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
from aws_resource_validator.pydantic_models.mgh_constants import *

class ApplicationStateTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    ApplicationStatus: Optional[ApplicationStatusType] = None
    LastUpdatedTime: Optional[datetime] = None

class CreatedArtifactTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None

class DiscoveredResourceTypeDef(BaseModel):
    ConfigurationId: str
    Description: Optional[str] = None

class CreateProgressUpdateStreamRequestRequestTypeDef(BaseModel):
    ProgressUpdateStreamName: str
    DryRun: Optional[bool] = None

class DeleteProgressUpdateStreamRequestRequestTypeDef(BaseModel):
    ProgressUpdateStreamName: str
    DryRun: Optional[bool] = None

class DescribeApplicationStateRequestRequestTypeDef(BaseModel):
    ApplicationId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeMigrationTaskRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str

class DisassociateCreatedArtifactRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifactName: str
    DryRun: Optional[bool] = None

class DisassociateDiscoveredResourceRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ConfigurationId: str
    DryRun: Optional[bool] = None

class ImportMigrationTaskRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DryRun: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationStatesRequestRequestTypeDef(BaseModel):
    ApplicationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCreatedArtifactsRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDiscoveredResourcesRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMigrationTasksRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceName: Optional[str] = None

class MigrationTaskSummaryTypeDef(BaseModel):
    ProgressUpdateStream: Optional[str] = None
    MigrationTaskName: Optional[str] = None
    Status: Optional[StatusType] = None
    ProgressPercent: Optional[int] = None
    StatusDetail: Optional[str] = None
    UpdateDateTime: Optional[datetime] = None

class ListProgressUpdateStreamsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProgressUpdateStreamSummaryTypeDef(BaseModel):
    ProgressUpdateStreamName: Optional[str] = None

class ResourceAttributeTypeDef(BaseModel):
    Type: ResourceAttributeTypeType
    Value: str

class TaskTypeDef(BaseModel):
    Status: StatusType
    StatusDetail: Optional[str] = None
    ProgressPercent: Optional[int] = None

class AssociateCreatedArtifactRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifact: CreatedArtifactTypeDef
    DryRun: Optional[bool] = None

class AssociateDiscoveredResourceRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DiscoveredResource: DiscoveredResourceTypeDef
    DryRun: Optional[bool] = None

class DescribeApplicationStateResultTypeDef(BaseModel):
    ApplicationStatus: ApplicationStatusType
    LastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationStatesResultTypeDef(BaseModel):
    ApplicationStateList: List[ApplicationStateTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCreatedArtifactsResultTypeDef(BaseModel):
    NextToken: str
    CreatedArtifactList: List[CreatedArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDiscoveredResourcesResultTypeDef(BaseModel):
    NextToken: str
    DiscoveredResourceList: List[DiscoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationStatesRequestListApplicationStatesPaginateTypeDef(BaseModel):
    ApplicationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMigrationTasksRequestListMigrationTasksPaginateTypeDef(BaseModel):
    ResourceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMigrationTasksResultTypeDef(BaseModel):
    NextToken: str
    MigrationTaskSummaryList: List[MigrationTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProgressUpdateStreamsResultTypeDef(BaseModel):
    ProgressUpdateStreamSummaryList: List[ProgressUpdateStreamSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourceAttributesRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ResourceAttributeList: Sequence[ResourceAttributeTypeDef]
    DryRun: Optional[bool] = None

class MigrationTaskTypeDef(BaseModel):
    ProgressUpdateStream: Optional[str] = None
    MigrationTaskName: Optional[str] = None
    Task: Optional[TaskTypeDef] = None
    UpdateDateTime: Optional[datetime] = None
    ResourceAttributeList: Optional[List[ResourceAttributeTypeDef]] = None

class NotifyApplicationStateRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    Status: ApplicationStatusType
    UpdateDateTime: Optional[TimestampTypeDef] = None
    DryRun: Optional[bool] = None

class NotifyMigrationTaskStateRequestRequestTypeDef(BaseModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    Task: TaskTypeDef
    UpdateDateTime: TimestampTypeDef
    NextUpdateSeconds: int
    DryRun: Optional[bool] = None

class DescribeMigrationTaskResultTypeDef(BaseModel):
    MigrationTask: MigrationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


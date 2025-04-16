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
from aws_resource_validator.pydantic_models.mgh_constants import *

class ApplicationState(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ApplicationStatus: Optional[ApplicationStatusType] = None
    LastUpdatedTime: Optional[datetime] = None


class CreatedArtifact(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None


class DiscoveredResource(BaseValidatorModel):
    ConfigurationId: str
    Description: Optional[str] = None


class SourceResource(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    StatusDetail: Optional[str] = None


class CreateProgressUpdateStreamRequest(BaseValidatorModel):
    ProgressUpdateStreamName: str
    DryRun: Optional[bool] = None


class DeleteProgressUpdateStreamRequest(BaseValidatorModel):
    ProgressUpdateStreamName: str
    DryRun: Optional[bool] = None


class DescribeApplicationStateRequest(BaseValidatorModel):
    ApplicationId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeMigrationTaskRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str


class DisassociateCreatedArtifactRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifactName: str
    DryRun: Optional[bool] = None


class DisassociateDiscoveredResourceRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ConfigurationId: str
    DryRun: Optional[bool] = None


class DisassociateSourceResourceRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    SourceResourceName: str
    DryRun: Optional[bool] = None


class ImportMigrationTaskRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DryRun: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationStatesRequest(BaseValidatorModel):
    ApplicationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCreatedArtifactsRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDiscoveredResourcesRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMigrationTaskUpdatesRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMigrationTasksRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceName: Optional[str] = None


class MigrationTaskSummary(BaseValidatorModel):
    ProgressUpdateStream: Optional[str] = None
    MigrationTaskName: Optional[str] = None
    Status: Optional[StatusType] = None
    ProgressPercent: Optional[int] = None
    StatusDetail: Optional[str] = None
    UpdateDateTime: Optional[datetime] = None


class ListProgressUpdateStreamsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProgressUpdateStreamSummary(BaseValidatorModel):
    ProgressUpdateStreamName: Optional[str] = None


class ListSourceResourcesRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class Task(BaseValidatorModel):
    Status: StatusType
    StatusDetail: Optional[str] = None
    ProgressPercent: Optional[int] = None


class AssociateCreatedArtifactRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifact: CreatedArtifact
    DryRun: Optional[bool] = None


class AssociateDiscoveredResourceRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DiscoveredResource: DiscoveredResource
    DryRun: Optional[bool] = None


class AssociateSourceResourceRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    SourceResource: SourceResource
    DryRun: Optional[bool] = None


class DescribeApplicationStateResult(BaseValidatorModel):
    ApplicationStatus: ApplicationStatusType
    LastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadata


class ListApplicationStatesResult(BaseValidatorModel):
    ApplicationStateList: List[ApplicationState]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCreatedArtifactsResult(BaseValidatorModel):
    CreatedArtifactList: List[CreatedArtifact]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDiscoveredResourcesResult(BaseValidatorModel):
    DiscoveredResourceList: List[DiscoveredResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSourceResourcesResult(BaseValidatorModel):
    SourceResourceList: List[SourceResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationStatesRequestPaginate(BaseValidatorModel):
    ApplicationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCreatedArtifactsRequestPaginate(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDiscoveredResourcesRequestPaginate(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMigrationTaskUpdatesRequestPaginate(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMigrationTasksRequestPaginate(BaseValidatorModel):
    ResourceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProgressUpdateStreamsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSourceResourcesRequestPaginate(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMigrationTasksResult(BaseValidatorModel):
    MigrationTaskSummaryList: List[MigrationTaskSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListProgressUpdateStreamsResult(BaseValidatorModel):
    ProgressUpdateStreamSummaryList: List[ProgressUpdateStreamSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResourceAttribute(BaseValidatorModel):
    pass


class PutResourceAttributesRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ResourceAttributeList: Sequence[ResourceAttribute]
    DryRun: Optional[bool] = None


class MigrationTask(BaseValidatorModel):
    ProgressUpdateStream: Optional[str] = None
    MigrationTaskName: Optional[str] = None
    Task: Optional[Task] = None
    UpdateDateTime: Optional[datetime] = None
    ResourceAttributeList: Optional[List[ResourceAttribute]] = None


class MigrationTaskUpdate(BaseValidatorModel):
    UpdateDateTime: Optional[datetime] = None
    UpdateType: Optional[Literal["MIGRATION_TASK_STATE_UPDATED"]] = None
    MigrationTaskState: Optional[Task] = None


class Timestamp(BaseValidatorModel):
    pass


class NotifyApplicationStateRequest(BaseValidatorModel):
    ApplicationId: str
    Status: ApplicationStatusType
    UpdateDateTime: Optional[Timestamp] = None
    DryRun: Optional[bool] = None


class NotifyMigrationTaskStateRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    Task: Task
    UpdateDateTime: Timestamp
    NextUpdateSeconds: int
    DryRun: Optional[bool] = None


class DescribeMigrationTaskResult(BaseValidatorModel):
    MigrationTask: MigrationTask
    ResponseMetadata: ResponseMetadata


class ListMigrationTaskUpdatesResult(BaseValidatorModel):
    MigrationTaskUpdateList: List[MigrationTaskUpdate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None



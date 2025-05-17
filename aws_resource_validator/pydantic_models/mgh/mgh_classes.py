from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.mgh.mgh_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'describe_application_state' function.
class DescribeApplicationStateRequest(BaseValidatorModel):
    ApplicationId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'describe_migration_task' function.
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


# This class is the input for the 'list_application_states' function.
class ListApplicationStatesRequest(BaseValidatorModel):
    ApplicationIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_created_artifacts' function.
class ListCreatedArtifactsRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_discovered_resources' function.
class ListDiscoveredResourcesRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_migration_task_updates' function.
class ListMigrationTaskUpdatesRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_migration_tasks' function.
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


# This class is the input for the 'list_progress_update_streams' function.
class ListProgressUpdateStreamsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProgressUpdateStreamSummary(BaseValidatorModel):
    ProgressUpdateStreamName: Optional[str] = None


# This class is the input for the 'list_source_resources' function.
class ListSourceResourcesRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ResourceAttribute(BaseValidatorModel):
    Type: ResourceAttributeTypeType
    Value: str


class Task(BaseValidatorModel):
    Status: StatusType
    StatusDetail: Optional[str] = None
    ProgressPercent: Optional[int] = None

Timestamp = Union[datetime, str]


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


# This class is the output for the 'describe_application_state' function.
class DescribeApplicationStateResult(BaseValidatorModel):
    ApplicationStatus: ApplicationStatusType
    LastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_application_states' function.
class ListApplicationStatesResult(BaseValidatorModel):
    ApplicationStateList: List[ApplicationState]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_created_artifacts' function.
class ListCreatedArtifactsResult(BaseValidatorModel):
    CreatedArtifactList: List[CreatedArtifact]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_discovered_resources' function.
class ListDiscoveredResourcesResult(BaseValidatorModel):
    DiscoveredResourceList: List[DiscoveredResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_source_resources' function.
class ListSourceResourcesResult(BaseValidatorModel):
    SourceResourceList: List[SourceResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationStatesRequestPaginate(BaseValidatorModel):
    ApplicationIds: Optional[List[str]] = None
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


# This class is the output for the 'list_migration_tasks' function.
class ListMigrationTasksResult(BaseValidatorModel):
    MigrationTaskSummaryList: List[MigrationTaskSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_progress_update_streams' function.
class ListProgressUpdateStreamsResult(BaseValidatorModel):
    ProgressUpdateStreamSummaryList: List[ProgressUpdateStreamSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutResourceAttributesRequest(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ResourceAttributeList: List[ResourceAttribute]
    DryRun: Optional[bool] = None


class MigrationTask(BaseValidatorModel):
    ProgressUpdateStream: Optional[str] = None
    MigrationTaskName: Optional[str] = None
    Task: Optional[Task] = None
    UpdateDateTime: Optional[datetime] = None
    ResourceAttributeList: Optional[List[ResourceAttribute]] = None


class MigrationTaskUpdate(BaseValidatorModel):
    UpdateDateTime: Optional[datetime] = None
    UpdateType: Optional[Literal['MIGRATION_TASK_STATE_UPDATED']] = None
    MigrationTaskState: Optional[Task] = None


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


# This class is the output for the 'describe_migration_task' function.
class DescribeMigrationTaskResult(BaseValidatorModel):
    MigrationTask: MigrationTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_migration_task_updates' function.
class ListMigrationTaskUpdatesResult(BaseValidatorModel):
    MigrationTaskUpdateList: List[MigrationTaskUpdate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
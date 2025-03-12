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

class ApplicationStateTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    ApplicationStatus: Optional[ApplicationStatusType] = None
    LastUpdatedTime: Optional[datetime] = None


class CreatedArtifactTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None


class DiscoveredResourceTypeDef(BaseValidatorModel):
    ConfigurationId: str
    Description: Optional[str] = None


class SourceResourceTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    StatusDetail: Optional[str] = None


class CreateProgressUpdateStreamRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStreamName: str
    DryRun: Optional[bool] = None


class DeleteProgressUpdateStreamRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStreamName: str
    DryRun: Optional[bool] = None


class DescribeApplicationStateRequestTypeDef(BaseValidatorModel):
    ApplicationId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DescribeMigrationTaskRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str


class DisassociateCreatedArtifactRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifactName: str
    DryRun: Optional[bool] = None


class DisassociateDiscoveredResourceRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ConfigurationId: str
    DryRun: Optional[bool] = None


class DisassociateSourceResourceRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    SourceResourceName: str
    DryRun: Optional[bool] = None


class ImportMigrationTaskRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DryRun: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationStatesRequestTypeDef(BaseValidatorModel):
    ApplicationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListCreatedArtifactsRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDiscoveredResourcesRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMigrationTaskUpdatesRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMigrationTasksRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceName: Optional[str] = None


class MigrationTaskSummaryTypeDef(BaseValidatorModel):
    ProgressUpdateStream: Optional[str] = None
    MigrationTaskName: Optional[str] = None
    Status: Optional[StatusType] = None
    ProgressPercent: Optional[int] = None
    StatusDetail: Optional[str] = None
    UpdateDateTime: Optional[datetime] = None


class ListProgressUpdateStreamsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ProgressUpdateStreamSummaryTypeDef(BaseValidatorModel):
    ProgressUpdateStreamName: Optional[str] = None


class ListSourceResourcesRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class TaskTypeDef(BaseValidatorModel):
    Status: StatusType
    StatusDetail: Optional[str] = None
    ProgressPercent: Optional[int] = None


class AssociateCreatedArtifactRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifact: CreatedArtifactTypeDef
    DryRun: Optional[bool] = None


class AssociateDiscoveredResourceRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DiscoveredResource: DiscoveredResourceTypeDef
    DryRun: Optional[bool] = None


class AssociateSourceResourceRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    SourceResource: SourceResourceTypeDef
    DryRun: Optional[bool] = None


class DescribeApplicationStateResultTypeDef(BaseValidatorModel):
    ApplicationStatus: ApplicationStatusType
    LastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ListApplicationStatesResultTypeDef(BaseValidatorModel):
    ApplicationStateList: List[ApplicationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCreatedArtifactsResultTypeDef(BaseValidatorModel):
    CreatedArtifactList: List[CreatedArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDiscoveredResourcesResultTypeDef(BaseValidatorModel):
    DiscoveredResourceList: List[DiscoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSourceResourcesResultTypeDef(BaseValidatorModel):
    SourceResourceList: List[SourceResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListApplicationStatesRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCreatedArtifactsRequestPaginateTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDiscoveredResourcesRequestPaginateTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMigrationTaskUpdatesRequestPaginateTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMigrationTasksRequestPaginateTypeDef(BaseValidatorModel):
    ResourceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProgressUpdateStreamsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSourceResourcesRequestPaginateTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMigrationTasksResultTypeDef(BaseValidatorModel):
    MigrationTaskSummaryList: List[MigrationTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListProgressUpdateStreamsResultTypeDef(BaseValidatorModel):
    ProgressUpdateStreamSummaryList: List[ProgressUpdateStreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResourceAttributeTypeDef(BaseValidatorModel):
    pass


class PutResourceAttributesRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ResourceAttributeList: Sequence[ResourceAttributeTypeDef]
    DryRun: Optional[bool] = None


class MigrationTaskTypeDef(BaseValidatorModel):
    ProgressUpdateStream: Optional[str] = None
    MigrationTaskName: Optional[str] = None
    Task: Optional[TaskTypeDef] = None
    UpdateDateTime: Optional[datetime] = None
    ResourceAttributeList: Optional[List[ResourceAttributeTypeDef]] = None


class MigrationTaskUpdateTypeDef(BaseValidatorModel):
    UpdateDateTime: Optional[datetime] = None
    UpdateType: Optional[Literal["MIGRATION_TASK_STATE_UPDATED"]] = None
    MigrationTaskState: Optional[TaskTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class NotifyApplicationStateRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    Status: ApplicationStatusType
    UpdateDateTime: Optional[TimestampTypeDef] = None
    DryRun: Optional[bool] = None


class NotifyMigrationTaskStateRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    Task: TaskTypeDef
    UpdateDateTime: TimestampTypeDef
    NextUpdateSeconds: int
    DryRun: Optional[bool] = None


class DescribeMigrationTaskResultTypeDef(BaseValidatorModel):
    MigrationTask: MigrationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListMigrationTaskUpdatesResultTypeDef(BaseValidatorModel):
    MigrationTaskUpdateList: List[MigrationTaskUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None



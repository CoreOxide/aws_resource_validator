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

class CreateProgressUpdateStreamRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStreamName: str
    DryRun: Optional[bool] = None

class DeleteProgressUpdateStreamRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStreamName: str
    DryRun: Optional[bool] = None

class DescribeApplicationStateRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DescribeMigrationTaskRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str

class DisassociateCreatedArtifactRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifactName: str
    DryRun: Optional[bool] = None

class DisassociateDiscoveredResourceRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    ConfigurationId: str
    DryRun: Optional[bool] = None

class ImportMigrationTaskRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DryRun: Optional[bool] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationStatesRequestRequestTypeDef(BaseValidatorModel):
    ApplicationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListCreatedArtifactsRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDiscoveredResourcesRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMigrationTasksRequestRequestTypeDef(BaseValidatorModel):
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

class ListProgressUpdateStreamsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ProgressUpdateStreamSummaryTypeDef(BaseValidatorModel):
    ProgressUpdateStreamName: Optional[str] = None

class ResourceAttributeTypeDef(BaseValidatorModel):
    Type: ResourceAttributeTypeType
    Value: str

class TaskTypeDef(BaseValidatorModel):
    Status: StatusType
    StatusDetail: Optional[str] = None
    ProgressPercent: Optional[int] = None

class AssociateCreatedArtifactRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    CreatedArtifact: CreatedArtifactTypeDef
    DryRun: Optional[bool] = None

class AssociateDiscoveredResourceRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    DiscoveredResource: DiscoveredResourceTypeDef
    DryRun: Optional[bool] = None

class DescribeApplicationStateResultTypeDef(BaseValidatorModel):
    ApplicationStatus: ApplicationStatusType
    LastUpdatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationStatesResultTypeDef(BaseValidatorModel):
    ApplicationStateList: List[ApplicationStateTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCreatedArtifactsResultTypeDef(BaseValidatorModel):
    NextToken: str
    CreatedArtifactList: List[CreatedArtifactTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDiscoveredResourcesResultTypeDef(BaseValidatorModel):
    NextToken: str
    DiscoveredResourceList: List[DiscoveredResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationStatesRequestListApplicationStatesPaginateTypeDef(BaseValidatorModel):
    ApplicationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCreatedArtifactsRequestListCreatedArtifactsPaginateTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDiscoveredResourcesRequestListDiscoveredResourcesPaginateTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMigrationTasksRequestListMigrationTasksPaginateTypeDef(BaseValidatorModel):
    ResourceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProgressUpdateStreamsRequestListProgressUpdateStreamsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMigrationTasksResultTypeDef(BaseValidatorModel):
    NextToken: str
    MigrationTaskSummaryList: List[MigrationTaskSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProgressUpdateStreamsResultTypeDef(BaseValidatorModel):
    ProgressUpdateStreamSummaryList: List[ProgressUpdateStreamSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourceAttributesRequestRequestTypeDef(BaseValidatorModel):
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

class NotifyApplicationStateRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    Status: ApplicationStatusType
    UpdateDateTime: Optional[TimestampTypeDef] = None
    DryRun: Optional[bool] = None

class NotifyMigrationTaskStateRequestRequestTypeDef(BaseValidatorModel):
    ProgressUpdateStream: str
    MigrationTaskName: str
    Task: TaskTypeDef
    UpdateDateTime: TimestampTypeDef
    NextUpdateSeconds: int
    DryRun: Optional[bool] = None

class DescribeMigrationTaskResultTypeDef(BaseValidatorModel):
    MigrationTask: MigrationTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


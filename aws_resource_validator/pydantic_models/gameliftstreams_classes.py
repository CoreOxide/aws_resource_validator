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
from aws_resource_validator.pydantic_models.gameliftstreams_constants import *

class LocationConfiguration(BaseValidatorModel):
    LocationName: str
    AlwaysOnCapacity: Optional[int] = None
    OnDemandCapacity: Optional[int] = None


class LocationState(BaseValidatorModel):
    AllocatedCapacity: Optional[int] = None
    AlwaysOnCapacity: Optional[int] = None
    IdleCapacity: Optional[int] = None
    LocationName: Optional[str] = None
    OnDemandCapacity: Optional[int] = None
    RequestedCapacity: Optional[int] = None
    Status: Optional[StreamGroupLocationStatusType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateApplicationsInput(BaseValidatorModel):
    ApplicationIdentifiers: Sequence[str]
    Identifier: str


class ReplicationStatus(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[ReplicationStatusTypeType] = None


class DefaultApplication(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None


class CreateStreamSessionConnectionInput(BaseValidatorModel):
    Identifier: str
    SignalRequest: str
    StreamSessionIdentifier: str
    ClientToken: Optional[str] = None


class DeleteApplicationInput(BaseValidatorModel):
    Identifier: str


class DeleteStreamGroupInput(BaseValidatorModel):
    Identifier: str


class DisassociateApplicationsInput(BaseValidatorModel):
    ApplicationIdentifiers: Sequence[str]
    Identifier: str


class ExportFilesMetadata(BaseValidatorModel):
    OutputUri: Optional[str] = None
    Status: Optional[ExportFilesStatusType] = None
    StatusReason: Optional[str] = None


class ExportStreamSessionFilesInput(BaseValidatorModel):
    Identifier: str
    OutputUri: str
    StreamSessionIdentifier: str


class GetApplicationInput(BaseValidatorModel):
    Identifier: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetStreamGroupInput(BaseValidatorModel):
    Identifier: str


class GetStreamSessionInput(BaseValidatorModel):
    Identifier: str
    StreamSessionIdentifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListStreamGroupsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListStreamSessionsByAccountInput(BaseValidatorModel):
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[StreamSessionStatusType] = None


class ListStreamSessionsInput(BaseValidatorModel):
    Identifier: str
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[StreamSessionStatusType] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class RemoveStreamGroupLocationsInput(BaseValidatorModel):
    Identifier: str
    Locations: Sequence[str]


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class TerminateStreamSessionInput(BaseValidatorModel):
    Identifier: str
    StreamSessionIdentifier: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateApplicationInput(BaseValidatorModel):
    Identifier: str
    ApplicationLogOutputUri: Optional[str] = None
    ApplicationLogPaths: Optional[Sequence[str]] = None
    Description: Optional[str] = None


class AddStreamGroupLocationsInput(BaseValidatorModel):
    Identifier: str
    LocationConfigurations: Sequence[LocationConfiguration]


class CreateStreamGroupInput(BaseValidatorModel):
    Description: str
    StreamClass: StreamClassType
    ClientToken: Optional[str] = None
    DefaultApplicationIdentifier: Optional[str] = None
    LocationConfigurations: Optional[Sequence[LocationConfiguration]] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateStreamGroupInput(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None
    LocationConfigurations: Optional[Sequence[LocationConfiguration]] = None


class AddStreamGroupLocationsOutput(BaseValidatorModel):
    Identifier: str
    Locations: List[LocationState]
    ResponseMetadata: ResponseMetadata


class AssociateApplicationsOutput(BaseValidatorModel):
    ApplicationArns: List[str]
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateStreamSessionConnectionOutput(BaseValidatorModel):
    SignalResponse: str
    ResponseMetadata: ResponseMetadata


class DisassociateApplicationsOutput(BaseValidatorModel):
    ApplicationArns: List[str]
    Arn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RuntimeEnvironment(BaseValidatorModel):
    pass


class ApplicationSummary(BaseValidatorModel):
    Arn: str
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedAt: Optional[datetime] = None
    RuntimeEnvironment: Optional[RuntimeEnvironment] = None
    Status: Optional[ApplicationStatusType] = None


class CreateApplicationInput(BaseValidatorModel):
    ApplicationSourceUri: str
    Description: str
    ExecutablePath: str
    RuntimeEnvironment: RuntimeEnvironment
    ApplicationLogOutputUri: Optional[str] = None
    ApplicationLogPaths: Optional[Sequence[str]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateApplicationOutput(BaseValidatorModel):
    ApplicationLogOutputUri: str
    ApplicationLogPaths: List[str]
    ApplicationSourceUri: str
    Arn: str
    AssociatedStreamGroups: List[str]
    CreatedAt: datetime
    Description: str
    ExecutablePath: str
    Id: str
    LastUpdatedAt: datetime
    ReplicationStatuses: List[ReplicationStatus]
    RuntimeEnvironment: RuntimeEnvironment
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadata


class GetApplicationOutput(BaseValidatorModel):
    ApplicationLogOutputUri: str
    ApplicationLogPaths: List[str]
    ApplicationSourceUri: str
    Arn: str
    AssociatedStreamGroups: List[str]
    CreatedAt: datetime
    Description: str
    ExecutablePath: str
    Id: str
    LastUpdatedAt: datetime
    ReplicationStatuses: List[ReplicationStatus]
    RuntimeEnvironment: RuntimeEnvironment
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadata


class UpdateApplicationOutput(BaseValidatorModel):
    ApplicationLogOutputUri: str
    ApplicationLogPaths: List[str]
    ApplicationSourceUri: str
    Arn: str
    AssociatedStreamGroups: List[str]
    CreatedAt: datetime
    Description: str
    ExecutablePath: str
    Id: str
    LastUpdatedAt: datetime
    ReplicationStatuses: List[ReplicationStatus]
    RuntimeEnvironment: RuntimeEnvironment
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadata


class CreateStreamGroupOutput(BaseValidatorModel):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplication
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationState]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadata


class GetStreamGroupOutput(BaseValidatorModel):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplication
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationState]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadata


class StreamGroupSummary(BaseValidatorModel):
    Arn: str
    CreatedAt: Optional[datetime] = None
    DefaultApplication: Optional[DefaultApplication] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedAt: Optional[datetime] = None
    Status: Optional[StreamGroupStatusType] = None
    StreamClass: Optional[StreamClassType] = None


class UpdateStreamGroupOutput(BaseValidatorModel):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplication
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationState]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadata


class GetApplicationInputWaitExtra(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetApplicationInputWait(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetStreamGroupInputWaitExtra(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetStreamGroupInputWait(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class GetStreamSessionInputWait(BaseValidatorModel):
    Identifier: str
    StreamSessionIdentifier: str
    WaiterConfig: Optional[WaiterConfig] = None


class ListApplicationsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamGroupsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamSessionsByAccountInputPaginate(BaseValidatorModel):
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    Status: Optional[StreamSessionStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamSessionsInputPaginate(BaseValidatorModel):
    Identifier: str
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    Status: Optional[StreamSessionStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationsOutput(BaseValidatorModel):
    Items: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStreamGroupsOutput(BaseValidatorModel):
    Items: List[StreamGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StreamSessionSummary(BaseValidatorModel):
    pass


class ListStreamSessionsByAccountOutput(BaseValidatorModel):
    Items: List[StreamSessionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListStreamSessionsOutput(BaseValidatorModel):
    Items: List[StreamSessionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None



from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.gameliftstreams.gameliftstreams_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


class RuntimeEnvironment(BaseValidatorModel):
    Type: RuntimeEnvironmentTypeType
    Version: str


# This class is the input for the 'associate_applications' function.
class AssociateApplicationsInput(BaseValidatorModel):
    ApplicationIdentifiers: List[str]
    Identifier: str


class ReplicationStatus(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[ReplicationStatusTypeType] = None


class DefaultApplication(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None


# This class is the input for the 'create_stream_session_connection' function.
class CreateStreamSessionConnectionInput(BaseValidatorModel):
    Identifier: str
    SignalRequest: str
    StreamSessionIdentifier: str
    ClientToken: Optional[str] = None


# This class is the input for the 'delete_application' function.
class DeleteApplicationInput(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'delete_stream_group' function.
class DeleteStreamGroupInput(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'disassociate_applications' function.
class DisassociateApplicationsInput(BaseValidatorModel):
    ApplicationIdentifiers: List[str]
    Identifier: str


class ExportFilesMetadata(BaseValidatorModel):
    OutputUri: Optional[str] = None
    Status: Optional[ExportFilesStatusType] = None
    StatusReason: Optional[str] = None


class ExportStreamSessionFilesInput(BaseValidatorModel):
    Identifier: str
    OutputUri: str
    StreamSessionIdentifier: str


# This class is the input for the 'get_application' function.
class GetApplicationInput(BaseValidatorModel):
    Identifier: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'get_stream_group' function.
class GetStreamGroupInput(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_stream_session' function.
class GetStreamSessionInput(BaseValidatorModel):
    Identifier: str
    StreamSessionIdentifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_stream_groups' function.
class ListStreamGroupsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_stream_sessions_by_account' function.
class ListStreamSessionsByAccountInput(BaseValidatorModel):
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[StreamSessionStatusType] = None


# This class is the input for the 'list_stream_sessions' function.
class ListStreamSessionsInput(BaseValidatorModel):
    Identifier: str
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[StreamSessionStatusType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'remove_stream_group_locations' function.
class RemoveStreamGroupLocationsInput(BaseValidatorModel):
    Identifier: str
    Locations: List[str]


# This class is the input for the 'start_stream_session' function.
class StartStreamSessionInput(BaseValidatorModel):
    ApplicationIdentifier: str
    Identifier: str
    Protocol: Literal['WebRTC']
    SignalRequest: str
    AdditionalEnvironmentVariables: Optional[Dict[str, str]] = None
    AdditionalLaunchArgs: Optional[List[str]] = None
    ClientToken: Optional[str] = None
    ConnectionTimeoutSeconds: Optional[int] = None
    Description: Optional[str] = None
    Locations: Optional[List[str]] = None
    SessionLengthSeconds: Optional[int] = None
    UserId: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


# This class is the input for the 'terminate_stream_session' function.
class TerminateStreamSessionInput(BaseValidatorModel):
    Identifier: str
    StreamSessionIdentifier: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_application' function.
class UpdateApplicationInput(BaseValidatorModel):
    Identifier: str
    ApplicationLogOutputUri: Optional[str] = None
    ApplicationLogPaths: Optional[List[str]] = None
    Description: Optional[str] = None


# This class is the input for the 'add_stream_group_locations' function.
class AddStreamGroupLocationsInput(BaseValidatorModel):
    Identifier: str
    LocationConfigurations: List[LocationConfiguration]


# This class is the input for the 'create_stream_group' function.
class CreateStreamGroupInput(BaseValidatorModel):
    Description: str
    StreamClass: StreamClassType
    ClientToken: Optional[str] = None
    DefaultApplicationIdentifier: Optional[str] = None
    LocationConfigurations: Optional[List[LocationConfiguration]] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_stream_group' function.
class UpdateStreamGroupInput(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None
    LocationConfigurations: Optional[List[LocationConfiguration]] = None


# This class is the output for the 'add_stream_group_locations' function.
class AddStreamGroupLocationsOutput(BaseValidatorModel):
    Identifier: str
    Locations: List[LocationState]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_applications' function.
class AssociateApplicationsOutput(BaseValidatorModel):
    ApplicationArns: List[str]
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_stream_session_connection' function.
class CreateStreamSessionConnectionOutput(BaseValidatorModel):
    SignalResponse: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_applications' function.
class DisassociateApplicationsOutput(BaseValidatorModel):
    ApplicationArns: List[str]
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'terminate_stream_session' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ApplicationSummary(BaseValidatorModel):
    Arn: str
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedAt: Optional[datetime] = None
    RuntimeEnvironment: Optional[RuntimeEnvironment] = None
    Status: Optional[ApplicationStatusType] = None


# This class is the input for the 'create_application' function.
class CreateApplicationInput(BaseValidatorModel):
    ApplicationSourceUri: str
    Description: str
    ExecutablePath: str
    RuntimeEnvironment: RuntimeEnvironment
    ApplicationLogOutputUri: Optional[str] = None
    ApplicationLogPaths: Optional[List[str]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_application' function.
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


# This class is the output for the 'get_application' function.
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


# This class is the output for the 'update_application' function.
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


# This class is the output for the 'create_stream_group' function.
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


# This class is the output for the 'get_stream_group' function.
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


# This class is the output for the 'update_stream_group' function.
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


# This class is the output for the 'get_stream_session' function.
class GetStreamSessionOutput(BaseValidatorModel):
    AdditionalEnvironmentVariables: Dict[str, str]
    AdditionalLaunchArgs: List[str]
    ApplicationArn: str
    Arn: str
    ConnectionTimeoutSeconds: int
    CreatedAt: datetime
    Description: str
    ExportFilesMetadata: ExportFilesMetadata
    LastUpdatedAt: datetime
    Location: str
    LogFileLocationUri: str
    Protocol: Literal['WebRTC']
    SessionLengthSeconds: int
    SignalRequest: str
    SignalResponse: str
    Status: StreamSessionStatusType
    StatusReason: StreamSessionStatusReasonType
    StreamGroupId: str
    UserId: str
    WebSdkProtocolUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_stream_session' function.
class StartStreamSessionOutput(BaseValidatorModel):
    AdditionalEnvironmentVariables: Dict[str, str]
    AdditionalLaunchArgs: List[str]
    ApplicationArn: str
    Arn: str
    ConnectionTimeoutSeconds: int
    CreatedAt: datetime
    Description: str
    ExportFilesMetadata: ExportFilesMetadata
    LastUpdatedAt: datetime
    Location: str
    LogFileLocationUri: str
    Protocol: Literal['WebRTC']
    SessionLengthSeconds: int
    SignalRequest: str
    SignalResponse: str
    Status: StreamSessionStatusType
    StatusReason: StreamSessionStatusReasonType
    StreamGroupId: str
    UserId: str
    WebSdkProtocolUrl: str
    ResponseMetadata: ResponseMetadata


class StreamSessionSummary(BaseValidatorModel):
    ApplicationArn: Optional[str] = None
    Arn: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ExportFilesMetadata: Optional[ExportFilesMetadata] = None
    LastUpdatedAt: Optional[datetime] = None
    Location: Optional[str] = None
    Protocol: Optional[Literal['WebRTC']] = None
    Status: Optional[StreamSessionStatusType] = None
    UserId: Optional[str] = None


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


# This class is the output for the 'list_applications' function.
class ListApplicationsOutput(BaseValidatorModel):
    Items: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_stream_groups' function.
class ListStreamGroupsOutput(BaseValidatorModel):
    Items: List[StreamGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_stream_sessions_by_account' function.
class ListStreamSessionsByAccountOutput(BaseValidatorModel):
    Items: List[StreamSessionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_stream_sessions' function.
class ListStreamSessionsOutput(BaseValidatorModel):
    Items: List[StreamSessionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
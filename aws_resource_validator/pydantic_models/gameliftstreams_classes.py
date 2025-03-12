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

class LocationConfigurationTypeDef(BaseValidatorModel):
    LocationName: str
    AlwaysOnCapacity: Optional[int] = None
    OnDemandCapacity: Optional[int] = None


class LocationStateTypeDef(BaseValidatorModel):
    AllocatedCapacity: Optional[int] = None
    AlwaysOnCapacity: Optional[int] = None
    IdleCapacity: Optional[int] = None
    LocationName: Optional[str] = None
    OnDemandCapacity: Optional[int] = None
    RequestedCapacity: Optional[int] = None
    Status: Optional[StreamGroupLocationStatusType] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateApplicationsInputTypeDef(BaseValidatorModel):
    ApplicationIdentifiers: Sequence[str]
    Identifier: str


class ReplicationStatusTypeDef(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[ReplicationStatusTypeType] = None


class DefaultApplicationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None


class CreateStreamSessionConnectionInputTypeDef(BaseValidatorModel):
    Identifier: str
    SignalRequest: str
    StreamSessionIdentifier: str
    ClientToken: Optional[str] = None


class DeleteApplicationInputTypeDef(BaseValidatorModel):
    Identifier: str


class DeleteStreamGroupInputTypeDef(BaseValidatorModel):
    Identifier: str


class DisassociateApplicationsInputTypeDef(BaseValidatorModel):
    ApplicationIdentifiers: Sequence[str]
    Identifier: str


class ExportFilesMetadataTypeDef(BaseValidatorModel):
    OutputUri: Optional[str] = None
    Status: Optional[ExportFilesStatusType] = None
    StatusReason: Optional[str] = None


class ExportStreamSessionFilesInputTypeDef(BaseValidatorModel):
    Identifier: str
    OutputUri: str
    StreamSessionIdentifier: str


class GetApplicationInputTypeDef(BaseValidatorModel):
    Identifier: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class GetStreamGroupInputTypeDef(BaseValidatorModel):
    Identifier: str


class GetStreamSessionInputTypeDef(BaseValidatorModel):
    Identifier: str
    StreamSessionIdentifier: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListStreamGroupsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListStreamSessionsByAccountInputTypeDef(BaseValidatorModel):
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[StreamSessionStatusType] = None


class ListStreamSessionsInputTypeDef(BaseValidatorModel):
    Identifier: str
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Status: Optional[StreamSessionStatusType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class RemoveStreamGroupLocationsInputTypeDef(BaseValidatorModel):
    Identifier: str
    Locations: Sequence[str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class TerminateStreamSessionInputTypeDef(BaseValidatorModel):
    Identifier: str
    StreamSessionIdentifier: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateApplicationInputTypeDef(BaseValidatorModel):
    Identifier: str
    ApplicationLogOutputUri: Optional[str] = None
    ApplicationLogPaths: Optional[Sequence[str]] = None
    Description: Optional[str] = None


class AddStreamGroupLocationsInputTypeDef(BaseValidatorModel):
    Identifier: str
    LocationConfigurations: Sequence[LocationConfigurationTypeDef]


class CreateStreamGroupInputTypeDef(BaseValidatorModel):
    Description: str
    StreamClass: StreamClassType
    ClientToken: Optional[str] = None
    DefaultApplicationIdentifier: Optional[str] = None
    LocationConfigurations: Optional[Sequence[LocationConfigurationTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateStreamGroupInputTypeDef(BaseValidatorModel):
    Identifier: str
    Description: Optional[str] = None
    LocationConfigurations: Optional[Sequence[LocationConfigurationTypeDef]] = None


class AddStreamGroupLocationsOutputTypeDef(BaseValidatorModel):
    Identifier: str
    Locations: List[LocationStateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateApplicationsOutputTypeDef(BaseValidatorModel):
    ApplicationArns: List[str]
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStreamSessionConnectionOutputTypeDef(BaseValidatorModel):
    SignalResponse: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateApplicationsOutputTypeDef(BaseValidatorModel):
    ApplicationArns: List[str]
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class RuntimeEnvironmentTypeDef(BaseValidatorModel):
    pass


class ApplicationSummaryTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: Optional[datetime] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedAt: Optional[datetime] = None
    RuntimeEnvironment: Optional[RuntimeEnvironmentTypeDef] = None
    Status: Optional[ApplicationStatusType] = None


class CreateApplicationInputTypeDef(BaseValidatorModel):
    ApplicationSourceUri: str
    Description: str
    ExecutablePath: str
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    ApplicationLogOutputUri: Optional[str] = None
    ApplicationLogPaths: Optional[Sequence[str]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateApplicationOutputTypeDef(BaseValidatorModel):
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
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadataTypeDef


class GetApplicationOutputTypeDef(BaseValidatorModel):
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
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApplicationOutputTypeDef(BaseValidatorModel):
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
    ReplicationStatuses: List[ReplicationStatusTypeDef]
    RuntimeEnvironment: RuntimeEnvironmentTypeDef
    Status: ApplicationStatusType
    StatusReason: ApplicationStatusReasonType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStreamGroupOutputTypeDef(BaseValidatorModel):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplicationTypeDef
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationStateTypeDef]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadataTypeDef


class GetStreamGroupOutputTypeDef(BaseValidatorModel):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplicationTypeDef
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationStateTypeDef]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadataTypeDef


class StreamGroupSummaryTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: Optional[datetime] = None
    DefaultApplication: Optional[DefaultApplicationTypeDef] = None
    Description: Optional[str] = None
    Id: Optional[str] = None
    LastUpdatedAt: Optional[datetime] = None
    Status: Optional[StreamGroupStatusType] = None
    StreamClass: Optional[StreamClassType] = None


class UpdateStreamGroupOutputTypeDef(BaseValidatorModel):
    Arn: str
    AssociatedApplications: List[str]
    CreatedAt: datetime
    DefaultApplication: DefaultApplicationTypeDef
    Description: str
    Id: str
    LastUpdatedAt: datetime
    LocationStates: List[LocationStateTypeDef]
    Status: StreamGroupStatusType
    StatusReason: StreamGroupStatusReasonType
    StreamClass: StreamClassType
    ResponseMetadata: ResponseMetadataTypeDef


class GetApplicationInputWaitExtraTypeDef(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetApplicationInputWaitTypeDef(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetStreamGroupInputWaitExtraTypeDef(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetStreamGroupInputWaitTypeDef(BaseValidatorModel):
    Identifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class GetStreamSessionInputWaitTypeDef(BaseValidatorModel):
    Identifier: str
    StreamSessionIdentifier: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class ListApplicationsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamGroupsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamSessionsByAccountInputPaginateTypeDef(BaseValidatorModel):
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    Status: Optional[StreamSessionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamSessionsInputPaginateTypeDef(BaseValidatorModel):
    Identifier: str
    ExportFilesStatus: Optional[ExportFilesStatusType] = None
    Status: Optional[StreamSessionStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationsOutputTypeDef(BaseValidatorModel):
    Items: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListStreamGroupsOutputTypeDef(BaseValidatorModel):
    Items: List[StreamGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StreamSessionSummaryTypeDef(BaseValidatorModel):
    pass


class ListStreamSessionsByAccountOutputTypeDef(BaseValidatorModel):
    Items: List[StreamSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListStreamSessionsOutputTypeDef(BaseValidatorModel):
    Items: List[StreamSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None



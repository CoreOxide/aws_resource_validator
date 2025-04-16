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
from aws_resource_validator.pydantic_models.appintegrations_constants import *

class ApplicationAssociationSummary(BaseValidatorModel):
    ApplicationAssociationArn: Optional[str] = None
    ApplicationArn: Optional[str] = None
    ClientId: Optional[str] = None


class ExternalUrlConfigOutput(BaseValidatorModel):
    AccessUrl: str
    ApprovedOrigins: Optional[List[str]] = None


class ExternalUrlConfig(BaseValidatorModel):
    AccessUrl: str
    ApprovedOrigins: Optional[Sequence[str]] = None


class ApplicationSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Namespace: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class Publication(BaseValidatorModel):
    Event: str
    Schema: str
    Description: Optional[str] = None


class Subscription(BaseValidatorModel):
    Event: str
    Description: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ScheduleConfiguration(BaseValidatorModel):
    ScheduleExpression: str
    FirstExecutionFrom: Optional[str] = None
    Object: Optional[str] = None


class FileConfigurationOutput(BaseValidatorModel):
    Folders: List[str]
    Filters: Optional[Dict[str, List[str]]] = None


class EventFilter(BaseValidatorModel):
    Source: str


class LastExecutionStatus(BaseValidatorModel):
    ExecutionStatus: Optional[ExecutionStatusType] = None
    StatusMessage: Optional[str] = None


class DataIntegrationSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    SourceURI: Optional[str] = None


class DeleteApplicationRequest(BaseValidatorModel):
    Arn: str


class DeleteDataIntegrationRequest(BaseValidatorModel):
    DataIntegrationIdentifier: str


class DeleteEventIntegrationRequest(BaseValidatorModel):
    Name: str


class EventIntegrationAssociation(BaseValidatorModel):
    EventIntegrationAssociationArn: Optional[str] = None
    EventIntegrationAssociationId: Optional[str] = None
    EventIntegrationName: Optional[str] = None
    ClientId: Optional[str] = None
    EventBridgeRuleName: Optional[str] = None
    ClientAssociationMetadata: Optional[Dict[str, str]] = None


class OnDemandConfiguration(BaseValidatorModel):
    StartTime: str
    EndTime: Optional[str] = None


class FileConfiguration(BaseValidatorModel):
    Folders: Sequence[str]
    Filters: Optional[Mapping[str, Sequence[str]]] = None


class GetApplicationRequest(BaseValidatorModel):
    Arn: str


class GetDataIntegrationRequest(BaseValidatorModel):
    Identifier: str


class GetEventIntegrationRequest(BaseValidatorModel):
    Name: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationAssociationsRequest(BaseValidatorModel):
    ApplicationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListApplicationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataIntegrationAssociationsRequest(BaseValidatorModel):
    DataIntegrationIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataIntegrationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventIntegrationAssociationsRequest(BaseValidatorModel):
    EventIntegrationName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventIntegrationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDataIntegrationRequest(BaseValidatorModel):
    Identifier: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateEventIntegrationRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None


class ApplicationSourceConfigOutput(BaseValidatorModel):
    ExternalUrlConfig: Optional[ExternalUrlConfigOutput] = None


class ApplicationSourceConfig(BaseValidatorModel):
    ExternalUrlConfig: Optional[ExternalUrlConfig] = None


class CreateApplicationResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


class CreateDataIntegrationAssociationResponse(BaseValidatorModel):
    DataIntegrationAssociationId: str
    DataIntegrationArn: str
    ResponseMetadata: ResponseMetadata


class CreateEventIntegrationResponse(BaseValidatorModel):
    EventIntegrationArn: str
    ResponseMetadata: ResponseMetadata


class ListApplicationAssociationsResponse(BaseValidatorModel):
    ApplicationAssociations: List[ApplicationAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListApplicationsResponse(BaseValidatorModel):
    Applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateDataIntegrationResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    KmsKey: str
    SourceURI: str
    ScheduleConfiguration: ScheduleConfiguration
    Tags: Dict[str, str]
    ClientToken: str
    FileConfiguration: FileConfigurationOutput
    ObjectConfiguration: Dict[str, Dict[str, List[str]]]
    ResponseMetadata: ResponseMetadata


class GetDataIntegrationResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    KmsKey: str
    SourceURI: str
    ScheduleConfiguration: ScheduleConfiguration
    Tags: Dict[str, str]
    FileConfiguration: FileConfigurationOutput
    ObjectConfiguration: Dict[str, Dict[str, List[str]]]
    ResponseMetadata: ResponseMetadata


class CreateEventIntegrationRequest(BaseValidatorModel):
    Name: str
    EventFilter: EventFilter
    EventBridgeBus: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class EventIntegration(BaseValidatorModel):
    EventIntegrationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    EventFilter: Optional[EventFilter] = None
    EventBridgeBus: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class GetEventIntegrationResponse(BaseValidatorModel):
    Name: str
    Description: str
    EventIntegrationArn: str
    EventBridgeBus: str
    EventFilter: EventFilter
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListDataIntegrationsResponse(BaseValidatorModel):
    DataIntegrations: List[DataIntegrationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEventIntegrationAssociationsResponse(BaseValidatorModel):
    EventIntegrationAssociations: List[EventIntegrationAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExecutionConfiguration(BaseValidatorModel):
    ExecutionMode: ExecutionModeType
    OnDemandConfiguration: Optional[OnDemandConfiguration] = None
    ScheduleConfiguration: Optional[ScheduleConfiguration] = None


class ListApplicationAssociationsRequestPaginate(BaseValidatorModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataIntegrationAssociationsRequestPaginate(BaseValidatorModel):
    DataIntegrationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataIntegrationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventIntegrationAssociationsRequestPaginate(BaseValidatorModel):
    EventIntegrationName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventIntegrationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetApplicationResponse(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Namespace: str
    Description: str
    ApplicationSourceConfig: ApplicationSourceConfigOutput
    Subscriptions: List[Subscription]
    Publications: List[Publication]
    CreatedTime: datetime
    LastModifiedTime: datetime
    Tags: Dict[str, str]
    Permissions: List[str]
    ResponseMetadata: ResponseMetadata


class ListEventIntegrationsResponse(BaseValidatorModel):
    EventIntegrations: List[EventIntegration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateDataIntegrationAssociationRequest(BaseValidatorModel):
    DataIntegrationIdentifier: str
    ClientId: Optional[str] = None
    ObjectConfiguration: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = None
    DestinationURI: Optional[str] = None
    ClientAssociationMetadata: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    ExecutionConfiguration: Optional[ExecutionConfiguration] = None


class DataIntegrationAssociationSummary(BaseValidatorModel):
    DataIntegrationAssociationArn: Optional[str] = None
    DataIntegrationArn: Optional[str] = None
    ClientId: Optional[str] = None
    DestinationURI: Optional[str] = None
    LastExecutionStatus: Optional[LastExecutionStatus] = None
    ExecutionConfiguration: Optional[ExecutionConfiguration] = None


class UpdateDataIntegrationAssociationRequest(BaseValidatorModel):
    DataIntegrationIdentifier: str
    DataIntegrationAssociationIdentifier: str
    ExecutionConfiguration: ExecutionConfiguration


class FileConfigurationUnion(BaseValidatorModel):
    pass


class CreateDataIntegrationRequest(BaseValidatorModel):
    Name: str
    KmsKey: str
    Description: Optional[str] = None
    SourceURI: Optional[str] = None
    ScheduleConfig: Optional[ScheduleConfiguration] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    FileConfiguration: Optional[FileConfigurationUnion] = None
    ObjectConfiguration: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = None


class ApplicationSourceConfigUnion(BaseValidatorModel):
    pass


class CreateApplicationRequest(BaseValidatorModel):
    Name: str
    Namespace: str
    ApplicationSourceConfig: ApplicationSourceConfigUnion
    Description: Optional[str] = None
    Subscriptions: Optional[Sequence[Subscription]] = None
    Publications: Optional[Sequence[Publication]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Permissions: Optional[Sequence[str]] = None


class UpdateApplicationRequest(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ApplicationSourceConfig: Optional[ApplicationSourceConfigUnion] = None
    Subscriptions: Optional[Sequence[Subscription]] = None
    Publications: Optional[Sequence[Publication]] = None
    Permissions: Optional[Sequence[str]] = None


class ListDataIntegrationAssociationsResponse(BaseValidatorModel):
    DataIntegrationAssociations: List[DataIntegrationAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None



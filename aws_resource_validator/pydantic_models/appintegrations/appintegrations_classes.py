from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.appintegrations.appintegrations_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ApplicationAssociationSummary(BaseValidatorModel):
    ApplicationAssociationArn: Optional[str] = None
    ApplicationArn: Optional[str] = None
    ClientId: Optional[str] = None


class ExternalUrlConfigOutput(BaseValidatorModel):
    AccessUrl: str
    ApprovedOrigins: Optional[List[str]] = None


class ExternalUrlConfig(BaseValidatorModel):
    AccessUrl: str
    ApprovedOrigins: Optional[List[str]] = None


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
    Folders: List[str]
    Filters: Optional[Dict[str, List[str]]] = None


# This class is the input for the 'get_application' function.
class GetApplicationRequest(BaseValidatorModel):
    Arn: str


# This class is the input for the 'get_data_integration' function.
class GetDataIntegrationRequest(BaseValidatorModel):
    Identifier: str


# This class is the input for the 'get_event_integration' function.
class GetEventIntegrationRequest(BaseValidatorModel):
    Name: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_application_associations' function.
class ListApplicationAssociationsRequest(BaseValidatorModel):
    ApplicationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_data_integration_associations' function.
class ListDataIntegrationAssociationsRequest(BaseValidatorModel):
    DataIntegrationIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_data_integrations' function.
class ListDataIntegrationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_event_integration_associations' function.
class ListEventIntegrationAssociationsRequest(BaseValidatorModel):
    EventIntegrationName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_event_integrations' function.
class ListEventIntegrationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


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


# This class is the output for the 'create_application' function.
class CreateApplicationResponse(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_integration_association' function.
class CreateDataIntegrationAssociationResponse(BaseValidatorModel):
    DataIntegrationAssociationId: str
    DataIntegrationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_event_integration' function.
class CreateEventIntegrationResponse(BaseValidatorModel):
    EventIntegrationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_application_associations' function.
class ListApplicationAssociationsResponse(BaseValidatorModel):
    ApplicationAssociations: List[ApplicationAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_applications' function.
class ListApplicationsResponse(BaseValidatorModel):
    Applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_data_integration' function.
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


# This class is the output for the 'get_data_integration' function.
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


# This class is the input for the 'create_event_integration' function.
class CreateEventIntegrationRequest(BaseValidatorModel):
    Name: str
    EventFilter: EventFilter
    EventBridgeBus: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class EventIntegration(BaseValidatorModel):
    EventIntegrationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    EventFilter: Optional[EventFilter] = None
    EventBridgeBus: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the output for the 'get_event_integration' function.
class GetEventIntegrationResponse(BaseValidatorModel):
    Name: str
    Description: str
    EventIntegrationArn: str
    EventBridgeBus: str
    EventFilter: EventFilter
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_data_integrations' function.
class ListDataIntegrationsResponse(BaseValidatorModel):
    DataIntegrations: List[DataIntegrationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_event_integration_associations' function.
class ListEventIntegrationAssociationsResponse(BaseValidatorModel):
    EventIntegrationAssociations: List[EventIntegrationAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExecutionConfiguration(BaseValidatorModel):
    ExecutionMode: ExecutionModeType
    OnDemandConfiguration: Optional[OnDemandConfiguration] = None
    ScheduleConfiguration: Optional[ScheduleConfiguration] = None

FileConfigurationUnion = Union[FileConfiguration, FileConfigurationOutput]


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


# This class is the output for the 'get_application' function.
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

ApplicationSourceConfigUnion = Union[ApplicationSourceConfig, ApplicationSourceConfigOutput]


# This class is the output for the 'list_event_integrations' function.
class ListEventIntegrationsResponse(BaseValidatorModel):
    EventIntegrations: List[EventIntegration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_data_integration_association' function.
class CreateDataIntegrationAssociationRequest(BaseValidatorModel):
    DataIntegrationIdentifier: str
    ClientId: Optional[str] = None
    ObjectConfiguration: Optional[Dict[str, Dict[str, List[str]]]] = None
    DestinationURI: Optional[str] = None
    ClientAssociationMetadata: Optional[Dict[str, str]] = None
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


# This class is the input for the 'create_data_integration' function.
class CreateDataIntegrationRequest(BaseValidatorModel):
    Name: str
    KmsKey: str
    Description: Optional[str] = None
    SourceURI: Optional[str] = None
    ScheduleConfig: Optional[ScheduleConfiguration] = None
    Tags: Optional[Dict[str, str]] = None
    ClientToken: Optional[str] = None
    FileConfiguration: Optional[FileConfigurationUnion] = None
    ObjectConfiguration: Optional[Dict[str, Dict[str, List[str]]]] = None


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    Name: str
    Namespace: str
    ApplicationSourceConfig: ApplicationSourceConfigUnion
    Description: Optional[str] = None
    Subscriptions: Optional[List[Subscription]] = None
    Publications: Optional[List[Publication]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    Permissions: Optional[List[str]] = None


class UpdateApplicationRequest(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ApplicationSourceConfig: Optional[ApplicationSourceConfigUnion] = None
    Subscriptions: Optional[List[Subscription]] = None
    Publications: Optional[List[Publication]] = None
    Permissions: Optional[List[str]] = None


# This class is the output for the 'list_data_integration_associations' function.
class ListDataIntegrationAssociationsResponse(BaseValidatorModel):
    DataIntegrationAssociations: List[DataIntegrationAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
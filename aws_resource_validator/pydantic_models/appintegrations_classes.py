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
from aws_resource_validator.pydantic_models.appintegrations_constants import *

class ApplicationAssociationSummaryTypeDef(BaseModel):
    ApplicationAssociationArn: Optional[str] = None
    ApplicationArn: Optional[str] = None
    ClientId: Optional[str] = None

class ExternalUrlConfigTypeDef(BaseModel):
    AccessUrl: str
    ApprovedOrigins: Optional[Sequence[str]] = None

class ApplicationSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Namespace: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class PublicationTypeDef(BaseModel):
    Event: str
    Schema: str
    Description: Optional[str] = None

class SubscriptionTypeDef(BaseModel):
    Event: str
    Description: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FileConfigurationTypeDef(BaseModel):
    Folders: Sequence[str]
    Filters: Optional[Mapping[str, Sequence[str]]] = None

class ScheduleConfigurationTypeDef(BaseModel):
    ScheduleExpression: str
    FirstExecutionFrom: Optional[str] = None
    Object: Optional[str] = None

class EventFilterTypeDef(BaseModel):
    Source: str

class DataIntegrationAssociationSummaryTypeDef(BaseModel):
    DataIntegrationAssociationArn: Optional[str] = None
    DataIntegrationArn: Optional[str] = None
    ClientId: Optional[str] = None

class DataIntegrationSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    SourceURI: Optional[str] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    Arn: str

class DeleteDataIntegrationRequestRequestTypeDef(BaseModel):
    DataIntegrationIdentifier: str

class DeleteEventIntegrationRequestRequestTypeDef(BaseModel):
    Name: str

class EventIntegrationAssociationTypeDef(BaseModel):
    EventIntegrationAssociationArn: Optional[str] = None
    EventIntegrationAssociationId: Optional[str] = None
    EventIntegrationName: Optional[str] = None
    ClientId: Optional[str] = None
    EventBridgeRuleName: Optional[str] = None
    ClientAssociationMetadata: Optional[Dict[str, str]] = None

class GetApplicationRequestRequestTypeDef(BaseModel):
    Arn: str

class GetDataIntegrationRequestRequestTypeDef(BaseModel):
    Identifier: str

class GetEventIntegrationRequestRequestTypeDef(BaseModel):
    Name: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationAssociationsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataIntegrationAssociationsRequestRequestTypeDef(BaseModel):
    DataIntegrationIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataIntegrationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventIntegrationAssociationsRequestRequestTypeDef(BaseModel):
    EventIntegrationName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventIntegrationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDataIntegrationRequestRequestTypeDef(BaseModel):
    Identifier: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateEventIntegrationRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None

class ApplicationSourceConfigTypeDef(BaseModel):
    ExternalUrlConfig: Optional[ExternalUrlConfigTypeDef] = None

class CreateApplicationResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventIntegrationResponseTypeDef(BaseModel):
    EventIntegrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssociationsResponseTypeDef(BaseModel):
    ApplicationAssociations: List[ApplicationAssociationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    Applications: List[ApplicationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataIntegrationRequestRequestTypeDef(BaseModel):
    Name: str
    KmsKey: str
    SourceURI: str
    Description: Optional[str] = None
    ScheduleConfig: Optional[ScheduleConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    FileConfiguration: Optional[FileConfigurationTypeDef] = None
    ObjectConfiguration: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = None

class CreateDataIntegrationResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    KmsKey: str
    SourceURI: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    Tags: Dict[str, str]
    ClientToken: str
    FileConfiguration: FileConfigurationTypeDef
    ObjectConfiguration: Dict[str, Dict[str, List[str]]]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataIntegrationResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Description: str
    KmsKey: str
    SourceURI: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    Tags: Dict[str, str]
    FileConfiguration: FileConfigurationTypeDef
    ObjectConfiguration: Dict[str, Dict[str, List[str]]]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventIntegrationRequestRequestTypeDef(BaseModel):
    Name: str
    EventFilter: EventFilterTypeDef
    EventBridgeBus: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class EventIntegrationTypeDef(BaseModel):
    EventIntegrationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    EventFilter: Optional[EventFilterTypeDef] = None
    EventBridgeBus: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class GetEventIntegrationResponseTypeDef(BaseModel):
    Name: str
    Description: str
    EventIntegrationArn: str
    EventBridgeBus: str
    EventFilter: EventFilterTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataIntegrationAssociationsResponseTypeDef(BaseModel):
    DataIntegrationAssociations: List[DataIntegrationAssociationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataIntegrationsResponseTypeDef(BaseModel):
    DataIntegrations: List[DataIntegrationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventIntegrationAssociationsResponseTypeDef(BaseModel):
    EventIntegrationAssociations: List[EventIntegrationAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef(BaseModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef(BaseModel):
    DataIntegrationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef(BaseModel):
    EventIntegrationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    Name: str
    Namespace: str
    ApplicationSourceConfig: ApplicationSourceConfigTypeDef
    Description: Optional[str] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None
    Publications: Optional[Sequence[PublicationTypeDef]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Permissions: Optional[Sequence[str]] = None

class GetApplicationResponseTypeDef(BaseModel):
    Arn: str
    Id: str
    Name: str
    Namespace: str
    Description: str
    ApplicationSourceConfig: ApplicationSourceConfigTypeDef
    Subscriptions: List[SubscriptionTypeDef]
    Publications: List[PublicationTypeDef]
    CreatedTime: datetime
    LastModifiedTime: datetime
    Tags: Dict[str, str]
    Permissions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ApplicationSourceConfig: Optional[ApplicationSourceConfigTypeDef] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None
    Publications: Optional[Sequence[PublicationTypeDef]] = None
    Permissions: Optional[Sequence[str]] = None

class ListEventIntegrationsResponseTypeDef(BaseModel):
    EventIntegrations: List[EventIntegrationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


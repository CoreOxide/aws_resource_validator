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
from aws_resource_validator.pydantic_models.appintegrations_constants import *

class ApplicationAssociationSummaryTypeDef(BaseValidatorModel):
    ApplicationAssociationArn: Optional[str] = None
    ApplicationArn: Optional[str] = None
    ClientId: Optional[str] = None

class ExternalUrlConfigTypeDef(BaseValidatorModel):
    AccessUrl: str
    ApprovedOrigins: Optional[Sequence[str]] = None

class ApplicationSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Namespace: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class PublicationTypeDef(BaseValidatorModel):
    Event: str
    Schema: str
    Description: Optional[str] = None

class SubscriptionTypeDef(BaseValidatorModel):
    Event: str
    Description: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FileConfigurationTypeDef(BaseValidatorModel):
    Folders: Sequence[str]
    Filters: Optional[Mapping[str, Sequence[str]]] = None

class ScheduleConfigurationTypeDef(BaseValidatorModel):
    ScheduleExpression: str
    FirstExecutionFrom: Optional[str] = None
    Object: Optional[str] = None

class EventFilterTypeDef(BaseValidatorModel):
    Source: str

class DataIntegrationAssociationSummaryTypeDef(BaseValidatorModel):
    DataIntegrationAssociationArn: Optional[str] = None
    DataIntegrationArn: Optional[str] = None
    ClientId: Optional[str] = None

class DataIntegrationSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    SourceURI: Optional[str] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class DeleteDataIntegrationRequestRequestTypeDef(BaseValidatorModel):
    DataIntegrationIdentifier: str

class DeleteEventIntegrationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class EventIntegrationAssociationTypeDef(BaseValidatorModel):
    EventIntegrationAssociationArn: Optional[str] = None
    EventIntegrationAssociationId: Optional[str] = None
    EventIntegrationName: Optional[str] = None
    ClientId: Optional[str] = None
    EventBridgeRuleName: Optional[str] = None
    ClientAssociationMetadata: Optional[Dict[str, str]] = None

class GetApplicationRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class GetDataIntegrationRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetEventIntegrationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationAssociationsRequestRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataIntegrationAssociationsRequestRequestTypeDef(BaseValidatorModel):
    DataIntegrationIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataIntegrationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventIntegrationAssociationsRequestRequestTypeDef(BaseValidatorModel):
    EventIntegrationName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventIntegrationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDataIntegrationRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateEventIntegrationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None

class ApplicationSourceConfigTypeDef(BaseValidatorModel):
    ExternalUrlConfig: Optional[ExternalUrlConfigTypeDef] = None

class CreateApplicationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventIntegrationResponseTypeDef(BaseValidatorModel):
    EventIntegrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssociationsResponseTypeDef(BaseValidatorModel):
    ApplicationAssociations: List[ApplicationAssociationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    Applications: List[ApplicationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataIntegrationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    KmsKey: str
    SourceURI: str
    Description: Optional[str] = None
    ScheduleConfig: Optional[ScheduleConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    FileConfiguration: Optional[FileConfigurationTypeDef] = None
    ObjectConfiguration: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = None

class CreateDataIntegrationResponseTypeDef(BaseValidatorModel):
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

class GetDataIntegrationResponseTypeDef(BaseValidatorModel):
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

class CreateEventIntegrationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    EventFilter: EventFilterTypeDef
    EventBridgeBus: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class EventIntegrationTypeDef(BaseValidatorModel):
    EventIntegrationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    EventFilter: Optional[EventFilterTypeDef] = None
    EventBridgeBus: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class GetEventIntegrationResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    EventIntegrationArn: str
    EventBridgeBus: str
    EventFilter: EventFilterTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataIntegrationAssociationsResponseTypeDef(BaseValidatorModel):
    DataIntegrationAssociations: List[DataIntegrationAssociationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataIntegrationsResponseTypeDef(BaseValidatorModel):
    DataIntegrations: List[DataIntegrationSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventIntegrationAssociationsResponseTypeDef(BaseValidatorModel):
    EventIntegrationAssociations: List[EventIntegrationAssociationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationAssociationsRequestListApplicationAssociationsPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataIntegrationAssociationsRequestListDataIntegrationAssociationsPaginateTypeDef(BaseValidatorModel):
    DataIntegrationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataIntegrationsRequestListDataIntegrationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventIntegrationAssociationsRequestListEventIntegrationAssociationsPaginateTypeDef(BaseValidatorModel):
    EventIntegrationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventIntegrationsRequestListEventIntegrationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Namespace: str
    ApplicationSourceConfig: ApplicationSourceConfigTypeDef
    Description: Optional[str] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None
    Publications: Optional[Sequence[PublicationTypeDef]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Permissions: Optional[Sequence[str]] = None

class GetApplicationResponseTypeDef(BaseValidatorModel):
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

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ApplicationSourceConfig: Optional[ApplicationSourceConfigTypeDef] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None
    Publications: Optional[Sequence[PublicationTypeDef]] = None
    Permissions: Optional[Sequence[str]] = None

class ListEventIntegrationsResponseTypeDef(BaseValidatorModel):
    EventIntegrations: List[EventIntegrationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef


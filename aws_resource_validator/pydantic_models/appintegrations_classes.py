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

class ApplicationAssociationSummaryTypeDef(BaseValidatorModel):
    ApplicationAssociationArn: Optional[str] = None
    ApplicationArn: Optional[str] = None
    ClientId: Optional[str] = None


class ExternalUrlConfigOutputTypeDef(BaseValidatorModel):
    AccessUrl: str
    ApprovedOrigins: Optional[List[str]] = None


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
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ScheduleConfigurationTypeDef(BaseValidatorModel):
    ScheduleExpression: str
    FirstExecutionFrom: Optional[str] = None
    Object: Optional[str] = None


class FileConfigurationOutputTypeDef(BaseValidatorModel):
    Folders: List[str]
    Filters: Optional[Dict[str, List[str]]] = None


class EventFilterTypeDef(BaseValidatorModel):
    Source: str


class LastExecutionStatusTypeDef(BaseValidatorModel):
    ExecutionStatus: Optional[ExecutionStatusType] = None
    StatusMessage: Optional[str] = None


class DataIntegrationSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None
    SourceURI: Optional[str] = None


class DeleteApplicationRequestTypeDef(BaseValidatorModel):
    Arn: str


class DeleteDataIntegrationRequestTypeDef(BaseValidatorModel):
    DataIntegrationIdentifier: str


class DeleteEventIntegrationRequestTypeDef(BaseValidatorModel):
    Name: str


class EventIntegrationAssociationTypeDef(BaseValidatorModel):
    EventIntegrationAssociationArn: Optional[str] = None
    EventIntegrationAssociationId: Optional[str] = None
    EventIntegrationName: Optional[str] = None
    ClientId: Optional[str] = None
    EventBridgeRuleName: Optional[str] = None
    ClientAssociationMetadata: Optional[Dict[str, str]] = None


class OnDemandConfigurationTypeDef(BaseValidatorModel):
    StartTime: str
    EndTime: Optional[str] = None


class FileConfigurationTypeDef(BaseValidatorModel):
    Folders: Sequence[str]
    Filters: Optional[Mapping[str, Sequence[str]]] = None


class GetApplicationRequestTypeDef(BaseValidatorModel):
    Arn: str


class GetDataIntegrationRequestTypeDef(BaseValidatorModel):
    Identifier: str


class GetEventIntegrationRequestTypeDef(BaseValidatorModel):
    Name: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationAssociationsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataIntegrationAssociationsRequestTypeDef(BaseValidatorModel):
    DataIntegrationIdentifier: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataIntegrationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventIntegrationAssociationsRequestTypeDef(BaseValidatorModel):
    EventIntegrationName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventIntegrationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDataIntegrationRequestTypeDef(BaseValidatorModel):
    Identifier: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateEventIntegrationRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None


class ApplicationSourceConfigOutputTypeDef(BaseValidatorModel):
    ExternalUrlConfig: Optional[ExternalUrlConfigOutputTypeDef] = None


class ApplicationSourceConfigTypeDef(BaseValidatorModel):
    ExternalUrlConfig: Optional[ExternalUrlConfigTypeDef] = None


class CreateApplicationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataIntegrationAssociationResponseTypeDef(BaseValidatorModel):
    DataIntegrationAssociationId: str
    DataIntegrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEventIntegrationResponseTypeDef(BaseValidatorModel):
    EventIntegrationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListApplicationAssociationsResponseTypeDef(BaseValidatorModel):
    ApplicationAssociations: List[ApplicationAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListApplicationsResponseTypeDef(BaseValidatorModel):
    Applications: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


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
    FileConfiguration: FileConfigurationOutputTypeDef
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
    FileConfiguration: FileConfigurationOutputTypeDef
    ObjectConfiguration: Dict[str, Dict[str, List[str]]]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEventIntegrationRequestTypeDef(BaseValidatorModel):
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


class ListDataIntegrationsResponseTypeDef(BaseValidatorModel):
    DataIntegrations: List[DataIntegrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListEventIntegrationAssociationsResponseTypeDef(BaseValidatorModel):
    EventIntegrationAssociations: List[EventIntegrationAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExecutionConfigurationTypeDef(BaseValidatorModel):
    ExecutionMode: ExecutionModeType
    OnDemandConfiguration: Optional[OnDemandConfigurationTypeDef] = None
    ScheduleConfiguration: Optional[ScheduleConfigurationTypeDef] = None


class ListApplicationAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    ApplicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataIntegrationAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    DataIntegrationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataIntegrationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventIntegrationAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    EventIntegrationName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventIntegrationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetApplicationResponseTypeDef(BaseValidatorModel):
    Arn: str
    Id: str
    Name: str
    Namespace: str
    Description: str
    ApplicationSourceConfig: ApplicationSourceConfigOutputTypeDef
    Subscriptions: List[SubscriptionTypeDef]
    Publications: List[PublicationTypeDef]
    CreatedTime: datetime
    LastModifiedTime: datetime
    Tags: Dict[str, str]
    Permissions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListEventIntegrationsResponseTypeDef(BaseValidatorModel):
    EventIntegrations: List[EventIntegrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateDataIntegrationAssociationRequestTypeDef(BaseValidatorModel):
    DataIntegrationIdentifier: str
    ClientId: Optional[str] = None
    ObjectConfiguration: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = None
    DestinationURI: Optional[str] = None
    ClientAssociationMetadata: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    ExecutionConfiguration: Optional[ExecutionConfigurationTypeDef] = None


class DataIntegrationAssociationSummaryTypeDef(BaseValidatorModel):
    DataIntegrationAssociationArn: Optional[str] = None
    DataIntegrationArn: Optional[str] = None
    ClientId: Optional[str] = None
    DestinationURI: Optional[str] = None
    LastExecutionStatus: Optional[LastExecutionStatusTypeDef] = None
    ExecutionConfiguration: Optional[ExecutionConfigurationTypeDef] = None


class UpdateDataIntegrationAssociationRequestTypeDef(BaseValidatorModel):
    DataIntegrationIdentifier: str
    DataIntegrationAssociationIdentifier: str
    ExecutionConfiguration: ExecutionConfigurationTypeDef


class FileConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataIntegrationRequestTypeDef(BaseValidatorModel):
    Name: str
    KmsKey: str
    Description: Optional[str] = None
    SourceURI: Optional[str] = None
    ScheduleConfig: Optional[ScheduleConfigurationTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    FileConfiguration: Optional[FileConfigurationUnionTypeDef] = None
    ObjectConfiguration: Optional[Mapping[str, Mapping[str, Sequence[str]]]] = None


class ApplicationSourceConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    Name: str
    Namespace: str
    ApplicationSourceConfig: ApplicationSourceConfigUnionTypeDef
    Description: Optional[str] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None
    Publications: Optional[Sequence[PublicationTypeDef]] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Permissions: Optional[Sequence[str]] = None


class UpdateApplicationRequestTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ApplicationSourceConfig: Optional[ApplicationSourceConfigUnionTypeDef] = None
    Subscriptions: Optional[Sequence[SubscriptionTypeDef]] = None
    Publications: Optional[Sequence[PublicationTypeDef]] = None
    Permissions: Optional[Sequence[str]] = None


class ListDataIntegrationAssociationsResponseTypeDef(BaseValidatorModel):
    DataIntegrationAssociations: List[DataIntegrationAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None



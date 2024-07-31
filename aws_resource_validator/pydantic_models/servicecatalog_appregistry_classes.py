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
from aws_resource_validator.pydantic_models.servicecatalog_appregistry_constants import *

class TagQueryConfigurationTypeDef(BaseModel):
    tagKey: Optional[str] = None

class ApplicationSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class ResourcesListItemTypeDef(BaseModel):
    resourceArn: Optional[str] = None
    errorMessage: Optional[str] = None
    status: Optional[str] = None
    resourceType: Optional[str] = None

class ApplicationTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    applicationTag: Optional[Dict[str, str]] = None

class AssociateAttributeGroupRequestRequestTypeDef(BaseModel):
    application: str
    attributeGroup: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateResourceRequestRequestTypeDef(BaseModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    options: Optional[Sequence[AssociationOptionType]] = None

class AttributeGroupDetailsTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[str] = None

class AttributeGroupSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    createdBy: Optional[str] = None

class AttributeGroupTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
    name: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateAttributeGroupRequestRequestTypeDef(BaseModel):
    name: str
    attributes: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    application: str

class DeleteAttributeGroupRequestRequestTypeDef(BaseModel):
    attributeGroup: str

class DisassociateAttributeGroupRequestRequestTypeDef(BaseModel):
    application: str
    attributeGroup: str

class DisassociateResourceRequestRequestTypeDef(BaseModel):
    application: str
    resourceType: ResourceTypeType
    resource: str

class GetApplicationRequestRequestTypeDef(BaseModel):
    application: str

class GetAssociatedResourceRequestRequestTypeDef(BaseModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    nextToken: Optional[str] = None
    resourceTagStatus: Optional[Sequence[ResourceItemStatusType]] = None
    maxResults: Optional[int] = None

class GetAttributeGroupRequestRequestTypeDef(BaseModel):
    attributeGroup: str

class ResourceGroupTypeDef(BaseModel):
    state: Optional[ResourceGroupStateType] = None
    arn: Optional[str] = None
    errorMessage: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssociatedAttributeGroupsRequestRequestTypeDef(BaseModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssociatedResourcesRequestRequestTypeDef(BaseModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAttributeGroupsForApplicationRequestRequestTypeDef(BaseModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAttributeGroupsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ResourceDetailsTypeDef(BaseModel):
    tagValue: Optional[str] = None

class SyncResourceRequestRequestTypeDef(BaseModel):
    resourceType: ResourceTypeType
    resource: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    application: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateAttributeGroupRequestRequestTypeDef(BaseModel):
    attributeGroup: str
    name: Optional[str] = None
    description: Optional[str] = None
    attributes: Optional[str] = None

class AppRegistryConfigurationTypeDef(BaseModel):
    tagQueryConfiguration: Optional[TagQueryConfigurationTypeDef] = None

class ApplicationTagResultTypeDef(BaseModel):
    applicationTagStatus: Optional[ApplicationTagStatusType] = None
    errorMessage: Optional[str] = None
    resources: Optional[List[ResourcesListItemTypeDef]] = None
    nextToken: Optional[str] = None

class AssociateAttributeGroupResponseTypeDef(BaseModel):
    applicationArn: str
    attributeGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceResponseTypeDef(BaseModel):
    applicationArn: str
    resourceArn: str
    options: List[AssociationOptionType]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResponseTypeDef(BaseModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationResponseTypeDef(BaseModel):
    application: ApplicationSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateAttributeGroupResponseTypeDef(BaseModel):
    applicationArn: str
    attributeGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceResponseTypeDef(BaseModel):
    applicationArn: str
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttributeGroupResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    attributes: str
    creationTime: datetime
    lastUpdateTime: datetime
    tags: Dict[str, str]
    createdBy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    applications: List[ApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedAttributeGroupsResponseTypeDef(BaseModel):
    attributeGroups: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SyncResourceResponseTypeDef(BaseModel):
    applicationArn: str
    resourceArn: str
    actionTaken: SyncActionType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttributeGroupsForApplicationResponseTypeDef(BaseModel):
    attributeGroupsDetails: List[AttributeGroupDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAttributeGroupResponseTypeDef(BaseModel):
    attributeGroup: AttributeGroupSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttributeGroupsResponseTypeDef(BaseModel):
    attributeGroups: List[AttributeGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAttributeGroupResponseTypeDef(BaseModel):
    attributeGroup: AttributeGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAttributeGroupResponseTypeDef(BaseModel):
    attributeGroup: AttributeGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationsTypeDef(BaseModel):
    resourceGroup: Optional[ResourceGroupTypeDef] = None
    applicationTagResourceGroup: Optional[ResourceGroupTypeDef] = None

class ResourceIntegrationsTypeDef(BaseModel):
    resourceGroup: Optional[ResourceGroupTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedAttributeGroupsRequestListAssociatedAttributeGroupsPaginateTypeDef(BaseModel):
    application: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedResourcesRequestListAssociatedResourcesPaginateTypeDef(BaseModel):
    application: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttributeGroupsRequestListAttributeGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ResourceInfoTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceDetails: Optional[ResourceDetailsTypeDef] = None
    options: Optional[List[AssociationOptionType]] = None

class GetConfigurationResponseTypeDef(BaseModel):
    configuration: AppRegistryConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfigurationRequestRequestTypeDef(BaseModel):
    configuration: AppRegistryConfigurationTypeDef

class GetApplicationResponseTypeDef(BaseModel):
    id: str
    arn: str
    name: str
    description: str
    creationTime: datetime
    lastUpdateTime: datetime
    associatedResourceCount: int
    tags: Dict[str, str]
    integrations: IntegrationsTypeDef
    applicationTag: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    associationTime: Optional[datetime] = None
    integrations: Optional[ResourceIntegrationsTypeDef] = None

class ListAssociatedResourcesResponseTypeDef(BaseModel):
    resources: List[ResourceInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedResourceResponseTypeDef(BaseModel):
    resource: ResourceTypeDef
    options: List[AssociationOptionType]
    applicationTagResult: ApplicationTagResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.servicecatalog_appregistry_constants import *

class TagQueryConfigurationTypeDef(BaseValidatorModel):
    tagKey: Optional[str] = None

class ApplicationSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None

class ResourcesListItemTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    errorMessage: Optional[str] = None
    status: Optional[str] = None
    resourceType: Optional[str] = None

class ApplicationTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    applicationTag: Optional[Dict[str, str]] = None

class AssociateAttributeGroupRequestRequestTypeDef(BaseValidatorModel):
    application: str
    attributeGroup: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateResourceRequestRequestTypeDef(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    options: Optional[Sequence[AssociationOptionType]] = None

class AttributeGroupDetailsTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[str] = None

class AttributeGroupSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    createdBy: Optional[str] = None

class AttributeGroupTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateAttributeGroupRequestRequestTypeDef(BaseValidatorModel):
    name: str
    attributes: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str

class DeleteAttributeGroupRequestRequestTypeDef(BaseValidatorModel):
    attributeGroup: str

class DisassociateAttributeGroupRequestRequestTypeDef(BaseValidatorModel):
    application: str
    attributeGroup: str

class DisassociateResourceRequestRequestTypeDef(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str

class GetApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str

class GetAssociatedResourceRequestRequestTypeDef(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    nextToken: Optional[str] = None
    resourceTagStatus: Optional[Sequence[ResourceItemStatusType]] = None
    maxResults: Optional[int] = None

class GetAttributeGroupRequestRequestTypeDef(BaseValidatorModel):
    attributeGroup: str

class ResourceGroupTypeDef(BaseValidatorModel):
    state: Optional[ResourceGroupStateType] = None
    arn: Optional[str] = None
    errorMessage: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssociatedAttributeGroupsRequestRequestTypeDef(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAssociatedResourcesRequestRequestTypeDef(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAttributeGroupsForApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAttributeGroupsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ResourceDetailsTypeDef(BaseValidatorModel):
    tagValue: Optional[str] = None

class SyncResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resource: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    application: str
    name: Optional[str] = None
    description: Optional[str] = None

class UpdateAttributeGroupRequestRequestTypeDef(BaseValidatorModel):
    attributeGroup: str
    name: Optional[str] = None
    description: Optional[str] = None
    attributes: Optional[str] = None

class AppRegistryConfigurationTypeDef(BaseValidatorModel):
    tagQueryConfiguration: Optional[TagQueryConfigurationTypeDef] = None

class ApplicationTagResultTypeDef(BaseValidatorModel):
    applicationTagStatus: Optional[ApplicationTagStatusType] = None
    errorMessage: Optional[str] = None
    resources: Optional[List[ResourcesListItemTypeDef]] = None
    nextToken: Optional[str] = None

class AssociateAttributeGroupResponseTypeDef(BaseValidatorModel):
    applicationArn: str
    attributeGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceResponseTypeDef(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    options: List[AssociationOptionType]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateApplicationResponseTypeDef(BaseValidatorModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteApplicationResponseTypeDef(BaseValidatorModel):
    application: ApplicationSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateAttributeGroupResponseTypeDef(BaseValidatorModel):
    applicationArn: str
    attributeGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceResponseTypeDef(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttributeGroupResponseTypeDef(BaseValidatorModel):
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

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    applications: List[ApplicationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedAttributeGroupsResponseTypeDef(BaseValidatorModel):
    attributeGroups: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SyncResourceResponseTypeDef(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    actionTaken: SyncActionType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationResponseTypeDef(BaseValidatorModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttributeGroupsForApplicationResponseTypeDef(BaseValidatorModel):
    attributeGroupsDetails: List[AttributeGroupDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAttributeGroupResponseTypeDef(BaseValidatorModel):
    attributeGroup: AttributeGroupSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttributeGroupsResponseTypeDef(BaseValidatorModel):
    attributeGroups: List[AttributeGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAttributeGroupResponseTypeDef(BaseValidatorModel):
    attributeGroup: AttributeGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAttributeGroupResponseTypeDef(BaseValidatorModel):
    attributeGroup: AttributeGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IntegrationsTypeDef(BaseValidatorModel):
    resourceGroup: Optional[ResourceGroupTypeDef] = None
    applicationTagResourceGroup: Optional[ResourceGroupTypeDef] = None

class ResourceIntegrationsTypeDef(BaseValidatorModel):
    resourceGroup: Optional[ResourceGroupTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedAttributeGroupsRequestListAssociatedAttributeGroupsPaginateTypeDef(BaseValidatorModel):
    application: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedResourcesRequestListAssociatedResourcesPaginateTypeDef(BaseValidatorModel):
    application: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttributeGroupsRequestListAttributeGroupsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ResourceInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceDetails: Optional[ResourceDetailsTypeDef] = None
    options: Optional[List[AssociationOptionType]] = None

class GetConfigurationResponseTypeDef(BaseValidatorModel):
    configuration: AppRegistryConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfigurationRequestRequestTypeDef(BaseValidatorModel):
    configuration: AppRegistryConfigurationTypeDef

class GetApplicationResponseTypeDef(BaseValidatorModel):
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

class ResourceTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    associationTime: Optional[datetime] = None
    integrations: Optional[ResourceIntegrationsTypeDef] = None

class ListAssociatedResourcesResponseTypeDef(BaseValidatorModel):
    resources: List[ResourceInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedResourceResponseTypeDef(BaseValidatorModel):
    resource: ResourceTypeDef
    options: List[AssociationOptionType]
    applicationTagResult: ApplicationTagResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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
from aws_resource_validator.pydantic_models.servicecatalog_appregistry_constants import *

class TagQueryConfigurationTypeDef(BaseValidatorModel):
    tagKey: Optional[str] = None


class ResourcesListItemTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    errorMessage: Optional[str] = None
    status: Optional[str] = None
    resourceType: Optional[str] = None


class AssociateAttributeGroupRequestTypeDef(BaseValidatorModel):
    application: str
    attributeGroup: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateResourceRequestTypeDef(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    options: Optional[Sequence[AssociationOptionType]] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    name: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateAttributeGroupRequestTypeDef(BaseValidatorModel):
    name: str
    attributes: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteApplicationRequestTypeDef(BaseValidatorModel):
    application: str


class DeleteAttributeGroupRequestTypeDef(BaseValidatorModel):
    attributeGroup: str


class DisassociateAttributeGroupRequestTypeDef(BaseValidatorModel):
    application: str
    attributeGroup: str


class DisassociateResourceRequestTypeDef(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str


class GetApplicationRequestTypeDef(BaseValidatorModel):
    application: str


class GetAssociatedResourceRequestTypeDef(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    nextToken: Optional[str] = None
    resourceTagStatus: Optional[Sequence[ResourceItemStatusType]] = None
    maxResults: Optional[int] = None


class GetAttributeGroupRequestTypeDef(BaseValidatorModel):
    attributeGroup: str


class ResourceGroupTypeDef(BaseValidatorModel):
    state: Optional[ResourceGroupStateType] = None
    arn: Optional[str] = None
    errorMessage: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssociatedAttributeGroupsRequestTypeDef(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssociatedResourcesRequestTypeDef(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAttributeGroupsForApplicationRequestTypeDef(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAttributeGroupsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ResourceDetailsTypeDef(BaseValidatorModel):
    tagValue: Optional[str] = None


class SyncResourceRequestTypeDef(BaseValidatorModel):
    resourceType: ResourceTypeType
    resource: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateApplicationRequestTypeDef(BaseValidatorModel):
    application: str
    name: Optional[str] = None
    description: Optional[str] = None


class UpdateAttributeGroupRequestTypeDef(BaseValidatorModel):
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


class ApplicationTypeDef(BaseValidatorModel):
    pass


class CreateApplicationResponseTypeDef(BaseValidatorModel):
    application: ApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ApplicationSummaryTypeDef(BaseValidatorModel):
    pass


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


class ListApplicationsResponseTypeDef(BaseValidatorModel):
    applications: List[ApplicationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAssociatedAttributeGroupsResponseTypeDef(BaseValidatorModel):
    attributeGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class AttributeGroupDetailsTypeDef(BaseValidatorModel):
    pass


class ListAttributeGroupsForApplicationResponseTypeDef(BaseValidatorModel):
    attributeGroupsDetails: List[AttributeGroupDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AttributeGroupSummaryTypeDef(BaseValidatorModel):
    pass


class DeleteAttributeGroupResponseTypeDef(BaseValidatorModel):
    attributeGroup: AttributeGroupSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAttributeGroupsResponseTypeDef(BaseValidatorModel):
    attributeGroups: List[AttributeGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AttributeGroupTypeDef(BaseValidatorModel):
    pass


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


class ListApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssociatedAttributeGroupsRequestPaginateTypeDef(BaseValidatorModel):
    application: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssociatedResourcesRequestPaginateTypeDef(BaseValidatorModel):
    application: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttributeGroupsForApplicationRequestPaginateTypeDef(BaseValidatorModel):
    application: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttributeGroupsRequestPaginateTypeDef(BaseValidatorModel):
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


class PutConfigurationRequestTypeDef(BaseValidatorModel):
    configuration: AppRegistryConfigurationTypeDef


class ResourceTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    associationTime: Optional[datetime] = None
    integrations: Optional[ResourceIntegrationsTypeDef] = None


class ListAssociatedResourcesResponseTypeDef(BaseValidatorModel):
    resources: List[ResourceInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetAssociatedResourceResponseTypeDef(BaseValidatorModel):
    resource: ResourceTypeDef
    options: List[AssociationOptionType]
    applicationTagResult: ApplicationTagResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef



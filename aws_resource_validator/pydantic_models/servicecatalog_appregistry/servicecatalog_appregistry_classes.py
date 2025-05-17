from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.servicecatalog_appregistry.servicecatalog_appregistry_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class TagQueryConfiguration(BaseValidatorModel):
    tagKey: Optional[str] = None


class ApplicationSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None


class ResourcesListItem(BaseValidatorModel):
    resourceArn: Optional[str] = None
    errorMessage: Optional[str] = None
    status: Optional[str] = None
    resourceType: Optional[str] = None


class Application(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    applicationTag: Optional[Dict[str, str]] = None


# This class is the input for the 'associate_attribute_group' function.
class AssociateAttributeGroupRequest(BaseValidatorModel):
    application: str
    attributeGroup: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'associate_resource' function.
class AssociateResourceRequest(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    options: Optional[List[AssociationOptionType]] = None


class AttributeGroupDetails(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    createdBy: Optional[str] = None


class AttributeGroupSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    createdBy: Optional[str] = None


class AttributeGroup(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_application' function.
class CreateApplicationRequest(BaseValidatorModel):
    name: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_attribute_group' function.
class CreateAttributeGroupRequest(BaseValidatorModel):
    name: str
    attributes: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'delete_application' function.
class DeleteApplicationRequest(BaseValidatorModel):
    application: str


# This class is the input for the 'delete_attribute_group' function.
class DeleteAttributeGroupRequest(BaseValidatorModel):
    attributeGroup: str


# This class is the input for the 'disassociate_attribute_group' function.
class DisassociateAttributeGroupRequest(BaseValidatorModel):
    application: str
    attributeGroup: str


# This class is the input for the 'disassociate_resource' function.
class DisassociateResourceRequest(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str


# This class is the input for the 'get_application' function.
class GetApplicationRequest(BaseValidatorModel):
    application: str


# This class is the input for the 'get_associated_resource' function.
class GetAssociatedResourceRequest(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    nextToken: Optional[str] = None
    resourceTagStatus: Optional[List[ResourceItemStatusType]] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_attribute_group' function.
class GetAttributeGroupRequest(BaseValidatorModel):
    attributeGroup: str


class ResourceGroup(BaseValidatorModel):
    state: Optional[ResourceGroupStateType] = None
    arn: Optional[str] = None
    errorMessage: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_applications' function.
class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_associated_attribute_groups' function.
class ListAssociatedAttributeGroupsRequest(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_associated_resources' function.
class ListAssociatedResourcesRequest(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_attribute_groups_for_application' function.
class ListAttributeGroupsForApplicationRequest(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_attribute_groups' function.
class ListAttributeGroupsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ResourceDetails(BaseValidatorModel):
    tagValue: Optional[str] = None


# This class is the input for the 'sync_resource' function.
class SyncResourceRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    resource: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_application' function.
class UpdateApplicationRequest(BaseValidatorModel):
    application: str
    name: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'update_attribute_group' function.
class UpdateAttributeGroupRequest(BaseValidatorModel):
    attributeGroup: str
    name: Optional[str] = None
    description: Optional[str] = None
    attributes: Optional[str] = None


class AppRegistryConfiguration(BaseValidatorModel):
    tagQueryConfiguration: Optional[TagQueryConfiguration] = None


class ApplicationTagResult(BaseValidatorModel):
    applicationTagStatus: Optional[ApplicationTagStatusType] = None
    errorMessage: Optional[str] = None
    resources: Optional[List[ResourcesListItem]] = None
    nextToken: Optional[str] = None


# This class is the output for the 'associate_attribute_group' function.
class AssociateAttributeGroupResponse(BaseValidatorModel):
    applicationArn: str
    attributeGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_resource' function.
class AssociateResourceResponse(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    options: List[AssociationOptionType]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_application' function.
class CreateApplicationResponse(BaseValidatorModel):
    application: Application
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_application' function.
class DeleteApplicationResponse(BaseValidatorModel):
    application: ApplicationSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_attribute_group' function.
class DisassociateAttributeGroupResponse(BaseValidatorModel):
    applicationArn: str
    attributeGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_resource' function.
class DisassociateResourceResponse(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_configuration' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_attribute_group' function.
class GetAttributeGroupResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    attributes: str
    creationTime: datetime
    lastUpdateTime: datetime
    tags: Dict[str, str]
    createdBy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_applications' function.
class ListApplicationsResponse(BaseValidatorModel):
    applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_associated_attribute_groups' function.
class ListAssociatedAttributeGroupsResponse(BaseValidatorModel):
    attributeGroups: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'sync_resource' function.
class SyncResourceResponse(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    actionTaken: SyncActionType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_application' function.
class UpdateApplicationResponse(BaseValidatorModel):
    application: Application
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_attribute_groups_for_application' function.
class ListAttributeGroupsForApplicationResponse(BaseValidatorModel):
    attributeGroupsDetails: List[AttributeGroupDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'delete_attribute_group' function.
class DeleteAttributeGroupResponse(BaseValidatorModel):
    attributeGroup: AttributeGroupSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_attribute_groups' function.
class ListAttributeGroupsResponse(BaseValidatorModel):
    attributeGroups: List[AttributeGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_attribute_group' function.
class CreateAttributeGroupResponse(BaseValidatorModel):
    attributeGroup: AttributeGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_attribute_group' function.
class UpdateAttributeGroupResponse(BaseValidatorModel):
    attributeGroup: AttributeGroup
    ResponseMetadata: ResponseMetadata


class Integrations(BaseValidatorModel):
    resourceGroup: Optional[ResourceGroup] = None
    applicationTagResourceGroup: Optional[ResourceGroup] = None


class ResourceIntegrations(BaseValidatorModel):
    resourceGroup: Optional[ResourceGroup] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociatedAttributeGroupsRequestPaginate(BaseValidatorModel):
    application: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociatedResourcesRequestPaginate(BaseValidatorModel):
    application: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttributeGroupsForApplicationRequestPaginate(BaseValidatorModel):
    application: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttributeGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ResourceInfo(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    resourceType: Optional[ResourceTypeType] = None
    resourceDetails: Optional[ResourceDetails] = None
    options: Optional[List[AssociationOptionType]] = None


class GetConfigurationResponse(BaseValidatorModel):
    configuration: AppRegistryConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_configuration' function.
class PutConfigurationRequest(BaseValidatorModel):
    configuration: AppRegistryConfiguration


# This class is the output for the 'get_application' function.
class GetApplicationResponse(BaseValidatorModel):
    id: str
    arn: str
    name: str
    description: str
    creationTime: datetime
    lastUpdateTime: datetime
    associatedResourceCount: int
    tags: Dict[str, str]
    integrations: Integrations
    applicationTag: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Resource(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    associationTime: Optional[datetime] = None
    integrations: Optional[ResourceIntegrations] = None


# This class is the output for the 'list_associated_resources' function.
class ListAssociatedResourcesResponse(BaseValidatorModel):
    resources: List[ResourceInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_associated_resource' function.
class GetAssociatedResourceResponse(BaseValidatorModel):
    resource: Resource
    options: List[AssociationOptionType]
    applicationTagResult: ApplicationTagResult
    ResponseMetadata: ResponseMetadata
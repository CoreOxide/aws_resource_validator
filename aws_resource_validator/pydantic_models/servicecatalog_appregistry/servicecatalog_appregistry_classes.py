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


class AssociateAttributeGroupRequest(BaseValidatorModel):
    application: str
    attributeGroup: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class CreateApplicationRequest(BaseValidatorModel):
    name: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateAttributeGroupRequest(BaseValidatorModel):
    name: str
    attributes: str
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DeleteApplicationRequest(BaseValidatorModel):
    application: str


class DeleteAttributeGroupRequest(BaseValidatorModel):
    attributeGroup: str


class DisassociateAttributeGroupRequest(BaseValidatorModel):
    application: str
    attributeGroup: str


class DisassociateResourceRequest(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str


class GetApplicationRequest(BaseValidatorModel):
    application: str


class GetAssociatedResourceRequest(BaseValidatorModel):
    application: str
    resourceType: ResourceTypeType
    resource: str
    nextToken: Optional[str] = None
    resourceTagStatus: Optional[List[ResourceItemStatusType]] = None
    maxResults: Optional[int] = None


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


class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssociatedAttributeGroupsRequest(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAssociatedResourcesRequest(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAttributeGroupsForApplicationRequest(BaseValidatorModel):
    application: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAttributeGroupsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ResourceDetails(BaseValidatorModel):
    tagValue: Optional[str] = None


class SyncResourceRequest(BaseValidatorModel):
    resourceType: ResourceTypeType
    resource: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateApplicationRequest(BaseValidatorModel):
    application: str
    name: Optional[str] = None
    description: Optional[str] = None


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


class AssociateAttributeGroupResponse(BaseValidatorModel):
    applicationArn: str
    attributeGroupArn: str
    ResponseMetadata: ResponseMetadata


class AssociateResourceResponse(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    options: List[AssociationOptionType]
    ResponseMetadata: ResponseMetadata


class CreateApplicationResponse(BaseValidatorModel):
    application: Application
    ResponseMetadata: ResponseMetadata


class DeleteApplicationResponse(BaseValidatorModel):
    application: ApplicationSummary
    ResponseMetadata: ResponseMetadata


class DisassociateAttributeGroupResponse(BaseValidatorModel):
    applicationArn: str
    attributeGroupArn: str
    ResponseMetadata: ResponseMetadata


class DisassociateResourceResponse(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


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


class ListApplicationsResponse(BaseValidatorModel):
    applications: List[ApplicationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAssociatedAttributeGroupsResponse(BaseValidatorModel):
    attributeGroups: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SyncResourceResponse(BaseValidatorModel):
    applicationArn: str
    resourceArn: str
    actionTaken: SyncActionType
    ResponseMetadata: ResponseMetadata


class UpdateApplicationResponse(BaseValidatorModel):
    application: Application
    ResponseMetadata: ResponseMetadata


class ListAttributeGroupsForApplicationResponse(BaseValidatorModel):
    attributeGroupsDetails: List[AttributeGroupDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DeleteAttributeGroupResponse(BaseValidatorModel):
    attributeGroup: AttributeGroupSummary
    ResponseMetadata: ResponseMetadata


class ListAttributeGroupsResponse(BaseValidatorModel):
    attributeGroups: List[AttributeGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateAttributeGroupResponse(BaseValidatorModel):
    attributeGroup: AttributeGroup
    ResponseMetadata: ResponseMetadata


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


class PutConfigurationRequest(BaseValidatorModel):
    configuration: AppRegistryConfiguration


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


class ListAssociatedResourcesResponse(BaseValidatorModel):
    resources: List[ResourceInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetAssociatedResourceResponse(BaseValidatorModel):
    resource: Resource
    options: List[AssociationOptionType]
    applicationTagResult: ApplicationTagResult
    ResponseMetadata: ResponseMetadata
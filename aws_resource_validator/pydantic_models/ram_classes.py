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
from aws_resource_validator.pydantic_models.ram_constants import *

class AcceptResourceShareInvitationRequestRequestTypeDef(BaseModel):
    resourceShareInvitationArn: str
    clientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateResourceSharePermissionRequestRequestTypeDef(BaseModel):
    resourceShareArn: str
    permissionArn: str
    replace: Optional[bool] = None
    clientToken: Optional[str] = None
    permissionVersion: Optional[int] = None

class AssociateResourceShareRequestRequestTypeDef(BaseModel):
    resourceShareArn: str
    resourceArns: Optional[Sequence[str]] = None
    principals: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    sources: Optional[Sequence[str]] = None

class ResourceShareAssociationTypeDef(BaseModel):
    resourceShareArn: Optional[str] = None
    resourceShareName: Optional[str] = None
    associatedEntity: Optional[str] = None
    associationType: Optional[ResourceShareAssociationTypeType] = None
    status: Optional[ResourceShareAssociationStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    external: Optional[bool] = None

class AssociatedPermissionTypeDef(BaseModel):
    arn: Optional[str] = None
    permissionVersion: Optional[str] = None
    defaultVersion: Optional[bool] = None
    resourceType: Optional[str] = None
    status: Optional[str] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    lastUpdatedTime: Optional[datetime] = None
    resourceShareArn: Optional[str] = None

class TagTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class CreatePermissionVersionRequestRequestTypeDef(BaseModel):
    permissionArn: str
    policyTemplate: str
    clientToken: Optional[str] = None

class DeletePermissionRequestRequestTypeDef(BaseModel):
    permissionArn: str
    clientToken: Optional[str] = None

class DeletePermissionVersionRequestRequestTypeDef(BaseModel):
    permissionArn: str
    permissionVersion: int
    clientToken: Optional[str] = None

class DeleteResourceShareRequestRequestTypeDef(BaseModel):
    resourceShareArn: str
    clientToken: Optional[str] = None

class DisassociateResourceSharePermissionRequestRequestTypeDef(BaseModel):
    resourceShareArn: str
    permissionArn: str
    clientToken: Optional[str] = None

class DisassociateResourceShareRequestRequestTypeDef(BaseModel):
    resourceShareArn: str
    resourceArns: Optional[Sequence[str]] = None
    principals: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    sources: Optional[Sequence[str]] = None

class GetPermissionRequestRequestTypeDef(BaseModel):
    permissionArn: str
    permissionVersion: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetResourcePoliciesRequestRequestTypeDef(BaseModel):
    resourceArns: Sequence[str]
    principal: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetResourceShareAssociationsRequestRequestTypeDef(BaseModel):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    principal: Optional[str] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetResourceShareInvitationsRequestRequestTypeDef(BaseModel):
    resourceShareInvitationArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TagFilterTypeDef(BaseModel):
    tagKey: Optional[str] = None
    tagValues: Optional[Sequence[str]] = None

class ListPendingInvitationResourcesRequestRequestTypeDef(BaseModel):
    resourceShareInvitationArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None

class ResourceTypeDef(BaseModel):
    arn: Optional[str] = None
    type: Optional[str] = None
    resourceShareArn: Optional[str] = None
    resourceGroupArn: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    resourceRegionScope: Optional[ResourceRegionScopeType] = None

class ListPermissionAssociationsRequestRequestTypeDef(BaseModel):
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    resourceType: Optional[str] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    defaultVersion: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPermissionVersionsRequestRequestTypeDef(BaseModel):
    permissionArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPermissionsRequestRequestTypeDef(BaseModel):
    resourceType: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    permissionType: Optional[PermissionTypeFilterType] = None

class ListPrincipalsRequestRequestTypeDef(BaseModel):
    resourceOwner: ResourceOwnerType
    resourceArn: Optional[str] = None
    principals: Optional[Sequence[str]] = None
    resourceType: Optional[str] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PrincipalTypeDef(BaseModel):
    id: Optional[str] = None
    resourceShareArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    external: Optional[bool] = None

class ListReplacePermissionAssociationsWorkRequestRequestTypeDef(BaseModel):
    workIds: Optional[Sequence[str]] = None
    status: Optional[ReplacePermissionAssociationsWorkStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ReplacePermissionAssociationsWorkTypeDef(BaseModel):
    id: Optional[str] = None
    fromPermissionArn: Optional[str] = None
    fromPermissionVersion: Optional[str] = None
    toPermissionArn: Optional[str] = None
    toPermissionVersion: Optional[str] = None
    status: Optional[ReplacePermissionAssociationsWorkStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None

class ListResourceSharePermissionsRequestRequestTypeDef(BaseModel):
    resourceShareArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListResourceTypesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None

class ServiceNameAndResourceTypeTypeDef(BaseModel):
    resourceType: Optional[str] = None
    serviceName: Optional[str] = None
    resourceRegionScope: Optional[ResourceRegionScopeType] = None

class ListResourcesRequestRequestTypeDef(BaseModel):
    resourceOwner: ResourceOwnerType
    principal: Optional[str] = None
    resourceType: Optional[str] = None
    resourceArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None

class PromotePermissionCreatedFromPolicyRequestRequestTypeDef(BaseModel):
    permissionArn: str
    name: str
    clientToken: Optional[str] = None

class PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef(BaseModel):
    resourceShareArn: str

class RejectResourceShareInvitationRequestRequestTypeDef(BaseModel):
    resourceShareInvitationArn: str
    clientToken: Optional[str] = None

class ReplacePermissionAssociationsRequestRequestTypeDef(BaseModel):
    fromPermissionArn: str
    toPermissionArn: str
    fromPermissionVersion: Optional[int] = None
    clientToken: Optional[str] = None

class SetDefaultPermissionVersionRequestRequestTypeDef(BaseModel):
    permissionArn: str
    permissionVersion: int
    clientToken: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    tagKeys: Sequence[str]
    resourceShareArn: Optional[str] = None
    resourceArn: Optional[str] = None

class UpdateResourceShareRequestRequestTypeDef(BaseModel):
    resourceShareArn: str
    name: Optional[str] = None
    allowExternalPrincipals: Optional[bool] = None
    clientToken: Optional[str] = None

class AssociateResourceSharePermissionResponseTypeDef(BaseModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePermissionResponseTypeDef(BaseModel):
    returnValue: bool
    clientToken: str
    permissionStatus: PermissionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePermissionVersionResponseTypeDef(BaseModel):
    returnValue: bool
    clientToken: str
    permissionStatus: PermissionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourceShareResponseTypeDef(BaseModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceSharePermissionResponseTypeDef(BaseModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSharingWithAwsOrganizationResponseTypeDef(BaseModel):
    returnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePoliciesResponseTypeDef(BaseModel):
    policies: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PromoteResourceShareCreatedFromPolicyResponseTypeDef(BaseModel):
    returnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SetDefaultPermissionVersionResponseTypeDef(BaseModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateResourceShareResponseTypeDef(BaseModel):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateResourceShareResponseTypeDef(BaseModel):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceShareAssociationsResponseTypeDef(BaseModel):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceShareInvitationTypeDef(BaseModel):
    resourceShareInvitationArn: Optional[str] = None
    resourceShareName: Optional[str] = None
    resourceShareArn: Optional[str] = None
    senderAccountId: Optional[str] = None
    receiverAccountId: Optional[str] = None
    invitationTimestamp: Optional[datetime] = None
    status: Optional[ResourceShareInvitationStatusType] = None
    resourceShareAssociations: Optional[List[ResourceShareAssociationTypeDef]] = None
    receiverArn: Optional[str] = None

class ListPermissionAssociationsResponseTypeDef(BaseModel):
    permissions: List[AssociatedPermissionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePermissionRequestRequestTypeDef(BaseModel):
    name: str
    resourceType: str
    policyTemplate: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateResourceShareRequestRequestTypeDef(BaseModel):
    name: str
    resourceArns: Optional[Sequence[str]] = None
    principals: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    allowExternalPrincipals: Optional[bool] = None
    clientToken: Optional[str] = None
    permissionArns: Optional[Sequence[str]] = None
    sources: Optional[Sequence[str]] = None

class ResourceSharePermissionDetailTypeDef(BaseModel):
    arn: Optional[str] = None
    version: Optional[str] = None
    defaultVersion: Optional[bool] = None
    name: Optional[str] = None
    resourceType: Optional[str] = None
    permission: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    isResourceTypeDefault: Optional[bool] = None
    permissionType: Optional[PermissionTypeType] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    status: Optional[PermissionStatusType] = None
    tags: Optional[List[TagTypeDef]] = None

class ResourceSharePermissionSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    version: Optional[str] = None
    defaultVersion: Optional[bool] = None
    name: Optional[str] = None
    resourceType: Optional[str] = None
    status: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    isResourceTypeDefault: Optional[bool] = None
    permissionType: Optional[PermissionTypeType] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    tags: Optional[List[TagTypeDef]] = None

class ResourceShareTypeDef(BaseModel):
    resourceShareArn: Optional[str] = None
    name: Optional[str] = None
    owningAccountId: Optional[str] = None
    allowExternalPrincipals: Optional[bool] = None
    status: Optional[ResourceShareStatusType] = None
    statusMessage: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    featureSet: Optional[ResourceShareFeatureSetType] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    tags: Sequence[TagTypeDef]
    resourceShareArn: Optional[str] = None
    resourceArn: Optional[str] = None

class GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef(BaseModel):
    resourceArns: Sequence[str]
    principal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceShareAssociationsRequestGetResourceShareAssociationsPaginateTypeDef(BaseModel):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    principal: Optional[str] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceShareInvitationsRequestGetResourceShareInvitationsPaginateTypeDef(BaseModel):
    resourceShareInvitationArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalsRequestListPrincipalsPaginateTypeDef(BaseModel):
    resourceOwner: ResourceOwnerType
    resourceArn: Optional[str] = None
    principals: Optional[Sequence[str]] = None
    resourceType: Optional[str] = None
    resourceShareArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesRequestListResourcesPaginateTypeDef(BaseModel):
    resourceOwner: ResourceOwnerType
    principal: Optional[str] = None
    resourceType: Optional[str] = None
    resourceArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceSharesRequestGetResourceSharesPaginateTypeDef(BaseModel):
    resourceOwner: ResourceOwnerType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceShareStatus: Optional[ResourceShareStatusType] = None
    name: Optional[str] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceSharesRequestRequestTypeDef(BaseModel):
    resourceOwner: ResourceOwnerType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceShareStatus: Optional[ResourceShareStatusType] = None
    name: Optional[str] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None

class ListPendingInvitationResourcesResponseTypeDef(BaseModel):
    resources: List[ResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesResponseTypeDef(BaseModel):
    resources: List[ResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrincipalsResponseTypeDef(BaseModel):
    principals: List[PrincipalTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReplacePermissionAssociationsWorkResponseTypeDef(BaseModel):
    replacePermissionAssociationsWorks: List[ReplacePermissionAssociationsWorkTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplacePermissionAssociationsResponseTypeDef(BaseModel):
    replacePermissionAssociationsWork: ReplacePermissionAssociationsWorkTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceTypesResponseTypeDef(BaseModel):
    resourceTypes: List[ServiceNameAndResourceTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptResourceShareInvitationResponseTypeDef(BaseModel):
    resourceShareInvitation: ResourceShareInvitationTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceShareInvitationsResponseTypeDef(BaseModel):
    resourceShareInvitations: List[ResourceShareInvitationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectResourceShareInvitationResponseTypeDef(BaseModel):
    resourceShareInvitation: ResourceShareInvitationTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePermissionVersionResponseTypeDef(BaseModel):
    permission: ResourceSharePermissionDetailTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPermissionResponseTypeDef(BaseModel):
    permission: ResourceSharePermissionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePermissionResponseTypeDef(BaseModel):
    permission: ResourceSharePermissionSummaryTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionVersionsResponseTypeDef(BaseModel):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionsResponseTypeDef(BaseModel):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceSharePermissionsResponseTypeDef(BaseModel):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PromotePermissionCreatedFromPolicyResponseTypeDef(BaseModel):
    permission: ResourceSharePermissionSummaryTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateResourceShareResponseTypeDef(BaseModel):
    resourceShare: ResourceShareTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceSharesResponseTypeDef(BaseModel):
    resourceShares: List[ResourceShareTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourceShareResponseTypeDef(BaseModel):
    resourceShare: ResourceShareTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


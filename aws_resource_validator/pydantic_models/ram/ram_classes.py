from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ram.ram_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_resource_share_invitation' function.
class AcceptResourceShareInvitationRequest(BaseValidatorModel):
    resourceShareInvitationArn: str
    clientToken: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'associate_resource_share_permission' function.
class AssociateResourceSharePermissionRequest(BaseValidatorModel):
    resourceShareArn: str
    permissionArn: str
    replace: Optional[bool] = None
    clientToken: Optional[str] = None
    permissionVersion: Optional[int] = None


# This class is the input for the 'associate_resource_share' function.
class AssociateResourceShareRequest(BaseValidatorModel):
    resourceShareArn: str
    resourceArns: Optional[List[str]] = None
    principals: Optional[List[str]] = None
    clientToken: Optional[str] = None
    sources: Optional[List[str]] = None


class ResourceShareAssociation(BaseValidatorModel):
    resourceShareArn: Optional[str] = None
    resourceShareName: Optional[str] = None
    associatedEntity: Optional[str] = None
    associationType: Optional[ResourceShareAssociationTypeType] = None
    status: Optional[ResourceShareAssociationStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    external: Optional[bool] = None


class AssociatedPermission(BaseValidatorModel):
    arn: Optional[str] = None
    permissionVersion: Optional[str] = None
    defaultVersion: Optional[bool] = None
    resourceType: Optional[str] = None
    status: Optional[str] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    lastUpdatedTime: Optional[datetime] = None
    resourceShareArn: Optional[str] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


# This class is the input for the 'create_permission_version' function.
class CreatePermissionVersionRequest(BaseValidatorModel):
    permissionArn: str
    policyTemplate: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_permission' function.
class DeletePermissionRequest(BaseValidatorModel):
    permissionArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'delete_permission_version' function.
class DeletePermissionVersionRequest(BaseValidatorModel):
    permissionArn: str
    permissionVersion: int
    clientToken: Optional[str] = None


# This class is the input for the 'delete_resource_share' function.
class DeleteResourceShareRequest(BaseValidatorModel):
    resourceShareArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'disassociate_resource_share_permission' function.
class DisassociateResourceSharePermissionRequest(BaseValidatorModel):
    resourceShareArn: str
    permissionArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'disassociate_resource_share' function.
class DisassociateResourceShareRequest(BaseValidatorModel):
    resourceShareArn: str
    resourceArns: Optional[List[str]] = None
    principals: Optional[List[str]] = None
    clientToken: Optional[str] = None
    sources: Optional[List[str]] = None


# This class is the input for the 'get_permission' function.
class GetPermissionRequest(BaseValidatorModel):
    permissionArn: str
    permissionVersion: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'get_resource_policies' function.
class GetResourcePoliciesRequest(BaseValidatorModel):
    resourceArns: List[str]
    principal: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_resource_share_associations' function.
class GetResourceShareAssociationsRequest(BaseValidatorModel):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: Optional[List[str]] = None
    resourceArn: Optional[str] = None
    principal: Optional[str] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_resource_share_invitations' function.
class GetResourceShareInvitationsRequest(BaseValidatorModel):
    resourceShareInvitationArns: Optional[List[str]] = None
    resourceShareArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TagFilter(BaseValidatorModel):
    tagKey: Optional[str] = None
    tagValues: Optional[List[str]] = None


# This class is the input for the 'list_pending_invitation_resources' function.
class ListPendingInvitationResourcesRequest(BaseValidatorModel):
    resourceShareInvitationArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None


class Resource(BaseValidatorModel):
    arn: Optional[str] = None
    type: Optional[str] = None
    resourceShareArn: Optional[str] = None
    resourceGroupArn: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    resourceRegionScope: Optional[ResourceRegionScopeType] = None


# This class is the input for the 'list_permission_associations' function.
class ListPermissionAssociationsRequest(BaseValidatorModel):
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    resourceType: Optional[str] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    defaultVersion: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_permission_versions' function.
class ListPermissionVersionsRequest(BaseValidatorModel):
    permissionArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_permissions' function.
class ListPermissionsRequest(BaseValidatorModel):
    resourceType: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    permissionType: Optional[PermissionTypeFilterType] = None


# This class is the input for the 'list_principals' function.
class ListPrincipalsRequest(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceArn: Optional[str] = None
    principals: Optional[List[str]] = None
    resourceType: Optional[str] = None
    resourceShareArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class Principal(BaseValidatorModel):
    id: Optional[str] = None
    resourceShareArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    external: Optional[bool] = None


# This class is the input for the 'list_replace_permission_associations_work' function.
class ListReplacePermissionAssociationsWorkRequest(BaseValidatorModel):
    workIds: Optional[List[str]] = None
    status: Optional[ReplacePermissionAssociationsWorkStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ReplacePermissionAssociationsWork(BaseValidatorModel):
    id: Optional[str] = None
    fromPermissionArn: Optional[str] = None
    fromPermissionVersion: Optional[str] = None
    toPermissionArn: Optional[str] = None
    toPermissionVersion: Optional[str] = None
    status: Optional[ReplacePermissionAssociationsWorkStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None


# This class is the input for the 'list_resource_share_permissions' function.
class ListResourceSharePermissionsRequest(BaseValidatorModel):
    resourceShareArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_resource_types' function.
class ListResourceTypesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None


class ServiceNameAndResourceType(BaseValidatorModel):
    resourceType: Optional[str] = None
    serviceName: Optional[str] = None
    resourceRegionScope: Optional[ResourceRegionScopeType] = None


# This class is the input for the 'list_resources' function.
class ListResourcesRequest(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    principal: Optional[str] = None
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceShareArns: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None


# This class is the input for the 'promote_permission_created_from_policy' function.
class PromotePermissionCreatedFromPolicyRequest(BaseValidatorModel):
    permissionArn: str
    name: str
    clientToken: Optional[str] = None


# This class is the input for the 'promote_resource_share_created_from_policy' function.
class PromoteResourceShareCreatedFromPolicyRequest(BaseValidatorModel):
    resourceShareArn: str


# This class is the input for the 'reject_resource_share_invitation' function.
class RejectResourceShareInvitationRequest(BaseValidatorModel):
    resourceShareInvitationArn: str
    clientToken: Optional[str] = None


# This class is the input for the 'replace_permission_associations' function.
class ReplacePermissionAssociationsRequest(BaseValidatorModel):
    fromPermissionArn: str
    toPermissionArn: str
    fromPermissionVersion: Optional[int] = None
    clientToken: Optional[str] = None


# This class is the input for the 'set_default_permission_version' function.
class SetDefaultPermissionVersionRequest(BaseValidatorModel):
    permissionArn: str
    permissionVersion: int
    clientToken: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    tagKeys: List[str]
    resourceShareArn: Optional[str] = None
    resourceArn: Optional[str] = None


# This class is the input for the 'update_resource_share' function.
class UpdateResourceShareRequest(BaseValidatorModel):
    resourceShareArn: str
    name: Optional[str] = None
    allowExternalPrincipals: Optional[bool] = None
    clientToken: Optional[str] = None


# This class is the output for the 'associate_resource_share_permission' function.
class AssociateResourceSharePermissionResponse(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_permission' function.
class DeletePermissionResponse(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    permissionStatus: PermissionStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_permission_version' function.
class DeletePermissionVersionResponse(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    permissionStatus: PermissionStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_share' function.
class DeleteResourceShareResponse(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_resource_share_permission' function.
class DisassociateResourceSharePermissionResponse(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadata


class EnableSharingWithAwsOrganizationResponse(BaseValidatorModel):
    returnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policies' function.
class GetResourcePoliciesResponse(BaseValidatorModel):
    policies: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'promote_resource_share_created_from_policy' function.
class PromoteResourceShareCreatedFromPolicyResponse(BaseValidatorModel):
    returnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_default_permission_version' function.
class SetDefaultPermissionVersionResponse(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_resource_share' function.
class AssociateResourceShareResponse(BaseValidatorModel):
    resourceShareAssociations: List[ResourceShareAssociation]
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_resource_share' function.
class DisassociateResourceShareResponse(BaseValidatorModel):
    resourceShareAssociations: List[ResourceShareAssociation]
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_share_associations' function.
class GetResourceShareAssociationsResponse(BaseValidatorModel):
    resourceShareAssociations: List[ResourceShareAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ResourceShareInvitation(BaseValidatorModel):
    resourceShareInvitationArn: Optional[str] = None
    resourceShareName: Optional[str] = None
    resourceShareArn: Optional[str] = None
    senderAccountId: Optional[str] = None
    receiverAccountId: Optional[str] = None
    invitationTimestamp: Optional[datetime] = None
    status: Optional[ResourceShareInvitationStatusType] = None
    resourceShareAssociations: Optional[List[ResourceShareAssociation]] = None
    receiverArn: Optional[str] = None


# This class is the output for the 'list_permission_associations' function.
class ListPermissionAssociationsResponse(BaseValidatorModel):
    permissions: List[AssociatedPermission]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_permission' function.
class CreatePermissionRequest(BaseValidatorModel):
    name: str
    resourceType: str
    policyTemplate: str
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_resource_share' function.
class CreateResourceShareRequest(BaseValidatorModel):
    name: str
    resourceArns: Optional[List[str]] = None
    principals: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None
    allowExternalPrincipals: Optional[bool] = None
    clientToken: Optional[str] = None
    permissionArns: Optional[List[str]] = None
    sources: Optional[List[str]] = None


class ResourceSharePermissionDetail(BaseValidatorModel):
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
    tags: Optional[List[Tag]] = None


class ResourceSharePermissionSummary(BaseValidatorModel):
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
    tags: Optional[List[Tag]] = None


class ResourceShare(BaseValidatorModel):
    resourceShareArn: Optional[str] = None
    name: Optional[str] = None
    owningAccountId: Optional[str] = None
    allowExternalPrincipals: Optional[bool] = None
    status: Optional[ResourceShareStatusType] = None
    statusMessage: Optional[str] = None
    tags: Optional[List[Tag]] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    featureSet: Optional[ResourceShareFeatureSetType] = None


class TagResourceRequest(BaseValidatorModel):
    tags: List[Tag]
    resourceShareArn: Optional[str] = None
    resourceArn: Optional[str] = None


class GetResourcePoliciesRequestPaginate(BaseValidatorModel):
    resourceArns: List[str]
    principal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourceShareAssociationsRequestPaginate(BaseValidatorModel):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: Optional[List[str]] = None
    resourceArn: Optional[str] = None
    principal: Optional[str] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourceShareInvitationsRequestPaginate(BaseValidatorModel):
    resourceShareInvitationArns: Optional[List[str]] = None
    resourceShareArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPrincipalsRequestPaginate(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceArn: Optional[str] = None
    principals: Optional[List[str]] = None
    resourceType: Optional[str] = None
    resourceShareArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourcesRequestPaginate(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    principal: Optional[str] = None
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceShareArns: Optional[List[str]] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourceSharesRequestPaginate(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceShareArns: Optional[List[str]] = None
    resourceShareStatus: Optional[ResourceShareStatusType] = None
    name: Optional[str] = None
    tagFilters: Optional[List[TagFilter]] = None
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_resource_shares' function.
class GetResourceSharesRequest(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceShareArns: Optional[List[str]] = None
    resourceShareStatus: Optional[ResourceShareStatusType] = None
    name: Optional[str] = None
    tagFilters: Optional[List[TagFilter]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None


# This class is the output for the 'list_pending_invitation_resources' function.
class ListPendingInvitationResourcesResponse(BaseValidatorModel):
    resources: List[Resource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_resources' function.
class ListResourcesResponse(BaseValidatorModel):
    resources: List[Resource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_principals' function.
class ListPrincipalsResponse(BaseValidatorModel):
    principals: List[Principal]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_replace_permission_associations_work' function.
class ListReplacePermissionAssociationsWorkResponse(BaseValidatorModel):
    replacePermissionAssociationsWorks: List[ReplacePermissionAssociationsWork]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'replace_permission_associations' function.
class ReplacePermissionAssociationsResponse(BaseValidatorModel):
    replacePermissionAssociationsWork: ReplacePermissionAssociationsWork
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resource_types' function.
class ListResourceTypesResponse(BaseValidatorModel):
    resourceTypes: List[ServiceNameAndResourceType]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'accept_resource_share_invitation' function.
class AcceptResourceShareInvitationResponse(BaseValidatorModel):
    resourceShareInvitation: ResourceShareInvitation
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_share_invitations' function.
class GetResourceShareInvitationsResponse(BaseValidatorModel):
    resourceShareInvitations: List[ResourceShareInvitation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'reject_resource_share_invitation' function.
class RejectResourceShareInvitationResponse(BaseValidatorModel):
    resourceShareInvitation: ResourceShareInvitation
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_permission_version' function.
class CreatePermissionVersionResponse(BaseValidatorModel):
    permission: ResourceSharePermissionDetail
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_permission' function.
class GetPermissionResponse(BaseValidatorModel):
    permission: ResourceSharePermissionDetail
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_permission' function.
class CreatePermissionResponse(BaseValidatorModel):
    permission: ResourceSharePermissionSummary
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_permission_versions' function.
class ListPermissionVersionsResponse(BaseValidatorModel):
    permissions: List[ResourceSharePermissionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_permissions' function.
class ListPermissionsResponse(BaseValidatorModel):
    permissions: List[ResourceSharePermissionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_resource_share_permissions' function.
class ListResourceSharePermissionsResponse(BaseValidatorModel):
    permissions: List[ResourceSharePermissionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'promote_permission_created_from_policy' function.
class PromotePermissionCreatedFromPolicyResponse(BaseValidatorModel):
    permission: ResourceSharePermissionSummary
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_resource_share' function.
class CreateResourceShareResponse(BaseValidatorModel):
    resourceShare: ResourceShare
    clientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_shares' function.
class GetResourceSharesResponse(BaseValidatorModel):
    resourceShares: List[ResourceShare]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_resource_share' function.
class UpdateResourceShareResponse(BaseValidatorModel):
    resourceShare: ResourceShare
    clientToken: str
    ResponseMetadata: ResponseMetadata
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
from aws_resource_validator.pydantic_models.ram_constants import *

class AcceptResourceShareInvitationRequestTypeDef(BaseValidatorModel):
    resourceShareInvitationArn: str
    clientToken: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociateResourceSharePermissionRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    permissionArn: str
    replace: Optional[bool] = None
    clientToken: Optional[str] = None
    permissionVersion: Optional[int] = None


class AssociateResourceShareRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    resourceArns: Optional[Sequence[str]] = None
    principals: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    sources: Optional[Sequence[str]] = None


class ResourceShareAssociationTypeDef(BaseValidatorModel):
    resourceShareArn: Optional[str] = None
    resourceShareName: Optional[str] = None
    associatedEntity: Optional[str] = None
    associationType: Optional[ResourceShareAssociationTypeType] = None
    status: Optional[ResourceShareAssociationStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    external: Optional[bool] = None


class AssociatedPermissionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    permissionVersion: Optional[str] = None
    defaultVersion: Optional[bool] = None
    resourceType: Optional[str] = None
    status: Optional[str] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    lastUpdatedTime: Optional[datetime] = None
    resourceShareArn: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class CreatePermissionVersionRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    policyTemplate: str
    clientToken: Optional[str] = None


class DeletePermissionRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    clientToken: Optional[str] = None


class DeletePermissionVersionRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    permissionVersion: int
    clientToken: Optional[str] = None


class DeleteResourceShareRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    clientToken: Optional[str] = None


class DisassociateResourceSharePermissionRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    permissionArn: str
    clientToken: Optional[str] = None


class DisassociateResourceShareRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    resourceArns: Optional[Sequence[str]] = None
    principals: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    sources: Optional[Sequence[str]] = None


class GetPermissionRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    permissionVersion: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetResourcePoliciesRequestTypeDef(BaseValidatorModel):
    resourceArns: Sequence[str]
    principal: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetResourceShareAssociationsRequestTypeDef(BaseValidatorModel):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    principal: Optional[str] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetResourceShareInvitationsRequestTypeDef(BaseValidatorModel):
    resourceShareInvitationArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TagFilterTypeDef(BaseValidatorModel):
    tagKey: Optional[str] = None
    tagValues: Optional[Sequence[str]] = None


class ListPendingInvitationResourcesRequestTypeDef(BaseValidatorModel):
    resourceShareInvitationArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None


class ListPermissionAssociationsRequestTypeDef(BaseValidatorModel):
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    resourceType: Optional[str] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    defaultVersion: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPermissionVersionsRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPermissionsRequestTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    permissionType: Optional[PermissionTypeFilterType] = None


class ListPrincipalsRequestTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceArn: Optional[str] = None
    principals: Optional[Sequence[str]] = None
    resourceType: Optional[str] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListReplacePermissionAssociationsWorkRequestTypeDef(BaseValidatorModel):
    workIds: Optional[Sequence[str]] = None
    status: Optional[ReplacePermissionAssociationsWorkStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListResourceSharePermissionsRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListResourceTypesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None


class ServiceNameAndResourceTypeTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    serviceName: Optional[str] = None
    resourceRegionScope: Optional[ResourceRegionScopeType] = None


class ListResourcesRequestTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    principal: Optional[str] = None
    resourceType: Optional[str] = None
    resourceArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None


class PromotePermissionCreatedFromPolicyRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    name: str
    clientToken: Optional[str] = None


class PromoteResourceShareCreatedFromPolicyRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str


class RejectResourceShareInvitationRequestTypeDef(BaseValidatorModel):
    resourceShareInvitationArn: str
    clientToken: Optional[str] = None


class ReplacePermissionAssociationsRequestTypeDef(BaseValidatorModel):
    fromPermissionArn: str
    toPermissionArn: str
    fromPermissionVersion: Optional[int] = None
    clientToken: Optional[str] = None


class SetDefaultPermissionVersionRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    permissionVersion: int
    clientToken: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    tagKeys: Sequence[str]
    resourceShareArn: Optional[str] = None
    resourceArn: Optional[str] = None


class UpdateResourceShareRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    name: Optional[str] = None
    allowExternalPrincipals: Optional[bool] = None
    clientToken: Optional[str] = None


class AssociateResourceSharePermissionResponseTypeDef(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePermissionResponseTypeDef(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    permissionStatus: PermissionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePermissionVersionResponseTypeDef(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    permissionStatus: PermissionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteResourceShareResponseTypeDef(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateResourceSharePermissionResponseTypeDef(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class EnableSharingWithAwsOrganizationResponseTypeDef(BaseValidatorModel):
    returnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePoliciesResponseTypeDef(BaseValidatorModel):
    policies: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PromoteResourceShareCreatedFromPolicyResponseTypeDef(BaseValidatorModel):
    returnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef


class SetDefaultPermissionVersionResponseTypeDef(BaseValidatorModel):
    returnValue: bool
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateResourceShareResponseTypeDef(BaseValidatorModel):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateResourceShareResponseTypeDef(BaseValidatorModel):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceShareAssociationsResponseTypeDef(BaseValidatorModel):
    resourceShareAssociations: List[ResourceShareAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ResourceShareInvitationTypeDef(BaseValidatorModel):
    resourceShareInvitationArn: Optional[str] = None
    resourceShareName: Optional[str] = None
    resourceShareArn: Optional[str] = None
    senderAccountId: Optional[str] = None
    receiverAccountId: Optional[str] = None
    invitationTimestamp: Optional[datetime] = None
    status: Optional[ResourceShareInvitationStatusType] = None
    resourceShareAssociations: Optional[List[ResourceShareAssociationTypeDef]] = None
    receiverArn: Optional[str] = None


class ListPermissionAssociationsResponseTypeDef(BaseValidatorModel):
    permissions: List[AssociatedPermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreatePermissionRequestTypeDef(BaseValidatorModel):
    name: str
    resourceType: str
    policyTemplate: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateResourceShareRequestTypeDef(BaseValidatorModel):
    name: str
    resourceArns: Optional[Sequence[str]] = None
    principals: Optional[Sequence[str]] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    allowExternalPrincipals: Optional[bool] = None
    clientToken: Optional[str] = None
    permissionArns: Optional[Sequence[str]] = None
    sources: Optional[Sequence[str]] = None


class ResourceSharePermissionDetailTypeDef(BaseValidatorModel):
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


class ResourceSharePermissionSummaryTypeDef(BaseValidatorModel):
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


class ResourceShareTypeDef(BaseValidatorModel):
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


class TagResourceRequestTypeDef(BaseValidatorModel):
    tags: Sequence[TagTypeDef]
    resourceShareArn: Optional[str] = None
    resourceArn: Optional[str] = None


class GetResourcePoliciesRequestPaginateTypeDef(BaseValidatorModel):
    resourceArns: Sequence[str]
    principal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourceShareAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    principal: Optional[str] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourceShareInvitationsRequestPaginateTypeDef(BaseValidatorModel):
    resourceShareInvitationArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPrincipalsRequestPaginateTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceArn: Optional[str] = None
    principals: Optional[Sequence[str]] = None
    resourceType: Optional[str] = None
    resourceShareArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourcesRequestPaginateTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    principal: Optional[str] = None
    resourceType: Optional[str] = None
    resourceArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourceSharesRequestPaginateTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceShareStatus: Optional[ResourceShareStatusType] = None
    name: Optional[str] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourceSharesRequestTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceShareStatus: Optional[ResourceShareStatusType] = None
    name: Optional[str] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None


class ResourceTypeDef(BaseValidatorModel):
    pass


class ListPendingInvitationResourcesResponseTypeDef(BaseValidatorModel):
    resources: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListResourcesResponseTypeDef(BaseValidatorModel):
    resources: List[ResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PrincipalTypeDef(BaseValidatorModel):
    pass


class ListPrincipalsResponseTypeDef(BaseValidatorModel):
    principals: List[PrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ReplacePermissionAssociationsWorkTypeDef(BaseValidatorModel):
    pass


class ListReplacePermissionAssociationsWorkResponseTypeDef(BaseValidatorModel):
    replacePermissionAssociationsWorks: List[ReplacePermissionAssociationsWorkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ReplacePermissionAssociationsResponseTypeDef(BaseValidatorModel):
    replacePermissionAssociationsWork: ReplacePermissionAssociationsWorkTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourceTypesResponseTypeDef(BaseValidatorModel):
    resourceTypes: List[ServiceNameAndResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AcceptResourceShareInvitationResponseTypeDef(BaseValidatorModel):
    resourceShareInvitation: ResourceShareInvitationTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceShareInvitationsResponseTypeDef(BaseValidatorModel):
    resourceShareInvitations: List[ResourceShareInvitationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RejectResourceShareInvitationResponseTypeDef(BaseValidatorModel):
    resourceShareInvitation: ResourceShareInvitationTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePermissionVersionResponseTypeDef(BaseValidatorModel):
    permission: ResourceSharePermissionDetailTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPermissionResponseTypeDef(BaseValidatorModel):
    permission: ResourceSharePermissionDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePermissionResponseTypeDef(BaseValidatorModel):
    permission: ResourceSharePermissionSummaryTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPermissionVersionsResponseTypeDef(BaseValidatorModel):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPermissionsResponseTypeDef(BaseValidatorModel):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListResourceSharePermissionsResponseTypeDef(BaseValidatorModel):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PromotePermissionCreatedFromPolicyResponseTypeDef(BaseValidatorModel):
    permission: ResourceSharePermissionSummaryTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateResourceShareResponseTypeDef(BaseValidatorModel):
    resourceShare: ResourceShareTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourceSharesResponseTypeDef(BaseValidatorModel):
    resourceShares: List[ResourceShareTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateResourceShareResponseTypeDef(BaseValidatorModel):
    resourceShare: ResourceShareTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef



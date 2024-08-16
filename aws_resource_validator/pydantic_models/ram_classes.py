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
from aws_resource_validator.pydantic_models.ram_constants import *

class AcceptResourceShareInvitationRequestRequestTypeDef(BaseValidatorModel):
    resourceShareInvitationArn: str
    clientToken: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociateResourceSharePermissionRequestRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    permissionArn: str
    replace: Optional[bool] = None
    clientToken: Optional[str] = None
    permissionVersion: Optional[int] = None

class AssociateResourceShareRequestRequestTypeDef(BaseValidatorModel):
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

class CreatePermissionVersionRequestRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    policyTemplate: str
    clientToken: Optional[str] = None

class DeletePermissionRequestRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    clientToken: Optional[str] = None

class DeletePermissionVersionRequestRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    permissionVersion: int
    clientToken: Optional[str] = None

class DeleteResourceShareRequestRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    clientToken: Optional[str] = None

class DisassociateResourceSharePermissionRequestRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    permissionArn: str
    clientToken: Optional[str] = None

class DisassociateResourceShareRequestRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    resourceArns: Optional[Sequence[str]] = None
    principals: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    sources: Optional[Sequence[str]] = None

class GetPermissionRequestRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    permissionVersion: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetResourcePoliciesRequestRequestTypeDef(BaseValidatorModel):
    resourceArns: Sequence[str]
    principal: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetResourceShareAssociationsRequestRequestTypeDef(BaseValidatorModel):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    principal: Optional[str] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetResourceShareInvitationsRequestRequestTypeDef(BaseValidatorModel):
    resourceShareInvitationArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class TagFilterTypeDef(BaseValidatorModel):
    tagKey: Optional[str] = None
    tagValues: Optional[Sequence[str]] = None

class ListPendingInvitationResourcesRequestRequestTypeDef(BaseValidatorModel):
    resourceShareInvitationArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None

class ResourceTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    type: Optional[str] = None
    resourceShareArn: Optional[str] = None
    resourceGroupArn: Optional[str] = None
    status: Optional[ResourceStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    resourceRegionScope: Optional[ResourceRegionScopeType] = None

class ListPermissionAssociationsRequestRequestTypeDef(BaseValidatorModel):
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    resourceType: Optional[str] = None
    featureSet: Optional[PermissionFeatureSetType] = None
    defaultVersion: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPermissionVersionsRequestRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPermissionsRequestRequestTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    permissionType: Optional[PermissionTypeFilterType] = None

class ListPrincipalsRequestRequestTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceArn: Optional[str] = None
    principals: Optional[Sequence[str]] = None
    resourceType: Optional[str] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PrincipalTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    resourceShareArn: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    external: Optional[bool] = None

class ListReplacePermissionAssociationsWorkRequestRequestTypeDef(BaseValidatorModel):
    workIds: Optional[Sequence[str]] = None
    status: Optional[ReplacePermissionAssociationsWorkStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ReplacePermissionAssociationsWorkTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    fromPermissionArn: Optional[str] = None
    fromPermissionVersion: Optional[str] = None
    toPermissionArn: Optional[str] = None
    toPermissionVersion: Optional[str] = None
    status: Optional[ReplacePermissionAssociationsWorkStatusType] = None
    statusMessage: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None

class ListResourceSharePermissionsRequestRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListResourceTypesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None

class ServiceNameAndResourceTypeTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    serviceName: Optional[str] = None
    resourceRegionScope: Optional[ResourceRegionScopeType] = None

class ListResourcesRequestRequestTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    principal: Optional[str] = None
    resourceType: Optional[str] = None
    resourceArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None

class PromotePermissionCreatedFromPolicyRequestRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    name: str
    clientToken: Optional[str] = None

class PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceShareArn: str

class RejectResourceShareInvitationRequestRequestTypeDef(BaseValidatorModel):
    resourceShareInvitationArn: str
    clientToken: Optional[str] = None

class ReplacePermissionAssociationsRequestRequestTypeDef(BaseValidatorModel):
    fromPermissionArn: str
    toPermissionArn: str
    fromPermissionVersion: Optional[int] = None
    clientToken: Optional[str] = None

class SetDefaultPermissionVersionRequestRequestTypeDef(BaseValidatorModel):
    permissionArn: str
    permissionVersion: int
    clientToken: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    tagKeys: Sequence[str]
    resourceShareArn: Optional[str] = None
    resourceArn: Optional[str] = None

class UpdateResourceShareRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePermissionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    resourceType: str
    policyTemplate: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateResourceShareRequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    tags: Sequence[TagTypeDef]
    resourceShareArn: Optional[str] = None
    resourceArn: Optional[str] = None

class GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef(BaseValidatorModel):
    resourceArns: Sequence[str]
    principal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceShareAssociationsRequestGetResourceShareAssociationsPaginateTypeDef(BaseValidatorModel):
    associationType: ResourceShareAssociationTypeType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceArn: Optional[str] = None
    principal: Optional[str] = None
    associationStatus: Optional[ResourceShareAssociationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceShareInvitationsRequestGetResourceShareInvitationsPaginateTypeDef(BaseValidatorModel):
    resourceShareInvitationArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPrincipalsRequestListPrincipalsPaginateTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceArn: Optional[str] = None
    principals: Optional[Sequence[str]] = None
    resourceType: Optional[str] = None
    resourceShareArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListResourcesRequestListResourcesPaginateTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    principal: Optional[str] = None
    resourceType: Optional[str] = None
    resourceArns: Optional[Sequence[str]] = None
    resourceShareArns: Optional[Sequence[str]] = None
    resourceRegionScope: Optional[ResourceRegionScopeFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceSharesRequestGetResourceSharesPaginateTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceShareStatus: Optional[ResourceShareStatusType] = None
    name: Optional[str] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourceSharesRequestRequestTypeDef(BaseValidatorModel):
    resourceOwner: ResourceOwnerType
    resourceShareArns: Optional[Sequence[str]] = None
    resourceShareStatus: Optional[ResourceShareStatusType] = None
    name: Optional[str] = None
    tagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    permissionArn: Optional[str] = None
    permissionVersion: Optional[int] = None

class ListPendingInvitationResourcesResponseTypeDef(BaseValidatorModel):
    resources: List[ResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourcesResponseTypeDef(BaseValidatorModel):
    resources: List[ResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPrincipalsResponseTypeDef(BaseValidatorModel):
    principals: List[PrincipalTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListReplacePermissionAssociationsWorkResponseTypeDef(BaseValidatorModel):
    replacePermissionAssociationsWorks: List[ReplacePermissionAssociationsWorkTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplacePermissionAssociationsResponseTypeDef(BaseValidatorModel):
    replacePermissionAssociationsWork: ReplacePermissionAssociationsWorkTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceTypesResponseTypeDef(BaseValidatorModel):
    resourceTypes: List[ServiceNameAndResourceTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptResourceShareInvitationResponseTypeDef(BaseValidatorModel):
    resourceShareInvitation: ResourceShareInvitationTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourceShareInvitationsResponseTypeDef(BaseValidatorModel):
    resourceShareInvitations: List[ResourceShareInvitationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPermissionsResponseTypeDef(BaseValidatorModel):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListResourceSharePermissionsResponseTypeDef(BaseValidatorModel):
    permissions: List[ResourceSharePermissionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateResourceShareResponseTypeDef(BaseValidatorModel):
    resourceShare: ResourceShareTypeDef
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


# Ram Ram Classes

# AcceptResourceShareInvitationRequest

### resourceShareInvitationArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AcceptResourceShareInvitationResponse

### resourceShareInvitation
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShareInvitation'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateResourceSharePermissionRequest

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### replace
- **Type**: typing.Optional[bool]

### clientToken
- **Type**: typing.Optional[str]

### permissionVersion
- **Type**: typing.Optional[int]


# AssociateResourceSharePermissionResponse

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateResourceShareRequest

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### principals
- **Type**: typing.Optional[typing.List[str]]

### clientToken
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.List[str]]


# AssociateResourceShareResponse

### resourceShareAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShareAssociation]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatedPermission

### arn
- **Type**: typing.Optional[str]

### permissionVersion
- **Type**: typing.Optional[str]

### defaultVersion
- **Type**: typing.Optional[bool]

### resourceType
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### featureSet
- **Type**: typing.Optional[typing.Literal['CREATED_FROM_POLICY', 'PROMOTING_TO_STANDARD', 'STANDARD']]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### resourceShareArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreatePermissionRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Tag]]


# CreatePermissionResponse

### permission
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResourceSharePermissionSummary'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePermissionVersionRequest

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreatePermissionVersionResponse

### permission
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResourceSharePermissionDetail'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceShareRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### principals
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Tag]]

### allowExternalPrincipals
- **Type**: typing.Optional[bool]

### clientToken
- **Type**: typing.Optional[str]

### permissionArns
- **Type**: typing.Optional[typing.List[str]]

### sources
- **Type**: typing.Optional[typing.List[str]]


# CreateResourceShareResponse

### resourceShare
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShare'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePermissionRequest

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePermissionResponse

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### permissionStatus
- **Type**: typing.Literal['ATTACHABLE', 'DELETED', 'DELETING', 'UNATTACHABLE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePermissionVersionRequest

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionVersion
- **Type**: <class 'int'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePermissionVersionResponse

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### permissionStatus
- **Type**: typing.Literal['ATTACHABLE', 'DELETED', 'DELETING', 'UNATTACHABLE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteResourceShareRequest

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteResourceShareResponse

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateResourceSharePermissionRequest

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DisassociateResourceSharePermissionResponse

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateResourceShareRequest

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### principals
- **Type**: typing.Optional[typing.List[str]]

### clientToken
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.List[str]]


# DisassociateResourceShareResponse

### resourceShareAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShareAssociation]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# EnableSharingWithAwsOrganizationResponse

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# GetPermissionRequest

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionVersion
- **Type**: typing.Optional[int]


# GetPermissionResponse

### permission
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResourceSharePermissionDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourcePoliciesRequest

### resourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetResourcePoliciesRequestPaginate

### resourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram.ram_classes.PaginatorConfig]


# GetResourcePoliciesResponse

### policies
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResourceShareAssociationsRequest

### associationType
- **Type**: typing.Literal['PRINCIPAL', 'RESOURCE']
- **Required**: Yes

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### resourceArn
- **Type**: typing.Optional[str]

### principal
- **Type**: typing.Optional[str]

### associationStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'ASSOCIATING', 'DISASSOCIATED', 'DISASSOCIATING', 'FAILED']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetResourceShareAssociationsRequestPaginate

### associationType
- **Type**: typing.Literal['PRINCIPAL', 'RESOURCE']
- **Required**: Yes

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### resourceArn
- **Type**: typing.Optional[str]

### principal
- **Type**: typing.Optional[str]

### associationStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'ASSOCIATING', 'DISASSOCIATED', 'DISASSOCIATING', 'FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram.ram_classes.PaginatorConfig]


# GetResourceShareAssociationsResponse

### resourceShareAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShareAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResourceShareInvitationsRequest

### resourceShareInvitationArns
- **Type**: typing.Optional[typing.List[str]]

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetResourceShareInvitationsRequestPaginate

### resourceShareInvitationArns
- **Type**: typing.Optional[typing.List[str]]

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram.ram_classes.PaginatorConfig]


# GetResourceShareInvitationsResponse

### resourceShareInvitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShareInvitation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResourceSharesRequest

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### resourceShareStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]

### name
- **Type**: typing.Optional[str]

### tagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.TagFilter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### permissionArn
- **Type**: typing.Optional[str]

### permissionVersion
- **Type**: typing.Optional[int]


# GetResourceSharesRequestPaginate

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### resourceShareStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]

### name
- **Type**: typing.Optional[str]

### tagFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.TagFilter]]

### permissionArn
- **Type**: typing.Optional[str]

### permissionVersion
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram.ram_classes.PaginatorConfig]


# GetResourceSharesResponse

### resourceShares
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShare]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPendingInvitationResourcesRequest

### resourceShareInvitationArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['ALL', 'GLOBAL', 'REGIONAL']]


# ListPendingInvitationResourcesResponse

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Resource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionAssociationsRequest

### permissionArn
- **Type**: typing.Optional[str]

### permissionVersion
- **Type**: typing.Optional[int]

### associationStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'ASSOCIATING', 'DISASSOCIATED', 'DISASSOCIATING', 'FAILED']]

### resourceType
- **Type**: typing.Optional[str]

### featureSet
- **Type**: typing.Optional[typing.Literal['CREATED_FROM_POLICY', 'PROMOTING_TO_STANDARD', 'STANDARD']]

### defaultVersion
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPermissionAssociationsResponse

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.AssociatedPermission]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionVersionsRequest

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPermissionVersionsResponse

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceSharePermissionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionsRequest

### resourceType
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### permissionType
- **Type**: typing.Optional[typing.Literal['ALL', 'AWS_MANAGED', 'CUSTOMER_MANAGED']]


# ListPermissionsResponse

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceSharePermissionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrincipalsRequest

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### resourceArn
- **Type**: typing.Optional[str]

### principals
- **Type**: typing.Optional[typing.List[str]]

### resourceType
- **Type**: typing.Optional[str]

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrincipalsRequestPaginate

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### resourceArn
- **Type**: typing.Optional[str]

### principals
- **Type**: typing.Optional[typing.List[str]]

### resourceType
- **Type**: typing.Optional[str]

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram.ram_classes.PaginatorConfig]


# ListPrincipalsResponse

### principals
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Principal]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReplacePermissionAssociationsWorkRequest

### workIds
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListReplacePermissionAssociationsWorkResponse

### replacePermissionAssociationsWorks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ReplacePermissionAssociationsWork]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceSharePermissionsRequest

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListResourceSharePermissionsResponse

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceSharePermissionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceTypesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['ALL', 'GLOBAL', 'REGIONAL']]


# ListResourceTypesResponse

### resourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ServiceNameAndResourceType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourcesRequest

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['ALL', 'GLOBAL', 'REGIONAL']]


# ListResourcesRequestPaginate

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceShareArns
- **Type**: typing.Optional[typing.List[str]]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['ALL', 'GLOBAL', 'REGIONAL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram.ram_classes.PaginatorConfig]


# ListResourcesResponse

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Resource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Principal

### id
- **Type**: typing.Optional[str]

### resourceShareArn
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### external
- **Type**: typing.Optional[bool]


# PromotePermissionCreatedFromPolicyRequest

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PromotePermissionCreatedFromPolicyResponse

### permission
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResourceSharePermissionSummary'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# PromoteResourceShareCreatedFromPolicyRequest

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes


# PromoteResourceShareCreatedFromPolicyResponse

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# RejectResourceShareInvitationRequest

### resourceShareInvitationArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# RejectResourceShareInvitationResponse

### resourceShareInvitation
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShareInvitation'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# ReplacePermissionAssociationsRequest

### fromPermissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### toPermissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### fromPermissionVersion
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]


# ReplacePermissionAssociationsResponse

### replacePermissionAssociationsWork
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ReplacePermissionAssociationsWork'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# ReplacePermissionAssociationsWork

### id
- **Type**: typing.Optional[str]

### fromPermissionArn
- **Type**: typing.Optional[str]

### fromPermissionVersion
- **Type**: typing.Optional[str]

### toPermissionArn
- **Type**: typing.Optional[str]

### toPermissionVersion
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### statusMessage
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# Resource

### arn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### resourceShareArn
- **Type**: typing.Optional[str]

### resourceGroupArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'LIMIT_EXCEEDED', 'PENDING', 'UNAVAILABLE', 'ZONAL_RESOURCE_INACCESSIBLE']]

### statusMessage
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['GLOBAL', 'REGIONAL']]


# ResourceShare

### resourceShareArn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### owningAccountId
- **Type**: typing.Optional[str]

### allowExternalPrincipals
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]

### statusMessage
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Tag]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### featureSet
- **Type**: typing.Optional[typing.Literal['CREATED_FROM_POLICY', 'PROMOTING_TO_STANDARD', 'STANDARD']]


# ResourceShareAssociation

### resourceShareArn
- **Type**: typing.Optional[str]

### resourceShareName
- **Type**: typing.Optional[str]

### associatedEntity
- **Type**: typing.Optional[str]

### associationType
- **Type**: typing.Optional[typing.Literal['PRINCIPAL', 'RESOURCE']]

### status
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'ASSOCIATING', 'DISASSOCIATED', 'DISASSOCIATING', 'FAILED']]

### statusMessage
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### external
- **Type**: typing.Optional[bool]


# ResourceShareInvitation

### resourceShareInvitationArn
- **Type**: typing.Optional[str]

### resourceShareName
- **Type**: typing.Optional[str]

### resourceShareArn
- **Type**: typing.Optional[str]

### senderAccountId
- **Type**: typing.Optional[str]

### receiverAccountId
- **Type**: typing.Optional[str]

### invitationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACCEPTED', 'EXPIRED', 'PENDING', 'REJECTED']]

### resourceShareAssociations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShareAssociation]]

### receiverArn
- **Type**: typing.Optional[str]


# ResourceSharePermissionDetail

### arn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### defaultVersion
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]

### permission
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### isResourceTypeDefault
- **Type**: typing.Optional[bool]

### permissionType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOMER_MANAGED']]

### featureSet
- **Type**: typing.Optional[typing.Literal['CREATED_FROM_POLICY', 'PROMOTING_TO_STANDARD', 'STANDARD']]

### status
- **Type**: typing.Optional[typing.Literal['ATTACHABLE', 'DELETED', 'DELETING', 'UNATTACHABLE']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Tag]]


# ResourceSharePermissionSummary

### arn
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### defaultVersion
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### isResourceTypeDefault
- **Type**: typing.Optional[bool]

### permissionType
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOMER_MANAGED']]

### featureSet
- **Type**: typing.Optional[typing.Literal['CREATED_FROM_POLICY', 'PROMOTING_TO_STANDARD', 'STANDARD']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Tag]]


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# ServiceNameAndResourceType

### resourceType
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['GLOBAL', 'REGIONAL']]


# SetDefaultPermissionVersionRequest

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionVersion
- **Type**: <class 'int'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# SetDefaultPermissionVersionResponse

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TagFilter

### tagKey
- **Type**: typing.Optional[str]

### tagValues
- **Type**: typing.Optional[typing.List[str]]


# TagResourceRequest

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram.ram_classes.Tag]
- **Required**: Yes

### resourceShareArn
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]


# UntagResourceRequest

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes

### resourceShareArn
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]


# UpdateResourceShareRequest

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### allowExternalPrincipals
- **Type**: typing.Optional[bool]

### clientToken
- **Type**: typing.Optional[str]


# UpdateResourceShareResponse

### resourceShare
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResourceShare'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram.ram_classes.ResponseMetadata'>
- **Required**: Yes



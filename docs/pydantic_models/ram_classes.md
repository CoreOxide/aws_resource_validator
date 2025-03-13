# Ram Classes

# AcceptResourceShareInvitationRequestTypeDef

### resourceShareInvitationArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# AcceptResourceShareInvitationResponseTypeDef

### resourceShareInvitation
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResourceShareInvitationTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateResourceSharePermissionRequestTypeDef

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


# AssociateResourceSharePermissionResponseTypeDef

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateResourceShareRequestTypeDef

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### principals
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.Sequence[str]]


# AssociateResourceShareResponseTypeDef

### resourceShareAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceShareAssociationTypeDef]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatedPermissionTypeDef

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

# CreatePermissionRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ram_classes.TagTypeDef]]


# CreatePermissionResponseTypeDef

### permission
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResourceSharePermissionSummaryTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePermissionVersionRequestTypeDef

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplate
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreatePermissionVersionResponseTypeDef

### permission
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResourceSharePermissionDetailTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceShareRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### principals
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ram_classes.TagTypeDef]]

### allowExternalPrincipals
- **Type**: typing.Optional[bool]

### clientToken
- **Type**: typing.Optional[str]

### permissionArns
- **Type**: typing.Optional[typing.Sequence[str]]

### sources
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateResourceShareResponseTypeDef

### resourceShare
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResourceShareTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePermissionRequestTypeDef

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePermissionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePermissionVersionRequestTypeDef

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionVersion
- **Type**: <class 'int'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeletePermissionVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteResourceShareRequestTypeDef

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteResourceShareResponseTypeDef

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateResourceSharePermissionRequestTypeDef

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DisassociateResourceSharePermissionResponseTypeDef

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateResourceShareRequestTypeDef

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### principals
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.Sequence[str]]


# DisassociateResourceShareResponseTypeDef

### resourceShareAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceShareAssociationTypeDef]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableSharingWithAwsOrganizationResponseTypeDef

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPermissionRequestTypeDef

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionVersion
- **Type**: typing.Optional[int]


# GetPermissionResponseTypeDef

### permission
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResourceSharePermissionDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourcePoliciesRequestPaginateTypeDef

### resourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram_classes.PaginatorConfigTypeDef]


# GetResourcePoliciesRequestTypeDef

### resourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetResourcePoliciesResponseTypeDef

### policies
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResourceShareAssociationsRequestPaginateTypeDef

### associationType
- **Type**: typing.Literal['PRINCIPAL', 'RESOURCE']
- **Required**: Yes

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceArn
- **Type**: typing.Optional[str]

### principal
- **Type**: typing.Optional[str]

### associationStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED', 'ASSOCIATING', 'DISASSOCIATED', 'DISASSOCIATING', 'FAILED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram_classes.PaginatorConfigTypeDef]


# GetResourceShareAssociationsRequestTypeDef

### associationType
- **Type**: typing.Literal['PRINCIPAL', 'RESOURCE']
- **Required**: Yes

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

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


# GetResourceShareAssociationsResponseTypeDef

### resourceShareAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceShareAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResourceShareInvitationsRequestPaginateTypeDef

### resourceShareInvitationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram_classes.PaginatorConfigTypeDef]


# GetResourceShareInvitationsRequestTypeDef

### resourceShareInvitationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# GetResourceShareInvitationsResponseTypeDef

### resourceShareInvitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceShareInvitationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetResourceSharesRequestPaginateTypeDef

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceShareStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]

### name
- **Type**: typing.Optional[str]

### tagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ram_classes.TagFilterTypeDef]]

### permissionArn
- **Type**: typing.Optional[str]

### permissionVersion
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram_classes.PaginatorConfigTypeDef]


# GetResourceSharesRequestTypeDef

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceShareStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DELETING', 'FAILED', 'PENDING']]

### name
- **Type**: typing.Optional[str]

### tagFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ram_classes.TagFilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### permissionArn
- **Type**: typing.Optional[str]

### permissionVersion
- **Type**: typing.Optional[int]


# GetResourceSharesResponseTypeDef

### resourceShares
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceShareTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPendingInvitationResourcesRequestTypeDef

### resourceShareInvitationArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['ALL', 'GLOBAL', 'REGIONAL']]


# ListPendingInvitationResourcesResponseTypeDef

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionAssociationsRequestTypeDef

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


# ListPermissionAssociationsResponseTypeDef

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.AssociatedPermissionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionVersionsRequestTypeDef

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPermissionVersionsResponseTypeDef

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceSharePermissionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPermissionsRequestTypeDef

### resourceType
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### permissionType
- **Type**: typing.Optional[typing.Literal['ALL', 'AWS_MANAGED', 'CUSTOMER_MANAGED']]


# ListPermissionsResponseTypeDef

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceSharePermissionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPrincipalsRequestPaginateTypeDef

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### resourceArn
- **Type**: typing.Optional[str]

### principals
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceType
- **Type**: typing.Optional[str]

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram_classes.PaginatorConfigTypeDef]


# ListPrincipalsRequestTypeDef

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### resourceArn
- **Type**: typing.Optional[str]

### principals
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceType
- **Type**: typing.Optional[str]

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPrincipalsResponseTypeDef

### principals
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.PrincipalTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListReplacePermissionAssociationsWorkRequestTypeDef

### workIds
- **Type**: typing.Optional[typing.Sequence[str]]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListReplacePermissionAssociationsWorkResponseTypeDef

### replacePermissionAssociationsWorks
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ReplacePermissionAssociationsWorkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceSharePermissionsRequestTypeDef

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListResourceSharePermissionsResponseTypeDef

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceSharePermissionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceTypesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['ALL', 'GLOBAL', 'REGIONAL']]


# ListResourceTypesResponseTypeDef

### resourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ServiceNameAndResourceTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourcesRequestPaginateTypeDef

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['ALL', 'GLOBAL', 'REGIONAL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ram_classes.PaginatorConfigTypeDef]


# ListResourcesRequestTypeDef

### resourceOwner
- **Type**: typing.Literal['OTHER-ACCOUNTS', 'SELF']
- **Required**: Yes

### principal
- **Type**: typing.Optional[str]

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceShareArns
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['ALL', 'GLOBAL', 'REGIONAL']]


# ListResourcesResponseTypeDef

### resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrincipalTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromotePermissionCreatedFromPolicyRequestTypeDef

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# PromotePermissionCreatedFromPolicyResponseTypeDef

### permission
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResourceSharePermissionSummaryTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PromoteResourceShareCreatedFromPolicyRequestTypeDef

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes


# PromoteResourceShareCreatedFromPolicyResponseTypeDef

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RejectResourceShareInvitationRequestTypeDef

### resourceShareInvitationArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# RejectResourceShareInvitationResponseTypeDef

### resourceShareInvitation
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResourceShareInvitationTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplacePermissionAssociationsRequestTypeDef

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


# ReplacePermissionAssociationsResponseTypeDef

### replacePermissionAssociationsWork
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ReplacePermissionAssociationsWorkTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplacePermissionAssociationsWorkTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceShareAssociationTypeDef

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


# ResourceShareInvitationTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram_classes.ResourceShareAssociationTypeDef]]

### receiverArn
- **Type**: typing.Optional[str]


# ResourceSharePermissionDetailTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram_classes.TagTypeDef]]


# ResourceSharePermissionSummaryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram_classes.TagTypeDef]]


# ResourceShareTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ram_classes.TagTypeDef]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### featureSet
- **Type**: typing.Optional[typing.Literal['CREATED_FROM_POLICY', 'PROMOTING_TO_STANDARD', 'STANDARD']]


# ResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadataTypeDef

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


# ServiceNameAndResourceTypeTypeDef

### resourceType
- **Type**: typing.Optional[str]

### serviceName
- **Type**: typing.Optional[str]

### resourceRegionScope
- **Type**: typing.Optional[typing.Literal['GLOBAL', 'REGIONAL']]


# SetDefaultPermissionVersionRequestTypeDef

### permissionArn
- **Type**: <class 'str'>
- **Required**: Yes

### permissionVersion
- **Type**: <class 'int'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# SetDefaultPermissionVersionResponseTypeDef

### returnValue
- **Type**: <class 'bool'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagFilterTypeDef

### tagKey
- **Type**: typing.Optional[str]

### tagValues
- **Type**: typing.Optional[typing.Sequence[str]]


# TagResourceRequestTypeDef

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ram_classes.TagTypeDef]
- **Required**: Yes

### resourceShareArn
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### resourceShareArn
- **Type**: typing.Optional[str]

### resourceArn
- **Type**: typing.Optional[str]


# UpdateResourceShareRequestTypeDef

### resourceShareArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### allowExternalPrincipals
- **Type**: typing.Optional[bool]

### clientToken
- **Type**: typing.Optional[str]


# UpdateResourceShareResponseTypeDef

### resourceShare
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResourceShareTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ram_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



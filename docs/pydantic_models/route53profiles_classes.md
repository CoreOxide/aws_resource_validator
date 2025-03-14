# Route53Profiles Classes

# AssociateProfileRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53profiles_classes.TagTypeDef]]


# AssociateProfileResponseTypeDef

### ProfileAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateResourceToProfileRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceProperties
- **Type**: typing.Optional[str]


# AssociateResourceToProfileResponseTypeDef

### ProfileResourceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileResourceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateProfileRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53profiles_classes.TagTypeDef]]


# CreateProfileResponseTypeDef

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProfileRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileResponseTypeDef

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateProfileRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateProfileResponseTypeDef

### ProfileAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateResourceFromProfileRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateResourceFromProfileResponseTypeDef

### ProfileResourceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileResourceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProfileAssociationRequestTypeDef

### ProfileAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileAssociationResponseTypeDef

### ProfileAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProfileRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileResourceAssociationRequestTypeDef

### ProfileResourceAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileResourceAssociationResponseTypeDef

### ProfileResourceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileResourceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProfileResponseTypeDef

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProfileAssociationsRequestPaginateTypeDef

### ProfileId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53profiles_classes.PaginatorConfigTypeDef]


# ListProfileAssociationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]


# ListProfileAssociationsResponseTypeDef

### ProfileAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53profiles_classes.ProfileAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileResourceAssociationsRequestPaginateTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53profiles_classes.PaginatorConfigTypeDef]


# ListProfileResourceAssociationsRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ListProfileResourceAssociationsResponseTypeDef

### ProfileResourceAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53profiles_classes.ProfileResourceAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfilesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53profiles_classes.PaginatorConfigTypeDef]


# ListProfilesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListProfilesResponseTypeDef

### ProfileSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53profiles_classes.ProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProfileAssociationTypeDef

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Id
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]


# ProfileResourceAssociationTypeDef

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Id
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]

### ResourceProperties
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]


# ProfileSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['NOT_SHARED', 'SHARED_BY_ME', 'SHARED_WITH_ME']]


# ProfileTypeDef

### Arn
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Id
- **Type**: typing.Optional[str]

### ModificationTime
- **Type**: typing.Optional[datetime.datetime]

### Name
- **Type**: typing.Optional[str]

### OwnerId
- **Type**: typing.Optional[str]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['NOT_SHARED', 'SHARED_BY_ME', 'SHARED_WITH_ME']]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'CREATING', 'DELETED', 'DELETING', 'FAILED', 'UPDATING']]

### StatusMessage
- **Type**: typing.Optional[str]


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


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateProfileResourceAssociationRequestTypeDef

### ProfileResourceAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### ResourceProperties
- **Type**: typing.Optional[str]


# UpdateProfileResourceAssociationResponseTypeDef

### ProfileResourceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ProfileResourceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



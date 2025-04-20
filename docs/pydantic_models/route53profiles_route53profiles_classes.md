# Route53Profiles Route53Profiles Classes

# AssociateProfileRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.Tag]]


# AssociateProfileResponse

### ProfileAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateResourceToProfileRequest

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


# AssociateResourceToProfileResponse

### ProfileResourceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileResourceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateProfileRequest

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.Tag]]


# CreateProfileResponse

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.Profile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProfileRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileResponse

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.Profile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateProfileRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateProfileResponse

### ProfileAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateResourceFromProfileRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateResourceFromProfileResponse

### ProfileResourceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileResourceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileAssociationRequest

### ProfileAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileAssociationResponse

### ProfileAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileResourceAssociationRequest

### ProfileResourceAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileResourceAssociationResponse

### ProfileResourceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileResourceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileResponse

### Profile
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.Profile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# ListProfileAssociationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]


# ListProfileAssociationsRequestPaginate

### ProfileId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.PaginatorConfig]


# ListProfileAssociationsResponse

### ProfileAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileResourceAssociationsRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ListProfileResourceAssociationsRequestPaginate

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.PaginatorConfig]


# ListProfileResourceAssociationsResponse

### ProfileResourceAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileResourceAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfilesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListProfilesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.PaginatorConfig]


# ListProfilesResponse

### ProfileSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Profile

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


# ProfileAssociation

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


# ProfileResourceAssociation

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


# ProfileSummary

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['NOT_SHARED', 'SHARED_BY_ME', 'SHARED_WITH_ME']]


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


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateProfileResourceAssociationRequest

### ProfileResourceAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### ResourceProperties
- **Type**: typing.Optional[str]


# UpdateProfileResourceAssociationResponse

### ProfileResourceAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ProfileResourceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53profiles.route53profiles_classes.ResponseMetadata'>
- **Required**: Yes



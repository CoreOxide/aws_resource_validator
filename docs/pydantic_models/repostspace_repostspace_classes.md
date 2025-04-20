# Repostspace Repostspace Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAddRoleInput

### accessorIds
- **Type**: typing.List[str]
- **Required**: Yes

### role
- **Type**: typing.Literal['ADMINISTRATOR', 'EXPERT', 'MODERATOR', 'SUPPORTREQUESTOR']
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchAddRoleOutput

### addedAccessorIds
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.repostspace.repostspace_classes.BatchError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace.repostspace_classes.ResponseMetadata'>
- **Required**: Yes


# BatchError

### accessorId
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'int'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchRemoveRoleInput

### accessorIds
- **Type**: typing.List[str]
- **Required**: Yes

### role
- **Type**: typing.Literal['ADMINISTRATOR', 'EXPERT', 'MODERATOR', 'SUPPORTREQUESTOR']
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchRemoveRoleOutput

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.repostspace.repostspace_classes.BatchError]
- **Required**: Yes

### removedAccessorIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace.repostspace_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSpaceInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### subdomain
- **Type**: <class 'str'>
- **Required**: Yes

### tier
- **Type**: typing.Literal['BASIC', 'STANDARD']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### userKMSKey
- **Type**: typing.Optional[str]


# CreateSpaceOutput

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace.repostspace_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSpaceInput

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterAdminInput

### adminId
- **Type**: <class 'str'>
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace.repostspace_classes.ResponseMetadata'>
- **Required**: Yes


# GetSpaceInput

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpaceOutput

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### configurationStatus
- **Type**: typing.Literal['CONFIGURED', 'UNCONFIGURED']
- **Required**: Yes

### contentSize
- **Type**: <class 'int'>
- **Required**: Yes

### createDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### deleteDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### groupAdmins
- **Type**: typing.List[str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### randomDomain
- **Type**: <class 'str'>
- **Required**: Yes

### roles
- **Type**: typing.Dict[str, typing.List[typing.Literal['ADMINISTRATOR', 'EXPERT', 'MODERATOR', 'SUPPORTREQUESTOR']]]
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### storageLimit
- **Type**: <class 'int'>
- **Required**: Yes

### tier
- **Type**: typing.Literal['BASIC', 'STANDARD']
- **Required**: Yes

### userAdmins
- **Type**: typing.List[str]
- **Required**: Yes

### userCount
- **Type**: <class 'int'>
- **Required**: Yes

### userKMSKey
- **Type**: <class 'str'>
- **Required**: Yes

### vanityDomain
- **Type**: <class 'str'>
- **Required**: Yes

### vanityDomainStatus
- **Type**: typing.Literal['APPROVED', 'PENDING', 'UNAPPROVED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace.repostspace_classes.ResponseMetadata'>
- **Required**: Yes


# ListSpacesInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.repostspace.repostspace_classes.PaginatorConfig]


# ListSpacesOutput

### spaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.repostspace.repostspace_classes.SpaceData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace.repostspace_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace.repostspace_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterAdminInput

### adminId
- **Type**: <class 'str'>
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


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


# SendInvitesInput

### accessorIds
- **Type**: typing.List[str]
- **Required**: Yes

### body
- **Type**: <class 'str'>
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes


# SpaceData

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### configurationStatus
- **Type**: typing.Literal['CONFIGURED', 'UNCONFIGURED']
- **Required**: Yes

### createDateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### randomDomain
- **Type**: <class 'str'>
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### storageLimit
- **Type**: <class 'int'>
- **Required**: Yes

### tier
- **Type**: typing.Literal['BASIC', 'STANDARD']
- **Required**: Yes

### vanityDomain
- **Type**: <class 'str'>
- **Required**: Yes

### vanityDomainStatus
- **Type**: typing.Literal['APPROVED', 'PENDING', 'UNAPPROVED']
- **Required**: Yes

### contentSize
- **Type**: typing.Optional[int]

### deleteDateTime
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### userCount
- **Type**: typing.Optional[int]

### userKMSKey
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateSpaceInput

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### tier
- **Type**: typing.Optional[typing.Literal['BASIC', 'STANDARD']]



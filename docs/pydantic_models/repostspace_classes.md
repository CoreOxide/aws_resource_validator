# Repostspace Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchAddRoleInputTypeDef

### accessorIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### role
- **Type**: typing.Literal['ADMINISTRATOR', 'EXPERT', 'MODERATOR', 'SUPPORTREQUESTOR']
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchAddRoleOutputTypeDef

### addedAccessorIds
- **Type**: typing.List[str]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.repostspace_classes.BatchErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchErrorTypeDef

### accessorId
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'int'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchRemoveRoleInputTypeDef

### accessorIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### role
- **Type**: typing.Literal['ADMINISTRATOR', 'EXPERT', 'MODERATOR', 'SUPPORTREQUESTOR']
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchRemoveRoleOutputTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.repostspace_classes.BatchErrorTypeDef]
- **Required**: Yes

### removedAccessorIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSpaceInputTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### userKMSKey
- **Type**: typing.Optional[str]


# CreateSpaceOutputTypeDef

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSpaceInputTypeDef

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterAdminInputTypeDef

### adminId
- **Type**: <class 'str'>
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSpaceInputTypeDef

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpaceOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSpacesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.repostspace_classes.PaginatorConfigTypeDef]


# ListSpacesInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesOutputTypeDef

### spaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.repostspace_classes.SpaceDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterAdminInputTypeDef

### adminId
- **Type**: <class 'str'>
- **Required**: Yes

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


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


# SendInvitesInputTypeDef

### accessorIds
- **Type**: typing.Sequence[str]
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


# SpaceDataTypeDef

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


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateSpaceInputTypeDef

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### tier
- **Type**: typing.Optional[typing.Literal['BASIC', 'STANDARD']]



# Pydantic Models in repostspace_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateSpaceInputRequestTypeDef

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


# DeleteSpaceInputRequestTypeDef

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterAdminInputRequestTypeDef

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


# GetSpaceInputRequestTypeDef

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


# ListSpacesInputListSpacesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.repostspace_classes.PaginatorConfigTypeDef]


# ListSpacesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesOutputTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### spaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.repostspace_classes.SpaceDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.repostspace_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# RegisterAdminInputRequestTypeDef

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

### HostId
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


# SendInvitesInputRequestTypeDef

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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateSpaceInputRequestTypeDef

### spaceId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### tier
- **Type**: typing.Optional[typing.Literal['BASIC', 'STANDARD']]



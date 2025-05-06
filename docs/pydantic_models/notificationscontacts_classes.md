# Notificationscontacts Classes

# ActivateEmailContactRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEmailContactRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### emailAddress
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateEmailContactResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notificationscontacts.notificationscontacts_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEmailContactRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# EmailContact

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### address
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['active', 'inactive']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# GetEmailContactRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEmailContactResponse

### emailContact
- **Type**: <class 'aws_resource_validator.pydantic_models.notificationscontacts.notificationscontacts_classes.EmailContact'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notificationscontacts.notificationscontacts_classes.ResponseMetadata'>
- **Required**: Yes


# ListEmailContactsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEmailContactsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notificationscontacts.notificationscontacts_classes.PaginatorConfig]


# ListEmailContactsResponse

### emailContacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.notificationscontacts.notificationscontacts_classes.EmailContact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notificationscontacts.notificationscontacts_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notificationscontacts.notificationscontacts_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# SendActivationCodeRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes



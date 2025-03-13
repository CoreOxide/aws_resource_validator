# Qapps Classes

# AppDefinitionInputOutputTypeDef

### cards
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CardInputOutputTypeDef]
- **Required**: Yes

### initialPrompt
- **Type**: typing.Optional[str]


# AppDefinitionInputTypeDef

### cards
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CardInputTypeDef]
- **Required**: Yes

### initialPrompt
- **Type**: typing.Optional[str]


# AppDefinitionInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AppDefinitionTypeDef

### appDefinitionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### cards
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CardTypeDef]
- **Required**: Yes

### canEdit
- **Type**: typing.Optional[bool]


# AssociateLibraryItemReviewInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateQAppWithUserInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeFilterOutputTypeDef

### andAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutputTypeDef]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutputTypeDef]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutputTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutputTypeDef]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutputTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutputTypeDef]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutputTypeDef]


# AttributeFilterTypeDef

### andAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeTypeDef]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeTypeDef]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeTypeDef]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeTypeDef]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateCategoryInputCategoryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateCategoryInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categories
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.BatchCreateCategoryInputCategoryTypeDef]
- **Required**: Yes


# BatchDeleteCategoryInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categories
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchUpdateCategoryInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categories
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CategoryInputTypeDef]
- **Required**: Yes


# CardInputOutputTypeDef

### textInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TextInputCardInputTypeDef]

### qQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QQueryCardInputOutputTypeDef]

### qPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QPluginCardInputTypeDef]

### fileUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FileUploadCardInputTypeDef]

### formInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FormInputCardInputOutputTypeDef]


# CardInputTypeDef

### textInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TextInputCardInputTypeDef]

### qQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QQueryCardInputTypeDef]

### qPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QPluginCardInputTypeDef]

### fileUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FileUploadCardInputTypeDef]

### formInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FormInputCardInputTypeDef]


# CardStatusTypeDef

### currentState
- **Type**: typing.Literal['COMPLETED', 'ERROR', 'IN_PROGRESS', 'WAITING']
- **Required**: Yes

### currentValue
- **Type**: <class 'str'>
- **Required**: Yes

### submissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qapps_classes.SubmissionTypeDef]]


# CardTypeDef

### textInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TextInputCardTypeDef]

### qQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QQueryCardTypeDef]

### qPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QPluginCardTypeDef]

### fileUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FileUploadCardTypeDef]

### formInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FormInputCardTypeDef]


# CardValueTypeDef

### cardId
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### submissionMutation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.SubmissionMutationTypeDef]


# CategoryInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CategoryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConversationMessageTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateLibraryItemInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### categories
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CreateLibraryItemOutputTypeDef

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ratingCount
- **Type**: <class 'int'>
- **Required**: Yes

### isVerified
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePresignedUrlInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### cardId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### fileContentsSha256
- **Type**: <class 'str'>
- **Required**: Yes

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: typing.Literal['APPLICATION', 'SESSION']
- **Required**: Yes

### sessionId
- **Type**: typing.Optional[str]


# CreatePresignedUrlOutputTypeDef

### fileId
- **Type**: <class 'str'>
- **Required**: Yes

### presignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### presignedUrlFields
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### presignedUrlExpiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQAppInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### appDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionInputUnionTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQAppOutputTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### initialPrompt
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETED', 'DRAFT', 'PUBLISHED']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### requiredCapabilities
- **Type**: typing.List[typing.Literal['CreatorMode', 'FileUpload', 'PluginMode', 'RetrievalMode']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLibraryItemInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQAppInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQAppPermissionsInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQAppPermissionsOutputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.PermissionOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateLibraryItemReviewInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateQAppFromUserInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentAttributeOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeValueOutputTypeDef'>
- **Required**: Yes


# DocumentAttributeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeValueTypeDef'>
- **Required**: Yes


# DocumentAttributeValueOutputTypeDef

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.List[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[datetime.datetime]


# DocumentAttributeValueTypeDef

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.Sequence[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TimestampTypeDef]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportQAppSessionDataInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportQAppSessionDataOutputTypeDef

### csvFileLink
- **Type**: <class 'str'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FileUploadCardInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileUploadCardTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputCardInputOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputCardInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputCardMetadataOutputTypeDef

### schema
- **Type**: typing.Dict[str, typing.Any]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.qapps_classes.FormInputCardMetadataOutputTypeDef'>>


# FormInputCardMetadataTypeDef

### schema
- **Type**: typing.Mapping[str, typing.Any]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.qapps_classes.FormInputCardMetadataTypeDef'>>


# FormInputCardTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetLibraryItemInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: typing.Optional[str]


# GetLibraryItemOutputTypeDef

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### categories
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CategoryTypeDef]
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ratingCount
- **Type**: <class 'int'>
- **Required**: Yes

### isRatedByUser
- **Type**: <class 'bool'>
- **Required**: Yes

### userCount
- **Type**: <class 'int'>
- **Required**: Yes

### isVerified
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQAppInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: typing.Optional[int]


# GetQAppOutputTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### initialPrompt
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETED', 'DRAFT', 'PUBLISHED']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### requiredCapabilities
- **Type**: typing.List[typing.Literal['CreatorMode', 'FileUpload', 'PluginMode', 'RetrievalMode']]
- **Required**: Yes

### appDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQAppSessionInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQAppSessionMetadataInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQAppSessionMetadataOutputTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionName
- **Type**: <class 'str'>
- **Required**: Yes

### sharingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.SessionSharingConfigurationTypeDef'>
- **Required**: Yes

### sessionOwner
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQAppSessionOutputTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionName
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### latestPublishedAppVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'ERROR', 'IN_PROGRESS', 'WAITING']
- **Required**: Yes

### cardStatus
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.qapps_classes.CardStatusTypeDef]
- **Required**: Yes

### userIsHost
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportDocumentInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### cardId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### fileContentsBase64
- **Type**: <class 'str'>
- **Required**: Yes

### fileName
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: typing.Literal['APPLICATION', 'SESSION']
- **Required**: Yes

### sessionId
- **Type**: typing.Optional[str]


# ImportDocumentOutputTypeDef

### fileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LibraryItemMemberTypeDef

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### categories
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CategoryTypeDef]
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### ratingCount
- **Type**: <class 'int'>
- **Required**: Yes

### updatedAt
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### isRatedByUser
- **Type**: typing.Optional[bool]

### userCount
- **Type**: typing.Optional[int]

### isVerified
- **Type**: typing.Optional[bool]


# ListCategoriesInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes


# ListCategoriesOutputTypeDef

### categories
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CategoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLibraryItemsInputPaginateTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categoryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.PaginatorConfigTypeDef]


# ListLibraryItemsInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### categoryId
- **Type**: typing.Optional[str]


# ListLibraryItemsOutputTypeDef

### libraryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.LibraryItemMemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQAppSessionDataInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# ListQAppSessionDataOutputTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionData
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.QAppSessionDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQAppsInputPaginateTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.PaginatorConfigTypeDef]


# ListQAppsInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListQAppsOutputTypeDef

### apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.UserAppItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionInputTypeDef

### action
- **Type**: typing.Literal['read', 'write']
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# PermissionOutputTypeDef

### action
- **Type**: typing.Literal['read', 'write']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.PrincipalOutputTypeDef'>
- **Required**: Yes


# PredictAppDefinitionTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### appDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionInputOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# PredictQAppInputOptionsTypeDef

### conversation
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.ConversationMessageTypeDef]]

### problemStatement
- **Type**: typing.Optional[str]


# PredictQAppInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.PredictQAppInputOptionsTypeDef]


# PredictQAppOutputTypeDef

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.PredictAppDefinitionTypeDef'>
- **Required**: Yes

### problemStatement
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PrincipalOutputTypeDef

### userId
- **Type**: typing.Optional[str]

### userType
- **Type**: typing.Optional[typing.Literal['owner', 'user']]

### email
- **Type**: typing.Optional[str]


# QAppSessionDataTypeDef

### cardId
- **Type**: <class 'str'>
- **Required**: Yes

### user
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.UserTypeDef'>
- **Required**: Yes

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### submissionId
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[datetime.datetime]


# QPluginCardInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QPluginCardTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QQueryCardInputOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QQueryCardInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QQueryCardTypeDef

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


# SessionSharingConfigurationTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### acceptResponses
- **Type**: typing.Optional[bool]

### revealCards
- **Type**: typing.Optional[bool]


# StartQAppSessionInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### initialValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CardValueTypeDef]]

### sessionId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartQAppSessionOutputTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopQAppSessionInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# SubmissionMutationTypeDef

### submissionId
- **Type**: <class 'str'>
- **Required**: Yes

### mutationType
- **Type**: typing.Literal['add', 'delete', 'edit']
- **Required**: Yes


# SubmissionTypeDef

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### submissionId
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[datetime.datetime]


# TagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextInputCardInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TextInputCardTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLibraryItemInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'PUBLISHED']]

### categories
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLibraryItemMetadataInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### isVerified
- **Type**: typing.Optional[bool]


# UpdateLibraryItemOutputTypeDef

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### categories
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CategoryTypeDef]
- **Required**: Yes

### status
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### ratingCount
- **Type**: <class 'int'>
- **Required**: Yes

### isRatedByUser
- **Type**: <class 'bool'>
- **Required**: Yes

### userCount
- **Type**: <class 'int'>
- **Required**: Yes

### isVerified
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQAppInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### appDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionInputUnionTypeDef]


# UpdateQAppOutputTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### initialPrompt
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETED', 'DRAFT', 'PUBLISHED']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### requiredCapabilities
- **Type**: typing.List[typing.Literal['CreatorMode', 'FileUpload', 'PluginMode', 'RetrievalMode']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQAppPermissionsInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### grantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.PermissionInputTypeDef]]

### revokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.PermissionInputTypeDef]]


# UpdateQAppPermissionsOutputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.PermissionOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQAppSessionInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CardValueTypeDef]]


# UpdateQAppSessionMetadataInputTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sharingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.SessionSharingConfigurationTypeDef'>
- **Required**: Yes

### sessionName
- **Type**: typing.Optional[str]


# UpdateQAppSessionMetadataOutputTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionName
- **Type**: <class 'str'>
- **Required**: Yes

### sharingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.SessionSharingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQAppSessionOutputTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserAppItemTypeDef

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appArn
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### canEdit
- **Type**: typing.Optional[bool]

### status
- **Type**: typing.Optional[str]

### isVerified
- **Type**: typing.Optional[bool]


# UserTypeDef

### userId
- **Type**: typing.Optional[str]



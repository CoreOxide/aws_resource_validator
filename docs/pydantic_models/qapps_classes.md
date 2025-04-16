# Qapps Classes

# AppDefinition

### appDefinitionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### cards
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.Card]
- **Required**: Yes

### canEdit
- **Type**: typing.Optional[bool]


# AppDefinitionInput

### cards
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CardInput]
- **Required**: Yes

### initialPrompt
- **Type**: typing.Optional[str]


# AppDefinitionInputOutput

### cards
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CardInputOutput]
- **Required**: Yes

### initialPrompt
- **Type**: typing.Optional[str]


# AppDefinitionInputUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateLibraryItemReviewInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateQAppWithUserInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeFilter

### andAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttribute]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttribute]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttribute]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttribute]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttribute]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttribute]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttribute]


# AttributeFilterOutput

### andAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### orAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### notFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### equalsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutput]

### containsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutput]

### containsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutput]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutput]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutput]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutput]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeOutput]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateCategoryInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categories
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.BatchCreateCategoryInputCategory]
- **Required**: Yes


# BatchCreateCategoryInputCategory

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDeleteCategoryInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categories
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchUpdateCategoryInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categories
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CategoryInput]
- **Required**: Yes


# Card

### textInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TextInputCard]

### qQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QQueryCard]

### qPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QPluginCard]

### fileUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FileUploadCard]

### formInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FormInputCard]


# CardInput

### textInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TextInputCardInput]

### qQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QQueryCardInput]

### qPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QPluginCardInput]

### fileUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FileUploadCardInput]

### formInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FormInputCardInput]


# CardInputOutput

### textInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TextInputCardInput]

### qQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QQueryCardInputOutput]

### qPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QPluginCardInput]

### fileUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FileUploadCardInput]

### formInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FormInputCardInputOutput]


# CardStatus

### currentState
- **Type**: typing.Literal['COMPLETED', 'ERROR', 'IN_PROGRESS', 'WAITING']
- **Required**: Yes

### currentValue
- **Type**: <class 'str'>
- **Required**: Yes

### submissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qapps_classes.Submission]]


# CardValue

### cardId
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### submissionMutation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.SubmissionMutation]


# Category

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CategoryInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConversationMessage

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateLibraryItemInput

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


# CreateLibraryItemOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePresignedUrlInput

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


# CreatePresignedUrlOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQAppInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### appDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionInputUnion'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQAppOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLibraryItemInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQAppInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQAppPermissionsInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQAppPermissionsOutput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.PermissionOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateLibraryItemReviewInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateQAppFromUserInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentAttribute

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeValue'>
- **Required**: Yes


# DocumentAttributeOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.DocumentAttributeValueOutput'>
- **Required**: Yes


# DocumentAttributeValue

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.Sequence[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.Timestamp]


# DocumentAttributeValueOutput

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.List[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[datetime.datetime]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# ExportQAppSessionDataInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportQAppSessionDataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# FileUploadCard

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileUploadCardInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputCard

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputCardInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputCardInputOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputCardMetadata

### schema
- **Type**: typing.Mapping[str, typing.Any]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.qapps_classes.FormInputCardMetadata'>>


# FormInputCardMetadataOutput

### schema
- **Type**: typing.Dict[str, typing.Any]
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.qapps_classes.FormInputCardMetadataOutput'>>


# GetLibraryItemInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: typing.Optional[str]


# GetLibraryItemOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.Category]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# GetQAppInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### appVersion
- **Type**: typing.Optional[int]


# GetQAppOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.AppDefinition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# GetQAppSessionInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQAppSessionMetadataInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQAppSessionMetadataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.SessionSharingConfiguration'>
- **Required**: Yes

### sessionOwner
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# GetQAppSessionOutput

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.qapps_classes.CardStatus]
- **Required**: Yes

### userIsHost
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# ImportDocumentInput

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


# ImportDocumentOutput

### fileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# LibraryItemMember

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.Category]
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


# ListCategoriesInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes


# ListCategoriesOutput

### categories
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.Category]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# ListLibraryItemsInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### categoryId
- **Type**: typing.Optional[str]


# ListLibraryItemsInputPaginate

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categoryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.PaginatorConfig]


# ListLibraryItemsOutput

### libraryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.LibraryItemMember]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQAppSessionDataInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# ListQAppSessionDataOutput

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionData
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.QAppSessionData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQAppsInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### limit
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListQAppsInputPaginate

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.PaginatorConfig]


# ListQAppsOutput

### apps
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.UserAppItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionInput

### action
- **Type**: typing.Literal['read', 'write']
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# PermissionOutput

### action
- **Type**: typing.Literal['read', 'write']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.PrincipalOutput'>
- **Required**: Yes


# PredictAppDefinition

### title
- **Type**: <class 'str'>
- **Required**: Yes

### appDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionInputOutput'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# PredictQAppInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.PredictQAppInputOptions]


# PredictQAppInputOptions

### conversation
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.ConversationMessage]]

### problemStatement
- **Type**: typing.Optional[str]


# PredictQAppOutput

### app
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.PredictAppDefinition'>
- **Required**: Yes

### problemStatement
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# PrincipalOutput

### userId
- **Type**: typing.Optional[str]

### userType
- **Type**: typing.Optional[typing.Literal['owner', 'user']]

### email
- **Type**: typing.Optional[str]


# QAppSessionData

### cardId
- **Type**: <class 'str'>
- **Required**: Yes

### user
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.User'>
- **Required**: Yes

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### submissionId
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[datetime.datetime]


# QPluginCard

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QPluginCardInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QQueryCard

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QQueryCardInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QQueryCardInputOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SessionSharingConfiguration

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### acceptResponses
- **Type**: typing.Optional[bool]

### revealCards
- **Type**: typing.Optional[bool]


# StartQAppSessionInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CardValue]]

### sessionId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartQAppSessionOutput

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# StopQAppSessionInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# Submission

### value
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### submissionId
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[datetime.datetime]


# SubmissionMutation

### submissionId
- **Type**: <class 'str'>
- **Required**: Yes

### mutationType
- **Type**: typing.Literal['add', 'delete', 'edit']
- **Required**: Yes


# TagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextInputCard

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TextInputCardInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLibraryItemInput

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


# UpdateLibraryItemMetadataInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes

### isVerified
- **Type**: typing.Optional[bool]


# UpdateLibraryItemOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.Category]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQAppInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionInputUnion]


# UpdateQAppOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQAppPermissionsInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### grantPermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.PermissionInput]]

### revokePermissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.PermissionInput]]


# UpdateQAppPermissionsOutput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.PermissionOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQAppSessionInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CardValue]]


# UpdateQAppSessionMetadataInput

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sharingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.SessionSharingConfiguration'>
- **Required**: Yes

### sessionName
- **Type**: typing.Optional[str]


# UpdateQAppSessionMetadataOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.SessionSharingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQAppSessionOutput

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadata'>
- **Required**: Yes


# User

### userId
- **Type**: typing.Optional[str]


# UserAppItem

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



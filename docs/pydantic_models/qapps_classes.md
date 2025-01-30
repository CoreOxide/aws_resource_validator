# qapps_classes

# AppDefinitionInputOutputTypeDef

### cards
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CardInputTypeDef]
- **Required**: Yes

### initialPrompt
- **Type**: typing.Optional[str]


# AppDefinitionInputTypeDef

### cards
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CardInputTypeDef]
- **Required**: Yes

### initialPrompt
- **Type**: typing.Optional[str]


# AppDefinitionTypeDef

### appDefinitionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### cards
- **Type**: typing.List[aws_resource_validator.pydantic_models.qapps_classes.CardTypeDef]
- **Required**: Yes

### canEdit
- **Type**: typing.Optional[bool]


# AssociateLibraryItemReviewInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateQAppWithUserInputRequestTypeDef

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CardInputTypeDef

### textInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TextInputCardInputTypeDef]

### qQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QQueryCardInputTypeDef]

### qPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QPluginCardInputTypeDef]

### fileUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FileUploadCardInputTypeDef]


# CardStatusTypeDef

### currentState
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS', 'WAITING']
- **Required**: Yes

### currentValue
- **Type**: <class 'str'>
- **Required**: Yes


# CardTypeDef

### textInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.TextInputCardTypeDef]

### qQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QQueryCardTypeDef]

### qPlugin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.QPluginCardTypeDef]

### fileUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.FileUploadCardTypeDef]


# CardValueTypeDef

### cardId
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# CategoryTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes


# ConversationMessageTypeDef

### body
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['SYSTEM', 'USER']
- **Required**: Yes


# CreateLibraryItemInputRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQAppInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### appDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionInputTypeDef'>
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


# DeleteLibraryItemInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQAppInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateLibraryItemReviewInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### libraryItemId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateQAppFromUserInputRequestTypeDef

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


# DocumentAttributeValueOutputTypeDef

### stringValue
- **Type**: typing.Optional[str]

### stringListValue
- **Type**: typing.Optional[typing.List[str]]

### longValue
- **Type**: typing.Optional[int]

### dateValue
- **Type**: typing.Optional[datetime.datetime]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FileUploadCardInputTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['file-upload', 'q-plugin', 'q-query', 'text-input']
- **Required**: Yes

### filename
- **Type**: typing.Optional[str]

### fileId
- **Type**: typing.Optional[str]

### allowOverride
- **Type**: typing.Optional[bool]


# FileUploadCardTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### dependencies
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['file-upload', 'q-plugin', 'q-query', 'text-input']
- **Required**: Yes

### filename
- **Type**: typing.Optional[str]

### fileId
- **Type**: typing.Optional[str]

### allowOverride
- **Type**: typing.Optional[bool]


# GetLibraryItemInputRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQAppInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes


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


# GetQAppSessionInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQAppSessionOutputTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'IN_PROGRESS', 'WAITING']
- **Required**: Yes

### cardStatus
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.qapps_classes.CardStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportDocumentInputRequestTypeDef

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


# ListLibraryItemsInputListLibraryItemsPaginateTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### categoryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.PaginatorConfigTypeDef]


# ListLibraryItemsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQAppsInputListQAppsPaginateTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.PaginatorConfigTypeDef]


# ListQAppsInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# PredictQAppInputRequestTypeDef

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


# QPluginCardInputTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['file-upload', 'q-plugin', 'q-query', 'text-input']
- **Required**: Yes

### prompt
- **Type**: <class 'str'>
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# QPluginCardTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### dependencies
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['file-upload', 'q-plugin', 'q-query', 'text-input']
- **Required**: Yes

### prompt
- **Type**: <class 'str'>
- **Required**: Yes

### pluginType
- **Type**: typing.Literal['CUSTOM', 'JIRA', 'SALESFORCE', 'SERVICE_NOW', 'ZENDESK']
- **Required**: Yes

### pluginId
- **Type**: <class 'str'>
- **Required**: Yes


# QQueryCardInputTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['file-upload', 'q-plugin', 'q-query', 'text-input']
- **Required**: Yes

### prompt
- **Type**: <class 'str'>
- **Required**: Yes

### outputSource
- **Type**: typing.Optional[typing.Literal['approved-sources', 'llm']]

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.AttributeFilterOutputTypeDef]


# QQueryCardTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### dependencies
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['file-upload', 'q-plugin', 'q-query', 'text-input']
- **Required**: Yes

### prompt
- **Type**: <class 'str'>
- **Required**: Yes

### outputSource
- **Type**: typing.Literal['approved-sources', 'llm']
- **Required**: Yes

### attributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.AttributeFilterOutputTypeDef]


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


# StartQAppSessionInputRequestTypeDef

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


# StopQAppSessionInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextInputCardInputTypeDef

### title
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['file-upload', 'q-plugin', 'q-query', 'text-input']
- **Required**: Yes

### placeholder
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]


# TextInputCardTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### dependencies
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['file-upload', 'q-plugin', 'q-query', 'text-input']
- **Required**: Yes

### placeholder
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLibraryItemInputRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qapps_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQAppInputRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qapps_classes.AppDefinitionInputTypeDef]


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


# UpdateQAppSessionInputRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qapps_classes.CardValueTypeDef]]


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



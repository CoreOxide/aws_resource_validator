# Amplifyuibuilder Classes

# ActionParametersOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionParametersPaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionParametersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiConfiguration

### graphQLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.GraphQLRenderConfig]

### dataStoreConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### noApiConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ApiConfigurationOutput

### graphQLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.GraphQLRenderConfig]

### dataStoreConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### noApiConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ApiConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenDependency

### name
- **Type**: typing.Optional[str]

### supportedVersion
- **Type**: typing.Optional[str]

### isSemVer
- **Type**: typing.Optional[bool]

### reason
- **Type**: typing.Optional[str]


# CodegenFeatureFlags

### isRelationshipSupported
- **Type**: typing.Optional[bool]

### isNonModelSupported
- **Type**: typing.Optional[bool]


# CodegenGenericDataEnum

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CodegenGenericDataEnumOutput

### values
- **Type**: typing.List[str]
- **Required**: Yes


# CodegenGenericDataEnumUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataField

### dataType
- **Type**: typing.Literal['AWSDate', 'AWSDateTime', 'AWSEmail', 'AWSIPAddress', 'AWSJSON', 'AWSPhone', 'AWSTime', 'AWSTimestamp', 'AWSURL', 'Boolean', 'Enum', 'Float', 'ID', 'Int', 'Model', 'NonModel', 'String']
- **Required**: Yes

### dataTypeValue
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: <class 'bool'>
- **Required**: Yes

### readOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### isArray
- **Type**: <class 'bool'>
- **Required**: Yes

### relationship
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataRelationshipTypeUnion]


# CodegenGenericDataFieldOutput

### dataType
- **Type**: typing.Literal['AWSDate', 'AWSDateTime', 'AWSEmail', 'AWSIPAddress', 'AWSJSON', 'AWSPhone', 'AWSTime', 'AWSTimestamp', 'AWSURL', 'Boolean', 'Enum', 'Float', 'ID', 'Int', 'Model', 'NonModel', 'String']
- **Required**: Yes

### dataTypeValue
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: <class 'bool'>
- **Required**: Yes

### readOnly
- **Type**: <class 'bool'>
- **Required**: Yes

### isArray
- **Type**: <class 'bool'>
- **Required**: Yes

### relationship
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataRelationshipTypeOutput]


# CodegenGenericDataFieldUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataModel

### fields
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataField]
- **Required**: Yes

### primaryKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### isJoinTable
- **Type**: typing.Optional[bool]


# CodegenGenericDataModelOutput

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldOutput]
- **Required**: Yes

### primaryKeys
- **Type**: typing.List[str]
- **Required**: Yes

### isJoinTable
- **Type**: typing.Optional[bool]


# CodegenGenericDataModelUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataNonModel

### fields
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldUnion]
- **Required**: Yes


# CodegenGenericDataNonModelOutput

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataFieldOutput]
- **Required**: Yes


# CodegenGenericDataNonModelUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataRelationshipTypeOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenGenericDataRelationshipTypeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenJob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenJobAsset

### downloadUrl
- **Type**: typing.Optional[str]


# CodegenJobGenericDataSchema

### dataSourceType
- **Type**: typing.Literal['DataStore']
- **Required**: Yes

### models
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataModelUnion]
- **Required**: Yes

### enums
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataEnumUnion]
- **Required**: Yes

### nonModels
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataNonModelUnion]
- **Required**: Yes


# CodegenJobGenericDataSchemaOutput

### dataSourceType
- **Type**: typing.Literal['DataStore']
- **Required**: Yes

### models
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataModelOutput]
- **Required**: Yes

### enums
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataEnumOutput]
- **Required**: Yes

### nonModels
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenGenericDataNonModelOutput]
- **Required**: Yes


# CodegenJobGenericDataSchemaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenJobRenderConfig

### react
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ReactStartCodegenJobDataUnion]


# CodegenJobRenderConfigOutput

### react
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ReactStartCodegenJobDataOutput]


# CodegenJobRenderConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodegenJobSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Component

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentBindingPropertiesValueProperties

### model
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### predicates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateUnion]]

### userAttribute
- **Type**: typing.Optional[str]

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### slotName
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValuePropertiesOutput

### model
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### predicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateOutput]]

### userAttribute
- **Type**: typing.Optional[str]

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### slotName
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValuePropertiesPaginator

### model
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### predicates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicatePaginator]]

### userAttribute
- **Type**: typing.Optional[str]

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### slotName
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentChild

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentProperty]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEvent]]

### sourceId
- **Type**: typing.Optional[str]


# ComponentChildOutput

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyOutput]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventOutput]]

### sourceId
- **Type**: typing.Optional[str]


# ComponentChildPaginator

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyPaginator]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventPaginator]]

### sourceId
- **Type**: typing.Optional[str]


# ComponentChildUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentDataConfiguration

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SortProperty]]

### predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateUnion]

### identifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# ComponentDataConfigurationOutput

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SortProperty]]

### predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicateOutput]

### identifiers
- **Type**: typing.Optional[typing.List[str]]


# ComponentDataConfigurationPaginator

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SortProperty]]

### predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PredicatePaginator]

### identifiers
- **Type**: typing.Optional[typing.List[str]]


# ComponentDataConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentEvent

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ActionParametersUnion]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentEventOutput

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ActionParametersOutput]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentEventPaginator

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ActionParametersPaginator]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentEventUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentProperty

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyPaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentPropertyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ComponentVariant

### variantValues
- **Type**: typing.Optional[typing.Mapping[str, str]]

### overrides
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]


# ComponentVariantOutput

### variantValues
- **Type**: typing.Optional[typing.Dict[str, str]]

### overrides
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]


# ComponentVariantUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateComponentData

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPropertyUnion]
- **Required**: Yes

### variants
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentVariantUnion]
- **Required**: Yes

### overrides
- **Type**: typing.Mapping[str, typing.Mapping[str, str]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentBindingPropertiesValueUnion]
- **Required**: Yes

### sourceId
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentChildUnion]]

### collectionProperties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentDataConfigurationUnion]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### events
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentEventUnion]]

### schemaVersion
- **Type**: typing.Optional[str]


# CreateComponentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### componentToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CreateComponentData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateComponentResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFormData

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormDataTypeConfig'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### fields
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldConfigUnion]
- **Required**: Yes

### style
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyle'>
- **Required**: Yes

### sectionalElements
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SectionalElement]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormCTA]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# CreateFormRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### formToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CreateFormData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateFormResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Form'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThemeData

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuesUnion]
- **Required**: Yes

### overrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValues]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateThemeRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### themeToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CreateThemeData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateThemeResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ExchangeCodeForTokenRequest

### provider
- **Type**: typing.Literal['figma']
- **Required**: Yes

### request
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ExchangeCodeForTokenRequestBody'>
- **Required**: Yes


# ExchangeCodeForTokenRequestBody

### code
- **Type**: <class 'str'>
- **Required**: Yes

### redirectUri
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: typing.Optional[str]


# ExchangeCodeForTokenResponse

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### expiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### refreshToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ExportComponentsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportComponentsRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfig]


# ExportComponentsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Component]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportComponentsResponsePaginator

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportFormsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportFormsRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfig]


# ExportFormsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Form]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportFormsResponsePaginator

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportThemesRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportThemesRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfig]


# ExportThemesResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Theme]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportThemesResponsePaginator

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemePaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# FieldConfig

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPosition]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldInputConfigUnion]

### validations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldValidationConfigurationUnion]]


# FieldConfigOutput

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPosition]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldInputConfigOutput]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldValidationConfigurationOutput]]


# FieldConfigPaginator

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPosition]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldInputConfigPaginator]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldValidationConfigurationOutput]]


# FieldConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldInputConfigOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldInputConfigPaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldInputConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldPosition

### fixed
- **Type**: typing.Optional[typing.Literal['first']]

### rightOf
- **Type**: typing.Optional[str]

### below
- **Type**: typing.Optional[str]


# FieldValidationConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldValidationConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileUploaderFieldConfig

### accessLevel
- **Type**: typing.Literal['private', 'protected', 'public']
- **Required**: Yes

### acceptedFileTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### showThumbnails
- **Type**: typing.Optional[bool]

### isResumable
- **Type**: typing.Optional[bool]

### maxFileCount
- **Type**: typing.Optional[int]

### maxSize
- **Type**: typing.Optional[int]


# FileUploaderFieldConfigOutput

### accessLevel
- **Type**: typing.Literal['private', 'protected', 'public']
- **Required**: Yes

### acceptedFileTypes
- **Type**: typing.List[str]
- **Required**: Yes

### showThumbnails
- **Type**: typing.Optional[bool]

### isResumable
- **Type**: typing.Optional[bool]

### maxFileCount
- **Type**: typing.Optional[int]

### maxSize
- **Type**: typing.Optional[int]


# Form

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormButton

### excluded
- **Type**: typing.Optional[bool]

### children
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldPosition]


# FormCTA

### position
- **Type**: typing.Optional[typing.Literal['bottom', 'top', 'top_and_bottom']]

### clear
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormButton]

### cancel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormButton]

### submit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormButton]


# FormDataTypeConfig

### dataSourceType
- **Type**: typing.Literal['Custom', 'DataStore']
- **Required**: Yes

### dataTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# FormInputBindingPropertiesValue

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputBindingPropertiesValueProperties

### model
- **Type**: typing.Optional[str]


# FormInputValueProperty

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyBindingProperties]

### concat
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# FormInputValuePropertyBindingProperties

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormInputValuePropertyOutput

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyBindingProperties]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FormInputValuePropertyPaginator

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyBindingProperties]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FormInputValuePropertyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormPaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FormStyle

### horizontalGap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleConfig]

### verticalGap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleConfig]

### outerPadding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyleConfig]


# FormStyleConfig

### tokenReference
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# FormSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetCodegenJobResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetComponentResponse

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetFormResponse

### form
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Form'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetMetadataRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMetadataResponse

### features
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetThemeResponse

### theme
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GraphQLRenderConfig

### typesFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### queriesFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### mutationsFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionsFilePath
- **Type**: <class 'str'>
- **Required**: Yes

### fragmentsFilePath
- **Type**: <class 'str'>
- **Required**: Yes


# ListCodegenJobsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCodegenJobsRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfig]


# ListCodegenJobsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListComponentsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListComponentsRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfig]


# ListComponentsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ComponentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFormsRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListFormsRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfig]


# ListFormsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ListThemesRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListThemesRequestPaginate

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PaginatorConfig]


# ListThemesResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredicateOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PredicatePaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PredicateUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutMetadataFlagBody

### newValue
- **Type**: <class 'str'>
- **Required**: Yes


# PutMetadataFlagRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### featureName
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.PutMetadataFlagBody'>
- **Required**: Yes


# ReactStartCodegenJobData

### module
- **Type**: typing.Optional[typing.Literal['es2020', 'esnext']]

### target
- **Type**: typing.Optional[typing.Literal['es2015', 'es2020']]

### script
- **Type**: typing.Optional[typing.Literal['js', 'jsx', 'tsx']]

### renderTypeDeclarations
- **Type**: typing.Optional[bool]

### inlineSourceMap
- **Type**: typing.Optional[bool]

### apiConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ApiConfigurationUnion]

### dependencies
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ReactStartCodegenJobDataOutput

### module
- **Type**: typing.Optional[typing.Literal['es2020', 'esnext']]

### target
- **Type**: typing.Optional[typing.Literal['es2015', 'es2020']]

### script
- **Type**: typing.Optional[typing.Literal['js', 'jsx', 'tsx']]

### renderTypeDeclarations
- **Type**: typing.Optional[bool]

### inlineSourceMap
- **Type**: typing.Optional[bool]

### apiConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ApiConfigurationOutput]

### dependencies
- **Type**: typing.Optional[typing.Dict[str, str]]


# ReactStartCodegenJobDataUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RefreshTokenRequest

### provider
- **Type**: typing.Literal['figma']
- **Required**: Yes

### refreshTokenBody
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.RefreshTokenRequestBody'>
- **Required**: Yes


# RefreshTokenRequestBody

### token
- **Type**: <class 'str'>
- **Required**: Yes

### clientId
- **Type**: typing.Optional[str]


# RefreshTokenResponse

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### expiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
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


# SectionalElement

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SortProperty

### field
- **Type**: <class 'str'>
- **Required**: Yes

### direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# StartCodegenJobData

### renderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobRenderConfigUnion'>
- **Required**: Yes

### genericDataSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJobGenericDataSchemaUnion]

### autoGenerateForms
- **Type**: typing.Optional[bool]

### features
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenFeatureFlags]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartCodegenJobRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### codegenJobToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.StartCodegenJobData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartCodegenJobResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.CodegenJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Theme

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemePaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeValue

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# ThemeValueOutput

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ThemeValuePaginator

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ThemeValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThemeValues

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValueUnion]


# ThemeValuesOutput

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValueOutput]


# ThemeValuesPaginator

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ThemeValuePaginator]


# ThemeValuesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateComponentResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFormData

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormDataTypeConfig]

### formActionType
- **Type**: typing.Optional[typing.Literal['create', 'update']]

### fields
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FieldConfigUnion]]

### style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormStyle]

### sectionalElements
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.SectionalElement]]

### schemaVersion
- **Type**: typing.Optional[str]

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormCTA]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# UpdateFormResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Form'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateThemeResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ValueMapping

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyUnion'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyUnion]


# ValueMappingOutput

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyOutput'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyOutput]


# ValueMappingPaginator

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyPaginator'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputValuePropertyPaginator]


# ValueMappingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ValueMappings

### values
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingUnion]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValue]]


# ValueMappingsOutput

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingOutput]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValue]]


# ValueMappingsPaginator

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder_classes.ValueMappingPaginator]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder_classes.FormInputBindingPropertiesValue]]



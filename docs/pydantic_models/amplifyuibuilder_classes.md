# Amplifyuibuilder Classes

# ActionParameters

### type
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput, NoneType]

### url
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput, NoneType]

### anchor
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput, NoneType]

### target
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput, NoneType]

### global_
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput, NoneType]

### model
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput, NoneType]

### fields
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty]]

### state
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.MutationActionSetStateParameter, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.MutationActionSetStateParameterOutput, NoneType]


# ActionParametersOutput

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]

### url
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]

### anchor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]

### global_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]

### model
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]

### fields
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.MutationActionSetStateParameterOutput]


# ActionParametersPaginator

### type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]

### url
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]

### anchor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]

### target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]

### global_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]

### model
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]

### fields
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.MutationActionSetStateParameterPaginator]


# ApiConfiguration

### graphQLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.GraphQLRenderConfig]

### dataStoreConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### noApiConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ApiConfigurationOutput

### graphQLConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.GraphQLRenderConfig]

### dataStoreConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### noApiConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


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
- **Type**: typing.List[str]
- **Required**: Yes


# CodegenGenericDataEnumOutput

### values
- **Type**: typing.List[str]
- **Required**: Yes


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataRelationshipType, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataRelationshipTypeOutput, NoneType]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataRelationshipTypeOutput]


# CodegenGenericDataModel

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataField]
- **Required**: Yes

### primaryKeys
- **Type**: typing.List[str]
- **Required**: Yes

### isJoinTable
- **Type**: typing.Optional[bool]


# CodegenGenericDataModelOutput

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataFieldOutput]
- **Required**: Yes

### primaryKeys
- **Type**: typing.List[str]
- **Required**: Yes

### isJoinTable
- **Type**: typing.Optional[bool]


# CodegenGenericDataNonModel

### fields
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataField, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataFieldOutput]]
- **Required**: Yes


# CodegenGenericDataNonModelOutput

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataFieldOutput]
- **Required**: Yes


# CodegenGenericDataRelationshipType

### type
- **Type**: typing.Literal['BELONGS_TO', 'HAS_MANY', 'HAS_ONE']
- **Required**: Yes

### relatedModelName
- **Type**: <class 'str'>
- **Required**: Yes

### relatedModelFields
- **Type**: typing.Optional[typing.List[str]]

### canUnlinkAssociatedModel
- **Type**: typing.Optional[bool]

### relatedJoinFieldName
- **Type**: typing.Optional[str]

### relatedJoinTableName
- **Type**: typing.Optional[str]

### belongsToFieldOnRelatedModel
- **Type**: typing.Optional[str]

### associatedFields
- **Type**: typing.Optional[typing.List[str]]

### isHasManyIndex
- **Type**: typing.Optional[bool]


# CodegenGenericDataRelationshipTypeOutput

### type
- **Type**: typing.Literal['BELONGS_TO', 'HAS_MANY', 'HAS_ONE']
- **Required**: Yes

### relatedModelName
- **Type**: <class 'str'>
- **Required**: Yes

### relatedModelFields
- **Type**: typing.Optional[typing.List[str]]

### canUnlinkAssociatedModel
- **Type**: typing.Optional[bool]

### relatedJoinFieldName
- **Type**: typing.Optional[str]

### relatedJoinTableName
- **Type**: typing.Optional[str]

### belongsToFieldOnRelatedModel
- **Type**: typing.Optional[str]

### associatedFields
- **Type**: typing.Optional[typing.List[str]]

### isHasManyIndex
- **Type**: typing.Optional[bool]


# CodegenJob

### id
- **Type**: <class 'str'>
- **Required**: Yes

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### renderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJobRenderConfigOutput]

### genericDataSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJobGenericDataSchemaOutput]

### autoGenerateForms
- **Type**: typing.Optional[bool]

### features
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenFeatureFlags]

### status
- **Type**: typing.Optional[typing.Literal['failed', 'in_progress', 'succeeded']]

### statusMessage
- **Type**: typing.Optional[str]

### asset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJobAsset]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### dependencies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenDependency]]


# CodegenJobAsset

### downloadUrl
- **Type**: typing.Optional[str]


# CodegenJobGenericDataSchema

### dataSourceType
- **Type**: typing.Literal['DataStore']
- **Required**: Yes

### models
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataModel, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataModelOutput]]
- **Required**: Yes

### enums
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataEnum, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataEnumOutput]]
- **Required**: Yes

### nonModels
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataNonModel, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataNonModelOutput]]
- **Required**: Yes


# CodegenJobGenericDataSchemaOutput

### dataSourceType
- **Type**: typing.Literal['DataStore']
- **Required**: Yes

### models
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataModelOutput]
- **Required**: Yes

### enums
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataEnumOutput]
- **Required**: Yes

### nonModels
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenGenericDataNonModelOutput]
- **Required**: Yes


# CodegenJobRenderConfig

### react
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ReactStartCodegenJobData, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ReactStartCodegenJobDataOutput, NoneType]


# CodegenJobRenderConfigOutput

### react
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ReactStartCodegenJobDataOutput]


# CodegenJobSummary

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]


# Component

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]
- **Required**: Yes

### variants
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentVariantOutput]
- **Required**: Yes

### overrides
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValueOutput]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sourceId
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentChildOutput]]

### collectionProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentDataConfigurationOutput]]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEventOutput]]

### schemaVersion
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValue

### type
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValueProperties, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValuePropertiesOutput, NoneType]

### defaultValue
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValueOutput

### type
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValuePropertiesOutput]

### defaultValue
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValuePaginator

### type
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValuePropertiesPaginator]

### defaultValue
- **Type**: typing.Optional[str]


# ComponentBindingPropertiesValueProperties

### model
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### predicates
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Predicate, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PredicateOutput]]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PredicateOutput]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PredicatePaginator]]

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


# ComponentChild

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEvent]]

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEventOutput]]

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]
- **Required**: Yes

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEventPaginator]]

### sourceId
- **Type**: typing.Optional[str]


# ComponentConditionProperty

### property
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### then
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### else_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### operandType
- **Type**: typing.Optional[str]


# ComponentConditionPropertyOutput

### property
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### then
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### else_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### operandType
- **Type**: typing.Optional[str]


# ComponentConditionPropertyPaginator

### property
- **Type**: typing.Optional[str]

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### then
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### else_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### operandType
- **Type**: typing.Optional[str]


# ComponentDataConfiguration

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.SortProperty]]

### predicate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Predicate, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PredicateOutput, NoneType]

### identifiers
- **Type**: typing.Optional[typing.List[str]]


# ComponentDataConfigurationOutput

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.SortProperty]]

### predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PredicateOutput]

### identifiers
- **Type**: typing.Optional[typing.List[str]]


# ComponentDataConfigurationPaginator

### model
- **Type**: <class 'str'>
- **Required**: Yes

### sort
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.SortProperty]]

### predicate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PredicatePaginator]

### identifiers
- **Type**: typing.Optional[typing.List[str]]


# ComponentEvent

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ActionParameters, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ActionParametersOutput, NoneType]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentEventOutput

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ActionParametersOutput]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentEventPaginator

### action
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ActionParametersPaginator]

### bindingEvent
- **Type**: typing.Optional[str]


# ComponentPaginator

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator]
- **Required**: Yes

### variants
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentVariantOutput]
- **Required**: Yes

### overrides
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValuePaginator]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sourceId
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentChildPaginator]]

### collectionProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentDataConfigurationPaginator]]

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### events
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEventPaginator]]

### schemaVersion
- **Type**: typing.Optional[str]


# ComponentProperty

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyBindingProperties]

### collectionBindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyBindingProperties]

### defaultValue
- **Type**: typing.Optional[str]

### model
- **Type**: typing.Optional[str]

### bindings
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormBindingElement]]

### event
- **Type**: typing.Optional[str]

### userAttribute
- **Type**: typing.Optional[str]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### condition
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentConditionProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentConditionPropertyOutput, NoneType]

### configured
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[str]

### importedValue
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### property
- **Type**: typing.Optional[str]


# ComponentPropertyBindingProperties

### property
- **Type**: <class 'str'>
- **Required**: Yes

### field
- **Type**: typing.Optional[str]


# ComponentPropertyOutput

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyBindingProperties]

### collectionBindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyBindingProperties]

### defaultValue
- **Type**: typing.Optional[str]

### model
- **Type**: typing.Optional[str]

### bindings
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormBindingElement]]

### event
- **Type**: typing.Optional[str]

### userAttribute
- **Type**: typing.Optional[str]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentConditionPropertyOutput]

### configured
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[str]

### importedValue
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### property
- **Type**: typing.Optional[str]


# ComponentPropertyPaginator

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyBindingProperties]

### collectionBindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyBindingProperties]

### defaultValue
- **Type**: typing.Optional[str]

### model
- **Type**: typing.Optional[str]

### bindings
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormBindingElement]]

### event
- **Type**: typing.Optional[str]

### userAttribute
- **Type**: typing.Optional[str]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentConditionPropertyPaginator]

### configured
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[str]

### importedValue
- **Type**: typing.Optional[str]

### componentName
- **Type**: typing.Optional[str]

### property
- **Type**: typing.Optional[str]


# ComponentSummary

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes


# ComponentVariant

### variantValues
- **Type**: typing.Optional[typing.Dict[str, str]]

### overrides
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]


# ComponentVariantOutput

### variantValues
- **Type**: typing.Optional[typing.Dict[str, str]]

### overrides
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]


# CreateComponentData

### name
- **Type**: <class 'str'>
- **Required**: Yes

### componentType
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]]
- **Required**: Yes

### variants
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentVariant, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentVariantOutput]]
- **Required**: Yes

### overrides
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValue, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValueOutput]]
- **Required**: Yes

### sourceId
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentChild, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentChildOutput]]]

### collectionProperties
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentDataConfiguration, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentDataConfigurationOutput]]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### events
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEvent, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEventOutput]]]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CreateComponentData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateComponentResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFormData

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormDataTypeConfig'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### fields
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldConfig, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldConfigOutput]]
- **Required**: Yes

### style
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormStyle'>
- **Required**: Yes

### sectionalElements
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.SectionalElement]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormCTA]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CreateFormData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateFormResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Form'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThemeData

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValues, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValuesOutput]]
- **Required**: Yes

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValues]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateThemeRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### themeToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CreateThemeData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateThemeResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteComponentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFormRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThemeRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ExchangeCodeForTokenRequest

### provider
- **Type**: typing.Literal['figma']
- **Required**: Yes

### request
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ExchangeCodeForTokenRequestBody'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PaginatorConfig]


# ExportComponentsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Component]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportComponentsResponsePaginator

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PaginatorConfig]


# ExportFormsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Form]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportFormsResponsePaginator

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PaginatorConfig]


# ExportThemesResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Theme]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ExportThemesResponsePaginator

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemePaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# FieldConfig

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldPosition]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldInputConfig, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldInputConfigOutput, NoneType]

### validations
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldValidationConfiguration, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldValidationConfigurationOutput]]]


# FieldConfigOutput

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldPosition]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldInputConfigOutput]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldValidationConfigurationOutput]]


# FieldConfigPaginator

### label
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldPosition]

### excluded
- **Type**: typing.Optional[bool]

### inputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldInputConfigPaginator]

### validations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldValidationConfigurationOutput]]


# FieldInputConfig

### type
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]

### readOnly
- **Type**: typing.Optional[bool]

### placeholder
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### descriptiveText
- **Type**: typing.Optional[str]

### defaultChecked
- **Type**: typing.Optional[bool]

### defaultCountryCode
- **Type**: typing.Optional[str]

### valueMappings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ValueMappings, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ValueMappingsOutput, NoneType]

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]

### step
- **Type**: typing.Optional[float]

### value
- **Type**: typing.Optional[str]

### isArray
- **Type**: typing.Optional[bool]

### fileUploaderConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FileUploaderFieldConfig, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FileUploaderFieldConfigOutput, NoneType]


# FieldInputConfigOutput

### type
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]

### readOnly
- **Type**: typing.Optional[bool]

### placeholder
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### descriptiveText
- **Type**: typing.Optional[str]

### defaultChecked
- **Type**: typing.Optional[bool]

### defaultCountryCode
- **Type**: typing.Optional[str]

### valueMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ValueMappingsOutput]

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]

### step
- **Type**: typing.Optional[float]

### value
- **Type**: typing.Optional[str]

### isArray
- **Type**: typing.Optional[bool]

### fileUploaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FileUploaderFieldConfigOutput]


# FieldInputConfigPaginator

### type
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: typing.Optional[bool]

### readOnly
- **Type**: typing.Optional[bool]

### placeholder
- **Type**: typing.Optional[str]

### defaultValue
- **Type**: typing.Optional[str]

### descriptiveText
- **Type**: typing.Optional[str]

### defaultChecked
- **Type**: typing.Optional[bool]

### defaultCountryCode
- **Type**: typing.Optional[str]

### valueMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ValueMappingsPaginator]

### name
- **Type**: typing.Optional[str]

### minValue
- **Type**: typing.Optional[float]

### maxValue
- **Type**: typing.Optional[float]

### step
- **Type**: typing.Optional[float]

### value
- **Type**: typing.Optional[str]

### isArray
- **Type**: typing.Optional[bool]

### fileUploaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FileUploaderFieldConfigOutput]


# FieldPosition

### fixed
- **Type**: typing.Optional[typing.Literal['first']]

### rightOf
- **Type**: typing.Optional[str]

### below
- **Type**: typing.Optional[str]


# FieldValidationConfiguration

### type
- **Type**: <class 'str'>
- **Required**: Yes

### strValues
- **Type**: typing.Optional[typing.List[str]]

### numValues
- **Type**: typing.Optional[typing.List[int]]

### validationMessage
- **Type**: typing.Optional[str]


# FieldValidationConfigurationOutput

### type
- **Type**: <class 'str'>
- **Required**: Yes

### strValues
- **Type**: typing.Optional[typing.List[str]]

### numValues
- **Type**: typing.Optional[typing.List[int]]

### validationMessage
- **Type**: typing.Optional[str]


# FileUploaderFieldConfig

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

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### style
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormStyle'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormDataTypeConfig'>
- **Required**: Yes

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldConfigOutput]
- **Required**: Yes

### sectionalElements
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.SectionalElement]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormCTA]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# FormBindingElement

### element
- **Type**: <class 'str'>
- **Required**: Yes

### property
- **Type**: <class 'str'>
- **Required**: Yes


# FormButton

### excluded
- **Type**: typing.Optional[bool]

### children
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldPosition]


# FormCTA

### position
- **Type**: typing.Optional[typing.Literal['bottom', 'top', 'top_and_bottom']]

### clear
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormButton]

### cancel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormButton]

### submit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormButton]


# FormDataTypeConfig

### dataSourceType
- **Type**: typing.Literal['Custom', 'DataStore']
- **Required**: Yes

### dataTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# FormInputBindingPropertiesValue

### type
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputBindingPropertiesValueProperties]


# FormInputBindingPropertiesValueProperties

### model
- **Type**: typing.Optional[str]


# FormInputValueProperty

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyBindingProperties]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FormInputValuePropertyBindingProperties

### property
- **Type**: <class 'str'>
- **Required**: Yes

### field
- **Type**: typing.Optional[str]


# FormInputValuePropertyOutput

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyBindingProperties]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FormInputValuePropertyPaginator

### value
- **Type**: typing.Optional[str]

### bindingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyBindingProperties]

### concat
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# FormPaginator

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### style
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormStyle'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormDataTypeConfig'>
- **Required**: Yes

### fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldConfigPaginator]
- **Required**: Yes

### sectionalElements
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.SectionalElement]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormCTA]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# FormStyle

### horizontalGap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormStyleConfig]

### verticalGap
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormStyleConfig]

### outerPadding
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormStyleConfig]


# FormStyleConfig

### tokenReference
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# FormSummary

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### dataType
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormDataTypeConfig'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### formActionType
- **Type**: typing.Literal['create', 'update']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCodegenJobRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCodegenJobResponse

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetComponentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetComponentResponse

### component
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetFormRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFormResponse

### form
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Form'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# GetThemeRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetThemeResponse

### theme
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PaginatorConfig]


# ListCodegenJobsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PaginatorConfig]


# ListComponentsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PaginatorConfig]


# ListFormsResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PaginatorConfig]


# ListThemesResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MutationActionSetStateParameter

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### property
- **Type**: <class 'str'>
- **Required**: Yes

### set
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]
- **Required**: Yes


# MutationActionSetStateParameterOutput

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### property
- **Type**: <class 'str'>
- **Required**: Yes

### set
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput'>
- **Required**: Yes


# MutationActionSetStateParameterPaginator

### componentName
- **Type**: <class 'str'>
- **Required**: Yes

### property
- **Type**: <class 'str'>
- **Required**: Yes

### set
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyPaginator'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Predicate

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### operandType
- **Type**: typing.Optional[str]


# PredicateOutput

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### operandType
- **Type**: typing.Optional[str]


# PredicatePaginator

### or_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### and_
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### field
- **Type**: typing.Optional[str]

### operator
- **Type**: typing.Optional[str]

### operand
- **Type**: typing.Optional[str]

### operandType
- **Type**: typing.Optional[str]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.PutMetadataFlagBody'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ApiConfiguration, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ApiConfigurationOutput, NoneType]

### dependencies
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ApiConfigurationOutput]

### dependencies
- **Type**: typing.Optional[typing.Dict[str, str]]


# RefreshTokenRequest

### provider
- **Type**: typing.Literal['figma']
- **Required**: Yes

### refreshTokenBody
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.RefreshTokenRequestBody'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
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

### type
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldPosition]

### text
- **Type**: typing.Optional[str]

### level
- **Type**: typing.Optional[int]

### orientation
- **Type**: typing.Optional[str]

### excluded
- **Type**: typing.Optional[bool]


# SortProperty

### field
- **Type**: <class 'str'>
- **Required**: Yes

### direction
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# StartCodegenJobData

### renderConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJobRenderConfig, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJobRenderConfigOutput]
- **Required**: Yes

### genericDataSchema
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJobGenericDataSchema, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJobGenericDataSchemaOutput, NoneType]

### autoGenerateForms
- **Type**: typing.Optional[bool]

### features
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenFeatureFlags]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartCodegenJobRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### codegenJobToCreate
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.StartCodegenJobData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartCodegenJobResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.CodegenJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Theme

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValuesOutput]
- **Required**: Yes

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValuesOutput]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ThemePaginator

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValuesPaginator]
- **Required**: Yes

### modifiedAt
- **Type**: typing.Optional[datetime.datetime]

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValuesPaginator]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ThemeSummary

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ThemeValue

### value
- **Type**: typing.Optional[str]

### children
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


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


# ThemeValues

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValue, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValueOutput, NoneType]


# ThemeValuesOutput

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValueOutput]


# ThemeValuesPaginator

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValuePaginator]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateComponentData

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### sourceId
- **Type**: typing.Optional[str]

### componentType
- **Type**: typing.Optional[str]

### properties
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentPropertyOutput]]]

### children
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentChild, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentChildOutput]]]

### variants
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentVariant, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentVariantOutput]]]

### overrides
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValue, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentBindingPropertiesValueOutput]]]

### collectionProperties
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentDataConfiguration, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentDataConfigurationOutput]]]

### events
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEvent, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ComponentEventOutput]]]

### schemaVersion
- **Type**: typing.Optional[str]


# UpdateComponentRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### updatedComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.UpdateComponentData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateComponentResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Component'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFormData

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormDataTypeConfig]

### formActionType
- **Type**: typing.Optional[typing.Literal['create', 'update']]

### fields
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldConfig, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FieldConfigOutput]]]

### style
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormStyle]

### sectionalElements
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.SectionalElement]]

### schemaVersion
- **Type**: typing.Optional[str]

### cta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormCTA]

### labelDecorator
- **Type**: typing.Optional[typing.Literal['none', 'optional', 'required']]


# UpdateFormRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### updatedForm
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.UpdateFormData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateFormResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Form'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateThemeData

### values
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValues, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValuesOutput]]
- **Required**: Yes

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### overrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ThemeValues]]


# UpdateThemeRequest

### appId
- **Type**: <class 'str'>
- **Required**: Yes

### environmentName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### updatedTheme
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.UpdateThemeData'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateThemeResponse

### entity
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.Theme'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ResponseMetadata'>
- **Required**: Yes


# ValueMapping

### value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValueProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyOutput]
- **Required**: Yes

### displayValue
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValueProperty, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyOutput, NoneType]


# ValueMappingOutput

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyOutput'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyOutput]


# ValueMappingPaginator

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyPaginator'>
- **Required**: Yes

### displayValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputValuePropertyPaginator]


# ValueMappings

### values
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ValueMapping, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ValueMappingOutput]]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputBindingPropertiesValue]]


# ValueMappingsOutput

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ValueMappingOutput]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputBindingPropertiesValue]]


# ValueMappingsPaginator

### values
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.ValueMappingPaginator]
- **Required**: Yes

### bindingProperties
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.amplifyuibuilder.amplifyuibuilder_classes.FormInputBindingPropertiesValue]]



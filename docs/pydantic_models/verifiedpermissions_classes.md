# Verifiedpermissions Classes

# ActionIdentifier

### actionType
- **Type**: <class 'str'>
- **Required**: Yes

### actionId
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeValue

### boolean
- **Type**: typing.Optional[bool]

### entityIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### long
- **Type**: typing.Optional[int]

### string
- **Type**: typing.Optional[str]

### set
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### record
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### ipaddr
- **Type**: typing.Optional[str]

### decimal
- **Type**: typing.Optional[str]


# AttributeValueOutput

### boolean
- **Type**: typing.Optional[bool]

### entityIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### long
- **Type**: typing.Optional[int]

### string
- **Type**: typing.Optional[str]

### set
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### record
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### ipaddr
- **Type**: typing.Optional[str]

### decimal
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetPolicyErrorItem

### code
- **Type**: typing.Literal['POLICY_NOT_FOUND', 'POLICY_STORE_NOT_FOUND']
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetPolicyInput

### requests
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchGetPolicyInputItem]
- **Required**: Yes


# BatchGetPolicyInputItem

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetPolicyOutput

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchGetPolicyOutputItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchGetPolicyErrorItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetPolicyOutputItem

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyDefinitionDetail'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# BatchIsAuthorizedInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### requests
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchIsAuthorizedInputItem, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchIsAuthorizedInputItemOutput]]
- **Required**: Yes

### entities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntitiesDefinition]


# BatchIsAuthorizedInputItem

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### context
- **Type**: typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinition, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinitionOutput, NoneType]


# BatchIsAuthorizedInputItemOutput

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinitionOutput]


# BatchIsAuthorizedOutput

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchIsAuthorizedOutputItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# BatchIsAuthorizedOutputItem

### request
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchIsAuthorizedInputItemOutput'>
- **Required**: Yes

### decision
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### determiningPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.DeterminingPolicyItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EvaluationErrorItem]
- **Required**: Yes


# BatchIsAuthorizedWithTokenInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### requests
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchIsAuthorizedWithTokenInputItem, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchIsAuthorizedWithTokenInputItemOutput]]
- **Required**: Yes

### identityToken
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]

### entities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntitiesDefinition]


# BatchIsAuthorizedWithTokenInputItem

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### context
- **Type**: typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinition, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinitionOutput, NoneType]


# BatchIsAuthorizedWithTokenInputItemOutput

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### context
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinitionOutput]


# BatchIsAuthorizedWithTokenOutput

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchIsAuthorizedWithTokenOutputItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# BatchIsAuthorizedWithTokenOutputItem

### request
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.BatchIsAuthorizedWithTokenInputItemOutput'>
- **Required**: Yes

### decision
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### determiningPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.DeterminingPolicyItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EvaluationErrorItem]
- **Required**: Yes


# CognitoGroupConfiguration

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# CognitoGroupConfigurationDetail

### groupEntityType
- **Type**: typing.Optional[str]


# CognitoGroupConfigurationItem

### groupEntityType
- **Type**: typing.Optional[str]


# CognitoUserPoolConfiguration

### userPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientIds
- **Type**: typing.Optional[typing.List[str]]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.CognitoGroupConfiguration]


# CognitoUserPoolConfigurationDetail

### userPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientIds
- **Type**: typing.List[str]
- **Required**: Yes

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.CognitoGroupConfigurationDetail]


# CognitoUserPoolConfigurationItem

### userPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientIds
- **Type**: typing.List[str]
- **Required**: Yes

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.CognitoGroupConfigurationItem]


# Configuration

### cognitoUserPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.CognitoUserPoolConfiguration]

### openIdConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectConfiguration]


# ConfigurationDetail

### cognitoUserPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.CognitoUserPoolConfigurationDetail]

### openIdConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectConfigurationDetail]


# ConfigurationItem

### cognitoUserPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.CognitoUserPoolConfigurationItem]

### openIdConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectConfigurationItem]


# ContextDefinition

### contextMap
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.AttributeValue, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.AttributeValueOutput]]]

### cedarJson
- **Type**: typing.Optional[str]


# ContextDefinitionOutput

### contextMap
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.AttributeValueOutput]]

### cedarJson
- **Type**: typing.Optional[str]


# CreateIdentitySourceInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.Configuration'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### principalEntityType
- **Type**: typing.Optional[str]


# CreateIdentitySourceOutput

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePolicyInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyDefinition'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreatePolicyOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Forbid', 'Permit']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePolicyStoreInput

### validationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ValidationSettings'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreatePolicyStoreOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePolicyTemplateInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreatePolicyTemplateOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIdentitySourceInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyStoreInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyTemplateInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeterminingPolicyItem

### policyId
- **Type**: <class 'str'>
- **Required**: Yes


# EntitiesDefinition

### entityList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityItem]]

### cedarJson
- **Type**: typing.Optional[str]


# EntityIdentifier

### entityType
- **Type**: <class 'str'>
- **Required**: Yes

### entityId
- **Type**: <class 'str'>
- **Required**: Yes


# EntityItem

### identifier
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.AttributeValue, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.AttributeValueOutput]]]

### parents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]]


# EntityReference

### unspecified
- **Type**: typing.Optional[bool]

### identifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]


# EvaluationErrorItem

### errorDescription
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentitySourceInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentitySourceOutput

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.IdentitySourceDetails'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### principalEntityType
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ConfigurationDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyDefinitionDetail'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Forbid', 'Permit']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyStoreInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyStoreOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### validationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ValidationSettings'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyTemplateInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyTemplateOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# GetSchemaInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSchemaOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.GetSchemaOutput'>>

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### namespaces
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# IdentitySourceDetails

### clientIds
- **Type**: typing.Optional[typing.List[str]]

### userPoolArn
- **Type**: typing.Optional[str]

### discoveryUrl
- **Type**: typing.Optional[str]

### openIdIssuer
- **Type**: typing.Optional[typing.Literal['COGNITO']]


# IdentitySourceFilter

### principalEntityType
- **Type**: typing.Optional[str]


# IdentitySourceItem

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### principalEntityType
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.IdentitySourceItemDetails]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ConfigurationItem]


# IdentitySourceItemDetails

### clientIds
- **Type**: typing.Optional[typing.List[str]]

### userPoolArn
- **Type**: typing.Optional[str]

### discoveryUrl
- **Type**: typing.Optional[str]

### openIdIssuer
- **Type**: typing.Optional[typing.Literal['COGNITO']]


# IsAuthorizedInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### context
- **Type**: typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinition, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinitionOutput, NoneType]

### entities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntitiesDefinition]


# IsAuthorizedOutput

### decision
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### determiningPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.DeterminingPolicyItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EvaluationErrorItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# IsAuthorizedWithTokenInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### identityToken
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### context
- **Type**: typing.Union[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinition, aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ContextDefinitionOutput, NoneType]

### entities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntitiesDefinition]


# IsAuthorizedWithTokenOutput

### decision
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### determiningPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.DeterminingPolicyItem]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EvaluationErrorItem]
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# ListIdentitySourcesInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.IdentitySourceFilter]]


# ListIdentitySourcesInputPaginate

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.IdentitySourceFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PaginatorConfig]


# ListIdentitySourcesOutput

### identitySources
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.IdentitySourceItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPoliciesInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyFilter]


# ListPoliciesInputPaginate

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PaginatorConfig]


# ListPoliciesOutput

### policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyStoresInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPolicyStoresInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PaginatorConfig]


# ListPolicyStoresOutput

### policyStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyStoreItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPolicyTemplatesInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPolicyTemplatesInputPaginate

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PaginatorConfig]


# ListPolicyTemplatesOutput

### policyTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyTemplateItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# OpenIdConnectAccessTokenConfiguration

### principalIdClaim
- **Type**: typing.Optional[str]

### audiences
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectAccessTokenConfigurationDetail

### principalIdClaim
- **Type**: typing.Optional[str]

### audiences
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectAccessTokenConfigurationItem

### principalIdClaim
- **Type**: typing.Optional[str]

### audiences
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectConfiguration

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### tokenSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectTokenSelection'>
- **Required**: Yes

### entityIdPrefix
- **Type**: typing.Optional[str]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectGroupConfiguration]


# OpenIdConnectConfigurationDetail

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### tokenSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectTokenSelectionDetail'>
- **Required**: Yes

### entityIdPrefix
- **Type**: typing.Optional[str]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectGroupConfigurationDetail]


# OpenIdConnectConfigurationItem

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### tokenSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectTokenSelectionItem'>
- **Required**: Yes

### entityIdPrefix
- **Type**: typing.Optional[str]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectGroupConfigurationItem]


# OpenIdConnectGroupConfiguration

### groupClaim
- **Type**: <class 'str'>
- **Required**: Yes

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# OpenIdConnectGroupConfigurationDetail

### groupClaim
- **Type**: <class 'str'>
- **Required**: Yes

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# OpenIdConnectGroupConfigurationItem

### groupClaim
- **Type**: <class 'str'>
- **Required**: Yes

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# OpenIdConnectIdentityTokenConfiguration

### principalIdClaim
- **Type**: typing.Optional[str]

### clientIds
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectIdentityTokenConfigurationDetail

### principalIdClaim
- **Type**: typing.Optional[str]

### clientIds
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectIdentityTokenConfigurationItem

### principalIdClaim
- **Type**: typing.Optional[str]

### clientIds
- **Type**: typing.Optional[typing.List[str]]


# OpenIdConnectTokenSelection

### accessTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectAccessTokenConfiguration]

### identityTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectIdentityTokenConfiguration]


# OpenIdConnectTokenSelectionDetail

### accessTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectAccessTokenConfigurationDetail]

### identityTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectIdentityTokenConfigurationDetail]


# OpenIdConnectTokenSelectionItem

### accessTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectAccessTokenConfigurationItem]

### identityTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.OpenIdConnectIdentityTokenConfigurationItem]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolicyDefinition

### static
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.StaticPolicyDefinition]

### templateLinked
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.TemplateLinkedPolicyDefinition]


# PolicyDefinitionDetail

### static
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.StaticPolicyDefinitionDetail]

### templateLinked
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.TemplateLinkedPolicyDefinitionDetail]


# PolicyDefinitionItem

### static
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.StaticPolicyDefinitionItem]

### templateLinked
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.TemplateLinkedPolicyDefinitionItem]


# PolicyFilter

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityReference]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityReference]

### policyType
- **Type**: typing.Optional[typing.Literal['STATIC', 'TEMPLATE_LINKED']]

### policyTemplateId
- **Type**: typing.Optional[str]


# PolicyItem

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.PolicyDefinitionItem'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]]

### effect
- **Type**: typing.Optional[typing.Literal['Forbid', 'Permit']]


# PolicyStoreItem

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]


# PolicyTemplateItem

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# PutSchemaInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.SchemaDefinition'>
- **Required**: Yes


# PutSchemaOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### namespaces
- **Type**: typing.List[str]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
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


# SchemaDefinition

### cedarJson
- **Type**: typing.Optional[str]


# StaticPolicyDefinition

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StaticPolicyDefinitionDetail

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# StaticPolicyDefinitionItem

### description
- **Type**: typing.Optional[str]


# TemplateLinkedPolicyDefinition

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]


# TemplateLinkedPolicyDefinitionDetail

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]


# TemplateLinkedPolicyDefinitionItem

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier]


# UpdateCognitoGroupConfiguration

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateCognitoUserPoolConfiguration

### userPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientIds
- **Type**: typing.Optional[typing.List[str]]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateCognitoGroupConfiguration]


# UpdateConfiguration

### cognitoUserPoolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateCognitoUserPoolConfiguration]

### openIdConnectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateOpenIdConnectConfiguration]


# UpdateIdentitySourceInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### updateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateConfiguration'>
- **Required**: Yes

### principalEntityType
- **Type**: typing.Optional[str]


# UpdateIdentitySourceOutput

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### identitySourceId
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateOpenIdConnectAccessTokenConfiguration

### principalIdClaim
- **Type**: typing.Optional[str]

### audiences
- **Type**: typing.Optional[typing.List[str]]


# UpdateOpenIdConnectConfiguration

### issuer
- **Type**: <class 'str'>
- **Required**: Yes

### tokenSelection
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateOpenIdConnectTokenSelection'>
- **Required**: Yes

### entityIdPrefix
- **Type**: typing.Optional[str]

### groupConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateOpenIdConnectGroupConfiguration]


# UpdateOpenIdConnectGroupConfiguration

### groupClaim
- **Type**: <class 'str'>
- **Required**: Yes

### groupEntityType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateOpenIdConnectIdentityTokenConfiguration

### principalIdClaim
- **Type**: typing.Optional[str]

### clientIds
- **Type**: typing.Optional[typing.List[str]]


# UpdateOpenIdConnectTokenSelection

### accessTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateOpenIdConnectAccessTokenConfiguration]

### identityTokenOnly
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateOpenIdConnectIdentityTokenConfiguration]


# UpdatePolicyDefinition

### static
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdateStaticPolicyDefinition]


# UpdatePolicyInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.UpdatePolicyDefinition'>
- **Required**: Yes


# UpdatePolicyOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyId
- **Type**: <class 'str'>
- **Required**: Yes

### policyType
- **Type**: typing.Literal['STATIC', 'TEMPLATE_LINKED']
- **Required**: Yes

### principal
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### resource
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.EntityIdentifier'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ActionIdentifier]
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### effect
- **Type**: typing.Literal['Forbid', 'Permit']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePolicyStoreInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### validationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ValidationSettings'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdatePolicyStoreOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePolicyTemplateInput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdatePolicyTemplateOutput

### policyStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### policyTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### createdDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.verifiedpermissions.verifiedpermissions_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStaticPolicyDefinition

### statement
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ValidationSettings

### mode
- **Type**: typing.Literal['OFF', 'STRICT']
- **Required**: Yes



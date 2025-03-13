# Customer Profiles Classes

# AddProfileKeyRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# AddProfileKeyResponseTypeDef

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdditionalSearchKeyTypeDef

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AddressDimensionOutputTypeDef

### City
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### County
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### PostalCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### Province
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]


# AddressDimensionTypeDef

### City
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### County
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### PostalCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### Province
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]


# AddressDimensionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddressTypeDef

### Address1
- **Type**: typing.Optional[str]

### Address2
- **Type**: typing.Optional[str]

### Address3
- **Type**: typing.Optional[str]

### Address4
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### County
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### Province
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### PostalCode
- **Type**: typing.Optional[str]


# AppflowIntegrationTypeDef

### FlowDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.FlowDefinitionTypeDef'>
- **Required**: Yes

### Batches
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.BatchTypeDef]]


# AppflowIntegrationWorkflowAttributesTypeDef

### SourceConnectorType
- **Type**: typing.Literal['Marketo', 'S3', 'Salesforce', 'Servicenow', 'Zendesk']
- **Required**: Yes

### ConnectorProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]


# AppflowIntegrationWorkflowMetricsTypeDef

### RecordsProcessed
- **Type**: <class 'int'>
- **Required**: Yes

### StepsCompleted
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSteps
- **Type**: <class 'int'>
- **Required**: Yes


# AppflowIntegrationWorkflowStepTypeDef

### FlowName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'RETRY', 'SPLIT']
- **Required**: Yes

### ExecutionMessage
- **Type**: <class 'str'>
- **Required**: Yes

### RecordsProcessed
- **Type**: <class 'int'>
- **Required**: Yes

### BatchRecordsStartTime
- **Type**: <class 'str'>
- **Required**: Yes

### BatchRecordsEndTime
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# AttributeDetailsOutputTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeItemTypeDef]
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeDetailsTypeDef

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeItemTypeDef]
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeDetailsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttributeDimensionOutputTypeDef

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# AttributeDimensionTypeDef

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AttributeDimensionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttributeItemTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeTypesSelectorOutputTypeDef

### AttributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### Address
- **Type**: typing.Optional[typing.List[str]]

### PhoneNumber
- **Type**: typing.Optional[typing.List[str]]

### EmailAddress
- **Type**: typing.Optional[typing.List[str]]


# AttributeTypesSelectorTypeDef

### AttributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### Address
- **Type**: typing.Optional[typing.Sequence[str]]

### PhoneNumber
- **Type**: typing.Optional[typing.Sequence[str]]

### EmailAddress
- **Type**: typing.Optional[typing.Sequence[str]]


# AttributeTypesSelectorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AttributeValueItemTypeDef

### Value
- **Type**: typing.Optional[str]


# AutoMergingOutputTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Consolidation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConsolidationOutputTypeDef]

### ConflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConflictResolutionTypeDef]

### MinAllowedConfidenceScoreForMerging
- **Type**: typing.Optional[float]


# AutoMergingTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Consolidation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConsolidationUnionTypeDef]

### ConflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConflictResolutionTypeDef]

### MinAllowedConfidenceScoreForMerging
- **Type**: typing.Optional[float]


# AutoMergingUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetCalculatedAttributeForProfileErrorTypeDef

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCalculatedAttributeForProfileRequestTypeDef

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ConditionOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionOverridesTypeDef]


# BatchGetCalculatedAttributeForProfileResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.BatchGetCalculatedAttributeForProfileErrorTypeDef]
- **Required**: Yes

### CalculatedAttributeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.CalculatedAttributeValueTypeDef]
- **Required**: Yes

### ConditionOverrides
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionOverridesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetProfileErrorTypeDef

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetProfileRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetProfileResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.BatchGetProfileErrorTypeDef]
- **Required**: Yes

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.TimestampTypeDef'>
- **Required**: Yes


# CalculatedAttributeDimensionOutputTypeDef

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### ConditionOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionOverridesTypeDef]


# CalculatedAttributeDimensionTypeDef

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ConditionOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionOverridesTypeDef]


# CalculatedAttributeDimensionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CalculatedAttributeValueTypeDef

### CalculatedAttributeName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### IsDataPartial
- **Type**: typing.Optional[str]

### ProfileId
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ConditionOverridesTypeDef

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.RangeOverrideTypeDef]


# ConditionsTypeDef

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.RangeTypeDef]

### ObjectCount
- **Type**: typing.Optional[int]

### Threshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ThresholdTypeDef]


# ConflictResolutionTypeDef

### ConflictResolvingModel
- **Type**: typing.Literal['RECENCY', 'SOURCE']
- **Required**: Yes

### SourceName
- **Type**: typing.Optional[str]


# ConnectorOperatorTypeDef

### Marketo
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'DIVISION', 'GREATER_THAN', 'LESS_THAN', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### S3
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Salesforce
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### ServiceNow
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Zendesk
- **Type**: typing.Optional[typing.Literal['ADDITION', 'DIVISION', 'GREATER_THAN', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]


# ConsolidationOutputTypeDef

### MatchingAttributesList
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# ConsolidationTypeDef

### MatchingAttributesList
- **Type**: typing.Sequence[typing.Sequence[str]]
- **Required**: Yes


# ConsolidationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCalculatedAttributeDefinitionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeDetailsUnionTypeDef'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['AVERAGE', 'COUNT', 'FIRST_OCCURRENCE', 'LAST_OCCURRENCE', 'MAXIMUM', 'MAX_OCCURRENCE', 'MINIMUM', 'SUM']
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Conditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionsTypeDef]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.FilterUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCalculatedAttributeDefinitionResponseTypeDef

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeDetailsOutputTypeDef'>
- **Required**: Yes

### Conditions
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionsTypeDef'>
- **Required**: Yes

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.FilterOutputTypeDef'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['AVERAGE', 'COUNT', 'FIRST_OCCURRENCE', 'LAST_OCCURRENCE', 'MAXIMUM', 'MAX_OCCURRENCE', 'MINIMUM', 'SUM']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultEncryptionKey
- **Type**: typing.Optional[str]

### DeadLetterQueueUrl
- **Type**: typing.Optional[str]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.MatchingRequestTypeDef]

### RuleBasedMatching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.RuleBasedMatchingRequestTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDomainResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultEncryptionKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterQueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Matching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.MatchingResponseTypeDef'>
- **Required**: Yes

### RuleBasedMatching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.RuleBasedMatchingResponseTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventStreamRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### EventStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEventStreamResponseTypeDef

### EventStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventTriggerRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerConditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerConditionUnionTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SegmentFilter
- **Type**: typing.Optional[str]

### EventTriggerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerLimitsUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEventTriggerResponseTypeDef

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerConditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerConditionOutputTypeDef]
- **Required**: Yes

### SegmentFilter
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerLimitsOutputTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIntegrationWorkflowRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowType
- **Type**: typing.Literal['APPFLOW_INTEGRATION']
- **Required**: Yes

### IntegrationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.IntegrationConfigTypeDef'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateIntegrationWorkflowResponseTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProfileRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountNumber
- **Type**: typing.Optional[str]

### AdditionalInformation
- **Type**: typing.Optional[str]

### PartyType
- **Type**: typing.Optional[typing.Literal['BUSINESS', 'INDIVIDUAL', 'OTHER']]

### BusinessName
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### MiddleName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### BirthDate
- **Type**: typing.Optional[str]

### Gender
- **Type**: typing.Optional[typing.Literal['FEMALE', 'MALE', 'UNSPECIFIED']]

### PhoneNumber
- **Type**: typing.Optional[str]

### MobilePhoneNumber
- **Type**: typing.Optional[str]

### HomePhoneNumber
- **Type**: typing.Optional[str]

### BusinessPhoneNumber
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### PersonalEmailAddress
- **Type**: typing.Optional[str]

### BusinessEmailAddress
- **Type**: typing.Optional[str]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressTypeDef]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressTypeDef]

### MailingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressTypeDef]

### BillingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressTypeDef]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PartyTypeString
- **Type**: typing.Optional[str]

### GenderString
- **Type**: typing.Optional[str]


# CreateProfileResponseTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSegmentDefinitionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentGroups
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.SegmentGroupUnionTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSegmentDefinitionResponseTypeDef

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SegmentDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSegmentEstimateRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.SegmentGroupStructureTypeDef'>
- **Required**: Yes


# CreateSegmentEstimateResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSegmentSnapshotRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['CSV', 'JSONL', 'ORC']
- **Required**: Yes

### EncryptionKey
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### DestinationUri
- **Type**: typing.Optional[str]


# CreateSegmentSnapshotResponseTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DateDimensionOutputTypeDef

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BETWEEN', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# DateDimensionTypeDef

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BETWEEN', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DateDimensionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteCalculatedAttributeDefinitionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEventStreamRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventTriggerRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventTriggerResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIntegrationRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProfileKeyRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileKeyResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProfileObjectRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileObjectUniqueKey
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileObjectResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProfileObjectTypeRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileObjectTypeResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProfileRequestTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSegmentDefinitionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSegmentDefinitionResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkflowRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationSummaryTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes

### UnhealthySince
- **Type**: typing.Optional[datetime.datetime]


# DetectProfileObjectTypeRequestTypeDef

### Objects
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DetectProfileObjectTypeResponseTypeDef

### DetectedProfileObjectTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.DetectedProfileObjectTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectedProfileObjectTypeTypeDef

### SourceLastUpdatedTimestampFormat
- **Type**: typing.Optional[str]

### Fields
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeFieldTypeDef]]

### Keys
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeKeyOutputTypeDef]]]


# DimensionOutputTypeDef

### ProfileAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileAttributesOutputTypeDef]

### CalculatedAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles_classes.CalculatedAttributeDimensionOutputTypeDef]]


# DimensionTypeDef

### ProfileAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileAttributesUnionTypeDef]

### CalculatedAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.customer_profiles_classes.CalculatedAttributeDimensionUnionTypeDef]]


# DomainStatsTypeDef

### ProfileCount
- **Type**: typing.Optional[int]

### MeteringProfileCount
- **Type**: typing.Optional[int]

### ObjectCount
- **Type**: typing.Optional[int]

### TotalSize
- **Type**: typing.Optional[int]


# EventStreamDestinationDetailsTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes

### UnhealthySince
- **Type**: typing.Optional[datetime.datetime]

### Message
- **Type**: typing.Optional[str]


# EventStreamSummaryTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventStreamName
- **Type**: <class 'str'>
- **Required**: Yes

### EventStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### StoppedSince
- **Type**: typing.Optional[datetime.datetime]

### DestinationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.DestinationSummaryTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventTriggerConditionOutputTypeDef

### EventTriggerDimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerDimensionOutputTypeDef]
- **Required**: Yes

### LogicalOperator
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes


# EventTriggerConditionTypeDef

### EventTriggerDimensions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerDimensionUnionTypeDef]
- **Required**: Yes

### LogicalOperator
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes


# EventTriggerConditionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventTriggerDimensionOutputTypeDef

### ObjectAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectAttributeOutputTypeDef]
- **Required**: Yes


# EventTriggerDimensionTypeDef

### ObjectAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectAttributeUnionTypeDef]
- **Required**: Yes


# EventTriggerDimensionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventTriggerLimitsOutputTypeDef

### EventExpiration
- **Type**: typing.Optional[int]

### Periods
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.PeriodTypeDef]]


# EventTriggerLimitsTypeDef

### EventExpiration
- **Type**: typing.Optional[int]

### Periods
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.PeriodTypeDef]]


# EventTriggerLimitsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventTriggerSummaryItemTypeDef

### ObjectTypeName
- **Type**: typing.Optional[str]

### EventTriggerName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExportingConfigTypeDef

### S3Exporting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.S3ExportingConfigTypeDef]


# ExportingLocationTypeDef

### S3Exporting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.S3ExportingLocationTypeDef]


# ExtraLengthValueProfileDimensionOutputTypeDef

### DimensionType
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'ENDS_WITH', 'EXCLUSIVE', 'INCLUSIVE']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ExtraLengthValueProfileDimensionTypeDef

### DimensionType
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'ENDS_WITH', 'EXCLUSIVE', 'INCLUSIVE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ExtraLengthValueProfileDimensionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldSourceProfileIdsTypeDef

### AccountNumber
- **Type**: typing.Optional[str]

### AdditionalInformation
- **Type**: typing.Optional[str]

### PartyType
- **Type**: typing.Optional[str]

### BusinessName
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### MiddleName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### BirthDate
- **Type**: typing.Optional[str]

### Gender
- **Type**: typing.Optional[str]

### PhoneNumber
- **Type**: typing.Optional[str]

### MobilePhoneNumber
- **Type**: typing.Optional[str]

### HomePhoneNumber
- **Type**: typing.Optional[str]

### BusinessPhoneNumber
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### PersonalEmailAddress
- **Type**: typing.Optional[str]

### BusinessEmailAddress
- **Type**: typing.Optional[str]

### Address
- **Type**: typing.Optional[str]

### ShippingAddress
- **Type**: typing.Optional[str]

### MailingAddress
- **Type**: typing.Optional[str]

### BillingAddress
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FilterAttributeDimensionOutputTypeDef

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# FilterAttributeDimensionTypeDef

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FilterDimensionOutputTypeDef

### Attributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles_classes.FilterAttributeDimensionOutputTypeDef]
- **Required**: Yes


# FilterDimensionTypeDef

### Attributes
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.customer_profiles_classes.FilterAttributeDimensionTypeDef]
- **Required**: Yes


# FilterGroupOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterGroupTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterOutputTypeDef

### Include
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.FilterGroupOutputTypeDef]
- **Required**: Yes


# FilterTypeDef

### Include
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes

### Groups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.FilterGroupTypeDef]
- **Required**: Yes


# FilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowDefinitionTypeDef

### FlowName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFlowConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.SourceFlowConfigTypeDef'>
- **Required**: Yes

### Tasks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.TaskTypeDef]
- **Required**: Yes

### TriggerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.TriggerConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# FoundByKeyValueTypeDef

### KeyName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# GetAutoMergingPreviewRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Consolidation
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ConsolidationUnionTypeDef'>
- **Required**: Yes

### ConflictResolution
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ConflictResolutionTypeDef'>
- **Required**: Yes

### MinAllowedConfidenceScoreForMerging
- **Type**: typing.Optional[float]


# GetAutoMergingPreviewResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfMatchesInSample
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfProfilesInSample
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfProfilesWillBeMerged
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCalculatedAttributeDefinitionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculatedAttributeDefinitionResponseTypeDef

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['AVERAGE', 'COUNT', 'FIRST_OCCURRENCE', 'LAST_OCCURRENCE', 'MAXIMUM', 'MAX_OCCURRENCE', 'MINIMUM', 'SUM']
- **Required**: Yes

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.FilterOutputTypeDef'>
- **Required**: Yes

### Conditions
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionsTypeDef'>
- **Required**: Yes

### AttributeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeDetailsOutputTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCalculatedAttributeForProfileRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculatedAttributeForProfileResponseTypeDef

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### IsDataPartial
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultEncryptionKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterQueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Stats
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.DomainStatsTypeDef'>
- **Required**: Yes

### Matching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.MatchingResponseTypeDef'>
- **Required**: Yes

### RuleBasedMatching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.RuleBasedMatchingResponseTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventStreamRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventStreamResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### StoppedSince
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DestinationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.EventStreamDestinationDetailsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventTriggerRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventTriggerResponseTypeDef

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerConditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerConditionOutputTypeDef]
- **Required**: Yes

### SegmentFilter
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerLimitsOutputTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityResolutionJobRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityResolutionJobResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'FIND_MATCHING', 'MERGING', 'PARTIAL_SUCCESS', 'PENDING', 'PREPROCESSING']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### JobStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AutoMerging
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.AutoMergingOutputTypeDef'>
- **Required**: Yes

### ExportingLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ExportingLocationTypeDef'>
- **Required**: Yes

### JobStats
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.JobStatsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIntegrationRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ObjectTypeNames
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### IsUnstructured
- **Type**: <class 'bool'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMatchesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetMatchesResponseTypeDef

### MatchGenerationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PotentialMatches
- **Type**: <class 'int'>
- **Required**: Yes

### Matches
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.MatchItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetProfileObjectTypeRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileObjectTypeResponseTypeDef

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### EncryptionKey
- **Type**: <class 'str'>
- **Required**: Yes

### AllowProfileCreation
- **Type**: <class 'bool'>
- **Required**: Yes

### SourceLastUpdatedTimestampFormat
- **Type**: <class 'str'>
- **Required**: Yes

### MaxAvailableProfileObjectCount
- **Type**: <class 'int'>
- **Required**: Yes

### MaxProfileObjectCount
- **Type**: <class 'int'>
- **Required**: Yes

### Fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeFieldTypeDef]
- **Required**: Yes

### Keys
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeKeyOutputTypeDef]]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProfileObjectTypeTemplateRequestTypeDef

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileObjectTypeTemplateResponseTypeDef

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceObject
- **Type**: <class 'str'>
- **Required**: Yes

### AllowProfileCreation
- **Type**: <class 'bool'>
- **Required**: Yes

### SourceLastUpdatedTimestampFormat
- **Type**: <class 'str'>
- **Required**: Yes

### Fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeFieldTypeDef]
- **Required**: Yes

### Keys
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeKeyOutputTypeDef]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentDefinitionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentDefinitionResponseTypeDef

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentGroups
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.SegmentGroupOutputTypeDef'>
- **Required**: Yes

### SegmentDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentEstimateRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EstimateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentEstimateResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EstimateId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### Estimate
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentMembershipRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetSegmentMembershipResponseTypeDef

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileQueryResultTypeDef]
- **Required**: Yes

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileQueryFailuresTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSegmentSnapshotRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentSnapshotResponseTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['CSV', 'JSONL', 'ORC']
- **Required**: Yes

### EncryptionKey
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationUri
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSimilarProfilesRequestPaginateTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MatchType
- **Type**: typing.Literal['ML_BASED_MATCHING', 'RULE_BASED_MATCHING']
- **Required**: Yes

### SearchKey
- **Type**: <class 'str'>
- **Required**: Yes

### SearchValue
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.PaginatorConfigTypeDef]


# GetSimilarProfilesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MatchType
- **Type**: typing.Literal['ML_BASED_MATCHING', 'RULE_BASED_MATCHING']
- **Required**: Yes

### SearchKey
- **Type**: <class 'str'>
- **Required**: Yes

### SearchValue
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetSimilarProfilesResponseTypeDef

### ProfileIds
- **Type**: typing.List[str]
- **Required**: Yes

### MatchId
- **Type**: <class 'str'>
- **Required**: Yes

### MatchType
- **Type**: typing.Literal['ML_BASED_MATCHING', 'RULE_BASED_MATCHING']
- **Required**: Yes

### RuleLevel
- **Type**: <class 'int'>
- **Required**: Yes

### ConfidenceScore
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetWorkflowRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowResponseTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowType
- **Type**: typing.Literal['APPFLOW_INTEGRATION']
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'RETRY', 'SPLIT']
- **Required**: Yes

### ErrorDescription
- **Type**: <class 'str'>
- **Required**: Yes

### StartDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Attributes
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.WorkflowAttributesTypeDef'>
- **Required**: Yes

### Metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.WorkflowMetricsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowStepsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetWorkflowStepsResponseTypeDef

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowType
- **Type**: typing.Literal['APPFLOW_INTEGRATION']
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.WorkflowStepItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GroupOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GroupTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IdentityResolutionJobTypeDef

### DomainName
- **Type**: typing.Optional[str]

### JobId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'FIND_MATCHING', 'MERGING', 'PARTIAL_SUCCESS', 'PENDING', 'PREPROCESSING']]

### JobStartTime
- **Type**: typing.Optional[datetime.datetime]

### JobEndTime
- **Type**: typing.Optional[datetime.datetime]

### JobStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.JobStatsTypeDef]

### ExportingLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ExportingLocationTypeDef]

### Message
- **Type**: typing.Optional[str]


# IncrementalPullConfigTypeDef

### DatetimeTypeFieldName
- **Type**: typing.Optional[str]


# IntegrationConfigTypeDef

### AppflowIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AppflowIntegrationTypeDef]


# JobScheduleTypeDef

### DayOfTheWeek
- **Type**: typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']
- **Required**: Yes

### Time
- **Type**: <class 'str'>
- **Required**: Yes


# JobStatsTypeDef

### NumberOfProfilesReviewed
- **Type**: typing.Optional[int]

### NumberOfMatchesFound
- **Type**: typing.Optional[int]

### NumberOfMergesDone
- **Type**: typing.Optional[int]


# ListAccountIntegrationsRequestTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeHidden
- **Type**: typing.Optional[bool]


# ListAccountIntegrationsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListIntegrationItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCalculatedAttributeDefinitionItemTypeDef

### CalculatedAttributeName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListCalculatedAttributeDefinitionsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCalculatedAttributeDefinitionsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListCalculatedAttributeDefinitionItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCalculatedAttributeForProfileItemTypeDef

### CalculatedAttributeName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### IsDataPartial
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ListCalculatedAttributesForProfileRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCalculatedAttributesForProfileResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListCalculatedAttributeForProfileItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainItemTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListDomainsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDomainsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListDomainItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventStreamsRequestPaginateTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.PaginatorConfigTypeDef]


# ListEventStreamsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventStreamsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.EventStreamSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventTriggersRequestPaginateTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.PaginatorConfigTypeDef]


# ListEventTriggersRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventTriggersResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerSummaryItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityResolutionJobsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIdentityResolutionJobsResponseTypeDef

### IdentityResolutionJobsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.IdentityResolutionJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIntegrationItemTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ObjectTypeName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### ObjectTypeNames
- **Type**: typing.Optional[typing.Dict[str, str]]

### WorkflowId
- **Type**: typing.Optional[str]

### IsUnstructured
- **Type**: typing.Optional[bool]

### RoleArn
- **Type**: typing.Optional[str]

### EventTriggerNames
- **Type**: typing.Optional[typing.List[str]]


# ListIntegrationsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeHidden
- **Type**: typing.Optional[bool]


# ListIntegrationsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListIntegrationItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectTypeAttributeItemTypeDef

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListObjectTypeAttributesRequestPaginateTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.PaginatorConfigTypeDef]


# ListObjectTypeAttributesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListObjectTypeAttributesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListObjectTypeAttributeItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileObjectTypeItemTypeDef

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### MaxProfileObjectCount
- **Type**: typing.Optional[int]

### MaxAvailableProfileObjectCount
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListProfileObjectTypeTemplateItemTypeDef

### TemplateId
- **Type**: typing.Optional[str]

### SourceName
- **Type**: typing.Optional[str]

### SourceObject
- **Type**: typing.Optional[str]


# ListProfileObjectTypeTemplatesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProfileObjectTypeTemplatesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListProfileObjectTypeTemplateItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileObjectTypesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProfileObjectTypesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListProfileObjectTypeItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileObjectsItemTypeDef

### ObjectTypeName
- **Type**: typing.Optional[str]

### ProfileObjectUniqueKey
- **Type**: typing.Optional[str]

### Object
- **Type**: typing.Optional[str]


# ListProfileObjectsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ObjectFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectFilterTypeDef]


# ListProfileObjectsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListProfileObjectsItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRuleBasedMatchesRequestPaginateTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.PaginatorConfigTypeDef]


# ListRuleBasedMatchesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRuleBasedMatchesResponseTypeDef

### MatchIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSegmentDefinitionsRequestPaginateTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.PaginatorConfigTypeDef]


# ListSegmentDefinitionsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSegmentDefinitionsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.SegmentDefinitionItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowsItemTypeDef

### WorkflowType
- **Type**: typing.Literal['APPFLOW_INTEGRATION']
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'RETRY', 'SPLIT']
- **Required**: Yes

### StatusDescription
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListWorkflowsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowType
- **Type**: typing.Optional[typing.Literal['APPFLOW_INTEGRATION']]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'RETRY', 'SPLIT']]

### QueryStartDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.TimestampTypeDef]

### QueryEndDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.TimestampTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkflowsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ListWorkflowsItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MarketoSourcePropertiesTypeDef

### Object
- **Type**: <class 'str'>
- **Required**: Yes


# MatchItemTypeDef

### MatchId
- **Type**: typing.Optional[str]

### ProfileIds
- **Type**: typing.Optional[typing.List[str]]

### ConfidenceScore
- **Type**: typing.Optional[float]


# MatchingRequestTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### JobSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.JobScheduleTypeDef]

### AutoMerging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AutoMergingUnionTypeDef]

### ExportingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ExportingConfigTypeDef]


# MatchingResponseTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### JobSchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.JobScheduleTypeDef]

### AutoMerging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AutoMergingOutputTypeDef]

### ExportingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ExportingConfigTypeDef]


# MatchingRuleOutputTypeDef

### Rule
- **Type**: typing.List[str]
- **Required**: Yes


# MatchingRuleTypeDef

### Rule
- **Type**: typing.Sequence[str]
- **Required**: Yes


# MatchingRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MergeProfilesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MainProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileIdsToBeMerged
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FieldSourceProfileIds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.FieldSourceProfileIdsTypeDef]


# MergeProfilesResponseTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ObjectAttributeOutputTypeDef

### ComparisonOperator
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### FieldName
- **Type**: typing.Optional[str]


# ObjectAttributeTypeDef

### ComparisonOperator
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Source
- **Type**: typing.Optional[str]

### FieldName
- **Type**: typing.Optional[str]


# ObjectAttributeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ObjectFilterTypeDef

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ObjectTypeFieldTypeDef

### Source
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[typing.Literal['EMAIL_ADDRESS', 'NAME', 'NUMBER', 'PHONE_NUMBER', 'STRING']]


# ObjectTypeKeyOutputTypeDef

### StandardIdentifiers
- **Type**: typing.Optional[typing.List[typing.Literal['ASSET', 'CASE', 'COMMUNICATION_RECORD', 'LOOKUP_ONLY', 'NEW_ONLY', 'ORDER', 'PROFILE', 'SECONDARY', 'UNIQUE']]]

### FieldNames
- **Type**: typing.Optional[typing.List[str]]


# ObjectTypeKeyTypeDef

### StandardIdentifiers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ASSET', 'CASE', 'COMMUNICATION_RECORD', 'LOOKUP_ONLY', 'NEW_ONLY', 'ORDER', 'PROFILE', 'SECONDARY', 'UNIQUE']]]

### FieldNames
- **Type**: typing.Optional[typing.Sequence[str]]


# ObjectTypeKeyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PeriodTypeDef

### Unit
- **Type**: typing.Literal['DAYS', 'HOURS', 'MONTHS', 'WEEKS']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes

### MaxInvocationsPerProfile
- **Type**: typing.Optional[int]

### Unlimited
- **Type**: typing.Optional[bool]


# ProfileAttributeValuesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# ProfileAttributeValuesResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeValueItemTypeDef]
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ProfileAttributesOutputTypeDef

### AccountNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### AdditionalInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ExtraLengthValueProfileDimensionOutputTypeDef]

### FirstName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### LastName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### MiddleName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### GenderString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### PartyTypeString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### BirthDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.DateDimensionOutputTypeDef]

### PhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### BusinessName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### BusinessPhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### HomePhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### MobilePhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### EmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### PersonalEmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### BusinessEmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionOutputTypeDef]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressDimensionOutputTypeDef]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressDimensionOutputTypeDef]

### MailingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressDimensionOutputTypeDef]

### BillingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressDimensionOutputTypeDef]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeDimensionOutputTypeDef]]


# ProfileAttributesTypeDef

### AccountNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### AdditionalInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ExtraLengthValueProfileDimensionUnionTypeDef]

### FirstName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### LastName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### MiddleName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### GenderString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### PartyTypeString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### BirthDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.DateDimensionUnionTypeDef]

### PhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### BusinessName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### BusinessPhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### HomePhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### MobilePhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### EmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### PersonalEmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### BusinessEmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileDimensionUnionTypeDef]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressDimensionUnionTypeDef]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressDimensionUnionTypeDef]

### MailingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressDimensionUnionTypeDef]

### BillingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressDimensionUnionTypeDef]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeDimensionUnionTypeDef]]


# ProfileAttributesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProfileDimensionOutputTypeDef

### DimensionType
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'ENDS_WITH', 'EXCLUSIVE', 'INCLUSIVE']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ProfileDimensionTypeDef

### DimensionType
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'ENDS_WITH', 'EXCLUSIVE', 'INCLUSIVE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ProfileDimensionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProfileQueryFailuresTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[int]


# ProfileQueryResultTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryResult
- **Type**: typing.Literal['ABSENT', 'PRESENT']
- **Required**: Yes

### Profile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileTypeDef]


# ProfileTypeDef

### ProfileId
- **Type**: typing.Optional[str]

### AccountNumber
- **Type**: typing.Optional[str]

### AdditionalInformation
- **Type**: typing.Optional[str]

### PartyType
- **Type**: typing.Optional[typing.Literal['BUSINESS', 'INDIVIDUAL', 'OTHER']]

### BusinessName
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### MiddleName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### BirthDate
- **Type**: typing.Optional[str]

### Gender
- **Type**: typing.Optional[typing.Literal['FEMALE', 'MALE', 'UNSPECIFIED']]

### PhoneNumber
- **Type**: typing.Optional[str]

### MobilePhoneNumber
- **Type**: typing.Optional[str]

### HomePhoneNumber
- **Type**: typing.Optional[str]

### BusinessPhoneNumber
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### PersonalEmailAddress
- **Type**: typing.Optional[str]

### BusinessEmailAddress
- **Type**: typing.Optional[str]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressTypeDef]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressTypeDef]

### MailingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressTypeDef]

### BillingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AddressTypeDef]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### FoundByItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.FoundByKeyValueTypeDef]]

### PartyTypeString
- **Type**: typing.Optional[str]

### GenderString
- **Type**: typing.Optional[str]


# PutIntegrationRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: typing.Optional[str]

### ObjectTypeName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### FlowDefinition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.FlowDefinitionTypeDef]

### ObjectTypeNames
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RoleArn
- **Type**: typing.Optional[str]

### EventTriggerNames
- **Type**: typing.Optional[typing.Sequence[str]]


# PutIntegrationResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ObjectTypeNames
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### IsUnstructured
- **Type**: <class 'bool'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutProfileObjectRequestTypeDef

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Object
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# PutProfileObjectResponseTypeDef

### ProfileObjectUniqueKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutProfileObjectTypeRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: typing.Optional[str]

### ExpirationDays
- **Type**: typing.Optional[int]

### EncryptionKey
- **Type**: typing.Optional[str]

### AllowProfileCreation
- **Type**: typing.Optional[bool]

### SourceLastUpdatedTimestampFormat
- **Type**: typing.Optional[str]

### MaxProfileObjectCount
- **Type**: typing.Optional[int]

### Fields
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeFieldTypeDef]]

### Keys
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeKeyUnionTypeDef]]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutProfileObjectTypeResponseTypeDef

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### EncryptionKey
- **Type**: <class 'str'>
- **Required**: Yes

### AllowProfileCreation
- **Type**: <class 'bool'>
- **Required**: Yes

### SourceLastUpdatedTimestampFormat
- **Type**: <class 'str'>
- **Required**: Yes

### MaxProfileObjectCount
- **Type**: <class 'int'>
- **Required**: Yes

### MaxAvailableProfileObjectCount
- **Type**: <class 'int'>
- **Required**: Yes

### Fields
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeFieldTypeDef]
- **Required**: Yes

### Keys
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ObjectTypeKeyOutputTypeDef]]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RangeOverrideTypeDef

### Start
- **Type**: <class 'int'>
- **Required**: Yes

### Unit
- **Type**: typing.Literal['DAYS']
- **Required**: Yes

### End
- **Type**: typing.Optional[int]


# RangeTypeDef

### Value
- **Type**: <class 'int'>
- **Required**: Yes

### Unit
- **Type**: typing.Literal['DAYS']
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


# RuleBasedMatchingRequestTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MatchingRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.MatchingRuleUnionTypeDef]]

### MaxAllowedRuleLevelForMerging
- **Type**: typing.Optional[int]

### MaxAllowedRuleLevelForMatching
- **Type**: typing.Optional[int]

### AttributeTypesSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeTypesSelectorUnionTypeDef]

### ConflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConflictResolutionTypeDef]

### ExportingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ExportingConfigTypeDef]


# RuleBasedMatchingResponseTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### MatchingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.MatchingRuleOutputTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'IN_PROGRESS', 'PENDING']]

### MaxAllowedRuleLevelForMerging
- **Type**: typing.Optional[int]

### MaxAllowedRuleLevelForMatching
- **Type**: typing.Optional[int]

### AttributeTypesSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeTypesSelectorOutputTypeDef]

### ConflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConflictResolutionTypeDef]

### ExportingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ExportingConfigTypeDef]


# S3ExportingConfigTypeDef

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyName
- **Type**: typing.Optional[str]


# S3ExportingLocationTypeDef

### S3BucketName
- **Type**: typing.Optional[str]

### S3KeyName
- **Type**: typing.Optional[str]


# S3SourcePropertiesTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### BucketPrefix
- **Type**: typing.Optional[str]


# SalesforceSourcePropertiesTypeDef

### Object
- **Type**: <class 'str'>
- **Required**: Yes

### EnableDynamicFieldUpdate
- **Type**: typing.Optional[bool]

### IncludeDeletedRecords
- **Type**: typing.Optional[bool]


# ScheduledTriggerPropertiesTypeDef

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DataPullMode
- **Type**: typing.Optional[typing.Literal['Complete', 'Incremental']]

### ScheduleStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.TimestampTypeDef]

### ScheduleEndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.TimestampTypeDef]

### Timezone
- **Type**: typing.Optional[str]

### ScheduleOffset
- **Type**: typing.Optional[int]

### FirstExecutionFrom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.TimestampTypeDef]


# SearchProfilesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AdditionalSearchKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.AdditionalSearchKeyTypeDef]]

### LogicalOperator
- **Type**: typing.Optional[typing.Literal['AND', 'OR']]


# SearchProfilesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.ProfileTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SegmentDefinitionItemTypeDef

### SegmentDefinitionName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SegmentDefinitionArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SegmentGroupOutputTypeDef

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.GroupOutputTypeDef]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupStructureTypeDef

### Groups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.GroupUnionTypeDef]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupTypeDef

### Groups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.GroupTypeDef]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceNowSourcePropertiesTypeDef

### Object
- **Type**: <class 'str'>
- **Required**: Yes


# SourceConnectorPropertiesTypeDef

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.MarketoSourcePropertiesTypeDef]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.S3SourcePropertiesTypeDef]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.SalesforceSourcePropertiesTypeDef]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ServiceNowSourcePropertiesTypeDef]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ZendeskSourcePropertiesTypeDef]


# SourceFlowConfigTypeDef

### ConnectorType
- **Type**: typing.Literal['Marketo', 'S3', 'Salesforce', 'Servicenow', 'Zendesk']
- **Required**: Yes

### SourceConnectorProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.SourceConnectorPropertiesTypeDef'>
- **Required**: Yes

### ConnectorProfileName
- **Type**: typing.Optional[str]

### IncrementalPullConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.IncrementalPullConfigTypeDef]


# SourceSegmentTypeDef

### SegmentDefinitionName
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TaskTypeDef

### SourceFields
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TaskType
- **Type**: typing.Literal['Arithmetic', 'Filter', 'Map', 'Mask', 'Merge', 'Truncate', 'Validate']
- **Required**: Yes

### ConnectorOperator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConnectorOperatorTypeDef]

### DestinationField
- **Type**: typing.Optional[str]

### TaskProperties
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CONCAT_FORMAT', 'DATA_TYPE', 'DESTINATION_DATA_TYPE', 'LOWER_BOUND', 'MASK_LENGTH', 'MASK_VALUE', 'MATH_OPERATION_FIELDS_ORDER', 'SOURCE_DATA_TYPE', 'SUBFIELD_CATEGORY_MAP', 'TRUNCATE_LENGTH', 'UPPER_BOUND', 'VALIDATION_ACTION', 'VALUE', 'VALUES'], str]]


# ThresholdTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUAL_TO', 'GREATER_THAN', 'LESS_THAN', 'NOT_EQUAL_TO']
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TriggerConfigTypeDef

### TriggerType
- **Type**: typing.Literal['Event', 'OnDemand', 'Scheduled']
- **Required**: Yes

### TriggerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.TriggerPropertiesTypeDef]


# TriggerPropertiesTypeDef

### Scheduled
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ScheduledTriggerPropertiesTypeDef]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAddressTypeDef

### Address1
- **Type**: typing.Optional[str]

### Address2
- **Type**: typing.Optional[str]

### Address3
- **Type**: typing.Optional[str]

### Address4
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### County
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### Province
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### PostalCode
- **Type**: typing.Optional[str]


# UpdateCalculatedAttributeDefinitionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Conditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionsTypeDef]


# UpdateCalculatedAttributeDefinitionResponseTypeDef

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['AVERAGE', 'COUNT', 'FIRST_OCCURRENCE', 'LAST_OCCURRENCE', 'MAXIMUM', 'MAX_OCCURRENCE', 'MINIMUM', 'SUM']
- **Required**: Yes

### Conditions
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ConditionsTypeDef'>
- **Required**: Yes

### AttributeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.AttributeDetailsOutputTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultExpirationDays
- **Type**: typing.Optional[int]

### DefaultEncryptionKey
- **Type**: typing.Optional[str]

### DeadLetterQueueUrl
- **Type**: typing.Optional[str]

### Matching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.MatchingRequestTypeDef]

### RuleBasedMatching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.RuleBasedMatchingRequestTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateDomainResponseTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### DefaultEncryptionKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeadLetterQueueUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Matching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.MatchingResponseTypeDef'>
- **Required**: Yes

### RuleBasedMatching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.RuleBasedMatchingResponseTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEventTriggerRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EventTriggerConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerConditionUnionTypeDef]]

### SegmentFilter
- **Type**: typing.Optional[str]

### EventTriggerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerLimitsUnionTypeDef]


# UpdateEventTriggerResponseTypeDef

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerConditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerConditionOutputTypeDef]
- **Required**: Yes

### SegmentFilter
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.EventTriggerLimitsOutputTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProfileRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### AdditionalInformation
- **Type**: typing.Optional[str]

### AccountNumber
- **Type**: typing.Optional[str]

### PartyType
- **Type**: typing.Optional[typing.Literal['BUSINESS', 'INDIVIDUAL', 'OTHER']]

### BusinessName
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### MiddleName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### BirthDate
- **Type**: typing.Optional[str]

### Gender
- **Type**: typing.Optional[typing.Literal['FEMALE', 'MALE', 'UNSPECIFIED']]

### PhoneNumber
- **Type**: typing.Optional[str]

### MobilePhoneNumber
- **Type**: typing.Optional[str]

### HomePhoneNumber
- **Type**: typing.Optional[str]

### BusinessPhoneNumber
- **Type**: typing.Optional[str]

### EmailAddress
- **Type**: typing.Optional[str]

### PersonalEmailAddress
- **Type**: typing.Optional[str]

### BusinessEmailAddress
- **Type**: typing.Optional[str]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.UpdateAddressTypeDef]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.UpdateAddressTypeDef]

### MailingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.UpdateAddressTypeDef]

### BillingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.UpdateAddressTypeDef]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PartyTypeString
- **Type**: typing.Optional[str]

### GenderString
- **Type**: typing.Optional[str]


# UpdateProfileResponseTypeDef

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkflowAttributesTypeDef

### AppflowIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AppflowIntegrationWorkflowAttributesTypeDef]


# WorkflowMetricsTypeDef

### AppflowIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AppflowIntegrationWorkflowMetricsTypeDef]


# WorkflowStepItemTypeDef

### AppflowIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles_classes.AppflowIntegrationWorkflowStepTypeDef]


# ZendeskSourcePropertiesTypeDef

### Object
- **Type**: <class 'str'>
- **Required**: Yes



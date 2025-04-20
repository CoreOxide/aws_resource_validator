# Customer Profiles Customer Profiles Classes

# AddProfileKeyRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# AddProfileKeyResponse

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# AdditionalSearchKey

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# Address

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


# AddressDimension

### City
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### Country
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### County
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### PostalCode
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### Province
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### State
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]


# AddressDimensionOutput

### City
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### Country
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### County
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### PostalCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### Province
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]


# AppflowIntegration

### FlowDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FlowDefinition'>
- **Required**: Yes

### Batches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Batch]]


# AppflowIntegrationWorkflowAttributes

### SourceConnectorType
- **Type**: typing.Literal['Marketo', 'S3', 'Salesforce', 'Servicenow', 'Zendesk']
- **Required**: Yes

### ConnectorProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]


# AppflowIntegrationWorkflowMetrics

### RecordsProcessed
- **Type**: <class 'int'>
- **Required**: Yes

### StepsCompleted
- **Type**: <class 'int'>
- **Required**: Yes

### TotalSteps
- **Type**: <class 'int'>
- **Required**: Yes


# AppflowIntegrationWorkflowStep

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


# AttributeDetails

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeItem]
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeDetailsOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeItem]
- **Required**: Yes

### Expression
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeDimension

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# AttributeDimensionOutput

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# AttributeItem

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AttributeTypesSelector

### AttributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### Address
- **Type**: typing.Optional[typing.List[str]]

### PhoneNumber
- **Type**: typing.Optional[typing.List[str]]

### EmailAddress
- **Type**: typing.Optional[typing.List[str]]


# AttributeTypesSelectorOutput

### AttributeMatchingModel
- **Type**: typing.Literal['MANY_TO_MANY', 'ONE_TO_ONE']
- **Required**: Yes

### Address
- **Type**: typing.Optional[typing.List[str]]

### PhoneNumber
- **Type**: typing.Optional[typing.List[str]]

### EmailAddress
- **Type**: typing.Optional[typing.List[str]]


# AttributeValueItem

### Value
- **Type**: typing.Optional[str]


# AutoMerging

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Consolidation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Consolidation, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ConsolidationOutput, NoneType]

### ConflictResolution
- **Type**: <class 'NoneType'>

### MinAllowedConfidenceScoreForMerging
- **Type**: typing.Optional[float]


# AutoMergingOutput

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Consolidation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ConsolidationOutput]

### ConflictResolution
- **Type**: <class 'NoneType'>

### MinAllowedConfidenceScoreForMerging
- **Type**: typing.Optional[float]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Batch

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# BatchGetCalculatedAttributeForProfileError

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetCalculatedAttributeForProfileRequest

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileIds
- **Type**: typing.List[str]
- **Required**: Yes

### ConditionOverrides
- **Type**: <class 'NoneType'>


# BatchGetCalculatedAttributeForProfileResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.BatchGetCalculatedAttributeForProfileError]
- **Required**: Yes

### CalculatedAttributeValues
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.CalculatedAttributeValue]
- **Required**: Yes

### ConditionOverrides
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ConditionOverrides'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetProfileError

### Code
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# BatchGetProfileRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetProfileResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.BatchGetProfileError]
- **Required**: Yes

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Profile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CalculatedAttributeDimension

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### ConditionOverrides
- **Type**: <class 'NoneType'>


# CalculatedAttributeDimensionOutput

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### ConditionOverrides
- **Type**: <class 'NoneType'>


# CalculatedAttributeValue

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


# ConditionOverrides

### Range
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.RangeOverride]


# Conditions

### Range
- **Type**: <class 'NoneType'>

### ObjectCount
- **Type**: typing.Optional[int]

### Threshold
- **Type**: <class 'NoneType'>


# ConflictResolution

### ConflictResolvingModel
- **Type**: typing.Literal['RECENCY', 'SOURCE']
- **Required**: Yes

### SourceName
- **Type**: typing.Optional[str]


# ConnectorOperator

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


# Consolidation

### MatchingAttributesList
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# ConsolidationOutput

### MatchingAttributesList
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes


# CreateCalculatedAttributeDefinitionRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeDetails
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeDetails, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeDetailsOutput]
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['AVERAGE', 'COUNT', 'FIRST_OCCURRENCE', 'LAST_OCCURRENCE', 'MAXIMUM', 'MAX_OCCURRENCE', 'MINIMUM', 'SUM']
- **Required**: Yes

### DisplayName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Conditions
- **Type**: <class 'NoneType'>

### Filter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Filter, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCalculatedAttributeDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeDetailsOutput'>
- **Required**: Yes

### Conditions
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Conditions'>
- **Required**: Yes

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchingRequest]

### RuleBasedMatching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.RuleBasedMatchingRequest]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDomainResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchingResponse'>
- **Required**: Yes

### RuleBasedMatching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.RuleBasedMatchingResponse'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventStreamRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateEventStreamResponse

### EventStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventTriggerRequest

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
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerCondition, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerConditionOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### SegmentFilter
- **Type**: typing.Optional[str]

### EventTriggerLimits
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerLimits, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerLimitsOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateEventTriggerResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerConditionOutput]
- **Required**: Yes

### SegmentFilter
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerLimitsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIntegrationWorkflowRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowType
- **Type**: typing.Literal['APPFLOW_INTEGRATION']
- **Required**: Yes

### IntegrationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.IntegrationConfig'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateIntegrationWorkflowResponse

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfileRequest

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
- **Type**: <class 'NoneType'>

### ShippingAddress
- **Type**: <class 'NoneType'>

### MailingAddress
- **Type**: <class 'NoneType'>

### BillingAddress
- **Type**: <class 'NoneType'>

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### PartyTypeString
- **Type**: typing.Optional[str]

### GenderString
- **Type**: typing.Optional[str]


# CreateProfileResponse

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSegmentDefinitionRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SegmentGroup, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SegmentGroupOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSegmentDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSegmentEstimateRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SegmentGroupStructure'>
- **Required**: Yes


# CreateSegmentEstimateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSegmentSnapshotRequest

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


# CreateSegmentSnapshotResponse

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DateDimension

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BETWEEN', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# DateDimensionOutput

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BETWEEN', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteCalculatedAttributeDefinitionRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEventStreamRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventTriggerRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventTriggerResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIntegrationRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIntegrationResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProfileKeyRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileKeyResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProfileObjectRequest

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


# DeleteProfileObjectResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProfileObjectTypeRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileObjectTypeResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProfileRequest

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProfileResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSegmentDefinitionRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSegmentDefinitionResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkflowRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationSummary

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes

### UnhealthySince
- **Type**: typing.Optional[datetime.datetime]


# DetectProfileObjectTypeRequest

### Objects
- **Type**: typing.List[str]
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DetectProfileObjectTypeResponse

### DetectedProfileObjectTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.DetectedProfileObjectType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# DetectedProfileObjectType

### SourceLastUpdatedTimestampFormat
- **Type**: typing.Optional[str]

### Fields
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeField]]

### Keys
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeKeyOutput]]]


# Dimension

### ProfileAttributes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileAttributes, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileAttributesOutput, NoneType]

### CalculatedAttributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.CalculatedAttributeDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.CalculatedAttributeDimensionOutput]]]


# DimensionOutput

### ProfileAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileAttributesOutput]

### CalculatedAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.CalculatedAttributeDimensionOutput]]


# DomainStats

### ProfileCount
- **Type**: typing.Optional[int]

### MeteringProfileCount
- **Type**: typing.Optional[int]

### ObjectCount
- **Type**: typing.Optional[int]

### TotalSize
- **Type**: typing.Optional[int]


# EventStreamDestinationDetails

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


# EventStreamSummary

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
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventTriggerCondition

### EventTriggerDimensions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerDimensionOutput]]
- **Required**: Yes

### LogicalOperator
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes


# EventTriggerConditionOutput

### EventTriggerDimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerDimensionOutput]
- **Required**: Yes

### LogicalOperator
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes


# EventTriggerDimension

### ObjectAttributes
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectAttribute, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectAttributeOutput]]
- **Required**: Yes


# EventTriggerDimensionOutput

### ObjectAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectAttributeOutput]
- **Required**: Yes


# EventTriggerLimits

### EventExpiration
- **Type**: typing.Optional[int]

### Periods
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Period]]


# EventTriggerLimitsOutput

### EventExpiration
- **Type**: typing.Optional[int]

### Periods
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Period]]


# EventTriggerSummaryItem

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


# ExportingConfig

### S3Exporting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.S3ExportingConfig]


# ExportingLocation

### S3Exporting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.S3ExportingLocation]


# ExtraLengthValueProfileDimension

### DimensionType
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'ENDS_WITH', 'EXCLUSIVE', 'INCLUSIVE']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ExtraLengthValueProfileDimensionOutput

### DimensionType
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'ENDS_WITH', 'EXCLUSIVE', 'INCLUSIVE']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# FieldSourceProfileIds

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# Filter

### Include
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterGroup]
- **Required**: Yes


# FilterAttributeDimension

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# FilterAttributeDimensionOutput

### DimensionType
- **Type**: typing.Literal['AFTER', 'BEFORE', 'BEGINS_WITH', 'BETWEEN', 'CONTAINS', 'ENDS_WITH', 'EQUAL', 'EXCLUSIVE', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'INCLUSIVE', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_BETWEEN', 'ON']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# FilterDimension

### Attributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterAttributeDimension]
- **Required**: Yes


# FilterDimensionOutput

### Attributes
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterAttributeDimensionOutput]
- **Required**: Yes


# FilterGroup

### Type
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes

### Dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterDimension]
- **Required**: Yes


# FilterGroupOutput

### Type
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes

### Dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterDimensionOutput]
- **Required**: Yes


# FilterOutput

### Include
- **Type**: typing.Literal['ALL', 'ANY', 'NONE']
- **Required**: Yes

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterGroupOutput]
- **Required**: Yes


# FlowDefinition

### FlowName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFlowConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SourceFlowConfig'>
- **Required**: Yes

### Tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Task]
- **Required**: Yes

### TriggerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.TriggerConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# FoundByKeyValue

### KeyName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# GetAutoMergingPreviewRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Consolidation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Consolidation, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ConsolidationOutput]
- **Required**: Yes

### ConflictResolution
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ConflictResolution'>
- **Required**: Yes

### MinAllowedConfidenceScoreForMerging
- **Type**: typing.Optional[float]


# GetAutoMergingPreviewResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetCalculatedAttributeDefinitionRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculatedAttributeDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FilterOutput'>
- **Required**: Yes

### Conditions
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Conditions'>
- **Required**: Yes

### AttributeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeDetailsOutput'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetCalculatedAttributeForProfileRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### CalculatedAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetCalculatedAttributeForProfileResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDomainResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.DomainStats'>
- **Required**: Yes

### Matching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchingResponse'>
- **Required**: Yes

### RuleBasedMatching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.RuleBasedMatchingResponse'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventStreamRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventStreamResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventStreamDestinationDetails'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventTriggerRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventTriggerResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerConditionOutput]
- **Required**: Yes

### SegmentFilter
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerLimitsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityResolutionJobRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityResolutionJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AutoMergingOutput'>
- **Required**: Yes

### ExportingLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ExportingLocation'>
- **Required**: Yes

### JobStats
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.JobStats'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetIntegrationRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: <class 'str'>
- **Required**: Yes


# GetIntegrationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetMatchesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetMatchesResponse

### MatchGenerationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PotentialMatches
- **Type**: <class 'int'>
- **Required**: Yes

### Matches
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetProfileObjectTypeRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileObjectTypeResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeField]
- **Required**: Yes

### Keys
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeKeyOutput]]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileObjectTypeTemplateRequest

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProfileObjectTypeTemplateResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeField]
- **Required**: Yes

### Keys
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeKeyOutput]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentDefinitionRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SegmentGroupOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentEstimateRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EstimateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentEstimateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentMembershipRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileIds
- **Type**: typing.List[str]
- **Required**: Yes


# GetSegmentMembershipResponse

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### Profiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileQueryResult]
- **Required**: Yes

### Failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileQueryFailures]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetSegmentSnapshotRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SegmentDefinitionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSegmentSnapshotResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetSimilarProfilesRequest

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


# GetSimilarProfilesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.PaginatorConfig]


# GetSimilarProfilesResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetWorkflowRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.WorkflowAttributes'>
- **Required**: Yes

### Metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.WorkflowMetrics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowStepsRequest

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


# GetWorkflowStepsResponse

### WorkflowId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowType
- **Type**: typing.Literal['APPFLOW_INTEGRATION']
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.WorkflowStepItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Group

### Dimensions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Dimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.DimensionOutput]]]

### SourceSegments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SourceSegment]]

### SourceType
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# GroupOutput

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.DimensionOutput]]

### SourceSegments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SourceSegment]]

### SourceType
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]

### Type
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# IdentityResolutionJob

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
- **Type**: <class 'NoneType'>

### ExportingLocation
- **Type**: <class 'NoneType'>

### Message
- **Type**: typing.Optional[str]


# IncrementalPullConfig

### DatetimeTypeFieldName
- **Type**: typing.Optional[str]


# IntegrationConfig

### AppflowIntegration
- **Type**: <class 'NoneType'>


# JobSchedule

### DayOfTheWeek
- **Type**: typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']
- **Required**: Yes

### Time
- **Type**: <class 'str'>
- **Required**: Yes


# JobStats

### NumberOfProfilesReviewed
- **Type**: typing.Optional[int]

### NumberOfMatchesFound
- **Type**: typing.Optional[int]

### NumberOfMergesDone
- **Type**: typing.Optional[int]


# ListAccountIntegrationsRequest

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeHidden
- **Type**: typing.Optional[bool]


# ListAccountIntegrationsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListIntegrationItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCalculatedAttributeDefinitionItem

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


# ListCalculatedAttributeDefinitionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCalculatedAttributeDefinitionsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListCalculatedAttributeDefinitionItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCalculatedAttributeForProfileItem

### CalculatedAttributeName
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### IsDataPartial
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ListCalculatedAttributesForProfileRequest

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


# ListCalculatedAttributesForProfileResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListCalculatedAttributeForProfileItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDomainItem

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


# ListDomainsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDomainsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListDomainItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventStreamsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventStreamsRequestPaginate

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.PaginatorConfig]


# ListEventStreamsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventStreamSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventTriggersRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventTriggersRequestPaginate

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.PaginatorConfig]


# ListEventTriggersResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerSummaryItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityResolutionJobsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIdentityResolutionJobsResponse

### IdentityResolutionJobsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.IdentityResolutionJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIntegrationItem

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


# ListIntegrationsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### IncludeHidden
- **Type**: typing.Optional[bool]


# ListIntegrationsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListIntegrationItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListObjectTypeAttributeItem

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ListObjectTypeAttributesRequest

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


# ListObjectTypeAttributesRequestPaginate

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.PaginatorConfig]


# ListObjectTypeAttributesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListObjectTypeAttributeItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileObjectTypeItem

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


# ListProfileObjectTypeTemplateItem

### TemplateId
- **Type**: typing.Optional[str]

### SourceName
- **Type**: typing.Optional[str]

### SourceObject
- **Type**: typing.Optional[str]


# ListProfileObjectTypeTemplatesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProfileObjectTypeTemplatesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListProfileObjectTypeTemplateItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileObjectTypesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProfileObjectTypesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListProfileObjectTypeItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProfileObjectsItem

### ObjectTypeName
- **Type**: typing.Optional[str]

### ProfileObjectUniqueKey
- **Type**: typing.Optional[str]

### Object
- **Type**: typing.Optional[str]


# ListProfileObjectsRequest

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
- **Type**: <class 'NoneType'>


# ListProfileObjectsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListProfileObjectsItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRuleBasedMatchesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRuleBasedMatchesRequestPaginate

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.PaginatorConfig]


# ListRuleBasedMatchesResponse

### MatchIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSegmentDefinitionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSegmentDefinitionsRequestPaginate

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.PaginatorConfig]


# ListSegmentDefinitionsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SegmentDefinitionItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# ListWorkflowsItem

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


# ListWorkflowsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkflowType
- **Type**: typing.Optional[typing.Literal['APPFLOW_INTEGRATION']]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'RETRY', 'SPLIT']]

### QueryStartDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### QueryEndDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWorkflowsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ListWorkflowsItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MarketoSourceProperties

### Object
- **Type**: <class 'str'>
- **Required**: Yes


# MatchItem

### MatchId
- **Type**: typing.Optional[str]

### ProfileIds
- **Type**: typing.Optional[typing.List[str]]

### ConfidenceScore
- **Type**: typing.Optional[float]


# MatchingRequest

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### JobSchedule
- **Type**: <class 'NoneType'>

### AutoMerging
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AutoMerging, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AutoMergingOutput, NoneType]

### ExportingConfig
- **Type**: <class 'NoneType'>


# MatchingResponse

### Enabled
- **Type**: typing.Optional[bool]

### JobSchedule
- **Type**: <class 'NoneType'>

### AutoMerging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AutoMergingOutput]

### ExportingConfig
- **Type**: <class 'NoneType'>


# MatchingRule

### Rule
- **Type**: typing.List[str]
- **Required**: Yes


# MatchingRuleOutput

### Rule
- **Type**: typing.List[str]
- **Required**: Yes


# MergeProfilesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MainProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileIdsToBeMerged
- **Type**: typing.List[str]
- **Required**: Yes

### FieldSourceProfileIds
- **Type**: <class 'NoneType'>


# MergeProfilesResponse

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# ObjectAttribute

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


# ObjectAttributeOutput

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


# ObjectFilter

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ObjectTypeField

### Source
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[typing.Literal['EMAIL_ADDRESS', 'NAME', 'NUMBER', 'PHONE_NUMBER', 'STRING']]


# ObjectTypeKey

### StandardIdentifiers
- **Type**: typing.Optional[typing.List[typing.Literal['ASSET', 'CASE', 'COMMUNICATION_RECORD', 'LOOKUP_ONLY', 'NEW_ONLY', 'ORDER', 'PROFILE', 'SECONDARY', 'UNIQUE']]]

### FieldNames
- **Type**: typing.Optional[typing.List[str]]


# ObjectTypeKeyOutput

### StandardIdentifiers
- **Type**: typing.Optional[typing.List[typing.Literal['ASSET', 'CASE', 'COMMUNICATION_RECORD', 'LOOKUP_ONLY', 'NEW_ONLY', 'ORDER', 'PROFILE', 'SECONDARY', 'UNIQUE']]]

### FieldNames
- **Type**: typing.Optional[typing.List[str]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Period

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


# Profile

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
- **Type**: <class 'NoneType'>

### ShippingAddress
- **Type**: <class 'NoneType'>

### MailingAddress
- **Type**: <class 'NoneType'>

### BillingAddress
- **Type**: <class 'NoneType'>

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### FoundByItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.FoundByKeyValue]]

### PartyTypeString
- **Type**: typing.Optional[str]

### GenderString
- **Type**: typing.Optional[str]


# ProfileAttributeValuesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# ProfileAttributeValuesResponse

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeValueItem]
- **Required**: Yes

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# ProfileAttributes

### AccountNumber
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### AdditionalInformation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ExtraLengthValueProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ExtraLengthValueProfileDimensionOutput, NoneType]

### FirstName
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### LastName
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### MiddleName
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### GenderString
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### PartyTypeString
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### BirthDate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.DateDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.DateDimensionOutput, NoneType]

### PhoneNumber
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### BusinessName
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### BusinessPhoneNumber
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### HomePhoneNumber
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### MobilePhoneNumber
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### EmailAddress
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### PersonalEmailAddress
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### BusinessEmailAddress
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput, NoneType]

### Address
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimensionOutput, NoneType]

### ShippingAddress
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimensionOutput, NoneType]

### MailingAddress
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimensionOutput, NoneType]

### BillingAddress
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimensionOutput, NoneType]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeDimension, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeDimensionOutput]]]


# ProfileAttributesOutput

### AccountNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### AdditionalInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ExtraLengthValueProfileDimensionOutput]

### FirstName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### LastName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### MiddleName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### GenderString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### PartyTypeString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### BirthDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.DateDimensionOutput]

### PhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### BusinessName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### BusinessPhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### HomePhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### MobilePhoneNumber
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### EmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### PersonalEmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### BusinessEmailAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ProfileDimensionOutput]

### Address
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimensionOutput]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimensionOutput]

### MailingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimensionOutput]

### BillingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AddressDimensionOutput]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeDimensionOutput]]


# ProfileDimension

### DimensionType
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'ENDS_WITH', 'EXCLUSIVE', 'INCLUSIVE']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ProfileDimensionOutput

### DimensionType
- **Type**: typing.Literal['BEGINS_WITH', 'CONTAINS', 'ENDS_WITH', 'EXCLUSIVE', 'INCLUSIVE']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ProfileQueryFailures

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[int]


# ProfileQueryResult

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryResult
- **Type**: typing.Literal['ABSENT', 'PRESENT']
- **Required**: Yes

### Profile
- **Type**: <class 'NoneType'>


# PutIntegrationRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Uri
- **Type**: typing.Optional[str]

### ObjectTypeName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### FlowDefinition
- **Type**: <class 'NoneType'>

### ObjectTypeNames
- **Type**: typing.Optional[typing.Dict[str, str]]

### RoleArn
- **Type**: typing.Optional[str]

### EventTriggerNames
- **Type**: typing.Optional[typing.List[str]]


# PutIntegrationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# PutProfileObjectRequest

### ObjectTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### Object
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# PutProfileObjectResponse

### ProfileObjectUniqueKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# PutProfileObjectTypeRequest

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeField]]

### Keys
- **Type**: typing.Optional[typing.Dict[str, typing.List[typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeKey, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeKeyOutput]]]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutProfileObjectTypeResponse

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeField]
- **Required**: Yes

### Keys
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ObjectTypeKeyOutput]]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# Range

### Value
- **Type**: <class 'int'>
- **Required**: Yes

### Unit
- **Type**: typing.Literal['DAYS']
- **Required**: Yes


# RangeOverride

### Start
- **Type**: <class 'int'>
- **Required**: Yes

### Unit
- **Type**: typing.Literal['DAYS']
- **Required**: Yes

### End
- **Type**: typing.Optional[int]


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


# RuleBasedMatchingRequest

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MatchingRules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchingRule, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchingRuleOutput]]]

### MaxAllowedRuleLevelForMerging
- **Type**: typing.Optional[int]

### MaxAllowedRuleLevelForMatching
- **Type**: typing.Optional[int]

### AttributeTypesSelector
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeTypesSelector, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeTypesSelectorOutput, NoneType]

### ConflictResolution
- **Type**: <class 'NoneType'>

### ExportingConfig
- **Type**: <class 'NoneType'>


# RuleBasedMatchingResponse

### Enabled
- **Type**: typing.Optional[bool]

### MatchingRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchingRuleOutput]]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'IN_PROGRESS', 'PENDING']]

### MaxAllowedRuleLevelForMerging
- **Type**: typing.Optional[int]

### MaxAllowedRuleLevelForMatching
- **Type**: typing.Optional[int]

### AttributeTypesSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeTypesSelectorOutput]

### ConflictResolution
- **Type**: <class 'NoneType'>

### ExportingConfig
- **Type**: <class 'NoneType'>


# S3ExportingConfig

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyName
- **Type**: typing.Optional[str]


# S3ExportingLocation

### S3BucketName
- **Type**: typing.Optional[str]

### S3KeyName
- **Type**: typing.Optional[str]


# S3SourceProperties

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### BucketPrefix
- **Type**: typing.Optional[str]


# SalesforceSourceProperties

### Object
- **Type**: <class 'str'>
- **Required**: Yes

### EnableDynamicFieldUpdate
- **Type**: typing.Optional[bool]

### IncludeDeletedRecords
- **Type**: typing.Optional[bool]


# ScheduledTriggerProperties

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DataPullMode
- **Type**: typing.Optional[typing.Literal['Complete', 'Incremental']]

### ScheduleStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ScheduleEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Timezone
- **Type**: typing.Optional[str]

### ScheduleOffset
- **Type**: typing.Optional[int]

### FirstExecutionFrom
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# SearchProfilesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### KeyName
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### AdditionalSearchKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AdditionalSearchKey]]

### LogicalOperator
- **Type**: typing.Optional[typing.Literal['AND', 'OR']]


# SearchProfilesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Profile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SegmentDefinitionItem

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


# SegmentGroup

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Group]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupOutput

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.GroupOutput]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# SegmentGroupStructure

### Groups
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Group, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.GroupOutput]]]

### Include
- **Type**: typing.Optional[typing.Literal['ALL', 'ANY', 'NONE']]


# ServiceNowSourceProperties

### Object
- **Type**: <class 'str'>
- **Required**: Yes


# SourceConnectorProperties

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MarketoSourceProperties]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.S3SourceProperties]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SalesforceSourceProperties]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ServiceNowSourceProperties]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ZendeskSourceProperties]


# SourceFlowConfig

### ConnectorType
- **Type**: typing.Literal['Marketo', 'S3', 'Salesforce', 'Servicenow', 'Zendesk']
- **Required**: Yes

### SourceConnectorProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.SourceConnectorProperties'>
- **Required**: Yes

### ConnectorProfileName
- **Type**: typing.Optional[str]

### IncrementalPullConfig
- **Type**: <class 'NoneType'>


# SourceSegment

### SegmentDefinitionName
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Task

### SourceFields
- **Type**: typing.List[str]
- **Required**: Yes

### TaskType
- **Type**: typing.Literal['Arithmetic', 'Filter', 'Map', 'Mask', 'Merge', 'Truncate', 'Validate']
- **Required**: Yes

### ConnectorOperator
- **Type**: <class 'NoneType'>

### DestinationField
- **Type**: typing.Optional[str]

### TaskProperties
- **Type**: typing.Optional[typing.Dict[typing.Literal['CONCAT_FORMAT', 'DATA_TYPE', 'DESTINATION_DATA_TYPE', 'LOWER_BOUND', 'MASK_LENGTH', 'MASK_VALUE', 'MATH_OPERATION_FIELDS_ORDER', 'SOURCE_DATA_TYPE', 'SUBFIELD_CATEGORY_MAP', 'TRUNCATE_LENGTH', 'UPPER_BOUND', 'VALIDATION_ACTION', 'VALUE', 'VALUES'], str]]


# Threshold

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUAL_TO', 'GREATER_THAN', 'LESS_THAN', 'NOT_EQUAL_TO']
- **Required**: Yes


# TriggerConfig

### TriggerType
- **Type**: typing.Literal['Event', 'OnDemand', 'Scheduled']
- **Required**: Yes

### TriggerProperties
- **Type**: <class 'NoneType'>


# TriggerProperties

### Scheduled
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ScheduledTriggerProperties]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAddress

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


# UpdateCalculatedAttributeDefinitionRequest

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
- **Type**: <class 'NoneType'>


# UpdateCalculatedAttributeDefinitionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.Conditions'>
- **Required**: Yes

### AttributeDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AttributeDetailsOutput'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchingRequest]

### RuleBasedMatching
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.RuleBasedMatchingRequest]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateDomainResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.MatchingResponse'>
- **Required**: Yes

### RuleBasedMatching
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.RuleBasedMatchingResponse'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEventTriggerRequest

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerCondition, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerConditionOutput]]]

### SegmentFilter
- **Type**: typing.Optional[str]

### EventTriggerLimits
- **Type**: typing.Union[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerLimits, aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerLimitsOutput, NoneType]


# UpdateEventTriggerResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerConditionOutput]
- **Required**: Yes

### SegmentFilter
- **Type**: <class 'str'>
- **Required**: Yes

### EventTriggerLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.EventTriggerLimitsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProfileRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.UpdateAddress]

### ShippingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.UpdateAddress]

### MailingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.UpdateAddress]

### BillingAddress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.UpdateAddress]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### PartyTypeString
- **Type**: typing.Optional[str]

### GenderString
- **Type**: typing.Optional[str]


# UpdateProfileResponse

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.ResponseMetadata'>
- **Required**: Yes


# WorkflowAttributes

### AppflowIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AppflowIntegrationWorkflowAttributes]


# WorkflowMetrics

### AppflowIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AppflowIntegrationWorkflowMetrics]


# WorkflowStepItem

### AppflowIntegration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.customer_profiles.customer_profiles_classes.AppflowIntegrationWorkflowStep]


# ZendeskSourceProperties

### Object
- **Type**: <class 'str'>
- **Required**: Yes



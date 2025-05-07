# Mailmanager Classes

# AddHeaderAction

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### HeaderValue
- **Type**: <class 'str'>
- **Required**: Yes


# AddonInstance

### AddonInstanceArn
- **Type**: typing.Optional[str]

### AddonInstanceId
- **Type**: typing.Optional[str]

### AddonName
- **Type**: typing.Optional[str]

### AddonSubscriptionId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AddonSubscription

### AddonName
- **Type**: typing.Optional[str]

### AddonSubscriptionArn
- **Type**: typing.Optional[str]

### AddonSubscriptionId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AddressFilter

### AddressPrefix
- **Type**: typing.Optional[str]


# AddressList

### AddressListArn
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# Analysis

### Analyzer
- **Type**: <class 'str'>
- **Required**: Yes

### ResultField
- **Type**: <class 'str'>
- **Required**: Yes


# Archive

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveName
- **Type**: typing.Optional[str]

### ArchiveState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PENDING_DELETION']]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ArchiveAction

### TargetArchive
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]


# ArchiveBooleanExpression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveBooleanToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# ArchiveBooleanToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['HAS_ATTACHMENTS']]


# ArchiveFilterCondition

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveBooleanExpression]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveStringExpression]


# ArchiveFilterConditionOutput

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveBooleanExpression]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveStringExpressionOutput]


# ArchiveFilters

### Include
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFilterCondition]]

### Unless
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFilterCondition]]


# ArchiveFiltersOutput

### Include
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFilterConditionOutput]]

### Unless
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFilterConditionOutput]]


# ArchiveRetention

### RetentionPeriod
- **Type**: typing.Optional[typing.Literal['EIGHTEEN_MONTHS', 'EIGHT_YEARS', 'FIVE_YEARS', 'FOUR_YEARS', 'NINE_MONTHS', 'NINE_YEARS', 'ONE_YEAR', 'PERMANENT', 'SEVEN_YEARS', 'SIX_MONTHS', 'SIX_YEARS', 'TEN_YEARS', 'THIRTY_MONTHS', 'THREE_MONTHS', 'THREE_YEARS', 'TWO_YEARS']]


# ArchiveStringExpression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveStringToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ArchiveStringExpressionOutput

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveStringToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ArchiveStringToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['CC', 'ENVELOPE_FROM', 'ENVELOPE_TO', 'FROM', 'SUBJECT', 'TO']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAddonInstanceRequest

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]]


# CreateAddonInstanceResponse

### AddonInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAddonSubscriptionRequest

### AddonName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]]


# CreateAddonSubscriptionResponse

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAddressListImportJobRequest

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportDataFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ImportDataFormat'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateAddressListImportJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### PreSignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAddressListRequest

### AddressListName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]]


# CreateAddressListResponse

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateArchiveRequest

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### Retention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveRetention]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]]


# CreateArchiveResponse

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIngressPointRequest

### IngressPointName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AUTH', 'OPEN']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### IngressPointConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]]


# CreateIngressPointResponse

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRelayRequest

### Authentication
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RelayAuthentication, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RelayAuthenticationOutput]
- **Required**: Yes

### RelayName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerPort
- **Type**: <class 'int'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]]


# CreateRelayResponse

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleSetRequest

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Rule, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleOutput]]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]]


# CreateRuleSetResponse

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrafficPolicyRequest

### DefaultAction
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### PolicyStatements
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PolicyStatement, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PolicyStatementOutput]]
- **Required**: Yes

### TrafficPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### MaxMessageSizeBytes
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]]


# CreateTrafficPolicyResponse

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAddonInstanceRequest

### AddonInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAddonSubscriptionRequest

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAddressListRequest

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteArchiveRequest

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngressPointRequest

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRelayRequest

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleSetRequest

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyRequest

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverToMailboxAction

### MailboxArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]


# DeliverToQBusinessAction

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]


# DeregisterMemberFromAddressListRequest

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# Envelope

### From
- **Type**: typing.Optional[str]

### Helo
- **Type**: typing.Optional[str]

### To
- **Type**: typing.Optional[typing.List[str]]


# ExportDestinationConfiguration

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.S3ExportDestinationConfiguration]


# ExportStatus

### CompletionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PREPROCESSING', 'PROCESSING', 'QUEUED']]

### SubmissionTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ExportSummary

### ExportId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ExportStatus]


# GetAddonInstanceRequest

### AddonInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAddonInstanceResponse

### AddonInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AddonName
- **Type**: <class 'str'>
- **Required**: Yes

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetAddonSubscriptionRequest

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAddonSubscriptionResponse

### AddonName
- **Type**: <class 'str'>
- **Required**: Yes

### AddonSubscriptionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetAddressListImportJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAddressListImportJobResponse

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### CompletedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### FailedItemsCount
- **Type**: <class 'int'>
- **Required**: Yes

### ImportDataFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ImportDataFormat'>
- **Required**: Yes

### ImportedItemsCount
- **Type**: <class 'int'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PreSignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### StartTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'CREATED', 'FAILED', 'PROCESSING', 'STOPPED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetAddressListRequest

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAddressListResponse

### AddressListArn
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetArchiveExportRequest

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveExportResponse

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportDestinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ExportDestinationConfiguration'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFiltersOutput'>
- **Required**: Yes

### FromTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ExportStatus'>
- **Required**: Yes

### ToTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetArchiveMessageContentRequest

### ArchivedMessageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveMessageContentResponse

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.MessageBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetArchiveMessageRequest

### ArchivedMessageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveMessageResponse

### Envelope
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Envelope'>
- **Required**: Yes

### MessageDownloadLink
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Metadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetArchiveRequest

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveResponse

### ArchiveArn
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveState
- **Type**: typing.Literal['ACTIVE', 'PENDING_DELETION']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Retention
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveRetention'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetArchiveSearchRequest

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveSearchResponse

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFiltersOutput'>
- **Required**: Yes

### FromTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.SearchStatus'>
- **Required**: Yes

### ToTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetArchiveSearchResultsRequest

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveSearchResultsResponse

### Rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Row]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetIngressPointRequest

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngressPointResponse

### ARecord
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IngressPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### IngressPointAuthConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressPointAuthConfiguration'>
- **Required**: Yes

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes

### IngressPointName
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CLOSED', 'DEPROVISIONING', 'FAILED', 'PROVISIONING', 'UPDATING']
- **Required**: Yes

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AUTH', 'OPEN']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetMemberOfAddressListRequest

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberOfAddressListResponse

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetRelayRequest

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRelayResponse

### Authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RelayAuthenticationOutput'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RelayArn
- **Type**: <class 'str'>
- **Required**: Yes

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes

### RelayName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerPort
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetRuleSetRequest

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleSetResponse

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModificationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RuleSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrafficPolicyRequest

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrafficPolicyResponse

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultAction
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MaxMessageSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### PolicyStatements
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PolicyStatementOutput]
- **Required**: Yes

### TrafficPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ImportDataFormat

### ImportDataType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# ImportJob

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportDataFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ImportDataFormat'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PreSignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'CREATED', 'FAILED', 'PROCESSING', 'STOPPED']
- **Required**: Yes

### CompletedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Error
- **Type**: typing.Optional[str]

### FailedItemsCount
- **Type**: typing.Optional[int]

### ImportedItemsCount
- **Type**: typing.Optional[int]

### StartTimestamp
- **Type**: typing.Optional[datetime.datetime]


# IngressAnalysis

### Analyzer
- **Type**: <class 'str'>
- **Required**: Yes

### ResultField
- **Type**: <class 'str'>
- **Required**: Yes


# IngressBooleanExpression

### Evaluate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressBooleanToEvaluate, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressBooleanToEvaluateOutput]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# IngressBooleanExpressionOutput

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressBooleanToEvaluateOutput'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# IngressBooleanToEvaluate

### Analysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressAnalysis]

### IsInAddressList
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressIsInAddressList, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressIsInAddressListOutput, NoneType]


# IngressBooleanToEvaluateOutput

### Analysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressAnalysis]

### IsInAddressList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressIsInAddressListOutput]


# IngressIpToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['SENDER_IP']]


# IngressIpv4Expression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressIpToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CIDR_MATCHES', 'NOT_CIDR_MATCHES']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# IngressIpv4ExpressionOutput

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressIpToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CIDR_MATCHES', 'NOT_CIDR_MATCHES']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# IngressIsInAddressList

### AddressLists
- **Type**: typing.List[str]
- **Required**: Yes

### Attribute
- **Type**: typing.Literal['RECIPIENT']
- **Required**: Yes


# IngressIsInAddressListOutput

### AddressLists
- **Type**: typing.List[str]
- **Required**: Yes

### Attribute
- **Type**: typing.Literal['RECIPIENT']
- **Required**: Yes


# IngressPoint

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes

### IngressPointName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CLOSED', 'DEPROVISIONING', 'FAILED', 'PROVISIONING', 'UPDATING']
- **Required**: Yes

### Type
- **Type**: typing.Literal['AUTH', 'OPEN']
- **Required**: Yes

### ARecord
- **Type**: typing.Optional[str]


# IngressPointAuthConfiguration

### IngressPointPasswordConfiguration
- **Type**: <class 'NoneType'>

### SecretArn
- **Type**: typing.Optional[str]


# IngressPointConfiguration

### SecretArn
- **Type**: typing.Optional[str]

### SmtpPassword
- **Type**: typing.Optional[str]


# IngressPointPasswordConfiguration

### PreviousSmtpPasswordExpiryTimestamp
- **Type**: typing.Optional[datetime.datetime]

### PreviousSmtpPasswordVersion
- **Type**: typing.Optional[str]

### SmtpPasswordVersion
- **Type**: typing.Optional[str]


# IngressStringExpression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressStringToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_EQUALS', 'STARTS_WITH']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# IngressStringExpressionOutput

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressStringToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_EQUALS', 'STARTS_WITH']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# IngressStringToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['RECIPIENT']]


# IngressTlsProtocolExpression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressTlsProtocolToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS', 'MINIMUM_TLS_VERSION']
- **Required**: Yes

### Value
- **Type**: typing.Literal['TLS1_2', 'TLS1_3']
- **Required**: Yes


# IngressTlsProtocolToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['TLS_PROTOCOL']]


# ListAddonInstancesRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListAddonInstancesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListAddonInstancesResponse

### AddonInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.AddonInstance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAddonSubscriptionsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListAddonSubscriptionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListAddonSubscriptionsResponse

### AddonSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.AddonSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAddressListImportJobsRequest

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListAddressListImportJobsRequestPaginate

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListAddressListImportJobsResponse

### ImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ImportJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAddressListsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListAddressListsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListAddressListsResponse

### AddressLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.AddressList]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArchiveExportsRequest

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListArchiveExportsRequestPaginate

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListArchiveExportsResponse

### Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ExportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArchiveSearchesRequest

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListArchiveSearchesRequestPaginate

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListArchiveSearchesResponse

### Searches
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.SearchSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArchivesRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListArchivesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListArchivesResponse

### Archives
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Archive]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIngressPointsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListIngressPointsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListIngressPointsResponse

### IngressPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressPoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersOfAddressListRequest

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.AddressFilter]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListMembersOfAddressListRequestPaginate

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.AddressFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListMembersOfAddressListResponse

### Addresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.SavedAddress]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRelaysRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListRelaysRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListRelaysResponse

### Relays
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Relay]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRuleSetsRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListRuleSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListRuleSetsResponse

### RuleSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleSet]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrafficPoliciesRequest

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListTrafficPoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PaginatorConfig]


# ListTrafficPoliciesResponse

### TrafficPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.TrafficPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MessageBody

### Html
- **Type**: typing.Optional[str]

### MessageMalformed
- **Type**: typing.Optional[bool]

### Text
- **Type**: typing.Optional[str]


# Metadata

### ConfigurationSet
- **Type**: typing.Optional[str]

### IngressPointId
- **Type**: typing.Optional[str]

### RuleSetId
- **Type**: typing.Optional[str]

### SenderHostname
- **Type**: typing.Optional[str]

### SenderIpAddress
- **Type**: typing.Optional[str]

### SendingMethod
- **Type**: typing.Optional[str]

### SendingPool
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### SourceIdentity
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### TlsCipherSuite
- **Type**: typing.Optional[str]

### TlsProtocol
- **Type**: typing.Optional[str]

### TrafficPolicyId
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolicyCondition

### BooleanExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressBooleanExpression, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressBooleanExpressionOutput, NoneType]

### IpExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressIpv4Expression, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressIpv4ExpressionOutput, NoneType]

### StringExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressStringExpression, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressStringExpressionOutput, NoneType]

### TlsExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressTlsProtocolExpression]


# PolicyConditionOutput

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressBooleanExpressionOutput]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressIpv4ExpressionOutput]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressStringExpressionOutput]

### TlsExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.IngressTlsProtocolExpression]


# PolicyStatement

### Action
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Conditions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PolicyCondition, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PolicyConditionOutput]]
- **Required**: Yes


# PolicyStatementOutput

### Action
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PolicyConditionOutput]
- **Required**: Yes


# RegisterMemberToAddressListRequest

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# Relay

### LastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### RelayId
- **Type**: typing.Optional[str]

### RelayName
- **Type**: typing.Optional[str]


# RelayAction

### Relay
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]

### MailFrom
- **Type**: typing.Optional[typing.Literal['PRESERVE', 'REPLACE']]


# RelayAuthentication

### NoAuthentication
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SecretArn
- **Type**: typing.Optional[str]


# RelayAuthenticationOutput

### NoAuthentication
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SecretArn
- **Type**: typing.Optional[str]


# ReplaceRecipientAction

### ReplaceWith
- **Type**: typing.Optional[typing.List[str]]


# ReplaceRecipientActionOutput

### ReplaceWith
- **Type**: typing.Optional[typing.List[str]]


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


# Row

### ArchivedMessageId
- **Type**: typing.Optional[str]

### Cc
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[str]

### Envelope
- **Type**: <class 'NoneType'>

### From
- **Type**: typing.Optional[str]

### HasAttachments
- **Type**: typing.Optional[bool]

### InReplyTo
- **Type**: typing.Optional[str]

### IngressPointId
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]

### ReceivedHeaders
- **Type**: typing.Optional[typing.List[str]]

### ReceivedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SenderHostname
- **Type**: typing.Optional[str]

### SenderIpAddress
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]

### To
- **Type**: typing.Optional[str]

### XMailer
- **Type**: typing.Optional[str]

### XOriginalMailer
- **Type**: typing.Optional[str]

### XPriority
- **Type**: typing.Optional[str]


# Rule

### Actions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleAction, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleActionOutput]]
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleCondition, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleConditionOutput]]]

### Name
- **Type**: typing.Optional[str]

### Unless
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleCondition, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleConditionOutput]]]


# RuleAction

### AddHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.AddHeaderAction]

### Archive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveAction]

### DeliverToMailbox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.DeliverToMailboxAction]

### DeliverToQBusiness
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.DeliverToQBusinessAction]

### Drop
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Relay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RelayAction]

### ReplaceRecipient
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ReplaceRecipientAction, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ReplaceRecipientActionOutput, NoneType]

### Send
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.SendAction]

### WriteToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.S3Action]


# RuleActionOutput

### AddHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.AddHeaderAction]

### Archive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveAction]

### DeliverToMailbox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.DeliverToMailboxAction]

### DeliverToQBusiness
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.DeliverToQBusinessAction]

### Drop
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Relay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RelayAction]

### ReplaceRecipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ReplaceRecipientActionOutput]

### Send
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.SendAction]

### WriteToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.S3Action]


# RuleBooleanExpression

### Evaluate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleBooleanToEvaluate, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleBooleanToEvaluateOutput]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# RuleBooleanExpressionOutput

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleBooleanToEvaluateOutput'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# RuleBooleanToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['READ_RECEIPT_REQUESTED', 'TLS', 'TLS_WRAPPED']]

### IsInAddressList
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleIsInAddressList, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleIsInAddressListOutput, NoneType]


# RuleBooleanToEvaluateOutput

### Attribute
- **Type**: typing.Optional[typing.Literal['READ_RECEIPT_REQUESTED', 'TLS', 'TLS_WRAPPED']]

### IsInAddressList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleIsInAddressListOutput]


# RuleCondition

### BooleanExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleBooleanExpression, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleBooleanExpressionOutput, NoneType]

### DmarcExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleDmarcExpression, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleDmarcExpressionOutput, NoneType]

### IpExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleIpExpression, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleIpExpressionOutput, NoneType]

### NumberExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleNumberExpression]

### StringExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleStringExpression, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleStringExpressionOutput, NoneType]

### VerdictExpression
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleVerdictExpression, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleVerdictExpressionOutput, NoneType]


# RuleConditionOutput

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleBooleanExpressionOutput]

### DmarcExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleDmarcExpressionOutput]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleIpExpressionOutput]

### NumberExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleNumberExpression]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleStringExpressionOutput]

### VerdictExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleVerdictExpressionOutput]


# RuleDmarcExpression

### Operator
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['NONE', 'QUARANTINE', 'REJECT']]
- **Required**: Yes


# RuleDmarcExpressionOutput

### Operator
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['NONE', 'QUARANTINE', 'REJECT']]
- **Required**: Yes


# RuleIpExpression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleIpToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CIDR_MATCHES', 'NOT_CIDR_MATCHES']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RuleIpExpressionOutput

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleIpToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CIDR_MATCHES', 'NOT_CIDR_MATCHES']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RuleIpToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['SOURCE_IP']]


# RuleIsInAddressList

### AddressLists
- **Type**: typing.List[str]
- **Required**: Yes

### Attribute
- **Type**: typing.Literal['CC', 'FROM', 'MAIL_FROM', 'RECIPIENT', 'SENDER', 'TO']
- **Required**: Yes


# RuleIsInAddressListOutput

### AddressLists
- **Type**: typing.List[str]
- **Required**: Yes

### Attribute
- **Type**: typing.Literal['CC', 'FROM', 'MAIL_FROM', 'RECIPIENT', 'SENDER', 'TO']
- **Required**: Yes


# RuleNumberExpression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleNumberToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_EQUALS']
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# RuleNumberToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['MESSAGE_SIZE']]


# RuleOutput

### Actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleActionOutput]
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleConditionOutput]]

### Name
- **Type**: typing.Optional[str]

### Unless
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleConditionOutput]]


# RuleSet

### LastModificationDate
- **Type**: typing.Optional[datetime.datetime]

### RuleSetId
- **Type**: typing.Optional[str]

### RuleSetName
- **Type**: typing.Optional[str]


# RuleStringExpression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleStringToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_EQUALS', 'STARTS_WITH']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RuleStringExpressionOutput

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleStringToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_EQUALS', 'STARTS_WITH']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RuleStringToEvaluate

### Attribute
- **Type**: typing.Optional[typing.Literal['CC', 'FROM', 'HELO', 'MAIL_FROM', 'RECIPIENT', 'SENDER', 'SUBJECT', 'TO']]

### MimeHeaderAttribute
- **Type**: typing.Optional[str]


# RuleVerdictExpression

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleVerdictToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['FAIL', 'GRAY', 'PASS', 'PROCESSING_FAILED']]
- **Required**: Yes


# RuleVerdictExpressionOutput

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleVerdictToEvaluate'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['FAIL', 'GRAY', 'PASS', 'PROCESSING_FAILED']]
- **Required**: Yes


# RuleVerdictToEvaluate

### Analysis
- **Type**: <class 'NoneType'>

### Attribute
- **Type**: typing.Optional[typing.Literal['DKIM', 'SPF']]


# S3Action

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]

### S3Prefix
- **Type**: typing.Optional[str]

### S3SseKmsKeyId
- **Type**: typing.Optional[str]


# S3ExportDestinationConfiguration

### S3Location
- **Type**: typing.Optional[str]


# SavedAddress

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# SearchStatus

### CompletionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'QUEUED', 'RUNNING']]

### SubmissionTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SearchSummary

### SearchId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.SearchStatus]


# SendAction

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]


# StartAddressListImportJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StartArchiveExportRequest

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportDestinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ExportDestinationConfiguration'>
- **Required**: Yes

### FromTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Filters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFilters, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFiltersOutput, NoneType]

### IncludeMetadata
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]


# StartArchiveExportResponse

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# StartArchiveSearchRequest

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### FromTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ToTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Filters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFilters, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveFiltersOutput, NoneType]


# StartArchiveSearchResponse

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ResponseMetadata'>
- **Required**: Yes


# StopAddressListImportJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopArchiveExportRequest

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes


# StopArchiveSearchRequest

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Tag]
- **Required**: Yes


# TrafficPolicy

### DefaultAction
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateArchiveRequest

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveName
- **Type**: typing.Optional[str]

### Retention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.ArchiveRetention]


# UpdateIngressPointRequest

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes

### IngressPointConfiguration
- **Type**: <class 'NoneType'>

### IngressPointName
- **Type**: typing.Optional[str]

### RuleSetId
- **Type**: typing.Optional[str]

### StatusToUpdate
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CLOSED']]

### TrafficPolicyId
- **Type**: typing.Optional[str]


# UpdateRelayRequest

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes

### Authentication
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RelayAuthentication, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RelayAuthenticationOutput, NoneType]

### RelayName
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### ServerPort
- **Type**: typing.Optional[int]


# UpdateRuleSetRequest

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetName
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.Rule, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.RuleOutput]]]


# UpdateTrafficPolicyRequest

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### MaxMessageSizeBytes
- **Type**: typing.Optional[int]

### PolicyStatements
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PolicyStatement, aws_resource_validator.pydantic_models.mailmanager.mailmanager_classes.PolicyStatementOutput]]]

### TrafficPolicyName
- **Type**: typing.Optional[str]



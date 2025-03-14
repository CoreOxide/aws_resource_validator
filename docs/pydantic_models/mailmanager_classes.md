# Mailmanager Classes

# AddHeaderActionTypeDef

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### HeaderValue
- **Type**: <class 'str'>
- **Required**: Yes


# AddonInstanceTypeDef

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


# AddonSubscriptionTypeDef

### AddonName
- **Type**: typing.Optional[str]

### AddonSubscriptionArn
- **Type**: typing.Optional[str]

### AddonSubscriptionId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AddressFilterTypeDef

### AddressPrefix
- **Type**: typing.Optional[str]


# AddressListTypeDef

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


# AnalysisTypeDef

### Analyzer
- **Type**: <class 'str'>
- **Required**: Yes

### ResultField
- **Type**: <class 'str'>
- **Required**: Yes


# ArchiveActionTypeDef

### TargetArchive
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]


# ArchiveBooleanExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveBooleanToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# ArchiveBooleanToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['HAS_ATTACHMENTS']]


# ArchiveFilterConditionOutputTypeDef

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveBooleanExpressionTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveStringExpressionOutputTypeDef]


# ArchiveFilterConditionTypeDef

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveBooleanExpressionTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveStringExpressionTypeDef]


# ArchiveFiltersOutputTypeDef

### Include
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFilterConditionOutputTypeDef]]

### Unless
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFilterConditionOutputTypeDef]]


# ArchiveFiltersTypeDef

### Include
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFilterConditionTypeDef]]

### Unless
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFilterConditionTypeDef]]


# ArchiveFiltersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ArchiveRetentionTypeDef

### RetentionPeriod
- **Type**: typing.Optional[typing.Literal['EIGHTEEN_MONTHS', 'EIGHT_YEARS', 'FIVE_YEARS', 'FOUR_YEARS', 'NINE_MONTHS', 'NINE_YEARS', 'ONE_YEAR', 'PERMANENT', 'SEVEN_YEARS', 'SIX_MONTHS', 'SIX_YEARS', 'TEN_YEARS', 'THIRTY_MONTHS', 'THREE_MONTHS', 'THREE_YEARS', 'TWO_YEARS']]


# ArchiveStringExpressionOutputTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveStringToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# ArchiveStringExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveStringToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ArchiveStringToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['CC', 'ENVELOPE_FROM', 'ENVELOPE_TO', 'FROM', 'SUBJECT', 'TO']]


# ArchiveTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveName
- **Type**: typing.Optional[str]

### ArchiveState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PENDING_DELETION']]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAddonInstanceRequestTypeDef

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]]


# CreateAddonInstanceResponseTypeDef

### AddonInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAddonSubscriptionRequestTypeDef

### AddonName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]]


# CreateAddonSubscriptionResponseTypeDef

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAddressListImportJobRequestTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### ImportDataFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ImportDataFormatTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateAddressListImportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### PreSignedUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAddressListRequestTypeDef

### AddressListName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]]


# CreateAddressListResponseTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateArchiveRequestTypeDef

### ArchiveName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]

### Retention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveRetentionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]]


# CreateArchiveResponseTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIngressPointResponseTypeDef

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRelayRequestTypeDef

### Authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RelayAuthenticationUnionTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]]


# CreateRelayResponseTypeDef

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleSetRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.RuleUnionTypeDef]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]]


# CreateRuleSetResponseTypeDef

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrafficPolicyRequestTypeDef

### DefaultAction
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### PolicyStatements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.PolicyStatementUnionTypeDef]
- **Required**: Yes

### TrafficPolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### MaxMessageSizeBytes
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]]


# CreateTrafficPolicyResponseTypeDef

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAddonInstanceRequestTypeDef

### AddonInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAddonSubscriptionRequestTypeDef

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAddressListRequestTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteArchiveRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngressPointRequestTypeDef

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRelayRequestTypeDef

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleSetRequestTypeDef

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyRequestTypeDef

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeliverToMailboxActionTypeDef

### MailboxArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]


# DeliverToQBusinessActionTypeDef

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


# DeregisterMemberFromAddressListRequestTypeDef

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# EnvelopeTypeDef

### From
- **Type**: typing.Optional[str]

### Helo
- **Type**: typing.Optional[str]

### To
- **Type**: typing.Optional[typing.List[str]]


# ExportDestinationConfigurationTypeDef

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.S3ExportDestinationConfigurationTypeDef]


# ExportStatusTypeDef

### CompletionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'PREPROCESSING', 'PROCESSING', 'QUEUED']]

### SubmissionTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ExportSummaryTypeDef

### ExportId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ExportStatusTypeDef]


# GetAddonInstanceRequestTypeDef

### AddonInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAddonInstanceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAddonSubscriptionRequestTypeDef

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAddonSubscriptionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAddressListImportJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAddressListImportJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ImportDataFormatTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAddressListRequestTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAddressListResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchiveExportRequestTypeDef

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveExportResponseTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportDestinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ExportDestinationConfigurationTypeDef'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFiltersOutputTypeDef'>
- **Required**: Yes

### FromTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ExportStatusTypeDef'>
- **Required**: Yes

### ToTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchiveMessageContentRequestTypeDef

### ArchivedMessageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveMessageContentResponseTypeDef

### Body
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.MessageBodyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchiveMessageRequestTypeDef

### ArchivedMessageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveMessageResponseTypeDef

### Envelope
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.EnvelopeTypeDef'>
- **Required**: Yes

### MessageDownloadLink
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.MetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchiveRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveRetentionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchiveSearchRequestTypeDef

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveSearchResponseTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFiltersOutputTypeDef'>
- **Required**: Yes

### FromTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.SearchStatusTypeDef'>
- **Required**: Yes

### ToTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchiveSearchResultsRequestTypeDef

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveSearchResultsResponseTypeDef

### Rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.RowTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIngressPointRequestTypeDef

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberOfAddressListRequestTypeDef

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberOfAddressListResponseTypeDef

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelayRequestTypeDef

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRelayResponseTypeDef

### Authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RelayAuthenticationOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRuleSetRequestTypeDef

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleSetResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.RuleOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrafficPolicyRequestTypeDef

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrafficPolicyResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.PolicyStatementOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportDataFormatTypeDef

### ImportDataType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# ImportJobTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ImportDataFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ImportDataFormatTypeDef'>
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


# IngressAnalysisTypeDef

### Analyzer
- **Type**: <class 'str'>
- **Required**: Yes

### ResultField
- **Type**: <class 'str'>
- **Required**: Yes


# IngressBooleanExpressionOutputTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressBooleanToEvaluateOutputTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# IngressBooleanExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressBooleanToEvaluateUnionTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# IngressBooleanExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngressBooleanToEvaluateOutputTypeDef

### Analysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressAnalysisTypeDef]

### IsInAddressList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressIsInAddressListOutputTypeDef]


# IngressBooleanToEvaluateTypeDef

### Analysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressAnalysisTypeDef]

### IsInAddressList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressIsInAddressListUnionTypeDef]


# IngressBooleanToEvaluateUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngressIpToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['SENDER_IP']]


# IngressIpv4ExpressionOutputTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressIpToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CIDR_MATCHES', 'NOT_CIDR_MATCHES']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# IngressIpv4ExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressIpToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CIDR_MATCHES', 'NOT_CIDR_MATCHES']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# IngressIpv4ExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngressIsInAddressListOutputTypeDef

### AddressLists
- **Type**: typing.List[str]
- **Required**: Yes

### Attribute
- **Type**: typing.Literal['RECIPIENT']
- **Required**: Yes


# IngressIsInAddressListTypeDef

### AddressLists
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Attribute
- **Type**: typing.Literal['RECIPIENT']
- **Required**: Yes


# IngressIsInAddressListUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngressPointAuthConfigurationTypeDef

### IngressPointPasswordConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressPointPasswordConfigurationTypeDef]

### SecretArn
- **Type**: typing.Optional[str]


# IngressPointConfigurationTypeDef

### SecretArn
- **Type**: typing.Optional[str]

### SmtpPassword
- **Type**: typing.Optional[str]


# IngressPointPasswordConfigurationTypeDef

### PreviousSmtpPasswordExpiryTimestamp
- **Type**: typing.Optional[datetime.datetime]

### PreviousSmtpPasswordVersion
- **Type**: typing.Optional[str]

### SmtpPasswordVersion
- **Type**: typing.Optional[str]


# IngressPointTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngressStringExpressionOutputTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressStringToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_EQUALS', 'STARTS_WITH']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# IngressStringExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressStringToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_EQUALS', 'STARTS_WITH']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# IngressStringExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngressStringToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['RECIPIENT']]


# IngressTlsProtocolExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressTlsProtocolToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS', 'MINIMUM_TLS_VERSION']
- **Required**: Yes

### Value
- **Type**: typing.Literal['TLS1_2', 'TLS1_3']
- **Required**: Yes


# IngressTlsProtocolToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['TLS_PROTOCOL']]


# ListAddonInstancesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListAddonInstancesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListAddonInstancesResponseTypeDef

### AddonInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.AddonInstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAddonSubscriptionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListAddonSubscriptionsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListAddonSubscriptionsResponseTypeDef

### AddonSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.AddonSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAddressListImportJobsRequestPaginateTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListAddressListImportJobsRequestTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListAddressListImportJobsResponseTypeDef

### ImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.ImportJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAddressListsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListAddressListsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListAddressListsResponseTypeDef

### AddressLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.AddressListTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArchiveExportsRequestPaginateTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListArchiveExportsRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListArchiveExportsResponseTypeDef

### Exports
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.ExportSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArchiveSearchesRequestPaginateTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListArchiveSearchesRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListArchiveSearchesResponseTypeDef

### Searches
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.SearchSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListArchivesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListArchivesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListArchivesResponseTypeDef

### Archives
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIngressPointsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListIngressPointsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListIngressPointsResponseTypeDef

### IngressPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.IngressPointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMembersOfAddressListRequestPaginateTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.AddressFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListMembersOfAddressListRequestTypeDef

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.AddressFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListMembersOfAddressListResponseTypeDef

### Addresses
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.SavedAddressTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRelaysRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListRelaysRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListRelaysResponseTypeDef

### Relays
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.RelayTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRuleSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListRuleSetsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListRuleSetsResponseTypeDef

### RuleSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.RuleSetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrafficPoliciesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListTrafficPoliciesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# ListTrafficPoliciesResponseTypeDef

### TrafficPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.TrafficPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MessageBodyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetadataTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolicyConditionOutputTypeDef

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressBooleanExpressionOutputTypeDef]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressIpv4ExpressionOutputTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressStringExpressionOutputTypeDef]

### TlsExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressTlsProtocolExpressionTypeDef]


# PolicyConditionTypeDef

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressBooleanExpressionUnionTypeDef]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressIpv4ExpressionUnionTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressStringExpressionUnionTypeDef]

### TlsExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressTlsProtocolExpressionTypeDef]


# PolicyConditionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PolicyStatementOutputTypeDef

### Action
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.PolicyConditionOutputTypeDef]
- **Required**: Yes


# PolicyStatementTypeDef

### Action
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.PolicyConditionUnionTypeDef]
- **Required**: Yes


# PolicyStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegisterMemberToAddressListRequestTypeDef

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### AddressListId
- **Type**: <class 'str'>
- **Required**: Yes


# RelayActionTypeDef

### Relay
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]

### MailFrom
- **Type**: typing.Optional[typing.Literal['PRESERVE', 'REPLACE']]


# RelayAuthenticationOutputTypeDef

### NoAuthentication
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SecretArn
- **Type**: typing.Optional[str]


# RelayAuthenticationTypeDef

### NoAuthentication
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### SecretArn
- **Type**: typing.Optional[str]


# RelayAuthenticationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RelayTypeDef

### LastModifiedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### RelayId
- **Type**: typing.Optional[str]

### RelayName
- **Type**: typing.Optional[str]


# ReplaceRecipientActionOutputTypeDef

### ReplaceWith
- **Type**: typing.Optional[typing.List[str]]


# ReplaceRecipientActionTypeDef

### ReplaceWith
- **Type**: typing.Optional[typing.Sequence[str]]


# ReplaceRecipientActionUnionTypeDef

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


# RowTypeDef

### ArchivedMessageId
- **Type**: typing.Optional[str]

### Cc
- **Type**: typing.Optional[str]

### Date
- **Type**: typing.Optional[str]

### Envelope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.EnvelopeTypeDef]

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


# RuleActionOutputTypeDef

### AddHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.AddHeaderActionTypeDef]

### Archive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveActionTypeDef]

### DeliverToMailbox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.DeliverToMailboxActionTypeDef]

### DeliverToQBusiness
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.DeliverToQBusinessActionTypeDef]

### Drop
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Relay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RelayActionTypeDef]

### ReplaceRecipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ReplaceRecipientActionOutputTypeDef]

### Send
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.SendActionTypeDef]

### WriteToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.S3ActionTypeDef]


# RuleActionTypeDef

### AddHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.AddHeaderActionTypeDef]

### Archive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveActionTypeDef]

### DeliverToMailbox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.DeliverToMailboxActionTypeDef]

### DeliverToQBusiness
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.DeliverToQBusinessActionTypeDef]

### Drop
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Relay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RelayActionTypeDef]

### ReplaceRecipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ReplaceRecipientActionUnionTypeDef]

### Send
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.SendActionTypeDef]

### WriteToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.S3ActionTypeDef]


# RuleActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleBooleanExpressionOutputTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleBooleanToEvaluateOutputTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# RuleBooleanExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleBooleanToEvaluateUnionTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# RuleBooleanExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleBooleanToEvaluateOutputTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['READ_RECEIPT_REQUESTED', 'TLS', 'TLS_WRAPPED']]

### IsInAddressList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleIsInAddressListOutputTypeDef]


# RuleBooleanToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['READ_RECEIPT_REQUESTED', 'TLS', 'TLS_WRAPPED']]

### IsInAddressList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleIsInAddressListUnionTypeDef]


# RuleBooleanToEvaluateUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleConditionOutputTypeDef

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleBooleanExpressionOutputTypeDef]

### DmarcExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleDmarcExpressionOutputTypeDef]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleIpExpressionOutputTypeDef]

### NumberExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleNumberExpressionTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleStringExpressionOutputTypeDef]

### VerdictExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleVerdictExpressionOutputTypeDef]


# RuleConditionTypeDef

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleBooleanExpressionUnionTypeDef]

### DmarcExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleDmarcExpressionUnionTypeDef]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleIpExpressionUnionTypeDef]

### NumberExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleNumberExpressionTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleStringExpressionUnionTypeDef]

### VerdictExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleVerdictExpressionUnionTypeDef]


# RuleConditionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleDmarcExpressionOutputTypeDef

### Operator
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['NONE', 'QUARANTINE', 'REJECT']]
- **Required**: Yes


# RuleDmarcExpressionTypeDef

### Operator
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[typing.Literal['NONE', 'QUARANTINE', 'REJECT']]
- **Required**: Yes


# RuleDmarcExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleIpExpressionOutputTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleIpToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CIDR_MATCHES', 'NOT_CIDR_MATCHES']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RuleIpExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleIpToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CIDR_MATCHES', 'NOT_CIDR_MATCHES']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RuleIpExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleIpToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['SOURCE_IP']]


# RuleIsInAddressListOutputTypeDef

### AddressLists
- **Type**: typing.List[str]
- **Required**: Yes

### Attribute
- **Type**: typing.Literal['CC', 'FROM', 'MAIL_FROM', 'RECIPIENT', 'SENDER', 'TO']
- **Required**: Yes


# RuleIsInAddressListTypeDef

### AddressLists
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Attribute
- **Type**: typing.Literal['CC', 'FROM', 'MAIL_FROM', 'RECIPIENT', 'SENDER', 'TO']
- **Required**: Yes


# RuleIsInAddressListUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleNumberExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleNumberToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'NOT_EQUALS']
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# RuleNumberToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['MESSAGE_SIZE']]


# RuleOutputTypeDef

### Actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.RuleActionOutputTypeDef]
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.RuleConditionOutputTypeDef]]

### Name
- **Type**: typing.Optional[str]

### Unless
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mailmanager_classes.RuleConditionOutputTypeDef]]


# RuleSetTypeDef

### LastModificationDate
- **Type**: typing.Optional[datetime.datetime]

### RuleSetId
- **Type**: typing.Optional[str]

### RuleSetName
- **Type**: typing.Optional[str]


# RuleStringExpressionOutputTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleStringToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_EQUALS', 'STARTS_WITH']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# RuleStringExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleStringToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'ENDS_WITH', 'EQUALS', 'NOT_EQUALS', 'STARTS_WITH']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RuleStringExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleStringToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['CC', 'FROM', 'HELO', 'MAIL_FROM', 'RECIPIENT', 'SENDER', 'SUBJECT', 'TO']]

### MimeHeaderAttribute
- **Type**: typing.Optional[str]


# RuleTypeDef

### Actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.RuleActionUnionTypeDef]
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.RuleConditionUnionTypeDef]]

### Name
- **Type**: typing.Optional[str]

### Unless
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.RuleConditionUnionTypeDef]]


# RuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleVerdictExpressionOutputTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleVerdictToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Values
- **Type**: typing.List[typing.Literal['FAIL', 'GRAY', 'PASS', 'PROCESSING_FAILED']]
- **Required**: Yes


# RuleVerdictExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleVerdictToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS', 'NOT_EQUALS']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[typing.Literal['FAIL', 'GRAY', 'PASS', 'PROCESSING_FAILED']]
- **Required**: Yes


# RuleVerdictExpressionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleVerdictToEvaluateTypeDef

### Analysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.AnalysisTypeDef]

### Attribute
- **Type**: typing.Optional[typing.Literal['DKIM', 'SPF']]


# S3ActionTypeDef

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


# S3ExportDestinationConfigurationTypeDef

### S3Location
- **Type**: typing.Optional[str]


# SavedAddressTypeDef

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# SearchStatusTypeDef

### CompletionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ErrorMessage
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'QUEUED', 'RUNNING']]

### SubmissionTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SearchSummaryTypeDef

### SearchId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.SearchStatusTypeDef]


# SendActionTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionFailurePolicy
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'DROP']]


# StartAddressListImportJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StartArchiveExportRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportDestinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ExportDestinationConfigurationTypeDef'>
- **Required**: Yes

### FromTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.TimestampTypeDef'>
- **Required**: Yes

### ToTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.TimestampTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFiltersUnionTypeDef]

### IncludeMetadata
- **Type**: typing.Optional[bool]

### MaxResults
- **Type**: typing.Optional[int]


# StartArchiveExportResponseTypeDef

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartArchiveSearchRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### FromTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.TimestampTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### ToTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.TimestampTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFiltersUnionTypeDef]


# StartArchiveSearchResponseTypeDef

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopAddressListImportJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopArchiveExportRequestTypeDef

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes


# StopArchiveSearchRequestTypeDef

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrafficPolicyTypeDef

### DefaultAction
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateArchiveRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveName
- **Type**: typing.Optional[str]

### Retention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveRetentionTypeDef]


# UpdateIngressPointRequestTypeDef

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes

### IngressPointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressPointConfigurationTypeDef]

### IngressPointName
- **Type**: typing.Optional[str]

### RuleSetId
- **Type**: typing.Optional[str]

### StatusToUpdate
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CLOSED']]

### TrafficPolicyId
- **Type**: typing.Optional[str]


# UpdateRelayRequestTypeDef

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes

### Authentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RelayAuthenticationUnionTypeDef]

### RelayName
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### ServerPort
- **Type**: typing.Optional[int]


# UpdateRuleSetRequestTypeDef

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetName
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.RuleUnionTypeDef]]


# UpdateTrafficPolicyRequestTypeDef

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### MaxMessageSizeBytes
- **Type**: typing.Optional[int]

### PolicyStatements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.PolicyStatementUnionTypeDef]]

### TrafficPolicyName
- **Type**: typing.Optional[str]



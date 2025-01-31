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
- **Type**: typing.Optional[typing.Literal['CC', 'FROM', 'SUBJECT', 'TO']]


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

# CreateAddonInstanceRequestRequestTypeDef

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


# CreateAddonSubscriptionRequestRequestTypeDef

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


# CreateArchiveRequestRequestTypeDef

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


# CreateIngressPointRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressPointConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.TagTypeDef]]


# CreateIngressPointResponseTypeDef

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRelayRequestRequestTypeDef

### Authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RelayAuthenticationTypeDef'>
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


# CreateRuleSetRequestRequestTypeDef

### RuleSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.mailmanager_classes.RuleTypeDef, aws_resource_validator.pydantic_models.mailmanager_classes.RuleOutputTypeDef]]
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


# CreateTrafficPolicyRequestRequestTypeDef

### DefaultAction
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### PolicyStatements
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.mailmanager_classes.PolicyStatementTypeDef, aws_resource_validator.pydantic_models.mailmanager_classes.PolicyStatementOutputTypeDef]]
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


# DeleteAddonInstanceRequestRequestTypeDef

### AddonInstanceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAddonSubscriptionRequestRequestTypeDef

### AddonSubscriptionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteArchiveRequestRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngressPointRequestRequestTypeDef

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRelayRequestRequestTypeDef

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleSetRequestRequestTypeDef

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyRequestRequestTypeDef

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


# GetAddonInstanceRequestRequestTypeDef

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


# GetAddonSubscriptionRequestRequestTypeDef

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


# GetArchiveExportRequestRequestTypeDef

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


# GetArchiveMessageContentRequestRequestTypeDef

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


# GetArchiveMessageRequestRequestTypeDef

### ArchivedMessageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetArchiveMessageResponseTypeDef

### MessageDownloadLink
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetArchiveRequestRequestTypeDef

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


# GetArchiveSearchRequestRequestTypeDef

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


# GetArchiveSearchResultsRequestRequestTypeDef

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


# GetIngressPointRequestRequestTypeDef

### IngressPointId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngressPointResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressPointAuthConfigurationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRelayRequestRequestTypeDef

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


# GetRuleSetRequestRequestTypeDef

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


# GetTrafficPolicyRequestRequestTypeDef

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


# IngressAnalysisTypeDef

### Analyzer
- **Type**: <class 'str'>
- **Required**: Yes

### ResultField
- **Type**: <class 'str'>
- **Required**: Yes


# IngressBooleanExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.IngressBooleanToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# IngressBooleanToEvaluateTypeDef

### Analysis
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressAnalysisTypeDef]


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


# ListAddonInstancesRequestListAddonInstancesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListAddonInstancesRequestRequestTypeDef

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


# ListAddonSubscriptionsRequestListAddonSubscriptionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListAddonSubscriptionsRequestRequestTypeDef

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


# ListArchiveExportsRequestListArchiveExportsPaginateTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListArchiveExportsRequestRequestTypeDef

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


# ListArchiveSearchesRequestListArchiveSearchesPaginateTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListArchiveSearchesRequestRequestTypeDef

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


# ListArchivesRequestListArchivesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListArchivesRequestRequestTypeDef

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


# ListIngressPointsRequestListIngressPointsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListIngressPointsRequestRequestTypeDef

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


# ListRelaysRequestListRelaysPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListRelaysRequestRequestTypeDef

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


# ListRuleSetsRequestListRuleSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListRuleSetsRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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


# ListTrafficPoliciesRequestListTrafficPoliciesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.PaginatorConfigTypeDef]


# ListTrafficPoliciesRequestRequestTypeDef

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

### Html
- **Type**: typing.Optional[str]

### MessageMalformed
- **Type**: typing.Optional[bool]

### Text
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressBooleanExpressionTypeDef]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressIpv4ExpressionOutputTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressStringExpressionOutputTypeDef]

### TlsExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressTlsProtocolExpressionTypeDef]


# PolicyConditionTypeDef

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressBooleanExpressionTypeDef]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressIpv4ExpressionTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressStringExpressionTypeDef]

### TlsExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.IngressTlsProtocolExpressionTypeDef]


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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.PolicyConditionTypeDef]
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

### From
- **Type**: typing.Optional[str]

### HasAttachments
- **Type**: typing.Optional[bool]

### InReplyTo
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]

### ReceivedHeaders
- **Type**: typing.Optional[typing.List[str]]

### ReceivedTimestamp
- **Type**: typing.Optional[datetime.datetime]

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

### Drop
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Relay
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RelayActionTypeDef]

### ReplaceRecipient
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ReplaceRecipientActionTypeDef]

### Send
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.SendActionTypeDef]

### WriteToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.S3ActionTypeDef]


# RuleBooleanExpressionTypeDef

### Evaluate
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.RuleBooleanToEvaluateTypeDef'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['IS_FALSE', 'IS_TRUE']
- **Required**: Yes


# RuleBooleanToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['READ_RECEIPT_REQUESTED', 'TLS', 'TLS_WRAPPED']]


# RuleConditionOutputTypeDef

### BooleanExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleBooleanExpressionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleBooleanExpressionTypeDef]

### DmarcExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleDmarcExpressionTypeDef]

### IpExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleIpExpressionTypeDef]

### NumberExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleNumberExpressionTypeDef]

### StringExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleStringExpressionTypeDef]

### VerdictExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RuleVerdictExpressionTypeDef]


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


# RuleIpToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['SOURCE_IP']]


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


# RuleStringToEvaluateTypeDef

### Attribute
- **Type**: typing.Optional[typing.Literal['CC', 'FROM', 'HELO', 'MAIL_FROM', 'RECIPIENT', 'SENDER', 'SUBJECT', 'TO']]


# RuleTypeDef

### Actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.RuleActionTypeDef]
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.RuleConditionTypeDef]]

### Name
- **Type**: typing.Optional[str]

### Unless
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mailmanager_classes.RuleConditionTypeDef]]


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


# StartArchiveExportRequestRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ExportDestinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ExportDestinationConfigurationTypeDef'>
- **Required**: Yes

### FromTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFiltersTypeDef]

### MaxResults
- **Type**: typing.Optional[int]


# StartArchiveExportResponseTypeDef

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartArchiveSearchRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveFiltersTypeDef]


# StartArchiveSearchResponseTypeDef

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mailmanager_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopArchiveExportRequestRequestTypeDef

### ExportId
- **Type**: <class 'str'>
- **Required**: Yes


# StopArchiveSearchRequestRequestTypeDef

### SearchId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateArchiveRequestRequestTypeDef

### ArchiveId
- **Type**: <class 'str'>
- **Required**: Yes

### ArchiveName
- **Type**: typing.Optional[str]

### Retention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.ArchiveRetentionTypeDef]


# UpdateIngressPointRequestRequestTypeDef

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


# UpdateRelayRequestRequestTypeDef

### RelayId
- **Type**: <class 'str'>
- **Required**: Yes

### Authentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mailmanager_classes.RelayAuthenticationTypeDef]

### RelayName
- **Type**: typing.Optional[str]

### ServerName
- **Type**: typing.Optional[str]

### ServerPort
- **Type**: typing.Optional[int]


# UpdateRuleSetRequestRequestTypeDef

### RuleSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleSetName
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.mailmanager_classes.RuleTypeDef, aws_resource_validator.pydantic_models.mailmanager_classes.RuleOutputTypeDef]]]


# UpdateTrafficPolicyRequestRequestTypeDef

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### MaxMessageSizeBytes
- **Type**: typing.Optional[int]

### PolicyStatements
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.mailmanager_classes.PolicyStatementTypeDef, aws_resource_validator.pydantic_models.mailmanager_classes.PolicyStatementOutputTypeDef]]]

### TrafficPolicyName
- **Type**: typing.Optional[str]



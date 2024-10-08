# Pydantic Models in appflow_classes

# AggregationConfigTypeDef

### aggregationType
- **Type**: typing.Optional[typing.Literal['None', 'SingleFile']]

### targetFileSize
- **Type**: typing.Optional[int]


# AmplitudeConnectorProfileCredentialsTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### secretKey
- **Type**: <class 'str'>
- **Required**: Yes


# AmplitudeSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# ApiKeyCredentialsTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### apiSecretKey
- **Type**: typing.Optional[str]


# AuthParameterTypeDef

### key
- **Type**: typing.Optional[str]

### isRequired
- **Type**: typing.Optional[bool]

### label
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### isSensitiveField
- **Type**: typing.Optional[bool]

### connectorSuppliedValues
- **Type**: typing.Optional[typing.List[str]]


# AuthenticationConfigTypeDef

### isBasicAuthSupported
- **Type**: typing.Optional[bool]

### isApiKeyAuthSupported
- **Type**: typing.Optional[bool]

### isOAuth2Supported
- **Type**: typing.Optional[bool]

### isCustomAuthSupported
- **Type**: typing.Optional[bool]

### oAuth2Defaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.OAuth2DefaultsTypeDef]

### customAuthConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow_classes.CustomAuthConfigTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthCredentialsTypeDef

### username
- **Type**: <class 'str'>
- **Required**: Yes

### password
- **Type**: <class 'str'>
- **Required**: Yes


# CancelFlowExecutionsRequestRequestTypeDef

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### executionIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CancelFlowExecutionsResponseTypeDef

### invalidExecutions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConnectorConfigurationTypeDef

### canUseAsSource
- **Type**: typing.Optional[bool]

### canUseAsDestination
- **Type**: typing.Optional[bool]

### supportedDestinationConnectors
- **Type**: typing.Optional[typing.List[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]]

### supportedSchedulingFrequencies
- **Type**: typing.Optional[typing.List[typing.Literal['BYMINUTE', 'DAILY', 'HOURLY', 'MONTHLY', 'ONCE', 'WEEKLY']]]

### isPrivateLinkEnabled
- **Type**: typing.Optional[bool]

### isPrivateLinkEndpointUrlRequired
- **Type**: typing.Optional[bool]

### supportedTriggerTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Event', 'OnDemand', 'Scheduled']]]

### connectorMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorMetadataTypeDef]

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### connectorLabel
- **Type**: typing.Optional[str]

### connectorDescription
- **Type**: typing.Optional[str]

### connectorOwner
- **Type**: typing.Optional[str]

### connectorName
- **Type**: typing.Optional[str]

### connectorVersion
- **Type**: typing.Optional[str]

### connectorArn
- **Type**: typing.Optional[str]

### connectorModes
- **Type**: typing.Optional[typing.List[str]]

### authenticationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.AuthenticationConfigTypeDef]

### connectorRuntimeSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow_classes.ConnectorRuntimeSettingTypeDef]]

### supportedApiVersions
- **Type**: typing.Optional[typing.List[str]]

### supportedOperators
- **Type**: typing.Optional[typing.List[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]]

### supportedWriteOperations
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]]

### connectorProvisioningType
- **Type**: typing.Optional[typing.Literal['LAMBDA']]

### connectorProvisioningConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorProvisioningConfigTypeDef]

### logoURL
- **Type**: typing.Optional[str]

### registeredAt
- **Type**: typing.Optional[datetime.datetime]

### registeredBy
- **Type**: typing.Optional[str]

### supportedDataTransferTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FILE', 'RECORD']]]

### supportedDataTransferApis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow_classes.DataTransferApiTypeDef]]


# ConnectorDetailTypeDef

### connectorDescription
- **Type**: typing.Optional[str]

### connectorName
- **Type**: typing.Optional[str]

### connectorOwner
- **Type**: typing.Optional[str]

### connectorVersion
- **Type**: typing.Optional[str]

### applicationType
- **Type**: typing.Optional[str]

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### connectorLabel
- **Type**: typing.Optional[str]

### registeredAt
- **Type**: typing.Optional[datetime.datetime]

### registeredBy
- **Type**: typing.Optional[str]

### connectorProvisioningType
- **Type**: typing.Optional[typing.Literal['LAMBDA']]

### connectorModes
- **Type**: typing.Optional[typing.List[str]]

### supportedDataTransferTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FILE', 'RECORD']]]


# ConnectorEntityFieldTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### parentIdentifier
- **Type**: typing.Optional[str]

### label
- **Type**: typing.Optional[str]

### isPrimaryKey
- **Type**: typing.Optional[bool]

### defaultValue
- **Type**: typing.Optional[str]

### isDeprecated
- **Type**: typing.Optional[bool]

### supportedFieldTypeDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SupportedFieldTypeDetailsTypeDef]

### description
- **Type**: typing.Optional[str]

### sourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SourceFieldPropertiesTypeDef]

### destinationProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.DestinationFieldPropertiesTypeDef]

### customProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConnectorEntityTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### label
- **Type**: typing.Optional[str]

### hasNestedEntities
- **Type**: typing.Optional[bool]


# ConnectorMetadataTypeDef

### Amplitude
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Datadog
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Dynatrace
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### GoogleAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.GoogleAnalyticsMetadataTypeDef]

### InforNexus
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Marketo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Redshift
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### S3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SalesforceMetadataTypeDef]

### ServiceNow
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Singular
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SlackMetadataTypeDef]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SnowflakeMetadataTypeDef]

### Trendmicro
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Veeva
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ZendeskMetadataTypeDef]

### EventBridge
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Upsolver
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### CustomerProfiles
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Honeycode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.HoneycodeMetadataTypeDef]

### SAPOData
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Pardot
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ConnectorOAuthRequestTypeDef

### authCode
- **Type**: typing.Optional[str]

### redirectUri
- **Type**: typing.Optional[str]


# ConnectorOperatorTypeDef

### Amplitude
- **Type**: typing.Optional[typing.Literal['BETWEEN']]

### Datadog
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'DIVISION', 'EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Dynatrace
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'DIVISION', 'EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### GoogleAnalytics
- **Type**: typing.Optional[typing.Literal['BETWEEN', 'PROJECTION']]

### InforNexus
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'DIVISION', 'EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Marketo
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'DIVISION', 'GREATER_THAN', 'LESS_THAN', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### S3
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Salesforce
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### ServiceNow
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Singular
- **Type**: typing.Optional[typing.Literal['ADDITION', 'DIVISION', 'EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Slack
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Trendmicro
- **Type**: typing.Optional[typing.Literal['ADDITION', 'DIVISION', 'EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Veeva
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Zendesk
- **Type**: typing.Optional[typing.Literal['ADDITION', 'DIVISION', 'GREATER_THAN', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### SAPOData
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### CustomConnector
- **Type**: typing.Optional[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]

### Pardot
- **Type**: typing.Optional[typing.Literal['ADDITION', 'DIVISION', 'EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]


# ConnectorProfileConfigTypeDef

### connectorProfileProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ConnectorProfilePropertiesTypeDef'>
- **Required**: Yes

### connectorProfileCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorProfileCredentialsTypeDef]


# ConnectorProfileCredentialsTypeDef

### Amplitude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.AmplitudeConnectorProfileCredentialsTypeDef]

### Datadog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.DatadogConnectorProfileCredentialsTypeDef]

### Dynatrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.DynatraceConnectorProfileCredentialsTypeDef]

### GoogleAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.GoogleAnalyticsConnectorProfileCredentialsTypeDef]

### Honeycode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.HoneycodeConnectorProfileCredentialsTypeDef]

### InforNexus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.InforNexusConnectorProfileCredentialsTypeDef]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.MarketoConnectorProfileCredentialsTypeDef]

### Redshift
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.RedshiftConnectorProfileCredentialsTypeDef]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SalesforceConnectorProfileCredentialsTypeDef]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ServiceNowConnectorProfileCredentialsTypeDef]

### Singular
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SingularConnectorProfileCredentialsTypeDef]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SlackConnectorProfileCredentialsTypeDef]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SnowflakeConnectorProfileCredentialsTypeDef]

### Trendmicro
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.TrendmicroConnectorProfileCredentialsTypeDef]

### Veeva
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.VeevaConnectorProfileCredentialsTypeDef]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ZendeskConnectorProfileCredentialsTypeDef]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SAPODataConnectorProfileCredentialsTypeDef]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.CustomConnectorProfileCredentialsTypeDef]

### Pardot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.PardotConnectorProfileCredentialsTypeDef]


# ConnectorProfilePropertiesTypeDef

### Amplitude
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Datadog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.DatadogConnectorProfilePropertiesTypeDef]

### Dynatrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.DynatraceConnectorProfilePropertiesTypeDef]

### GoogleAnalytics
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Honeycode
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### InforNexus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.InforNexusConnectorProfilePropertiesTypeDef]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.MarketoConnectorProfilePropertiesTypeDef]

### Redshift
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.RedshiftConnectorProfilePropertiesTypeDef]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SalesforceConnectorProfilePropertiesTypeDef]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ServiceNowConnectorProfilePropertiesTypeDef]

### Singular
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SlackConnectorProfilePropertiesTypeDef]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SnowflakeConnectorProfilePropertiesTypeDef]

### Trendmicro
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Veeva
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.VeevaConnectorProfilePropertiesTypeDef]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ZendeskConnectorProfilePropertiesTypeDef]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SAPODataConnectorProfilePropertiesTypeDef]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.CustomConnectorProfilePropertiesTypeDef]

### Pardot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.PardotConnectorProfilePropertiesTypeDef]


# ConnectorProfileTypeDef

### connectorProfileArn
- **Type**: typing.Optional[str]

### connectorProfileName
- **Type**: typing.Optional[str]

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### connectorLabel
- **Type**: typing.Optional[str]

### connectionMode
- **Type**: typing.Optional[typing.Literal['Private', 'Public']]

### credentialsArn
- **Type**: typing.Optional[str]

### connectorProfileProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorProfilePropertiesTypeDef]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### privateConnectionProvisioningState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.PrivateConnectionProvisioningStateTypeDef]


# ConnectorProvisioningConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectorRuntimeSettingTypeDef

### key
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[str]

### isRequired
- **Type**: typing.Optional[bool]

### label
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### scope
- **Type**: typing.Optional[str]

### connectorSuppliedValueOptions
- **Type**: typing.Optional[typing.List[str]]


# CreateConnectorProfileRequestRequestTypeDef

### connectorProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### connectionMode
- **Type**: typing.Literal['Private', 'Public']
- **Required**: Yes

### connectorProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ConnectorProfileConfigTypeDef'>
- **Required**: Yes

### kmsArn
- **Type**: typing.Optional[str]

### connectorLabel
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# CreateConnectorProfileResponseTypeDef

### connectorProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFlowRequestRequestTypeDef

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### triggerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.TriggerConfigTypeDef'>
- **Required**: Yes

### sourceFlowConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.SourceFlowConfigTypeDef'>
- **Required**: Yes

### destinationFlowConfigList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appflow_classes.DestinationFlowConfigTypeDef]
- **Required**: Yes

### tasks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appflow_classes.TaskTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### kmsArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### metadataCatalogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.MetadataCatalogConfigTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# CreateFlowResponseTypeDef

### flowArn
- **Type**: <class 'str'>
- **Required**: Yes

### flowStatus
- **Type**: typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomAuthConfigTypeDef

### customAuthenticationType
- **Type**: typing.Optional[str]

### authParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow_classes.AuthParameterTypeDef]]


# CustomAuthCredentialsTypeDef

### customAuthenticationType
- **Type**: <class 'str'>
- **Required**: Yes

### credentialsMap
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CustomConnectorDestinationPropertiesTypeDef

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]

### idFieldNames
- **Type**: typing.Optional[typing.Sequence[str]]

### customProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CustomConnectorProfileCredentialsTypeDef

### authenticationType
- **Type**: typing.Literal['APIKEY', 'BASIC', 'CUSTOM', 'OAUTH2']
- **Required**: Yes

### basic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.BasicAuthCredentialsTypeDef]

### oauth2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.OAuth2CredentialsTypeDef]

### apiKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ApiKeyCredentialsTypeDef]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.CustomAuthCredentialsTypeDef]


# CustomConnectorProfilePropertiesTypeDef

### profileProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### oAuth2Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.OAuth2PropertiesTypeDef]


# CustomConnectorSourcePropertiesTypeDef

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### customProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### dataTransferApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.DataTransferApiTypeDef]


# CustomerProfilesDestinationPropertiesTypeDef

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### objectTypeName
- **Type**: typing.Optional[str]


# DataTransferApiTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ASYNC', 'AUTOMATIC', 'SYNC']]


# DatadogConnectorProfileCredentialsTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### applicationKey
- **Type**: <class 'str'>
- **Required**: Yes


# DatadogConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# DatadogSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectorProfileRequestRequestTypeDef

### connectorProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteFlowRequestRequestTypeDef

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DescribeConnectorEntityRequestRequestTypeDef

### connectorEntityName
- **Type**: <class 'str'>
- **Required**: Yes

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### connectorProfileName
- **Type**: typing.Optional[str]

### apiVersion
- **Type**: typing.Optional[str]


# DescribeConnectorEntityResponseTypeDef

### connectorEntityFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.ConnectorEntityFieldTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectorProfilesRequestRequestTypeDef

### connectorProfileNames
- **Type**: typing.Optional[typing.Sequence[str]]

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### connectorLabel
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeConnectorProfilesResponseTypeDef

### connectorProfileDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.ConnectorProfileTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectorRequestRequestTypeDef

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### connectorLabel
- **Type**: typing.Optional[str]


# DescribeConnectorResponseTypeDef

### connectorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ConnectorConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectorsRequestRequestTypeDef

### connectorTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeConnectorsResponseTypeDef

### connectorConfigurations
- **Type**: typing.Dict[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk'], aws_resource_validator.pydantic_models.appflow_classes.ConnectorConfigurationTypeDef]
- **Required**: Yes

### connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.ConnectorDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFlowExecutionRecordsRequestRequestTypeDef

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeFlowExecutionRecordsResponseTypeDef

### flowExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.ExecutionRecordTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFlowRequestRequestTypeDef

### flowName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowResponseTypeDef

### flowArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsArn
- **Type**: <class 'str'>
- **Required**: Yes

### flowStatus
- **Type**: typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']
- **Required**: Yes

### flowStatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### sourceFlowConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.SourceFlowConfigTypeDef'>
- **Required**: Yes

### destinationFlowConfigList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.DestinationFlowConfigTypeDef]
- **Required**: Yes

### lastRunExecutionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ExecutionDetailsTypeDef'>
- **Required**: Yes

### triggerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.TriggerConfigTypeDef'>
- **Required**: Yes

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.TaskTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### metadataCatalogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.MetadataCatalogConfigTypeDef'>
- **Required**: Yes

### lastRunMetadataCatalogDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.MetadataCatalogDetailTypeDef]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationConnectorPropertiesTypeDef

### Redshift
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.RedshiftDestinationPropertiesTypeDef]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.S3DestinationPropertiesTypeDef]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SalesforceDestinationPropertiesTypeDef]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SnowflakeDestinationPropertiesTypeDef]

### EventBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.EventBridgeDestinationPropertiesTypeDef]

### LookoutMetrics
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Upsolver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.UpsolverDestinationPropertiesTypeDef]

### Honeycode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.HoneycodeDestinationPropertiesTypeDef]

### CustomerProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.CustomerProfilesDestinationPropertiesTypeDef]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ZendeskDestinationPropertiesTypeDef]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.MarketoDestinationPropertiesTypeDef]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.CustomConnectorDestinationPropertiesTypeDef]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SAPODataDestinationPropertiesTypeDef]


# DestinationFieldPropertiesTypeDef

### isCreatable
- **Type**: typing.Optional[bool]

### isNullable
- **Type**: typing.Optional[bool]

### isUpsertable
- **Type**: typing.Optional[bool]

### isUpdatable
- **Type**: typing.Optional[bool]

### isDefaultedOnCreate
- **Type**: typing.Optional[bool]

### supportedWriteOperations
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]]


# DestinationFlowConfigTypeDef

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### destinationConnectorProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.DestinationConnectorPropertiesTypeDef'>
- **Required**: Yes

### apiVersion
- **Type**: typing.Optional[str]

### connectorProfileName
- **Type**: typing.Optional[str]


# DynatraceConnectorProfileCredentialsTypeDef

### apiToken
- **Type**: <class 'str'>
- **Required**: Yes


# DynatraceConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# DynatraceSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorHandlingConfigTypeDef

### failOnFirstDestinationError
- **Type**: typing.Optional[bool]

### bucketPrefix
- **Type**: typing.Optional[str]

### bucketName
- **Type**: typing.Optional[str]


# ErrorInfoTypeDef

### putFailuresCount
- **Type**: typing.Optional[int]

### executionMessage
- **Type**: typing.Optional[str]


# EventBridgeDestinationPropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]


# ExecutionDetailsTypeDef

### mostRecentExecutionMessage
- **Type**: typing.Optional[str]

### mostRecentExecutionTime
- **Type**: typing.Optional[datetime.datetime]

### mostRecentExecutionStatus
- **Type**: typing.Optional[typing.Literal['CancelStarted', 'Canceled', 'Error', 'InProgress', 'Successful']]


# ExecutionRecordTypeDef

### executionId
- **Type**: typing.Optional[str]

### executionStatus
- **Type**: typing.Optional[typing.Literal['CancelStarted', 'Canceled', 'Error', 'InProgress', 'Successful']]

### executionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ExecutionResultTypeDef]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### dataPullStartTime
- **Type**: typing.Optional[datetime.datetime]

### dataPullEndTime
- **Type**: typing.Optional[datetime.datetime]

### metadataCatalogDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow_classes.MetadataCatalogDetailTypeDef]]


# ExecutionResultTypeDef

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorInfoTypeDef]

### bytesProcessed
- **Type**: typing.Optional[int]

### bytesWritten
- **Type**: typing.Optional[int]

### recordsProcessed
- **Type**: typing.Optional[int]

### numParallelProcesses
- **Type**: typing.Optional[int]

### maxPageSize
- **Type**: typing.Optional[int]


# FieldTypeDetailsTypeDef

### fieldType
- **Type**: <class 'str'>
- **Required**: Yes

### filterOperators
- **Type**: typing.List[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]
- **Required**: Yes

### supportedValues
- **Type**: typing.Optional[typing.List[str]]

### valueRegexPattern
- **Type**: typing.Optional[str]

### supportedDateFormat
- **Type**: typing.Optional[str]

### fieldValueRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.RangeTypeDef]

### fieldLengthRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.RangeTypeDef]


# FlowDefinitionTypeDef

### flowArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### flowName
- **Type**: typing.Optional[str]

### flowStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']]

### sourceConnectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### sourceConnectorLabel
- **Type**: typing.Optional[str]

### destinationConnectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### destinationConnectorLabel
- **Type**: typing.Optional[str]

### triggerType
- **Type**: typing.Optional[typing.Literal['Event', 'OnDemand', 'Scheduled']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### createdBy
- **Type**: typing.Optional[str]

### lastUpdatedBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### lastRunExecutionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ExecutionDetailsTypeDef]


# GlueDataCatalogConfigTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### tablePrefix
- **Type**: <class 'str'>
- **Required**: Yes


# GoogleAnalyticsConnectorProfileCredentialsTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]


# GoogleAnalyticsMetadataTypeDef

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]


# GoogleAnalyticsSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# HoneycodeConnectorProfileCredentialsTypeDef

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]


# HoneycodeDestinationPropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]


# HoneycodeMetadataTypeDef

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]


# IncrementalPullConfigTypeDef

### datetimeTypeFieldName
- **Type**: typing.Optional[str]


# InforNexusConnectorProfileCredentialsTypeDef

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### secretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### datakey
- **Type**: <class 'str'>
- **Required**: Yes


# InforNexusConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# InforNexusSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaConnectorProvisioningConfigTypeDef

### lambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListConnectorEntitiesRequestRequestTypeDef

### connectorProfileName
- **Type**: typing.Optional[str]

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### entitiesPath
- **Type**: typing.Optional[str]

### apiVersion
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorEntitiesResponseTypeDef

### connectorEntityMap
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.appflow_classes.ConnectorEntityTypeDef]]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConnectorsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsResponseTypeDef

### connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.ConnectorDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFlowsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowsResponseTypeDef

### flows
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow_classes.FlowDefinitionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MarketoConnectorProfileCredentialsTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]


# MarketoConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# MarketoDestinationPropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]


# MarketoSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# MetadataCatalogConfigTypeDef

### glueDataCatalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.GlueDataCatalogConfigTypeDef]


# MetadataCatalogDetailTypeDef

### catalogType
- **Type**: typing.Optional[typing.Literal['GLUE']]

### tableName
- **Type**: typing.Optional[str]

### tableRegistrationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.RegistrationOutputTypeDef]

### partitionRegistrationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.RegistrationOutputTypeDef]


# OAuth2CredentialsTypeDef

### clientId
- **Type**: typing.Optional[str]

### clientSecret
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]


# OAuth2CustomParameterTypeDef

### key
- **Type**: typing.Optional[str]

### isRequired
- **Type**: typing.Optional[bool]

### label
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### isSensitiveField
- **Type**: typing.Optional[bool]

### connectorSuppliedValues
- **Type**: typing.Optional[typing.List[str]]

### type
- **Type**: typing.Optional[typing.Literal['AUTH_URL', 'TOKEN_URL']]


# OAuth2DefaultsTypeDef

### oauthScopes
- **Type**: typing.Optional[typing.List[str]]

### tokenUrls
- **Type**: typing.Optional[typing.List[str]]

### authCodeUrls
- **Type**: typing.Optional[typing.List[str]]

### oauth2GrantTypesSupported
- **Type**: typing.Optional[typing.List[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]]

### oauth2CustomProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow_classes.OAuth2CustomParameterTypeDef]]


# OAuth2PropertiesTypeDef

### tokenUrl
- **Type**: <class 'str'>
- **Required**: Yes

### oAuth2GrantType
- **Type**: typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']
- **Required**: Yes

### tokenUrlCustomProperties
- **Type**: typing.Optional[typing.Mapping[str, str]]


# OAuthCredentialsTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]


# OAuthPropertiesTypeDef

### tokenUrl
- **Type**: <class 'str'>
- **Required**: Yes

### authCodeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### oAuthScopes
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PardotConnectorProfileCredentialsTypeDef

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]

### clientCredentialsArn
- **Type**: typing.Optional[str]


# PardotConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: typing.Optional[str]

### isSandboxEnvironment
- **Type**: typing.Optional[bool]

### businessUnitId
- **Type**: typing.Optional[str]


# PardotSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# PrefixConfigTypeDef

### prefixType
- **Type**: typing.Optional[typing.Literal['FILENAME', 'PATH', 'PATH_AND_FILENAME']]

### prefixFormat
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'YEAR']]

### pathPrefixHierarchy
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EXECUTION_ID', 'SCHEMA_VERSION']]]


# PrivateConnectionProvisioningStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'PENDING']]

### failureMessage
- **Type**: typing.Optional[str]

### failureCause
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'CONNECTOR_AUTHENTICATION', 'CONNECTOR_SERVER', 'INTERNAL_SERVER', 'VALIDATION']]


# RangeTypeDef

### maximum
- **Type**: typing.Optional[float]

### minimum
- **Type**: typing.Optional[float]


# RedshiftConnectorProfileCredentialsTypeDef

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Optional[str]


# RedshiftConnectorProfilePropertiesTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseUrl
- **Type**: typing.Optional[str]

### bucketPrefix
- **Type**: typing.Optional[str]

### dataApiRoleArn
- **Type**: typing.Optional[str]

### isRedshiftServerless
- **Type**: typing.Optional[bool]

### clusterIdentifier
- **Type**: typing.Optional[str]

### workgroupName
- **Type**: typing.Optional[str]

### databaseName
- **Type**: typing.Optional[str]


# RedshiftDestinationPropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateBucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]


# RegisterConnectorRequestRequestTypeDef

### connectorLabel
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### connectorProvisioningType
- **Type**: typing.Optional[typing.Literal['LAMBDA']]

### connectorProvisioningConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorProvisioningConfigTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# RegisterConnectorResponseTypeDef

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegistrationOutputTypeDef

### message
- **Type**: typing.Optional[str]

### result
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CancelStarted', 'Canceled', 'Error', 'InProgress', 'Successful']]


# ResetConnectorMetadataCacheRequestRequestTypeDef

### connectorProfileName
- **Type**: typing.Optional[str]

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### connectorEntityName
- **Type**: typing.Optional[str]

### entitiesPath
- **Type**: typing.Optional[str]

### apiVersion
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# S3DestinationPropertiesTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### s3OutputFormatConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.S3OutputFormatConfigTypeDef]


# S3InputFormatConfigTypeDef

### s3InputFileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON']]


# S3OutputFormatConfigTypeDef

### fileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON', 'PARQUET']]

### prefixConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.PrefixConfigTypeDef]

### aggregationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.AggregationConfigTypeDef]

### preserveSourceDataTyping
- **Type**: typing.Optional[bool]


# S3SourcePropertiesTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### s3InputFormatConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.S3InputFormatConfigTypeDef]


# SAPODataConnectorProfileCredentialsTypeDef

### basicAuthCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.BasicAuthCredentialsTypeDef]

### oAuthCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.OAuthCredentialsTypeDef]


# SAPODataConnectorProfilePropertiesTypeDef

### applicationHostUrl
- **Type**: <class 'str'>
- **Required**: Yes

### applicationServicePath
- **Type**: <class 'str'>
- **Required**: Yes

### portNumber
- **Type**: <class 'int'>
- **Required**: Yes

### clientNumber
- **Type**: <class 'str'>
- **Required**: Yes

### logonLanguage
- **Type**: typing.Optional[str]

### privateLinkServiceName
- **Type**: typing.Optional[str]

### oAuthProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.OAuthPropertiesTypeDef]

### disableSSO
- **Type**: typing.Optional[bool]


# SAPODataDestinationPropertiesTypeDef

### objectPath
- **Type**: <class 'str'>
- **Required**: Yes

### successResponseHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SuccessResponseHandlingConfigTypeDef]

### idFieldNames
- **Type**: typing.Optional[typing.Sequence[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]


# SAPODataPaginationConfigTypeDef

### maxPageSize
- **Type**: <class 'int'>
- **Required**: Yes


# SAPODataParallelismConfigTypeDef

### maxParallelism
- **Type**: <class 'int'>
- **Required**: Yes


# SAPODataSourcePropertiesTypeDef

### objectPath
- **Type**: typing.Optional[str]

### parallelismConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SAPODataParallelismConfigTypeDef]

### paginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SAPODataPaginationConfigTypeDef]


# SalesforceConnectorProfileCredentialsTypeDef

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]

### clientCredentialsArn
- **Type**: typing.Optional[str]

### oAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### jwtToken
- **Type**: typing.Optional[str]


# SalesforceConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: typing.Optional[str]

### isSandboxEnvironment
- **Type**: typing.Optional[bool]

### usePrivateLinkForMetadataAndAuthorization
- **Type**: typing.Optional[bool]


# SalesforceDestinationPropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### idFieldNames
- **Type**: typing.Optional[typing.Sequence[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]

### dataTransferApi
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'BULKV2', 'REST_SYNC']]


# SalesforceMetadataTypeDef

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]

### dataTransferApis
- **Type**: typing.Optional[typing.List[typing.Literal['AUTOMATIC', 'BULKV2', 'REST_SYNC']]]

### oauth2GrantTypesSupported
- **Type**: typing.Optional[typing.List[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]]


# SalesforceSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### enableDynamicFieldUpdate
- **Type**: typing.Optional[bool]

### includeDeletedRecords
- **Type**: typing.Optional[bool]

### dataTransferApi
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'BULKV2', 'REST_SYNC']]


# ScheduledTriggerPropertiesTypeDef

### scheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### dataPullMode
- **Type**: typing.Optional[typing.Literal['Complete', 'Incremental']]

### scheduleStartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### scheduleEndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### timezone
- **Type**: typing.Optional[str]

### scheduleOffset
- **Type**: typing.Optional[int]

### firstExecutionFrom
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### flowErrorDeactivationThreshold
- **Type**: typing.Optional[int]


# ServiceNowConnectorProfileCredentialsTypeDef

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Optional[str]

### oAuth2Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.OAuth2CredentialsTypeDef]


# ServiceNowConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceNowSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# SingularConnectorProfileCredentialsTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes


# SingularSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# SlackConnectorProfileCredentialsTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]


# SlackConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# SlackMetadataTypeDef

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]


# SlackSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# SnowflakeConnectorProfileCredentialsTypeDef

### username
- **Type**: <class 'str'>
- **Required**: Yes

### password
- **Type**: <class 'str'>
- **Required**: Yes


# SnowflakeConnectorProfilePropertiesTypeDef

### warehouse
- **Type**: <class 'str'>
- **Required**: Yes

### stage
- **Type**: <class 'str'>
- **Required**: Yes

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### privateLinkServiceName
- **Type**: typing.Optional[str]

### accountName
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]


# SnowflakeDestinationPropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateBucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]


# SnowflakeMetadataTypeDef

### supportedRegions
- **Type**: typing.Optional[typing.List[str]]


# SourceConnectorPropertiesTypeDef

### Amplitude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.AmplitudeSourcePropertiesTypeDef]

### Datadog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.DatadogSourcePropertiesTypeDef]

### Dynatrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.DynatraceSourcePropertiesTypeDef]

### GoogleAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.GoogleAnalyticsSourcePropertiesTypeDef]

### InforNexus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.InforNexusSourcePropertiesTypeDef]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.MarketoSourcePropertiesTypeDef]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.S3SourcePropertiesTypeDef]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SalesforceSourcePropertiesTypeDef]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ServiceNowSourcePropertiesTypeDef]

### Singular
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SingularSourcePropertiesTypeDef]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SlackSourcePropertiesTypeDef]

### Trendmicro
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.TrendmicroSourcePropertiesTypeDef]

### Veeva
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.VeevaSourcePropertiesTypeDef]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ZendeskSourcePropertiesTypeDef]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.SAPODataSourcePropertiesTypeDef]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.CustomConnectorSourcePropertiesTypeDef]

### Pardot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.PardotSourcePropertiesTypeDef]


# SourceFieldPropertiesTypeDef

### isRetrievable
- **Type**: typing.Optional[bool]

### isQueryable
- **Type**: typing.Optional[bool]

### isTimestampFieldForIncrementalQueries
- **Type**: typing.Optional[bool]


# SourceFlowConfigTypeDef

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### sourceConnectorProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.SourceConnectorPropertiesTypeDef'>
- **Required**: Yes

### apiVersion
- **Type**: typing.Optional[str]

### connectorProfileName
- **Type**: typing.Optional[str]

### incrementalPullConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.IncrementalPullConfigTypeDef]


# StartFlowRequestRequestTypeDef

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartFlowResponseTypeDef

### flowArn
- **Type**: <class 'str'>
- **Required**: Yes

### flowStatus
- **Type**: typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']
- **Required**: Yes

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopFlowRequestRequestTypeDef

### flowName
- **Type**: <class 'str'>
- **Required**: Yes


# StopFlowResponseTypeDef

### flowArn
- **Type**: <class 'str'>
- **Required**: Yes

### flowStatus
- **Type**: typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SuccessResponseHandlingConfigTypeDef

### bucketPrefix
- **Type**: typing.Optional[str]

### bucketName
- **Type**: typing.Optional[str]


# SupportedFieldTypeDetailsTypeDef

### v1
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.FieldTypeDetailsTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TaskTypeDef

### sourceFields
- **Type**: typing.Sequence[str]
- **Required**: Yes

### taskType
- **Type**: typing.Literal['Arithmetic', 'Filter', 'Map', 'Map_all', 'Mask', 'Merge', 'Partition', 'Passthrough', 'Truncate', 'Validate']
- **Required**: Yes

### connectorOperator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOperatorTypeDef]

### destinationField
- **Type**: typing.Optional[str]

### taskProperties
- **Type**: typing.Optional[typing.Mapping[typing.Literal['CONCAT_FORMAT', 'DATA_TYPE', 'DESTINATION_DATA_TYPE', 'EXCLUDE_SOURCE_FIELDS_LIST', 'INCLUDE_NEW_FIELDS', 'LOWER_BOUND', 'MASK_LENGTH', 'MASK_VALUE', 'MATH_OPERATION_FIELDS_ORDER', 'ORDERED_PARTITION_KEYS_LIST', 'SOURCE_DATA_TYPE', 'SUBFIELD_CATEGORY_MAP', 'TRUNCATE_LENGTH', 'UPPER_BOUND', 'VALIDATION_ACTION', 'VALUE', 'VALUES'], str]]


# TrendmicroConnectorProfileCredentialsTypeDef

### apiSecretKey
- **Type**: <class 'str'>
- **Required**: Yes


# TrendmicroSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes


# TriggerConfigTypeDef

### triggerType
- **Type**: typing.Literal['Event', 'OnDemand', 'Scheduled']
- **Required**: Yes

### triggerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.TriggerPropertiesTypeDef]


# TriggerPropertiesTypeDef

### Scheduled
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ScheduledTriggerPropertiesTypeDef]


# UnregisterConnectorRequestRequestTypeDef

### connectorLabel
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateConnectorProfileRequestRequestTypeDef

### connectorProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### connectionMode
- **Type**: typing.Literal['Private', 'Public']
- **Required**: Yes

### connectorProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ConnectorProfileConfigTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateConnectorProfileResponseTypeDef

### connectorProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateConnectorRegistrationRequestRequestTypeDef

### connectorLabel
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### connectorProvisioningConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorProvisioningConfigTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# UpdateConnectorRegistrationResponseTypeDef

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlowRequestRequestTypeDef

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### triggerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.TriggerConfigTypeDef'>
- **Required**: Yes

### sourceFlowConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.SourceFlowConfigTypeDef'>
- **Required**: Yes

### destinationFlowConfigList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appflow_classes.DestinationFlowConfigTypeDef]
- **Required**: Yes

### tasks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appflow_classes.TaskTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### metadataCatalogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.MetadataCatalogConfigTypeDef]

### clientToken
- **Type**: typing.Optional[str]


# UpdateFlowResponseTypeDef

### flowStatus
- **Type**: typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpsolverDestinationPropertiesTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3OutputFormatConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.UpsolverS3OutputFormatConfigTypeDef'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]


# UpsolverS3OutputFormatConfigTypeDef

### prefixConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow_classes.PrefixConfigTypeDef'>
- **Required**: Yes

### fileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON', 'PARQUET']]

### aggregationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.AggregationConfigTypeDef]


# VeevaConnectorProfileCredentialsTypeDef

### username
- **Type**: <class 'str'>
- **Required**: Yes

### password
- **Type**: <class 'str'>
- **Required**: Yes


# VeevaConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# VeevaSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### documentType
- **Type**: typing.Optional[str]

### includeSourceFiles
- **Type**: typing.Optional[bool]

### includeRenditions
- **Type**: typing.Optional[bool]

### includeAllVersions
- **Type**: typing.Optional[bool]


# ZendeskConnectorProfileCredentialsTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ConnectorOAuthRequestTypeDef]


# ZendeskConnectorProfilePropertiesTypeDef

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ZendeskDestinationPropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes

### idFieldNames
- **Type**: typing.Optional[typing.Sequence[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow_classes.ErrorHandlingConfigTypeDef]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]


# ZendeskMetadataTypeDef

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]


# ZendeskSourcePropertiesTypeDef

### object
- **Type**: <class 'str'>
- **Required**: Yes



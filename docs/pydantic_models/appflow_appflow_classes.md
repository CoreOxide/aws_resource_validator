# Appflow Appflow Classes

# AggregationConfig

### aggregationType
- **Type**: typing.Optional[typing.Literal['None', 'SingleFile']]

### targetFileSize
- **Type**: typing.Optional[int]


# AmplitudeConnectorProfileCredentials

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### secretKey
- **Type**: <class 'str'>
- **Required**: Yes


# AmplitudeSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# ApiKeyCredentials

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### apiSecretKey
- **Type**: typing.Optional[str]


# AuthParameter

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


# AuthenticationConfig

### isBasicAuthSupported
- **Type**: typing.Optional[bool]

### isApiKeyAuthSupported
- **Type**: typing.Optional[bool]

### isOAuth2Supported
- **Type**: typing.Optional[bool]

### isCustomAuthSupported
- **Type**: typing.Optional[bool]

### oAuth2Defaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuth2Defaults]

### customAuthConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomAuthConfig]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthCredentials

### username
- **Type**: <class 'str'>
- **Required**: Yes

### password
- **Type**: <class 'str'>
- **Required**: Yes


# CancelFlowExecutionsRequest

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### executionIds
- **Type**: typing.Optional[typing.List[str]]


# CancelFlowExecutionsResponse

### invalidExecutions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# ConnectorConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorMetadata]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.AuthenticationConfig]

### connectorRuntimeSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorRuntimeSetting]]

### supportedApiVersions
- **Type**: typing.Optional[typing.List[str]]

### supportedOperators
- **Type**: typing.Optional[typing.List[typing.Literal['ADDITION', 'BETWEEN', 'CONTAINS', 'DIVISION', 'EQUAL_TO', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL_TO', 'LESS_THAN', 'LESS_THAN_OR_EQUAL_TO', 'MASK_ALL', 'MASK_FIRST_N', 'MASK_LAST_N', 'MULTIPLICATION', 'NOT_EQUAL_TO', 'NO_OP', 'PROJECTION', 'SUBTRACTION', 'VALIDATE_NON_NEGATIVE', 'VALIDATE_NON_NULL', 'VALIDATE_NON_ZERO', 'VALIDATE_NUMERIC']]]

### supportedWriteOperations
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]]

### connectorProvisioningType
- **Type**: typing.Optional[typing.Literal['LAMBDA']]

### connectorProvisioningConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProvisioningConfig]

### logoURL
- **Type**: typing.Optional[str]

### registeredAt
- **Type**: typing.Optional[datetime.datetime]

### registeredBy
- **Type**: typing.Optional[str]

### supportedDataTransferTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FILE', 'RECORD']]]

### supportedDataTransferApis
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.DataTransferApi]]


# ConnectorDetail

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


# ConnectorEntity

### name
- **Type**: <class 'str'>
- **Required**: Yes

### label
- **Type**: typing.Optional[str]

### hasNestedEntities
- **Type**: typing.Optional[bool]


# ConnectorEntityField

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SupportedFieldTypeDetails]

### description
- **Type**: typing.Optional[str]

### sourceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SourceFieldProperties]

### destinationProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationFieldProperties]

### customProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConnectorMetadata

### Amplitude
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Datadog
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Dynatrace
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### GoogleAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.GoogleAnalyticsMetadata]

### InforNexus
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Marketo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Redshift
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### S3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceMetadata]

### ServiceNow
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Singular
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SlackMetadata]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SnowflakeMetadata]

### Trendmicro
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Veeva
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskMetadata]

### EventBridge
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Upsolver
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### CustomerProfiles
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Honeycode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.HoneycodeMetadata]

### SAPOData
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Pardot
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ConnectorOAuthRequest

### authCode
- **Type**: typing.Optional[str]

### redirectUri
- **Type**: typing.Optional[str]


# ConnectorOperator

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


# ConnectorProfile

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProfilePropertiesOutput]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### privateConnectionProvisioningState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.PrivateConnectionProvisioningState]


# ConnectorProfileConfig

### connectorProfileProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProfileProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProfilePropertiesOutput]
- **Required**: Yes

### connectorProfileCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProfileCredentials]


# ConnectorProfileCredentials

### Amplitude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.AmplitudeConnectorProfileCredentials]

### Datadog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DatadogConnectorProfileCredentials]

### Dynatrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DynatraceConnectorProfileCredentials]

### GoogleAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.GoogleAnalyticsConnectorProfileCredentials]

### Honeycode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.HoneycodeConnectorProfileCredentials]

### InforNexus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.InforNexusConnectorProfileCredentials]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MarketoConnectorProfileCredentials]

### Redshift
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.RedshiftConnectorProfileCredentials]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceConnectorProfileCredentials]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ServiceNowConnectorProfileCredentials]

### Singular
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SingularConnectorProfileCredentials]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SlackConnectorProfileCredentials]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SnowflakeConnectorProfileCredentials]

### Trendmicro
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.TrendmicroConnectorProfileCredentials]

### Veeva
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.VeevaConnectorProfileCredentials]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskConnectorProfileCredentials]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataConnectorProfileCredentials]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorProfileCredentials]

### Pardot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.PardotConnectorProfileCredentials]


# ConnectorProfileProperties

### Amplitude
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Datadog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DatadogConnectorProfileProperties]

### Dynatrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DynatraceConnectorProfileProperties]

### GoogleAnalytics
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Honeycode
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### InforNexus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.InforNexusConnectorProfileProperties]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MarketoConnectorProfileProperties]

### Redshift
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.RedshiftConnectorProfileProperties]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceConnectorProfileProperties]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ServiceNowConnectorProfileProperties]

### Singular
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SlackConnectorProfileProperties]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SnowflakeConnectorProfileProperties]

### Trendmicro
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Veeva
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.VeevaConnectorProfileProperties]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskConnectorProfileProperties]

### SAPOData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataConnectorProfileProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataConnectorProfilePropertiesOutput, NoneType]

### CustomConnector
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorProfileProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorProfilePropertiesOutput, NoneType]

### Pardot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.PardotConnectorProfileProperties]


# ConnectorProfilePropertiesOutput

### Amplitude
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Datadog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DatadogConnectorProfileProperties]

### Dynatrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DynatraceConnectorProfileProperties]

### GoogleAnalytics
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Honeycode
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### InforNexus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.InforNexusConnectorProfileProperties]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MarketoConnectorProfileProperties]

### Redshift
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.RedshiftConnectorProfileProperties]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceConnectorProfileProperties]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ServiceNowConnectorProfileProperties]

### Singular
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SlackConnectorProfileProperties]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SnowflakeConnectorProfileProperties]

### Trendmicro
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Veeva
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.VeevaConnectorProfileProperties]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskConnectorProfileProperties]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataConnectorProfilePropertiesOutput]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorProfilePropertiesOutput]

### Pardot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.PardotConnectorProfileProperties]


# ConnectorProvisioningConfig

### lambda_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.LambdaConnectorProvisioningConfig]


# ConnectorRuntimeSetting

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


# CreateConnectorProfileRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProfileConfig'>
- **Required**: Yes

### kmsArn
- **Type**: typing.Optional[str]

### connectorLabel
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# CreateConnectorProfileResponse

### connectorProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFlowRequest

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### triggerConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.TriggerConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.TriggerConfigOutput]
- **Required**: Yes

### sourceFlowConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.SourceFlowConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.SourceFlowConfigOutput]
- **Required**: Yes

### destinationFlowConfigList
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationFlowConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationFlowConfigOutput]]
- **Required**: Yes

### tasks
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.Task, aws_resource_validator.pydantic_models.appflow.appflow_classes.TaskOutput]]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### kmsArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### metadataCatalogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MetadataCatalogConfig]

### clientToken
- **Type**: typing.Optional[str]


# CreateFlowResponse

### flowArn
- **Type**: <class 'str'>
- **Required**: Yes

### flowStatus
- **Type**: typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# CustomAuthConfig

### customAuthenticationType
- **Type**: typing.Optional[str]

### authParameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.AuthParameter]]


# CustomAuthCredentials

### customAuthenticationType
- **Type**: <class 'str'>
- **Required**: Yes

### credentialsMap
- **Type**: typing.Optional[typing.Dict[str, str]]


# CustomConnectorDestinationProperties

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]

### idFieldNames
- **Type**: typing.Optional[typing.List[str]]

### customProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# CustomConnectorDestinationPropertiesOutput

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]

### idFieldNames
- **Type**: typing.Optional[typing.List[str]]

### customProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# CustomConnectorProfileCredentials

### authenticationType
- **Type**: typing.Literal['APIKEY', 'BASIC', 'CUSTOM', 'OAUTH2']
- **Required**: Yes

### basic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.BasicAuthCredentials]

### oauth2
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuth2Credentials]

### apiKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ApiKeyCredentials]

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomAuthCredentials]


# CustomConnectorProfileProperties

### profileProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### oAuth2Properties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuth2Properties, aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuth2PropertiesOutput, NoneType]


# CustomConnectorProfilePropertiesOutput

### profileProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### oAuth2Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuth2PropertiesOutput]


# CustomConnectorSourceProperties

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### customProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### dataTransferApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DataTransferApi]


# CustomConnectorSourcePropertiesOutput

### entityName
- **Type**: <class 'str'>
- **Required**: Yes

### customProperties
- **Type**: typing.Optional[typing.Dict[str, str]]

### dataTransferApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DataTransferApi]


# CustomerProfilesDestinationProperties

### domainName
- **Type**: <class 'str'>
- **Required**: Yes

### objectTypeName
- **Type**: typing.Optional[str]


# DataTransferApi

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ASYNC', 'AUTOMATIC', 'SYNC']]


# DatadogConnectorProfileCredentials

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes

### applicationKey
- **Type**: <class 'str'>
- **Required**: Yes


# DatadogConnectorProfileProperties

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# DatadogSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectorProfileRequest

### connectorProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DeleteFlowRequest

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# DescribeConnectorEntityRequest

### connectorEntityName
- **Type**: <class 'str'>
- **Required**: Yes

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### connectorProfileName
- **Type**: typing.Optional[str]

### apiVersion
- **Type**: typing.Optional[str]


# DescribeConnectorEntityResponse

### connectorEntityFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorEntityField]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectorProfilesRequest

### connectorProfileNames
- **Type**: typing.Optional[typing.List[str]]

### connectorType
- **Type**: typing.Optional[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]

### connectorLabel
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeConnectorProfilesResponse

### connectorProfileDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProfile]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeConnectorRequest

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### connectorLabel
- **Type**: typing.Optional[str]


# DescribeConnectorResponse

### connectorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectorsRequest

### connectorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeConnectorsResponse

### connectorConfigurations
- **Type**: typing.Dict[typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk'], aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorConfiguration]
- **Required**: Yes

### connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeFlowExecutionRecordsRequest

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeFlowExecutionRecordsResponse

### flowExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.ExecutionRecord]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeFlowRequest

### flowName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlowResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.SourceFlowConfigOutput'>
- **Required**: Yes

### destinationFlowConfigList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationFlowConfigOutput]
- **Required**: Yes

### lastRunExecutionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ExecutionDetails'>
- **Required**: Yes

### triggerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.TriggerConfigOutput'>
- **Required**: Yes

### tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.TaskOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.MetadataCatalogConfig'>
- **Required**: Yes

### lastRunMetadataCatalogDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.MetadataCatalogDetail]
- **Required**: Yes

### schemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationConnectorProperties

### Redshift
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.RedshiftDestinationProperties]

### S3
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.S3DestinationProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.S3DestinationPropertiesOutput, NoneType]

### Salesforce
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceDestinationProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceDestinationPropertiesOutput, NoneType]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SnowflakeDestinationProperties]

### EventBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.EventBridgeDestinationProperties]

### LookoutMetrics
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Upsolver
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.UpsolverDestinationProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.UpsolverDestinationPropertiesOutput, NoneType]

### Honeycode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.HoneycodeDestinationProperties]

### CustomerProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomerProfilesDestinationProperties]

### Zendesk
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskDestinationProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskDestinationPropertiesOutput, NoneType]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MarketoDestinationProperties]

### CustomConnector
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorDestinationProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorDestinationPropertiesOutput, NoneType]

### SAPOData
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataDestinationProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataDestinationPropertiesOutput, NoneType]


# DestinationConnectorPropertiesOutput

### Redshift
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.RedshiftDestinationProperties]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.S3DestinationPropertiesOutput]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceDestinationPropertiesOutput]

### Snowflake
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SnowflakeDestinationProperties]

### EventBridge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.EventBridgeDestinationProperties]

### LookoutMetrics
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Upsolver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.UpsolverDestinationPropertiesOutput]

### Honeycode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.HoneycodeDestinationProperties]

### CustomerProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomerProfilesDestinationProperties]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskDestinationPropertiesOutput]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MarketoDestinationProperties]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorDestinationPropertiesOutput]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataDestinationPropertiesOutput]


# DestinationFieldProperties

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


# DestinationFlowConfig

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### destinationConnectorProperties
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationConnectorProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationConnectorPropertiesOutput]
- **Required**: Yes

### apiVersion
- **Type**: typing.Optional[str]

### connectorProfileName
- **Type**: typing.Optional[str]


# DestinationFlowConfigOutput

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### destinationConnectorProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationConnectorPropertiesOutput'>
- **Required**: Yes

### apiVersion
- **Type**: typing.Optional[str]

### connectorProfileName
- **Type**: typing.Optional[str]


# DynatraceConnectorProfileCredentials

### apiToken
- **Type**: <class 'str'>
- **Required**: Yes


# DynatraceConnectorProfileProperties

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# DynatraceSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorHandlingConfig

### failOnFirstDestinationError
- **Type**: typing.Optional[bool]

### bucketPrefix
- **Type**: typing.Optional[str]

### bucketName
- **Type**: typing.Optional[str]


# ErrorInfo

### putFailuresCount
- **Type**: typing.Optional[int]

### executionMessage
- **Type**: typing.Optional[str]


# EventBridgeDestinationProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]


# ExecutionDetails

### mostRecentExecutionMessage
- **Type**: typing.Optional[str]

### mostRecentExecutionTime
- **Type**: typing.Optional[datetime.datetime]

### mostRecentExecutionStatus
- **Type**: typing.Optional[typing.Literal['CancelStarted', 'Canceled', 'Error', 'InProgress', 'Successful']]


# ExecutionRecord

### executionId
- **Type**: typing.Optional[str]

### executionStatus
- **Type**: typing.Optional[typing.Literal['CancelStarted', 'Canceled', 'Error', 'InProgress', 'Successful']]

### executionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ExecutionResult]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### dataPullStartTime
- **Type**: typing.Optional[datetime.datetime]

### dataPullEndTime
- **Type**: typing.Optional[datetime.datetime]

### metadataCatalogDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.MetadataCatalogDetail]]


# ExecutionResult

### errorInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorInfo]

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


# FieldTypeDetails

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.Range]

### fieldLengthRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.Range]


# FlowDefinition

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ExecutionDetails]


# GlueDataCatalogConfig

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### tablePrefix
- **Type**: <class 'str'>
- **Required**: Yes


# GoogleAnalyticsConnectorProfileCredentials

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]


# GoogleAnalyticsMetadata

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]


# GoogleAnalyticsSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# HoneycodeConnectorProfileCredentials

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]


# HoneycodeDestinationProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]


# HoneycodeMetadata

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]


# IncrementalPullConfig

### datetimeTypeFieldName
- **Type**: typing.Optional[str]


# InforNexusConnectorProfileCredentials

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


# InforNexusConnectorProfileProperties

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# InforNexusSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaConnectorProvisioningConfig

### lambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListConnectorEntitiesRequest

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


# ListConnectorEntitiesResponse

### connectorEntityMap
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorEntity]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListConnectorsResponse

### connectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFlowsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowsResponse

### flows
- **Type**: typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.FlowDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# MarketoConnectorProfileCredentials

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]


# MarketoConnectorProfileProperties

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# MarketoDestinationProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]


# MarketoSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# MetadataCatalogConfig

### glueDataCatalog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.GlueDataCatalogConfig]


# MetadataCatalogDetail

### catalogType
- **Type**: typing.Optional[typing.Literal['GLUE']]

### tableName
- **Type**: typing.Optional[str]

### tableRegistrationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.RegistrationOutput]

### partitionRegistrationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.RegistrationOutput]


# OAuth2Credentials

### clientId
- **Type**: typing.Optional[str]

### clientSecret
- **Type**: typing.Optional[str]

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]


# OAuth2CustomParameter

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


# OAuth2Defaults

### oauthScopes
- **Type**: typing.Optional[typing.List[str]]

### tokenUrls
- **Type**: typing.Optional[typing.List[str]]

### authCodeUrls
- **Type**: typing.Optional[typing.List[str]]

### oauth2GrantTypesSupported
- **Type**: typing.Optional[typing.List[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]]

### oauth2CustomProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuth2CustomParameter]]


# OAuth2Properties

### tokenUrl
- **Type**: <class 'str'>
- **Required**: Yes

### oAuth2GrantType
- **Type**: typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']
- **Required**: Yes

### tokenUrlCustomProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# OAuth2PropertiesOutput

### tokenUrl
- **Type**: <class 'str'>
- **Required**: Yes

### oAuth2GrantType
- **Type**: typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']
- **Required**: Yes

### tokenUrlCustomProperties
- **Type**: typing.Optional[typing.Dict[str, str]]


# OAuthCredentials

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]


# OAuthProperties

### tokenUrl
- **Type**: <class 'str'>
- **Required**: Yes

### authCodeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### oAuthScopes
- **Type**: typing.List[str]
- **Required**: Yes


# OAuthPropertiesOutput

### tokenUrl
- **Type**: <class 'str'>
- **Required**: Yes

### authCodeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### oAuthScopes
- **Type**: typing.List[str]
- **Required**: Yes


# PardotConnectorProfileCredentials

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]

### clientCredentialsArn
- **Type**: typing.Optional[str]


# PardotConnectorProfileProperties

### instanceUrl
- **Type**: typing.Optional[str]

### isSandboxEnvironment
- **Type**: typing.Optional[bool]

### businessUnitId
- **Type**: typing.Optional[str]


# PardotSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# PrefixConfig

### prefixType
- **Type**: typing.Optional[typing.Literal['FILENAME', 'PATH', 'PATH_AND_FILENAME']]

### prefixFormat
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'YEAR']]

### pathPrefixHierarchy
- **Type**: typing.Optional[typing.List[typing.Literal['EXECUTION_ID', 'SCHEMA_VERSION']]]


# PrefixConfigOutput

### prefixType
- **Type**: typing.Optional[typing.Literal['FILENAME', 'PATH', 'PATH_AND_FILENAME']]

### prefixFormat
- **Type**: typing.Optional[typing.Literal['DAY', 'HOUR', 'MINUTE', 'MONTH', 'YEAR']]

### pathPrefixHierarchy
- **Type**: typing.Optional[typing.List[typing.Literal['EXECUTION_ID', 'SCHEMA_VERSION']]]


# PrivateConnectionProvisioningState

### status
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'PENDING']]

### failureMessage
- **Type**: typing.Optional[str]

### failureCause
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'CONNECTOR_AUTHENTICATION', 'CONNECTOR_SERVER', 'INTERNAL_SERVER', 'VALIDATION']]


# Range

### maximum
- **Type**: typing.Optional[float]

### minimum
- **Type**: typing.Optional[float]


# RedshiftConnectorProfileCredentials

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Optional[str]


# RedshiftConnectorProfileProperties

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


# RedshiftDestinationProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateBucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]


# RegisterConnectorRequest

### connectorLabel
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### connectorProvisioningType
- **Type**: typing.Optional[typing.Literal['LAMBDA']]

### connectorProvisioningConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProvisioningConfig]

### clientToken
- **Type**: typing.Optional[str]


# RegisterConnectorResponse

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# RegistrationOutput

### message
- **Type**: typing.Optional[str]

### result
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CancelStarted', 'Canceled', 'Error', 'InProgress', 'Successful']]


# ResetConnectorMetadataCacheRequest

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


# S3DestinationProperties

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### s3OutputFormatConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.S3OutputFormatConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.S3OutputFormatConfigOutput, NoneType]


# S3DestinationPropertiesOutput

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### s3OutputFormatConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.S3OutputFormatConfigOutput]


# S3InputFormatConfig

### s3InputFileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON']]


# S3OutputFormatConfig

### fileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON', 'PARQUET']]

### prefixConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.PrefixConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.PrefixConfigOutput, NoneType]

### aggregationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.AggregationConfig]

### preserveSourceDataTyping
- **Type**: typing.Optional[bool]


# S3OutputFormatConfigOutput

### fileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON', 'PARQUET']]

### prefixConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.PrefixConfigOutput]

### aggregationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.AggregationConfig]

### preserveSourceDataTyping
- **Type**: typing.Optional[bool]


# S3SourceProperties

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### s3InputFormatConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.S3InputFormatConfig]


# SAPODataConnectorProfileCredentials

### basicAuthCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.BasicAuthCredentials]

### oAuthCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuthCredentials]


# SAPODataConnectorProfileProperties

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuthProperties, aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuthPropertiesOutput, NoneType]

### disableSSO
- **Type**: typing.Optional[bool]


# SAPODataConnectorProfilePropertiesOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuthPropertiesOutput]

### disableSSO
- **Type**: typing.Optional[bool]


# SAPODataDestinationProperties

### objectPath
- **Type**: <class 'str'>
- **Required**: Yes

### successResponseHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SuccessResponseHandlingConfig]

### idFieldNames
- **Type**: typing.Optional[typing.List[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]


# SAPODataDestinationPropertiesOutput

### objectPath
- **Type**: <class 'str'>
- **Required**: Yes

### successResponseHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SuccessResponseHandlingConfig]

### idFieldNames
- **Type**: typing.Optional[typing.List[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]


# SAPODataPaginationConfig

### maxPageSize
- **Type**: <class 'int'>
- **Required**: Yes


# SAPODataParallelismConfig

### maxParallelism
- **Type**: <class 'int'>
- **Required**: Yes


# SAPODataSourceProperties

### objectPath
- **Type**: typing.Optional[str]

### parallelismConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataParallelismConfig]

### paginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataPaginationConfig]


# SalesforceConnectorProfileCredentials

### accessToken
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]

### clientCredentialsArn
- **Type**: typing.Optional[str]

### oAuth2GrantType
- **Type**: typing.Optional[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]

### jwtToken
- **Type**: typing.Optional[str]


# SalesforceConnectorProfileProperties

### instanceUrl
- **Type**: typing.Optional[str]

### isSandboxEnvironment
- **Type**: typing.Optional[bool]

### usePrivateLinkForMetadataAndAuthorization
- **Type**: typing.Optional[bool]


# SalesforceDestinationProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes

### idFieldNames
- **Type**: typing.Optional[typing.List[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]

### dataTransferApi
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'BULKV2', 'REST_SYNC']]


# SalesforceDestinationPropertiesOutput

### object
- **Type**: <class 'str'>
- **Required**: Yes

### idFieldNames
- **Type**: typing.Optional[typing.List[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]

### dataTransferApi
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'BULKV2', 'REST_SYNC']]


# SalesforceMetadata

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]

### dataTransferApis
- **Type**: typing.Optional[typing.List[typing.Literal['AUTOMATIC', 'BULKV2', 'REST_SYNC']]]

### oauth2GrantTypesSupported
- **Type**: typing.Optional[typing.List[typing.Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER']]]


# SalesforceSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes

### enableDynamicFieldUpdate
- **Type**: typing.Optional[bool]

### includeDeletedRecords
- **Type**: typing.Optional[bool]

### dataTransferApi
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'BULKV2', 'REST_SYNC']]


# ScheduledTriggerProperties

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


# ScheduledTriggerPropertiesOutput

### scheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### dataPullMode
- **Type**: typing.Optional[typing.Literal['Complete', 'Incremental']]

### scheduleStartTime
- **Type**: typing.Optional[datetime.datetime]

### scheduleEndTime
- **Type**: typing.Optional[datetime.datetime]

### timezone
- **Type**: typing.Optional[str]

### scheduleOffset
- **Type**: typing.Optional[int]

### firstExecutionFrom
- **Type**: typing.Optional[datetime.datetime]

### flowErrorDeactivationThreshold
- **Type**: typing.Optional[int]


# ServiceNowConnectorProfileCredentials

### username
- **Type**: typing.Optional[str]

### password
- **Type**: typing.Optional[str]

### oAuth2Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.OAuth2Credentials]


# ServiceNowConnectorProfileProperties

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceNowSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# SingularConnectorProfileCredentials

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes


# SingularSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# SlackConnectorProfileCredentials

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]


# SlackConnectorProfileProperties

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# SlackMetadata

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]


# SlackSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# SnowflakeConnectorProfileCredentials

### username
- **Type**: <class 'str'>
- **Required**: Yes

### password
- **Type**: <class 'str'>
- **Required**: Yes


# SnowflakeConnectorProfileProperties

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


# SnowflakeDestinationProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes

### intermediateBucketName
- **Type**: <class 'str'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]


# SnowflakeMetadata

### supportedRegions
- **Type**: typing.Optional[typing.List[str]]


# SourceConnectorProperties

### Amplitude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.AmplitudeSourceProperties]

### Datadog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DatadogSourceProperties]

### Dynatrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DynatraceSourceProperties]

### GoogleAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.GoogleAnalyticsSourceProperties]

### InforNexus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.InforNexusSourceProperties]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MarketoSourceProperties]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.S3SourceProperties]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceSourceProperties]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ServiceNowSourceProperties]

### Singular
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SingularSourceProperties]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SlackSourceProperties]

### Trendmicro
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.TrendmicroSourceProperties]

### Veeva
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.VeevaSourceProperties]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskSourceProperties]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataSourceProperties]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorSourceProperties]

### Pardot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.PardotSourceProperties]


# SourceConnectorPropertiesOutput

### Amplitude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.AmplitudeSourceProperties]

### Datadog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DatadogSourceProperties]

### Dynatrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.DynatraceSourceProperties]

### GoogleAnalytics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.GoogleAnalyticsSourceProperties]

### InforNexus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.InforNexusSourceProperties]

### Marketo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MarketoSourceProperties]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.S3SourceProperties]

### Salesforce
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SalesforceSourceProperties]

### ServiceNow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ServiceNowSourceProperties]

### Singular
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SingularSourceProperties]

### Slack
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SlackSourceProperties]

### Trendmicro
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.TrendmicroSourceProperties]

### Veeva
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.VeevaSourceProperties]

### Zendesk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ZendeskSourceProperties]

### SAPOData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.SAPODataSourceProperties]

### CustomConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.CustomConnectorSourcePropertiesOutput]

### Pardot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.PardotSourceProperties]


# SourceFieldProperties

### isRetrievable
- **Type**: typing.Optional[bool]

### isQueryable
- **Type**: typing.Optional[bool]

### isTimestampFieldForIncrementalQueries
- **Type**: typing.Optional[bool]


# SourceFlowConfig

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### sourceConnectorProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.SourceConnectorProperties'>
- **Required**: Yes

### apiVersion
- **Type**: typing.Optional[str]

### connectorProfileName
- **Type**: typing.Optional[str]

### incrementalPullConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.IncrementalPullConfig]


# SourceFlowConfigOutput

### connectorType
- **Type**: typing.Literal['Amplitude', 'CustomConnector', 'CustomerProfiles', 'Datadog', 'Dynatrace', 'EventBridge', 'Googleanalytics', 'Honeycode', 'Infornexus', 'LookoutMetrics', 'Marketo', 'Pardot', 'Redshift', 'S3', 'SAPOData', 'Salesforce', 'Servicenow', 'Singular', 'Slack', 'Snowflake', 'Trendmicro', 'Upsolver', 'Veeva', 'Zendesk']
- **Required**: Yes

### sourceConnectorProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.SourceConnectorPropertiesOutput'>
- **Required**: Yes

### apiVersion
- **Type**: typing.Optional[str]

### connectorProfileName
- **Type**: typing.Optional[str]

### incrementalPullConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.IncrementalPullConfig]


# StartFlowRequest

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# StartFlowResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# StopFlowRequest

### flowName
- **Type**: <class 'str'>
- **Required**: Yes


# StopFlowResponse

### flowArn
- **Type**: <class 'str'>
- **Required**: Yes

### flowStatus
- **Type**: typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# SuccessResponseHandlingConfig

### bucketPrefix
- **Type**: typing.Optional[str]

### bucketName
- **Type**: typing.Optional[str]


# SupportedFieldTypeDetails

### v1
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.FieldTypeDetails'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# Task

### sourceFields
- **Type**: typing.List[str]
- **Required**: Yes

### taskType
- **Type**: typing.Literal['Arithmetic', 'Filter', 'Map', 'Map_all', 'Mask', 'Merge', 'Partition', 'Passthrough', 'Truncate', 'Validate']
- **Required**: Yes

### connectorOperator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOperator]

### destinationField
- **Type**: typing.Optional[str]

### taskProperties
- **Type**: typing.Optional[typing.Dict[typing.Literal['CONCAT_FORMAT', 'DATA_TYPE', 'DESTINATION_DATA_TYPE', 'EXCLUDE_SOURCE_FIELDS_LIST', 'INCLUDE_NEW_FIELDS', 'LOWER_BOUND', 'MASK_LENGTH', 'MASK_VALUE', 'MATH_OPERATION_FIELDS_ORDER', 'ORDERED_PARTITION_KEYS_LIST', 'SOURCE_DATA_TYPE', 'SUBFIELD_CATEGORY_MAP', 'TRUNCATE_LENGTH', 'UPPER_BOUND', 'VALIDATION_ACTION', 'VALUE', 'VALUES'], str]]


# TaskOutput

### sourceFields
- **Type**: typing.List[str]
- **Required**: Yes

### taskType
- **Type**: typing.Literal['Arithmetic', 'Filter', 'Map', 'Map_all', 'Mask', 'Merge', 'Partition', 'Passthrough', 'Truncate', 'Validate']
- **Required**: Yes

### connectorOperator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOperator]

### destinationField
- **Type**: typing.Optional[str]

### taskProperties
- **Type**: typing.Optional[typing.Dict[typing.Literal['CONCAT_FORMAT', 'DATA_TYPE', 'DESTINATION_DATA_TYPE', 'EXCLUDE_SOURCE_FIELDS_LIST', 'INCLUDE_NEW_FIELDS', 'LOWER_BOUND', 'MASK_LENGTH', 'MASK_VALUE', 'MATH_OPERATION_FIELDS_ORDER', 'ORDERED_PARTITION_KEYS_LIST', 'SOURCE_DATA_TYPE', 'SUBFIELD_CATEGORY_MAP', 'TRUNCATE_LENGTH', 'UPPER_BOUND', 'VALIDATION_ACTION', 'VALUE', 'VALUES'], str]]


# TrendmicroConnectorProfileCredentials

### apiSecretKey
- **Type**: <class 'str'>
- **Required**: Yes


# TrendmicroSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes


# TriggerConfig

### triggerType
- **Type**: typing.Literal['Event', 'OnDemand', 'Scheduled']
- **Required**: Yes

### triggerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.TriggerProperties]


# TriggerConfigOutput

### triggerType
- **Type**: typing.Literal['Event', 'OnDemand', 'Scheduled']
- **Required**: Yes

### triggerProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.TriggerPropertiesOutput]


# TriggerProperties

### Scheduled
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ScheduledTriggerProperties]


# TriggerPropertiesOutput

### Scheduled
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ScheduledTriggerPropertiesOutput]


# UnregisterConnectorRequest

### connectorLabel
- **Type**: <class 'str'>
- **Required**: Yes

### forceDelete
- **Type**: typing.Optional[bool]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateConnectorProfileRequest

### connectorProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### connectionMode
- **Type**: typing.Literal['Private', 'Public']
- **Required**: Yes

### connectorProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProfileConfig'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# UpdateConnectorProfileResponse

### connectorProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateConnectorRegistrationRequest

### connectorLabel
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### connectorProvisioningConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorProvisioningConfig]

### clientToken
- **Type**: typing.Optional[str]


# UpdateConnectorRegistrationResponse

### connectorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFlowRequest

### flowName
- **Type**: <class 'str'>
- **Required**: Yes

### triggerConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.TriggerConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.TriggerConfigOutput]
- **Required**: Yes

### sourceFlowConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.SourceFlowConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.SourceFlowConfigOutput]
- **Required**: Yes

### destinationFlowConfigList
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationFlowConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.DestinationFlowConfigOutput]]
- **Required**: Yes

### tasks
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.Task, aws_resource_validator.pydantic_models.appflow.appflow_classes.TaskOutput]]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### metadataCatalogConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.MetadataCatalogConfig]

### clientToken
- **Type**: typing.Optional[str]


# UpdateFlowResponse

### flowStatus
- **Type**: typing.Literal['Active', 'Deleted', 'Deprecated', 'Draft', 'Errored', 'Suspended']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.ResponseMetadata'>
- **Required**: Yes


# UpsolverDestinationProperties

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3OutputFormatConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.UpsolverS3OutputFormatConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.UpsolverS3OutputFormatConfigOutput]
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]


# UpsolverDestinationPropertiesOutput

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### s3OutputFormatConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.UpsolverS3OutputFormatConfigOutput'>
- **Required**: Yes

### bucketPrefix
- **Type**: typing.Optional[str]


# UpsolverS3OutputFormatConfig

### prefixConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.appflow.appflow_classes.PrefixConfig, aws_resource_validator.pydantic_models.appflow.appflow_classes.PrefixConfigOutput]
- **Required**: Yes

### fileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON', 'PARQUET']]

### aggregationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.AggregationConfig]


# UpsolverS3OutputFormatConfigOutput

### prefixConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.appflow.appflow_classes.PrefixConfigOutput'>
- **Required**: Yes

### fileType
- **Type**: typing.Optional[typing.Literal['CSV', 'JSON', 'PARQUET']]

### aggregationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.AggregationConfig]


# VeevaConnectorProfileCredentials

### username
- **Type**: <class 'str'>
- **Required**: Yes

### password
- **Type**: <class 'str'>
- **Required**: Yes


# VeevaConnectorProfileProperties

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# VeevaSourceProperties

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


# ZendeskConnectorProfileCredentials

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### accessToken
- **Type**: typing.Optional[str]

### oAuthRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ConnectorOAuthRequest]


# ZendeskConnectorProfileProperties

### instanceUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ZendeskDestinationProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes

### idFieldNames
- **Type**: typing.Optional[typing.List[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]


# ZendeskDestinationPropertiesOutput

### object
- **Type**: <class 'str'>
- **Required**: Yes

### idFieldNames
- **Type**: typing.Optional[typing.List[str]]

### errorHandlingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appflow.appflow_classes.ErrorHandlingConfig]

### writeOperationType
- **Type**: typing.Optional[typing.Literal['DELETE', 'INSERT', 'UPDATE', 'UPSERT']]


# ZendeskMetadata

### oAuthScopes
- **Type**: typing.Optional[typing.List[str]]


# ZendeskSourceProperties

### object
- **Type**: <class 'str'>
- **Required**: Yes



# Iot Service

### AcmCertificateArn
- **Type**: string
- **Pattern**: `arn:aws(-cn|-us-gov|-iso-b|-iso)?:acm:[a-z]{2}-(gov-|iso-|isob-)?[a-z]{4,9}-\d{1}:\d{12}:certificate/[a-zA-Z0-9/-]+`
- **Min Length**: 1
- **Max Length**: 2048

### AggregationTypeValue
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 12

### AttributeName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.,@/:#-]+`
- **Max Length**: 128

### AttributeValue
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_.,@/:#=\[\]-]*`
- **Max Length**: 800

### AuditDescription
- **Type**: string
- **Pattern**: `[\p{Graph}\x20]*`
- **Max Length**: 1000

### AuditTaskId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 40

### AuthorizerFunctionArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 2048

### AuthorizerName
- **Type**: string
- **Pattern**: `[\w=,@-]+`
- **Min Length**: 1
- **Max Length**: 128

### AwsAccountId
- **Type**: string
- **Pattern**: `[0-9]+`
- **Min Length**: 12
- **Max Length**: 12

### BehaviorName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### BillingGroupDescription
- **Type**: string
- **Pattern**: `[\p{Graph}\x20]*`
- **Max Length**: 2028

### BillingGroupId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 128

### BillingGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### CertificateId
- **Type**: string
- **Pattern**: `(0x)?[a-fA-F0-9]+`
- **Min Length**: 64
- **Max Length**: 64

### CertificatePem
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 65536

### CertificateProviderFunctionArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 2048

### CertificateProviderName
- **Type**: string
- **Pattern**: `[\w=,@-]+`
- **Min Length**: 1
- **Max Length**: 128

### CertificateSigningRequest
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 4096

### Cidr
- **Type**: string
- **Pattern**: `[a-fA-F0-9:\.\/]+`
- **Min Length**: 2
- **Max Length**: 43

### ClientCertificateCallbackArn
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 2048

### ClientRequestToken
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-_]+$`
- **Min Length**: 1
- **Max Length**: 64

### ClientToken
- **Type**: string
- **Pattern**: `\S{36,64}`
- **Min Length**: 36
- **Max Length**: 64

### CommandDescription
- **Type**: string
- **Pattern**: `[^\p{C}]*`
- **Max Length**: 2028

### CommandExecutionId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### CommandExecutionResultName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 32

### CommandId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### CommandParameterDescription
- **Type**: string
- **Pattern**: `[^\p{C}]*`
- **Max Length**: 2028

### CommandParameterName
- **Type**: string
- **Pattern**: `^[.$a-zA-Z0-9_-]+$`
- **Min Length**: 1
- **Max Length**: 192

### Comment
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Max Length**: 2028

### ConnectionAttributeName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:.]+`
- **Max Length**: 128

### ConnectivityApiThingName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### CustomMetricDisplayName
- **Type**: string
- **Pattern**: `[\p{Graph}\x20]*`
- **Max Length**: 128

### DayOfMonth
- **Type**: string
- **Pattern**: `^([1-9]|[12][0-9]|3[01])$|^LAST$`

### DetailsKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### DetailsValue
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Min Length**: 1

### DimensionName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### DisplayName
- **Type**: string
- **Pattern**: `[^\p{C}]*`
- **Max Length**: 64

### DomainConfigurationName
- **Type**: string
- **Pattern**: `[\w.-]+`
- **Min Length**: 1
- **Max Length**: 128

### DomainName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 253

### ElasticsearchEndpoint
- **Type**: string
- **Pattern**: `https?://.*`

### EndpointType
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 128

### Environment
- **Type**: string
- **Pattern**: `[^\p{C}]+`

### EvaluationStatistic
- **Type**: string
- **Pattern**: `(p0|p0\.1|p0\.01|p1|p10|p50|p90|p99|p99\.9|p99\.99|p100)`

### Example
- **Type**: string
- **Pattern**: `[^\p{C}]+`

### FindingId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 128

### FirehoseSeparator
- **Type**: string
- **Pattern**: `([\n\t])|(\r\n)|(,)`

### FleetMetricDescription
- **Type**: string
- **Pattern**: `[\p{Graph}\x20]*`
- **Max Length**: 1024

### FleetMetricName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_\-\.]+`
- **Min Length**: 1
- **Max Length**: 128

### HttpHeaderName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 8192

### HttpHeaderValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 8192

### HttpQueryString
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 4096

### IndexName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### IssuerCertificateSerialNumber
- **Type**: string
- **Pattern**: `[a-fA-F0-9:]+`
- **Max Length**: 20

### IssuerCertificateSubject
- **Type**: string
- **Pattern**: `[\p{Graph}\x20]*`
- **Max Length**: 1000

### IssuerId
- **Type**: string
- **Pattern**: `(0x)?[a-fA-F0-9]+`
- **Max Length**: 64

### JobDescription
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Max Length**: 2028

### JobId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### JobTemplateArn
- **Type**: string
- **Pattern**: `^arn:[!-~]+$`
- **Min Length**: 1
- **Max Length**: 1600

### JobTemplateId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 64

### KeyName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### KeyValue
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 5120

### ManagedTemplateVersion
- **Type**: string
- **Pattern**: `^[1-9]+.[0-9]+`

### Marker
- **Type**: string
- **Pattern**: `[A-Za-z0-9+/]+={0,2}`
- **Max Length**: 1024

### Message
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 128

### MetricName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### MitigationActionName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Max Length**: 128

### MitigationActionsTaskId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 128

### MqttClientId
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 65535

### MqttUsername
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 65535

### NamespaceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`

### OTAUpdateDescription
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Max Length**: 2028

### OTAUpdateId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 128

### PackageName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_.]+`
- **Min Length**: 1
- **Max Length**: 128

### PackageVersionArn
- **Type**: string
- **Pattern**: `^arn:[!-~]+$`
- **Min Length**: 1
- **Max Length**: 1600

### Parameter
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 2048

### ParameterKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 128

### ParameterValue
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Min Length**: 1
- **Max Length**: 30720

### PayloadVersion
- **Type**: string
- **Pattern**: `^[0-9-]+$`
- **Min Length**: 10
- **Max Length**: 32

### PolicyDocument
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 404600

### PolicyName
- **Type**: string
- **Pattern**: `[\w+=,.@-]+`
- **Min Length**: 1
- **Max Length**: 128

### PolicyVersionId
- **Type**: string
- **Pattern**: `[0-9]+`

### PrincipalId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9]+`
- **Min Length**: 1
- **Max Length**: 128

### ReasonCode
- **Type**: string
- **Pattern**: `[\p{Upper}\p{Digit}_]+`
- **Max Length**: 128

### RegistrationCode
- **Type**: string
- **Pattern**: `(0x)?[a-fA-F0-9]+`
- **Min Length**: 64
- **Max Length**: 64

### RegistryS3BucketName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9._-]+`
- **Min Length**: 3
- **Max Length**: 256

### RegistryS3KeyName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9!_.*\'()-\/]+`
- **Min Length**: 1
- **Max Length**: 1024

### ReservedDomainConfigurationName
- **Type**: string
- **Pattern**: `[\w.:-]+`
- **Min Length**: 1
- **Max Length**: 128

### Resource
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 2048

### ResourceAttributeKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1

### ResourceAttributeValue
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Min Length**: 1

### ResourceDescription
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Min Length**: 0
- **Max Length**: 1024

### RoleAlias
- **Type**: string
- **Pattern**: `[\w=,@-]+`
- **Min Length**: 1
- **Max Length**: 128

### RuleName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_]+$`
- **Min Length**: 1
- **Max Length**: 128

### SalesforceEndpoint
- **Type**: string
- **Pattern**: `https://ingestion-[a-zA-Z0-9]{1,12}\.[a-zA-Z0-9]+\.((sfdc-matrix\.net)|(sfdcnow\.com))/streams/\w{1,20}/\w{1,20}/event`
- **Max Length**: 2000

### ScheduledAuditName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 128

### SecurityPolicy
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Max Length**: 128

### SecurityProfileDescription
- **Type**: string
- **Pattern**: `[\p{Graph}\x20]*`
- **Max Length**: 1000

### SecurityProfileName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### ServerName
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 253

### ShadowName
- **Type**: string
- **Pattern**: `[$a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 64

### StatusReasonCode
- **Type**: string
- **Pattern**: `[A-Z0-9_-]+`
- **Max Length**: 64

### StatusReasonDescription
- **Type**: string
- **Pattern**: `[^\p{C}]*`
- **Max Length**: 1024

### StreamDescription
- **Type**: string
- **Pattern**: `[^\p{C}]+`
- **Max Length**: 2028

### StreamId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 128

### TagKey
- **Type**: string
- **Pattern**: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
- **Min Length**: 1
- **Max Length**: 128

### TemplateBody
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 10240

### TemplateDescription
- **Type**: string
- **Pattern**: `[^\p{C}]*`
- **Min Length**: 0
- **Max Length**: 500

### TemplateName
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_-]+$`
- **Min Length**: 1
- **Max Length**: 36

### ThingGroupDescription
- **Type**: string
- **Pattern**: `[\p{Graph}\x20]*`
- **Max Length**: 2028

### ThingGroupId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 128

### ThingGroupName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### ThingName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### ThingTypeDescription
- **Type**: string
- **Pattern**: `[\p{Graph}\x20]*`
- **Max Length**: 2028

### ThingTypeName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:_-]+`
- **Min Length**: 1
- **Max Length**: 128

### Token
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 1
- **Max Length**: 6144

### TokenKeyName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_-]+`
- **Min Length**: 1
- **Max Length**: 128

### TokenSignature
- **Type**: string
- **Pattern**: `[A-Za-z0-9+/]+={0,2}`
- **Min Length**: 1
- **Max Length**: 2560

### UnsignedLongParameterValue
- **Type**: string
- **Pattern**: `^[0-9]*$`
- **Min Length**: 1
- **Max Length**: 20

### UserPropertyKeyName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9:$.]+`
- **Max Length**: 128

### Value
- **Type**: string
- **Pattern**: `[\s\S]*`
- **Min Length**: 0
- **Max Length**: 4096

### VerificationStateDescription
- **Type**: string
- **Pattern**: `[^\p{Cntrl}]*`
- **Max Length**: 1000

### VersionName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-_.]+`
- **Min Length**: 1
- **Max Length**: 64

### ViolationId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9\-]+`
- **Min Length**: 1
- **Max Length**: 128


# Observabilityadmin Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.ResponseMetadata'>
- **Required**: Yes


# GetTelemetryEvaluationStatusForOrganizationOutput

### Status
- **Type**: typing.Literal['FAILED_START', 'FAILED_STOP', 'NOT_STARTED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.ResponseMetadata'>
- **Required**: Yes


# GetTelemetryEvaluationStatusOutput

### Status
- **Type**: typing.Literal['FAILED_START', 'FAILED_STOP', 'NOT_STARTED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.ResponseMetadata'>
- **Required**: Yes


# ListResourceTelemetryForOrganizationInput

### AccountIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdentifierPrefix
- **Type**: typing.Optional[str]

### ResourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::EC2::Instance', 'AWS::EC2::VPC', 'AWS::Lambda::Function']]]

### TelemetryConfigurationState
- **Type**: typing.Optional[typing.Dict[typing.Literal['Logs', 'Metrics', 'Traces'], typing.Literal['Disabled', 'Enabled', 'NotApplicable']]]

### ResourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceTelemetryForOrganizationInputPaginate

### AccountIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### ResourceIdentifierPrefix
- **Type**: typing.Optional[str]

### ResourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::EC2::Instance', 'AWS::EC2::VPC', 'AWS::Lambda::Function']]]

### TelemetryConfigurationState
- **Type**: typing.Optional[typing.Dict[typing.Literal['Logs', 'Metrics', 'Traces'], typing.Literal['Disabled', 'Enabled', 'NotApplicable']]]

### ResourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.PaginatorConfig]


# ListResourceTelemetryForOrganizationOutput

### TelemetryConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.TelemetryConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceTelemetryInput

### ResourceIdentifierPrefix
- **Type**: typing.Optional[str]

### ResourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::EC2::Instance', 'AWS::EC2::VPC', 'AWS::Lambda::Function']]]

### TelemetryConfigurationState
- **Type**: typing.Optional[typing.Dict[typing.Literal['Logs', 'Metrics', 'Traces'], typing.Literal['Disabled', 'Enabled', 'NotApplicable']]]

### ResourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceTelemetryInputPaginate

### ResourceIdentifierPrefix
- **Type**: typing.Optional[str]

### ResourceTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS::EC2::Instance', 'AWS::EC2::VPC', 'AWS::Lambda::Function']]]

### TelemetryConfigurationState
- **Type**: typing.Optional[typing.Dict[typing.Literal['Logs', 'Metrics', 'Traces'], typing.Literal['Disabled', 'Enabled', 'NotApplicable']]]

### ResourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.PaginatorConfig]


# ListResourceTelemetryOutput

### TelemetryConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.TelemetryConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.observabilityadmin.observabilityadmin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# TelemetryConfiguration

### AccountIdentifier
- **Type**: typing.Optional[str]

### TelemetryConfigurationState
- **Type**: typing.Optional[typing.Dict[typing.Literal['Logs', 'Metrics', 'Traces'], typing.Literal['Disabled', 'Enabled', 'NotApplicable']]]

### ResourceType
- **Type**: typing.Optional[typing.Literal['AWS::EC2::Instance', 'AWS::EC2::VPC', 'AWS::Lambda::Function']]

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ResourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LastUpdateTimeStamp
- **Type**: typing.Optional[int]



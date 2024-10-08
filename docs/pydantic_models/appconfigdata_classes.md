# Pydantic Models in appconfigdata_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetLatestConfigurationRequestRequestTypeDef

### ConfigurationToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetLatestConfigurationResponseTypeDef

### NextPollConfigurationToken
- **Type**: <class 'str'>
- **Required**: Yes

### NextPollIntervalInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfigdata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# StartConfigurationSessionRequestRequestTypeDef

### ApplicationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RequiredMinimumPollIntervalInSeconds
- **Type**: typing.Optional[int]


# StartConfigurationSessionResponseTypeDef

### InitialConfigurationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfigdata_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



# Bedrock Data Automation Runtime Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blueprint

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# DataAutomationConfiguration

### dataAutomationProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# EncryptionConfiguration

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### kmsEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventBridgeConfiguration

### eventBridgeEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# GetDataAutomationStatusRequest

### invocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataAutomationStatusResponse

### status
- **Type**: typing.Literal['ClientError', 'Created', 'InProgress', 'ServiceError', 'Success']
- **Required**: Yes

### errorType
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.OutputConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# InputConfiguration

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# InvokeDataAutomationAsyncRequest

### inputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.InputConfiguration'>
- **Required**: Yes

### outputConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.OutputConfiguration'>
- **Required**: Yes

### dataAutomationProfileArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### dataAutomationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.DataAutomationConfiguration]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.EncryptionConfiguration]

### notificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.NotificationConfiguration]

### blueprints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.Blueprint]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.Tag]]


# InvokeDataAutomationAsyncResponse

### invocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# NotificationConfiguration

### eventBridgeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.EventBridgeConfiguration'>
- **Required**: Yes


# OutputConfiguration

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


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


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation_runtime.bedrock_data_automation_runtime_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes



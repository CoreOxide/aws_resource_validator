# Workmailmessageflow Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetRawMessageContentRequestRequestTypeDef

### messageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRawMessageContentResponseTypeDef

### messageContent
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmailmessageflow_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRawMessageContentRequestRequestTypeDef

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.workmailmessageflow_classes.RawMessageContentTypeDef'>
- **Required**: Yes


# RawMessageContentTypeDef

### s3Reference
- **Type**: <class 'aws_resource_validator.pydantic_models.workmailmessageflow_classes.S3ReferenceTypeDef'>
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


# S3ReferenceTypeDef

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### objectVersion
- **Type**: typing.Optional[str]



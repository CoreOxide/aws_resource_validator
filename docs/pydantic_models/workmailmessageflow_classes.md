# Workmailmessageflow Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetRawMessageContentRequest

### messageId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRawMessageContentResponse

### messageContent
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmailmessageflow.workmailmessageflow_classes.ResponseMetadata'>
- **Required**: Yes


# PutRawMessageContentRequest

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.workmailmessageflow.workmailmessageflow_classes.RawMessageContent'>
- **Required**: Yes


# RawMessageContent

### s3Reference
- **Type**: <class 'aws_resource_validator.pydantic_models.workmailmessageflow.workmailmessageflow_classes.S3Reference'>
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


# S3Reference

### bucket
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### objectVersion
- **Type**: typing.Optional[str]



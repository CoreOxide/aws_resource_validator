# Cloudtrail Data Cloudtrail Data Classes

# AuditEvent

### eventData
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### eventDataChecksum
- **Type**: typing.Optional[str]


# AuditEventResultEntry

### eventID
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutAuditEventsRequest

### auditEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_data.cloudtrail_data_classes.AuditEvent]
- **Required**: Yes

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]


# PutAuditEventsResponse

### failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_data.cloudtrail_data_classes.ResultErrorEntry]
- **Required**: Yes

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_data.cloudtrail_data_classes.AuditEventResultEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_data.cloudtrail_data_classes.ResponseMetadata'>
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


# ResultErrorEntry

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes



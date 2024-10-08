# Pydantic Models in cloudtrail_data_classes

# AuditEventResultEntryTypeDef

### eventID
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# AuditEventTypeDef

### eventData
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### eventDataChecksum
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutAuditEventsRequestRequestTypeDef

### auditEvents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudtrail_data_classes.AuditEventTypeDef]
- **Required**: Yes

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]


# PutAuditEventsResponseTypeDef

### failed
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_data_classes.ResultErrorEntryTypeDef]
- **Required**: Yes

### successful
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudtrail_data_classes.AuditEventResultEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudtrail_data_classes.ResponseMetadataTypeDef'>
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


# ResultErrorEntryTypeDef

### errorCode
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes



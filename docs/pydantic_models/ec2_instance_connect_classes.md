# Ec2 Instance Connect Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadataTypeDef

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


# SendSSHPublicKeyRequestRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceOSUser
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKey
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZone
- **Type**: typing.Optional[str]


# SendSSHPublicKeyResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ec2_instance_connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendSerialConsoleSSHPublicKeyRequestRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKey
- **Type**: <class 'str'>
- **Required**: Yes

### SerialPort
- **Type**: typing.Optional[int]


# SendSerialConsoleSSHPublicKeyResponseTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### Success
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ec2_instance_connect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



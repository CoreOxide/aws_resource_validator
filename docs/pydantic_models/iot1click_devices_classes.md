# iot1click_devices_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClaimDevicesByClaimCodeRequestRequestTypeDef

### ClaimCode
- **Type**: <class 'str'>
- **Required**: Yes


# ClaimDevicesByClaimCodeResponseTypeDef

### ClaimCode
- **Type**: <class 'str'>
- **Required**: Yes

### Total
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDeviceRequestRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDeviceResponseTypeDef

### DeviceDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.DeviceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceDescriptionTypeDef

### Arn
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### DeviceId
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### RemainingLife
- **Type**: typing.Optional[float]

### Type
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# DeviceEventTypeDef

### Device
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_devices_classes.DeviceTypeDef]

### StdEvent
- **Type**: typing.Optional[str]


# DeviceMethodTypeDef

### DeviceType
- **Type**: typing.Optional[str]

### MethodName
- **Type**: typing.Optional[str]


# DeviceTypeDef

### Attributes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### DeviceId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FinalizeDeviceClaimRequestRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# FinalizeDeviceClaimResponseTypeDef

### State
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeviceMethodsRequestRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceMethodsResponseTypeDef

### DeviceMethods
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot1click_devices_classes.DeviceMethodTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InitiateDeviceClaimRequestRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# InitiateDeviceClaimResponseTypeDef

### State
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeDeviceMethodRequestRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceMethod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_devices_classes.DeviceMethodTypeDef]

### DeviceMethodParameters
- **Type**: typing.Optional[str]


# InvokeDeviceMethodResponseTypeDef

### DeviceMethodResponse
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeviceEventsRequestListDeviceEventsPaginateTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### FromTimeStamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTimeStamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_devices_classes.PaginatorConfigTypeDef]


# ListDeviceEventsRequestRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### FromTimeStamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTimeStamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDeviceEventsResponseTypeDef

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot1click_devices_classes.DeviceEventTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDevicesRequestListDevicesPaginateTypeDef

### DeviceType
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot1click_devices_classes.PaginatorConfigTypeDef]


# ListDevicesRequestRequestTypeDef

### DeviceType
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDevicesResponseTypeDef

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot1click_devices_classes.DeviceDescriptionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UnclaimDeviceRequestRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# UnclaimDeviceResponseTypeDef

### State
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot1click_devices_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDeviceStateRequestRequestTypeDef

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: typing.Optional[bool]



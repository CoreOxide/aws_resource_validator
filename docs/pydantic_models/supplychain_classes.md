# supplychain_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillOfMaterialsImportJobTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'NEW', 'QUEUED', 'SUCCESS']
- **Required**: Yes

### s3uri
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# CreateBillOfMaterialsImportJobRequestRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### s3uri
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateBillOfMaterialsImportJobResponseTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBillOfMaterialsImportJobRequestRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBillOfMaterialsImportJobResponseTypeDef

### job
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.BillOfMaterialsImportJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# SendDataIntegrationEventRequestRequestTypeDef

### instanceId
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: typing.Literal['scn.data.forecast', 'scn.data.inboundorder', 'scn.data.inboundorderline', 'scn.data.inboundorderlineschedule', 'scn.data.inventorylevel', 'scn.data.outboundorderline', 'scn.data.outboundshipment', 'scn.data.processheader', 'scn.data.processoperation', 'scn.data.processproduct', 'scn.data.reservation', 'scn.data.shipment', 'scn.data.shipmentstop', 'scn.data.shipmentstoporder', 'scn.data.supplyplan']
- **Required**: Yes

### data
- **Type**: <class 'str'>
- **Required**: Yes

### eventGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### eventTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### clientToken
- **Type**: typing.Optional[str]


# SendDataIntegrationEventResponseTypeDef

### eventId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.supplychain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



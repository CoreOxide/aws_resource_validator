# Pydantic Models in route53_recovery_cluster_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetRoutingControlStateRequestRequestTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoutingControlStateResponseTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControlState
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes

### RoutingControlName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoutingControlsRequestListRoutingControlsPaginateTypeDef

### ControlPanelArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.PaginatorConfigTypeDef]


# ListRoutingControlsRequestRequestTypeDef

### ControlPanelArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRoutingControlsResponseTypeDef

### RoutingControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.RoutingControlTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.ResponseMetadataTypeDef'>
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


# RoutingControlTypeDef

### ControlPanelArn
- **Type**: typing.Optional[str]

### ControlPanelName
- **Type**: typing.Optional[str]

### RoutingControlArn
- **Type**: typing.Optional[str]

### RoutingControlName
- **Type**: typing.Optional[str]

### RoutingControlState
- **Type**: typing.Optional[typing.Literal['Off', 'On']]

### Owner
- **Type**: typing.Optional[str]


# UpdateRoutingControlStateEntryTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControlState
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes


# UpdateRoutingControlStateRequestRequestTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControlState
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes

### SafetyRulesToOverride
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateRoutingControlStatesRequestRequestTypeDef

### UpdateRoutingControlStateEntries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.UpdateRoutingControlStateEntryTypeDef]
- **Required**: Yes

### SafetyRulesToOverride
- **Type**: typing.Optional[typing.Sequence[str]]


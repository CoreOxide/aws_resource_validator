# Route53 Recovery Cluster Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetRoutingControlStateRequest

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoutingControlStateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.ResponseMetadata'>
- **Required**: Yes


# ListRoutingControlsRequest

### ControlPanelArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListRoutingControlsRequestPaginate

### ControlPanelArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.PaginatorConfig]


# ListRoutingControlsResponse

### RoutingControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.RoutingControl]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# RoutingControl

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


# UpdateRoutingControlStateEntry

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControlState
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes


# UpdateRoutingControlStateRequest

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControlState
- **Type**: typing.Literal['Off', 'On']
- **Required**: Yes

### SafetyRulesToOverride
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateRoutingControlStatesRequest

### UpdateRoutingControlStateEntries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_recovery_cluster_classes.UpdateRoutingControlStateEntry]
- **Required**: Yes

### SafetyRulesToOverride
- **Type**: typing.Optional[typing.Sequence[str]]



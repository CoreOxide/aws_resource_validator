# Route53 Recovery Control Config Classes

# AssertionRule

### AssertedControls
- **Type**: typing.List[str]
- **Required**: Yes

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleConfig'>
- **Required**: Yes

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DEPLOYED', 'PENDING', 'PENDING_DELETION']
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
- **Required**: Yes

### Owner
- **Type**: typing.Optional[str]


# AssertionRuleUpdate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Cluster

### ClusterArn
- **Type**: typing.Optional[str]

### ClusterEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ClusterEndpoint]]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'PENDING', 'PENDING_DELETION']]

### Owner
- **Type**: typing.Optional[str]


# ClusterEndpoint

### Endpoint
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# ControlPanel

### ClusterArn
- **Type**: typing.Optional[str]

### ControlPanelArn
- **Type**: typing.Optional[str]

### DefaultControlPanel
- **Type**: typing.Optional[bool]

### Name
- **Type**: typing.Optional[str]

### RoutingControlCount
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'PENDING', 'PENDING_DELETION']]

### Owner
- **Type**: typing.Optional[str]


# CreateClusterRequest

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# CreateControlPanelRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ControlPanelName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateControlPanelResponse

### ControlPanel
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRoutingControlRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControlName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ControlPanelArn
- **Type**: typing.Optional[str]


# CreateRoutingControlResponse

### RoutingControl
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControl'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSafetyRuleRequest

### AssertionRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.NewAssertionRule]

### ClientToken
- **Type**: typing.Optional[str]

### GatingRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.NewGatingRule]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSafetyRuleResponse

### AssertionRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRule'>
- **Required**: Yes

### GatingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClusterRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteControlPanelRequest

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoutingControlRequest

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSafetyRuleRequest

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequest

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequestWait

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterRequestWaitExtra

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeClusterResponse

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.Cluster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeControlPanelRequest

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeControlPanelRequestWait

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeControlPanelRequestWaitExtra

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeControlPanelResponse

### ControlPanel
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRoutingControlRequest

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoutingControlRequestWait

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeRoutingControlRequestWaitExtra

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeRoutingControlResponse

### RoutingControl
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControl'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSafetyRuleRequest

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSafetyRuleResponse

### AssertionRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRule'>
- **Required**: Yes

### GatingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# GatingRule

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### GatingControls
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleConfig'>
- **Required**: Yes

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DEPLOYED', 'PENDING', 'PENDING_DELETION']
- **Required**: Yes

### TargetControls
- **Type**: typing.List[str]
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
- **Required**: Yes

### Owner
- **Type**: typing.Optional[str]


# GatingRuleUpdate

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
- **Required**: Yes


# GetResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# ListAssociatedRoute53HealthChecksRequest

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedRoute53HealthChecksRequestPaginate

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfig]


# ListAssociatedRoute53HealthChecksResponse

### HealthCheckIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfig]


# ListClustersResponse

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.Cluster]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListControlPanelsRequest

### ClusterArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListControlPanelsRequestPaginate

### ClusterArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfig]


# ListControlPanelsResponse

### ControlPanels
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingControlsRequest

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingControlsRequestPaginate

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfig]


# ListRoutingControlsResponse

### RoutingControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControl]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSafetyRulesRequest

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSafetyRulesRequestPaginate

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfig]


# ListSafetyRulesResponse

### SafetyRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.Rule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# NewAssertionRule

### AssertedControls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleConfig'>
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
- **Required**: Yes


# NewGatingRule

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### GatingControls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RuleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleConfig'>
- **Required**: Yes

### TargetControls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
- **Required**: Yes


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

### Name
- **Type**: typing.Optional[str]

### RoutingControlArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'PENDING', 'PENDING_DELETION']]

### Owner
- **Type**: typing.Optional[str]


# Rule

### ASSERTION
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRule]

### GATING
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRule]


# RuleConfig

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateControlPanelRequest

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ControlPanelName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateControlPanelResponse

### ControlPanel
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRoutingControlRequest

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControlName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoutingControlResponse

### RoutingControl
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControl'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSafetyRuleRequest

### AssertionRuleUpdate
- **Type**: <class 'NoneType'>

### GatingRuleUpdate
- **Type**: <class 'NoneType'>


# UpdateSafetyRuleResponse

### AssertionRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRule'>
- **Required**: Yes

### GatingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



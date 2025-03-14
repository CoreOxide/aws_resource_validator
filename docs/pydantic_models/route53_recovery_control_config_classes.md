# Route53 Recovery Control Config Classes

# AssertionRuleTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleConfigTypeDef'>
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


# AssertionRuleUpdateTypeDef

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

# ClusterEndpointTypeDef

### Endpoint
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# ClusterTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### ClusterEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ClusterEndpointTypeDef]]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'PENDING', 'PENDING_DELETION']]

### Owner
- **Type**: typing.Optional[str]


# ControlPanelTypeDef

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


# CreateClusterRequestTypeDef

### ClusterName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateControlPanelRequestTypeDef

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


# CreateControlPanelResponseTypeDef

### ControlPanel
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoutingControlRequestTypeDef

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


# CreateRoutingControlResponseTypeDef

### RoutingControl
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControlTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSafetyRuleRequestTypeDef

### AssertionRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.NewAssertionRuleTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### GatingRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.NewGatingRuleTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSafetyRuleResponseTypeDef

### AssertionRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRuleTypeDef'>
- **Required**: Yes

### GatingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClusterRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteControlPanelRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoutingControlRequestTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSafetyRuleRequestTypeDef

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequestWaitExtraTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeClusterRequestWaitTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeControlPanelRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeControlPanelRequestWaitExtraTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeControlPanelRequestWaitTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeControlPanelResponseTypeDef

### ControlPanel
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRoutingControlRequestTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoutingControlRequestWaitExtraTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeRoutingControlRequestWaitTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeRoutingControlResponseTypeDef

### RoutingControl
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControlTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSafetyRuleRequestTypeDef

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSafetyRuleResponseTypeDef

### AssertionRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRuleTypeDef'>
- **Required**: Yes

### GatingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GatingRuleTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleConfigTypeDef'>
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


# GatingRuleUpdateTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
- **Required**: Yes


# GetResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssociatedRoute53HealthChecksRequestPaginateTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListAssociatedRoute53HealthChecksRequestTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAssociatedRoute53HealthChecksResponseTypeDef

### HealthCheckIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListClustersRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListClustersRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersResponseTypeDef

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ClusterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListControlPanelsRequestPaginateTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListControlPanelsRequestTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListControlPanelsResponseTypeDef

### ControlPanels
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingControlsRequestPaginateTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListRoutingControlsRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingControlsResponseTypeDef

### RoutingControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControlTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSafetyRulesRequestPaginateTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListSafetyRulesRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSafetyRulesResponseTypeDef

### SafetyRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NewAssertionRuleTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleConfigTypeDef'>
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
- **Required**: Yes


# NewGatingRuleTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleConfigTypeDef'>
- **Required**: Yes

### TargetControls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### WaitPeriodMs
- **Type**: <class 'int'>
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


# RoutingControlTypeDef

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


# RuleConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleTypeDef

### ASSERTION
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRuleTypeDef]

### GATING
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRuleTypeDef]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateControlPanelRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ControlPanelName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateControlPanelResponseTypeDef

### ControlPanel
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRoutingControlRequestTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControlName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoutingControlResponseTypeDef

### RoutingControl
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControlTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSafetyRuleRequestTypeDef

### AssertionRuleUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRuleUpdateTypeDef]

### GatingRuleUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRuleUpdateTypeDef]


# UpdateSafetyRuleResponseTypeDef

### AssertionRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRuleTypeDef'>
- **Required**: Yes

### GatingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



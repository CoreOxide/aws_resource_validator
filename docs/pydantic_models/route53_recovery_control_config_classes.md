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


# CreateClusterRequestRequestTypeDef

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


# CreateControlPanelRequestRequestTypeDef

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


# CreateRoutingControlRequestRequestTypeDef

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


# CreateSafetyRuleRequestRequestTypeDef

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


# DeleteClusterRequestRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteControlPanelRequestRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoutingControlRequestRequestTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSafetyRuleRequestRequestTypeDef

### SafetyRuleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterRequestClusterCreatedWaitTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeClusterRequestClusterDeletedWaitTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeClusterRequestRequestTypeDef

### ClusterArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClusterResponseTypeDef

### Cluster
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ClusterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeControlPanelRequestControlPanelCreatedWaitTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeControlPanelRequestControlPanelDeletedWaitTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeControlPanelRequestRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeControlPanelResponseTypeDef

### ControlPanel
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ControlPanelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRoutingControlRequestRequestTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeRoutingControlRequestRoutingControlCreatedWaitTypeDef

### RoutingControlArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.WaiterConfigTypeDef]


# DescribeRoutingControlRequestRoutingControlDeletedWaitTypeDef

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


# DescribeSafetyRuleRequestRequestTypeDef

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


# GetResourcePolicyRequestRequestTypeDef

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


# ListAssociatedRoute53HealthChecksRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListClustersRequestListClustersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListClustersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListClustersResponseTypeDef

### Clusters
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ClusterTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListControlPanelsRequestListControlPanelsPaginateTypeDef

### ClusterArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListControlPanelsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoutingControlsRequestListRoutingControlsPaginateTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListRoutingControlsRequestRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRoutingControlsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingControls
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RoutingControlTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSafetyRulesRequestListSafetyRulesPaginateTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.PaginatorConfigTypeDef]


# ListSafetyRulesRequestRequestTypeDef

### ControlPanelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSafetyRulesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### SafetyRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.RuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.ResponseMetadataTypeDef'>
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

### Name
- **Type**: typing.Optional[str]

### RoutingControlArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DEPLOYED', 'PENDING', 'PENDING_DELETION']]

### Owner
- **Type**: typing.Optional[str]


# RuleConfigTypeDef

### Inverted
- **Type**: <class 'bool'>
- **Required**: Yes

### Threshold
- **Type**: <class 'int'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AND', 'ATLEAST', 'OR']
- **Required**: Yes


# RuleTypeDef

### ASSERTION
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.AssertionRuleTypeDef]

### GATING
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_recovery_control_config_classes.GatingRuleTypeDef]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateControlPanelRequestRequestTypeDef

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


# UpdateRoutingControlRequestRequestTypeDef

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


# UpdateSafetyRuleRequestRequestTypeDef

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



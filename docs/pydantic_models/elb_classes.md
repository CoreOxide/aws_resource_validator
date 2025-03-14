# Elb Classes

# AccessLogTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### S3BucketName
- **Type**: typing.Optional[str]

### EmitInterval
- **Type**: typing.Optional[int]

### S3BucketPrefix
- **Type**: typing.Optional[str]


# AddAvailabilityZonesInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AddAvailabilityZonesOutputTypeDef

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddTagsInputTypeDef

### LoadBalancerNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.TagTypeDef]
- **Required**: Yes


# AdditionalAttributeTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AppCookieStickinessPolicyTypeDef

### PolicyName
- **Type**: typing.Optional[str]

### CookieName
- **Type**: typing.Optional[str]


# ApplySecurityGroupsToLoadBalancerInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ApplySecurityGroupsToLoadBalancerOutputTypeDef

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachLoadBalancerToSubnetsInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AttachLoadBalancerToSubnetsOutputTypeDef

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BackendServerDescriptionTypeDef

### InstancePort
- **Type**: typing.Optional[int]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigureHealthCheckInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.HealthCheckTypeDef'>
- **Required**: Yes


# ConfigureHealthCheckOutputTypeDef

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.HealthCheckTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConnectionDrainingTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Timeout
- **Type**: typing.Optional[int]


# ConnectionSettingsTypeDef

### IdleTimeout
- **Type**: <class 'int'>
- **Required**: Yes


# CreateAccessPointInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Listeners
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.ListenerTypeDef]
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### Scheme
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.TagTypeDef]]


# CreateAccessPointOutputTypeDef

### DNSName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppCookieStickinessPolicyInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### CookieName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateLBCookieStickinessPolicyInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### CookieExpirationPeriod
- **Type**: typing.Optional[int]


# CreateLoadBalancerListenerInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Listeners
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.ListenerTypeDef]
- **Required**: Yes


# CreateLoadBalancerPolicyInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyTypeName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.PolicyAttributeTypeDef]]


# CrossZoneLoadBalancingTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteAccessPointInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoadBalancerListenerInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerPorts
- **Type**: typing.Sequence[int]
- **Required**: Yes


# DeleteLoadBalancerPolicyInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterEndPointsInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]
- **Required**: Yes


# DeregisterEndPointsOutputTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccessPointsInputPaginateTypeDef

### LoadBalancerNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.PaginatorConfigTypeDef]


# DescribeAccessPointsInputTypeDef

### LoadBalancerNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeAccessPointsOutputTypeDef

### LoadBalancerDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb_classes.LoadBalancerDescriptionTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountLimitsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.PaginatorConfigTypeDef]


# DescribeAccountLimitsInputTypeDef

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeAccountLimitsOutputTypeDef

### Limits
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb_classes.LimitTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndPointStateInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]]


# DescribeEndPointStateInputWaitExtraExtraTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.WaiterConfigTypeDef]


# DescribeEndPointStateInputWaitExtraTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.WaiterConfigTypeDef]


# DescribeEndPointStateInputWaitTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.WaiterConfigTypeDef]


# DescribeEndPointStateOutputTypeDef

### InstanceStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb_classes.InstanceStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoadBalancerAttributesInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoadBalancerAttributesOutputTypeDef

### LoadBalancerAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.LoadBalancerAttributesOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoadBalancerPoliciesInputTypeDef

### LoadBalancerName
- **Type**: typing.Optional[str]

### PolicyNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeLoadBalancerPoliciesOutputTypeDef

### PolicyDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb_classes.PolicyDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoadBalancerPolicyTypesInputTypeDef

### PolicyTypeNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeLoadBalancerPolicyTypesOutputTypeDef

### PolicyTypeDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb_classes.PolicyTypeDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTagsInputTypeDef

### LoadBalancerNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTagsOutputTypeDef

### TagDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb_classes.TagDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachLoadBalancerFromSubnetsInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DetachLoadBalancerFromSubnetsOutputTypeDef

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HealthCheckTypeDef

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### Interval
- **Type**: <class 'int'>
- **Required**: Yes

### Timeout
- **Type**: <class 'int'>
- **Required**: Yes

### UnhealthyThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### HealthyThreshold
- **Type**: <class 'int'>
- **Required**: Yes


# InstanceStateTypeDef

### InstanceId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### ReasonCode
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# InstanceTypeDef

### InstanceId
- **Type**: typing.Optional[str]


# LBCookieStickinessPolicyTypeDef

### PolicyName
- **Type**: typing.Optional[str]

### CookieExpirationPeriod
- **Type**: typing.Optional[int]


# LimitTypeDef

### Name
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[str]


# ListenerDescriptionTypeDef

### Listener
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.ListenerTypeDef]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# ListenerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoadBalancerAttributesOutputTypeDef

### CrossZoneLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.CrossZoneLoadBalancingTypeDef]

### AccessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.AccessLogTypeDef]

### ConnectionDraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.ConnectionDrainingTypeDef]

### ConnectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.ConnectionSettingsTypeDef]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.AdditionalAttributeTypeDef]]


# LoadBalancerAttributesTypeDef

### CrossZoneLoadBalancing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.CrossZoneLoadBalancingTypeDef]

### AccessLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.AccessLogTypeDef]

### ConnectionDraining
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.ConnectionDrainingTypeDef]

### ConnectionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.ConnectionSettingsTypeDef]

### AdditionalAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.AdditionalAttributeTypeDef]]


# LoadBalancerAttributesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoadBalancerDescriptionTypeDef

### LoadBalancerName
- **Type**: typing.Optional[str]

### DNSName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneNameID
- **Type**: typing.Optional[str]

### ListenerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.ListenerDescriptionTypeDef]]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.PoliciesTypeDef]

### BackendServerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.BackendServerDescriptionTypeDef]]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### VPCId
- **Type**: typing.Optional[str]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]]

### HealthCheck
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.HealthCheckTypeDef]

### SourceSecurityGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb_classes.SourceSecurityGroupTypeDef]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Scheme
- **Type**: typing.Optional[str]


# ModifyLoadBalancerAttributesInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.LoadBalancerAttributesUnionTypeDef'>
- **Required**: Yes


# ModifyLoadBalancerAttributesOutputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.LoadBalancerAttributesOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PoliciesTypeDef

### AppCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.AppCookieStickinessPolicyTypeDef]]

### LBCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.LBCookieStickinessPolicyTypeDef]]

### OtherPolicies
- **Type**: typing.Optional[typing.List[str]]


# PolicyAttributeDescriptionTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValue
- **Type**: typing.Optional[str]


# PolicyAttributeTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValue
- **Type**: typing.Optional[str]


# PolicyAttributeTypeDescriptionTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### AttributeType
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### Cardinality
- **Type**: typing.Optional[str]


# PolicyDescriptionTypeDef

### PolicyName
- **Type**: typing.Optional[str]

### PolicyTypeName
- **Type**: typing.Optional[str]

### PolicyAttributeDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.PolicyAttributeDescriptionTypeDef]]


# PolicyTypeDescriptionTypeDef

### PolicyTypeName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PolicyAttributeTypeDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.PolicyAttributeTypeDescriptionTypeDef]]


# RegisterEndPointsInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]
- **Required**: Yes


# RegisterEndPointsOutputTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb_classes.InstanceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveAvailabilityZonesInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveAvailabilityZonesOutputTypeDef

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsInputTypeDef

### LoadBalancerNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elb_classes.TagKeyOnlyTypeDef]
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


# SetLoadBalancerListenerSSLCertificateInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerPort
- **Type**: <class 'int'>
- **Required**: Yes

### SSLCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# SetLoadBalancerPoliciesForBackendServerInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### InstancePort
- **Type**: <class 'int'>
- **Required**: Yes

### PolicyNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SetLoadBalancerPoliciesOfListenerInputTypeDef

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerPort
- **Type**: <class 'int'>
- **Required**: Yes

### PolicyNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SourceSecurityGroupTypeDef

### OwnerAlias
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# TagDescriptionTypeDef

### LoadBalancerName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb_classes.TagTypeDef]]


# TagKeyOnlyTypeDef

### Key
- **Type**: typing.Optional[str]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



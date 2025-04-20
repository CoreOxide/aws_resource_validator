# Elb Elb Classes

# AccessLog

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### S3BucketName
- **Type**: typing.Optional[str]

### EmitInterval
- **Type**: typing.Optional[int]

### S3BucketPrefix
- **Type**: typing.Optional[str]


# AddAvailabilityZonesInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes


# AddAvailabilityZonesOutput

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsInput

### LoadBalancerNames
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Tag]
- **Required**: Yes


# AdditionalAttribute

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# AppCookieStickinessPolicy

### PolicyName
- **Type**: typing.Optional[str]

### CookieName
- **Type**: typing.Optional[str]


# ApplySecurityGroupsToLoadBalancerInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes


# ApplySecurityGroupsToLoadBalancerOutput

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# AttachLoadBalancerToSubnetsInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# AttachLoadBalancerToSubnetsOutput

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# BackendServerDescription

### InstancePort
- **Type**: typing.Optional[int]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigureHealthCheckInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.HealthCheck'>
- **Required**: Yes


# ConfigureHealthCheckOutput

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.HealthCheck'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# ConnectionDraining

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Timeout
- **Type**: typing.Optional[int]


# ConnectionSettings

### IdleTimeout
- **Type**: <class 'int'>
- **Required**: Yes


# CreateAccessPointInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Listener]
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Scheme
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Tag]]


# CreateAccessPointOutput

### DNSName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppCookieStickinessPolicyInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### CookieName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateLBCookieStickinessPolicyInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### CookieExpirationPeriod
- **Type**: typing.Optional[int]


# CreateLoadBalancerListenerInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Listener]
- **Required**: Yes


# CreateLoadBalancerPolicyInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.PolicyAttribute]]


# CrossZoneLoadBalancing

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# DeleteAccessPointInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoadBalancerListenerInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerPorts
- **Type**: typing.List[int]
- **Required**: Yes


# DeleteLoadBalancerPolicyInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterEndPointsInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]
- **Required**: Yes


# DeregisterEndPointsOutput

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccessPointsInput

### LoadBalancerNames
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeAccessPointsInputPaginate

### LoadBalancerNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb.elb_classes.PaginatorConfig]


# DescribeAccessPointsOutput

### LoadBalancerDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.LoadBalancerDescription]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountLimitsInput

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeAccountLimitsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elb.elb_classes.PaginatorConfig]


# DescribeAccountLimitsOutput

### Limits
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Limit]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndPointStateInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]]


# DescribeEndPointStateInputWait

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEndPointStateInputWaitExtra

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEndPointStateInputWaitExtraExtra

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeEndPointStateOutput

### InstanceStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.InstanceState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoadBalancerAttributesInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoadBalancerAttributesOutput

### LoadBalancerAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.LoadBalancerAttributesOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoadBalancerPoliciesInput

### LoadBalancerName
- **Type**: typing.Optional[str]

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# DescribeLoadBalancerPoliciesOutput

### PolicyDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.PolicyDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoadBalancerPolicyTypesInput

### PolicyTypeNames
- **Type**: typing.Optional[typing.List[str]]


# DescribeLoadBalancerPolicyTypesOutput

### PolicyTypeDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.PolicyTypeDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTagsInput

### LoadBalancerNames
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeTagsOutput

### TagDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.TagDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# DetachLoadBalancerFromSubnetsInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# DetachLoadBalancerFromSubnetsOutput

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# HealthCheck

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


# Instance

### InstanceId
- **Type**: typing.Optional[str]


# InstanceState

### InstanceId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### ReasonCode
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# LBCookieStickinessPolicy

### PolicyName
- **Type**: typing.Optional[str]

### CookieExpirationPeriod
- **Type**: typing.Optional[int]


# Limit

### Name
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[str]


# Listener

### Protocol
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerPort
- **Type**: <class 'int'>
- **Required**: Yes

### InstancePort
- **Type**: <class 'int'>
- **Required**: Yes

### InstanceProtocol
- **Type**: typing.Optional[str]

### SSLCertificateId
- **Type**: typing.Optional[str]


# ListenerDescription

### Listener
- **Type**: <class 'NoneType'>

### PolicyNames
- **Type**: typing.Optional[typing.List[str]]


# LoadBalancerAttributes

### CrossZoneLoadBalancing
- **Type**: <class 'NoneType'>

### AccessLog
- **Type**: <class 'NoneType'>

### ConnectionDraining
- **Type**: <class 'NoneType'>

### ConnectionSettings
- **Type**: <class 'NoneType'>

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.AdditionalAttribute]]


# LoadBalancerAttributesOutput

### CrossZoneLoadBalancing
- **Type**: <class 'NoneType'>

### AccessLog
- **Type**: <class 'NoneType'>

### ConnectionDraining
- **Type**: <class 'NoneType'>

### ConnectionSettings
- **Type**: <class 'NoneType'>

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.AdditionalAttribute]]


# LoadBalancerDescription

### LoadBalancerName
- **Type**: typing.Optional[str]

### DNSName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneNameID
- **Type**: typing.Optional[str]

### ListenerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.ListenerDescription]]

### Policies
- **Type**: <class 'NoneType'>

### BackendServerDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.BackendServerDescription]]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### VPCId
- **Type**: typing.Optional[str]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]]

### HealthCheck
- **Type**: <class 'NoneType'>

### SourceSecurityGroup
- **Type**: <class 'NoneType'>

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### Scheme
- **Type**: typing.Optional[str]


# ModifyLoadBalancerAttributesInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerAttributes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elb.elb_classes.LoadBalancerAttributes, aws_resource_validator.pydantic_models.elb.elb_classes.LoadBalancerAttributesOutput]
- **Required**: Yes


# ModifyLoadBalancerAttributesOutput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.LoadBalancerAttributesOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Policies

### AppCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.AppCookieStickinessPolicy]]

### LBCookieStickinessPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.LBCookieStickinessPolicy]]

### OtherPolicies
- **Type**: typing.Optional[typing.List[str]]


# PolicyAttribute

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValue
- **Type**: typing.Optional[str]


# PolicyAttributeDescription

### AttributeName
- **Type**: typing.Optional[str]

### AttributeValue
- **Type**: typing.Optional[str]


# PolicyAttributeTypeDescription

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


# PolicyDescription

### PolicyName
- **Type**: typing.Optional[str]

### PolicyTypeName
- **Type**: typing.Optional[str]

### PolicyAttributeDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.PolicyAttributeDescription]]


# PolicyTypeDescription

### PolicyTypeName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PolicyAttributeTypeDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.PolicyAttributeTypeDescription]]


# RegisterEndPointsInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]
- **Required**: Yes


# RegisterEndPointsOutput

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Instance]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveAvailabilityZonesInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes


# RemoveAvailabilityZonesOutput

### AvailabilityZones
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elb.elb_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsInput

### LoadBalancerNames
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.TagKeyOnly]
- **Required**: Yes


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


# SetLoadBalancerListenerSSLCertificateInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerPort
- **Type**: <class 'int'>
- **Required**: Yes

### SSLCertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# SetLoadBalancerPoliciesForBackendServerInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### InstancePort
- **Type**: <class 'int'>
- **Required**: Yes

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes


# SetLoadBalancerPoliciesOfListenerInput

### LoadBalancerName
- **Type**: <class 'str'>
- **Required**: Yes

### LoadBalancerPort
- **Type**: <class 'int'>
- **Required**: Yes

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes


# SourceSecurityGroup

### OwnerAlias
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagDescription

### LoadBalancerName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elb.elb_classes.Tag]]


# TagKeyOnly

### Key
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



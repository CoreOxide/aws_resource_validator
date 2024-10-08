# Pydantic Models in elbv2_classes

# ActionExtraOutputTypeDef

### Type
- **Type**: typing.Literal['authenticate-cognito', 'authenticate-oidc', 'fixed-response', 'forward', 'redirect']
- **Required**: Yes

### TargetGroupArn
- **Type**: typing.Optional[str]

### AuthenticateOidcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AuthenticateOidcActionConfigExtraOutputTypeDef]

### AuthenticateCognitoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AuthenticateCognitoActionConfigExtraOutputTypeDef]

### Order
- **Type**: typing.Optional[int]

### RedirectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.RedirectActionConfigTypeDef]

### FixedResponseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.FixedResponseActionConfigTypeDef]

### ForwardConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.ForwardActionConfigExtraOutputTypeDef]


# ActionOutputTypeDef

### Type
- **Type**: typing.Literal['authenticate-cognito', 'authenticate-oidc', 'fixed-response', 'forward', 'redirect']
- **Required**: Yes

### TargetGroupArn
- **Type**: typing.Optional[str]

### AuthenticateOidcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AuthenticateOidcActionConfigOutputTypeDef]

### AuthenticateCognitoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AuthenticateCognitoActionConfigOutputTypeDef]

### Order
- **Type**: typing.Optional[int]

### RedirectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.RedirectActionConfigTypeDef]

### FixedResponseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.FixedResponseActionConfigTypeDef]

### ForwardConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.ForwardActionConfigOutputTypeDef]


# ActionTypeDef

### Type
- **Type**: typing.Literal['authenticate-cognito', 'authenticate-oidc', 'fixed-response', 'forward', 'redirect']
- **Required**: Yes

### TargetGroupArn
- **Type**: typing.Optional[str]

### AuthenticateOidcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AuthenticateOidcActionConfigTypeDef]

### AuthenticateCognitoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AuthenticateCognitoActionConfigTypeDef]

### Order
- **Type**: typing.Optional[int]

### RedirectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.RedirectActionConfigTypeDef]

### FixedResponseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.FixedResponseActionConfigTypeDef]

### ForwardConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.ForwardActionConfigTypeDef]


# AddListenerCertificatesInputRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.CertificateTypeDef]
- **Required**: Yes


# AddListenerCertificatesOutputTypeDef

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.CertificateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddTagsInputRequestTypeDef

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TagTypeDef]
- **Required**: Yes


# AddTrustStoreRevocationsInputRequestTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationContents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.RevocationContentTypeDef]]


# AddTrustStoreRevocationsOutputTypeDef

### TrustStoreRevocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStoreRevocationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AnomalyDetectionTypeDef

### Result
- **Type**: typing.Optional[typing.Literal['anomalous', 'normal']]

### MitigationInEffect
- **Type**: typing.Optional[typing.Literal['no', 'yes']]


# AuthenticateCognitoActionConfigExtraOutputTypeDef

### UserPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolClientId
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolDomain
- **Type**: <class 'str'>
- **Required**: Yes

### SessionCookieName
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SessionTimeout
- **Type**: typing.Optional[int]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Dict[str, str]]

### OnUnauthenticatedRequest
- **Type**: typing.Optional[typing.Literal['allow', 'authenticate', 'deny']]


# AuthenticateCognitoActionConfigOutputTypeDef

### UserPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolClientId
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolDomain
- **Type**: <class 'str'>
- **Required**: Yes

### SessionCookieName
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SessionTimeout
- **Type**: typing.Optional[int]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Dict[str, str]]

### OnUnauthenticatedRequest
- **Type**: typing.Optional[typing.Literal['allow', 'authenticate', 'deny']]


# AuthenticateCognitoActionConfigTypeDef

### UserPoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolClientId
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolDomain
- **Type**: <class 'str'>
- **Required**: Yes

### SessionCookieName
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SessionTimeout
- **Type**: typing.Optional[int]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OnUnauthenticatedRequest
- **Type**: typing.Optional[typing.Literal['allow', 'authenticate', 'deny']]


# AuthenticateOidcActionConfigExtraOutputTypeDef

### Issuer
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### TokenEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### UserInfoEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: typing.Optional[str]

### SessionCookieName
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SessionTimeout
- **Type**: typing.Optional[int]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Dict[str, str]]

### OnUnauthenticatedRequest
- **Type**: typing.Optional[typing.Literal['allow', 'authenticate', 'deny']]

### UseExistingClientSecret
- **Type**: typing.Optional[bool]


# AuthenticateOidcActionConfigOutputTypeDef

### Issuer
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### TokenEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### UserInfoEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: typing.Optional[str]

### SessionCookieName
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SessionTimeout
- **Type**: typing.Optional[int]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Dict[str, str]]

### OnUnauthenticatedRequest
- **Type**: typing.Optional[typing.Literal['allow', 'authenticate', 'deny']]

### UseExistingClientSecret
- **Type**: typing.Optional[bool]


# AuthenticateOidcActionConfigTypeDef

### Issuer
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### TokenEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### UserInfoEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: typing.Optional[str]

### SessionCookieName
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[str]

### SessionTimeout
- **Type**: typing.Optional[int]

### AuthenticationRequestExtraParams
- **Type**: typing.Optional[typing.Mapping[str, str]]

### OnUnauthenticatedRequest
- **Type**: typing.Optional[typing.Literal['allow', 'authenticate', 'deny']]

### UseExistingClientSecret
- **Type**: typing.Optional[bool]


# AvailabilityZoneTypeDef

### ZoneName
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### OutpostId
- **Type**: typing.Optional[str]

### LoadBalancerAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerAddressTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateTypeDef

### CertificateArn
- **Type**: typing.Optional[str]

### IsDefault
- **Type**: typing.Optional[bool]


# CipherTypeDef

### Name
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]


# CreateListenerInputRequestTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultActions
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.elbv2_classes.ActionTypeDef, aws_resource_validator.pydantic_models.elbv2_classes.ActionExtraOutputTypeDef]]
- **Required**: Yes

### Protocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### Port
- **Type**: typing.Optional[int]

### SslPolicy
- **Type**: typing.Optional[str]

### Certificates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.CertificateTypeDef]]

### AlpnPolicy
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TagTypeDef]]

### MutualAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.MutualAuthenticationAttributesTypeDef]


# CreateListenerOutputTypeDef

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoadBalancerInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.SubnetMappingTypeDef]]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### Scheme
- **Type**: typing.Optional[typing.Literal['internal', 'internet-facing']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TagTypeDef]]

### Type
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']]

### CustomerOwnedIpv4Pool
- **Type**: typing.Optional[str]


# CreateLoadBalancerOutputTypeDef

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleInputRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Conditions
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionTypeDef, aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionExtraOutputTypeDef]]
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.elbv2_classes.ActionTypeDef, aws_resource_validator.pydantic_models.elbv2_classes.ActionExtraOutputTypeDef]]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TagTypeDef]]


# CreateRuleOutputTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.RuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTargetGroupInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### ProtocolVersion
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### HealthCheckProtocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### HealthCheckPort
- **Type**: typing.Optional[str]

### HealthCheckEnabled
- **Type**: typing.Optional[bool]

### HealthCheckPath
- **Type**: typing.Optional[str]

### HealthCheckIntervalSeconds
- **Type**: typing.Optional[int]

### HealthCheckTimeoutSeconds
- **Type**: typing.Optional[int]

### HealthyThresholdCount
- **Type**: typing.Optional[int]

### UnhealthyThresholdCount
- **Type**: typing.Optional[int]

### Matcher
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.MatcherTypeDef]

### TargetType
- **Type**: typing.Optional[typing.Literal['alb', 'instance', 'ip', 'lambda']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TagTypeDef]]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# CreateTargetGroupOutputTypeDef

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrustStoreInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CaCertificatesBundleS3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### CaCertificatesBundleS3Key
- **Type**: <class 'str'>
- **Required**: Yes

### CaCertificatesBundleS3ObjectVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TagTypeDef]]


# CreateTrustStoreOutputTypeDef

### TrustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStoreTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteListenerInputRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoadBalancerInputRequestTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleInputRequestTypeDef

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetGroupInputRequestTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustStoreInputRequestTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTargetsInputRequestTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]
- **Required**: Yes


# DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeAccountLimitsInputRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeAccountLimitsOutputTypeDef

### Limits
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LimitTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeListenerCertificatesInputDescribeListenerCertificatesPaginateTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeListenerCertificatesInputRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeListenerCertificatesOutputTypeDef

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.CertificateTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeListenersInputDescribeListenersPaginateTypeDef

### LoadBalancerArn
- **Type**: typing.Optional[str]

### ListenerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeListenersInputRequestTypeDef

### LoadBalancerArn
- **Type**: typing.Optional[str]

### ListenerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeListenersOutputTypeDef

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoadBalancerAttributesInputRequestTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoadBalancerAttributesOutputTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLoadBalancersInputDescribeLoadBalancersPaginateTypeDef

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeLoadBalancersInputLoadBalancerAvailableWaitTypeDef

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.WaiterConfigTypeDef]


# DescribeLoadBalancersInputLoadBalancerExistsWaitTypeDef

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.WaiterConfigTypeDef]


# DescribeLoadBalancersInputLoadBalancersDeletedWaitTypeDef

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.WaiterConfigTypeDef]


# DescribeLoadBalancersInputRequestTypeDef

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeLoadBalancersOutputTypeDef

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRulesInputDescribeRulesPaginateTypeDef

### ListenerArn
- **Type**: typing.Optional[str]

### RuleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeRulesInputRequestTypeDef

### ListenerArn
- **Type**: typing.Optional[str]

### RuleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeRulesOutputTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.RuleTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSSLPoliciesInputDescribeSSLPoliciesPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### LoadBalancerType
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeSSLPoliciesInputRequestTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### LoadBalancerType
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]


# DescribeSSLPoliciesOutputTypeDef

### SslPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.SslPolicyTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTagsInputRequestTypeDef

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTagsOutputTypeDef

### TagDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TagDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTargetGroupAttributesInputRequestTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTargetGroupAttributesOutputTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTargetGroupsInputDescribeTargetGroupsPaginateTypeDef

### LoadBalancerArn
- **Type**: typing.Optional[str]

### TargetGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeTargetGroupsInputRequestTypeDef

### LoadBalancerArn
- **Type**: typing.Optional[str]

### TargetGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTargetGroupsOutputTypeDef

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTargetHealthInputRequestTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]]

### Include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'AnomalyDetection']]]


# DescribeTargetHealthInputTargetDeregisteredWaitTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]]

### Include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'AnomalyDetection']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.WaiterConfigTypeDef]


# DescribeTargetHealthInputTargetInServiceWaitTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]]

### Include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'AnomalyDetection']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.WaiterConfigTypeDef]


# DescribeTargetHealthOutputTypeDef

### TargetHealthDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetHealthDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrustStoreAssociationsInputRequestTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTrustStoreAssociationsOutputTypeDef

### TrustStoreAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStoreAssociationTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrustStoreRevocationTypeDef

### TrustStoreArn
- **Type**: typing.Optional[str]

### RevocationId
- **Type**: typing.Optional[int]

### RevocationType
- **Type**: typing.Optional[typing.Literal['CRL']]

### NumberOfRevokedEntries
- **Type**: typing.Optional[int]


# DescribeTrustStoreRevocationsInputRequestTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationIds
- **Type**: typing.Optional[typing.Sequence[int]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTrustStoreRevocationsOutputTypeDef

### TrustStoreRevocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.DescribeTrustStoreRevocationTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrustStoresInputRequestTypeDef

### TrustStoreArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTrustStoresOutputTypeDef

### TrustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStoreTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FixedResponseActionConfigTypeDef

### StatusCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageBody
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]


# ForwardActionConfigExtraOutputTypeDef

### TargetGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTupleTypeDef]]

### TargetGroupStickinessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupStickinessConfigTypeDef]


# ForwardActionConfigOutputTypeDef

### TargetGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTupleTypeDef]]

### TargetGroupStickinessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupStickinessConfigTypeDef]


# ForwardActionConfigTypeDef

### TargetGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTupleTypeDef]]

### TargetGroupStickinessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupStickinessConfigTypeDef]


# GetTrustStoreCaCertificatesBundleInputRequestTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrustStoreCaCertificatesBundleOutputTypeDef

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrustStoreRevocationContentInputRequestTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationId
- **Type**: <class 'int'>
- **Required**: Yes


# GetTrustStoreRevocationContentOutputTypeDef

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HostHeaderConditionConfigExtraOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# HostHeaderConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# HostHeaderConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# HttpHeaderConditionConfigExtraOutputTypeDef

### HttpHeaderName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpHeaderConditionConfigOutputTypeDef

### HttpHeaderName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpHeaderConditionConfigTypeDef

### HttpHeaderName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# HttpRequestMethodConditionConfigExtraOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpRequestMethodConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpRequestMethodConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# LimitTypeDef

### Name
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[str]


# ListenerTypeDef

### ListenerArn
- **Type**: typing.Optional[str]

### LoadBalancerArn
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### Certificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.CertificateTypeDef]]

### SslPolicy
- **Type**: typing.Optional[str]

### DefaultActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ActionOutputTypeDef]]

### AlpnPolicy
- **Type**: typing.Optional[typing.List[str]]

### MutualAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.MutualAuthenticationAttributesTypeDef]


# LoadBalancerAddressTypeDef

### IpAddress
- **Type**: typing.Optional[str]

### AllocationId
- **Type**: typing.Optional[str]

### PrivateIPv4Address
- **Type**: typing.Optional[str]

### IPv6Address
- **Type**: typing.Optional[str]


# LoadBalancerAttributeTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# LoadBalancerStateTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['active', 'active_impaired', 'failed', 'provisioning']]

### Reason
- **Type**: typing.Optional[str]


# LoadBalancerTypeDef

### LoadBalancerArn
- **Type**: typing.Optional[str]

### DNSName
- **Type**: typing.Optional[str]

### CanonicalHostedZoneId
- **Type**: typing.Optional[str]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]

### LoadBalancerName
- **Type**: typing.Optional[str]

### Scheme
- **Type**: typing.Optional[typing.Literal['internal', 'internet-facing']]

### VpcId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerStateTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.AvailabilityZoneTypeDef]]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']]

### CustomerOwnedIpv4Pool
- **Type**: typing.Optional[str]

### EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic
- **Type**: typing.Optional[str]


# MatcherTypeDef

### HttpCode
- **Type**: typing.Optional[str]

### GrpcCode
- **Type**: typing.Optional[str]


# ModifyListenerInputRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### SslPolicy
- **Type**: typing.Optional[str]

### Certificates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.CertificateTypeDef]]

### DefaultActions
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.elbv2_classes.ActionTypeDef, aws_resource_validator.pydantic_models.elbv2_classes.ActionExtraOutputTypeDef]]]

### AlpnPolicy
- **Type**: typing.Optional[typing.Sequence[str]]

### MutualAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.MutualAuthenticationAttributesTypeDef]


# ModifyListenerOutputTypeDef

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyLoadBalancerAttributesInputRequestTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerAttributeTypeDef]
- **Required**: Yes


# ModifyLoadBalancerAttributesOutputTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyRuleInputRequestTypeDef

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionTypeDef, aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionExtraOutputTypeDef]]]

### Actions
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.elbv2_classes.ActionTypeDef, aws_resource_validator.pydantic_models.elbv2_classes.ActionExtraOutputTypeDef]]]


# ModifyRuleOutputTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.RuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyTargetGroupAttributesInputRequestTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupAttributeTypeDef]
- **Required**: Yes


# ModifyTargetGroupAttributesOutputTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyTargetGroupInputRequestTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckProtocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### HealthCheckPort
- **Type**: typing.Optional[str]

### HealthCheckPath
- **Type**: typing.Optional[str]

### HealthCheckEnabled
- **Type**: typing.Optional[bool]

### HealthCheckIntervalSeconds
- **Type**: typing.Optional[int]

### HealthCheckTimeoutSeconds
- **Type**: typing.Optional[int]

### HealthyThresholdCount
- **Type**: typing.Optional[int]

### UnhealthyThresholdCount
- **Type**: typing.Optional[int]

### Matcher
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.MatcherTypeDef]


# ModifyTargetGroupOutputTypeDef

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyTrustStoreInputRequestTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### CaCertificatesBundleS3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### CaCertificatesBundleS3Key
- **Type**: <class 'str'>
- **Required**: Yes

### CaCertificatesBundleS3ObjectVersion
- **Type**: typing.Optional[str]


# ModifyTrustStoreOutputTypeDef

### TrustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStoreTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MutualAuthenticationAttributesTypeDef

### Mode
- **Type**: typing.Optional[str]

### TrustStoreArn
- **Type**: typing.Optional[str]

### IgnoreClientCertificateExpiry
- **Type**: typing.Optional[bool]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathPatternConditionConfigExtraOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# PathPatternConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# PathPatternConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# QueryStringConditionConfigExtraOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringKeyValuePairTypeDef]]


# QueryStringConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringKeyValuePairTypeDef]]


# QueryStringConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringKeyValuePairTypeDef]]


# QueryStringKeyValuePairTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# RedirectActionConfigTypeDef

### StatusCode
- **Type**: typing.Literal['HTTP_301', 'HTTP_302']
- **Required**: Yes

### Protocol
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[str]

### Host
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Query
- **Type**: typing.Optional[str]


# RegisterTargetsInputRequestTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]
- **Required**: Yes


# RemoveListenerCertificatesInputRequestTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.CertificateTypeDef]
- **Required**: Yes


# RemoveTagsInputRequestTypeDef

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveTrustStoreRevocationsInputRequestTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationIds
- **Type**: typing.Sequence[int]
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


# RevocationContentTypeDef

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### RevocationType
- **Type**: typing.Optional[typing.Literal['CRL']]


# RuleConditionExtraOutputTypeDef

### Field
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### HostHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HostHeaderConditionConfigExtraOutputTypeDef]

### PathPatternConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PathPatternConditionConfigExtraOutputTypeDef]

### HttpHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpHeaderConditionConfigExtraOutputTypeDef]

### QueryStringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringConditionConfigExtraOutputTypeDef]

### HttpRequestMethodConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpRequestMethodConditionConfigExtraOutputTypeDef]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.SourceIpConditionConfigExtraOutputTypeDef]


# RuleConditionOutputTypeDef

### Field
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### HostHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HostHeaderConditionConfigOutputTypeDef]

### PathPatternConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PathPatternConditionConfigOutputTypeDef]

### HttpHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpHeaderConditionConfigOutputTypeDef]

### QueryStringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringConditionConfigOutputTypeDef]

### HttpRequestMethodConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpRequestMethodConditionConfigOutputTypeDef]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.SourceIpConditionConfigOutputTypeDef]


# RuleConditionTypeDef

### Field
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### HostHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HostHeaderConditionConfigTypeDef]

### PathPatternConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PathPatternConditionConfigTypeDef]

### HttpHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpHeaderConditionConfigTypeDef]

### QueryStringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringConditionConfigTypeDef]

### HttpRequestMethodConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpRequestMethodConditionConfigTypeDef]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.SourceIpConditionConfigTypeDef]


# RulePriorityPairTypeDef

### RuleArn
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]


# RuleTypeDef

### RuleArn
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[str]

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionOutputTypeDef]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ActionOutputTypeDef]]

### IsDefault
- **Type**: typing.Optional[bool]


# SetIpAddressTypeInputRequestTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddressType
- **Type**: typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']
- **Required**: Yes


# SetIpAddressTypeOutputTypeDef

### IpAddressType
- **Type**: typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetRulePrioritiesInputRequestTypeDef

### RulePriorities
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.RulePriorityPairTypeDef]
- **Required**: Yes


# SetRulePrioritiesOutputTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.RuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetSecurityGroupsInputRequestTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Sequence[str]
- **Required**: Yes

### EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic
- **Type**: typing.Optional[typing.Literal['off', 'on']]


# SetSecurityGroupsOutputTypeDef

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic
- **Type**: typing.Literal['off', 'on']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetSubnetsInputRequestTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.SubnetMappingTypeDef]]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']]


# SetSubnetsOutputTypeDef

### AvailabilityZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.AvailabilityZoneTypeDef]
- **Required**: Yes

### IpAddressType
- **Type**: typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SourceIpConditionConfigExtraOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# SourceIpConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# SourceIpConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# SslPolicyTypeDef

### SslProtocols
- **Type**: typing.Optional[typing.List[str]]

### Ciphers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.CipherTypeDef]]

### Name
- **Type**: typing.Optional[str]

### SupportedLoadBalancerTypes
- **Type**: typing.Optional[typing.List[str]]


# SubnetMappingTypeDef

### SubnetId
- **Type**: typing.Optional[str]

### AllocationId
- **Type**: typing.Optional[str]

### PrivateIPv4Address
- **Type**: typing.Optional[str]

### IPv6Address
- **Type**: typing.Optional[str]


# TagDescriptionTypeDef

### ResourceArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TagTypeDef]]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TargetDescriptionTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]


# TargetGroupAttributeTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TargetGroupStickinessConfigTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### DurationSeconds
- **Type**: typing.Optional[int]


# TargetGroupTupleTypeDef

### TargetGroupArn
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]


# TargetGroupTypeDef

### TargetGroupArn
- **Type**: typing.Optional[str]

### TargetGroupName
- **Type**: typing.Optional[str]

### Protocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### Port
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### HealthCheckProtocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### HealthCheckPort
- **Type**: typing.Optional[str]

### HealthCheckEnabled
- **Type**: typing.Optional[bool]

### HealthCheckIntervalSeconds
- **Type**: typing.Optional[int]

### HealthCheckTimeoutSeconds
- **Type**: typing.Optional[int]

### HealthyThresholdCount
- **Type**: typing.Optional[int]

### UnhealthyThresholdCount
- **Type**: typing.Optional[int]

### HealthCheckPath
- **Type**: typing.Optional[str]

### Matcher
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.MatcherTypeDef]

### LoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### TargetType
- **Type**: typing.Optional[typing.Literal['alb', 'instance', 'ip', 'lambda']]

### ProtocolVersion
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# TargetHealthDescriptionTypeDef

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]

### HealthCheckPort
- **Type**: typing.Optional[str]

### TargetHealth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.TargetHealthTypeDef]

### AnomalyDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AnomalyDetectionTypeDef]


# TargetHealthTypeDef

### State
- **Type**: typing.Optional[typing.Literal['draining', 'healthy', 'initial', 'unavailable', 'unhealthy', 'unhealthy.draining', 'unused']]

### Reason
- **Type**: typing.Optional[typing.Literal['Elb.InitialHealthChecking', 'Elb.InternalError', 'Elb.RegistrationInProgress', 'Target.DeregistrationInProgress', 'Target.FailedHealthChecks', 'Target.HealthCheckDisabled', 'Target.InvalidState', 'Target.IpUnusable', 'Target.NotInUse', 'Target.NotRegistered', 'Target.ResponseCodeMismatch', 'Target.Timeout']]

### Description
- **Type**: typing.Optional[str]


# TrustStoreAssociationTypeDef

### ResourceArn
- **Type**: typing.Optional[str]


# TrustStoreRevocationTypeDef

### TrustStoreArn
- **Type**: typing.Optional[str]

### RevocationId
- **Type**: typing.Optional[int]

### RevocationType
- **Type**: typing.Optional[typing.Literal['CRL']]

### NumberOfRevokedEntries
- **Type**: typing.Optional[int]


# TrustStoreTypeDef

### Name
- **Type**: typing.Optional[str]

### TrustStoreArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING']]

### NumberOfCaCertificates
- **Type**: typing.Optional[int]

### TotalRevokedEntries
- **Type**: typing.Optional[int]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



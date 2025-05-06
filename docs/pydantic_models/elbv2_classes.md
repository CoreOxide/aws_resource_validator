# Elbv2 Classes

# Action

### Type
- **Type**: typing.Literal['authenticate-cognito', 'authenticate-oidc', 'fixed-response', 'forward', 'redirect']
- **Required**: Yes

### TargetGroupArn
- **Type**: typing.Optional[str]

### AuthenticateOidcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.AuthenticateOidcActionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.AuthenticateOidcActionConfigOutput, NoneType]

### AuthenticateCognitoConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.AuthenticateCognitoActionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.AuthenticateCognitoActionConfigOutput, NoneType]

### Order
- **Type**: typing.Optional[int]

### RedirectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RedirectActionConfig]

### FixedResponseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.FixedResponseActionConfig]

### ForwardConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ForwardActionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ForwardActionConfigOutput, NoneType]


# ActionOutput

### Type
- **Type**: typing.Literal['authenticate-cognito', 'authenticate-oidc', 'fixed-response', 'forward', 'redirect']
- **Required**: Yes

### TargetGroupArn
- **Type**: typing.Optional[str]

### AuthenticateOidcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.AuthenticateOidcActionConfigOutput]

### AuthenticateCognitoConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.AuthenticateCognitoActionConfigOutput]

### Order
- **Type**: typing.Optional[int]

### RedirectConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RedirectActionConfig]

### FixedResponseConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.FixedResponseActionConfig]

### ForwardConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ForwardActionConfigOutput]


# AddListenerCertificatesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Certificate]
- **Required**: Yes


# AddListenerCertificatesOutput

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Certificate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsInput

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Tag]
- **Required**: Yes


# AddTrustStoreRevocationsInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationContents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RevocationContent]]


# AddTrustStoreRevocationsOutput

### TrustStoreRevocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TrustStoreRevocation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# AdministrativeOverride

### State
- **Type**: typing.Optional[typing.Literal['no_override', 'unknown', 'zonal_shift_active', 'zonal_shift_delegated_to_dns']]

### Reason
- **Type**: typing.Optional[typing.Literal['AdministrativeOverride.NoOverride', 'AdministrativeOverride.Unknown', 'AdministrativeOverride.ZonalShiftActive', 'AdministrativeOverride.ZonalShiftDelegatedToDns']]

### Description
- **Type**: typing.Optional[str]


# AnomalyDetection

### Result
- **Type**: typing.Optional[typing.Literal['anomalous', 'normal']]

### MitigationInEffect
- **Type**: typing.Optional[typing.Literal['no', 'yes']]


# AuthenticateCognitoActionConfig

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


# AuthenticateCognitoActionConfigOutput

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


# AuthenticateOidcActionConfig

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


# AuthenticateOidcActionConfigOutput

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


# AvailabilityZone

### ZoneName
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### OutpostId
- **Type**: typing.Optional[str]

### LoadBalancerAddresses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.LoadBalancerAddress]]

### SourceNatIpv6Prefixes
- **Type**: typing.Optional[typing.List[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityReservationStatus

### Code
- **Type**: typing.Optional[typing.Literal['failed', 'pending', 'provisioned', 'rebalancing']]

### Reason
- **Type**: typing.Optional[str]


# Certificate

### CertificateArn
- **Type**: typing.Optional[str]

### IsDefault
- **Type**: typing.Optional[bool]


# Cipher

### Name
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]


# CreateListenerInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultActions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Action, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ActionOutput]]
- **Required**: Yes

### Protocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### Port
- **Type**: typing.Optional[int]

### SslPolicy
- **Type**: typing.Optional[str]

### Certificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Certificate]]

### AlpnPolicy
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Tag]]

### MutualAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.MutualAuthenticationAttributes]


# CreateListenerOutput

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Listener]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoadBalancerInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SubnetMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.SubnetMapping]]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### Scheme
- **Type**: typing.Optional[typing.Literal['internal', 'internet-facing']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Tag]]

### Type
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']]

### CustomerOwnedIpv4Pool
- **Type**: typing.Optional[str]

### EnablePrefixForIpv6SourceNat
- **Type**: typing.Optional[typing.Literal['off', 'on']]

### IpamPools
- **Type**: <class 'NoneType'>


# CreateLoadBalancerOutput

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.LoadBalancer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Conditions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RuleCondition, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RuleConditionOutput]]
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Actions
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Action, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ActionOutput]]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Tag]]


# CreateRuleOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Rule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTargetGroupInput

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
- **Type**: <class 'NoneType'>

### TargetType
- **Type**: typing.Optional[typing.Literal['alb', 'instance', 'ip', 'lambda']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Tag]]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# CreateTargetGroupOutput

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrustStoreInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Tag]]


# CreateTrustStoreOutput

### TrustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TrustStore]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteListenerInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoadBalancerInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleInput

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSharedTrustStoreAssociationInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetGroupInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustStoreInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTargetsInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetDescription]
- **Required**: Yes


# DescribeAccountLimitsInput

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeAccountLimitsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PaginatorConfig]


# DescribeAccountLimitsOutput

### Limits
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Limit]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCapacityReservationInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCapacityReservationOutput

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DecreaseRequestsRemaining
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumLoadBalancerCapacity
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.MinimumLoadBalancerCapacity'>
- **Required**: Yes

### CapacityReservationState
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ZonalCapacityReservationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeListenerAttributesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeListenerAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ListenerAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeListenerCertificatesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeListenerCertificatesInputPaginate

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PaginatorConfig]


# DescribeListenerCertificatesOutput

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Certificate]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeListenersInput

### LoadBalancerArn
- **Type**: typing.Optional[str]

### ListenerArns
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeListenersInputPaginate

### LoadBalancerArn
- **Type**: typing.Optional[str]

### ListenerArns
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PaginatorConfig]


# DescribeListenersOutput

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Listener]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoadBalancerAttributesInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoadBalancerAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.LoadBalancerAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoadBalancersInput

### LoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeLoadBalancersInputPaginate

### LoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PaginatorConfig]


# DescribeLoadBalancersInputWait

### LoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeLoadBalancersInputWaitExtra

### LoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeLoadBalancersInputWaitExtraExtra

### LoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeLoadBalancersOutput

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.LoadBalancer]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRulesInput

### ListenerArn
- **Type**: typing.Optional[str]

### RuleArns
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeRulesInputPaginate

### ListenerArn
- **Type**: typing.Optional[str]

### RuleArns
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PaginatorConfig]


# DescribeRulesOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Rule]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSSLPoliciesInput

### Names
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### LoadBalancerType
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]


# DescribeSSLPoliciesInputPaginate

### Names
- **Type**: typing.Optional[typing.List[str]]

### LoadBalancerType
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PaginatorConfig]


# DescribeSSLPoliciesOutput

### SslPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.SslPolicy]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTagsInput

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeTagsOutput

### TagDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TagDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTargetGroupAttributesInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTargetGroupAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetGroupAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTargetGroupsInput

### LoadBalancerArn
- **Type**: typing.Optional[str]

### TargetGroupArns
- **Type**: typing.Optional[typing.List[str]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTargetGroupsInputPaginate

### LoadBalancerArn
- **Type**: typing.Optional[str]

### TargetGroupArns
- **Type**: typing.Optional[typing.List[str]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PaginatorConfig]


# DescribeTargetGroupsOutput

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetGroup]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTargetHealthInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetDescription]]

### Include
- **Type**: typing.Optional[typing.List[typing.Literal['All', 'AnomalyDetection']]]


# DescribeTargetHealthInputWait

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetDescription]]

### Include
- **Type**: typing.Optional[typing.List[typing.Literal['All', 'AnomalyDetection']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTargetHealthInputWaitExtra

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetDescription]]

### Include
- **Type**: typing.Optional[typing.List[typing.Literal['All', 'AnomalyDetection']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTargetHealthOutput

### TargetHealthDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetHealthDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustStoreAssociationsInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTrustStoreAssociationsOutput

### TrustStoreAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TrustStoreAssociation]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustStoreRevocation

### TrustStoreArn
- **Type**: typing.Optional[str]

### RevocationId
- **Type**: typing.Optional[int]

### RevocationType
- **Type**: typing.Optional[typing.Literal['CRL']]

### NumberOfRevokedEntries
- **Type**: typing.Optional[int]


# DescribeTrustStoreRevocationsInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationIds
- **Type**: typing.Optional[typing.List[int]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTrustStoreRevocationsOutput

### TrustStoreRevocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.DescribeTrustStoreRevocation]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustStoresInput

### TrustStoreArns
- **Type**: typing.Optional[typing.List[str]]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTrustStoresOutput

### TrustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TrustStore]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# FixedResponseActionConfig

### StatusCode
- **Type**: <class 'str'>
- **Required**: Yes

### MessageBody
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]


# ForwardActionConfig

### TargetGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetGroupTuple]]

### TargetGroupStickinessConfig
- **Type**: <class 'NoneType'>


# ForwardActionConfigOutput

### TargetGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetGroupTuple]]

### TargetGroupStickinessConfig
- **Type**: <class 'NoneType'>


# GetResourcePolicyInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyOutput

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrustStoreCaCertificatesBundleInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrustStoreCaCertificatesBundleOutput

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrustStoreRevocationContentInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationId
- **Type**: <class 'int'>
- **Required**: Yes


# GetTrustStoreRevocationContentOutput

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# HostHeaderConditionConfig

### Values
- **Type**: typing.Optional[typing.List[str]]


# HostHeaderConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpHeaderConditionConfig

### HttpHeaderName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpHeaderConditionConfigOutput

### HttpHeaderName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpRequestMethodConditionConfig

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpRequestMethodConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# IpamPools

### Ipv4IpamPoolId
- **Type**: typing.Optional[str]


# Limit

### Name
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[str]


# Listener

### ListenerArn
- **Type**: typing.Optional[str]

### LoadBalancerArn
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['GENEVE', 'HTTP', 'HTTPS', 'TCP', 'TCP_UDP', 'TLS', 'UDP']]

### Certificates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Certificate]]

### SslPolicy
- **Type**: typing.Optional[str]

### DefaultActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ActionOutput]]

### AlpnPolicy
- **Type**: typing.Optional[typing.List[str]]

### MutualAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.MutualAuthenticationAttributes]


# ListenerAttribute

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# LoadBalancer

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.LoadBalancerState]

### Type
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.AvailabilityZone]]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']]

### CustomerOwnedIpv4Pool
- **Type**: typing.Optional[str]

### EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic
- **Type**: typing.Optional[str]

### EnablePrefixForIpv6SourceNat
- **Type**: typing.Optional[typing.Literal['off', 'on']]

### IpamPools
- **Type**: <class 'NoneType'>


# LoadBalancerAddress

### IpAddress
- **Type**: typing.Optional[str]

### AllocationId
- **Type**: typing.Optional[str]

### PrivateIPv4Address
- **Type**: typing.Optional[str]

### IPv6Address
- **Type**: typing.Optional[str]


# LoadBalancerAttribute

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# LoadBalancerState

### Code
- **Type**: typing.Optional[typing.Literal['active', 'active_impaired', 'failed', 'provisioning']]

### Reason
- **Type**: typing.Optional[str]


# Matcher

### HttpCode
- **Type**: typing.Optional[str]

### GrpcCode
- **Type**: typing.Optional[str]


# MinimumLoadBalancerCapacity

### CapacityUnits
- **Type**: typing.Optional[int]


# ModifyCapacityReservationInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### MinimumLoadBalancerCapacity
- **Type**: <class 'NoneType'>

### ResetCapacityReservation
- **Type**: typing.Optional[bool]


# ModifyCapacityReservationOutput

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DecreaseRequestsRemaining
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumLoadBalancerCapacity
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.MinimumLoadBalancerCapacity'>
- **Required**: Yes

### CapacityReservationState
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ZonalCapacityReservationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyIpPoolsInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### IpamPools
- **Type**: <class 'NoneType'>

### RemoveIpamPools
- **Type**: typing.Optional[typing.List[typing.Literal['ipv4']]]


# ModifyIpPoolsOutput

### IpamPools
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.IpamPools'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyListenerAttributesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ListenerAttribute]
- **Required**: Yes


# ModifyListenerAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ListenerAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyListenerInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Certificate]]

### DefaultActions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Action, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ActionOutput]]]

### AlpnPolicy
- **Type**: typing.Optional[typing.List[str]]

### MutualAuthentication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.MutualAuthenticationAttributes]


# ModifyListenerOutput

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Listener]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyLoadBalancerAttributesInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.LoadBalancerAttribute]
- **Required**: Yes


# ModifyLoadBalancerAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.LoadBalancerAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyRuleInput

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RuleCondition, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RuleConditionOutput]]]

### Actions
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Action, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ActionOutput]]]


# ModifyRuleOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Rule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyTargetGroupAttributesInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetGroupAttribute]
- **Required**: Yes


# ModifyTargetGroupAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetGroupAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyTargetGroupInput

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
- **Type**: <class 'NoneType'>


# ModifyTargetGroupOutput

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyTrustStoreInput

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


# ModifyTrustStoreOutput

### TrustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TrustStore]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# MutualAuthenticationAttributes

### Mode
- **Type**: typing.Optional[str]

### TrustStoreArn
- **Type**: typing.Optional[str]

### IgnoreClientCertificateExpiry
- **Type**: typing.Optional[bool]

### TrustStoreAssociationStatus
- **Type**: typing.Optional[typing.Literal['active', 'removed']]

### AdvertiseTrustStoreCaNames
- **Type**: typing.Optional[typing.Literal['off', 'on']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathPatternConditionConfig

### Values
- **Type**: typing.Optional[typing.List[str]]


# PathPatternConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# QueryStringConditionConfig

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.QueryStringKeyValuePair]]


# QueryStringConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.QueryStringKeyValuePair]]


# QueryStringKeyValuePair

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# RedirectActionConfig

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


# RegisterTargetsInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetDescription]
- **Required**: Yes


# RemoveListenerCertificatesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Certificate]
- **Required**: Yes


# RemoveTagsInput

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# RemoveTrustStoreRevocationsInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationIds
- **Type**: typing.List[int]
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


# RevocationContent

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### RevocationType
- **Type**: typing.Optional[typing.Literal['CRL']]


# Rule

### RuleArn
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[str]

### Conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RuleConditionOutput]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ActionOutput]]

### IsDefault
- **Type**: typing.Optional[bool]


# RuleCondition

### Field
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### HostHeaderConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HostHeaderConditionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HostHeaderConditionConfigOutput, NoneType]

### PathPatternConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PathPatternConditionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PathPatternConditionConfigOutput, NoneType]

### HttpHeaderConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HttpHeaderConditionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HttpHeaderConditionConfigOutput, NoneType]

### QueryStringConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.QueryStringConditionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.QueryStringConditionConfigOutput, NoneType]

### HttpRequestMethodConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HttpRequestMethodConditionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HttpRequestMethodConditionConfigOutput, NoneType]

### SourceIpConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.SourceIpConditionConfig, aws_resource_validator.pydantic_models.elbv2.elbv2_classes.SourceIpConditionConfigOutput, NoneType]


# RuleConditionOutput

### Field
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### HostHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HostHeaderConditionConfigOutput]

### PathPatternConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.PathPatternConditionConfigOutput]

### HttpHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HttpHeaderConditionConfigOutput]

### QueryStringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.QueryStringConditionConfigOutput]

### HttpRequestMethodConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.HttpRequestMethodConditionConfigOutput]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.SourceIpConditionConfigOutput]


# RulePriorityPair

### RuleArn
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]


# SetIpAddressTypeInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddressType
- **Type**: typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']
- **Required**: Yes


# SetIpAddressTypeOutput

### IpAddressType
- **Type**: typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# SetRulePrioritiesInput

### RulePriorities
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.RulePriorityPair]
- **Required**: Yes


# SetRulePrioritiesOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Rule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# SetSecurityGroupsInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic
- **Type**: typing.Optional[typing.Literal['off', 'on']]


# SetSecurityGroupsOutput

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### EnforceSecurityGroupInboundRulesOnPrivateLinkTraffic
- **Type**: typing.Literal['off', 'on']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# SetSubnetsInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SubnetMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.SubnetMapping]]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']]

### EnablePrefixForIpv6SourceNat
- **Type**: typing.Optional[typing.Literal['off', 'on']]


# SetSubnetsOutput

### AvailabilityZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.AvailabilityZone]
- **Required**: Yes

### IpAddressType
- **Type**: typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']
- **Required**: Yes

### EnablePrefixForIpv6SourceNat
- **Type**: typing.Literal['off', 'on']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# SourceIpConditionConfig

### Values
- **Type**: typing.Optional[typing.List[str]]


# SourceIpConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# SslPolicy

### SslProtocols
- **Type**: typing.Optional[typing.List[str]]

### Ciphers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Cipher]]

### Name
- **Type**: typing.Optional[str]

### SupportedLoadBalancerTypes
- **Type**: typing.Optional[typing.List[str]]


# SubnetMapping

### SubnetId
- **Type**: typing.Optional[str]

### AllocationId
- **Type**: typing.Optional[str]

### PrivateIPv4Address
- **Type**: typing.Optional[str]

### IPv6Address
- **Type**: typing.Optional[str]

### SourceNatIpv6Prefix
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagDescription

### ResourceArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.Tag]]


# TargetDescription

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]


# TargetGroup

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
- **Type**: <class 'NoneType'>

### LoadBalancerArns
- **Type**: typing.Optional[typing.List[str]]

### TargetType
- **Type**: typing.Optional[typing.Literal['alb', 'instance', 'ip', 'lambda']]

### ProtocolVersion
- **Type**: typing.Optional[str]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['ipv4', 'ipv6']]


# TargetGroupAttribute

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TargetGroupStickinessConfig

### Enabled
- **Type**: typing.Optional[bool]

### DurationSeconds
- **Type**: typing.Optional[int]


# TargetGroupTuple

### TargetGroupArn
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]


# TargetHealth

### State
- **Type**: typing.Optional[typing.Literal['draining', 'healthy', 'initial', 'unavailable', 'unhealthy', 'unhealthy.draining', 'unused']]

### Reason
- **Type**: typing.Optional[typing.Literal['Elb.InitialHealthChecking', 'Elb.InternalError', 'Elb.RegistrationInProgress', 'Target.DeregistrationInProgress', 'Target.FailedHealthChecks', 'Target.HealthCheckDisabled', 'Target.InvalidState', 'Target.IpUnusable', 'Target.NotInUse', 'Target.NotRegistered', 'Target.ResponseCodeMismatch', 'Target.Timeout']]

### Description
- **Type**: typing.Optional[str]


# TargetHealthDescription

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.TargetDescription]

### HealthCheckPort
- **Type**: typing.Optional[str]

### TargetHealth
- **Type**: <class 'NoneType'>

### AnomalyDetection
- **Type**: <class 'NoneType'>

### AdministrativeOverride
- **Type**: <class 'NoneType'>


# TrustStore

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


# TrustStoreAssociation

### ResourceArn
- **Type**: typing.Optional[str]


# TrustStoreRevocation

### TrustStoreArn
- **Type**: typing.Optional[str]

### RevocationId
- **Type**: typing.Optional[int]

### RevocationType
- **Type**: typing.Optional[typing.Literal['CRL']]

### NumberOfRevokedEntries
- **Type**: typing.Optional[int]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# ZonalCapacityReservationState

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2.elbv2_classes.CapacityReservationStatus]

### AvailabilityZone
- **Type**: typing.Optional[str]

### EffectiveCapacityUnits
- **Type**: typing.Optional[float]



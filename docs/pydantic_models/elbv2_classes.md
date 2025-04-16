# Elbv2 Classes

# ActionOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddListenerCertificatesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.Certificate]
- **Required**: Yes


# AddListenerCertificatesOutput

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Certificate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsInput

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.Tag]
- **Required**: Yes


# AddTrustStoreRevocationsInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationContents
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.RevocationContent]]


# AddTrustStoreRevocationsOutput

### TrustStoreRevocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStoreRevocation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Mapping[str, str]]

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerAddress]]

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


# CreateListenerOutput

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Listener]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoadBalancerOutput

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionUnion]
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.ActionUnion]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.Tag]]


# CreateRuleOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Rule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTargetGroupOutput

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.Tag]]


# CreateTrustStoreOutput

### TrustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStore]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescription]
- **Required**: Yes


# DescribeAccountLimitsInput

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeAccountLimitsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfig]


# DescribeAccountLimitsOutput

### Limits
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Limit]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.MinimumLoadBalancerCapacity'>
- **Required**: Yes

### CapacityReservationState
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ZonalCapacityReservationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeListenerAttributesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeListenerAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfig]


# DescribeListenerCertificatesOutput

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Certificate]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeListenersInput

### LoadBalancerArn
- **Type**: typing.Optional[str]

### ListenerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeListenersInputPaginate

### LoadBalancerArn
- **Type**: typing.Optional[str]

### ListenerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfig]


# DescribeListenersOutput

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Listener]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoadBalancerAttributesInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLoadBalancerAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLoadBalancersInput

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeLoadBalancersInputPaginate

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfig]


# DescribeLoadBalancersInputWait

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeLoadBalancersInputWaitExtra

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeLoadBalancersInputWaitExtraExtra

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeLoadBalancersOutput

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancer]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRulesInput

### ListenerArn
- **Type**: typing.Optional[str]

### RuleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeRulesInputPaginate

### ListenerArn
- **Type**: typing.Optional[str]

### RuleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfig]


# DescribeRulesOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Rule]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSSLPoliciesInput

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]

### LoadBalancerType
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]


# DescribeSSLPoliciesInputPaginate

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### LoadBalancerType
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfig]


# DescribeSSLPoliciesOutput

### SslPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.SslPolicy]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTagsInput

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeTagsOutput

### TagDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TagDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTargetGroupAttributesInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTargetGroupAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTargetGroupsInput

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


# DescribeTargetGroupsInputPaginate

### LoadBalancerArn
- **Type**: typing.Optional[str]

### TargetGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfig]


# DescribeTargetGroupsOutput

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroup]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTargetHealthInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescription]]

### Include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'AnomalyDetection']]]


# DescribeTargetHealthInputWait

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescription]]

### Include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'AnomalyDetection']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTargetHealthInputWaitExtra

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescription]]

### Include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'AnomalyDetection']]]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeTargetHealthOutput

### TargetHealthDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetHealthDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStoreAssociation]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[int]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTrustStoreRevocationsOutput

### TrustStoreRevocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.DescribeTrustStoreRevocation]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustStoresInput

### TrustStoreArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeTrustStoresOutput

### TrustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStore]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTuple]]

### TargetGroupStickinessConfig
- **Type**: <class 'NoneType'>


# ForwardActionConfigOutput

### TargetGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTuple]]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# HostHeaderConditionConfig

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# HostHeaderConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# HostHeaderConditionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HttpHeaderConditionConfig

### HttpHeaderName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# HttpHeaderConditionConfigOutput

### HttpHeaderName
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpHeaderConditionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HttpRequestMethodConditionConfig

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# HttpRequestMethodConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpRequestMethodConditionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IpamPools

### Ipv4IpamPoolId
- **Type**: typing.Optional[str]


# Limit

### Name
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[str]


# Listener

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListenerAttribute

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# LoadBalancer

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.MinimumLoadBalancerCapacity'>
- **Required**: Yes

### CapacityReservationState
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ZonalCapacityReservationState]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyIpPoolsInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### IpamPools
- **Type**: <class 'NoneType'>

### RemoveIpamPools
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ipv4']]]


# ModifyIpPoolsOutput

### IpamPools
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.IpamPools'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyListenerAttributesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.ListenerAttribute]
- **Required**: Yes


# ModifyListenerAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyListenerOutput

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Listener]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyLoadBalancerAttributesInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerAttribute]
- **Required**: Yes


# ModifyLoadBalancerAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyRuleInput

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionUnion]]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.ActionUnion]]


# ModifyRuleOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Rule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# ModifyTargetGroupAttributesInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupAttribute]
- **Required**: Yes


# ModifyTargetGroupAttributesOutput

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupAttribute]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TrustStore]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[str]]


# PathPatternConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# PathPatternConditionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryStringConditionConfig

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringKeyValuePair]]


# QueryStringConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringKeyValuePair]]


# QueryStringConditionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryStringKeyValuePair

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# RegisterTargetsInput

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescription]
- **Required**: Yes


# RemoveListenerCertificatesInput

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.Certificate]
- **Required**: Yes


# RemoveTagsInput

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveTrustStoreRevocationsInput

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationIds
- **Type**: typing.Sequence[int]
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionOutput]]

### Actions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ActionOutput]]

### IsDefault
- **Type**: typing.Optional[bool]


# RuleCondition

### Field
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]

### HostHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HostHeaderConditionConfigUnion]

### PathPatternConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PathPatternConditionConfigUnion]

### HttpHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpHeaderConditionConfigUnion]

### QueryStringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringConditionConfigUnion]

### HttpRequestMethodConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpRequestMethodConditionConfigUnion]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.SourceIpConditionConfigUnion]


# RuleConditionOutput

### Field
- **Type**: typing.Optional[str]

### Values
- **Type**: typing.Optional[typing.List[str]]

### HostHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HostHeaderConditionConfigOutput]

### PathPatternConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PathPatternConditionConfigOutput]

### HttpHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpHeaderConditionConfigOutput]

### QueryStringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringConditionConfigOutput]

### HttpRequestMethodConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpRequestMethodConditionConfigOutput]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.SourceIpConditionConfigOutput]


# RuleConditionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# SetRulePrioritiesInput

### RulePriorities
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.RulePriorityPair]
- **Required**: Yes


# SetRulePrioritiesOutput

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Rule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# SetSecurityGroupsInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Sequence[str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# SetSubnetsInput

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.SubnetMapping]]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']]

### EnablePrefixForIpv6SourceNat
- **Type**: typing.Optional[typing.Literal['off', 'on']]


# SetSubnetsOutput

### AvailabilityZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.AvailabilityZone]
- **Required**: Yes

### IpAddressType
- **Type**: typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']
- **Required**: Yes

### EnablePrefixForIpv6SourceNat
- **Type**: typing.Literal['off', 'on']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadata'>
- **Required**: Yes


# SourceIpConditionConfig

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# SourceIpConditionConfigOutput

### Values
- **Type**: typing.Optional[typing.List[str]]


# SourceIpConditionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SslPolicy

### SslProtocols
- **Type**: typing.Optional[typing.List[str]]

### Ciphers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Cipher]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.Tag]]


# TargetDescription

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: typing.Optional[int]

### AvailabilityZone
- **Type**: typing.Optional[str]


# TargetGroup

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescription]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.CapacityReservationStatus]

### AvailabilityZone
- **Type**: typing.Optional[str]

### EffectiveCapacityUnits
- **Type**: typing.Optional[float]



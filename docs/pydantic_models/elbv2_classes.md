# Elbv2 Classes

# ActionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AddListenerCertificatesInputTypeDef

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


# AddTagsInputTypeDef

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TagTypeDef]
- **Required**: Yes


# AddTrustStoreRevocationsInputTypeDef

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


# AdministrativeOverrideTypeDef

### State
- **Type**: typing.Optional[typing.Literal['no_override', 'unknown', 'zonal_shift_active', 'zonal_shift_delegated_to_dns']]

### Reason
- **Type**: typing.Optional[typing.Literal['AdministrativeOverride.NoOverride', 'AdministrativeOverride.Unknown', 'AdministrativeOverride.ZonalShiftActive', 'AdministrativeOverride.ZonalShiftDelegatedToDns']]

### Description
- **Type**: typing.Optional[str]


# AnomalyDetectionTypeDef

### Result
- **Type**: typing.Optional[typing.Literal['anomalous', 'normal']]

### MitigationInEffect
- **Type**: typing.Optional[typing.Literal['no', 'yes']]


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

### SourceNatIpv6Prefixes
- **Type**: typing.Optional[typing.List[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CapacityReservationStatusTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['failed', 'pending', 'provisioned', 'rebalancing']]

### Reason
- **Type**: typing.Optional[str]


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


# CreateListenerOutputTypeDef

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoadBalancerOutputTypeDef

### LoadBalancers
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.LoadBalancerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleInputTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionUnionTypeDef]
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.ActionUnionTypeDef]
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


# CreateTargetGroupOutputTypeDef

### TargetGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.TargetGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrustStoreInputTypeDef

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


# DeleteListenerInputTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoadBalancerInputTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleInputTypeDef

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSharedTrustStoreAssociationInputTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetGroupInputTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustStoreInputTypeDef

### TrustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterTargetsInputTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]
- **Required**: Yes


# DescribeAccountLimitsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeAccountLimitsInputTypeDef

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


# DescribeCapacityReservationInputTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCapacityReservationOutputTypeDef

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DecreaseRequestsRemaining
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumLoadBalancerCapacity
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.MinimumLoadBalancerCapacityTypeDef'>
- **Required**: Yes

### CapacityReservationState
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ZonalCapacityReservationStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeListenerAttributesInputTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeListenerAttributesOutputTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeListenerCertificatesInputPaginateTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeListenerCertificatesInputTypeDef

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


# DescribeListenersInputPaginateTypeDef

### LoadBalancerArn
- **Type**: typing.Optional[str]

### ListenerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeListenersInputTypeDef

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


# DescribeLoadBalancerAttributesInputTypeDef

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


# DescribeLoadBalancersInputPaginateTypeDef

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeLoadBalancersInputTypeDef

### LoadBalancerArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### PageSize
- **Type**: typing.Optional[int]


# DescribeLoadBalancersInputWaitExtraExtraTypeDef

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


# DescribeLoadBalancersInputWaitExtraTypeDef

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


# DescribeLoadBalancersInputWaitTypeDef

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


# DescribeRulesInputPaginateTypeDef

### ListenerArn
- **Type**: typing.Optional[str]

### RuleArns
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeRulesInputTypeDef

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


# DescribeSSLPoliciesInputPaginateTypeDef

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### LoadBalancerType
- **Type**: typing.Optional[typing.Literal['application', 'gateway', 'network']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeSSLPoliciesInputTypeDef

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


# DescribeTagsInputTypeDef

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


# DescribeTargetGroupAttributesInputTypeDef

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


# DescribeTargetGroupsInputPaginateTypeDef

### LoadBalancerArn
- **Type**: typing.Optional[str]

### TargetGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Names
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PaginatorConfigTypeDef]


# DescribeTargetGroupsInputTypeDef

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


# DescribeTargetHealthInputTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]]

### Include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'AnomalyDetection']]]


# DescribeTargetHealthInputWaitExtraTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]]

### Include
- **Type**: typing.Optional[typing.Sequence[typing.Literal['All', 'AnomalyDetection']]]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.WaiterConfigTypeDef]


# DescribeTargetHealthInputWaitTypeDef

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


# DescribeTrustStoreAssociationsInputTypeDef

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


# DescribeTrustStoreRevocationsInputTypeDef

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


# DescribeTrustStoresInputTypeDef

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


# GetResourcePolicyInputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourcePolicyOutputTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrustStoreCaCertificatesBundleInputTypeDef

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


# GetTrustStoreRevocationContentInputTypeDef

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


# HostHeaderConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# HostHeaderConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# HostHeaderConditionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# HttpHeaderConditionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HttpRequestMethodConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# HttpRequestMethodConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# HttpRequestMethodConditionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IpamPoolsTypeDef

### Ipv4IpamPoolId
- **Type**: typing.Optional[str]


# LimitTypeDef

### Name
- **Type**: typing.Optional[str]

### Max
- **Type**: typing.Optional[str]


# ListenerAttributeTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# ListenerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MatcherTypeDef

### HttpCode
- **Type**: typing.Optional[str]

### GrpcCode
- **Type**: typing.Optional[str]


# MinimumLoadBalancerCapacityTypeDef

### CapacityUnits
- **Type**: typing.Optional[int]


# ModifyCapacityReservationInputTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### MinimumLoadBalancerCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.MinimumLoadBalancerCapacityTypeDef]

### ResetCapacityReservation
- **Type**: typing.Optional[bool]


# ModifyCapacityReservationOutputTypeDef

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DecreaseRequestsRemaining
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumLoadBalancerCapacity
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.MinimumLoadBalancerCapacityTypeDef'>
- **Required**: Yes

### CapacityReservationState
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ZonalCapacityReservationStateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyIpPoolsInputTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### IpamPools
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.IpamPoolsTypeDef]

### RemoveIpamPools
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ipv4']]]


# ModifyIpPoolsOutputTypeDef

### IpamPools
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.IpamPoolsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyListenerAttributesInputTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.ListenerAttributeTypeDef]
- **Required**: Yes


# ModifyListenerAttributesOutputTypeDef

### Attributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerAttributeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyListenerOutputTypeDef

### Listeners
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.ListenerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyLoadBalancerAttributesInputTypeDef

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


# ModifyRuleInputTypeDef

### RuleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.RuleConditionUnionTypeDef]]

### Actions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.ActionUnionTypeDef]]


# ModifyRuleOutputTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.RuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModifyTargetGroupAttributesInputTypeDef

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


# ModifyTargetGroupInputTypeDef

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


# ModifyTrustStoreInputTypeDef

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

### TrustStoreAssociationStatus
- **Type**: typing.Optional[typing.Literal['active', 'removed']]

### AdvertiseTrustStoreCaNames
- **Type**: typing.Optional[typing.Literal['off', 'on']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PathPatternConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# PathPatternConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# PathPatternConditionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryStringConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringKeyValuePairTypeDef]]


# QueryStringConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringKeyValuePairTypeDef]]


# QueryStringConditionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryStringKeyValuePairTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# RegisterTargetsInputTypeDef

### TargetGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]
- **Required**: Yes


# RemoveListenerCertificatesInputTypeDef

### ListenerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Certificates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.CertificateTypeDef]
- **Required**: Yes


# RemoveTagsInputTypeDef

### ResourceArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveTrustStoreRevocationsInputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HostHeaderConditionConfigUnionTypeDef]

### PathPatternConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.PathPatternConditionConfigUnionTypeDef]

### HttpHeaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpHeaderConditionConfigUnionTypeDef]

### QueryStringConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.QueryStringConditionConfigUnionTypeDef]

### HttpRequestMethodConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.HttpRequestMethodConditionConfigUnionTypeDef]

### SourceIpConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.SourceIpConditionConfigUnionTypeDef]


# RuleConditionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SetIpAddressTypeInputTypeDef

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


# SetRulePrioritiesInputTypeDef

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


# SetSecurityGroupsInputTypeDef

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


# SetSubnetsInputTypeDef

### LoadBalancerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### SubnetMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elbv2_classes.SubnetMappingTypeDef]]

### IpAddressType
- **Type**: typing.Optional[typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']]

### EnablePrefixForIpv6SourceNat
- **Type**: typing.Optional[typing.Literal['off', 'on']]


# SetSubnetsOutputTypeDef

### AvailabilityZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.elbv2_classes.AvailabilityZoneTypeDef]
- **Required**: Yes

### IpAddressType
- **Type**: typing.Literal['dualstack', 'dualstack-without-public-ipv4', 'ipv4']
- **Required**: Yes

### EnablePrefixForIpv6SourceNat
- **Type**: typing.Literal['off', 'on']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elbv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SourceIpConditionConfigOutputTypeDef

### Values
- **Type**: typing.Optional[typing.List[str]]


# SourceIpConditionConfigTypeDef

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# SourceIpConditionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### SourceNatIpv6Prefix
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetHealthDescriptionTypeDef

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.TargetDescriptionTypeDef]

### HealthCheckPort
- **Type**: typing.Optional[str]

### TargetHealth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.TargetHealthTypeDef]

### AnomalyDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AnomalyDetectionTypeDef]

### AdministrativeOverride
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.AdministrativeOverrideTypeDef]


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


# ZonalCapacityReservationStateTypeDef

### State
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elbv2_classes.CapacityReservationStatusTypeDef]

### AvailabilityZone
- **Type**: typing.Optional[str]

### EffectiveCapacityUnits
- **Type**: typing.Optional[float]



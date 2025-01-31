# Route53 Classes

# AccountLimitTypeDef

### Type
- **Type**: typing.Literal['MAX_HEALTH_CHECKS_BY_OWNER', 'MAX_HOSTED_ZONES_BY_OWNER', 'MAX_REUSABLE_DELEGATION_SETS_BY_OWNER', 'MAX_TRAFFIC_POLICIES_BY_OWNER', 'MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes


# ActivateKeySigningKeyRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ActivateKeySigningKeyResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AlarmIdentifierTypeDef

### Region
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-west-1', 'us-west-2']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AliasTargetTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### DNSName
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluateTargetHealth
- **Type**: <class 'bool'>
- **Required**: Yes


# AssociateVPCWithHostedZoneRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# AssociateVPCWithHostedZoneResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChangeBatchTypeDef

### Changes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_classes.ChangeTypeDef]
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# ChangeCidrCollectionRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Changes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_classes.CidrCollectionChangeTypeDef]
- **Required**: Yes

### CollectionVersion
- **Type**: typing.Optional[int]


# ChangeCidrCollectionResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChangeInfoTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['INSYNC', 'PENDING']
- **Required**: Yes

### SubmittedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# ChangeResourceRecordSetsRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeBatchTypeDef'>
- **Required**: Yes


# ChangeResourceRecordSetsResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChangeTagsForResourceRequestRequestTypeDef

### ResourceType
- **Type**: typing.Literal['healthcheck', 'hostedzone']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AddTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53_classes.TagTypeDef]]

### RemoveTagKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# ChangeTypeDef

### Action
- **Type**: typing.Literal['CREATE', 'DELETE', 'UPSERT']
- **Required**: Yes

### ResourceRecordSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResourceRecordSetTypeDef'>
- **Required**: Yes


# CidrBlockSummaryTypeDef

### CidrBlock
- **Type**: typing.Optional[str]

### LocationName
- **Type**: typing.Optional[str]


# CidrCollectionChangeTypeDef

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['DELETE_IF_EXISTS', 'PUT']
- **Required**: Yes

### CidrList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CidrCollectionTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# CidrRoutingConfigTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchAlarmConfigurationTypeDef

### EvaluationPeriods
- **Type**: <class 'int'>
- **Required**: Yes

### Threshold
- **Type**: <class 'float'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['GreaterThanOrEqualToThreshold', 'GreaterThanThreshold', 'LessThanOrEqualToThreshold', 'LessThanThreshold']
- **Required**: Yes

### Period
- **Type**: <class 'int'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes

### Statistic
- **Type**: typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum']
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53_classes.DimensionTypeDef]]


# CollectionSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# CoordinatesTypeDef

### Latitude
- **Type**: <class 'str'>
- **Required**: Yes

### Longitude
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCidrCollectionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCidrCollectionResponseTypeDef

### Collection
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.CidrCollectionTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHealthCheckRequestRequestTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckConfigTypeDef'>
- **Required**: Yes


# CreateHealthCheckResponseTypeDef

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHostedZoneRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef]

### HostedZoneConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.HostedZoneConfigTypeDef]

### DelegationSetId
- **Type**: typing.Optional[str]


# CreateHostedZoneResponseTypeDef

### HostedZone
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZoneTypeDef'>
- **Required**: Yes

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### DelegationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DelegationSetTypeDef'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKeySigningKeyRequestRequestTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyManagementServiceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes


# CreateKeySigningKeyResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### KeySigningKey
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.KeySigningKeyTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQueryLoggingConfigRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogsLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateQueryLoggingConfigResponseTypeDef

### QueryLoggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.QueryLoggingConfigTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateReusableDelegationSetRequestRequestTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: typing.Optional[str]


# CreateReusableDelegationSetResponseTypeDef

### DelegationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DelegationSetTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrafficPolicyInstanceRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TTL
- **Type**: <class 'int'>
- **Required**: Yes

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyVersion
- **Type**: <class 'int'>
- **Required**: Yes


# CreateTrafficPolicyInstanceResponseTypeDef

### TrafficPolicyInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstanceTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrafficPolicyRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# CreateTrafficPolicyResponseTypeDef

### TrafficPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrafficPolicyVersionRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# CreateTrafficPolicyVersionResponseTypeDef

### TrafficPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVPCAssociationAuthorizationRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef'>
- **Required**: Yes


# CreateVPCAssociationAuthorizationResponseTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DNSSECStatusTypeDef

### ServeSignature
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# DeactivateKeySigningKeyRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeactivateKeySigningKeyResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DelegationSetTypeDef

### NameServers
- **Type**: typing.List[str]
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### CallerReference
- **Type**: typing.Optional[str]


# DeleteCidrCollectionRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHealthCheckRequestRequestTypeDef

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostedZoneRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostedZoneResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteKeySigningKeyRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeySigningKeyResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteQueryLoggingConfigRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReusableDelegationSetRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyInstanceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteVPCAssociationAuthorizationRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef'>
- **Required**: Yes


# DimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DisableHostedZoneDNSSECRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableHostedZoneDNSSECResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateVPCFromHostedZoneRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# DisassociateVPCFromHostedZoneResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableHostedZoneDNSSECRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes


# EnableHostedZoneDNSSECResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GeoLocationDetailsTypeDef

### ContinentCode
- **Type**: typing.Optional[str]

### ContinentName
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[str]

### CountryName
- **Type**: typing.Optional[str]

### SubdivisionCode
- **Type**: typing.Optional[str]

### SubdivisionName
- **Type**: typing.Optional[str]


# GeoLocationTypeDef

### ContinentCode
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[str]

### SubdivisionCode
- **Type**: typing.Optional[str]


# GeoProximityLocationTypeDef

### AWSRegion
- **Type**: typing.Optional[str]

### LocalZoneGroup
- **Type**: typing.Optional[str]

### Coordinates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.CoordinatesTypeDef]

### Bias
- **Type**: typing.Optional[int]


# GetAccountLimitRequestRequestTypeDef

### Type
- **Type**: typing.Literal['MAX_HEALTH_CHECKS_BY_OWNER', 'MAX_HOSTED_ZONES_BY_OWNER', 'MAX_REUSABLE_DELEGATION_SETS_BY_OWNER', 'MAX_TRAFFIC_POLICIES_BY_OWNER', 'MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER']
- **Required**: Yes


# GetAccountLimitResponseTypeDef

### Limit
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.AccountLimitTypeDef'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChangeRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetChangeRequestResourceRecordSetsChangedWaitTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.WaiterConfigTypeDef]


# GetChangeResponseTypeDef

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCheckerIpRangesResponseTypeDef

### CheckerIpRanges
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDNSSECRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDNSSECResponseTypeDef

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DNSSECStatusTypeDef'>
- **Required**: Yes

### KeySigningKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.KeySigningKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGeoLocationRequestRequestTypeDef

### ContinentCode
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[str]

### SubdivisionCode
- **Type**: typing.Optional[str]


# GetGeoLocationResponseTypeDef

### GeoLocationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.GeoLocationDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHealthCheckCountResponseTypeDef

### HealthCheckCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHealthCheckLastFailureReasonRequestRequestTypeDef

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHealthCheckLastFailureReasonResponseTypeDef

### HealthCheckObservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HealthCheckObservationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHealthCheckRequestRequestTypeDef

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHealthCheckResponseTypeDef

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHealthCheckStatusRequestRequestTypeDef

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHealthCheckStatusResponseTypeDef

### HealthCheckObservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HealthCheckObservationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHostedZoneCountResponseTypeDef

### HostedZoneCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHostedZoneLimitRequestRequestTypeDef

### Type
- **Type**: typing.Literal['MAX_RRSETS_BY_ZONE', 'MAX_VPCS_ASSOCIATED_BY_ZONE']
- **Required**: Yes

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHostedZoneLimitResponseTypeDef

### Limit
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZoneLimitTypeDef'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHostedZoneRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetHostedZoneResponseTypeDef

### HostedZone
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZoneTypeDef'>
- **Required**: Yes

### DelegationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DelegationSetTypeDef'>
- **Required**: Yes

### VPCs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQueryLoggingConfigRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryLoggingConfigResponseTypeDef

### QueryLoggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.QueryLoggingConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReusableDelegationSetLimitRequestRequestTypeDef

### Type
- **Type**: typing.Literal['MAX_ZONES_BY_REUSABLE_DELEGATION_SET']
- **Required**: Yes

### DelegationSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReusableDelegationSetLimitResponseTypeDef

### Limit
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ReusableDelegationSetLimitTypeDef'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetReusableDelegationSetRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetReusableDelegationSetResponseTypeDef

### DelegationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DelegationSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrafficPolicyInstanceCountResponseTypeDef

### TrafficPolicyInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrafficPolicyInstanceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrafficPolicyInstanceResponseTypeDef

### TrafficPolicyInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrafficPolicyRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes


# GetTrafficPolicyResponseTypeDef

### TrafficPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HealthCheckConfigPaginatorTypeDef

### Type
- **Type**: typing.Literal['CALCULATED', 'CLOUDWATCH_METRIC', 'HTTP', 'HTTPS', 'HTTPS_STR_MATCH', 'HTTP_STR_MATCH', 'RECOVERY_CONTROL', 'TCP']
- **Required**: Yes

### IPAddress
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ResourcePath
- **Type**: typing.Optional[str]

### FullyQualifiedDomainName
- **Type**: typing.Optional[str]

### SearchString
- **Type**: typing.Optional[str]

### RequestInterval
- **Type**: typing.Optional[int]

### FailureThreshold
- **Type**: typing.Optional[int]

### MeasureLatency
- **Type**: typing.Optional[bool]

### Inverted
- **Type**: typing.Optional[bool]

### Disabled
- **Type**: typing.Optional[bool]

### HealthThreshold
- **Type**: typing.Optional[int]

### ChildHealthChecks
- **Type**: typing.Optional[typing.List[str]]

### EnableSNI
- **Type**: typing.Optional[bool]

### Regions
- **Type**: typing.Optional[typing.List[typing.Literal['ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-west-1', 'sa-east-1', 'us-east-1', 'us-west-1', 'us-west-2']]]

### AlarmIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.AlarmIdentifierTypeDef]

### InsufficientDataHealthStatus
- **Type**: typing.Optional[typing.Literal['Healthy', 'LastKnownStatus', 'Unhealthy']]

### RoutingControlArn
- **Type**: typing.Optional[str]


# HealthCheckConfigTypeDef

### Type
- **Type**: typing.Literal['CALCULATED', 'CLOUDWATCH_METRIC', 'HTTP', 'HTTPS', 'HTTPS_STR_MATCH', 'HTTP_STR_MATCH', 'RECOVERY_CONTROL', 'TCP']
- **Required**: Yes

### IPAddress
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ResourcePath
- **Type**: typing.Optional[str]

### FullyQualifiedDomainName
- **Type**: typing.Optional[str]

### SearchString
- **Type**: typing.Optional[str]

### RequestInterval
- **Type**: typing.Optional[int]

### FailureThreshold
- **Type**: typing.Optional[int]

### MeasureLatency
- **Type**: typing.Optional[bool]

### Inverted
- **Type**: typing.Optional[bool]

### Disabled
- **Type**: typing.Optional[bool]

### HealthThreshold
- **Type**: typing.Optional[int]

### ChildHealthChecks
- **Type**: typing.Optional[typing.Sequence[str]]

### EnableSNI
- **Type**: typing.Optional[bool]

### Regions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-west-1', 'sa-east-1', 'us-east-1', 'us-west-1', 'us-west-2']]]

### AlarmIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.AlarmIdentifierTypeDef]

### InsufficientDataHealthStatus
- **Type**: typing.Optional[typing.Literal['Healthy', 'LastKnownStatus', 'Unhealthy']]

### RoutingControlArn
- **Type**: typing.Optional[str]


# HealthCheckObservationTypeDef

### Region
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-west-1', 'sa-east-1', 'us-east-1', 'us-west-1', 'us-west-2']]

### IPAddress
- **Type**: typing.Optional[str]

### StatusReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.StatusReportTypeDef]


# HealthCheckPaginatorTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckConfigPaginatorTypeDef'>
- **Required**: Yes

### HealthCheckVersion
- **Type**: <class 'int'>
- **Required**: Yes

### LinkedService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.LinkedServiceTypeDef]

### CloudWatchAlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.CloudWatchAlarmConfigurationTypeDef]


# HealthCheckTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckConfigTypeDef'>
- **Required**: Yes

### HealthCheckVersion
- **Type**: <class 'int'>
- **Required**: Yes

### LinkedService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.LinkedServiceTypeDef]

### CloudWatchAlarmConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.CloudWatchAlarmConfigurationTypeDef]


# HostedZoneConfigTypeDef

### Comment
- **Type**: typing.Optional[str]

### PrivateZone
- **Type**: typing.Optional[bool]


# HostedZoneLimitTypeDef

### Type
- **Type**: typing.Literal['MAX_RRSETS_BY_ZONE', 'MAX_VPCS_ASSOCIATED_BY_ZONE']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes


# HostedZoneOwnerTypeDef

### OwningAccount
- **Type**: typing.Optional[str]

### OwningService
- **Type**: typing.Optional[str]


# HostedZoneSummaryTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Owner
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZoneOwnerTypeDef'>
- **Required**: Yes


# HostedZoneTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.HostedZoneConfigTypeDef]

### ResourceRecordSetCount
- **Type**: typing.Optional[int]

### LinkedService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.LinkedServiceTypeDef]


# KeySigningKeyTypeDef

### Name
- **Type**: typing.Optional[str]

### KmsArn
- **Type**: typing.Optional[str]

### Flag
- **Type**: typing.Optional[int]

### SigningAlgorithmMnemonic
- **Type**: typing.Optional[str]

### SigningAlgorithmType
- **Type**: typing.Optional[int]

### DigestAlgorithmMnemonic
- **Type**: typing.Optional[str]

### DigestAlgorithmType
- **Type**: typing.Optional[int]

### KeyTag
- **Type**: typing.Optional[int]

### DigestValue
- **Type**: typing.Optional[str]

### PublicKey
- **Type**: typing.Optional[str]

### DSRecord
- **Type**: typing.Optional[str]

### DNSKEYRecord
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# LinkedServiceTypeDef

### ServicePrincipal
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ListCidrBlocksRequestListCidrBlocksPaginateTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListCidrBlocksRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListCidrBlocksResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### CidrBlocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.CidrBlockSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCidrCollectionsRequestListCidrCollectionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListCidrCollectionsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListCidrCollectionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### CidrCollections
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.CollectionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCidrLocationsRequestListCidrLocationsPaginateTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListCidrLocationsRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListCidrLocationsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### CidrLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.LocationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGeoLocationsRequestRequestTypeDef

### StartContinentCode
- **Type**: typing.Optional[str]

### StartCountryCode
- **Type**: typing.Optional[str]

### StartSubdivisionCode
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListGeoLocationsResponseTypeDef

### GeoLocationDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.GeoLocationDetailsTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextContinentCode
- **Type**: <class 'str'>
- **Required**: Yes

### NextCountryCode
- **Type**: <class 'str'>
- **Required**: Yes

### NextSubdivisionCode
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListHealthChecksRequestListHealthChecksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListHealthChecksRequestRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListHealthChecksResponsePaginatorTypeDef

### HealthChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HealthCheckPaginatorTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListHealthChecksResponseTypeDef

### HealthChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HealthCheckTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListHostedZonesByNameRequestRequestTypeDef

### DNSName
- **Type**: typing.Optional[str]

### HostedZoneId
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListHostedZonesByNameResponseTypeDef

### HostedZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HostedZoneTypeDef]
- **Required**: Yes

### DNSName
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextDNSName
- **Type**: <class 'str'>
- **Required**: Yes

### NextHostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListHostedZonesByVPCRequestRequestTypeDef

### VPCId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCRegion
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-west-1', 'us-west-2']
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListHostedZonesByVPCResponseTypeDef

### HostedZoneSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HostedZoneSummaryTypeDef]
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListHostedZonesRequestListHostedZonesPaginateTypeDef

### DelegationSetId
- **Type**: typing.Optional[str]

### HostedZoneType
- **Type**: typing.Optional[typing.Literal['PrivateHostedZone']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListHostedZonesRequestRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]

### DelegationSetId
- **Type**: typing.Optional[str]

### HostedZoneType
- **Type**: typing.Optional[typing.Literal['PrivateHostedZone']]


# ListHostedZonesResponseTypeDef

### HostedZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HostedZoneTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQueryLoggingConfigsRequestListQueryLoggingConfigsPaginateTypeDef

### HostedZoneId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListQueryLoggingConfigsRequestRequestTypeDef

### HostedZoneId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListQueryLoggingConfigsResponseTypeDef

### QueryLoggingConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.QueryLoggingConfigTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceRecordSetsRequestListResourceRecordSetsPaginateTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListResourceRecordSetsRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### StartRecordName
- **Type**: typing.Optional[str]

### StartRecordType
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']]

### StartRecordIdentifier
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListResourceRecordSetsResponsePaginatorTypeDef

### ResourceRecordSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.ResourceRecordSetPaginatorTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextRecordName
- **Type**: <class 'str'>
- **Required**: Yes

### NextRecordType
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### NextRecordIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceRecordSetsResponseTypeDef

### ResourceRecordSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.ResourceRecordSetTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextRecordName
- **Type**: <class 'str'>
- **Required**: Yes

### NextRecordType
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### NextRecordIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListReusableDelegationSetsRequestRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListReusableDelegationSetsResponseTypeDef

### DelegationSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.DelegationSetTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceType
- **Type**: typing.Literal['healthcheck', 'hostedzone']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### ResourceTagSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResourceTagSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourcesRequestRequestTypeDef

### ResourceType
- **Type**: typing.Literal['healthcheck', 'hostedzone']
- **Required**: Yes

### ResourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ListTagsForResourcesResponseTypeDef

### ResourceTagSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.ResourceTagSetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrafficPoliciesRequestRequestTypeDef

### TrafficPolicyIdMarker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPoliciesResponseTypeDef

### TrafficPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicySummaryTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### TrafficPolicyIdMarker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrafficPolicyInstancesByHostedZoneRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyInstanceNameMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPolicyInstancesByHostedZoneResponseTypeDef

### TrafficPolicyInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstanceTypeDef]
- **Required**: Yes

### TrafficPolicyInstanceNameMarker
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrafficPolicyInstancesByPolicyRequestRequestTypeDef

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyVersion
- **Type**: <class 'int'>
- **Required**: Yes

### HostedZoneIdMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceNameMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPolicyInstancesByPolicyResponseTypeDef

### TrafficPolicyInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstanceTypeDef]
- **Required**: Yes

### HostedZoneIdMarker
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyInstanceNameMarker
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrafficPolicyInstancesRequestRequestTypeDef

### HostedZoneIdMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceNameMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPolicyInstancesResponseTypeDef

### TrafficPolicyInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstanceTypeDef]
- **Required**: Yes

### HostedZoneIdMarker
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyInstanceNameMarker
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrafficPolicyVersionsRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyVersionMarker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPolicyVersionsResponseTypeDef

### TrafficPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### TrafficPolicyVersionMarker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVPCAssociationAuthorizationsRequestListVPCAssociationAuthorizationsPaginateTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListVPCAssociationAuthorizationsRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListVPCAssociationAuthorizationsResponseTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### VPCs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LocationSummaryTypeDef

### LocationName
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QueryLoggingConfigTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogsLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceRecordSetPaginatorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### SetIdentifier
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]

### Region
- **Type**: typing.Optional[typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]

### GeoLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.GeoLocationTypeDef]

### Failover
- **Type**: typing.Optional[typing.Literal['PRIMARY', 'SECONDARY']]

### MultiValueAnswer
- **Type**: typing.Optional[bool]

### TTL
- **Type**: typing.Optional[int]

### ResourceRecords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53_classes.ResourceRecordTypeDef]]

### AliasTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.AliasTargetTypeDef]

### HealthCheckId
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceId
- **Type**: typing.Optional[str]

### CidrRoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.CidrRoutingConfigTypeDef]

### GeoProximityLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.GeoProximityLocationTypeDef]


# ResourceRecordSetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### SetIdentifier
- **Type**: typing.Optional[str]

### Weight
- **Type**: typing.Optional[int]

### Region
- **Type**: typing.Optional[typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2']]

### GeoLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.GeoLocationTypeDef]

### Failover
- **Type**: typing.Optional[typing.Literal['PRIMARY', 'SECONDARY']]

### MultiValueAnswer
- **Type**: typing.Optional[bool]

### TTL
- **Type**: typing.Optional[int]

### ResourceRecords
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53_classes.ResourceRecordTypeDef]]

### AliasTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.AliasTargetTypeDef]

### HealthCheckId
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceId
- **Type**: typing.Optional[str]

### CidrRoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.CidrRoutingConfigTypeDef]

### GeoProximityLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.GeoProximityLocationTypeDef]


# ResourceRecordTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceTagSetTypeDef

### ResourceType
- **Type**: typing.Optional[typing.Literal['healthcheck', 'hostedzone']]

### ResourceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53_classes.TagTypeDef]]


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


# ReusableDelegationSetLimitTypeDef

### Type
- **Type**: typing.Literal['MAX_ZONES_BY_REUSABLE_DELEGATION_SET']
- **Required**: Yes

### Value
- **Type**: <class 'int'>
- **Required**: Yes


# StatusReportTypeDef

### Status
- **Type**: typing.Optional[str]

### CheckedTime
- **Type**: typing.Optional[datetime.datetime]


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TestDNSAnswerRequestRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### RecordName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordType
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### ResolverIP
- **Type**: typing.Optional[str]

### EDNS0ClientSubnetIP
- **Type**: typing.Optional[str]

### EDNS0ClientSubnetMask
- **Type**: typing.Optional[str]


# TestDNSAnswerResponseTypeDef

### Nameserver
- **Type**: <class 'str'>
- **Required**: Yes

### RecordName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordType
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### RecordData
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseCode
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TrafficPolicyInstanceTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TTL
- **Type**: <class 'int'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyVersion
- **Type**: <class 'int'>
- **Required**: Yes

### TrafficPolicyType
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes


# TrafficPolicySummaryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### LatestVersion
- **Type**: <class 'int'>
- **Required**: Yes

### TrafficPolicyCount
- **Type**: <class 'int'>
- **Required**: Yes


# TrafficPolicyTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'TXT']
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# UpdateHealthCheckRequestRequestTypeDef

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckVersion
- **Type**: typing.Optional[int]

### IPAddress
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### ResourcePath
- **Type**: typing.Optional[str]

### FullyQualifiedDomainName
- **Type**: typing.Optional[str]

### SearchString
- **Type**: typing.Optional[str]

### FailureThreshold
- **Type**: typing.Optional[int]

### Inverted
- **Type**: typing.Optional[bool]

### Disabled
- **Type**: typing.Optional[bool]

### HealthThreshold
- **Type**: typing.Optional[int]

### ChildHealthChecks
- **Type**: typing.Optional[typing.Sequence[str]]

### EnableSNI
- **Type**: typing.Optional[bool]

### Regions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-west-1', 'sa-east-1', 'us-east-1', 'us-west-1', 'us-west-2']]]

### AlarmIdentifier
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.AlarmIdentifierTypeDef]

### InsufficientDataHealthStatus
- **Type**: typing.Optional[typing.Literal['Healthy', 'LastKnownStatus', 'Unhealthy']]

### ResetElements
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ChildHealthChecks', 'FullyQualifiedDomainName', 'Regions', 'ResourcePath']]]


# UpdateHealthCheckResponseTypeDef

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateHostedZoneCommentRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# UpdateHostedZoneCommentResponseTypeDef

### HostedZone
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZoneTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrafficPolicyCommentRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTrafficPolicyCommentResponseTypeDef

### TrafficPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrafficPolicyInstanceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### TTL
- **Type**: <class 'int'>
- **Required**: Yes

### TrafficPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyVersion
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateTrafficPolicyInstanceResponseTypeDef

### TrafficPolicyInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VPCTypeDef

### VPCRegion
- **Type**: typing.Optional[typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-west-1', 'us-west-2']]

### VPCId
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



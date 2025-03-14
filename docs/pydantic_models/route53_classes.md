# Route53 Classes

# AccountLimitTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActivateKeySigningKeyRequestTypeDef

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
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ap-southeast-5', 'ap-southeast-7', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'mx-central-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-west-1', 'us-west-2']
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


# AssociateVPCWithHostedZoneRequestTypeDef

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


# ChangeCidrCollectionRequestTypeDef

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


# ChangeResourceRecordSetsRequestTypeDef

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


# ChangeTagsForResourceRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResourceRecordSetUnionTypeDef'>
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


# CreateCidrCollectionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes


# CreateHealthCheckRequestTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckConfigUnionTypeDef'>
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


# CreateHostedZoneRequestTypeDef

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


# CreateKeySigningKeyRequestTypeDef

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


# CreateQueryLoggingConfigRequestTypeDef

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


# CreateReusableDelegationSetRequestTypeDef

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


# CreateTrafficPolicyInstanceRequestTypeDef

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


# CreateTrafficPolicyRequestTypeDef

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


# CreateTrafficPolicyVersionRequestTypeDef

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


# CreateVPCAssociationAuthorizationRequestTypeDef

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


# DeactivateKeySigningKeyRequestTypeDef

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


# DeleteCidrCollectionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHealthCheckRequestTypeDef

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostedZoneRequestTypeDef

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


# DeleteKeySigningKeyRequestTypeDef

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


# DeleteQueryLoggingConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReusableDelegationSetRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyInstanceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteVPCAssociationAuthorizationRequestTypeDef

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


# DisableHostedZoneDNSSECRequestTypeDef

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


# DisassociateVPCFromHostedZoneRequestTypeDef

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


# EnableHostedZoneDNSSECRequestTypeDef

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


# GetChangeRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetChangeRequestWaitTypeDef

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


# GetDNSSECRequestTypeDef

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


# GetGeoLocationRequestTypeDef

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


# GetHealthCheckLastFailureReasonRequestTypeDef

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


# GetHealthCheckRequestTypeDef

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


# GetHealthCheckStatusRequestTypeDef

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


# GetHostedZoneRequestTypeDef

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


# GetQueryLoggingConfigRequestTypeDef

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


# GetReusableDelegationSetRequestTypeDef

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


# GetTrafficPolicyInstanceRequestTypeDef

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


# GetTrafficPolicyRequestTypeDef

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


# HealthCheckConfigOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HealthCheckConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HealthCheckObservationTypeDef

### Region
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-west-1', 'sa-east-1', 'us-east-1', 'us-west-1', 'us-west-2']]

### IPAddress
- **Type**: typing.Optional[str]

### StatusReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.StatusReportTypeDef]


# HealthCheckTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckConfigOutputTypeDef'>
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ListCidrBlocksRequestPaginateTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListCidrBlocksRequestTypeDef

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

### CidrBlocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.CidrBlockSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCidrCollectionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListCidrCollectionsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListCidrCollectionsResponseTypeDef

### CidrCollections
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.CollectionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCidrLocationsRequestPaginateTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListCidrLocationsRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListCidrLocationsResponseTypeDef

### CidrLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.LocationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGeoLocationsRequestTypeDef

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


# ListHealthChecksRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListHealthChecksRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


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


# ListHostedZonesByNameRequestTypeDef

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


# ListHostedZonesByVPCRequestTypeDef

### VPCId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCRegion
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ap-southeast-5', 'ap-southeast-7', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'mx-central-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-west-1', 'us-west-2']
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHostedZonesRequestPaginateTypeDef

### DelegationSetId
- **Type**: typing.Optional[str]

### HostedZoneType
- **Type**: typing.Optional[typing.Literal['PrivateHostedZone']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListHostedZonesRequestTypeDef

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


# ListQueryLoggingConfigsRequestPaginateTypeDef

### HostedZoneId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListQueryLoggingConfigsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceRecordSetsRequestPaginateTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListResourceRecordSetsRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### StartRecordName
- **Type**: typing.Optional[str]

### StartRecordType
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']]

### StartRecordIdentifier
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListResourceRecordSetsResponseTypeDef

### ResourceRecordSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.ResourceRecordSetOutputTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### NextRecordName
- **Type**: <class 'str'>
- **Required**: Yes

### NextRecordType
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']
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


# ListReusableDelegationSetsRequestTypeDef

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


# ListTagsForResourceRequestTypeDef

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


# ListTagsForResourcesRequestTypeDef

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


# ListTrafficPoliciesRequestTypeDef

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


# ListTrafficPolicyInstancesByHostedZoneRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyInstanceNameMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']]

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
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']
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


# ListTrafficPolicyInstancesByPolicyRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']]

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
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']
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


# ListTrafficPolicyInstancesRequestTypeDef

### HostedZoneIdMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceNameMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']]

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
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']
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


# ListTrafficPolicyVersionsRequestTypeDef

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


# ListVPCAssociationAuthorizationsRequestPaginateTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfigTypeDef]


# ListVPCAssociationAuthorizationsRequestTypeDef

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

### VPCs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.VPCTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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


# ResourceRecordSetOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceRecordSetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ReusableDelegationSetLimitTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# TestDNSAnswerRequestTypeDef

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### RecordName
- **Type**: <class 'str'>
- **Required**: Yes

### RecordType
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']
- **Required**: Yes

### ResolverIP
- **Type**: typing.Optional[str]

### EDNS0ClientSubnetIP
- **Type**: typing.Optional[str]

### EDNS0ClientSubnetMask
- **Type**: typing.Optional[str]


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
- **Type**: typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']
- **Required**: Yes


# TrafficPolicySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrafficPolicyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateHealthCheckRequestTypeDef

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


# UpdateHostedZoneCommentRequestTypeDef

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


# UpdateTrafficPolicyCommentRequestTypeDef

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


# UpdateTrafficPolicyInstanceRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ap-southeast-5', 'ap-southeast-7', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'mx-central-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-west-1', 'us-west-2']]

### VPCId
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



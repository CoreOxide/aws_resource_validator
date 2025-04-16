# Route53 Classes

# AccountLimit

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActivateKeySigningKeyRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ActivateKeySigningKeyResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# AlarmIdentifier

### Region
- **Type**: typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ap-southeast-5', 'ap-southeast-7', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'mx-central-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-west-1', 'us-west-2']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# AliasTarget

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### DNSName
- **Type**: <class 'str'>
- **Required**: Yes

### EvaluateTargetHealth
- **Type**: <class 'bool'>
- **Required**: Yes


# AssociateVPCWithHostedZoneRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPC'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# AssociateVPCWithHostedZoneResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Change

### Action
- **Type**: typing.Literal['CREATE', 'DELETE', 'UPSERT']
- **Required**: Yes

### ResourceRecordSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResourceRecordSetUnion'>
- **Required**: Yes


# ChangeBatch

### Changes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_classes.Change]
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# ChangeCidrCollectionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Changes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.route53_classes.CidrCollectionChange]
- **Required**: Yes

### CollectionVersion
- **Type**: typing.Optional[int]


# ChangeCidrCollectionResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ChangeInfo

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


# ChangeResourceRecordSetsRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeBatch'>
- **Required**: Yes


# ChangeResourceRecordSetsResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ChangeTagsForResourceRequest

### ResourceType
- **Type**: typing.Literal['healthcheck', 'hostedzone']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### AddTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.route53_classes.Tag]]

### RemoveTagKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# CidrBlockSummary

### CidrBlock
- **Type**: typing.Optional[str]

### LocationName
- **Type**: typing.Optional[str]


# CidrCollection

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# CidrCollectionChange

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['DELETE_IF_EXISTS', 'PUT']
- **Required**: Yes

### CidrList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CidrRoutingConfig

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationName
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchAlarmConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53_classes.Dimension]]


# CollectionSummary

### Arn
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]


# Coordinates

### Latitude
- **Type**: <class 'str'>
- **Required**: Yes

### Longitude
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCidrCollectionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes


# CreateHealthCheckRequest

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckConfigUnion'>
- **Required**: Yes


# CreateHealthCheckResponse

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheck'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHostedZoneRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'NoneType'>

### HostedZoneConfig
- **Type**: <class 'NoneType'>

### DelegationSetId
- **Type**: typing.Optional[str]


# CreateHostedZoneResponse

### HostedZone
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZone'>
- **Required**: Yes

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### DelegationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DelegationSet'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPC'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKeySigningKeyRequest

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


# CreateKeySigningKeyResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### KeySigningKey
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.KeySigningKey'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQueryLoggingConfigRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogsLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateQueryLoggingConfigResponse

### QueryLoggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.QueryLoggingConfig'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# CreateReusableDelegationSetRequest

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: typing.Optional[str]


# CreateReusableDelegationSetResponse

### DelegationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DelegationSet'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrafficPolicyInstanceRequest

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


# CreateTrafficPolicyInstanceResponse

### TrafficPolicyInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstance'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrafficPolicyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# CreateTrafficPolicyResponse

### TrafficPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicy'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrafficPolicyVersionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Document
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# CreateTrafficPolicyVersionResponse

### TrafficPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicy'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVPCAssociationAuthorizationRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPC'>
- **Required**: Yes


# CreateVPCAssociationAuthorizationResponse

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPC'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# DNSSECStatus

### ServeSignature
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# DeactivateKeySigningKeyRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeactivateKeySigningKeyResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# DelegationSet

### NameServers
- **Type**: typing.List[str]
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### CallerReference
- **Type**: typing.Optional[str]


# DeleteCidrCollectionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHealthCheckRequest

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostedZoneRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostedZoneResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteKeySigningKeyRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeySigningKeyResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteQueryLoggingConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReusableDelegationSetRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyInstanceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrafficPolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteVPCAssociationAuthorizationRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPC'>
- **Required**: Yes


# Dimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# DisableHostedZoneDNSSECRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableHostedZoneDNSSECResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateVPCFromHostedZoneRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPC
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.VPC'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# DisassociateVPCFromHostedZoneResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# EnableHostedZoneDNSSECRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes


# EnableHostedZoneDNSSECResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GeoLocation

### ContinentCode
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[str]

### SubdivisionCode
- **Type**: typing.Optional[str]


# GeoLocationDetails

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


# GeoProximityLocation

### AWSRegion
- **Type**: typing.Optional[str]

### LocalZoneGroup
- **Type**: typing.Optional[str]

### Coordinates
- **Type**: <class 'NoneType'>

### Bias
- **Type**: typing.Optional[int]


# GetAccountLimitResponse

### Limit
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.AccountLimit'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetChangeRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetChangeRequestWait

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetChangeResponse

### ChangeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ChangeInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetCheckerIpRangesResponse

### CheckerIpRanges
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetDNSSECRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDNSSECResponse

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DNSSECStatus'>
- **Required**: Yes

### KeySigningKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.KeySigningKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetGeoLocationRequest

### ContinentCode
- **Type**: typing.Optional[str]

### CountryCode
- **Type**: typing.Optional[str]

### SubdivisionCode
- **Type**: typing.Optional[str]


# GetGeoLocationResponse

### GeoLocationDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.GeoLocationDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetHealthCheckCountResponse

### HealthCheckCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetHealthCheckLastFailureReasonRequest

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHealthCheckLastFailureReasonResponse

### HealthCheckObservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HealthCheckObservation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetHealthCheckRequest

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHealthCheckResponse

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheck'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetHealthCheckStatusRequest

### HealthCheckId
- **Type**: <class 'str'>
- **Required**: Yes


# GetHealthCheckStatusResponse

### HealthCheckObservations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HealthCheckObservation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetHostedZoneCountResponse

### HostedZoneCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetHostedZoneLimitResponse

### Limit
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZoneLimit'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetHostedZoneRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetHostedZoneResponse

### HostedZone
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZone'>
- **Required**: Yes

### DelegationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DelegationSet'>
- **Required**: Yes

### VPCs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.VPC]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetQueryLoggingConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetQueryLoggingConfigResponse

### QueryLoggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.QueryLoggingConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetReusableDelegationSetLimitResponse

### Limit
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ReusableDelegationSetLimit'>
- **Required**: Yes

### Count
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetReusableDelegationSetRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetReusableDelegationSetResponse

### DelegationSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.DelegationSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrafficPolicyInstanceCountResponse

### TrafficPolicyInstanceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrafficPolicyInstanceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrafficPolicyInstanceResponse

### TrafficPolicyInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrafficPolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes


# GetTrafficPolicyResponse

### TrafficPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# HealthCheck

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### HealthCheckConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheckConfigOutput'>
- **Required**: Yes

### HealthCheckVersion
- **Type**: <class 'int'>
- **Required**: Yes

### LinkedService
- **Type**: <class 'NoneType'>

### CloudWatchAlarmConfiguration
- **Type**: <class 'NoneType'>


# HealthCheckConfigOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HealthCheckConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HealthCheckObservation

### Region
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-west-1', 'sa-east-1', 'us-east-1', 'us-west-1', 'us-west-2']]

### IPAddress
- **Type**: typing.Optional[str]

### StatusReport
- **Type**: <class 'NoneType'>


# HostedZone

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.HostedZoneConfig]

### ResourceRecordSetCount
- **Type**: typing.Optional[int]

### LinkedService
- **Type**: <class 'NoneType'>


# HostedZoneConfig

### Comment
- **Type**: typing.Optional[str]

### PrivateZone
- **Type**: typing.Optional[bool]


# HostedZoneLimit

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HostedZoneOwner

### OwningAccount
- **Type**: typing.Optional[str]

### OwningService
- **Type**: typing.Optional[str]


# HostedZoneSummary

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Owner
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZoneOwner'>
- **Required**: Yes


# KeySigningKey

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


# LinkedService

### ServicePrincipal
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ListCidrBlocksRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListCidrBlocksRequestPaginate

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfig]


# ListCidrBlocksResponse

### CidrBlocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.CidrBlockSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCidrCollectionsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListCidrCollectionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfig]


# ListCidrCollectionsResponse

### CidrCollections
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.CollectionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCidrLocationsRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListCidrLocationsRequestPaginate

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfig]


# ListCidrLocationsResponse

### CidrLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.LocationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGeoLocationsRequest

### StartContinentCode
- **Type**: typing.Optional[str]

### StartCountryCode
- **Type**: typing.Optional[str]

### StartSubdivisionCode
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListGeoLocationsResponse

### GeoLocationDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.GeoLocationDetails]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListHealthChecksRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListHealthChecksRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfig]


# ListHealthChecksResponse

### HealthChecks
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HealthCheck]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListHostedZonesByNameRequest

### DNSName
- **Type**: typing.Optional[str]

### HostedZoneId
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListHostedZonesByNameResponse

### HostedZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HostedZone]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListHostedZonesByVPCRequest

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


# ListHostedZonesByVPCResponse

### HostedZoneSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HostedZoneSummary]
- **Required**: Yes

### MaxItems
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHostedZonesRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]

### DelegationSetId
- **Type**: typing.Optional[str]

### HostedZoneType
- **Type**: typing.Optional[typing.Literal['PrivateHostedZone']]


# ListHostedZonesRequestPaginate

### DelegationSetId
- **Type**: typing.Optional[str]

### HostedZoneType
- **Type**: typing.Optional[typing.Literal['PrivateHostedZone']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfig]


# ListHostedZonesResponse

### HostedZones
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.HostedZone]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListQueryLoggingConfigsRequest

### HostedZoneId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListQueryLoggingConfigsRequestPaginate

### HostedZoneId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfig]


# ListQueryLoggingConfigsResponse

### QueryLoggingConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.QueryLoggingConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceRecordSetsRequest

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


# ListResourceRecordSetsRequestPaginate

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfig]


# ListResourceRecordSetsResponse

### ResourceRecordSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.ResourceRecordSetOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListReusableDelegationSetsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListReusableDelegationSetsResponse

### DelegationSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.DelegationSet]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### ResourceType
- **Type**: typing.Literal['healthcheck', 'hostedzone']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceTagSet
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResourceTagSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourcesRequest

### ResourceType
- **Type**: typing.Literal['healthcheck', 'hostedzone']
- **Required**: Yes

### ResourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ListTagsForResourcesResponse

### ResourceTagSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.ResourceTagSet]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrafficPoliciesRequest

### TrafficPolicyIdMarker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPoliciesResponse

### TrafficPolicySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicySummary]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrafficPolicyInstancesByHostedZoneRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyInstanceNameMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPolicyInstancesByHostedZoneResponse

### TrafficPolicyInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstance]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrafficPolicyInstancesByPolicyRequest

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


# ListTrafficPolicyInstancesByPolicyResponse

### TrafficPolicyInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstance]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrafficPolicyInstancesRequest

### HostedZoneIdMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceNameMarker
- **Type**: typing.Optional[str]

### TrafficPolicyInstanceTypeMarker
- **Type**: typing.Optional[typing.Literal['A', 'AAAA', 'CAA', 'CNAME', 'DS', 'HTTPS', 'MX', 'NAPTR', 'NS', 'PTR', 'SOA', 'SPF', 'SRV', 'SSHFP', 'SVCB', 'TLSA', 'TXT']]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPolicyInstancesResponse

### TrafficPolicyInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstance]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrafficPolicyVersionsRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### TrafficPolicyVersionMarker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListTrafficPolicyVersionsResponse

### TrafficPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.TrafficPolicy]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# ListVPCAssociationAuthorizationsRequest

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[str]


# ListVPCAssociationAuthorizationsRequestPaginate

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.route53_classes.PaginatorConfig]


# ListVPCAssociationAuthorizationsResponse

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### VPCs
- **Type**: typing.List[aws_resource_validator.pydantic_models.route53_classes.VPC]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocationSummary

### LocationName
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QueryLoggingConfig

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogsLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceRecord

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceRecordSetOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceRecordSetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceTagSet

### ResourceType
- **Type**: typing.Optional[typing.Literal['healthcheck', 'hostedzone']]

### ResourceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.route53_classes.Tag]]


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


# ReusableDelegationSetLimit

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StatusReport

### Status
- **Type**: typing.Optional[str]

### CheckedTime
- **Type**: typing.Optional[datetime.datetime]


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TestDNSAnswerRequest

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


# TrafficPolicy

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrafficPolicyInstance

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


# TrafficPolicySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateHealthCheckRequest

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
- **Type**: <class 'NoneType'>

### InsufficientDataHealthStatus
- **Type**: typing.Optional[typing.Literal['Healthy', 'LastKnownStatus', 'Unhealthy']]

### ResetElements
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ChildHealthChecks', 'FullyQualifiedDomainName', 'Regions', 'ResourcePath']]]


# UpdateHealthCheckResponse

### HealthCheck
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HealthCheck'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateHostedZoneCommentRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# UpdateHostedZoneCommentResponse

### HostedZone
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.HostedZone'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrafficPolicyCommentRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateTrafficPolicyCommentResponse

### TrafficPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrafficPolicyInstanceRequest

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


# UpdateTrafficPolicyInstanceResponse

### TrafficPolicyInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.TrafficPolicyInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.route53_classes.ResponseMetadata'>
- **Required**: Yes


# VPC

### VPCRegion
- **Type**: typing.Optional[typing.Literal['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-south-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ap-southeast-4', 'ap-southeast-5', 'ap-southeast-7', 'ca-central-1', 'ca-west-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-central-2', 'eu-north-1', 'eu-south-1', 'eu-south-2', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'il-central-1', 'me-central-1', 'me-south-1', 'mx-central-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-iso-east-1', 'us-iso-west-1', 'us-isob-east-1', 'us-west-1', 'us-west-2']]

### VPCId
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



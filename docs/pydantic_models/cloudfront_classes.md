# Cloudfront Classes

# ActiveTrustedKeyGroups

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.KGKeyPairIds]]


# ActiveTrustedSigners

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.Signer]]


# AliasICPRecordal

### CNAME
- **Type**: typing.Optional[str]

### ICPRecordalStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'PENDING', 'SUSPENDED']]


# Aliases

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# AliasesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# AliasesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AllowedMethods

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes

### CachedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CachedMethodsUnion]


# AllowedMethodsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes

### CachedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CachedMethodsOutput]


# AllowedMethodsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnycastIpList

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AnycastIps
- **Type**: typing.List[str]
- **Required**: Yes

### IpCount
- **Type**: <class 'int'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# AnycastIpListCollection

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.AnycastIpListSummary]]

### NextMarker
- **Type**: typing.Optional[str]


# AnycastIpListSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### IpCount
- **Type**: <class 'int'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# AssociateAliasRequest

### TargetDistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CacheBehavior

### PathPattern
- **Type**: <class 'str'>
- **Required**: Yes

### TargetOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewerProtocolPolicy
- **Type**: typing.Literal['allow-all', 'https-only', 'redirect-to-https']
- **Required**: Yes

### TrustedSigners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersUnion]

### TrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedKeyGroupsUnion]

### AllowedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AllowedMethodsUnion]

### SmoothStreaming
- **Type**: typing.Optional[bool]

### Compress
- **Type**: typing.Optional[bool]

### LambdaFunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationsUnion]

### FunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationsUnion]

### FieldLevelEncryptionId
- **Type**: typing.Optional[str]

### RealtimeLogConfigArn
- **Type**: typing.Optional[str]

### CachePolicyId
- **Type**: typing.Optional[str]

### OriginRequestPolicyId
- **Type**: typing.Optional[str]

### ResponseHeadersPolicyId
- **Type**: typing.Optional[str]

### GrpcConfig
- **Type**: <class 'NoneType'>

### ForwardedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ForwardedValuesUnion]

### MinTTL
- **Type**: typing.Optional[int]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]


# CacheBehaviorOutput

### PathPattern
- **Type**: <class 'str'>
- **Required**: Yes

### TargetOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewerProtocolPolicy
- **Type**: typing.Literal['allow-all', 'https-only', 'redirect-to-https']
- **Required**: Yes

### TrustedSigners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersOutput]

### TrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedKeyGroupsOutput]

### AllowedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AllowedMethodsOutput]

### SmoothStreaming
- **Type**: typing.Optional[bool]

### Compress
- **Type**: typing.Optional[bool]

### LambdaFunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationsOutput]

### FunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationsOutput]

### FieldLevelEncryptionId
- **Type**: typing.Optional[str]

### RealtimeLogConfigArn
- **Type**: typing.Optional[str]

### CachePolicyId
- **Type**: typing.Optional[str]

### OriginRequestPolicyId
- **Type**: typing.Optional[str]

### ResponseHeadersPolicyId
- **Type**: typing.Optional[str]

### GrpcConfig
- **Type**: <class 'NoneType'>

### ForwardedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ForwardedValuesOutput]

### MinTTL
- **Type**: typing.Optional[int]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]


# CacheBehaviorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CacheBehaviors

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorUnion]]


# CacheBehaviorsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorOutput]]


# CacheBehaviorsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CachePolicy

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CachePolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyConfigOutput'>
- **Required**: Yes


# CachePolicyConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MinTTL
- **Type**: <class 'int'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]

### ParametersInCacheKeyAndForwardedToOrigin
- **Type**: <class 'NoneType'>


# CachePolicyConfigOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MinTTL
- **Type**: <class 'int'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]

### ParametersInCacheKeyAndForwardedToOrigin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ParametersInCacheKeyAndForwardedToOriginOutput]


# CachePolicyConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CachePolicyCookiesConfig

### CookieBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNames]


# CachePolicyCookiesConfigOutput

### CookieBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesOutput]


# CachePolicyHeadersConfig

### HeaderBehavior
- **Type**: typing.Literal['none', 'whitelist']
- **Required**: Yes

### Headers
- **Type**: <class 'NoneType'>


# CachePolicyHeadersConfigOutput

### HeaderBehavior
- **Type**: typing.Literal['none', 'whitelist']
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersOutput]


# CachePolicyList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicySummary]]


# CachePolicyQueryStringsConfig

### QueryStringBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### QueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringNames]


# CachePolicyQueryStringsConfigOutput

### QueryStringBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### QueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringNamesOutput]


# CachePolicySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CachedMethods

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes


# CachedMethodsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes


# CachedMethodsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudFrontOriginAccessIdentity

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### S3CanonicalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### CloudFrontOriginAccessIdentityConfig
- **Type**: <class 'NoneType'>


# CloudFrontOriginAccessIdentityConfig

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes


# CloudFrontOriginAccessIdentityList

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentitySummary]]


# CloudFrontOriginAccessIdentitySummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### S3CanonicalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes


# ConflictingAlias

### Alias
- **Type**: typing.Optional[str]

### DistributionId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ConflictingAliasesList

### NextMarker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### Quantity
- **Type**: typing.Optional[int]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ConflictingAlias]]


# ContentTypeProfile

### Format
- **Type**: typing.Literal['URLEncoded']
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: typing.Optional[str]


# ContentTypeProfileConfig

### ForwardWhenContentTypeIsUnknown
- **Type**: <class 'bool'>
- **Required**: Yes

### ContentTypeProfiles
- **Type**: <class 'NoneType'>


# ContentTypeProfileConfigOutput

### ForwardWhenContentTypeIsUnknown
- **Type**: <class 'bool'>
- **Required**: Yes

### ContentTypeProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfilesOutput]


# ContentTypeProfiles

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfile]]


# ContentTypeProfilesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfile]]


# ContinuousDeploymentPolicy

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ContinuousDeploymentPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyConfigOutput'>
- **Required**: Yes


# ContinuousDeploymentPolicyConfig

### StagingDistributionDnsNames
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StagingDistributionDnsNames'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TrafficConfig
- **Type**: <class 'NoneType'>


# ContinuousDeploymentPolicyConfigOutput

### StagingDistributionDnsNames
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StagingDistributionDnsNamesOutput'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TrafficConfig
- **Type**: <class 'NoneType'>


# ContinuousDeploymentPolicyConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContinuousDeploymentPolicyList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicySummary]]


# ContinuousDeploymentPolicySummary

### ContinuousDeploymentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicy'>
- **Required**: Yes


# ContinuousDeploymentSingleHeaderConfig

### Header
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ContinuousDeploymentSingleWeightConfig

### Weight
- **Type**: <class 'float'>
- **Required**: Yes

### SessionStickinessConfig
- **Type**: <class 'NoneType'>


# CookieNames

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# CookieNamesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# CookieNamesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CookiePreference

### Forward
- **Type**: typing.Literal['all', 'none', 'whitelist']
- **Required**: Yes

### WhitelistedNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesUnion]


# CookiePreferenceOutput

### Forward
- **Type**: typing.Literal['all', 'none', 'whitelist']
- **Required**: Yes

### WhitelistedNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesOutput]


# CookiePreferenceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CopyDistributionRequest

### PrimaryDistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Staging
- **Type**: typing.Optional[bool]

### IfMatch
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]


# CopyDistributionResult

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Distribution'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAnycastIpListRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IpCount
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnion]


# CreateAnycastIpListResult

### AnycastIpList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AnycastIpList'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCachePolicyRequest

### CachePolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyConfigUnion'>
- **Required**: Yes


# CreateCachePolicyResult

### CachePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicy'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCloudFrontOriginAccessIdentityRequest

### CloudFrontOriginAccessIdentityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityConfig'>
- **Required**: Yes


# CreateCloudFrontOriginAccessIdentityResult

### CloudFrontOriginAccessIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentity'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContinuousDeploymentPolicyRequest

### ContinuousDeploymentPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyConfigUnion'>
- **Required**: Yes


# CreateContinuousDeploymentPolicyResult

### ContinuousDeploymentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicy'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDistributionRequest

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigUnion'>
- **Required**: Yes


# CreateDistributionResult

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Distribution'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDistributionWithTagsRequest

### DistributionConfigWithTags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigWithTags'>
- **Required**: Yes


# CreateDistributionWithTagsResult

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Distribution'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFieldLevelEncryptionConfigRequest

### FieldLevelEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionConfigUnion'>
- **Required**: Yes


# CreateFieldLevelEncryptionConfigResult

### FieldLevelEncryption
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryption'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFieldLevelEncryptionProfileRequest

### FieldLevelEncryptionProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileConfigUnion'>
- **Required**: Yes


# CreateFieldLevelEncryptionProfileResult

### FieldLevelEncryptionProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfile'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFunctionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionConfigUnion'>
- **Required**: Yes

### FunctionCode
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Blob'>
- **Required**: Yes


# CreateFunctionResult

### FunctionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummary'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInvalidationRequest

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### InvalidationBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationBatchUnion'>
- **Required**: Yes


# CreateInvalidationResult

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### Invalidation
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Invalidation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKeyGroupRequest

### KeyGroupConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupConfigUnion'>
- **Required**: Yes


# CreateKeyGroupResult

### KeyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroup'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKeyValueStoreRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### ImportSource
- **Type**: <class 'NoneType'>


# CreateKeyValueStoreResult

### KeyValueStore
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStore'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMonitoringSubscriptionRequest

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.MonitoringSubscription'>
- **Required**: Yes


# CreateMonitoringSubscriptionResult

### MonitoringSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.MonitoringSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOriginAccessControlRequest

### OriginAccessControlConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlConfig'>
- **Required**: Yes


# CreateOriginAccessControlResult

### OriginAccessControl
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControl'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOriginRequestPolicyRequest

### OriginRequestPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyConfigUnion'>
- **Required**: Yes


# CreateOriginRequestPolicyResult

### OriginRequestPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicy'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePublicKeyRequest

### PublicKeyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyConfig'>
- **Required**: Yes


# CreatePublicKeyResult

### PublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKey'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRealtimeLogConfigRequest

### EndPoints
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.EndPoint]
- **Required**: Yes

### Fields
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SamplingRate
- **Type**: <class 'int'>
- **Required**: Yes


# CreateRealtimeLogConfigResult

### RealtimeLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResponseHeadersPolicyRequest

### ResponseHeadersPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyConfigUnion'>
- **Required**: Yes


# CreateResponseHeadersPolicyResult

### ResponseHeadersPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicy'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamingDistributionRequest

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigUnion'>
- **Required**: Yes


# CreateStreamingDistributionResult

### StreamingDistribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistribution'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamingDistributionWithTagsRequest

### StreamingDistributionConfigWithTags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigWithTags'>
- **Required**: Yes


# CreateStreamingDistributionWithTagsResult

### StreamingDistribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistribution'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVpcOriginRequest

### VpcOriginEndpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginEndpointConfigUnion'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnion]


# CreateVpcOriginResult

### VpcOrigin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOrigin'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# CustomErrorResponse

### ErrorCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponsePagePath
- **Type**: typing.Optional[str]

### ResponseCode
- **Type**: typing.Optional[str]

### ErrorCachingMinTTL
- **Type**: typing.Optional[int]


# CustomErrorResponses

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponse]]


# CustomErrorResponsesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponse]]


# CustomErrorResponsesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomHeaders

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.OriginCustomHeader]]


# CustomHeadersOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginCustomHeader]]


# CustomHeadersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomOriginConfig

### HTTPPort
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPSPort
- **Type**: <class 'int'>
- **Required**: Yes

### OriginProtocolPolicy
- **Type**: typing.Literal['http-only', 'https-only', 'match-viewer']
- **Required**: Yes

### OriginSslProtocols
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginSslProtocolsUnion]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]


# CustomOriginConfigOutput

### HTTPPort
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPSPort
- **Type**: <class 'int'>
- **Required**: Yes

### OriginProtocolPolicy
- **Type**: typing.Literal['http-only', 'https-only', 'match-viewer']
- **Required**: Yes

### OriginSslProtocols
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginSslProtocolsOutput]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]


# CustomOriginConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultCacheBehavior

### TargetOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewerProtocolPolicy
- **Type**: typing.Literal['allow-all', 'https-only', 'redirect-to-https']
- **Required**: Yes

### TrustedSigners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersUnion]

### TrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedKeyGroupsUnion]

### AllowedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AllowedMethodsUnion]

### SmoothStreaming
- **Type**: typing.Optional[bool]

### Compress
- **Type**: typing.Optional[bool]

### LambdaFunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationsUnion]

### FunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationsUnion]

### FieldLevelEncryptionId
- **Type**: typing.Optional[str]

### RealtimeLogConfigArn
- **Type**: typing.Optional[str]

### CachePolicyId
- **Type**: typing.Optional[str]

### OriginRequestPolicyId
- **Type**: typing.Optional[str]

### ResponseHeadersPolicyId
- **Type**: typing.Optional[str]

### GrpcConfig
- **Type**: <class 'NoneType'>

### ForwardedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ForwardedValuesUnion]

### MinTTL
- **Type**: typing.Optional[int]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]


# DefaultCacheBehaviorOutput

### TargetOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewerProtocolPolicy
- **Type**: typing.Literal['allow-all', 'https-only', 'redirect-to-https']
- **Required**: Yes

### TrustedSigners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersOutput]

### TrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedKeyGroupsOutput]

### AllowedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AllowedMethodsOutput]

### SmoothStreaming
- **Type**: typing.Optional[bool]

### Compress
- **Type**: typing.Optional[bool]

### LambdaFunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationsOutput]

### FunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationsOutput]

### FieldLevelEncryptionId
- **Type**: typing.Optional[str]

### RealtimeLogConfigArn
- **Type**: typing.Optional[str]

### CachePolicyId
- **Type**: typing.Optional[str]

### OriginRequestPolicyId
- **Type**: typing.Optional[str]

### ResponseHeadersPolicyId
- **Type**: typing.Optional[str]

### GrpcConfig
- **Type**: <class 'NoneType'>

### ForwardedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ForwardedValuesOutput]

### MinTTL
- **Type**: typing.Optional[int]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]


# DefaultCacheBehaviorUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAnycastIpListRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCachePolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteCloudFrontOriginAccessIdentityRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteContinuousDeploymentPolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteDistributionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteFieldLevelEncryptionConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteFieldLevelEncryptionProfileRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteFunctionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteKeyValueStoreRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitoringSubscriptionRequest

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginAccessControlRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteOriginRequestPolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeletePublicKeyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteRealtimeLogConfigRequest

### Name
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# DeleteResponseHeadersPolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteStreamingDistributionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteVpcOriginRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcOriginResult

### VpcOrigin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOrigin'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFunctionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# DescribeFunctionResult

### FunctionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummary'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeKeyValueStoreRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeKeyValueStoreResult

### KeyValueStore
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStore'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# Distribution

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InProgressInvalidationBatches
- **Type**: <class 'int'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigOutput'>
- **Required**: Yes

### ActiveTrustedSigners
- **Type**: <class 'NoneType'>

### ActiveTrustedKeyGroups
- **Type**: <class 'NoneType'>

### AliasICPRecordals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.AliasICPRecordal]]


# DistributionConfig

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Origins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginsUnion'>
- **Required**: Yes

### DefaultCacheBehavior
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DefaultCacheBehaviorUnion'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AliasesUnion]

### DefaultRootObject
- **Type**: typing.Optional[str]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupsUnion]

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorsUnion]

### CustomErrorResponses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponsesUnion]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LoggingConfig]

### PriceClass
- **Type**: typing.Optional[typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']]

### ViewerCertificate
- **Type**: <class 'NoneType'>

### Restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.RestrictionsUnion]

### WebACLId
- **Type**: typing.Optional[str]

### HttpVersion
- **Type**: typing.Optional[typing.Literal['http1.1', 'http2', 'http2and3', 'http3']]

### IsIPV6Enabled
- **Type**: typing.Optional[bool]

### ContinuousDeploymentPolicyId
- **Type**: typing.Optional[str]

### Staging
- **Type**: typing.Optional[bool]

### AnycastIpListId
- **Type**: typing.Optional[str]


# DistributionConfigOutput

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Origins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginsOutput'>
- **Required**: Yes

### DefaultCacheBehavior
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DefaultCacheBehaviorOutput'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AliasesOutput]

### DefaultRootObject
- **Type**: typing.Optional[str]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupsOutput]

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorsOutput]

### CustomErrorResponses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponsesOutput]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LoggingConfig]

### PriceClass
- **Type**: typing.Optional[typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']]

### ViewerCertificate
- **Type**: <class 'NoneType'>

### Restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.RestrictionsOutput]

### WebACLId
- **Type**: typing.Optional[str]

### HttpVersion
- **Type**: typing.Optional[typing.Literal['http1.1', 'http2', 'http2and3', 'http3']]

### IsIPV6Enabled
- **Type**: typing.Optional[bool]

### ContinuousDeploymentPolicyId
- **Type**: typing.Optional[str]

### Staging
- **Type**: typing.Optional[bool]

### AnycastIpListId
- **Type**: typing.Optional[str]


# DistributionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DistributionConfigWithTags

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigUnion'>
- **Required**: Yes

### Tags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnion'>
- **Required**: Yes


# DistributionIdList

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[str]]


# DistributionList

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.DistributionSummary]]


# DistributionSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AliasesOutput'>
- **Required**: Yes

### Origins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginsOutput'>
- **Required**: Yes

### DefaultCacheBehavior
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DefaultCacheBehaviorOutput'>
- **Required**: Yes

### CacheBehaviors
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorsOutput'>
- **Required**: Yes

### CustomErrorResponses
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponsesOutput'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### PriceClass
- **Type**: typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ViewerCertificate
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ViewerCertificate'>
- **Required**: Yes

### Restrictions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RestrictionsOutput'>
- **Required**: Yes

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### HttpVersion
- **Type**: typing.Literal['http1.1', 'http2', 'http2and3', 'http3']
- **Required**: Yes

### IsIPV6Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Staging
- **Type**: <class 'bool'>
- **Required**: Yes

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupsOutput]

### AliasICPRecordals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.AliasICPRecordal]]

### AnycastIpListId
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionEntities

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntity]]


# EncryptionEntitiesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntityOutput]]


# EncryptionEntity

### PublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderId
- **Type**: <class 'str'>
- **Required**: Yes

### FieldPatterns
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldPatterns'>
- **Required**: Yes


# EncryptionEntityOutput

### PublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderId
- **Type**: <class 'str'>
- **Required**: Yes

### FieldPatterns
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldPatternsOutput'>
- **Required**: Yes


# EndPoint

### StreamType
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisStreamConfig
- **Type**: <class 'NoneType'>


# FieldLevelEncryption

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FieldLevelEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionConfigOutput'>
- **Required**: Yes


# FieldLevelEncryptionConfig

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### QueryArgProfileConfig
- **Type**: <class 'NoneType'>

### ContentTypeProfileConfig
- **Type**: <class 'NoneType'>


# FieldLevelEncryptionConfigOutput

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### QueryArgProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfileConfigOutput]

### ContentTypeProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfileConfigOutput]


# FieldLevelEncryptionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldLevelEncryptionList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionSummary]]


# FieldLevelEncryptionProfile

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FieldLevelEncryptionProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileConfigOutput'>
- **Required**: Yes


# FieldLevelEncryptionProfileConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionEntities
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntities'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# FieldLevelEncryptionProfileConfigOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionEntities
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntitiesOutput'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# FieldLevelEncryptionProfileConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldLevelEncryptionProfileList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileSummary]]


# FieldLevelEncryptionProfileSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionEntities
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntitiesOutput'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# FieldLevelEncryptionSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### QueryArgProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfileConfigOutput]

### ContentTypeProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfileConfigOutput]


# FieldPatterns

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# FieldPatternsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# ForwardedValues

### QueryString
- **Type**: <class 'bool'>
- **Required**: Yes

### Cookies
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CookiePreferenceUnion'>
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersUnion]

### QueryStringCacheKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringCacheKeysUnion]


# ForwardedValuesOutput

### QueryString
- **Type**: <class 'bool'>
- **Required**: Yes

### Cookies
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CookiePreferenceOutput'>
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersOutput]

### QueryStringCacheKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringCacheKeysOutput]


# ForwardedValuesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionAssociation

### FunctionARN
- **Type**: <class 'str'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['origin-request', 'origin-response', 'viewer-request', 'viewer-response']
- **Required**: Yes


# FunctionAssociations

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociation]]


# FunctionAssociationsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociation]]


# FunctionAssociationsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionConfig

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### Runtime
- **Type**: typing.Literal['cloudfront-js-1.0', 'cloudfront-js-2.0']
- **Required**: Yes

### KeyValueStoreAssociations
- **Type**: <class 'NoneType'>


# FunctionConfigOutput

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### Runtime
- **Type**: typing.Literal['cloudfront-js-1.0', 'cloudfront-js-2.0']
- **Required**: Yes

### KeyValueStoreAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreAssociationsOutput]


# FunctionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummary]]


# FunctionMetadata

### FunctionARN
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### CreatedTime
- **Type**: typing.Optional[datetime.datetime]


# FunctionSummary

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionConfigOutput'>
- **Required**: Yes

### FunctionMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionMetadata'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[str]


# GeoRestriction

### RestrictionType
- **Type**: typing.Literal['blacklist', 'none', 'whitelist']
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# GeoRestrictionOutput

### RestrictionType
- **Type**: typing.Literal['blacklist', 'none', 'whitelist']
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# GeoRestrictionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAnycastIpListRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnycastIpListResult

### AnycastIpList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AnycastIpList'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetCachePolicyConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCachePolicyConfigResult

### CachePolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetCachePolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCachePolicyResult

### CachePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicy'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetCloudFrontOriginAccessIdentityConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudFrontOriginAccessIdentityConfigResult

### CloudFrontOriginAccessIdentityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityConfig'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetCloudFrontOriginAccessIdentityRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudFrontOriginAccessIdentityResult

### CloudFrontOriginAccessIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentity'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetContinuousDeploymentPolicyConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetContinuousDeploymentPolicyConfigResult

### ContinuousDeploymentPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetContinuousDeploymentPolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetContinuousDeploymentPolicyResult

### ContinuousDeploymentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicy'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetDistributionConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDistributionConfigResult

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetDistributionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDistributionRequestWait

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetDistributionResult

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Distribution'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetFieldLevelEncryptionConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFieldLevelEncryptionConfigResult

### FieldLevelEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetFieldLevelEncryptionProfileConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFieldLevelEncryptionProfileConfigResult

### FieldLevelEncryptionProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetFieldLevelEncryptionProfileRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFieldLevelEncryptionProfileResult

### FieldLevelEncryptionProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfile'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetFieldLevelEncryptionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFieldLevelEncryptionResult

### FieldLevelEncryption
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryption'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetFunctionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# GetFunctionResult

### FunctionCode
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetInvalidationRequest

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetInvalidationRequestWait

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetInvalidationResult

### Invalidation
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Invalidation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetKeyGroupConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyGroupConfigResult

### KeyGroupConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetKeyGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyGroupResult

### KeyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroup'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetMonitoringSubscriptionRequest

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitoringSubscriptionResult

### MonitoringSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.MonitoringSubscription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetOriginAccessControlConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginAccessControlConfigResult

### OriginAccessControlConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlConfig'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetOriginAccessControlRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginAccessControlResult

### OriginAccessControl
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControl'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetOriginRequestPolicyConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginRequestPolicyConfigResult

### OriginRequestPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetOriginRequestPolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginRequestPolicyResult

### OriginRequestPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicy'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetPublicKeyConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetPublicKeyConfigResult

### PublicKeyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyConfig'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetPublicKeyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetPublicKeyResult

### PublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKey'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetRealtimeLogConfigRequest

### Name
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# GetRealtimeLogConfigResult

### RealtimeLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetResponseHeadersPolicyConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetResponseHeadersPolicyConfigResult

### ResponseHeadersPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetResponseHeadersPolicyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetResponseHeadersPolicyResult

### ResponseHeadersPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicy'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetStreamingDistributionConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamingDistributionConfigResult

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetStreamingDistributionRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamingDistributionRequestWait

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetStreamingDistributionResult

### StreamingDistribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistribution'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GetVpcOriginRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcOriginResult

### VpcOrigin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOrigin'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# GrpcConfig

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# Headers

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# HeadersOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# HeadersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportSource

### SourceType
- **Type**: typing.Literal['S3']
- **Required**: Yes

### SourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# Invalidation

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### InvalidationBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationBatchOutput'>
- **Required**: Yes


# InvalidationBatch

### Paths
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Paths'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes


# InvalidationBatchOutput

### Paths
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PathsOutput'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes


# InvalidationBatchUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InvalidationList

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationSummary]]


# InvalidationSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes


# KGKeyPairIds

### KeyGroupId
- **Type**: typing.Optional[str]

### KeyPairIds
- **Type**: <class 'NoneType'>


# KeyGroup

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KeyGroupConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupConfigOutput'>
- **Required**: Yes


# KeyGroupConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# KeyGroupConfigOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[str]
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# KeyGroupConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeyGroupList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupSummary]]


# KeyGroupSummary

### KeyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroup'>
- **Required**: Yes


# KeyPairIds

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# KeyValueStore

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[str]


# KeyValueStoreAssociation

### KeyValueStoreARN
- **Type**: <class 'str'>
- **Required**: Yes


# KeyValueStoreAssociations

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreAssociation]]


# KeyValueStoreAssociationsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreAssociation]]


# KeyValueStoreList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStore]]


# KinesisStreamConfig

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaFunctionAssociation

### LambdaFunctionARN
- **Type**: <class 'str'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['origin-request', 'origin-response', 'viewer-request', 'viewer-response']
- **Required**: Yes

### IncludeBody
- **Type**: typing.Optional[bool]


# LambdaFunctionAssociations

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociation]]


# LambdaFunctionAssociationsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociation]]


# LambdaFunctionAssociationsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAnycastIpListsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAnycastIpListsResult

### AnycastIpLists
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AnycastIpListCollection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListCachePoliciesResult

### CachePolicyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListCloudFrontOriginAccessIdentitiesRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListCloudFrontOriginAccessIdentitiesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfig]


# ListCloudFrontOriginAccessIdentitiesResult

### CloudFrontOriginAccessIdentityList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListConflictingAliasesRequest

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListConflictingAliasesResult

### ConflictingAliasesList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ConflictingAliasesList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListContinuousDeploymentPoliciesRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListContinuousDeploymentPoliciesResult

### ContinuousDeploymentPolicyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsByAnycastIpListIdRequest

### AnycastIpListId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByAnycastIpListIdResult

### DistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsByCachePolicyIdRequest

### CachePolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByCachePolicyIdResult

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsByKeyGroupRequest

### KeyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByKeyGroupResult

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsByOriginRequestPolicyIdRequest

### OriginRequestPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByOriginRequestPolicyIdResult

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsByRealtimeLogConfigRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]

### RealtimeLogConfigName
- **Type**: typing.Optional[str]

### RealtimeLogConfigArn
- **Type**: typing.Optional[str]


# ListDistributionsByRealtimeLogConfigResult

### DistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsByResponseHeadersPolicyIdRequest

### ResponseHeadersPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByResponseHeadersPolicyIdResult

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsByVpcOriginIdRequest

### VpcOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByVpcOriginIdResult

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsByWebACLIdRequest

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByWebACLIdResult

### DistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListDistributionsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfig]


# ListDistributionsResult

### DistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListFieldLevelEncryptionConfigsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListFieldLevelEncryptionConfigsResult

### FieldLevelEncryptionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListFieldLevelEncryptionProfilesRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListFieldLevelEncryptionProfilesResult

### FieldLevelEncryptionProfileList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListFunctionsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# ListFunctionsResult

### FunctionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListInvalidationsRequest

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListInvalidationsRequestPaginate

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfig]


# ListInvalidationsResult

### InvalidationList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListKeyGroupsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListKeyGroupsResult

### KeyGroupList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListKeyValueStoresRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ListKeyValueStoresRequestPaginate

### Status
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfig]


# ListKeyValueStoresResult

### KeyValueStoreList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListOriginAccessControlsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListOriginAccessControlsResult

### OriginAccessControlList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListOriginRequestPoliciesResult

### OriginRequestPolicyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListPublicKeysRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListPublicKeysRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfig]


# ListPublicKeysResult

### PublicKeyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListRealtimeLogConfigsRequest

### MaxItems
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]


# ListRealtimeLogConfigsResult

### RealtimeLogConfigs
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfigs'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListResponseHeadersPoliciesResult

### ResponseHeadersPolicyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListStreamingDistributionsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListStreamingDistributionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfig]


# ListStreamingDistributionsResult

### StreamingDistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### Resource
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResult

### Tags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ListVpcOriginsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListVpcOriginsResult

### VpcOriginList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginList'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingConfig

### Enabled
- **Type**: typing.Optional[bool]

### IncludeCookies
- **Type**: typing.Optional[bool]

### Bucket
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]


# MonitoringSubscription

### RealtimeMetricsSubscriptionConfig
- **Type**: <class 'NoneType'>


# Origin

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginPath
- **Type**: typing.Optional[str]

### CustomHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomHeadersUnion]

### S3OriginConfig
- **Type**: <class 'NoneType'>

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomOriginConfigUnion]

### VpcOriginConfig
- **Type**: <class 'NoneType'>

### ConnectionAttempts
- **Type**: typing.Optional[int]

### ConnectionTimeout
- **Type**: typing.Optional[int]

### OriginShield
- **Type**: <class 'NoneType'>

### OriginAccessControlId
- **Type**: typing.Optional[str]


# OriginAccessControl

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### OriginAccessControlConfig
- **Type**: <class 'NoneType'>


# OriginAccessControlConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SigningProtocol
- **Type**: typing.Literal['sigv4']
- **Required**: Yes

### SigningBehavior
- **Type**: typing.Literal['always', 'never', 'no-override']
- **Required**: Yes

### OriginAccessControlOriginType
- **Type**: typing.Literal['lambda', 'mediapackagev2', 'mediastore', 's3']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# OriginAccessControlList

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlSummary]]


# OriginAccessControlSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SigningProtocol
- **Type**: typing.Literal['sigv4']
- **Required**: Yes

### SigningBehavior
- **Type**: typing.Literal['always', 'never', 'no-override']
- **Required**: Yes

### OriginAccessControlOriginType
- **Type**: typing.Literal['lambda', 'mediapackagev2', 'mediastore', 's3']
- **Required**: Yes


# OriginCustomHeader

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### HeaderValue
- **Type**: <class 'str'>
- **Required**: Yes


# OriginGroup

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### FailoverCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupFailoverCriteriaUnion'>
- **Required**: Yes

### Members
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupMembersUnion'>
- **Required**: Yes

### SelectionCriteria
- **Type**: typing.Optional[typing.Literal['default', 'media-quality-based']]


# OriginGroupFailoverCriteria

### StatusCodes
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StatusCodesUnion'>
- **Required**: Yes


# OriginGroupFailoverCriteriaOutput

### StatusCodes
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StatusCodesOutput'>
- **Required**: Yes


# OriginGroupFailoverCriteriaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginGroupMember

### OriginId
- **Type**: <class 'str'>
- **Required**: Yes


# OriginGroupMembers

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupMember]
- **Required**: Yes


# OriginGroupMembersOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupMember]
- **Required**: Yes


# OriginGroupMembersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginGroupOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### FailoverCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupFailoverCriteriaOutput'>
- **Required**: Yes

### Members
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupMembersOutput'>
- **Required**: Yes

### SelectionCriteria
- **Type**: typing.Optional[typing.Literal['default', 'media-quality-based']]


# OriginGroupUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginGroups

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupUnion]]


# OriginGroupsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupOutput]]


# OriginGroupsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginOutput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginPath
- **Type**: typing.Optional[str]

### CustomHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomHeadersOutput]

### S3OriginConfig
- **Type**: <class 'NoneType'>

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomOriginConfigOutput]

### VpcOriginConfig
- **Type**: <class 'NoneType'>

### ConnectionAttempts
- **Type**: typing.Optional[int]

### ConnectionTimeout
- **Type**: typing.Optional[int]

### OriginShield
- **Type**: <class 'NoneType'>

### OriginAccessControlId
- **Type**: typing.Optional[str]


# OriginRequestPolicy

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OriginRequestPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyConfigOutput'>
- **Required**: Yes


# OriginRequestPolicyConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HeadersConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyHeadersConfig'>
- **Required**: Yes

### CookiesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyCookiesConfig'>
- **Required**: Yes

### QueryStringsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyQueryStringsConfig'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# OriginRequestPolicyConfigOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HeadersConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyHeadersConfigOutput'>
- **Required**: Yes

### CookiesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyCookiesConfigOutput'>
- **Required**: Yes

### QueryStringsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyQueryStringsConfigOutput'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# OriginRequestPolicyConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginRequestPolicyCookiesConfig

### CookieBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNames]


# OriginRequestPolicyCookiesConfigOutput

### CookieBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesOutput]


# OriginRequestPolicyHeadersConfig

### HeaderBehavior
- **Type**: typing.Literal['allExcept', 'allViewer', 'allViewerAndWhitelistCloudFront', 'none', 'whitelist']
- **Required**: Yes

### Headers
- **Type**: <class 'NoneType'>


# OriginRequestPolicyHeadersConfigOutput

### HeaderBehavior
- **Type**: typing.Literal['allExcept', 'allViewer', 'allViewerAndWhitelistCloudFront', 'none', 'whitelist']
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersOutput]


# OriginRequestPolicyList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicySummary]]


# OriginRequestPolicyQueryStringsConfig

### QueryStringBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### QueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringNames]


# OriginRequestPolicyQueryStringsConfigOutput

### QueryStringBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### QueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringNamesOutput]


# OriginRequestPolicySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginShield

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OriginShieldRegion
- **Type**: typing.Optional[str]


# OriginSslProtocols

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Literal['SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2']]
- **Required**: Yes


# OriginSslProtocolsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Literal['SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2']]
- **Required**: Yes


# OriginSslProtocolsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Origins

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.OriginUnion]
- **Required**: Yes


# OriginsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginOutput]
- **Required**: Yes


# OriginsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParametersInCacheKeyAndForwardedToOrigin

### EnableAcceptEncodingGzip
- **Type**: <class 'bool'>
- **Required**: Yes

### HeadersConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyHeadersConfig'>
- **Required**: Yes

### CookiesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyCookiesConfig'>
- **Required**: Yes

### QueryStringsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyQueryStringsConfig'>
- **Required**: Yes

### EnableAcceptEncodingBrotli
- **Type**: typing.Optional[bool]


# ParametersInCacheKeyAndForwardedToOriginOutput

### EnableAcceptEncodingGzip
- **Type**: <class 'bool'>
- **Required**: Yes

### HeadersConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyHeadersConfigOutput'>
- **Required**: Yes

### CookiesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyCookiesConfigOutput'>
- **Required**: Yes

### QueryStringsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyQueryStringsConfigOutput'>
- **Required**: Yes

### EnableAcceptEncodingBrotli
- **Type**: typing.Optional[bool]


# Paths

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# PathsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# PublicKey

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PublicKeyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyConfig'>
- **Required**: Yes


# PublicKeyConfig

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EncodedKey
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# PublicKeyList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeySummary]]


# PublicKeySummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EncodedKey
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# PublishFunctionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# PublishFunctionResult

### FunctionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# QueryArgProfile

### QueryArg
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# QueryArgProfileConfig

### ForwardWhenQueryArgProfileIsUnknown
- **Type**: <class 'bool'>
- **Required**: Yes

### QueryArgProfiles
- **Type**: <class 'NoneType'>


# QueryArgProfileConfigOutput

### ForwardWhenQueryArgProfileIsUnknown
- **Type**: <class 'bool'>
- **Required**: Yes

### QueryArgProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfilesOutput]


# QueryArgProfiles

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfile]]


# QueryArgProfilesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfile]]


# QueryStringCacheKeys

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# QueryStringCacheKeysOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# QueryStringCacheKeysUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryStringNames

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# QueryStringNamesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# RealtimeLogConfig

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SamplingRate
- **Type**: <class 'int'>
- **Required**: Yes

### EndPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.EndPoint]
- **Required**: Yes

### Fields
- **Type**: typing.List[str]
- **Required**: Yes


# RealtimeLogConfigs

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfig]]

### NextMarker
- **Type**: typing.Optional[str]


# RealtimeMetricsSubscriptionConfig

### RealtimeMetricsSubscriptionStatus
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# ResponseHeadersPolicy

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseHeadersPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyConfigOutput'>
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowHeaders

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowHeadersOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowMethods

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Literal['ALL', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowMethodsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Literal['ALL', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowOrigins

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowOriginsOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlExposeHeaders

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# ResponseHeadersPolicyAccessControlExposeHeadersOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# ResponseHeadersPolicyConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### CorsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCorsConfig]

### SecurityHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicySecurityHeadersConfig]

### ServerTimingHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyServerTimingHeadersConfig]

### CustomHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCustomHeadersConfig]

### RemoveHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyRemoveHeadersConfig]


# ResponseHeadersPolicyConfigOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### CorsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCorsConfigOutput]

### SecurityHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicySecurityHeadersConfig]

### ServerTimingHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyServerTimingHeadersConfig]

### CustomHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCustomHeadersConfigOutput]

### RemoveHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyRemoveHeadersConfigOutput]


# ResponseHeadersPolicyConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseHeadersPolicyContentSecurityPolicy

### Override
- **Type**: <class 'bool'>
- **Required**: Yes

### ContentSecurityPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# ResponseHeadersPolicyContentTypeOptions

### Override
- **Type**: <class 'bool'>
- **Required**: Yes


# ResponseHeadersPolicyCorsConfig

### AccessControlAllowOrigins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowOrigins'>
- **Required**: Yes

### AccessControlAllowHeaders
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowHeaders'>
- **Required**: Yes

### AccessControlAllowMethods
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowMethods'>
- **Required**: Yes

### AccessControlAllowCredentials
- **Type**: <class 'bool'>
- **Required**: Yes

### OriginOverride
- **Type**: <class 'bool'>
- **Required**: Yes

### AccessControlExposeHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlExposeHeaders]

### AccessControlMaxAgeSec
- **Type**: typing.Optional[int]


# ResponseHeadersPolicyCorsConfigOutput

### AccessControlAllowOrigins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowOriginsOutput'>
- **Required**: Yes

### AccessControlAllowHeaders
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowHeadersOutput'>
- **Required**: Yes

### AccessControlAllowMethods
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowMethodsOutput'>
- **Required**: Yes

### AccessControlAllowCredentials
- **Type**: <class 'bool'>
- **Required**: Yes

### OriginOverride
- **Type**: <class 'bool'>
- **Required**: Yes

### AccessControlExposeHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlExposeHeadersOutput]

### AccessControlMaxAgeSec
- **Type**: typing.Optional[int]


# ResponseHeadersPolicyCustomHeader

### Header
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Override
- **Type**: <class 'bool'>
- **Required**: Yes


# ResponseHeadersPolicyCustomHeadersConfig

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCustomHeader]]


# ResponseHeadersPolicyCustomHeadersConfigOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCustomHeader]]


# ResponseHeadersPolicyFrameOptions

### Override
- **Type**: <class 'bool'>
- **Required**: Yes

### FrameOption
- **Type**: typing.Literal['DENY', 'SAMEORIGIN']
- **Required**: Yes


# ResponseHeadersPolicyList

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicySummary]]


# ResponseHeadersPolicyReferrerPolicy

### Override
- **Type**: <class 'bool'>
- **Required**: Yes

### ReferrerPolicy
- **Type**: typing.Literal['no-referrer', 'no-referrer-when-downgrade', 'origin', 'origin-when-cross-origin', 'same-origin', 'strict-origin', 'strict-origin-when-cross-origin', 'unsafe-url']
- **Required**: Yes


# ResponseHeadersPolicyRemoveHeader

### Header
- **Type**: <class 'str'>
- **Required**: Yes


# ResponseHeadersPolicyRemoveHeadersConfig

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyRemoveHeader]]


# ResponseHeadersPolicyRemoveHeadersConfigOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyRemoveHeader]]


# ResponseHeadersPolicySecurityHeadersConfig

### XSSProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyXSSProtection]

### FrameOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyFrameOptions]

### ReferrerPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyReferrerPolicy]

### ContentSecurityPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyContentSecurityPolicy]

### ContentTypeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyContentTypeOptions]

### StrictTransportSecurity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyStrictTransportSecurity]


# ResponseHeadersPolicyServerTimingHeadersConfig

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SamplingRate
- **Type**: typing.Optional[float]


# ResponseHeadersPolicyStrictTransportSecurity

### Override
- **Type**: <class 'bool'>
- **Required**: Yes

### AccessControlMaxAgeSec
- **Type**: <class 'int'>
- **Required**: Yes

### IncludeSubdomains
- **Type**: typing.Optional[bool]

### Preload
- **Type**: typing.Optional[bool]


# ResponseHeadersPolicySummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseHeadersPolicyXSSProtection

### Override
- **Type**: <class 'bool'>
- **Required**: Yes

### Protection
- **Type**: <class 'bool'>
- **Required**: Yes

### ModeBlock
- **Type**: typing.Optional[bool]

### ReportUri
- **Type**: typing.Optional[str]


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


# Restrictions

### GeoRestriction
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.GeoRestrictionUnion'>
- **Required**: Yes


# RestrictionsOutput

### GeoRestriction
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.GeoRestrictionOutput'>
- **Required**: Yes


# RestrictionsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3Origin

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginAccessIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# S3OriginConfig

### OriginAccessIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# SessionStickinessConfig

### IdleTTL
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumTTL
- **Type**: <class 'int'>
- **Required**: Yes


# Signer

### AwsAccountNumber
- **Type**: typing.Optional[str]

### KeyPairIds
- **Type**: <class 'NoneType'>


# StagingDistributionDnsNames

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# StagingDistributionDnsNamesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# StatusCodes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[int]
- **Required**: Yes


# StatusCodesOutput

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[int]
- **Required**: Yes


# StatusCodesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StreamingDistribution

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveTrustedSigners
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ActiveTrustedSigners'>
- **Required**: Yes

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigOutput'>
- **Required**: Yes

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# StreamingDistributionConfig

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### S3Origin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.S3Origin'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedSigners
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersUnion'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AliasesUnion]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.StreamingLoggingConfig]

### PriceClass
- **Type**: typing.Optional[typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']]


# StreamingDistributionConfigOutput

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### S3Origin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.S3Origin'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedSigners
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersOutput'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AliasesOutput]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.StreamingLoggingConfig]

### PriceClass
- **Type**: typing.Optional[typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']]


# StreamingDistributionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StreamingDistributionConfigWithTags

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigUnion'>
- **Required**: Yes

### Tags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnion'>
- **Required**: Yes


# StreamingDistributionList

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionSummary]]


# StreamingDistributionSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Origin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.S3Origin'>
- **Required**: Yes

### Aliases
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AliasesOutput'>
- **Required**: Yes

### TrustedSigners
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersOutput'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### PriceClass
- **Type**: typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# StreamingLoggingConfig

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagKeys

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# TagResourceRequest

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnion'>
- **Required**: Yes


# Tags

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.Tag]]


# TagsOutput

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.Tag]]


# TagsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TestFunctionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes

### EventObject
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Blob'>
- **Required**: Yes

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# TestFunctionResult

### TestResult
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TestResult'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# TestResult

### FunctionSummary
- **Type**: <class 'NoneType'>

### ComputeUtilization
- **Type**: typing.Optional[str]

### FunctionExecutionLogs
- **Type**: typing.Optional[typing.List[str]]

### FunctionErrorMessage
- **Type**: typing.Optional[str]

### FunctionOutput
- **Type**: typing.Optional[str]


# TrafficConfig

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrustedKeyGroups

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# TrustedKeyGroupsOutput

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# TrustedKeyGroupsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrustedSigners

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# TrustedSignersOutput

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# TrustedSignersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagKeys'>
- **Required**: Yes


# UpdateCachePolicyRequest

### CachePolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateCachePolicyResult

### CachePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicy'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateCloudFrontOriginAccessIdentityRequest

### CloudFrontOriginAccessIdentityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityConfig'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateCloudFrontOriginAccessIdentityResult

### CloudFrontOriginAccessIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentity'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContinuousDeploymentPolicyRequest

### ContinuousDeploymentPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateContinuousDeploymentPolicyResult

### ContinuousDeploymentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicy'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDistributionRequest

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateDistributionResult

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Distribution'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDistributionWithStagingConfigRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### StagingDistributionId
- **Type**: typing.Optional[str]

### IfMatch
- **Type**: typing.Optional[str]


# UpdateDistributionWithStagingConfigResult

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Distribution'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFieldLevelEncryptionConfigRequest

### FieldLevelEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateFieldLevelEncryptionConfigResult

### FieldLevelEncryption
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryption'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFieldLevelEncryptionProfileRequest

### FieldLevelEncryptionProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateFieldLevelEncryptionProfileResult

### FieldLevelEncryptionProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfile'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFunctionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionConfigUnion'>
- **Required**: Yes

### FunctionCode
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.Blob'>
- **Required**: Yes


# UpdateFunctionResult

### FunctionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummary'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKeyGroupRequest

### KeyGroupConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateKeyGroupResult

### KeyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroup'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKeyValueStoreRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateKeyValueStoreResult

### KeyValueStore
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStore'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateOriginAccessControlRequest

### OriginAccessControlConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlConfig'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateOriginAccessControlResult

### OriginAccessControl
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControl'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateOriginRequestPolicyRequest

### OriginRequestPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateOriginRequestPolicyResult

### OriginRequestPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicy'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePublicKeyRequest

### PublicKeyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyConfig'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdatePublicKeyResult

### PublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKey'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRealtimeLogConfigRequest

### EndPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.EndPoint]]

### Fields
- **Type**: typing.Optional[typing.Sequence[str]]

### Name
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### SamplingRate
- **Type**: typing.Optional[int]


# UpdateRealtimeLogConfigResult

### RealtimeLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResponseHeadersPolicyRequest

### ResponseHeadersPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateResponseHeadersPolicyResult

### ResponseHeadersPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicy'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStreamingDistributionRequest

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateStreamingDistributionResult

### StreamingDistribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistribution'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVpcOriginRequest

### VpcOriginEndpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginEndpointConfigUnion'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateVpcOriginResult

### VpcOrigin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOrigin'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadata'>
- **Required**: Yes


# ViewerCertificate

### CloudFrontDefaultCertificate
- **Type**: typing.Optional[bool]

### IAMCertificateId
- **Type**: typing.Optional[str]

### ACMCertificateArn
- **Type**: typing.Optional[str]

### SSLSupportMethod
- **Type**: typing.Optional[typing.Literal['sni-only', 'static-ip', 'vip']]

### MinimumProtocolVersion
- **Type**: typing.Optional[typing.Literal['SSLv3', 'TLSv1', 'TLSv1.1_2016', 'TLSv1.2_2018', 'TLSv1.2_2019', 'TLSv1.2_2021', 'TLSv1_2016']]

### Certificate
- **Type**: typing.Optional[str]

### CertificateSource
- **Type**: typing.Optional[typing.Literal['acm', 'cloudfront', 'iam']]


# VpcOrigin

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### VpcOriginEndpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginEndpointConfigOutput'>
- **Required**: Yes


# VpcOriginConfig

### VpcOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]


# VpcOriginEndpointConfig

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPPort
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPSPort
- **Type**: <class 'int'>
- **Required**: Yes

### OriginProtocolPolicy
- **Type**: typing.Literal['http-only', 'https-only', 'match-viewer']
- **Required**: Yes

### OriginSslProtocols
- **Type**: <class 'NoneType'>


# VpcOriginEndpointConfigOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPPort
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPSPort
- **Type**: <class 'int'>
- **Required**: Yes

### OriginProtocolPolicy
- **Type**: typing.Literal['http-only', 'https-only', 'match-viewer']
- **Required**: Yes

### OriginSslProtocols
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginSslProtocolsOutput]


# VpcOriginEndpointConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcOriginList

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginSummary]]


# VpcOriginSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



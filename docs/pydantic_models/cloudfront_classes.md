# Cloudfront Classes

# ActiveTrustedKeyGroupsTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.KGKeyPairIdsTypeDef]]


# ActiveTrustedSignersTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.SignerTypeDef]]


# AliasICPRecordalTypeDef

### CNAME
- **Type**: typing.Optional[str]

### ICPRecordalStatus
- **Type**: typing.Optional[typing.Literal['APPROVED', 'PENDING', 'SUSPENDED']]


# AliasesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# AliasesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# AliasesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AllowedMethodsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes

### CachedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CachedMethodsOutputTypeDef]


# AllowedMethodsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes

### CachedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CachedMethodsUnionTypeDef]


# AllowedMethodsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnycastIpListCollectionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.AnycastIpListSummaryTypeDef]]

### NextMarker
- **Type**: typing.Optional[str]


# AnycastIpListSummaryTypeDef

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


# AnycastIpListTypeDef

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


# AssociateAliasRequestTypeDef

### TargetDistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CacheBehaviorOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersOutputTypeDef]

### TrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedKeyGroupsOutputTypeDef]

### AllowedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AllowedMethodsOutputTypeDef]

### SmoothStreaming
- **Type**: typing.Optional[bool]

### Compress
- **Type**: typing.Optional[bool]

### LambdaFunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationsOutputTypeDef]

### FunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationsOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.GrpcConfigTypeDef]

### ForwardedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ForwardedValuesOutputTypeDef]

### MinTTL
- **Type**: typing.Optional[int]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]


# CacheBehaviorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersUnionTypeDef]

### TrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedKeyGroupsUnionTypeDef]

### AllowedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AllowedMethodsUnionTypeDef]

### SmoothStreaming
- **Type**: typing.Optional[bool]

### Compress
- **Type**: typing.Optional[bool]

### LambdaFunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationsUnionTypeDef]

### FunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationsUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.GrpcConfigTypeDef]

### ForwardedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ForwardedValuesUnionTypeDef]

### MinTTL
- **Type**: typing.Optional[int]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]


# CacheBehaviorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CacheBehaviorsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorOutputTypeDef]]


# CacheBehaviorsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorUnionTypeDef]]


# CacheBehaviorsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CachePolicyConfigOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ParametersInCacheKeyAndForwardedToOriginOutputTypeDef]


# CachePolicyConfigTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ParametersInCacheKeyAndForwardedToOriginTypeDef]


# CachePolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CachePolicyCookiesConfigOutputTypeDef

### CookieBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesOutputTypeDef]


# CachePolicyCookiesConfigTypeDef

### CookieBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesTypeDef]


# CachePolicyHeadersConfigOutputTypeDef

### HeaderBehavior
- **Type**: typing.Literal['none', 'whitelist']
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersOutputTypeDef]


# CachePolicyHeadersConfigTypeDef

### HeaderBehavior
- **Type**: typing.Literal['none', 'whitelist']
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersTypeDef]


# CachePolicyListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicySummaryTypeDef]]


# CachePolicyQueryStringsConfigOutputTypeDef

### QueryStringBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### QueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringNamesOutputTypeDef]


# CachePolicyQueryStringsConfigTypeDef

### QueryStringBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### QueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringNamesTypeDef]


# CachePolicySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CachePolicyTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CachePolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyConfigOutputTypeDef'>
- **Required**: Yes


# CachedMethodsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes


# CachedMethodsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Literal['DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes


# CachedMethodsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudFrontOriginAccessIdentityConfigTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes


# CloudFrontOriginAccessIdentityListTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentitySummaryTypeDef]]


# CloudFrontOriginAccessIdentitySummaryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### S3CanonicalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes


# CloudFrontOriginAccessIdentityTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### S3CanonicalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### CloudFrontOriginAccessIdentityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityConfigTypeDef]


# ConflictingAliasTypeDef

### Alias
- **Type**: typing.Optional[str]

### DistributionId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ConflictingAliasesListTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### Quantity
- **Type**: typing.Optional[int]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ConflictingAliasTypeDef]]


# ContentTypeProfileConfigOutputTypeDef

### ForwardWhenContentTypeIsUnknown
- **Type**: <class 'bool'>
- **Required**: Yes

### ContentTypeProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfilesOutputTypeDef]


# ContentTypeProfileConfigTypeDef

### ForwardWhenContentTypeIsUnknown
- **Type**: <class 'bool'>
- **Required**: Yes

### ContentTypeProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfilesTypeDef]


# ContentTypeProfileTypeDef

### Format
- **Type**: typing.Literal['URLEncoded']
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: typing.Optional[str]


# ContentTypeProfilesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfileTypeDef]]


# ContentTypeProfilesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfileTypeDef]]


# ContinuousDeploymentPolicyConfigOutputTypeDef

### StagingDistributionDnsNames
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StagingDistributionDnsNamesOutputTypeDef'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TrafficConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrafficConfigTypeDef]


# ContinuousDeploymentPolicyConfigTypeDef

### StagingDistributionDnsNames
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StagingDistributionDnsNamesTypeDef'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### TrafficConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrafficConfigTypeDef]


# ContinuousDeploymentPolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContinuousDeploymentPolicyListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicySummaryTypeDef]]


# ContinuousDeploymentPolicySummaryTypeDef

### ContinuousDeploymentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyTypeDef'>
- **Required**: Yes


# ContinuousDeploymentPolicyTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ContinuousDeploymentPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyConfigOutputTypeDef'>
- **Required**: Yes


# ContinuousDeploymentSingleHeaderConfigTypeDef

### Header
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ContinuousDeploymentSingleWeightConfigTypeDef

### Weight
- **Type**: <class 'float'>
- **Required**: Yes

### SessionStickinessConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.SessionStickinessConfigTypeDef]


# CookieNamesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# CookieNamesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# CookieNamesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CookiePreferenceOutputTypeDef

### Forward
- **Type**: typing.Literal['all', 'none', 'whitelist']
- **Required**: Yes

### WhitelistedNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesOutputTypeDef]


# CookiePreferenceTypeDef

### Forward
- **Type**: typing.Literal['all', 'none', 'whitelist']
- **Required**: Yes

### WhitelistedNames
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesUnionTypeDef]


# CookiePreferenceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CopyDistributionRequestTypeDef

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


# CopyDistributionResultTypeDef

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAnycastIpListRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IpCount
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnionTypeDef]


# CreateAnycastIpListResultTypeDef

### AnycastIpList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AnycastIpListTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCachePolicyRequestTypeDef

### CachePolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyConfigUnionTypeDef'>
- **Required**: Yes


# CreateCachePolicyResultTypeDef

### CachePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCloudFrontOriginAccessIdentityRequestTypeDef

### CloudFrontOriginAccessIdentityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityConfigTypeDef'>
- **Required**: Yes


# CreateCloudFrontOriginAccessIdentityResultTypeDef

### CloudFrontOriginAccessIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContinuousDeploymentPolicyRequestTypeDef

### ContinuousDeploymentPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyConfigUnionTypeDef'>
- **Required**: Yes


# CreateContinuousDeploymentPolicyResultTypeDef

### ContinuousDeploymentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDistributionRequestTypeDef

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigUnionTypeDef'>
- **Required**: Yes


# CreateDistributionResultTypeDef

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDistributionWithTagsRequestTypeDef

### DistributionConfigWithTags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigWithTagsTypeDef'>
- **Required**: Yes


# CreateDistributionWithTagsResultTypeDef

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFieldLevelEncryptionConfigRequestTypeDef

### FieldLevelEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionConfigUnionTypeDef'>
- **Required**: Yes


# CreateFieldLevelEncryptionConfigResultTypeDef

### FieldLevelEncryption
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFieldLevelEncryptionProfileRequestTypeDef

### FieldLevelEncryptionProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileConfigUnionTypeDef'>
- **Required**: Yes


# CreateFieldLevelEncryptionProfileResultTypeDef

### FieldLevelEncryptionProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFunctionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionConfigUnionTypeDef'>
- **Required**: Yes

### FunctionCode
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.BlobTypeDef'>
- **Required**: Yes


# CreateFunctionResultTypeDef

### FunctionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummaryTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInvalidationRequestTypeDef

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### InvalidationBatch
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationBatchUnionTypeDef'>
- **Required**: Yes


# CreateInvalidationResultTypeDef

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### Invalidation
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKeyGroupRequestTypeDef

### KeyGroupConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupConfigUnionTypeDef'>
- **Required**: Yes


# CreateKeyGroupResultTypeDef

### KeyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKeyValueStoreRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### ImportSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ImportSourceTypeDef]


# CreateKeyValueStoreResultTypeDef

### KeyValueStore
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMonitoringSubscriptionRequestTypeDef

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### MonitoringSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.MonitoringSubscriptionTypeDef'>
- **Required**: Yes


# CreateMonitoringSubscriptionResultTypeDef

### MonitoringSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.MonitoringSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOriginAccessControlRequestTypeDef

### OriginAccessControlConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlConfigTypeDef'>
- **Required**: Yes


# CreateOriginAccessControlResultTypeDef

### OriginAccessControl
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOriginRequestPolicyRequestTypeDef

### OriginRequestPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyConfigUnionTypeDef'>
- **Required**: Yes


# CreateOriginRequestPolicyResultTypeDef

### OriginRequestPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePublicKeyRequestTypeDef

### PublicKeyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyConfigTypeDef'>
- **Required**: Yes


# CreatePublicKeyResultTypeDef

### PublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRealtimeLogConfigRequestTypeDef

### EndPoints
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.EndPointTypeDef]
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


# CreateRealtimeLogConfigResultTypeDef

### RealtimeLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResponseHeadersPolicyRequestTypeDef

### ResponseHeadersPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyConfigUnionTypeDef'>
- **Required**: Yes


# CreateResponseHeadersPolicyResultTypeDef

### ResponseHeadersPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamingDistributionRequestTypeDef

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigUnionTypeDef'>
- **Required**: Yes


# CreateStreamingDistributionResultTypeDef

### StreamingDistribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamingDistributionWithTagsRequestTypeDef

### StreamingDistributionConfigWithTags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigWithTagsTypeDef'>
- **Required**: Yes


# CreateStreamingDistributionWithTagsResultTypeDef

### StreamingDistribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVpcOriginRequestTypeDef

### VpcOriginEndpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginEndpointConfigUnionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnionTypeDef]


# CreateVpcOriginResultTypeDef

### VpcOrigin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomErrorResponseTypeDef

### ErrorCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponsePagePath
- **Type**: typing.Optional[str]

### ResponseCode
- **Type**: typing.Optional[str]

### ErrorCachingMinTTL
- **Type**: typing.Optional[int]


# CustomErrorResponsesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponseTypeDef]]


# CustomErrorResponsesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponseTypeDef]]


# CustomErrorResponsesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomHeadersOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginCustomHeaderTypeDef]]


# CustomHeadersTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.OriginCustomHeaderTypeDef]]


# CustomHeadersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomOriginConfigOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginSslProtocolsOutputTypeDef]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]


# CustomOriginConfigTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginSslProtocolsUnionTypeDef]

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]


# CustomOriginConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DefaultCacheBehaviorOutputTypeDef

### TargetOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewerProtocolPolicy
- **Type**: typing.Literal['allow-all', 'https-only', 'redirect-to-https']
- **Required**: Yes

### TrustedSigners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersOutputTypeDef]

### TrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedKeyGroupsOutputTypeDef]

### AllowedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AllowedMethodsOutputTypeDef]

### SmoothStreaming
- **Type**: typing.Optional[bool]

### Compress
- **Type**: typing.Optional[bool]

### LambdaFunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationsOutputTypeDef]

### FunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationsOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.GrpcConfigTypeDef]

### ForwardedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ForwardedValuesOutputTypeDef]

### MinTTL
- **Type**: typing.Optional[int]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]


# DefaultCacheBehaviorTypeDef

### TargetOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### ViewerProtocolPolicy
- **Type**: typing.Literal['allow-all', 'https-only', 'redirect-to-https']
- **Required**: Yes

### TrustedSigners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersUnionTypeDef]

### TrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.TrustedKeyGroupsUnionTypeDef]

### AllowedMethods
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AllowedMethodsUnionTypeDef]

### SmoothStreaming
- **Type**: typing.Optional[bool]

### Compress
- **Type**: typing.Optional[bool]

### LambdaFunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationsUnionTypeDef]

### FunctionAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationsUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.GrpcConfigTypeDef]

### ForwardedValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ForwardedValuesUnionTypeDef]

### MinTTL
- **Type**: typing.Optional[int]

### DefaultTTL
- **Type**: typing.Optional[int]

### MaxTTL
- **Type**: typing.Optional[int]


# DefaultCacheBehaviorUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAnycastIpListRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCachePolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteCloudFrontOriginAccessIdentityRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteContinuousDeploymentPolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteDistributionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteFieldLevelEncryptionConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteFieldLevelEncryptionProfileRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteFunctionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKeyGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteKeyValueStoreRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMonitoringSubscriptionRequestTypeDef

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginAccessControlRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteOriginRequestPolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeletePublicKeyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteRealtimeLogConfigRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# DeleteResponseHeadersPolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteStreamingDistributionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# DeleteVpcOriginRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVpcOriginResultTypeDef

### VpcOrigin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFunctionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# DescribeFunctionResultTypeDef

### FunctionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummaryTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeKeyValueStoreRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeKeyValueStoreResultTypeDef

### KeyValueStore
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DistributionConfigOutputTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Origins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginsOutputTypeDef'>
- **Required**: Yes

### DefaultCacheBehavior
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DefaultCacheBehaviorOutputTypeDef'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AliasesOutputTypeDef]

### DefaultRootObject
- **Type**: typing.Optional[str]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupsOutputTypeDef]

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorsOutputTypeDef]

### CustomErrorResponses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponsesOutputTypeDef]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LoggingConfigTypeDef]

### PriceClass
- **Type**: typing.Optional[typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']]

### ViewerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ViewerCertificateTypeDef]

### Restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.RestrictionsOutputTypeDef]

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


# DistributionConfigTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Origins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginsUnionTypeDef'>
- **Required**: Yes

### DefaultCacheBehavior
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DefaultCacheBehaviorUnionTypeDef'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AliasesUnionTypeDef]

### DefaultRootObject
- **Type**: typing.Optional[str]

### OriginGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupsUnionTypeDef]

### CacheBehaviors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorsUnionTypeDef]

### CustomErrorResponses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponsesUnionTypeDef]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.LoggingConfigTypeDef]

### PriceClass
- **Type**: typing.Optional[typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']]

### ViewerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ViewerCertificateTypeDef]

### Restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.RestrictionsUnionTypeDef]

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


# DistributionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DistributionConfigWithTagsTypeDef

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigUnionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnionTypeDef'>
- **Required**: Yes


# DistributionIdListTypeDef

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


# DistributionListTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.DistributionSummaryTypeDef]]


# DistributionSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AliasesOutputTypeDef'>
- **Required**: Yes

### Origins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginsOutputTypeDef'>
- **Required**: Yes

### DefaultCacheBehavior
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DefaultCacheBehaviorOutputTypeDef'>
- **Required**: Yes

### CacheBehaviors
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CacheBehaviorsOutputTypeDef'>
- **Required**: Yes

### CustomErrorResponses
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CustomErrorResponsesOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ViewerCertificateTypeDef'>
- **Required**: Yes

### Restrictions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RestrictionsOutputTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupsOutputTypeDef]

### AliasICPRecordals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.AliasICPRecordalTypeDef]]

### AnycastIpListId
- **Type**: typing.Optional[str]


# DistributionTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigOutputTypeDef'>
- **Required**: Yes

### ActiveTrustedSigners
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ActiveTrustedSignersTypeDef]

### ActiveTrustedKeyGroups
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ActiveTrustedKeyGroupsTypeDef]

### AliasICPRecordals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.AliasICPRecordalTypeDef]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionEntitiesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntityOutputTypeDef]]


# EncryptionEntitiesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntityTypeDef]]


# EncryptionEntityOutputTypeDef

### PublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderId
- **Type**: <class 'str'>
- **Required**: Yes

### FieldPatterns
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldPatternsOutputTypeDef'>
- **Required**: Yes


# EncryptionEntityTypeDef

### PublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderId
- **Type**: <class 'str'>
- **Required**: Yes

### FieldPatterns
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldPatternsTypeDef'>
- **Required**: Yes


# EndPointTypeDef

### StreamType
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisStreamConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.KinesisStreamConfigTypeDef]


# FieldLevelEncryptionConfigOutputTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### QueryArgProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfileConfigOutputTypeDef]

### ContentTypeProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfileConfigOutputTypeDef]


# FieldLevelEncryptionConfigTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### QueryArgProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfileConfigTypeDef]

### ContentTypeProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfileConfigTypeDef]


# FieldLevelEncryptionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldLevelEncryptionListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionSummaryTypeDef]]


# FieldLevelEncryptionProfileConfigOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionEntities
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntitiesOutputTypeDef'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# FieldLevelEncryptionProfileConfigTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionEntities
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntitiesTypeDef'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# FieldLevelEncryptionProfileConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldLevelEncryptionProfileListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileSummaryTypeDef]]


# FieldLevelEncryptionProfileSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.EncryptionEntitiesOutputTypeDef'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# FieldLevelEncryptionProfileTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FieldLevelEncryptionProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileConfigOutputTypeDef'>
- **Required**: Yes


# FieldLevelEncryptionSummaryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### QueryArgProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfileConfigOutputTypeDef]

### ContentTypeProfileConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ContentTypeProfileConfigOutputTypeDef]


# FieldLevelEncryptionTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FieldLevelEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionConfigOutputTypeDef'>
- **Required**: Yes


# FieldPatternsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# FieldPatternsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# ForwardedValuesOutputTypeDef

### QueryString
- **Type**: <class 'bool'>
- **Required**: Yes

### Cookies
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CookiePreferenceOutputTypeDef'>
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersOutputTypeDef]

### QueryStringCacheKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringCacheKeysOutputTypeDef]


# ForwardedValuesTypeDef

### QueryString
- **Type**: <class 'bool'>
- **Required**: Yes

### Cookies
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CookiePreferenceUnionTypeDef'>
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersUnionTypeDef]

### QueryStringCacheKeys
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringCacheKeysUnionTypeDef]


# ForwardedValuesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionAssociationTypeDef

### FunctionARN
- **Type**: <class 'str'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['origin-request', 'origin-response', 'viewer-request', 'viewer-response']
- **Required**: Yes


# FunctionAssociationsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationTypeDef]]


# FunctionAssociationsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionAssociationTypeDef]]


# FunctionAssociationsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionConfigOutputTypeDef

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### Runtime
- **Type**: typing.Literal['cloudfront-js-1.0', 'cloudfront-js-2.0']
- **Required**: Yes

### KeyValueStoreAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreAssociationsOutputTypeDef]


# FunctionConfigTypeDef

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### Runtime
- **Type**: typing.Literal['cloudfront-js-1.0', 'cloudfront-js-2.0']
- **Required**: Yes

### KeyValueStoreAssociations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreAssociationsTypeDef]


# FunctionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummaryTypeDef]]


# FunctionMetadataTypeDef

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


# FunctionSummaryTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionConfigOutputTypeDef'>
- **Required**: Yes

### FunctionMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionMetadataTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[str]


# GeoRestrictionOutputTypeDef

### RestrictionType
- **Type**: typing.Literal['blacklist', 'none', 'whitelist']
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# GeoRestrictionTypeDef

### RestrictionType
- **Type**: typing.Literal['blacklist', 'none', 'whitelist']
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# GeoRestrictionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAnycastIpListRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetAnycastIpListResultTypeDef

### AnycastIpList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AnycastIpListTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCachePolicyConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCachePolicyConfigResultTypeDef

### CachePolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCachePolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCachePolicyResultTypeDef

### CachePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCloudFrontOriginAccessIdentityConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudFrontOriginAccessIdentityConfigResultTypeDef

### CloudFrontOriginAccessIdentityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityConfigTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCloudFrontOriginAccessIdentityRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudFrontOriginAccessIdentityResultTypeDef

### CloudFrontOriginAccessIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContinuousDeploymentPolicyConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetContinuousDeploymentPolicyConfigResultTypeDef

### ContinuousDeploymentPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContinuousDeploymentPolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetContinuousDeploymentPolicyResultTypeDef

### ContinuousDeploymentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDistributionConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDistributionConfigResultTypeDef

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDistributionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDistributionRequestWaitTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.WaiterConfigTypeDef]


# GetDistributionResultTypeDef

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFieldLevelEncryptionConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFieldLevelEncryptionConfigResultTypeDef

### FieldLevelEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFieldLevelEncryptionProfileConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFieldLevelEncryptionProfileConfigResultTypeDef

### FieldLevelEncryptionProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFieldLevelEncryptionProfileRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFieldLevelEncryptionProfileResultTypeDef

### FieldLevelEncryptionProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFieldLevelEncryptionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFieldLevelEncryptionResultTypeDef

### FieldLevelEncryption
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# GetFunctionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInvalidationRequestTypeDef

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetInvalidationRequestWaitTypeDef

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.WaiterConfigTypeDef]


# GetInvalidationResultTypeDef

### Invalidation
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKeyGroupConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyGroupConfigResultTypeDef

### KeyGroupConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKeyGroupRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetKeyGroupResultTypeDef

### KeyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMonitoringSubscriptionRequestTypeDef

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMonitoringSubscriptionResultTypeDef

### MonitoringSubscription
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.MonitoringSubscriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOriginAccessControlConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginAccessControlConfigResultTypeDef

### OriginAccessControlConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlConfigTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOriginAccessControlRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginAccessControlResultTypeDef

### OriginAccessControl
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOriginRequestPolicyConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginRequestPolicyConfigResultTypeDef

### OriginRequestPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOriginRequestPolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginRequestPolicyResultTypeDef

### OriginRequestPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPublicKeyConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetPublicKeyConfigResultTypeDef

### PublicKeyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyConfigTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPublicKeyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetPublicKeyResultTypeDef

### PublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRealtimeLogConfigRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# GetRealtimeLogConfigResultTypeDef

### RealtimeLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResponseHeadersPolicyConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetResponseHeadersPolicyConfigResultTypeDef

### ResponseHeadersPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResponseHeadersPolicyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetResponseHeadersPolicyResultTypeDef

### ResponseHeadersPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamingDistributionConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamingDistributionConfigResultTypeDef

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamingDistributionRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamingDistributionRequestWaitTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.WaiterConfigTypeDef]


# GetStreamingDistributionResultTypeDef

### StreamingDistribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVpcOriginRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetVpcOriginResultTypeDef

### VpcOrigin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GrpcConfigTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes


# HeadersOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# HeadersTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# HeadersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImportSourceTypeDef

### SourceType
- **Type**: typing.Literal['S3']
- **Required**: Yes

### SourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# InvalidationBatchOutputTypeDef

### Paths
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PathsOutputTypeDef'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes


# InvalidationBatchTypeDef

### Paths
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PathsTypeDef'>
- **Required**: Yes

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes


# InvalidationBatchUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InvalidationListTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationSummaryTypeDef]]


# InvalidationSummaryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes


# InvalidationTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationBatchOutputTypeDef'>
- **Required**: Yes


# KGKeyPairIdsTypeDef

### KeyGroupId
- **Type**: typing.Optional[str]

### KeyPairIds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.KeyPairIdsTypeDef]


# KeyGroupConfigOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.List[str]
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# KeyGroupConfigTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# KeyGroupConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeyGroupListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupSummaryTypeDef]]


# KeyGroupSummaryTypeDef

### KeyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupTypeDef'>
- **Required**: Yes


# KeyGroupTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### KeyGroupConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupConfigOutputTypeDef'>
- **Required**: Yes


# KeyPairIdsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# KeyValueStoreAssociationTypeDef

### KeyValueStoreARN
- **Type**: <class 'str'>
- **Required**: Yes


# KeyValueStoreAssociationsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreAssociationTypeDef]]


# KeyValueStoreAssociationsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreAssociationTypeDef]]


# KeyValueStoreListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreTypeDef]]


# KeyValueStoreTypeDef

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


# KinesisStreamConfigTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaFunctionAssociationTypeDef

### LambdaFunctionARN
- **Type**: <class 'str'>
- **Required**: Yes

### EventType
- **Type**: typing.Literal['origin-request', 'origin-response', 'viewer-request', 'viewer-response']
- **Required**: Yes

### IncludeBody
- **Type**: typing.Optional[bool]


# LambdaFunctionAssociationsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationTypeDef]]


# LambdaFunctionAssociationsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.LambdaFunctionAssociationTypeDef]]


# LambdaFunctionAssociationsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAnycastIpListsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAnycastIpListsResultTypeDef

### AnycastIpLists
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AnycastIpListCollectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCachePoliciesResultTypeDef

### CachePolicyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCloudFrontOriginAccessIdentitiesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfigTypeDef]


# ListCloudFrontOriginAccessIdentitiesRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListCloudFrontOriginAccessIdentitiesResultTypeDef

### CloudFrontOriginAccessIdentityList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListConflictingAliasesRequestTypeDef

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


# ListConflictingAliasesResultTypeDef

### ConflictingAliasesList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ConflictingAliasesListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContinuousDeploymentPoliciesRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListContinuousDeploymentPoliciesResultTypeDef

### ContinuousDeploymentPolicyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsByAnycastIpListIdRequestTypeDef

### AnycastIpListId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByAnycastIpListIdResultTypeDef

### DistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsByCachePolicyIdRequestTypeDef

### CachePolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByCachePolicyIdResultTypeDef

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsByKeyGroupRequestTypeDef

### KeyGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByKeyGroupResultTypeDef

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsByOriginRequestPolicyIdRequestTypeDef

### OriginRequestPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByOriginRequestPolicyIdResultTypeDef

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsByRealtimeLogConfigRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]

### RealtimeLogConfigName
- **Type**: typing.Optional[str]

### RealtimeLogConfigArn
- **Type**: typing.Optional[str]


# ListDistributionsByRealtimeLogConfigResultTypeDef

### DistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsByResponseHeadersPolicyIdRequestTypeDef

### ResponseHeadersPolicyId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByResponseHeadersPolicyIdResultTypeDef

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsByVpcOriginIdRequestTypeDef

### VpcOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByVpcOriginIdResultTypeDef

### DistributionIdList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionIdListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsByWebACLIdRequestTypeDef

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsByWebACLIdResultTypeDef

### DistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDistributionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfigTypeDef]


# ListDistributionsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListDistributionsResultTypeDef

### DistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFieldLevelEncryptionConfigsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListFieldLevelEncryptionConfigsResultTypeDef

### FieldLevelEncryptionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFieldLevelEncryptionProfilesRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListFieldLevelEncryptionProfilesResultTypeDef

### FieldLevelEncryptionProfileList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# ListFunctionsResultTypeDef

### FunctionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInvalidationsRequestPaginateTypeDef

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfigTypeDef]


# ListInvalidationsRequestTypeDef

### DistributionId
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListInvalidationsResultTypeDef

### InvalidationList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.InvalidationListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKeyGroupsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListKeyGroupsResultTypeDef

### KeyGroupList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKeyValueStoresRequestPaginateTypeDef

### Status
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfigTypeDef]


# ListKeyValueStoresRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ListKeyValueStoresResultTypeDef

### KeyValueStoreList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOriginAccessControlsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListOriginAccessControlsResultTypeDef

### OriginAccessControlList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOriginRequestPoliciesResultTypeDef

### OriginRequestPolicyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPublicKeysRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfigTypeDef]


# ListPublicKeysRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListPublicKeysResultTypeDef

### PublicKeyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRealtimeLogConfigsRequestTypeDef

### MaxItems
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]


# ListRealtimeLogConfigsResultTypeDef

### RealtimeLogConfigs
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfigsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResponseHeadersPoliciesResultTypeDef

### ResponseHeadersPolicyList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStreamingDistributionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.PaginatorConfigTypeDef]


# ListStreamingDistributionsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListStreamingDistributionsResultTypeDef

### StreamingDistributionList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResultTypeDef

### Tags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVpcOriginsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[str]


# ListVpcOriginsResultTypeDef

### VpcOriginList
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginListTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingConfigTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### IncludeCookies
- **Type**: typing.Optional[bool]

### Bucket
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]


# MonitoringSubscriptionTypeDef

### RealtimeMetricsSubscriptionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeMetricsSubscriptionConfigTypeDef]


# OriginAccessControlConfigTypeDef

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


# OriginAccessControlListTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlSummaryTypeDef]]


# OriginAccessControlSummaryTypeDef

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


# OriginAccessControlTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### OriginAccessControlConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlConfigTypeDef]


# OriginCustomHeaderTypeDef

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### HeaderValue
- **Type**: <class 'str'>
- **Required**: Yes


# OriginGroupFailoverCriteriaOutputTypeDef

### StatusCodes
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StatusCodesOutputTypeDef'>
- **Required**: Yes


# OriginGroupFailoverCriteriaTypeDef

### StatusCodes
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StatusCodesUnionTypeDef'>
- **Required**: Yes


# OriginGroupFailoverCriteriaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginGroupMemberTypeDef

### OriginId
- **Type**: <class 'str'>
- **Required**: Yes


# OriginGroupMembersOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupMemberTypeDef]
- **Required**: Yes


# OriginGroupMembersTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupMemberTypeDef]
- **Required**: Yes


# OriginGroupMembersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginGroupOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### FailoverCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupFailoverCriteriaOutputTypeDef'>
- **Required**: Yes

### Members
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupMembersOutputTypeDef'>
- **Required**: Yes

### SelectionCriteria
- **Type**: typing.Optional[typing.Literal['default', 'media-quality-based']]


# OriginGroupTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### FailoverCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupFailoverCriteriaUnionTypeDef'>
- **Required**: Yes

### Members
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupMembersUnionTypeDef'>
- **Required**: Yes

### SelectionCriteria
- **Type**: typing.Optional[typing.Literal['default', 'media-quality-based']]


# OriginGroupUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginGroupsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupOutputTypeDef]]


# OriginGroupsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.OriginGroupUnionTypeDef]]


# OriginGroupsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginOutputTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginPath
- **Type**: typing.Optional[str]

### CustomHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomHeadersOutputTypeDef]

### S3OriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.S3OriginConfigTypeDef]

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomOriginConfigOutputTypeDef]

### VpcOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginConfigTypeDef]

### ConnectionAttempts
- **Type**: typing.Optional[int]

### ConnectionTimeout
- **Type**: typing.Optional[int]

### OriginShield
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginShieldTypeDef]

### OriginAccessControlId
- **Type**: typing.Optional[str]


# OriginRequestPolicyConfigOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HeadersConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyHeadersConfigOutputTypeDef'>
- **Required**: Yes

### CookiesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyCookiesConfigOutputTypeDef'>
- **Required**: Yes

### QueryStringsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyQueryStringsConfigOutputTypeDef'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# OriginRequestPolicyConfigTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HeadersConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyHeadersConfigTypeDef'>
- **Required**: Yes

### CookiesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyCookiesConfigTypeDef'>
- **Required**: Yes

### QueryStringsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyQueryStringsConfigTypeDef'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]


# OriginRequestPolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginRequestPolicyCookiesConfigOutputTypeDef

### CookieBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesOutputTypeDef]


# OriginRequestPolicyCookiesConfigTypeDef

### CookieBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CookieNamesTypeDef]


# OriginRequestPolicyHeadersConfigOutputTypeDef

### HeaderBehavior
- **Type**: typing.Literal['allExcept', 'allViewer', 'allViewerAndWhitelistCloudFront', 'none', 'whitelist']
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersOutputTypeDef]


# OriginRequestPolicyHeadersConfigTypeDef

### HeaderBehavior
- **Type**: typing.Literal['allExcept', 'allViewer', 'allViewerAndWhitelistCloudFront', 'none', 'whitelist']
- **Required**: Yes

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.HeadersTypeDef]


# OriginRequestPolicyListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicySummaryTypeDef]]


# OriginRequestPolicyQueryStringsConfigOutputTypeDef

### QueryStringBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### QueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringNamesOutputTypeDef]


# OriginRequestPolicyQueryStringsConfigTypeDef

### QueryStringBehavior
- **Type**: typing.Literal['all', 'allExcept', 'none', 'whitelist']
- **Required**: Yes

### QueryStrings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryStringNamesTypeDef]


# OriginRequestPolicySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginRequestPolicyTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OriginRequestPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyConfigOutputTypeDef'>
- **Required**: Yes


# OriginShieldTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### OriginShieldRegion
- **Type**: typing.Optional[str]


# OriginSslProtocolsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Literal['SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2']]
- **Required**: Yes


# OriginSslProtocolsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Literal['SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2']]
- **Required**: Yes


# OriginSslProtocolsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginPath
- **Type**: typing.Optional[str]

### CustomHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomHeadersUnionTypeDef]

### S3OriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.S3OriginConfigTypeDef]

### CustomOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.CustomOriginConfigUnionTypeDef]

### VpcOriginConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginConfigTypeDef]

### ConnectionAttempts
- **Type**: typing.Optional[int]

### ConnectionTimeout
- **Type**: typing.Optional[int]

### OriginShield
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginShieldTypeDef]

### OriginAccessControlId
- **Type**: typing.Optional[str]


# OriginUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OriginsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.OriginOutputTypeDef]
- **Required**: Yes


# OriginsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.OriginUnionTypeDef]
- **Required**: Yes


# OriginsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParametersInCacheKeyAndForwardedToOriginOutputTypeDef

### EnableAcceptEncodingGzip
- **Type**: <class 'bool'>
- **Required**: Yes

### HeadersConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyHeadersConfigOutputTypeDef'>
- **Required**: Yes

### CookiesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyCookiesConfigOutputTypeDef'>
- **Required**: Yes

### QueryStringsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyQueryStringsConfigOutputTypeDef'>
- **Required**: Yes

### EnableAcceptEncodingBrotli
- **Type**: typing.Optional[bool]


# ParametersInCacheKeyAndForwardedToOriginTypeDef

### EnableAcceptEncodingGzip
- **Type**: <class 'bool'>
- **Required**: Yes

### HeadersConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyHeadersConfigTypeDef'>
- **Required**: Yes

### CookiesConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyCookiesConfigTypeDef'>
- **Required**: Yes

### QueryStringsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyQueryStringsConfigTypeDef'>
- **Required**: Yes

### EnableAcceptEncodingBrotli
- **Type**: typing.Optional[bool]


# PathsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# PathsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# PublicKeyConfigTypeDef

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


# PublicKeyListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeySummaryTypeDef]]


# PublicKeySummaryTypeDef

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


# PublicKeyTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PublicKeyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyConfigTypeDef'>
- **Required**: Yes


# PublishFunctionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# PublishFunctionResultTypeDef

### FunctionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryArgProfileConfigOutputTypeDef

### ForwardWhenQueryArgProfileIsUnknown
- **Type**: <class 'bool'>
- **Required**: Yes

### QueryArgProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfilesOutputTypeDef]


# QueryArgProfileConfigTypeDef

### ForwardWhenQueryArgProfileIsUnknown
- **Type**: <class 'bool'>
- **Required**: Yes

### QueryArgProfiles
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfilesTypeDef]


# QueryArgProfileTypeDef

### QueryArg
- **Type**: <class 'str'>
- **Required**: Yes

### ProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# QueryArgProfilesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfileTypeDef]]


# QueryArgProfilesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.QueryArgProfileTypeDef]]


# QueryStringCacheKeysOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# QueryStringCacheKeysTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# QueryStringCacheKeysUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryStringNamesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# QueryStringNamesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# RealtimeLogConfigTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.EndPointTypeDef]
- **Required**: Yes

### Fields
- **Type**: typing.List[str]
- **Required**: Yes


# RealtimeLogConfigsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfigTypeDef]]

### NextMarker
- **Type**: typing.Optional[str]


# RealtimeMetricsSubscriptionConfigTypeDef

### RealtimeMetricsSubscriptionStatus
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowHeadersTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[typing.Literal['ALL', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowMethodsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[typing.Literal['ALL', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT']]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlAllowOriginsTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# ResponseHeadersPolicyAccessControlExposeHeadersTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# ResponseHeadersPolicyConfigOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### CorsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCorsConfigOutputTypeDef]

### SecurityHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicySecurityHeadersConfigTypeDef]

### ServerTimingHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyServerTimingHeadersConfigTypeDef]

### CustomHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef]

### RemoveHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef]


# ResponseHeadersPolicyConfigTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### CorsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCorsConfigTypeDef]

### SecurityHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicySecurityHeadersConfigTypeDef]

### ServerTimingHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyServerTimingHeadersConfigTypeDef]

### CustomHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCustomHeadersConfigTypeDef]

### RemoveHeadersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyRemoveHeadersConfigTypeDef]


# ResponseHeadersPolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseHeadersPolicyContentSecurityPolicyTypeDef

### Override
- **Type**: <class 'bool'>
- **Required**: Yes

### ContentSecurityPolicy
- **Type**: <class 'str'>
- **Required**: Yes


# ResponseHeadersPolicyContentTypeOptionsTypeDef

### Override
- **Type**: <class 'bool'>
- **Required**: Yes


# ResponseHeadersPolicyCorsConfigOutputTypeDef

### AccessControlAllowOrigins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowOriginsOutputTypeDef'>
- **Required**: Yes

### AccessControlAllowHeaders
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowHeadersOutputTypeDef'>
- **Required**: Yes

### AccessControlAllowMethods
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowMethodsOutputTypeDef'>
- **Required**: Yes

### AccessControlAllowCredentials
- **Type**: <class 'bool'>
- **Required**: Yes

### OriginOverride
- **Type**: <class 'bool'>
- **Required**: Yes

### AccessControlExposeHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlExposeHeadersOutputTypeDef]

### AccessControlMaxAgeSec
- **Type**: typing.Optional[int]


# ResponseHeadersPolicyCorsConfigTypeDef

### AccessControlAllowOrigins
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowOriginsTypeDef'>
- **Required**: Yes

### AccessControlAllowHeaders
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowHeadersTypeDef'>
- **Required**: Yes

### AccessControlAllowMethods
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlAllowMethodsTypeDef'>
- **Required**: Yes

### AccessControlAllowCredentials
- **Type**: <class 'bool'>
- **Required**: Yes

### OriginOverride
- **Type**: <class 'bool'>
- **Required**: Yes

### AccessControlExposeHeaders
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyAccessControlExposeHeadersTypeDef]

### AccessControlMaxAgeSec
- **Type**: typing.Optional[int]


# ResponseHeadersPolicyCustomHeaderTypeDef

### Header
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Override
- **Type**: <class 'bool'>
- **Required**: Yes


# ResponseHeadersPolicyCustomHeadersConfigOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCustomHeaderTypeDef]]


# ResponseHeadersPolicyCustomHeadersConfigTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyCustomHeaderTypeDef]]


# ResponseHeadersPolicyFrameOptionsTypeDef

### Override
- **Type**: <class 'bool'>
- **Required**: Yes

### FrameOption
- **Type**: typing.Literal['DENY', 'SAMEORIGIN']
- **Required**: Yes


# ResponseHeadersPolicyListTypeDef

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicySummaryTypeDef]]


# ResponseHeadersPolicyReferrerPolicyTypeDef

### Override
- **Type**: <class 'bool'>
- **Required**: Yes

### ReferrerPolicy
- **Type**: typing.Literal['no-referrer', 'no-referrer-when-downgrade', 'origin', 'origin-when-cross-origin', 'same-origin', 'strict-origin', 'strict-origin-when-cross-origin', 'unsafe-url']
- **Required**: Yes


# ResponseHeadersPolicyRemoveHeaderTypeDef

### Header
- **Type**: <class 'str'>
- **Required**: Yes


# ResponseHeadersPolicyRemoveHeadersConfigOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyRemoveHeaderTypeDef]]


# ResponseHeadersPolicyRemoveHeadersConfigTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyRemoveHeaderTypeDef]]


# ResponseHeadersPolicySecurityHeadersConfigTypeDef

### XSSProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyXSSProtectionTypeDef]

### FrameOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyFrameOptionsTypeDef]

### ReferrerPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyReferrerPolicyTypeDef]

### ContentSecurityPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyContentSecurityPolicyTypeDef]

### ContentTypeOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyContentTypeOptionsTypeDef]

### StrictTransportSecurity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyStrictTransportSecurityTypeDef]


# ResponseHeadersPolicyServerTimingHeadersConfigTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### SamplingRate
- **Type**: typing.Optional[float]


# ResponseHeadersPolicyStrictTransportSecurityTypeDef

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


# ResponseHeadersPolicySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseHeadersPolicyTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseHeadersPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyConfigOutputTypeDef'>
- **Required**: Yes


# ResponseHeadersPolicyXSSProtectionTypeDef

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


# RestrictionsOutputTypeDef

### GeoRestriction
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.GeoRestrictionOutputTypeDef'>
- **Required**: Yes


# RestrictionsTypeDef

### GeoRestriction
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.GeoRestrictionUnionTypeDef'>
- **Required**: Yes


# RestrictionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3OriginConfigTypeDef

### OriginAccessIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# S3OriginTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginAccessIdentity
- **Type**: <class 'str'>
- **Required**: Yes


# SessionStickinessConfigTypeDef

### IdleTTL
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumTTL
- **Type**: <class 'int'>
- **Required**: Yes


# SignerTypeDef

### AwsAccountNumber
- **Type**: typing.Optional[str]

### KeyPairIds
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.KeyPairIdsTypeDef]


# StagingDistributionDnsNamesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# StagingDistributionDnsNamesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# StatusCodesOutputTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[int]
- **Required**: Yes


# StatusCodesTypeDef

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Sequence[int]
- **Required**: Yes


# StatusCodesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StreamingDistributionConfigOutputTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### S3Origin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.S3OriginTypeDef'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedSigners
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersOutputTypeDef'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AliasesOutputTypeDef]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.StreamingLoggingConfigTypeDef]

### PriceClass
- **Type**: typing.Optional[typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']]


# StreamingDistributionConfigTypeDef

### CallerReference
- **Type**: <class 'str'>
- **Required**: Yes

### S3Origin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.S3OriginTypeDef'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedSigners
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersUnionTypeDef'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Aliases
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.AliasesUnionTypeDef]

### Logging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.StreamingLoggingConfigTypeDef]

### PriceClass
- **Type**: typing.Optional[typing.Literal['PriceClass_100', 'PriceClass_200', 'PriceClass_All']]


# StreamingDistributionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StreamingDistributionConfigWithTagsTypeDef

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigUnionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnionTypeDef'>
- **Required**: Yes


# StreamingDistributionListTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionSummaryTypeDef]]


# StreamingDistributionSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.S3OriginTypeDef'>
- **Required**: Yes

### Aliases
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.AliasesOutputTypeDef'>
- **Required**: Yes

### TrustedSigners
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TrustedSignersOutputTypeDef'>
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


# StreamingDistributionTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ActiveTrustedSignersTypeDef'>
- **Required**: Yes

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigOutputTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# StreamingLoggingConfigTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: <class 'str'>
- **Required**: Yes


# TagKeysTypeDef

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# TagResourceRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagsUnionTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagsOutputTypeDef

### Items
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.TagTypeDef]]


# TagsTypeDef

### Items
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.TagTypeDef]]


# TagsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TestFunctionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes

### EventObject
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.BlobTypeDef'>
- **Required**: Yes

### Stage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# TestFunctionResultTypeDef

### TestResult
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TestResultTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TestResultTypeDef

### FunctionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummaryTypeDef]

### ComputeUtilization
- **Type**: typing.Optional[str]

### FunctionExecutionLogs
- **Type**: typing.Optional[typing.List[str]]

### FunctionErrorMessage
- **Type**: typing.Optional[str]

### FunctionOutput
- **Type**: typing.Optional[str]


# TrafficConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrustedKeyGroupsOutputTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# TrustedKeyGroupsTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# TrustedKeyGroupsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrustedSignersOutputTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.List[str]]


# TrustedSignersTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Quantity
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.Optional[typing.Sequence[str]]


# TrustedSignersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.TagKeysTypeDef'>
- **Required**: Yes


# UpdateCachePolicyRequestTypeDef

### CachePolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateCachePolicyResultTypeDef

### CachePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CachePolicyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateCloudFrontOriginAccessIdentityRequestTypeDef

### CloudFrontOriginAccessIdentityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityConfigTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateCloudFrontOriginAccessIdentityResultTypeDef

### CloudFrontOriginAccessIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.CloudFrontOriginAccessIdentityTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateContinuousDeploymentPolicyRequestTypeDef

### ContinuousDeploymentPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateContinuousDeploymentPolicyResultTypeDef

### ContinuousDeploymentPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ContinuousDeploymentPolicyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDistributionRequestTypeDef

### DistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateDistributionResultTypeDef

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDistributionWithStagingConfigRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### StagingDistributionId
- **Type**: typing.Optional[str]

### IfMatch
- **Type**: typing.Optional[str]


# UpdateDistributionWithStagingConfigResultTypeDef

### Distribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.DistributionTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFieldLevelEncryptionConfigRequestTypeDef

### FieldLevelEncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateFieldLevelEncryptionConfigResultTypeDef

### FieldLevelEncryption
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFieldLevelEncryptionProfileRequestTypeDef

### FieldLevelEncryptionProfileConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateFieldLevelEncryptionProfileResultTypeDef

### FieldLevelEncryptionProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FieldLevelEncryptionProfileTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFunctionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionConfigUnionTypeDef'>
- **Required**: Yes

### FunctionCode
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.BlobTypeDef'>
- **Required**: Yes


# UpdateFunctionResultTypeDef

### FunctionSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.FunctionSummaryTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKeyGroupRequestTypeDef

### KeyGroupConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateKeyGroupResultTypeDef

### KeyGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyGroupTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKeyValueStoreRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateKeyValueStoreResultTypeDef

### KeyValueStore
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.KeyValueStoreTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateOriginAccessControlRequestTypeDef

### OriginAccessControlConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlConfigTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateOriginAccessControlResultTypeDef

### OriginAccessControl
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginAccessControlTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateOriginRequestPolicyRequestTypeDef

### OriginRequestPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateOriginRequestPolicyResultTypeDef

### OriginRequestPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.OriginRequestPolicyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePublicKeyRequestTypeDef

### PublicKeyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyConfigTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdatePublicKeyResultTypeDef

### PublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.PublicKeyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRealtimeLogConfigRequestTypeDef

### EndPoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cloudfront_classes.EndPointTypeDef]]

### Fields
- **Type**: typing.Optional[typing.Sequence[str]]

### Name
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### SamplingRate
- **Type**: typing.Optional[int]


# UpdateRealtimeLogConfigResultTypeDef

### RealtimeLogConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.RealtimeLogConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResponseHeadersPolicyRequestTypeDef

### ResponseHeadersPolicyConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateResponseHeadersPolicyResultTypeDef

### ResponseHeadersPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseHeadersPolicyTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStreamingDistributionRequestTypeDef

### StreamingDistributionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: typing.Optional[str]


# UpdateStreamingDistributionResultTypeDef

### StreamingDistribution
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.StreamingDistributionTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVpcOriginRequestTypeDef

### VpcOriginEndpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginEndpointConfigUnionTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IfMatch
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateVpcOriginResultTypeDef

### VpcOrigin
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ViewerCertificateTypeDef

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


# VpcOriginConfigTypeDef

### VpcOriginId
- **Type**: <class 'str'>
- **Required**: Yes

### OriginReadTimeout
- **Type**: typing.Optional[int]

### OriginKeepaliveTimeout
- **Type**: typing.Optional[int]


# VpcOriginEndpointConfigOutputTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginSslProtocolsOutputTypeDef]


# VpcOriginEndpointConfigTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudfront_classes.OriginSslProtocolsTypeDef]


# VpcOriginEndpointConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcOriginListTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginSummaryTypeDef]]


# VpcOriginSummaryTypeDef

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


# VpcOriginTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudfront_classes.VpcOriginEndpointConfigOutputTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



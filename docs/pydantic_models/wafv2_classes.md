# Wafv2 Classes

# APIKeySummaryTypeDef

### TokenDomains
- **Type**: typing.Optional[typing.List[str]]

### APIKey
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[int]


# AWSManagedRulesACFPRuleSetOutputTypeDef

### CreationPath
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationPagePath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RequestInspectionACFPOutputTypeDef'>
- **Required**: Yes

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionOutputTypeDef]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesACFPRuleSetTypeDef

### CreationPath
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationPagePath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RequestInspectionACFPUnionTypeDef'>
- **Required**: Yes

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionUnionTypeDef]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesACFPRuleSetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AWSManagedRulesATPRuleSetOutputTypeDef

### LoginPath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RequestInspectionTypeDef]

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionOutputTypeDef]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesATPRuleSetTypeDef

### LoginPath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RequestInspectionTypeDef]

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionUnionTypeDef]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesATPRuleSetUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AWSManagedRulesBotControlRuleSetTypeDef

### InspectionLevel
- **Type**: typing.Literal['COMMON', 'TARGETED']
- **Required**: Yes

### EnableMachineLearning
- **Type**: typing.Optional[bool]


# ActionConditionTypeDef

### Action
- **Type**: typing.Literal['ALLOW', 'BLOCK', 'CAPTCHA', 'CHALLENGE', 'COUNT', 'EXCLUDED_AS_COUNT']
- **Required**: Yes


# AddressFieldTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# AllowActionOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingOutputTypeDef]


# AllowActionTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingUnionTypeDef]


# AllowActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AndStatementOutputTypeDef

### Statements
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# AndStatementTypeDef

### Statements
- **Type**: typing.Sequence[typing.Mapping[str, typing.Any]]
- **Required**: Yes


# AndStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateWebACLRequestTypeDef

### WebACLArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationConfigOutputTypeDef

### RequestBody
- **Type**: typing.Optional[typing.Dict[typing.Literal['API_GATEWAY', 'APP_RUNNER_SERVICE', 'CLOUDFRONT', 'COGNITO_USER_POOL', 'VERIFIED_ACCESS_INSTANCE'], aws_resource_validator.pydantic_models.wafv2_classes.RequestBodyAssociatedResourceTypeConfigTypeDef]]


# AssociationConfigTypeDef

### RequestBody
- **Type**: typing.Optional[typing.Mapping[typing.Literal['API_GATEWAY', 'APP_RUNNER_SERVICE', 'CLOUDFRONT', 'COGNITO_USER_POOL', 'VERIFIED_ACCESS_INSTANCE'], aws_resource_validator.pydantic_models.wafv2_classes.RequestBodyAssociatedResourceTypeConfigTypeDef]]


# AssociationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockActionOutputTypeDef

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseOutputTypeDef]


# BlockActionTypeDef

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseUnionTypeDef]


# BlockActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BodyTypeDef

### OversizeHandling
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']]


# ByteMatchStatementOutputTypeDef

### SearchString
- **Type**: <class 'bytes'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutputTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# ByteMatchStatementTypeDef

### SearchString
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.BlobTypeDef'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnionTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# ByteMatchStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaptchaActionOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingOutputTypeDef]


# CaptchaActionTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingUnionTypeDef]


# CaptchaActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaptchaConfigTypeDef

### ImmunityTimeProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ImmunityTimePropertyTypeDef]


# CaptchaResponseTypeDef

### ResponseCode
- **Type**: typing.Optional[int]

### SolveTimestamp
- **Type**: typing.Optional[int]

### FailureReason
- **Type**: typing.Optional[typing.Literal['TOKEN_DOMAIN_MISMATCH', 'TOKEN_EXPIRED', 'TOKEN_INVALID', 'TOKEN_MISSING']]


# ChallengeActionOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingOutputTypeDef]


# ChallengeActionTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingUnionTypeDef]


# ChallengeActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChallengeConfigTypeDef

### ImmunityTimeProperty
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ImmunityTimePropertyTypeDef]


# ChallengeResponseTypeDef

### ResponseCode
- **Type**: typing.Optional[int]

### SolveTimestamp
- **Type**: typing.Optional[int]

### FailureReason
- **Type**: typing.Optional[typing.Literal['TOKEN_DOMAIN_MISMATCH', 'TOKEN_EXPIRED', 'TOKEN_INVALID', 'TOKEN_MISSING']]


# CheckCapacityRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnionTypeDef]
- **Required**: Yes


# CheckCapacityResponseTypeDef

### Capacity
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConditionTypeDef

### ActionCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ActionConditionTypeDef]

### LabelNameCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.LabelNameConditionTypeDef]


# CookieMatchPatternOutputTypeDef

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedCookies
- **Type**: typing.Optional[typing.List[str]]

### ExcludedCookies
- **Type**: typing.Optional[typing.List[str]]


# CookieMatchPatternTypeDef

### All
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IncludedCookies
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedCookies
- **Type**: typing.Optional[typing.Sequence[str]]


# CookieMatchPatternUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CookiesOutputTypeDef

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.CookieMatchPatternOutputTypeDef'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# CookiesTypeDef

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.CookieMatchPatternUnionTypeDef'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# CookiesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CountActionOutputTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingOutputTypeDef]


# CountActionTypeDef

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingUnionTypeDef]


# CountActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAPIKeyRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### TokenDomains
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CreateAPIKeyResponseTypeDef

### APIKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIPSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### IPAddressVersion
- **Type**: typing.Literal['IPV4', 'IPV6']
- **Required**: Yes

### Addresses
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TagTypeDef]]


# CreateIPSetResponseTypeDef

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.IPSetSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRegexPatternSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### RegularExpressionList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RegexTypeDef]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TagTypeDef]]


# CreateRegexPatternSetResponseTypeDef

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Capacity
- **Type**: <class 'int'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TagTypeDef]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBodyTypeDef]]


# CreateRuleGroupResponseTypeDef

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWebACLRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### DefaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.DefaultActionUnionTypeDef'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnionTypeDef]]

### DataProtectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TagTypeDef]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBodyTypeDef]]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaConfigTypeDef]

### ChallengeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeConfigTypeDef]

### TokenDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### AssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AssociationConfigUnionTypeDef]


# CreateWebACLResponseTypeDef

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.WebACLSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomHTTPHeaderTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# CustomRequestHandlingOutputTypeDef

### InsertHeaders
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.CustomHTTPHeaderTypeDef]
- **Required**: Yes


# CustomRequestHandlingTypeDef

### InsertHeaders
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.CustomHTTPHeaderTypeDef]
- **Required**: Yes


# CustomRequestHandlingUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomResponseBodyTypeDef

### ContentType
- **Type**: typing.Literal['APPLICATION_JSON', 'TEXT_HTML', 'TEXT_PLAIN']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# CustomResponseOutputTypeDef

### ResponseCode
- **Type**: <class 'int'>
- **Required**: Yes

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.CustomHTTPHeaderTypeDef]]


# CustomResponseTypeDef

### ResponseCode
- **Type**: <class 'int'>
- **Required**: Yes

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseHeaders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.CustomHTTPHeaderTypeDef]]


# CustomResponseUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataProtectionConfigOutputTypeDef

### DataProtections
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionOutputTypeDef]
- **Required**: Yes


# DataProtectionConfigTypeDef

### DataProtections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionTypeDef]
- **Required**: Yes


# DataProtectionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataProtectionOutputTypeDef

### Field
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToProtectOutputTypeDef'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['HASH', 'SUBSTITUTION']
- **Required**: Yes

### ExcludeRuleMatchDetails
- **Type**: typing.Optional[bool]

### ExcludeRateBasedDetails
- **Type**: typing.Optional[bool]


# DataProtectionTypeDef

### Field
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToProtectTypeDef'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['HASH', 'SUBSTITUTION']
- **Required**: Yes

### ExcludeRuleMatchDetails
- **Type**: typing.Optional[bool]

### ExcludeRateBasedDetails
- **Type**: typing.Optional[bool]


# DefaultActionOutputTypeDef

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BlockActionOutputTypeDef]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AllowActionOutputTypeDef]


# DefaultActionTypeDef

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BlockActionTypeDef]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AllowActionTypeDef]


# DefaultActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAPIKeyRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### APIKey
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFirewallManagerRuleGroupsRequestTypeDef

### WebACLArn
- **Type**: <class 'str'>
- **Required**: Yes

### WebACLLockToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFirewallManagerRuleGroupsResponseTypeDef

### NextWebACLLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIPSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoggingConfigurationRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# DeletePermissionPolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegexPatternSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebACLRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAllManagedProductsRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes


# DescribeAllManagedProductsResponseTypeDef

### ManagedProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedProductDescriptorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeManagedProductsByVendorRequestTypeDef

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes


# DescribeManagedProductsByVendorResponseTypeDef

### ManagedProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedProductDescriptorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeManagedRuleGroupRequestTypeDef

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### VersionName
- **Type**: typing.Optional[str]


# DescribeManagedRuleGroupResponseTypeDef

### VersionName
- **Type**: <class 'str'>
- **Required**: Yes

### SnsTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### Capacity
- **Type**: <class 'int'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleSummaryTypeDef]
- **Required**: Yes

### LabelNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### AvailableLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelSummaryTypeDef]
- **Required**: Yes

### ConsumedLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateWebACLRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmailFieldTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# ExcludedRuleTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# FieldToMatchOutputTypeDef

### SingleHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SingleHeaderTypeDef]

### SingleQueryArgument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SingleQueryArgumentTypeDef]

### AllQueryArguments
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### UriPath
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### QueryString
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BodyTypeDef]

### Method
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### JsonBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.JsonBodyOutputTypeDef]

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.HeadersOutputTypeDef]

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CookiesOutputTypeDef]

### HeaderOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.HeaderOrderTypeDef]

### JA3Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.JA3FingerprintTypeDef]

### JA4Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.JA4FingerprintTypeDef]


# FieldToMatchTypeDef

### SingleHeader
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SingleHeaderTypeDef]

### SingleQueryArgument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SingleQueryArgumentTypeDef]

### AllQueryArguments
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### UriPath
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### QueryString
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BodyTypeDef]

### Method
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### JsonBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.JsonBodyUnionTypeDef]

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.HeadersUnionTypeDef]

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CookiesUnionTypeDef]

### HeaderOrder
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.HeaderOrderTypeDef]

### JA3Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.JA3FingerprintTypeDef]

### JA4Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.JA4FingerprintTypeDef]


# FieldToMatchUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldToProtectOutputTypeDef

### FieldType
- **Type**: typing.Literal['BODY', 'QUERY_STRING', 'SINGLE_COOKIE', 'SINGLE_HEADER', 'SINGLE_QUERY_ARGUMENT']
- **Required**: Yes

### FieldKeys
- **Type**: typing.Optional[typing.List[str]]


# FieldToProtectTypeDef

### FieldType
- **Type**: typing.Literal['BODY', 'QUERY_STRING', 'SINGLE_COOKIE', 'SINGLE_HEADER', 'SINGLE_QUERY_ARGUMENT']
- **Required**: Yes

### FieldKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# FilterOutputTypeDef

### Behavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes

### Requirement
- **Type**: typing.Literal['MEETS_ALL', 'MEETS_ANY']
- **Required**: Yes

### Conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ConditionTypeDef]
- **Required**: Yes


# FilterTypeDef

### Behavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes

### Requirement
- **Type**: typing.Literal['MEETS_ALL', 'MEETS_ANY']
- **Required**: Yes

### Conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.ConditionTypeDef]
- **Required**: Yes


# FirewallManagerRuleGroupTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### FirewallManagerStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FirewallManagerStatementTypeDef'>
- **Required**: Yes

### OverrideAction
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.OverrideActionOutputTypeDef'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes


# FirewallManagerStatementTypeDef

### ManagedRuleGroupStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupStatementOutputTypeDef]

### RuleGroupReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupReferenceStatementOutputTypeDef]


# ForwardedIPConfigTypeDef

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# GenerateMobileSdkReleaseUrlRequestTypeDef

### Platform
- **Type**: typing.Literal['ANDROID', 'IOS']
- **Required**: Yes

### ReleaseVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateMobileSdkReleaseUrlResponseTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GeoMatchStatementOutputTypeDef

### CountryCodes
- **Type**: typing.Optional[typing.List[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'XK', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### ForwardedIPConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ForwardedIPConfigTypeDef]


# GeoMatchStatementTypeDef

### CountryCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'XK', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### ForwardedIPConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ForwardedIPConfigTypeDef]


# GeoMatchStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetDecryptedAPIKeyRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### APIKey
- **Type**: <class 'str'>
- **Required**: Yes


# GetDecryptedAPIKeyResponseTypeDef

### TokenDomains
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIPSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetIPSetResponseTypeDef

### IPSet
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.IPSetTypeDef'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoggingConfigurationRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# GetLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetManagedRuleSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedRuleSetResponseTypeDef

### ManagedRuleSet
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleSetTypeDef'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMobileSdkReleaseRequestTypeDef

### Platform
- **Type**: typing.Literal['ANDROID', 'IOS']
- **Required**: Yes

### ReleaseVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetMobileSdkReleaseResponseTypeDef

### MobileSdkRelease
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.MobileSdkReleaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPermissionPolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPermissionPolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRateBasedStatementManagedKeysRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### WebACLName
- **Type**: <class 'str'>
- **Required**: Yes

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroupRuleName
- **Type**: typing.Optional[str]


# GetRateBasedStatementManagedKeysResponseTypeDef

### ManagedKeysIPV4
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementManagedKeysIPSetTypeDef'>
- **Required**: Yes

### ManagedKeysIPV6
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementManagedKeysIPSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegexPatternSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetRegexPatternSetResponseTypeDef

### RegexPatternSet
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetTypeDef'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRuleGroupRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[typing.Literal['CLOUDFRONT', 'REGIONAL']]

### Id
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# GetRuleGroupResponseTypeDef

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupTypeDef'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSampledRequestsRequestTypeDef

### WebAclArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuleMetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TimeWindowUnionTypeDef'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes


# GetSampledRequestsResponseTypeDef

### SampledRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.SampledHTTPRequestTypeDef]
- **Required**: Yes

### PopulationSize
- **Type**: <class 'int'>
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TimeWindowOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWebACLForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebACLForResourceResponseTypeDef

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.WebACLTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWebACLRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebACLResponseTypeDef

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.WebACLTypeDef'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationIntegrationURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HTTPHeaderTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# HTTPRequestTypeDef

### ClientIP
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### URI
- **Type**: typing.Optional[str]

### Method
- **Type**: typing.Optional[str]

### HTTPVersion
- **Type**: typing.Optional[str]

### Headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.HTTPHeaderTypeDef]]


# HeaderMatchPatternOutputTypeDef

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedHeaders
- **Type**: typing.Optional[typing.List[str]]

### ExcludedHeaders
- **Type**: typing.Optional[typing.List[str]]


# HeaderMatchPatternTypeDef

### All
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IncludedHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedHeaders
- **Type**: typing.Optional[typing.Sequence[str]]


# HeaderMatchPatternUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HeaderOrderTypeDef

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# HeadersOutputTypeDef

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.HeaderMatchPatternOutputTypeDef'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# HeadersTypeDef

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.HeaderMatchPatternUnionTypeDef'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# HeadersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IPSetForwardedIPConfigTypeDef

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes

### Position
- **Type**: typing.Literal['ANY', 'FIRST', 'LAST']
- **Required**: Yes


# IPSetReferenceStatementTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### IPSetForwardedIPConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.IPSetForwardedIPConfigTypeDef]


# IPSetSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LockToken
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# IPSetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### IPAddressVersion
- **Type**: typing.Literal['IPV4', 'IPV6']
- **Required**: Yes

### Addresses
- **Type**: typing.List[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ImmunityTimePropertyTypeDef

### ImmunityTime
- **Type**: <class 'int'>
- **Required**: Yes


# JA3FingerprintTypeDef

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# JA4FingerprintTypeDef

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# JsonBodyOutputTypeDef

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.JsonMatchPatternOutputTypeDef'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### InvalidFallbackBehavior
- **Type**: typing.Optional[typing.Literal['EVALUATE_AS_STRING', 'MATCH', 'NO_MATCH']]

### OversizeHandling
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']]


# JsonBodyTypeDef

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.JsonMatchPatternUnionTypeDef'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### InvalidFallbackBehavior
- **Type**: typing.Optional[typing.Literal['EVALUATE_AS_STRING', 'MATCH', 'NO_MATCH']]

### OversizeHandling
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']]


# JsonBodyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JsonMatchPatternOutputTypeDef

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedPaths
- **Type**: typing.Optional[typing.List[str]]


# JsonMatchPatternTypeDef

### All
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IncludedPaths
- **Type**: typing.Optional[typing.Sequence[str]]


# JsonMatchPatternUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LabelMatchStatementTypeDef

### Scope
- **Type**: typing.Literal['LABEL', 'NAMESPACE']
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# LabelNameConditionTypeDef

### LabelName
- **Type**: <class 'str'>
- **Required**: Yes


# LabelSummaryTypeDef

### Name
- **Type**: typing.Optional[str]


# LabelTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ListAPIKeysRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListAPIKeysResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### APIKeySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.APIKeySummaryTypeDef]
- **Required**: Yes

### ApplicationIntegrationURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAvailableManagedRuleGroupVersionsRequestTypeDef

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListAvailableManagedRuleGroupVersionsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupVersionTypeDef]
- **Required**: Yes

### CurrentDefaultVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAvailableManagedRuleGroupsRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListAvailableManagedRuleGroupsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedRuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIPSetsRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListIPSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### IPSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.IPSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLoggingConfigurationsRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# ListLoggingConfigurationsResponseTypeDef

### LoggingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LoggingConfigurationOutputTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListManagedRuleSetsRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListManagedRuleSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedRuleSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMobileSdkReleasesRequestTypeDef

### Platform
- **Type**: typing.Literal['ANDROID', 'IOS']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListMobileSdkReleasesResponseTypeDef

### ReleaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ReleaseSummaryTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRegexPatternSetsRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRegexPatternSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RegexPatternSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourcesForWebACLRequestTypeDef

### WebACLArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'APPLICATION_LOAD_BALANCER', 'APPSYNC', 'APP_RUNNER_SERVICE', 'COGNITO_USER_POOL', 'VERIFIED_ACCESS_INSTANCE']]


# ListResourcesForWebACLResponseTypeDef

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRuleGroupsRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRuleGroupsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTagsForResourceResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### TagInfoForResource
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TagInfoForResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWebACLsRequestTypeDef

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListWebACLsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### WebACLs
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.WebACLSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingConfigurationOutputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.List[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutputTypeDef]]

### ManagedByFirewallManager
- **Type**: typing.Optional[bool]

### LoggingFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.LoggingFilterOutputTypeDef]

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# LoggingConfigurationTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchTypeDef]]

### ManagedByFirewallManager
- **Type**: typing.Optional[bool]

### LoggingFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.LoggingFilterTypeDef]

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# LoggingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoggingFilterOutputTypeDef

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.FilterOutputTypeDef]
- **Required**: Yes

### DefaultBehavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes


# LoggingFilterTypeDef

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.FilterTypeDef]
- **Required**: Yes

### DefaultBehavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes


# ManagedProductDescriptorTypeDef

### VendorName
- **Type**: typing.Optional[str]

### ManagedRuleSetName
- **Type**: typing.Optional[str]

### ProductId
- **Type**: typing.Optional[str]

### ProductLink
- **Type**: typing.Optional[str]

### ProductTitle
- **Type**: typing.Optional[str]

### ProductDescription
- **Type**: typing.Optional[str]

### SnsTopicArn
- **Type**: typing.Optional[str]

### IsVersioningSupported
- **Type**: typing.Optional[bool]

### IsAdvancedManagedRuleSet
- **Type**: typing.Optional[bool]


# ManagedRuleGroupConfigOutputTypeDef

### LoginPath
- **Type**: typing.Optional[str]

### PayloadType
- **Type**: typing.Optional[typing.Literal['FORM_ENCODED', 'JSON']]

### UsernameField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.UsernameFieldTypeDef]

### PasswordField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.PasswordFieldTypeDef]

### AWSManagedRulesBotControlRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesBotControlRuleSetTypeDef]

### AWSManagedRulesATPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesATPRuleSetOutputTypeDef]

### AWSManagedRulesACFPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesACFPRuleSetOutputTypeDef]


# ManagedRuleGroupConfigTypeDef

### LoginPath
- **Type**: typing.Optional[str]

### PayloadType
- **Type**: typing.Optional[typing.Literal['FORM_ENCODED', 'JSON']]

### UsernameField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.UsernameFieldTypeDef]

### PasswordField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.PasswordFieldTypeDef]

### AWSManagedRulesBotControlRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesBotControlRuleSetTypeDef]

### AWSManagedRulesATPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesATPRuleSetUnionTypeDef]

### AWSManagedRulesACFPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesACFPRuleSetUnionTypeDef]


# ManagedRuleGroupConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ManagedRuleGroupStatementOutputTypeDef

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ExcludedRuleTypeDef]]

### ScopeDownStatement
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ManagedRuleGroupConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupConfigOutputTypeDef]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOverrideOutputTypeDef]]


# ManagedRuleGroupStatementTypeDef

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]

### ExcludedRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.ExcludedRuleTypeDef]]

### ScopeDownStatement
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ManagedRuleGroupConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupConfigUnionTypeDef]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOverrideUnionTypeDef]]


# ManagedRuleGroupStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ManagedRuleGroupSummaryTypeDef

### VendorName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VersioningSupported
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]


# ManagedRuleGroupVersionTypeDef

### Name
- **Type**: typing.Optional[str]

### LastUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ManagedRuleSetSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LockToken
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### LabelNamespace
- **Type**: typing.Optional[str]


# ManagedRuleSetTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### PublishedVersions
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleSetVersionTypeDef]]

### RecommendedVersion
- **Type**: typing.Optional[str]

### LabelNamespace
- **Type**: typing.Optional[str]


# ManagedRuleSetVersionTypeDef

### AssociatedRuleGroupArn
- **Type**: typing.Optional[str]

### Capacity
- **Type**: typing.Optional[int]

### ForecastedLifetime
- **Type**: typing.Optional[int]

### PublishTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ExpiryTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MobileSdkReleaseTypeDef

### ReleaseVersion
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### ReleaseNotes
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TagTypeDef]]


# NotStatementOutputTypeDef

### Statement
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# NotStatementTypeDef

### Statement
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# NotStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrStatementOutputTypeDef

### Statements
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# OrStatementTypeDef

### Statements
- **Type**: typing.Sequence[typing.Mapping[str, typing.Any]]
- **Required**: Yes


# OrStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OverrideActionOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OverrideActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PasswordFieldTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# PhoneNumberFieldTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# PutLoggingConfigurationRequestTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.LoggingConfigurationUnionTypeDef'>
- **Required**: Yes


# PutLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutManagedRuleSetVersionsRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### RecommendedVersion
- **Type**: typing.Optional[str]

### VersionsToPublish
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.VersionToPublishTypeDef]]


# PutManagedRuleSetVersionsResponseTypeDef

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutPermissionPolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# RateBasedStatementCustomKeyOutputTypeDef

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitHeaderOutputTypeDef]

### Cookie
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitCookieOutputTypeDef]

### QueryArgument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitQueryArgumentOutputTypeDef]

### QueryString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitQueryStringOutputTypeDef]

### HTTPMethod
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ForwardedIP
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IP
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### LabelNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitLabelNamespaceTypeDef]

### UriPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitUriPathOutputTypeDef]

### JA3Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitJA3FingerprintTypeDef]

### JA4Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitJA4FingerprintTypeDef]


# RateBasedStatementCustomKeyTypeDef

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitHeaderUnionTypeDef]

### Cookie
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitCookieUnionTypeDef]

### QueryArgument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitQueryArgumentUnionTypeDef]

### QueryString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitQueryStringUnionTypeDef]

### HTTPMethod
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ForwardedIP
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IP
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### LabelNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitLabelNamespaceTypeDef]

### UriPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitUriPathUnionTypeDef]

### JA3Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitJA3FingerprintTypeDef]

### JA4Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitJA4FingerprintTypeDef]


# RateBasedStatementCustomKeyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateBasedStatementManagedKeysIPSetTypeDef

### IPAddressVersion
- **Type**: typing.Optional[typing.Literal['IPV4', 'IPV6']]

### Addresses
- **Type**: typing.Optional[typing.List[str]]


# RateBasedStatementOutputTypeDef

### Limit
- **Type**: <class 'int'>
- **Required**: Yes

### AggregateKeyType
- **Type**: typing.Literal['CONSTANT', 'CUSTOM_KEYS', 'FORWARDED_IP', 'IP']
- **Required**: Yes

### EvaluationWindowSec
- **Type**: typing.Optional[int]

### ScopeDownStatement
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ForwardedIPConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ForwardedIPConfigTypeDef]

### CustomKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementCustomKeyOutputTypeDef]]


# RateBasedStatementTypeDef

### Limit
- **Type**: <class 'int'>
- **Required**: Yes

### AggregateKeyType
- **Type**: typing.Literal['CONSTANT', 'CUSTOM_KEYS', 'FORWARDED_IP', 'IP']
- **Required**: Yes

### EvaluationWindowSec
- **Type**: typing.Optional[int]

### ScopeDownStatement
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ForwardedIPConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ForwardedIPConfigTypeDef]

### CustomKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementCustomKeyUnionTypeDef]]


# RateBasedStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitCookieOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitCookieTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitCookieUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitHeaderOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitHeaderTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitHeaderUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitJA3FingerprintTypeDef

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# RateLimitJA4FingerprintTypeDef

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# RateLimitLabelNamespaceTypeDef

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# RateLimitQueryArgumentOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitQueryArgumentTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitQueryArgumentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitQueryStringOutputTypeDef

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitQueryStringTypeDef

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitQueryStringUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitUriPathOutputTypeDef

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitUriPathTypeDef

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RateLimitUriPathUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegexMatchStatementOutputTypeDef

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutputTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RegexMatchStatementTypeDef

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnionTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RegexMatchStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegexPatternSetReferenceStatementOutputTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutputTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RegexPatternSetReferenceStatementTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnionTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# RegexPatternSetReferenceStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegexPatternSetSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LockToken
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# RegexPatternSetTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RegularExpressionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RegexTypeDef]]


# RegexTypeDef

### RegexString
- **Type**: typing.Optional[str]


# ReleaseSummaryTypeDef

### ReleaseVersion
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# RequestBodyAssociatedResourceTypeConfigTypeDef

### DefaultSizeInspectionLimit
- **Type**: typing.Literal['KB_16', 'KB_32', 'KB_48', 'KB_64']
- **Required**: Yes


# RequestInspectionACFPOutputTypeDef

### PayloadType
- **Type**: typing.Literal['FORM_ENCODED', 'JSON']
- **Required**: Yes

### UsernameField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.UsernameFieldTypeDef]

### PasswordField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.PasswordFieldTypeDef]

### EmailField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.EmailFieldTypeDef]

### PhoneNumberFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.PhoneNumberFieldTypeDef]]

### AddressFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.AddressFieldTypeDef]]


# RequestInspectionACFPTypeDef

### PayloadType
- **Type**: typing.Literal['FORM_ENCODED', 'JSON']
- **Required**: Yes

### UsernameField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.UsernameFieldTypeDef]

### PasswordField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.PasswordFieldTypeDef]

### EmailField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.EmailFieldTypeDef]

### PhoneNumberFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.PhoneNumberFieldTypeDef]]

### AddressFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.AddressFieldTypeDef]]


# RequestInspectionACFPUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RequestInspectionTypeDef

### PayloadType
- **Type**: typing.Literal['FORM_ENCODED', 'JSON']
- **Required**: Yes

### UsernameField
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.UsernameFieldTypeDef'>
- **Required**: Yes

### PasswordField
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.PasswordFieldTypeDef'>
- **Required**: Yes


# ResponseInspectionBodyContainsOutputTypeDef

### SuccessStrings
- **Type**: typing.List[str]
- **Required**: Yes

### FailureStrings
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseInspectionBodyContainsTypeDef

### SuccessStrings
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FailureStrings
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseInspectionBodyContainsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspectionHeaderOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.List[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseInspectionHeaderTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseInspectionHeaderUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspectionJsonOutputTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.List[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseInspectionJsonTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseInspectionJsonUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspectionOutputTypeDef

### StatusCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionStatusCodeOutputTypeDef]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionHeaderOutputTypeDef]

### BodyContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionBodyContainsOutputTypeDef]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionJsonOutputTypeDef]


# ResponseInspectionStatusCodeOutputTypeDef

### SuccessCodes
- **Type**: typing.List[int]
- **Required**: Yes

### FailureCodes
- **Type**: typing.List[int]
- **Required**: Yes


# ResponseInspectionStatusCodeTypeDef

### SuccessCodes
- **Type**: typing.Sequence[int]
- **Required**: Yes

### FailureCodes
- **Type**: typing.Sequence[int]
- **Required**: Yes


# ResponseInspectionStatusCodeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspectionTypeDef

### StatusCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionStatusCodeUnionTypeDef]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionHeaderUnionTypeDef]

### BodyContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionBodyContainsUnionTypeDef]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionJsonUnionTypeDef]


# ResponseInspectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# RuleActionOutputTypeDef

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BlockActionOutputTypeDef]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AllowActionOutputTypeDef]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CountActionOutputTypeDef]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaActionOutputTypeDef]

### Challenge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeActionOutputTypeDef]


# RuleActionOverrideOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActionToUse
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOutputTypeDef'>
- **Required**: Yes


# RuleActionOverrideTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActionToUse
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RuleActionUnionTypeDef'>
- **Required**: Yes


# RuleActionOverrideUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleActionTypeDef

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BlockActionUnionTypeDef]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AllowActionUnionTypeDef]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CountActionUnionTypeDef]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaActionUnionTypeDef]

### Challenge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeActionUnionTypeDef]


# RuleActionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupReferenceStatementOutputTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ExcludedRuleTypeDef]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOverrideOutputTypeDef]]


# RuleGroupReferenceStatementTypeDef

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludedRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.ExcludedRuleTypeDef]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOverrideUnionTypeDef]]


# RuleGroupReferenceStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LockToken
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# RuleGroupTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Capacity
- **Type**: <class 'int'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleOutputTypeDef]]

### LabelNamespace
- **Type**: typing.Optional[str]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBodyTypeDef]]

### AvailableLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelSummaryTypeDef]]

### ConsumedLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelSummaryTypeDef]]


# RuleOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Statement
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.StatementOutputTypeDef'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOutputTypeDef]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.OverrideActionOutputTypeDef]

### RuleLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelTypeDef]]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaConfigTypeDef]

### ChallengeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeConfigTypeDef]


# RuleSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOutputTypeDef]


# RuleTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Statement
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.StatementUnionTypeDef'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionUnionTypeDef]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.OverrideActionUnionTypeDef]

### RuleLabels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.LabelTypeDef]]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaConfigTypeDef]

### ChallengeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeConfigTypeDef]


# RuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SampledHTTPRequestTypeDef

### Request
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.HTTPRequestTypeDef'>
- **Required**: Yes

### Weight
- **Type**: <class 'int'>
- **Required**: Yes

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Action
- **Type**: typing.Optional[str]

### RuleNameWithinRuleGroup
- **Type**: typing.Optional[str]

### RequestHeadersInserted
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.HTTPHeaderTypeDef]]

### ResponseCodeSent
- **Type**: typing.Optional[int]

### Labels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelTypeDef]]

### CaptchaResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaResponseTypeDef]

### ChallengeResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeResponseTypeDef]

### OverriddenAction
- **Type**: typing.Optional[str]


# SingleHeaderTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# SingleQueryArgumentTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# SizeConstraintStatementOutputTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutputTypeDef'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# SizeConstraintStatementTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnionTypeDef'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# SizeConstraintStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SqliMatchStatementOutputTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutputTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes

### SensitivityLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW']]


# SqliMatchStatementTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnionTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes

### SensitivityLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW']]


# SqliMatchStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StatementOutputTypeDef

### ByteMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ByteMatchStatementOutputTypeDef]

### SqliMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SqliMatchStatementOutputTypeDef]

### XssMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.XssMatchStatementOutputTypeDef]

### SizeConstraintStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SizeConstraintStatementOutputTypeDef]

### GeoMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.GeoMatchStatementOutputTypeDef]

### RuleGroupReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupReferenceStatementOutputTypeDef]

### IPSetReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.IPSetReferenceStatementTypeDef]

### RegexPatternSetReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetReferenceStatementOutputTypeDef]

### RateBasedStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementOutputTypeDef]

### AndStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AndStatementOutputTypeDef]

### OrStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.OrStatementOutputTypeDef]

### NotStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.NotStatementOutputTypeDef]

### ManagedRuleGroupStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupStatementOutputTypeDef]

### LabelMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.LabelMatchStatementTypeDef]

### RegexMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RegexMatchStatementOutputTypeDef]


# StatementTypeDef

### ByteMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ByteMatchStatementUnionTypeDef]

### SqliMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SqliMatchStatementUnionTypeDef]

### XssMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.XssMatchStatementUnionTypeDef]

### SizeConstraintStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SizeConstraintStatementUnionTypeDef]

### GeoMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.GeoMatchStatementUnionTypeDef]

### RuleGroupReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupReferenceStatementUnionTypeDef]

### IPSetReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.IPSetReferenceStatementTypeDef]

### RegexPatternSetReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetReferenceStatementUnionTypeDef]

### RateBasedStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementUnionTypeDef]

### AndStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AndStatementUnionTypeDef]

### OrStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.OrStatementUnionTypeDef]

### NotStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.NotStatementUnionTypeDef]

### ManagedRuleGroupStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupStatementUnionTypeDef]

### LabelMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.LabelMatchStatementTypeDef]

### RegexMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RegexMatchStatementUnionTypeDef]


# StatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagInfoForResourceTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TagTypeDef]]


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TextTransformationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeWindowOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TimeWindowTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TimestampTypeDef'>
- **Required**: Yes


# TimeWindowUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateIPSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Addresses
- **Type**: typing.Sequence[str]
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateIPSetResponseTypeDef

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateManagedRuleSetVersionExpiryDateRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### VersionToExpire
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiryTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TimestampTypeDef'>
- **Required**: Yes


# UpdateManagedRuleSetVersionExpiryDateResponseTypeDef

### ExpiringVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiryTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRegexPatternSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### RegularExpressionList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RegexTypeDef]
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateRegexPatternSetResponseTypeDef

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRuleGroupRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnionTypeDef]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBodyTypeDef]]


# UpdateRuleGroupResponseTypeDef

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWebACLRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.DefaultActionUnionTypeDef'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnionTypeDef]]

### DataProtectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionConfigUnionTypeDef]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBodyTypeDef]]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaConfigTypeDef]

### ChallengeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeConfigTypeDef]

### TokenDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### AssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AssociationConfigUnionTypeDef]


# UpdateWebACLResponseTypeDef

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsernameFieldTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# VersionToPublishTypeDef

### AssociatedRuleGroupArn
- **Type**: typing.Optional[str]

### ForecastedLifetime
- **Type**: typing.Optional[int]


# VisibilityConfigTypeDef

### SampledRequestsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CloudWatchMetricsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes


# WebACLSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### LockToken
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# WebACLTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.DefaultActionOutputTypeDef'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfigTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleOutputTypeDef]]

### DataProtectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionConfigOutputTypeDef]

### Capacity
- **Type**: typing.Optional[int]

### PreProcessFirewallManagerRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.FirewallManagerRuleGroupTypeDef]]

### PostProcessFirewallManagerRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.FirewallManagerRuleGroupTypeDef]]

### ManagedByFirewallManager
- **Type**: typing.Optional[bool]

### LabelNamespace
- **Type**: typing.Optional[str]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBodyTypeDef]]

### CaptchaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaConfigTypeDef]

### ChallengeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeConfigTypeDef]

### TokenDomains
- **Type**: typing.Optional[typing.List[str]]

### AssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AssociationConfigOutputTypeDef]

### RetrofittedByFirewallManager
- **Type**: typing.Optional[bool]


# XssMatchStatementOutputTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutputTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# XssMatchStatementTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnionTypeDef'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformationTypeDef]
- **Required**: Yes


# XssMatchStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


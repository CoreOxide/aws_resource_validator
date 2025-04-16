# Wafv2 Classes

# APIKeySummary

### TokenDomains
- **Type**: typing.Optional[typing.List[str]]

### APIKey
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Version
- **Type**: typing.Optional[int]


# AWSManagedRulesACFPRuleSet

### CreationPath
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationPagePath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RequestInspectionACFPUnion'>
- **Required**: Yes

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionUnion]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesACFPRuleSetOutput

### CreationPath
- **Type**: <class 'str'>
- **Required**: Yes

### RegistrationPagePath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RequestInspectionACFPOutput'>
- **Required**: Yes

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionOutput]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesACFPRuleSetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AWSManagedRulesATPRuleSet

### LoginPath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: <class 'NoneType'>

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionUnion]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesATPRuleSetOutput

### LoginPath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: <class 'NoneType'>

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionOutput]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesATPRuleSetUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AWSManagedRulesBotControlRuleSet

### InspectionLevel
- **Type**: typing.Literal['COMMON', 'TARGETED']
- **Required**: Yes

### EnableMachineLearning
- **Type**: typing.Optional[bool]


# ActionCondition

### Action
- **Type**: typing.Literal['ALLOW', 'BLOCK', 'CAPTCHA', 'CHALLENGE', 'COUNT', 'EXCLUDED_AS_COUNT']
- **Required**: Yes


# AddressField

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# AllowAction

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingUnion]


# AllowActionOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingOutput]


# AllowActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AndStatement

### Statements
- **Type**: typing.Sequence[typing.Mapping[str, typing.Any]]
- **Required**: Yes


# AndStatementOutput

### Statements
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# AndStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateWebACLRequest

### WebACLArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationConfig

### RequestBody
- **Type**: typing.Optional[typing.Mapping[typing.Literal['API_GATEWAY', 'APP_RUNNER_SERVICE', 'CLOUDFRONT', 'COGNITO_USER_POOL', 'VERIFIED_ACCESS_INSTANCE'], aws_resource_validator.pydantic_models.wafv2_classes.RequestBodyAssociatedResourceTypeConfig]]


# AssociationConfigOutput

### RequestBody
- **Type**: typing.Optional[typing.Dict[typing.Literal['API_GATEWAY', 'APP_RUNNER_SERVICE', 'CLOUDFRONT', 'COGNITO_USER_POOL', 'VERIFIED_ACCESS_INSTANCE'], aws_resource_validator.pydantic_models.wafv2_classes.RequestBodyAssociatedResourceTypeConfig]]


# AssociationConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockAction

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseUnion]


# BlockActionOutput

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseOutput]


# BlockActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Body

### OversizeHandling
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']]


# ByteMatchStatement

### SearchString
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.Blob'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnion'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# ByteMatchStatementOutput

### SearchString
- **Type**: <class 'bytes'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# ByteMatchStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaptchaAction

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingUnion]


# CaptchaActionOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingOutput]


# CaptchaActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaptchaConfig

### ImmunityTimeProperty
- **Type**: <class 'NoneType'>


# CaptchaResponse

### ResponseCode
- **Type**: typing.Optional[int]

### SolveTimestamp
- **Type**: typing.Optional[int]

### FailureReason
- **Type**: typing.Optional[typing.Literal['TOKEN_DOMAIN_MISMATCH', 'TOKEN_EXPIRED', 'TOKEN_INVALID', 'TOKEN_MISSING']]


# ChallengeAction

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingUnion]


# ChallengeActionOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingOutput]


# ChallengeActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChallengeConfig

### ImmunityTimeProperty
- **Type**: <class 'NoneType'>


# ChallengeResponse

### ResponseCode
- **Type**: typing.Optional[int]

### SolveTimestamp
- **Type**: typing.Optional[int]

### FailureReason
- **Type**: typing.Optional[typing.Literal['TOKEN_DOMAIN_MISMATCH', 'TOKEN_EXPIRED', 'TOKEN_INVALID', 'TOKEN_MISSING']]


# CheckCapacityRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnion]
- **Required**: Yes


# CheckCapacityResponse

### Capacity
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# Condition

### ActionCondition
- **Type**: <class 'NoneType'>

### LabelNameCondition
- **Type**: <class 'NoneType'>


# CookieMatchPattern

### All
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IncludedCookies
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedCookies
- **Type**: typing.Optional[typing.Sequence[str]]


# CookieMatchPatternOutput

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedCookies
- **Type**: typing.Optional[typing.List[str]]

### ExcludedCookies
- **Type**: typing.Optional[typing.List[str]]


# CookieMatchPatternUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Cookies

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.CookieMatchPatternUnion'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# CookiesOutput

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.CookieMatchPatternOutput'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# CookiesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CountAction

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingUnion]


# CountActionOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CustomRequestHandlingOutput]


# CountActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAPIKeyRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### TokenDomains
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CreateAPIKeyResponse

### APIKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIPSetRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Tag]]


# CreateIPSetResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.IPSetSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegexPatternSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### RegularExpressionList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Regex]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Tag]]


# CreateRegexPatternSetResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleGroupRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnion]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Tag]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBody]]


# CreateRuleGroupResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWebACLRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### DefaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.DefaultActionUnion'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnion]]

### DataProtectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionConfigUnion]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Tag]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBody]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>

### TokenDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### AssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AssociationConfigUnion]


# CreateWebACLResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.WebACLSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# CustomHTTPHeader

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# CustomRequestHandling

### InsertHeaders
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.CustomHTTPHeader]
- **Required**: Yes


# CustomRequestHandlingOutput

### InsertHeaders
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.CustomHTTPHeader]
- **Required**: Yes


# CustomRequestHandlingUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomResponse

### ResponseCode
- **Type**: <class 'int'>
- **Required**: Yes

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseHeaders
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.CustomHTTPHeader]]


# CustomResponseBody

### ContentType
- **Type**: typing.Literal['APPLICATION_JSON', 'TEXT_HTML', 'TEXT_PLAIN']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


# CustomResponseOutput

### ResponseCode
- **Type**: <class 'int'>
- **Required**: Yes

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.CustomHTTPHeader]]


# CustomResponseUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataProtection

### Field
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToProtect'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['HASH', 'SUBSTITUTION']
- **Required**: Yes

### ExcludeRuleMatchDetails
- **Type**: typing.Optional[bool]

### ExcludeRateBasedDetails
- **Type**: typing.Optional[bool]


# DataProtectionConfig

### DataProtections
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.DataProtection]
- **Required**: Yes


# DataProtectionConfigOutput

### DataProtections
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionOutput]
- **Required**: Yes


# DataProtectionConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataProtectionOutput

### Field
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToProtectOutput'>
- **Required**: Yes

### Action
- **Type**: typing.Literal['HASH', 'SUBSTITUTION']
- **Required**: Yes

### ExcludeRuleMatchDetails
- **Type**: typing.Optional[bool]

### ExcludeRateBasedDetails
- **Type**: typing.Optional[bool]


# DefaultAction

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BlockAction]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AllowAction]


# DefaultActionOutput

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BlockActionOutput]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AllowActionOutput]


# DefaultActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAPIKeyRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### APIKey
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFirewallManagerRuleGroupsRequest

### WebACLArn
- **Type**: <class 'str'>
- **Required**: Yes

### WebACLLockToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFirewallManagerRuleGroupsResponse

### NextWebACLLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIPSetRequest

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


# DeleteLoggingConfigurationRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# DeletePermissionPolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegexPatternSetRequest

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


# DeleteRuleGroupRequest

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


# DeleteWebACLRequest

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


# DescribeAllManagedProductsRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes


# DescribeAllManagedProductsResponse

### ManagedProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedProductDescriptor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeManagedProductsByVendorRequest

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes


# DescribeManagedProductsByVendorResponse

### ManagedProducts
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedProductDescriptor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeManagedRuleGroupRequest

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


# DescribeManagedRuleGroupResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleSummary]
- **Required**: Yes

### LabelNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### AvailableLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelSummary]
- **Required**: Yes

### ConsumedLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateWebACLRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmailField

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# ExcludedRule

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# FieldToMatch

### SingleHeader
- **Type**: <class 'NoneType'>

### SingleQueryArgument
- **Type**: <class 'NoneType'>

### AllQueryArguments
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### UriPath
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### QueryString
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Body
- **Type**: <class 'NoneType'>

### Method
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### JsonBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.JsonBodyUnion]

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.HeadersUnion]

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CookiesUnion]

### HeaderOrder
- **Type**: <class 'NoneType'>

### JA3Fingerprint
- **Type**: <class 'NoneType'>

### JA4Fingerprint
- **Type**: <class 'NoneType'>


# FieldToMatchOutput

### SingleHeader
- **Type**: <class 'NoneType'>

### SingleQueryArgument
- **Type**: <class 'NoneType'>

### AllQueryArguments
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### UriPath
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### QueryString
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Body
- **Type**: <class 'NoneType'>

### Method
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### JsonBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.JsonBodyOutput]

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.HeadersOutput]

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CookiesOutput]

### HeaderOrder
- **Type**: <class 'NoneType'>

### JA3Fingerprint
- **Type**: <class 'NoneType'>

### JA4Fingerprint
- **Type**: <class 'NoneType'>


# FieldToMatchUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FieldToProtect

### FieldType
- **Type**: typing.Literal['BODY', 'QUERY_STRING', 'SINGLE_COOKIE', 'SINGLE_HEADER', 'SINGLE_QUERY_ARGUMENT']
- **Required**: Yes

### FieldKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# FieldToProtectOutput

### FieldType
- **Type**: typing.Literal['BODY', 'QUERY_STRING', 'SINGLE_COOKIE', 'SINGLE_HEADER', 'SINGLE_QUERY_ARGUMENT']
- **Required**: Yes

### FieldKeys
- **Type**: typing.Optional[typing.List[str]]


# Filter

### Behavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes

### Requirement
- **Type**: typing.Literal['MEETS_ALL', 'MEETS_ANY']
- **Required**: Yes

### Conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Condition]
- **Required**: Yes


# FilterOutput

### Behavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes

### Requirement
- **Type**: typing.Literal['MEETS_ALL', 'MEETS_ANY']
- **Required**: Yes

### Conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.Condition]
- **Required**: Yes


# FirewallManagerRuleGroup

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### FirewallManagerStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FirewallManagerStatement'>
- **Required**: Yes

### OverrideAction
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.OverrideActionOutput'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes


# FirewallManagerStatement

### ManagedRuleGroupStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupStatementOutput]

### RuleGroupReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupReferenceStatementOutput]


# ForwardedIPConfig

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# GenerateMobileSdkReleaseUrlRequest

### Platform
- **Type**: typing.Literal['ANDROID', 'IOS']
- **Required**: Yes

### ReleaseVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateMobileSdkReleaseUrlResponse

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GeoMatchStatement

### CountryCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'XK', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### ForwardedIPConfig
- **Type**: <class 'NoneType'>


# GeoMatchStatementOutput

### CountryCodes
- **Type**: typing.Optional[typing.List[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'XK', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### ForwardedIPConfig
- **Type**: <class 'NoneType'>


# GeoMatchStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetDecryptedAPIKeyRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### APIKey
- **Type**: <class 'str'>
- **Required**: Yes


# GetDecryptedAPIKeyResponse

### TokenDomains
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetIPSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetIPSetResponse

### IPSet
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.IPSet'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoggingConfigurationRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# GetLoggingConfigurationResponse

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedRuleSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedRuleSetResponse

### ManagedRuleSet
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleSet'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetMobileSdkReleaseRequest

### Platform
- **Type**: typing.Literal['ANDROID', 'IOS']
- **Required**: Yes

### ReleaseVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetMobileSdkReleaseResponse

### MobileSdkRelease
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.MobileSdkRelease'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetPermissionPolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPermissionPolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetRateBasedStatementManagedKeysRequest

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


# GetRateBasedStatementManagedKeysResponse

### ManagedKeysIPV4
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementManagedKeysIPSet'>
- **Required**: Yes

### ManagedKeysIPV6
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementManagedKeysIPSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegexPatternSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetRegexPatternSetResponse

### RegexPatternSet
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSet'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetRuleGroupRequest

### Name
- **Type**: typing.Optional[str]

### Scope
- **Type**: typing.Optional[typing.Literal['CLOUDFRONT', 'REGIONAL']]

### Id
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# GetRuleGroupResponse

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RuleGroup'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetSampledRequestsRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TimeWindowUnion'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes


# GetSampledRequestsResponse

### SampledRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.SampledHTTPRequest]
- **Required**: Yes

### PopulationSize
- **Type**: <class 'int'>
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TimeWindowOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetWebACLForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebACLForResourceResponse

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.WebACL'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetWebACLRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebACLResponse

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.WebACL'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationIntegrationURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# HTTPHeader

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# HTTPRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.HTTPHeader]]


# HeaderMatchPattern

### All
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IncludedHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludedHeaders
- **Type**: typing.Optional[typing.Sequence[str]]


# HeaderMatchPatternOutput

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedHeaders
- **Type**: typing.Optional[typing.List[str]]

### ExcludedHeaders
- **Type**: typing.Optional[typing.List[str]]


# HeaderMatchPatternUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HeaderOrder

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# Headers

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.HeaderMatchPatternUnion'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# HeadersOutput

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.HeaderMatchPatternOutput'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# HeadersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IPSet

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


# IPSetForwardedIPConfig

### HeaderName
- **Type**: <class 'str'>
- **Required**: Yes

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes

### Position
- **Type**: typing.Literal['ANY', 'FIRST', 'LAST']
- **Required**: Yes


# IPSetReferenceStatement

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### IPSetForwardedIPConfig
- **Type**: <class 'NoneType'>


# IPSetSummary

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


# ImmunityTimeProperty

### ImmunityTime
- **Type**: <class 'int'>
- **Required**: Yes


# JA3Fingerprint

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# JA4Fingerprint

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# JsonBody

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.JsonMatchPatternUnion'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### InvalidFallbackBehavior
- **Type**: typing.Optional[typing.Literal['EVALUATE_AS_STRING', 'MATCH', 'NO_MATCH']]

### OversizeHandling
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']]


# JsonBodyOutput

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.JsonMatchPatternOutput'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### InvalidFallbackBehavior
- **Type**: typing.Optional[typing.Literal['EVALUATE_AS_STRING', 'MATCH', 'NO_MATCH']]

### OversizeHandling
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']]


# JsonBodyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JsonMatchPattern

### All
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IncludedPaths
- **Type**: typing.Optional[typing.Sequence[str]]


# JsonMatchPatternOutput

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedPaths
- **Type**: typing.Optional[typing.List[str]]


# JsonMatchPatternUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Label

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# LabelMatchStatement

### Scope
- **Type**: typing.Literal['LABEL', 'NAMESPACE']
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# LabelNameCondition

### LabelName
- **Type**: <class 'str'>
- **Required**: Yes


# LabelSummary

### Name
- **Type**: typing.Optional[str]


# ListAPIKeysRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListAPIKeysResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### APIKeySummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.APIKeySummary]
- **Required**: Yes

### ApplicationIntegrationURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListAvailableManagedRuleGroupVersionsRequest

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


# ListAvailableManagedRuleGroupVersionsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupVersion]
- **Required**: Yes

### CurrentDefaultVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListAvailableManagedRuleGroupsRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListAvailableManagedRuleGroupsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedRuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListIPSetsRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListIPSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### IPSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.IPSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListLoggingConfigurationsRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# ListLoggingConfigurationsResponse

### LoggingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LoggingConfigurationOutput]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListManagedRuleSetsRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListManagedRuleSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedRuleSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListMobileSdkReleasesRequest

### Platform
- **Type**: typing.Literal['ANDROID', 'IOS']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListMobileSdkReleasesResponse

### ReleaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ReleaseSummary]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListRegexPatternSetsRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRegexPatternSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RegexPatternSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListResourcesForWebACLRequest

### WebACLArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'APPLICATION_LOAD_BALANCER', 'APPSYNC', 'APP_RUNNER_SERVICE', 'COGNITO_USER_POOL', 'VERIFIED_ACCESS_INSTANCE']]


# ListResourcesForWebACLResponse

### ResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListRuleGroupsRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRuleGroupsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTagsForResourceResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### TagInfoForResource
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.TagInfoForResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# ListWebACLsRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListWebACLsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### WebACLs
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.WebACLSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingConfiguration

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatch]]

### ManagedByFirewallManager
- **Type**: typing.Optional[bool]

### LoggingFilter
- **Type**: <class 'NoneType'>

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# LoggingConfigurationOutput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.List[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutput]]

### ManagedByFirewallManager
- **Type**: typing.Optional[bool]

### LoggingFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.LoggingFilterOutput]

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# LoggingConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LoggingFilter

### Filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Filter]
- **Required**: Yes

### DefaultBehavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes


# LoggingFilterOutput

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.FilterOutput]
- **Required**: Yes

### DefaultBehavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes


# ManagedProductDescriptor

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


# ManagedRuleGroupConfig

### LoginPath
- **Type**: typing.Optional[str]

### PayloadType
- **Type**: typing.Optional[typing.Literal['FORM_ENCODED', 'JSON']]

### UsernameField
- **Type**: <class 'NoneType'>

### PasswordField
- **Type**: <class 'NoneType'>

### AWSManagedRulesBotControlRuleSet
- **Type**: <class 'NoneType'>

### AWSManagedRulesATPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesATPRuleSetUnion]

### AWSManagedRulesACFPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesACFPRuleSetUnion]


# ManagedRuleGroupConfigOutput

### LoginPath
- **Type**: typing.Optional[str]

### PayloadType
- **Type**: typing.Optional[typing.Literal['FORM_ENCODED', 'JSON']]

### UsernameField
- **Type**: <class 'NoneType'>

### PasswordField
- **Type**: <class 'NoneType'>

### AWSManagedRulesBotControlRuleSet
- **Type**: <class 'NoneType'>

### AWSManagedRulesATPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesATPRuleSetOutput]

### AWSManagedRulesACFPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AWSManagedRulesACFPRuleSetOutput]


# ManagedRuleGroupConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ManagedRuleGroupStatement

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]

### ExcludedRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.ExcludedRule]]

### ScopeDownStatement
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ManagedRuleGroupConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupConfigUnion]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOverrideUnion]]


# ManagedRuleGroupStatementOutput

### VendorName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Optional[str]

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ExcludedRule]]

### ScopeDownStatement
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ManagedRuleGroupConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupConfigOutput]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOverrideOutput]]


# ManagedRuleGroupStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ManagedRuleGroupSummary

### VendorName
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VersioningSupported
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]


# ManagedRuleGroupVersion

### Name
- **Type**: typing.Optional[str]

### LastUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ManagedRuleSet

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleSetVersion]]

### RecommendedVersion
- **Type**: typing.Optional[str]

### LabelNamespace
- **Type**: typing.Optional[str]


# ManagedRuleSetSummary

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


# ManagedRuleSetVersion

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


# MobileSdkRelease

### ReleaseVersion
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### ReleaseNotes
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.Tag]]


# NotStatement

### Statement
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# NotStatementOutput

### Statement
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# NotStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OrStatement

### Statements
- **Type**: typing.Sequence[typing.Mapping[str, typing.Any]]
- **Required**: Yes


# OrStatementOutput

### Statements
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# OrStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OverrideActionOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OverrideActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PasswordField

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# PhoneNumberField

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# PutLoggingConfigurationRequest

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.LoggingConfigurationUnion'>
- **Required**: Yes


# PutLoggingConfigurationResponse

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# PutManagedRuleSetVersionsRequest

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.VersionToPublish]]


# PutManagedRuleSetVersionsResponse

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# PutPermissionPolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# RateBasedStatement

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
- **Type**: <class 'NoneType'>

### CustomKeys
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementCustomKeyUnion]]


# RateBasedStatementCustomKey

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitHeaderUnion]

### Cookie
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitCookieUnion]

### QueryArgument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitQueryArgumentUnion]

### QueryString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitQueryStringUnion]

### HTTPMethod
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ForwardedIP
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### IP
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### LabelNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitLabelNamespace]

### UriPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitUriPathUnion]

### JA3Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitJA3Fingerprint]

### JA4Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitJA4Fingerprint]


# RateBasedStatementCustomKeyOutput

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitHeaderOutput]

### Cookie
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitCookieOutput]

### QueryArgument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitQueryArgumentOutput]

### QueryString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitQueryStringOutput]

### HTTPMethod
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ForwardedIP
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IP
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### LabelNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitLabelNamespace]

### UriPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitUriPathOutput]

### JA3Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitJA3Fingerprint]

### JA4Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateLimitJA4Fingerprint]


# RateBasedStatementCustomKeyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateBasedStatementManagedKeysIPSet

### IPAddressVersion
- **Type**: typing.Optional[typing.Literal['IPV4', 'IPV6']]

### Addresses
- **Type**: typing.Optional[typing.List[str]]


# RateBasedStatementOutput

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
- **Type**: <class 'NoneType'>

### CustomKeys
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementCustomKeyOutput]]


# RateBasedStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitCookie

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitCookieOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitCookieUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitHeader

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitHeaderOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitHeaderUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitJA3Fingerprint

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# RateLimitJA4Fingerprint

### FallbackBehavior
- **Type**: typing.Literal['MATCH', 'NO_MATCH']
- **Required**: Yes


# RateLimitLabelNamespace

### Namespace
- **Type**: <class 'str'>
- **Required**: Yes


# RateLimitQueryArgument

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitQueryArgumentOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitQueryArgumentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitQueryString

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitQueryStringOutput

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitQueryStringUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RateLimitUriPath

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitUriPathOutput

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitUriPathUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Regex

### RegexString
- **Type**: typing.Optional[str]


# RegexMatchStatement

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnion'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RegexMatchStatementOutput

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RegexMatchStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegexPatternSet

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RegularExpressionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.Regex]]


# RegexPatternSetReferenceStatement

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnion'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RegexPatternSetReferenceStatementOutput

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# RegexPatternSetReferenceStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegexPatternSetSummary

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


# ReleaseSummary

### ReleaseVersion
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# RequestBodyAssociatedResourceTypeConfig

### DefaultSizeInspectionLimit
- **Type**: typing.Literal['KB_16', 'KB_32', 'KB_48', 'KB_64']
- **Required**: Yes


# RequestInspection

### PayloadType
- **Type**: typing.Literal['FORM_ENCODED', 'JSON']
- **Required**: Yes

### UsernameField
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.UsernameField'>
- **Required**: Yes

### PasswordField
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.PasswordField'>
- **Required**: Yes


# RequestInspectionACFP

### PayloadType
- **Type**: typing.Literal['FORM_ENCODED', 'JSON']
- **Required**: Yes

### UsernameField
- **Type**: <class 'NoneType'>

### PasswordField
- **Type**: <class 'NoneType'>

### EmailField
- **Type**: <class 'NoneType'>

### PhoneNumberFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.PhoneNumberField]]

### AddressFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.AddressField]]


# RequestInspectionACFPOutput

### PayloadType
- **Type**: typing.Literal['FORM_ENCODED', 'JSON']
- **Required**: Yes

### UsernameField
- **Type**: <class 'NoneType'>

### PasswordField
- **Type**: <class 'NoneType'>

### EmailField
- **Type**: <class 'NoneType'>

### PhoneNumberFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.PhoneNumberField]]

### AddressFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.AddressField]]


# RequestInspectionACFPUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspection

### StatusCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionStatusCodeUnion]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionHeaderUnion]

### BodyContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionBodyContainsUnion]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionJsonUnion]


# ResponseInspectionBodyContains

### SuccessStrings
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FailureStrings
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseInspectionBodyContainsOutput

### SuccessStrings
- **Type**: typing.List[str]
- **Required**: Yes

### FailureStrings
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseInspectionBodyContainsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspectionHeader

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseInspectionHeaderOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.List[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseInspectionHeaderUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspectionJson

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResponseInspectionJsonOutput

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.List[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseInspectionJsonUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspectionOutput

### StatusCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionStatusCodeOutput]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionHeaderOutput]

### BodyContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionBodyContainsOutput]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ResponseInspectionJsonOutput]


# ResponseInspectionStatusCode

### SuccessCodes
- **Type**: typing.Sequence[int]
- **Required**: Yes

### FailureCodes
- **Type**: typing.Sequence[int]
- **Required**: Yes


# ResponseInspectionStatusCodeOutput

### SuccessCodes
- **Type**: typing.List[int]
- **Required**: Yes

### FailureCodes
- **Type**: typing.List[int]
- **Required**: Yes


# ResponseInspectionStatusCodeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseInspectionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# Rule

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Statement
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.StatementUnion'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionUnion]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.OverrideActionUnion]

### RuleLabels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Label]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>


# RuleAction

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BlockActionUnion]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AllowActionUnion]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CountActionUnion]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaActionUnion]

### Challenge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeActionUnion]


# RuleActionOutput

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.BlockActionOutput]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AllowActionOutput]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CountActionOutput]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.CaptchaActionOutput]

### Challenge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ChallengeActionOutput]


# RuleActionOverride

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActionToUse
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RuleActionUnion'>
- **Required**: Yes


# RuleActionOverrideOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActionToUse
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOutput'>
- **Required**: Yes


# RuleActionOverrideUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleActionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroup

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleOutput]]

### LabelNamespace
- **Type**: typing.Optional[str]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBody]]

### AvailableLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelSummary]]

### ConsumedLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.LabelSummary]]


# RuleGroupReferenceStatement

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludedRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.ExcludedRule]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOverrideUnion]]


# RuleGroupReferenceStatementOutput

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.ExcludedRule]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOverrideOutput]]


# RuleGroupReferenceStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleGroupSummary

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


# RuleOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Statement
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.StatementOutput'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOutput]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.OverrideActionOutput]

### RuleLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.Label]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>


# RuleSummary

### Name
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleActionOutput]


# RuleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SampledHTTPRequest

### Request
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.HTTPRequest'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.HTTPHeader]]

### ResponseCodeSent
- **Type**: typing.Optional[int]

### Labels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.Label]]

### CaptchaResponse
- **Type**: <class 'NoneType'>

### ChallengeResponse
- **Type**: <class 'NoneType'>

### OverriddenAction
- **Type**: typing.Optional[str]


# SingleHeader

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# SingleQueryArgument

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# SizeConstraintStatement

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnion'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# SizeConstraintStatementOutput

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# SizeConstraintStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SqliMatchStatement

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnion'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes

### SensitivityLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW']]


# SqliMatchStatementOutput

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes

### SensitivityLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW']]


# SqliMatchStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Statement

### ByteMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ByteMatchStatementUnion]

### SqliMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SqliMatchStatementUnion]

### XssMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.XssMatchStatementUnion]

### SizeConstraintStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SizeConstraintStatementUnion]

### GeoMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.GeoMatchStatementUnion]

### RuleGroupReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupReferenceStatementUnion]

### IPSetReferenceStatement
- **Type**: <class 'NoneType'>

### RegexPatternSetReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetReferenceStatementUnion]

### RateBasedStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementUnion]

### AndStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AndStatementUnion]

### OrStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.OrStatementUnion]

### NotStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.NotStatementUnion]

### ManagedRuleGroupStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupStatementUnion]

### LabelMatchStatement
- **Type**: <class 'NoneType'>

### RegexMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RegexMatchStatementUnion]


# StatementOutput

### ByteMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ByteMatchStatementOutput]

### SqliMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SqliMatchStatementOutput]

### XssMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.XssMatchStatementOutput]

### SizeConstraintStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.SizeConstraintStatementOutput]

### GeoMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.GeoMatchStatementOutput]

### RuleGroupReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RuleGroupReferenceStatementOutput]

### IPSetReferenceStatement
- **Type**: <class 'NoneType'>

### RegexPatternSetReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RegexPatternSetReferenceStatementOutput]

### RateBasedStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RateBasedStatementOutput]

### AndStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AndStatementOutput]

### OrStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.OrStatementOutput]

### NotStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.NotStatementOutput]

### ManagedRuleGroupStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.ManagedRuleGroupStatementOutput]

### LabelMatchStatement
- **Type**: <class 'NoneType'>

### RegexMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.RegexMatchStatementOutput]


# StatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagInfoForResource

### ResourceARN
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.Tag]]


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Tag]
- **Required**: Yes


# TextTransformation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimeWindow

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.Timestamp'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.Timestamp'>
- **Required**: Yes


# TimeWindowOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TimeWindowUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateIPSetRequest

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


# UpdateIPSetResponse

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateManagedRuleSetVersionExpiryDateRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.Timestamp'>
- **Required**: Yes


# UpdateManagedRuleSetVersionExpiryDateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRegexPatternSetRequest

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.Regex]
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateRegexPatternSetResponse

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRuleGroupRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnion]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBody]]


# UpdateRuleGroupResponse

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWebACLRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.DefaultActionUnion'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.RuleUnion]]

### DataProtectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionConfigUnion]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBody]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>

### TokenDomains
- **Type**: typing.Optional[typing.Sequence[str]]

### AssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AssociationConfigUnion]


# UpdateWebACLResponse

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# UsernameField

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# VersionToPublish

### AssociatedRuleGroupArn
- **Type**: typing.Optional[str]

### ForecastedLifetime
- **Type**: typing.Optional[int]


# VisibilityConfig

### SampledRequestsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CloudWatchMetricsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes


# WebACL

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.DefaultActionOutput'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.RuleOutput]]

### DataProtectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.DataProtectionConfigOutput]

### Capacity
- **Type**: typing.Optional[int]

### PreProcessFirewallManagerRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.FirewallManagerRuleGroup]]

### PostProcessFirewallManagerRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2_classes.FirewallManagerRuleGroup]]

### ManagedByFirewallManager
- **Type**: typing.Optional[bool]

### LabelNamespace
- **Type**: typing.Optional[str]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2_classes.CustomResponseBody]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>

### TokenDomains
- **Type**: typing.Optional[typing.List[str]]

### AssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2_classes.AssociationConfigOutput]

### RetrofittedByFirewallManager
- **Type**: typing.Optional[bool]


# WebACLSummary

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


# XssMatchStatement

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchUnion'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# XssMatchStatementOutput

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2_classes.TextTransformation]
- **Required**: Yes


# XssMatchStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">


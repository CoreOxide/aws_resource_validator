# Wafv2 Wafv2 Classes

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RequestInspectionACFP, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RequestInspectionACFPOutput]
- **Required**: Yes

### ResponseInspection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspection, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionOutput, NoneType]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RequestInspectionACFPOutput'>
- **Required**: Yes

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionOutput]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesATPRuleSet

### LoginPath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: <class 'NoneType'>

### ResponseInspection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspection, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionOutput, NoneType]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


# AWSManagedRulesATPRuleSetOutput

### LoginPath
- **Type**: <class 'str'>
- **Required**: Yes

### RequestInspection
- **Type**: <class 'NoneType'>

### ResponseInspection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionOutput]

### EnableRegexInPath
- **Type**: typing.Optional[bool]


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandling, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandlingOutput, NoneType]


# AllowActionOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandlingOutput]


# AndStatement

### Statements
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# AndStatementOutput

### Statements
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# AssociateWebACLRequest

### WebACLArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociationConfig

### RequestBody
- **Type**: typing.Optional[typing.Dict[typing.Literal['API_GATEWAY', 'APP_RUNNER_SERVICE', 'CLOUDFRONT', 'COGNITO_USER_POOL', 'VERIFIED_ACCESS_INSTANCE'], aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RequestBodyAssociatedResourceTypeConfig]]


# AssociationConfigOutput

### RequestBody
- **Type**: typing.Optional[typing.Dict[typing.Literal['API_GATEWAY', 'APP_RUNNER_SERVICE', 'CLOUDFRONT', 'COGNITO_USER_POOL', 'VERIFIED_ACCESS_INSTANCE'], aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RequestBodyAssociatedResourceTypeConfig]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockAction

### CustomResponse
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponse, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponseOutput, NoneType]


# BlockActionOutput

### CustomResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponseOutput]


# Body

### OversizeHandling
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']]


# ByteMatchStatement

### SearchString
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### FieldToMatch
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatch, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput]
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# ByteMatchStatementOutput

### SearchString
- **Type**: <class 'bytes'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# CaptchaAction

### CustomRequestHandling
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandling, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandlingOutput, NoneType]


# CaptchaActionOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandlingOutput]


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandling, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandlingOutput, NoneType]


# ChallengeActionOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandlingOutput]


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
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Rule, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleOutput]]
- **Required**: Yes


# CheckCapacityResponse

### Capacity
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# Condition

### ActionCondition
- **Type**: <class 'NoneType'>

### LabelNameCondition
- **Type**: <class 'NoneType'>


# CookieMatchPattern

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedCookies
- **Type**: typing.Optional[typing.List[str]]

### ExcludedCookies
- **Type**: typing.Optional[typing.List[str]]


# CookieMatchPatternOutput

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedCookies
- **Type**: typing.Optional[typing.List[str]]

### ExcludedCookies
- **Type**: typing.Optional[typing.List[str]]


# Cookies

### MatchPattern
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CookieMatchPattern, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CookieMatchPatternOutput]
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# CookiesOutput

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CookieMatchPatternOutput'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# CountAction

### CustomRequestHandling
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandling, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandlingOutput, NoneType]


# CountActionOutput

### CustomRequestHandling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomRequestHandlingOutput]


# CreateAPIKeyRequest

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### TokenDomains
- **Type**: typing.List[str]
- **Required**: Yes


# CreateAPIKeyResponse

### APIKey
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[str]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Tag]]


# CreateIPSetResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.IPSetSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegexPatternSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### RegularExpressionList
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Regex]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Tag]]


# CreateRegexPatternSetResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexPatternSetSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Rule, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Tag]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponseBody]]


# CreateRuleGroupResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleGroupSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWebACLRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: typing.Literal['CLOUDFRONT', 'REGIONAL']
- **Required**: Yes

### DefaultAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DefaultAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DefaultActionOutput]
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Rule, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleOutput]]]

### DataProtectionConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DataProtectionConfig, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DataProtectionConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Tag]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponseBody]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>

### TokenDomains
- **Type**: typing.Optional[typing.List[str]]

### AssociationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AssociationConfig, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AssociationConfigOutput, NoneType]


# CreateWebACLResponse

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.WebACLSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomHTTPHeader]
- **Required**: Yes


# CustomRequestHandlingOutput

### InsertHeaders
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomHTTPHeader]
- **Required**: Yes


# CustomResponse

### ResponseCode
- **Type**: <class 'int'>
- **Required**: Yes

### CustomResponseBodyKey
- **Type**: typing.Optional[str]

### ResponseHeaders
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomHTTPHeader]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomHTTPHeader]]


# DataProtection

### Field
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToProtect'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DataProtection]
- **Required**: Yes


# DataProtectionConfigOutput

### DataProtections
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DataProtectionOutput]
- **Required**: Yes


# DataProtectionOutput

### Field
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToProtectOutput'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.BlockAction]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AllowAction]


# DefaultActionOutput

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.BlockActionOutput]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AllowActionOutput]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedProductDescriptor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedProductDescriptor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleSummary]
- **Required**: Yes

### LabelNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### AvailableLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LabelSummary]
- **Required**: Yes

### ConsumedLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LabelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.JsonBody, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.JsonBodyOutput, NoneType]

### Headers
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Headers, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.HeadersOutput, NoneType]

### Cookies
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Cookies, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CookiesOutput, NoneType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.JsonBodyOutput]

### Headers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.HeadersOutput]

### Cookies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CookiesOutput]

### HeaderOrder
- **Type**: <class 'NoneType'>

### JA3Fingerprint
- **Type**: <class 'NoneType'>

### JA4Fingerprint
- **Type**: <class 'NoneType'>


# FieldToProtect

### FieldType
- **Type**: typing.Literal['BODY', 'QUERY_STRING', 'SINGLE_COOKIE', 'SINGLE_HEADER', 'SINGLE_QUERY_ARGUMENT']
- **Required**: Yes

### FieldKeys
- **Type**: typing.Optional[typing.List[str]]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Condition]
- **Required**: Yes


# FilterOutput

### Behavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes

### Requirement
- **Type**: typing.Literal['MEETS_ALL', 'MEETS_ANY']
- **Required**: Yes

### Conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Condition]
- **Required**: Yes


# FirewallManagerRuleGroup

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### FirewallManagerStatement
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FirewallManagerStatement'>
- **Required**: Yes

### OverrideAction
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.OverrideActionOutput'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes


# FirewallManagerStatement

### ManagedRuleGroupStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupStatementOutput]

### RuleGroupReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleGroupReferenceStatementOutput]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GeoMatchStatement

### CountryCodes
- **Type**: typing.Optional[typing.List[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'XK', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### ForwardedIPConfig
- **Type**: <class 'NoneType'>


# GeoMatchStatementOutput

### CountryCodes
- **Type**: typing.Optional[typing.List[typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'XK', 'YE', 'YT', 'ZA', 'ZM', 'ZW']]]

### ForwardedIPConfig
- **Type**: <class 'NoneType'>


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.IPSet'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleSet'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.MobileSdkRelease'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateBasedStatementManagedKeysIPSet'>
- **Required**: Yes

### ManagedKeysIPV6
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateBasedStatementManagedKeysIPSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexPatternSet'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleGroup'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TimeWindow, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TimeWindowOutput]
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes


# GetSampledRequestsResponse

### SampledRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.SampledHTTPRequest]
- **Required**: Yes

### PopulationSize
- **Type**: <class 'int'>
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TimeWindowOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# GetWebACLForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebACLForResourceResponse

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.WebACL'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.WebACL'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationIntegrationURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.HTTPHeader]]


# HeaderMatchPattern

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedHeaders
- **Type**: typing.Optional[typing.List[str]]

### ExcludedHeaders
- **Type**: typing.Optional[typing.List[str]]


# HeaderMatchPatternOutput

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedHeaders
- **Type**: typing.Optional[typing.List[str]]

### ExcludedHeaders
- **Type**: typing.Optional[typing.List[str]]


# HeaderOrder

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# Headers

### MatchPattern
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.HeaderMatchPattern, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.HeaderMatchPatternOutput]
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


# HeadersOutput

### MatchPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.HeaderMatchPatternOutput'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### OversizeHandling
- **Type**: typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']
- **Required**: Yes


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.JsonMatchPattern, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.JsonMatchPatternOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.JsonMatchPatternOutput'>
- **Required**: Yes

### MatchScope
- **Type**: typing.Literal['ALL', 'KEY', 'VALUE']
- **Required**: Yes

### InvalidFallbackBehavior
- **Type**: typing.Optional[typing.Literal['EVALUATE_AS_STRING', 'MATCH', 'NO_MATCH']]

### OversizeHandling
- **Type**: typing.Optional[typing.Literal['CONTINUE', 'MATCH', 'NO_MATCH']]


# JsonMatchPattern

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedPaths
- **Type**: typing.Optional[typing.List[str]]


# JsonMatchPatternOutput

### All
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IncludedPaths
- **Type**: typing.Optional[typing.List[str]]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.APIKeySummary]
- **Required**: Yes

### ApplicationIntegrationURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupVersion]
- **Required**: Yes

### CurrentDefaultVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.IPSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LoggingConfigurationOutput]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ReleaseSummary]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexPatternSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TagInfoForResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.WebACLSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingConfiguration

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.List[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatch]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput]]

### ManagedByFirewallManager
- **Type**: typing.Optional[bool]

### LoggingFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LoggingFilterOutput]

### LogType
- **Type**: typing.Optional[typing.Literal['WAF_LOGS']]

### LogScope
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SECURITY_LAKE']]


# LoggingFilter

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Filter]
- **Required**: Yes

### DefaultBehavior
- **Type**: typing.Literal['DROP', 'KEEP']
- **Required**: Yes


# LoggingFilterOutput

### Filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FilterOutput]
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AWSManagedRulesATPRuleSet, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AWSManagedRulesATPRuleSetOutput, NoneType]

### AWSManagedRulesACFPRuleSet
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AWSManagedRulesACFPRuleSet, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AWSManagedRulesACFPRuleSetOutput, NoneType]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AWSManagedRulesATPRuleSetOutput]

### AWSManagedRulesACFPRuleSet
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AWSManagedRulesACFPRuleSetOutput]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ExcludedRule]]

### ScopeDownStatement
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ManagedRuleGroupConfigs
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupConfig, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupConfigOutput]]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOverride, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOverrideOutput]]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ExcludedRule]]

### ScopeDownStatement
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ManagedRuleGroupConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupConfigOutput]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOverrideOutput]]


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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleSetVersion]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Tag]]


# NotStatement

### Statement
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# NotStatementOutput

### Statement
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# OrStatement

### Statements
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# OrStatementOutput

### Statements
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# OverrideAction

### Count
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CountAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CountActionOutput, NoneType]

### None_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# OverrideActionOutput

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CountActionOutput]

### None_
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LoggingConfiguration, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LoggingConfigurationOutput]
- **Required**: Yes


# PutLoggingConfigurationResponse

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VersionToPublish]]


# PutManagedRuleSetVersionsResponse

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ForwardedIPConfig
- **Type**: <class 'NoneType'>

### CustomKeys
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateBasedStatementCustomKey, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateBasedStatementCustomKeyOutput]]]


# RateBasedStatementCustomKey

### Header
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitHeader, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitHeaderOutput, NoneType]

### Cookie
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitCookie, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitCookieOutput, NoneType]

### QueryArgument
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitQueryArgument, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitQueryArgumentOutput, NoneType]

### QueryString
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitQueryString, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitQueryStringOutput, NoneType]

### HTTPMethod
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ForwardedIP
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IP
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### LabelNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitLabelNamespace]

### UriPath
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitUriPath, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitUriPathOutput, NoneType]

### JA3Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitJA3Fingerprint]

### JA4Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitJA4Fingerprint]


# RateBasedStatementCustomKeyOutput

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitHeaderOutput]

### Cookie
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitCookieOutput]

### QueryArgument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitQueryArgumentOutput]

### QueryString
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitQueryStringOutput]

### HTTPMethod
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ForwardedIP
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### IP
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### LabelNamespace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitLabelNamespace]

### UriPath
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitUriPathOutput]

### JA3Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitJA3Fingerprint]

### JA4Fingerprint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateLimitJA4Fingerprint]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateBasedStatementCustomKeyOutput]]


# RateLimitCookie

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitCookieOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitHeader

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitHeaderOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitQueryArgumentOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitQueryString

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitQueryStringOutput

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitUriPath

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RateLimitUriPathOutput

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# Regex

### RegexString
- **Type**: typing.Optional[str]


# RegexMatchStatement

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatch, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput]
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RegexMatchStatementOutput

### RegexString
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Regex]]


# RegexPatternSetReferenceStatement

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatch, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput]
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# RegexPatternSetReferenceStatementOutput

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.UsernameField'>
- **Required**: Yes

### PasswordField
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.PasswordField'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.PhoneNumberField]]

### AddressFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AddressField]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.PhoneNumberField]]

### AddressFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AddressField]]


# ResponseInspection

### StatusCode
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionStatusCode, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionStatusCodeOutput, NoneType]

### Header
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionHeader, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionHeaderOutput, NoneType]

### BodyContains
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionBodyContains, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionBodyContainsOutput, NoneType]

### Json
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionJson, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionJsonOutput, NoneType]


# ResponseInspectionBodyContains

### SuccessStrings
- **Type**: typing.List[str]
- **Required**: Yes

### FailureStrings
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseInspectionBodyContainsOutput

### SuccessStrings
- **Type**: typing.List[str]
- **Required**: Yes

### FailureStrings
- **Type**: typing.List[str]
- **Required**: Yes


# ResponseInspectionHeader

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.List[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.List[str]
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


# ResponseInspectionJson

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SuccessValues
- **Type**: typing.List[str]
- **Required**: Yes

### FailureValues
- **Type**: typing.List[str]
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


# ResponseInspectionOutput

### StatusCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionStatusCodeOutput]

### Header
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionHeaderOutput]

### BodyContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionBodyContainsOutput]

### Json
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseInspectionJsonOutput]


# ResponseInspectionStatusCode

### SuccessCodes
- **Type**: typing.List[int]
- **Required**: Yes

### FailureCodes
- **Type**: typing.List[int]
- **Required**: Yes


# ResponseInspectionStatusCodeOutput

### SuccessCodes
- **Type**: typing.List[int]
- **Required**: Yes

### FailureCodes
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


# Rule

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Statement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Statement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.StatementOutput]
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Action
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOutput, NoneType]

### OverrideAction
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.OverrideAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.OverrideActionOutput, NoneType]

### RuleLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Label]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>


# RuleAction

### Block
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.BlockAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.BlockActionOutput, NoneType]

### Allow
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AllowAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AllowActionOutput, NoneType]

### Count
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CountAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CountActionOutput, NoneType]

### Captcha
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CaptchaAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CaptchaActionOutput, NoneType]

### Challenge
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ChallengeAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ChallengeActionOutput, NoneType]


# RuleActionOutput

### Block
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.BlockActionOutput]

### Allow
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AllowActionOutput]

### Count
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CountActionOutput]

### Captcha
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CaptchaActionOutput]

### Challenge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ChallengeActionOutput]


# RuleActionOverride

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActionToUse
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOutput]
- **Required**: Yes


# RuleActionOverrideOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActionToUse
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOutput'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleOutput]]

### LabelNamespace
- **Type**: typing.Optional[str]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponseBody]]

### AvailableLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LabelSummary]]

### ConsumedLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.LabelSummary]]


# RuleGroupReferenceStatement

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ExcludedRule]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOverride, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOverrideOutput]]]


# RuleGroupReferenceStatementOutput

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ExcludedRule]]

### RuleActionOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOverrideOutput]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.StatementOutput'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOutput]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.OverrideActionOutput]

### RuleLabels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Label]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>


# RuleSummary

### Name
- **Type**: typing.Optional[str]

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleActionOutput]


# SampledHTTPRequest

### Request
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.HTTPRequest'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.HTTPHeader]]

### ResponseCodeSent
- **Type**: typing.Optional[int]

### Labels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Label]]

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatch, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput]
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# SizeConstraintStatementOutput

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# SqliMatchStatement

### FieldToMatch
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatch, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput]
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes

### SensitivityLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW']]


# SqliMatchStatementOutput

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes

### SensitivityLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW']]


# Statement

### ByteMatchStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ByteMatchStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ByteMatchStatementOutput, NoneType]

### SqliMatchStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.SqliMatchStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.SqliMatchStatementOutput, NoneType]

### XssMatchStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.XssMatchStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.XssMatchStatementOutput, NoneType]

### SizeConstraintStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.SizeConstraintStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.SizeConstraintStatementOutput, NoneType]

### GeoMatchStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.GeoMatchStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.GeoMatchStatementOutput, NoneType]

### RuleGroupReferenceStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleGroupReferenceStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleGroupReferenceStatementOutput, NoneType]

### IPSetReferenceStatement
- **Type**: <class 'NoneType'>

### RegexPatternSetReferenceStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexPatternSetReferenceStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexPatternSetReferenceStatementOutput, NoneType]

### RateBasedStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateBasedStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateBasedStatementOutput, NoneType]

### AndStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AndStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AndStatementOutput, NoneType]

### OrStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.OrStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.OrStatementOutput, NoneType]

### NotStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.NotStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.NotStatementOutput, NoneType]

### ManagedRuleGroupStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupStatementOutput, NoneType]

### LabelMatchStatement
- **Type**: <class 'NoneType'>

### RegexMatchStatement
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexMatchStatement, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexMatchStatementOutput, NoneType]


# StatementOutput

### ByteMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ByteMatchStatementOutput]

### SqliMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.SqliMatchStatementOutput]

### XssMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.XssMatchStatementOutput]

### SizeConstraintStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.SizeConstraintStatementOutput]

### GeoMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.GeoMatchStatementOutput]

### RuleGroupReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleGroupReferenceStatementOutput]

### IPSetReferenceStatement
- **Type**: <class 'NoneType'>

### RegexPatternSetReferenceStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexPatternSetReferenceStatementOutput]

### RateBasedStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RateBasedStatementOutput]

### AndStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AndStatementOutput]

### OrStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.OrStatementOutput]

### NotStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.NotStatementOutput]

### ManagedRuleGroupStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ManagedRuleGroupStatementOutput]

### LabelMatchStatement
- **Type**: <class 'NoneType'>

### RegexMatchStatement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RegexMatchStatementOutput]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Tag]]


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Tag]
- **Required**: Yes


# TextTransformation

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['BASE64_DECODE', 'BASE64_DECODE_EXT', 'CMD_LINE', 'COMPRESS_WHITE_SPACE', 'CSS_DECODE', 'ESCAPE_SEQ_DECODE', 'HEX_DECODE', 'HTML_ENTITY_DECODE', 'JS_DECODE', 'LOWERCASE', 'MD5', 'NONE', 'NORMALIZE_PATH', 'NORMALIZE_PATH_WIN', 'REMOVE_NULLS', 'REPLACE_COMMENTS', 'REPLACE_NULLS', 'SQL_HEX_DECODE', 'URL_DECODE', 'URL_DECODE_UNI', 'UTF8_TO_UNICODE']
- **Required**: Yes


# TimeWindow

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# TimeWindowOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
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
- **Type**: typing.List[str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.Union[datetime.datetime, str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Regex]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Rule, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleOutput]]]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponseBody]]


# UpdateRuleGroupResponse

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DefaultAction, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DefaultActionOutput]
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### LockToken
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.Rule, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleOutput]]]

### DataProtectionConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DataProtectionConfig, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DataProtectionConfigOutput, NoneType]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponseBody]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>

### TokenDomains
- **Type**: typing.Optional[typing.List[str]]

### AssociationConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AssociationConfig, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AssociationConfigOutput, NoneType]


# UpdateWebACLResponse

### NextLockToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DefaultActionOutput'>
- **Required**: Yes

### VisibilityConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.VisibilityConfig'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.RuleOutput]]

### DataProtectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.DataProtectionConfigOutput]

### Capacity
- **Type**: typing.Optional[int]

### PreProcessFirewallManagerRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FirewallManagerRuleGroup]]

### PostProcessFirewallManagerRuleGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FirewallManagerRuleGroup]]

### ManagedByFirewallManager
- **Type**: typing.Optional[bool]

### LabelNamespace
- **Type**: typing.Optional[str]

### CustomResponseBodies
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.CustomResponseBody]]

### CaptchaConfig
- **Type**: <class 'NoneType'>

### ChallengeConfig
- **Type**: <class 'NoneType'>

### TokenDomains
- **Type**: typing.Optional[typing.List[str]]

### AssociationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.AssociationConfigOutput]

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatch, aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput]
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes


# XssMatchStatementOutput

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.wafv2.wafv2_classes.FieldToMatchOutput'>
- **Required**: Yes

### TextTransformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.wafv2.wafv2_classes.TextTransformation]
- **Required**: Yes



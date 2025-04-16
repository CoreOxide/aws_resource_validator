# Waf Classes

# ActivatedRuleOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActivatedRuleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByteMatchSet

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ByteMatchTuples
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ByteMatchTupleOutput]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# ByteMatchSetSummary

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ByteMatchSetUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### ByteMatchTuple
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ByteMatchTupleUnion'>
- **Required**: Yes


# ByteMatchTuple

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatch'>
- **Required**: Yes

### TargetString
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.Blob'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# ByteMatchTupleOutput

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatch'>
- **Required**: Yes

### TargetString
- **Type**: <class 'bytes'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# ByteMatchTupleUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateByteMatchSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateByteMatchSetResponse

### ByteMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ByteMatchSet'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateGeoMatchSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGeoMatchSetResponse

### GeoMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.GeoMatchSet'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIPSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateIPSetResponse

### IPSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.IPSet'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRateBasedRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### RateKey
- **Type**: typing.Literal['IP']
- **Required**: Yes

### RateLimit
- **Type**: <class 'int'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.Tag]]


# CreateRateBasedRuleResponse

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RateBasedRule'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegexMatchSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRegexMatchSetResponse

### RegexMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexMatchSet'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRegexPatternSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRegexPatternSetResponse

### RegexPatternSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexPatternSet'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleGroupRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.Tag]]


# CreateRuleGroupResponse

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RuleGroup'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.Tag]]


# CreateRuleResponse

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.Rule'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSizeConstraintSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSizeConstraintSetResponse

### SizeConstraintSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SizeConstraintSet'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSqlInjectionMatchSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSqlInjectionMatchSetResponse

### SqlInjectionMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchSet'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWebACLMigrationStackRequest

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### IgnoreUnsupportedType
- **Type**: <class 'bool'>
- **Required**: Yes


# CreateWebACLMigrationStackResponse

### S3ObjectUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWebACLRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.WafAction'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.Tag]]


# CreateWebACLResponse

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.WebACL'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# CreateXssMatchSetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateXssMatchSetResponse

### XssMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.XssMatchSet'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteByteMatchSetRequest

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteByteMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGeoMatchSetRequest

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGeoMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIPSetRequest

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIPSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLoggingConfigurationRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionPolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRateBasedRuleRequest

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRateBasedRuleResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRegexMatchSetRequest

### RegexMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegexMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRegexPatternSetRequest

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegexPatternSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRuleGroupRequest

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleGroupResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRuleRequest

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSizeConstraintSetRequest

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSizeConstraintSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSqlInjectionMatchSetRequest

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSqlInjectionMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWebACLRequest

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebACLResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteXssMatchSetRequest

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteXssMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ExcludedRule

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# FieldToMatch

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GeoMatchConstraint

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GeoMatchSet

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### GeoMatchConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.GeoMatchConstraint]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# GeoMatchSetSummary

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GeoMatchSetUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### GeoMatchConstraint
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.GeoMatchConstraint'>
- **Required**: Yes


# GetByteMatchSetRequest

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetByteMatchSetResponse

### ByteMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ByteMatchSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetChangeTokenResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetChangeTokenStatusRequest

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetChangeTokenStatusResponse

### ChangeTokenStatus
- **Type**: typing.Literal['INSYNC', 'PENDING', 'PROVISIONED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetGeoMatchSetRequest

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGeoMatchSetResponse

### GeoMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.GeoMatchSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetIPSetRequest

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIPSetResponse

### IPSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.IPSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoggingConfigurationRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggingConfigurationResponse

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetRateBasedRuleManagedKeysRequest

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]


# GetRateBasedRuleManagedKeysRequestPaginate

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# GetRateBasedRuleManagedKeysResponse

### ManagedKeys
- **Type**: typing.List[str]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetRateBasedRuleRequest

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRateBasedRuleResponse

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RateBasedRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegexMatchSetRequest

### RegexMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRegexMatchSetResponse

### RegexMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexMatchSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegexPatternSetRequest

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRegexPatternSetResponse

### RegexPatternSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexPatternSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetRuleGroupRequest

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleGroupResponse

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RuleGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetRuleRequest

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleResponse

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.Rule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetSampledRequestsRequest

### WebAclId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TimeWindowUnion'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes


# GetSampledRequestsResponse

### SampledRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SampledHTTPRequest]
- **Required**: Yes

### PopulationSize
- **Type**: <class 'int'>
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TimeWindowOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetSizeConstraintSetRequest

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSizeConstraintSetResponse

### SizeConstraintSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SizeConstraintSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetSqlInjectionMatchSetRequest

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSqlInjectionMatchSetResponse

### SqlInjectionMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetWebACLRequest

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebACLResponse

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.WebACL'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# GetXssMatchSetRequest

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetXssMatchSetResponse

### XssMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.XssMatchSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.HTTPHeader]]


# IPSet

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IPSetDescriptors
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.IPSetDescriptor]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# IPSetDescriptor

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IPSetSummary

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# IPSetUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### IPSetDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.IPSetDescriptor'>
- **Required**: Yes


# ListActivatedRulesInRuleGroupRequest

### RuleGroupId
- **Type**: typing.Optional[str]

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListActivatedRulesInRuleGroupRequestPaginate

### RuleGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListActivatedRulesInRuleGroupResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ActivatedRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListByteMatchSetsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListByteMatchSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListByteMatchSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ByteMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ByteMatchSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListGeoMatchSetsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListGeoMatchSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListGeoMatchSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### GeoMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.GeoMatchSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListIPSetsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListIPSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListIPSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### IPSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.IPSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListLoggingConfigurationsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListLoggingConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListLoggingConfigurationsResponse

### LoggingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationOutput]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListRateBasedRulesRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRateBasedRulesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListRateBasedRulesResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListRegexMatchSetsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRegexMatchSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListRegexMatchSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RegexMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RegexMatchSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListRegexPatternSetsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRegexPatternSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListRegexPatternSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RegexPatternSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RegexPatternSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListRuleGroupsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRuleGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListRuleGroupsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RuleGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListRulesRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRulesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListRulesResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListSizeConstraintSetsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListSizeConstraintSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListSizeConstraintSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### SizeConstraintSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SizeConstraintSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListSqlInjectionMatchSetsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListSqlInjectionMatchSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListSqlInjectionMatchSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### SqlInjectionMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListSubscribedRuleGroupsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListSubscribedRuleGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListSubscribedRuleGroupsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SubscribedRuleGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TagInfoForResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListWebACLsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListWebACLsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListWebACLsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### WebACLs
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.WebACLSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# ListXssMatchSetsRequest

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListXssMatchSetsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfig]


# ListXssMatchSetsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### XssMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.XssMatchSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingConfiguration

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.FieldToMatch]]


# LoggingConfigurationOutput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.List[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.FieldToMatch]]


# LoggingConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Predicate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutLoggingConfigurationRequest

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationUnion'>
- **Required**: Yes


# PutLoggingConfigurationResponse

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# PutPermissionPolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# RateBasedRule

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### MatchPredicates
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.Predicate]
- **Required**: Yes

### RateKey
- **Type**: typing.Literal['IP']
- **Required**: Yes

### RateLimit
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]


# RegexMatchSet

### RegexMatchSetId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RegexMatchTuples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.RegexMatchTuple]]


# RegexMatchSetSummary

### RegexMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# RegexMatchSetUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### RegexMatchTuple
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexMatchTuple'>
- **Required**: Yes


# RegexMatchTuple

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatch'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes


# RegexPatternSet

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RegexPatternStrings
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# RegexPatternSetSummary

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# RegexPatternSetUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### RegexPatternString
- **Type**: <class 'str'>
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

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Predicates
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.Predicate]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]


# RuleGroup

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]


# RuleGroupSummary

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# RuleGroupUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### ActivatedRule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleUnion'>
- **Required**: Yes


# RuleSummary

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# RuleUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### Predicate
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.Predicate'>
- **Required**: Yes


# SampledHTTPRequest

### Request
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.HTTPRequest'>
- **Required**: Yes

### Weight
- **Type**: <class 'int'>
- **Required**: Yes

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Action
- **Type**: typing.Optional[str]

### RuleWithinRuleGroup
- **Type**: typing.Optional[str]


# SizeConstraint

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatch'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Literal['EQ', 'GE', 'GT', 'LE', 'LT', 'NE']
- **Required**: Yes

### Size
- **Type**: <class 'int'>
- **Required**: Yes


# SizeConstraintSet

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes

### SizeConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SizeConstraint]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# SizeConstraintSetSummary

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# SizeConstraintSetUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### SizeConstraint
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SizeConstraint'>
- **Required**: Yes


# SqlInjectionMatchSet

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### SqlInjectionMatchTuples
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchTuple]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# SqlInjectionMatchSetSummary

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# SqlInjectionMatchSetUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### SqlInjectionMatchTuple
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchTuple'>
- **Required**: Yes


# SqlInjectionMatchTuple

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatch'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes


# SubscribedRuleGroupSummary

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.Tag]]


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.Tag]
- **Required**: Yes


# TimeWindow

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.Timestamp'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.Timestamp'>
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


# UpdateByteMatchSetRequest

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.ByteMatchSetUpdate]
- **Required**: Yes


# UpdateByteMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGeoMatchSetRequest

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.GeoMatchSetUpdate]
- **Required**: Yes


# UpdateGeoMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIPSetRequest

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.IPSetUpdate]
- **Required**: Yes


# UpdateIPSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRateBasedRuleRequest

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RuleUpdate]
- **Required**: Yes

### RateLimit
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateRateBasedRuleResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRegexMatchSetRequest

### RegexMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RegexMatchSetUpdate]
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRegexMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRegexPatternSetRequest

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RegexPatternSetUpdate]
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRegexPatternSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRuleGroupRequest

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RuleGroupUpdate]
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRuleGroupResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRuleRequest

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RuleUpdate]
- **Required**: Yes


# UpdateRuleResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSizeConstraintSetRequest

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.SizeConstraintSetUpdate]
- **Required**: Yes


# UpdateSizeConstraintSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSqlInjectionMatchSetRequest

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchSetUpdate]
- **Required**: Yes


# UpdateSqlInjectionMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWebACLRequest

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.WebACLUpdate]]

### DefaultAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.WafAction]


# UpdateWebACLResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateXssMatchSetRequest

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.XssMatchSetUpdate]
- **Required**: Yes


# UpdateXssMatchSetResponse

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadata'>
- **Required**: Yes


# WafAction

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WebACL

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.WafAction'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleOutput]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### WebACLArn
- **Type**: typing.Optional[str]


# WebACLSummary

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# WebACLUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### ActivatedRule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleUnion'>
- **Required**: Yes


# XssMatchSet

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### XssMatchTuples
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.XssMatchTuple]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# XssMatchSetSummary

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# XssMatchSetUpdate

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### XssMatchTuple
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.XssMatchTuple'>
- **Required**: Yes


# XssMatchTuple

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatch'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes



# Waf Classes

# ActivatedRuleOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActivatedRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByteMatchSetSummaryTypeDef

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# ByteMatchSetTypeDef

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ByteMatchTuples
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ByteMatchTupleOutputTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# ByteMatchSetUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### ByteMatchTuple
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ByteMatchTupleUnionTypeDef'>
- **Required**: Yes


# ByteMatchTupleOutputTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef'>
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


# ByteMatchTupleTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef'>
- **Required**: Yes

### TargetString
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.BlobTypeDef'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# ByteMatchTupleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateByteMatchSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateByteMatchSetResponseTypeDef

### ByteMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ByteMatchSetTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGeoMatchSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGeoMatchSetResponseTypeDef

### GeoMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.GeoMatchSetTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIPSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateIPSetResponseTypeDef

### IPSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.IPSetTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRateBasedRuleRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.TagTypeDef]]


# CreateRateBasedRuleResponseTypeDef

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RateBasedRuleTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRegexMatchSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRegexMatchSetResponseTypeDef

### RegexMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexMatchSetTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRegexPatternSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateRegexPatternSetResponseTypeDef

### RegexPatternSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexPatternSetTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleGroupRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.TagTypeDef]]


# CreateRuleGroupResponseTypeDef

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RuleGroupTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRuleRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.TagTypeDef]]


# CreateRuleResponseTypeDef

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RuleTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSizeConstraintSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSizeConstraintSetResponseTypeDef

### SizeConstraintSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SizeConstraintSetTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSqlInjectionMatchSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSqlInjectionMatchSetResponseTypeDef

### SqlInjectionMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchSetTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWebACLMigrationStackRequestTypeDef

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### IgnoreUnsupportedType
- **Type**: <class 'bool'>
- **Required**: Yes


# CreateWebACLMigrationStackResponseTypeDef

### S3ObjectUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWebACLRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.WafActionTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.TagTypeDef]]


# CreateWebACLResponseTypeDef

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.WebACLTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateXssMatchSetRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateXssMatchSetResponseTypeDef

### XssMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.XssMatchSetTypeDef'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteByteMatchSetRequestTypeDef

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteByteMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGeoMatchSetRequestTypeDef

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGeoMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIPSetRequestTypeDef

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIPSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLoggingConfigurationRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionPolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRateBasedRuleRequestTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRateBasedRuleResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRegexMatchSetRequestTypeDef

### RegexMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegexMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRegexPatternSetRequestTypeDef

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRegexPatternSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRuleGroupRequestTypeDef

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleGroupResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRuleRequestTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRuleResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSizeConstraintSetRequestTypeDef

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSizeConstraintSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSqlInjectionMatchSetRequestTypeDef

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSqlInjectionMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWebACLRequestTypeDef

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebACLResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteXssMatchSetRequestTypeDef

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteXssMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExcludedRuleTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# FieldToMatchTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GeoMatchConstraintTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GeoMatchSetSummaryTypeDef

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GeoMatchSetTypeDef

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### GeoMatchConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.GeoMatchConstraintTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# GeoMatchSetUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### GeoMatchConstraint
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.GeoMatchConstraintTypeDef'>
- **Required**: Yes


# GetByteMatchSetRequestTypeDef

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetByteMatchSetResponseTypeDef

### ByteMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ByteMatchSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChangeTokenResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChangeTokenStatusRequestTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetChangeTokenStatusResponseTypeDef

### ChangeTokenStatus
- **Type**: typing.Literal['INSYNC', 'PENDING', 'PROVISIONED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGeoMatchSetRequestTypeDef

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGeoMatchSetResponseTypeDef

### GeoMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.GeoMatchSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIPSetRequestTypeDef

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIPSetResponseTypeDef

### IPSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.IPSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoggingConfigurationRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRateBasedRuleManagedKeysRequestPaginateTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# GetRateBasedRuleManagedKeysRequestTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### NextMarker
- **Type**: typing.Optional[str]


# GetRateBasedRuleManagedKeysResponseTypeDef

### ManagedKeys
- **Type**: typing.List[str]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRateBasedRuleRequestTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRateBasedRuleResponseTypeDef

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RateBasedRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegexMatchSetRequestTypeDef

### RegexMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRegexMatchSetResponseTypeDef

### RegexMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexMatchSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegexPatternSetRequestTypeDef

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRegexPatternSetResponseTypeDef

### RegexPatternSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexPatternSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRuleGroupRequestTypeDef

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleGroupResponseTypeDef

### RuleGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RuleGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRuleRequestTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRuleResponseTypeDef

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSampledRequestsRequestTypeDef

### WebAclId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TimeWindowUnionTypeDef'>
- **Required**: Yes

### MaxItems
- **Type**: <class 'int'>
- **Required**: Yes


# GetSampledRequestsResponseTypeDef

### SampledRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SampledHTTPRequestTypeDef]
- **Required**: Yes

### PopulationSize
- **Type**: <class 'int'>
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TimeWindowOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSizeConstraintSetRequestTypeDef

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSizeConstraintSetResponseTypeDef

### SizeConstraintSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SizeConstraintSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSqlInjectionMatchSetRequestTypeDef

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSqlInjectionMatchSetResponseTypeDef

### SqlInjectionMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWebACLRequestTypeDef

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWebACLResponseTypeDef

### WebACL
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.WebACLTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetXssMatchSetRequestTypeDef

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetXssMatchSetResponseTypeDef

### XssMatchSet
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.XssMatchSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.HTTPHeaderTypeDef]]


# IPSetDescriptorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IPSetSummaryTypeDef

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# IPSetTypeDef

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes

### IPSetDescriptors
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.IPSetDescriptorTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# IPSetUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### IPSetDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.IPSetDescriptorTypeDef'>
- **Required**: Yes


# ListActivatedRulesInRuleGroupRequestPaginateTypeDef

### RuleGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListActivatedRulesInRuleGroupRequestTypeDef

### RuleGroupId
- **Type**: typing.Optional[str]

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListActivatedRulesInRuleGroupResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ActivatedRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListByteMatchSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListByteMatchSetsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListByteMatchSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ByteMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ByteMatchSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGeoMatchSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListGeoMatchSetsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListGeoMatchSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### GeoMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.GeoMatchSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIPSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListIPSetsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListIPSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### IPSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.IPSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLoggingConfigurationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListLoggingConfigurationsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListLoggingConfigurationsResponseTypeDef

### LoggingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationOutputTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRateBasedRulesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRateBasedRulesRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRateBasedRulesResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRegexMatchSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRegexMatchSetsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRegexMatchSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RegexMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RegexMatchSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRegexPatternSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRegexPatternSetsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRegexPatternSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RegexPatternSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RegexPatternSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRuleGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRuleGroupsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRuleGroupsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RuleGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRulesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRulesRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListRulesResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.RuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSizeConstraintSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListSizeConstraintSetsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListSizeConstraintSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### SizeConstraintSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SizeConstraintSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSqlInjectionMatchSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListSqlInjectionMatchSetsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListSqlInjectionMatchSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### SqlInjectionMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubscribedRuleGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListSubscribedRuleGroupsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListSubscribedRuleGroupsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### RuleGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SubscribedRuleGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TagInfoForResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWebACLsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListWebACLsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListWebACLsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### WebACLs
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.WebACLSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListXssMatchSetsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListXssMatchSetsRequestTypeDef

### NextMarker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListXssMatchSetsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### XssMatchSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.XssMatchSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingConfigurationOutputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.List[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef]]


# LoggingConfigurationTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef]]


# LoggingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredicateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutLoggingConfigurationRequestTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationUnionTypeDef'>
- **Required**: Yes


# PutLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutPermissionPolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# RateBasedRuleTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### MatchPredicates
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.PredicateTypeDef]
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


# RegexMatchSetSummaryTypeDef

### RegexMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# RegexMatchSetTypeDef

### RegexMatchSetId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### RegexMatchTuples
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.RegexMatchTupleTypeDef]]


# RegexMatchSetUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### RegexMatchTuple
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.RegexMatchTupleTypeDef'>
- **Required**: Yes


# RegexMatchTupleTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes


# RegexPatternSetSummaryTypeDef

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# RegexPatternSetTypeDef

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RegexPatternStrings
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# RegexPatternSetUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### RegexPatternString
- **Type**: <class 'str'>
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


# RuleGroupSummaryTypeDef

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# RuleGroupTypeDef

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]


# RuleGroupUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### ActivatedRule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleUnionTypeDef'>
- **Required**: Yes


# RuleSummaryTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# RuleTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Predicates
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.PredicateTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]


# RuleUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### Predicate
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.PredicateTypeDef'>
- **Required**: Yes


# SampledHTTPRequestTypeDef

### Request
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.HTTPRequestTypeDef'>
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


# SizeConstraintSetSummaryTypeDef

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# SizeConstraintSetTypeDef

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes

### SizeConstraints
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SizeConstraintTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# SizeConstraintSetUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### SizeConstraint
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SizeConstraintTypeDef'>
- **Required**: Yes


# SizeConstraintTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef'>
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


# SqlInjectionMatchSetSummaryTypeDef

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# SqlInjectionMatchSetTypeDef

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### SqlInjectionMatchTuples
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchTupleTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# SqlInjectionMatchSetUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### SqlInjectionMatchTuple
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchTupleTypeDef'>
- **Required**: Yes


# SqlInjectionMatchTupleTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes


# SubscribedRuleGroupSummaryTypeDef

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes


# TagInfoForResourceTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### TagList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.TagTypeDef]]


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimeWindowOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TimeWindowTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TimestampTypeDef'>
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


# UpdateByteMatchSetRequestTypeDef

### ByteMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.ByteMatchSetUpdateTypeDef]
- **Required**: Yes


# UpdateByteMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGeoMatchSetRequestTypeDef

### GeoMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.GeoMatchSetUpdateTypeDef]
- **Required**: Yes


# UpdateGeoMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIPSetRequestTypeDef

### IPSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.IPSetUpdateTypeDef]
- **Required**: Yes


# UpdateIPSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRateBasedRuleRequestTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RuleUpdateTypeDef]
- **Required**: Yes

### RateLimit
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateRateBasedRuleResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRegexMatchSetRequestTypeDef

### RegexMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RegexMatchSetUpdateTypeDef]
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRegexMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRegexPatternSetRequestTypeDef

### RegexPatternSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RegexPatternSetUpdateTypeDef]
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRegexPatternSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRuleGroupRequestTypeDef

### RuleGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RuleGroupUpdateTypeDef]
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRuleGroupResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRuleRequestTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.RuleUpdateTypeDef]
- **Required**: Yes


# UpdateRuleResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSizeConstraintSetRequestTypeDef

### SizeConstraintSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.SizeConstraintSetUpdateTypeDef]
- **Required**: Yes


# UpdateSizeConstraintSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSqlInjectionMatchSetRequestTypeDef

### SqlInjectionMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.SqlInjectionMatchSetUpdateTypeDef]
- **Required**: Yes


# UpdateSqlInjectionMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWebACLRequestTypeDef

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.WebACLUpdateTypeDef]]

### DefaultAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.WafActionTypeDef]


# UpdateWebACLResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateXssMatchSetRequestTypeDef

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### Updates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.XssMatchSetUpdateTypeDef]
- **Required**: Yes


# UpdateXssMatchSetResponseTypeDef

### ChangeToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WafActionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WebACLSummaryTypeDef

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# WebACLTypeDef

### WebACLId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultAction
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.WafActionTypeDef'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleOutputTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### WebACLArn
- **Type**: typing.Optional[str]


# WebACLUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### ActivatedRule
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleUnionTypeDef'>
- **Required**: Yes


# XssMatchSetSummaryTypeDef

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# XssMatchSetTypeDef

### XssMatchSetId
- **Type**: <class 'str'>
- **Required**: Yes

### XssMatchTuples
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.XssMatchTupleTypeDef]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# XssMatchSetUpdateTypeDef

### Action
- **Type**: typing.Literal['DELETE', 'INSERT']
- **Required**: Yes

### XssMatchTuple
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.XssMatchTupleTypeDef'>
- **Required**: Yes


# XssMatchTupleTypeDef

### FieldToMatch
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef'>
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes



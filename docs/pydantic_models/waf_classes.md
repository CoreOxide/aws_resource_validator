# waf_classes

# ActivatedRuleExtraOutputTypeDef

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.WafActionTypeDef]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.WafOverrideActionTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['GROUP', 'RATE_BASED', 'REGULAR']]

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.ExcludedRuleTypeDef]]


# ActivatedRuleOutputTypeDef

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.WafActionTypeDef]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.WafOverrideActionTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['GROUP', 'RATE_BASED', 'REGULAR']]

### ExcludedRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.ExcludedRuleTypeDef]]


# ActivatedRuleTypeDef

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.WafActionTypeDef]

### OverrideAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.WafOverrideActionTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['GROUP', 'RATE_BASED', 'REGULAR']]

### ExcludedRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.waf_classes.ExcludedRuleTypeDef]]


# BaseValidatorModel

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
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ByteMatchTupleTypeDef'>
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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### TextTransformation
- **Type**: typing.Literal['CMD_LINE', 'COMPRESS_WHITE_SPACE', 'HTML_ENTITY_DECODE', 'LOWERCASE', 'NONE', 'URL_DECODE']
- **Required**: Yes

### PositionalConstraint
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_WORD', 'ENDS_WITH', 'EXACTLY', 'STARTS_WITH']
- **Required**: Yes


# CreateByteMatchSetRequestRequestTypeDef

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


# CreateGeoMatchSetRequestRequestTypeDef

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


# CreateIPSetRequestRequestTypeDef

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


# CreateRateBasedRuleRequestRequestTypeDef

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


# CreateRegexMatchSetRequestRequestTypeDef

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


# CreateRegexPatternSetRequestRequestTypeDef

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


# CreateRuleGroupRequestRequestTypeDef

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


# CreateRuleRequestRequestTypeDef

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


# CreateSizeConstraintSetRequestRequestTypeDef

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


# CreateSqlInjectionMatchSetRequestRequestTypeDef

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


# CreateWebACLMigrationStackRequestRequestTypeDef

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


# CreateWebACLRequestRequestTypeDef

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


# CreateXssMatchSetRequestRequestTypeDef

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


# DeleteByteMatchSetRequestRequestTypeDef

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


# DeleteGeoMatchSetRequestRequestTypeDef

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


# DeleteIPSetRequestRequestTypeDef

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


# DeleteLoggingConfigurationRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionPolicyRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRateBasedRuleRequestRequestTypeDef

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


# DeleteRegexMatchSetRequestRequestTypeDef

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


# DeleteRegexPatternSetRequestRequestTypeDef

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


# DeleteRuleGroupRequestRequestTypeDef

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


# DeleteRuleRequestRequestTypeDef

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


# DeleteSizeConstraintSetRequestRequestTypeDef

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


# DeleteSqlInjectionMatchSetRequestRequestTypeDef

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


# DeleteWebACLRequestRequestTypeDef

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


# DeleteXssMatchSetRequestRequestTypeDef

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

### Type
- **Type**: typing.Literal['ALL_QUERY_ARGS', 'BODY', 'HEADER', 'METHOD', 'QUERY_STRING', 'SINGLE_QUERY_ARG', 'URI']
- **Required**: Yes

### Data
- **Type**: typing.Optional[str]


# GeoMatchConstraintTypeDef

### Type
- **Type**: typing.Literal['Country']
- **Required**: Yes

### Value
- **Type**: typing.Literal['AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AX', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BQ', 'BR', 'BS', 'BT', 'BV', 'BW', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CG', 'CH', 'CI', 'CK', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK', 'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JE', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG', 'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'SS', 'ST', 'SV', 'SX', 'SY', 'SZ', 'TC', 'TD', 'TF', 'TG', 'TH', 'TJ', 'TK', 'TL', 'TM', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW']
- **Required**: Yes


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


# GetByteMatchSetRequestRequestTypeDef

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


# GetChangeTokenStatusRequestRequestTypeDef

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


# GetGeoMatchSetRequestRequestTypeDef

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


# GetIPSetRequestRequestTypeDef

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


# GetLoggingConfigurationRequestRequestTypeDef

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


# GetPermissionPolicyRequestRequestTypeDef

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


# GetRateBasedRuleManagedKeysRequestGetRateBasedRuleManagedKeysPaginateTypeDef

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# GetRateBasedRuleManagedKeysRequestRequestTypeDef

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


# GetRateBasedRuleRequestRequestTypeDef

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


# GetRegexMatchSetRequestRequestTypeDef

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


# GetRegexPatternSetRequestRequestTypeDef

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


# GetRuleGroupRequestRequestTypeDef

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


# GetRuleRequestRequestTypeDef

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


# GetSampledRequestsRequestRequestTypeDef

### WebAclId
- **Type**: <class 'str'>
- **Required**: Yes

### RuleId
- **Type**: <class 'str'>
- **Required**: Yes

### TimeWindow
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.TimeWindowTypeDef'>
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


# GetSizeConstraintSetRequestRequestTypeDef

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


# GetSqlInjectionMatchSetRequestRequestTypeDef

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


# GetWebACLRequestRequestTypeDef

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


# GetXssMatchSetRequestRequestTypeDef

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

### Type
- **Type**: typing.Literal['IPV4', 'IPV6']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


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


# ListActivatedRulesInRuleGroupRequestListActivatedRulesInRuleGroupPaginateTypeDef

### RuleGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListActivatedRulesInRuleGroupRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleExtraOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListByteMatchSetsRequestListByteMatchSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListByteMatchSetsRequestRequestTypeDef

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


# ListGeoMatchSetsRequestListGeoMatchSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListGeoMatchSetsRequestRequestTypeDef

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


# ListIPSetsRequestListIPSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListIPSetsRequestRequestTypeDef

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


# ListLoggingConfigurationsRequestListLoggingConfigurationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListLoggingConfigurationsRequestRequestTypeDef

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


# ListRateBasedRulesRequestListRateBasedRulesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRateBasedRulesRequestRequestTypeDef

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


# ListRegexMatchSetsRequestListRegexMatchSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRegexMatchSetsRequestRequestTypeDef

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


# ListRegexPatternSetsRequestListRegexPatternSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRegexPatternSetsRequestRequestTypeDef

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


# ListRuleGroupsRequestListRuleGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRuleGroupsRequestRequestTypeDef

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


# ListRulesRequestListRulesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListRulesRequestRequestTypeDef

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


# ListSizeConstraintSetsRequestListSizeConstraintSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListSizeConstraintSetsRequestRequestTypeDef

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


# ListSqlInjectionMatchSetsRequestListSqlInjectionMatchSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListSqlInjectionMatchSetsRequestRequestTypeDef

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


# ListSubscribedRuleGroupsRequestListSubscribedRuleGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListSubscribedRuleGroupsRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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


# ListWebACLsRequestListWebACLsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListWebACLsRequestRequestTypeDef

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


# ListXssMatchSetsRequestListXssMatchSetsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.waf_classes.PaginatorConfigTypeDef]


# ListXssMatchSetsRequestRequestTypeDef

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


# LoggingConfigurationExtraOutputTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogDestinationConfigs
- **Type**: typing.List[str]
- **Required**: Yes

### RedactedFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.waf_classes.FieldToMatchTypeDef]]


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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PredicateTypeDef

### Negated
- **Type**: <class 'bool'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ByteMatch', 'GeoMatch', 'IPMatch', 'RegexMatch', 'SizeConstraint', 'SqlInjectionMatch', 'XssMatch']
- **Required**: Yes

### DataId
- **Type**: <class 'str'>
- **Required**: Yes


# PutLoggingConfigurationRequestRequestTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes


# PutLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutPermissionPolicyRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleTypeDef'>
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


# TagResourceRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateByteMatchSetRequestRequestTypeDef

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


# UpdateGeoMatchSetRequestRequestTypeDef

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


# UpdateIPSetRequestRequestTypeDef

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


# UpdateRateBasedRuleRequestRequestTypeDef

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


# UpdateRegexMatchSetRequestRequestTypeDef

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


# UpdateRegexPatternSetRequestRequestTypeDef

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


# UpdateRuleGroupRequestRequestTypeDef

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


# UpdateRuleRequestRequestTypeDef

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


# UpdateSizeConstraintSetRequestRequestTypeDef

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


# UpdateSqlInjectionMatchSetRequestRequestTypeDef

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


# UpdateWebACLRequestRequestTypeDef

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


# UpdateXssMatchSetRequestRequestTypeDef

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

### Type
- **Type**: typing.Literal['ALLOW', 'BLOCK', 'COUNT']
- **Required**: Yes


# WafOverrideActionTypeDef

### Type
- **Type**: typing.Literal['COUNT', 'NONE']
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.waf_classes.ActivatedRuleTypeDef'>
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



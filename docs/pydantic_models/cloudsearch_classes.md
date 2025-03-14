# Cloudsearch Classes

# AccessPoliciesStatusTypeDef

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# AnalysisOptionsTypeDef

### Synonyms
- **Type**: typing.Optional[str]

### Stopwords
- **Type**: typing.Optional[str]

### StemmingDictionary
- **Type**: typing.Optional[str]

### JapaneseTokenizationDictionary
- **Type**: typing.Optional[str]

### AlgorithmicStemming
- **Type**: typing.Optional[typing.Literal['full', 'light', 'minimal', 'none']]


# AnalysisSchemeStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.AnalysisSchemeTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# AnalysisSchemeTypeDef

### AnalysisSchemeName
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisSchemeLanguage
- **Type**: typing.Literal['ar', 'bg', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'eu', 'fa', 'fi', 'fr', 'ga', 'gl', 'he', 'hi', 'hu', 'hy', 'id', 'it', 'ja', 'ko', 'lv', 'mul', 'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'th', 'tr', 'zh-Hans', 'zh-Hant']
- **Required**: Yes

### AnalysisOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.AnalysisOptionsTypeDef]


# AvailabilityOptionsStatusTypeDef

### Options
- **Type**: <class 'bool'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BuildSuggestersRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# BuildSuggestersResponseTypeDef

### FieldNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDomainResponseTypeDef

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.DomainStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DateArrayOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### SourceFields
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]


# DateOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### SourceField
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]

### SortEnabled
- **Type**: typing.Optional[bool]


# DefineAnalysisSchemeRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.AnalysisSchemeTypeDef'>
- **Required**: Yes


# DefineAnalysisSchemeResponseTypeDef

### AnalysisScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.AnalysisSchemeStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefineExpressionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ExpressionTypeDef'>
- **Required**: Yes


# DefineExpressionResponseTypeDef

### Expression
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ExpressionStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefineIndexFieldRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexField
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.IndexFieldTypeDef'>
- **Required**: Yes


# DefineIndexFieldResponseTypeDef

### IndexField
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.IndexFieldStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefineSuggesterRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Suggester
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.SuggesterTypeDef'>
- **Required**: Yes


# DefineSuggesterResponseTypeDef

### Suggester
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.SuggesterStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAnalysisSchemeRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisSchemeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAnalysisSchemeResponseTypeDef

### AnalysisScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.AnalysisSchemeStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResponseTypeDef

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.DomainStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteExpressionRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExpressionResponseTypeDef

### Expression
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ExpressionStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteIndexFieldRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexFieldName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexFieldResponseTypeDef

### IndexField
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.IndexFieldStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSuggesterRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SuggesterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSuggesterResponseTypeDef

### Suggester
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.SuggesterStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnalysisSchemesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisSchemeNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Deployed
- **Type**: typing.Optional[bool]


# DescribeAnalysisSchemesResponseTypeDef

### AnalysisSchemes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch_classes.AnalysisSchemeStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAvailabilityOptionsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Deployed
- **Type**: typing.Optional[bool]


# DescribeAvailabilityOptionsResponseTypeDef

### AvailabilityOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.AvailabilityOptionsStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainEndpointOptionsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Deployed
- **Type**: typing.Optional[bool]


# DescribeDomainEndpointOptionsResponseTypeDef

### DomainEndpointOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.DomainEndpointOptionsStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainsRequestTypeDef

### DomainNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeDomainsResponseTypeDef

### DomainStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch_classes.DomainStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExpressionsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Deployed
- **Type**: typing.Optional[bool]


# DescribeExpressionsResponseTypeDef

### Expressions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch_classes.ExpressionStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIndexFieldsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### FieldNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Deployed
- **Type**: typing.Optional[bool]


# DescribeIndexFieldsResponseTypeDef

### IndexFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch_classes.IndexFieldStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeScalingParametersRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScalingParametersResponseTypeDef

### ScalingParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ScalingParametersStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceAccessPoliciesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Deployed
- **Type**: typing.Optional[bool]


# DescribeServiceAccessPoliciesResponseTypeDef

### AccessPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.AccessPoliciesStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSuggestersRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SuggesterNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Deployed
- **Type**: typing.Optional[bool]


# DescribeSuggestersResponseTypeDef

### Suggesters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch_classes.SuggesterStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentSuggesterOptionsTypeDef

### SourceField
- **Type**: <class 'str'>
- **Required**: Yes

### FuzzyMatching
- **Type**: typing.Optional[typing.Literal['high', 'low', 'none']]

### SortExpression
- **Type**: typing.Optional[str]


# DomainEndpointOptionsStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.DomainEndpointOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# DomainEndpointOptionsTypeDef

### EnforceHTTPS
- **Type**: typing.Optional[bool]

### TLSSecurityPolicy
- **Type**: typing.Optional[typing.Literal['Policy-Min-TLS-1-0-2019-07', 'Policy-Min-TLS-1-2-2019-07']]


# DomainStatusTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### RequiresIndexDocuments
- **Type**: <class 'bool'>
- **Required**: Yes

### ARN
- **Type**: typing.Optional[str]

### Created
- **Type**: typing.Optional[bool]

### Deleted
- **Type**: typing.Optional[bool]

### DocService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.ServiceEndpointTypeDef]

### SearchService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.ServiceEndpointTypeDef]

### Processing
- **Type**: typing.Optional[bool]

### SearchInstanceType
- **Type**: typing.Optional[str]

### SearchPartitionCount
- **Type**: typing.Optional[int]

### SearchInstanceCount
- **Type**: typing.Optional[int]

### Limits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.LimitsTypeDef]


# DoubleArrayOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[float]

### SourceFields
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]


# DoubleOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[float]

### SourceField
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]

### SortEnabled
- **Type**: typing.Optional[bool]


# ExpressionStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ExpressionTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# ExpressionTypeDef

### ExpressionName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionValue
- **Type**: <class 'str'>
- **Required**: Yes


# IndexDocumentsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# IndexDocumentsResponseTypeDef

### FieldNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IndexFieldStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.IndexFieldTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# IndexFieldTypeDef

### IndexFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexFieldType
- **Type**: typing.Literal['date', 'date-array', 'double', 'double-array', 'int', 'int-array', 'latlon', 'literal', 'literal-array', 'text', 'text-array']
- **Required**: Yes

### IntOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.IntOptionsTypeDef]

### DoubleOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.DoubleOptionsTypeDef]

### LiteralOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.LiteralOptionsTypeDef]

### TextOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.TextOptionsTypeDef]

### DateOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.DateOptionsTypeDef]

### LatLonOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.LatLonOptionsTypeDef]

### IntArrayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.IntArrayOptionsTypeDef]

### DoubleArrayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.DoubleArrayOptionsTypeDef]

### LiteralArrayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.LiteralArrayOptionsTypeDef]

### TextArrayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.TextArrayOptionsTypeDef]

### DateArrayOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch_classes.DateArrayOptionsTypeDef]


# IntArrayOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[int]

### SourceFields
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]


# IntOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[int]

### SourceField
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]

### SortEnabled
- **Type**: typing.Optional[bool]


# LatLonOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### SourceField
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]

### SortEnabled
- **Type**: typing.Optional[bool]


# LimitsTypeDef

### MaximumReplicationCount
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumPartitionCount
- **Type**: <class 'int'>
- **Required**: Yes


# ListDomainNamesResponseTypeDef

### DomainNames
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LiteralArrayOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### SourceFields
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]


# LiteralOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### SourceField
- **Type**: typing.Optional[str]

### FacetEnabled
- **Type**: typing.Optional[bool]

### SearchEnabled
- **Type**: typing.Optional[bool]

### ReturnEnabled
- **Type**: typing.Optional[bool]

### SortEnabled
- **Type**: typing.Optional[bool]


# OptionStatusTypeDef

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### State
- **Type**: typing.Literal['Active', 'FailedToValidate', 'Processing', 'RequiresIndexDocuments']
- **Required**: Yes

### UpdateVersion
- **Type**: typing.Optional[int]

### PendingDeletion
- **Type**: typing.Optional[bool]


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


# ScalingParametersStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ScalingParametersTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# ScalingParametersTypeDef

### DesiredInstanceType
- **Type**: typing.Optional[typing.Literal['search.2xlarge', 'search.large', 'search.m1.large', 'search.m1.small', 'search.m2.2xlarge', 'search.m2.xlarge', 'search.m3.2xlarge', 'search.m3.large', 'search.m3.medium', 'search.m3.xlarge', 'search.medium', 'search.previousgeneration.2xlarge', 'search.previousgeneration.large', 'search.previousgeneration.small', 'search.previousgeneration.xlarge', 'search.small', 'search.xlarge']]

### DesiredReplicationCount
- **Type**: typing.Optional[int]

### DesiredPartitionCount
- **Type**: typing.Optional[int]


# ServiceEndpointTypeDef

### Endpoint
- **Type**: typing.Optional[str]


# SuggesterStatusTypeDef

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.SuggesterTypeDef'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.OptionStatusTypeDef'>
- **Required**: Yes


# SuggesterTypeDef

### SuggesterName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentSuggesterOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.DocumentSuggesterOptionsTypeDef'>
- **Required**: Yes


# TextArrayOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### SourceFields
- **Type**: typing.Optional[str]

### ReturnEnabled
- **Type**: typing.Optional[bool]

### HighlightEnabled
- **Type**: typing.Optional[bool]

### AnalysisScheme
- **Type**: typing.Optional[str]


# TextOptionsTypeDef

### DefaultValue
- **Type**: typing.Optional[str]

### SourceField
- **Type**: typing.Optional[str]

### ReturnEnabled
- **Type**: typing.Optional[bool]

### SortEnabled
- **Type**: typing.Optional[bool]

### HighlightEnabled
- **Type**: typing.Optional[bool]

### AnalysisScheme
- **Type**: typing.Optional[str]


# UpdateAvailabilityOptionsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiAZ
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateAvailabilityOptionsResponseTypeDef

### AvailabilityOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.AvailabilityOptionsStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDomainEndpointOptionsRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainEndpointOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.DomainEndpointOptionsTypeDef'>
- **Required**: Yes


# UpdateDomainEndpointOptionsResponseTypeDef

### DomainEndpointOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.DomainEndpointOptionsStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScalingParametersRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ScalingParametersTypeDef'>
- **Required**: Yes


# UpdateScalingParametersResponseTypeDef

### ScalingParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ScalingParametersStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateServiceAccessPoliciesRequestTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessPolicies
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceAccessPoliciesResponseTypeDef

### AccessPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.AccessPoliciesStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



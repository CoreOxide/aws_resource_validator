# Cloudsearch Classes

# AccessPoliciesStatus

### Options
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.OptionStatus'>
- **Required**: Yes


# AnalysisOptions

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


# AnalysisScheme

### AnalysisSchemeName
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisSchemeLanguage
- **Type**: typing.Literal['ar', 'bg', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'eu', 'fa', 'fi', 'fr', 'ga', 'gl', 'he', 'hi', 'hu', 'hy', 'id', 'it', 'ja', 'ko', 'lv', 'mul', 'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'th', 'tr', 'zh-Hans', 'zh-Hant']
- **Required**: Yes

### AnalysisOptions
- **Type**: <class 'NoneType'>


# AnalysisSchemeStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AnalysisScheme'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.OptionStatus'>
- **Required**: Yes


# AvailabilityOptionsStatus

### Options
- **Type**: <class 'bool'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.OptionStatus'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BuildSuggestersRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# BuildSuggestersResponse

### FieldNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDomainResponse

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.DomainStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DateArrayOptions

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


# DateOptions

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


# DefineAnalysisSchemeRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AnalysisScheme'>
- **Required**: Yes


# DefineAnalysisSchemeResponse

### AnalysisScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AnalysisSchemeStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DefineExpressionRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Expression
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.Expression'>
- **Required**: Yes


# DefineExpressionResponse

### Expression
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ExpressionStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DefineIndexFieldRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexField
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.IndexField'>
- **Required**: Yes


# DefineIndexFieldResponse

### IndexField
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.IndexFieldStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DefineSuggesterRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Suggester
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.Suggester'>
- **Required**: Yes


# DefineSuggesterResponse

### Suggester
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.SuggesterStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAnalysisSchemeRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisSchemeName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAnalysisSchemeResponse

### AnalysisScheme
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AnalysisSchemeStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDomainResponse

### DomainStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.DomainStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteExpressionRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExpressionResponse

### Expression
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ExpressionStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteIndexFieldRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexFieldName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexFieldResponse

### IndexField
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.IndexFieldStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSuggesterRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SuggesterName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSuggesterResponse

### Suggester
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.SuggesterStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAnalysisSchemesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisSchemeNames
- **Type**: typing.Optional[typing.List[str]]

### Deployed
- **Type**: typing.Optional[bool]


# DescribeAnalysisSchemesResponse

### AnalysisSchemes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AnalysisSchemeStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAvailabilityOptionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Deployed
- **Type**: typing.Optional[bool]


# DescribeAvailabilityOptionsResponse

### AvailabilityOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AvailabilityOptionsStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainEndpointOptionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Deployed
- **Type**: typing.Optional[bool]


# DescribeDomainEndpointOptionsResponse

### DomainEndpointOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.DomainEndpointOptionsStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainsRequest

### DomainNames
- **Type**: typing.Optional[typing.List[str]]


# DescribeDomainsResponse

### DomainStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.DomainStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExpressionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionNames
- **Type**: typing.Optional[typing.List[str]]

### Deployed
- **Type**: typing.Optional[bool]


# DescribeExpressionsResponse

### Expressions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ExpressionStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIndexFieldsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### FieldNames
- **Type**: typing.Optional[typing.List[str]]

### Deployed
- **Type**: typing.Optional[bool]


# DescribeIndexFieldsResponse

### IndexFields
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.IndexFieldStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeScalingParametersRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScalingParametersResponse

### ScalingParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ScalingParametersStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeServiceAccessPoliciesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### Deployed
- **Type**: typing.Optional[bool]


# DescribeServiceAccessPoliciesResponse

### AccessPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AccessPoliciesStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSuggestersRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### SuggesterNames
- **Type**: typing.Optional[typing.List[str]]

### Deployed
- **Type**: typing.Optional[bool]


# DescribeSuggestersResponse

### Suggesters
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.SuggesterStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# DocumentSuggesterOptions

### SourceField
- **Type**: <class 'str'>
- **Required**: Yes

### FuzzyMatching
- **Type**: typing.Optional[typing.Literal['high', 'low', 'none']]

### SortExpression
- **Type**: typing.Optional[str]


# DomainEndpointOptions

### EnforceHTTPS
- **Type**: typing.Optional[bool]

### TLSSecurityPolicy
- **Type**: typing.Optional[typing.Literal['Policy-Min-TLS-1-0-2019-07', 'Policy-Min-TLS-1-2-2019-07']]


# DomainEndpointOptionsStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.DomainEndpointOptions'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.OptionStatus'>
- **Required**: Yes


# DomainStatus

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ServiceEndpoint]

### SearchService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ServiceEndpoint]

### Processing
- **Type**: typing.Optional[bool]

### SearchInstanceType
- **Type**: typing.Optional[str]

### SearchPartitionCount
- **Type**: typing.Optional[int]

### SearchInstanceCount
- **Type**: typing.Optional[int]

### Limits
- **Type**: <class 'NoneType'>


# DoubleArrayOptions

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


# DoubleOptions

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


# Expression

### ExpressionName
- **Type**: <class 'str'>
- **Required**: Yes

### ExpressionValue
- **Type**: <class 'str'>
- **Required**: Yes


# ExpressionStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.Expression'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.OptionStatus'>
- **Required**: Yes


# IndexDocumentsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# IndexDocumentsResponse

### FieldNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# IndexField

### IndexFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexFieldType
- **Type**: typing.Literal['date', 'date-array', 'double', 'double-array', 'int', 'int-array', 'latlon', 'literal', 'literal-array', 'text', 'text-array']
- **Required**: Yes

### IntOptions
- **Type**: <class 'NoneType'>

### DoubleOptions
- **Type**: <class 'NoneType'>

### LiteralOptions
- **Type**: <class 'NoneType'>

### TextOptions
- **Type**: <class 'NoneType'>

### DateOptions
- **Type**: <class 'NoneType'>

### LatLonOptions
- **Type**: <class 'NoneType'>

### IntArrayOptions
- **Type**: <class 'NoneType'>

### DoubleArrayOptions
- **Type**: <class 'NoneType'>

### LiteralArrayOptions
- **Type**: <class 'NoneType'>

### TextArrayOptions
- **Type**: <class 'NoneType'>

### DateArrayOptions
- **Type**: <class 'NoneType'>


# IndexFieldStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.IndexField'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.OptionStatus'>
- **Required**: Yes


# IntArrayOptions

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


# IntOptions

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


# LatLonOptions

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


# Limits

### MaximumReplicationCount
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumPartitionCount
- **Type**: <class 'int'>
- **Required**: Yes


# ListDomainNamesResponse

### DomainNames
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# LiteralArrayOptions

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


# LiteralOptions

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


# OptionStatus

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


# ScalingParameters

### DesiredInstanceType
- **Type**: typing.Optional[typing.Literal['search.2xlarge', 'search.large', 'search.m1.large', 'search.m1.small', 'search.m2.2xlarge', 'search.m2.xlarge', 'search.m3.2xlarge', 'search.m3.large', 'search.m3.medium', 'search.m3.xlarge', 'search.medium', 'search.previousgeneration.2xlarge', 'search.previousgeneration.large', 'search.previousgeneration.small', 'search.previousgeneration.xlarge', 'search.small', 'search.xlarge']]

### DesiredReplicationCount
- **Type**: typing.Optional[int]

### DesiredPartitionCount
- **Type**: typing.Optional[int]


# ScalingParametersStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ScalingParameters'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.OptionStatus'>
- **Required**: Yes


# ServiceEndpoint

### Endpoint
- **Type**: typing.Optional[str]


# Suggester

### SuggesterName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentSuggesterOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.DocumentSuggesterOptions'>
- **Required**: Yes


# SuggesterStatus

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.Suggester'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.OptionStatus'>
- **Required**: Yes


# TextArrayOptions

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


# TextOptions

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


# UpdateAvailabilityOptionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiAZ
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateAvailabilityOptionsResponse

### AvailabilityOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AvailabilityOptionsStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDomainEndpointOptionsRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DomainEndpointOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.DomainEndpointOptions'>
- **Required**: Yes


# UpdateDomainEndpointOptionsResponse

### DomainEndpointOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.DomainEndpointOptionsStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScalingParametersRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ScalingParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ScalingParameters'>
- **Required**: Yes


# UpdateScalingParametersResponse

### ScalingParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ScalingParametersStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateServiceAccessPoliciesRequest

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessPolicies
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateServiceAccessPoliciesResponse

### AccessPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.AccessPoliciesStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearch.cloudsearch_classes.ResponseMetadata'>
- **Required**: Yes



# Pydantic Models in cloudsearchdomain_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BucketInfoTypeDef

### buckets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudsearchdomain_classes.BucketTypeDef]]


# BucketTypeDef

### value
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]


# DocumentServiceWarningTypeDef

### message
- **Type**: typing.Optional[str]


# FieldStatsTypeDef

### min
- **Type**: typing.Optional[str]

### max
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### missing
- **Type**: typing.Optional[int]

### sum
- **Type**: typing.Optional[float]

### sumOfSquares
- **Type**: typing.Optional[float]

### mean
- **Type**: typing.Optional[str]

### stddev
- **Type**: typing.Optional[float]


# HitTypeDef

### id
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### exprs
- **Type**: typing.Optional[typing.Dict[str, str]]

### highlights
- **Type**: typing.Optional[typing.Dict[str, str]]


# HitsTypeDef

### found
- **Type**: typing.Optional[int]

### start
- **Type**: typing.Optional[int]

### cursor
- **Type**: typing.Optional[str]

### hit
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudsearchdomain_classes.HitTypeDef]]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# SearchRequestRequestTypeDef

### query
- **Type**: <class 'str'>
- **Required**: Yes

### cursor
- **Type**: typing.Optional[str]

### expr
- **Type**: typing.Optional[str]

### facet
- **Type**: typing.Optional[str]

### filterQuery
- **Type**: typing.Optional[str]

### highlight
- **Type**: typing.Optional[str]

### partial
- **Type**: typing.Optional[bool]

### queryOptions
- **Type**: typing.Optional[str]

### queryParser
- **Type**: typing.Optional[typing.Literal['dismax', 'lucene', 'simple', 'structured']]

### returnFields
- **Type**: typing.Optional[str]

### size
- **Type**: typing.Optional[int]

### sort
- **Type**: typing.Optional[str]

### start
- **Type**: typing.Optional[int]

### stats
- **Type**: typing.Optional[str]


# SearchResponseTypeDef

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain_classes.SearchStatusTypeDef'>
- **Required**: Yes

### hits
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain_classes.HitsTypeDef'>
- **Required**: Yes

### facets
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.cloudsearchdomain_classes.BucketInfoTypeDef]
- **Required**: Yes

### stats
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.cloudsearchdomain_classes.FieldStatsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchStatusTypeDef

### timems
- **Type**: typing.Optional[int]

### rid
- **Type**: typing.Optional[str]


# SuggestModelTypeDef

### query
- **Type**: typing.Optional[str]

### found
- **Type**: typing.Optional[int]

### suggestions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudsearchdomain_classes.SuggestionMatchTypeDef]]


# SuggestRequestRequestTypeDef

### query
- **Type**: <class 'str'>
- **Required**: Yes

### suggester
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: typing.Optional[int]


# SuggestResponseTypeDef

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain_classes.SuggestStatusTypeDef'>
- **Required**: Yes

### suggest
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain_classes.SuggestModelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SuggestStatusTypeDef

### timems
- **Type**: typing.Optional[int]

### rid
- **Type**: typing.Optional[str]


# SuggestionMatchTypeDef

### suggestion
- **Type**: typing.Optional[str]

### score
- **Type**: typing.Optional[int]

### id
- **Type**: typing.Optional[str]


# UploadDocumentsRequestRequestTypeDef

### documents
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### contentType
- **Type**: typing.Literal['application/json', 'application/xml']
- **Required**: Yes


# UploadDocumentsResponseTypeDef

### status
- **Type**: <class 'str'>
- **Required**: Yes

### adds
- **Type**: <class 'int'>
- **Required**: Yes

### deletes
- **Type**: <class 'int'>
- **Required**: Yes

### warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearchdomain_classes.DocumentServiceWarningTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



# Cloudsearchdomain Cloudsearchdomain Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Bucket

### value
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]


# BucketInfo

### buckets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.Bucket]]


# DocumentServiceWarning

### message
- **Type**: typing.Optional[str]


# FieldStats

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


# Hit

### id
- **Type**: typing.Optional[str]

### fields
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]

### exprs
- **Type**: typing.Optional[typing.Dict[str, str]]

### highlights
- **Type**: typing.Optional[typing.Dict[str, str]]


# Hits

### found
- **Type**: typing.Optional[int]

### start
- **Type**: typing.Optional[int]

### cursor
- **Type**: typing.Optional[str]

### hit
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.Hit]]


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


# SearchRequest

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


# SearchResponse

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.SearchStatus'>
- **Required**: Yes

### hits
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.Hits'>
- **Required**: Yes

### facets
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.BucketInfo]
- **Required**: Yes

### stats
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.FieldStats]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.ResponseMetadata'>
- **Required**: Yes


# SearchStatus

### timems
- **Type**: typing.Optional[int]

### rid
- **Type**: typing.Optional[str]


# SuggestModel

### query
- **Type**: typing.Optional[str]

### found
- **Type**: typing.Optional[int]

### suggestions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.SuggestionMatch]]


# SuggestRequest

### query
- **Type**: <class 'str'>
- **Required**: Yes

### suggester
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: typing.Optional[int]


# SuggestResponse

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.SuggestStatus'>
- **Required**: Yes

### suggest
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.SuggestModel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.ResponseMetadata'>
- **Required**: Yes


# SuggestStatus

### timems
- **Type**: typing.Optional[int]

### rid
- **Type**: typing.Optional[str]


# SuggestionMatch

### suggestion
- **Type**: typing.Optional[str]

### score
- **Type**: typing.Optional[int]

### id
- **Type**: typing.Optional[str]


# UploadDocumentsRequest

### documents
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### contentType
- **Type**: typing.Literal['application/json', 'application/xml']
- **Required**: Yes


# UploadDocumentsResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.DocumentServiceWarning]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain.cloudsearchdomain_classes.ResponseMetadata'>
- **Required**: Yes



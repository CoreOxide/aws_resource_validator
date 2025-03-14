# Cloudsearchdomain Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HitTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SearchRequestTypeDef

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


# SuggestRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UploadDocumentsRequestTypeDef

### documents
- **Type**: <class 'aws_resource_validator.pydantic_models.cloudsearchdomain_classes.BlobTypeDef'>
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



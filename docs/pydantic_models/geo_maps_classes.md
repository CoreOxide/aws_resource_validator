# Geo Maps Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetGlyphsRequest

### FontStack
- **Type**: <class 'str'>
- **Required**: Yes

### FontUnicodeRange
- **Type**: <class 'str'>
- **Required**: Yes


# GetGlyphsResponse

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_maps.geo_maps_classes.ResponseMetadata'>
- **Required**: Yes


# GetSpritesRequest

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### Style
- **Type**: typing.Literal['Hybrid', 'Monochrome', 'Satellite', 'Standard']
- **Required**: Yes

### ColorScheme
- **Type**: typing.Literal['Dark', 'Light']
- **Required**: Yes

### Variant
- **Type**: typing.Literal['Default']
- **Required**: Yes


# GetSpritesResponse

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_maps.geo_maps_classes.ResponseMetadata'>
- **Required**: Yes


# GetStaticMapRequest

### Height
- **Type**: <class 'int'>
- **Required**: Yes

### FileName
- **Type**: <class 'str'>
- **Required**: Yes

### Width
- **Type**: <class 'int'>
- **Required**: Yes

### BoundingBox
- **Type**: typing.Optional[str]

### BoundedPositions
- **Type**: typing.Optional[str]

### Center
- **Type**: typing.Optional[str]

### CompactOverlay
- **Type**: typing.Optional[str]

### GeoJsonOverlay
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### Padding
- **Type**: typing.Optional[int]

### Radius
- **Type**: typing.Optional[int]

### ScaleBarUnit
- **Type**: typing.Optional[typing.Literal['Kilometers', 'KilometersMiles', 'Miles', 'MilesKilometers']]

### Style
- **Type**: typing.Optional[typing.Literal['Satellite']]

### Zoom
- **Type**: typing.Optional[float]


# GetStaticMapResponse

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_maps.geo_maps_classes.ResponseMetadata'>
- **Required**: Yes


# GetStyleDescriptorRequest

### Style
- **Type**: typing.Literal['Hybrid', 'Monochrome', 'Satellite', 'Standard']
- **Required**: Yes

### ColorScheme
- **Type**: typing.Optional[typing.Literal['Dark', 'Light']]

### PoliticalView
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]


# GetStyleDescriptorResponse

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_maps.geo_maps_classes.ResponseMetadata'>
- **Required**: Yes


# GetTileRequest

### Tileset
- **Type**: <class 'str'>
- **Required**: Yes

### Z
- **Type**: <class 'str'>
- **Required**: Yes

### X
- **Type**: <class 'str'>
- **Required**: Yes

### Y
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# GetTileResponse

### Blob
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### CacheControl
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### PricingBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.geo_maps.geo_maps_classes.ResponseMetadata'>
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



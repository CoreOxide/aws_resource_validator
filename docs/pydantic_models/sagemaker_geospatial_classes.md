# Sagemaker Geospatial Classes

# AreaOfInterest

### AreaOfInterestGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestGeometryUnion]


# AreaOfInterestGeometry

### MultiPolygonGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.MultiPolygonGeometryInputUnion]

### PolygonGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PolygonGeometryInputUnion]


# AreaOfInterestGeometryOutput

### MultiPolygonGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.MultiPolygonGeometryInputOutput]

### PolygonGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PolygonGeometryInputOutput]


# AreaOfInterestGeometryUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AreaOfInterestOutput

### AreaOfInterestGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestGeometryOutput]


# AreaOfInterestUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetValue

### Href
- **Type**: typing.Optional[str]


# BandMathConfigInput

### CustomIndices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.CustomIndicesInput]

### PredefinedIndices
- **Type**: typing.Optional[typing.Sequence[str]]


# BandMathConfigInputOutput

### CustomIndices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.CustomIndicesInputOutput]

### PredefinedIndices
- **Type**: typing.Optional[typing.List[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudRemovalConfigInput

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['INTERPOLATION']]

### InterpolationValue
- **Type**: typing.Optional[str]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# CloudRemovalConfigInputOutput

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['INTERPOLATION']]

### InterpolationValue
- **Type**: typing.Optional[str]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# CustomIndicesInput

### Operations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.Operation]]


# CustomIndicesInputOutput

### Operations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.Operation]]


# DeleteEarthObservationJobInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVectorEnrichmentJobInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# EarthObservationJobErrorDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EoCloudCoverInput

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ExportEarthObservationJobInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputConfigInput'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ExportSourceImages
- **Type**: typing.Optional[bool]


# ExportEarthObservationJobOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExportSourceImages
- **Type**: <class 'bool'>
- **Required**: Yes

### ExportStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputConfigInput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes


# ExportErrorDetails

### ExportResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportErrorDetailsOutput]

### ExportSourceImages
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportErrorDetailsOutput]


# ExportErrorDetailsOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExportS3DataInput

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ExportVectorEnrichmentJobInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportVectorEnrichmentJobOutputConfig'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# ExportVectorEnrichmentJobOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExportStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportVectorEnrichmentJobOutputConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes


# ExportVectorEnrichmentJobOutputConfig

### S3Data
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobS3Data'>
- **Required**: Yes


# GeoMosaicConfigInput

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'BILINEAR', 'CUBIC', 'CUBICSPLINE', 'LANCZOS', 'MAX', 'MED', 'MIN', 'MODE', 'NEAR', 'Q1', 'Q3', 'RMS', 'SUM']]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# GeoMosaicConfigInputOutput

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'BILINEAR', 'CUBIC', 'CUBICSPLINE', 'LANCZOS', 'MAX', 'MED', 'MIN', 'MODE', 'NEAR', 'Q1', 'Q3', 'RMS', 'SUM']]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# Geometry

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetEarthObservationJobInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEarthObservationJobOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ErrorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.EarthObservationJobErrorDetails'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExportErrorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportErrorDetails'>
- **Required**: Yes

### ExportStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.InputConfigOutput'>
- **Required**: Yes

### JobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.JobConfigInputOutput'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputBands
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputBand]
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED', 'STOPPING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes


# GetRasterDataCollectionInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTileInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ImageAssets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Target
- **Type**: typing.Literal['INPUT', 'OUTPUT']
- **Required**: Yes

### x
- **Type**: <class 'int'>
- **Required**: Yes

### y
- **Type**: <class 'int'>
- **Required**: Yes

### z
- **Type**: <class 'int'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### ImageMask
- **Type**: typing.Optional[bool]

### OutputDataType
- **Type**: typing.Optional[typing.Literal['FLOAT32', 'FLOAT64', 'INT16', 'INT32', 'UINT16']]

### OutputFormat
- **Type**: typing.Optional[str]

### PropertyFilters
- **Type**: typing.Optional[str]

### TimeRangeFilter
- **Type**: typing.Optional[str]


# GetTileOutput

### BinaryFile
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes


# GetVectorEnrichmentJobInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# InputConfigInput

### PreviousEarthObservationJobArn
- **Type**: typing.Optional[str]

### RasterDataCollectionQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.RasterDataCollectionQueryInput]


# InputConfigOutput

### PreviousEarthObservationJobArn
- **Type**: typing.Optional[str]

### RasterDataCollectionQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.RasterDataCollectionQueryOutput]


# ItemSource

### DateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.Geometry'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Assets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AssetValue]]

### Properties
- **Type**: <class 'NoneType'>


# JobConfigInput

### BandMathConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.BandMathConfigInput]

### CloudMaskingConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### CloudRemovalConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.CloudRemovalConfigInput]

### GeoMosaicConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.GeoMosaicConfigInput]

### LandCoverSegmentationConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ResamplingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResamplingConfigInput]

### StackConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.StackConfigInput]

### TemporalStatisticsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TemporalStatisticsConfigInput]

### ZonalStatisticsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ZonalStatisticsConfigInput]


# JobConfigInputOutput

### BandMathConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.BandMathConfigInputOutput]

### CloudMaskingConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### CloudRemovalConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.CloudRemovalConfigInputOutput]

### GeoMosaicConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.GeoMosaicConfigInputOutput]

### LandCoverSegmentationConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ResamplingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResamplingConfigInputOutput]

### StackConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.StackConfigInputOutput]

### TemporalStatisticsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TemporalStatisticsConfigInputOutput]

### ZonalStatisticsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ZonalStatisticsConfigInputOutput]


# JobConfigInputUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LandsatCloudCoverLandInput

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ListEarthObservationJobInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED', 'STOPPING']]


# ListEarthObservationJobInputPaginate

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED', 'STOPPING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PaginatorConfig]


# ListEarthObservationJobOutput

### EarthObservationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ListEarthObservationJobOutputConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEarthObservationJobOutputConfig

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OperationType
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED', 'STOPPING']
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListRasterDataCollectionsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRasterDataCollectionsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PaginatorConfig]


# ListRasterDataCollectionsOutput

### RasterDataCollectionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.RasterDataCollectionMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes


# ListVectorEnrichmentJobInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### StatusEquals
- **Type**: typing.Optional[str]


# ListVectorEnrichmentJobInputPaginate

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### StatusEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PaginatorConfig]


# ListVectorEnrichmentJobOutput

### VectorEnrichmentJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ListVectorEnrichmentJobOutputConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListVectorEnrichmentJobOutputConfig

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MapMatchingConfig

### IdAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### TimestampAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### XAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### YAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# MultiPolygonGeometryInput

### Coordinates
- **Type**: typing.Sequence[typing.Sequence[typing.Sequence[typing.Sequence[float]]]]
- **Required**: Yes


# MultiPolygonGeometryInputOutput

### Coordinates
- **Type**: typing.List[typing.List[typing.List[typing.List[float]]]]
- **Required**: Yes


# MultiPolygonGeometryInputUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Operation

### Equation
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputType
- **Type**: typing.Optional[typing.Literal['FLOAT32', 'FLOAT64', 'INT16', 'INT32', 'UINT16']]


# OutputBand

### BandName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataType
- **Type**: typing.Literal['FLOAT32', 'FLOAT64', 'INT16', 'INT32', 'UINT16']
- **Required**: Yes


# OutputConfigInput

### S3Data
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportS3DataInput'>
- **Required**: Yes


# OutputResolutionResamplingInput

### UserDefined
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.UserDefined'>
- **Required**: Yes


# OutputResolutionStackInput

### Predefined
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'HIGHEST', 'LOWEST']]

### UserDefined
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlatformInput

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['EQUALS', 'NOT_EQUALS', 'STARTS_WITH']]


# PolygonGeometryInput

### Coordinates
- **Type**: typing.Sequence[typing.Sequence[typing.Sequence[float]]]
- **Required**: Yes


# PolygonGeometryInputOutput

### Coordinates
- **Type**: typing.List[typing.List[typing.List[float]]]
- **Required**: Yes


# PolygonGeometryInputUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Properties

### EoCloudCover
- **Type**: typing.Optional[float]

### LandsatCloudCoverLand
- **Type**: typing.Optional[float]

### Platform
- **Type**: typing.Optional[str]

### ViewOffNadir
- **Type**: typing.Optional[float]

### ViewSunAzimuth
- **Type**: typing.Optional[float]

### ViewSunElevation
- **Type**: typing.Optional[float]


# Property

### EoCloudCover
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.EoCloudCoverInput]

### LandsatCloudCoverLand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.LandsatCloudCoverLandInput]

### Platform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PlatformInput]

### ViewOffNadir
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ViewOffNadirInput]

### ViewSunAzimuth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ViewSunAzimuthInput]

### ViewSunElevation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ViewSunElevationInput]


# PropertyFilter

### Property
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.Property'>
- **Required**: Yes


# PropertyFilters

### LogicalOperator
- **Type**: typing.Optional[typing.Literal['AND']]

### Properties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFilter]]


# PropertyFiltersOutput

### LogicalOperator
- **Type**: typing.Optional[typing.Literal['AND']]

### Properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFilter]]


# PropertyFiltersUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RasterDataCollectionMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RasterDataCollectionQueryInput

### RasterDataCollectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRangeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TimeRangeFilterInput'>
- **Required**: Yes

### AreaOfInterest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestUnion]

### PropertyFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFiltersUnion]


# RasterDataCollectionQueryOutput

### RasterDataCollectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### RasterDataCollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRangeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TimeRangeFilterOutput'>
- **Required**: Yes

### AreaOfInterest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestOutput]

### PropertyFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFiltersOutput]


# RasterDataCollectionQueryWithBandFilterInput

### TimeRangeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TimeRangeFilterInput'>
- **Required**: Yes

### AreaOfInterest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestUnion]

### BandFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### PropertyFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFiltersUnion]


# ResamplingConfigInput

### OutputResolution
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputResolutionResamplingInput'>
- **Required**: Yes

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'BILINEAR', 'CUBIC', 'CUBICSPLINE', 'LANCZOS', 'MAX', 'MED', 'MIN', 'MODE', 'NEAR', 'Q1', 'Q3', 'RMS', 'SUM']]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# ResamplingConfigInputOutput

### OutputResolution
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputResolutionResamplingInput'>
- **Required**: Yes

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'BILINEAR', 'CUBIC', 'CUBICSPLINE', 'LANCZOS', 'MAX', 'MED', 'MIN', 'MODE', 'NEAR', 'Q1', 'Q3', 'RMS', 'SUM']]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


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


# ReverseGeocodingConfig

### XAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### YAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# SearchRasterDataCollectionInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RasterDataCollectionQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.RasterDataCollectionQueryWithBandFilterInput'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchRasterDataCollectionOutput

### ApproximateResultCount
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ItemSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StackConfigInput

### OutputResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputResolutionStackInput]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# StackConfigInputOutput

### OutputResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputResolutionStackInput]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# StartEarthObservationJobInput

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.InputConfigInput'>
- **Required**: Yes

### JobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.JobConfigInputUnion'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartEarthObservationJobOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.InputConfigOutput'>
- **Required**: Yes

### JobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.JobConfigInputOutput'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED', 'STOPPING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadata'>
- **Required**: Yes


# StartVectorEnrichmentJobInput

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobInputConfig'>
- **Required**: Yes

### JobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobConfig'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StopEarthObservationJobInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopVectorEnrichmentJobInput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemporalStatisticsConfigInput

### Statistics
- **Type**: typing.Sequence[typing.Literal['MEAN', 'MEDIAN', 'STANDARD_DEVIATION']]
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.Literal['ALL', 'YEARLY']]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# TemporalStatisticsConfigInputOutput

### Statistics
- **Type**: typing.List[typing.Literal['MEAN', 'MEDIAN', 'STANDARD_DEVIATION']]
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.Literal['ALL', 'YEARLY']]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# TimeRangeFilterInput

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.Timestamp'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.Timestamp'>
- **Required**: Yes


# TimeRangeFilterOutput

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UserDefined

### Unit
- **Type**: typing.Literal['METERS']
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# VectorEnrichmentJobConfig

### MapMatchingConfig
- **Type**: <class 'NoneType'>

### ReverseGeocodingConfig
- **Type**: <class 'NoneType'>


# VectorEnrichmentJobDataSourceConfigInput

### S3Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobS3Data]


# VectorEnrichmentJobErrorDetails

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[typing.Literal['CLIENT_ERROR', 'SERVER_ERROR']]


# VectorEnrichmentJobInputConfig

### DataSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobDataSourceConfigInput'>
- **Required**: Yes

### DocumentType
- **Type**: typing.Literal['CSV']
- **Required**: Yes


# VectorEnrichmentJobS3Data

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ViewOffNadirInput

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ViewSunAzimuthInput

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ViewSunElevationInput

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ZonalStatisticsConfigInput

### Statistics
- **Type**: typing.Sequence[typing.Literal['MAX', 'MEAN', 'MEDIAN', 'MIN', 'STANDARD_DEVIATION', 'SUM']]
- **Required**: Yes

### ZoneS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]

### ZoneS3PathKmsKeyId
- **Type**: typing.Optional[str]


# ZonalStatisticsConfigInputOutput

### Statistics
- **Type**: typing.List[typing.Literal['MAX', 'MEAN', 'MEDIAN', 'MIN', 'STANDARD_DEVIATION', 'SUM']]
- **Required**: Yes

### ZoneS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### TargetBands
- **Type**: typing.Optional[typing.List[str]]

### ZoneS3PathKmsKeyId
- **Type**: typing.Optional[str]



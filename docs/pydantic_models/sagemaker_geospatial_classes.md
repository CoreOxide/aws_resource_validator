# Sagemaker Geospatial Classes

# AreaOfInterestGeometryOutputTypeDef

### MultiPolygonGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.MultiPolygonGeometryInputOutputTypeDef]

### PolygonGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PolygonGeometryInputOutputTypeDef]


# AreaOfInterestGeometryTypeDef

### MultiPolygonGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.MultiPolygonGeometryInputUnionTypeDef]

### PolygonGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PolygonGeometryInputUnionTypeDef]


# AreaOfInterestGeometryUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AreaOfInterestOutputTypeDef

### AreaOfInterestGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestGeometryOutputTypeDef]


# AreaOfInterestTypeDef

### AreaOfInterestGeometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestGeometryUnionTypeDef]


# AreaOfInterestUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssetValueTypeDef

### Href
- **Type**: typing.Optional[str]


# BandMathConfigInputOutputTypeDef

### CustomIndices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.CustomIndicesInputOutputTypeDef]

### PredefinedIndices
- **Type**: typing.Optional[typing.List[str]]


# BandMathConfigInputTypeDef

### CustomIndices
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.CustomIndicesInputTypeDef]

### PredefinedIndices
- **Type**: typing.Optional[typing.Sequence[str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudRemovalConfigInputOutputTypeDef

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['INTERPOLATION']]

### InterpolationValue
- **Type**: typing.Optional[str]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# CloudRemovalConfigInputTypeDef

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['INTERPOLATION']]

### InterpolationValue
- **Type**: typing.Optional[str]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# CustomIndicesInputOutputTypeDef

### Operations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OperationTypeDef]]


# CustomIndicesInputTypeDef

### Operations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OperationTypeDef]]


# DeleteEarthObservationJobInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVectorEnrichmentJobInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# EarthObservationJobErrorDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EoCloudCoverInputTypeDef

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ExportEarthObservationJobInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputConfigInputTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ExportSourceImages
- **Type**: typing.Optional[bool]


# ExportEarthObservationJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputConfigInputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExportErrorDetailsOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExportErrorDetailsTypeDef

### ExportResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportErrorDetailsOutputTypeDef]

### ExportSourceImages
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportErrorDetailsOutputTypeDef]


# ExportS3DataInputTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ExportVectorEnrichmentJobInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportVectorEnrichmentJobOutputConfigTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# ExportVectorEnrichmentJobOutputConfigTypeDef

### S3Data
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobS3DataTypeDef'>
- **Required**: Yes


# ExportVectorEnrichmentJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportVectorEnrichmentJobOutputConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GeoMosaicConfigInputOutputTypeDef

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'BILINEAR', 'CUBIC', 'CUBICSPLINE', 'LANCZOS', 'MAX', 'MED', 'MIN', 'MODE', 'NEAR', 'Q1', 'Q3', 'RMS', 'SUM']]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# GeoMosaicConfigInputTypeDef

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'BILINEAR', 'CUBIC', 'CUBICSPLINE', 'LANCZOS', 'MAX', 'MED', 'MIN', 'MODE', 'NEAR', 'Q1', 'Q3', 'RMS', 'SUM']]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# GeometryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetEarthObservationJobInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEarthObservationJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.EarthObservationJobErrorDetailsTypeDef'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExportErrorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportErrorDetailsTypeDef'>
- **Required**: Yes

### ExportStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.InputConfigOutputTypeDef'>
- **Required**: Yes

### JobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.JobConfigInputOutputTypeDef'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputBands
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputBandTypeDef]
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED', 'STOPPING']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRasterDataCollectionInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTileInputTypeDef

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


# GetTileOutputTypeDef

### BinaryFile
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVectorEnrichmentJobInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# InputConfigInputTypeDef

### PreviousEarthObservationJobArn
- **Type**: typing.Optional[str]

### RasterDataCollectionQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.RasterDataCollectionQueryInputTypeDef]


# InputConfigOutputTypeDef

### PreviousEarthObservationJobArn
- **Type**: typing.Optional[str]

### RasterDataCollectionQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.RasterDataCollectionQueryOutputTypeDef]


# ItemSourceTypeDef

### DateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Geometry
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.GeometryTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Assets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AssetValueTypeDef]]

### Properties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertiesTypeDef]


# JobConfigInputOutputTypeDef

### BandMathConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.BandMathConfigInputOutputTypeDef]

### CloudMaskingConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### CloudRemovalConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.CloudRemovalConfigInputOutputTypeDef]

### GeoMosaicConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.GeoMosaicConfigInputOutputTypeDef]

### LandCoverSegmentationConfig
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ResamplingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResamplingConfigInputOutputTypeDef]

### StackConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.StackConfigInputOutputTypeDef]

### TemporalStatisticsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TemporalStatisticsConfigInputOutputTypeDef]

### ZonalStatisticsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ZonalStatisticsConfigInputOutputTypeDef]


# JobConfigInputTypeDef

### BandMathConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.BandMathConfigInputTypeDef]

### CloudMaskingConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### CloudRemovalConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.CloudRemovalConfigInputTypeDef]

### GeoMosaicConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.GeoMosaicConfigInputTypeDef]

### LandCoverSegmentationConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ResamplingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResamplingConfigInputTypeDef]

### StackConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.StackConfigInputTypeDef]

### TemporalStatisticsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TemporalStatisticsConfigInputTypeDef]

### ZonalStatisticsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ZonalStatisticsConfigInputTypeDef]


# JobConfigInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LandsatCloudCoverLandInputTypeDef

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ListEarthObservationJobInputPaginateTypeDef

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### StatusEquals
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'DELETED', 'DELETING', 'FAILED', 'INITIALIZING', 'IN_PROGRESS', 'STOPPED', 'STOPPING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PaginatorConfigTypeDef]


# ListEarthObservationJobInputTypeDef

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


# ListEarthObservationJobOutputConfigTypeDef

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


# ListEarthObservationJobOutputTypeDef

### EarthObservationJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ListEarthObservationJobOutputConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRasterDataCollectionsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PaginatorConfigTypeDef]


# ListRasterDataCollectionsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRasterDataCollectionsOutputTypeDef

### RasterDataCollectionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.RasterDataCollectionMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVectorEnrichmentJobInputPaginateTypeDef

### SortBy
- **Type**: typing.Optional[str]

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### StatusEquals
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PaginatorConfigTypeDef]


# ListVectorEnrichmentJobInputTypeDef

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


# ListVectorEnrichmentJobOutputConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListVectorEnrichmentJobOutputTypeDef

### VectorEnrichmentJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ListVectorEnrichmentJobOutputConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MapMatchingConfigTypeDef

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


# MultiPolygonGeometryInputOutputTypeDef

### Coordinates
- **Type**: typing.List[typing.List[typing.List[typing.List[float]]]]
- **Required**: Yes


# MultiPolygonGeometryInputTypeDef

### Coordinates
- **Type**: typing.Sequence[typing.Sequence[typing.Sequence[typing.Sequence[float]]]]
- **Required**: Yes


# MultiPolygonGeometryInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OperationTypeDef

### Equation
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OutputType
- **Type**: typing.Optional[typing.Literal['FLOAT32', 'FLOAT64', 'INT16', 'INT32', 'UINT16']]


# OutputBandTypeDef

### BandName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputDataType
- **Type**: typing.Literal['FLOAT32', 'FLOAT64', 'INT16', 'INT32', 'UINT16']
- **Required**: Yes


# OutputConfigInputTypeDef

### S3Data
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ExportS3DataInputTypeDef'>
- **Required**: Yes


# OutputResolutionResamplingInputTypeDef

### UserDefined
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.UserDefinedTypeDef'>
- **Required**: Yes


# OutputResolutionStackInputTypeDef

### Predefined
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'HIGHEST', 'LOWEST']]

### UserDefined
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.UserDefinedTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlatformInputTypeDef

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['EQUALS', 'NOT_EQUALS', 'STARTS_WITH']]


# PolygonGeometryInputOutputTypeDef

### Coordinates
- **Type**: typing.List[typing.List[typing.List[float]]]
- **Required**: Yes


# PolygonGeometryInputTypeDef

### Coordinates
- **Type**: typing.Sequence[typing.Sequence[typing.Sequence[float]]]
- **Required**: Yes


# PolygonGeometryInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PropertiesTypeDef

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


# PropertyFilterTypeDef

### Property
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyTypeDef'>
- **Required**: Yes


# PropertyFiltersOutputTypeDef

### LogicalOperator
- **Type**: typing.Optional[typing.Literal['AND']]

### Properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFilterTypeDef]]


# PropertyFiltersTypeDef

### LogicalOperator
- **Type**: typing.Optional[typing.Literal['AND']]

### Properties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFilterTypeDef]]


# PropertyFiltersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PropertyTypeDef

### EoCloudCover
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.EoCloudCoverInputTypeDef]

### LandsatCloudCoverLand
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.LandsatCloudCoverLandInputTypeDef]

### Platform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PlatformInputTypeDef]

### ViewOffNadir
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ViewOffNadirInputTypeDef]

### ViewSunAzimuth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ViewSunAzimuthInputTypeDef]

### ViewSunElevation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ViewSunElevationInputTypeDef]


# RasterDataCollectionMetadataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RasterDataCollectionQueryInputTypeDef

### RasterDataCollectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRangeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TimeRangeFilterInputTypeDef'>
- **Required**: Yes

### AreaOfInterest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestUnionTypeDef]

### PropertyFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFiltersUnionTypeDef]


# RasterDataCollectionQueryOutputTypeDef

### RasterDataCollectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### RasterDataCollectionName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeRangeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TimeRangeFilterOutputTypeDef'>
- **Required**: Yes

### AreaOfInterest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestOutputTypeDef]

### PropertyFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFiltersOutputTypeDef]


# RasterDataCollectionQueryWithBandFilterInputTypeDef

### TimeRangeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TimeRangeFilterInputTypeDef'>
- **Required**: Yes

### AreaOfInterest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.AreaOfInterestUnionTypeDef]

### BandFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### PropertyFilters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.PropertyFiltersUnionTypeDef]


# ResamplingConfigInputOutputTypeDef

### OutputResolution
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputResolutionResamplingInputTypeDef'>
- **Required**: Yes

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'BILINEAR', 'CUBIC', 'CUBICSPLINE', 'LANCZOS', 'MAX', 'MED', 'MIN', 'MODE', 'NEAR', 'Q1', 'Q3', 'RMS', 'SUM']]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# ResamplingConfigInputTypeDef

### OutputResolution
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputResolutionResamplingInputTypeDef'>
- **Required**: Yes

### AlgorithmName
- **Type**: typing.Optional[typing.Literal['AVERAGE', 'BILINEAR', 'CUBIC', 'CUBICSPLINE', 'LANCZOS', 'MAX', 'MED', 'MIN', 'MODE', 'NEAR', 'Q1', 'Q3', 'RMS', 'SUM']]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


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


# ReverseGeocodingConfigTypeDef

### XAttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### YAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# SearchRasterDataCollectionInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### RasterDataCollectionQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.RasterDataCollectionQueryWithBandFilterInputTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchRasterDataCollectionOutputTypeDef

### ApproximateResultCount
- **Type**: <class 'int'>
- **Required**: Yes

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ItemSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# StackConfigInputOutputTypeDef

### OutputResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputResolutionStackInputTypeDef]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# StackConfigInputTypeDef

### OutputResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.OutputResolutionStackInputTypeDef]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# StartEarthObservationJobInputTypeDef

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.InputConfigInputTypeDef'>
- **Required**: Yes

### JobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.JobConfigInputUnionTypeDef'>
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


# StartEarthObservationJobOutputTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.InputConfigOutputTypeDef'>
- **Required**: Yes

### JobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.JobConfigInputOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartVectorEnrichmentJobInputTypeDef

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobInputConfigTypeDef'>
- **Required**: Yes

### JobConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobConfigTypeDef'>
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


# StopEarthObservationJobInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# StopVectorEnrichmentJobInputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemporalStatisticsConfigInputOutputTypeDef

### Statistics
- **Type**: typing.List[typing.Literal['MEAN', 'MEDIAN', 'STANDARD_DEVIATION']]
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.Literal['ALL', 'YEARLY']]

### TargetBands
- **Type**: typing.Optional[typing.List[str]]


# TemporalStatisticsConfigInputTypeDef

### Statistics
- **Type**: typing.Sequence[typing.Literal['MEAN', 'MEDIAN', 'STANDARD_DEVIATION']]
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[typing.Literal['ALL', 'YEARLY']]

### TargetBands
- **Type**: typing.Optional[typing.Sequence[str]]


# TimeRangeFilterInputTypeDef

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TimestampTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.TimestampTypeDef'>
- **Required**: Yes


# TimeRangeFilterOutputTypeDef

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UserDefinedTypeDef

### Unit
- **Type**: typing.Literal['METERS']
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# VectorEnrichmentJobConfigTypeDef

### MapMatchingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.MapMatchingConfigTypeDef]

### ReverseGeocodingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.ReverseGeocodingConfigTypeDef]


# VectorEnrichmentJobDataSourceConfigInputTypeDef

### S3Data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobS3DataTypeDef]


# VectorEnrichmentJobErrorDetailsTypeDef

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorType
- **Type**: typing.Optional[typing.Literal['CLIENT_ERROR', 'SERVER_ERROR']]


# VectorEnrichmentJobInputConfigTypeDef

### DataSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_geospatial_classes.VectorEnrichmentJobDataSourceConfigInputTypeDef'>
- **Required**: Yes

### DocumentType
- **Type**: typing.Literal['CSV']
- **Required**: Yes


# VectorEnrichmentJobS3DataTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# ViewOffNadirInputTypeDef

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ViewSunAzimuthInputTypeDef

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ViewSunElevationInputTypeDef

### LowerBound
- **Type**: <class 'float'>
- **Required**: Yes

### UpperBound
- **Type**: <class 'float'>
- **Required**: Yes


# ZonalStatisticsConfigInputOutputTypeDef

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


# ZonalStatisticsConfigInputTypeDef

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



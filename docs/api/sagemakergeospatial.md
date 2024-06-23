# Sagemakergeospatial Service

### DataCollectionArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:raster-data-collection/(public|premium|user)/[a-z0-9]{12,}$`

### EarthObservationJobArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:earth-observation-job/[a-z0-9]{12,}$`

### ExecutionRoleArn
- **Type**: string
- **Pattern**: `^arn:(aws[a-z-]*):iam::([0-9]{12}):role/[a-zA-Z0-9+=,.@_/-]+$`
- **Min Length**: 20
- **Max Length**: 2048

### S3Uri
- **Type**: string
- **Pattern**: `^s3://([^/]+)/?(.*)$`

### VectorEnrichmentJobArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z-]{0,12}:sagemaker-geospatial:[a-z0-9-]{1,25}:[0-9]{12}:vector-enrichment-job/[a-z0-9]{12,}$`


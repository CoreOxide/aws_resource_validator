# Dataexchange Classes

# ActionTypeDef

### ExportRevisionToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.AutoExportRevisionToS3RequestDetailsTypeDef]


# ApiGatewayApiAssetTypeDef

### ApiDescription
- **Type**: typing.Optional[str]

### ApiEndpoint
- **Type**: typing.Optional[str]

### ApiId
- **Type**: typing.Optional[str]

### ApiKey
- **Type**: typing.Optional[str]

### ApiName
- **Type**: typing.Optional[str]

### ApiSpecificationDownloadUrl
- **Type**: typing.Optional[str]

### ApiSpecificationDownloadUrlExpiresAt
- **Type**: typing.Optional[datetime.datetime]

### ProtocolType
- **Type**: typing.Optional[typing.Literal['REST']]

### Stage
- **Type**: typing.Optional[str]


# AssetDestinationEntryTypeDef

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# AssetDetailsPaginatorTypeDef

### S3SnapshotAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.S3SnapshotAssetTypeDef]

### RedshiftDataShareAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.RedshiftDataShareAssetTypeDef]

### ApiGatewayApiAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ApiGatewayApiAssetTypeDef]

### S3DataAccessAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.S3DataAccessAssetTypeDef]

### LakeFormationDataPermissionAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.LakeFormationDataPermissionAssetPaginatorTypeDef]


# AssetDetailsTypeDef

### S3SnapshotAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.S3SnapshotAssetTypeDef]

### RedshiftDataShareAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.RedshiftDataShareAssetTypeDef]

### ApiGatewayApiAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ApiGatewayApiAssetTypeDef]

### S3DataAccessAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.S3DataAccessAssetTypeDef]

### LakeFormationDataPermissionAsset
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.LakeFormationDataPermissionAssetTypeDef]


# AssetEntryPaginatorTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.AssetDetailsPaginatorTypeDef'>
- **Required**: Yes

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceId
- **Type**: typing.Optional[str]


# AssetEntryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.AssetDetailsTypeDef'>
- **Required**: Yes

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceId
- **Type**: typing.Optional[str]


# AssetSourceEntryTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# AutoExportRevisionDestinationEntryTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPattern
- **Type**: typing.Optional[str]


# AutoExportRevisionToS3RequestDetailsTypeDef

### RevisionDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.AutoExportRevisionDestinationEntryTypeDef'>
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportServerSideEncryptionTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDataSetRequestRequestTypeDef

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDataSetResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: typing.Literal['ENTITLED', 'OWNED']
- **Required**: Yes

### OriginDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.OriginDetailsTypeDef'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventActionRequestRequestTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ActionTypeDef'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.EventTypeDef'>
- **Required**: Yes


# CreateEventActionResponseTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ActionTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.EventTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobRequestRequestTypeDef

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.RequestDetailsTypeDef'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET', 'EXPORT_ASSETS_TO_S3', 'EXPORT_ASSET_TO_SIGNED_URL', 'EXPORT_REVISIONS_TO_S3', 'IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY', 'IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES', 'IMPORT_ASSETS_FROM_S3', 'IMPORT_ASSET_FROM_API_GATEWAY_API', 'IMPORT_ASSET_FROM_SIGNED_URL']
- **Required**: Yes


# CreateJobResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseDetailsTypeDef'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.JobErrorTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'ERROR', 'IN_PROGRESS', 'TIMED_OUT', 'WAITING']
- **Required**: Yes

### Type
- **Type**: typing.Literal['CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET', 'EXPORT_ASSETS_TO_S3', 'EXPORT_ASSET_TO_SIGNED_URL', 'EXPORT_REVISIONS_TO_S3', 'IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY', 'IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES', 'IMPORT_ASSETS_FROM_S3', 'IMPORT_ASSET_FROM_API_GATEWAY_API', 'IMPORT_ASSET_FROM_SIGNED_URL']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRevisionRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRevisionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Finalized
- **Type**: <class 'bool'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RevocationComment
- **Type**: <class 'str'>
- **Required**: Yes

### Revoked
- **Type**: <class 'bool'>
- **Required**: Yes

### RevokedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateS3DataAccessFromS3BucketRequestDetailsTypeDef

### AssetSource
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.S3DataAccessAssetSourceEntryTypeDef'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateS3DataAccessFromS3BucketResponseDetailsPaginatorTypeDef

### AssetSource
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.S3DataAccessAssetSourceEntryPaginatorTypeDef'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateS3DataAccessFromS3BucketResponseDetailsTypeDef

### AssetSource
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.S3DataAccessAssetSourceEntryTypeDef'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DataSetEntryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: typing.Literal['ENTITLED', 'OWNED']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OriginDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.OriginDetailsTypeDef]

### SourceId
- **Type**: typing.Optional[str]


# DataUpdateRequestDetailsTypeDef

### DataUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DatabaseLFTagPolicyAndPermissionsPaginatorTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagPaginatorTypeDef]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE']]
- **Required**: Yes


# DatabaseLFTagPolicyAndPermissionsTypeDef

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagTypeDef]
- **Required**: Yes

### Permissions
- **Type**: typing.Sequence[typing.Literal['DESCRIBE']]
- **Required**: Yes


# DatabaseLFTagPolicyPaginatorTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagPaginatorTypeDef]
- **Required**: Yes


# DatabaseLFTagPolicyTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagTypeDef]
- **Required**: Yes


# DeleteAssetRequestRequestTypeDef

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSetRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventActionRequestRequestTypeDef

### EventActionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRevisionRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecationRequestDetailsTypeDef

### DeprecationAt
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# DetailsTypeDef

### ImportAssetFromSignedUrlJobErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetFromSignedUrlJobErrorDetailsTypeDef]

### ImportAssetsFromS3JobErrorDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.AssetSourceEntryTypeDef]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventActionEntryTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ActionTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.EventTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# EventTypeDef

### RevisionPublished
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.RevisionPublishedTypeDef]


# ExportAssetToSignedUrlRequestDetailsTypeDef

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportAssetToSignedUrlResponseDetailsTypeDef

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### SignedUrl
- **Type**: typing.Optional[str]

### SignedUrlExpiresAt
- **Type**: typing.Optional[datetime.datetime]


# ExportAssetsToS3RequestDetailsTypeDef

### AssetDestinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.AssetDestinationEntryTypeDef]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportServerSideEncryptionTypeDef]


# ExportAssetsToS3ResponseDetailsTypeDef

### AssetDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.AssetDestinationEntryTypeDef]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportServerSideEncryptionTypeDef]


# ExportRevisionsToS3RequestDetailsTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionDestinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.RevisionDestinationEntryTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportServerSideEncryptionTypeDef]


# ExportRevisionsToS3ResponseDetailsTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.RevisionDestinationEntryTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportServerSideEncryptionTypeDef]

### EventActionArn
- **Type**: typing.Optional[str]


# ExportServerSideEncryptionTypeDef

### Type
- **Type**: typing.Literal['AES256', 'aws:kms']
- **Required**: Yes

### KmsKeyArn
- **Type**: typing.Optional[str]


# GetAssetRequestRequestTypeDef

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssetResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.AssetDetailsTypeDef'>
- **Required**: Yes

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSetRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSetResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: typing.Literal['ENTITLED', 'OWNED']
- **Required**: Yes

### OriginDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.OriginDetailsTypeDef'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventActionRequestRequestTypeDef

### EventActionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventActionResponseTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ActionTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.EventTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseDetailsTypeDef'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.JobErrorTypeDef]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'ERROR', 'IN_PROGRESS', 'TIMED_OUT', 'WAITING']
- **Required**: Yes

### Type
- **Type**: typing.Literal['CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET', 'EXPORT_ASSETS_TO_S3', 'EXPORT_ASSET_TO_SIGNED_URL', 'EXPORT_REVISIONS_TO_S3', 'IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY', 'IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES', 'IMPORT_ASSETS_FROM_S3', 'IMPORT_ASSET_FROM_API_GATEWAY_API', 'IMPORT_ASSET_FROM_SIGNED_URL']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRevisionRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRevisionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Finalized
- **Type**: <class 'bool'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RevocationComment
- **Type**: <class 'str'>
- **Required**: Yes

### Revoked
- **Type**: <class 'bool'>
- **Required**: Yes

### RevokedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportAssetFromApiGatewayApiRequestDetailsTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiSpecificationMd5Hash
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['REST']
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### ApiDescription
- **Type**: typing.Optional[str]

### ApiKey
- **Type**: typing.Optional[str]


# ImportAssetFromApiGatewayApiResponseDetailsTypeDef

### ApiId
- **Type**: <class 'str'>
- **Required**: Yes

### ApiName
- **Type**: <class 'str'>
- **Required**: Yes

### ApiSpecificationMd5Hash
- **Type**: <class 'str'>
- **Required**: Yes

### ApiSpecificationUploadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ApiSpecificationUploadUrlExpiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### ProtocolType
- **Type**: typing.Literal['REST']
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Stage
- **Type**: <class 'str'>
- **Required**: Yes

### ApiDescription
- **Type**: typing.Optional[str]

### ApiKey
- **Type**: typing.Optional[str]


# ImportAssetFromSignedUrlJobErrorDetailsTypeDef

### AssetName
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetFromSignedUrlRequestDetailsTypeDef

### AssetName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Md5Hash
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetFromSignedUrlResponseDetailsTypeDef

### AssetName
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Md5Hash
- **Type**: typing.Optional[str]

### SignedUrl
- **Type**: typing.Optional[str]

### SignedUrlExpiresAt
- **Type**: typing.Optional[datetime.datetime]


# ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DatabaseLFTagPolicyAndPermissionsTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TableLFTagPolicyAndPermissionsTypeDef]


# ImportAssetsFromLakeFormationTagPolicyResponseDetailsPaginatorTypeDef

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DatabaseLFTagPolicyAndPermissionsPaginatorTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TableLFTagPolicyAndPermissionsPaginatorTypeDef]


# ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DatabaseLFTagPolicyAndPermissionsTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TableLFTagPolicyAndPermissionsTypeDef]


# ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef

### AssetSources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.RedshiftDataShareAssetSourceEntryTypeDef]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef

### AssetSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.RedshiftDataShareAssetSourceEntryTypeDef]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetsFromS3RequestDetailsTypeDef

### AssetSources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.AssetSourceEntryTypeDef]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetsFromS3ResponseDetailsTypeDef

### AssetSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.AssetSourceEntryTypeDef]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# JobEntryPaginatorTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseDetailsPaginatorTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'ERROR', 'IN_PROGRESS', 'TIMED_OUT', 'WAITING']
- **Required**: Yes

### Type
- **Type**: typing.Literal['CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET', 'EXPORT_ASSETS_TO_S3', 'EXPORT_ASSET_TO_SIGNED_URL', 'EXPORT_REVISIONS_TO_S3', 'IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY', 'IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES', 'IMPORT_ASSETS_FROM_S3', 'IMPORT_ASSET_FROM_API_GATEWAY_API', 'IMPORT_ASSET_FROM_SIGNED_URL']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.JobErrorTypeDef]]


# JobEntryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseDetailsTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'ERROR', 'IN_PROGRESS', 'TIMED_OUT', 'WAITING']
- **Required**: Yes

### Type
- **Type**: typing.Literal['CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET', 'EXPORT_ASSETS_TO_S3', 'EXPORT_ASSET_TO_SIGNED_URL', 'EXPORT_REVISIONS_TO_S3', 'IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY', 'IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES', 'IMPORT_ASSETS_FROM_S3', 'IMPORT_ASSET_FROM_API_GATEWAY_API', 'IMPORT_ASSET_FROM_SIGNED_URL']
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.JobErrorTypeDef]]


# JobErrorTypeDef

### Code
- **Type**: typing.Literal['ACCESS_DENIED_EXCEPTION', 'INTERNAL_SERVER_EXCEPTION', 'MALWARE_DETECTED', 'MALWARE_SCAN_ENCRYPTED_FILE', 'RESOURCE_NOT_FOUND_EXCEPTION', 'SERVICE_QUOTA_EXCEEDED_EXCEPTION', 'VALIDATION_EXCEPTION']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DetailsTypeDef]

### LimitName
- **Type**: typing.Optional[typing.Literal['AWS Lake Formation data permission assets per revision', 'Amazon Redshift datashare assets per revision', 'Amazon S3 data access assets per revision', 'Asset size in GB', 'Assets per revision']]

### LimitValue
- **Type**: typing.Optional[float]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['ASSET', 'DATA_SET', 'REVISION']]


# KmsKeyToGrantTypeDef

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# LFResourceDetailsPaginatorTypeDef

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DatabaseLFTagPolicyPaginatorTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TableLFTagPolicyPaginatorTypeDef]


# LFResourceDetailsTypeDef

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DatabaseLFTagPolicyTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TableLFTagPolicyTypeDef]


# LFTagPaginatorTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# LFTagPolicyDetailsPaginatorTypeDef

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.LFResourceDetailsPaginatorTypeDef'>
- **Required**: Yes


# LFTagPolicyDetailsTypeDef

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.LFResourceDetailsTypeDef'>
- **Required**: Yes


# LFTagTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# LakeFormationDataPermissionAssetPaginatorTypeDef

### LakeFormationDataPermissionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.LakeFormationDataPermissionDetailsPaginatorTypeDef'>
- **Required**: Yes

### LakeFormationDataPermissionType
- **Type**: typing.Literal['LFTagPolicy']
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]


# LakeFormationDataPermissionAssetTypeDef

### LakeFormationDataPermissionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.LakeFormationDataPermissionDetailsTypeDef'>
- **Required**: Yes

### LakeFormationDataPermissionType
- **Type**: typing.Literal['LFTagPolicy']
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]


# LakeFormationDataPermissionDetailsPaginatorTypeDef

### LFTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagPolicyDetailsPaginatorTypeDef]


# LakeFormationDataPermissionDetailsTypeDef

### LFTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagPolicyDetailsTypeDef]


# LakeFormationTagPolicyDetailsTypeDef

### Database
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]


# ListDataSetRevisionsRequestListDataSetRevisionsPaginateTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListDataSetRevisionsRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetRevisionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.RevisionEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSetsRequestListDataSetsPaginateTypeDef

### Origin
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListDataSetsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Origin
- **Type**: typing.Optional[str]


# ListDataSetsResponseTypeDef

### DataSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.DataSetEntryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEventActionsRequestListEventActionsPaginateTypeDef

### EventSourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListEventActionsRequestRequestTypeDef

### EventSourceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEventActionsResponseTypeDef

### EventActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.EventActionEntryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsRequestListJobsPaginateTypeDef

### DataSetId
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListJobsRequestRequestTypeDef

### DataSetId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# ListJobsResponsePaginatorTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.JobEntryPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.JobEntryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRevisionAssetsRequestListRevisionAssetsPaginateTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListRevisionAssetsRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRevisionAssetsResponsePaginatorTypeDef

### Assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.AssetEntryPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRevisionAssetsResponseTypeDef

### Assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.AssetEntryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotificationDetailsTypeDef

### DataUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DataUpdateRequestDetailsTypeDef]

### Deprecation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DeprecationRequestDetailsTypeDef]

### SchemaChange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.SchemaChangeRequestDetailsTypeDef]


# OriginDetailsTypeDef

### ProductId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RedshiftDataShareAssetSourceEntryTypeDef

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftDataShareAssetTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftDataShareDetailsTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Function
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]

### Schema
- **Type**: typing.Optional[str]

### View
- **Type**: typing.Optional[str]


# RequestDetailsTypeDef

### ExportAssetToSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportAssetToSignedUrlRequestDetailsTypeDef]

### ExportAssetsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportAssetsToS3RequestDetailsTypeDef]

### ExportRevisionsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportRevisionsToS3RequestDetailsTypeDef]

### ImportAssetFromSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetFromSignedUrlRequestDetailsTypeDef]

### ImportAssetsFromS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromS3RequestDetailsTypeDef]

### ImportAssetsFromRedshiftDataShares
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromRedshiftDataSharesRequestDetailsTypeDef]

### ImportAssetFromApiGatewayApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetFromApiGatewayApiRequestDetailsTypeDef]

### CreateS3DataAccessFromS3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.CreateS3DataAccessFromS3BucketRequestDetailsTypeDef]

### ImportAssetsFromLakeFormationTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromLakeFormationTagPolicyRequestDetailsTypeDef]


# ResponseDetailsPaginatorTypeDef

### ExportAssetToSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportAssetToSignedUrlResponseDetailsTypeDef]

### ExportAssetsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportAssetsToS3ResponseDetailsTypeDef]

### ExportRevisionsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportRevisionsToS3ResponseDetailsTypeDef]

### ImportAssetFromSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetFromSignedUrlResponseDetailsTypeDef]

### ImportAssetsFromS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromS3ResponseDetailsTypeDef]

### ImportAssetsFromRedshiftDataShares
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef]

### ImportAssetFromApiGatewayApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetFromApiGatewayApiResponseDetailsTypeDef]

### CreateS3DataAccessFromS3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.CreateS3DataAccessFromS3BucketResponseDetailsPaginatorTypeDef]

### ImportAssetsFromLakeFormationTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromLakeFormationTagPolicyResponseDetailsPaginatorTypeDef]


# ResponseDetailsTypeDef

### ExportAssetToSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportAssetToSignedUrlResponseDetailsTypeDef]

### ExportAssetsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportAssetsToS3ResponseDetailsTypeDef]

### ExportRevisionsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ExportRevisionsToS3ResponseDetailsTypeDef]

### ImportAssetFromSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetFromSignedUrlResponseDetailsTypeDef]

### ImportAssetsFromS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromS3ResponseDetailsTypeDef]

### ImportAssetsFromRedshiftDataShares
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromRedshiftDataSharesResponseDetailsTypeDef]

### ImportAssetFromApiGatewayApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetFromApiGatewayApiResponseDetailsTypeDef]

### CreateS3DataAccessFromS3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.CreateS3DataAccessFromS3BucketResponseDetailsTypeDef]

### ImportAssetsFromLakeFormationTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ImportAssetsFromLakeFormationTagPolicyResponseDetailsTypeDef]


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


# RevisionDestinationEntryTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPattern
- **Type**: typing.Optional[str]


# RevisionEntryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### Finalized
- **Type**: typing.Optional[bool]

### SourceId
- **Type**: typing.Optional[str]

### RevocationComment
- **Type**: typing.Optional[str]

### Revoked
- **Type**: typing.Optional[bool]

### RevokedAt
- **Type**: typing.Optional[datetime.datetime]


# RevisionPublishedTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeRevisionRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationComment
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeRevisionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Finalized
- **Type**: <class 'bool'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RevocationComment
- **Type**: <class 'str'>
- **Required**: Yes

### Revoked
- **Type**: <class 'bool'>
- **Required**: Yes

### RevokedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3DataAccessAssetSourceEntryPaginatorTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPrefixes
- **Type**: typing.Optional[typing.List[str]]

### Keys
- **Type**: typing.Optional[typing.List[str]]

### KmsKeysToGrant
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.KmsKeyToGrantTypeDef]]


# S3DataAccessAssetSourceEntryTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]

### Keys
- **Type**: typing.Optional[typing.Sequence[str]]

### KmsKeysToGrant
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.KmsKeyToGrantTypeDef]]


# S3DataAccessAssetTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPrefixes
- **Type**: typing.Optional[typing.List[str]]

### Keys
- **Type**: typing.Optional[typing.List[str]]

### S3AccessPointAlias
- **Type**: typing.Optional[str]

### S3AccessPointArn
- **Type**: typing.Optional[str]

### KmsKeysToGrant
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.KmsKeyToGrantTypeDef]]


# S3DataAccessDetailsTypeDef

### KeyPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]

### Keys
- **Type**: typing.Optional[typing.Sequence[str]]


# S3SnapshotAssetTypeDef

### Size
- **Type**: <class 'float'>
- **Required**: Yes


# SchemaChangeDetailsTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ADD', 'MODIFY', 'REMOVE']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# SchemaChangeRequestDetailsTypeDef

### SchemaChangeAt
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Changes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.SchemaChangeDetailsTypeDef]]


# ScopeDetailsTypeDef

### LakeFormationTagPolicies
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.LakeFormationTagPolicyDetailsTypeDef]]

### RedshiftDataShares
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.RedshiftDataShareDetailsTypeDef]]

### S3DataAccesses
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.S3DataAccessDetailsTypeDef]]


# SendApiAssetRequestRequestTypeDef

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: typing.Optional[str]

### QueryStringParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### RequestHeaders
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Method
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]


# SendApiAssetResponseTypeDef

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SendDataSetNotificationRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['DATA_DELAY', 'DATA_UPDATE', 'DEPRECATION', 'SCHEMA_CHANGE']
- **Required**: Yes

### Scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ScopeDetailsTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### Comment
- **Type**: typing.Optional[str]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.NotificationDetailsTypeDef]


# StartJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# TableLFTagPolicyAndPermissionsPaginatorTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagPaginatorTypeDef]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes


# TableLFTagPolicyAndPermissionsTypeDef

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagTypeDef]
- **Required**: Yes

### Permissions
- **Type**: typing.Sequence[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes


# TableLFTagPolicyPaginatorTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagPaginatorTypeDef]
- **Required**: Yes


# TableLFTagPolicyTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagTypeDef]
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAssetRequestRequestTypeDef

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAssetResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.AssetDetailsTypeDef'>
- **Required**: Yes

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSetRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdateDataSetResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetType
- **Type**: typing.Literal['API_GATEWAY_API', 'LAKE_FORMATION_DATA_PERMISSION', 'REDSHIFT_DATA_SHARE', 'S3_DATA_ACCESS', 'S3_SNAPSHOT']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Origin
- **Type**: typing.Literal['ENTITLED', 'OWNED']
- **Required**: Yes

### OriginDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.OriginDetailsTypeDef'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEventActionRequestRequestTypeDef

### EventActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.ActionTypeDef]


# UpdateEventActionResponseTypeDef

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ActionTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.EventTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRevisionRequestRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### Finalized
- **Type**: typing.Optional[bool]


# UpdateRevisionResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Finalized
- **Type**: <class 'bool'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RevocationComment
- **Type**: <class 'str'>
- **Required**: Yes

### Revoked
- **Type**: <class 'bool'>
- **Required**: Yes

### RevokedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes



# Dataexchange Classes

# AcceptDataGrantRequest

### DataGrantArn
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptDataGrantResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SenderPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiverPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptanceState
- **Type**: typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']
- **Required**: Yes

### AcceptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndsAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GrantDistributionScope
- **Type**: typing.Literal['AWS_ORGANIZATION', 'NONE']
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# Action

### ExportRevisionToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AutoExportRevisionToS3RequestDetails]


# ApiGatewayApiAsset

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


# AssetDestinationEntry

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: typing.Optional[str]


# AssetDetails

### S3SnapshotAsset
- **Type**: <class 'NoneType'>

### RedshiftDataShareAsset
- **Type**: <class 'NoneType'>

### ApiGatewayApiAsset
- **Type**: <class 'NoneType'>

### S3DataAccessAsset
- **Type**: <class 'NoneType'>

### LakeFormationDataPermissionAsset
- **Type**: <class 'NoneType'>


# AssetEntry

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetDetails'>
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


# AssetSourceEntry

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# AutoExportRevisionDestinationEntry

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPattern
- **Type**: typing.Optional[str]


# AutoExportRevisionToS3RequestDetails

### RevisionDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AutoExportRevisionDestinationEntry'>
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportServerSideEncryption]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDataGrantRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### GrantDistributionScope
- **Type**: typing.Literal['AWS_ORGANIZATION', 'NONE']
- **Required**: Yes

### ReceiverPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### EndsAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDataGrantResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SenderPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiverPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptanceState
- **Type**: typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']
- **Required**: Yes

### AcceptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndsAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GrantDistributionScope
- **Type**: typing.Literal['AWS_ORGANIZATION', 'NONE']
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSetRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDataSetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.OriginDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventActionRequest

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Action'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Event'>
- **Required**: Yes


# CreateEventActionResponse

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Action'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Event'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# CreateJobRequest

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.RequestDetails'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET', 'EXPORT_ASSETS_TO_S3', 'EXPORT_ASSET_TO_SIGNED_URL', 'EXPORT_REVISIONS_TO_S3', 'IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY', 'IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES', 'IMPORT_ASSETS_FROM_S3', 'IMPORT_ASSET_FROM_API_GATEWAY_API', 'IMPORT_ASSET_FROM_SIGNED_URL']
- **Required**: Yes


# CreateJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseDetails'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.JobError]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRevisionRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Comment
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateRevisionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# CreateS3DataAccessFromS3BucketRequestDetails

### AssetSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.S3DataAccessAssetSourceEntry, aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.S3DataAccessAssetSourceEntryOutput]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateS3DataAccessFromS3BucketResponseDetails

### AssetSource
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.S3DataAccessAssetSourceEntryOutput'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DataGrantSummaryEntry

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SenderPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiverPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptanceState
- **Type**: typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AcceptedAt
- **Type**: typing.Optional[datetime.datetime]

### EndsAt
- **Type**: typing.Optional[datetime.datetime]


# DataSetEntry

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
- **Type**: <class 'NoneType'>

### SourceId
- **Type**: typing.Optional[str]


# DataUpdateRequestDetails

### DataUpdatedAt
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DatabaseLFTagPolicy

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFTagOutput]
- **Required**: Yes


# DatabaseLFTagPolicyAndPermissions

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFTag]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE']]
- **Required**: Yes


# DatabaseLFTagPolicyAndPermissionsOutput

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFTagOutput]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE']]
- **Required**: Yes


# DeleteAssetRequest

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataGrantRequest

### DataGrantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSetRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventActionRequest

### EventActionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRevisionRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecationRequestDetails

### DeprecationAt
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# Details

### ImportAssetFromSignedUrlJobErrorDetails
- **Type**: <class 'NoneType'>

### ImportAssetsFromS3JobErrorDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetSourceEntry]]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# Event

### RevisionPublished
- **Type**: <class 'NoneType'>


# EventActionEntry

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Action'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Event'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ExportAssetToSignedUrlRequestDetails

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ExportAssetToSignedUrlResponseDetails

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


# ExportAssetsToS3RequestDetails

### AssetDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetDestinationEntry]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportServerSideEncryption]


# ExportAssetsToS3ResponseDetails

### AssetDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetDestinationEntry]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportServerSideEncryption]


# ExportRevisionsToS3RequestDetails

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.RevisionDestinationEntry]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportServerSideEncryption]


# ExportRevisionsToS3ResponseDetails

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.RevisionDestinationEntry]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportServerSideEncryption]

### EventActionArn
- **Type**: typing.Optional[str]


# ExportServerSideEncryption

### Type
- **Type**: typing.Literal['AES256', 'aws:kms']
- **Required**: Yes

### KmsKeyArn
- **Type**: typing.Optional[str]


# GetAssetRequest

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssetResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataGrantRequest

### DataGrantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataGrantResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SenderPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiverPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptanceState
- **Type**: typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']
- **Required**: Yes

### AcceptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndsAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GrantDistributionScope
- **Type**: typing.Literal['AWS_ORGANIZATION', 'NONE']
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceDataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSetRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.OriginDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventActionRequest

### EventActionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventActionResponse

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Action'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Event'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseDetails'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.JobError]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# GetReceivedDataGrantRequest

### DataGrantArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetReceivedDataGrantResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SenderPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiverPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptanceState
- **Type**: typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']
- **Required**: Yes

### AcceptedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndsAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### GrantDistributionScope
- **Type**: typing.Literal['AWS_ORGANIZATION', 'NONE']
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# GetRevisionRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRevisionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# ImportAssetFromApiGatewayApiRequestDetails

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


# ImportAssetFromApiGatewayApiResponseDetails

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


# ImportAssetFromSignedUrlJobErrorDetails

### AssetName
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetFromSignedUrlRequestDetails

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


# ImportAssetFromSignedUrlResponseDetails

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


# ImportAssetsFromLakeFormationTagPolicyRequestDetails

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.DatabaseLFTagPolicyAndPermissions, aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.DatabaseLFTagPolicyAndPermissionsOutput, NoneType]

### Table
- **Type**: typing.Union[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.TableLFTagPolicyAndPermissions, aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.TableLFTagPolicyAndPermissionsOutput, NoneType]


# ImportAssetsFromLakeFormationTagPolicyResponseDetails

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.DatabaseLFTagPolicyAndPermissionsOutput]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.TableLFTagPolicyAndPermissionsOutput]


# ImportAssetsFromRedshiftDataSharesRequestDetails

### AssetSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.RedshiftDataShareAssetSourceEntry]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetsFromRedshiftDataSharesResponseDetails

### AssetSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.RedshiftDataShareAssetSourceEntry]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetsFromS3RequestDetails

### AssetSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetSourceEntry]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# ImportAssetsFromS3ResponseDetails

### AssetSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetSourceEntry]
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# JobEntry

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseDetails'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.JobError]]


# JobError

### Code
- **Type**: typing.Literal['ACCESS_DENIED_EXCEPTION', 'INTERNAL_SERVER_EXCEPTION', 'MALWARE_DETECTED', 'MALWARE_SCAN_ENCRYPTED_FILE', 'RESOURCE_NOT_FOUND_EXCEPTION', 'SERVICE_QUOTA_EXCEEDED_EXCEPTION', 'VALIDATION_EXCEPTION']
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'NoneType'>

### LimitName
- **Type**: typing.Optional[typing.Literal['AWS Lake Formation data permission assets per revision', 'Amazon Redshift datashare assets per revision', 'Amazon S3 data access assets per revision', 'Asset size in GB', 'Assets per revision']]

### LimitValue
- **Type**: typing.Optional[float]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['ASSET', 'DATA_SET', 'REVISION']]


# KmsKeyToGrant

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# LFResourceDetails

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.DatabaseLFTagPolicy]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.TableLFTagPolicy]


# LFTag

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# LFTagOutput

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# LFTagPolicyDetails

### CatalogId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['DATABASE', 'TABLE']
- **Required**: Yes

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFResourceDetails'>
- **Required**: Yes


# LakeFormationDataPermissionAsset

### LakeFormationDataPermissionDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LakeFormationDataPermissionDetails'>
- **Required**: Yes

### LakeFormationDataPermissionType
- **Type**: typing.Literal['LFTagPolicy']
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]


# LakeFormationDataPermissionDetails

### LFTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFTagPolicyDetails]


# LakeFormationTagPolicyDetails

### Database
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]


# ListDataGrantsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataGrantsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.PaginatorConfig]


# ListDataGrantsResponse

### DataGrantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.DataGrantSummaryEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetRevisionsRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetRevisionsRequestPaginate

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.PaginatorConfig]


# ListDataSetRevisionsResponse

### Revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.RevisionEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Origin
- **Type**: typing.Optional[str]


# ListDataSetsRequestPaginate

### Origin
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.PaginatorConfig]


# ListDataSetsResponse

### DataSets
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.DataSetEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventActionsRequest

### EventSourceId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEventActionsRequestPaginate

### EventSourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.PaginatorConfig]


# ListEventActionsResponse

### EventActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.EventActionEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequest

### DataSetId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# ListJobsRequestPaginate

### DataSetId
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.PaginatorConfig]


# ListJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.JobEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReceivedDataGrantsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AcceptanceState
- **Type**: typing.Optional[typing.List[typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']]]


# ListReceivedDataGrantsRequestPaginate

### AcceptanceState
- **Type**: typing.Optional[typing.List[typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.PaginatorConfig]


# ListReceivedDataGrantsResponse

### DataGrantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ReceivedDataGrantSummariesEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRevisionAssetsRequest

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


# ListRevisionAssetsRequestPaginate

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.PaginatorConfig]


# ListRevisionAssetsResponse

### Assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# NotificationDetails

### DataUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.DataUpdateRequestDetails]

### Deprecation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.DeprecationRequestDetails]

### SchemaChange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.SchemaChangeRequestDetails]


# OriginDetails

### ProductId
- **Type**: typing.Optional[str]

### DataGrantId
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ReceivedDataGrantSummariesEntry

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SenderPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### ReceiverPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### AcceptanceState
- **Type**: typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AcceptedAt
- **Type**: typing.Optional[datetime.datetime]

### EndsAt
- **Type**: typing.Optional[datetime.datetime]


# RedshiftDataShareAsset

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftDataShareAssetSourceEntry

### DataShareArn
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftDataShareDetails

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


# RequestDetails

### ExportAssetToSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportAssetToSignedUrlRequestDetails]

### ExportAssetsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportAssetsToS3RequestDetails]

### ExportRevisionsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportRevisionsToS3RequestDetails]

### ImportAssetFromSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetFromSignedUrlRequestDetails]

### ImportAssetsFromS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetsFromS3RequestDetails]

### ImportAssetsFromRedshiftDataShares
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetsFromRedshiftDataSharesRequestDetails]

### ImportAssetFromApiGatewayApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetFromApiGatewayApiRequestDetails]

### CreateS3DataAccessFromS3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.CreateS3DataAccessFromS3BucketRequestDetails]

### ImportAssetsFromLakeFormationTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetsFromLakeFormationTagPolicyRequestDetails]


# ResponseDetails

### ExportAssetToSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportAssetToSignedUrlResponseDetails]

### ExportAssetsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportAssetsToS3ResponseDetails]

### ExportRevisionsToS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ExportRevisionsToS3ResponseDetails]

### ImportAssetFromSignedUrl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetFromSignedUrlResponseDetails]

### ImportAssetsFromS3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetsFromS3ResponseDetails]

### ImportAssetsFromRedshiftDataShares
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetsFromRedshiftDataSharesResponseDetails]

### ImportAssetFromApiGatewayApi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetFromApiGatewayApiResponseDetails]

### CreateS3DataAccessFromS3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.CreateS3DataAccessFromS3BucketResponseDetails]

### ImportAssetsFromLakeFormationTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ImportAssetsFromLakeFormationTagPolicyResponseDetails]


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


# RevisionDestinationEntry

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPattern
- **Type**: typing.Optional[str]


# RevisionEntry

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


# RevisionPublished

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeRevisionRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### RevocationComment
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeRevisionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# S3DataAccessAsset

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.KmsKeyToGrant]]


# S3DataAccessAssetSourceEntry

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPrefixes
- **Type**: typing.Optional[typing.List[str]]

### Keys
- **Type**: typing.Optional[typing.List[str]]

### KmsKeysToGrant
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.KmsKeyToGrant]]


# S3DataAccessAssetSourceEntryOutput

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### KeyPrefixes
- **Type**: typing.Optional[typing.List[str]]

### Keys
- **Type**: typing.Optional[typing.List[str]]

### KmsKeysToGrant
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.KmsKeyToGrant]]


# S3DataAccessDetails

### KeyPrefixes
- **Type**: typing.Optional[typing.List[str]]

### Keys
- **Type**: typing.Optional[typing.List[str]]


# S3SnapshotAsset

### Size
- **Type**: <class 'float'>
- **Required**: Yes


# SchemaChangeDetails

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ADD', 'MODIFY', 'REMOVE']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# SchemaChangeRequestDetails

### SchemaChangeAt
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Changes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.SchemaChangeDetails]]


# ScopeDetails

### LakeFormationTagPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LakeFormationTagPolicyDetails]]

### RedshiftDataShares
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.RedshiftDataShareDetails]]

### S3DataAccesses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.S3DataAccessDetails]]


# SendApiAssetRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### RequestHeaders
- **Type**: typing.Optional[typing.Dict[str, str]]

### Method
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]


# SendApiAssetResponse

### Body
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# SendDataSetNotificationRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['DATA_DELAY', 'DATA_UPDATE', 'DEPRECATION', 'SCHEMA_CHANGE']
- **Required**: Yes

### Scope
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ScopeDetails]

### ClientToken
- **Type**: typing.Optional[str]

### Comment
- **Type**: typing.Optional[str]

### Details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.NotificationDetails]


# StartJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# TableLFTagPolicy

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFTagOutput]
- **Required**: Yes


# TableLFTagPolicyAndPermissions

### Expression
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFTag, aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFTagOutput]]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes


# TableLFTagPolicyAndPermissionsOutput

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.LFTagOutput]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAssetRequest

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


# UpdateAssetResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AssetDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.AssetDetails'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSetRequest

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdateDataSetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.OriginDetails'>
- **Required**: Yes

### SourceId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEventActionRequest

### EventActionId
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'NoneType'>


# UpdateEventActionResponse

### Action
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Action'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Event
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.Event'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRevisionRequest

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


# UpdateRevisionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange.dataexchange_classes.ResponseMetadata'>
- **Required**: Yes



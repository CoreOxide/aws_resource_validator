# Dataexchange Classes

# AcceptDataGrantRequestTypeDef

### DataGrantArn
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptDataGrantResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

# CancelJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateDataGrantRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TimestampTypeDef]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDataGrantResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSetRequestTypeDef

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


# CreateEventActionRequestTypeDef

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


# CreateRevisionRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.S3DataAccessAssetSourceEntryUnionTypeDef'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateS3DataAccessFromS3BucketResponseDetailsTypeDef

### AssetSource
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.S3DataAccessAssetSourceEntryOutputTypeDef'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DataGrantSummaryEntryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TimestampTypeDef]


# DatabaseLFTagPolicyAndPermissionsOutputTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagOutputTypeDef]
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


# DatabaseLFTagPolicyAndPermissionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatabaseLFTagPolicyTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagOutputTypeDef]
- **Required**: Yes


# DeleteAssetRequestTypeDef

### AssetId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataGrantRequestTypeDef

### DataGrantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSetRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventActionRequestTypeDef

### EventActionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRevisionRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecationRequestDetailsTypeDef

### DeprecationAt
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.TimestampTypeDef'>
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAssetRequestTypeDef

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


# GetDataGrantRequestTypeDef

### DataGrantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataGrantResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSetRequestTypeDef

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


# GetEventActionRequestTypeDef

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


# GetJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetReceivedDataGrantRequestTypeDef

### DataGrantArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetReceivedDataGrantResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRevisionRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DatabaseLFTagPolicyAndPermissionsUnionTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TableLFTagPolicyAndPermissionsUnionTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DatabaseLFTagPolicyAndPermissionsOutputTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TableLFTagPolicyAndPermissionsOutputTypeDef]


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


# JobEntryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# LFResourceDetailsTypeDef

### Database
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.DatabaseLFTagPolicyTypeDef]

### Table
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.TableLFTagPolicyTypeDef]


# LFTagOutputTypeDef

### TagKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
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


# LFTagUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# LakeFormationDataPermissionDetailsTypeDef

### LFTagPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagPolicyDetailsTypeDef]


# LakeFormationTagPolicyDetailsTypeDef

### Database
- **Type**: typing.Optional[str]

### Table
- **Type**: typing.Optional[str]


# ListDataGrantsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListDataGrantsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataGrantsResponseTypeDef

### DataGrantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.DataGrantSummaryEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetRevisionsRequestPaginateTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListDataSetRevisionsRequestTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetRevisionsResponseTypeDef

### Revisions
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.RevisionEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSetsRequestPaginateTypeDef

### Origin
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListDataSetsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventActionsRequestPaginateTypeDef

### EventSourceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListEventActionsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListJobsRequestPaginateTypeDef

### DataSetId
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListJobsRequestTypeDef

### DataSetId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# ListJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.JobEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListReceivedDataGrantsRequestPaginateTypeDef

### AcceptanceState
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListReceivedDataGrantsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AcceptanceState
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACCEPTED', 'PENDING_RECEIVER_ACCEPTANCE']]]


# ListReceivedDataGrantsResponseTypeDef

### DataGrantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.ReceivedDataGrantSummariesEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRevisionAssetsRequestPaginateTypeDef

### DataSetId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.dataexchange_classes.PaginatorConfigTypeDef]


# ListRevisionAssetsRequestTypeDef

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


# ListRevisionAssetsResponseTypeDef

### Assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.AssetEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.ResponseMetadataTypeDef'>
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

### DataGrantId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ReceivedDataGrantSummariesEntryTypeDef

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


# RevokeRevisionRequestTypeDef

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


# S3DataAccessAssetSourceEntryOutputTypeDef

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


# S3DataAccessAssetSourceEntryUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SchemaChangeRequestDetailsTypeDef

### SchemaChangeAt
- **Type**: <class 'aws_resource_validator.pydantic_models.dataexchange_classes.TimestampTypeDef'>
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


# SendApiAssetRequestTypeDef

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


# StartJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# TableLFTagPolicyAndPermissionsOutputTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagOutputTypeDef]
- **Required**: Yes

### Permissions
- **Type**: typing.List[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes


# TableLFTagPolicyAndPermissionsTypeDef

### Expression
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagUnionTypeDef]
- **Required**: Yes

### Permissions
- **Type**: typing.Sequence[typing.Literal['DESCRIBE', 'SELECT']]
- **Required**: Yes


# TableLFTagPolicyAndPermissionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TableLFTagPolicyTypeDef

### Expression
- **Type**: typing.List[aws_resource_validator.pydantic_models.dataexchange_classes.LFTagOutputTypeDef]
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
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


# UpdateAssetRequestTypeDef

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


# UpdateDataSetRequestTypeDef

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


# UpdateEventActionRequestTypeDef

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


# UpdateRevisionRequestTypeDef

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



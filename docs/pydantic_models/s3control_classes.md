# S3Control Classes

# AbortIncompleteMultipartUploadTypeDef

### DaysAfterInitiation
- **Type**: typing.Optional[int]


# AccessControlTranslationTypeDef

### Owner
- **Type**: typing.Literal['Destination']
- **Required**: Yes


# AccessGrantsLocationConfigurationTypeDef

### S3SubPrefix
- **Type**: typing.Optional[str]


# AccessPointTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkOrigin
- **Type**: typing.Literal['Internet', 'VPC']
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.VpcConfigurationTypeDef]

### AccessPointArn
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### BucketAccountId
- **Type**: typing.Optional[str]


# AccountLevelTypeDef

### BucketLevel
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.BucketLevelTypeDef'>
- **Required**: Yes

### ActivityMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ActivityMetricsTypeDef]

### AdvancedCostOptimizationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AdvancedCostOptimizationMetricsTypeDef]

### AdvancedDataProtectionMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AdvancedDataProtectionMetricsTypeDef]

### DetailedStatusCodesMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.DetailedStatusCodesMetricsTypeDef]

### StorageLensGroupLevel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupLevelTypeDef]


# ActivityMetricsTypeDef

### IsEnabled
- **Type**: typing.Optional[bool]


# AdvancedCostOptimizationMetricsTypeDef

### IsEnabled
- **Type**: typing.Optional[bool]


# AdvancedDataProtectionMetricsTypeDef

### IsEnabled
- **Type**: typing.Optional[bool]


# AssociateAccessGrantsIdentityCenterRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterArn
- **Type**: <class 'str'>
- **Required**: Yes


# AsyncErrorDetailsTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]

### Resource
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]


# AsyncOperationTypeDef

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Operation
- **Type**: typing.Optional[typing.Literal['CreateMultiRegionAccessPoint', 'DeleteMultiRegionAccessPoint', 'PutMultiRegionAccessPointPolicy']]

### RequestTokenARN
- **Type**: typing.Optional[str]

### RequestParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AsyncRequestParametersTypeDef]

### RequestStatus
- **Type**: typing.Optional[str]

### ResponseDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AsyncResponseDetailsTypeDef]


# AsyncRequestParametersTypeDef

### CreateMultiRegionAccessPointRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.CreateMultiRegionAccessPointInputTypeDef]

### DeleteMultiRegionAccessPointRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.DeleteMultiRegionAccessPointInputTypeDef]

### PutMultiRegionAccessPointPolicyRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PutMultiRegionAccessPointPolicyInputTypeDef]


# AsyncResponseDetailsTypeDef

### MultiRegionAccessPointDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointsAsyncResponseTypeDef]

### ErrorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AsyncErrorDetailsTypeDef]


# AwsLambdaTransformationTypeDef

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionPayload
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BucketLevelTypeDef

### ActivityMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ActivityMetricsTypeDef]

### PrefixLevel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PrefixLevelTypeDef]

### AdvancedCostOptimizationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AdvancedCostOptimizationMetricsTypeDef]

### AdvancedDataProtectionMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AdvancedDataProtectionMetricsTypeDef]

### DetailedStatusCodesMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.DetailedStatusCodesMetricsTypeDef]


# CloudWatchMetricsTypeDef

### IsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# CreateAccessGrantRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### Grantee
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.GranteeTypeDef'>
- **Required**: Yes

### Permission
- **Type**: typing.Literal['READ', 'READWRITE', 'WRITE']
- **Required**: Yes

### AccessGrantsLocationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AccessGrantsLocationConfigurationTypeDef]

### ApplicationArn
- **Type**: typing.Optional[str]

### S3PrefixType
- **Type**: typing.Optional[typing.Literal['Object']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.TagTypeDef]]


# CreateAccessGrantResultTypeDef

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Grantee
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.GranteeTypeDef'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AccessGrantsLocationConfigurationTypeDef'>
- **Required**: Yes

### Permission
- **Type**: typing.Literal['READ', 'READWRITE', 'WRITE']
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantScope
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccessGrantsInstanceRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.TagTypeDef]]


# CreateAccessGrantsInstanceResultTypeDef

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccessGrantsLocationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### LocationScope
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.TagTypeDef]]


# CreateAccessGrantsLocationResultTypeDef

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationScope
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccessPointForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaConfigurationTypeDef'>
- **Required**: Yes


# CreateAccessPointForObjectLambdaResultTypeDef

### ObjectLambdaAccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaAccessPointAliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccessPointRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.VpcConfigurationTypeDef]

### PublicAccessBlockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfigurationTypeDef]

### BucketAccountId
- **Type**: typing.Optional[str]


# CreateAccessPointResultTypeDef

### AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBucketConfigurationTypeDef

### LocationConstraint
- **Type**: typing.Optional[typing.Literal['EU', 'ap-northeast-1', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'cn-north-1', 'eu-central-1', 'eu-west-1', 'sa-east-1', 'us-west-1', 'us-west-2']]


# CreateBucketRequestRequestTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'private', 'public-read', 'public-read-write']]

### CreateBucketConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.CreateBucketConfigurationTypeDef]

### GrantFullControl
- **Type**: typing.Optional[str]

### GrantRead
- **Type**: typing.Optional[str]

### GrantReadACP
- **Type**: typing.Optional[str]

### GrantWrite
- **Type**: typing.Optional[str]

### GrantWriteACP
- **Type**: typing.Optional[str]

### ObjectLockEnabledForBucket
- **Type**: typing.Optional[bool]

### OutpostId
- **Type**: typing.Optional[str]


# CreateBucketResultTypeDef

### Location
- **Type**: <class 'str'>
- **Required**: Yes

### BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateJobRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobOperationTypeDef'>
- **Required**: Yes

### Report
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobReportTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfirmationRequired
- **Type**: typing.Optional[bool]

### Manifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestTypeDef]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]]

### ManifestGenerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestGeneratorTypeDef]


# CreateJobResultTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMultiRegionAccessPointInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Regions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.RegionTypeDef]
- **Required**: Yes

### PublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfigurationTypeDef]


# CreateMultiRegionAccessPointRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.CreateMultiRegionAccessPointInputTypeDef'>
- **Required**: Yes


# CreateMultiRegionAccessPointResultTypeDef

### RequestTokenARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStorageLensGroupRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.TagTypeDef]]


# CredentialsTypeDef

### AccessKeyId
- **Type**: typing.Optional[str]

### SecretAccessKey
- **Type**: typing.Optional[str]

### SessionToken
- **Type**: typing.Optional[str]

### Expiration
- **Type**: typing.Optional[datetime.datetime]


# DeleteAccessGrantRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessGrantsInstanceRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessGrantsInstanceResourcePolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessGrantsLocationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointPolicyForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointPolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketLifecycleConfigurationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketPolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketReplicationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBucketTaggingRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteJobTaggingRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMarkerReplicationTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# DeleteMultiRegionAccessPointInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMultiRegionAccessPointRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.DeleteMultiRegionAccessPointInputTypeDef'>
- **Required**: Yes


# DeleteMultiRegionAccessPointResultTypeDef

### RequestTokenARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePublicAccessBlockRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageLensConfigurationRequestRequestTypeDef

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageLensConfigurationTaggingRequestRequestTypeDef

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageLensGroupRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeJobResultTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobDescriptorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMultiRegionAccessPointOperationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestTokenARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMultiRegionAccessPointOperationResultTypeDef

### AsyncOperation
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AsyncOperationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: typing.Optional[str]

### ReplicationTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationTimeTypeDef]

### AccessControlTranslation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AccessControlTranslationTypeDef]

### EncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.EncryptionConfigurationTypeDef]

### Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MetricsTypeDef]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'OUTPOSTS', 'REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]


# DetailedStatusCodesMetricsTypeDef

### IsEnabled
- **Type**: typing.Optional[bool]


# DissociateAccessGrantsIdentityCenterRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionConfigurationTypeDef

### ReplicaKmsKeyID
- **Type**: typing.Optional[str]


# EstablishedMultiRegionAccessPointPolicyTypeDef

### Policy
- **Type**: typing.Optional[str]


# ExcludeTypeDef

### Buckets
- **Type**: typing.Optional[typing.List[str]]

### Regions
- **Type**: typing.Optional[typing.List[str]]


# ExistingObjectReplicationTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# GeneratedManifestEncryptionTypeDef

### SSES3
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### SSEKMS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.SSEKMSEncryptionTypeDef]


# GetAccessGrantRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantResultTypeDef

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantArn
- **Type**: <class 'str'>
- **Required**: Yes

### Grantee
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.GranteeTypeDef'>
- **Required**: Yes

### Permission
- **Type**: typing.Literal['READ', 'READWRITE', 'WRITE']
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AccessGrantsLocationConfigurationTypeDef'>
- **Required**: Yes

### GrantScope
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessGrantsInstanceForPrefixRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantsInstanceForPrefixResultTypeDef

### AccessGrantsInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessGrantsInstanceRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantsInstanceResourcePolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantsInstanceResourcePolicyResultTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### Organization
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessGrantsInstanceResultTypeDef

### AccessGrantsInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityCenterArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessGrantsLocationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessGrantsLocationResultTypeDef

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationScope
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessPointConfigurationForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointConfigurationForObjectLambdaResultTypeDef

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessPointForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointForObjectLambdaResultTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PublicAccessBlockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfigurationTypeDef'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Alias
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaAccessPointAliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessPointPolicyForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointPolicyForObjectLambdaResultTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessPointPolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointPolicyResultTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessPointPolicyStatusForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointPolicyStatusForObjectLambdaResultTypeDef

### PolicyStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PolicyStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessPointPolicyStatusRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointPolicyStatusResultTypeDef

### PolicyStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PolicyStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessPointRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessPointResultTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkOrigin
- **Type**: typing.Literal['Internet', 'VPC']
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.VpcConfigurationTypeDef'>
- **Required**: Yes

### PublicAccessBlockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfigurationTypeDef'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### BucketAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketLifecycleConfigurationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketLifecycleConfigurationResultTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketPolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketPolicyResultTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketReplicationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketReplicationResultTypeDef

### ReplicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ReplicationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketResultTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### PublicAccessBlockEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketTaggingRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketTaggingResultTypeDef

### TagSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketVersioningRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes


# GetBucketVersioningResultTypeDef

### Status
- **Type**: typing.Literal['Enabled', 'Suspended']
- **Required**: Yes

### MFADelete
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataAccessRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### Permission
- **Type**: typing.Literal['READ', 'READWRITE', 'WRITE']
- **Required**: Yes

### DurationSeconds
- **Type**: typing.Optional[int]

### Privilege
- **Type**: typing.Optional[typing.Literal['Default', 'Minimal']]

### TargetType
- **Type**: typing.Optional[typing.Literal['Object']]


# GetDataAccessResultTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.CredentialsTypeDef'>
- **Required**: Yes

### MatchedGrantTarget
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobTaggingRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobTaggingResultTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMultiRegionAccessPointPolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionAccessPointPolicyResultTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointPolicyDocumentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMultiRegionAccessPointPolicyStatusRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionAccessPointPolicyStatusResultTypeDef

### Established
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PolicyStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMultiRegionAccessPointRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionAccessPointResultTypeDef

### AccessPoint
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointReportTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMultiRegionAccessPointRoutesRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Mrap
- **Type**: <class 'str'>
- **Required**: Yes


# GetMultiRegionAccessPointRoutesResultTypeDef

### Mrap
- **Type**: <class 'str'>
- **Required**: Yes

### Routes
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointRouteTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPublicAccessBlockOutputTypeDef

### PublicAccessBlockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPublicAccessBlockRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageLensConfigurationRequestRequestTypeDef

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageLensConfigurationResultTypeDef

### StorageLensConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStorageLensConfigurationTaggingRequestRequestTypeDef

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageLensConfigurationTaggingResultTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.StorageLensTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStorageLensGroupRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageLensGroupResultTypeDef

### StorageLensGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GranteeTypeDef

### GranteeType
- **Type**: typing.Optional[typing.Literal['DIRECTORY_GROUP', 'DIRECTORY_USER', 'IAM']]

### GranteeIdentifier
- **Type**: typing.Optional[str]


# IncludeTypeDef

### Buckets
- **Type**: typing.Optional[typing.List[str]]

### Regions
- **Type**: typing.Optional[typing.List[str]]


# JobDescriptorTypeDef

### JobId
- **Type**: typing.Optional[str]

### ConfirmationRequired
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Cancelled', 'Cancelling', 'Complete', 'Completing', 'Failed', 'Failing', 'New', 'Paused', 'Pausing', 'Preparing', 'Ready', 'Suspended']]

### Manifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestTypeDef]

### Operation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobOperationTypeDef]

### Priority
- **Type**: typing.Optional[int]

### ProgressSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobProgressSummaryTypeDef]

### StatusUpdateReason
- **Type**: typing.Optional[str]

### FailureReasons
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.JobFailureTypeDef]]

### Report
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobReportTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TerminationDate
- **Type**: typing.Optional[datetime.datetime]

### RoleArn
- **Type**: typing.Optional[str]

### SuspendedDate
- **Type**: typing.Optional[datetime.datetime]

### SuspendedCause
- **Type**: typing.Optional[str]

### ManifestGenerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestGeneratorTypeDef]

### GeneratedManifestDescriptor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3GeneratedManifestDescriptorTypeDef]


# JobFailureTypeDef

### FailureCode
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# JobListDescriptorTypeDef

### JobId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[typing.Literal['LambdaInvoke', 'S3DeleteObjectTagging', 'S3InitiateRestoreObject', 'S3PutObjectAcl', 'S3PutObjectCopy', 'S3PutObjectLegalHold', 'S3PutObjectRetention', 'S3PutObjectTagging', 'S3ReplicateObject']]

### Priority
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Cancelled', 'Cancelling', 'Complete', 'Completing', 'Failed', 'Failing', 'New', 'Paused', 'Pausing', 'Preparing', 'Ready', 'Suspended']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### TerminationDate
- **Type**: typing.Optional[datetime.datetime]

### ProgressSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobProgressSummaryTypeDef]


# JobManifestGeneratorFilterTypeDef

### EligibleForReplication
- **Type**: typing.Optional[bool]

### CreatedAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreatedBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ObjectReplicationStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['COMPLETED', 'FAILED', 'NONE', 'REPLICA']]]

### KeyNameConstraint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.KeyNameConstraintTypeDef]

### ObjectSizeGreaterThanBytes
- **Type**: typing.Optional[int]

### ObjectSizeLessThanBytes
- **Type**: typing.Optional[int]

### MatchAnyStorageClass
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD', 'STANDARD_IA']]]


# JobManifestGeneratorTypeDef

### S3JobManifestGenerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3JobManifestGeneratorTypeDef]


# JobManifestLocationTypeDef

### ObjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectVersionId
- **Type**: typing.Optional[str]


# JobManifestSpecTypeDef

### Format
- **Type**: typing.Literal['S3BatchOperations_CSV_20180820', 'S3InventoryReport_CSV_20161130']
- **Required**: Yes

### Fields
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Bucket', 'Ignore', 'Key', 'VersionId']]]


# JobManifestTypeDef

### Spec
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobManifestSpecTypeDef'>
- **Required**: Yes

### Location
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.JobManifestLocationTypeDef'>
- **Required**: Yes


# JobOperationTypeDef

### LambdaInvoke
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LambdaInvokeOperationTypeDef]

### S3PutObjectCopy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3CopyObjectOperationTypeDef]

### S3PutObjectAcl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectAclOperationTypeDef]

### S3PutObjectTagging
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectTaggingOperationTypeDef]

### S3DeleteObjectTagging
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### S3InitiateRestoreObject
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3InitiateRestoreObjectOperationTypeDef]

### S3PutObjectLegalHold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectLegalHoldOperationTypeDef]

### S3PutObjectRetention
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3SetObjectRetentionOperationTypeDef]

### S3ReplicateObject
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# JobProgressSummaryTypeDef

### TotalNumberOfTasks
- **Type**: typing.Optional[int]

### NumberOfTasksSucceeded
- **Type**: typing.Optional[int]

### NumberOfTasksFailed
- **Type**: typing.Optional[int]

### Timers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobTimersTypeDef]


# JobReportTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Bucket
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[typing.Literal['Report_CSV_20180820']]

### Prefix
- **Type**: typing.Optional[str]

### ReportScope
- **Type**: typing.Optional[typing.Literal['AllTasks', 'FailedTasksOnly']]


# JobTimersTypeDef

### ElapsedTimeInActiveSeconds
- **Type**: typing.Optional[int]


# KeyNameConstraintTypeDef

### MatchAnyPrefix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySubstring
- **Type**: typing.Optional[typing.Sequence[str]]


# LambdaInvokeOperationTypeDef

### FunctionArn
- **Type**: typing.Optional[str]

### InvocationSchemaVersion
- **Type**: typing.Optional[str]

### UserArguments
- **Type**: typing.Optional[typing.Mapping[str, str]]


# LifecycleConfigurationTypeDef

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleTypeDef]]


# LifecycleExpirationTypeDef

### Date
- **Type**: typing.Optional[datetime.datetime]

### Days
- **Type**: typing.Optional[int]

### ExpiredObjectDeleteMarker
- **Type**: typing.Optional[bool]


# LifecycleRuleAndOperatorTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]]

### ObjectSizeGreaterThan
- **Type**: typing.Optional[int]

### ObjectSizeLessThan
- **Type**: typing.Optional[int]


# LifecycleRuleFilterTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleAndOperatorTypeDef]

### ObjectSizeGreaterThan
- **Type**: typing.Optional[int]

### ObjectSizeLessThan
- **Type**: typing.Optional[int]


# LifecycleRuleTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Expiration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleExpirationTypeDef]

### ID
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleRuleFilterTypeDef]

### Transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.TransitionTypeDef]]

### NoncurrentVersionTransitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.NoncurrentVersionTransitionTypeDef]]

### NoncurrentVersionExpiration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.NoncurrentVersionExpirationTypeDef]

### AbortIncompleteMultipartUpload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AbortIncompleteMultipartUploadTypeDef]


# ListAccessGrantEntryTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### AccessGrantId
- **Type**: typing.Optional[str]

### AccessGrantArn
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.GranteeTypeDef]

### Permission
- **Type**: typing.Optional[typing.Literal['READ', 'READWRITE', 'WRITE']]

### AccessGrantsLocationId
- **Type**: typing.Optional[str]

### AccessGrantsLocationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AccessGrantsLocationConfigurationTypeDef]

### GrantScope
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ListAccessGrantsInstanceEntryTypeDef

### AccessGrantsInstanceId
- **Type**: typing.Optional[str]

### AccessGrantsInstanceArn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### IdentityCenterArn
- **Type**: typing.Optional[str]


# ListAccessGrantsInstancesRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessGrantsInstancesResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsInstancesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListAccessGrantsInstanceEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccessGrantsLocationsEntryTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### AccessGrantsLocationId
- **Type**: typing.Optional[str]

### AccessGrantsLocationArn
- **Type**: typing.Optional[str]

### LocationScope
- **Type**: typing.Optional[str]

### IAMRoleArn
- **Type**: typing.Optional[str]


# ListAccessGrantsLocationsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### LocationScope
- **Type**: typing.Optional[str]


# ListAccessGrantsLocationsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListAccessGrantsLocationsEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccessGrantsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### GranteeType
- **Type**: typing.Optional[typing.Literal['DIRECTORY_GROUP', 'DIRECTORY_USER', 'IAM']]

### GranteeIdentifier
- **Type**: typing.Optional[str]

### Permission
- **Type**: typing.Optional[typing.Literal['READ', 'READWRITE', 'WRITE']]

### GrantScope
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ListAccessGrantsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListAccessGrantEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccessPointsForObjectLambdaRequestListAccessPointsForObjectLambdaPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PaginatorConfigTypeDef]


# ListAccessPointsForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessPointsForObjectLambdaResultTypeDef

### ObjectLambdaAccessPointList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaAccessPointTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccessPointsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessPointsResultTypeDef

### AccessPointList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.AccessPointTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Active', 'Cancelled', 'Cancelling', 'Complete', 'Completing', 'Failed', 'Failing', 'New', 'Paused', 'Pausing', 'Preparing', 'Ready', 'Suspended']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListJobsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.JobListDescriptorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMultiRegionAccessPointsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMultiRegionAccessPointsResultTypeDef

### AccessPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointReportTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRegionalBucketsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### OutpostId
- **Type**: typing.Optional[str]


# ListRegionalBucketsResultTypeDef

### RegionalBucketList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.RegionalBucketTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStorageLensConfigurationEntryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensArn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes

### IsEnabled
- **Type**: typing.Optional[bool]


# ListStorageLensConfigurationsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStorageLensConfigurationsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListStorageLensConfigurationEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStorageLensGroupEntryTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### HomeRegion
- **Type**: <class 'str'>
- **Required**: Yes


# ListStorageLensGroupsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStorageLensGroupsResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensGroupList
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ListStorageLensGroupEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResultTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MatchObjectAgeTypeDef

### DaysGreaterThan
- **Type**: typing.Optional[int]

### DaysLessThan
- **Type**: typing.Optional[int]


# MatchObjectSizeTypeDef

### BytesGreaterThan
- **Type**: typing.Optional[int]

### BytesLessThan
- **Type**: typing.Optional[int]


# MetricsTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### EventThreshold
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationTimeValueTypeDef]


# MultiRegionAccessPointPolicyDocumentTypeDef

### Established
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.EstablishedMultiRegionAccessPointPolicyTypeDef]

### Proposed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ProposedMultiRegionAccessPointPolicyTypeDef]


# MultiRegionAccessPointRegionalResponseTypeDef

### Name
- **Type**: typing.Optional[str]

### RequestStatus
- **Type**: typing.Optional[str]


# MultiRegionAccessPointReportTypeDef

### Name
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### PublicAccessBlock
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfigurationTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'INCONSISTENT_ACROSS_REGIONS', 'PARTIALLY_CREATED', 'PARTIALLY_DELETED', 'READY']]

### Regions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.RegionReportTypeDef]]


# MultiRegionAccessPointRouteTypeDef

### TrafficDialPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### Bucket
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]


# MultiRegionAccessPointsAsyncResponseTypeDef

### Regions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointRegionalResponseTypeDef]]


# NoncurrentVersionExpirationTypeDef

### NoncurrentDays
- **Type**: typing.Optional[int]

### NewerNoncurrentVersions
- **Type**: typing.Optional[int]


# NoncurrentVersionTransitionTypeDef

### NoncurrentDays
- **Type**: typing.Optional[int]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD_IA']]


# ObjectLambdaAccessPointAliasTypeDef

### Value
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['PROVISIONING', 'READY']]


# ObjectLambdaAccessPointTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectLambdaAccessPointArn
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaAccessPointAliasTypeDef]


# ObjectLambdaConfigurationTypeDef

### SupportingAccessPoint
- **Type**: <class 'str'>
- **Required**: Yes

### TransformationConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaTransformationConfigurationTypeDef]
- **Required**: Yes

### CloudWatchMetricsEnabled
- **Type**: typing.Optional[bool]

### AllowedFeatures
- **Type**: typing.Optional[typing.Sequence[typing.Literal['GetObject-PartNumber', 'GetObject-Range', 'HeadObject-PartNumber', 'HeadObject-Range']]]


# ObjectLambdaContentTransformationTypeDef

### AwsLambda
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.AwsLambdaTransformationTypeDef]


# ObjectLambdaTransformationConfigurationTypeDef

### Actions
- **Type**: typing.Sequence[typing.Literal['GetObject', 'HeadObject', 'ListObjects', 'ListObjectsV2']]
- **Required**: Yes

### ContentTransformation
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaContentTransformationTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolicyStatusTypeDef

### IsPublic
- **Type**: typing.Optional[bool]


# PrefixLevelStorageMetricsTypeDef

### IsEnabled
- **Type**: typing.Optional[bool]

### SelectionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.SelectionCriteriaTypeDef]


# PrefixLevelTypeDef

### StorageMetrics
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PrefixLevelStorageMetricsTypeDef'>
- **Required**: Yes


# ProposedMultiRegionAccessPointPolicyTypeDef

### Policy
- **Type**: typing.Optional[str]


# PublicAccessBlockConfigurationTypeDef

### BlockPublicAcls
- **Type**: typing.Optional[bool]

### IgnorePublicAcls
- **Type**: typing.Optional[bool]

### BlockPublicPolicy
- **Type**: typing.Optional[bool]

### RestrictPublicBuckets
- **Type**: typing.Optional[bool]


# PutAccessGrantsInstanceResourcePolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### Organization
- **Type**: typing.Optional[str]


# PutAccessGrantsInstanceResourcePolicyResultTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### Organization
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutAccessPointConfigurationForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ObjectLambdaConfigurationTypeDef'>
- **Required**: Yes


# PutAccessPointPolicyForObjectLambdaRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutAccessPointPolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutBucketLifecycleConfigurationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### LifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.LifecycleConfigurationTypeDef]


# PutBucketPolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ConfirmRemoveSelfBucketAccess
- **Type**: typing.Optional[bool]


# PutBucketReplicationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ReplicationConfigurationTypeDef'>
- **Required**: Yes


# PutBucketTaggingRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Tagging
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.TaggingTypeDef'>
- **Required**: Yes


# PutBucketVersioningRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### VersioningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.VersioningConfigurationTypeDef'>
- **Required**: Yes

### MFA
- **Type**: typing.Optional[str]


# PutJobTaggingRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]
- **Required**: Yes


# PutMultiRegionAccessPointPolicyInputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutMultiRegionAccessPointPolicyRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Details
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PutMultiRegionAccessPointPolicyInputTypeDef'>
- **Required**: Yes


# PutMultiRegionAccessPointPolicyResultTypeDef

### RequestTokenARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutPublicAccessBlockRequestRequestTypeDef

### PublicAccessBlockConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.PublicAccessBlockConfigurationTypeDef'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# PutStorageLensConfigurationRequestRequestTypeDef

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensConfigurationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.StorageLensTagTypeDef]]


# PutStorageLensConfigurationTaggingRequestRequestTypeDef

### ConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.StorageLensTagTypeDef]
- **Required**: Yes


# RegionReportTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### BucketAccountId
- **Type**: typing.Optional[str]


# RegionTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### BucketAccountId
- **Type**: typing.Optional[str]


# RegionalBucketTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### PublicAccessBlockEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### CreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BucketArn
- **Type**: typing.Optional[str]

### OutpostId
- **Type**: typing.Optional[str]


# ReplicaModificationsTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# ReplicationConfigurationTypeDef

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRuleTypeDef]
- **Required**: Yes


# ReplicationRuleAndOperatorTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]]


# ReplicationRuleFilterTypeDef

### Prefix
- **Type**: typing.Optional[str]

### Tag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRuleAndOperatorTypeDef]


# ReplicationRuleTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.DestinationTypeDef'>
- **Required**: Yes

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ID
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### Prefix
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicationRuleFilterTypeDef]

### SourceSelectionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.SourceSelectionCriteriaTypeDef]

### ExistingObjectReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ExistingObjectReplicationTypeDef]

### DeleteMarkerReplication
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.DeleteMarkerReplicationTypeDef]


# ReplicationTimeTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### Time
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ReplicationTimeValueTypeDef'>
- **Required**: Yes


# ReplicationTimeValueTypeDef

### Minutes
- **Type**: typing.Optional[int]


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


# S3AccessControlListTypeDef

### Owner
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.S3ObjectOwnerTypeDef'>
- **Required**: Yes

### Grants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3GrantTypeDef]]


# S3AccessControlPolicyTypeDef

### AccessControlList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3AccessControlListTypeDef]

### CannedAccessControlList
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]


# S3BucketDestinationTypeDef

### Format
- **Type**: typing.Literal['CSV', 'Parquet']
- **Required**: Yes

### OutputSchemaVersion
- **Type**: typing.Literal['V_1']
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Prefix
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensDataExportEncryptionTypeDef]


# S3CopyObjectOperationTypeDef

### TargetResource
- **Type**: typing.Optional[str]

### CannedAccessControlList
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### AccessControlGrants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3GrantTypeDef]]

### MetadataDirective
- **Type**: typing.Optional[typing.Literal['COPY', 'REPLACE']]

### ModifiedSinceConstraint
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NewObjectMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3ObjectMetadataTypeDef]

### NewObjectTagging
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]]

### RedirectLocation
- **Type**: typing.Optional[str]

### RequesterPays
- **Type**: typing.Optional[bool]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD', 'STANDARD_IA']]

### UnModifiedSinceConstraint
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SSEAwsKmsKeyId
- **Type**: typing.Optional[str]

### TargetKeyPrefix
- **Type**: typing.Optional[str]

### ObjectLockLegalHoldStatus
- **Type**: typing.Optional[typing.Literal['OFF', 'ON']]

### ObjectLockMode
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'GOVERNANCE']]

### ObjectLockRetainUntilDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BucketKeyEnabled
- **Type**: typing.Optional[bool]

### ChecksumAlgorithm
- **Type**: typing.Optional[typing.Literal['CRC32', 'CRC32C', 'SHA1', 'SHA256']]


# S3GeneratedManifestDescriptorTypeDef

### Format
- **Type**: typing.Optional[typing.Literal['S3InventoryReport_CSV_20211130']]

### Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestLocationTypeDef]


# S3GrantTypeDef

### Grantee
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3GranteeTypeDef]

### Permission
- **Type**: typing.Optional[typing.Literal['FULL_CONTROL', 'READ', 'READ_ACP', 'WRITE', 'WRITE_ACP']]


# S3GranteeTypeDef

### TypeIdentifier
- **Type**: typing.Optional[typing.Literal['emailAddress', 'id', 'uri']]

### Identifier
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# S3InitiateRestoreObjectOperationTypeDef

### ExpirationInDays
- **Type**: typing.Optional[int]

### GlacierJobTier
- **Type**: typing.Optional[typing.Literal['BULK', 'STANDARD']]


# S3JobManifestGeneratorTypeDef

### SourceBucket
- **Type**: <class 'str'>
- **Required**: Yes

### EnableManifestOutput
- **Type**: <class 'bool'>
- **Required**: Yes

### ExpectedBucketOwner
- **Type**: typing.Optional[str]

### ManifestOutputLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3ManifestOutputLocationTypeDef]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.JobManifestGeneratorFilterTypeDef]


# S3ManifestOutputLocationTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestFormat
- **Type**: typing.Literal['S3InventoryReport_CSV_20211130']
- **Required**: Yes

### ExpectedManifestBucketOwner
- **Type**: typing.Optional[str]

### ManifestPrefix
- **Type**: typing.Optional[str]

### ManifestEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.GeneratedManifestEncryptionTypeDef]


# S3ObjectLockLegalHoldTypeDef

### Status
- **Type**: typing.Literal['OFF', 'ON']
- **Required**: Yes


# S3ObjectMetadataTypeDef

### CacheControl
- **Type**: typing.Optional[str]

### ContentDisposition
- **Type**: typing.Optional[str]

### ContentEncoding
- **Type**: typing.Optional[str]

### ContentLanguage
- **Type**: typing.Optional[str]

### UserMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ContentLength
- **Type**: typing.Optional[int]

### ContentMD5
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### HttpExpiresDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### RequesterCharged
- **Type**: typing.Optional[bool]

### SSEAlgorithm
- **Type**: typing.Optional[typing.Literal['AES256', 'KMS']]


# S3ObjectOwnerTypeDef

### ID
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]


# S3RetentionTypeDef

### RetainUntilDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### Mode
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'GOVERNANCE']]


# S3SetObjectAclOperationTypeDef

### AccessControlPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3AccessControlPolicyTypeDef]


# S3SetObjectLegalHoldOperationTypeDef

### LegalHold
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.S3ObjectLockLegalHoldTypeDef'>
- **Required**: Yes


# S3SetObjectRetentionOperationTypeDef

### Retention
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.S3RetentionTypeDef'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# S3SetObjectTaggingOperationTypeDef

### TagSet
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]]


# S3TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SSEKMSEncryptionTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# SSEKMSTypeDef

### KeyId
- **Type**: <class 'str'>
- **Required**: Yes


# SelectionCriteriaTypeDef

### Delimiter
- **Type**: typing.Optional[str]

### MaxDepth
- **Type**: typing.Optional[int]

### MinStorageBytesPercentage
- **Type**: typing.Optional[float]


# SourceSelectionCriteriaTypeDef

### SseKmsEncryptedObjects
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.SseKmsEncryptedObjectsTypeDef]

### ReplicaModifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ReplicaModificationsTypeDef]


# SseKmsEncryptedObjectsTypeDef

### Status
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# StorageLensAwsOrgTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# StorageLensConfigurationTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AccountLevel
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.AccountLevelTypeDef'>
- **Required**: Yes

### IsEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Include
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.IncludeTypeDef]

### Exclude
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.ExcludeTypeDef]

### DataExport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensDataExportTypeDef]

### AwsOrg
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensAwsOrgTypeDef]

### StorageLensArn
- **Type**: typing.Optional[str]


# StorageLensDataExportEncryptionTypeDef

### SSES3
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### SSEKMS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.SSEKMSTypeDef]


# StorageLensDataExportTypeDef

### S3BucketDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.S3BucketDestinationTypeDef]

### CloudWatchMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.CloudWatchMetricsTypeDef]


# StorageLensGroupAndOperatorTypeDef

### MatchAnyPrefix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]]

### MatchObjectAge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MatchObjectAgeTypeDef]

### MatchObjectSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MatchObjectSizeTypeDef]


# StorageLensGroupFilterTypeDef

### MatchAnyPrefix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]]

### MatchObjectAge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MatchObjectAgeTypeDef]

### MatchObjectSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MatchObjectSizeTypeDef]

### And
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupAndOperatorTypeDef]

### Or
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupOrOperatorTypeDef]


# StorageLensGroupLevelSelectionCriteriaTypeDef

### Include
- **Type**: typing.Optional[typing.List[str]]

### Exclude
- **Type**: typing.Optional[typing.List[str]]


# StorageLensGroupLevelTypeDef

### SelectionCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupLevelSelectionCriteriaTypeDef]


# StorageLensGroupOrOperatorTypeDef

### MatchAnyPrefix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnySuffix
- **Type**: typing.Optional[typing.Sequence[str]]

### MatchAnyTag
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]]

### MatchObjectAge
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MatchObjectAgeTypeDef]

### MatchObjectSize
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.s3control_classes.MatchObjectSizeTypeDef]


# StorageLensGroupTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupFilterTypeDef'>
- **Required**: Yes

### StorageLensGroupArn
- **Type**: typing.Optional[str]


# StorageLensTagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitMultiRegionAccessPointRoutesRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Mrap
- **Type**: <class 'str'>
- **Required**: Yes

### RouteUpdates
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.MultiRegionAccessPointRouteTypeDef]
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TaggingTypeDef

### TagSet
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.s3control_classes.S3TagTypeDef]
- **Required**: Yes


# TransitionTypeDef

### Date
- **Type**: typing.Optional[datetime.datetime]

### Days
- **Type**: typing.Optional[int]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'STANDARD_IA']]


# UntagResourceRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessGrantsLocationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAccessGrantsLocationResultTypeDef

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessGrantsLocationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessGrantsLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationScope
- **Type**: <class 'str'>
- **Required**: Yes

### IAMRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateJobPriorityRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateJobPriorityResultTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateJobStatusRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### RequestedJobStatus
- **Type**: typing.Literal['Cancelled', 'Ready']
- **Required**: Yes

### StatusUpdateReason
- **Type**: typing.Optional[str]


# UpdateJobStatusResultTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Cancelled', 'Cancelling', 'Complete', 'Completing', 'Failed', 'Failing', 'New', 'Paused', 'Pausing', 'Preparing', 'Ready', 'Suspended']
- **Required**: Yes

### StatusUpdateReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStorageLensGroupRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageLensGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.s3control_classes.StorageLensGroupTypeDef'>
- **Required**: Yes


# VersioningConfigurationTypeDef

### MFADelete
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### Status
- **Type**: typing.Optional[typing.Literal['Enabled', 'Suspended']]


# VpcConfigurationTypeDef

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes



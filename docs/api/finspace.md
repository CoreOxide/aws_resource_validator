# Finspace Service

### AvailabilityZoneId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 8
- **Max Length**: 12

### ChangesetId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]+$`
- **Min Length**: 1
- **Max Length**: 26

### ClientToken
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 36

### ClientTokenString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 64

### DataBundleArn
- **Type**: string
- **Pattern**: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d*:data-bundle/[0-9A-Za-z_-]{1,128}$`
- **Min Length**: 20
- **Max Length**: 2048

### DatabaseName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### DbPath
- **Type**: string
- **Pattern**: `^(\*)*[\/\?\*]([^\/]+\/){0,2}[^\/]*$`
- **Min Length**: 1
- **Max Length**: 1025

### Description
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9. ]{1,1000}$`
- **Min Length**: 1
- **Max Length**: 1000

### EmailId
- **Type**: string
- **Pattern**: `[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+[.]+[A-Za-z]+`
- **Min Length**: 1
- **Max Length**: 128

### EnvironmentArn
- **Type**: string
- **Pattern**: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:environment/[0-9A-Za-z_-]{1,128}$`
- **Min Length**: 20
- **Max Length**: 2048

### EnvironmentErrorMessage
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9. ]{1,1000}$`
- **Min Length**: 0
- **Max Length**: 1000

### EnvironmentId
- **Type**: string
- **Pattern**: `.*\S.*`
- **Min Length**: 1
- **Max Length**: 32

### EnvironmentName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]$`
- **Min Length**: 1
- **Max Length**: 255

### ExecutionRoleArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w-\/.@+=,]{1,1017}$`
- **Min Length**: 1
- **Max Length**: 1024

### FederationAttributeKey
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 32

### FederationAttributeValue
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1000

### FederationProviderName
- **Type**: string
- **Pattern**: `[^_\p{Z}][\p{L}\p{M}\p{S}\p{N}\p{P}][^_\p{Z}]+`
- **Min Length**: 1
- **Max Length**: 32

### FinSpaceTaggableArn
- **Type**: string
- **Pattern**: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:(environment|kxEnvironment)/[0-9A-Za-z_-]{1,128}(/(kxCluster|kxUser|kxVolume|kxScalingGroup)/[a-zA-Z0-9_-]{1,255}|/(kxDatabase/[a-zA-Z0-9_-]{1,255}(/kxDataview/[a-zA-Z0-9_-]{1,255})?))?$`
- **Min Length**: 20
- **Max Length**: 2048

### IdType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{1,26}$`
- **Min Length**: 1
- **Max Length**: 26

### InitializationScriptFilePath
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_\-\.\/\\]+$`
- **Min Length**: 1
- **Max Length**: 255

### KmsKeyARN
- **Type**: string
- **Pattern**: `^arn:aws:kms:.*:\d+:.*$`
- **Min Length**: 1
- **Max Length**: 1000

### KmsKeyId
- **Type**: string
- **Pattern**: `^[a-zA-Z-0-9-:\/]*$`
- **Min Length**: 1
- **Max Length**: 1000

### KxClusterDescription
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_\-\.\s]+$`
- **Min Length**: 1
- **Max Length**: 1000

### KxClusterName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### KxClusterStatusReason
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_\-\.\s]+$`
- **Min Length**: 1
- **Max Length**: 250

### KxCommandLineArgumentKey
- **Type**: string
- **Pattern**: `^(?![Aa][Ww][Ss])(s|([a-zA-Z][a-zA-Z0-9_]+))|(AWS_ZIP_DEFAULT)`
- **Min Length**: 1
- **Max Length**: 1024

### KxCommandLineArgumentValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_:./,]+$`
- **Min Length**: 1
- **Max Length**: 1024

### KxDataviewName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### KxDataviewStatusReason
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_\-\.\s]+$`
- **Min Length**: 1
- **Max Length**: 250

### KxEnvironmentId
- **Type**: string
- **Pattern**: `^[a-z0-9]+$`
- **Min Length**: 1
- **Max Length**: 32

### KxEnvironmentName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### KxHostType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._]+`
- **Min Length**: 1
- **Max Length**: 32

### KxScalingGroupName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### KxUserArn
- **Type**: string
- **Pattern**: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:kxEnvironment/[0-9A-Za-z_-]{1,128}/kxUser/[0-9A-Za-z_-]{1,128}$`
- **Min Length**: 20
- **Max Length**: 2048

### KxUserNameString
- **Type**: string
- **Pattern**: `^[0-9A-Za-z_-]{1,50}$`
- **Min Length**: 1
- **Max Length**: 50

### KxVolumeArn
- **Type**: string
- **Pattern**: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:kxEnvironment/[0-9A-Za-z_-]{1,128}(/kxSharedVolume/[a-zA-Z0-9_-]{1,255})?$`
- **Min Length**: 20
- **Max Length**: 2048

### KxVolumeName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### KxVolumeStatusReason
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\_\-\.\s]+$`
- **Min Length**: 1
- **Max Length**: 250

### NameString
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9]{1,50}$`
- **Min Length**: 1
- **Max Length**: 50

### NodeType
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._]+$`
- **Min Length**: 1
- **Max Length**: 32

### PaginationToken
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1
- **Max Length**: 1000

### Protocol
- **Type**: string
- **Pattern**: `^-1|[0-9]+$`
- **Min Length**: 1
- **Max Length**: 5

### ReleaseLabel
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9._-]+$`
- **Min Length**: 1
- **Max Length**: 16

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
- **Min Length**: 20
- **Max Length**: 2048

### S3Bucket
- **Type**: string
- **Pattern**: `^[a-z0-9][a-z0-9\.\-]*[a-z0-9]$`
- **Min Length**: 3
- **Max Length**: 255

### S3Key
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9\/\!\-_\.\*\'\(\)]+$`
- **Min Length**: 1
- **Max Length**: 1024

### S3Path
- **Type**: string
- **Pattern**: `^s3:\/\/[a-z0-9][a-z0-9-.]{1,61}[a-z0-9]\/([^\/]+\/)*[^\/]*$`
- **Min Length**: 9
- **Max Length**: 1093

### SamlMetadataDocument
- **Type**: string
- **Pattern**: `.*`
- **Min Length**: 1000
- **Max Length**: 10000000

### SecurityGroupIdString
- **Type**: string
- **Pattern**: `^sg-([a-z0-9]{8}$|[a-z0-9]{17}$)`
- **Min Length**: 1
- **Max Length**: 1024

### SignedKxConnectionString
- **Type**: string
- **Pattern**: `^(:|:tcps:\/\/)[a-zA-Z0-9-\.\_]+:\d+:[a-zA-Z0-9-\.\_]+:\S+$`
- **Min Length**: 1
- **Max Length**: 2048

### SmsDomainUrl
- **Type**: string
- **Pattern**: `^[a-zA-Z-0-9-:\/.]*$`
- **Min Length**: 1
- **Max Length**: 1000

### SubnetIdString
- **Type**: string
- **Pattern**: `^subnet-([a-z0-9]{8}$|[a-z0-9]{17}$)`
- **Min Length**: 1
- **Max Length**: 1024

### TagKey
- **Type**: string
- **Pattern**: `^(?!aws:)[a-zA-Z+-=._:/]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9+-=._:@ ]+$`
- **Min Length**: 1
- **Max Length**: 256

### ValidCIDRBlock
- **Type**: string
- **Pattern**: `^(?:\d{1,3}\.){3}\d{1,3}(?:\/(?:3[0-2]|[12]\d|\d))$`
- **Min Length**: 1
- **Max Length**: 18

### ValidHostname
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$`
- **Min Length**: 3
- **Max Length**: 255

### ValidIPAddress
- **Type**: string
- **Pattern**: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`

### VolumeName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
- **Min Length**: 3
- **Max Length**: 63

### VpcIdString
- **Type**: string
- **Pattern**: `^vpc-([a-z0-9]{8}$|[a-z0-9]{17}$)`
- **Min Length**: 1
- **Max Length**: 1024

### arn
- **Type**: string
- **Pattern**: `^arn:*:*:*:*:*`
- **Min Length**: 20
- **Max Length**: 2048

### url
- **Type**: string
- **Pattern**: `^https?://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
- **Min Length**: 1
- **Max Length**: 1000

### urn
- **Type**: string
- **Pattern**: `^[A-Za-z0-9._\-:\/#\+]+$`
- **Min Length**: 1
- **Max Length**: 255


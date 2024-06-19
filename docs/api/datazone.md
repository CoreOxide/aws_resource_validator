# Datazone Service

### AssetId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### AssetIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### AssetTypeIdentifier
- **Type**: string
- **Pattern**: `^(?!\.)[\w\.]*\w$`
- **Min Length**: 1
- **Max Length**: 513

### AuthorizedPrincipalIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9:/_-]*$`

### AwsAccountId
- **Type**: string
- **Pattern**: `^\d{12}$`

### AwsRegion
- **Type**: string
- **Pattern**: `^[a-z]{2}-[a-z]{4,10}-\d$`

### ClientToken
- **Type**: string
- **Pattern**: `^[\x21-\x7E]+$`
- **Min Length**: 1
- **Max Length**: 128

### CronString
- **Type**: string
- **Pattern**: `cron\((\b[0-5]?[0-9]\b) (\b2[0-3]\b|\b[0-1]?[0-9]\b) (.*){1,5} (.*){1,5} (.*){1,5} (.*){1,5}\)`
- **Min Length**: 1
- **Max Length**: 256

### CustomParameterKeyNameString
- **Type**: string
- **Pattern**: `^[a-zA-Z_][a-zA-Z0-9_]*$`

### DataPointIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{0,36}$`

### DataProductId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### DataSourceId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### DataSourceRunId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### DomainId
- **Type**: string
- **Pattern**: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`

### EntityId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### EntityIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### EnvironmentBlueprintId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### EnvironmentBlueprintName
- **Type**: string
- **Pattern**: `^[\w -]+$`
- **Min Length**: 1
- **Max Length**: 64

### EnvironmentId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### EnvironmentName
- **Type**: string
- **Pattern**: `^[\w -]+$`
- **Min Length**: 1
- **Max Length**: 64

### EnvironmentProfileId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### EnvironmentProfileName
- **Type**: string
- **Pattern**: `^[\w -]+$`
- **Min Length**: 1
- **Max Length**: 64

### FormName
- **Type**: string
- **Pattern**: `^(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`
- **Min Length**: 1
- **Max Length**: 128

### FormTypeIdentifier
- **Type**: string
- **Pattern**: `^(?!\.)[\w\.]*\w$`
- **Min Length**: 1
- **Max Length**: 385

### FormTypeName
- **Type**: string
- **Pattern**: `^(amazon.datazone.)?(?![0-9_])\w+$|^_\w*[a-zA-Z0-9]\w*$`
- **Min Length**: 1
- **Max Length**: 128

### GlossaryId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### GlossaryTermId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### GlueRunConfigurationInputDataAccessRoleString
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]{1,128}$`

### GlueRunConfigurationOutputAccountIdString
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### GlueRunConfigurationOutputDataAccessRoleString
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]{1,128}$`

### GlueRunConfigurationOutputRegionString
- **Type**: string
- **Pattern**: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
- **Min Length**: 4
- **Max Length**: 16

### GroupIdentifier
- **Type**: string
- **Pattern**: `(^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$|[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r  ]+)`

### GroupProfileId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### GroupProfileName
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 1024

### KmsKeyArn
- **Type**: string
- **Pattern**: `^arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
- **Min Length**: 1
- **Max Length**: 1024

### ListingId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### MetadataGenerationRunIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### ProjectId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### ProjectName
- **Type**: string
- **Pattern**: `^[\w -]+$`
- **Min Length**: 1
- **Max Length**: 64

### RedshiftClusterStorageClusterNameString
- **Type**: string
- **Pattern**: `^[0-9a-z].[a-z0-9\-]*$`
- **Min Length**: 1
- **Max Length**: 63

### RedshiftCredentialConfigurationSecretManagerArnString
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:secretsmanager:[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]:\d{12}:secret:.*$`
- **Min Length**: 0
- **Max Length**: 256

### RedshiftRunConfigurationInputDataAccessRoleString
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]{1,128}$`

### RedshiftRunConfigurationOutputAccountIdString
- **Type**: string
- **Pattern**: `^\d{12}$`
- **Min Length**: 12
- **Max Length**: 12

### RedshiftRunConfigurationOutputDataAccessRoleString
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]{1,128}$`

### RedshiftRunConfigurationOutputRegionString
- **Type**: string
- **Pattern**: `[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]`
- **Min Length**: 4
- **Max Length**: 16

### RedshiftServerlessStorageWorkgroupNameString
- **Type**: string
- **Pattern**: `^[a-z0-9-]+$`
- **Min Length**: 3
- **Max Length**: 64

### RegionName
- **Type**: string
- **Pattern**: `^[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]$`
- **Min Length**: 4
- **Max Length**: 16

### RoleArn
- **Type**: string
- **Pattern**: `^arn:aws[^:]*:iam::\d{12}:(role|role/service-role)/[\w+=,.@-]*$`

### SubscriptionGrantId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### SubscriptionId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### SubscriptionRequestId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### SubscriptionTargetId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### TagKey
- **Type**: string
- **Pattern**: `^[\w \.:/=+@-]+$`
- **Min Length**: 1
- **Max Length**: 128

### TagValue
- **Type**: string
- **Pattern**: `^[\w \.:/=+@-]*$`
- **Min Length**: 0
- **Max Length**: 256

### TaskId
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### TimeSeriesDataPointIdentifier
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9_-]{1,36}$`

### TypeName
- **Type**: string
- **Pattern**: `^[^\.]*`
- **Min Length**: 1
- **Max Length**: 256

### UserIdentifier
- **Type**: string
- **Pattern**: `(^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$|^[a-zA-Z_0-9+=,.@-]+$|^arn:aws:iam::\d{12}:.+$)`

### UserProfileId
- **Type**: string
- **Pattern**: `^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`

### UserProfileName
- **Type**: string
- **Pattern**: `^[a-zA-Z_0-9+=,.@-]+$`
- **Min Length**: 1
- **Max Length**: 1024


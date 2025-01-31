# Macie2 Classes

# AcceptInvitationRequestRequestTypeDef

### invitationId
- **Type**: <class 'str'>
- **Required**: Yes

### administratorAccountId
- **Type**: typing.Optional[str]

### masterAccount
- **Type**: typing.Optional[str]


# AccessControlListTypeDef

### allowsPublicReadAccess
- **Type**: typing.Optional[bool]

### allowsPublicWriteAccess
- **Type**: typing.Optional[bool]


# AccountDetailTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes


# AccountLevelPermissionsTypeDef

### blockPublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BlockPublicAccessTypeDef]


# AdminAccountTypeDef

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLING_IN_PROGRESS', 'ENABLED']]


# AllowListCriteriaTypeDef

### regex
- **Type**: typing.Optional[str]

### s3WordsList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3WordsListTypeDef]


# AllowListStatusTypeDef

### code
- **Type**: typing.Literal['OK', 'S3_OBJECT_ACCESS_DENIED', 'S3_OBJECT_EMPTY', 'S3_OBJECT_NOT_FOUND', 'S3_OBJECT_OVERSIZE', 'S3_THROTTLED', 'S3_USER_ACCESS_DENIED', 'UNKNOWN_ERROR']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# AllowListSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ApiCallDetailsTypeDef

### api
- **Type**: typing.Optional[str]

### apiServiceName
- **Type**: typing.Optional[str]

### firstSeen
- **Type**: typing.Optional[datetime.datetime]

### lastSeen
- **Type**: typing.Optional[datetime.datetime]


# AssumedRoleTypeDef

### accessKeyId
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### sessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SessionContextTypeDef]


# AutomatedDiscoveryAccountTypeDef

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AutomatedDiscoveryAccountUpdateErrorTypeDef

### accountId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['ACCOUNT_NOT_FOUND', 'ACCOUNT_PAUSED']]


# AutomatedDiscoveryAccountUpdateTypeDef

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsAccountTypeDef

### accountId
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]


# AwsServiceTypeDef

### invokedBy
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetCustomDataIdentifierSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### deleted
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# BatchGetCustomDataIdentifiersRequestRequestTypeDef

### ids
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetCustomDataIdentifiersResponseTypeDef

### customDataIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.BatchGetCustomDataIdentifierSummaryTypeDef]
- **Required**: Yes

### notFoundIdentifierIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateAutomatedDiscoveryAccountsRequestRequestTypeDef

### accounts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.AutomatedDiscoveryAccountUpdateTypeDef]]


# BatchUpdateAutomatedDiscoveryAccountsResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.AutomatedDiscoveryAccountUpdateErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlockPublicAccessTypeDef

### blockPublicAcls
- **Type**: typing.Optional[bool]

### blockPublicPolicy
- **Type**: typing.Optional[bool]

### ignorePublicAcls
- **Type**: typing.Optional[bool]

### restrictPublicBuckets
- **Type**: typing.Optional[bool]


# BucketCountByEffectivePermissionTypeDef

### publiclyAccessible
- **Type**: typing.Optional[int]

### publiclyReadable
- **Type**: typing.Optional[int]

### publiclyWritable
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# BucketCountByEncryptionTypeTypeDef

### kmsManaged
- **Type**: typing.Optional[int]

### s3Managed
- **Type**: typing.Optional[int]

### unencrypted
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# BucketCountBySharedAccessTypeTypeDef

### external
- **Type**: typing.Optional[int]

### internal
- **Type**: typing.Optional[int]

### notShared
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef

### allowsUnencryptedObjectUploads
- **Type**: typing.Optional[int]

### deniesUnencryptedObjectUploads
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# BucketCriteriaAdditionalPropertiesTypeDef

### eq
- **Type**: typing.Optional[typing.Sequence[str]]

### gt
- **Type**: typing.Optional[int]

### gte
- **Type**: typing.Optional[int]

### lt
- **Type**: typing.Optional[int]

### lte
- **Type**: typing.Optional[int]

### neq
- **Type**: typing.Optional[typing.Sequence[str]]

### prefix
- **Type**: typing.Optional[str]


# BucketLevelPermissionsTypeDef

### accessControlList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.AccessControlListTypeDef]

### blockPublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BlockPublicAccessTypeDef]

### bucketPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BucketPolicyTypeDef]


# BucketMetadataTypeDef

### accountId
- **Type**: typing.Optional[str]

### allowsUnencryptedObjectUploads
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE', 'UNKNOWN']]

### automatedDiscoveryMonitoringStatus
- **Type**: typing.Optional[typing.Literal['MONITORED', 'NOT_MONITORED']]

### bucketArn
- **Type**: typing.Optional[str]

### bucketCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### bucketName
- **Type**: typing.Optional[str]

### classifiableObjectCount
- **Type**: typing.Optional[int]

### classifiableSizeInBytes
- **Type**: typing.Optional[int]

### errorCode
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED']]

### errorMessage
- **Type**: typing.Optional[str]

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.JobDetailsTypeDef]

### lastAutomatedDiscoveryTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]

### objectCount
- **Type**: typing.Optional[int]

### objectCountByEncryptionType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ObjectCountByEncryptionTypeTypeDef]

### publicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BucketPublicAccessTypeDef]

### region
- **Type**: typing.Optional[str]

### replicationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ReplicationDetailsTypeDef]

### sensitivityScore
- **Type**: typing.Optional[int]

### serverSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BucketServerSideEncryptionTypeDef]

### sharedAccess
- **Type**: typing.Optional[typing.Literal['EXTERNAL', 'INTERNAL', 'NOT_SHARED', 'UNKNOWN']]

### sizeInBytes
- **Type**: typing.Optional[int]

### sizeInBytesCompressed
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.KeyValuePairTypeDef]]

### unclassifiableObjectCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ObjectLevelStatisticsTypeDef]

### unclassifiableObjectSizeInBytes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ObjectLevelStatisticsTypeDef]

### versioning
- **Type**: typing.Optional[bool]


# BucketPermissionConfigurationTypeDef

### accountLevelPermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.AccountLevelPermissionsTypeDef]

### bucketLevelPermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BucketLevelPermissionsTypeDef]


# BucketPolicyTypeDef

### allowsPublicReadAccess
- **Type**: typing.Optional[bool]

### allowsPublicWriteAccess
- **Type**: typing.Optional[bool]


# BucketPublicAccessTypeDef

### effectivePermission
- **Type**: typing.Optional[typing.Literal['NOT_PUBLIC', 'PUBLIC', 'UNKNOWN']]

### permissionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BucketPermissionConfigurationTypeDef]


# BucketServerSideEncryptionTypeDef

### kmsMasterKeyId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AES256', 'NONE', 'aws:kms', 'aws:kms:dsse']]


# BucketSortCriteriaTypeDef

### attributeName
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# BucketStatisticsBySensitivityTypeDef

### classificationError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SensitivityAggregationsTypeDef]

### notClassified
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SensitivityAggregationsTypeDef]

### notSensitive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SensitivityAggregationsTypeDef]

### sensitive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SensitivityAggregationsTypeDef]


# CellTypeDef

### cellReference
- **Type**: typing.Optional[str]

### column
- **Type**: typing.Optional[int]

### columnName
- **Type**: typing.Optional[str]

### row
- **Type**: typing.Optional[int]


# ClassificationDetailsTypeDef

### detailedResultsLocation
- **Type**: typing.Optional[str]

### jobArn
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### originType
- **Type**: typing.Optional[typing.Literal['AUTOMATED_SENSITIVE_DATA_DISCOVERY', 'SENSITIVE_DATA_DISCOVERY_JOB']]

### result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ClassificationResultTypeDef]


# ClassificationExportConfigurationTypeDef

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3DestinationTypeDef]


# ClassificationResultStatusTypeDef

### code
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# ClassificationResultTypeDef

### additionalOccurrences
- **Type**: typing.Optional[bool]

### customDataIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.CustomDataIdentifiersTypeDef]

### mimeType
- **Type**: typing.Optional[str]

### sensitiveData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.SensitiveDataItemTypeDef]]

### sizeClassified
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ClassificationResultStatusTypeDef]


# ClassificationScopeSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# CreateAllowListRequestRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.AllowListCriteriaTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAllowListResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateClassificationJobRequestRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### jobType
- **Type**: typing.Literal['ONE_TIME', 'SCHEDULED']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### s3JobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.S3JobDefinitionTypeDef'>
- **Required**: Yes

### allowListIds
- **Type**: typing.Optional[typing.Sequence[str]]

### customDataIdentifierIds
- **Type**: typing.Optional[typing.Sequence[str]]

### description
- **Type**: typing.Optional[str]

### initialRun
- **Type**: typing.Optional[bool]

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.Sequence[str]]

### managedDataIdentifierSelector
- **Type**: typing.Optional[typing.Literal['ALL', 'EXCLUDE', 'INCLUDE', 'NONE', 'RECOMMENDED']]

### samplingPercentage
- **Type**: typing.Optional[int]

### scheduleFrequency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.JobScheduleFrequencyTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateClassificationJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomDataIdentifierRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### regex
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### ignoreWords
- **Type**: typing.Optional[typing.Sequence[str]]

### keywords
- **Type**: typing.Optional[typing.Sequence[str]]

### maximumMatchDistance
- **Type**: typing.Optional[int]

### severityLevels
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.SeverityLevelTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCustomDataIdentifierResponseTypeDef

### customDataIdentifierId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFindingsFilterRequestRequestTypeDef

### action
- **Type**: typing.Literal['ARCHIVE', 'NOOP']
- **Required**: Yes

### findingCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.FindingCriteriaTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFindingsFilterResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInvitationsRequestRequestTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### disableEmailNotification
- **Type**: typing.Optional[bool]

### message
- **Type**: typing.Optional[str]


# CreateInvitationsResponseTypeDef

### unprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMemberRequestRequestTypeDef

### account
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.AccountDetailTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMemberResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSampleFindingsRequestRequestTypeDef

### findingTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Policy:IAMUser/S3BlockPublicAccessDisabled', 'Policy:IAMUser/S3BucketEncryptionDisabled', 'Policy:IAMUser/S3BucketPublic', 'Policy:IAMUser/S3BucketReplicatedExternally', 'Policy:IAMUser/S3BucketSharedExternally', 'Policy:IAMUser/S3BucketSharedWithCloudFront', 'SensitiveData:S3Object/Credentials', 'SensitiveData:S3Object/CustomIdentifier', 'SensitiveData:S3Object/Financial', 'SensitiveData:S3Object/Multiple', 'SensitiveData:S3Object/Personal']]]


# CriteriaBlockForJobOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CriteriaBlockForJobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CriteriaForJobOutputTypeDef

### simpleCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SimpleCriterionForJobOutputTypeDef]

### tagCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.TagCriterionForJobOutputTypeDef]


# CriteriaForJobTypeDef

### simpleCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SimpleCriterionForJobTypeDef]

### tagCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.TagCriterionForJobTypeDef]


# CriterionAdditionalPropertiesOutputTypeDef

### eq
- **Type**: typing.Optional[typing.List[str]]

### eqExactMatch
- **Type**: typing.Optional[typing.List[str]]

### gt
- **Type**: typing.Optional[int]

### gte
- **Type**: typing.Optional[int]

### lt
- **Type**: typing.Optional[int]

### lte
- **Type**: typing.Optional[int]

### neq
- **Type**: typing.Optional[typing.List[str]]


# CriterionAdditionalPropertiesTypeDef

### eq
- **Type**: typing.Optional[typing.Sequence[str]]

### eqExactMatch
- **Type**: typing.Optional[typing.Sequence[str]]

### gt
- **Type**: typing.Optional[int]

### gte
- **Type**: typing.Optional[int]

### lt
- **Type**: typing.Optional[int]

### lte
- **Type**: typing.Optional[int]

### neq
- **Type**: typing.Optional[typing.Sequence[str]]


# CustomDataIdentifierSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# CustomDataIdentifiersTypeDef

### detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.CustomDetectionTypeDef]]

### totalCount
- **Type**: typing.Optional[int]


# CustomDetectionTypeDef

### arn
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.OccurrencesTypeDef]


# DeclineInvitationsRequestRequestTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeclineInvitationsResponseTypeDef

### unprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DefaultDetectionTypeDef

### count
- **Type**: typing.Optional[int]

### occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.OccurrencesTypeDef]

### type
- **Type**: typing.Optional[str]


# DeleteAllowListRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ignoreJobChecks
- **Type**: typing.Optional[str]


# DeleteCustomDataIdentifierRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFindingsFilterRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInvitationsRequestRequestTypeDef

### accountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteInvitationsResponseTypeDef

### unprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.UnprocessedAccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMemberRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBucketsRequestDescribeBucketsPaginateTypeDef

### criteria
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.macie2_classes.BucketCriteriaAdditionalPropertiesTypeDef]]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BucketSortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# DescribeBucketsRequestRequestTypeDef

### criteria
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.macie2_classes.BucketCriteriaAdditionalPropertiesTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BucketSortCriteriaTypeDef]


# DescribeBucketsResponseTypeDef

### buckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.BucketMetadataTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClassificationJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClassificationJobResponseTypeDef

### allowListIds
- **Type**: typing.List[str]
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customDataIdentifierIds
- **Type**: typing.List[str]
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### initialRun
- **Type**: <class 'bool'>
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'IDLE', 'PAUSED', 'RUNNING', 'USER_PAUSED']
- **Required**: Yes

### jobType
- **Type**: typing.Literal['ONE_TIME', 'SCHEDULED']
- **Required**: Yes

### lastRunErrorStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.LastRunErrorStatusTypeDef'>
- **Required**: Yes

### lastRunTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### managedDataIdentifierIds
- **Type**: typing.List[str]
- **Required**: Yes

### managedDataIdentifierSelector
- **Type**: typing.Literal['ALL', 'EXCLUDE', 'INCLUDE', 'NONE', 'RECOMMENDED']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### s3JobDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.S3JobDefinitionOutputTypeDef'>
- **Required**: Yes

### samplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### scheduleFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.JobScheduleFrequencyOutputTypeDef'>
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.StatisticsTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### userPausedDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.UserPausedDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationConfigurationResponseTypeDef

### autoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### maxAccountLimitReached
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectedDataDetailsTypeDef

### value
- **Type**: <class 'str'>
- **Required**: Yes


# DetectionTypeDef

### arn
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### suppressed
- **Type**: typing.Optional[bool]

### type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'MANAGED']]


# DisableOrganizationAdminAccountRequestRequestTypeDef

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DomainDetailsTypeDef

### domainName
- **Type**: typing.Optional[str]


# EnableMacieRequestRequestTypeDef

### clientToken
- **Type**: typing.Optional[str]

### findingPublishingFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']]

### status
- **Type**: typing.Optional[typing.Literal['ENABLED', 'PAUSED']]


# EnableOrganizationAdminAccountRequestRequestTypeDef

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# FederatedUserTypeDef

### accessKeyId
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### sessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SessionContextTypeDef]


# FindingActionTypeDef

### actionType
- **Type**: typing.Optional[typing.Literal['AWS_API_CALL']]

### apiCallDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ApiCallDetailsTypeDef]


# FindingActorTypeDef

### domainDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.DomainDetailsTypeDef]

### ipAddressDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.IpAddressDetailsTypeDef]

### userIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.UserIdentityTypeDef]


# FindingCriteriaOutputTypeDef

### criterion
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.macie2_classes.CriterionAdditionalPropertiesOutputTypeDef]]


# FindingCriteriaTypeDef

### criterion
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.macie2_classes.CriterionAdditionalPropertiesTypeDef]]


# FindingStatisticsSortCriteriaTypeDef

### attributeName
- **Type**: typing.Optional[typing.Literal['count', 'groupKey']]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# FindingTypeDef

### accountId
- **Type**: typing.Optional[str]

### archived
- **Type**: typing.Optional[bool]

### category
- **Type**: typing.Optional[typing.Literal['CLASSIFICATION', 'POLICY']]

### classificationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ClassificationDetailsTypeDef]

### count
- **Type**: typing.Optional[int]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### partition
- **Type**: typing.Optional[str]

### policyDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PolicyDetailsTypeDef]

### region
- **Type**: typing.Optional[str]

### resourcesAffected
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ResourcesAffectedTypeDef]

### sample
- **Type**: typing.Optional[bool]

### schemaVersion
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SeverityTypeDef]

### title
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Policy:IAMUser/S3BlockPublicAccessDisabled', 'Policy:IAMUser/S3BucketEncryptionDisabled', 'Policy:IAMUser/S3BucketPublic', 'Policy:IAMUser/S3BucketReplicatedExternally', 'Policy:IAMUser/S3BucketSharedExternally', 'Policy:IAMUser/S3BucketSharedWithCloudFront', 'SensitiveData:S3Object/Credentials', 'SensitiveData:S3Object/CustomIdentifier', 'SensitiveData:S3Object/Financial', 'SensitiveData:S3Object/Multiple', 'SensitiveData:S3Object/Personal']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# FindingsFilterListItemTypeDef

### action
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'NOOP']]

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetAdministratorAccountResponseTypeDef

### administrator
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.InvitationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAllowListRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetAllowListResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.AllowListCriteriaTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.AllowListStatusTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAutomatedDiscoveryConfigurationResponseTypeDef

### autoEnableOrganizationMembers
- **Type**: typing.Literal['ALL', 'NEW', 'NONE']
- **Required**: Yes

### classificationScopeId
- **Type**: <class 'str'>
- **Required**: Yes

### disabledAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### firstEnabledAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sensitivityInspectionTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBucketStatisticsRequestRequestTypeDef

### accountId
- **Type**: typing.Optional[str]


# GetBucketStatisticsResponseTypeDef

### bucketCount
- **Type**: <class 'int'>
- **Required**: Yes

### bucketCountByEffectivePermission
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.BucketCountByEffectivePermissionTypeDef'>
- **Required**: Yes

### bucketCountByEncryptionType
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.BucketCountByEncryptionTypeTypeDef'>
- **Required**: Yes

### bucketCountByObjectEncryptionRequirement
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef'>
- **Required**: Yes

### bucketCountBySharedAccessType
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.BucketCountBySharedAccessTypeTypeDef'>
- **Required**: Yes

### bucketStatisticsBySensitivity
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.BucketStatisticsBySensitivityTypeDef'>
- **Required**: Yes

### classifiableObjectCount
- **Type**: <class 'int'>
- **Required**: Yes

### classifiableSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### lastUpdated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### objectCount
- **Type**: <class 'int'>
- **Required**: Yes

### sizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### sizeInBytesCompressed
- **Type**: <class 'int'>
- **Required**: Yes

### unclassifiableObjectCount
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ObjectLevelStatisticsTypeDef'>
- **Required**: Yes

### unclassifiableObjectSizeInBytes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ObjectLevelStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetClassificationExportConfigurationResponseTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ClassificationExportConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetClassificationScopeRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetClassificationScopeResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### s3
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.S3ClassificationScopeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCustomDataIdentifierRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomDataIdentifierResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deleted
- **Type**: <class 'bool'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ignoreWords
- **Type**: typing.List[str]
- **Required**: Yes

### keywords
- **Type**: typing.List[str]
- **Required**: Yes

### maximumMatchDistance
- **Type**: <class 'int'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### regex
- **Type**: <class 'str'>
- **Required**: Yes

### severityLevels
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.SeverityLevelTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingStatisticsRequestRequestTypeDef

### groupBy
- **Type**: typing.Literal['classificationDetails.jobId', 'resourcesAffected.s3Bucket.name', 'severity.description', 'type']
- **Required**: Yes

### findingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.FindingCriteriaTypeDef]

### size
- **Type**: typing.Optional[int]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.FindingStatisticsSortCriteriaTypeDef]


# GetFindingStatisticsResponseTypeDef

### countsByGroup
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.GroupCountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingsFilterRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFindingsFilterResponseTypeDef

### action
- **Type**: typing.Literal['ARCHIVE', 'NOOP']
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### findingCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.FindingCriteriaOutputTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### position
- **Type**: <class 'int'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingsPublicationConfigurationResponseTypeDef

### securityHubConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.SecurityHubConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFindingsRequestRequestTypeDef

### findingIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SortCriteriaTypeDef]


# GetFindingsResponseTypeDef

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.FindingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInvitationsCountResponseTypeDef

### invitationsCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMacieSessionResponseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### findingPublishingFrequency
- **Type**: typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']
- **Required**: Yes

### serviceRole
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ENABLED', 'PAUSED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMasterAccountResponseTypeDef

### master
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.InvitationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMemberRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberResponseTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### administratorAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes

### invitedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### masterAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### relationshipStatus
- **Type**: typing.Literal['AccountSuspended', 'Created', 'EmailVerificationFailed', 'EmailVerificationInProgress', 'Enabled', 'Invited', 'Paused', 'RegionDisabled', 'Removed', 'Resigned']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceProfileRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceProfileResponseTypeDef

### profileUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sensitivityScore
- **Type**: <class 'int'>
- **Required**: Yes

### sensitivityScoreOverridden
- **Type**: <class 'bool'>
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResourceStatisticsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRevealConfigurationResponseTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.RevealConfigurationTypeDef'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.RetrievalConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSensitiveDataOccurrencesAvailabilityRequestRequestTypeDef

### findingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSensitiveDataOccurrencesAvailabilityResponseTypeDef

### code
- **Type**: typing.Literal['AVAILABLE', 'UNAVAILABLE']
- **Required**: Yes

### reasons
- **Type**: typing.List[typing.Literal['ACCOUNT_NOT_IN_ORGANIZATION', 'INVALID_CLASSIFICATION_RESULT', 'INVALID_RESULT_SIGNATURE', 'MEMBER_ROLE_TOO_PERMISSIVE', 'MISSING_GET_MEMBER_PERMISSION', 'OBJECT_EXCEEDS_SIZE_QUOTA', 'OBJECT_UNAVAILABLE', 'RESULT_NOT_SIGNED', 'ROLE_TOO_PERMISSIVE', 'UNSUPPORTED_FINDING_TYPE', 'UNSUPPORTED_OBJECT_TYPE']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSensitiveDataOccurrencesRequestFindingRevealedWaitTypeDef

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.WaiterConfigTypeDef]


# GetSensitiveDataOccurrencesRequestRequestTypeDef

### findingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSensitiveDataOccurrencesResponseTypeDef

### error
- **Type**: <class 'str'>
- **Required**: Yes

### sensitiveDataOccurrences
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.macie2_classes.DetectedDataDetailsTypeDef]]
- **Required**: Yes

### status
- **Type**: typing.Literal['ERROR', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSensitivityInspectionTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSensitivityInspectionTemplateResponseTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### excludes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.SensitivityInspectionTemplateExcludesOutputTypeDef'>
- **Required**: Yes

### includes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.SensitivityInspectionTemplateIncludesOutputTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sensitivityInspectionTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUsageStatisticsRequestGetUsageStatisticsPaginateTypeDef

### filterBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.UsageStatisticsFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.UsageStatisticsSortByTypeDef]

### timeRange
- **Type**: typing.Optional[typing.Literal['MONTH_TO_DATE', 'PAST_30_DAYS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# GetUsageStatisticsRequestRequestTypeDef

### filterBy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.UsageStatisticsFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.UsageStatisticsSortByTypeDef]

### timeRange
- **Type**: typing.Optional[typing.Literal['MONTH_TO_DATE', 'PAST_30_DAYS']]


# GetUsageStatisticsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### records
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.UsageRecordTypeDef]
- **Required**: Yes

### timeRange
- **Type**: typing.Literal['MONTH_TO_DATE', 'PAST_30_DAYS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUsageTotalsRequestRequestTypeDef

### timeRange
- **Type**: typing.Optional[str]


# GetUsageTotalsResponseTypeDef

### timeRange
- **Type**: typing.Literal['MONTH_TO_DATE', 'PAST_30_DAYS']
- **Required**: Yes

### usageTotals
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.UsageTotalTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupCountTypeDef

### count
- **Type**: typing.Optional[int]

### groupKey
- **Type**: typing.Optional[str]


# IamUserTypeDef

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### userName
- **Type**: typing.Optional[str]


# InvitationTypeDef

### accountId
- **Type**: typing.Optional[str]

### invitationId
- **Type**: typing.Optional[str]

### invitedAt
- **Type**: typing.Optional[datetime.datetime]

### relationshipStatus
- **Type**: typing.Optional[typing.Literal['AccountSuspended', 'Created', 'EmailVerificationFailed', 'EmailVerificationInProgress', 'Enabled', 'Invited', 'Paused', 'RegionDisabled', 'Removed', 'Resigned']]


# IpAddressDetailsTypeDef

### ipAddressV4
- **Type**: typing.Optional[str]

### ipCity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.IpCityTypeDef]

### ipCountry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.IpCountryTypeDef]

### ipGeoLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.IpGeoLocationTypeDef]

### ipOwner
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.IpOwnerTypeDef]


# IpCityTypeDef

### name
- **Type**: typing.Optional[str]


# IpCountryTypeDef

### code
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# IpGeoLocationTypeDef

### lat
- **Type**: typing.Optional[float]

### lon
- **Type**: typing.Optional[float]


# IpOwnerTypeDef

### asn
- **Type**: typing.Optional[str]

### asnOrg
- **Type**: typing.Optional[str]

### isp
- **Type**: typing.Optional[str]

### org
- **Type**: typing.Optional[str]


# JobDetailsTypeDef

### isDefinedInJob
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE', 'UNKNOWN']]

### isMonitoredByJob
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE', 'UNKNOWN']]

### lastJobId
- **Type**: typing.Optional[str]

### lastJobRunTime
- **Type**: typing.Optional[datetime.datetime]


# JobScheduleFrequencyOutputTypeDef

### dailySchedule
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### monthlySchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.MonthlyScheduleTypeDef]

### weeklySchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.WeeklyScheduleTypeDef]


# JobScheduleFrequencyTypeDef

### dailySchedule
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### monthlySchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.MonthlyScheduleTypeDef]

### weeklySchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.WeeklyScheduleTypeDef]


# JobScopeTermOutputTypeDef

### simpleScopeTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SimpleScopeTermOutputTypeDef]

### tagScopeTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.TagScopeTermOutputTypeDef]


# JobScopeTermTypeDef

### simpleScopeTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SimpleScopeTermTypeDef]

### tagScopeTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.TagScopeTermTypeDef]


# JobScopingBlockOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobScopingBlockTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobSummaryTypeDef

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3BucketCriteriaForJobOutputTypeDef]

### bucketDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.S3BucketDefinitionForJobOutputTypeDef]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### jobId
- **Type**: typing.Optional[str]

### jobStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETE', 'IDLE', 'PAUSED', 'RUNNING', 'USER_PAUSED']]

### jobType
- **Type**: typing.Optional[typing.Literal['ONE_TIME', 'SCHEDULED']]

### lastRunErrorStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.LastRunErrorStatusTypeDef]

### name
- **Type**: typing.Optional[str]

### userPausedDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.UserPausedDetailsTypeDef]


# KeyValuePairTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# LastRunErrorStatusTypeDef

### code
- **Type**: typing.Optional[typing.Literal['ERROR', 'NONE']]


# ListAllowListsRequestListAllowListsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListAllowListsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAllowListsResponseTypeDef

### allowLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.AllowListSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAutomatedDiscoveryAccountsRequestListAutomatedDiscoveryAccountsPaginateTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListAutomatedDiscoveryAccountsRequestRequestTypeDef

### accountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAutomatedDiscoveryAccountsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.AutomatedDiscoveryAccountTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListClassificationJobsRequestListClassificationJobsPaginateTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ListJobsFilterCriteriaTypeDef]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ListJobsSortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListClassificationJobsRequestRequestTypeDef

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ListJobsFilterCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ListJobsSortCriteriaTypeDef]


# ListClassificationJobsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.JobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListClassificationScopesRequestListClassificationScopesPaginateTypeDef

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListClassificationScopesRequestRequestTypeDef

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListClassificationScopesResponseTypeDef

### classificationScopes
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.ClassificationScopeSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomDataIdentifiersRequestListCustomDataIdentifiersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListCustomDataIdentifiersRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomDataIdentifiersResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.CustomDataIdentifierSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingsFiltersRequestListFindingsFiltersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListFindingsFiltersRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsFiltersResponseTypeDef

### findingsFilterListItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.FindingsFilterListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingsRequestListFindingsPaginateTypeDef

### findingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.FindingCriteriaTypeDef]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListFindingsRequestRequestTypeDef

### findingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.FindingCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SortCriteriaTypeDef]


# ListFindingsResponseTypeDef

### findingIds
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInvitationsRequestListInvitationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListInvitationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInvitationsResponseTypeDef

### invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.InvitationTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsFilterCriteriaTypeDef

### excludes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.ListJobsFilterTermTypeDef]]

### includes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.ListJobsFilterTermTypeDef]]


# ListJobsFilterTermTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['createdAt', 'jobStatus', 'jobType', 'name']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# ListJobsSortCriteriaTypeDef

### attributeName
- **Type**: typing.Optional[typing.Literal['createdAt', 'jobStatus', 'jobType', 'name']]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListManagedDataIdentifiersRequestListManagedDataIdentifiersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListManagedDataIdentifiersRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListManagedDataIdentifiersResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.ManagedDataIdentifierSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMembersRequestListMembersPaginateTypeDef

### onlyAssociated
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListMembersRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### onlyAssociated
- **Type**: typing.Optional[str]


# ListMembersResponseTypeDef

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.MemberTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOrganizationAdminAccountsRequestListOrganizationAdminAccountsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListOrganizationAdminAccountsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsResponseTypeDef

### adminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.AdminAccountTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceProfileArtifactsRequestListResourceProfileArtifactsPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListResourceProfileArtifactsRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceProfileArtifactsResponseTypeDef

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.ResourceProfileArtifactTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListResourceProfileDetectionsRequestListResourceProfileDetectionsPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListResourceProfileDetectionsRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListResourceProfileDetectionsResponseTypeDef

### detections
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.DetectionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSensitivityInspectionTemplatesRequestListSensitivityInspectionTemplatesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# ListSensitivityInspectionTemplatesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSensitivityInspectionTemplatesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sensitivityInspectionTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.SensitivityInspectionTemplatesEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagedDataIdentifierSummaryTypeDef

### category
- **Type**: typing.Optional[typing.Literal['CREDENTIALS', 'CUSTOM_IDENTIFIER', 'FINANCIAL_INFORMATION', 'PERSONAL_INFORMATION']]

### id
- **Type**: typing.Optional[str]


# MatchingBucketTypeDef

### accountId
- **Type**: typing.Optional[str]

### automatedDiscoveryMonitoringStatus
- **Type**: typing.Optional[typing.Literal['MONITORED', 'NOT_MONITORED']]

### bucketName
- **Type**: typing.Optional[str]

### classifiableObjectCount
- **Type**: typing.Optional[int]

### classifiableSizeInBytes
- **Type**: typing.Optional[int]

### errorCode
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED']]

### errorMessage
- **Type**: typing.Optional[str]

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.JobDetailsTypeDef]

### lastAutomatedDiscoveryTime
- **Type**: typing.Optional[datetime.datetime]

### objectCount
- **Type**: typing.Optional[int]

### objectCountByEncryptionType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ObjectCountByEncryptionTypeTypeDef]

### sensitivityScore
- **Type**: typing.Optional[int]

### sizeInBytes
- **Type**: typing.Optional[int]

### sizeInBytesCompressed
- **Type**: typing.Optional[int]

### unclassifiableObjectCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ObjectLevelStatisticsTypeDef]

### unclassifiableObjectSizeInBytes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ObjectLevelStatisticsTypeDef]


# MatchingResourceTypeDef

### matchingBucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.MatchingBucketTypeDef]


# MemberTypeDef

### accountId
- **Type**: typing.Optional[str]

### administratorAccountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### email
- **Type**: typing.Optional[str]

### invitedAt
- **Type**: typing.Optional[datetime.datetime]

### masterAccountId
- **Type**: typing.Optional[str]

### relationshipStatus
- **Type**: typing.Optional[typing.Literal['AccountSuspended', 'Created', 'EmailVerificationFailed', 'EmailVerificationInProgress', 'Enabled', 'Invited', 'Paused', 'RegionDisabled', 'Removed', 'Resigned']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# MonthlyScheduleTypeDef

### dayOfMonth
- **Type**: typing.Optional[int]


# ObjectCountByEncryptionTypeTypeDef

### customerManaged
- **Type**: typing.Optional[int]

### kmsManaged
- **Type**: typing.Optional[int]

### s3Managed
- **Type**: typing.Optional[int]

### unencrypted
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# ObjectLevelStatisticsTypeDef

### fileType
- **Type**: typing.Optional[int]

### storageClass
- **Type**: typing.Optional[int]

### total
- **Type**: typing.Optional[int]


# OccurrencesTypeDef

### cells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.CellTypeDef]]

### lineRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.RangeTypeDef]]

### offsetRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.RangeTypeDef]]

### pages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.PageTypeDef]]

### records
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.RecordTypeDef]]


# PageTypeDef

### lineRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.RangeTypeDef]

### offsetRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.RangeTypeDef]

### pageNumber
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolicyDetailsTypeDef

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.FindingActionTypeDef]

### actor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.FindingActorTypeDef]


# PutClassificationExportConfigurationRequestRequestTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ClassificationExportConfigurationTypeDef'>
- **Required**: Yes


# PutClassificationExportConfigurationResponseTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ClassificationExportConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutFindingsPublicationConfigurationRequestRequestTypeDef

### clientToken
- **Type**: typing.Optional[str]

### securityHubConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SecurityHubConfigurationTypeDef]


# RangeTypeDef

### end
- **Type**: typing.Optional[int]

### start
- **Type**: typing.Optional[int]

### startColumn
- **Type**: typing.Optional[int]


# RecordTypeDef

### jsonPath
- **Type**: typing.Optional[str]

### recordIndex
- **Type**: typing.Optional[int]


# ReplicationDetailsTypeDef

### replicated
- **Type**: typing.Optional[bool]

### replicatedExternally
- **Type**: typing.Optional[bool]

### replicationAccounts
- **Type**: typing.Optional[typing.List[str]]


# ResourceProfileArtifactTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### classificationResultStatus
- **Type**: <class 'str'>
- **Required**: Yes

### sensitive
- **Type**: typing.Optional[bool]


# ResourceStatisticsTypeDef

### totalBytesClassified
- **Type**: typing.Optional[int]

### totalDetections
- **Type**: typing.Optional[int]

### totalDetectionsSuppressed
- **Type**: typing.Optional[int]

### totalItemsClassified
- **Type**: typing.Optional[int]

### totalItemsSensitive
- **Type**: typing.Optional[int]

### totalItemsSkipped
- **Type**: typing.Optional[int]

### totalItemsSkippedInvalidEncryption
- **Type**: typing.Optional[int]

### totalItemsSkippedInvalidKms
- **Type**: typing.Optional[int]

### totalItemsSkippedPermissionDenied
- **Type**: typing.Optional[int]


# ResourcesAffectedTypeDef

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3BucketTypeDef]

### s3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3ObjectTypeDef]


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


# RetrievalConfigurationTypeDef

### retrievalMode
- **Type**: typing.Literal['ASSUME_ROLE', 'CALLER_CREDENTIALS']
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]


# RevealConfigurationTypeDef

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]


# S3BucketCriteriaForJobOutputTypeDef

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.CriteriaBlockForJobOutputTypeDef]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.CriteriaBlockForJobOutputTypeDef]


# S3BucketCriteriaForJobTypeDef

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.CriteriaBlockForJobTypeDef]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.CriteriaBlockForJobTypeDef]


# S3BucketDefinitionForJobOutputTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### buckets
- **Type**: typing.List[str]
- **Required**: Yes


# S3BucketDefinitionForJobTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### buckets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# S3BucketOwnerTypeDef

### displayName
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# S3BucketTypeDef

### allowsUnencryptedObjectUploads
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE', 'UNKNOWN']]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### defaultServerSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ServerSideEncryptionTypeDef]

### name
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3BucketOwnerTypeDef]

### publicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.BucketPublicAccessTypeDef]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.KeyValuePairTypeDef]]


# S3ClassificationScopeExclusionTypeDef

### bucketNames
- **Type**: typing.List[str]
- **Required**: Yes


# S3ClassificationScopeExclusionUpdateTypeDef

### bucketNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### operation
- **Type**: typing.Literal['ADD', 'REMOVE', 'REPLACE']
- **Required**: Yes


# S3ClassificationScopeTypeDef

### excludes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.S3ClassificationScopeExclusionTypeDef'>
- **Required**: Yes


# S3ClassificationScopeUpdateTypeDef

### excludes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.S3ClassificationScopeExclusionUpdateTypeDef'>
- **Required**: Yes


# S3DestinationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# S3JobDefinitionOutputTypeDef

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3BucketCriteriaForJobOutputTypeDef]

### bucketDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.S3BucketDefinitionForJobOutputTypeDef]]

### scoping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ScopingOutputTypeDef]


# S3JobDefinitionTypeDef

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3BucketCriteriaForJobTypeDef]

### bucketDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.S3BucketDefinitionForJobTypeDef]]

### scoping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ScopingTypeDef]


# S3ObjectTypeDef

### bucketArn
- **Type**: typing.Optional[str]

### eTag
- **Type**: typing.Optional[str]

### extension
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]

### lastModified
- **Type**: typing.Optional[datetime.datetime]

### path
- **Type**: typing.Optional[str]

### publicAccess
- **Type**: typing.Optional[bool]

### serverSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ServerSideEncryptionTypeDef]

### size
- **Type**: typing.Optional[int]

### storageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'OUTPOSTS', 'REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.KeyValuePairTypeDef]]

### versionId
- **Type**: typing.Optional[str]


# S3WordsListTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### objectKey
- **Type**: <class 'str'>
- **Required**: Yes


# ScopingOutputTypeDef

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.JobScopingBlockOutputTypeDef]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.JobScopingBlockOutputTypeDef]


# ScopingTypeDef

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.JobScopingBlockTypeDef]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.JobScopingBlockTypeDef]


# SearchResourcesBucketCriteriaTypeDef

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesCriteriaBlockTypeDef]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesCriteriaBlockTypeDef]


# SearchResourcesCriteriaBlockTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SearchResourcesCriteriaTypeDef

### simpleCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesSimpleCriterionTypeDef]

### tagCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesTagCriterionTypeDef]


# SearchResourcesRequestRequestTypeDef

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesBucketCriteriaTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesSortCriteriaTypeDef]


# SearchResourcesRequestSearchResourcesPaginateTypeDef

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesBucketCriteriaTypeDef]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesSortCriteriaTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.PaginatorConfigTypeDef]


# SearchResourcesResponseTypeDef

### matchingResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2_classes.MatchingResourceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchResourcesSimpleCriterionTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['EQ', 'NE']]

### key
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'AUTOMATED_DISCOVERY_MONITORING_STATUS', 'S3_BUCKET_EFFECTIVE_PERMISSION', 'S3_BUCKET_NAME', 'S3_BUCKET_SHARED_ACCESS']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# SearchResourcesSortCriteriaTypeDef

### attributeName
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'RESOURCE_NAME', 'S3_CLASSIFIABLE_OBJECT_COUNT', 'S3_CLASSIFIABLE_SIZE_IN_BYTES']]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# SearchResourcesTagCriterionPairTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# SearchResourcesTagCriterionTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['EQ', 'NE']]

### tagValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.SearchResourcesTagCriterionPairTypeDef]]


# SecurityHubConfigurationTypeDef

### publishClassificationFindings
- **Type**: <class 'bool'>
- **Required**: Yes

### publishPolicyFindings
- **Type**: <class 'bool'>
- **Required**: Yes


# SensitiveDataItemTypeDef

### category
- **Type**: typing.Optional[typing.Literal['CREDENTIALS', 'CUSTOM_IDENTIFIER', 'FINANCIAL_INFORMATION', 'PERSONAL_INFORMATION']]

### detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.DefaultDetectionTypeDef]]

### totalCount
- **Type**: typing.Optional[int]


# SensitivityAggregationsTypeDef

### classifiableSizeInBytes
- **Type**: typing.Optional[int]

### publiclyAccessibleCount
- **Type**: typing.Optional[int]

### totalCount
- **Type**: typing.Optional[int]

### totalSizeInBytes
- **Type**: typing.Optional[int]


# SensitivityInspectionTemplateExcludesOutputTypeDef

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]


# SensitivityInspectionTemplateExcludesTypeDef

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.Sequence[str]]


# SensitivityInspectionTemplateIncludesOutputTypeDef

### allowListIds
- **Type**: typing.Optional[typing.List[str]]

### customDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]


# SensitivityInspectionTemplateIncludesTypeDef

### allowListIds
- **Type**: typing.Optional[typing.Sequence[str]]

### customDataIdentifierIds
- **Type**: typing.Optional[typing.Sequence[str]]

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.Sequence[str]]


# SensitivityInspectionTemplatesEntryTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# ServerSideEncryptionTypeDef

### encryptionType
- **Type**: typing.Optional[typing.Literal['AES256', 'NONE', 'UNKNOWN', 'aws:kms', 'aws:kms:dsse']]

### kmsMasterKeyId
- **Type**: typing.Optional[str]


# ServiceLimitTypeDef

### isServiceLimited
- **Type**: typing.Optional[bool]

### unit
- **Type**: typing.Optional[typing.Literal['TERABYTES']]

### value
- **Type**: typing.Optional[int]


# SessionContextAttributesTypeDef

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### mfaAuthenticated
- **Type**: typing.Optional[bool]


# SessionContextTypeDef

### attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SessionContextAttributesTypeDef]

### sessionIssuer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SessionIssuerTypeDef]


# SessionIssuerTypeDef

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### userName
- **Type**: typing.Optional[str]


# SeverityLevelTypeDef

### occurrencesThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### severity
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes


# SeverityTypeDef

### description
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium']]

### score
- **Type**: typing.Optional[int]


# SimpleCriterionForJobOutputTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'S3_BUCKET_EFFECTIVE_PERMISSION', 'S3_BUCKET_NAME', 'S3_BUCKET_SHARED_ACCESS']]

### values
- **Type**: typing.Optional[typing.List[str]]


# SimpleCriterionForJobTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'S3_BUCKET_EFFECTIVE_PERMISSION', 'S3_BUCKET_NAME', 'S3_BUCKET_SHARED_ACCESS']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# SimpleScopeTermOutputTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['OBJECT_EXTENSION', 'OBJECT_KEY', 'OBJECT_LAST_MODIFIED_DATE', 'OBJECT_SIZE']]

### values
- **Type**: typing.Optional[typing.List[str]]


# SimpleScopeTermTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['OBJECT_EXTENSION', 'OBJECT_KEY', 'OBJECT_LAST_MODIFIED_DATE', 'OBJECT_SIZE']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# SortCriteriaTypeDef

### attributeName
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# StatisticsTypeDef

### approximateNumberOfObjectsToProcess
- **Type**: typing.Optional[float]

### numberOfRuns
- **Type**: typing.Optional[float]


# SuppressDataIdentifierTypeDef

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'MANAGED']]


# TagCriterionForJobOutputTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### tagValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.TagCriterionPairForJobTypeDef]]


# TagCriterionForJobTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### tagValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.TagCriterionPairForJobTypeDef]]


# TagCriterionPairForJobTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagScopeTermOutputTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[str]

### tagValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.TagValuePairTypeDef]]

### target
- **Type**: typing.Optional[typing.Literal['S3_OBJECT']]


# TagScopeTermTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[str]

### tagValues
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.TagValuePairTypeDef]]

### target
- **Type**: typing.Optional[typing.Literal['S3_OBJECT']]


# TagValuePairTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TestCustomDataIdentifierRequestRequestTypeDef

### regex
- **Type**: <class 'str'>
- **Required**: Yes

### sampleText
- **Type**: <class 'str'>
- **Required**: Yes

### ignoreWords
- **Type**: typing.Optional[typing.Sequence[str]]

### keywords
- **Type**: typing.Optional[typing.Sequence[str]]

### maximumMatchDistance
- **Type**: typing.Optional[int]


# TestCustomDataIdentifierResponseTypeDef

### matchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UnprocessedAccountTypeDef

### accountId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['ClientError', 'InternalError']]

### errorMessage
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAllowListRequestRequestTypeDef

### criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.AllowListCriteriaTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAllowListResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAutomatedDiscoveryConfigurationRequestRequestTypeDef

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### autoEnableOrganizationMembers
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]


# UpdateClassificationJobRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'IDLE', 'PAUSED', 'RUNNING', 'USER_PAUSED']
- **Required**: Yes


# UpdateClassificationScopeRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.S3ClassificationScopeUpdateTypeDef]


# UpdateFindingsFilterRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'NOOP']]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### findingCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.FindingCriteriaTypeDef]

### name
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[int]


# UpdateFindingsFilterResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMacieSessionRequestRequestTypeDef

### findingPublishingFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']]

### status
- **Type**: typing.Optional[typing.Literal['ENABLED', 'PAUSED']]


# UpdateMemberSessionRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ENABLED', 'PAUSED']
- **Required**: Yes


# UpdateOrganizationConfigurationRequestRequestTypeDef

### autoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateResourceProfileDetectionsRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### suppressDataIdentifiers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.macie2_classes.SuppressDataIdentifierTypeDef]]


# UpdateResourceProfileRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### sensitivityScoreOverride
- **Type**: typing.Optional[int]


# UpdateRetrievalConfigurationTypeDef

### retrievalMode
- **Type**: typing.Literal['ASSUME_ROLE', 'CALLER_CREDENTIALS']
- **Required**: Yes

### roleName
- **Type**: typing.Optional[str]


# UpdateRevealConfigurationRequestRequestTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.RevealConfigurationTypeDef'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.UpdateRetrievalConfigurationTypeDef]


# UpdateRevealConfigurationResponseTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.RevealConfigurationTypeDef'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.RetrievalConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSensitivityInspectionTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SensitivityInspectionTemplateExcludesTypeDef]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.SensitivityInspectionTemplateIncludesTypeDef]


# UsageByAccountTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### estimatedCost
- **Type**: typing.Optional[str]

### serviceLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.ServiceLimitTypeDef]

### type
- **Type**: typing.Optional[typing.Literal['AUTOMATED_OBJECT_MONITORING', 'AUTOMATED_SENSITIVE_DATA_DISCOVERY', 'DATA_INVENTORY_EVALUATION', 'SENSITIVE_DATA_DISCOVERY']]


# UsageRecordTypeDef

### accountId
- **Type**: typing.Optional[str]

### automatedDiscoveryFreeTrialStartDate
- **Type**: typing.Optional[datetime.datetime]

### freeTrialStartDate
- **Type**: typing.Optional[datetime.datetime]

### usage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2_classes.UsageByAccountTypeDef]]


# UsageStatisticsFilterTypeDef

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE']]

### key
- **Type**: typing.Optional[typing.Literal['accountId', 'freeTrialStartDate', 'serviceLimit', 'total']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# UsageStatisticsSortByTypeDef

### key
- **Type**: typing.Optional[typing.Literal['accountId', 'freeTrialStartDate', 'serviceLimitValue', 'total']]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# UsageTotalTypeDef

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### estimatedCost
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AUTOMATED_OBJECT_MONITORING', 'AUTOMATED_SENSITIVE_DATA_DISCOVERY', 'DATA_INVENTORY_EVALUATION', 'SENSITIVE_DATA_DISCOVERY']]


# UserIdentityRootTypeDef

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]


# UserIdentityTypeDef

### assumedRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.AssumedRoleTypeDef]

### awsAccount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.AwsAccountTypeDef]

### awsService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.AwsServiceTypeDef]

### federatedUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.FederatedUserTypeDef]

### iamUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.IamUserTypeDef]

### root
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2_classes.UserIdentityRootTypeDef]

### type
- **Type**: typing.Optional[typing.Literal['AWSAccount', 'AWSService', 'AssumedRole', 'FederatedUser', 'IAMUser', 'Root']]


# UserPausedDetailsTypeDef

### jobExpiresAt
- **Type**: typing.Optional[datetime.datetime]

### jobImminentExpirationHealthEventArn
- **Type**: typing.Optional[str]

### jobPausedAt
- **Type**: typing.Optional[datetime.datetime]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WeeklyScheduleTypeDef

### dayOfWeek
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]



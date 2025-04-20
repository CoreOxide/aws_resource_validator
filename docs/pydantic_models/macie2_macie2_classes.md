# Macie2 Macie2 Classes

# AcceptInvitationRequest

### invitationId
- **Type**: <class 'str'>
- **Required**: Yes

### administratorAccountId
- **Type**: typing.Optional[str]

### masterAccount
- **Type**: typing.Optional[str]


# AccessControlList

### allowsPublicReadAccess
- **Type**: typing.Optional[bool]

### allowsPublicWriteAccess
- **Type**: typing.Optional[bool]


# AccountDetail

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes


# AccountLevelPermissions

### blockPublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BlockPublicAccess]


# AdminAccount

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLING_IN_PROGRESS', 'ENABLED']]


# AllowListCriteria

### regex
- **Type**: typing.Optional[str]

### s3WordsList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3WordsList]


# AllowListStatus

### code
- **Type**: typing.Literal['OK', 'S3_OBJECT_ACCESS_DENIED', 'S3_OBJECT_EMPTY', 'S3_OBJECT_NOT_FOUND', 'S3_OBJECT_OVERSIZE', 'S3_THROTTLED', 'S3_USER_ACCESS_DENIED', 'UNKNOWN_ERROR']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# AllowListSummary

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


# ApiCallDetails

### api
- **Type**: typing.Optional[str]

### apiServiceName
- **Type**: typing.Optional[str]

### firstSeen
- **Type**: typing.Optional[datetime.datetime]

### lastSeen
- **Type**: typing.Optional[datetime.datetime]


# AssumedRole

### accessKeyId
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### sessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SessionContext]


# AutomatedDiscoveryAccount

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AutomatedDiscoveryAccountUpdate

### accountId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AutomatedDiscoveryAccountUpdateError

### accountId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['ACCOUNT_NOT_FOUND', 'ACCOUNT_PAUSED']]


# AwsAccount

### accountId
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]


# AwsService

### invokedBy
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetCustomDataIdentifierSummary

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


# BatchGetCustomDataIdentifiersRequest

### ids
- **Type**: typing.Optional[typing.List[str]]


# BatchGetCustomDataIdentifiersResponse

### customDataIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.BatchGetCustomDataIdentifierSummary]
- **Required**: Yes

### notFoundIdentifierIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateAutomatedDiscoveryAccountsRequest

### accounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.AutomatedDiscoveryAccountUpdate]]


# BatchUpdateAutomatedDiscoveryAccountsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.AutomatedDiscoveryAccountUpdateError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# BlockPublicAccess

### blockPublicAcls
- **Type**: typing.Optional[bool]

### blockPublicPolicy
- **Type**: typing.Optional[bool]

### ignorePublicAcls
- **Type**: typing.Optional[bool]

### restrictPublicBuckets
- **Type**: typing.Optional[bool]


# BucketCountByEffectivePermission

### publiclyAccessible
- **Type**: typing.Optional[int]

### publiclyReadable
- **Type**: typing.Optional[int]

### publiclyWritable
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# BucketCountByEncryptionType

### kmsManaged
- **Type**: typing.Optional[int]

### s3Managed
- **Type**: typing.Optional[int]

### unencrypted
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# BucketCountBySharedAccessType

### external
- **Type**: typing.Optional[int]

### internal
- **Type**: typing.Optional[int]

### notShared
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# BucketCountPolicyAllowsUnencryptedObjectUploads

### allowsUnencryptedObjectUploads
- **Type**: typing.Optional[int]

### deniesUnencryptedObjectUploads
- **Type**: typing.Optional[int]

### unknown
- **Type**: typing.Optional[int]


# BucketCriteriaAdditionalProperties

### eq
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

### prefix
- **Type**: typing.Optional[str]


# BucketLevelPermissions

### accessControlList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.AccessControlList]

### blockPublicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BlockPublicAccess]

### bucketPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketPolicy]


# BucketMetadata

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
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'BUCKET_COUNT_EXCEEDS_QUOTA']]

### errorMessage
- **Type**: typing.Optional[str]

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobDetails]

### lastAutomatedDiscoveryTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdated
- **Type**: typing.Optional[datetime.datetime]

### objectCount
- **Type**: typing.Optional[int]

### objectCountByEncryptionType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ObjectCountByEncryptionType]

### publicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketPublicAccess]

### region
- **Type**: typing.Optional[str]

### replicationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ReplicationDetails]

### sensitivityScore
- **Type**: typing.Optional[int]

### serverSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketServerSideEncryption]

### sharedAccess
- **Type**: typing.Optional[typing.Literal['EXTERNAL', 'INTERNAL', 'NOT_SHARED', 'UNKNOWN']]

### sizeInBytes
- **Type**: typing.Optional[int]

### sizeInBytesCompressed
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.KeyValuePair]]

### unclassifiableObjectCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ObjectLevelStatistics]

### unclassifiableObjectSizeInBytes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ObjectLevelStatistics]

### versioning
- **Type**: typing.Optional[bool]


# BucketPermissionConfiguration

### accountLevelPermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.AccountLevelPermissions]

### bucketLevelPermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketLevelPermissions]


# BucketPolicy

### allowsPublicReadAccess
- **Type**: typing.Optional[bool]

### allowsPublicWriteAccess
- **Type**: typing.Optional[bool]


# BucketPublicAccess

### effectivePermission
- **Type**: typing.Optional[typing.Literal['NOT_PUBLIC', 'PUBLIC', 'UNKNOWN']]

### permissionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketPermissionConfiguration]


# BucketServerSideEncryption

### kmsMasterKeyId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AES256', 'NONE', 'aws:kms', 'aws:kms:dsse']]


# BucketSortCriteria

### attributeName
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# BucketStatisticsBySensitivity

### classificationError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityAggregations]

### notClassified
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityAggregations]

### notSensitive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityAggregations]

### sensitive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityAggregations]


# Cell

### cellReference
- **Type**: typing.Optional[str]

### column
- **Type**: typing.Optional[int]

### columnName
- **Type**: typing.Optional[str]

### row
- **Type**: typing.Optional[int]


# ClassificationDetails

### detailedResultsLocation
- **Type**: typing.Optional[str]

### jobArn
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]

### originType
- **Type**: typing.Optional[typing.Literal['AUTOMATED_SENSITIVE_DATA_DISCOVERY', 'SENSITIVE_DATA_DISCOVERY_JOB']]

### result
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ClassificationResult]


# ClassificationExportConfiguration

### s3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3Destination]


# ClassificationResult

### additionalOccurrences
- **Type**: typing.Optional[bool]

### customDataIdentifiers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.CustomDataIdentifiers]

### mimeType
- **Type**: typing.Optional[str]

### sensitiveData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitiveDataItem]]

### sizeClassified
- **Type**: typing.Optional[int]

### status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ClassificationResultStatus]


# ClassificationResultStatus

### code
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# ClassificationScopeSummary

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# CreateAllowListRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.AllowListCriteria'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAllowListResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateClassificationJobRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3JobDefinition, aws_resource_validator.pydantic_models.macie2.macie2_classes.S3JobDefinitionOutput]
- **Required**: Yes

### allowListIds
- **Type**: typing.Optional[typing.List[str]]

### customDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### initialRun
- **Type**: typing.Optional[bool]

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]

### managedDataIdentifierSelector
- **Type**: typing.Optional[typing.Literal['ALL', 'EXCLUDE', 'INCLUDE', 'NONE', 'RECOMMENDED']]

### samplingPercentage
- **Type**: typing.Optional[int]

### scheduleFrequency
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScheduleFrequency, aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScheduleFrequencyOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateClassificationJobResponse

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomDataIdentifierRequest

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
- **Type**: typing.Optional[typing.List[str]]

### keywords
- **Type**: typing.Optional[typing.List[str]]

### maximumMatchDistance
- **Type**: typing.Optional[int]

### severityLevels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.SeverityLevel]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCustomDataIdentifierResponse

### customDataIdentifierId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFindingsFilterRequest

### action
- **Type**: typing.Literal['ARCHIVE', 'NOOP']
- **Required**: Yes

### findingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteria, aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteriaOutput]
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateFindingsFilterResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInvitationsRequest

### accountIds
- **Type**: typing.List[str]
- **Required**: Yes

### disableEmailNotification
- **Type**: typing.Optional[bool]

### message
- **Type**: typing.Optional[str]


# CreateInvitationsResponse

### unprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMemberRequest

### account
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.AccountDetail'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMemberResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSampleFindingsRequest

### findingTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Policy:IAMUser/S3BlockPublicAccessDisabled', 'Policy:IAMUser/S3BucketEncryptionDisabled', 'Policy:IAMUser/S3BucketPublic', 'Policy:IAMUser/S3BucketReplicatedExternally', 'Policy:IAMUser/S3BucketSharedExternally', 'Policy:IAMUser/S3BucketSharedWithCloudFront', 'SensitiveData:S3Object/Credentials', 'SensitiveData:S3Object/CustomIdentifier', 'SensitiveData:S3Object/Financial', 'SensitiveData:S3Object/Multiple', 'SensitiveData:S3Object/Personal']]]


# CriteriaBlockForJob

### and_
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.CriteriaForJob]]


# CriteriaBlockForJobOutput

### and_
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.CriteriaForJobOutput]]


# CriteriaForJob

### simpleCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SimpleCriterionForJob]

### tagCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.TagCriterionForJob]


# CriteriaForJobOutput

### simpleCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SimpleCriterionForJobOutput]

### tagCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.TagCriterionForJobOutput]


# CriterionAdditionalProperties

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


# CriterionAdditionalPropertiesOutput

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


# CustomDataIdentifierSummary

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


# CustomDataIdentifiers

### detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.CustomDetection]]

### totalCount
- **Type**: typing.Optional[int]


# CustomDetection

### arn
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.Occurrences]


# DeclineInvitationsRequest

### accountIds
- **Type**: typing.List[str]
- **Required**: Yes


# DeclineInvitationsResponse

### unprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# DefaultDetection

### count
- **Type**: typing.Optional[int]

### occurrences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.Occurrences]

### type
- **Type**: typing.Optional[str]


# DeleteAllowListRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ignoreJobChecks
- **Type**: typing.Optional[str]


# DeleteCustomDataIdentifierRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFindingsFilterRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInvitationsRequest

### accountIds
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteInvitationsResponse

### unprocessedAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.UnprocessedAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMemberRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBucketsRequest

### criteria
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketCriteriaAdditionalProperties]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketSortCriteria]


# DescribeBucketsRequestPaginate

### criteria
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketCriteriaAdditionalProperties]]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketSortCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# DescribeBucketsResponse

### buckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeClassificationJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClassificationJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.LastRunErrorStatus'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.S3JobDefinitionOutput'>
- **Required**: Yes

### samplingPercentage
- **Type**: <class 'int'>
- **Required**: Yes

### scheduleFrequency
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScheduleFrequencyOutput'>
- **Required**: Yes

### statistics
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.Statistics'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### userPausedDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.UserPausedDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationConfigurationResponse

### autoEnable
- **Type**: <class 'bool'>
- **Required**: Yes

### maxAccountLimitReached
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# DetectedDataDetails

### value
- **Type**: <class 'str'>
- **Required**: Yes


# Detection

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


# DisableOrganizationAdminAccountRequest

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DomainDetails

### domainName
- **Type**: typing.Optional[str]


# EnableMacieRequest

### clientToken
- **Type**: typing.Optional[str]

### findingPublishingFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']]

### status
- **Type**: typing.Optional[typing.Literal['ENABLED', 'PAUSED']]


# EnableOrganizationAdminAccountRequest

### adminAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# FederatedUser

### accessKeyId
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### sessionContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SessionContext]


# Finding

### accountId
- **Type**: typing.Optional[str]

### archived
- **Type**: typing.Optional[bool]

### category
- **Type**: typing.Optional[typing.Literal['CLASSIFICATION', 'POLICY']]

### classificationDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ClassificationDetails]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PolicyDetails]

### region
- **Type**: typing.Optional[str]

### resourcesAffected
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ResourcesAffected]

### sample
- **Type**: typing.Optional[bool]

### schemaVersion
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.Severity]

### title
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Policy:IAMUser/S3BlockPublicAccessDisabled', 'Policy:IAMUser/S3BucketEncryptionDisabled', 'Policy:IAMUser/S3BucketPublic', 'Policy:IAMUser/S3BucketReplicatedExternally', 'Policy:IAMUser/S3BucketSharedExternally', 'Policy:IAMUser/S3BucketSharedWithCloudFront', 'SensitiveData:S3Object/Credentials', 'SensitiveData:S3Object/CustomIdentifier', 'SensitiveData:S3Object/Financial', 'SensitiveData:S3Object/Multiple', 'SensitiveData:S3Object/Personal']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# FindingAction

### actionType
- **Type**: typing.Optional[typing.Literal['AWS_API_CALL']]

### apiCallDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ApiCallDetails]


# FindingActor

### domainDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.DomainDetails]

### ipAddressDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.IpAddressDetails]

### userIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.UserIdentity]


# FindingCriteria

### criterion
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.macie2.macie2_classes.CriterionAdditionalProperties]]


# FindingCriteriaOutput

### criterion
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.macie2.macie2_classes.CriterionAdditionalPropertiesOutput]]


# FindingStatisticsSortCriteria

### attributeName
- **Type**: typing.Optional[typing.Literal['count', 'groupKey']]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# FindingsFilterListItem

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


# GetAdministratorAccountResponse

### administrator
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.Invitation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetAllowListRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetAllowListResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.AllowListCriteria'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.AllowListStatus'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetAutomatedDiscoveryConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetBucketStatisticsRequest

### accountId
- **Type**: typing.Optional[str]


# GetBucketStatisticsResponse

### bucketCount
- **Type**: <class 'int'>
- **Required**: Yes

### bucketCountByEffectivePermission
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketCountByEffectivePermission'>
- **Required**: Yes

### bucketCountByEncryptionType
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketCountByEncryptionType'>
- **Required**: Yes

### bucketCountByObjectEncryptionRequirement
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketCountPolicyAllowsUnencryptedObjectUploads'>
- **Required**: Yes

### bucketCountBySharedAccessType
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketCountBySharedAccessType'>
- **Required**: Yes

### bucketStatisticsBySensitivity
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketStatisticsBySensitivity'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ObjectLevelStatistics'>
- **Required**: Yes

### unclassifiableObjectSizeInBytes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ObjectLevelStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetClassificationExportConfigurationResponse

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ClassificationExportConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetClassificationScopeRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetClassificationScopeResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### s3
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.S3ClassificationScope'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetCustomDataIdentifierRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCustomDataIdentifierResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.SeverityLevel]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingStatisticsRequest

### groupBy
- **Type**: typing.Literal['classificationDetails.jobId', 'resourcesAffected.s3Bucket.name', 'severity.description', 'type']
- **Required**: Yes

### findingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteria, aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteriaOutput, NoneType]

### size
- **Type**: typing.Optional[int]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingStatisticsSortCriteria]


# GetFindingStatisticsResponse

### countsByGroup
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.GroupCount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingsFilterRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetFindingsFilterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteriaOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingsPublicationConfigurationResponse

### securityHubConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.SecurityHubConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetFindingsRequest

### findingIds
- **Type**: typing.List[str]
- **Required**: Yes

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SortCriteria]


# GetFindingsResponse

### findings
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Finding]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetInvitationsCountResponse

### invitationsCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetMacieSessionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetMasterAccountResponse

### master
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.Invitation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetMemberRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMemberResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceProfileRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceProfileResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResourceStatistics'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetRevealConfigurationResponse

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.RevealConfiguration'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.RetrievalConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetSensitiveDataOccurrencesAvailabilityRequest

### findingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSensitiveDataOccurrencesAvailabilityResponse

### code
- **Type**: typing.Literal['AVAILABLE', 'UNAVAILABLE']
- **Required**: Yes

### reasons
- **Type**: typing.List[typing.Literal['ACCOUNT_NOT_IN_ORGANIZATION', 'INVALID_CLASSIFICATION_RESULT', 'INVALID_RESULT_SIGNATURE', 'MEMBER_ROLE_TOO_PERMISSIVE', 'MISSING_GET_MEMBER_PERMISSION', 'OBJECT_EXCEEDS_SIZE_QUOTA', 'OBJECT_UNAVAILABLE', 'RESULT_NOT_SIGNED', 'ROLE_TOO_PERMISSIVE', 'UNSUPPORTED_FINDING_TYPE', 'UNSUPPORTED_OBJECT_TYPE']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetSensitiveDataOccurrencesRequest

### findingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSensitiveDataOccurrencesRequestWait

### findingId
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetSensitiveDataOccurrencesResponse

### error
- **Type**: <class 'str'>
- **Required**: Yes

### sensitiveDataOccurrences
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.DetectedDataDetails]]
- **Required**: Yes

### status
- **Type**: typing.Literal['ERROR', 'PROCESSING', 'SUCCESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetSensitivityInspectionTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSensitivityInspectionTemplateResponse

### description
- **Type**: <class 'str'>
- **Required**: Yes

### excludes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityInspectionTemplateExcludesOutput'>
- **Required**: Yes

### includes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityInspectionTemplateIncludesOutput'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sensitivityInspectionTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GetUsageStatisticsRequest

### filterBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.UsageStatisticsFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.UsageStatisticsSortBy]

### timeRange
- **Type**: typing.Optional[typing.Literal['MONTH_TO_DATE', 'PAST_30_DAYS']]


# GetUsageStatisticsRequestPaginate

### filterBy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.UsageStatisticsFilter]]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.UsageStatisticsSortBy]

### timeRange
- **Type**: typing.Optional[typing.Literal['MONTH_TO_DATE', 'PAST_30_DAYS']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# GetUsageStatisticsResponse

### records
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.UsageRecord]
- **Required**: Yes

### timeRange
- **Type**: typing.Literal['MONTH_TO_DATE', 'PAST_30_DAYS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetUsageTotalsRequest

### timeRange
- **Type**: typing.Optional[str]


# GetUsageTotalsResponse

### timeRange
- **Type**: typing.Literal['MONTH_TO_DATE', 'PAST_30_DAYS']
- **Required**: Yes

### usageTotals
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.UsageTotal]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# GroupCount

### count
- **Type**: typing.Optional[int]

### groupKey
- **Type**: typing.Optional[str]


# IamUser

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]

### userName
- **Type**: typing.Optional[str]


# Invitation

### accountId
- **Type**: typing.Optional[str]

### invitationId
- **Type**: typing.Optional[str]

### invitedAt
- **Type**: typing.Optional[datetime.datetime]

### relationshipStatus
- **Type**: typing.Optional[typing.Literal['AccountSuspended', 'Created', 'EmailVerificationFailed', 'EmailVerificationInProgress', 'Enabled', 'Invited', 'Paused', 'RegionDisabled', 'Removed', 'Resigned']]


# IpAddressDetails

### ipAddressV4
- **Type**: typing.Optional[str]

### ipCity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.IpCity]

### ipCountry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.IpCountry]

### ipGeoLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.IpGeoLocation]

### ipOwner
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.IpOwner]


# IpCity

### name
- **Type**: typing.Optional[str]


# IpCountry

### code
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# IpGeoLocation

### lat
- **Type**: typing.Optional[float]

### lon
- **Type**: typing.Optional[float]


# IpOwner

### asn
- **Type**: typing.Optional[str]

### asnOrg
- **Type**: typing.Optional[str]

### isp
- **Type**: typing.Optional[str]

### org
- **Type**: typing.Optional[str]


# JobDetails

### isDefinedInJob
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE', 'UNKNOWN']]

### isMonitoredByJob
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE', 'UNKNOWN']]

### lastJobId
- **Type**: typing.Optional[str]

### lastJobRunTime
- **Type**: typing.Optional[datetime.datetime]


# JobScheduleFrequency

### dailySchedule
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### monthlySchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.MonthlySchedule]

### weeklySchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.WeeklySchedule]


# JobScheduleFrequencyOutput

### dailySchedule
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### monthlySchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.MonthlySchedule]

### weeklySchedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.WeeklySchedule]


# JobScopeTerm

### simpleScopeTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SimpleScopeTerm]

### tagScopeTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.TagScopeTerm]


# JobScopeTermOutput

### simpleScopeTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SimpleScopeTermOutput]

### tagScopeTerm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.TagScopeTermOutput]


# JobScopingBlock

### and_
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScopeTerm]]


# JobScopingBlockOutput

### and_
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScopeTermOutput]]


# JobSummary

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3BucketCriteriaForJobOutput]

### bucketDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3BucketDefinitionForJobOutput]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### jobId
- **Type**: typing.Optional[str]

### jobStatus
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETE', 'IDLE', 'PAUSED', 'RUNNING', 'USER_PAUSED']]

### jobType
- **Type**: typing.Optional[typing.Literal['ONE_TIME', 'SCHEDULED']]

### lastRunErrorStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.LastRunErrorStatus]

### name
- **Type**: typing.Optional[str]

### userPausedDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.UserPausedDetails]


# KeyValuePair

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# LastRunErrorStatus

### code
- **Type**: typing.Optional[typing.Literal['ERROR', 'NONE']]


# ListAllowListsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAllowListsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListAllowListsResponse

### allowLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.AllowListSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAutomatedDiscoveryAccountsRequest

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAutomatedDiscoveryAccountsRequestPaginate

### accountIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListAutomatedDiscoveryAccountsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.AutomatedDiscoveryAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListClassificationJobsRequest

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ListJobsFilterCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ListJobsSortCriteria]


# ListClassificationJobsRequestPaginate

### filterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ListJobsFilterCriteria]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ListJobsSortCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListClassificationJobsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListClassificationScopesRequest

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListClassificationScopesRequestPaginate

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListClassificationScopesResponse

### classificationScopes
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.ClassificationScopeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListCustomDataIdentifiersRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListCustomDataIdentifiersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListCustomDataIdentifiersResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.CustomDataIdentifierSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsFiltersRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsFiltersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListFindingsFiltersResponse

### findingsFilterListItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingsFilterListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsRequest

### findingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteria, aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteriaOutput, NoneType]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SortCriteria]


# ListFindingsRequestPaginate

### findingCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteria, aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteriaOutput, NoneType]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SortCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListFindingsResponse

### findingIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInvitationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListInvitationsResponse

### invitations
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Invitation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobsFilterCriteria

### excludes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.ListJobsFilterTerm]]

### includes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.ListJobsFilterTerm]]


# ListJobsFilterTerm

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['createdAt', 'jobStatus', 'jobType', 'name']]

### values
- **Type**: typing.Optional[typing.List[str]]


# ListJobsSortCriteria

### attributeName
- **Type**: typing.Optional[typing.Literal['createdAt', 'jobStatus', 'jobType', 'name']]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# ListManagedDataIdentifiersRequest

### nextToken
- **Type**: typing.Optional[str]


# ListManagedDataIdentifiersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListManagedDataIdentifiersResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.ManagedDataIdentifierSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMembersRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### onlyAssociated
- **Type**: typing.Optional[str]


# ListMembersRequestPaginate

### onlyAssociated
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListMembersResponse

### members
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Member]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListOrganizationAdminAccountsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListOrganizationAdminAccountsResponse

### adminAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.AdminAccount]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceProfileArtifactsRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceProfileArtifactsRequestPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListResourceProfileArtifactsResponse

### artifacts
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.ResourceProfileArtifact]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListResourceProfileDetectionsRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListResourceProfileDetectionsRequestPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListResourceProfileDetectionsResponse

### detections
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Detection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSensitivityInspectionTemplatesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSensitivityInspectionTemplatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# ListSensitivityInspectionTemplatesResponse

### sensitivityInspectionTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityInspectionTemplatesEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# ManagedDataIdentifierSummary

### category
- **Type**: typing.Optional[typing.Literal['CREDENTIALS', 'CUSTOM_IDENTIFIER', 'FINANCIAL_INFORMATION', 'PERSONAL_INFORMATION']]

### id
- **Type**: typing.Optional[str]


# MatchingBucket

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
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'BUCKET_COUNT_EXCEEDS_QUOTA']]

### errorMessage
- **Type**: typing.Optional[str]

### jobDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobDetails]

### lastAutomatedDiscoveryTime
- **Type**: typing.Optional[datetime.datetime]

### objectCount
- **Type**: typing.Optional[int]

### objectCountByEncryptionType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ObjectCountByEncryptionType]

### sensitivityScore
- **Type**: typing.Optional[int]

### sizeInBytes
- **Type**: typing.Optional[int]

### sizeInBytesCompressed
- **Type**: typing.Optional[int]

### unclassifiableObjectCount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ObjectLevelStatistics]

### unclassifiableObjectSizeInBytes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ObjectLevelStatistics]


# MatchingResource

### matchingBucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.MatchingBucket]


# Member

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


# MonthlySchedule

### dayOfMonth
- **Type**: typing.Optional[int]


# ObjectCountByEncryptionType

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


# ObjectLevelStatistics

### fileType
- **Type**: typing.Optional[int]

### storageClass
- **Type**: typing.Optional[int]

### total
- **Type**: typing.Optional[int]


# Occurrences

### cells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Cell]]

### lineRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Range]]

### offsetRanges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Range]]

### pages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Page]]

### records
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.Record]]


# Page

### lineRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.Range]

### offsetRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.Range]

### pageNumber
- **Type**: typing.Optional[int]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PolicyDetails

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingAction]

### actor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingActor]


# PutClassificationExportConfigurationRequest

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ClassificationExportConfiguration'>
- **Required**: Yes


# PutClassificationExportConfigurationResponse

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ClassificationExportConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# PutFindingsPublicationConfigurationRequest

### clientToken
- **Type**: typing.Optional[str]

### securityHubConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SecurityHubConfiguration]


# Range

### end
- **Type**: typing.Optional[int]

### start
- **Type**: typing.Optional[int]

### startColumn
- **Type**: typing.Optional[int]


# Record

### jsonPath
- **Type**: typing.Optional[str]

### recordIndex
- **Type**: typing.Optional[int]


# ReplicationDetails

### replicated
- **Type**: typing.Optional[bool]

### replicatedExternally
- **Type**: typing.Optional[bool]

### replicationAccounts
- **Type**: typing.Optional[typing.List[str]]


# ResourceProfileArtifact

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### classificationResultStatus
- **Type**: <class 'str'>
- **Required**: Yes

### sensitive
- **Type**: typing.Optional[bool]


# ResourceStatistics

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


# ResourcesAffected

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3Bucket]

### s3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3Object]


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


# RetrievalConfiguration

### retrievalMode
- **Type**: typing.Literal['ASSUME_ROLE', 'CALLER_CREDENTIALS']
- **Required**: Yes

### externalId
- **Type**: typing.Optional[str]

### roleName
- **Type**: typing.Optional[str]


# RevealConfiguration

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]


# S3Bucket

### allowsUnencryptedObjectUploads
- **Type**: typing.Optional[typing.Literal['FALSE', 'TRUE', 'UNKNOWN']]

### arn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### defaultServerSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ServerSideEncryption]

### name
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3BucketOwner]

### publicAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.BucketPublicAccess]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.KeyValuePair]]


# S3BucketCriteriaForJob

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.CriteriaBlockForJob]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.CriteriaBlockForJob]


# S3BucketCriteriaForJobOutput

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.CriteriaBlockForJobOutput]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.CriteriaBlockForJobOutput]


# S3BucketDefinitionForJob

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### buckets
- **Type**: typing.List[str]
- **Required**: Yes


# S3BucketDefinitionForJobOutput

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### buckets
- **Type**: typing.List[str]
- **Required**: Yes


# S3BucketOwner

### displayName
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]


# S3ClassificationScope

### excludes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.S3ClassificationScopeExclusion'>
- **Required**: Yes


# S3ClassificationScopeExclusion

### bucketNames
- **Type**: typing.List[str]
- **Required**: Yes


# S3ClassificationScopeExclusionUpdate

### bucketNames
- **Type**: typing.List[str]
- **Required**: Yes

### operation
- **Type**: typing.Literal['ADD', 'REMOVE', 'REPLACE']
- **Required**: Yes


# S3ClassificationScopeUpdate

### excludes
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.S3ClassificationScopeExclusionUpdate'>
- **Required**: Yes


# S3Destination

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### keyPrefix
- **Type**: typing.Optional[str]


# S3JobDefinition

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3BucketCriteriaForJob]

### bucketDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3BucketDefinitionForJob]]

### scoping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.Scoping]


# S3JobDefinitionOutput

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3BucketCriteriaForJobOutput]

### bucketDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3BucketDefinitionForJobOutput]]

### scoping
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ScopingOutput]


# S3Object

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ServerSideEncryption]

### size
- **Type**: typing.Optional[int]

### storageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_IR', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'OUTPOSTS', 'REDUCED_REDUNDANCY', 'STANDARD', 'STANDARD_IA']]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.KeyValuePair]]

### versionId
- **Type**: typing.Optional[str]


# S3WordsList

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### objectKey
- **Type**: <class 'str'>
- **Required**: Yes


# Scoping

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScopingBlock]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScopingBlock]


# ScopingOutput

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScopingBlockOutput]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.JobScopingBlockOutput]


# SearchResourcesBucketCriteria

### excludes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesCriteriaBlock]

### includes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesCriteriaBlock]


# SearchResourcesCriteria

### simpleCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesSimpleCriterion]

### tagCriterion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesTagCriterion]


# SearchResourcesCriteriaBlock

### and_
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesCriteria]]


# SearchResourcesRequest

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesBucketCriteria]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesSortCriteria]


# SearchResourcesRequestPaginate

### bucketCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesBucketCriteria]

### sortCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesSortCriteria]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.PaginatorConfig]


# SearchResourcesResponse

### matchingResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.MatchingResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchResourcesSimpleCriterion

### comparator
- **Type**: typing.Optional[typing.Literal['EQ', 'NE']]

### key
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'AUTOMATED_DISCOVERY_MONITORING_STATUS', 'S3_BUCKET_EFFECTIVE_PERMISSION', 'S3_BUCKET_NAME', 'S3_BUCKET_SHARED_ACCESS']]

### values
- **Type**: typing.Optional[typing.List[str]]


# SearchResourcesSortCriteria

### attributeName
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'RESOURCE_NAME', 'S3_CLASSIFIABLE_OBJECT_COUNT', 'S3_CLASSIFIABLE_SIZE_IN_BYTES']]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# SearchResourcesTagCriterion

### comparator
- **Type**: typing.Optional[typing.Literal['EQ', 'NE']]

### tagValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.SearchResourcesTagCriterionPair]]


# SearchResourcesTagCriterionPair

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# SecurityHubConfiguration

### publishClassificationFindings
- **Type**: <class 'bool'>
- **Required**: Yes

### publishPolicyFindings
- **Type**: <class 'bool'>
- **Required**: Yes


# SensitiveDataItem

### category
- **Type**: typing.Optional[typing.Literal['CREDENTIALS', 'CUSTOM_IDENTIFIER', 'FINANCIAL_INFORMATION', 'PERSONAL_INFORMATION']]

### detections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.DefaultDetection]]

### totalCount
- **Type**: typing.Optional[int]


# SensitivityAggregations

### classifiableSizeInBytes
- **Type**: typing.Optional[int]

### publiclyAccessibleCount
- **Type**: typing.Optional[int]

### totalCount
- **Type**: typing.Optional[int]

### totalSizeInBytes
- **Type**: typing.Optional[int]


# SensitivityInspectionTemplateExcludes

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]


# SensitivityInspectionTemplateExcludesOutput

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]


# SensitivityInspectionTemplateIncludes

### allowListIds
- **Type**: typing.Optional[typing.List[str]]

### customDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]


# SensitivityInspectionTemplateIncludesOutput

### allowListIds
- **Type**: typing.Optional[typing.List[str]]

### customDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]

### managedDataIdentifierIds
- **Type**: typing.Optional[typing.List[str]]


# SensitivityInspectionTemplatesEntry

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# ServerSideEncryption

### encryptionType
- **Type**: typing.Optional[typing.Literal['AES256', 'NONE', 'UNKNOWN', 'aws:kms', 'aws:kms:dsse']]

### kmsMasterKeyId
- **Type**: typing.Optional[str]


# ServiceLimit

### isServiceLimited
- **Type**: typing.Optional[bool]

### unit
- **Type**: typing.Optional[typing.Literal['TERABYTES']]

### value
- **Type**: typing.Optional[int]


# SessionContext

### attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SessionContextAttributes]

### sessionIssuer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.SessionIssuer]


# SessionContextAttributes

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### mfaAuthenticated
- **Type**: typing.Optional[bool]


# SessionIssuer

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


# Severity

### description
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium']]

### score
- **Type**: typing.Optional[int]


# SeverityLevel

### occurrencesThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### severity
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM']
- **Required**: Yes


# SimpleCriterionForJob

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'S3_BUCKET_EFFECTIVE_PERMISSION', 'S3_BUCKET_NAME', 'S3_BUCKET_SHARED_ACCESS']]

### values
- **Type**: typing.Optional[typing.List[str]]


# SimpleCriterionForJobOutput

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['ACCOUNT_ID', 'S3_BUCKET_EFFECTIVE_PERMISSION', 'S3_BUCKET_NAME', 'S3_BUCKET_SHARED_ACCESS']]

### values
- **Type**: typing.Optional[typing.List[str]]


# SimpleScopeTerm

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['OBJECT_EXTENSION', 'OBJECT_KEY', 'OBJECT_LAST_MODIFIED_DATE', 'OBJECT_SIZE']]

### values
- **Type**: typing.Optional[typing.List[str]]


# SimpleScopeTermOutput

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[typing.Literal['OBJECT_EXTENSION', 'OBJECT_KEY', 'OBJECT_LAST_MODIFIED_DATE', 'OBJECT_SIZE']]

### values
- **Type**: typing.Optional[typing.List[str]]


# SortCriteria

### attributeName
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# Statistics

### approximateNumberOfObjectsToProcess
- **Type**: typing.Optional[float]

### numberOfRuns
- **Type**: typing.Optional[float]


# SuppressDataIdentifier

### id
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['CUSTOM', 'MANAGED']]


# TagCriterionForJob

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### tagValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.TagCriterionPairForJob]]


# TagCriterionForJobOutput

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### tagValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.TagCriterionPairForJob]]


# TagCriterionPairForJob

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagScopeTerm

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[str]

### tagValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.TagValuePair]]

### target
- **Type**: typing.Optional[typing.Literal['S3_OBJECT']]


# TagScopeTermOutput

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE', 'STARTS_WITH']]

### key
- **Type**: typing.Optional[str]

### tagValues
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.TagValuePair]]

### target
- **Type**: typing.Optional[typing.Literal['S3_OBJECT']]


# TagValuePair

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TestCustomDataIdentifierRequest

### regex
- **Type**: <class 'str'>
- **Required**: Yes

### sampleText
- **Type**: <class 'str'>
- **Required**: Yes

### ignoreWords
- **Type**: typing.Optional[typing.List[str]]

### keywords
- **Type**: typing.Optional[typing.List[str]]

### maximumMatchDistance
- **Type**: typing.Optional[int]


# TestCustomDataIdentifierResponse

### matchCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# UnprocessedAccount

### accountId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['ClientError', 'InternalError']]

### errorMessage
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAllowListRequest

### criteria
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.AllowListCriteria'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateAllowListResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAutomatedDiscoveryConfigurationRequest

### status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### autoEnableOrganizationMembers
- **Type**: typing.Optional[typing.Literal['ALL', 'NEW', 'NONE']]


# UpdateClassificationJobRequest

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### jobStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'IDLE', 'PAUSED', 'RUNNING', 'USER_PAUSED']
- **Required**: Yes


# UpdateClassificationScopeRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.S3ClassificationScopeUpdate]


# UpdateFindingsFilterRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteria, aws_resource_validator.pydantic_models.macie2.macie2_classes.FindingCriteriaOutput, NoneType]

### name
- **Type**: typing.Optional[str]

### position
- **Type**: typing.Optional[int]


# UpdateFindingsFilterResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMacieSessionRequest

### findingPublishingFrequency
- **Type**: typing.Optional[typing.Literal['FIFTEEN_MINUTES', 'ONE_HOUR', 'SIX_HOURS']]

### status
- **Type**: typing.Optional[typing.Literal['ENABLED', 'PAUSED']]


# UpdateMemberSessionRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ENABLED', 'PAUSED']
- **Required**: Yes


# UpdateOrganizationConfigurationRequest

### autoEnable
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateResourceProfileDetectionsRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### suppressDataIdentifiers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.SuppressDataIdentifier]]


# UpdateResourceProfileRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### sensitivityScoreOverride
- **Type**: typing.Optional[int]


# UpdateRetrievalConfiguration

### retrievalMode
- **Type**: typing.Literal['ASSUME_ROLE', 'CALLER_CREDENTIALS']
- **Required**: Yes

### roleName
- **Type**: typing.Optional[str]


# UpdateRevealConfigurationRequest

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.RevealConfiguration'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.UpdateRetrievalConfiguration]


# UpdateRevealConfigurationResponse

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.RevealConfiguration'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.RetrievalConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.macie2.macie2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSensitivityInspectionTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### excludes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityInspectionTemplateExcludes, aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityInspectionTemplateExcludesOutput, NoneType]

### includes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityInspectionTemplateIncludes, aws_resource_validator.pydantic_models.macie2.macie2_classes.SensitivityInspectionTemplateIncludesOutput, NoneType]


# UsageByAccount

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### estimatedCost
- **Type**: typing.Optional[str]

### serviceLimit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.ServiceLimit]

### type
- **Type**: typing.Optional[typing.Literal['AUTOMATED_OBJECT_MONITORING', 'AUTOMATED_SENSITIVE_DATA_DISCOVERY', 'DATA_INVENTORY_EVALUATION', 'SENSITIVE_DATA_DISCOVERY']]


# UsageRecord

### accountId
- **Type**: typing.Optional[str]

### automatedDiscoveryFreeTrialStartDate
- **Type**: typing.Optional[datetime.datetime]

### freeTrialStartDate
- **Type**: typing.Optional[datetime.datetime]

### usage
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.macie2.macie2_classes.UsageByAccount]]


# UsageStatisticsFilter

### comparator
- **Type**: typing.Optional[typing.Literal['CONTAINS', 'EQ', 'GT', 'GTE', 'LT', 'LTE', 'NE']]

### key
- **Type**: typing.Optional[typing.Literal['accountId', 'freeTrialStartDate', 'serviceLimit', 'total']]

### values
- **Type**: typing.Optional[typing.List[str]]


# UsageStatisticsSortBy

### key
- **Type**: typing.Optional[typing.Literal['accountId', 'freeTrialStartDate', 'serviceLimitValue', 'total']]

### orderBy
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# UsageTotal

### currency
- **Type**: typing.Optional[typing.Literal['USD']]

### estimatedCost
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['AUTOMATED_OBJECT_MONITORING', 'AUTOMATED_SENSITIVE_DATA_DISCOVERY', 'DATA_INVENTORY_EVALUATION', 'SENSITIVE_DATA_DISCOVERY']]


# UserIdentity

### assumedRole
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.AssumedRole]

### awsAccount
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.AwsAccount]

### awsService
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.AwsService]

### federatedUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.FederatedUser]

### iamUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.IamUser]

### root
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.macie2.macie2_classes.UserIdentityRoot]

### type
- **Type**: typing.Optional[typing.Literal['AWSAccount', 'AWSService', 'AssumedRole', 'FederatedUser', 'IAMUser', 'Root']]


# UserIdentityRoot

### accountId
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### principalId
- **Type**: typing.Optional[str]


# UserPausedDetails

### jobExpiresAt
- **Type**: typing.Optional[datetime.datetime]

### jobImminentExpirationHealthEventArn
- **Type**: typing.Optional[str]

### jobPausedAt
- **Type**: typing.Optional[datetime.datetime]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WeeklySchedule

### dayOfWeek
- **Type**: typing.Optional[typing.Literal['FRIDAY', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'WEDNESDAY']]



# voice_id_classes

# AssociateFraudsterRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudsterId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateFraudsterResponseTypeDef

### Fraudster
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudsterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthenticationConfigurationTypeDef

### AcceptanceThreshold
- **Type**: <class 'int'>
- **Required**: Yes


# AuthenticationResultTypeDef

### AudioAggregationEndedAt
- **Type**: typing.Optional[datetime.datetime]

### AudioAggregationStartedAt
- **Type**: typing.Optional[datetime.datetime]

### AuthenticationResultId
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.AuthenticationConfigurationTypeDef]

### CustomerSpeakerId
- **Type**: typing.Optional[str]

### Decision
- **Type**: typing.Optional[typing.Literal['ACCEPT', 'NOT_ENOUGH_SPEECH', 'REJECT', 'SPEAKER_EXPIRED', 'SPEAKER_ID_NOT_PROVIDED', 'SPEAKER_NOT_ENROLLED', 'SPEAKER_OPTED_OUT']]

### GeneratedSpeakerId
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDomainRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideEncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ServerSideEncryptionConfigurationTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.voice_id_classes.TagTypeDef]]


# CreateDomainResponseTypeDef

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.DomainTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWatchlistRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CreateWatchlistResponseTypeDef

### Watchlist
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.WatchlistTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFraudsterRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudsterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSpeakerRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWatchlistRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainResponseTypeDef

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.DomainTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFraudsterRegistrationJobRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFraudsterRegistrationJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudsterRegistrationJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFraudsterRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudsterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFraudsterResponseTypeDef

### Fraudster
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudsterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSpeakerEnrollmentJobRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSpeakerEnrollmentJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.SpeakerEnrollmentJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSpeakerRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSpeakerResponseTypeDef

### Speaker
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.SpeakerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWatchlistRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWatchlistResponseTypeDef

### Watchlist
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.WatchlistTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateFraudsterRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudsterId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFraudsterResponseTypeDef

### Fraudster
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudsterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainSummaryTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### DomainStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PENDING', 'SUSPENDED']]

### Name
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.ServerSideEncryptionConfigurationTypeDef]

### ServerSideEncryptionUpdateDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.ServerSideEncryptionUpdateDetailsTypeDef]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### WatchlistDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.WatchlistDetailsTypeDef]


# DomainTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### DomainStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'PENDING', 'SUSPENDED']]

### Name
- **Type**: typing.Optional[str]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.ServerSideEncryptionConfigurationTypeDef]

### ServerSideEncryptionUpdateDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.ServerSideEncryptionUpdateDetailsTypeDef]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### WatchlistDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.WatchlistDetailsTypeDef]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnrollmentConfigTypeDef

### ExistingEnrollmentAction
- **Type**: typing.Optional[typing.Literal['OVERWRITE', 'SKIP']]

### FraudDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.EnrollmentJobFraudDetectionConfigTypeDef]


# EnrollmentJobFraudDetectionConfigTypeDef

### FraudDetectionAction
- **Type**: typing.Optional[typing.Literal['FAIL', 'IGNORE']]

### RiskThreshold
- **Type**: typing.Optional[int]

### WatchlistIds
- **Type**: typing.Optional[typing.List[str]]


# EvaluateSessionRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionNameOrId
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateSessionResponseTypeDef

### AuthenticationResult
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.AuthenticationResultTypeDef'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudDetectionResult
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudDetectionResultTypeDef'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingStatus
- **Type**: typing.Literal['ENDED', 'ONGOING', 'PENDING_CONFIGURATION']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FailureDetailsTypeDef

### Message
- **Type**: typing.Optional[str]

### StatusCode
- **Type**: typing.Optional[int]


# FraudDetectionConfigurationTypeDef

### RiskThreshold
- **Type**: typing.Optional[int]

### WatchlistId
- **Type**: typing.Optional[str]


# FraudDetectionResultTypeDef

### AudioAggregationEndedAt
- **Type**: typing.Optional[datetime.datetime]

### AudioAggregationStartedAt
- **Type**: typing.Optional[datetime.datetime]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.FraudDetectionConfigurationTypeDef]

### Decision
- **Type**: typing.Optional[typing.Literal['HIGH_RISK', 'LOW_RISK', 'NOT_ENOUGH_SPEECH']]

### FraudDetectionResultId
- **Type**: typing.Optional[str]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['KNOWN_FRAUDSTER', 'VOICE_SPOOFING']]]

### RiskDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.FraudRiskDetailsTypeDef]


# FraudRiskDetailsTypeDef

### KnownFraudsterRisk
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.KnownFraudsterRiskTypeDef'>
- **Required**: Yes

### VoiceSpoofingRisk
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.VoiceSpoofingRiskTypeDef'>
- **Required**: Yes


# FraudsterRegistrationJobSummaryTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DomainId
- **Type**: typing.Optional[str]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.FailureDetailsTypeDef]

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.JobProgressTypeDef]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]


# FraudsterRegistrationJobTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.FailureDetailsTypeDef]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.InputDataConfigTypeDef]

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.JobProgressTypeDef]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.OutputDataConfigTypeDef]

### RegistrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.RegistrationConfigTypeDef]


# FraudsterSummaryTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DomainId
- **Type**: typing.Optional[str]

### GeneratedFraudsterId
- **Type**: typing.Optional[str]

### WatchlistIds
- **Type**: typing.Optional[typing.List[str]]


# FraudsterTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DomainId
- **Type**: typing.Optional[str]

### GeneratedFraudsterId
- **Type**: typing.Optional[str]

### WatchlistIds
- **Type**: typing.Optional[typing.List[str]]


# InputDataConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# JobProgressTypeDef

### PercentComplete
- **Type**: typing.Optional[int]


# KnownFraudsterRiskTypeDef

### RiskScore
- **Type**: <class 'int'>
- **Required**: Yes

### GeneratedFraudsterId
- **Type**: typing.Optional[str]


# ListDomainsRequestListDomainsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfigTypeDef]


# ListDomainsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsResponseTypeDef

### DomainSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.DomainSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFraudsterRegistrationJobsRequestListFraudsterRegistrationJobsPaginateTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfigTypeDef]


# ListFraudsterRegistrationJobsRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFraudsterRegistrationJobsResponseTypeDef

### JobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.FraudsterRegistrationJobSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFraudstersRequestListFraudstersPaginateTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfigTypeDef]


# ListFraudstersRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WatchlistId
- **Type**: typing.Optional[str]


# ListFraudstersResponseTypeDef

### FraudsterSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.FraudsterSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSpeakerEnrollmentJobsRequestListSpeakerEnrollmentJobsPaginateTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfigTypeDef]


# ListSpeakerEnrollmentJobsRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSpeakerEnrollmentJobsResponseTypeDef

### JobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.SpeakerEnrollmentJobSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSpeakersRequestListSpeakersPaginateTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfigTypeDef]


# ListSpeakersRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSpeakersResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.SpeakerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWatchlistsRequestListWatchlistsPaginateTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfigTypeDef]


# ListWatchlistsRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListWatchlistsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.WatchlistSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OptOutSpeakerRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerId
- **Type**: <class 'str'>
- **Required**: Yes


# OptOutSpeakerResponseTypeDef

### Speaker
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.SpeakerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OutputDataConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegistrationConfigTypeDef

### DuplicateRegistrationAction
- **Type**: typing.Optional[typing.Literal['REGISTER_AS_NEW', 'SKIP']]

### FraudsterSimilarityThreshold
- **Type**: typing.Optional[int]

### WatchlistIds
- **Type**: typing.Optional[typing.List[str]]


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


# ServerSideEncryptionConfigurationTypeDef

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# ServerSideEncryptionUpdateDetailsTypeDef

### Message
- **Type**: typing.Optional[str]

### OldKmsKeyId
- **Type**: typing.Optional[str]

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]


# SpeakerEnrollmentJobSummaryTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DomainId
- **Type**: typing.Optional[str]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.FailureDetailsTypeDef]

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.JobProgressTypeDef]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]


# SpeakerEnrollmentJobTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### EnrollmentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.EnrollmentConfigTypeDef]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.FailureDetailsTypeDef]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.InputDataConfigTypeDef]

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobProgress
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.JobProgressTypeDef]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.OutputDataConfigTypeDef]


# SpeakerSummaryTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### CustomerSpeakerId
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### GeneratedSpeakerId
- **Type**: typing.Optional[str]

### LastAccessedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ENROLLED', 'EXPIRED', 'OPTED_OUT', 'PENDING']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# SpeakerTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### CustomerSpeakerId
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### GeneratedSpeakerId
- **Type**: typing.Optional[str]

### LastAccessedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ENROLLED', 'EXPIRED', 'OPTED_OUT', 'PENDING']]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# StartFraudsterRegistrationJobRequestRequestTypeDef

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### RegistrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.RegistrationConfigTypeDef]


# StartFraudsterRegistrationJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudsterRegistrationJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSpeakerEnrollmentJobRequestRequestTypeDef

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.InputDataConfigTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### EnrollmentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.EnrollmentConfigTypeDef]

### JobName
- **Type**: typing.Optional[str]


# StartSpeakerEnrollmentJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.SpeakerEnrollmentJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.voice_id_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDomainRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideEncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ServerSideEncryptionConfigurationTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateDomainResponseTypeDef

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.DomainTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWatchlistRequestRequestTypeDef

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdateWatchlistResponseTypeDef

### Watchlist
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.WatchlistTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VoiceSpoofingRiskTypeDef

### RiskScore
- **Type**: <class 'int'>
- **Required**: Yes


# WatchlistDetailsTypeDef

### DefaultWatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# WatchlistSummaryTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DefaultWatchlist
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### WatchlistId
- **Type**: typing.Optional[str]


# WatchlistTypeDef

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DefaultWatchlist
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### WatchlistId
- **Type**: typing.Optional[str]



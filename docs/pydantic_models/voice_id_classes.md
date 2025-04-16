# Voice Id Classes

# AssociateFraudsterRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudsterId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateFraudsterResponse

### Fraudster
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Fraudster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# AuthenticationConfiguration

### AcceptanceThreshold
- **Type**: <class 'int'>
- **Required**: Yes


# AuthenticationResult

### AudioAggregationEndedAt
- **Type**: typing.Optional[datetime.datetime]

### AudioAggregationStartedAt
- **Type**: typing.Optional[datetime.datetime]

### AuthenticationResultId
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.AuthenticationConfiguration]

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

# CreateDomainRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideEncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ServerSideEncryptionConfiguration'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.voice_id_classes.Tag]]


# CreateDomainResponse

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Domain'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWatchlistRequest

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


# CreateWatchlistResponse

### Watchlist
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Watchlist'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFraudsterRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudsterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSpeakerRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWatchlistRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDomainResponse

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Domain'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFraudsterRegistrationJobRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFraudsterRegistrationJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudsterRegistrationJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFraudsterRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudsterId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFraudsterResponse

### Fraudster
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Fraudster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSpeakerEnrollmentJobRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSpeakerEnrollmentJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.SpeakerEnrollmentJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSpeakerRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSpeakerResponse

### Speaker
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Speaker'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWatchlistRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWatchlistResponse

### Watchlist
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Watchlist'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateFraudsterRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudsterId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateFraudsterResponse

### Fraudster
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Fraudster'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# Domain

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
- **Type**: <class 'NoneType'>

### ServerSideEncryptionUpdateDetails
- **Type**: <class 'NoneType'>

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### WatchlistDetails
- **Type**: <class 'NoneType'>


# DomainSummary

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
- **Type**: <class 'NoneType'>

### ServerSideEncryptionUpdateDetails
- **Type**: <class 'NoneType'>

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### WatchlistDetails
- **Type**: <class 'NoneType'>


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# EnrollmentConfig

### ExistingEnrollmentAction
- **Type**: typing.Optional[typing.Literal['OVERWRITE', 'SKIP']]

### FraudDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.EnrollmentJobFraudDetectionConfig]


# EnrollmentConfigOutput

### ExistingEnrollmentAction
- **Type**: typing.Optional[typing.Literal['OVERWRITE', 'SKIP']]

### FraudDetectionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.EnrollmentJobFraudDetectionConfigOutput]


# EnrollmentConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnrollmentJobFraudDetectionConfig

### FraudDetectionAction
- **Type**: typing.Optional[typing.Literal['FAIL', 'IGNORE']]

### RiskThreshold
- **Type**: typing.Optional[int]

### WatchlistIds
- **Type**: typing.Optional[typing.Sequence[str]]


# EnrollmentJobFraudDetectionConfigOutput

### FraudDetectionAction
- **Type**: typing.Optional[typing.Literal['FAIL', 'IGNORE']]

### RiskThreshold
- **Type**: typing.Optional[int]

### WatchlistIds
- **Type**: typing.Optional[typing.List[str]]


# EvaluateSessionRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionNameOrId
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluateSessionResponse

### AuthenticationResult
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.AuthenticationResult'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### FraudDetectionResult
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudDetectionResult'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# FailureDetails

### Message
- **Type**: typing.Optional[str]

### StatusCode
- **Type**: typing.Optional[int]


# FraudDetectionConfiguration

### RiskThreshold
- **Type**: typing.Optional[int]

### WatchlistId
- **Type**: typing.Optional[str]


# FraudDetectionResult

### AudioAggregationEndedAt
- **Type**: typing.Optional[datetime.datetime]

### AudioAggregationStartedAt
- **Type**: typing.Optional[datetime.datetime]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.FraudDetectionConfiguration]

### Decision
- **Type**: typing.Optional[typing.Literal['HIGH_RISK', 'LOW_RISK', 'NOT_ENOUGH_SPEECH']]

### FraudDetectionResultId
- **Type**: typing.Optional[str]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['KNOWN_FRAUDSTER', 'VOICE_SPOOFING']]]

### RiskDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.FraudRiskDetails]


# FraudRiskDetails

### KnownFraudsterRisk
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.KnownFraudsterRisk'>
- **Required**: Yes

### VoiceSpoofingRisk
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.VoiceSpoofingRisk'>
- **Required**: Yes


# Fraudster

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DomainId
- **Type**: typing.Optional[str]

### GeneratedFraudsterId
- **Type**: typing.Optional[str]

### WatchlistIds
- **Type**: typing.Optional[typing.List[str]]


# FraudsterRegistrationJob

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### FailureDetails
- **Type**: <class 'NoneType'>

### InputDataConfig
- **Type**: <class 'NoneType'>

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobProgress
- **Type**: <class 'NoneType'>

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### RegistrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.RegistrationConfigOutput]


# FraudsterRegistrationJobSummary

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DomainId
- **Type**: typing.Optional[str]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### FailureDetails
- **Type**: <class 'NoneType'>

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobProgress
- **Type**: <class 'NoneType'>

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]


# FraudsterSummary

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DomainId
- **Type**: typing.Optional[str]

### GeneratedFraudsterId
- **Type**: typing.Optional[str]

### WatchlistIds
- **Type**: typing.Optional[typing.List[str]]


# InputDataConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# JobProgress

### PercentComplete
- **Type**: typing.Optional[int]


# KnownFraudsterRisk

### RiskScore
- **Type**: <class 'int'>
- **Required**: Yes

### GeneratedFraudsterId
- **Type**: typing.Optional[str]


# ListDomainsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDomainsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfig]


# ListDomainsResponse

### DomainSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.DomainSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFraudsterRegistrationJobsRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListFraudsterRegistrationJobsRequestPaginate

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfig]


# ListFraudsterRegistrationJobsResponse

### JobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.FraudsterRegistrationJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFraudstersRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WatchlistId
- **Type**: typing.Optional[str]


# ListFraudstersRequestPaginate

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### WatchlistId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfig]


# ListFraudstersResponse

### FraudsterSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.FraudsterSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSpeakerEnrollmentJobsRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSpeakerEnrollmentJobsRequestPaginate

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfig]


# ListSpeakerEnrollmentJobsResponse

### JobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.SpeakerEnrollmentJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSpeakersRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSpeakersRequestPaginate

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfig]


# ListSpeakersResponse

### SpeakerSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.SpeakerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# ListWatchlistsRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListWatchlistsRequestPaginate

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.PaginatorConfig]


# ListWatchlistsResponse

### WatchlistSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.voice_id_classes.WatchlistSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OptOutSpeakerRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerId
- **Type**: <class 'str'>
- **Required**: Yes


# OptOutSpeakerResponse

### Speaker
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Speaker'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# OutputDataConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegistrationConfig

### DuplicateRegistrationAction
- **Type**: typing.Optional[typing.Literal['REGISTER_AS_NEW', 'SKIP']]

### FraudsterSimilarityThreshold
- **Type**: typing.Optional[int]

### WatchlistIds
- **Type**: typing.Optional[typing.Sequence[str]]


# RegistrationConfigOutput

### DuplicateRegistrationAction
- **Type**: typing.Optional[typing.Literal['REGISTER_AS_NEW', 'SKIP']]

### FraudsterSimilarityThreshold
- **Type**: typing.Optional[int]

### WatchlistIds
- **Type**: typing.Optional[typing.List[str]]


# RegistrationConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ServerSideEncryptionConfiguration

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# ServerSideEncryptionUpdateDetails

### Message
- **Type**: typing.Optional[str]

### OldKmsKeyId
- **Type**: typing.Optional[str]

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']]


# Speaker

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


# SpeakerEnrollmentJob

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### DomainId
- **Type**: typing.Optional[str]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### EnrollmentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.EnrollmentConfigOutput]

### FailureDetails
- **Type**: <class 'NoneType'>

### InputDataConfig
- **Type**: <class 'NoneType'>

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobProgress
- **Type**: <class 'NoneType'>

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]

### OutputDataConfig
- **Type**: <class 'NoneType'>


# SpeakerEnrollmentJobSummary

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### DomainId
- **Type**: typing.Optional[str]

### EndedAt
- **Type**: typing.Optional[datetime.datetime]

### FailureDetails
- **Type**: <class 'NoneType'>

### JobId
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobProgress
- **Type**: <class 'NoneType'>

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ERRORS', 'FAILED', 'IN_PROGRESS', 'SUBMITTED']]


# SpeakerSummary

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


# StartFraudsterRegistrationJobRequest

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.OutputDataConfig'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### RegistrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.RegistrationConfigUnion]


# StartFraudsterRegistrationJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.FraudsterRegistrationJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# StartSpeakerEnrollmentJobRequest

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.InputDataConfig'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.OutputDataConfig'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### EnrollmentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.voice_id_classes.EnrollmentConfigUnion]

### JobName
- **Type**: typing.Optional[str]


# StartSpeakerEnrollmentJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.SpeakerEnrollmentJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.voice_id_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDomainRequest

### DomainId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideEncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ServerSideEncryptionConfiguration'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateDomainResponse

### Domain
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Domain'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWatchlistRequest

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


# UpdateWatchlistResponse

### Watchlist
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.Watchlist'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.voice_id_classes.ResponseMetadata'>
- **Required**: Yes


# VoiceSpoofingRisk

### RiskScore
- **Type**: <class 'int'>
- **Required**: Yes


# Watchlist

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


# WatchlistDetails

### DefaultWatchlistId
- **Type**: <class 'str'>
- **Required**: Yes


# WatchlistSummary

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



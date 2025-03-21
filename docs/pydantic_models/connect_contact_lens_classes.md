# Connect Contact Lens Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CategoriesTypeDef

### MatchedCategories
- **Type**: typing.List[str]
- **Required**: Yes

### MatchedDetails
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.connect_contact_lens_classes.CategoryDetailsTypeDef]
- **Required**: Yes


# CategoryDetailsTypeDef

### PointsOfInterest
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_contact_lens_classes.PointOfInterestTypeDef]
- **Required**: Yes


# CharacterOffsetsTypeDef

### BeginOffsetChar
- **Type**: <class 'int'>
- **Required**: Yes

### EndOffsetChar
- **Type**: <class 'int'>
- **Required**: Yes


# IssueDetectedTypeDef

### CharacterOffsets
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_contact_lens_classes.CharacterOffsetsTypeDef'>
- **Required**: Yes


# ListRealtimeContactAnalysisSegmentsRequestTypeDef

### InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### ContactId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRealtimeContactAnalysisSegmentsResponseTypeDef

### Segments
- **Type**: typing.List[aws_resource_validator.pydantic_models.connect_contact_lens_classes.RealtimeContactAnalysisSegmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.connect_contact_lens_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PointOfInterestTypeDef

### BeginOffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes

### EndOffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes


# PostContactSummaryTypeDef

### Status
- **Type**: typing.Literal['COMPLETED', 'FAILED']
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### FailureCode
- **Type**: typing.Optional[typing.Literal['FAILED_SAFETY_GUIDELINES', 'INSUFFICIENT_CONVERSATION_CONTENT', 'INTERNAL_ERROR', 'INVALID_ANALYSIS_CONFIGURATION', 'QUOTA_EXCEEDED']]


# RealtimeContactAnalysisSegmentTypeDef

### Transcript
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_contact_lens_classes.TranscriptTypeDef]

### Categories
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_contact_lens_classes.CategoriesTypeDef]

### PostContactSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.connect_contact_lens_classes.PostContactSummaryTypeDef]


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


# TranscriptTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantRole
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### BeginOffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes

### EndOffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes

### Sentiment
- **Type**: typing.Literal['NEGATIVE', 'NEUTRAL', 'POSITIVE']
- **Required**: Yes

### IssuesDetected
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.connect_contact_lens_classes.IssueDetectedTypeDef]]



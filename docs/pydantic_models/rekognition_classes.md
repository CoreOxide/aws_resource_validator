# Rekognition Classes

# AgeRange

### Low
- **Type**: typing.Optional[int]

### High
- **Type**: typing.Optional[int]


# Asset

### GroundTruthManifest
- **Type**: <class 'NoneType'>


# AssociateFacesRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### FaceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UserMatchThreshold
- **Type**: typing.Optional[float]

### ClientRequestToken
- **Type**: typing.Optional[str]


# AssociateFacesResponse

### AssociatedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AssociatedFace]
- **Required**: Yes

### UnsuccessfulFaceAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnsuccessfulFaceAssociation]
- **Required**: Yes

### UserStatus
- **Type**: typing.Literal['ACTIVE', 'CREATED', 'CREATING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatedFace

### FaceId
- **Type**: typing.Optional[str]


# AudioMetadata

### Codec
- **Type**: typing.Optional[str]

### DurationMillis
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]

### NumberOfChannels
- **Type**: typing.Optional[int]


# AuditImage

### Bytes
- **Type**: typing.Optional[bytes]

### S3Object
- **Type**: <class 'NoneType'>

### BoundingBox
- **Type**: <class 'NoneType'>


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Beard

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# BlackFrame

### MaxPixelThreshold
- **Type**: typing.Optional[float]

### MinCoveragePercentage
- **Type**: typing.Optional[float]


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BoundingBox

### Width
- **Type**: typing.Optional[float]

### Height
- **Type**: typing.Optional[float]

### Left
- **Type**: typing.Optional[float]

### Top
- **Type**: typing.Optional[float]


# Celebrity

### Urls
- **Type**: typing.Optional[typing.List[str]]

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ComparedFace]

### MatchConfidence
- **Type**: typing.Optional[float]

### KnownGender
- **Type**: <class 'NoneType'>


# CelebrityDetail

### Urls
- **Type**: typing.Optional[typing.List[str]]

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### BoundingBox
- **Type**: <class 'NoneType'>

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetail]

### KnownGender
- **Type**: <class 'NoneType'>


# CelebrityRecognition

### Timestamp
- **Type**: typing.Optional[int]

### Celebrity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CelebrityDetail]


# CompareFacesMatch

### Similarity
- **Type**: typing.Optional[float]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ComparedFace]


# CompareFacesRequest

### SourceImage
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### TargetImage
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### SimilarityThreshold
- **Type**: typing.Optional[float]

### QualityFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'NONE']]


# CompareFacesResponse

### SourceImageFace
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ComparedSourceImageFace'>
- **Required**: Yes

### FaceMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.CompareFacesMatch]
- **Required**: Yes

### UnmatchedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ComparedFace]
- **Required**: Yes

### SourceImageOrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### TargetImageOrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# ComparedFace

### BoundingBox
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[float]

### Landmarks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Landmark]]

### Pose
- **Type**: <class 'NoneType'>

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ImageQuality]

### Emotions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Emotion]]

### Smile
- **Type**: <class 'NoneType'>


# ComparedSourceImageFace

### BoundingBox
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[float]


# ConnectedHomeSettings

### Labels
- **Type**: typing.Sequence[str]
- **Required**: Yes

### MinConfidence
- **Type**: typing.Optional[float]


# ConnectedHomeSettingsForUpdate

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]

### MinConfidence
- **Type**: typing.Optional[float]


# ConnectedHomeSettingsOutput

### Labels
- **Type**: typing.List[str]
- **Required**: Yes

### MinConfidence
- **Type**: typing.Optional[float]


# ContentModerationDetection

### Timestamp
- **Type**: typing.Optional[int]

### ModerationLabel
- **Type**: <class 'NoneType'>

### StartTimestampMillis
- **Type**: typing.Optional[int]

### EndTimestampMillis
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]

### ContentTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ContentType]]


# ContentType

### Confidence
- **Type**: typing.Optional[float]

### Name
- **Type**: typing.Optional[str]


# CopyProjectVersionRequest

### SourceProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.OutputConfig'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KmsKeyId
- **Type**: typing.Optional[str]


# CopyProjectVersionResponse

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# CoversBodyPart

### Confidence
- **Type**: typing.Optional[float]

### Value
- **Type**: typing.Optional[bool]


# CreateCollectionRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCollectionResponse

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### CollectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetRequest

### DatasetType
- **Type**: typing.Literal['TEST', 'TRAIN']
- **Required**: Yes

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetSource
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDatasetResponse

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFaceLivenessSessionRequest

### KmsKeyId
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CreateFaceLivenessSessionRequestSettings]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateFaceLivenessSessionRequestSettings

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.LivenessOutputConfig]

### AuditImagesLimit
- **Type**: typing.Optional[int]


# CreateFaceLivenessSessionResponse

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectRequest

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### Feature
- **Type**: typing.Optional[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]

### AutoUpdate
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectResponse

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProjectVersionRequest

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.OutputConfig'>
- **Required**: Yes

### TrainingData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TrainingDataUnion]

### TestingData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TestingDataUnion]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KmsKeyId
- **Type**: typing.Optional[str]

### VersionDescription
- **Type**: typing.Optional[str]

### FeatureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CustomizationFeatureConfig]


# CreateProjectVersionResponse

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamProcessorRequest

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorInput'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorOutput'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorSettingsUnion'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorNotificationChannel]

### KmsKeyId
- **Type**: typing.Optional[str]

### RegionsOfInterest
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestUnion]]

### DataSharingPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorDataSharingPreference]


# CreateStreamProcessorResponse

### StreamProcessorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CustomLabel

### Name
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### Geometry
- **Type**: <class 'NoneType'>


# CustomizationFeatureConfig

### ContentModeration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CustomizationFeatureContentModerationConfig]


# CustomizationFeatureContentModerationConfig

### ConfidenceThreshold
- **Type**: typing.Optional[float]


# DatasetChanges

### GroundTruth
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Blob'>
- **Required**: Yes


# DatasetDescription

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]

### StatusMessageCode
- **Type**: typing.Optional[typing.Literal['CLIENT_ERROR', 'SERVICE_ERROR', 'SUCCESS']]

### DatasetStats
- **Type**: <class 'NoneType'>


# DatasetLabelDescription

### LabelName
- **Type**: typing.Optional[str]

### LabelStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DatasetLabelStats]


# DatasetLabelStats

### EntryCount
- **Type**: typing.Optional[int]

### BoundingBoxCount
- **Type**: typing.Optional[int]


# DatasetMetadata

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DatasetType
- **Type**: typing.Optional[typing.Literal['TEST', 'TRAIN']]

### DatasetArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATE_COMPLETE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS', 'UPDATE_COMPLETE', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]

### StatusMessageCode
- **Type**: typing.Optional[typing.Literal['CLIENT_ERROR', 'SERVICE_ERROR', 'SUCCESS']]


# DatasetSource

### GroundTruthManifest
- **Type**: <class 'NoneType'>

### DatasetArn
- **Type**: typing.Optional[str]


# DatasetStats

### LabeledEntries
- **Type**: typing.Optional[int]

### TotalEntries
- **Type**: typing.Optional[int]

### TotalLabels
- **Type**: typing.Optional[int]

### ErrorEntries
- **Type**: typing.Optional[int]


# DeleteCollectionRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCollectionResponse

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDatasetRequest

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFacesRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### FaceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteFacesResponse

### DeletedFaces
- **Type**: typing.List[str]
- **Required**: Yes

### UnsuccessfulFaceDeletions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnsuccessfulFaceDeletion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProjectPolicyRequest

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DeleteProjectRequest

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectResponse

### Status
- **Type**: typing.Literal['CREATED', 'CREATING', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProjectVersionRequest

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectVersionResponse

### Status
- **Type**: typing.Literal['COPYING_COMPLETED', 'COPYING_FAILED', 'COPYING_IN_PROGRESS', 'DELETING', 'DEPRECATED', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'TRAINING_COMPLETED', 'TRAINING_FAILED', 'TRAINING_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteStreamProcessorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DescribeCollectionRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCollectionResponse

### FaceCount
- **Type**: <class 'int'>
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### CollectionARN
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UserCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatasetRequest

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

### DatasetDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.DatasetDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProjectVersionsRequest

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeProjectVersionsRequestPaginate

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# DescribeProjectVersionsRequestWait

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeProjectVersionsRequestWaitExtra

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeProjectVersionsResponse

### ProjectVersionDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProjectVersionDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeProjectsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ProjectNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]]


# DescribeProjectsRequestPaginate

### ProjectNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# DescribeProjectsResponse

### ProjectDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProjectDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStreamProcessorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStreamProcessorResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StreamProcessorArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdateTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorInput'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorOutput'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorSettingsOutput'>
- **Required**: Yes

### NotificationChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorNotificationChannel'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### RegionsOfInterest
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestOutput]
- **Required**: Yes

### DataSharingPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorDataSharingPreference'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DetectCustomLabelsRequest

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### MinConfidence
- **Type**: typing.Optional[float]


# DetectCustomLabelsResponse

### CustomLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.CustomLabel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DetectFacesRequest

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGE_RANGE', 'ALL', 'BEARD', 'DEFAULT', 'EMOTIONS', 'EYEGLASSES', 'EYES_OPEN', 'EYE_DIRECTION', 'FACE_OCCLUDED', 'GENDER', 'MOUTH_OPEN', 'MUSTACHE', 'SMILE', 'SUNGLASSES']]]


# DetectFacesResponse

### FaceDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetail]
- **Required**: Yes

### OrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DetectLabelsImageBackground

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageQuality]

### DominantColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DominantColor]]


# DetectLabelsImageForeground

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageQuality]

### DominantColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DominantColor]]


# DetectLabelsImageProperties

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageQuality]

### DominantColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DominantColor]]

### Foreground
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageForeground]

### Background
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageBackground]


# DetectLabelsImagePropertiesSettings

### MaxDominantColors
- **Type**: typing.Optional[int]


# DetectLabelsImageQuality

### Brightness
- **Type**: typing.Optional[float]

### Sharpness
- **Type**: typing.Optional[float]

### Contrast
- **Type**: typing.Optional[float]


# DetectLabelsRequest

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### MaxLabels
- **Type**: typing.Optional[int]

### MinConfidence
- **Type**: typing.Optional[float]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['GENERAL_LABELS', 'IMAGE_PROPERTIES']]]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsSettings]


# DetectLabelsResponse

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Label]
- **Required**: Yes

### OrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### LabelModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ImageProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DetectLabelsSettings

### GeneralLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GeneralLabelsSettings]

### ImageProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImagePropertiesSettings]


# DetectModerationLabelsRequest

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### MinConfidence
- **Type**: typing.Optional[float]

### HumanLoopConfig
- **Type**: <class 'NoneType'>

### ProjectVersion
- **Type**: typing.Optional[str]


# DetectModerationLabelsResponse

### ModerationLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ModerationLabel]
- **Required**: Yes

### ModerationModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopActivationOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.HumanLoopActivationOutput'>
- **Required**: Yes

### ProjectVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ContentTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ContentType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DetectProtectiveEquipmentRequest

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### SummarizationAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ProtectiveEquipmentSummarizationAttributes]


# DetectProtectiveEquipmentResponse

### ProtectiveEquipmentModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Persons
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProtectiveEquipmentPerson]
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ProtectiveEquipmentSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DetectTextFilters

### WordFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectionFilter]

### RegionsOfInterest
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestUnion]]


# DetectTextRequest

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectTextFilters]


# DetectTextResponse

### TextDetections
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.TextDetection]
- **Required**: Yes

### TextModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DetectionFilter

### MinConfidence
- **Type**: typing.Optional[float]

### MinBoundingBoxHeight
- **Type**: typing.Optional[float]

### MinBoundingBoxWidth
- **Type**: typing.Optional[float]


# DisassociateFacesRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### FaceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DisassociateFacesResponse

### DisassociatedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DisassociatedFace]
- **Required**: Yes

### UnsuccessfulFaceDisassociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnsuccessfulFaceDisassociation]
- **Required**: Yes

### UserStatus
- **Type**: typing.Literal['ACTIVE', 'CREATED', 'CREATING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociatedFace

### FaceId
- **Type**: typing.Optional[str]


# DistributeDataset

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DistributeDatasetEntriesRequest

### Datasets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.DistributeDataset]
- **Required**: Yes


# DominantColor

### Red
- **Type**: typing.Optional[int]

### Blue
- **Type**: typing.Optional[int]

### Green
- **Type**: typing.Optional[int]

### HexCode
- **Type**: typing.Optional[str]

### CSSColor
- **Type**: typing.Optional[str]

### SimplifiedColor
- **Type**: typing.Optional[str]

### PixelPercent
- **Type**: typing.Optional[float]


# Emotion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EquipmentDetection

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvaluationResult

### F1Score
- **Type**: typing.Optional[float]

### Summary
- **Type**: <class 'NoneType'>


# EyeDirection

### Yaw
- **Type**: typing.Optional[float]

### Pitch
- **Type**: typing.Optional[float]

### Confidence
- **Type**: typing.Optional[float]


# EyeOpen

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# Eyeglasses

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# Face

### FaceId
- **Type**: typing.Optional[str]

### BoundingBox
- **Type**: <class 'NoneType'>

### ImageId
- **Type**: typing.Optional[str]

### ExternalImageId
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### IndexFacesModelVersion
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]


# FaceDetail

### BoundingBox
- **Type**: <class 'NoneType'>

### AgeRange
- **Type**: <class 'NoneType'>

### Smile
- **Type**: <class 'NoneType'>

### Eyeglasses
- **Type**: <class 'NoneType'>

### Sunglasses
- **Type**: <class 'NoneType'>

### Gender
- **Type**: <class 'NoneType'>

### Beard
- **Type**: <class 'NoneType'>

### Mustache
- **Type**: <class 'NoneType'>

### EyesOpen
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.EyeOpen]

### MouthOpen
- **Type**: <class 'NoneType'>

### Emotions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Emotion]]

### Landmarks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Landmark]]

### Pose
- **Type**: <class 'NoneType'>

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ImageQuality]

### Confidence
- **Type**: typing.Optional[float]

### FaceOccluded
- **Type**: <class 'NoneType'>

### EyeDirection
- **Type**: <class 'NoneType'>


# FaceDetection

### Timestamp
- **Type**: typing.Optional[int]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetail]


# FaceMatch

### Similarity
- **Type**: typing.Optional[float]

### Face
- **Type**: <class 'NoneType'>


# FaceOccluded

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# FaceRecord

### Face
- **Type**: <class 'NoneType'>

### FaceDetail
- **Type**: <class 'NoneType'>


# FaceSearchSettings

### CollectionId
- **Type**: typing.Optional[str]

### FaceMatchThreshold
- **Type**: typing.Optional[float]


# Gender

### Value
- **Type**: typing.Optional[typing.Literal['Female', 'Male']]

### Confidence
- **Type**: typing.Optional[float]


# GeneralLabelsSettings

### LabelInclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### LabelExclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### LabelCategoryInclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### LabelCategoryExclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]


# Geometry

### BoundingBox
- **Type**: <class 'NoneType'>

### Polygon
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Point]]


# GetCelebrityInfoRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCelebrityInfoResponse

### Urls
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### KnownGender
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.KnownGender'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# GetCelebrityRecognitionRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['ID', 'TIMESTAMP']]


# GetCelebrityRecognitionResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadata'>
- **Required**: Yes

### Celebrities
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.CelebrityRecognition]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetContentModerationRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['NAME', 'TIMESTAMP']]

### AggregateBy
- **Type**: typing.Optional[typing.Literal['SEGMENTS', 'TIMESTAMPS']]


# GetContentModerationRequestMetadata

### SortBy
- **Type**: typing.Optional[typing.Literal['NAME', 'TIMESTAMP']]

### AggregateBy
- **Type**: typing.Optional[typing.Literal['SEGMENTS', 'TIMESTAMPS']]


# GetContentModerationResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadata'>
- **Required**: Yes

### ModerationLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ContentModerationDetection]
- **Required**: Yes

### ModerationModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### GetRequestMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.GetContentModerationRequestMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFaceDetectionRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetFaceDetectionResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadata'>
- **Required**: Yes

### Faces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetection]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFaceLivenessSessionResultsRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFaceLivenessSessionResultsResponse

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'EXPIRED', 'FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### Confidence
- **Type**: <class 'float'>
- **Required**: Yes

### ReferenceImage
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.AuditImage'>
- **Required**: Yes

### AuditImages
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AuditImage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# GetFaceSearchRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['INDEX', 'TIMESTAMP']]


# GetFaceSearchResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadata'>
- **Required**: Yes

### Persons
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.PersonMatch]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLabelDetectionRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['NAME', 'TIMESTAMP']]

### AggregateBy
- **Type**: typing.Optional[typing.Literal['SEGMENTS', 'TIMESTAMPS']]


# GetLabelDetectionRequestMetadata

### SortBy
- **Type**: typing.Optional[typing.Literal['NAME', 'TIMESTAMP']]

### AggregateBy
- **Type**: typing.Optional[typing.Literal['SEGMENTS', 'TIMESTAMPS']]


# GetLabelDetectionResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadata'>
- **Required**: Yes

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LabelDetection]
- **Required**: Yes

### LabelModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### GetRequestMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.GetLabelDetectionRequestMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMediaAnalysisJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaAnalysisJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOperationsConfig'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']
- **Required**: Yes

### FailureDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisJobFailureDetails'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisInput'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOutputConfig'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Results
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisResults'>
- **Required**: Yes

### ManifestSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisManifestSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# GetPersonTrackingRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['INDEX', 'TIMESTAMP']]


# GetPersonTrackingResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadata'>
- **Required**: Yes

### Persons
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.PersonDetection]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSegmentDetectionRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetSegmentDetectionResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadata]
- **Required**: Yes

### AudioMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AudioMetadata]
- **Required**: Yes

### Segments
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.SegmentDetection]
- **Required**: Yes

### SelectedSegmentTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.SegmentTypeInfo]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTextDetectionRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetTextDetectionResponse

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadata'>
- **Required**: Yes

### TextDetections
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.TextDetectionResult]
- **Required**: Yes

### TextModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GroundTruthManifest

### S3Object
- **Type**: <class 'NoneType'>


# HumanLoopActivationOutput

### HumanLoopArn
- **Type**: typing.Optional[str]

### HumanLoopActivationReasons
- **Type**: typing.Optional[typing.List[str]]

### HumanLoopActivationConditionsEvaluationResults
- **Type**: typing.Optional[str]


# HumanLoopConfig

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.HumanLoopDataAttributes]


# HumanLoopDataAttributes

### ContentClassifiers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]]


# Image

### Bytes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.Blob]

### S3Object
- **Type**: <class 'NoneType'>


# ImageQuality

### Brightness
- **Type**: typing.Optional[float]

### Sharpness
- **Type**: typing.Optional[float]


# IndexFacesRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### ExternalImageId
- **Type**: typing.Optional[str]

### DetectionAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGE_RANGE', 'ALL', 'BEARD', 'DEFAULT', 'EMOTIONS', 'EYEGLASSES', 'EYES_OPEN', 'EYE_DIRECTION', 'FACE_OCCLUDED', 'GENDER', 'MOUTH_OPEN', 'MUSTACHE', 'SMILE', 'SUNGLASSES']]]

### MaxFaces
- **Type**: typing.Optional[int]

### QualityFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'NONE']]


# IndexFacesResponse

### FaceRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceRecord]
- **Required**: Yes

### OrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### UnindexedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnindexedFace]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# Instance

### BoundingBox
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[float]

### DominantColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DominantColor]]


# KinesisDataStream

### Arn
- **Type**: typing.Optional[str]


# KinesisVideoStream

### Arn
- **Type**: typing.Optional[str]


# KinesisVideoStreamStartSelector

### ProducerTimestamp
- **Type**: typing.Optional[int]

### FragmentNumber
- **Type**: typing.Optional[str]


# KnownGender

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Label

### Name
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Instance]]

### Parents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Parent]]

### Aliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LabelAlias]]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LabelCategory]]


# LabelAlias

### Name
- **Type**: typing.Optional[str]


# LabelCategory

### Name
- **Type**: typing.Optional[str]


# LabelDetection

### Timestamp
- **Type**: typing.Optional[int]

### Label
- **Type**: <class 'NoneType'>

### StartTimestampMillis
- **Type**: typing.Optional[int]

### EndTimestampMillis
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]


# LabelDetectionSettings

### GeneralLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GeneralLabelsSettings]


# Landmark

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListCollectionsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCollectionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# ListCollectionsResponse

### CollectionIds
- **Type**: typing.List[str]
- **Required**: Yes

### FaceModelVersions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetEntriesRequest

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContainsLabels
- **Type**: typing.Optional[typing.Sequence[str]]

### Labeled
- **Type**: typing.Optional[bool]

### SourceRefContains
- **Type**: typing.Optional[str]

### HasErrors
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetEntriesRequestPaginate

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContainsLabels
- **Type**: typing.Optional[typing.Sequence[str]]

### Labeled
- **Type**: typing.Optional[bool]

### SourceRefContains
- **Type**: typing.Optional[str]

### HasErrors
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# ListDatasetEntriesResponse

### DatasetEntries
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetLabelsRequest

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetLabelsRequestPaginate

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# ListDatasetLabelsResponse

### DatasetLabelDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DatasetLabelDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFacesRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### UserId
- **Type**: typing.Optional[str]

### FaceIds
- **Type**: typing.Optional[typing.Sequence[str]]


# ListFacesRequestPaginate

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### FaceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# ListFacesResponse

### Faces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Face]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMediaAnalysisJobsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaAnalysisJobsResponse

### MediaAnalysisJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisJobDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProjectPoliciesRequest

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProjectPoliciesRequestPaginate

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# ListProjectPoliciesResponse

### ProjectPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProjectPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamProcessorsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStreamProcessorsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# ListStreamProcessorsResponse

### StreamProcessors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# ListUsersRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequestPaginate

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfig]


# ListUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.User]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LivenessOutputConfig

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]


# MatchedUser

### UserId
- **Type**: typing.Optional[str]

### UserStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATED', 'CREATING', 'UPDATING']]


# MediaAnalysisDetectModerationLabelsConfig

### MinConfidence
- **Type**: typing.Optional[float]

### ProjectVersion
- **Type**: typing.Optional[str]


# MediaAnalysisInput

### S3Object
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.S3Object'>
- **Required**: Yes


# MediaAnalysisJobDescription

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### OperationsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOperationsConfig'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisInput'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOutputConfig'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisJobFailureDetails]

### CompletionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### KmsKeyId
- **Type**: typing.Optional[str]

### Results
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisResults]

### ManifestSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisManifestSummary]


# MediaAnalysisJobFailureDetails

### Code
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'INTERNAL_ERROR', 'INVALID_KMS_KEY', 'INVALID_MANIFEST', 'INVALID_OUTPUT_CONFIG', 'INVALID_S3_OBJECT', 'RESOURCE_NOT_FOUND', 'RESOURCE_NOT_READY', 'THROTTLED']]

### Message
- **Type**: typing.Optional[str]


# MediaAnalysisManifestSummary

### S3Object
- **Type**: <class 'NoneType'>


# MediaAnalysisModelVersions

### Moderation
- **Type**: typing.Optional[str]


# MediaAnalysisOperationsConfig

### DetectModerationLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisDetectModerationLabelsConfig]


# MediaAnalysisOutputConfig

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]


# MediaAnalysisResults

### S3Object
- **Type**: <class 'NoneType'>

### ModelVersions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisModelVersions]


# ModerationLabel

### Confidence
- **Type**: typing.Optional[float]

### Name
- **Type**: typing.Optional[str]

### ParentName
- **Type**: typing.Optional[str]

### TaxonomyLevel
- **Type**: typing.Optional[int]


# MouthOpen

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# Mustache

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# NotificationChannel

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# OutputConfig

### S3Bucket
- **Type**: typing.Optional[str]

### S3KeyPrefix
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parent

### Name
- **Type**: typing.Optional[str]


# PersonDetail

### Index
- **Type**: typing.Optional[int]

### BoundingBox
- **Type**: <class 'NoneType'>

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetail]


# PersonDetection

### Timestamp
- **Type**: typing.Optional[int]

### Person
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PersonDetail]


# PersonMatch

### Timestamp
- **Type**: typing.Optional[int]

### Person
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PersonDetail]

### FaceMatches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceMatch]]


# Point

### X
- **Type**: typing.Optional[float]

### Y
- **Type**: typing.Optional[float]


# Pose

### Roll
- **Type**: typing.Optional[float]

### Yaw
- **Type**: typing.Optional[float]

### Pitch
- **Type**: typing.Optional[float]


# ProjectDescription

### ProjectArn
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'DELETING']]

### Datasets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DatasetMetadata]]

### Feature
- **Type**: typing.Optional[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]

### AutoUpdate
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ProjectPolicy

### ProjectArn
- **Type**: typing.Optional[str]

### PolicyName
- **Type**: typing.Optional[str]

### PolicyRevisionId
- **Type**: typing.Optional[str]

### PolicyDocument
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ProjectVersionDescription

### ProjectVersionArn
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### MinInferenceUnits
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['COPYING_COMPLETED', 'COPYING_FAILED', 'COPYING_IN_PROGRESS', 'DELETING', 'DEPRECATED', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'TRAINING_COMPLETED', 'TRAINING_FAILED', 'TRAINING_IN_PROGRESS']]

### StatusMessage
- **Type**: typing.Optional[str]

### BillableTrainingTimeInSeconds
- **Type**: typing.Optional[int]

### TrainingEndTimestamp
- **Type**: typing.Optional[datetime.datetime]

### OutputConfig
- **Type**: <class 'NoneType'>

### TrainingDataResult
- **Type**: <class 'NoneType'>

### TestingDataResult
- **Type**: <class 'NoneType'>

### EvaluationResult
- **Type**: <class 'NoneType'>

### ManifestSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GroundTruthManifest]

### KmsKeyId
- **Type**: typing.Optional[str]

### MaxInferenceUnits
- **Type**: typing.Optional[int]

### SourceProjectVersionArn
- **Type**: typing.Optional[str]

### VersionDescription
- **Type**: typing.Optional[str]

### Feature
- **Type**: typing.Optional[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]

### BaseModelVersion
- **Type**: typing.Optional[str]

### FeatureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CustomizationFeatureConfig]


# ProtectiveEquipmentBodyPart

### Name
- **Type**: typing.Optional[typing.Literal['FACE', 'HEAD', 'LEFT_HAND', 'RIGHT_HAND']]

### Confidence
- **Type**: typing.Optional[float]

### EquipmentDetections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.EquipmentDetection]]


# ProtectiveEquipmentPerson

### BodyParts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProtectiveEquipmentBodyPart]]

### BoundingBox
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[float]

### Id
- **Type**: typing.Optional[int]


# ProtectiveEquipmentSummarizationAttributes

### MinConfidence
- **Type**: <class 'float'>
- **Required**: Yes

### RequiredEquipmentTypes
- **Type**: typing.Sequence[typing.Literal['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']]
- **Required**: Yes


# ProtectiveEquipmentSummary

### PersonsWithRequiredEquipment
- **Type**: typing.Optional[typing.List[int]]

### PersonsWithoutRequiredEquipment
- **Type**: typing.Optional[typing.List[int]]

### PersonsIndeterminate
- **Type**: typing.Optional[typing.List[int]]


# PutProjectPolicyRequest

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# PutProjectPolicyResponse

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# RecognizeCelebritiesRequest

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes


# RecognizeCelebritiesResponse

### CelebrityFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Celebrity]
- **Required**: Yes

### UnrecognizedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ComparedFace]
- **Required**: Yes

### OrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# RegionOfInterest

### BoundingBox
- **Type**: <class 'NoneType'>

### Polygon
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.Point]]


# RegionOfInterestOutput

### BoundingBox
- **Type**: <class 'NoneType'>

### Polygon
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Point]]


# RegionOfInterestUnion

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


# S3Destination

### Bucket
- **Type**: typing.Optional[str]

### KeyPrefix
- **Type**: typing.Optional[str]


# S3Object

### Bucket
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# SearchFacesByImageRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### MaxFaces
- **Type**: typing.Optional[int]

### FaceMatchThreshold
- **Type**: typing.Optional[float]

### QualityFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'NONE']]


# SearchFacesByImageResponse

### SearchedFaceBoundingBox
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.BoundingBox'>
- **Required**: Yes

### SearchedFaceConfidence
- **Type**: <class 'float'>
- **Required**: Yes

### FaceMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceMatch]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# SearchFacesRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### FaceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxFaces
- **Type**: typing.Optional[int]

### FaceMatchThreshold
- **Type**: typing.Optional[float]


# SearchFacesResponse

### SearchedFaceId
- **Type**: <class 'str'>
- **Required**: Yes

### FaceMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceMatch]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# SearchUsersByImageRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Image'>
- **Required**: Yes

### UserMatchThreshold
- **Type**: typing.Optional[float]

### MaxUsers
- **Type**: typing.Optional[int]

### QualityFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'NONE']]


# SearchUsersByImageResponse

### UserMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UserMatch]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SearchedFace
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.SearchedFaceDetails'>
- **Required**: Yes

### UnsearchedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnsearchedFace]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# SearchUsersRequest

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### FaceId
- **Type**: typing.Optional[str]

### UserMatchThreshold
- **Type**: typing.Optional[float]

### MaxUsers
- **Type**: typing.Optional[int]


# SearchUsersResponse

### UserMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UserMatch]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SearchedFace
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.SearchedFace'>
- **Required**: Yes

### SearchedUser
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.SearchedUser'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# SearchedFace

### FaceId
- **Type**: typing.Optional[str]


# SearchedFaceDetails

### FaceDetail
- **Type**: <class 'NoneType'>


# SearchedUser

### UserId
- **Type**: typing.Optional[str]


# SegmentDetection

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SegmentTypeInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ShotSegment

### Index
- **Type**: typing.Optional[int]

### Confidence
- **Type**: typing.Optional[float]


# Smile

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# StartCelebrityRecognitionRequest

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### JobTag
- **Type**: typing.Optional[str]


# StartCelebrityRecognitionResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartContentModerationRequest

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### MinConfidence
- **Type**: typing.Optional[float]

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### JobTag
- **Type**: typing.Optional[str]


# StartContentModerationResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartFaceDetectionRequest

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### FaceAttributes
- **Type**: typing.Optional[typing.Literal['ALL', 'DEFAULT']]

### JobTag
- **Type**: typing.Optional[str]


# StartFaceDetectionResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartFaceSearchRequest

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### FaceMatchThreshold
- **Type**: typing.Optional[float]

### NotificationChannel
- **Type**: <class 'NoneType'>

### JobTag
- **Type**: typing.Optional[str]


# StartFaceSearchResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartLabelDetectionRequest

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### MinConfidence
- **Type**: typing.Optional[float]

### NotificationChannel
- **Type**: <class 'NoneType'>

### JobTag
- **Type**: typing.Optional[str]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['GENERAL_LABELS']]]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.LabelDetectionSettings]


# StartLabelDetectionResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartMediaAnalysisJobRequest

### OperationsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOperationsConfig'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisInput'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOutputConfig'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


# StartMediaAnalysisJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartPersonTrackingRequest

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### JobTag
- **Type**: typing.Optional[str]


# StartPersonTrackingResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartProjectVersionRequest

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### MinInferenceUnits
- **Type**: <class 'int'>
- **Required**: Yes

### MaxInferenceUnits
- **Type**: typing.Optional[int]


# StartProjectVersionResponse

### Status
- **Type**: typing.Literal['COPYING_COMPLETED', 'COPYING_FAILED', 'COPYING_IN_PROGRESS', 'DELETING', 'DEPRECATED', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'TRAINING_COMPLETED', 'TRAINING_FAILED', 'TRAINING_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartSegmentDetectionFilters

### TechnicalCueFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StartTechnicalCueDetectionFilter]

### ShotFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StartShotDetectionFilter]


# StartSegmentDetectionRequest

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### SegmentTypes
- **Type**: typing.Sequence[typing.Literal['SHOT', 'TECHNICAL_CUE']]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### JobTag
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StartSegmentDetectionFilters]


# StartSegmentDetectionResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartShotDetectionFilter

### MinSegmentConfidence
- **Type**: typing.Optional[float]


# StartStreamProcessorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StartSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessingStartSelector]

### StopSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessingStopSelector]


# StartStreamProcessorResponse

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StartTechnicalCueDetectionFilter

### MinSegmentConfidence
- **Type**: typing.Optional[float]

### BlackFrame
- **Type**: <class 'NoneType'>


# StartTextDetectionFilters

### WordFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectionFilter]

### RegionsOfInterest
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestUnion]]


# StartTextDetectionRequest

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.Video'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### JobTag
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StartTextDetectionFilters]


# StartTextDetectionResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StopProjectVersionRequest

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopProjectVersionResponse

### Status
- **Type**: typing.Literal['COPYING_COMPLETED', 'COPYING_FAILED', 'COPYING_IN_PROGRESS', 'DELETING', 'DEPRECATED', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'TRAINING_COMPLETED', 'TRAINING_FAILED', 'TRAINING_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadata'>
- **Required**: Yes


# StopStreamProcessorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StreamProcessingStartSelector

### KVSStreamStartSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.KinesisVideoStreamStartSelector]


# StreamProcessingStopSelector

### MaxDurationInSeconds
- **Type**: typing.Optional[int]


# StreamProcessor

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING']]


# StreamProcessorDataSharingPreference

### OptIn
- **Type**: <class 'bool'>
- **Required**: Yes


# StreamProcessorInput

### KinesisVideoStream
- **Type**: <class 'NoneType'>


# StreamProcessorNotificationChannel

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# StreamProcessorOutput

### KinesisDataStream
- **Type**: <class 'NoneType'>

### S3Destination
- **Type**: <class 'NoneType'>


# StreamProcessorSettings

### FaceSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceSearchSettings]

### ConnectedHome
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ConnectedHomeSettings]


# StreamProcessorSettingsForUpdate

### ConnectedHomeForUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ConnectedHomeSettingsForUpdate]


# StreamProcessorSettingsOutput

### FaceSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceSearchSettings]

### ConnectedHome
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ConnectedHomeSettingsOutput]


# StreamProcessorSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Summary

### S3Object
- **Type**: <class 'NoneType'>


# Sunglasses

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TestingData

### Assets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.Asset]]

### AutoCreate
- **Type**: typing.Optional[bool]


# TestingDataOutput

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Asset]]

### AutoCreate
- **Type**: typing.Optional[bool]


# TestingDataResult

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TestingDataOutput]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TestingDataOutput]

### Validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ValidationData]


# TestingDataUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TextDetection

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TextDetectionResult

### Timestamp
- **Type**: typing.Optional[int]

### TextDetection
- **Type**: <class 'NoneType'>


# TrainingData

### Assets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.Asset]]


# TrainingDataOutput

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Asset]]


# TrainingDataResult

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TrainingDataOutput]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TrainingDataOutput]

### Validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ValidationData]


# TrainingDataUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnindexedFace

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['EXCEEDS_MAX_FACES', 'EXTREME_POSE', 'LOW_BRIGHTNESS', 'LOW_CONFIDENCE', 'LOW_FACE_QUALITY', 'LOW_SHARPNESS', 'SMALL_BOUNDING_BOX']]]

### FaceDetail
- **Type**: <class 'NoneType'>


# UnsearchedFace

### FaceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetail]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['EXCEEDS_MAX_FACES', 'EXTREME_POSE', 'FACE_NOT_LARGEST', 'LOW_BRIGHTNESS', 'LOW_CONFIDENCE', 'LOW_FACE_QUALITY', 'LOW_SHARPNESS', 'SMALL_BOUNDING_BOX']]]


# UnsuccessfulFaceAssociation

### FaceId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['ASSOCIATED_TO_A_DIFFERENT_USER', 'FACE_NOT_FOUND', 'LOW_MATCH_CONFIDENCE']]]


# UnsuccessfulFaceDeletion

### FaceId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['ASSOCIATED_TO_AN_EXISTING_USER', 'FACE_NOT_FOUND']]]


# UnsuccessfulFaceDisassociation

### FaceId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['ASSOCIATED_TO_A_DIFFERENT_USER', 'FACE_NOT_FOUND']]]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetEntriesRequest

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Changes
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.DatasetChanges'>
- **Required**: Yes


# UpdateStreamProcessorRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SettingsForUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorSettingsForUpdate]

### RegionsOfInterestForUpdate
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestUnion]]

### DataSharingPreferenceForUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorDataSharingPreference]

### ParametersToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ConnectedHomeMinConfidence', 'RegionsOfInterest']]]


# User

### UserId
- **Type**: typing.Optional[str]

### UserStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATED', 'CREATING', 'UPDATING']]


# UserMatch

### Similarity
- **Type**: typing.Optional[float]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MatchedUser]


# ValidationData

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.Asset]]


# Video

### S3Object
- **Type**: <class 'NoneType'>


# VideoMetadata

### Codec
- **Type**: typing.Optional[str]

### DurationMillis
- **Type**: typing.Optional[int]

### Format
- **Type**: typing.Optional[str]

### FrameRate
- **Type**: typing.Optional[float]

### FrameHeight
- **Type**: typing.Optional[int]

### FrameWidth
- **Type**: typing.Optional[int]

### ColorRange
- **Type**: typing.Optional[typing.Literal['FULL', 'LIMITED']]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



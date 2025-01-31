# Rekognition Classes

# AgeRangeTypeDef

### Low
- **Type**: typing.Optional[int]

### High
- **Type**: typing.Optional[int]


# AssetTypeDef

### GroundTruthManifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GroundTruthManifestTypeDef]


# AssociateFacesRequestRequestTypeDef

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


# AssociateFacesResponseTypeDef

### AssociatedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AssociatedFaceTypeDef]
- **Required**: Yes

### UnsuccessfulFaceAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnsuccessfulFaceAssociationTypeDef]
- **Required**: Yes

### UserStatus
- **Type**: typing.Literal['ACTIVE', 'CREATED', 'CREATING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatedFaceTypeDef

### FaceId
- **Type**: typing.Optional[str]


# AudioMetadataTypeDef

### Codec
- **Type**: typing.Optional[str]

### DurationMillis
- **Type**: typing.Optional[int]

### SampleRate
- **Type**: typing.Optional[int]

### NumberOfChannels
- **Type**: typing.Optional[int]


# AuditImageTypeDef

### Bytes
- **Type**: typing.Optional[bytes]

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.S3ObjectTypeDef]

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BeardTypeDef

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# BlackFrameTypeDef

### MaxPixelThreshold
- **Type**: typing.Optional[float]

### MinCoveragePercentage
- **Type**: typing.Optional[float]


# BoundingBoxTypeDef

### Width
- **Type**: typing.Optional[float]

### Height
- **Type**: typing.Optional[float]

### Left
- **Type**: typing.Optional[float]

### Top
- **Type**: typing.Optional[float]


# CelebrityDetailTypeDef

### Urls
- **Type**: typing.Optional[typing.List[str]]

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetailTypeDef]

### KnownGender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.KnownGenderTypeDef]


# CelebrityRecognitionTypeDef

### Timestamp
- **Type**: typing.Optional[int]

### Celebrity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CelebrityDetailTypeDef]


# CelebrityTypeDef

### Urls
- **Type**: typing.Optional[typing.List[str]]

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ComparedFaceTypeDef]

### MatchConfidence
- **Type**: typing.Optional[float]

### KnownGender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.KnownGenderTypeDef]


# CompareFacesMatchTypeDef

### Similarity
- **Type**: typing.Optional[float]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ComparedFaceTypeDef]


# CompareFacesRequestRequestTypeDef

### SourceImage
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### TargetImage
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### SimilarityThreshold
- **Type**: typing.Optional[float]

### QualityFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'NONE']]


# CompareFacesResponseTypeDef

### SourceImageFace
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ComparedSourceImageFaceTypeDef'>
- **Required**: Yes

### FaceMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.CompareFacesMatchTypeDef]
- **Required**: Yes

### UnmatchedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ComparedFaceTypeDef]
- **Required**: Yes

### SourceImageOrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### TargetImageOrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ComparedFaceTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Confidence
- **Type**: typing.Optional[float]

### Landmarks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LandmarkTypeDef]]

### Pose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PoseTypeDef]

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ImageQualityTypeDef]

### Emotions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.EmotionTypeDef]]

### Smile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.SmileTypeDef]


# ComparedSourceImageFaceTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Confidence
- **Type**: typing.Optional[float]


# ConnectedHomeSettingsForUpdateTypeDef

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]

### MinConfidence
- **Type**: typing.Optional[float]


# ConnectedHomeSettingsOutputTypeDef

### Labels
- **Type**: typing.List[str]
- **Required**: Yes

### MinConfidence
- **Type**: typing.Optional[float]


# ConnectedHomeSettingsTypeDef

### Labels
- **Type**: typing.Sequence[str]
- **Required**: Yes

### MinConfidence
- **Type**: typing.Optional[float]


# ContentModerationDetectionTypeDef

### Timestamp
- **Type**: typing.Optional[int]

### ModerationLabel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ModerationLabelTypeDef]

### StartTimestampMillis
- **Type**: typing.Optional[int]

### EndTimestampMillis
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]

### ContentTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ContentTypeTypeDef]]


# ContentTypeTypeDef

### Confidence
- **Type**: typing.Optional[float]

### Name
- **Type**: typing.Optional[str]


# CopyProjectVersionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.OutputConfigTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KmsKeyId
- **Type**: typing.Optional[str]


# CopyProjectVersionResponseTypeDef

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CoversBodyPartTypeDef

### Confidence
- **Type**: typing.Optional[float]

### Value
- **Type**: typing.Optional[bool]


# CreateCollectionRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCollectionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetRequestRequestTypeDef

### DatasetType
- **Type**: typing.Literal['TEST', 'TRAIN']
- **Required**: Yes

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DatasetSourceTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDatasetResponseTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFaceLivenessSessionRequestRequestTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CreateFaceLivenessSessionRequestSettingsTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateFaceLivenessSessionRequestSettingsTypeDef

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.LivenessOutputConfigTypeDef]

### AuditImagesLimit
- **Type**: typing.Optional[int]


# CreateFaceLivenessSessionResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectRequestRequestTypeDef

### ProjectName
- **Type**: <class 'str'>
- **Required**: Yes

### Feature
- **Type**: typing.Optional[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]

### AutoUpdate
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProjectResponseTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectVersionRequestRequestTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionName
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.OutputConfigTypeDef'>
- **Required**: Yes

### TrainingData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TrainingDataTypeDef]

### TestingData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TestingDataTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KmsKeyId
- **Type**: typing.Optional[str]

### VersionDescription
- **Type**: typing.Optional[str]

### FeatureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CustomizationFeatureConfigTypeDef]


# CreateProjectVersionResponseTypeDef

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamProcessorRequestRequestTypeDef

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorInputTypeDef'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorOutputTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorSettingsTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorNotificationChannelTypeDef]

### KmsKeyId
- **Type**: typing.Optional[str]

### RegionsOfInterest
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestTypeDef, aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestOutputTypeDef]]]

### DataSharingPreference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorDataSharingPreferenceTypeDef]


# CreateStreamProcessorResponseTypeDef

### StreamProcessorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CustomLabelTypeDef

### Name
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GeometryTypeDef]


# CustomizationFeatureConfigTypeDef

### ContentModeration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CustomizationFeatureContentModerationConfigTypeDef]


# CustomizationFeatureContentModerationConfigTypeDef

### ConfidenceThreshold
- **Type**: typing.Optional[float]


# DatasetChangesTypeDef

### GroundTruth
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# DatasetDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DatasetStatsTypeDef]


# DatasetLabelDescriptionTypeDef

### LabelName
- **Type**: typing.Optional[str]

### LabelStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DatasetLabelStatsTypeDef]


# DatasetLabelStatsTypeDef

### EntryCount
- **Type**: typing.Optional[int]

### BoundingBoxCount
- **Type**: typing.Optional[int]


# DatasetMetadataTypeDef

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


# DatasetSourceTypeDef

### GroundTruthManifest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GroundTruthManifestTypeDef]

### DatasetArn
- **Type**: typing.Optional[str]


# DatasetStatsTypeDef

### LabeledEntries
- **Type**: typing.Optional[int]

### TotalEntries
- **Type**: typing.Optional[int]

### TotalLabels
- **Type**: typing.Optional[int]

### ErrorEntries
- **Type**: typing.Optional[int]


# DeleteCollectionRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCollectionResponseTypeDef

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDatasetRequestRequestTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFacesRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### FaceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteFacesResponseTypeDef

### DeletedFaces
- **Type**: typing.List[str]
- **Required**: Yes

### UnsuccessfulFaceDeletions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnsuccessfulFaceDeletionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectPolicyRequestRequestTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DeleteProjectRequestRequestTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectResponseTypeDef

### Status
- **Type**: typing.Literal['CREATED', 'CREATING', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectVersionRequestRequestTypeDef

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectVersionResponseTypeDef

### Status
- **Type**: typing.Literal['COPYING_COMPLETED', 'COPYING_FAILED', 'COPYING_IN_PROGRESS', 'DELETING', 'DEPRECATED', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'TRAINING_COMPLETED', 'TRAINING_FAILED', 'TRAINING_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStreamProcessorRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DescribeCollectionRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCollectionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatasetRequestRequestTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

### DatasetDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.DatasetDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProjectVersionsRequestDescribeProjectVersionsPaginateTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# DescribeProjectVersionsRequestProjectVersionRunningWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.WaiterConfigTypeDef]


# DescribeProjectVersionsRequestProjectVersionTrainingCompletedWaitTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.WaiterConfigTypeDef]


# DescribeProjectVersionsRequestRequestTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNames
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeProjectVersionsResponseTypeDef

### ProjectVersionDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProjectVersionDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeProjectsRequestDescribeProjectsPaginateTypeDef

### ProjectNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# DescribeProjectsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ProjectNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]]


# DescribeProjectsResponseTypeDef

### ProjectDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProjectDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStreamProcessorRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStreamProcessorResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorInputTypeDef'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorSettingsOutputTypeDef'>
- **Required**: Yes

### NotificationChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorNotificationChannelTypeDef'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### RegionsOfInterest
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestOutputTypeDef]
- **Required**: Yes

### DataSharingPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorDataSharingPreferenceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectCustomLabelsRequestRequestTypeDef

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### MinConfidence
- **Type**: typing.Optional[float]


# DetectCustomLabelsResponseTypeDef

### CustomLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.CustomLabelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectFacesRequestRequestTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGE_RANGE', 'ALL', 'BEARD', 'DEFAULT', 'EMOTIONS', 'EYEGLASSES', 'EYES_OPEN', 'EYE_DIRECTION', 'FACE_OCCLUDED', 'GENDER', 'MOUTH_OPEN', 'MUSTACHE', 'SMILE', 'SUNGLASSES']]]


# DetectFacesResponseTypeDef

### FaceDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetailTypeDef]
- **Required**: Yes

### OrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectLabelsImageBackgroundTypeDef

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageQualityTypeDef]

### DominantColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DominantColorTypeDef]]


# DetectLabelsImageForegroundTypeDef

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageQualityTypeDef]

### DominantColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DominantColorTypeDef]]


# DetectLabelsImagePropertiesSettingsTypeDef

### MaxDominantColors
- **Type**: typing.Optional[int]


# DetectLabelsImagePropertiesTypeDef

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageQualityTypeDef]

### DominantColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DominantColorTypeDef]]

### Foreground
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageForegroundTypeDef]

### Background
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImageBackgroundTypeDef]


# DetectLabelsImageQualityTypeDef

### Brightness
- **Type**: typing.Optional[float]

### Sharpness
- **Type**: typing.Optional[float]

### Contrast
- **Type**: typing.Optional[float]


# DetectLabelsRequestRequestTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### MaxLabels
- **Type**: typing.Optional[int]

### MinConfidence
- **Type**: typing.Optional[float]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['GENERAL_LABELS', 'IMAGE_PROPERTIES']]]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsSettingsTypeDef]


# DetectLabelsResponseTypeDef

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LabelTypeDef]
- **Required**: Yes

### OrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### LabelModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ImageProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImagePropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectLabelsSettingsTypeDef

### GeneralLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GeneralLabelsSettingsTypeDef]

### ImageProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectLabelsImagePropertiesSettingsTypeDef]


# DetectModerationLabelsRequestRequestTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### MinConfidence
- **Type**: typing.Optional[float]

### HumanLoopConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.HumanLoopConfigTypeDef]

### ProjectVersion
- **Type**: typing.Optional[str]


# DetectModerationLabelsResponseTypeDef

### ModerationLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ModerationLabelTypeDef]
- **Required**: Yes

### ModerationModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### HumanLoopActivationOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.HumanLoopActivationOutputTypeDef'>
- **Required**: Yes

### ProjectVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ContentTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ContentTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectProtectiveEquipmentRequestRequestTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### SummarizationAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ProtectiveEquipmentSummarizationAttributesTypeDef]


# DetectProtectiveEquipmentResponseTypeDef

### ProtectiveEquipmentModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Persons
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProtectiveEquipmentPersonTypeDef]
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ProtectiveEquipmentSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectTextFiltersTypeDef

### WordFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectionFilterTypeDef]

### RegionsOfInterest
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestTypeDef]]


# DetectTextRequestRequestTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectTextFiltersTypeDef]


# DetectTextResponseTypeDef

### TextDetections
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.TextDetectionTypeDef]
- **Required**: Yes

### TextModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectionFilterTypeDef

### MinConfidence
- **Type**: typing.Optional[float]

### MinBoundingBoxHeight
- **Type**: typing.Optional[float]

### MinBoundingBoxWidth
- **Type**: typing.Optional[float]


# DisassociateFacesRequestRequestTypeDef

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


# DisassociateFacesResponseTypeDef

### DisassociatedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DisassociatedFaceTypeDef]
- **Required**: Yes

### UnsuccessfulFaceDisassociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnsuccessfulFaceDisassociationTypeDef]
- **Required**: Yes

### UserStatus
- **Type**: typing.Literal['ACTIVE', 'CREATED', 'CREATING', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociatedFaceTypeDef

### FaceId
- **Type**: typing.Optional[str]


# DistributeDatasetEntriesRequestRequestTypeDef

### Datasets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.DistributeDatasetTypeDef]
- **Required**: Yes


# DistributeDatasetTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DominantColorTypeDef

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


# EmotionTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['ANGRY', 'CALM', 'CONFUSED', 'DISGUSTED', 'FEAR', 'HAPPY', 'SAD', 'SURPRISED', 'UNKNOWN']]

### Confidence
- **Type**: typing.Optional[float]


# EquipmentDetectionTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Confidence
- **Type**: typing.Optional[float]

### Type
- **Type**: typing.Optional[typing.Literal['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']]

### CoversBodyPart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CoversBodyPartTypeDef]


# EvaluationResultTypeDef

### F1Score
- **Type**: typing.Optional[float]

### Summary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.SummaryTypeDef]


# EyeDirectionTypeDef

### Yaw
- **Type**: typing.Optional[float]

### Pitch
- **Type**: typing.Optional[float]

### Confidence
- **Type**: typing.Optional[float]


# EyeOpenTypeDef

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# EyeglassesTypeDef

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# FaceDetailTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### AgeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.AgeRangeTypeDef]

### Smile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.SmileTypeDef]

### Eyeglasses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.EyeglassesTypeDef]

### Sunglasses
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.SunglassesTypeDef]

### Gender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GenderTypeDef]

### Beard
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BeardTypeDef]

### Mustache
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MustacheTypeDef]

### EyesOpen
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.EyeOpenTypeDef]

### MouthOpen
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MouthOpenTypeDef]

### Emotions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.EmotionTypeDef]]

### Landmarks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LandmarkTypeDef]]

### Pose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PoseTypeDef]

### Quality
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ImageQualityTypeDef]

### Confidence
- **Type**: typing.Optional[float]

### FaceOccluded
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceOccludedTypeDef]

### EyeDirection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.EyeDirectionTypeDef]


# FaceDetectionTypeDef

### Timestamp
- **Type**: typing.Optional[int]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetailTypeDef]


# FaceMatchTypeDef

### Similarity
- **Type**: typing.Optional[float]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceTypeDef]


# FaceOccludedTypeDef

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# FaceRecordTypeDef

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceTypeDef]

### FaceDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetailTypeDef]


# FaceSearchSettingsTypeDef

### CollectionId
- **Type**: typing.Optional[str]

### FaceMatchThreshold
- **Type**: typing.Optional[float]


# FaceTypeDef

### FaceId
- **Type**: typing.Optional[str]

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

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


# GenderTypeDef

### Value
- **Type**: typing.Optional[typing.Literal['Female', 'Male']]

### Confidence
- **Type**: typing.Optional[float]


# GeneralLabelsSettingsTypeDef

### LabelInclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### LabelExclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### LabelCategoryInclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### LabelCategoryExclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]


# GeometryTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Polygon
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.PointTypeDef]]


# GetCelebrityInfoRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# GetCelebrityInfoResponseTypeDef

### Urls
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### KnownGender
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.KnownGenderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCelebrityRecognitionRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['ID', 'TIMESTAMP']]


# GetCelebrityRecognitionResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadataTypeDef'>
- **Required**: Yes

### Celebrities
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.CelebrityRecognitionTypeDef]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetContentModerationRequestMetadataTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['NAME', 'TIMESTAMP']]

### AggregateBy
- **Type**: typing.Optional[typing.Literal['SEGMENTS', 'TIMESTAMPS']]


# GetContentModerationRequestRequestTypeDef

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


# GetContentModerationResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadataTypeDef'>
- **Required**: Yes

### ModerationLabels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ContentModerationDetectionTypeDef]
- **Required**: Yes

### ModerationModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### GetRequestMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.GetContentModerationRequestMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFaceDetectionRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetFaceDetectionResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadataTypeDef'>
- **Required**: Yes

### Faces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetectionTypeDef]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetFaceLivenessSessionResultsRequestRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetFaceLivenessSessionResultsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.AuditImageTypeDef'>
- **Required**: Yes

### AuditImages
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AuditImageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFaceSearchRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['INDEX', 'TIMESTAMP']]


# GetFaceSearchResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadataTypeDef'>
- **Required**: Yes

### Persons
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.PersonMatchTypeDef]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLabelDetectionRequestMetadataTypeDef

### SortBy
- **Type**: typing.Optional[typing.Literal['NAME', 'TIMESTAMP']]

### AggregateBy
- **Type**: typing.Optional[typing.Literal['SEGMENTS', 'TIMESTAMPS']]


# GetLabelDetectionRequestRequestTypeDef

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


# GetLabelDetectionResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadataTypeDef'>
- **Required**: Yes

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LabelDetectionTypeDef]
- **Required**: Yes

### LabelModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### GetRequestMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.GetLabelDetectionRequestMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMediaAnalysisJobRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaAnalysisJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### OperationsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOperationsConfigTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']
- **Required**: Yes

### FailureDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisJobFailureDetailsTypeDef'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisInputTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOutputConfigTypeDef'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Results
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisResultsTypeDef'>
- **Required**: Yes

### ManifestSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisManifestSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPersonTrackingRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SortBy
- **Type**: typing.Optional[typing.Literal['INDEX', 'TIMESTAMP']]


# GetPersonTrackingResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadataTypeDef'>
- **Required**: Yes

### Persons
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.PersonDetectionTypeDef]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSegmentDetectionRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetSegmentDetectionResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadataTypeDef]
- **Required**: Yes

### AudioMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AudioMetadataTypeDef]
- **Required**: Yes

### Segments
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.SegmentDetectionTypeDef]
- **Required**: Yes

### SelectedSegmentTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.SegmentTypeInfoTypeDef]
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTextDetectionRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetTextDetectionResponseTypeDef

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### VideoMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoMetadataTypeDef'>
- **Required**: Yes

### TextDetections
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.TextDetectionResultTypeDef]
- **Required**: Yes

### TextModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### JobTag
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GroundTruthManifestTypeDef

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.S3ObjectTypeDef]


# HumanLoopActivationOutputTypeDef

### HumanLoopArn
- **Type**: typing.Optional[str]

### HumanLoopActivationReasons
- **Type**: typing.Optional[typing.List[str]]

### HumanLoopActivationConditionsEvaluationResults
- **Type**: typing.Optional[str]


# HumanLoopConfigTypeDef

### HumanLoopName
- **Type**: <class 'str'>
- **Required**: Yes

### FlowDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.HumanLoopDataAttributesTypeDef]


# HumanLoopDataAttributesTypeDef

### ContentClassifiers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]]


# ImageQualityTypeDef

### Brightness
- **Type**: typing.Optional[float]

### Sharpness
- **Type**: typing.Optional[float]


# ImageTypeDef

### Bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.S3ObjectTypeDef]


# IndexFacesRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### ExternalImageId
- **Type**: typing.Optional[str]

### DetectionAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AGE_RANGE', 'ALL', 'BEARD', 'DEFAULT', 'EMOTIONS', 'EYEGLASSES', 'EYES_OPEN', 'EYE_DIRECTION', 'FACE_OCCLUDED', 'GENDER', 'MOUTH_OPEN', 'MUSTACHE', 'SMILE', 'SUNGLASSES']]]

### MaxFaces
- **Type**: typing.Optional[int]

### QualityFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'NONE']]


# IndexFacesResponseTypeDef

### FaceRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceRecordTypeDef]
- **Required**: Yes

### OrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### UnindexedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnindexedFaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InstanceTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Confidence
- **Type**: typing.Optional[float]

### DominantColors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DominantColorTypeDef]]


# KinesisDataStreamTypeDef

### Arn
- **Type**: typing.Optional[str]


# KinesisVideoStreamStartSelectorTypeDef

### ProducerTimestamp
- **Type**: typing.Optional[int]

### FragmentNumber
- **Type**: typing.Optional[str]


# KinesisVideoStreamTypeDef

### Arn
- **Type**: typing.Optional[str]


# KnownGenderTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['Female', 'Male', 'Nonbinary', 'Unlisted']]


# LabelAliasTypeDef

### Name
- **Type**: typing.Optional[str]


# LabelCategoryTypeDef

### Name
- **Type**: typing.Optional[str]


# LabelDetectionSettingsTypeDef

### GeneralLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GeneralLabelsSettingsTypeDef]


# LabelDetectionTypeDef

### Timestamp
- **Type**: typing.Optional[int]

### Label
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.LabelTypeDef]

### StartTimestampMillis
- **Type**: typing.Optional[int]

### EndTimestampMillis
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]


# LabelTypeDef

### Name
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### Instances
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.InstanceTypeDef]]

### Parents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ParentTypeDef]]

### Aliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LabelAliasTypeDef]]

### Categories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.LabelCategoryTypeDef]]


# LandmarkTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['chinBottom', 'eyeLeft', 'eyeRight', 'leftEyeBrowLeft', 'leftEyeBrowRight', 'leftEyeBrowUp', 'leftEyeDown', 'leftEyeLeft', 'leftEyeRight', 'leftEyeUp', 'leftPupil', 'midJawlineLeft', 'midJawlineRight', 'mouthDown', 'mouthLeft', 'mouthRight', 'mouthUp', 'nose', 'noseLeft', 'noseRight', 'rightEyeBrowLeft', 'rightEyeBrowRight', 'rightEyeBrowUp', 'rightEyeDown', 'rightEyeLeft', 'rightEyeRight', 'rightEyeUp', 'rightPupil', 'upperJawlineLeft', 'upperJawlineRight']]

### X
- **Type**: typing.Optional[float]

### Y
- **Type**: typing.Optional[float]


# ListCollectionsRequestListCollectionsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# ListCollectionsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListCollectionsResponseTypeDef

### CollectionIds
- **Type**: typing.List[str]
- **Required**: Yes

### FaceModelVersions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetEntriesRequestListDatasetEntriesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# ListDatasetEntriesRequestRequestTypeDef

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


# ListDatasetEntriesResponseTypeDef

### DatasetEntries
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatasetLabelsRequestListDatasetLabelsPaginateTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# ListDatasetLabelsRequestRequestTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetLabelsResponseTypeDef

### DatasetLabelDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DatasetLabelDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFacesRequestListFacesPaginateTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### FaceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# ListFacesRequestRequestTypeDef

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


# ListFacesResponseTypeDef

### Faces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceTypeDef]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMediaAnalysisJobsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaAnalysisJobsResponseTypeDef

### MediaAnalysisJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisJobDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProjectPoliciesRequestListProjectPoliciesPaginateTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# ListProjectPoliciesRequestRequestTypeDef

### ProjectArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProjectPoliciesResponseTypeDef

### ProjectPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProjectPolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamProcessorsRequestListStreamProcessorsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# ListStreamProcessorsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListStreamProcessorsResponseTypeDef

### StreamProcessors
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersRequestListUsersPaginateTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PaginatorConfigTypeDef]


# ListUsersRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UserTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LivenessOutputConfigTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]


# MatchedUserTypeDef

### UserId
- **Type**: typing.Optional[str]

### UserStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATED', 'CREATING', 'UPDATING']]


# MediaAnalysisDetectModerationLabelsConfigTypeDef

### MinConfidence
- **Type**: typing.Optional[float]

### ProjectVersion
- **Type**: typing.Optional[str]


# MediaAnalysisInputTypeDef

### S3Object
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.S3ObjectTypeDef'>
- **Required**: Yes


# MediaAnalysisJobDescriptionTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### OperationsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOperationsConfigTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisInputTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOutputConfigTypeDef'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisJobFailureDetailsTypeDef]

### CompletionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### KmsKeyId
- **Type**: typing.Optional[str]

### Results
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisResultsTypeDef]

### ManifestSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisManifestSummaryTypeDef]


# MediaAnalysisJobFailureDetailsTypeDef

### Code
- **Type**: typing.Optional[typing.Literal['ACCESS_DENIED', 'INTERNAL_ERROR', 'INVALID_KMS_KEY', 'INVALID_MANIFEST', 'INVALID_OUTPUT_CONFIG', 'INVALID_S3_OBJECT', 'RESOURCE_NOT_FOUND', 'RESOURCE_NOT_READY', 'THROTTLED']]

### Message
- **Type**: typing.Optional[str]


# MediaAnalysisManifestSummaryTypeDef

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.S3ObjectTypeDef]


# MediaAnalysisModelVersionsTypeDef

### Moderation
- **Type**: typing.Optional[str]


# MediaAnalysisOperationsConfigTypeDef

### DetectModerationLabels
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisDetectModerationLabelsConfigTypeDef]


# MediaAnalysisOutputConfigTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3KeyPrefix
- **Type**: typing.Optional[str]


# MediaAnalysisResultsTypeDef

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.S3ObjectTypeDef]

### ModelVersions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisModelVersionsTypeDef]


# ModerationLabelTypeDef

### Confidence
- **Type**: typing.Optional[float]

### Name
- **Type**: typing.Optional[str]

### ParentName
- **Type**: typing.Optional[str]

### TaxonomyLevel
- **Type**: typing.Optional[int]


# MouthOpenTypeDef

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# MustacheTypeDef

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# NotificationChannelTypeDef

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# OutputConfigTypeDef

### S3Bucket
- **Type**: typing.Optional[str]

### S3KeyPrefix
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParentTypeDef

### Name
- **Type**: typing.Optional[str]


# PersonDetailTypeDef

### Index
- **Type**: typing.Optional[int]

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Face
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetailTypeDef]


# PersonDetectionTypeDef

### Timestamp
- **Type**: typing.Optional[int]

### Person
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PersonDetailTypeDef]


# PersonMatchTypeDef

### Timestamp
- **Type**: typing.Optional[int]

### Person
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.PersonDetailTypeDef]

### FaceMatches
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceMatchTypeDef]]


# PointTypeDef

### X
- **Type**: typing.Optional[float]

### Y
- **Type**: typing.Optional[float]


# PoseTypeDef

### Roll
- **Type**: typing.Optional[float]

### Yaw
- **Type**: typing.Optional[float]

### Pitch
- **Type**: typing.Optional[float]


# ProjectDescriptionTypeDef

### ProjectArn
- **Type**: typing.Optional[str]

### CreationTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'DELETING']]

### Datasets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.DatasetMetadataTypeDef]]

### Feature
- **Type**: typing.Optional[typing.Literal['CONTENT_MODERATION', 'CUSTOM_LABELS']]

### AutoUpdate
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ProjectPolicyTypeDef

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


# ProjectVersionDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.OutputConfigTypeDef]

### TrainingDataResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TrainingDataResultTypeDef]

### TestingDataResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TestingDataResultTypeDef]

### EvaluationResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.EvaluationResultTypeDef]

### ManifestSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GroundTruthManifestTypeDef]

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

### BaseValidatorModelVersion
- **Type**: typing.Optional[str]

### FeatureConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.CustomizationFeatureConfigTypeDef]


# ProtectiveEquipmentBodyPartTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['FACE', 'HEAD', 'LEFT_HAND', 'RIGHT_HAND']]

### Confidence
- **Type**: typing.Optional[float]

### EquipmentDetections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.EquipmentDetectionTypeDef]]


# ProtectiveEquipmentPersonTypeDef

### BodyParts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ProtectiveEquipmentBodyPartTypeDef]]

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Confidence
- **Type**: typing.Optional[float]

### Id
- **Type**: typing.Optional[int]


# ProtectiveEquipmentSummarizationAttributesTypeDef

### MinConfidence
- **Type**: <class 'float'>
- **Required**: Yes

### RequiredEquipmentTypes
- **Type**: typing.Sequence[typing.Literal['FACE_COVER', 'HAND_COVER', 'HEAD_COVER']]
- **Required**: Yes


# ProtectiveEquipmentSummaryTypeDef

### PersonsWithRequiredEquipment
- **Type**: typing.Optional[typing.List[int]]

### PersonsWithoutRequiredEquipment
- **Type**: typing.Optional[typing.List[int]]

### PersonsIndeterminate
- **Type**: typing.Optional[typing.List[int]]


# PutProjectPolicyRequestRequestTypeDef

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


# PutProjectPolicyResponseTypeDef

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecognizeCelebritiesRequestRequestTypeDef

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes


# RecognizeCelebritiesResponseTypeDef

### CelebrityFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.CelebrityTypeDef]
- **Required**: Yes

### UnrecognizedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.ComparedFaceTypeDef]
- **Required**: Yes

### OrientationCorrection
- **Type**: typing.Literal['ROTATE_0', 'ROTATE_180', 'ROTATE_270', 'ROTATE_90']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegionOfInterestOutputTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Polygon
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.PointTypeDef]]


# RegionOfInterestTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef]

### Polygon
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.PointTypeDef]]


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


# S3DestinationTypeDef

### Bucket
- **Type**: typing.Optional[str]

### KeyPrefix
- **Type**: typing.Optional[str]


# S3ObjectTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# SearchFacesByImageRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### MaxFaces
- **Type**: typing.Optional[int]

### FaceMatchThreshold
- **Type**: typing.Optional[float]

### QualityFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'NONE']]


# SearchFacesByImageResponseTypeDef

### SearchedFaceBoundingBox
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.BoundingBoxTypeDef'>
- **Required**: Yes

### SearchedFaceConfidence
- **Type**: <class 'float'>
- **Required**: Yes

### FaceMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceMatchTypeDef]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchFacesRequestRequestTypeDef

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


# SearchFacesResponseTypeDef

### SearchedFaceId
- **Type**: <class 'str'>
- **Required**: Yes

### FaceMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.FaceMatchTypeDef]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchUsersByImageRequestRequestTypeDef

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### Image
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ImageTypeDef'>
- **Required**: Yes

### UserMatchThreshold
- **Type**: typing.Optional[float]

### MaxUsers
- **Type**: typing.Optional[int]

### QualityFilter
- **Type**: typing.Optional[typing.Literal['AUTO', 'HIGH', 'LOW', 'MEDIUM', 'NONE']]


# SearchUsersByImageResponseTypeDef

### UserMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UserMatchTypeDef]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SearchedFace
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.SearchedFaceDetailsTypeDef'>
- **Required**: Yes

### UnsearchedFaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UnsearchedFaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchUsersRequestRequestTypeDef

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


# SearchUsersResponseTypeDef

### UserMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.rekognition_classes.UserMatchTypeDef]
- **Required**: Yes

### FaceModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SearchedFace
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.SearchedFaceTypeDef'>
- **Required**: Yes

### SearchedUser
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.SearchedUserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchedFaceDetailsTypeDef

### FaceDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetailTypeDef]


# SearchedFaceTypeDef

### FaceId
- **Type**: typing.Optional[str]


# SearchedUserTypeDef

### UserId
- **Type**: typing.Optional[str]


# SegmentDetectionTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['SHOT', 'TECHNICAL_CUE']]

### StartTimestampMillis
- **Type**: typing.Optional[int]

### EndTimestampMillis
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]

### StartTimecodeSMPTE
- **Type**: typing.Optional[str]

### EndTimecodeSMPTE
- **Type**: typing.Optional[str]

### DurationSMPTE
- **Type**: typing.Optional[str]

### TechnicalCueSegment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TechnicalCueSegmentTypeDef]

### ShotSegment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ShotSegmentTypeDef]

### StartFrameNumber
- **Type**: typing.Optional[int]

### EndFrameNumber
- **Type**: typing.Optional[int]

### DurationFrames
- **Type**: typing.Optional[int]


# SegmentTypeInfoTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['SHOT', 'TECHNICAL_CUE']]

### ModelVersion
- **Type**: typing.Optional[str]


# ShotSegmentTypeDef

### Index
- **Type**: typing.Optional[int]

### Confidence
- **Type**: typing.Optional[float]


# SmileTypeDef

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# StartCelebrityRecognitionRequestRequestTypeDef

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.NotificationChannelTypeDef]

### JobTag
- **Type**: typing.Optional[str]


# StartCelebrityRecognitionResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartContentModerationRequestRequestTypeDef

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### MinConfidence
- **Type**: typing.Optional[float]

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.NotificationChannelTypeDef]

### JobTag
- **Type**: typing.Optional[str]


# StartContentModerationResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartFaceDetectionRequestRequestTypeDef

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.NotificationChannelTypeDef]

### FaceAttributes
- **Type**: typing.Optional[typing.Literal['ALL', 'DEFAULT']]

### JobTag
- **Type**: typing.Optional[str]


# StartFaceDetectionResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartFaceSearchRequestRequestTypeDef

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### CollectionId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### FaceMatchThreshold
- **Type**: typing.Optional[float]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.NotificationChannelTypeDef]

### JobTag
- **Type**: typing.Optional[str]


# StartFaceSearchResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartLabelDetectionRequestRequestTypeDef

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### MinConfidence
- **Type**: typing.Optional[float]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.NotificationChannelTypeDef]

### JobTag
- **Type**: typing.Optional[str]

### Features
- **Type**: typing.Optional[typing.Sequence[typing.Literal['GENERAL_LABELS']]]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.LabelDetectionSettingsTypeDef]


# StartLabelDetectionResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMediaAnalysisJobRequestRequestTypeDef

### OperationsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOperationsConfigTypeDef'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisInputTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.MediaAnalysisOutputConfigTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]


# StartMediaAnalysisJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartPersonTrackingRequestRequestTypeDef

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.NotificationChannelTypeDef]

### JobTag
- **Type**: typing.Optional[str]


# StartPersonTrackingResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartProjectVersionRequestRequestTypeDef

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### MinInferenceUnits
- **Type**: <class 'int'>
- **Required**: Yes

### MaxInferenceUnits
- **Type**: typing.Optional[int]


# StartProjectVersionResponseTypeDef

### Status
- **Type**: typing.Literal['COPYING_COMPLETED', 'COPYING_FAILED', 'COPYING_IN_PROGRESS', 'DELETING', 'DEPRECATED', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'TRAINING_COMPLETED', 'TRAINING_FAILED', 'TRAINING_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSegmentDetectionFiltersTypeDef

### TechnicalCueFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StartTechnicalCueDetectionFilterTypeDef]

### ShotFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StartShotDetectionFilterTypeDef]


# StartSegmentDetectionRequestRequestTypeDef

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### SegmentTypes
- **Type**: typing.Sequence[typing.Literal['SHOT', 'TECHNICAL_CUE']]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.NotificationChannelTypeDef]

### JobTag
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StartSegmentDetectionFiltersTypeDef]


# StartSegmentDetectionResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartShotDetectionFilterTypeDef

### MinSegmentConfidence
- **Type**: typing.Optional[float]


# StartStreamProcessorRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StartSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessingStartSelectorTypeDef]

### StopSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessingStopSelectorTypeDef]


# StartStreamProcessorResponseTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTechnicalCueDetectionFilterTypeDef

### MinSegmentConfidence
- **Type**: typing.Optional[float]

### BlackFrame
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.BlackFrameTypeDef]


# StartTextDetectionFiltersTypeDef

### WordFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.DetectionFilterTypeDef]

### RegionsOfInterest
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestTypeDef]]


# StartTextDetectionRequestRequestTypeDef

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.VideoTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.NotificationChannelTypeDef]

### JobTag
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StartTextDetectionFiltersTypeDef]


# StartTextDetectionResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopProjectVersionRequestRequestTypeDef

### ProjectVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopProjectVersionResponseTypeDef

### Status
- **Type**: typing.Literal['COPYING_COMPLETED', 'COPYING_FAILED', 'COPYING_IN_PROGRESS', 'DELETING', 'DEPRECATED', 'EXPIRED', 'FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'TRAINING_COMPLETED', 'TRAINING_FAILED', 'TRAINING_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopStreamProcessorRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StreamProcessingStartSelectorTypeDef

### KVSStreamStartSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.KinesisVideoStreamStartSelectorTypeDef]


# StreamProcessingStopSelectorTypeDef

### MaxDurationInSeconds
- **Type**: typing.Optional[int]


# StreamProcessorDataSharingPreferenceTypeDef

### OptIn
- **Type**: <class 'bool'>
- **Required**: Yes


# StreamProcessorInputTypeDef

### KinesisVideoStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.KinesisVideoStreamTypeDef]


# StreamProcessorNotificationChannelTypeDef

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# StreamProcessorOutputTypeDef

### KinesisDataStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.KinesisDataStreamTypeDef]

### S3Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.S3DestinationTypeDef]


# StreamProcessorSettingsForUpdateTypeDef

### ConnectedHomeForUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ConnectedHomeSettingsForUpdateTypeDef]


# StreamProcessorSettingsOutputTypeDef

### FaceSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceSearchSettingsTypeDef]

### ConnectedHome
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ConnectedHomeSettingsOutputTypeDef]


# StreamProcessorSettingsTypeDef

### FaceSearch
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceSearchSettingsTypeDef]

### ConnectedHome
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ConnectedHomeSettingsTypeDef]


# StreamProcessorTypeDef

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING']]


# SummaryTypeDef

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.S3ObjectTypeDef]


# SunglassesTypeDef

### Value
- **Type**: typing.Optional[bool]

### Confidence
- **Type**: typing.Optional[float]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TechnicalCueSegmentTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['BlackFrames', 'ColorBars', 'Content', 'EndCredits', 'OpeningCredits', 'Slate', 'StudioLogo']]

### Confidence
- **Type**: typing.Optional[float]


# TestingDataExtraOutputTypeDef

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AssetTypeDef]]

### AutoCreate
- **Type**: typing.Optional[bool]


# TestingDataOutputTypeDef

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AssetTypeDef]]

### AutoCreate
- **Type**: typing.Optional[bool]


# TestingDataResultTypeDef

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TestingDataOutputTypeDef]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TestingDataOutputTypeDef]

### Validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ValidationDataTypeDef]


# TestingDataTypeDef

### Assets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.AssetTypeDef]]

### AutoCreate
- **Type**: typing.Optional[bool]


# TextDetectionResultTypeDef

### Timestamp
- **Type**: typing.Optional[int]

### TextDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TextDetectionTypeDef]


# TextDetectionTypeDef

### DetectedText
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['LINE', 'WORD']]

### Id
- **Type**: typing.Optional[int]

### ParentId
- **Type**: typing.Optional[int]

### Confidence
- **Type**: typing.Optional[float]

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.GeometryTypeDef]


# TrainingDataExtraOutputTypeDef

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AssetTypeDef]]


# TrainingDataOutputTypeDef

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AssetTypeDef]]


# TrainingDataResultTypeDef

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TrainingDataOutputTypeDef]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.TrainingDataOutputTypeDef]

### Validation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.ValidationDataTypeDef]


# TrainingDataTypeDef

### Assets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.rekognition_classes.AssetTypeDef]]


# UnindexedFaceTypeDef

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['EXCEEDS_MAX_FACES', 'EXTREME_POSE', 'LOW_BRIGHTNESS', 'LOW_CONFIDENCE', 'LOW_FACE_QUALITY', 'LOW_SHARPNESS', 'SMALL_BOUNDING_BOX']]]

### FaceDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetailTypeDef]


# UnsearchedFaceTypeDef

### FaceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.FaceDetailTypeDef]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['EXCEEDS_MAX_FACES', 'EXTREME_POSE', 'FACE_NOT_LARGEST', 'LOW_BRIGHTNESS', 'LOW_CONFIDENCE', 'LOW_FACE_QUALITY', 'LOW_SHARPNESS', 'SMALL_BOUNDING_BOX']]]


# UnsuccessfulFaceAssociationTypeDef

### FaceId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['ASSOCIATED_TO_A_DIFFERENT_USER', 'FACE_NOT_FOUND', 'LOW_MATCH_CONFIDENCE']]]


# UnsuccessfulFaceDeletionTypeDef

### FaceId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['ASSOCIATED_TO_AN_EXISTING_USER', 'FACE_NOT_FOUND']]]


# UnsuccessfulFaceDisassociationTypeDef

### FaceId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Reasons
- **Type**: typing.Optional[typing.List[typing.Literal['ASSOCIATED_TO_A_DIFFERENT_USER', 'FACE_NOT_FOUND']]]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatasetEntriesRequestRequestTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Changes
- **Type**: <class 'aws_resource_validator.pydantic_models.rekognition_classes.DatasetChangesTypeDef'>
- **Required**: Yes


# UpdateStreamProcessorRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SettingsForUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorSettingsForUpdateTypeDef]

### RegionsOfInterestForUpdate
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestTypeDef, aws_resource_validator.pydantic_models.rekognition_classes.RegionOfInterestOutputTypeDef]]]

### DataSharingPreferenceForUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.StreamProcessorDataSharingPreferenceTypeDef]

### ParametersToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ConnectedHomeMinConfidence', 'RegionsOfInterest']]]


# UserMatchTypeDef

### Similarity
- **Type**: typing.Optional[float]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.MatchedUserTypeDef]


# UserTypeDef

### UserId
- **Type**: typing.Optional[str]

### UserStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATED', 'CREATING', 'UPDATING']]


# ValidationDataTypeDef

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.rekognition_classes.AssetTypeDef]]


# VideoMetadataTypeDef

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


# VideoTypeDef

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.rekognition_classes.S3ObjectTypeDef]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]



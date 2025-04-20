# Comprehend Comprehend Classes

# AugmentedManifestsListItem

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.List[str]
- **Required**: Yes

### Split
- **Type**: typing.Optional[typing.Literal['TEST', 'TRAIN']]

### AnnotationDataS3Uri
- **Type**: typing.Optional[str]

### SourceDocumentsS3Uri
- **Type**: typing.Optional[str]

### DocumentType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT_DOCUMENT', 'SEMI_STRUCTURED_DOCUMENT']]


# AugmentedManifestsListItemOutput

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.List[str]
- **Required**: Yes

### Split
- **Type**: typing.Optional[typing.Literal['TEST', 'TRAIN']]

### AnnotationDataS3Uri
- **Type**: typing.Optional[str]

### SourceDocumentsS3Uri
- **Type**: typing.Optional[str]

### DocumentType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT_DOCUMENT', 'SEMI_STRUCTURED_DOCUMENT']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchDetectDominantLanguageItemResult

### Index
- **Type**: typing.Optional[int]

### Languages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DominantLanguage]]


# BatchDetectDominantLanguageRequest

### TextList
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDetectDominantLanguageResponse

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchDetectDominantLanguageItemResult]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchItemError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDetectEntitiesItemResult

### Index
- **Type**: typing.Optional[int]

### Entities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Entity]]


# BatchDetectEntitiesRequest

### TextList
- **Type**: typing.List[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# BatchDetectEntitiesResponse

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchDetectEntitiesItemResult]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchItemError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDetectKeyPhrasesItemResult

### Index
- **Type**: typing.Optional[int]

### KeyPhrases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.KeyPhrase]]


# BatchDetectKeyPhrasesRequest

### TextList
- **Type**: typing.List[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# BatchDetectKeyPhrasesResponse

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchDetectKeyPhrasesItemResult]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchItemError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDetectSentimentItemResult

### Index
- **Type**: typing.Optional[int]

### Sentiment
- **Type**: typing.Optional[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]

### SentimentScore
- **Type**: <class 'NoneType'>


# BatchDetectSentimentRequest

### TextList
- **Type**: typing.List[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# BatchDetectSentimentResponse

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchDetectSentimentItemResult]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchItemError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDetectSyntaxItemResult

### Index
- **Type**: typing.Optional[int]

### SyntaxTokens
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.SyntaxToken]]


# BatchDetectSyntaxRequest

### TextList
- **Type**: typing.List[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['de', 'en', 'es', 'fr', 'it', 'pt']
- **Required**: Yes


# BatchDetectSyntaxResponse

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchDetectSyntaxItemResult]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchItemError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDetectTargetedSentimentItemResult

### Index
- **Type**: typing.Optional[int]

### Entities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TargetedSentimentEntity]]


# BatchDetectTargetedSentimentRequest

### TextList
- **Type**: typing.List[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# BatchDetectTargetedSentimentResponse

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchDetectTargetedSentimentItemResult]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BatchItemError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# BatchItemError

### Index
- **Type**: typing.Optional[int]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# Block

### Id
- **Type**: typing.Optional[str]

### BlockType
- **Type**: typing.Optional[typing.Literal['LINE', 'WORD']]

### Text
- **Type**: typing.Optional[str]

### Page
- **Type**: typing.Optional[int]

### Geometry
- **Type**: <class 'NoneType'>

### Relationships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.RelationshipsListItem]]


# BlockReference

### BlockId
- **Type**: typing.Optional[str]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### ChildBlocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ChildBlock]]


# BoundingBox

### Height
- **Type**: typing.Optional[float]

### Left
- **Type**: typing.Optional[float]

### Top
- **Type**: typing.Optional[float]

### Width
- **Type**: typing.Optional[float]


# ChildBlock

### ChildBlockId
- **Type**: typing.Optional[str]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]


# ClassifierEvaluationMetrics

### Accuracy
- **Type**: typing.Optional[float]

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### F1Score
- **Type**: typing.Optional[float]

### MicroPrecision
- **Type**: typing.Optional[float]

### MicroRecall
- **Type**: typing.Optional[float]

### MicroF1Score
- **Type**: typing.Optional[float]

### HammingLoss
- **Type**: typing.Optional[float]


# ClassifierMetadata

### NumberOfLabels
- **Type**: typing.Optional[int]

### NumberOfTrainedDocuments
- **Type**: typing.Optional[int]

### NumberOfTestDocuments
- **Type**: typing.Optional[int]

### EvaluationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ClassifierEvaluationMetrics]


# ClassifyDocumentRequest

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### Text
- **Type**: typing.Optional[str]

### Bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### DocumentReaderConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentReaderConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentReaderConfigOutput, NoneType]


# ClassifyDocumentResponse

### Classes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClass]
- **Required**: Yes

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentLabel]
- **Required**: Yes

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentMetadata'>
- **Required**: Yes

### DocumentType
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentTypeListItem]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ErrorsListItem]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.WarningsListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# ContainsPiiEntitiesRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# ContainsPiiEntitiesResponse

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityLabel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatasetRequest

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetInputDataConfig'>
- **Required**: Yes

### DatasetType
- **Type**: typing.Optional[typing.Literal['TEST', 'TRAIN']]

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# CreateDatasetResponse

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDocumentClassifierRequest

### DocumentClassifierName
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierInputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierInputDataConfigOutput]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### VersionName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierOutputDataConfig]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### Mode
- **Type**: typing.Optional[typing.Literal['MULTI_CLASS', 'MULTI_LABEL']]

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### ModelPolicy
- **Type**: typing.Optional[str]


# CreateDocumentClassifierResponse

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEndpointRequest

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredInferenceUnits
- **Type**: <class 'int'>
- **Required**: Yes

### ModelArn
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### FlywheelArn
- **Type**: typing.Optional[str]


# CreateEndpointResponse

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEntityRecognizerRequest

### RecognizerName
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerInputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerInputDataConfigOutput]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### VersionName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### ModelPolicy
- **Type**: typing.Optional[str]


# CreateEntityRecognizerResponse

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFlywheelRequest

### FlywheelName
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### DataLakeS3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveModelArn
- **Type**: typing.Optional[str]

### TaskConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TaskConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TaskConfigOutput, NoneType]

### ModelType
- **Type**: typing.Optional[typing.Literal['DOCUMENT_CLASSIFIER', 'ENTITY_RECOGNIZER']]

### DataSecurityConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DataSecurityConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DataSecurityConfigOutput, NoneType]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# CreateFlywheelResponse

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DataSecurityConfig

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### DataLakeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: <class 'NoneType'>


# DataSecurityConfigOutput

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### DataLakeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]


# DatasetAugmentedManifestsListItem

### AttributeNames
- **Type**: typing.List[str]
- **Required**: Yes

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### AnnotationDataS3Uri
- **Type**: typing.Optional[str]

### SourceDocumentsS3Uri
- **Type**: typing.Optional[str]

### DocumentType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT_DOCUMENT', 'SEMI_STRUCTURED_DOCUMENT']]


# DatasetDocumentClassifierInputDataConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### LabelDelimiter
- **Type**: typing.Optional[str]


# DatasetEntityRecognizerAnnotations

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# DatasetEntityRecognizerDocuments

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### InputFormat
- **Type**: typing.Optional[typing.Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE']]


# DatasetEntityRecognizerEntityList

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# DatasetEntityRecognizerInputDataConfig

### Documents
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetEntityRecognizerDocuments'>
- **Required**: Yes

### Annotations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetEntityRecognizerAnnotations]

### EntityList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetEntityRecognizerEntityList]


# DatasetFilter

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'FAILED']]

### DatasetType
- **Type**: typing.Optional[typing.Literal['TEST', 'TRAIN']]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DatasetInputDataConfig

### AugmentedManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetAugmentedManifestsListItem]]

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### DocumentClassifierInputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetDocumentClassifierInputDataConfig]

### EntityRecognizerInputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetEntityRecognizerInputDataConfig]


# DatasetProperties

### DatasetArn
- **Type**: typing.Optional[str]

### DatasetName
- **Type**: typing.Optional[str]

### DatasetType
- **Type**: typing.Optional[typing.Literal['TEST', 'TRAIN']]

### DatasetS3Uri
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'FAILED']]

### Message
- **Type**: typing.Optional[str]

### NumberOfDocuments
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# DeleteDocumentClassifierRequest

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointRequest

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEntityRecognizerRequest

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlywheelRequest

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DescribeDatasetRequest

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponse

### DatasetProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDocumentClassificationJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDocumentClassificationJobResponse

### DocumentClassificationJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassificationJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDocumentClassifierRequest

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDocumentClassifierResponse

### DocumentClassifierProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDominantLanguageDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDominantLanguageDetectionJobResponse

### DominantLanguageDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DominantLanguageDetectionJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointRequest

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointResponse

### EndpointProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EndpointProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEntitiesDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntitiesDetectionJobResponse

### EntitiesDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntitiesDetectionJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEntityRecognizerRequest

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntityRecognizerResponse

### EntityRecognizerProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventsDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEventsDetectionJobResponse

### EventsDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EventsDetectionJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFlywheelIterationRequest

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlywheelIterationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlywheelIterationResponse

### FlywheelIterationProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelIterationProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFlywheelRequest

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlywheelResponse

### FlywheelProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeKeyPhrasesDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeKeyPhrasesDetectionJobResponse

### KeyPhrasesDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.KeyPhrasesDetectionJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePiiEntitiesDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePiiEntitiesDetectionJobResponse

### PiiEntitiesDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PiiEntitiesDetectionJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourcePolicyResponse

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSentimentDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSentimentDetectionJobResponse

### SentimentDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.SentimentDetectionJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTargetedSentimentDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTargetedSentimentDetectionJobResponse

### TargetedSentimentDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TargetedSentimentDetectionJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTopicsDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicsDetectionJobResponse

### TopicsDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TopicsDetectionJobProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DetectDominantLanguageRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes


# DetectDominantLanguageResponse

### Languages
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DominantLanguage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DetectEntitiesRequest

### Text
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### EndpointArn
- **Type**: typing.Optional[str]

### Bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### DocumentReaderConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentReaderConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentReaderConfigOutput, NoneType]


# DetectEntitiesResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Entity]
- **Required**: Yes

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentMetadata'>
- **Required**: Yes

### DocumentType
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentTypeListItem]
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Block]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ErrorsListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DetectKeyPhrasesRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# DetectKeyPhrasesResponse

### KeyPhrases
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.KeyPhrase]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DetectPiiEntitiesRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# DetectPiiEntitiesResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PiiEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DetectSentimentRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# DetectSentimentResponse

### Sentiment
- **Type**: typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']
- **Required**: Yes

### SentimentScore
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.SentimentScore'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DetectSyntaxRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['de', 'en', 'es', 'fr', 'it', 'pt']
- **Required**: Yes


# DetectSyntaxResponse

### SyntaxTokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.SyntaxToken]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DetectTargetedSentimentRequest

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# DetectTargetedSentimentResponse

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TargetedSentimentEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DetectToxicContentRequest

### TextSegments
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TextSegment]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# DetectToxicContentResponse

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ToxicLabels]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# DocumentClass

### Name
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]

### Page
- **Type**: typing.Optional[int]


# DocumentClassificationConfig

### Mode
- **Type**: typing.Literal['MULTI_CLASS', 'MULTI_LABEL']
- **Required**: Yes

### Labels
- **Type**: typing.Optional[typing.List[str]]


# DocumentClassificationConfigOutput

### Mode
- **Type**: typing.Literal['MULTI_CLASS', 'MULTI_LABEL']
- **Required**: Yes

### Labels
- **Type**: typing.Optional[typing.List[str]]


# DocumentClassificationJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DocumentClassificationJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### DocumentClassifierArn
- **Type**: typing.Optional[str]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]

### FlywheelArn
- **Type**: typing.Optional[str]


# DocumentClassifierDocuments

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### TestS3Uri
- **Type**: typing.Optional[str]


# DocumentClassifierFilter

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'IN_ERROR', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED', 'TRAINED', 'TRAINED_WITH_WARNING', 'TRAINING']]

### DocumentClassifierName
- **Type**: typing.Optional[str]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DocumentClassifierInputDataConfig

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### S3Uri
- **Type**: typing.Optional[str]

### TestS3Uri
- **Type**: typing.Optional[str]

### LabelDelimiter
- **Type**: typing.Optional[str]

### AugmentedManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.AugmentedManifestsListItem]]

### DocumentType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT_DOCUMENT', 'SEMI_STRUCTURED_DOCUMENT']]

### Documents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierDocuments]

### DocumentReaderConfig
- **Type**: <class 'NoneType'>


# DocumentClassifierInputDataConfigOutput

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### S3Uri
- **Type**: typing.Optional[str]

### TestS3Uri
- **Type**: typing.Optional[str]

### LabelDelimiter
- **Type**: typing.Optional[str]

### AugmentedManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.AugmentedManifestsListItemOutput]]

### DocumentType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT_DOCUMENT', 'SEMI_STRUCTURED_DOCUMENT']]

### Documents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierDocuments]

### DocumentReaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentReaderConfigOutput]


# DocumentClassifierOutputDataConfig

### S3Uri
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### FlywheelStatsS3Prefix
- **Type**: typing.Optional[str]


# DocumentClassifierProperties

### DocumentClassifierArn
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'IN_ERROR', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED', 'TRAINED', 'TRAINED_WITH_WARNING', 'TRAINING']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingStartTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingEndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierInputDataConfigOutput]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierOutputDataConfig]

### ClassifierMetadata
- **Type**: <class 'NoneType'>

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]

### Mode
- **Type**: typing.Optional[typing.Literal['MULTI_CLASS', 'MULTI_LABEL']]

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### SourceModelArn
- **Type**: typing.Optional[str]

### FlywheelArn
- **Type**: typing.Optional[str]


# DocumentClassifierSummary

### DocumentClassifierName
- **Type**: typing.Optional[str]

### NumberOfVersions
- **Type**: typing.Optional[int]

### LatestVersionCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LatestVersionName
- **Type**: typing.Optional[str]

### LatestVersionStatus
- **Type**: typing.Optional[typing.Literal['DELETING', 'IN_ERROR', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED', 'TRAINED', 'TRAINED_WITH_WARNING', 'TRAINING']]


# DocumentLabel

### Name
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]

### Page
- **Type**: typing.Optional[int]


# DocumentMetadata

### Pages
- **Type**: typing.Optional[int]

### ExtractedCharacters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ExtractedCharactersListItem]]


# DocumentReaderConfig

### DocumentReadAction
- **Type**: typing.Literal['TEXTRACT_ANALYZE_DOCUMENT', 'TEXTRACT_DETECT_DOCUMENT_TEXT']
- **Required**: Yes

### DocumentReadMode
- **Type**: typing.Optional[typing.Literal['FORCE_DOCUMENT_READ_ACTION', 'SERVICE_DEFAULT']]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'TABLES']]]


# DocumentReaderConfigOutput

### DocumentReadAction
- **Type**: typing.Literal['TEXTRACT_ANALYZE_DOCUMENT', 'TEXTRACT_DETECT_DOCUMENT_TEXT']
- **Required**: Yes

### DocumentReadMode
- **Type**: typing.Optional[typing.Literal['FORCE_DOCUMENT_READ_ACTION', 'SERVICE_DEFAULT']]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'TABLES']]]


# DocumentTypeListItem

### Page
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[typing.Literal['IMAGE', 'MS_WORD', 'NATIVE_PDF', 'PLAIN_TEXT', 'SCANNED_PDF', 'TEXTRACT_ANALYZE_DOCUMENT_JSON', 'TEXTRACT_DETECT_DOCUMENT_TEXT_JSON']]


# DominantLanguage

### LanguageCode
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# DominantLanguageDetectionJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DominantLanguageDetectionJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]


# EndpointFilter

### ModelArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED', 'IN_SERVICE', 'UPDATING']]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# EndpointProperties

### EndpointArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED', 'IN_SERVICE', 'UPDATING']]

### Message
- **Type**: typing.Optional[str]

### ModelArn
- **Type**: typing.Optional[str]

### DesiredModelArn
- **Type**: typing.Optional[str]

### DesiredInferenceUnits
- **Type**: typing.Optional[int]

### CurrentInferenceUnits
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### DesiredDataAccessRoleArn
- **Type**: typing.Optional[str]

### FlywheelArn
- **Type**: typing.Optional[str]


# EntitiesDetectionJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# EntitiesDetectionJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### EntityRecognizerArn
- **Type**: typing.Optional[str]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]

### FlywheelArn
- **Type**: typing.Optional[str]


# Entity

### Score
- **Type**: typing.Optional[float]

### Type
- **Type**: typing.Optional[typing.Literal['COMMERCIAL_ITEM', 'DATE', 'EVENT', 'LOCATION', 'ORGANIZATION', 'OTHER', 'PERSON', 'QUANTITY', 'TITLE']]

### Text
- **Type**: typing.Optional[str]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### BlockReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.BlockReference]]


# EntityLabel

### Name
- **Type**: typing.Optional[typing.Literal['ADDRESS', 'AGE', 'ALL', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'DATE_TIME', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IN_AADHAAR', 'IN_NREGA', 'IN_PERMANENT_ACCOUNT_NUMBER', 'IN_VOTER_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSPORT_NUMBER', 'PASSWORD', 'PHONE', 'PIN', 'SSN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]

### Score
- **Type**: typing.Optional[float]


# EntityRecognitionConfig

### EntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityTypesListItem]
- **Required**: Yes


# EntityRecognitionConfigOutput

### EntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityTypesListItem]
- **Required**: Yes


# EntityRecognizerAnnotations

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### TestS3Uri
- **Type**: typing.Optional[str]


# EntityRecognizerDocuments

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### TestS3Uri
- **Type**: typing.Optional[str]

### InputFormat
- **Type**: typing.Optional[typing.Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE']]


# EntityRecognizerEntityList

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# EntityRecognizerEvaluationMetrics

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### F1Score
- **Type**: typing.Optional[float]


# EntityRecognizerFilter

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'IN_ERROR', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED', 'TRAINED', 'TRAINED_WITH_WARNING', 'TRAINING']]

### RecognizerName
- **Type**: typing.Optional[str]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# EntityRecognizerInputDataConfig

### EntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityTypesListItem]
- **Required**: Yes

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### Documents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerDocuments]

### Annotations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerAnnotations]

### EntityList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerEntityList]

### AugmentedManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.AugmentedManifestsListItem]]


# EntityRecognizerInputDataConfigOutput

### EntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityTypesListItem]
- **Required**: Yes

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### Documents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerDocuments]

### Annotations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerAnnotations]

### EntityList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerEntityList]

### AugmentedManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.AugmentedManifestsListItemOutput]]


# EntityRecognizerMetadata

### NumberOfTrainedDocuments
- **Type**: typing.Optional[int]

### NumberOfTestDocuments
- **Type**: typing.Optional[int]

### EvaluationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerEvaluationMetrics]

### EntityTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerMetadataEntityTypesListItem]]


# EntityRecognizerMetadataEntityTypesListItem

### Type
- **Type**: typing.Optional[str]

### EvaluationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityTypesEvaluationMetrics]

### NumberOfTrainMentions
- **Type**: typing.Optional[int]


# EntityRecognizerOutputDataConfig

### FlywheelStatsS3Prefix
- **Type**: typing.Optional[str]


# EntityRecognizerProperties

### EntityRecognizerArn
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'IN_ERROR', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED', 'TRAINED', 'TRAINED_WITH_WARNING', 'TRAINING']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingStartTime
- **Type**: typing.Optional[datetime.datetime]

### TrainingEndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerInputDataConfigOutput]

### RecognizerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerMetadata]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### SourceModelArn
- **Type**: typing.Optional[str]

### FlywheelArn
- **Type**: typing.Optional[str]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerOutputDataConfig]


# EntityRecognizerSummary

### RecognizerName
- **Type**: typing.Optional[str]

### NumberOfVersions
- **Type**: typing.Optional[int]

### LatestVersionCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### LatestVersionName
- **Type**: typing.Optional[str]

### LatestVersionStatus
- **Type**: typing.Optional[typing.Literal['DELETING', 'IN_ERROR', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED', 'TRAINED', 'TRAINED_WITH_WARNING', 'TRAINING']]


# EntityTypesEvaluationMetrics

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### F1Score
- **Type**: typing.Optional[float]


# EntityTypesListItem

### Type
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorsListItem

### Page
- **Type**: typing.Optional[int]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['INTERNAL_SERVER_ERROR', 'PAGE_CHARACTERS_EXCEEDED', 'PAGE_SIZE_EXCEEDED', 'TEXTRACT_BAD_PAGE', 'TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED']]

### ErrorMessage
- **Type**: typing.Optional[str]


# EventsDetectionJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# EventsDetectionJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### TargetEventTypes
- **Type**: typing.Optional[typing.List[str]]


# ExtractedCharactersListItem

### Page
- **Type**: typing.Optional[int]

### Count
- **Type**: typing.Optional[int]


# FlywheelFilter

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# FlywheelIterationFilter

### CreationTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### CreationTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# FlywheelIterationProperties

### FlywheelArn
- **Type**: typing.Optional[str]

### FlywheelIterationId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'EVALUATING', 'FAILED', 'STOPPED', 'STOP_REQUESTED', 'TRAINING']]

### Message
- **Type**: typing.Optional[str]

### EvaluatedModelArn
- **Type**: typing.Optional[str]

### EvaluatedModelMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelModelEvaluationMetrics]

### TrainedModelArn
- **Type**: typing.Optional[str]

### TrainedModelMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelModelEvaluationMetrics]

### EvaluationManifestS3Prefix
- **Type**: typing.Optional[str]


# FlywheelModelEvaluationMetrics

### AverageF1Score
- **Type**: typing.Optional[float]

### AveragePrecision
- **Type**: typing.Optional[float]

### AverageRecall
- **Type**: typing.Optional[float]

### AverageAccuracy
- **Type**: typing.Optional[float]


# FlywheelProperties

### FlywheelArn
- **Type**: typing.Optional[str]

### ActiveModelArn
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### TaskConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TaskConfigOutput]

### DataLakeS3Uri
- **Type**: typing.Optional[str]

### DataSecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DataSecurityConfigOutput]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### ModelType
- **Type**: typing.Optional[typing.Literal['DOCUMENT_CLASSIFIER', 'ENTITY_RECOGNIZER']]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LatestFlywheelIteration
- **Type**: typing.Optional[str]


# FlywheelSummary

### FlywheelArn
- **Type**: typing.Optional[str]

### ActiveModelArn
- **Type**: typing.Optional[str]

### DataLakeS3Uri
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### ModelType
- **Type**: typing.Optional[typing.Literal['DOCUMENT_CLASSIFIER', 'ENTITY_RECOGNIZER']]

### Message
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### LatestFlywheelIteration
- **Type**: typing.Optional[str]


# Geometry

### BoundingBox
- **Type**: <class 'NoneType'>

### Polygon
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Point]]


# ImportModelRequest

### SourceModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelName
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# ImportModelResponse

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# InputDataConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### InputFormat
- **Type**: typing.Optional[typing.Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE']]

### DocumentReaderConfig
- **Type**: <class 'NoneType'>


# InputDataConfigOutput

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### InputFormat
- **Type**: typing.Optional[typing.Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE']]

### DocumentReaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentReaderConfigOutput]


# KeyPhrase

### Score
- **Type**: typing.Optional[float]

### Text
- **Type**: typing.Optional[str]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]


# KeyPhrasesDetectionJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# KeyPhrasesDetectionJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]


# ListDatasetsRequest

### FlywheelArn
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponse

### DatasetPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DatasetProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentClassificationJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassificationJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDocumentClassificationJobsRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassificationJobFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListDocumentClassificationJobsResponse

### DocumentClassificationJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassificationJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentClassifierSummariesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDocumentClassifierSummariesResponse

### DocumentClassifierSummariesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentClassifiersRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDocumentClassifiersRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListDocumentClassifiersResponse

### DocumentClassifierPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassifierProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDominantLanguageDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DominantLanguageDetectionJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDominantLanguageDetectionJobsRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DominantLanguageDetectionJobFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListDominantLanguageDetectionJobsResponse

### DominantLanguageDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DominantLanguageDetectionJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EndpointFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEndpointsRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EndpointFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListEndpointsResponse

### EndpointPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EndpointProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitiesDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntitiesDetectionJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntitiesDetectionJobsRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntitiesDetectionJobFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListEntitiesDetectionJobsResponse

### EntitiesDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntitiesDetectionJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntityRecognizerSummariesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntityRecognizerSummariesResponse

### EntityRecognizerSummariesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntityRecognizersRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntityRecognizersRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListEntityRecognizersResponse

### EntityRecognizerPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognizerProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventsDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EventsDetectionJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventsDetectionJobsResponse

### EventsDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EventsDetectionJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlywheelIterationHistoryRequest

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelIterationFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFlywheelIterationHistoryResponse

### FlywheelIterationPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelIterationProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlywheelsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFlywheelsResponse

### FlywheelSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKeyPhrasesDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.KeyPhrasesDetectionJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListKeyPhrasesDetectionJobsRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.KeyPhrasesDetectionJobFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListKeyPhrasesDetectionJobsResponse

### KeyPhrasesDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.KeyPhrasesDetectionJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPiiEntitiesDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PiiEntitiesDetectionJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPiiEntitiesDetectionJobsRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PiiEntitiesDetectionJobFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListPiiEntitiesDetectionJobsResponse

### PiiEntitiesDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PiiEntitiesDetectionJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSentimentDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.SentimentDetectionJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSentimentDetectionJobsRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.SentimentDetectionJobFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListSentimentDetectionJobsResponse

### SentimentDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.SentimentDetectionJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# ListTargetedSentimentDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TargetedSentimentDetectionJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTargetedSentimentDetectionJobsResponse

### TargetedSentimentDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TargetedSentimentDetectionJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTopicsDetectionJobsRequest

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TopicsDetectionJobFilter]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTopicsDetectionJobsRequestPaginate

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TopicsDetectionJobFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PaginatorConfig]


# ListTopicsDetectionJobsResponse

### TopicsDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TopicsDetectionJobProperties]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MentionSentiment

### Sentiment
- **Type**: typing.Optional[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]

### SentimentScore
- **Type**: <class 'NoneType'>


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


# PartOfSpeechTag

### Tag
- **Type**: typing.Optional[typing.Literal['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'CONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'O', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB']]

### Score
- **Type**: typing.Optional[float]


# PiiEntitiesDetectionJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PiiEntitiesDetectionJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PiiOutputDataConfig]

### RedactionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.RedactionConfigOutput]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['ONLY_OFFSETS', 'ONLY_REDACTION']]


# PiiEntity

### Score
- **Type**: typing.Optional[float]

### Type
- **Type**: typing.Optional[typing.Literal['ADDRESS', 'AGE', 'ALL', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'DATE_TIME', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IN_AADHAAR', 'IN_NREGA', 'IN_PERMANENT_ACCOUNT_NUMBER', 'IN_VOTER_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSPORT_NUMBER', 'PASSWORD', 'PHONE', 'PIN', 'SSN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]


# PiiOutputDataConfig

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# Point

### X
- **Type**: typing.Optional[float]

### Y
- **Type**: typing.Optional[float]


# PutResourcePolicyRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# PutResourcePolicyResponse

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# RedactionConfig

### PiiEntityTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADDRESS', 'AGE', 'ALL', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'DATE_TIME', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IN_AADHAAR', 'IN_NREGA', 'IN_PERMANENT_ACCOUNT_NUMBER', 'IN_VOTER_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSPORT_NUMBER', 'PASSWORD', 'PHONE', 'PIN', 'SSN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]]

### MaskMode
- **Type**: typing.Optional[typing.Literal['MASK', 'REPLACE_WITH_PII_ENTITY_TYPE']]

### MaskCharacter
- **Type**: typing.Optional[str]


# RedactionConfigOutput

### PiiEntityTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADDRESS', 'AGE', 'ALL', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'DATE_TIME', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IN_AADHAAR', 'IN_NREGA', 'IN_PERMANENT_ACCOUNT_NUMBER', 'IN_VOTER_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSPORT_NUMBER', 'PASSWORD', 'PHONE', 'PIN', 'SSN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]]

### MaskMode
- **Type**: typing.Optional[typing.Literal['MASK', 'REPLACE_WITH_PII_ENTITY_TYPE']]

### MaskCharacter
- **Type**: typing.Optional[str]


# RelationshipsListItem

### Ids
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[typing.Literal['CHILD']]


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


# SentimentDetectionJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# SentimentDetectionJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]


# SentimentScore

### Positive
- **Type**: typing.Optional[float]

### Negative
- **Type**: typing.Optional[float]

### Neutral
- **Type**: typing.Optional[float]

### Mixed
- **Type**: typing.Optional[float]


# StartDocumentClassificationJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### DocumentClassifierArn
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]

### FlywheelArn
- **Type**: typing.Optional[str]


# StartDocumentClassificationJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartDominantLanguageDetectionJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# StartDominantLanguageDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartEntitiesDetectionJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### EntityRecognizerArn
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]

### FlywheelArn
- **Type**: typing.Optional[str]


# StartEntitiesDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartEventsDetectionJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### TargetEventTypes
- **Type**: typing.List[str]
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# StartEventsDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartFlywheelIterationRequest

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartFlywheelIterationResponse

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlywheelIterationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartKeyPhrasesDetectionJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# StartKeyPhrasesDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartPiiEntitiesDetectionJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### Mode
- **Type**: typing.Literal['ONLY_OFFSETS', 'ONLY_REDACTION']
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### RedactionConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.RedactionConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.RedactionConfigOutput, NoneType]

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# StartPiiEntitiesDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartSentimentDetectionJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# StartSentimentDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartTargetedSentimentDetectionJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# StartTargetedSentimentDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StartTopicsDetectionJobRequest

### InputDataConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.OutputDataConfig'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### NumberOfTopics
- **Type**: typing.Optional[int]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]]


# StartTopicsDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobArn
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StopDominantLanguageDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopDominantLanguageDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StopEntitiesDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopEntitiesDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StopEventsDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopEventsDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StopKeyPhrasesDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopKeyPhrasesDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StopPiiEntitiesDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopPiiEntitiesDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StopSentimentDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopSentimentDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StopTargetedSentimentDetectionJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopTargetedSentimentDetectionJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# StopTrainingDocumentClassifierRequest

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopTrainingEntityRecognizerRequest

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes


# SyntaxToken

### TokenId
- **Type**: typing.Optional[int]

### Text
- **Type**: typing.Optional[str]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### PartOfSpeech
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.PartOfSpeechTag]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.Tag]
- **Required**: Yes


# TargetedSentimentDetectionJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TargetedSentimentDetectionJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]


# TargetedSentimentEntity

### DescriptiveMentionIndex
- **Type**: typing.Optional[typing.List[int]]

### Mentions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.TargetedSentimentMention]]


# TargetedSentimentMention

### Score
- **Type**: typing.Optional[float]

### GroupScore
- **Type**: typing.Optional[float]

### Text
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE', 'BOOK', 'BRAND', 'COMMERCIAL_ITEM', 'DATE', 'EVENT', 'FACILITY', 'GAME', 'LOCATION', 'MOVIE', 'MUSIC', 'ORGANIZATION', 'OTHER', 'PERSON', 'PERSONAL_TITLE', 'QUANTITY', 'SOFTWARE']]

### MentionSentiment
- **Type**: <class 'NoneType'>

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]


# TaskConfig

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### DocumentClassificationConfig
- **Type**: <class 'NoneType'>

### EntityRecognitionConfig
- **Type**: <class 'NoneType'>


# TaskConfigOutput

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### DocumentClassificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.DocumentClassificationConfigOutput]

### EntityRecognitionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.EntityRecognitionConfigOutput]


# TextSegment

### Text
- **Type**: <class 'str'>
- **Required**: Yes


# TopicsDetectionJobFilter

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### SubmitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TopicsDetectionJobProperties

### JobId
- **Type**: typing.Optional[str]

### JobArn
- **Type**: typing.Optional[str]

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### Message
- **Type**: typing.Optional[str]

### SubmitTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### InputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.InputDataConfigOutput]

### OutputDataConfig
- **Type**: <class 'NoneType'>

### NumberOfTopics
- **Type**: typing.Optional[int]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput]


# ToxicContent

### Name
- **Type**: typing.Optional[typing.Literal['GRAPHIC', 'HARASSMENT_OR_ABUSE', 'HATE_SPEECH', 'INSULT', 'PROFANITY', 'SEXUAL', 'VIOLENCE_OR_THREAT']]

### Score
- **Type**: typing.Optional[float]


# ToxicLabels

### Labels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ToxicContent]]

### Toxicity
- **Type**: typing.Optional[float]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDataSecurityConfig

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfig, aws_resource_validator.pydantic_models.comprehend.comprehend_classes.VpcConfigOutput, NoneType]


# UpdateEndpointRequest

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredModelArn
- **Type**: typing.Optional[str]

### DesiredInferenceUnits
- **Type**: typing.Optional[int]

### DesiredDataAccessRoleArn
- **Type**: typing.Optional[str]

### FlywheelArn
- **Type**: typing.Optional[str]


# UpdateEndpointResponse

### DesiredModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFlywheelRequest

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveModelArn
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### DataSecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend.comprehend_classes.UpdateDataSecurityConfig]


# UpdateFlywheelResponse

### FlywheelProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.FlywheelProperties'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend.comprehend_classes.ResponseMetadata'>
- **Required**: Yes


# VpcConfig

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigOutput

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# WarningsListItem

### Page
- **Type**: typing.Optional[int]

### WarnCode
- **Type**: typing.Optional[typing.Literal['INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL', 'INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL']]

### WarnMessage
- **Type**: typing.Optional[str]



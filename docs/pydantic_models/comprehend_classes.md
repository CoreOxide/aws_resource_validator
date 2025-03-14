# Comprehend Classes

# AugmentedManifestsListItemOutputTypeDef

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


# AugmentedManifestsListItemTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeNames
- **Type**: typing.Sequence[str]
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

# BatchDetectDominantLanguageItemResultTypeDef

### Index
- **Type**: typing.Optional[int]

### Languages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DominantLanguageTypeDef]]


# BatchDetectDominantLanguageRequestTypeDef

### TextList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDetectDominantLanguageResponseTypeDef

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchDetectDominantLanguageItemResultTypeDef]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchItemErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDetectEntitiesItemResultTypeDef

### Index
- **Type**: typing.Optional[int]

### Entities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntityTypeDef]]


# BatchDetectEntitiesRequestTypeDef

### TextList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# BatchDetectEntitiesResponseTypeDef

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchDetectEntitiesItemResultTypeDef]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchItemErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDetectKeyPhrasesItemResultTypeDef

### Index
- **Type**: typing.Optional[int]

### KeyPhrases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.KeyPhraseTypeDef]]


# BatchDetectKeyPhrasesRequestTypeDef

### TextList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# BatchDetectKeyPhrasesResponseTypeDef

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchDetectKeyPhrasesItemResultTypeDef]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchItemErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDetectSentimentItemResultTypeDef

### Index
- **Type**: typing.Optional[int]

### Sentiment
- **Type**: typing.Optional[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]

### SentimentScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.SentimentScoreTypeDef]


# BatchDetectSentimentRequestTypeDef

### TextList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# BatchDetectSentimentResponseTypeDef

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchDetectSentimentItemResultTypeDef]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchItemErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDetectSyntaxItemResultTypeDef

### Index
- **Type**: typing.Optional[int]

### SyntaxTokens
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.SyntaxTokenTypeDef]]


# BatchDetectSyntaxRequestTypeDef

### TextList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['de', 'en', 'es', 'fr', 'it', 'pt']
- **Required**: Yes


# BatchDetectSyntaxResponseTypeDef

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchDetectSyntaxItemResultTypeDef]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchItemErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDetectTargetedSentimentItemResultTypeDef

### Index
- **Type**: typing.Optional[int]

### Entities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.TargetedSentimentEntityTypeDef]]


# BatchDetectTargetedSentimentRequestTypeDef

### TextList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# BatchDetectTargetedSentimentResponseTypeDef

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchDetectTargetedSentimentItemResultTypeDef]
- **Required**: Yes

### ErrorList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BatchItemErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchItemErrorTypeDef

### Index
- **Type**: typing.Optional[int]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# BlockReferenceTypeDef

### BlockId
- **Type**: typing.Optional[str]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### ChildBlocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.ChildBlockTypeDef]]


# BlockTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BoundingBoxTypeDef

### Height
- **Type**: typing.Optional[float]

### Left
- **Type**: typing.Optional[float]

### Top
- **Type**: typing.Optional[float]

### Width
- **Type**: typing.Optional[float]


# ChildBlockTypeDef

### ChildBlockId
- **Type**: typing.Optional[str]

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]


# ClassifierEvaluationMetricsTypeDef

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


# ClassifierMetadataTypeDef

### NumberOfLabels
- **Type**: typing.Optional[int]

### NumberOfTrainedDocuments
- **Type**: typing.Optional[int]

### NumberOfTestDocuments
- **Type**: typing.Optional[int]

### EvaluationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.ClassifierEvaluationMetricsTypeDef]


# ClassifyDocumentResponseTypeDef

### Classes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassTypeDef]
- **Required**: Yes

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DocumentLabelTypeDef]
- **Required**: Yes

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### DocumentType
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DocumentTypeListItemTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.ErrorsListItemTypeDef]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.WarningsListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ContainsPiiEntitiesResponseTypeDef

### Labels
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntityLabelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatasetRequestTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetName
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DatasetInputDataConfigTypeDef'>
- **Required**: Yes

### DatasetType
- **Type**: typing.Optional[typing.Literal['TEST', 'TRAIN']]

### Description
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# CreateDatasetResponseTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDocumentClassifierRequestTypeDef

### DocumentClassifierName
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierInputDataConfigUnionTypeDef'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### VersionName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierOutputDataConfigTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### Mode
- **Type**: typing.Optional[typing.Literal['MULTI_CLASS', 'MULTI_LABEL']]

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### ModelPolicy
- **Type**: typing.Optional[str]


# CreateDocumentClassifierResponseTypeDef

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEndpointRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### FlywheelArn
- **Type**: typing.Optional[str]


# CreateEndpointResponseTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEntityRecognizerRequestTypeDef

### RecognizerName
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerInputDataConfigUnionTypeDef'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### VersionName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### ModelPolicy
- **Type**: typing.Optional[str]


# CreateEntityRecognizerResponseTypeDef

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFlywheelRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TaskConfigUnionTypeDef]

### ModelType
- **Type**: typing.Optional[typing.Literal['DOCUMENT_CLASSIFIER', 'ENTITY_RECOGNIZER']]

### DataSecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DataSecurityConfigUnionTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# CreateFlywheelResponseTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSecurityConfigOutputTypeDef

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### DataLakeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]


# DataSecurityConfigTypeDef

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### DataLakeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigTypeDef]


# DataSecurityConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatasetAugmentedManifestsListItemTypeDef

### AttributeNames
- **Type**: typing.Sequence[str]
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


# DatasetDocumentClassifierInputDataConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### LabelDelimiter
- **Type**: typing.Optional[str]


# DatasetEntityRecognizerAnnotationsTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# DatasetEntityRecognizerDocumentsTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### InputFormat
- **Type**: typing.Optional[typing.Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE']]


# DatasetEntityRecognizerEntityListTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# DatasetEntityRecognizerInputDataConfigTypeDef

### Documents
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DatasetEntityRecognizerDocumentsTypeDef'>
- **Required**: Yes

### Annotations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DatasetEntityRecognizerAnnotationsTypeDef]

### EntityList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DatasetEntityRecognizerEntityListTypeDef]


# DatasetFilterTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'FAILED']]

### DatasetType
- **Type**: typing.Optional[typing.Literal['TEST', 'TRAIN']]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# DatasetInputDataConfigTypeDef

### AugmentedManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.DatasetAugmentedManifestsListItemTypeDef]]

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### DocumentClassifierInputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DatasetDocumentClassifierInputDataConfigTypeDef]

### EntityRecognizerInputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DatasetEntityRecognizerInputDataConfigTypeDef]


# DatasetPropertiesTypeDef

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


# DeleteDocumentClassifierRequestTypeDef

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEndpointRequestTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEntityRecognizerRequestTypeDef

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlywheelRequestTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DescribeDatasetRequestTypeDef

### DatasetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatasetResponseTypeDef

### DatasetProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DatasetPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDocumentClassificationJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDocumentClassificationJobResponseTypeDef

### DocumentClassificationJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassificationJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDocumentClassifierRequestTypeDef

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDocumentClassifierResponseTypeDef

### DocumentClassifierProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDominantLanguageDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDominantLanguageDetectionJobResponseTypeDef

### DominantLanguageDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DominantLanguageDetectionJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointRequestTypeDef

### EndpointArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEndpointResponseTypeDef

### EndpointProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.EndpointPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEntitiesDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntitiesDetectionJobResponseTypeDef

### EntitiesDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.EntitiesDetectionJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEntityRecognizerRequestTypeDef

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntityRecognizerResponseTypeDef

### EntityRecognizerProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventsDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEventsDetectionJobResponseTypeDef

### EventsDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.EventsDetectionJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFlywheelIterationRequestTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlywheelIterationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlywheelIterationResponseTypeDef

### FlywheelIterationProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.FlywheelIterationPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFlywheelRequestTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFlywheelResponseTypeDef

### FlywheelProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.FlywheelPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeKeyPhrasesDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeKeyPhrasesDetectionJobResponseTypeDef

### KeyPhrasesDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.KeyPhrasesDetectionJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePiiEntitiesDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePiiEntitiesDetectionJobResponseTypeDef

### PiiEntitiesDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.PiiEntitiesDetectionJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourcePolicyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSentimentDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSentimentDetectionJobResponseTypeDef

### SentimentDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.SentimentDetectionJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTargetedSentimentDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTargetedSentimentDetectionJobResponseTypeDef

### TargetedSentimentDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.TargetedSentimentDetectionJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTopicsDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTopicsDetectionJobResponseTypeDef

### TopicsDetectionJobProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.TopicsDetectionJobPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectDominantLanguageResponseTypeDef

### Languages
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DominantLanguageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectEntitiesResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntityTypeDef]
- **Required**: Yes

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### DocumentType
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DocumentTypeListItemTypeDef]
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.BlockTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.ErrorsListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectKeyPhrasesResponseTypeDef

### KeyPhrases
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.KeyPhraseTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectPiiEntitiesResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.PiiEntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectSentimentResponseTypeDef

### Sentiment
- **Type**: typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']
- **Required**: Yes

### SentimentScore
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.SentimentScoreTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectSyntaxResponseTypeDef

### SyntaxTokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.SyntaxTokenTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectTargetedSentimentResponseTypeDef

### Entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.TargetedSentimentEntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectToxicContentRequestTypeDef

### TextSegments
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TextSegmentTypeDef]
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes


# DetectToxicContentResponseTypeDef

### ResultList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.ToxicLabelsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentClassTypeDef

### Name
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]

### Page
- **Type**: typing.Optional[int]


# DocumentClassificationConfigOutputTypeDef

### Mode
- **Type**: typing.Literal['MULTI_CLASS', 'MULTI_LABEL']
- **Required**: Yes

### Labels
- **Type**: typing.Optional[typing.List[str]]


# DocumentClassificationConfigTypeDef

### Mode
- **Type**: typing.Literal['MULTI_CLASS', 'MULTI_LABEL']
- **Required**: Yes

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]


# DocumentClassificationJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# DocumentClassificationJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]

### FlywheelArn
- **Type**: typing.Optional[str]


# DocumentClassifierDocumentsTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### TestS3Uri
- **Type**: typing.Optional[str]


# DocumentClassifierFilterTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'IN_ERROR', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED', 'TRAINED', 'TRAINED_WITH_WARNING', 'TRAINING']]

### DocumentClassifierName
- **Type**: typing.Optional[str]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# DocumentClassifierInputDataConfigOutputTypeDef

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### S3Uri
- **Type**: typing.Optional[str]

### TestS3Uri
- **Type**: typing.Optional[str]

### LabelDelimiter
- **Type**: typing.Optional[str]

### AugmentedManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.AugmentedManifestsListItemOutputTypeDef]]

### DocumentType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT_DOCUMENT', 'SEMI_STRUCTURED_DOCUMENT']]

### Documents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierDocumentsTypeDef]

### DocumentReaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentReaderConfigOutputTypeDef]


# DocumentClassifierInputDataConfigTypeDef

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### S3Uri
- **Type**: typing.Optional[str]

### TestS3Uri
- **Type**: typing.Optional[str]

### LabelDelimiter
- **Type**: typing.Optional[str]

### AugmentedManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.AugmentedManifestsListItemTypeDef]]

### DocumentType
- **Type**: typing.Optional[typing.Literal['PLAIN_TEXT_DOCUMENT', 'SEMI_STRUCTURED_DOCUMENT']]

### Documents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierDocumentsTypeDef]

### DocumentReaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentReaderConfigTypeDef]


# DocumentClassifierInputDataConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentClassifierOutputDataConfigTypeDef

### S3Uri
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### FlywheelStatsS3Prefix
- **Type**: typing.Optional[str]


# DocumentClassifierPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierInputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierOutputDataConfigTypeDef]

### ClassifierMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.ClassifierMetadataTypeDef]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]

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


# DocumentClassifierSummaryTypeDef

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


# DocumentLabelTypeDef

### Name
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]

### Page
- **Type**: typing.Optional[int]


# DocumentMetadataTypeDef

### Pages
- **Type**: typing.Optional[int]

### ExtractedCharacters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.ExtractedCharactersListItemTypeDef]]


# DocumentReaderConfigOutputTypeDef

### DocumentReadAction
- **Type**: typing.Literal['TEXTRACT_ANALYZE_DOCUMENT', 'TEXTRACT_DETECT_DOCUMENT_TEXT']
- **Required**: Yes

### DocumentReadMode
- **Type**: typing.Optional[typing.Literal['FORCE_DOCUMENT_READ_ACTION', 'SERVICE_DEFAULT']]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'TABLES']]]


# DocumentReaderConfigTypeDef

### DocumentReadAction
- **Type**: typing.Literal['TEXTRACT_ANALYZE_DOCUMENT', 'TEXTRACT_DETECT_DOCUMENT_TEXT']
- **Required**: Yes

### DocumentReadMode
- **Type**: typing.Optional[typing.Literal['FORCE_DOCUMENT_READ_ACTION', 'SERVICE_DEFAULT']]

### FeatureTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FORMS', 'TABLES']]]


# DocumentTypeListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DominantLanguageDetectionJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# DominantLanguageDetectionJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]


# DominantLanguageTypeDef

### LanguageCode
- **Type**: typing.Optional[str]

### Score
- **Type**: typing.Optional[float]


# EndpointFilterTypeDef

### ModelArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CREATING', 'DELETING', 'FAILED', 'IN_SERVICE', 'UPDATING']]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# EndpointPropertiesTypeDef

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


# EntitiesDetectionJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# EntitiesDetectionJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]

### FlywheelArn
- **Type**: typing.Optional[str]


# EntityLabelTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['ADDRESS', 'AGE', 'ALL', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'DATE_TIME', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IN_AADHAAR', 'IN_NREGA', 'IN_PERMANENT_ACCOUNT_NUMBER', 'IN_VOTER_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSPORT_NUMBER', 'PASSWORD', 'PHONE', 'PIN', 'SSN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]

### Score
- **Type**: typing.Optional[float]


# EntityRecognitionConfigOutputTypeDef

### EntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntityTypesListItemTypeDef]
- **Required**: Yes


# EntityRecognitionConfigTypeDef

### EntityTypes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.EntityTypesListItemTypeDef]
- **Required**: Yes


# EntityRecognizerAnnotationsTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### TestS3Uri
- **Type**: typing.Optional[str]


# EntityRecognizerDocumentsTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### TestS3Uri
- **Type**: typing.Optional[str]

### InputFormat
- **Type**: typing.Optional[typing.Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE']]


# EntityRecognizerEntityListTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# EntityRecognizerEvaluationMetricsTypeDef

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### F1Score
- **Type**: typing.Optional[float]


# EntityRecognizerFilterTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DELETING', 'IN_ERROR', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED', 'TRAINED', 'TRAINED_WITH_WARNING', 'TRAINING']]

### RecognizerName
- **Type**: typing.Optional[str]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# EntityRecognizerInputDataConfigOutputTypeDef

### EntityTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntityTypesListItemTypeDef]
- **Required**: Yes

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### Documents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerDocumentsTypeDef]

### Annotations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerAnnotationsTypeDef]

### EntityList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerEntityListTypeDef]

### AugmentedManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.AugmentedManifestsListItemOutputTypeDef]]


# EntityRecognizerInputDataConfigTypeDef

### EntityTypes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.EntityTypesListItemTypeDef]
- **Required**: Yes

### DataFormat
- **Type**: typing.Optional[typing.Literal['AUGMENTED_MANIFEST', 'COMPREHEND_CSV']]

### Documents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerDocumentsTypeDef]

### Annotations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerAnnotationsTypeDef]

### EntityList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerEntityListTypeDef]

### AugmentedManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.AugmentedManifestsListItemTypeDef]]


# EntityRecognizerInputDataConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntityRecognizerMetadataEntityTypesListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntityRecognizerMetadataTypeDef

### NumberOfTrainedDocuments
- **Type**: typing.Optional[int]

### NumberOfTestDocuments
- **Type**: typing.Optional[int]

### EvaluationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerEvaluationMetricsTypeDef]

### EntityTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerMetadataEntityTypesListItemTypeDef]]


# EntityRecognizerOutputDataConfigTypeDef

### FlywheelStatsS3Prefix
- **Type**: typing.Optional[str]


# EntityRecognizerPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerInputDataConfigOutputTypeDef]

### RecognizerMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerMetadataTypeDef]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VersionName
- **Type**: typing.Optional[str]

### SourceModelArn
- **Type**: typing.Optional[str]

### FlywheelArn
- **Type**: typing.Optional[str]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerOutputDataConfigTypeDef]


# EntityRecognizerSummaryTypeDef

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


# EntityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EntityTypesEvaluationMetricsTypeDef

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]

### F1Score
- **Type**: typing.Optional[float]


# EntityTypesListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ErrorsListItemTypeDef

### Page
- **Type**: typing.Optional[int]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['INTERNAL_SERVER_ERROR', 'PAGE_CHARACTERS_EXCEEDED', 'PAGE_SIZE_EXCEEDED', 'TEXTRACT_BAD_PAGE', 'TEXTRACT_PROVISIONED_THROUGHPUT_EXCEEDED']]

### ErrorMessage
- **Type**: typing.Optional[str]


# EventsDetectionJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# EventsDetectionJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### TargetEventTypes
- **Type**: typing.Optional[typing.List[str]]


# ExtractedCharactersListItemTypeDef

### Page
- **Type**: typing.Optional[int]

### Count
- **Type**: typing.Optional[int]


# FlywheelFilterTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# FlywheelIterationFilterTypeDef

### CreationTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### CreationTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# FlywheelIterationPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.FlywheelModelEvaluationMetricsTypeDef]

### TrainedModelArn
- **Type**: typing.Optional[str]

### TrainedModelMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.FlywheelModelEvaluationMetricsTypeDef]

### EvaluationManifestS3Prefix
- **Type**: typing.Optional[str]


# FlywheelModelEvaluationMetricsTypeDef

### AverageF1Score
- **Type**: typing.Optional[float]

### AveragePrecision
- **Type**: typing.Optional[float]

### AverageRecall
- **Type**: typing.Optional[float]

### AverageAccuracy
- **Type**: typing.Optional[float]


# FlywheelPropertiesTypeDef

### FlywheelArn
- **Type**: typing.Optional[str]

### ActiveModelArn
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### TaskConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TaskConfigOutputTypeDef]

### DataLakeS3Uri
- **Type**: typing.Optional[str]

### DataSecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DataSecurityConfigOutputTypeDef]

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


# FlywheelSummaryTypeDef

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


# GeometryTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.BoundingBoxTypeDef]

### Polygon
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.PointTypeDef]]


# ImportModelRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# ImportModelResponseTypeDef

### ModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputDataConfigOutputTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### InputFormat
- **Type**: typing.Optional[typing.Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE']]

### DocumentReaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentReaderConfigOutputTypeDef]


# InputDataConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### InputFormat
- **Type**: typing.Optional[typing.Literal['ONE_DOC_PER_FILE', 'ONE_DOC_PER_LINE']]

### DocumentReaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentReaderConfigTypeDef]


# InputDataConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeyPhraseTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeyPhrasesDetectionJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# KeyPhrasesDetectionJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]


# ListDatasetsRequestTypeDef

### FlywheelArn
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DatasetFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatasetsResponseTypeDef

### DatasetPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DatasetPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentClassificationJobsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassificationJobFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListDocumentClassificationJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassificationJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDocumentClassificationJobsResponseTypeDef

### DocumentClassificationJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassificationJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentClassifierSummariesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDocumentClassifierSummariesResponseTypeDef

### DocumentClassifierSummariesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDocumentClassifiersRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListDocumentClassifiersRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDocumentClassifiersResponseTypeDef

### DocumentClassifierPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassifierPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDominantLanguageDetectionJobsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DominantLanguageDetectionJobFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListDominantLanguageDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DominantLanguageDetectionJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDominantLanguageDetectionJobsResponseTypeDef

### DominantLanguageDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.DominantLanguageDetectionJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEndpointsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EndpointFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListEndpointsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EndpointFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEndpointsResponseTypeDef

### EndpointPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EndpointPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntitiesDetectionJobsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntitiesDetectionJobFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListEntitiesDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntitiesDetectionJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntitiesDetectionJobsResponseTypeDef

### EntitiesDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntitiesDetectionJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntityRecognizerSummariesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntityRecognizerSummariesResponseTypeDef

### EntityRecognizerSummariesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntityRecognizersRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListEntityRecognizersRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntityRecognizersResponseTypeDef

### EntityRecognizerPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognizerPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventsDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EventsDetectionJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventsDetectionJobsResponseTypeDef

### EventsDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.EventsDetectionJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlywheelIterationHistoryRequestTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.FlywheelIterationFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFlywheelIterationHistoryResponseTypeDef

### FlywheelIterationPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.FlywheelIterationPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFlywheelsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.FlywheelFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFlywheelsResponseTypeDef

### FlywheelSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.FlywheelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListKeyPhrasesDetectionJobsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.KeyPhrasesDetectionJobFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListKeyPhrasesDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.KeyPhrasesDetectionJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListKeyPhrasesDetectionJobsResponseTypeDef

### KeyPhrasesDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.KeyPhrasesDetectionJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPiiEntitiesDetectionJobsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PiiEntitiesDetectionJobFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListPiiEntitiesDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PiiEntitiesDetectionJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPiiEntitiesDetectionJobsResponseTypeDef

### PiiEntitiesDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.PiiEntitiesDetectionJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSentimentDetectionJobsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.SentimentDetectionJobFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListSentimentDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.SentimentDetectionJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListSentimentDetectionJobsResponseTypeDef

### SentimentDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.SentimentDetectionJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetedSentimentDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TargetedSentimentDetectionJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTargetedSentimentDetectionJobsResponseTypeDef

### TargetedSentimentDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.TargetedSentimentDetectionJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTopicsDetectionJobsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TopicsDetectionJobFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PaginatorConfigTypeDef]


# ListTopicsDetectionJobsRequestTypeDef

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TopicsDetectionJobFilterTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTopicsDetectionJobsResponseTypeDef

### TopicsDetectionJobPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.comprehend_classes.TopicsDetectionJobPropertiesTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MentionSentimentTypeDef

### Sentiment
- **Type**: typing.Optional[typing.Literal['MIXED', 'NEGATIVE', 'NEUTRAL', 'POSITIVE']]

### SentimentScore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.SentimentScoreTypeDef]


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


# PartOfSpeechTagTypeDef

### Tag
- **Type**: typing.Optional[typing.Literal['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'CONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'O', 'PART', 'PRON', 'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB']]

### Score
- **Type**: typing.Optional[float]


# PiiEntitiesDetectionJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# PiiEntitiesDetectionJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.PiiOutputDataConfigTypeDef]

### RedactionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.RedactionConfigOutputTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['ONLY_OFFSETS', 'ONLY_REDACTION']]


# PiiEntityTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PiiOutputDataConfigTypeDef

### S3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]


# PointTypeDef

### X
- **Type**: typing.Optional[float]

### Y
- **Type**: typing.Optional[float]


# PutResourcePolicyRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourcePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# PutResourcePolicyResponseTypeDef

### PolicyRevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RedactionConfigOutputTypeDef

### PiiEntityTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ADDRESS', 'AGE', 'ALL', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'DATE_TIME', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IN_AADHAAR', 'IN_NREGA', 'IN_PERMANENT_ACCOUNT_NUMBER', 'IN_VOTER_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSPORT_NUMBER', 'PASSWORD', 'PHONE', 'PIN', 'SSN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]]

### MaskMode
- **Type**: typing.Optional[typing.Literal['MASK', 'REPLACE_WITH_PII_ENTITY_TYPE']]

### MaskCharacter
- **Type**: typing.Optional[str]


# RedactionConfigTypeDef

### PiiEntityTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADDRESS', 'AGE', 'ALL', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CVV', 'CREDIT_DEBIT_EXPIRY', 'CREDIT_DEBIT_NUMBER', 'DATE_TIME', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IN_AADHAAR', 'IN_NREGA', 'IN_PERMANENT_ACCOUNT_NUMBER', 'IN_VOTER_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSPORT_NUMBER', 'PASSWORD', 'PHONE', 'PIN', 'SSN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]]

### MaskMode
- **Type**: typing.Optional[typing.Literal['MASK', 'REPLACE_WITH_PII_ENTITY_TYPE']]

### MaskCharacter
- **Type**: typing.Optional[str]


# RedactionConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SentimentDetectionJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# SentimentDetectionJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]


# SentimentScoreTypeDef

### Positive
- **Type**: typing.Optional[float]

### Negative
- **Type**: typing.Optional[float]

### Neutral
- **Type**: typing.Optional[float]

### Mixed
- **Type**: typing.Optional[float]


# StartDocumentClassificationJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]

### FlywheelArn
- **Type**: typing.Optional[str]


# StartDocumentClassificationJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDominantLanguageDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# StartDominantLanguageDetectionJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartEntitiesDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]

### FlywheelArn
- **Type**: typing.Optional[str]


# StartEntitiesDetectionJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartEventsDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### TargetEventTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# StartEventsDetectionJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartFlywheelIterationRequestTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartFlywheelIterationResponseTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### FlywheelIterationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartKeyPhrasesDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# StartKeyPhrasesDetectionJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartPiiEntitiesDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.RedactionConfigUnionTypeDef]

### JobName
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# StartPiiEntitiesDetectionJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSentimentDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# StartSentimentDetectionJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTargetedSentimentDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# StartTargetedSentimentDetectionJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTopicsDetectionJobRequestTypeDef

### InputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigUnionTypeDef'>
- **Required**: Yes

### OutputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]]


# StartTopicsDetectionJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDominantLanguageDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopDominantLanguageDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopEntitiesDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopEntitiesDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopEventsDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopEventsDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopKeyPhrasesDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopKeyPhrasesDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopPiiEntitiesDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopPiiEntitiesDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopSentimentDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopSentimentDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopTargetedSentimentDetectionJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopTargetedSentimentDetectionJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopTrainingDocumentClassifierRequestTypeDef

### DocumentClassifierArn
- **Type**: <class 'str'>
- **Required**: Yes


# StopTrainingEntityRecognizerRequestTypeDef

### EntityRecognizerArn
- **Type**: <class 'str'>
- **Required**: Yes


# SyntaxTokenTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.comprehend_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TargetedSentimentDetectionJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# TargetedSentimentDetectionJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef]

### LanguageCode
- **Type**: typing.Optional[typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]


# TargetedSentimentEntityTypeDef

### DescriptiveMentionIndex
- **Type**: typing.Optional[typing.List[int]]

### Mentions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.TargetedSentimentMentionTypeDef]]


# TargetedSentimentMentionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TaskConfigOutputTypeDef

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### DocumentClassificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassificationConfigOutputTypeDef]

### EntityRecognitionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognitionConfigOutputTypeDef]


# TaskConfigTypeDef

### LanguageCode
- **Type**: typing.Literal['ar', 'de', 'en', 'es', 'fr', 'hi', 'it', 'ja', 'ko', 'pt', 'zh', 'zh-TW']
- **Required**: Yes

### DocumentClassificationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.DocumentClassificationConfigTypeDef]

### EntityRecognitionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.EntityRecognitionConfigTypeDef]


# TaskConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TextSegmentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TopicsDetectionJobFilterTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'STOPPED', 'STOP_REQUESTED', 'SUBMITTED']]

### SubmitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]

### SubmitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.TimestampTypeDef]


# TopicsDetectionJobPropertiesTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.InputDataConfigOutputTypeDef]

### OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.OutputDataConfigTypeDef]

### NumberOfTopics
- **Type**: typing.Optional[int]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigOutputTypeDef]


# ToxicContentTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['GRAPHIC', 'HARASSMENT_OR_ABUSE', 'HATE_SPEECH', 'INSULT', 'PROFANITY', 'SEXUAL', 'VIOLENCE_OR_THREAT']]

### Score
- **Type**: typing.Optional[float]


# ToxicLabelsTypeDef

### Labels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.comprehend_classes.ToxicContentTypeDef]]

### Toxicity
- **Type**: typing.Optional[float]


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDataSecurityConfigTypeDef

### ModelKmsKeyId
- **Type**: typing.Optional[str]

### VolumeKmsKeyId
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.VpcConfigUnionTypeDef]


# UpdateEndpointRequestTypeDef

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


# UpdateEndpointResponseTypeDef

### DesiredModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlywheelRequestTypeDef

### FlywheelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveModelArn
- **Type**: typing.Optional[str]

### DataAccessRoleArn
- **Type**: typing.Optional[str]

### DataSecurityConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.comprehend_classes.UpdateDataSecurityConfigTypeDef]


# UpdateFlywheelResponseTypeDef

### FlywheelProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.FlywheelPropertiesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.comprehend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcConfigOutputTypeDef

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigTypeDef

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VpcConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WarningsListItemTypeDef

### Page
- **Type**: typing.Optional[int]

### WarnCode
- **Type**: typing.Optional[typing.Literal['INFERENCING_NATIVE_DOCUMENT_WITH_PLAINTEXT_TRAINED_MODEL', 'INFERENCING_PLAINTEXT_WITH_NATIVE_TRAINED_MODEL']]

### WarnMessage
- **Type**: typing.Optional[str]



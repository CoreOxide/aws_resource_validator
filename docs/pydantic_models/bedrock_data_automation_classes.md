# Bedrock Data Automation Classes

# AudioExtractionCategory

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIO_CONTENT_MODERATION', 'TOPIC_CONTENT_MODERATION', 'TRANSCRIPT']]]


# AudioExtractionCategoryOutput

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIO_CONTENT_MODERATION', 'TOPIC_CONTENT_MODERATION', 'TRANSCRIPT']]]


# AudioStandardExtraction

### category
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.AudioExtractionCategory'>
- **Required**: Yes


# AudioStandardExtractionOutput

### category
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.AudioExtractionCategoryOutput'>
- **Required**: Yes


# AudioStandardGenerativeField

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIO_SUMMARY', 'IAB', 'TOPIC_SUMMARY']]]


# AudioStandardGenerativeFieldOutput

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIO_SUMMARY', 'IAB', 'TOPIC_SUMMARY']]]


# AudioStandardOutputConfiguration

### extraction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.AudioStandardExtraction]

### generativeField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.AudioStandardGenerativeField]


# AudioStandardOutputConfigurationOutput

### extraction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.AudioStandardExtractionOutput]

### generativeField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.AudioStandardGenerativeFieldOutput]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blueprint

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Blueprint'>>

### type
- **Type**: typing.Literal['DOCUMENT', 'IMAGE']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### blueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### blueprintVersion
- **Type**: typing.Optional[str]

### blueprintStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### kmsKeyId
- **Type**: typing.Optional[str]

### kmsEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]


# BlueprintFilter

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### blueprintVersion
- **Type**: typing.Optional[str]

### blueprintStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# BlueprintItem

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### blueprintVersion
- **Type**: typing.Optional[str]

### blueprintStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# BlueprintSummary

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### blueprintVersion
- **Type**: typing.Optional[str]

### blueprintStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### blueprintName
- **Type**: typing.Optional[str]

### lastModifiedTime
- **Type**: typing.Optional[datetime.datetime]


# CreateBlueprintRequest

### blueprintName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DOCUMENT', 'IMAGE']
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.CreateBlueprintRequest'>>

### blueprintStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### clientToken
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.EncryptionConfiguration]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Tag]]


# CreateBlueprintResponse

### blueprint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Blueprint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBlueprintVersionRequest

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateBlueprintVersionResponse

### blueprint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Blueprint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataAutomationProjectRequest

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### standardOutputConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.StandardOutputConfiguration, aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.StandardOutputConfigurationOutput]
- **Required**: Yes

### projectDescription
- **Type**: typing.Optional[str]

### projectStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### customOutputConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.CustomOutputConfiguration, aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.CustomOutputConfigurationOutput, NoneType]

### overrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.OverrideConfiguration]

### clientToken
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.EncryptionConfiguration]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Tag]]


# CreateDataAutomationProjectResponse

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectStage
- **Type**: typing.Literal['DEVELOPMENT', 'LIVE']
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# CustomOutputConfiguration

### blueprints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.BlueprintItem]]


# CustomOutputConfigurationOutput

### blueprints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.BlueprintItem]]


# DataAutomationProject

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### projectStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### projectDescription
- **Type**: typing.Optional[str]

### standardOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.StandardOutputConfigurationOutput]

### customOutputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.CustomOutputConfigurationOutput]

### overrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.OverrideConfiguration]

### kmsKeyId
- **Type**: typing.Optional[str]

### kmsEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]


# DataAutomationProjectFilter

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# DataAutomationProjectSummary

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### projectStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### projectName
- **Type**: typing.Optional[str]


# DeleteBlueprintRequest

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### blueprintVersion
- **Type**: typing.Optional[str]


# DeleteDataAutomationProjectRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataAutomationProjectResponse

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# DocumentBoundingBox

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# DocumentExtractionGranularity

### types
- **Type**: typing.Optional[typing.List[typing.Literal['DOCUMENT', 'ELEMENT', 'LINE', 'PAGE', 'WORD']]]


# DocumentExtractionGranularityOutput

### types
- **Type**: typing.Optional[typing.List[typing.Literal['DOCUMENT', 'ELEMENT', 'LINE', 'PAGE', 'WORD']]]


# DocumentOutputAdditionalFileFormat

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# DocumentOutputFormat

### textFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentOutputTextFormat'>
- **Required**: Yes

### additionalFileFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentOutputAdditionalFileFormat'>
- **Required**: Yes


# DocumentOutputFormatOutput

### textFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentOutputTextFormatOutput'>
- **Required**: Yes

### additionalFileFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentOutputAdditionalFileFormat'>
- **Required**: Yes


# DocumentOutputTextFormat

### types
- **Type**: typing.Optional[typing.List[typing.Literal['CSV', 'HTML', 'MARKDOWN', 'PLAIN_TEXT']]]


# DocumentOutputTextFormatOutput

### types
- **Type**: typing.Optional[typing.List[typing.Literal['CSV', 'HTML', 'MARKDOWN', 'PLAIN_TEXT']]]


# DocumentOverrideConfiguration

### splitter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.SplitterConfiguration]


# DocumentStandardExtraction

### granularity
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentExtractionGranularity'>
- **Required**: Yes

### boundingBox
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentBoundingBox'>
- **Required**: Yes


# DocumentStandardExtractionOutput

### granularity
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentExtractionGranularityOutput'>
- **Required**: Yes

### boundingBox
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentBoundingBox'>
- **Required**: Yes


# DocumentStandardGenerativeField

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# DocumentStandardOutputConfiguration

### extraction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentStandardExtraction]

### generativeField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentStandardGenerativeField]

### outputFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentOutputFormat]


# DocumentStandardOutputConfigurationOutput

### extraction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentStandardExtractionOutput]

### generativeField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentStandardGenerativeField]

### outputFormat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentOutputFormatOutput]


# EncryptionConfiguration

### kmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### kmsEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]


# GetBlueprintRequest

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### blueprintVersion
- **Type**: typing.Optional[str]

### blueprintStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# GetBlueprintResponse

### blueprint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Blueprint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataAutomationProjectRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]


# GetDataAutomationProjectResponse

### project
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DataAutomationProject'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# ImageBoundingBox

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# ImageExtractionCategory

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['CONTENT_MODERATION', 'LOGOS', 'TEXT_DETECTION']]]


# ImageExtractionCategoryOutput

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['CONTENT_MODERATION', 'LOGOS', 'TEXT_DETECTION']]]


# ImageStandardExtraction

### category
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageExtractionCategory'>
- **Required**: Yes

### boundingBox
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageBoundingBox'>
- **Required**: Yes


# ImageStandardExtractionOutput

### category
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageExtractionCategoryOutput'>
- **Required**: Yes

### boundingBox
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageBoundingBox'>
- **Required**: Yes


# ImageStandardGenerativeField

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['IAB', 'IMAGE_SUMMARY']]]


# ImageStandardGenerativeFieldOutput

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['IAB', 'IMAGE_SUMMARY']]]


# ImageStandardOutputConfiguration

### extraction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageStandardExtraction]

### generativeField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageStandardGenerativeField]


# ImageStandardOutputConfigurationOutput

### extraction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageStandardExtractionOutput]

### generativeField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageStandardGenerativeFieldOutput]


# ListBlueprintsRequest

### blueprintArn
- **Type**: typing.Optional[str]

### resourceOwner
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'SERVICE']]

### blueprintStageFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'DEVELOPMENT', 'LIVE']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### projectFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DataAutomationProjectFilter]


# ListBlueprintsRequestPaginate

### blueprintArn
- **Type**: typing.Optional[str]

### resourceOwner
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'SERVICE']]

### blueprintStageFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'DEVELOPMENT', 'LIVE']]

### projectFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DataAutomationProjectFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.PaginatorConfig]


# ListBlueprintsResponse

### blueprints
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.BlueprintSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataAutomationProjectsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### projectStageFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'DEVELOPMENT', 'LIVE']]

### blueprintFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.BlueprintFilter]

### resourceOwner
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'SERVICE']]


# ListDataAutomationProjectsRequestPaginate

### projectStageFilter
- **Type**: typing.Optional[typing.Literal['ALL', 'DEVELOPMENT', 'LIVE']]

### blueprintFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.BlueprintFilter]

### resourceOwner
- **Type**: typing.Optional[typing.Literal['ACCOUNT', 'SERVICE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.PaginatorConfig]


# ListDataAutomationProjectsResponse

### projects
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DataAutomationProjectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# OverrideConfiguration

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentOverrideConfiguration]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# SplitterConfiguration

### state
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# StandardOutputConfiguration

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentStandardOutputConfiguration]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageStandardOutputConfiguration]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoStandardOutputConfiguration]

### audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.AudioStandardOutputConfiguration]


# StandardOutputConfigurationOutput

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.DocumentStandardOutputConfigurationOutput]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ImageStandardOutputConfigurationOutput]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoStandardOutputConfigurationOutput]

### audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.AudioStandardOutputConfigurationOutput]


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateBlueprintRequest

### blueprintArn
- **Type**: <class 'str'>
- **Required**: Yes

### schema
- **Type**: <class 'str'>
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.UpdateBlueprintRequest'>>

### blueprintStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.EncryptionConfiguration]


# UpdateBlueprintResponse

### blueprint
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.Blueprint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataAutomationProjectRequest

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### standardOutputConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.StandardOutputConfiguration, aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.StandardOutputConfigurationOutput]
- **Required**: Yes

### projectStage
- **Type**: typing.Optional[typing.Literal['DEVELOPMENT', 'LIVE']]

### projectDescription
- **Type**: typing.Optional[str]

### customOutputConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.CustomOutputConfiguration, aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.CustomOutputConfigurationOutput, NoneType]

### overrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.OverrideConfiguration]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.EncryptionConfiguration]


# UpdateDataAutomationProjectResponse

### projectArn
- **Type**: <class 'str'>
- **Required**: Yes

### projectStage
- **Type**: typing.Literal['DEVELOPMENT', 'LIVE']
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.ResponseMetadata'>
- **Required**: Yes


# VideoBoundingBox

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# VideoExtractionCategory

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['CONTENT_MODERATION', 'LOGOS', 'TEXT_DETECTION', 'TRANSCRIPT']]]


# VideoExtractionCategoryOutput

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['CONTENT_MODERATION', 'LOGOS', 'TEXT_DETECTION', 'TRANSCRIPT']]]


# VideoStandardExtraction

### category
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoExtractionCategory'>
- **Required**: Yes

### boundingBox
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoBoundingBox'>
- **Required**: Yes


# VideoStandardExtractionOutput

### category
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoExtractionCategoryOutput'>
- **Required**: Yes

### boundingBox
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoBoundingBox'>
- **Required**: Yes


# VideoStandardGenerativeField

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['CHAPTER_SUMMARY', 'IAB', 'VIDEO_SUMMARY']]]


# VideoStandardGenerativeFieldOutput

### state
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### types
- **Type**: typing.Optional[typing.List[typing.Literal['CHAPTER_SUMMARY', 'IAB', 'VIDEO_SUMMARY']]]


# VideoStandardOutputConfiguration

### extraction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoStandardExtraction]

### generativeField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoStandardGenerativeField]


# VideoStandardOutputConfigurationOutput

### extraction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoStandardExtractionOutput]

### generativeField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_data_automation.bedrock_data_automation_classes.VideoStandardGenerativeFieldOutput]



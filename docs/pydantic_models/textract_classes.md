# Textract Classes

# Adapter

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Pages
- **Type**: typing.Optional[typing.List[str]]


# AdapterOverview

### AdapterId
- **Type**: typing.Optional[str]

### AdapterName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]]


# AdapterVersionDatasetConfig

### ManifestS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.S3Object]


# AdapterVersionEvaluationMetric

### Baseline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.EvaluationMetric]

### AdapterVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.EvaluationMetric]

### FeatureType
- **Type**: typing.Optional[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]


# AdapterVersionOverview

### AdapterId
- **Type**: typing.Optional[str]

### AdapterVersion
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'AT_RISK', 'CREATION_ERROR', 'CREATION_IN_PROGRESS', 'DEPRECATED']]

### StatusMessage
- **Type**: typing.Optional[str]


# AdaptersConfig

### Adapters
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Adapter]
- **Required**: Yes


# AnalyzeDocumentRequest

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.Document'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### HumanLoopConfig
- **Type**: <class 'NoneType'>

### QueriesConfig
- **Type**: <class 'NoneType'>

### AdaptersConfig
- **Type**: <class 'NoneType'>


# AnalyzeDocumentResponse

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Block]
- **Required**: Yes

### HumanLoopActivationOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.HumanLoopActivationOutput'>
- **Required**: Yes

### AnalyzeDocumentModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# AnalyzeExpenseRequest

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.Document'>
- **Required**: Yes


# AnalyzeExpenseResponse

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### ExpenseDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseDocument]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# AnalyzeIDDetections

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### NormalizedValue
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[float]


# AnalyzeIDRequest

### DocumentPages
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Document]
- **Required**: Yes


# AnalyzeIDResponse

### IdentityDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.IdentityDocument]
- **Required**: Yes

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### AnalyzeIDModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Block

### BlockType
- **Type**: typing.Optional[typing.Literal['CELL', 'KEY_VALUE_SET', 'LAYOUT_FIGURE', 'LAYOUT_FOOTER', 'LAYOUT_HEADER', 'LAYOUT_KEY_VALUE', 'LAYOUT_LIST', 'LAYOUT_PAGE_NUMBER', 'LAYOUT_SECTION_HEADER', 'LAYOUT_TABLE', 'LAYOUT_TEXT', 'LAYOUT_TITLE', 'LINE', 'MERGED_CELL', 'PAGE', 'QUERY', 'QUERY_RESULT', 'SELECTION_ELEMENT', 'SIGNATURE', 'TABLE', 'TABLE_FOOTER', 'TABLE_TITLE', 'TITLE', 'WORD']]

### Confidence
- **Type**: typing.Optional[float]

### Text
- **Type**: typing.Optional[str]

### TextType
- **Type**: typing.Optional[typing.Literal['HANDWRITING', 'PRINTED']]

### RowIndex
- **Type**: typing.Optional[int]

### ColumnIndex
- **Type**: typing.Optional[int]

### RowSpan
- **Type**: typing.Optional[int]

### ColumnSpan
- **Type**: typing.Optional[int]

### Geometry
- **Type**: <class 'NoneType'>

### Id
- **Type**: typing.Optional[str]

### Relationships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Relationship]]

### EntityTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COLUMN_HEADER', 'KEY', 'SEMI_STRUCTURED_TABLE', 'STRUCTURED_TABLE', 'TABLE_FOOTER', 'TABLE_SECTION_TITLE', 'TABLE_SUMMARY', 'TABLE_TITLE', 'VALUE']]]

### SelectionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SELECTED', 'SELECTED']]

### Page
- **Type**: typing.Optional[int]

### Query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.QueryOutput]


# BoundingBox

### Width
- **Type**: typing.Optional[float]

### Height
- **Type**: typing.Optional[float]

### Left
- **Type**: typing.Optional[float]

### Top
- **Type**: typing.Optional[float]


# CreateAdapterRequest

### AdapterName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### AutoUpdate
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAdapterResponse

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAdapterVersionRequest

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.AdapterVersionDatasetConfig'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.OutputConfig'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### KMSKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAdapterVersionResponse

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAdapterRequest

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAdapterVersionRequest

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DetectDocumentTextRequest

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.Document'>
- **Required**: Yes


# DetectDocumentTextResponse

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Block]
- **Required**: Yes

### DetectDocumentTextModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# DetectedSignature

### Page
- **Type**: typing.Optional[int]


# Document

### Bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### S3Object
- **Type**: <class 'NoneType'>


# DocumentGroup

### Type
- **Type**: typing.Optional[str]

### SplitDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.SplitDocument]]

### DetectedSignatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.DetectedSignature]]

### UndetectedSignatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.UndetectedSignature]]


# DocumentLocation

### S3Object
- **Type**: <class 'NoneType'>


# DocumentMetadata

### Pages
- **Type**: typing.Optional[int]


# EvaluationMetric

### F1Score
- **Type**: typing.Optional[float]

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]


# ExpenseCurrency

### Code
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]


# ExpenseDetection

### Text
- **Type**: typing.Optional[str]

### Geometry
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[float]


# ExpenseDocument

### ExpenseIndex
- **Type**: typing.Optional[int]

### SummaryFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseField]]

### LineItemGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.LineItemGroup]]

### Blocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Block]]


# ExpenseField

### Type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseType]

### LabelDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseDetection]

### ValueDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseDetection]

### PageNumber
- **Type**: typing.Optional[int]

### Currency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseCurrency]

### GroupProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseGroupProperty]]


# ExpenseGroupProperty

### Types
- **Type**: typing.Optional[typing.List[str]]

### Id
- **Type**: typing.Optional[str]


# ExpenseType

### Text
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]


# Extraction

### LendingDocument
- **Type**: <class 'NoneType'>

### ExpenseDocument
- **Type**: <class 'NoneType'>

### IdentityDocument
- **Type**: <class 'NoneType'>


# Geometry

### BoundingBox
- **Type**: <class 'NoneType'>

### Polygon
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Point]]


# GetAdapterRequest

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdapterResponse

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### AutoUpdate
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# GetAdapterVersionRequest

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdapterVersionResponse

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterVersion
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'AT_RISK', 'CREATION_ERROR', 'CREATION_IN_PROGRESS', 'DEPRECATED']
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.AdapterVersionDatasetConfig'>
- **Required**: Yes

### KMSKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.OutputConfig'>
- **Required**: Yes

### EvaluationMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.AdapterVersionEvaluationMetric]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# GetDocumentAnalysisRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetDocumentAnalysisResponse

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Block]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Warning]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzeDocumentModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetDocumentTextDetectionRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetDocumentTextDetectionResponse

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Block]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Warning]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### DetectDocumentTextModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetExpenseAnalysisRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetExpenseAnalysisResponse

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### ExpenseDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseDocument]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Warning]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzeExpenseModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLendingAnalysisRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetLendingAnalysisResponse

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.LendingResult]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Warning]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzeLendingModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetLendingAnalysisSummaryRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLendingAnalysisSummaryResponse

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentMetadata'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.LendingSummary'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Warning]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzeLendingModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.HumanLoopDataAttributes]


# HumanLoopDataAttributes

### ContentClassifiers
- **Type**: typing.Optional[typing.List[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]]


# IdentityDocument

### DocumentIndex
- **Type**: typing.Optional[int]

### IdentityDocumentFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.IdentityDocumentField]]

### Blocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Block]]


# IdentityDocumentField

### Type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.AnalyzeIDDetections]

### ValueDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.AnalyzeIDDetections]


# LendingDetection

### Text
- **Type**: typing.Optional[str]

### SelectionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SELECTED', 'SELECTED']]

### Geometry
- **Type**: <class 'NoneType'>

### Confidence
- **Type**: typing.Optional[float]


# LendingDocument

### LendingFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.LendingField]]

### SignatureDetections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.SignatureDetection]]


# LendingField

### Type
- **Type**: typing.Optional[str]

### KeyDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.LendingDetection]

### ValueDetections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.LendingDetection]]


# LendingResult

### Page
- **Type**: typing.Optional[int]

### PageClassification
- **Type**: <class 'NoneType'>

### Extractions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Extraction]]


# LendingSummary

### DocumentGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.DocumentGroup]]

### UndetectedDocumentTypes
- **Type**: typing.Optional[typing.List[str]]


# LineItemFields

### LineItemExpenseFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.ExpenseField]]


# LineItemGroup

### LineItemGroupIndex
- **Type**: typing.Optional[int]

### LineItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.LineItemFields]]


# ListAdapterVersionsRequest

### AdapterId
- **Type**: typing.Optional[str]

### AfterCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BeforeCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAdapterVersionsRequestPaginate

### AdapterId
- **Type**: typing.Optional[str]

### AfterCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BeforeCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.PaginatorConfig]


# ListAdapterVersionsResponse

### AdapterVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.AdapterVersionOverview]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAdaptersRequest

### AfterCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BeforeCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAdaptersRequestPaginate

### AfterCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BeforeCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract.textract_classes.PaginatorConfig]


# ListAdaptersResponse

### Adapters
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.AdapterOverview]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# NormalizedValue

### Value
- **Type**: typing.Optional[str]

### ValueType
- **Type**: typing.Optional[typing.Literal['DATE']]


# NotificationChannel

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# OutputConfig

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: typing.Optional[str]


# PageClassification

### PageType
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Prediction]
- **Required**: Yes

### PageNumber
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract.textract_classes.Prediction]
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Point

### X
- **Type**: typing.Optional[float]

### Y
- **Type**: typing.Optional[float]


# Prediction

### Value
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]


# QueriesConfig

### Queries
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.textract.textract_classes.Query, aws_resource_validator.pydantic_models.textract.textract_classes.QueryOutput]]
- **Required**: Yes


# Query

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Pages
- **Type**: typing.Optional[typing.List[str]]


# QueryOutput

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Pages
- **Type**: typing.Optional[typing.List[str]]


# Relationship

### Type
- **Type**: typing.Optional[typing.Literal['ANSWER', 'CHILD', 'COMPLEX_FEATURES', 'MERGED_CELL', 'TABLE', 'TABLE_FOOTER', 'TABLE_TITLE', 'TITLE', 'VALUE']]

### Ids
- **Type**: typing.Optional[typing.List[str]]


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


# S3Object

### Bucket
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# SignatureDetection

### Confidence
- **Type**: typing.Optional[float]

### Geometry
- **Type**: <class 'NoneType'>


# SplitDocument

### Index
- **Type**: typing.Optional[int]

### Pages
- **Type**: typing.Optional[typing.List[int]]


# StartDocumentAnalysisRequest

### DocumentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentLocation'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobTag
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### OutputConfig
- **Type**: <class 'NoneType'>

### KMSKeyId
- **Type**: typing.Optional[str]

### QueriesConfig
- **Type**: <class 'NoneType'>

### AdaptersConfig
- **Type**: <class 'NoneType'>


# StartDocumentAnalysisResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# StartDocumentTextDetectionRequest

### DocumentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentLocation'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobTag
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### OutputConfig
- **Type**: <class 'NoneType'>

### KMSKeyId
- **Type**: typing.Optional[str]


# StartDocumentTextDetectionResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# StartExpenseAnalysisRequest

### DocumentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentLocation'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobTag
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### OutputConfig
- **Type**: <class 'NoneType'>

### KMSKeyId
- **Type**: typing.Optional[str]


# StartExpenseAnalysisResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# StartLendingAnalysisRequest

### DocumentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.DocumentLocation'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobTag
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: <class 'NoneType'>

### OutputConfig
- **Type**: <class 'NoneType'>

### KMSKeyId
- **Type**: typing.Optional[str]


# StartLendingAnalysisResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UndetectedSignature

### Page
- **Type**: typing.Optional[int]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAdapterRequest

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AdapterName
- **Type**: typing.Optional[str]

### AutoUpdate
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateAdapterResponse

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### AutoUpdate
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract.textract_classes.ResponseMetadata'>
- **Required**: Yes


# Warning

### ErrorCode
- **Type**: typing.Optional[str]

### Pages
- **Type**: typing.Optional[typing.List[int]]



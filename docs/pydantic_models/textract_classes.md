# textract_classes

# AdapterOverviewTypeDef

### AdapterId
- **Type**: typing.Optional[str]

### AdapterName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FeatureTypes
- **Type**: typing.Optional[typing.List[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]]


# AdapterTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Pages
- **Type**: typing.Optional[typing.Sequence[str]]


# AdapterVersionDatasetConfigTypeDef

### ManifestS3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.S3ObjectTypeDef]


# AdapterVersionEvaluationMetricTypeDef

### Baseline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.EvaluationMetricTypeDef]

### AdapterVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.EvaluationMetricTypeDef]

### FeatureType
- **Type**: typing.Optional[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]


# AdapterVersionOverviewTypeDef

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


# AdaptersConfigTypeDef

### Adapters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.textract_classes.AdapterTypeDef]
- **Required**: Yes


# AnalyzeDocumentRequestRequestTypeDef

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentTypeDef'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.Sequence[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### HumanLoopConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.HumanLoopConfigTypeDef]

### QueriesConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.QueriesConfigTypeDef]

### AdaptersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.AdaptersConfigTypeDef]


# AnalyzeDocumentResponseTypeDef

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.BlockTypeDef]
- **Required**: Yes

### HumanLoopActivationOutput
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.HumanLoopActivationOutputTypeDef'>
- **Required**: Yes

### AnalyzeDocumentModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AnalyzeExpenseRequestRequestTypeDef

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentTypeDef'>
- **Required**: Yes


# AnalyzeExpenseResponseTypeDef

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### ExpenseDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.ExpenseDocumentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AnalyzeIDDetectionsTypeDef

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### NormalizedValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.NormalizedValueTypeDef]

### Confidence
- **Type**: typing.Optional[float]


# AnalyzeIDRequestRequestTypeDef

### DocumentPages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.textract_classes.DocumentTypeDef]
- **Required**: Yes


# AnalyzeIDResponseTypeDef

### IdentityDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.IdentityDocumentTypeDef]
- **Required**: Yes

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### AnalyzeIDModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlockTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.GeometryTypeDef]

### Id
- **Type**: typing.Optional[str]

### Relationships
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.RelationshipTypeDef]]

### EntityTypes
- **Type**: typing.Optional[typing.List[typing.Literal['COLUMN_HEADER', 'KEY', 'SEMI_STRUCTURED_TABLE', 'STRUCTURED_TABLE', 'TABLE_FOOTER', 'TABLE_SECTION_TITLE', 'TABLE_SUMMARY', 'TABLE_TITLE', 'VALUE']]]

### SelectionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SELECTED', 'SELECTED']]

### Page
- **Type**: typing.Optional[int]

### Query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.QueryTypeDef]


# BoundingBoxTypeDef

### Width
- **Type**: typing.Optional[float]

### Height
- **Type**: typing.Optional[float]

### Left
- **Type**: typing.Optional[float]

### Top
- **Type**: typing.Optional[float]


# CreateAdapterRequestRequestTypeDef

### AdapterName
- **Type**: <class 'str'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.Sequence[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### AutoUpdate
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAdapterResponseTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAdapterVersionRequestRequestTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### DatasetConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.AdapterVersionDatasetConfigTypeDef'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.OutputConfigTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### KMSKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAdapterVersionResponseTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAdapterRequestRequestTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAdapterVersionRequestRequestTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterVersion
- **Type**: <class 'str'>
- **Required**: Yes


# DetectDocumentTextRequestRequestTypeDef

### Document
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentTypeDef'>
- **Required**: Yes


# DetectDocumentTextResponseTypeDef

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.BlockTypeDef]
- **Required**: Yes

### DetectDocumentTextModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetectedSignatureTypeDef

### Page
- **Type**: typing.Optional[int]


# DocumentGroupTypeDef

### Type
- **Type**: typing.Optional[str]

### SplitDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.SplitDocumentTypeDef]]

### DetectedSignatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.DetectedSignatureTypeDef]]

### UndetectedSignatures
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.UndetectedSignatureTypeDef]]


# DocumentLocationTypeDef

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.S3ObjectTypeDef]


# DocumentMetadataTypeDef

### Pages
- **Type**: typing.Optional[int]


# DocumentTypeDef

### Bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### S3Object
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.S3ObjectTypeDef]


# EvaluationMetricTypeDef

### F1Score
- **Type**: typing.Optional[float]

### Precision
- **Type**: typing.Optional[float]

### Recall
- **Type**: typing.Optional[float]


# ExpenseCurrencyTypeDef

### Code
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]


# ExpenseDetectionTypeDef

### Text
- **Type**: typing.Optional[str]

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.GeometryTypeDef]

### Confidence
- **Type**: typing.Optional[float]


# ExpenseDocumentTypeDef

### ExpenseIndex
- **Type**: typing.Optional[int]

### SummaryFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.ExpenseFieldTypeDef]]

### LineItemGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.LineItemGroupTypeDef]]

### Blocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.BlockTypeDef]]


# ExpenseFieldTypeDef

### Type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.ExpenseTypeTypeDef]

### LabelDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.ExpenseDetectionTypeDef]

### ValueDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.ExpenseDetectionTypeDef]

### PageNumber
- **Type**: typing.Optional[int]

### Currency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.ExpenseCurrencyTypeDef]

### GroupProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.ExpenseGroupPropertyTypeDef]]


# ExpenseGroupPropertyTypeDef

### Types
- **Type**: typing.Optional[typing.List[str]]

### Id
- **Type**: typing.Optional[str]


# ExpenseTypeTypeDef

### Text
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]


# ExtractionTypeDef

### LendingDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.LendingDocumentTypeDef]

### ExpenseDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.ExpenseDocumentTypeDef]

### IdentityDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.IdentityDocumentTypeDef]


# GeometryTypeDef

### BoundingBox
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.BoundingBoxTypeDef]

### Polygon
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.PointTypeDef]]


# GetAdapterRequestRequestTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdapterResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAdapterVersionRequestRequestTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### AdapterVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetAdapterVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.AdapterVersionDatasetConfigTypeDef'>
- **Required**: Yes

### KMSKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.OutputConfigTypeDef'>
- **Required**: Yes

### EvaluationMetrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.AdapterVersionEvaluationMetricTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDocumentAnalysisRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetDocumentAnalysisResponseTypeDef

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.BlockTypeDef]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.WarningTypeDef]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzeDocumentModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDocumentTextDetectionRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetDocumentTextDetectionResponseTypeDef

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Blocks
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.BlockTypeDef]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.WarningTypeDef]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### DetectDocumentTextModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExpenseAnalysisRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetExpenseAnalysisResponseTypeDef

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ExpenseDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.ExpenseDocumentTypeDef]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.WarningTypeDef]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzeExpenseModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLendingAnalysisRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetLendingAnalysisResponseTypeDef

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Results
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.LendingResultTypeDef]
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.WarningTypeDef]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzeLendingModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLendingAnalysisSummaryRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLendingAnalysisSummaryResponseTypeDef

### DocumentMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentMetadataTypeDef'>
- **Required**: Yes

### JobStatus
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'PARTIAL_SUCCESS', 'SUCCEEDED']
- **Required**: Yes

### Summary
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.LendingSummaryTypeDef'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.WarningTypeDef]
- **Required**: Yes

### StatusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AnalyzeLendingModelVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.HumanLoopDataAttributesTypeDef]


# HumanLoopDataAttributesTypeDef

### ContentClassifiers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FreeOfAdultContent', 'FreeOfPersonallyIdentifiableInformation']]]


# IdentityDocumentFieldTypeDef

### Type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.AnalyzeIDDetectionsTypeDef]

### ValueDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.AnalyzeIDDetectionsTypeDef]


# IdentityDocumentTypeDef

### DocumentIndex
- **Type**: typing.Optional[int]

### IdentityDocumentFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.IdentityDocumentFieldTypeDef]]

### Blocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.BlockTypeDef]]


# LendingDetectionTypeDef

### Text
- **Type**: typing.Optional[str]

### SelectionStatus
- **Type**: typing.Optional[typing.Literal['NOT_SELECTED', 'SELECTED']]

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.GeometryTypeDef]

### Confidence
- **Type**: typing.Optional[float]


# LendingDocumentTypeDef

### LendingFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.LendingFieldTypeDef]]

### SignatureDetections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.SignatureDetectionTypeDef]]


# LendingFieldTypeDef

### Type
- **Type**: typing.Optional[str]

### KeyDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.LendingDetectionTypeDef]

### ValueDetections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.LendingDetectionTypeDef]]


# LendingResultTypeDef

### Page
- **Type**: typing.Optional[int]

### PageClassification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.PageClassificationTypeDef]

### Extractions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.ExtractionTypeDef]]


# LendingSummaryTypeDef

### DocumentGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.DocumentGroupTypeDef]]

### UndetectedDocumentTypes
- **Type**: typing.Optional[typing.List[str]]


# LineItemFieldsTypeDef

### LineItemExpenseFields
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.ExpenseFieldTypeDef]]


# LineItemGroupTypeDef

### LineItemGroupIndex
- **Type**: typing.Optional[int]

### LineItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.textract_classes.LineItemFieldsTypeDef]]


# ListAdapterVersionsRequestListAdapterVersionsPaginateTypeDef

### AdapterId
- **Type**: typing.Optional[str]

### AfterCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BeforeCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.PaginatorConfigTypeDef]


# ListAdapterVersionsRequestRequestTypeDef

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


# ListAdapterVersionsResponseTypeDef

### AdapterVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.AdapterVersionOverviewTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAdaptersRequestListAdaptersPaginateTypeDef

### AfterCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BeforeCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.PaginatorConfigTypeDef]


# ListAdaptersRequestRequestTypeDef

### AfterCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### BeforeCreationTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAdaptersResponseTypeDef

### Adapters
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.AdapterOverviewTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NormalizedValueTypeDef

### Value
- **Type**: typing.Optional[str]

### ValueType
- **Type**: typing.Optional[typing.Literal['DATE']]


# NotificationChannelTypeDef

### SNSTopicArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# OutputConfigTypeDef

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: typing.Optional[str]


# PageClassificationTypeDef

### PageType
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.PredictionTypeDef]
- **Required**: Yes

### PageNumber
- **Type**: typing.List[aws_resource_validator.pydantic_models.textract_classes.PredictionTypeDef]
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PointTypeDef

### X
- **Type**: typing.Optional[float]

### Y
- **Type**: typing.Optional[float]


# PredictionTypeDef

### Value
- **Type**: typing.Optional[str]

### Confidence
- **Type**: typing.Optional[float]


# QueriesConfigTypeDef

### Queries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.textract_classes.QueryTypeDef]
- **Required**: Yes


# QueryTypeDef

### Text
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: typing.Optional[str]

### Pages
- **Type**: typing.Optional[typing.Sequence[str]]


# RelationshipTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['ANSWER', 'CHILD', 'COMPLEX_FEATURES', 'MERGED_CELL', 'TABLE', 'TABLE_FOOTER', 'TABLE_TITLE', 'TITLE', 'VALUE']]

### Ids
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


# S3ObjectTypeDef

### Bucket
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]


# SignatureDetectionTypeDef

### Confidence
- **Type**: typing.Optional[float]

### Geometry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.GeometryTypeDef]


# SplitDocumentTypeDef

### Index
- **Type**: typing.Optional[int]

### Pages
- **Type**: typing.Optional[typing.List[int]]


# StartDocumentAnalysisRequestRequestTypeDef

### DocumentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentLocationTypeDef'>
- **Required**: Yes

### FeatureTypes
- **Type**: typing.Sequence[typing.Literal['FORMS', 'LAYOUT', 'QUERIES', 'SIGNATURES', 'TABLES']]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobTag
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.NotificationChannelTypeDef]

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.OutputConfigTypeDef]

### KMSKeyId
- **Type**: typing.Optional[str]

### QueriesConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.QueriesConfigTypeDef]

### AdaptersConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.AdaptersConfigTypeDef]


# StartDocumentAnalysisResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDocumentTextDetectionRequestRequestTypeDef

### DocumentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentLocationTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobTag
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.NotificationChannelTypeDef]

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.OutputConfigTypeDef]

### KMSKeyId
- **Type**: typing.Optional[str]


# StartDocumentTextDetectionResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartExpenseAnalysisRequestRequestTypeDef

### DocumentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentLocationTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobTag
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.NotificationChannelTypeDef]

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.OutputConfigTypeDef]

### KMSKeyId
- **Type**: typing.Optional[str]


# StartExpenseAnalysisResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartLendingAnalysisRequestRequestTypeDef

### DocumentLocation
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.DocumentLocationTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### JobTag
- **Type**: typing.Optional[str]

### NotificationChannel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.NotificationChannelTypeDef]

### OutputConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.textract_classes.OutputConfigTypeDef]

### KMSKeyId
- **Type**: typing.Optional[str]


# StartLendingAnalysisResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UndetectedSignatureTypeDef

### Page
- **Type**: typing.Optional[int]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAdapterRequestRequestTypeDef

### AdapterId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AdapterName
- **Type**: typing.Optional[str]

### AutoUpdate
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateAdapterResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.textract_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WarningTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### Pages
- **Type**: typing.Optional[typing.List[int]]



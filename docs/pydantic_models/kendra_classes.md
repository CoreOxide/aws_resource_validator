# Kendra Classes

# AccessControlConfigurationSummaryTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# AccessControlListConfigurationTypeDef

### KeyPath
- **Type**: typing.Optional[str]


# AclConfigurationTypeDef

### AllowedGroupsColumnName
- **Type**: <class 'str'>
- **Required**: Yes


# AdditionalResultAttributeTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['TEXT_WITH_HIGHLIGHTS_VALUE']
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.AdditionalResultAttributeValueTypeDef'>
- **Required**: Yes


# AdditionalResultAttributeValueTypeDef

### TextWithHighlightsValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TextWithHighlightsTypeDef]


# AlfrescoConfigurationOutputTypeDef

### SiteUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SslCertificateS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes

### CrawlSystemFolders
- **Type**: typing.Optional[bool]

### CrawlComments
- **Type**: typing.Optional[bool]

### EntityFilter
- **Type**: typing.Optional[typing.List[typing.Literal['blog', 'documentLibrary', 'wiki']]]

### DocumentLibraryFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### BlogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### WikiFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef]


# AlfrescoConfigurationTypeDef

### SiteUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SiteId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SslCertificateS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes

### CrawlSystemFolders
- **Type**: typing.Optional[bool]

### CrawlComments
- **Type**: typing.Optional[bool]

### EntityFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['blog', 'documentLibrary', 'wiki']]]

### DocumentLibraryFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### BlogFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### WikiFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]


# AssociateEntitiesToExperienceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.EntityConfigurationTypeDef]
- **Required**: Yes


# AssociateEntitiesToExperienceResponseTypeDef

### FailedEntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FailedEntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatePersonasToEntitiesRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Personas
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.EntityPersonaConfigurationTypeDef]
- **Required**: Yes


# AssociatePersonasToEntitiesResponseTypeDef

### FailedEntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FailedEntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttributeFilterTypeDef

### AndAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### OrAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### NotFilter
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### EqualsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]

### ContainsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]

### ContainsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]

### GreaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]

### GreaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]

### LessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]

### LessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]


# AttributeSuggestionsDescribeConfigTypeDef

### SuggestableConfigList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.SuggestableConfigTypeDef]]

### AttributeSuggestionsMode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# AttributeSuggestionsGetConfigTypeDef

### SuggestionAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### AdditionalResponseAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### AttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AttributeFilterTypeDef]

### UserContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserContextTypeDef]


# AttributeSuggestionsUpdateConfigTypeDef

### SuggestableConfigList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.SuggestableConfigTypeDef]]

### AttributeSuggestionsMode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# AuthenticationConfigurationOutputTypeDef

### BasicAuthentication
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.BasicAuthenticationConfigurationTypeDef]]


# AuthenticationConfigurationTypeDef

### BasicAuthentication
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.BasicAuthenticationConfigurationTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthenticationConfigurationTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Credentials
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteDocumentRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DataSourceSyncJobMetricTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceSyncJobMetricTargetTypeDef]


# BatchDeleteDocumentResponseFailedDocumentTypeDef

### Id
- **Type**: typing.Optional[str]

### DataSourceId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest']]

### ErrorMessage
- **Type**: typing.Optional[str]


# BatchDeleteDocumentResponseTypeDef

### FailedDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.BatchDeleteDocumentResponseFailedDocumentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteFeaturedResultsSetErrorTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['InternalError', 'InvalidRequest']
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteFeaturedResultsSetRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturedResultsSetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeleteFeaturedResultsSetResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.BatchDeleteFeaturedResultsSetErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetDocumentStatusRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentInfoList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentInfoTypeDef]
- **Required**: Yes


# BatchGetDocumentStatusResponseErrorTypeDef

### DocumentId
- **Type**: typing.Optional[str]

### DataSourceId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest']]

### ErrorMessage
- **Type**: typing.Optional[str]


# BatchGetDocumentStatusResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.BatchGetDocumentStatusResponseErrorTypeDef]
- **Required**: Yes

### DocumentStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.StatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchPutDocumentRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentTypeDef]
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### CustomDocumentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CustomDocumentEnrichmentConfigurationUnionTypeDef]


# BatchPutDocumentResponseFailedDocumentTypeDef

### Id
- **Type**: typing.Optional[str]

### DataSourceId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest']]

### ErrorMessage
- **Type**: typing.Optional[str]


# BatchPutDocumentResponseTypeDef

### FailedDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.BatchPutDocumentResponseFailedDocumentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BoxConfigurationOutputTypeDef

### EnterpriseId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### UseChangeLog
- **Type**: typing.Optional[bool]

### CrawlComments
- **Type**: typing.Optional[bool]

### CrawlTasks
- **Type**: typing.Optional[bool]

### CrawlWebLinks
- **Type**: typing.Optional[bool]

### FileFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### TaskFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### CommentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### WebLinkFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef]


# BoxConfigurationTypeDef

### EnterpriseId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### UseChangeLog
- **Type**: typing.Optional[bool]

### CrawlComments
- **Type**: typing.Optional[bool]

### CrawlTasks
- **Type**: typing.Optional[bool]

### CrawlWebLinks
- **Type**: typing.Optional[bool]

### FileFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### TaskFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### CommentFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### WebLinkFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]


# CapacityUnitsConfigurationTypeDef

### StorageCapacityUnits
- **Type**: <class 'int'>
- **Required**: Yes

### QueryCapacityUnits
- **Type**: <class 'int'>
- **Required**: Yes


# ClearQuerySuggestionsRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# ClickFeedbackTypeDef

### ResultId
- **Type**: <class 'str'>
- **Required**: Yes

### ClickTime
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.TimestampTypeDef'>
- **Required**: Yes


# CollapseConfigurationTypeDef

### DocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### SortingConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.SortingConfigurationTypeDef]]

### MissingAttributeKeyStrategy
- **Type**: typing.Optional[typing.Literal['COLLAPSE', 'EXPAND', 'IGNORE']]

### Expand
- **Type**: typing.Optional[bool]

### ExpandConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ExpandConfigurationTypeDef]


# CollapsedResultDetailTypeDef

### DocumentAttribute
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeOutputTypeDef'>
- **Required**: Yes

### ExpandedResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.ExpandedResultItemTypeDef]]


# ColumnConfigurationOutputTypeDef

### DocumentIdColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentDataColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeDetectingColumns
- **Type**: typing.List[str]
- **Required**: Yes

### DocumentTitleColumnName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# ColumnConfigurationTypeDef

### DocumentIdColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentDataColumnName
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeDetectingColumns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DocumentTitleColumnName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# ConfluenceAttachmentConfigurationOutputTypeDef

### CrawlAttachments
- **Type**: typing.Optional[bool]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceAttachmentToIndexFieldMappingTypeDef]]


# ConfluenceAttachmentConfigurationTypeDef

### CrawlAttachments
- **Type**: typing.Optional[bool]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceAttachmentToIndexFieldMappingTypeDef]]


# ConfluenceAttachmentToIndexFieldMappingTypeDef

### DataSourceFieldName
- **Type**: typing.Optional[typing.Literal['AUTHOR', 'CONTENT_TYPE', 'CREATED_DATE', 'DISPLAY_URL', 'FILE_SIZE', 'ITEM_TYPE', 'PARENT_ID', 'SPACE_KEY', 'SPACE_NAME', 'URL', 'VERSION']]

### DateFieldFormat
- **Type**: typing.Optional[str]

### IndexFieldName
- **Type**: typing.Optional[str]


# ConfluenceBlogConfigurationOutputTypeDef

### BlogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceBlogToIndexFieldMappingTypeDef]]


# ConfluenceBlogConfigurationTypeDef

### BlogFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceBlogToIndexFieldMappingTypeDef]]


# ConfluenceBlogToIndexFieldMappingTypeDef

### DataSourceFieldName
- **Type**: typing.Optional[typing.Literal['AUTHOR', 'DISPLAY_URL', 'ITEM_TYPE', 'LABELS', 'PUBLISH_DATE', 'SPACE_KEY', 'SPACE_NAME', 'URL', 'VERSION']]

### DateFieldFormat
- **Type**: typing.Optional[str]

### IndexFieldName
- **Type**: typing.Optional[str]


# ConfluenceConfigurationOutputTypeDef

### ServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Literal['CLOUD', 'SERVER']
- **Required**: Yes

### SpaceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceSpaceConfigurationOutputTypeDef]

### PageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluencePageConfigurationOutputTypeDef]

### BlogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceBlogConfigurationOutputTypeDef]

### AttachmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceAttachmentConfigurationOutputTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ProxyConfigurationTypeDef]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'PAT']]


# ConfluenceConfigurationTypeDef

### ServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: typing.Literal['CLOUD', 'SERVER']
- **Required**: Yes

### SpaceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceSpaceConfigurationTypeDef]

### PageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluencePageConfigurationTypeDef]

### BlogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceBlogConfigurationTypeDef]

### AttachmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceAttachmentConfigurationTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ProxyConfigurationTypeDef]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'PAT']]


# ConfluencePageConfigurationOutputTypeDef

### PageFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.ConfluencePageToIndexFieldMappingTypeDef]]


# ConfluencePageConfigurationTypeDef

### PageFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.ConfluencePageToIndexFieldMappingTypeDef]]


# ConfluencePageToIndexFieldMappingTypeDef

### DataSourceFieldName
- **Type**: typing.Optional[typing.Literal['AUTHOR', 'CONTENT_STATUS', 'CREATED_DATE', 'DISPLAY_URL', 'ITEM_TYPE', 'LABELS', 'MODIFIED_DATE', 'PARENT_ID', 'SPACE_KEY', 'SPACE_NAME', 'URL', 'VERSION']]

### DateFieldFormat
- **Type**: typing.Optional[str]

### IndexFieldName
- **Type**: typing.Optional[str]


# ConfluenceSpaceConfigurationOutputTypeDef

### CrawlPersonalSpaces
- **Type**: typing.Optional[bool]

### CrawlArchivedSpaces
- **Type**: typing.Optional[bool]

### IncludeSpaces
- **Type**: typing.Optional[typing.List[str]]

### ExcludeSpaces
- **Type**: typing.Optional[typing.List[str]]

### SpaceFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceSpaceToIndexFieldMappingTypeDef]]


# ConfluenceSpaceConfigurationTypeDef

### CrawlPersonalSpaces
- **Type**: typing.Optional[bool]

### CrawlArchivedSpaces
- **Type**: typing.Optional[bool]

### IncludeSpaces
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludeSpaces
- **Type**: typing.Optional[typing.Sequence[str]]

### SpaceFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceSpaceToIndexFieldMappingTypeDef]]


# ConfluenceSpaceToIndexFieldMappingTypeDef

### DataSourceFieldName
- **Type**: typing.Optional[typing.Literal['DISPLAY_URL', 'ITEM_TYPE', 'SPACE_KEY', 'URL']]

### DateFieldFormat
- **Type**: typing.Optional[str]

### IndexFieldName
- **Type**: typing.Optional[str]


# ConnectionConfigurationTypeDef

### DatabaseHost
- **Type**: <class 'str'>
- **Required**: Yes

### DatabasePort
- **Type**: <class 'int'>
- **Required**: Yes

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes


# ContentSourceConfigurationOutputTypeDef

### DataSourceIds
- **Type**: typing.Optional[typing.List[str]]

### FaqIds
- **Type**: typing.Optional[typing.List[str]]

### DirectPutContent
- **Type**: typing.Optional[bool]


# ContentSourceConfigurationTypeDef

### DataSourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### FaqIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DirectPutContent
- **Type**: typing.Optional[bool]


# CorrectionTypeDef

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Term
- **Type**: typing.Optional[str]

### CorrectedTerm
- **Type**: typing.Optional[str]


# CreateAccessControlConfigurationRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.PrincipalTypeDef]]

### HierarchicalAccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.HierarchicalPrincipalUnionTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateAccessControlConfigurationResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExperienceRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ExperienceConfigurationUnionTypeDef]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# CreateExperienceResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFaqRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### S3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.TagTypeDef]]

### FileFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'CSV_WITH_HEADER', 'JSON']]

### ClientToken
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]


# CreateFaqResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFeaturedResultsSetRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturedResultsSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### QueryTexts
- **Type**: typing.Optional[typing.Sequence[str]]

### FeaturedDocuments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.FeaturedDocumentTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.TagTypeDef]]


# CreateFeaturedResultsSetResponseTypeDef

### FeaturedResultsSet
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.FeaturedResultsSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIndexRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Edition
- **Type**: typing.Optional[typing.Literal['DEVELOPER_EDITION', 'ENTERPRISE_EDITION', 'GEN_AI_ENTERPRISE_EDITION']]

### ServerSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ServerSideEncryptionConfigurationTypeDef]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.TagTypeDef]]

### UserTokenConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.UserTokenConfigurationTypeDef]]

### UserContextPolicy
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_FILTER', 'USER_TOKEN']]

### UserGroupResolutionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserGroupResolutionConfigurationTypeDef]


# CreateIndexResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQuerySuggestionsBlockListRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.TagTypeDef]]


# CreateQuerySuggestionsBlockListResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateThesaurusRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateThesaurusResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomDocumentEnrichmentConfigurationOutputTypeDef

### InlineConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.InlineCustomDocumentEnrichmentConfigurationOutputTypeDef]]

### PreExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.HookConfigurationOutputTypeDef]

### PostExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.HookConfigurationOutputTypeDef]

### RoleArn
- **Type**: typing.Optional[str]


# CustomDocumentEnrichmentConfigurationTypeDef

### InlineConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.InlineCustomDocumentEnrichmentConfigurationTypeDef]]

### PreExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.HookConfigurationTypeDef]

### PostExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.HookConfigurationTypeDef]

### RoleArn
- **Type**: typing.Optional[str]


# CustomDocumentEnrichmentConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceConfigurationOutputTypeDef

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3DataSourceConfigurationOutputTypeDef]

### SharePointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SharePointConfigurationOutputTypeDef]

### DatabaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DatabaseConfigurationOutputTypeDef]

### SalesforceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceConfigurationOutputTypeDef]

### OneDriveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.OneDriveConfigurationOutputTypeDef]

### ServiceNowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ServiceNowConfigurationOutputTypeDef]

### ConfluenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceConfigurationOutputTypeDef]

### GoogleDriveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.GoogleDriveConfigurationOutputTypeDef]

### WebCrawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.WebCrawlerConfigurationOutputTypeDef]

### WorkDocsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.WorkDocsConfigurationOutputTypeDef]

### FsxConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.FsxConfigurationOutputTypeDef]

### SlackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SlackConfigurationOutputTypeDef]

### BoxConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.BoxConfigurationOutputTypeDef]

### QuipConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.QuipConfigurationOutputTypeDef]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.JiraConfigurationOutputTypeDef]

### GitHubConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.GitHubConfigurationOutputTypeDef]

### AlfrescoConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AlfrescoConfigurationOutputTypeDef]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TemplateConfigurationOutputTypeDef]


# DataSourceConfigurationTypeDef

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3DataSourceConfigurationTypeDef]

### SharePointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SharePointConfigurationTypeDef]

### DatabaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DatabaseConfigurationTypeDef]

### SalesforceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceConfigurationTypeDef]

### OneDriveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.OneDriveConfigurationTypeDef]

### ServiceNowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ServiceNowConfigurationTypeDef]

### ConfluenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ConfluenceConfigurationTypeDef]

### GoogleDriveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.GoogleDriveConfigurationTypeDef]

### WebCrawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.WebCrawlerConfigurationTypeDef]

### WorkDocsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.WorkDocsConfigurationTypeDef]

### FsxConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.FsxConfigurationTypeDef]

### SlackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SlackConfigurationTypeDef]

### BoxConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.BoxConfigurationTypeDef]

### QuipConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.QuipConfigurationTypeDef]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.JiraConfigurationTypeDef]

### GitHubConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.GitHubConfigurationTypeDef]

### AlfrescoConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AlfrescoConfigurationTypeDef]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TemplateConfigurationTypeDef]


# DataSourceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceGroupTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DataSourceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceSyncJobMetricTargetTypeDef

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceSyncJobId
- **Type**: typing.Optional[str]


# DataSourceSyncJobMetricsTypeDef

### DocumentsAdded
- **Type**: typing.Optional[str]

### DocumentsModified
- **Type**: typing.Optional[str]

### DocumentsDeleted
- **Type**: typing.Optional[str]

### DocumentsFailed
- **Type**: typing.Optional[str]

### DocumentsScanned
- **Type**: typing.Optional[str]


# DataSourceSyncJobTypeDef

### ExecutionId
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest']]

### DataSourceErrorCode
- **Type**: typing.Optional[str]

### Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceSyncJobMetricsTypeDef]


# DataSourceToIndexFieldMappingTypeDef

### DataSourceFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DateFieldFormat
- **Type**: typing.Optional[str]


# DataSourceVpcConfigurationOutputTypeDef

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# DataSourceVpcConfigurationTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DataSourceVpcConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DatabaseConfigurationOutputTypeDef

### DatabaseEngineType
- **Type**: typing.Literal['RDS_AURORA_MYSQL', 'RDS_AURORA_POSTGRESQL', 'RDS_MYSQL', 'RDS_POSTGRESQL']
- **Required**: Yes

### ConnectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ConnectionConfigurationTypeDef'>
- **Required**: Yes

### ColumnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ColumnConfigurationOutputTypeDef'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef]

### AclConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AclConfigurationTypeDef]

### SqlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SqlConfigurationTypeDef]


# DatabaseConfigurationTypeDef

### DatabaseEngineType
- **Type**: typing.Literal['RDS_AURORA_MYSQL', 'RDS_AURORA_POSTGRESQL', 'RDS_MYSQL', 'RDS_POSTGRESQL']
- **Required**: Yes

### ConnectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ConnectionConfigurationTypeDef'>
- **Required**: Yes

### ColumnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ColumnConfigurationTypeDef'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]

### AclConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AclConfigurationTypeDef]

### SqlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SqlConfigurationTypeDef]


# DeleteAccessControlConfigurationRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperienceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFaqRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrincipalMappingRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]

### OrderingId
- **Type**: typing.Optional[int]


# DeleteQuerySuggestionsBlockListRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThesaurusRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessControlConfigurationRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessControlConfigurationResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### AccessControlList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.PrincipalTypeDef]
- **Required**: Yes

### HierarchicalAccessControlList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.HierarchicalPrincipalOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSourceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExperienceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExperienceResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.ExperienceEndpointTypeDef]
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ExperienceConfigurationOutputTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFaqRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFaqResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### S3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### FileFormat
- **Type**: typing.Literal['CSV', 'CSV_WITH_HEADER', 'JSON']
- **Required**: Yes

### LanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFeaturedResultsSetRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturedResultsSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFeaturedResultsSetResponseTypeDef

### FeaturedResultsSetId
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturedResultsSetName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### QueryTexts
- **Type**: typing.List[str]
- **Required**: Yes

### FeaturedDocumentsWithMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FeaturedDocumentWithMetadataTypeDef]
- **Required**: Yes

### FeaturedDocumentsMissing
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FeaturedDocumentMissingTypeDef]
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIndexRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIndexResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Edition
- **Type**: typing.Literal['DEVELOPER_EDITION', 'ENTERPRISE_EDITION', 'GEN_AI_ENTERPRISE_EDITION']
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerSideEncryptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ServerSideEncryptionConfigurationTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'SYSTEM_UPDATING', 'UPDATING']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DocumentMetadataConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentMetadataConfigurationOutputTypeDef]
- **Required**: Yes

### IndexStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.IndexStatisticsTypeDef'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityUnits
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.CapacityUnitsConfigurationTypeDef'>
- **Required**: Yes

### UserTokenConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.UserTokenConfigurationTypeDef]
- **Required**: Yes

### UserContextPolicy
- **Type**: typing.Literal['ATTRIBUTE_FILTER', 'USER_TOKEN']
- **Required**: Yes

### UserGroupResolutionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.UserGroupResolutionConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePrincipalMappingRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]


# DescribePrincipalMappingResponseTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupOrderingIdSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.GroupOrderingIdSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeQuerySuggestionsBlockListRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQuerySuggestionsBlockListResponseTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ACTIVE_BUT_UPDATE_FAILED', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes

### ItemCount
- **Type**: <class 'int'>
- **Required**: Yes

### FileSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeQuerySuggestionsConfigRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQuerySuggestionsConfigResponseTypeDef

### Mode
- **Type**: typing.Literal['ENABLED', 'LEARN_ONLY']
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'UPDATING']
- **Required**: Yes

### QueryLogLookBackWindowInDays
- **Type**: <class 'int'>
- **Required**: Yes

### IncludeQueriesWithoutUserInformation
- **Type**: <class 'bool'>
- **Required**: Yes

### MinimumNumberOfQueryingUsers
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumQueryCount
- **Type**: <class 'int'>
- **Required**: Yes

### LastSuggestionsBuildTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastClearTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TotalSuggestionsCount
- **Type**: <class 'int'>
- **Required**: Yes

### AttributeSuggestionsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.AttributeSuggestionsDescribeConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeThesaurusRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThesaurusResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'ACTIVE_BUT_UPDATE_FAILED', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes

### FileSizeBytes
- **Type**: <class 'int'>
- **Required**: Yes

### TermCount
- **Type**: <class 'int'>
- **Required**: Yes

### SynonymRuleCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateEntitiesFromExperienceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.EntityConfigurationTypeDef]
- **Required**: Yes


# DisassociateEntitiesFromExperienceResponseTypeDef

### FailedEntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FailedEntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociatePersonasFromEntitiesRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociatePersonasFromEntitiesResponseTypeDef

### FailedEntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FailedEntityTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DocumentAttributeConditionOutputTypeDef

### ConditionDocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'Exists', 'GreaterThan', 'GreaterThanOrEquals', 'LessThan', 'LessThanOrEquals', 'NotContains', 'NotEquals', 'NotExists']
- **Required**: Yes

### ConditionOnValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueOutputTypeDef]


# DocumentAttributeConditionTypeDef

### ConditionDocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'Exists', 'GreaterThan', 'GreaterThanOrEquals', 'LessThan', 'LessThanOrEquals', 'NotContains', 'NotEquals', 'NotExists']
- **Required**: Yes

### ConditionOnValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueTypeDef]


# DocumentAttributeOutputTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueOutputTypeDef'>
- **Required**: Yes


# DocumentAttributeTargetOutputTypeDef

### TargetDocumentAttributeKey
- **Type**: typing.Optional[str]

### TargetDocumentAttributeValueDeletion
- **Type**: typing.Optional[bool]

### TargetDocumentAttributeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueOutputTypeDef]


# DocumentAttributeTargetTypeDef

### TargetDocumentAttributeKey
- **Type**: typing.Optional[str]

### TargetDocumentAttributeValueDeletion
- **Type**: typing.Optional[bool]

### TargetDocumentAttributeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueTypeDef]


# DocumentAttributeTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueUnionTypeDef'>
- **Required**: Yes


# DocumentAttributeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentAttributeValueCountPairTypeDef

### DocumentAttributeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueOutputTypeDef]

### Count
- **Type**: typing.Optional[int]

### FacetResults
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# DocumentAttributeValueOutputTypeDef

### StringValue
- **Type**: typing.Optional[str]

### StringListValue
- **Type**: typing.Optional[typing.List[str]]

### LongValue
- **Type**: typing.Optional[int]

### DateValue
- **Type**: typing.Optional[datetime.datetime]


# DocumentAttributeValueTypeDef

### StringValue
- **Type**: typing.Optional[str]

### StringListValue
- **Type**: typing.Optional[typing.Sequence[str]]

### LongValue
- **Type**: typing.Optional[int]

### DateValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TimestampTypeDef]


# DocumentAttributeValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentInfoTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]]


# DocumentMetadataConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentMetadataConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentRelevanceConfigurationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Relevance
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.RelevanceUnionTypeDef'>
- **Required**: Yes


# DocumentTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### Blob
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.BlobTypeDef]

### S3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeUnionTypeDef]]

### AccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.PrincipalTypeDef]]

### HierarchicalAccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.HierarchicalPrincipalUnionTypeDef]]

### ContentType
- **Type**: typing.Optional[typing.Literal['CSV', 'HTML', 'JSON', 'MD', 'MS_EXCEL', 'MS_WORD', 'PDF', 'PLAIN_TEXT', 'PPT', 'RTF', 'XML', 'XSLT']]

### AccessControlConfigurationId
- **Type**: typing.Optional[str]


# DocumentsMetadataConfigurationTypeDef

### S3Prefix
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EntityConfigurationTypeDef

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# EntityDisplayDataTypeDef

### UserName
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### IdentifiedUserName
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]


# EntityPersonaConfigurationTypeDef

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Persona
- **Type**: typing.Literal['OWNER', 'VIEWER']
- **Required**: Yes


# ExpandConfigurationTypeDef

### MaxResultItemsToExpand
- **Type**: typing.Optional[int]

### MaxExpandedResultsPerItem
- **Type**: typing.Optional[int]


# ExpandedResultItemTypeDef

### Id
- **Type**: typing.Optional[str]

### DocumentId
- **Type**: typing.Optional[str]

### DocumentTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TextWithHighlightsTypeDef]

### DocumentExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TextWithHighlightsTypeDef]

### DocumentURI
- **Type**: typing.Optional[str]

### DocumentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeOutputTypeDef]]


# ExperienceConfigurationOutputTypeDef

### ContentSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ContentSourceConfigurationOutputTypeDef]

### UserIdentityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserIdentityConfigurationTypeDef]


# ExperienceConfigurationTypeDef

### ContentSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ContentSourceConfigurationTypeDef]

### UserIdentityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserIdentityConfigurationTypeDef]


# ExperienceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExperienceEndpointTypeDef

### EndpointType
- **Type**: typing.Optional[typing.Literal['HOME']]

### Endpoint
- **Type**: typing.Optional[str]


# ExperienceEntitiesSummaryTypeDef

### EntityId
- **Type**: typing.Optional[str]

### EntityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### DisplayData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.EntityDisplayDataTypeDef]


# ExperiencesSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.ExperienceEndpointTypeDef]]


# FacetResultTypeDef

### DocumentAttributeKey
- **Type**: typing.Optional[str]

### DocumentAttributeValueType
- **Type**: typing.Optional[typing.Literal['DATE_VALUE', 'LONG_VALUE', 'STRING_LIST_VALUE', 'STRING_VALUE']]

### DocumentAttributeValueCountPairs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueCountPairTypeDef]]


# FacetTypeDef

### DocumentAttributeKey
- **Type**: typing.Optional[str]

### Facets
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### MaxResults
- **Type**: typing.Optional[int]


# FailedEntityTypeDef

### EntityId
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FaqStatisticsTypeDef

### IndexedQuestionAnswersCount
- **Type**: <class 'int'>
- **Required**: Yes


# FaqSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### FileFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'CSV_WITH_HEADER', 'JSON']]

### LanguageCode
- **Type**: typing.Optional[str]


# FeaturedDocumentMissingTypeDef

### Id
- **Type**: typing.Optional[str]


# FeaturedDocumentTypeDef

### Id
- **Type**: typing.Optional[str]


# FeaturedDocumentWithMetadataTypeDef

### Id
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### URI
- **Type**: typing.Optional[str]


# FeaturedResultsItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FeaturedResultsSetSummaryTypeDef

### FeaturedResultsSetId
- **Type**: typing.Optional[str]

### FeaturedResultsSetName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LastUpdatedTimestamp
- **Type**: typing.Optional[int]

### CreationTimestamp
- **Type**: typing.Optional[int]


# FeaturedResultsSetTypeDef

### FeaturedResultsSetId
- **Type**: typing.Optional[str]

### FeaturedResultsSetName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### QueryTexts
- **Type**: typing.Optional[typing.List[str]]

### FeaturedDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.FeaturedDocumentTypeDef]]

### LastUpdatedTimestamp
- **Type**: typing.Optional[int]

### CreationTimestamp
- **Type**: typing.Optional[int]


# FsxConfigurationOutputTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemType
- **Type**: typing.Literal['WINDOWS']
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef'>
- **Required**: Yes

### SecretArn
- **Type**: typing.Optional[str]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# FsxConfigurationTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemType
- **Type**: typing.Literal['WINDOWS']
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef'>
- **Required**: Yes

### SecretArn
- **Type**: typing.Optional[str]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# GetQuerySuggestionsRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: <class 'str'>
- **Required**: Yes

### MaxSuggestionsCount
- **Type**: typing.Optional[int]

### SuggestionTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DOCUMENT_ATTRIBUTES', 'QUERY']]]

### AttributeSuggestionsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AttributeSuggestionsGetConfigTypeDef]


# GetQuerySuggestionsResponseTypeDef

### QuerySuggestionsId
- **Type**: <class 'str'>
- **Required**: Yes

### Suggestions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.SuggestionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSnapshotsRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Interval
- **Type**: typing.Literal['ONE_MONTH_AGO', 'ONE_WEEK_AGO', 'THIS_MONTH', 'THIS_WEEK', 'TWO_MONTHS_AGO', 'TWO_WEEKS_AGO']
- **Required**: Yes

### MetricType
- **Type**: typing.Literal['AGG_QUERY_DOC_METRICS', 'DOCS_BY_CLICK_COUNT', 'QUERIES_BY_COUNT', 'QUERIES_BY_ZERO_CLICK_RATE', 'QUERIES_BY_ZERO_RESULT_RATE', 'TREND_QUERY_DOC_METRICS']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# GetSnapshotsResponseTypeDef

### SnapShotTimeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.TimeRangeOutputTypeDef'>
- **Required**: Yes

### SnapshotsDataHeader
- **Type**: typing.List[str]
- **Required**: Yes

### SnapshotsData
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GitHubConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GitHubConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GitHubDocumentCrawlPropertiesTypeDef

### CrawlRepositoryDocuments
- **Type**: typing.Optional[bool]

### CrawlIssue
- **Type**: typing.Optional[bool]

### CrawlIssueComment
- **Type**: typing.Optional[bool]

### CrawlIssueCommentAttachment
- **Type**: typing.Optional[bool]

### CrawlPullRequest
- **Type**: typing.Optional[bool]

### CrawlPullRequestComment
- **Type**: typing.Optional[bool]

### CrawlPullRequestCommentAttachment
- **Type**: typing.Optional[bool]


# GoogleDriveConfigurationOutputTypeDef

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### ExcludeMimeTypes
- **Type**: typing.Optional[typing.List[str]]

### ExcludeUserAccounts
- **Type**: typing.Optional[typing.List[str]]

### ExcludeSharedDrives
- **Type**: typing.Optional[typing.List[str]]


# GoogleDriveConfigurationTypeDef

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### ExcludeMimeTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludeUserAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludeSharedDrives
- **Type**: typing.Optional[typing.Sequence[str]]


# GroupMembersTypeDef

### MemberGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.MemberGroupTypeDef]]

### MemberUsers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.MemberUserTypeDef]]

### S3PathforGroupMembers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]


# GroupOrderingIdSummaryTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DELETED', 'DELETING', 'FAILED', 'PROCESSING', 'SUCCEEDED']]

### LastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ReceivedAt
- **Type**: typing.Optional[datetime.datetime]

### OrderingId
- **Type**: typing.Optional[int]

### FailureReason
- **Type**: typing.Optional[str]


# GroupSummaryTypeDef

### GroupId
- **Type**: typing.Optional[str]

### OrderingId
- **Type**: typing.Optional[int]


# HierarchicalPrincipalOutputTypeDef

### PrincipalList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.PrincipalTypeDef]
- **Required**: Yes


# HierarchicalPrincipalTypeDef

### PrincipalList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.PrincipalTypeDef]
- **Required**: Yes


# HierarchicalPrincipalUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HookConfigurationOutputTypeDef

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeConditionOutputTypeDef]


# HookConfigurationTypeDef

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeConditionTypeDef]


# IndexConfigurationSummaryTypeDef

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'SYSTEM_UPDATING', 'UPDATING']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Edition
- **Type**: typing.Optional[typing.Literal['DEVELOPER_EDITION', 'ENTERPRISE_EDITION', 'GEN_AI_ENTERPRISE_EDITION']]


# IndexStatisticsTypeDef

### FaqStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.FaqStatisticsTypeDef'>
- **Required**: Yes

### TextDocumentStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.TextDocumentStatisticsTypeDef'>
- **Required**: Yes


# InlineCustomDocumentEnrichmentConfigurationOutputTypeDef

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeConditionOutputTypeDef]

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTargetOutputTypeDef]

### DocumentContentDeletion
- **Type**: typing.Optional[bool]


# InlineCustomDocumentEnrichmentConfigurationTypeDef

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeConditionTypeDef]

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTargetTypeDef]

### DocumentContentDeletion
- **Type**: typing.Optional[bool]


# JiraConfigurationOutputTypeDef

### JiraAccountUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### UseChangeLog
- **Type**: typing.Optional[bool]

### Project
- **Type**: typing.Optional[typing.List[str]]

### IssueType
- **Type**: typing.Optional[typing.List[str]]

### Status
- **Type**: typing.Optional[typing.List[str]]

### IssueSubEntityFilter
- **Type**: typing.Optional[typing.List[typing.Literal['ATTACHMENTS', 'COMMENTS', 'WORKLOGS']]]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### CommentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### IssueFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### ProjectFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### WorkLogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef]


# JiraConfigurationTypeDef

### JiraAccountUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### UseChangeLog
- **Type**: typing.Optional[bool]

### Project
- **Type**: typing.Optional[typing.Sequence[str]]

### IssueType
- **Type**: typing.Optional[typing.Sequence[str]]

### Status
- **Type**: typing.Optional[typing.Sequence[str]]

### IssueSubEntityFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ATTACHMENTS', 'COMMENTS', 'WORKLOGS']]]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### CommentFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### IssueFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### ProjectFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### WorkLogFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]


# JsonTokenTypeConfigurationTypeDef

### UserNameAttributeField
- **Type**: <class 'str'>
- **Required**: Yes

### GroupAttributeField
- **Type**: <class 'str'>
- **Required**: Yes


# JwtTokenTypeConfigurationTypeDef

### KeyLocation
- **Type**: typing.Literal['SECRET_MANAGER', 'URL']
- **Required**: Yes

### URL
- **Type**: typing.Optional[str]

### SecretManagerArn
- **Type**: typing.Optional[str]

### UserNameAttributeField
- **Type**: typing.Optional[str]

### GroupAttributeField
- **Type**: typing.Optional[str]

### Issuer
- **Type**: typing.Optional[str]

### ClaimRegex
- **Type**: typing.Optional[str]


# ListAccessControlConfigurationsRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessControlConfigurationsResponseTypeDef

### AccessControlConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.AccessControlConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSourceSyncJobsRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### StartTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TimeRangeUnionTypeDef]

### StatusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]


# ListDataSourceSyncJobsResponseTypeDef

### History
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceSyncJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataSourcesResponseTypeDef

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntityPersonasRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEntityPersonasResponseTypeDef

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.PersonasSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExperienceEntitiesRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExperienceEntitiesResponseTypeDef

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.ExperienceEntitiesSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExperiencesRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListExperiencesResponseTypeDef

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.ExperiencesSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFaqsRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFaqsResponseTypeDef

### FaqSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FaqSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFeaturedResultsSetsRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFeaturedResultsSetsResponseTypeDef

### FeaturedResultsSetSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FeaturedResultsSetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsOlderThanOrderingIdRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### OrderingId
- **Type**: <class 'int'>
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupsOlderThanOrderingIdResponseTypeDef

### GroupsSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.GroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndicesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIndicesResponseTypeDef

### IndexConfigurationSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.IndexConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQuerySuggestionsBlockListsRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQuerySuggestionsBlockListsResponseTypeDef

### BlockListSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.QuerySuggestionsBlockListSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListThesauriRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListThesauriResponseTypeDef

### ThesaurusSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.ThesaurusSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MemberGroupTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]


# MemberUserTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# OnPremiseConfigurationTypeDef

### HostUrl
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationName
- **Type**: <class 'str'>
- **Required**: Yes

### SslCertificateS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef'>
- **Required**: Yes


# OneDriveConfigurationOutputTypeDef

### TenantDomain
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### OneDriveUsers
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.OneDriveUsersOutputTypeDef'>
- **Required**: Yes

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### DisableLocalGroups
- **Type**: typing.Optional[bool]


# OneDriveConfigurationTypeDef

### TenantDomain
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### OneDriveUsers
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.OneDriveUsersTypeDef'>
- **Required**: Yes

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### DisableLocalGroups
- **Type**: typing.Optional[bool]


# OneDriveUsersOutputTypeDef

### OneDriveUserList
- **Type**: typing.Optional[typing.List[str]]

### OneDriveUserS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]


# OneDriveUsersTypeDef

### OneDriveUserList
- **Type**: typing.Optional[typing.Sequence[str]]

### OneDriveUserS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]


# PersonasSummaryTypeDef

### EntityId
- **Type**: typing.Optional[str]

### Persona
- **Type**: typing.Optional[typing.Literal['OWNER', 'VIEWER']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# PrincipalTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ProxyConfigurationTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Credentials
- **Type**: typing.Optional[str]


# PutPrincipalMappingRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupMembers
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.GroupMembersTypeDef'>
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]

### OrderingId
- **Type**: typing.Optional[int]

### RoleArn
- **Type**: typing.Optional[str]


# QueryRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: typing.Optional[str]

### AttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AttributeFilterTypeDef]

### Facets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.FacetTypeDef]]

### RequestedDocumentAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### QueryResultTypeFilter
- **Type**: typing.Optional[typing.Literal['ANSWER', 'DOCUMENT', 'QUESTION_ANSWER']]

### DocumentRelevanceOverrideConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentRelevanceConfigurationTypeDef]]

### PageNumber
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### SortingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SortingConfigurationTypeDef]

### SortingConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.SortingConfigurationTypeDef]]

### UserContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserContextTypeDef]

### VisitorId
- **Type**: typing.Optional[str]

### SpellCorrectionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SpellCorrectionConfigurationTypeDef]

### CollapseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CollapseConfigurationTypeDef]


# QueryResultItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryResultTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.QueryResultItemTypeDef]
- **Required**: Yes

### FacetResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FacetResultTypeDef]
- **Required**: Yes

### TotalNumberOfResults
- **Type**: <class 'int'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.WarningTypeDef]
- **Required**: Yes

### SpellCorrectedQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.SpellCorrectedQueryTypeDef]
- **Required**: Yes

### FeaturedResultsItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FeaturedResultsItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QuerySuggestionsBlockListSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ACTIVE_BUT_UPDATE_FAILED', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### ItemCount
- **Type**: typing.Optional[int]


# QuipConfigurationOutputTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlFileComments
- **Type**: typing.Optional[bool]

### CrawlChatRooms
- **Type**: typing.Optional[bool]

### CrawlAttachments
- **Type**: typing.Optional[bool]

### FolderIds
- **Type**: typing.Optional[typing.List[str]]

### ThreadFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### MessageFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef]


# QuipConfigurationTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlFileComments
- **Type**: typing.Optional[bool]

### CrawlChatRooms
- **Type**: typing.Optional[bool]

### CrawlAttachments
- **Type**: typing.Optional[bool]

### FolderIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ThreadFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### MessageFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]


# RelevanceFeedbackTypeDef

### ResultId
- **Type**: <class 'str'>
- **Required**: Yes

### RelevanceValue
- **Type**: typing.Literal['NOT_RELEVANT', 'RELEVANT']
- **Required**: Yes


# RelevanceOutputTypeDef

### Freshness
- **Type**: typing.Optional[bool]

### Importance
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[str]

### RankOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### ValueImportanceMap
- **Type**: typing.Optional[typing.Dict[str, int]]


# RelevanceTypeDef

### Freshness
- **Type**: typing.Optional[bool]

### Importance
- **Type**: typing.Optional[int]

### Duration
- **Type**: typing.Optional[str]

### RankOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### ValueImportanceMap
- **Type**: typing.Optional[typing.Mapping[str, int]]


# RelevanceUnionTypeDef

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


# RetrieveRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AttributeFilterTypeDef]

### RequestedDocumentAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### DocumentRelevanceOverrideConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentRelevanceConfigurationTypeDef]]

### PageNumber
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### UserContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserContextTypeDef]


# RetrieveResultItemTypeDef

### Id
- **Type**: typing.Optional[str]

### DocumentId
- **Type**: typing.Optional[str]

### DocumentTitle
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### DocumentURI
- **Type**: typing.Optional[str]

### DocumentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeOutputTypeDef]]

### ScoreAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ScoreAttributesTypeDef]


# RetrieveResultTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.RetrieveResultItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3DataSourceConfigurationOutputTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### InclusionPrefixes
- **Type**: typing.Optional[typing.List[str]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### DocumentsMetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentsMetadataConfigurationTypeDef]

### AccessControlListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AccessControlListConfigurationTypeDef]


# S3DataSourceConfigurationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### InclusionPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### DocumentsMetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentsMetadataConfigurationTypeDef]

### AccessControlListConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AccessControlListConfigurationTypeDef]


# S3PathTypeDef

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# SaaSConfigurationTypeDef

### OrganizationName
- **Type**: <class 'str'>
- **Required**: Yes

### HostUrl
- **Type**: <class 'str'>
- **Required**: Yes


# SalesforceChatterFeedConfigurationOutputTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### IncludeFilterTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE_USER', 'STANDARD_USER']]]


# SalesforceChatterFeedConfigurationTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### IncludeFilterTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE_USER', 'STANDARD_USER']]]


# SalesforceConfigurationOutputTypeDef

### ServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardObjectConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.SalesforceStandardObjectConfigurationOutputTypeDef]]

### KnowledgeArticleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceKnowledgeArticleConfigurationOutputTypeDef]

### ChatterFeedConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceChatterFeedConfigurationOutputTypeDef]

### CrawlAttachments
- **Type**: typing.Optional[bool]

### StandardObjectAttachmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceStandardObjectAttachmentConfigurationOutputTypeDef]

### IncludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExcludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]


# SalesforceConfigurationTypeDef

### ServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardObjectConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.SalesforceStandardObjectConfigurationTypeDef]]

### KnowledgeArticleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceKnowledgeArticleConfigurationTypeDef]

### ChatterFeedConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceChatterFeedConfigurationTypeDef]

### CrawlAttachments
- **Type**: typing.Optional[bool]

### StandardObjectAttachmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceStandardObjectAttachmentConfigurationTypeDef]

### IncludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.Sequence[str]]


# SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SalesforceKnowledgeArticleConfigurationOutputTypeDef

### IncludedStates
- **Type**: typing.List[typing.Literal['ARCHIVED', 'DRAFT', 'PUBLISHED']]
- **Required**: Yes

### StandardKnowledgeArticleTypeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef]

### CustomKnowledgeArticleTypeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.SalesforceCustomKnowledgeArticleTypeConfigurationOutputTypeDef]]


# SalesforceKnowledgeArticleConfigurationTypeDef

### IncludedStates
- **Type**: typing.Sequence[typing.Literal['ARCHIVED', 'DRAFT', 'PUBLISHED']]
- **Required**: Yes

### StandardKnowledgeArticleTypeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef]

### CustomKnowledgeArticleTypeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef]]


# SalesforceStandardKnowledgeArticleTypeConfigurationOutputTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SalesforceStandardObjectAttachmentConfigurationOutputTypeDef

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SalesforceStandardObjectAttachmentConfigurationTypeDef

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SalesforceStandardObjectConfigurationOutputTypeDef

### Name
- **Type**: typing.Literal['ACCOUNT', 'CAMPAIGN', 'CASE', 'CONTACT', 'CONTRACT', 'DOCUMENT', 'GROUP', 'IDEA', 'LEAD', 'OPPORTUNITY', 'PARTNER', 'PRICEBOOK', 'PRODUCT', 'PROFILE', 'SOLUTION', 'TASK', 'USER']
- **Required**: Yes

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SalesforceStandardObjectConfigurationTypeDef

### Name
- **Type**: typing.Literal['ACCOUNT', 'CAMPAIGN', 'CASE', 'CONTACT', 'CONTRACT', 'DOCUMENT', 'GROUP', 'IDEA', 'LEAD', 'OPPORTUNITY', 'PARTNER', 'PRICEBOOK', 'PRODUCT', 'PROFILE', 'SOLUTION', 'TASK', 'USER']
- **Required**: Yes

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# ScoreAttributesTypeDef

### ScoreConfidence
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NOT_AVAILABLE', 'VERY_HIGH']]


# SearchTypeDef

### Facetable
- **Type**: typing.Optional[bool]

### Searchable
- **Type**: typing.Optional[bool]

### Displayable
- **Type**: typing.Optional[bool]

### Sortable
- **Type**: typing.Optional[bool]


# SeedUrlConfigurationOutputTypeDef

### SeedUrls
- **Type**: typing.List[str]
- **Required**: Yes

### WebCrawlerMode
- **Type**: typing.Optional[typing.Literal['EVERYTHING', 'HOST_ONLY', 'SUBDOMAINS']]


# SeedUrlConfigurationTypeDef

### SeedUrls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### WebCrawlerMode
- **Type**: typing.Optional[typing.Literal['EVERYTHING', 'HOST_ONLY', 'SUBDOMAINS']]


# ServerSideEncryptionConfigurationTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]


# ServiceNowConfigurationOutputTypeDef

### HostUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNowBuildVersion
- **Type**: typing.Literal['LONDON', 'OTHERS']
- **Required**: Yes

### KnowledgeArticleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ServiceNowKnowledgeArticleConfigurationOutputTypeDef]

### ServiceCatalogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ServiceNowServiceCatalogConfigurationOutputTypeDef]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'OAUTH2']]


# ServiceNowConfigurationTypeDef

### HostUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNowBuildVersion
- **Type**: typing.Literal['LONDON', 'OTHERS']
- **Required**: Yes

### KnowledgeArticleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ServiceNowKnowledgeArticleConfigurationTypeDef]

### ServiceCatalogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ServiceNowServiceCatalogConfigurationTypeDef]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'OAUTH2']]


# ServiceNowKnowledgeArticleConfigurationOutputTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlAttachments
- **Type**: typing.Optional[bool]

### IncludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExcludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### FilterQuery
- **Type**: typing.Optional[str]


# ServiceNowKnowledgeArticleConfigurationTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlAttachments
- **Type**: typing.Optional[bool]

### IncludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### FilterQuery
- **Type**: typing.Optional[str]


# ServiceNowServiceCatalogConfigurationOutputTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlAttachments
- **Type**: typing.Optional[bool]

### IncludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExcludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# ServiceNowServiceCatalogConfigurationTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlAttachments
- **Type**: typing.Optional[bool]

### IncludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExcludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SharePointConfigurationOutputTypeDef

### SharePointVersion
- **Type**: typing.Literal['SHAREPOINT_2013', 'SHAREPOINT_2016', 'SHAREPOINT_2019', 'SHAREPOINT_ONLINE']
- **Required**: Yes

### Urls
- **Type**: typing.List[str]
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlAttachments
- **Type**: typing.Optional[bool]

### UseChangeLog
- **Type**: typing.Optional[bool]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### DisableLocalGroups
- **Type**: typing.Optional[bool]

### SslCertificateS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'OAUTH2']]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ProxyConfigurationTypeDef]


# SharePointConfigurationTypeDef

### SharePointVersion
- **Type**: typing.Literal['SHAREPOINT_2013', 'SHAREPOINT_2016', 'SHAREPOINT_2019', 'SHAREPOINT_ONLINE']
- **Required**: Yes

### Urls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlAttachments
- **Type**: typing.Optional[bool]

### UseChangeLog
- **Type**: typing.Optional[bool]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### DisableLocalGroups
- **Type**: typing.Optional[bool]

### SslCertificateS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'OAUTH2']]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ProxyConfigurationTypeDef]


# SiteMapsConfigurationOutputTypeDef

### SiteMaps
- **Type**: typing.List[str]
- **Required**: Yes


# SiteMapsConfigurationTypeDef

### SiteMaps
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SlackConfigurationOutputTypeDef

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SlackEntityList
- **Type**: typing.List[typing.Literal['DIRECT_MESSAGE', 'GROUP_MESSAGE', 'PRIVATE_CHANNEL', 'PUBLIC_CHANNEL']]
- **Required**: Yes

### SinceCrawlDate
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationOutputTypeDef]

### UseChangeLog
- **Type**: typing.Optional[bool]

### CrawlBotMessage
- **Type**: typing.Optional[bool]

### ExcludeArchived
- **Type**: typing.Optional[bool]

### LookBackPeriod
- **Type**: typing.Optional[int]

### PrivateChannelFilter
- **Type**: typing.Optional[typing.List[str]]

### PublicChannelFilter
- **Type**: typing.Optional[typing.List[str]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SlackConfigurationTypeDef

### TeamId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SlackEntityList
- **Type**: typing.Sequence[typing.Literal['DIRECT_MESSAGE', 'GROUP_MESSAGE', 'PRIVATE_CHANNEL', 'PUBLIC_CHANNEL']]
- **Required**: Yes

### SinceCrawlDate
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]

### UseChangeLog
- **Type**: typing.Optional[bool]

### CrawlBotMessage
- **Type**: typing.Optional[bool]

### ExcludeArchived
- **Type**: typing.Optional[bool]

### LookBackPeriod
- **Type**: typing.Optional[int]

### PrivateChannelFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### PublicChannelFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SortingConfigurationTypeDef

### DocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# SourceDocumentTypeDef

### DocumentId
- **Type**: typing.Optional[str]

### SuggestionAttributes
- **Type**: typing.Optional[typing.List[str]]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeOutputTypeDef]]


# SpellCorrectedQueryTypeDef

### SuggestedQueryText
- **Type**: typing.Optional[str]

### Corrections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.CorrectionTypeDef]]


# SpellCorrectionConfigurationTypeDef

### IncludeQuerySpellCheckSuggestions
- **Type**: <class 'bool'>
- **Required**: Yes


# SqlConfigurationTypeDef

### QueryIdentifiersEnclosingOption
- **Type**: typing.Optional[typing.Literal['DOUBLE_QUOTES', 'NONE']]


# StartDataSourceSyncJobRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDataSourceSyncJobResponseTypeDef

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StatusTypeDef

### DocumentId
- **Type**: typing.Optional[str]

### DocumentStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'INDEXED', 'NOT_FOUND', 'PROCESSING', 'UPDATED', 'UPDATE_FAILED']]

### FailureCode
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# StopDataSourceSyncJobRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitFeedbackRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ClickFeedbackItems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.ClickFeedbackTypeDef]]

### RelevanceFeedbackItems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.RelevanceFeedbackTypeDef]]


# SuggestableConfigTypeDef

### AttributeName
- **Type**: typing.Optional[str]

### Suggestable
- **Type**: typing.Optional[bool]


# SuggestionHighlightTypeDef

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]


# SuggestionTypeDef

### Id
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SuggestionValueTypeDef]

### SourceDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.SourceDocumentTypeDef]]


# SuggestionValueTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TableCellTypeDef

### Value
- **Type**: typing.Optional[str]

### TopAnswer
- **Type**: typing.Optional[bool]

### Highlighted
- **Type**: typing.Optional[bool]

### Header
- **Type**: typing.Optional[bool]


# TableExcerptTypeDef

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.TableRowTypeDef]]

### TotalNumberOfRows
- **Type**: typing.Optional[int]


# TableRowTypeDef

### Cells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.TableCellTypeDef]]


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TemplateConfigurationOutputTypeDef

### Template
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TemplateConfigurationTypeDef

### Template
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# TextDocumentStatisticsTypeDef

### IndexedTextDocumentsCount
- **Type**: <class 'int'>
- **Required**: Yes

### IndexedTextBytes
- **Type**: <class 'int'>
- **Required**: Yes


# TextWithHighlightsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThesaurusSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'ACTIVE_BUT_UPDATE_FAILED', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# TimeRangeOutputTypeDef

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# TimeRangeTypeDef

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TimestampTypeDef]


# TimeRangeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessControlConfigurationRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### AccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.PrincipalTypeDef]]

### HierarchicalAccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.HierarchicalPrincipalUnionTypeDef]]


# UpdateDataSourceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceConfigurationUnionTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationUnionTypeDef]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### CustomDocumentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CustomDocumentEnrichmentConfigurationUnionTypeDef]


# UpdateExperienceRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ExperienceConfigurationUnionTypeDef]

### Description
- **Type**: typing.Optional[str]


# UpdateFeaturedResultsSetRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturedResultsSetId
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturedResultsSetName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### QueryTexts
- **Type**: typing.Optional[typing.Sequence[str]]

### FeaturedDocuments
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.FeaturedDocumentTypeDef]]


# UpdateFeaturedResultsSetResponseTypeDef

### FeaturedResultsSet
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.FeaturedResultsSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIndexRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DocumentMetadataConfigurationUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentMetadataConfigurationUnionTypeDef]]

### CapacityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CapacityUnitsConfigurationTypeDef]

### UserTokenConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.UserTokenConfigurationTypeDef]]

### UserContextPolicy
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_FILTER', 'USER_TOKEN']]

### UserGroupResolutionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserGroupResolutionConfigurationTypeDef]


# UpdateQuerySuggestionsBlockListRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SourceS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateQuerySuggestionsConfigRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['ENABLED', 'LEARN_ONLY']]

### QueryLogLookBackWindowInDays
- **Type**: typing.Optional[int]

### IncludeQueriesWithoutUserInformation
- **Type**: typing.Optional[bool]

### MinimumNumberOfQueryingUsers
- **Type**: typing.Optional[int]

### MinimumQueryCount
- **Type**: typing.Optional[int]

### AttributeSuggestionsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AttributeSuggestionsUpdateConfigTypeDef]


# UpdateThesaurusRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### SourceS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]


# UrlsOutputTypeDef

### SeedUrlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SeedUrlConfigurationOutputTypeDef]

### SiteMapsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SiteMapsConfigurationOutputTypeDef]


# UrlsTypeDef

### SeedUrlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SeedUrlConfigurationTypeDef]

### SiteMapsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SiteMapsConfigurationTypeDef]


# UserContextTypeDef

### Token
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Groups
- **Type**: typing.Optional[typing.Sequence[str]]

### DataSourceGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceGroupTypeDef]]


# UserGroupResolutionConfigurationTypeDef

### UserGroupResolutionMode
- **Type**: typing.Literal['AWS_SSO', 'NONE']
- **Required**: Yes


# UserIdentityConfigurationTypeDef

### IdentityAttributeName
- **Type**: typing.Optional[str]


# UserTokenConfigurationTypeDef

### JwtTokenTypeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.JwtTokenTypeConfigurationTypeDef]

### JsonTokenTypeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.JsonTokenTypeConfigurationTypeDef]


# WarningTypeDef

### Message
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[typing.Literal['QUERY_LANGUAGE_INVALID_SYNTAX']]


# WebCrawlerConfigurationOutputTypeDef

### Urls
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.UrlsOutputTypeDef'>
- **Required**: Yes

### CrawlDepth
- **Type**: typing.Optional[int]

### MaxLinksPerPage
- **Type**: typing.Optional[int]

### MaxContentSizePerPageInMegaBytes
- **Type**: typing.Optional[float]

### MaxUrlsPerMinuteCrawlRate
- **Type**: typing.Optional[int]

### UrlInclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### UrlExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ProxyConfigurationTypeDef]

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AuthenticationConfigurationOutputTypeDef]


# WebCrawlerConfigurationTypeDef

### Urls
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.UrlsTypeDef'>
- **Required**: Yes

### CrawlDepth
- **Type**: typing.Optional[int]

### MaxLinksPerPage
- **Type**: typing.Optional[int]

### MaxContentSizePerPageInMegaBytes
- **Type**: typing.Optional[float]

### MaxUrlsPerMinuteCrawlRate
- **Type**: typing.Optional[int]

### UrlInclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### UrlExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ProxyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ProxyConfigurationTypeDef]

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.AuthenticationConfigurationTypeDef]


# WorkDocsConfigurationOutputTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlComments
- **Type**: typing.Optional[bool]

### UseChangeLog
- **Type**: typing.Optional[bool]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# WorkDocsConfigurationTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### CrawlComments
- **Type**: typing.Optional[bool]

### UseChangeLog
- **Type**: typing.Optional[bool]

### InclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]



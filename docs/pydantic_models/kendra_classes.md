# kendra_classes

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


# AssociateEntitiesToExperienceRequestRequestTypeDef

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


# AssociatePersonasToEntitiesRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### OrAllFilters
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### NotFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### EqualsTo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]

### ContainsAll
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]

### ContainsAny
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]

### GreaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]

### GreaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]

### LessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]

### LessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]


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


# BatchDeleteDocumentRequestRequestTypeDef

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


# BatchDeleteFeaturedResultsSetRequestRequestTypeDef

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


# BatchGetDocumentStatusRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentInfoList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentInfoTypeDef]
- **Required**: Yes


# BatchGetDocumentStatusResponseErrorTypeDef

### DocumentId
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


# BatchPutDocumentRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentTypeDef]
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### CustomDocumentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CustomDocumentEnrichmentConfigurationTypeDef]


# BatchPutDocumentResponseFailedDocumentTypeDef

### Id
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


# ClearQuerySuggestionsRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# ClickFeedbackTypeDef

### ResultId
- **Type**: <class 'str'>
- **Required**: Yes

### ClickTime
- **Type**: typing.Union[datetime.datetime, str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef'>
- **Required**: Yes

### ExpandedResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.ExpandedResultItemTypeDef]]


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


# CreateAccessControlConfigurationRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.HierarchicalPrincipalTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateAccessControlConfigurationResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ALFRESCO', 'BOX', 'CONFLUENCE', 'CUSTOM', 'DATABASE', 'FSX', 'GITHUB', 'GOOGLEDRIVE', 'JIRA', 'ONEDRIVE', 'QUIP', 'S3', 'SALESFORCE', 'SERVICENOW', 'SHAREPOINT', 'SLACK', 'TEMPLATE', 'WEBCRAWLER', 'WORKDOCS']
- **Required**: Yes

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceConfigurationTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.TagTypeDef]]

### ClientToken
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### CustomDocumentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CustomDocumentEnrichmentConfigurationTypeDef]


# CreateDataSourceResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExperienceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ExperienceConfigurationTypeDef]

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


# CreateFaqRequestRequestTypeDef

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


# CreateFeaturedResultsSetRequestRequestTypeDef

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


# CreateIndexRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Edition
- **Type**: typing.Optional[typing.Literal['DEVELOPER_EDITION', 'ENTERPRISE_EDITION']]

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


# CreateQuerySuggestionsBlockListRequestRequestTypeDef

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


# CreateThesaurusRequestRequestTypeDef

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


# CustomDocumentEnrichmentConfigurationTypeDef

### InlineConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.InlineCustomDocumentEnrichmentConfigurationTypeDef]]

### PreExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.HookConfigurationTypeDef]

### PostExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.HookConfigurationTypeDef]

### RoleArn
- **Type**: typing.Optional[str]


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


# DataSourceGroupTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DataSourceSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ALFRESCO', 'BOX', 'CONFLUENCE', 'CUSTOM', 'DATABASE', 'FSX', 'GITHUB', 'GOOGLEDRIVE', 'JIRA', 'ONEDRIVE', 'QUIP', 'S3', 'SALESFORCE', 'SERVICENOW', 'SHAREPOINT', 'SLACK', 'TEMPLATE', 'WEBCRAWLER', 'WORKDOCS']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### LanguageCode
- **Type**: typing.Optional[str]


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


# DataSourceVpcConfigurationTypeDef

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


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


# DeleteAccessControlConfigurationRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperienceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFaqRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrincipalMappingRequestRequestTypeDef

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


# DeleteQuerySuggestionsBlockListRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThesaurusRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessControlConfigurationRequestRequestTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.HierarchicalPrincipalTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDataSourceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSourceResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ALFRESCO', 'BOX', 'CONFLUENCE', 'CUSTOM', 'DATABASE', 'FSX', 'GITHUB', 'GOOGLEDRIVE', 'JIRA', 'ONEDRIVE', 'QUIP', 'S3', 'SALESFORCE', 'SERVICENOW', 'SHAREPOINT', 'SLACK', 'TEMPLATE', 'WEBCRAWLER', 'WORKDOCS']
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DataSourceConfigurationTypeDef'>
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef'>
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
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### Schedule
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDocumentEnrichmentConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.CustomDocumentEnrichmentConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExperienceRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ExperienceConfigurationTypeDef'>
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


# DescribeFaqRequestRequestTypeDef

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


# DescribeFeaturedResultsSetRequestRequestTypeDef

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


# DescribeIndexRequestRequestTypeDef

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
- **Type**: typing.Literal['DEVELOPER_EDITION', 'ENTERPRISE_EDITION']
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentMetadataConfigurationTypeDef]
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


# DescribePrincipalMappingRequestRequestTypeDef

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


# DescribeQuerySuggestionsBlockListRequestRequestTypeDef

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


# DescribeQuerySuggestionsConfigRequestRequestTypeDef

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


# DescribeThesaurusRequestRequestTypeDef

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


# DisassociateEntitiesFromExperienceRequestRequestTypeDef

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


# DisassociatePersonasFromEntitiesRequestRequestTypeDef

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


# DocumentAttributeConditionTypeDef

### ConditionDocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'Exists', 'GreaterThan', 'GreaterThanOrEquals', 'LessThan', 'LessThanOrEquals', 'NotContains', 'NotEquals', 'NotExists']
- **Required**: Yes

### ConditionOnValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueTypeDef'>
- **Required**: Yes


# DocumentAttributeValueCountPairTypeDef

### DocumentAttributeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeValueTypeDef]

### Count
- **Type**: typing.Optional[int]

### FacetResults
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# DocumentAttributeValueTypeDef

### StringValue
- **Type**: typing.Optional[str]

### StringListValue
- **Type**: typing.Optional[typing.Sequence[str]]

### LongValue
- **Type**: typing.Optional[int]

### DateValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DocumentInfoTypeDef

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]]


# DocumentMetadataConfigurationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['DATE_VALUE', 'LONG_VALUE', 'STRING_LIST_VALUE', 'STRING_VALUE']
- **Required**: Yes

### Relevance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.RelevanceTypeDef]

### Search
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SearchTypeDef]


# DocumentRelevanceConfigurationTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Relevance
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.RelevanceTypeDef'>
- **Required**: Yes


# DocumentTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### Blob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### S3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.S3PathTypeDef]

### Attributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]]

### AccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.PrincipalTypeDef]]

### HierarchicalAccessControlList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.HierarchicalPrincipalTypeDef]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]]


# ExperienceConfigurationTypeDef

### ContentSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ContentSourceConfigurationTypeDef]

### UserIdentityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserIdentityConfigurationTypeDef]


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
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

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

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ANSWER', 'DOCUMENT', 'QUESTION_ANSWER']]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.AdditionalResultAttributeTypeDef]]

### DocumentId
- **Type**: typing.Optional[str]

### DocumentTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TextWithHighlightsTypeDef]

### DocumentExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TextWithHighlightsTypeDef]

### DocumentURI
- **Type**: typing.Optional[str]

### DocumentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]]

### FeedbackToken
- **Type**: typing.Optional[str]


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


# GetQuerySuggestionsRequestRequestTypeDef

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


# GetSnapshotsRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.TimeRangeTypeDef'>
- **Required**: Yes

### SnapshotsDataHeader
- **Type**: typing.List[str]
- **Required**: Yes

### SnapshotsData
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GitHubConfigurationTypeDef

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SaaSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SaaSConfigurationTypeDef]

### OnPremiseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.OnPremiseConfigurationTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['ON_PREMISE', 'SAAS']]

### UseChangeLog
- **Type**: typing.Optional[bool]

### GitHubDocumentCrawlProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.GitHubDocumentCrawlPropertiesTypeDef]

### RepositoryFilter
- **Type**: typing.Optional[typing.Sequence[str]]

### InclusionFolderNamePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### InclusionFileTypePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### InclusionFileNamePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionFolderNamePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionFileTypePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### ExclusionFileNamePatterns
- **Type**: typing.Optional[typing.Sequence[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]

### GitHubRepositoryConfigurationFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### GitHubCommitConfigurationFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### GitHubIssueDocumentConfigurationFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### GitHubIssueCommentConfigurationFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### GitHubIssueAttachmentConfigurationFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### GitHubPullRequestCommentConfigurationFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### GitHubPullRequestDocumentConfigurationFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]

### GitHubPullRequestDocumentAttachmentConfigurationFieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


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


# HierarchicalPrincipalTypeDef

### PrincipalList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.PrincipalTypeDef]
- **Required**: Yes


# HighlightTypeDef

### BeginOffset
- **Type**: <class 'int'>
- **Required**: Yes

### EndOffset
- **Type**: <class 'int'>
- **Required**: Yes

### TopAnswer
- **Type**: typing.Optional[bool]

### Type
- **Type**: typing.Optional[typing.Literal['STANDARD', 'THESAURUS_SYNONYM']]


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
- **Type**: typing.Optional[typing.Literal['DEVELOPER_EDITION', 'ENTERPRISE_EDITION']]


# IndexStatisticsTypeDef

### FaqStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.FaqStatisticsTypeDef'>
- **Required**: Yes

### TextDocumentStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.TextDocumentStatisticsTypeDef'>
- **Required**: Yes


# InlineCustomDocumentEnrichmentConfigurationTypeDef

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeConditionTypeDef]

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTargetTypeDef]

### DocumentContentDeletion
- **Type**: typing.Optional[bool]


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


# ListAccessControlConfigurationsRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessControlConfigurationsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### AccessControlConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.AccessControlConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourceSyncJobsRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TimeRangeTypeDef]

### StatusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]


# ListDataSourceSyncJobsResponseTypeDef

### History
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.DataSourceSyncJobTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourcesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEntityPersonasRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExperienceEntitiesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExperiencesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFaqsRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFaqsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### FaqSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.FaqSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFeaturedResultsSetsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupsOlderThanOrderingIdRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIndicesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIndicesResponseTypeDef

### IndexConfigurationSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.IndexConfigurationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQuerySuggestionsBlockListsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListThesauriRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListThesauriResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ThesaurusSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra_classes.ThesaurusSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### Access
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]


# ProxyConfigurationTypeDef

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Credentials
- **Type**: typing.Optional[str]


# PutPrincipalMappingRequestRequestTypeDef

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


# QueryRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: typing.Optional[str]

### AttributeFilter
- **Type**: typing.Optional[ForwardRef('AttributeFilterTypeDef')]

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

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ANSWER', 'DOCUMENT', 'QUESTION_ANSWER']]

### Format
- **Type**: typing.Optional[typing.Literal['TABLE', 'TEXT']]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.AdditionalResultAttributeTypeDef]]

### DocumentId
- **Type**: typing.Optional[str]

### DocumentTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TextWithHighlightsTypeDef]

### DocumentExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TextWithHighlightsTypeDef]

### DocumentURI
- **Type**: typing.Optional[str]

### DocumentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]]

### ScoreAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ScoreAttributesTypeDef]

### FeedbackToken
- **Type**: typing.Optional[str]

### TableExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.TableExcerptTypeDef]

### CollapsedResultDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CollapsedResultDetailTypeDef]


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
- **Type**: typing.Optional[typing.Dict[str, int]]


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


# RetrieveRequestRequestTypeDef

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeFilter
- **Type**: typing.Optional[ForwardRef('AttributeFilterTypeDef')]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]]

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


# SalesforceKnowledgeArticleConfigurationTypeDef

### IncludedStates
- **Type**: typing.Sequence[typing.Literal['ARCHIVED', 'DRAFT', 'PUBLISHED']]
- **Required**: Yes

### StandardKnowledgeArticleTypeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef]

### CustomKnowledgeArticleTypeConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef]]


# SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


# SalesforceStandardObjectAttachmentConfigurationTypeDef

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DataSourceToIndexFieldMappingTypeDef]]


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


# SeedUrlConfigurationTypeDef

### SeedUrls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### WebCrawlerMode
- **Type**: typing.Optional[typing.Literal['EVERYTHING', 'HOST_ONLY', 'SUBDOMAINS']]


# ServerSideEncryptionConfigurationTypeDef

### KmsKeyId
- **Type**: typing.Optional[str]


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


# SiteMapsConfigurationTypeDef

### SiteMaps
- **Type**: typing.Sequence[str]
- **Required**: Yes


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.DocumentAttributeTypeDef]]


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


# StartDataSourceSyncJobRequestRequestTypeDef

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


# StopDataSourceSyncJobRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitFeedbackRequestRequestTypeDef

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


# SuggestionTextWithHighlightsTypeDef

### Text
- **Type**: typing.Optional[str]

### Highlights
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.SuggestionHighlightTypeDef]]


# SuggestionTypeDef

### Id
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SuggestionValueTypeDef]

### SourceDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.SourceDocumentTypeDef]]


# SuggestionValueTypeDef

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.SuggestionTextWithHighlightsTypeDef]


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


# TagResourceRequestRequestTypeDef

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

### Text
- **Type**: typing.Optional[str]

### Highlights
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra_classes.HighlightTypeDef]]


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


# TimeRangeTypeDef

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessControlConfigurationRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.HierarchicalPrincipalTypeDef]]


# UpdateDataSourceRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceConfigurationTypeDef]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.DataSourceVpcConfigurationTypeDef]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### CustomDocumentEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CustomDocumentEnrichmentConfigurationTypeDef]


# UpdateExperienceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.ExperienceConfigurationTypeDef]

### Description
- **Type**: typing.Optional[str]


# UpdateFeaturedResultsSetRequestRequestTypeDef

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


# UpdateIndexRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.DocumentMetadataConfigurationTypeDef]]

### CapacityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.CapacityUnitsConfigurationTypeDef]

### UserTokenConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kendra_classes.UserTokenConfigurationTypeDef]]

### UserContextPolicy
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_FILTER', 'USER_TOKEN']]

### UserGroupResolutionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra_classes.UserGroupResolutionConfigurationTypeDef]


# UpdateQuerySuggestionsBlockListRequestRequestTypeDef

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


# UpdateQuerySuggestionsConfigRequestRequestTypeDef

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


# UpdateThesaurusRequestRequestTypeDef

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



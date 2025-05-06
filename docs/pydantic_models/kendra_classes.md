# Kendra Classes

# AccessControlConfigurationSummary

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# AccessControlListConfiguration

### KeyPath
- **Type**: typing.Optional[str]


# AclConfiguration

### AllowedGroupsColumnName
- **Type**: <class 'str'>
- **Required**: Yes


# AdditionalResultAttribute

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### ValueType
- **Type**: typing.Literal['TEXT_WITH_HIGHLIGHTS_VALUE']
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.AdditionalResultAttributeValue'>
- **Required**: Yes


# AdditionalResultAttributeValue

### TextWithHighlightsValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.TextWithHighlights]


# AlfrescoConfiguration

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
- **Required**: Yes

### CrawlSystemFolders
- **Type**: typing.Optional[bool]

### CrawlComments
- **Type**: typing.Optional[bool]

### EntityFilter
- **Type**: typing.Optional[typing.List[typing.Literal['blog', 'documentLibrary', 'wiki']]]

### DocumentLibraryFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### BlogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### WikiFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]


# AlfrescoConfigurationOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
- **Required**: Yes

### CrawlSystemFolders
- **Type**: typing.Optional[bool]

### CrawlComments
- **Type**: typing.Optional[bool]

### EntityFilter
- **Type**: typing.Optional[typing.List[typing.Literal['blog', 'documentLibrary', 'wiki']]]

### DocumentLibraryFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### BlogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### WikiFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]


# AssociateEntitiesToExperienceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.EntityConfiguration]
- **Required**: Yes


# AssociateEntitiesToExperienceResponse

### FailedEntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FailedEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatePersonasToEntitiesRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Personas
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.EntityPersonaConfiguration]
- **Required**: Yes


# AssociatePersonasToEntitiesResponse

### FailedEntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FailedEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# AttributeFilter

### AndAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### OrAllFilters
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### NotFilter
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### EqualsTo
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput, NoneType]

### ContainsAll
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput, NoneType]

### ContainsAny
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput, NoneType]

### GreaterThan
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput, NoneType]

### GreaterThanOrEquals
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput, NoneType]

### LessThan
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput, NoneType]

### LessThanOrEquals
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput, NoneType]


# AttributeSuggestionsDescribeConfig

### SuggestableConfigList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SuggestableConfig]]

### AttributeSuggestionsMode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# AttributeSuggestionsGetConfig

### SuggestionAttributes
- **Type**: typing.Optional[typing.List[str]]

### AdditionalResponseAttributes
- **Type**: typing.Optional[typing.List[str]]

### AttributeFilter
- **Type**: <class 'NoneType'>

### UserContext
- **Type**: <class 'NoneType'>


# AttributeSuggestionsUpdateConfig

### SuggestableConfigList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SuggestableConfig]]

### AttributeSuggestionsMode
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]


# AuthenticationConfiguration

### BasicAuthentication
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.BasicAuthenticationConfiguration]]


# AuthenticationConfigurationOutput

### BasicAuthentication
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.BasicAuthenticationConfiguration]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BasicAuthenticationConfiguration

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Credentials
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteDocumentRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentIdList
- **Type**: typing.List[str]
- **Required**: Yes

### DataSourceSyncJobMetricTarget
- **Type**: <class 'NoneType'>


# BatchDeleteDocumentResponse

### FailedDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.BatchDeleteDocumentResponseFailedDocument]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteDocumentResponseFailedDocument

### Id
- **Type**: typing.Optional[str]

### DataSourceId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest']]

### ErrorMessage
- **Type**: typing.Optional[str]


# BatchDeleteFeaturedResultsSetError

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorCode
- **Type**: typing.Literal['InternalError', 'InvalidRequest']
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes


# BatchDeleteFeaturedResultsSetRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturedResultsSetIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeleteFeaturedResultsSetResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.BatchDeleteFeaturedResultsSetError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDocumentStatusRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentInfo]
- **Required**: Yes


# BatchGetDocumentStatusResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.BatchGetDocumentStatusResponseError]
- **Required**: Yes

### DocumentStatusList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Status]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetDocumentStatusResponseError

### DocumentId
- **Type**: typing.Optional[str]

### DataSourceId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest']]

### ErrorMessage
- **Type**: typing.Optional[str]


# BatchPutDocumentRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Documents
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Document]
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### CustomDocumentEnrichmentConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.CustomDocumentEnrichmentConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.CustomDocumentEnrichmentConfigurationOutput, NoneType]


# BatchPutDocumentResponse

### FailedDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.BatchPutDocumentResponseFailedDocument]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# BatchPutDocumentResponseFailedDocument

### Id
- **Type**: typing.Optional[str]

### DataSourceId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['InternalError', 'InvalidRequest']]

### ErrorMessage
- **Type**: typing.Optional[str]


# BoxConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### TaskFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### CommentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### WebLinkFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]


# BoxConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### TaskFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### CommentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### WebLinkFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]


# CapacityUnitsConfiguration

### StorageCapacityUnits
- **Type**: <class 'int'>
- **Required**: Yes

### QueryCapacityUnits
- **Type**: <class 'int'>
- **Required**: Yes


# ClearQuerySuggestionsRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# ClickFeedback

### ResultId
- **Type**: <class 'str'>
- **Required**: Yes

### ClickTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# CollapseConfiguration

### DocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### SortingConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SortingConfiguration]]

### MissingAttributeKeyStrategy
- **Type**: typing.Optional[typing.Literal['COLLAPSE', 'EXPAND', 'IGNORE']]

### Expand
- **Type**: typing.Optional[bool]

### ExpandConfiguration
- **Type**: <class 'NoneType'>


# CollapsedResultDetail

### DocumentAttribute
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput'>
- **Required**: Yes

### ExpandedResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ExpandedResultItem]]


# ColumnConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# ColumnConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# ConfluenceAttachmentConfiguration

### CrawlAttachments
- **Type**: typing.Optional[bool]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceAttachmentToIndexFieldMapping]]


# ConfluenceAttachmentConfigurationOutput

### CrawlAttachments
- **Type**: typing.Optional[bool]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceAttachmentToIndexFieldMapping]]


# ConfluenceAttachmentToIndexFieldMapping

### DataSourceFieldName
- **Type**: typing.Optional[typing.Literal['AUTHOR', 'CONTENT_TYPE', 'CREATED_DATE', 'DISPLAY_URL', 'FILE_SIZE', 'ITEM_TYPE', 'PARENT_ID', 'SPACE_KEY', 'SPACE_NAME', 'URL', 'VERSION']]

### DateFieldFormat
- **Type**: typing.Optional[str]

### IndexFieldName
- **Type**: typing.Optional[str]


# ConfluenceBlogConfiguration

### BlogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceBlogToIndexFieldMapping]]


# ConfluenceBlogConfigurationOutput

### BlogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceBlogToIndexFieldMapping]]


# ConfluenceBlogToIndexFieldMapping

### DataSourceFieldName
- **Type**: typing.Optional[typing.Literal['AUTHOR', 'DISPLAY_URL', 'ITEM_TYPE', 'LABELS', 'PUBLISH_DATE', 'SPACE_KEY', 'SPACE_NAME', 'URL', 'VERSION']]

### DateFieldFormat
- **Type**: typing.Optional[str]

### IndexFieldName
- **Type**: typing.Optional[str]


# ConfluenceConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceSpaceConfiguration]

### PageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluencePageConfiguration]

### BlogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceBlogConfiguration]

### AttachmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceAttachmentConfiguration]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ProxyConfiguration
- **Type**: <class 'NoneType'>

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'PAT']]


# ConfluenceConfigurationOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceSpaceConfigurationOutput]

### PageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluencePageConfigurationOutput]

### BlogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceBlogConfigurationOutput]

### AttachmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceAttachmentConfigurationOutput]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ProxyConfiguration
- **Type**: <class 'NoneType'>

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'PAT']]


# ConfluencePageConfiguration

### PageFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluencePageToIndexFieldMapping]]


# ConfluencePageConfigurationOutput

### PageFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluencePageToIndexFieldMapping]]


# ConfluencePageToIndexFieldMapping

### DataSourceFieldName
- **Type**: typing.Optional[typing.Literal['AUTHOR', 'CONTENT_STATUS', 'CREATED_DATE', 'DISPLAY_URL', 'ITEM_TYPE', 'LABELS', 'MODIFIED_DATE', 'PARENT_ID', 'SPACE_KEY', 'SPACE_NAME', 'URL', 'VERSION']]

### DateFieldFormat
- **Type**: typing.Optional[str]

### IndexFieldName
- **Type**: typing.Optional[str]


# ConfluenceSpaceConfiguration

### CrawlPersonalSpaces
- **Type**: typing.Optional[bool]

### CrawlArchivedSpaces
- **Type**: typing.Optional[bool]

### IncludeSpaces
- **Type**: typing.Optional[typing.List[str]]

### ExcludeSpaces
- **Type**: typing.Optional[typing.List[str]]

### SpaceFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceSpaceToIndexFieldMapping]]


# ConfluenceSpaceConfigurationOutput

### CrawlPersonalSpaces
- **Type**: typing.Optional[bool]

### CrawlArchivedSpaces
- **Type**: typing.Optional[bool]

### IncludeSpaces
- **Type**: typing.Optional[typing.List[str]]

### ExcludeSpaces
- **Type**: typing.Optional[typing.List[str]]

### SpaceFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceSpaceToIndexFieldMapping]]


# ConfluenceSpaceToIndexFieldMapping

### DataSourceFieldName
- **Type**: typing.Optional[typing.Literal['DISPLAY_URL', 'ITEM_TYPE', 'SPACE_KEY', 'URL']]

### DateFieldFormat
- **Type**: typing.Optional[str]

### IndexFieldName
- **Type**: typing.Optional[str]


# ConnectionConfiguration

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


# ContentSourceConfiguration

### DataSourceIds
- **Type**: typing.Optional[typing.List[str]]

### FaqIds
- **Type**: typing.Optional[typing.List[str]]

### DirectPutContent
- **Type**: typing.Optional[bool]


# ContentSourceConfigurationOutput

### DataSourceIds
- **Type**: typing.Optional[typing.List[str]]

### FaqIds
- **Type**: typing.Optional[typing.List[str]]

### DirectPutContent
- **Type**: typing.Optional[bool]


# Correction

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]

### Term
- **Type**: typing.Optional[str]

### CorrectedTerm
- **Type**: typing.Optional[str]


# CreateAccessControlConfigurationRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AccessControlList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Principal]]

### HierarchicalAccessControlList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.HierarchicalPrincipal, aws_resource_validator.pydantic_models.kendra.kendra_classes.HierarchicalPrincipalOutput]]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateAccessControlConfigurationResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceConfigurationOutput, NoneType]

### VpcConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### CustomDocumentEnrichmentConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.CustomDocumentEnrichmentConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.CustomDocumentEnrichmentConfigurationOutput, NoneType]


# CreateDataSourceResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExperienceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperienceConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperienceConfigurationOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]


# CreateExperienceResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFaqRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### S3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Tag]]

### FileFormat
- **Type**: typing.Optional[typing.Literal['CSV', 'CSV_WITH_HEADER', 'JSON']]

### ClientToken
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]


# CreateFaqResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFeaturedResultsSetRequest

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
- **Type**: typing.Optional[typing.List[str]]

### FeaturedDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedDocument]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Tag]]


# CreateFeaturedResultsSetResponse

### FeaturedResultsSet
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedResultsSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIndexRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Edition
- **Type**: typing.Optional[typing.Literal['DEVELOPER_EDITION', 'ENTERPRISE_EDITION', 'GEN_AI_ENTERPRISE_EDITION']]

### ServerSideEncryptionConfiguration
- **Type**: <class 'NoneType'>

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Tag]]

### UserTokenConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.UserTokenConfiguration]]

### UserContextPolicy
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_FILTER', 'USER_TOKEN']]

### UserGroupResolutionConfiguration
- **Type**: <class 'NoneType'>


# CreateIndexResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQuerySuggestionsBlockListRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Tag]]


# CreateQuerySuggestionsBlockListResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# CreateThesaurusRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Tag]]

### ClientToken
- **Type**: typing.Optional[str]


# CreateThesaurusResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# CustomDocumentEnrichmentConfiguration

### InlineConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.InlineCustomDocumentEnrichmentConfiguration]]

### PreExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.HookConfiguration]

### PostExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.HookConfiguration]

### RoleArn
- **Type**: typing.Optional[str]


# CustomDocumentEnrichmentConfigurationOutput

### InlineConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.InlineCustomDocumentEnrichmentConfigurationOutput]]

### PreExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.HookConfigurationOutput]

### PostExtractionHookConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.HookConfigurationOutput]

### RoleArn
- **Type**: typing.Optional[str]


# DataSourceConfiguration

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3DataSourceConfiguration]

### SharePointConfiguration
- **Type**: <class 'NoneType'>

### DatabaseConfiguration
- **Type**: <class 'NoneType'>

### SalesforceConfiguration
- **Type**: <class 'NoneType'>

### OneDriveConfiguration
- **Type**: <class 'NoneType'>

### ServiceNowConfiguration
- **Type**: <class 'NoneType'>

### ConfluenceConfiguration
- **Type**: <class 'NoneType'>

### GoogleDriveConfiguration
- **Type**: <class 'NoneType'>

### WebCrawlerConfiguration
- **Type**: <class 'NoneType'>

### WorkDocsConfiguration
- **Type**: <class 'NoneType'>

### FsxConfiguration
- **Type**: <class 'NoneType'>

### SlackConfiguration
- **Type**: <class 'NoneType'>

### BoxConfiguration
- **Type**: <class 'NoneType'>

### QuipConfiguration
- **Type**: <class 'NoneType'>

### JiraConfiguration
- **Type**: <class 'NoneType'>

### GitHubConfiguration
- **Type**: <class 'NoneType'>

### AlfrescoConfiguration
- **Type**: <class 'NoneType'>

### TemplateConfiguration
- **Type**: <class 'NoneType'>


# DataSourceConfigurationOutput

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3DataSourceConfigurationOutput]

### SharePointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SharePointConfigurationOutput]

### DatabaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DatabaseConfigurationOutput]

### SalesforceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceConfigurationOutput]

### OneDriveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.OneDriveConfigurationOutput]

### ServiceNowConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ServiceNowConfigurationOutput]

### ConfluenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ConfluenceConfigurationOutput]

### GoogleDriveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.GoogleDriveConfigurationOutput]

### WebCrawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.WebCrawlerConfigurationOutput]

### WorkDocsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.WorkDocsConfigurationOutput]

### FsxConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.FsxConfigurationOutput]

### SlackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SlackConfigurationOutput]

### BoxConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.BoxConfigurationOutput]

### QuipConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.QuipConfigurationOutput]

### JiraConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.JiraConfigurationOutput]

### GitHubConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.GitHubConfigurationOutput]

### AlfrescoConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.AlfrescoConfigurationOutput]

### TemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.TemplateConfigurationOutput]


# DataSourceGroup

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DataSourceSummary

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


# DataSourceSyncJob

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceSyncJobMetrics]


# DataSourceSyncJobMetricTarget

### DataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceSyncJobId
- **Type**: typing.Optional[str]


# DataSourceSyncJobMetrics

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


# DataSourceToIndexFieldMapping

### DataSourceFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### IndexFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DateFieldFormat
- **Type**: typing.Optional[str]


# DataSourceVpcConfiguration

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# DataSourceVpcConfigurationOutput

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes


# DatabaseConfiguration

### DatabaseEngineType
- **Type**: typing.Literal['RDS_AURORA_MYSQL', 'RDS_AURORA_POSTGRESQL', 'RDS_MYSQL', 'RDS_POSTGRESQL']
- **Required**: Yes

### ConnectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ConnectionConfiguration'>
- **Required**: Yes

### ColumnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ColumnConfiguration'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]

### AclConfiguration
- **Type**: <class 'NoneType'>

### SqlConfiguration
- **Type**: <class 'NoneType'>


# DatabaseConfigurationOutput

### DatabaseEngineType
- **Type**: typing.Literal['RDS_AURORA_MYSQL', 'RDS_AURORA_POSTGRESQL', 'RDS_MYSQL', 'RDS_POSTGRESQL']
- **Required**: Yes

### ConnectionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ConnectionConfiguration'>
- **Required**: Yes

### ColumnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ColumnConfigurationOutput'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]

### AclConfiguration
- **Type**: <class 'NoneType'>

### SqlConfiguration
- **Type**: <class 'NoneType'>


# DeleteAccessControlConfigurationRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperienceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFaqRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIndexRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrincipalMappingRequest

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


# DeleteQuerySuggestionsBlockListRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteThesaurusRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessControlConfigurationRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccessControlConfigurationResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Principal]
- **Required**: Yes

### HierarchicalAccessControlList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.HierarchicalPrincipalOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDataSourceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDataSourceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceConfigurationOutput'>
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.CustomDocumentEnrichmentConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeExperienceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExperienceResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperienceEndpoint]
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperienceConfigurationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFaqRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFaqResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFeaturedResultsSetRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### FeaturedResultsSetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFeaturedResultsSetResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedDocumentWithMetadata]
- **Required**: Yes

### FeaturedDocumentsMissing
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedDocumentMissing]
- **Required**: Yes

### LastUpdatedTimestamp
- **Type**: <class 'int'>
- **Required**: Yes

### CreationTimestamp
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIndexRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIndexResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ServerSideEncryptionConfiguration'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentMetadataConfigurationOutput]
- **Required**: Yes

### IndexStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.IndexStatistics'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityUnits
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.CapacityUnitsConfiguration'>
- **Required**: Yes

### UserTokenConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.UserTokenConfiguration]
- **Required**: Yes

### UserContextPolicy
- **Type**: typing.Literal['ATTRIBUTE_FILTER', 'USER_TOKEN']
- **Required**: Yes

### UserGroupResolutionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.UserGroupResolutionConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePrincipalMappingRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]


# DescribePrincipalMappingResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.GroupOrderingIdSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeQuerySuggestionsBlockListRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQuerySuggestionsBlockListResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeQuerySuggestionsConfigRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeQuerySuggestionsConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.AttributeSuggestionsDescribeConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeThesaurusRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeThesaurusResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateEntitiesFromExperienceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.EntityConfiguration]
- **Required**: Yes


# DisassociateEntitiesFromExperienceResponse

### FailedEntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FailedEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociatePersonasFromEntitiesRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityIds
- **Type**: typing.List[str]
- **Required**: Yes


# DisassociatePersonasFromEntitiesResponse

### FailedEntityList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FailedEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# Document

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Title
- **Type**: typing.Optional[str]

### Blob
- **Type**: <class 'NoneType'>

### S3Path
- **Type**: <class 'NoneType'>

### Attributes
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput]]]

### AccessControlList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Principal]]

### HierarchicalAccessControlList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.HierarchicalPrincipal, aws_resource_validator.pydantic_models.kendra.kendra_classes.HierarchicalPrincipalOutput]]]

### ContentType
- **Type**: typing.Optional[typing.Literal['CSV', 'HTML', 'JSON', 'MD', 'MS_EXCEL', 'MS_WORD', 'PDF', 'PLAIN_TEXT', 'PPT', 'RTF', 'XML', 'XSLT']]

### AccessControlConfigurationId
- **Type**: typing.Optional[str]


# DocumentAttribute

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValue, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValueOutput]
- **Required**: Yes


# DocumentAttributeCondition

### ConditionDocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'Exists', 'GreaterThan', 'GreaterThanOrEquals', 'LessThan', 'LessThanOrEquals', 'NotContains', 'NotEquals', 'NotExists']
- **Required**: Yes

### ConditionOnValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValue]


# DocumentAttributeConditionOutput

### ConditionDocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'Exists', 'GreaterThan', 'GreaterThanOrEquals', 'LessThan', 'LessThanOrEquals', 'NotContains', 'NotEquals', 'NotExists']
- **Required**: Yes

### ConditionOnValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValueOutput]


# DocumentAttributeOutput

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValueOutput'>
- **Required**: Yes


# DocumentAttributeTarget

### TargetDocumentAttributeKey
- **Type**: typing.Optional[str]

### TargetDocumentAttributeValueDeletion
- **Type**: typing.Optional[bool]

### TargetDocumentAttributeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValue]


# DocumentAttributeTargetOutput

### TargetDocumentAttributeKey
- **Type**: typing.Optional[str]

### TargetDocumentAttributeValueDeletion
- **Type**: typing.Optional[bool]

### TargetDocumentAttributeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValueOutput]


# DocumentAttributeValue

### StringValue
- **Type**: typing.Optional[str]

### StringListValue
- **Type**: typing.Optional[typing.List[str]]

### LongValue
- **Type**: typing.Optional[int]

### DateValue
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DocumentAttributeValueCountPair

### DocumentAttributeValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValueOutput]

### Count
- **Type**: typing.Optional[int]

### FacetResults
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# DocumentAttributeValueOutput

### StringValue
- **Type**: typing.Optional[str]

### StringListValue
- **Type**: typing.Optional[typing.List[str]]

### LongValue
- **Type**: typing.Optional[int]

### DateValue
- **Type**: typing.Optional[datetime.datetime]


# DocumentInfo

### DocumentId
- **Type**: <class 'str'>
- **Required**: Yes

### Attributes
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttribute, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput]]]


# DocumentMetadataConfiguration

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['DATE_VALUE', 'LONG_VALUE', 'STRING_LIST_VALUE', 'STRING_VALUE']
- **Required**: Yes

### Relevance
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.Relevance, aws_resource_validator.pydantic_models.kendra.kendra_classes.RelevanceOutput, NoneType]

### Search
- **Type**: <class 'NoneType'>


# DocumentMetadataConfigurationOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['DATE_VALUE', 'LONG_VALUE', 'STRING_LIST_VALUE', 'STRING_VALUE']
- **Required**: Yes

### Relevance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.RelevanceOutput]

### Search
- **Type**: <class 'NoneType'>


# DocumentRelevanceConfiguration

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Relevance
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.Relevance, aws_resource_validator.pydantic_models.kendra.kendra_classes.RelevanceOutput]
- **Required**: Yes


# DocumentsMetadataConfiguration

### S3Prefix
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# EntityConfiguration

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# EntityDisplayData

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


# EntityPersonaConfiguration

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Persona
- **Type**: typing.Literal['OWNER', 'VIEWER']
- **Required**: Yes


# ExpandConfiguration

### MaxResultItemsToExpand
- **Type**: typing.Optional[int]

### MaxExpandedResultsPerItem
- **Type**: typing.Optional[int]


# ExpandedResultItem

### Id
- **Type**: typing.Optional[str]

### DocumentId
- **Type**: typing.Optional[str]

### DocumentTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.TextWithHighlights]

### DocumentExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.TextWithHighlights]

### DocumentURI
- **Type**: typing.Optional[str]

### DocumentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput]]


# ExperienceConfiguration

### ContentSourceConfiguration
- **Type**: <class 'NoneType'>

### UserIdentityConfiguration
- **Type**: <class 'NoneType'>


# ExperienceConfigurationOutput

### ContentSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ContentSourceConfigurationOutput]

### UserIdentityConfiguration
- **Type**: <class 'NoneType'>


# ExperienceEndpoint

### EndpointType
- **Type**: typing.Optional[typing.Literal['HOME']]

### Endpoint
- **Type**: typing.Optional[str]


# ExperienceEntitiesSummary

### EntityId
- **Type**: typing.Optional[str]

### EntityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### DisplayData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.EntityDisplayData]


# ExperiencesSummary

### Name
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED']]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperienceEndpoint]]


# Facet

### DocumentAttributeKey
- **Type**: typing.Optional[str]

### Facets
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### MaxResults
- **Type**: typing.Optional[int]


# FacetResult

### DocumentAttributeKey
- **Type**: typing.Optional[str]

### DocumentAttributeValueType
- **Type**: typing.Optional[typing.Literal['DATE_VALUE', 'LONG_VALUE', 'STRING_LIST_VALUE', 'STRING_VALUE']]

### DocumentAttributeValueCountPairs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeValueCountPair]]


# FailedEntity

### EntityId
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FaqStatistics

### IndexedQuestionAnswersCount
- **Type**: <class 'int'>
- **Required**: Yes


# FaqSummary

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


# FeaturedDocument

### Id
- **Type**: typing.Optional[str]


# FeaturedDocumentMissing

### Id
- **Type**: typing.Optional[str]


# FeaturedDocumentWithMetadata

### Id
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### URI
- **Type**: typing.Optional[str]


# FeaturedResultsItem

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ANSWER', 'DOCUMENT', 'QUESTION_ANSWER']]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.AdditionalResultAttribute]]

### DocumentId
- **Type**: typing.Optional[str]

### DocumentTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.TextWithHighlights]

### DocumentExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.TextWithHighlights]

### DocumentURI
- **Type**: typing.Optional[str]

### DocumentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput]]

### FeedbackToken
- **Type**: typing.Optional[str]


# FeaturedResultsSet

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedDocument]]

### LastUpdatedTimestamp
- **Type**: typing.Optional[int]

### CreationTimestamp
- **Type**: typing.Optional[int]


# FeaturedResultsSetSummary

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


# FsxConfiguration

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemType
- **Type**: typing.Literal['WINDOWS']
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration'>
- **Required**: Yes

### SecretArn
- **Type**: typing.Optional[str]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# FsxConfigurationOutput

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemType
- **Type**: typing.Literal['WINDOWS']
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput'>
- **Required**: Yes

### SecretArn
- **Type**: typing.Optional[str]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# GetQuerySuggestionsRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: <class 'str'>
- **Required**: Yes

### MaxSuggestionsCount
- **Type**: typing.Optional[int]

### SuggestionTypes
- **Type**: typing.Optional[typing.List[typing.Literal['DOCUMENT_ATTRIBUTES', 'QUERY']]]

### AttributeSuggestionsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.AttributeSuggestionsGetConfig]


# GetQuerySuggestionsResponse

### QuerySuggestionsId
- **Type**: <class 'str'>
- **Required**: Yes

### Suggestions
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Suggestion]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# GetSnapshotsRequest

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


# GetSnapshotsResponse

### SnapShotTimeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.TimeRangeOutput'>
- **Required**: Yes

### SnapshotsDataHeader
- **Type**: typing.List[str]
- **Required**: Yes

### SnapshotsData
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GitHubConfiguration

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SaaSConfiguration
- **Type**: <class 'NoneType'>

### OnPremiseConfiguration
- **Type**: <class 'NoneType'>

### Type
- **Type**: typing.Optional[typing.Literal['ON_PREMISE', 'SAAS']]

### UseChangeLog
- **Type**: typing.Optional[bool]

### GitHubDocumentCrawlProperties
- **Type**: <class 'NoneType'>

### RepositoryFilter
- **Type**: typing.Optional[typing.List[str]]

### InclusionFolderNamePatterns
- **Type**: typing.Optional[typing.List[str]]

### InclusionFileTypePatterns
- **Type**: typing.Optional[typing.List[str]]

### InclusionFileNamePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionFolderNamePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionFileTypePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionFileNamePatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]

### GitHubRepositoryConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubCommitConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubIssueDocumentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubIssueCommentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubIssueAttachmentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubPullRequestCommentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubPullRequestDocumentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubPullRequestDocumentAttachmentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# GitHubConfigurationOutput

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### SaaSConfiguration
- **Type**: <class 'NoneType'>

### OnPremiseConfiguration
- **Type**: <class 'NoneType'>

### Type
- **Type**: typing.Optional[typing.Literal['ON_PREMISE', 'SAAS']]

### UseChangeLog
- **Type**: typing.Optional[bool]

### GitHubDocumentCrawlProperties
- **Type**: <class 'NoneType'>

### RepositoryFilter
- **Type**: typing.Optional[typing.List[str]]

### InclusionFolderNamePatterns
- **Type**: typing.Optional[typing.List[str]]

### InclusionFileTypePatterns
- **Type**: typing.Optional[typing.List[str]]

### InclusionFileNamePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionFolderNamePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionFileTypePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionFileNamePatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]

### GitHubRepositoryConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubCommitConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubIssueDocumentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubIssueCommentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubIssueAttachmentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubPullRequestCommentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubPullRequestDocumentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### GitHubPullRequestDocumentAttachmentConfigurationFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# GitHubDocumentCrawlProperties

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


# GoogleDriveConfiguration

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### ExcludeMimeTypes
- **Type**: typing.Optional[typing.List[str]]

### ExcludeUserAccounts
- **Type**: typing.Optional[typing.List[str]]

### ExcludeSharedDrives
- **Type**: typing.Optional[typing.List[str]]


# GoogleDriveConfigurationOutput

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### ExcludeMimeTypes
- **Type**: typing.Optional[typing.List[str]]

### ExcludeUserAccounts
- **Type**: typing.Optional[typing.List[str]]

### ExcludeSharedDrives
- **Type**: typing.Optional[typing.List[str]]


# GroupMembers

### MemberGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.MemberGroup]]

### MemberUsers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.MemberUser]]

### S3PathforGroupMembers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path]


# GroupOrderingIdSummary

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


# GroupSummary

### GroupId
- **Type**: typing.Optional[str]

### OrderingId
- **Type**: typing.Optional[int]


# HierarchicalPrincipal

### PrincipalList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Principal]
- **Required**: Yes


# HierarchicalPrincipalOutput

### PrincipalList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Principal]
- **Required**: Yes


# Highlight

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


# HookConfiguration

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeCondition]


# HookConfigurationOutput

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeConditionOutput]


# IndexConfigurationSummary

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


# IndexStatistics

### FaqStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.FaqStatistics'>
- **Required**: Yes

### TextDocumentStatistics
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.TextDocumentStatistics'>
- **Required**: Yes


# InlineCustomDocumentEnrichmentConfiguration

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeCondition]

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeTarget]

### DocumentContentDeletion
- **Type**: typing.Optional[bool]


# InlineCustomDocumentEnrichmentConfigurationOutput

### Condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeConditionOutput]

### Target
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeTargetOutput]

### DocumentContentDeletion
- **Type**: typing.Optional[bool]


# JiraConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### CommentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### IssueFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### ProjectFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### WorkLogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]


# JiraConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### CommentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### IssueFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### ProjectFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### WorkLogFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]


# JsonTokenTypeConfiguration

### UserNameAttributeField
- **Type**: <class 'str'>
- **Required**: Yes

### GroupAttributeField
- **Type**: <class 'str'>
- **Required**: Yes


# JwtTokenTypeConfiguration

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


# ListAccessControlConfigurationsRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccessControlConfigurationsResponse

### AccessControlConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.AccessControlConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSourceSyncJobsRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.TimeRange, aws_resource_validator.pydantic_models.kendra.kendra_classes.TimeRangeOutput, NoneType]

### StatusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'INCOMPLETE', 'STOPPING', 'SUCCEEDED', 'SYNCING', 'SYNCING_INDEXING']]


# ListDataSourceSyncJobsResponse

### History
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceSyncJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDataSourcesResponse

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEntityPersonasRequest

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


# ListEntityPersonasResponse

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.PersonasSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExperienceEntitiesRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExperienceEntitiesResponse

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperienceEntitiesSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListExperiencesRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListExperiencesResponse

### SummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperiencesSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFaqsRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFaqsResponse

### FaqSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FaqSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListFeaturedResultsSetsRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListFeaturedResultsSetsResponse

### FeaturedResultsSetSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedResultsSetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsOlderThanOrderingIdRequest

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


# ListGroupsOlderThanOrderingIdResponse

### GroupsSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.GroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIndicesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListIndicesResponse

### IndexConfigurationSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.IndexConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQuerySuggestionsBlockListsRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListQuerySuggestionsBlockListsResponse

### BlockListSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.QuerySuggestionsBlockListSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# ListThesauriRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListThesauriResponse

### ThesaurusSummaryItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ThesaurusSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MemberGroup

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]


# MemberUser

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# OnPremiseConfiguration

### HostUrl
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationName
- **Type**: <class 'str'>
- **Required**: Yes

### SslCertificateS3Path
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path'>
- **Required**: Yes


# OneDriveConfiguration

### TenantDomain
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### OneDriveUsers
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.OneDriveUsers'>
- **Required**: Yes

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### DisableLocalGroups
- **Type**: typing.Optional[bool]


# OneDriveConfigurationOutput

### TenantDomain
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### OneDriveUsers
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.OneDriveUsersOutput'>
- **Required**: Yes

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### DisableLocalGroups
- **Type**: typing.Optional[bool]


# OneDriveUsers

### OneDriveUserList
- **Type**: typing.Optional[typing.List[str]]

### OneDriveUserS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path]


# OneDriveUsersOutput

### OneDriveUserList
- **Type**: typing.Optional[typing.List[str]]

### OneDriveUserS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path]


# PersonasSummary

### EntityId
- **Type**: typing.Optional[str]

### Persona
- **Type**: typing.Optional[typing.Literal['OWNER', 'VIEWER']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### UpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# Principal

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


# ProxyConfiguration

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes

### Credentials
- **Type**: typing.Optional[str]


# PutPrincipalMappingRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupMembers
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.GroupMembers'>
- **Required**: Yes

### DataSourceId
- **Type**: typing.Optional[str]

### OrderingId
- **Type**: typing.Optional[int]

### RoleArn
- **Type**: typing.Optional[str]


# QueryRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: typing.Optional[str]

### AttributeFilter
- **Type**: <class 'NoneType'>

### Facets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Facet]]

### RequestedDocumentAttributes
- **Type**: typing.Optional[typing.List[str]]

### QueryResultTypeFilter
- **Type**: typing.Optional[typing.Literal['ANSWER', 'DOCUMENT', 'QUESTION_ANSWER']]

### DocumentRelevanceOverrideConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentRelevanceConfiguration]]

### PageNumber
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### SortingConfiguration
- **Type**: <class 'NoneType'>

### SortingConfigurations
- **Type**: typing.Optional[typing.List[NoneType]]

### UserContext
- **Type**: <class 'NoneType'>

### VisitorId
- **Type**: typing.Optional[str]

### SpellCorrectionConfiguration
- **Type**: <class 'NoneType'>

### CollapseConfiguration
- **Type**: <class 'NoneType'>


# QueryResult

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.QueryResultItem]
- **Required**: Yes

### FacetResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FacetResult]
- **Required**: Yes

### TotalNumberOfResults
- **Type**: <class 'int'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Warning]
- **Required**: Yes

### SpellCorrectedQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SpellCorrectedQuery]
- **Required**: Yes

### FeaturedResultsItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedResultsItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# QueryResultItem

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['ANSWER', 'DOCUMENT', 'QUESTION_ANSWER']]

### Format
- **Type**: typing.Optional[typing.Literal['TABLE', 'TEXT']]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.AdditionalResultAttribute]]

### DocumentId
- **Type**: typing.Optional[str]

### DocumentTitle
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.TextWithHighlights]

### DocumentExcerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.TextWithHighlights]

### DocumentURI
- **Type**: typing.Optional[str]

### DocumentAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput]]

### ScoreAttributes
- **Type**: <class 'NoneType'>

### FeedbackToken
- **Type**: typing.Optional[str]

### TableExcerpt
- **Type**: <class 'NoneType'>

### CollapsedResultDetail
- **Type**: <class 'NoneType'>


# QuerySuggestionsBlockListSummary

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


# QuipConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### MessageFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]


# QuipConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### MessageFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### AttachmentFieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### InclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### ExclusionPatterns
- **Type**: typing.Optional[typing.List[str]]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]


# Relevance

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


# RelevanceFeedback

### ResultId
- **Type**: <class 'str'>
- **Required**: Yes

### RelevanceValue
- **Type**: typing.Literal['NOT_RELEVANT', 'RELEVANT']
- **Required**: Yes


# RelevanceOutput

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


# RetrieveRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryText
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeFilter
- **Type**: <class 'NoneType'>

### RequestedDocumentAttributes
- **Type**: typing.Optional[typing.List[str]]

### DocumentRelevanceOverrideConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentRelevanceConfiguration]]

### PageNumber
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### UserContext
- **Type**: <class 'NoneType'>


# RetrieveResult

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResultItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.RetrieveResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# RetrieveResultItem

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput]]

### ScoreAttributes
- **Type**: <class 'NoneType'>


# S3DataSourceConfiguration

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
- **Type**: <class 'NoneType'>

### AccessControlListConfiguration
- **Type**: <class 'NoneType'>


# S3DataSourceConfigurationOutput

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
- **Type**: <class 'NoneType'>

### AccessControlListConfiguration
- **Type**: <class 'NoneType'>


# S3Path

### Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### Key
- **Type**: <class 'str'>
- **Required**: Yes


# SaaSConfiguration

### OrganizationName
- **Type**: <class 'str'>
- **Required**: Yes

### HostUrl
- **Type**: <class 'str'>
- **Required**: Yes


# SalesforceChatterFeedConfiguration

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### IncludeFilterTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE_USER', 'STANDARD_USER']]]


# SalesforceChatterFeedConfigurationOutput

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### IncludeFilterTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE_USER', 'STANDARD_USER']]]


# SalesforceConfiguration

### ServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardObjectConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceStandardObjectConfiguration]]

### KnowledgeArticleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceKnowledgeArticleConfiguration]

### ChatterFeedConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceChatterFeedConfiguration]

### CrawlAttachments
- **Type**: typing.Optional[bool]

### StandardObjectAttachmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceStandardObjectAttachmentConfiguration]

### IncludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExcludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]


# SalesforceConfigurationOutput

### ServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### StandardObjectConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceStandardObjectConfigurationOutput]]

### KnowledgeArticleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceKnowledgeArticleConfigurationOutput]

### ChatterFeedConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceChatterFeedConfigurationOutput]

### CrawlAttachments
- **Type**: typing.Optional[bool]

### StandardObjectAttachmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceStandardObjectAttachmentConfigurationOutput]

### IncludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]

### ExcludeAttachmentFilePatterns
- **Type**: typing.Optional[typing.List[str]]


# SalesforceCustomKnowledgeArticleTypeConfiguration

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SalesforceCustomKnowledgeArticleTypeConfigurationOutput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SalesforceKnowledgeArticleConfiguration

### IncludedStates
- **Type**: typing.List[typing.Literal['ARCHIVED', 'DRAFT', 'PUBLISHED']]
- **Required**: Yes

### StandardKnowledgeArticleTypeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceStandardKnowledgeArticleTypeConfiguration]

### CustomKnowledgeArticleTypeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceCustomKnowledgeArticleTypeConfiguration]]


# SalesforceKnowledgeArticleConfigurationOutput

### IncludedStates
- **Type**: typing.List[typing.Literal['ARCHIVED', 'DRAFT', 'PUBLISHED']]
- **Required**: Yes

### StandardKnowledgeArticleTypeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceStandardKnowledgeArticleTypeConfigurationOutput]

### CustomKnowledgeArticleTypeConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SalesforceCustomKnowledgeArticleTypeConfigurationOutput]]


# SalesforceStandardKnowledgeArticleTypeConfiguration

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SalesforceStandardKnowledgeArticleTypeConfigurationOutput

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SalesforceStandardObjectAttachmentConfiguration

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SalesforceStandardObjectAttachmentConfigurationOutput

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SalesforceStandardObjectConfiguration

### Name
- **Type**: typing.Literal['ACCOUNT', 'CAMPAIGN', 'CASE', 'CONTACT', 'CONTRACT', 'DOCUMENT', 'GROUP', 'IDEA', 'LEAD', 'OPPORTUNITY', 'PARTNER', 'PRICEBOOK', 'PRODUCT', 'PROFILE', 'SOLUTION', 'TASK', 'USER']
- **Required**: Yes

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SalesforceStandardObjectConfigurationOutput

### Name
- **Type**: typing.Literal['ACCOUNT', 'CAMPAIGN', 'CASE', 'CONTACT', 'CONTRACT', 'DOCUMENT', 'GROUP', 'IDEA', 'LEAD', 'OPPORTUNITY', 'PARTNER', 'PRICEBOOK', 'PRODUCT', 'PROFILE', 'SOLUTION', 'TASK', 'USER']
- **Required**: Yes

### DocumentDataFieldName
- **Type**: <class 'str'>
- **Required**: Yes

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# ScoreAttributes

### ScoreConfidence
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NOT_AVAILABLE', 'VERY_HIGH']]


# Search

### Facetable
- **Type**: typing.Optional[bool]

### Searchable
- **Type**: typing.Optional[bool]

### Displayable
- **Type**: typing.Optional[bool]

### Sortable
- **Type**: typing.Optional[bool]


# SeedUrlConfiguration

### SeedUrls
- **Type**: typing.List[str]
- **Required**: Yes

### WebCrawlerMode
- **Type**: typing.Optional[typing.Literal['EVERYTHING', 'HOST_ONLY', 'SUBDOMAINS']]


# SeedUrlConfigurationOutput

### SeedUrls
- **Type**: typing.List[str]
- **Required**: Yes

### WebCrawlerMode
- **Type**: typing.Optional[typing.Literal['EVERYTHING', 'HOST_ONLY', 'SUBDOMAINS']]


# ServerSideEncryptionConfiguration

### KmsKeyId
- **Type**: typing.Optional[str]


# ServiceNowConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ServiceNowKnowledgeArticleConfiguration]

### ServiceCatalogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ServiceNowServiceCatalogConfiguration]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'OAUTH2']]


# ServiceNowConfigurationOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ServiceNowKnowledgeArticleConfigurationOutput]

### ServiceCatalogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.ServiceNowServiceCatalogConfigurationOutput]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'OAUTH2']]


# ServiceNowKnowledgeArticleConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### FilterQuery
- **Type**: typing.Optional[str]


# ServiceNowKnowledgeArticleConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### FilterQuery
- **Type**: typing.Optional[str]


# ServiceNowServiceCatalogConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# ServiceNowServiceCatalogConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SharePointConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### DisableLocalGroups
- **Type**: typing.Optional[bool]

### SslCertificateS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'OAUTH2']]

### ProxyConfiguration
- **Type**: <class 'NoneType'>


# SharePointConfigurationOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]

### FieldMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]

### DocumentTitleFieldName
- **Type**: typing.Optional[str]

### DisableLocalGroups
- **Type**: typing.Optional[bool]

### SslCertificateS3Path
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['HTTP_BASIC', 'OAUTH2']]

### ProxyConfiguration
- **Type**: <class 'NoneType'>


# SiteMapsConfiguration

### SiteMaps
- **Type**: typing.List[str]
- **Required**: Yes


# SiteMapsConfigurationOutput

### SiteMaps
- **Type**: typing.List[str]
- **Required**: Yes


# SlackConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SlackConfigurationOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# SortingConfiguration

### DocumentAttributeKey
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Literal['ASC', 'DESC']
- **Required**: Yes


# SourceDocument

### DocumentId
- **Type**: typing.Optional[str]

### SuggestionAttributes
- **Type**: typing.Optional[typing.List[str]]

### AdditionalAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentAttributeOutput]]


# SpellCorrectedQuery

### SuggestedQueryText
- **Type**: typing.Optional[str]

### Corrections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Correction]]


# SpellCorrectionConfiguration

### IncludeQuerySpellCheckSuggestions
- **Type**: <class 'bool'>
- **Required**: Yes


# SqlConfiguration

### QueryIdentifiersEnclosingOption
- **Type**: typing.Optional[typing.Literal['DOUBLE_QUOTES', 'NONE']]


# StartDataSourceSyncJobRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# StartDataSourceSyncJobResponse

### ExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# Status

### DocumentId
- **Type**: typing.Optional[str]

### DocumentStatus
- **Type**: typing.Optional[typing.Literal['FAILED', 'INDEXED', 'NOT_FOUND', 'PROCESSING', 'UPDATED', 'UPDATE_FAILED']]

### FailureCode
- **Type**: typing.Optional[str]

### FailureReason
- **Type**: typing.Optional[str]


# StopDataSourceSyncJobRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes


# SubmitFeedbackRequest

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### ClickFeedbackItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.ClickFeedback]]

### RelevanceFeedbackItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.RelevanceFeedback]]


# SuggestableConfig

### AttributeName
- **Type**: typing.Optional[str]

### Suggestable
- **Type**: typing.Optional[bool]


# Suggestion

### Id
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SuggestionValue]

### SourceDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SourceDocument]]


# SuggestionHighlight

### BeginOffset
- **Type**: typing.Optional[int]

### EndOffset
- **Type**: typing.Optional[int]


# SuggestionTextWithHighlights

### Text
- **Type**: typing.Optional[str]

### Highlights
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.SuggestionHighlight]]


# SuggestionValue

### Text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SuggestionTextWithHighlights]


# TableCell

### Value
- **Type**: typing.Optional[str]

### TopAnswer
- **Type**: typing.Optional[bool]

### Highlighted
- **Type**: typing.Optional[bool]

### Header
- **Type**: typing.Optional[bool]


# TableExcerpt

### Rows
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.TableRow]]

### TotalNumberOfRows
- **Type**: typing.Optional[int]


# TableRow

### Cells
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.TableCell]]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Tag]
- **Required**: Yes


# TemplateConfiguration

### Template
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TemplateConfigurationOutput

### Template
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# TextDocumentStatistics

### IndexedTextDocumentsCount
- **Type**: <class 'int'>
- **Required**: Yes

### IndexedTextBytes
- **Type**: <class 'int'>
- **Required**: Yes


# TextWithHighlights

### Text
- **Type**: typing.Optional[str]

### Highlights
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Highlight]]


# ThesaurusSummary

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


# TimeRange

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TimeRangeOutput

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccessControlConfigurationRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.Principal]]

### HierarchicalAccessControlList
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.HierarchicalPrincipal, aws_resource_validator.pydantic_models.kendra.kendra_classes.HierarchicalPrincipalOutput]]]


# UpdateDataSourceRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IndexId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceConfigurationOutput, NoneType]

### VpcConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceVpcConfigurationOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### Schedule
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### LanguageCode
- **Type**: typing.Optional[str]

### CustomDocumentEnrichmentConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.CustomDocumentEnrichmentConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.CustomDocumentEnrichmentConfigurationOutput, NoneType]


# UpdateExperienceRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperienceConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.ExperienceConfigurationOutput, NoneType]

### Description
- **Type**: typing.Optional[str]


# UpdateFeaturedResultsSetRequest

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
- **Type**: typing.Optional[typing.List[str]]

### FeaturedDocuments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedDocument]]


# UpdateFeaturedResultsSetResponse

### FeaturedResultsSet
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.FeaturedResultsSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIndexRequest

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentMetadataConfiguration, aws_resource_validator.pydantic_models.kendra.kendra_classes.DocumentMetadataConfigurationOutput]]]

### CapacityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.CapacityUnitsConfiguration]

### UserTokenConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.UserTokenConfiguration]]

### UserContextPolicy
- **Type**: typing.Optional[typing.Literal['ATTRIBUTE_FILTER', 'USER_TOKEN']]

### UserGroupResolutionConfiguration
- **Type**: <class 'NoneType'>


# UpdateQuerySuggestionsBlockListRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path]

### RoleArn
- **Type**: typing.Optional[str]


# UpdateQuerySuggestionsConfigRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.AttributeSuggestionsUpdateConfig]


# UpdateThesaurusRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.S3Path]


# Urls

### SeedUrlConfiguration
- **Type**: <class 'NoneType'>

### SiteMapsConfiguration
- **Type**: <class 'NoneType'>


# UrlsOutput

### SeedUrlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SeedUrlConfigurationOutput]

### SiteMapsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.SiteMapsConfigurationOutput]


# UserContext

### Token
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Groups
- **Type**: typing.Optional[typing.List[str]]

### DataSourceGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceGroup]]


# UserGroupResolutionConfiguration

### UserGroupResolutionMode
- **Type**: typing.Literal['AWS_SSO', 'NONE']
- **Required**: Yes


# UserIdentityConfiguration

### IdentityAttributeName
- **Type**: typing.Optional[str]


# UserTokenConfiguration

### JwtTokenTypeConfiguration
- **Type**: <class 'NoneType'>

### JsonTokenTypeConfiguration
- **Type**: <class 'NoneType'>


# Warning

### Message
- **Type**: typing.Optional[str]

### Code
- **Type**: typing.Optional[typing.Literal['QUERY_LANGUAGE_INVALID_SYNTAX']]


# WebCrawlerConfiguration

### Urls
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.Urls'>
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
- **Type**: <class 'NoneType'>

### AuthenticationConfiguration
- **Type**: <class 'NoneType'>


# WebCrawlerConfigurationOutput

### Urls
- **Type**: <class 'aws_resource_validator.pydantic_models.kendra.kendra_classes.UrlsOutput'>
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
- **Type**: <class 'NoneType'>

### AuthenticationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kendra.kendra_classes.AuthenticationConfigurationOutput]


# WorkDocsConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]


# WorkDocsConfigurationOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kendra.kendra_classes.DataSourceToIndexFieldMapping]]



# Kendra Service

### AccessControlConfigurationId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9-]+`
- **Min Length**: 1
- **Max Length**: 36

### AccessControlConfigurationName
- **Type**: string
- **Pattern**: `[\S\s]*`
- **Min Length**: 1
- **Max Length**: 200

### ClaimRegex
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 100

### ColumnName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 100

### ConfluenceSpaceIdentifier
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 255

### DataSourceDateFieldFormat
- **Type**: string
- **Pattern**: `^(?!\s).*(?<!\s)$`
- **Min Length**: 4
- **Max Length**: 40

### DataSourceFieldName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_.]*$`
- **Min Length**: 1
- **Max Length**: 100

### DataSourceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 100

### DataSourceName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### DataSourceSyncJobId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 100

### DatabaseName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 100

### Description
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 0
- **Max Length**: 1000

### DocumentAttributeKey
- **Type**: string
- **Pattern**: `[a-zA-Z0-9_][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 200

### Domain
- **Type**: string
- **Pattern**: `^(?!-)[A-Za-z0-9-].*(?<!-)$`
- **Min Length**: 1
- **Max Length**: 63

### Duration
- **Type**: string
- **Pattern**: `[0-9]+[s]`
- **Min Length**: 1
- **Max Length**: 10

### Endpoint
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 2048

### EnterpriseId
- **Type**: string
- **Pattern**: `^[A-Z0-9]*$`
- **Min Length**: 1
- **Max Length**: 64

### EntityId
- **Type**: string
- **Pattern**: `^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$`
- **Min Length**: 1
- **Max Length**: 47

### ErrorMessage
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 2048

### ExperienceId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 36

### ExperienceName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### FailureReason
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 2048

### FaqId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 100

### FaqName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 100

### FeaturedResultsSetDescription
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 0
- **Max Length**: 1000

### FeaturedResultsSetId
- **Type**: string
- **Pattern**: `^[a-zA-Z-0-9]*`
- **Min Length**: 36
- **Max Length**: 36

### FeaturedResultsSetName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][ a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### FeedbackToken
- **Type**: string
- **Pattern**: `^\P{C}*.\P{C}*$`
- **Min Length**: 1
- **Max Length**: 2048

### FileSystemId
- **Type**: string
- **Pattern**: `^(fs-[0-9a-f]{8,})$`
- **Min Length**: 11
- **Max Length**: 21

### GroupAttributeField
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 100

### GroupId
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 1024

### Host
- **Type**: string
- **Pattern**: `([^\s]*)`
- **Min Length**: 1
- **Max Length**: 253

### IdentityAttributeName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### IndexFieldName
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 30

### IndexId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]*`
- **Min Length**: 36
- **Max Length**: 36

### IndexName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 1000

### Issuer
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 65

### JiraAccountUrl
- **Type**: string
- **Pattern**: `^https:\/\/[a-zA-Z0-9_\-\.]+(\.atlassian\.net\/)$`
- **Min Length**: 1
- **Max Length**: 2048

### LambdaArn
- **Type**: string
- **Pattern**: `/arn:aws[a-zA-Z-]*:lambda:[a-z]+-[a-z]+-[0-9]:[0-9]{12}:function:[a-zA-Z0-9-_]+(\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?(:[a-zA-Z0-9-_]+)?/`
- **Min Length**: 1
- **Max Length**: 2048

### LanguageCode
- **Type**: string
- **Pattern**: `[a-zA-Z-]*`
- **Min Length**: 2
- **Max Length**: 10

### MetricValue
- **Type**: string
- **Pattern**: `(([1-9][0-9]*)|0)`

### MimeType
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 256

### NameType
- **Type**: string
- **Pattern**: `^[\S\s]*$`
- **Min Length**: 1
- **Max Length**: 100

### OneDriveUser
- **Type**: string
- **Pattern**: `^(?!\s).+@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$`
- **Min Length**: 1
- **Max Length**: 256

### OrganizationId
- **Type**: string
- **Pattern**: `d-[0-9a-fA-F]{10}`
- **Min Length**: 12
- **Max Length**: 12

### OrganizationName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 60

### PrincipalName
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 200

### QueryId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]*`
- **Min Length**: 1
- **Max Length**: 36

### QuerySuggestionsBlockListId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9-]*`
- **Min Length**: 36
- **Max Length**: 36

### QuerySuggestionsBlockListName
- **Type**: string
- **Pattern**: `^[a-zA-Z0-9](-*[a-zA-Z0-9])*`
- **Min Length**: 1
- **Max Length**: 100

### RepositoryName
- **Type**: string
- **Pattern**: `^[A-Za-z0-9_.-]+$`
- **Min Length**: 1
- **Max Length**: 64

### RoleArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 0
- **Max Length**: 1284

### S3BucketName
- **Type**: string
- **Pattern**: `[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]`
- **Min Length**: 3
- **Max Length**: 63

### SalesforceCustomKnowledgeArticleTypeName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 100

### SecretArn
- **Type**: string
- **Pattern**: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`
- **Min Length**: 1
- **Max Length**: 1284

### SeedUrl
- **Type**: string
- **Pattern**: `^(https?):\/\/([^\s]*)`
- **Min Length**: 1
- **Max Length**: 2048

### ServiceNowHostUrl
- **Type**: string
- **Pattern**: `^(?!(^(https?|ftp|file):\/\/))[a-z0-9-]+(\.service-now\.com)$`
- **Min Length**: 1
- **Max Length**: 2048

### ServiceNowKnowledgeArticleFilterQuery
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 2048

### SharedDriveId
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 256

### SinceCrawlDate
- **Type**: string
- **Pattern**: `(20\d{2})-(0?[1-9]|1[0-2])-(0?[1-9]|1\d|2\d|3[01])`
- **Min Length**: 10
- **Max Length**: 10

### SiteId
- **Type**: string
- **Pattern**: `^[A-Za-z0-9-]+$`
- **Min Length**: 1
- **Max Length**: 128

### SiteMap
- **Type**: string
- **Pattern**: `^(https?):\/\/([^\s]*)`
- **Min Length**: 1
- **Max Length**: 2048

### SiteUrl
- **Type**: string
- **Pattern**: `^https:\/\/[a-zA-Z0-9_\-\.]+$`
- **Min Length**: 1
- **Max Length**: 2048

### SubnetId
- **Type**: string
- **Pattern**: `[\-0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 200

### SuggestionQueryText
- **Type**: string
- **Pattern**: `^\P{C}*$`

### TableName
- **Type**: string
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`
- **Min Length**: 1
- **Max Length**: 100

### TeamId
- **Type**: string
- **Pattern**: `[A-Z0-9]*`
- **Min Length**: 1
- **Max Length**: 64

### TenantDomain
- **Type**: string
- **Pattern**: `^([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-z]{2,}$`
- **Min Length**: 1
- **Max Length**: 256

### ThesaurusId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 100

### ThesaurusName
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 100

### Token
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 100000

### Url
- **Type**: string
- **Pattern**: `^(https?|ftp|file):\/\/([^\s]*)`
- **Min Length**: 1
- **Max Length**: 2048

### UserAccount
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 256

### UserId
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 1024

### UserNameAttributeField
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 100

### VisitorId
- **Type**: string
- **Pattern**: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
- **Min Length**: 1
- **Max Length**: 256

### VpcSecurityGroupId
- **Type**: string
- **Pattern**: `[-0-9a-zA-Z]+`
- **Min Length**: 1
- **Max Length**: 200

### WarningMessage
- **Type**: string
- **Pattern**: `^\P{C}*$`
- **Min Length**: 1
- **Max Length**: 2048

